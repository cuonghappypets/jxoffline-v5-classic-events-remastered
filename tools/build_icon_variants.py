#!/usr/bin/env python3
"""Derive distinctive grade/filling/color variants from our CC0 original SVGs.

Never includes or redistributes client sprites. No third-party libraries.
Generated SVGs are committed so GitHub Pages works without a build server.
"""
from pathlib import Path
import re
import xml.etree.ElementTree as ET

ASSETS = Path(__file__).resolve().parents[1] / "docs" / "assets" / "item-icons"
MADE = []

def variant(source, output, replacements=(), overlay="", title=None):
    raw = (ASSETS / (source + ".svg")).read_text(encoding="utf8")
    for old, new in replacements:
        if old not in raw:
            raise ValueError(f"{source} missing expected palette {old}")
        raw = raw.replace(old, new)
    if overlay:
        if "</g>" not in raw: raise ValueError(f"{source}: no icon foreground")
        raw = raw.replace("</g>", overlay + "</g>", 1)
    if title:
        raw = re.sub(r'<title>[^<]*</title>',f'<title>{title}</title>',raw,count=1)
        raw = re.sub(r'aria-label="[^"]+"',f'aria-label="{title}"',raw,count=1)
    if "CC0-1.0" not in raw: raise ValueError("Missing original-art SPDX marker")
    ET.fromstring(raw)
    target=ASSETS/(output + ".svg")
    target.write_text(raw,encoding="utf8")
    MADE.append(output)

# Pastry variants preserve one common 64px silhouette while changing filling.
motifs = {
    "lotus": ('#e9bb74', '#dfd6a0', '<g fill="#fef7d4" stroke="#916d54" stroke-width="1.2"><ellipse cx="32" cy="26" rx="4" ry="7"/><ellipse cx="32" cy="38" rx="4" ry="7"/><ellipse cx="26" cy="32" rx="7" ry="4"/><ellipse cx="38" cy="32" rx="7" ry="4"/></g><circle cx="32" cy="32" r="3" fill="#cf9f40"/>'),
    "egg": ('#e4a759', '#f8eec8', '<circle cx="32" cy="32" r="9" fill="#f6ead4" stroke="#b07935" stroke-width="1.8"/><circle cx="32" cy="32" r="5" fill="#e6a33b"/>'),
    "bean": ('#d3ad68', '#d5da8c', '<ellipse cx="32" cy="32" rx="9" ry="7" fill="#779d59" stroke="#58753f" stroke-width="2"/><path d="M26 32Q32 38 39 29" fill="none" stroke="#dbe6a0" stroke-width="2"/>'),
    "meat": ('#dba268', '#f0d0a4', '<circle cx="32" cy="32" r="9" fill="#a7563d" stroke="#7d3b2a" stroke-width="2"/><path d="M27 33Q32 26 37 33T28 37" fill="none" stroke="#f6c6a1" stroke-width="2"/>'),
    "taro": ('#c9a0ce', '#e6d3e8', '<circle cx="32" cy="32" r="9" fill="#a37cae" stroke="#805b8b" stroke-width="2"/><path d="M28 27L37 37M37 27L28 37" stroke="#e8c7ee" stroke-width="2"/>'),
    "special": ('#e6b85d', '#fff2c0', '<circle cx="32" cy="32" r="10" fill="#a94b3a" stroke="#f5cd67" stroke-width="2"/><path d="m32 23 2.4 6 6.6.4-5.1 4 1.7 6.4-5.6-3.7-5.6 3.7 1.7-6.4-5.1-4 6.6-.4Z" fill="#ffe39a"/>'),
    "pig": ('#e7b870', '#f8d8b6', '<circle cx="32" cy="32" r="10" fill="#e7a1a6" stroke="#a75d69" stroke-width="1.5"/><path d="M22 28L19 24 20 35M42 28l3-4-1 11" stroke="#a75d69" fill="#e7a1a6" stroke-width="2"/><ellipse cx="32" cy="35" rx="5" ry="3" fill="#f8c0bc"/><circle cx="30" cy="35" r="1" fill="#9b5260"/><circle cx="34" cy="35" r="1" fill="#9b5260"/><circle cx="27" cy="29" r="1" fill="#513934"/><circle cx="37" cy="29" r="1" fill="#513934"/>'),
    "peach": ('#e8b980', '#f5c9a2', '<path d="M32 23C22 18 18 30 25 37Q31 45 32 42Q33 45 39 37Q46 30 32 23Z" fill="#db957b" stroke="#9a634f" stroke-width="1.8"/><path d="M31 24Q32 20 37 20" stroke="#769455" stroke-width="2.2" fill="none"/>'),
}
for label, (base_color, middle, mark) in motifs.items():
    variant("mooncake", "mooncake-"+label,
            (("#e9b764",base_color),("#f4d08c",middle)),mark,
            "Mooncake: "+label+" filling illustration")

variant("banh-chung","banh-chung-mixed",(),
        '<circle cx="32" cy="34" r="7" fill="#e8ca85" stroke="#8e673d" stroke-width="2"/><circle cx="30" cy="33" r="2" fill="#b75e3e"/><circle cx="35" cy="36" r="2" fill="#789c47"/>',
        "Banh chung mixed filling")
variant("banh-chung","banh-chung-premium",(),
        '<path d="M25 35l5 5 10-12" fill="none" stroke="#f6d578" stroke-width="4"/><circle cx="50" cy="14" r="6" fill="#d7b456" stroke="#885d28" stroke-width="1.5"/>',
        "Premium banh chung")
variant("banh-tet","banh-tet-bean",
        (('fill="#d6a66c"','fill="#e8c559"'),),
        '<ellipse cx="32" cy="53" rx="2" ry="2" fill="#e5d27c"/>',
        "Banh tet bean filling")
variant("banh-tet","banh-tet-mixed",
        (('fill="#d6a66c"','fill="#ad7048"'),),
        '<circle cx="29" cy="52" r="1.4" fill="#d6c067"/><circle cx="34" cy="55" r="1.4" fill="#a34d3c"/>',
        "Banh tet mixed filling")

for shade, body, lid in [
    ("white","#f5eee1","#fff9ec"),("gold","#d9aa4c","#efcb70"),("green","#679d73","#9cc5a1")
]:
    variant("gift-box","gift-box-"+shade,(("#cb6d69",body),("#e88c7d",lid)),title="Gift box: "+shade)

for shade, face, side, stroke in [
    ("blue","#8fe0eb","#3696b5","#307f9d"),
    ("green","#92d5a2","#4e9c6e","#3c805e"),
    ("red","#f3a6ab","#cc596b","#ac455b"),
    ("purple","#cbafe9","#8764bc","#695199"),
    ("gold","#efcf79","#c99b3c","#9e7836"),
    ("rainbow","#e5bce1","#7eafdd","#976b9a"),
]:
    variant("crystal","crystal-"+shade,
            (("#8fe0eb",face),("#3696b5",side),("#307f9d",stroke)),
            title="Crystal: "+shade)

for shade, color in [("ruby","#a93854"),("amber","#d5a34c")]:
    variant("ring","ring-"+shade,(("#a85563",color),),title="Ring with "+shade+" gem")

for grade, val, face in [
    ("small","I","#9ec89c"),("medium","II","#e5c376"),("large","III","#db8c71")
]:
    variant("potion-bottle","potion-"+grade,(),
            f'<circle cx="49" cy="13" r="10" fill="{face}" stroke="#87683f" stroke-width="1.8"/>'
            f'<text x="49" y="16.4" text-anchor="middle" font-family="Georgia,serif" font-weight="700" font-size="10" fill="#443529">{val}</text>',
            "Potion "+grade)

for season, body in [
    ("spring","#9dbb6f"),("summer","#d9ad69"),
    ("autumn","#c18b69"),("winter","#80a9c5")
]:
    variant("bag","bag-"+season,(("#c79a66",body),),title="Festive pouch "+season)

sparkle='<path d="m52 8 1.8 5.7L60 16l-6.2 2.3L52 24l-2-5.7L44 16l6-2.3Z" fill="#f3ca65" stroke="#9e6e36" stroke-width="1.5"/>'
for shape in ("butterfly","carp","revolving","star","round","tube"):
    variant("lantern-"+shape,"lantern-"+shape+"-special",(),sparkle,
            "Premium lantern: "+shape)

variant("cake","cake-special",(),
        '<path d="m48 7 2 6 6 2-6 2-2 6-2-6-6-2 6-2Z" fill="#edc85d" stroke="#ac7e39" stroke-width="1"/>',
        "Premium celebration cake")

# Lantern craft paper: the named color must match the illustration.
for shade, face in [
    ("yellow","#e6c34f"), ("blue","#73afd3"), ("green","#8eb86f"),
    ("red","#d8796b"), ("orange","#e9a45a")
]:
    variant("paper","paper-"+shade,(("#e2d17f",face),),
            title="Colored lantern paper: "+shade)

# Tiểu/Trung/Đại pills share one silhouette with clear grade badges.
for grade, rank, face in [
    ("small","I","#95bf8a"),("medium","II","#e4c477"),
    ("large","III","#df9e72")
]:
    variant("pill","pill-"+grade,(),
            f'<circle cx="50" cy="14" r="10" fill="{face}" stroke="#875c37" stroke-width="1.5"/>'
            f'<text x="50" y="17" text-anchor="middle" font-family="Georgia,serif" font-size="9" font-weight="700" fill="#433628">{rank}</text>',
            "Pill grade "+grade)

# Collectibles are fragments, not complete weapons or a completed picture.
# Keep color/shape cues to the source family without presenting a full item.
for label, border, face in [
    ("small","#876e55","#e7c991"),("large","#6b788d","#c5cedb")
]:
    variant("paper","fragment-"+label,
            (("#9a6861",border),("#e2d17f",face)),
            '<path d="m23 24 9 3 4-6 7 7-6 5 4 10-12 2-5-8-9-2Z" fill="#fff9e5" stroke="#9d8058" stroke-width="1.8"/>',
            "Collectible "+label+" fragment")
for theme, face in [("traveler","#8bbba9"),("immortal","#b5a3ce")]:
    for part in range(1,7):
        variant("paper","picture-"+theme+"-"+str(part),
                (("#e2d17f",face),),
                '<path d="M22 24l10-4 8 6-4 10-10 6-8-8Z" fill="#fff3d0" stroke="#806e77" stroke-width="1.7"/>'
                f'<circle cx="{23+part*3}" cy="{27+(part%3)*4}" r="3" fill="#ba8059"/>',
                f"Picture puzzle fragment {theme} {part}")
for part in range(1,5):
    variant("flag","flag-piece-"+str(part),(),
            f'<path d="M{16+part*3} 22l10-2 7 10-7 12-9-6Z" fill="#f1dcb4" stroke="#865846" stroke-width="2"/>',
            "Flag fragment "+str(part))

# Material rankings: the same ancient plaque silhouette in five substances.
for material, face in [
    ("wood","#987443"),("copper","#bd8b5b"),
    ("silver","#d3d9e2"),("gold","#e8c15c"),("jade","#84b6a2")
]:
    variant("talisman","plaque-"+material,
            (("#f7d778",face),),
            title="Material plaque "+material)

# Eight-letter festive tokens share a tiled physical form. Individual names
# stay as labels, while a small Roman index distinguishes positions at 32px.
for n in range(1,9):
    variant("paper","letter-tile-"+str(n),(),
            f'<circle cx="49" cy="14" r="9" fill="#ce9d62" stroke="#86623e" stroke-width="1.5"/>'
            f'<text x="49" y="17" text-anchor="middle" font-size="9" font-family="Georgia,serif" fill="#fff8e5">{n}</text>',
            "Festival character tile "+str(n))

# These are original simple silhouettes, not copied client sprites.
variant("mooncake","peach-bun-bean",(),
        '<path d="M22 36Q13 23 29 18l4-7 5 8q16 9 1 28Q32 56 22 36Z" fill="#f0bea3" stroke="#b87968" stroke-width="2.5"/>'
        '<path d="M32 17q6-10 14-5" fill="none" stroke="#699057" stroke-width="2.5"/>'
        '<circle cx="32" cy="37" r="4.5" fill="#91a95c"/>',
        "Longevity peach bun with bean filling")
variant("mooncake","peach-bun-date",(),
        '<path d="M22 36Q13 23 29 18l4-7 5 8q16 9 1 28Q32 56 22 36Z" fill="#f0bea3" stroke="#b87968" stroke-width="2.5"/>'
        '<path d="M32 17q6-10 14-5" fill="none" stroke="#699057" stroke-width="2.5"/>'
        '<circle cx="32" cy="37" r="4.5" fill="#a9554a"/>',
        "Longevity peach bun with jujube filling")

# Fashion accessories #46 need their own actual silhouettes.
variant("mirror","lipstick",(),
        '<path d="M24 48V27h16v21Z" fill="#d9aa6b" stroke="#875d45" stroke-width="2.5"/>'
        '<path d="M25 27V18l12-8 3 9v8Z" fill="#bb4e62" stroke="#83364c" stroke-width="2.5"/>',
        "Lipstick")
variant("mirror","hairclip",(),
        '<path d="M11 34Q32 15 53 34Q32 52 11 34Z" fill="#e1b66c" stroke="#875f3e" stroke-width="3"/>'
        '<path d="M20 33L28 25 36 33 44 25" fill="none" stroke="#fce7b9" stroke-width="2"/>',
        "Decorative hair clip")
variant("mirror","comb",(),
        '<rect x="13" y="20" width="38" height="10" rx="3" fill="#ad764a" stroke="#714c36" stroke-width="2"/>'
        '<path d="M17 30v22m5-22v22m5-22v22m5-22v22m5-22v22m5-22v22m5-22v22" stroke="#895b3f" stroke-width="3"/>',
        "Hair comb")

# Three firecracker sizes, with an optional festive gold spark.
for size, badge in [
    ("small","I"),("medium","II"),("large","III")
]:
    for extra in (False,True):
        name="firecracker-"+size+("-special" if extra else "")
        variant("firecracker",name,(),
                f'<circle cx="49" cy="13" r="10" fill="#e7c277" stroke="#ad7944" stroke-width="1.5"/>'
                f'<text x="49" y="16" text-anchor="middle" font-family="Georgia,serif" font-size="8" font-weight="700" fill="#604529">{badge}</text>'
                + ('<path d="m13 11 2 4 5 1-5 2-2 4-2-4-5-2 5-1Z" fill="#f8e3a2"/>' if extra else ""),
                "Firecracker "+size+(" special" if extra else ""))

for color, tint in [("yellow","#dfc35c"),("purple","#a588c7"),("green","#79ae82")]:
    variant("snowman","snowman-"+color,(("#c86461",tint),),title="Snowman "+color)
variant("gift-box","gift-box-blue",
        (("#cb6d69","#5c9ac5"),("#e88c7d","#8fbed7")),
        title="Blue gift box")
variant("pendant","pendant-amber",
        (("#83b9a0","#daa65a"),("#c9e5ba","#f0d78c")),
        title="Amber-yellow jade pendant")
variant("potion-bottle","potion-special",(),
        '<path d="m51 7 2 5 5 2-5 2-2 5-2-5-5-2 5-2Z" fill="#f8d689" stroke="#9a7046" stroke-width="1"/>',
        "Special restorative potion")

# Ball assembly parts are NOT a completed soccer ball.
variant("ball","ball-gold",
        (("#faf3df","#f0d080"),("#526c82","#c3913b")),
        title="Gold football")
variant("ball","ball-shell",(),
        '<path d="M17 42Q32 28 47 42" fill="none" stroke="#e5bf78" stroke-width="7"/>'
        '<path d="M18 43Q32 32 45 43" fill="none" stroke="#9b704a" stroke-width="2"/>',
        "Football outer shell")
variant("ball","ball-bladder",(),
        '<ellipse cx="32" cy="33" rx="18" ry="13" fill="#b6a3a0" stroke="#71675d" stroke-width="3"/>'
        '<path d="m36 20 3-6" stroke="#71675d" stroke-width="3"/>',
        "Ball rubber bladder")
variant("flower","seed",(),
        '<path d="M13 46Q32 21 51 46Q32 59 13 46Z" fill="#b18252" stroke="#75563b" stroke-width="3"/>'
        '<path d="M32 39q0-13 9-17" fill="none" stroke="#66904d" stroke-width="3"/>',
        "Plant seed")
variant("flower","sapling",(),
        '<path d="M32 53V29M32 34Q19 18 14 30Q18 43 32 39M32 32Q44 17 51 28Q48 41 32 38" fill="#8bb96c" stroke="#4c814d" stroke-width="3"/>',
        "Young sapling")
variant("bag","ingredient-sack",(),
        '<path d="M17 29h30l4 23H13Z" fill="#dbc69e" stroke="#876c4d" stroke-width="3"/>'
        '<path d="M22 33h20M20 42h24" stroke="#a99161" stroke-width="2"/>',
        "Raw ingredient sack")
variant("potion-bottle","milk-bottle",(),
        '<rect x="22" y="22" width="20" height="29" rx="4" fill="#fffaf0" stroke="#9cb0b1" stroke-width="2.5"/>'
        '<path d="M25 19h14" stroke="#8ea7b1" stroke-width="4"/>',
        "Milk bottle")
variant("package","yeast-starter",(),
        '<rect x="19" y="28" width="27" height="22" rx="5" fill="#e0bc83" stroke="#977248" stroke-width="3"/>'
        '<circle cx="29" cy="35" r="3" fill="#c38b55"/><circle cx="38" cy="43" r="2.5" fill="#a8794c"/>',
        "Yeast starter")
variant("potion-bottle","wine-gourd",(),
        '<path d="M31 11q-9 5-3 14-17 6-14 21 3 12 18 12 19 0 19-16 0-12-15-17 5-11-5-14Z" fill="#c29360" stroke="#835f3b" stroke-width="3"/>'
        '<path d="M22 38h20" stroke="#e5c98c" stroke-width="3"/>',
        "Wine gourd")
variant("potion-bottle","water-bucket",(),
        '<path d="M17 27h30l-4 28H21Z" fill="#b98b5c" stroke="#7b5a3f" stroke-width="3"/>'
        '<path d="M21 27q0-21 11-21t11 21" fill="none" stroke="#8b765d" stroke-width="4"/>'
        '<path d="M19 30h26" stroke="#90bdc9" stroke-width="3"/>',
        "Water bucket")
variant("talisman","signal-horn",(),
        '<path d="M13 43l28-23 10-2-4 26-24 8Z" fill="#d1af67" stroke="#89653b" stroke-width="3"/>'
        '<path d="M23 43l-7 9" stroke="#89653b" stroke-width="4"/>',
        "Signal horn")
variant("hat","bucket-hat",(),
        '<path d="M17 29Q20 11 32 11T47 29l7 15Q32 53 10 44Z" fill="#718e67" stroke="#405e45" stroke-width="3"/>'
        '<path d="M13 42Q32 47 51 42" stroke="#d0d7aa" stroke-width="3"/>',
        "Soft bucket hat")
for shade, tint in [
    ("peace","#779d7c"),("freedom","#8ba6ba"),
    ("happiness","#d5a96e"),("soldier","#718765")
]:
    variant("hat","soft-hat-"+shade,
            (("#506f93",tint),),
            '<path d="M12 41Q32 49 52 41" fill="none" stroke="#8e7754" stroke-width="3"/>',
            "Soft event hat "+shade)

print("Built",len(MADE),"original-art SVG variants")
