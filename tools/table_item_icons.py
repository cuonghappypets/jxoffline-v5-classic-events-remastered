#!/usr/bin/env python3
"""Source-mapped, lossless SVG decoration inside event handbook tables.

One-time audited planning: python tools/table_item_icons.py --seed
Deterministic rebuild:  python tools/table_item_icons.py
Verify against plan:   python tools/table_item_icons.py --check

Only insert decorative <img> tags in existing <td> text nodes.  No text,
attributes, links, numbers, inline tags or game logic are rewritten.
The versioned table_icon_map.json freezes resolved aliases by page/table/row
and a SHA256 of the unmodified cell HTML; future copy edits fail closed.
"""
import argparse
from collections import Counter, defaultdict
import hashlib
import html
import json
from pathlib import Path
import re
import unicodedata

from item_icons import MANIFEST, ASSETS

ROOT=Path(__file__).resolve().parents[1]
PAGES=ROOT/"docs"/"events"
MAP=ROOT/"tools"/"table_icon_map.json"
TABLE=re.compile(r'<table\b[^>]*>.*?</table>',re.I|re.S)
ROW=re.compile(r'<tr\b[^>]*>.*?</tr>',re.I|re.S)
CELL=re.compile(r'(?P<open><td\b[^>]*>)(?P<inner>.*?)(?P<close></td>)',re.I|re.S)
HEADER=re.compile(r'(?P<open><th\b[^>]*>)(?P<inner>.*?)(?P<close></th>)',re.I|re.S)
TH=re.compile(r'<th\b[^>]*>(.*?)</th>',re.I|re.S)
TAG=re.compile(r'(<[^>]+>)')
IMG=re.compile(r'<img\b(?=[^>]*\bclass="table-item-icon")[^>]*>')
STRIP=re.compile(r'<[^>]+>')
KEY=re.compile(r'(?<![\w])(?:gold,\d+|[46],[01],\d+|4,\d+,1)(?![\w])')
BADHEAD=re.compile(r'^(?:tỷ lệ|xác suất|phí|exp|tiền|điểm|số lượng|mã vật phẩm|id|map|tọa độ|trần|cấp yêu cầu|lượt gọi|giới hạn|cấp quái|nhóm quái|thành công|độ trễ|25 điểm|15–24|1–14|0$)',re.I)
SKIP_TAGS={"code","small","a","script","style"}
MANUAL={
    "Huyền Tinh": "mineral", "HT2":"mineral","HT3":"mineral","HT4":"mineral","HT5":"mineral",
    "Tinh Thạch":"crystal","Thủy Tinh":"crystal","Đá quý":"crystal",
    "Giấy vàng":"paper-yellow","Giấy lam":"paper-blue","Giấy lục":"paper-green",
    "Giấy đỏ":"paper-red","Giấy cam":"paper-orange",
    "Giấy kiếng":"paper","Thanh tre":"bamboo","Dây cói":"rope",
    "Dừa":"dua","TTL đặc biệt":"potion-special",
    "Phúc Duyên Lộ Tiểu":"potion-small","Phúc Duyên Lộ Trung":"potion-medium",
    "Phúc Duyên Lộ Đại":"potion-large","PDL Tiểu":"potion-small",
    "PDL Trung":"potion-medium","PDL Đại":"potion-large",
    "Tiên Thảo Lộ":"potion-bottle","Thiên Sơn Bảo Lộ":"potion-bottle",
    "Bột mì":"ingredient-sack","Bột tinh":"ingredient-sack",
    "Bột gạo":"ingredient-sack","Bột sen":"ingredient-sack",
    "Đường cát":"ingredient-sack","Đường tinh":"ingredient-sack",
    "Đường":"ingredient-sack","Bột":"ingredient-sack",
    "Đậu xanh":"ingredient-sack","Hạt sen":"ingredient-sack",
    "Hạnh nhân":"ingredient-sack","Đậu phộng":"ingredient-sack","Cơm dừa":"ingredient-sack",
    "Trứng gà":"egg","Trứng":"egg","Sữa tươi":"milk-bottle","Sữa":"milk-bottle",
    "Táo đỏ":"apple","Nến":"candle","Chuông":"bell","Vớ":"stocking",
    "Thiệp":"scroll","Ngôi sao":"star","Quế Hoa Tửu":"wine-gourd",
    "Lục Bảo Châu":"crystal-green",
    "Hoa hồng":"flower","Cành hồng":"flower","Cành cúc":"flower",
    "Nơ đỏ":"silk", "Mật thư":"scroll", "Mật Đồ":"scroll",
    "Mật Đồ Lễ hội":"scroll","Kim Thạch Lễ hội":"crystal",
    "Tín vật":"talisman","Bí quyết":"book",
    "Kim chỉ":"silk","Vải hảo hạng":"silk","Cuộn vải":"silk",
    "Vải":"silk",
    "Bánh thường":"mooncake", "Bánh con heo":"mooncake-pig",
    "Bánh kem":"cake","Bánh sinh nhật":"cake",
    "Thỏi son":"lipstick","Kẹp tóc":"hairclip","Lược":"comb","Gương":"mirror",
    "Dây chuyền":"necklace","Thủ trạc":"bracer","Hoa tai":"earring","Nhẫn":"ring",
    "Khăn quàng cổ":"silk","Nước hoa":"potion-bottle",
    "Bình nước":"potion-bottle","Túi thức ăn":"bag",
    "Bánh hạt sen":"mooncake-lotus","Bánh đậu xanh":"mooncake-bean",
    "Bánh khoai môn":"mooncake-taro",
    "Thịt gà":"chicken-meat","Thịt heo":"pork-meat",
    "Gà nướng":"roast-chicken","Heo quay":"roast-pork",
    "Hộp bánh":"gift-box","Ngũ Hành Kỳ Thạch":"crystal-rainbow",
    "Mặt nạ":"mask","Thần Bí Đại Hồng Bao":"gift-box",
    "Tây Hồ Long Tỉnh Trà":"potion-bottle",
    "Hộp quà":"gift-box","Rương bạc":"gift-box","Hoàng Kim Bảo Hạp":"gift-box",
    "Đại Hỷ Bảo Hạp":"gift-box","Đại Cát Bảo Hạp":"gift-box",
    "Mảnh cờ":"flag-piece-1",
    "Bánh Kem Như Ý":"cake","Bánh Kem Cát Tường":"cake",
    "Bánh Đậu Xanh":"mooncake-bean",
}
# Scoped aliases are unambiguous only for a specific table + column.
# Keys are (page ID, zero-based table number, zero-based column number).
SCOPED={
 ("02",1,0):{"Bươm bướm":"lantern-butterfly","Ngôi sao":"lantern-star",
            "Ống":"lantern-tube","Tròn":"lantern-round","Cá chép":"lantern-carp",
            "Kéo quân":"lantern-revolving"},
 ("27",0,0):{"Bươm bướm":"lantern-butterfly","Ngôi sao":"lantern-star",
            "Ống":"lantern-tube","Tròn":"lantern-round","Cá chép":"lantern-carp",
            "Kéo quân":"lantern-revolving"},
 ("02",2,0):{"Thường":"mooncake","Đậu xanh":"mooncake-bean",
             "Nhân trứng":"mooncake-egg","Đặc biệt":"mooncake-special",
             "Hạt sen":"mooncake-lotus","Con heo":"mooncake-pig"},
 ("02",2,1):{"Bươm bướm đặc biệt":"lantern-butterfly-special",
             "Ngôi sao đặc biệt":"lantern-star-special",
             "Ống đặc biệt":"lantern-tube-special","Tròn đặc biệt":"lantern-round-special",
             "Cá chép đặc biệt":"lantern-carp-special",
             "Kéo quân đặc biệt":"lantern-revolving-special"},
 ("04",1,0):{"Đậu xanh":"mooncake-bean","Hạt sen":"mooncake-lotus",
             "Đậu trứng":"mooncake-egg","Sen trứng":"mooncake-egg",
             "Quả nhân":"mooncake","Thập cẩm":"mooncake-special"},
 ("06",1,0):{"Đậu xanh":"cake","Hạt sen":"cake","Trứng":"cake",
             "Thập cẩm":"cake","Gà nướng":"roast-chicken",
             "Heo quay":"roast-pork","Hộp bánh":"gift-box"},
 ("10",1,0):{"Thường":"cake","Đặc biệt":"cake-special"},
 ("13",1,0):{"Bánh sinh nhật thượng hạng":"cake-special"},
 ("13",2,0):{"Vui Vẻ":"candle","Bình An":"candle",
              "May Mắn":"candle","Hạnh Phúc":"candle"},
 ("16",0,0):{"Trắng":"gift-box-white","Xanh":"gift-box-blue",
              "Vàng":"gift-box-gold"},
 ("15",1,0):{"Đậu xanh":"peach-bun-bean","Nhân táo":"peach-bun-date"},
 ("03",1,0):{"Tiểu":"firecracker-small","Trung":"firecracker-medium","Đại":"firecracker-large"},
 ("03",0,2):{"tiểu":"firecracker-small","trung":"firecracker-medium",
             "đại":"firecracker-large",
             "Phong tiểu đặc biệt":"firecracker-small-special",
             "Phong trung đặc biệt":"firecracker-medium-special",
             "Phong đại đặc biệt":"firecracker-large-special"},
 ("05",0,0):{"Kim":"element-metal","Mộc":"element-wood","Thủy":"element-water",
             "Hỏa":"element-fire","Thổ":"element-earth","Ngũ Sắc":"crystal-rainbow"},
 ("05",1,0):{"Hoàng":"snowman-yellow","Tử":"snowman-purple","Lục":"snowman-green"},
 ("05",1,1):{"Kim":"element-metal","Mộc":"element-wood","Thủy":"element-water",
             "Hỏa":"element-fire","Thổ":"element-earth","Ngũ Sắc":"crystal-rainbow"},
 ("20",0,0):{"Xuân":"bag-spring","Hạ":"bag-summer","Thu":"bag-autumn","Đông":"bag-winter"},
 ("21",0,0):{"Thịnh Vượng":"gift-box","Phát Tài":"gift-box"},
 ("21",0,1):{"Phúc":"lucky-phuc","Lộc":"lucky-loc","Thọ":"lucky-tho"},
 ("19",0,0):{"Thượng hạng":"mooncake-special",
             "Hảo hạng":"mooncake","Thường":"mooncake"},
 ("25",0,0):{"Hồng":"flower","Cúc":"flower"},
 ("25",1,0):{"Hồng":"flower","Cúc":"flower"},
 ("28",1,0):{"Mộc":"plaque-wood","Đồng":"plaque-copper","Ngân":"plaque-silver",
             "Kim":"plaque-gold","Ngọc":"plaque-jade"},
 ("38",0,0):{"Dâu":"cake","Sô-cô-la":"cake-special"},
 ("38",0,1):{"Vớ":"stocking"},
 ("41",1,0):{"Hòa bình":"soft-hat-peace","Tự do":"soft-hat-freedom",
             "Hạnh phúc":"soft-hat-happiness"},
 ("42",0,0):{"Mai Trường Thọ":"sapling","Mai An Khang":"sapling",
             "Mai Thịnh Vượng":"sapling","Mai Hạnh Phúc":"sapling",
             "Mai Tài Phú":"sapling"},
 ("45",0,0):{"An Lành":"sapling","Hòa Bình":"sapling",
             "Độc Lập":"sapling","Tự Do":"sapling",
             "Hạnh Phúc":"sapling","Thịnh Vượng":"sapling"},
 ("09",1,0):{"Lam":"crystal-blue","Tử":"crystal-purple",
             "Lục":"crystal-green"},
 ("59",0,1):{"Mộc":"element-wood","Hỏa":"element-fire","Thổ":"element-earth"},
 ("61",1,0):{"Thất":"paper","Thành":"paper","Đại":"paper","Chiến":"paper"},
}
for pid,tbl,col in (("02",1,1),("27",0,1)):
 SCOPED[(pid,tbl,col)]={"vàng":"paper-yellow","lam":"paper-blue",
   "lục":"paper-green","đỏ":"paper-red","cam":"paper-orange"}
# Synthetic short aliases limited to table contexts where individual words
# genuinely refer to items rather than adjectives, NPCs or elements.
EXTRA={
 ("20",1,0):{"Phong":"letter-tile-5","Hỏa":"letter-tile-6",
              "Liên":"letter-tile-7","Thành":"letter-tile-8",
              "Mừng":"letter-tile-1","VLTK":"letter-tile-2",
              "Tuổi":"letter-tile-4"},
 ("41",0,0):{"mũ tai bèo":"bucket-hat","mũ hòa bình":"soft-hat-peace",
              "mũ tự do":"soft-hat-freedom","mũ hạnh phúc":"soft-hat-happiness"},
 ("41",0,1):{"mũ hòa bình":"soft-hat-peace",
              "mũ tự do":"soft-hat-freedom","mũ hạnh phúc":"soft-hat-happiness"},
}
SCOPED.update(EXTRA)
HEADER_ITEMS={
    ("20",0):[
        ("Mừng","letter-tile-1","6,1,1752"),
        ("VLTK","letter-tile-2","6,1,1753"),
        ("3","letter-tile-3","6,1,1754"),
        ("Tuổi","letter-tile-4","6,1,1755"),
        ("Phong","letter-tile-5","6,1,1756"),
        ("Hỏa","letter-tile-6","6,1,1757"),
        ("Liên","letter-tile-7","6,1,1758"),
        ("Thành","letter-tile-8","6,1,1759"),
    ]
}
# Exclude generic labels reused as narrative or grade metadata.
UNSAFE={"3","free item","vltk","mung","phong","hoa","thanh","that","dai",
        "chien","lien","tuoi","trung","thuong","nho","kim","moc","thuy",
        "tho","ngoc","do","lam","luc","vang","den","thiep","ao",
        "mau","hat","quyen","bao","qua","tui","nhan","trung","phuc","loc","tho"}

def normalized(raw):
    out=[]; pos=[]
    for i,ch in enumerate(raw):
        if ch=="đ" or ch=="Đ": letters="d"
        else: letters="".join(x for x in unicodedata.normalize("NFD",ch.casefold()) if unicodedata.category(x)!="Mn")
        for x in letters:out.append(x);pos.append(i)
    return "".join(out),pos

def key(s):
    return re.sub(r"\s+"," ",normalized(html.unescape(s).strip())[0]).strip()

def literal(s):
    return re.sub(r"\s+"," ",html.unescape(s).strip().casefold())

def nodeparts(inner):
    """Text chunks plus literal tags; preserve every existing source byte."""
    return TAG.split(inner)

def visible_text(inner):
    return html.unescape(STRIP.sub("",IMG.sub("",inner)))

def stripped(inner):
    return IMG.sub("",inner)

def digest(inner):
    return hashlib.sha256(inner.encode("utf8")).hexdigest()

def catalog():
    rows=json.loads(MANIFEST.read_text(encoding="utf8"))["pages"]
    names=defaultdict(list);byid={}
    for pid,entries in rows.items():
        for r in entries:
            byid[r["key"]]=(r["icon"],r["name"])
            n=key(r["name"])
            if n and n not in UNSAFE and len(n)>3: names[n].append((r["icon"],r["key"],pid,r["name"]))
            # Keep useful stable core while stripping verbose explanations.
            clipped=re.sub(r"\s*\([^)]*(?:vật liệu làm lồng đèn|event item)[^)]*\)","",r["name"],flags=re.I)
            clipped=re.sub(r"\s+-\s+Le hoi\s+\d{4}.*$","",clipped,flags=re.I)
            nk=key(clipped)
            if nk!=n and nk and nk not in UNSAFE and len(nk)>3:
                names[nk].append((r["icon"],r["key"],pid,clipped))
    unique={}
    for text,entries in names.items():
        icons={i for i,_,_,_ in entries}
        if len(icons)==1:
            icon=entries[0][0]
            unique[text]=(icon,entries[0][1],{literal(s) for _,_,_,s in entries})
    for phrase,icon in MANUAL.items():
        unique[key(phrase)]=(icon,None,{literal(phrase)})
    return unique,byid

def terms_for(page,tidx,cidx,base):
    out=dict(base)
    scoped=SCOPED.get((page,tidx,cidx),{})
    for phrase,icon in scoped.items():out[key(phrase)]=(icon,None,{literal(phrase)})
    return out

def match_text(raw,aliases):
    """Never infer an icon from arbitrary substrings of a longer word."""
    text=html.unescape(raw)
    norm,index=normalized(text)
    # Positions refer to raw text; HTML entities are rare in these cells.
    if text!=raw:return []
    choices=[]
    for phrase,(icon,ref,spellings) in aliases.items():
        if len(phrase)<3 and phrase not in {"tu","vo","do"}:continue
        regex=r"(?<![a-z0-9])"+re.escape(phrase).replace(r"\ ",r"\s+")+r"(?![a-z])"
        for m in re.finditer(regex,norm):
            a=index[m.start()]; b=index[m.end()-1]+1
            # Diacritic-insensitive search alone conflates trứng/trúng/trung,
            # nhẫn/nhận, etc.  A table illustration must match *actual*
            # spelling, not merely normalized phonetics.
            if literal(raw[a:b]) not in spellings:continue
            choices.append((a,b,phrase,icon,ref))
    # Earlier start, longest name, stable tie-break. Do not decorate overlaps.
    choices.sort(key=lambda r:(r[0],-(r[1]-r[0]),r[2]))
    selected=[];end=0
    for a,b,phrase,icon,ref in choices:
        if a<end:continue
        selected.append({"start":a,"end":b,"text":raw[a:b],"icon":icon,"key":ref})
        end=b
    return selected

def plan_cell(pid,tid,cid,header,inner,aliases,force=None):
    if BADHEAD.search(header.strip()):return []
    parts=nodeparts(stripped(inner))
    textidx=0;items=[];blocked=[];stack=[]
    for part in parts:
        if part.startswith("<"):
            closing=re.match(r"</([\w-]+)",part)
            opening=re.match(r"<([\w-]+)",part)
            if closing and stack:
                if stack[-1]==closing.group(1).lower():stack.pop()
            elif opening and not part.endswith("/>"):
                stack.append(opening.group(1).lower())
            continue
        if not part:continue
        if any(tag in SKIP_TAGS for tag in stack):
            textidx+=1;continue
        entries=match_text(part,terms_for(pid,tid,cid,aliases))
        if (pid,tid,cid)==("20",1,0):
            # Distinguish the actual digit tile in "VLTK 3 Tuổi" from
            # quantities such as "3 mỗi chữ" and money "3 vạn".
            for digit in re.finditer(r"\bVLTK\s+(3)\s+Tuổi\b",part,re.I):
                a,b=digit.span(1)
                entries.append({"start":a,"end":b,"text":part[a:b],
                                "icon":"letter-tile-3","key":"6,1,1754"})
        if cid==0 and header.casefold().startswith("phần thưởng thêm"):
            # "Hoàng Kim, dòng 164" is an item key, not numeric metadata.
            for gold in re.finditer(r"\bHoàng Kim,\s*dòng\s*(\d+)\b",part,re.I):
                itemkey="gold,"+gold.group(1)
                if itemkey in ID_LOOKUP:
                    a,b=gold.span()
                    entries.append({"start":a,"end":b,"text":part[a:b],
                                    "icon":ID_LOOKUP[itemkey][0],"key":itemkey})
        entries.sort(key=lambda e:(e["start"],-e["end"]))
        for e in entries:
            e["node"]=textidx
            items.append(e)
        textidx+=1
    # Reliable reward ID overrides text heuristics on the reward-name column.
    if force is not None and cid==0 and not items:
        for idx,part in enumerate(parts):
            if part.startswith("<") or not part.strip():continue
            txt=html.unescape(part)
            if re.search(r"(?i)^(?:\s*\d+\s*|\s*)?(?:danh vọng|exp|tiền|bạc|lượng)",txt):break
            at=len(part)-len(part.lstrip())
            items=[{"node":sum(1 for p in parts[:idx] if not p.startswith("<") and p),
                    "start":at,"end":at,"text":"","icon":force[0],"key":force[1]}]
            break
    # A matching name, even with duplicate aliases, gets the row's verified
    # item ID rather than a lexically similar item's ID.
    if force is not None and cid==0 and items:
        for e in items[:1]:
            e["icon"],e["key"]=force
    return items

def render(inner,marks):
    source=stripped(inner)
    parts=nodeparts(source)
    grouped=defaultdict(list)
    for e in marks:grouped[e["node"]].append(e)
    n=0
    for i,part in enumerate(parts):
        if part.startswith("<") or not part:continue
        edits=grouped.get(n,[])
        n+=1
        for e in sorted(edits,key=lambda x:x["start"],reverse=True):
            a,b=e["start"],e["end"]
            if part[a:b]!=e["text"]:raise RuntimeError("Annotation drift in table text")
            ref="" if not e["key"] else f' data-item-key="{html.escape(e["key"],quote=True)}"'
            img=(f'<img class="table-item-icon" src="../assets/item-icons/{e["icon"]}.svg"'
                 f' alt="" aria-hidden="true" loading="lazy" width="22" height="22"{ref}>')
            part=part[:a]+img+part[a:]
        parts[i]=part
    return "".join(parts)

def tables_of(document):
    return list(TABLE.finditer(document))

def table_cells(source):
    """Yields row/cell indices, headers, original cell, and verified row key."""
    headings=[html.unescape(STRIP.sub("",v)).strip() for v in TH.findall(source)]
    rownum=0
    for row in ROW.finditer(source):
        cells=list(CELL.finditer(row.group(0)))
        if not cells:continue
        # Only the explicit Mã vật phẩm column can force a source key.
        # Coordinates, quest IDs and prose numbers must never do so.
        idcols=[i for i,h in enumerate(headings)
                if h.casefold().strip().startswith("mã vật phẩm")]
        rowkeys=[m.group(0) for i in idcols if i<len(cells)
                 for m in KEY.finditer(visible_text(cells[i].group("inner")))]
        candidate=next((x for x in rowkeys if x in ID_LOOKUP),None)
        force=None if not candidate else (ID_LOOKUP[candidate][0],candidate)
        for col,c in enumerate(cells):
            head=headings[col] if col<len(headings) else ""
            yield rownum,col,head,c,force
        rownum+=1

def seed():
    global ID_LOOKUP
    base,ID_LOOKUP=catalog()
    result={}
    inventory=Counter()
    for page in sorted(PAGES.glob("[0-9][0-9].html")):
        pid=page.stem
        document=page.read_text(encoding="utf8")
        result[pid]=[]
        for tid,table in enumerate(tables_of(document)):
            inventory["tables"]+=1
            header_items=HEADER_ITEMS.get((pid,tid))
            if header_items:
                ths=list(HEADER.finditer(table.group(0)))
                if len(ths)!=len(header_items)+1:
                    raise RuntimeError(f"{pid}/{tid}: table header count drift")
                for col,(label,icon,ref) in enumerate(header_items,start=1):
                    original=stripped(ths[col].group("inner"))
                    if visible_text(original).strip()!=label:
                        raise RuntimeError(f"{pid}/{tid} header {col}: name drift")
                    if not (ASSETS/(icon+".svg")).is_file():
                        raise RuntimeError(f"Missing {icon}.svg")
                    start=len(original)-len(original.lstrip())
                    mark={"node":0,"start":start,"end":start,"text":"",
                          "icon":icon,"key":ref}
                    result[pid].append({"table":tid,"row":-1,"col":col,
                                        "sha256":digest(original),"matches":[mark]})
                    inventory["header_icons"]+=1
            for row,col,head,c,force in table_cells(table.group(0)):
                inventory["cells"]+=1
                orig=stripped(c.group("inner"))
                matches=plan_cell(pid,tid,col,head,orig,base,force)
                if not matches:continue
                for item in matches:
                    if not (ASSETS/(item["icon"]+".svg")).is_file():
                        raise RuntimeError(f"{pid}/{tid}/{row}/{col}: missing {item['icon']}")
                result[pid].append({"table":tid,"row":row,"col":col,"sha256":digest(orig),"matches":matches})
                inventory["decorated_cells"]+=1
                inventory["mentions"]+=len(matches)
    MAP.write_text(json.dumps({"schema":1,"pages":result},ensure_ascii=False,indent=2)+"\n",encoding="utf8")
    print("SEED",dict(inventory),"pages with matches",sum(bool(x) for x in result.values()))

def build(check=False):
    data=json.loads(MAP.read_text(encoding="utf8"))
    if set(data["pages"])!={p.stem for p in PAGES.glob("[0-9][0-9].html")}:raise RuntimeError("Page inventory drift")
    total=Counter()
    for pid,planned in sorted(data["pages"].items()):
        page=PAGES/(pid+".html")
        source=page.read_text(encoding="utf8")
        placements={(x["table"],x["row"],x["col"]):x for x in planned}
        used=set()
        def transform_table(t,tid):
            rowno=[0]
            def transform_row(r):
                cells=list(CELL.finditer(r.group(0)))
                if not cells:
                    headcol=[0]
                    def decorate_header(th):
                        col=headcol[0];headcol[0]+=1
                        item=placements.get((tid,-1,col))
                        orig=stripped(th.group("inner"))
                        if not item:
                            return th.group("open")+orig+th.group("close")
                        if digest(orig)!=item["sha256"]:
                            raise RuntimeError(f"{pid}/{tid}: heading {col} changed")
                        used.add((tid,-1,col))
                        total["mentions"]+=len(item["matches"])
                        return th.group("open")+render(orig,item["matches"])+th.group("close")
                    return HEADER.sub(decorate_header,r.group(0))
                row=rowno[0];rowno[0]+=1
                col=[0]
                def transform_cell(c):
                    cid=col[0];col[0]+=1
                    item=placements.get((tid,row,cid))
                    if item is None:
                        # Rebuilding a revised map must also remove annotations
                        # discarded after semantic QA (false friends, etc.).
                        return c.group("open")+stripped(c.group("inner"))+c.group("close")
                    old=stripped(c.group("inner"))
                    if digest(old)!=item["sha256"]:
                        raise RuntimeError(f"{pid}/{tid}/{row}/{cid}: underlying table cell changed")
                    for m in item["matches"]:
                        if not (ASSETS/(m["icon"]+".svg")).is_file():
                            raise RuntimeError(f"Missing {m['icon']}.svg")
                    used.add((tid,row,cid))
                    total["mentions"]+=len(item["matches"])
                    return c.group("open")+render(old,item["matches"])+c.group("close")
                return CELL.sub(transform_cell,r.group(0))
            return ROW.sub(transform_row,t)
        tid=[0]
        def change_table(m):
            i=tid[0];tid[0]+=1
            return transform_table(m.group(0),i)
        updated=TABLE.sub(change_table,source)
        if set(placements)!=used:raise RuntimeError(f"{pid}: missing planned table/row/cell IDs: {set(placements)-used}")
        if updated!=source:
            total["modified_pages"]+=1
            if not check:page.write_text(updated,encoding="utf8")
        total["pages"]+=1
    if check and total["modified_pages"]:
        raise RuntimeError(f"Not yet built: {total['modified_pages']} changed pages")
    print(("CHECK" if check else "BUILD"),dict(total))

if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--seed",action="store_true")
    args.add_argument("--check",action="store_true")
    opts=args.parse_args()
    ID_LOOKUP={}
    if opts.seed:seed()
    else:build(opts.check)
