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

print("Built",len(MADE),"original-art SVG variants")
