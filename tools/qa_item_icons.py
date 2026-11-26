#!/usr/bin/env python3
"""Static, semantic and optional browser QA for player-facing item art.

Run:
    python tools/qa_item_icons.py
    python tools/qa_item_icons.py --browser
Uses only standard library for static QA. Browser mode requires Playwright and
Microsoft Edge. No network or game assets are used.
"""
import argparse
from collections import Counter
import html
import json
from pathlib import Path
import re
import subprocess
import sys
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
EVENTS=ROOT/"docs"/"events"
SVG=ROOT/"docs"/"assets"/"item-icons"
MANIFEST=ROOT/"tools"/"item_icon_map.json"
QA=ROOT.parent.parent/"05_HANDBOOK"/"qa"
TAG=re.compile(r'<img class="item-illustration"[^>]*>')
TABLE_TAG=re.compile(r'<img class="table-item-icon"[^>]*>')
CARD=re.compile(r'<div class="item-card">(?P<image><img[^>]*>)?<div><strong>(?P<name>.*?)</strong>',re.S)
ATTR=re.compile(r'([a-zA-Z][\w-]*)="([^"]*)"')
def attrs(raw):
    return dict(ATTR.findall(raw or ""))
def fail(msg):
    raise AssertionError(msg)
def static():
    source=json.loads(MANIFEST.read_text(encoding="utf8"))
    pages=source["pages"]
    assert source["kind"]=="original-illustration"
    assert len(pages)==61,len(pages)
    assert len(list(EVENTS.glob("[0-9][0-9].html")))==61
    names=Counter()
    total=0
    refs=set()
    for name,expected in sorted(pages.items()):
        path=EVENTS/(name+".html")
        raw=path.read_text(encoding="utf8")
        cards=list(CARD.finditer(raw))
        assert len(cards)==len(expected),(name,len(cards),len(expected))
        for j,(card,item) in enumerate(zip(cards,expected)):
            label=html.unescape(card.group("name")).strip()
            if label!=item["name"]:fail(f"{name}:{j} card name drift {label!r}")
            img=card.group("image")
            if not img:fail(f"{name}:{j} no item illustration")
            a=attrs(img)
            expected_src=f'../assets/item-icons/{item["icon"]}.svg'
            if a.get("src")!=expected_src:fail(f"{name}:{j} wrong path {a.get('src')}")
            if a.get("data-item-key")!=item["key"]:fail(f"{name}:{j} wrong ID")
            if a.get("alt")!="" or a.get("aria-hidden")!="true":fail(f"{name}:{j} redundant non-decorative alt")
            if not (SVG/(item["icon"]+".svg")).is_file():fail(f"{name}:{j} missing asset")
            refs.add(item["icon"])
            names[label]+=1
        total+=len(cards)
        # Invariant: content is unchanged relative to the checkout HEAD,
        # except for the intentionally inserted decorative SVG img elements.
        old=subprocess.run(["git","show",f"HEAD:docs/events/{name}.html"],cwd=ROOT,
                           capture_output=True,text=True,encoding="utf8",check=True).stdout
        if TABLE_TAG.sub("",TAG.sub("",raw)).replace("\r\n","\n")!=TABLE_TAG.sub("",TAG.sub("",old)).replace("\r\n","\n"):
            fail(f"{name}: article content differs from HEAD beyond icon markup")
    assert total==575,(total,575)
    js=(ROOT/"docs/assets/app.js").read_text(encoding="utf8")
    if "const iconRules" in js or "card.prepend(symbol)" in js:
        fail("Legacy inaccurate emoji injection still active")
    allsvg=list(SVG.glob("*.svg"))
    for path in allsvg:
        tree=ET.parse(path)
        root=tree.getroot()
        if root.tag!="{http://www.w3.org/2000/svg}svg" or root.get("viewBox")!="0 0 64 64":
            fail(f"{path.name}: malformed/viewBox changed")
        raw=path.read_text(encoding="utf8")
        if "CC0-1.0" not in raw or re.search(r'<(?:script|image)\b|(?:xlink:)?href\s*=',raw,re.I):
            fail(f"{path.name}: unlicensed or external content")
    required=[
        ("01","Mãng cầu","mang-cau"),("01","Dừa","dua"),
        ("01","Đu đủ","du-du"),("01","Xoài","xoai"),("01","Sung","sung"),
        ("01","Bánh chưng Thập cẩm","banh-chung-mixed"),
        ("01","Bánh tét nhân đậu","banh-tet-bean"),
        ("01","Bánh tét thập cẩm","banh-tet-mixed"),
    ]
    for pid,label,pic in required:
        entries=[r for r in pages[pid] if r["name"]==label]
        assert entries and entries[0]["icon"]==pic,(pid,label,entries)
    assert all(r["icon"]=="mineral" for group in pages.values() for r in group if r["name"]=="Huyền Tinh Khoáng Thạch")
    assert all(r["icon"]=="book" for group in pages.values() for r in group if r["name"]=="Võ Lâm Mật Tịch")
    # An Bang and Dinh Quoc must use equipment *slot*, not crystal/coin catchalls.
    equip=[r for group in pages.values() for r in group if r["name"].startswith(("An Bang ","Định Quốc "))]
    assert equip and {r["icon"] for r in equip}>={
        "ring-amber","ring-ruby","necklace","pendant-amber","armor",
        "hat","boots","bracer","belt"},Counter(x["icon"] for x in equip)
    print(f"STATIC PASS: {len(pages)} event pages, {total} illustrated cards, "
          f"{len(names)} labels, {len({r['key'] for group in pages.values() for r in group})} "
          f"source IDs, {len(refs)} used SVGs / {len(allsvg)} valid assets. "
          f"Article text unchanged.")
def browser():
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        raise RuntimeError("Browser QA needs playwright") from exc
    QA.mkdir(parents=True,exist_ok=True)
    with sync_playwright() as pw:
        b=pw.chromium.launch(headless=True,executable_path=r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
        try:
            for mode,size in [("desktop",{"width":1440,"height":900}),
                              ("mobile",{"width":390,"height":844})]:
                context=b.new_context(viewport=size,device_scale_factor=1)
                page=context.new_page()
                page.goto((ROOT/"docs/index.html").resolve().as_uri(),wait_until="load")
                page.locator("#search").fill("mam ngu qua")
                matches=page.locator("#event-grid .event-card:visible").count()
                if not matches: fail(f"BROWSER {mode}: Vietnamese accent-insensitive search failed")
                page.locator("#theme").click()
                if page.evaluate("document.documentElement.dataset.theme")!="dark":
                    fail(f"BROWSER {mode}: theme toggle failed")
                for pid in ("01","02","20","35","48","59"):
                    page.goto((EVENTS/(pid+".html")).resolve().as_uri(),wait_until="load")
                    page.locator("#vat-pham").scroll_into_view_if_needed()
                    # Browser image loading is lazy: exercise each row at its
                    # real scroll position, especially on mobile viewports.
                    for image in page.locator("#vat-pham .item-card img.item-illustration").all():
                        image.scroll_into_view_if_needed()
                        image.evaluate("(x) => x.decode()")
                    result=page.locator("#vat-pham .item-card img.item-illustration").evaluate_all(
                        "(xs) => xs.map(x=>({src:x.getAttribute('src'),loaded:x.complete && x.naturalWidth>0,actual:x.getBoundingClientRect().width}))"
                    )
                    if not result or any(not x["loaded"] or x["actual"]<25 for x in result):
                        fail(f"BROWSER {mode} #{pid}: broken/small art {result}")
                    if page.evaluate("document.documentElement.scrollWidth > window.innerWidth+1"):
                        fail(f"BROWSER {mode} #{pid}: horizontal overflow")
                    if pid in ("01","02","35","48","59"):
                        page.locator("#vat-pham").screenshot(path=str(QA/(f"item_icons_{mode}_{pid}.png")))
                context.close()
                print(f"BROWSER {mode}: 6 representative pages, image loads/width/overflow PASS.")
        finally:
            b.close()
    print(f"Screenshots: {QA}")
if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--browser",action="store_true")
    opts=parser.parse_args()
    static()
    if opts.browser: browser()
