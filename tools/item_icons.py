#!/usr/bin/env python3
"""Reproducible, player-facing item illustrations for CGPT handbook.

No game sprites or VNG artwork are embedded.  The committed manifest maps each
event's *ordered* public item cards to an original SVG family and a source
client item ID.  Seed once from the local source catalog; regular builds use
only the committed manifest and original SVGs.

Usage:
  python tools/item_icons.py --seed    # private workspace catalog required
  python tools/item_icons.py           # rebuild public HTML from manifest
  python tools/item_icons.py --check   # assert published markup/assets
"""
import argparse
from collections import Counter, defaultdict
import hashlib
import html
import json
from pathlib import Path
import re
import sys
import unicodedata
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "docs" / "events"
ASSETS = ROOT / "docs" / "assets" / "item-icons"
MANIFEST = ROOT / "tools" / "item_icon_map.json"
# The private sources directory lives alongside 01_REPOSITORY in this workspace:
PRIVATE = ROOT.parent.parent / "05_HANDBOOK" / "sources"
PATTERN = re.compile(
    r'(?P<open><div class="item-card">)(?P<art><img\b(?=[^>]*\bclass="item-illustration")[^>]*>)?'
    r'(?P<label><div><strong>(?P<name>.*?)</strong>)', re.S
)
NORMALIZE = lambda s: "".join(ch for ch in unicodedata.normalize("NFD", str(s).lower().replace("đ", "d")) if unicodedata.category(ch) != "Mn")
def words(s):
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9]+", " ", NORMALIZE(s))).strip()

def classify(raw, key):
    n = words(raw)
    has = lambda *p: any(x in n for x in p)
    start = lambda *p: any(n.startswith(x) for x in p)
    # Icon semantics take precedence over arbitrary text shared by item names.
    # Source-backed overrides for items whose display names suggest the wrong
    # physical form. Keyed by client-004 IDs, never by neighboring text.
    keyed = {
        "6,1,23": "book",        # Thiết La Hán: obj_item_lection.spr
        "6,1,35": "book",        # Vân Long Kích. Mâu pháp: martial manual
        "6,1,41": "book",        # Thúy Yên Song đao: martial manual
        "gold,146": "necklace",  # Phỉ Thúy Ngọc Hạng Khuyên: equip/nick
        "gold,187": "necklace",  # Hiệp Cốt Đa Tình Hoàn: equip/nick
        "6,1,1221": "paper-yellow",
        "6,1,1222": "paper-blue",
        "6,1,1223": "paper-green",
        "6,1,1224": "paper-red",
        "6,1,1225": "paper-orange",
        "6,1,217": "pill-small",
        "6,1,216": "pill-medium",
        "6,1,215": "pill-large",
        "6,1,1179": "peach-bun-bean",
        "6,1,1180": "peach-bun-date",
        "6,1,30340": "plaque-wood",
        "6,1,30383": "plaque-copper",
        "6,1,30384": "plaque-silver",
        "6,1,30569": "plaque-gold",
        "6,1,30570": "plaque-jade",
        "6,1,1960": "lipstick",
        "6,1,1961": "hairclip",
        "6,1,1963": "comb",
        "6,1,1634": "snowman-yellow",
        "6,1,1635": "snowman-purple",
        "6,1,1636": "snowman-green",
        "6,1,1441": "gift-box-blue",
        "6,0,1012": "gift-box-blue",
        "gold,166": "pendant-amber",
        "6,1,1765": "potion-special",
        "6,1,2358": "ball-shell",
        "6,1,2361": "ball-bladder",
        "6,1,2363": "ball",
        "6,1,2364": "ball-gold",
        "6,1,1927": "seed",
        "6,1,2207": "seed",
        "6,1,2294": "seed",
        "6,1,30571": "sapling",
        "6,1,2010": "ingredient-sack",
        "6,1,2012": "yeast-starter",
        "6,1,2013": "wine-gourd",
        "6,1,2296": "water-bucket",
        "4,975,1": "milk-bottle",
        "4,976,1": "ingredient-sack",
        "4,977,1": "ingredient-sack",
        "6,1,1175": "ingredient-sack",
        "6,1,1176": "ingredient-sack",
        "6,1,1177": "ingredient-sack",
        "6,1,214": "signal-horn",
        "6,1,2097": "bucket-hat",
        "6,1,2098": "soft-hat-peace",
        "6,1,2099": "soft-hat-freedom",
        "6,1,2100": "soft-hat-happiness",
        "6,1,2304": "soft-hat-soldier",
    }
    if key in keyed: return keyed[key]
    if re.fullmatch(r"6,1,135[1-9]",key):
        num=int(key.split(",")[-1])
        size=("small","medium","large")[(num-1351)%3]
        return "firecracker-"+size+("-special" if num in {1354,1355,1356} else "")
    if re.fullmatch(r"4,\d+,1",key) and n.startswith("manh "):
        source_index=int(key.split(",")[1])
        return "fragment-large" if source_index in set(
            list(range(585,594))+list(range(594,602))+
            list(range(631,639))+list(range(684,692))+
            list(range(702,710))) else "fragment-small"
    if re.fullmatch(r"6,1,12(?:0[7-9]|1[0-8])",key):
        idx=int(key.split(",")[-1])-1207
        theme="traveler" if idx<6 else "immortal"
        return "picture-"+theme+"-"+str(idx%6+1)
    if re.fullmatch(r"6,1,173[5-8]",key):
        return "flag-piece-"+str(int(key.split(",")[-1])-1734)
    if re.fullmatch(r"6,1,175[2-9]",key):
        return "letter-tile-"+str(int(key.split(",")[-1])-1751)
    if has("banh chung"):
        return "banh-chung-premium" if has("thuong hang") else "banh-chung-mixed"
    if has("banh tet"):
        return "banh-tet-bean" if has("nhan dau") else "banh-tet-mixed"
    if has("banh trung thu", "banh hat sen", "banh khoai mon",
           "banh dau xanh", "banh nhan thit", "dao van tho"):
        if has("con heo"): return "mooncake-pig"
        if has("hat sen"): return "mooncake-lotus"
        if has("nhan trung"): return "mooncake-egg"
        if has("dau xanh"): return "mooncake-bean"
        if has("nhan thit"): return "mooncake-meat"
        if has("khoai mon"): return "mooncake-taro"
        if has("dac biet"): return "mooncake-special"
        if has("dao van tho"): return "mooncake-peach"
        return "mooncake"
    if has("banh kem", "banh sinh nhat") and has("dac biet", "thuong han"):
        return "cake-special"
    if start("hop qua ", "qua mau "):
        if has("vang"): return "gift-box-gold"
        if has("trang"): return "gift-box-white"
        if has("xanh"): return "gift-box-green"
    if start("tui dai hy "):
        for season, family in [("xuan","bag-spring"),("ha ","bag-summer"),
                               ("thu ","bag-autumn"),("dong","bag-winter")]:
            if season in n: return family
    if has("phuc duyen lo"):
        if has("tieu"): return "potion-small"
        if has("trung"): return "potion-medium"
        if has("dai"): return "potion-large"
    if has("long den") and has("dac biet"):
        for part, icon in [("buom buom","lantern-butterfly"),
                           ("ca chep","lantern-carp"),
                           ("keo quan","lantern-revolving"),
                           ("ngoi sao","lantern-star"),
                           ("tron","lantern-round"),
                           ("ong","lantern-tube")]:
            if part in n: return icon+"-special"
    if has("lam thuy tinh"): return "crystal-blue"
    if has("luc thuy tinh"): return "crystal-green"
    if has("tu thuy tinh"): return "crystal-purple"
    if has("tinh hong bao thach"): return "crystal-red"
    if has("ngu sac bang tinh"): return "crystal-rainbow"
    if has("phu dung thach"): return "crystal-purple"
    if has("khong tuoc thach"): return "crystal-green"
    if has("ke huyet thach gioi chi"): return "ring-ruby"
    if has("cuc hoa thach chi hoan"): return "ring-amber"
    # Exact exceptions prevent substring collisions: "hoa" in "hoa dan",
    # "ao" in "bao", "nhan" in "ca nhan", etc.
    if n in {"3", "chien", "mung", "thanh", "lien", "that", "dai",
             "tuoi", "vltk", "tieu tu khung", "nguyet ha lao nhan",
             "khang don chi giac"}: return "paper"
    if n in {"moc", "kim", "thuy", "hoa", "tho", "phong"}:
        return {"moc":"element-wood", "kim":"element-metal",
                "thuy":"element-water", "hoa":"element-fire",
                "tho":"element-earth", "phong":"flag"}[n]
    if start("an bang "):
        if has("hang lien"): return "necklace"
        if has("ngoc boi"): return "pendant"
        return "ring"
    if start("dinh quoc "):
        if has("truong sam"): return "armor"
        if has("phat quan"): return "hat"
        if has("nhuyen ngoa"): return "boots"
        if has("ho uyen"): return "bracer"
        if has("yeu dai"): return "belt"
    if start("dong sat "):
        return "pendant" if has("ngoc", "hang khuyen") else "ring"
    if start("thuy yen song dao"): return "sword"
    if start("cuon vai"): return "silk"
    if start("to tam huong bao"): return "bag"
    if start("to tam"): return "silk"
    if start("manh u minh thuong"): return "spear"
    if start("manh dai nhan than chuy"): return "hammer"
    if has("bac dau mon"): return "talisman"
    if has("long den", "vat lieu") and has("vat lieu"):
        if has("thanh tre"): return "bamboo"
        if has("day coi"): return "rope"
        if has("giay kieng"): return "paper"
        return "gift-box"
    if has("bong hoang kim", "bong da", "vo bong", "ruot cao su"): return "ball"
    if has("vo giang sinh"): return "stocking"
    if has("bo cau"): return "bird"
    if has("hoa tai"): return "earring"
    if n == "nen": return "candle"
    if has("quoc khanh", "bao li xi", "le vat tinh nhan"): return "gift-box"
    if has("bach qua lo", "thien son bao lo", "tien thao lo", "que hoa tuu",
           "do khang tuu", "hoi quan linh duoc lo", "phuc duyen lo"): return "potion-bottle"
    if has("thuoc tru sau"): return "potion-bottle"
    if has("tao hoa dan", "tong kim ", "bach chan don", "bach cau hoan"): return "pill"
    if has("ngu sac bang tinh"): return "crystal"
    if has("hoa bang tinh"): return "element-fire"
    if has("hat giang sinh", "hat thien tue", "cay con"): return "flower"
    if has("thiet la han", "chat deo"): return "package"
    if has("ham tinh thuat", "han tinh thuat", "ngu loi thuat", "ngu phong thuat",
           "ngu tam thuat", "nhiep hon", "phi tieu thuat", "phi dao thuat",
           "tu tien thuat"): return "book"
    if has("thiep hoa hong"): return "scroll"
    if n == "tao do": return "apple"
    if has("manh co"): return "flag"
    if start("tui ") or has("huong bao"): return "bag"
    exact = {
        "mang cau": "mang-cau", "dua": "dua", "du du": "du-du",
        "xoai": "xoai", "sung": "sung",
    }
    if n in exact: return exact[n]
    if start("mang cau"): return "mang-cau"
    if start("du du"): return "du-du"
    if start("dua ") or n == "dua": return "dua"
    if start("xoai "): return "xoai"
    if start("sung "): return "sung"
    if has("banh chung"): return "banh-chung"
    if has("banh tet"): return "banh-tet"
    if has("banh trung thu", "banh hat sen", "banh khoai mon", "banh dau xanh", "banh nhan thit", "dao van tho"): return "mooncake"
    if has("banh kem", "banh sinh nhat", "banh bong lan"): return "cake"
    if start("banh ", "bao gao", "bot ", "duong ", "dau xanh", "sua tuoi"): return "rice"
    if has("long den"):
        for part, icon in [
            ("buom buom", "lantern-butterfly"), ("ca chep", "lantern-carp"),
            ("keo quan", "lantern-revolving"), ("ngoi sao", "lantern-star"),
            ("tron", "lantern-round"), ("ong", "lantern-tube"),
        ]:
            if part in n: return icon
        return "lantern-round"
    if has("phong phao", "phao ", "phao tieu", "phao trung", "phao dai"): return "firecracker"
    if has("nen ", "nen do"): return "candle"
    if has("chuong giang sinh"): return "bell"
    if has("tuyet nhan", "hoang tuyet", "luc tuyet", "tu tuyet"): return "snowman"
    if has("hoa tuyet", "ngoi sao"): return "star"
    if has("hoa hong", "hoa sen", "nhanh mai", "hat cay", "cay con", "that tinh thao"): return "flower"
    if has("bac dau mon", "lenh bai", "hieu phu", "kim bai", "moc bai", "ngan bai", "ngoc bai", "dong bai", "thuong co lenh", "khieu chien", "chi an"): return "talisman"
    if has("huyen tinh khoang", "huyen thiet", "thien nien han thiet", "khoang", "thep tinh luyen", "chu sa", "chung nhu", "mat ngan"): return "mineral"
    for element, icon in [
        ("kim bang tinh", "element-metal"), ("moc bang tinh", "element-wood"),
        ("thuy bang tinh", "element-water"), ("hoa bang tinh", "element-fire"),
        ("tho bang tinh", "element-earth")
    ]:
        if element in n: return icon
    if n == "free item":
        return {"6,1,30070":"element-wood","6,1,30072":"element-fire","6,1,30073":"element-earth"}.get(key,"crystal")
    if has("thuy tinh", "bao thach", "tinh thach", "ngoc thach", "kim thach", "khoang thach", "khong tuoc thach", "tran bang thach", "phu dung thach", "hoa bang tinh"): return "crystal"
    if has("do pho", "mat do", "thiep", "giay kieng", "giay goi", "manh tranh", "mat thu", "tho dia phu"): return "scroll"
    if has("mat tich", "tam kinh", "tay tuy kinh", "quyen 1", "quyen 2", "quyen 3", "kiem pho", "truong phap", "kiem phap", "thuong phap", "dao phap", "chuong phap", "con phap", "thu phap", "vo lam mat tich", "truyen cong thuat", "nghiep thuat", "nghiep phap", "ngoc kinh", "nghiem phap", "ky thuat", "nghe thuat"): return "book"
    if has("vo lam mat thu"): return "scroll"
    # Gold equipment slot exact families. An Bang & Dinh Quoc are distinct.
    if has("truong sam", "nghe thuong", "huyet sam", "ca sa", "bao giap") and not has("manh "): return "armor"
    if has("phat quan", "chiec mu", "mu "): return "hat"
    if has("nhuyen ngoa", "nhuyen ly", "doi giay", "giay bo doi"): return "boots"
    if has("ho uyen", "thu trac"): return "bracer"
    if has("yeu dai", "phat dai", "dai lung"): return "belt"
    if has("hang lien", "hang khuyen", "day chuyen", "vong co"): return "necklace"
    if has("ngoc boi", "nghia boi", "khau", "lang nha boi", "tinh y ket", "day deo"): return "pendant"
    if has("gioi chi", "chi hoan", "da tinh hoan", "dan tam gioi") or re.search(r"\bnhan\b",n): return "ring"
    if has("manh "):
        if has("dao", "kiem", "thuong", "chuy", "phi dao"): return "sword"
        if has("huyen ngoc", "ngoc khau"): return "pendant"
        if has("than thiet", "thiet"): return "mineral"
        return "paper"
    if has("kiem", "phi dao", "gioi dao", "dao ", "chuy"): return "sword"
    if has("thuong", "mau phap"): return "spear"
    if has("hoang kim bao hap", "bao hap", "ruong", "hop ", "le bao", "hong bao", "li xi", "qua ", "qua quoc khanh", "dai hy"): return "gift-box"
    if has("tui ", "bao ", "huong bao", "tui vat dung"): return "bag"
    if has("hoa hong", "bo cau", "la ", "to tam", "do may"): return "flower"
    if has("thanh tre"): return "bamboo"
    if has("day coi", "day ", "cuon vai", "to tam", "kim chi", "khan quang", "no do", "khan "): return "silk"
    if has("giay", "manh co", "manh tranh", "co ", "la co"): return "paper"
    if has("binh nuoc", "nuoc tinh", "thung nuoc", "ruou", "long tinh tra", "le duoc", "duoc lo", "duyen lo", "bao lo", "thuy", "bao lo", "nuoc hoa", "tinh chat"): return "potion-bottle"
    if has("hoan", "dan ", "bach chan", "duoc", "thuoc"): return "pill"
    if has("trung ga"): return "egg"
    if has("bong ", "vo bong", "cao su"): return "ball"
    if has("guong", "luoc", "kep toc", "thoi son"): return "mirror"
    if has("chien co"): return "drum"
    if has("co", "ky", "chien thang"): return "flag"
    if has("cuon vai", "vai", "to tam", "buoc", "day"): return "silk"
    if has("vat lieu", "ket", "ruot", "men ", "phan bon", "phu lieu", "dung cu"): return "package"
    if has("bao", "hop", "goi", "thiep"): return "gift-box"
    # Neutral sealed packet is intentionally used where a catalog name gives
    # no defensible physical shape, never as an alleged original game sprite.
    return "package"

def read_cards(page):
    return [(html.unescape(match.group("name")).strip(), match) for match in PATTERN.finditer(page)]

def seed():
    if not (PRIVATE / "events.json").exists():
        raise RuntimeError("Private source missing; seed only in authorized workspace")
    events = {int(e["id"]):e for e in json.loads((PRIVATE / "events.json").read_text(encoding="utf8"))}
    catalog = json.loads((PRIVATE / "item_icons.json").read_text(encoding="utf8"))
    pages = {}
    issues = []
    for page in sorted(HTML.glob("[0-9][0-9].html")):
        pid = int(page.stem)
        cards = read_cards(page.read_text(encoding="utf8"))
        available = list(events[pid]["tuples"])
        records = []
        for label, _ in cards:
            candidates = [k for k in available if words(catalog.get(k,{}).get("name","")) == words(label)]
            if not candidates:
                issues.append(f"{page.name}: no client item for {label!r}")
                continue
            chosen = candidates[0]
            available.remove(chosen)
            records.append({"name":label,"key":chosen,"icon":classify(label,chosen)})
        if len(cards) != len(records):
            raise RuntimeError("Unmapped source keys:\n" + "\n".join(issues))
        pages[page.stem] = records
    if len(pages) != 61 or sum(map(len,pages.values())) != 575:
        raise RuntimeError("Source inventory changed; inspect before seeding")
    MANIFEST.parent.mkdir(parents=True,exist_ok=True)
    MANIFEST.write_text(json.dumps({"schema":1,"kind":"original-illustration","pages":pages},ensure_ascii=False,indent=2)+"\n",encoding="utf8")
    print("SEED:",len(pages),"pages,",sum(map(len,pages.values())),"mapped item occurrences,",len({v["key"] for rows in pages.values() for v in rows}),"unique keys")

def reclassify():
    """Update illustration families without rereading or distributing private catalog."""
    data=json.loads(MANIFEST.read_text(encoding="utf8"))
    changes=0
    for rows in data["pages"].values():
        for row in rows:
            icon=classify(row["name"],row["key"])
            if row["icon"]!=icon:
                row["icon"]=icon
                changes+=1
    MANIFEST.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf8")
    print("RECLASSIFY:",changes,"icon assignments changed")

def validate_svgs():
    files={}
    for p in ASSETS.glob("*.svg"):
        root=ET.parse(p).getroot()
        if root.tag != "{http://www.w3.org/2000/svg}svg": raise RuntimeError("Malformed SVG root: "+str(p))
        txt=p.read_text(encoding="utf8")
        if re.search(r'<(?:script|image)\b|(?:xlink:)?href\s*=|url\(\s*["\x27]?https?://',txt,re.I):
            raise RuntimeError("Non-self-contained SVG: "+str(p))
        files[p.stem]=p
    if not files: raise RuntimeError("No original SVG assets")
    return files

def build(check=False):
    payload=json.loads(MANIFEST.read_text(encoding="utf8"))
    pages=payload["pages"]
    icons=validate_svgs()
    unmapped={r["icon"] for rows in pages.values() for r in rows} - set(icons)
    if unmapped: raise RuntimeError("SVG assets missing: "+", ".join(sorted(unmapped)))
    assert set(pages)=={p.stem for p in HTML.glob("[0-9][0-9].html")}, "Page inventory drift"
    total=0
    changed=0
    for pid, rows in pages.items():
        page=HTML/(pid+".html")
        old=page.read_text(encoding="utf8")
        count=[0]
        def convert(m):
            index=count[0]
            if index>=len(rows): raise RuntimeError(f"{pid}: unexpected extra item card")
            row=rows[index]
            label=html.unescape(m.group("name")).strip()
            if label!=row["name"]: raise RuntimeError(f"{pid} card {index}: source drift {label!r} != {row['name']!r}")
            # data-item-key is a traceable catalog reference, not a sprite claim.
            img=(f'<img class="item-illustration" src="../assets/item-icons/{row["icon"]}.svg" '
                 f'alt="" aria-hidden="true" loading="lazy" width="44" height="44" '
                 f'data-item-key="{html.escape(row["key"],quote=True)}">')
            count[0]+=1
            return m.group("open")+img+m.group("label")
        updated=PATTERN.sub(convert,old)
        if count[0]!=len(rows): raise RuntimeError(f"{pid}: only {count[0]}/{len(rows)} cards")
        if updated!=old:
            changed+=1
            if not check: page.write_text(updated,encoding="utf8")
        total+=count[0]
    if check and changed: raise RuntimeError(f"{changed} pages do not match committed manifest")
    print(("CHECK" if check else "BUILD")+f": {len(pages)} pages / {total} cards / {len(icons)} original SVG families / {changed} pages updated")
    return 0

if __name__=="__main__":
    a=argparse.ArgumentParser()
    a.add_argument("--seed",action="store_true",help="Build committed mapping once from private authorized sources")
    a.add_argument("--reclassify",action="store_true",help="Rerun classification on committed manifest")
    a.add_argument("--check",action="store_true",help="Check HTML matches committed mapping and assets")
    opts=a.parse_args()
    if opts.seed: seed()
    elif opts.reclassify: reclassify()
    else: build(opts.check)
