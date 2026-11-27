#!/usr/bin/env python3
"""Regression QA: deterministic table artwork plus optional real-browser review.

python tools/qa_table_icons.py
python tools/qa_table_icons.py --browser
"""
import argparse
from collections import Counter
import json
from pathlib import Path
import re
import subprocess
import xml.etree.ElementTree as ET

from table_item_icons import (
    ASSETS, MAP, PAGES, TABLE, ROW, CELL, HEADER, IMG, digest, stripped,
    render, HEADER_ITEMS,
)
ROOT=Path(__file__).resolve().parents[1]
QA=ROOT.parent.parent/"05_HANDBOOK"/"qa"
ATTR=re.compile(r'([\w-]+)="([^"]*)"')

def verify(compare_head=False):
    data=json.loads(MAP.read_text(encoding="utf8"))
    assert data["schema"]==1
    assert set(data["pages"])=={p.stem for p in PAGES.glob("[0-9][0-9].html")}
    stats=Counter()
    allfiles={p.stem:p for p in ASSETS.glob("*.svg")}
    for path in allfiles.values():
        element=ET.parse(path).getroot()
        assert element.tag.endswith("}svg") and element.get("viewBox")=="0 0 64 64",path
        assert "CC0-1.0" in path.read_text(encoding="utf8"),path
    for pid,plans in data["pages"].items():
        html=(PAGES/(pid+".html")).read_text(encoding="utf8")
        if compare_head:
            before=subprocess.run(
                ["git","show",f"HEAD:docs/events/{pid}.html"],cwd=ROOT,
                encoding="utf8",capture_output=True,check=True).stdout
            if IMG.sub("",html).replace("\r\n","\n")!=IMG.sub("",before).replace("\r\n","\n"):
                raise AssertionError(f"{pid}: article content changed beyond SVG insertions")
        tables=list(TABLE.finditer(html))
        planned={(p["table"],p["row"],p["col"]):p for p in plans}
        assert len(planned)==len(plans),(pid,"duplicate annotation address")
        reached=set()
        for ti,tab in enumerate(tables):
            stats["tables"]+=1
            row=0
            for tr in ROW.finditer(tab.group(0)):
                ths=list(HEADER.finditer(tr.group(0)))
                tds=list(CELL.finditer(tr.group(0)))
                if ths and not tds:
                    for col,c in enumerate(ths):
                        address=(ti,-1,col)
                        expected=planned.get(address)
                        check_cell(pid,address,c,expected,allfiles)
                        if expected:reached.add(address);stats["header_mentions"]+=len(expected["matches"])
                    continue
                if tds:
                    stats["rows"]+=1
                    for col,c in enumerate(tds):
                        address=(ti,row,col)
                        expected=planned.get(address)
                        check_cell(pid,address,c,expected,allfiles)
                        if expected:reached.add(address);stats["cells_decorated"]+=1;stats["mentions"]+=len(expected["matches"])
                        stats["cells"]+=1
                    row+=1
        assert reached==set(planned),(pid,"unvisited",set(planned)-reached)
    assert stats["header_mentions"]==8,stats
    assert stats["mentions"]>800,stats
    assert stats["cells_decorated"]>700,stats
    # Strong positive/negative assertions for the exact bug classes raised
    # in the owner screenshots and the independent semantic audit.
    checks=[
       ("01",0,1,0,"dua"),
       ("02",0,1,0,"paper-blue"),
       ("02",1,3,1,"paper-red"),
       ("02",2,3,1,"lantern-round-special"),
       ("04",1,2,3,"ingredient-sack"),
       ("05",1,1,0,"snowman-purple"),
       ("06",0,5,0,"chicken-meat"),
       ("06",0,6,0,"pork-meat"),
       ("13",2,2,0,"candle"),
       ("16",0,1,0,"gift-box-blue"),
       ("19",0,0,0,"mooncake-special"),
       ("20",0,-1,3,"letter-tile-3"),
       ("20",1,1,0,"letter-tile-3"),
       ("25",1,0,0,"flower"),
       ("30",2,6,1,"book"),
       ("38",0,0,1,"stocking"),
       ("41",0,0,0,"bucket-hat"),
       ("58",0,0,1,"soft-hat-soldier"),
       ("59",0,0,1,"element-wood"),
    ]
    for pid,table,row,col,icon in checks:
        record=next((x for x in data["pages"][pid] if (x["table"],x["row"],x["col"])==(table,row,col)),None)
        if not record or icon not in {m["icon"] for m in record["matches"]}:
            raise AssertionError((pid,table,row,col,icon,record))
    # No icon on word homographs, NPC/map coordinate tables, ordinary number
    # columns, or arbitrary 3/EXP values.
    assert data["pages"]["50"]==[], "NPC Phúc/Lộc/Thọ are not collectible tiles"
    assert data["pages"]["42"],"Sapling family is explicitly scoped"
    assert not any(x["table"]==0 and x["col"]==2 for x in data["pages"]["11"]), "nhận != nhẫn"
    assert not any(m["text"].casefold()=="trúng" for group in data["pages"].values() for x in group for m in x["matches"]), "trúng != trứng"
    print("TABLE STATIC PASS:",dict(stats),"pages="+str(len(data["pages"])),"SVGs="+str(len(allfiles)))

def check_cell(pid,address,c,expected,icons):
    inside=c.group("inner")
    original=stripped(inside)
    marks=list(IMG.finditer(inside))
    if expected is None:
        assert not marks,(pid,address,"unexpected image")
        return
    assert digest(original)==expected["sha256"],(pid,address,"underlying cell changed")
    assert inside==render(original,expected["matches"]),(pid,address,"icon injection mismatch")
    assert len(marks)==len(expected["matches"]),(pid,address,"missing icon")
    for image,plan in zip(marks,expected["matches"]):
        data=dict(ATTR.findall(image.group(0)))
        assert data.get("src")==f'../assets/item-icons/{plan["icon"]}.svg',(pid,address,"src",data)
        assert data.get("alt")=="" and data.get("aria-hidden")=="true"
        assert data.get("loading")=="lazy"
        if plan["key"]:assert data.get("data-item-key")==plan["key"]
        assert plan["icon"] in icons,(pid,address,"missing SVG")

def browser(base):
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as e:raise RuntimeError("Playwright Python required") from e
    QA.mkdir(parents=True,exist_ok=True)
    with sync_playwright() as pw:
        b=pw.chromium.launch(headless=True,
            executable_path=r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
        try:
            for name,width,height in (("desktop",1366,900),("mobile",390,844),("small-mobile",320,720)):
                context=b.new_context(viewport={"width":width,"height":height})
                page=context.new_page()
                selection=[("01",0),("02",0),("02",1),("04",1),
                           ("05",1),("06",0),("13",1),("16",0),
                           ("19",0),("20",0),("21",0),("25",1),
                           ("30",2),("35",1),("38",0),("41",0),
                           ("58",0),("61",1)]
                for pid,idx in selection:
                    url=(PAGES/(pid+".html")).resolve().as_uri() if base is None else base.rstrip("/")+"/events/"+pid+".html?tableqa=1"
                    page.goto(url,wait_until="domcontentloaded",timeout=30000)
                    table=page.locator("table").nth(idx)
                    if table.locator("img.table-item-icon").count()==0:
                        raise AssertionError(f"{name} {pid}#{idx}: no table illustrations")
                    for item in table.locator("img.table-item-icon").all():
                        item.scroll_into_view_if_needed()
                        item.evaluate("(x)=>x.decode()")
                    stat=table.locator("img.table-item-icon").evaluate_all(
                        "(items)=>items.every(x=>x.complete && x.naturalWidth>0 && x.getBoundingClientRect().width>=15)")
                    if not stat:raise AssertionError(f"{name} {pid}#{idx}: SVG failed to decode")
                    overflow=page.evaluate("document.documentElement.scrollWidth>innerWidth+1")
                    if overflow:raise AssertionError(f"{name} {pid}#{idx}: page horizontal overflow")
                    if (pid,idx) in (("02",0),("02",1),("04",1),
                                     ("06",0),("16",0),("20",0),("21",0)) and name!="small-mobile":
                        table.screenshot(path=str(QA/f"table_icons_{name}_{pid}_{idx}.png"))
                print("TABLE BROWSER PASS",name,len(selection),"representative tables")
                context.close()
        finally:b.close()

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--browser",action="store_true")
    parser.add_argument("--live",action="store_true",help="Test public Pages instead of local file")
    parser.add_argument("--compare-head",action="store_true",help="Require prose identical to Git HEAD for icon-only edits")
    opts=parser.parse_args()
    verify(opts.compare_head)
    if opts.browser:
        browser("https://cuonghappypets.github.io/jxoffline-v5-classic-events-remastered" if opts.live else None)
