"""Sort visible handbook entries by historical opening date, never by game ID.

The fallback keys are editorial ordering hints, not verified opening dates.
Stable event filenames, in-game IDs and all historical source text are retained.
Run from any directory; --check reports whether the current pages are ordered.
"""
import argparse
from datetime import date
from html import escape, unescape
from pathlib import Path
import re

DOCS = Path(__file__).resolve().parents[1] / "docs"
CARD = re.compile(r'<a class="event-card".*?</a>', re.S)
GROUP = re.compile(r'<section class="timeline-year">.*?</section>', re.S)
ROW = re.compile(r'<div class="timeline-row">.*?(?=<div class="timeline-row">|</section>)', re.S)
PREV = re.compile(r'<div class="nextprev">.*?</div>', re.S)
DATE = re.compile(r'^(\d{1,2})/(\d{1,2})/(\d{4})')
HINTS = {
    1: (2006, 2, 1, "Báo chí 01/02/2006"),
    12: (2005, 5, 1, "Dịp Quốc tế Lao động"),
    13: (2006, 6, 8, "Báo chí 08/06/2006"),
    9: (2006, 8, 1, "Dịp Vu Lan"),
    14: (2006, 9, 2, "Dịp Quốc khánh"),
    16: (2007, 6, 1, "Dịp sinh nhật Võ Lâm"),
    26: (2007, 9, 2, "Dịp Quốc khánh"),
    19: (2008, 2, 1, "Dịp Tết"),
    22: (2008, 2, 1, "Dịp Tết"),
    33: (2008, 4, 30, "Dịp 30/4"),
    34: (2008, 4, 30, "Dịp 30/4"),
    62: (2007, 4, 30, "Dịp 30/04/2007"),
    63: (2006, 12, 25, "Dịp 25/12/2006"),
}
NOTE = ('<p class="player-notice" id="chronology-note">Danh mục xếp theo mốc mở hoặc mốc tham chiếu lịch sử. '
        'Số thứ tự (STT) trong Lệnh bài khớp cẩm nang; ID # vẫn là mã kỹ thuật cố định. '
        'Nếu chưa rõ ngày mở, xếp theo dịp lễ hoặc cuối năm; thứ tự này không khẳng định ngày tổ chức chính thức.</p>')
GUIDE_NOTE = ('<p id="chronology-note">Danh sách và dòng thời gian dùng STT theo mốc lịch sử. '
              'ID # của sự kiện và đường dẫn bài viết không đổi; tìm trong game theo STT hoặc tên. '
              'Các dịp lễ chưa có ngày mở xác minh chỉ là căn cứ xếp gần đúng.</p>')


def one(pattern, text):
    matches = list(re.finditer(pattern, text, re.S))
    assert len(matches) == 1, (pattern, len(matches))
    return matches[0]


def load(path):
    return path.read_bytes().decode("utf-8")


def entry_id(text):
    return int(one(r'href="events/(\d+)\.html"', text)[1])


def replace_region(text, parts, replacement):
    old = "".join(parts)
    assert old and text.count(old) == 1
    return text.replace(old, replacement, 1)


def build():
    index, history, guide = [load(DOCS / n) for n in ("index.html", "history.html", "guide.html")]
    cards = CARD.findall(index)
    groups = GROUP.findall(history)
    rows = [row for group in groups for row in ROW.findall(group)]
    by_id = {entry_id(c): c for c in cards}
    by_row = {entry_id(r): r for r in rows}
    assert len(by_id) == len(cards) == len(rows) == len(by_row)
    assert set(by_id) == set(by_row)
    entries = {}
    for id, card in by_id.items():
        page = DOCS / "events" / f"{id:02}.html"
        article = load(page)
        title = unescape(one(r'<h1>(.*?)</h1>', article)[1])
        header = one(r'<div class="article-header"><div class="eyebrow">(.*?)</div>', article)[1]
        edition = int(header[:4])
        start = unescape(one(r'<div class="date-grid"><div><small>.*?</small><strong>(.*?)</strong>', article)[1])
        match = DATE.match(start)
        if id == 2:
            key, label, group = (9999, 12, 31, id), "Biến thể cộng đồng · chưa rõ niên đại", "Biến thể cộng đồng"
        elif id in (62, 63):
            y, m, d, hint = HINTS[id]
            key, label, group = (y, m, d, id), hint + " · chưa rõ ngày mở", str(y)
        elif match:
            d, m, y = map(int, match.groups())
            date(y, m, d)
            key, label, group = (y, m, d, id), start, str(y)
        elif id in HINTS:
            y, m, d, hint = HINTS[id]
            key, label, group = (y, m, d, id), hint + " · chưa rõ ngày mở", str(y)
        else:
            key, label, group = (edition, 13, 1, id), "Chưa rõ ngày mở", str(edition)
        entries[id] = dict(page=page, article=article, title=title, key=key, label=label, group=group)
    order = sorted(entries, key=lambda id: entries[id]["key"])
    out = {}
    sorted_cards, sorted_groups = [], {}
    for i, id in enumerate(order, 1):
        e = entries[id]
        num = f"{i:02}"
        card = by_id[id]
        meta = one(r'<div class="card-meta"><span>.*?</span>', card)
        season = one(r'data-season="([^"]*)"', card)[1]
        year = "Cộng đồng" if id == 2 else e["group"]
        card = card[:meta.start()] + f'<div class="card-meta"><span>STT {num} · {year} · {season}</span>' + card[meta.end():]
        card = re.sub(r' data-year="[^"]*"', f' data-year="{year}"', card, count=1)
        card = re.sub(r' data-event-id="[^"]*"', '', card, count=1)
        card = card.replace('<a class="event-card"', f'<a class="event-card" data-event-id="{id:02}"', 1)
        card = re.sub(r'<small class="event-date">.*?</small>', '', card, flags=re.S)
        card = card.replace('</h2>', f'</h2><small class="event-date">{escape(e["label"])} · ID #{id:02}</small>', 1)
        # Moving the multiline search attribute can expose pre-existing trailing
        # blanks as new diff lines; they carry no search meaning.
        sorted_cards.append(re.sub(r'[ \t]+(?=\r?$)', '', card, flags=re.M))
        row = by_row[id]
        row = re.sub(r'(<a href="events/\d+\.html"><strong>)(?:\d+\. )?', rf'\g<1>{num}. ', row, count=1)
        row = re.sub(r'<small class="timeline-id">.*?</small>', '', row, flags=re.S)
        row = row.replace('</strong></a>', f'</strong></a><small class="timeline-id">ID #{id:02}</small>', 1)
        sorted_groups.setdefault(e["group"], []).append(row)
        article = e["article"]
        crumb = one(r'<div class="crumb">.*?</div>', article)
        replacement = re.sub(r' / (?:STT \d+ · ID #|#)\d+</div>$', f' / STT {num} · ID #{id:02}</div>', crumb[0])
        assert replacement != crumb[0] or f'STT {num} · ID #{id:02}' in crumb[0]
        article = article[:crumb.start()] + replacement + article[crumb.end():]
        head = one(r'<div class="article-header"><div class="eyebrow">.*?</div>', article)
        replacement = re.sub(r' · (?:SỰ KIỆN \d+|STT \d+ · ID #\d+)</div>$', f' · STT {num} · ID #{id:02}</div>', head[0])
        assert f'STT {num} · ID #{id:02}' in replacement
        article = article[:head.start()] + replacement + article[head.end():]
        prev_id = order[i-2] if i > 1 else None
        next_id = order[i] if i < len(order) else None
        left = f'<a href="{prev_id:02}.html">← {escape(entries[prev_id]["title"], quote=False)}</a>' if prev_id else '<a href="../index.html">← Danh sách</a>'
        right = f'<a href="{next_id:02}.html">{escape(entries[next_id]["title"], quote=False)} →</a>' if next_id else '<a href="../index.html">Về danh sách →</a>'
        assert len(PREV.findall(article)) == 1
        article = PREV.sub(lambda _: '<div class="nextprev">' + left + right + '</div>', article)
        out[e["page"]] = article
    index = replace_region(index, cards, "".join(sorted_cards))
    index = re.sub(r'<p class="player-notice" id="chronology-note">.*?</p>', '', index, flags=re.S)
    index = index.replace('<div class="filters">', NOTE + '<div class="filters">', 1)
    if 2 in entries and '<option>Cộng đồng</option>' not in index:
        index = index.replace('<option>2010</option></select>', '<option>2010</option><option>Cộng đồng</option></select>', 1)
    elif 2 not in entries:
        index = index.replace('<option>Cộng đồng</option>', '')
    history = replace_region(history, groups, ''.join(f'<section class="timeline-year"><h2>{escape(group)}</h2>'+''.join(rs)+'</section>' for group, rs in sorted_groups.items()))
    history = history.replace('xếp theo năm.', 'xếp theo mốc mở hoặc mốc tham chiếu lịch sử.')
    history = re.sub(r'<p class="player-notice" id="chronology-note">.*?</p>', '', history, flags=re.S)
    history = history.replace('<section class="timeline-year">', NOTE + '<section class="timeline-year">', 1)
    guide = re.sub(r'<p id="chronology-note">.*?</p>', '', guide, flags=re.S)
    guide = guide.replace('<h2 id="nguon">Nguồn tư liệu và giới hạn</h2>', '<h2 id="nguon">Nguồn tư liệu và giới hạn</h2>' + GUIDE_NOTE, 1)
    assert GUIDE_NOTE in guide
    out.update({DOCS/"index.html": index, DOCS/"history.html": history, DOCS/"guide.html": guide})
    return out, order


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    output, order = build()
    changes = [p for p, content in output.items() if load(p) != content]
    if args.check:
        assert not changes, [str(p) for p in changes]
    else:
        for p in changes:
            p.write_bytes(output[p].encode("utf-8"))
    print(f"{len(order)} entries, {len(changes)} changed pages; order: " + ", ".join(map(str, order)))
