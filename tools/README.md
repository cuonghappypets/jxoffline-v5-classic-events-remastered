# CGPT handbook item illustrations

This is the **public, reproducible icon layer** for the 61-event player
handbook in `docs/`. It does not modify addon code, reward values or prose.

## Data and provenance

- `item_icon_map.json` is the committed, ordered map of **575 visible cards** to
  their client-004 reference key, display name and selected original SVG family.
  There are 390 distinct labels and 400 different referenced item keys. The
  distinction matters: names repeat, especially the three `Free Item` cards.
- `../docs/assets/item-icons/*.svg` contains original CGPT family
  illustrations and deterministic color/filling/grade variants. These are
  **original artwork released as CC0-1.0**, including the metadata in each SVG,
  not extracted client sprites or images from old VNG websites.
- A matching client-004 item key is an identification aid, **not** proof that
  the drawn SVG is the original sprite. The handbook explicitly labels the art
  as illustrative. No third-party artwork is redistributed.
- The original local `05_HANDBOOK/sources/events.json` and
  `item_icons.json` were consulted once to seed the ordered public map; those
  private catalog/source files **are not a build dependency** and are not
  copied into the public repository.

## Repeatable build

Run from the public repository root, with Python 3:

```powershell
python tools/build_icon_variants.py
python tools/item_icons.py
python tools/table_item_icons.py
python tools/item_icons.py --check
python tools/table_item_icons.py --check
python tools/qa_item_icons.py
python tools/qa_table_icons.py
```

The illustrator maps each card to a local SVG **statically**, without remote
requests or JavaScript dependency. The converter refuses to proceed if any
display name or card count differs from its versioned source map, or if an SVG
is missing. Running it again produces no further HTML edits. Unlike the former
runtime emoji/category heuristic, exact item keys can disambiguate duplicate
names within and across events.

### Item icons inside tables

`table_icon_map.json` is the **reviewable source of truth** for the additional
table decorations across all 61 event HTML files. It inventories 108 tables,
including item-rich editorial tables, complex crafting formulas, reward
tables and deliberate non-item tables. Each decoration carries its page,
table/row/column, literal text span, original-cell SHA256, illustration
family and an item reference key *only when supported*. The generator is
standard-library Python; no website runtime matching or private sprite
dependency is needed.

`table_item_icons.py` replays that manifest into HTML without altering
numbers, formulas, text, source IDs, inline formatting, external links or
gameplay. It preserves intact non-item rows (NPC/map coordinates, EXP
thresholds, rates), ignores client-name `<small>` metadata, and supports
multiple separate ingredients in one cell. The tool refuses edits to
underlying table text until the manifest has been deliberately reviewed
and rebuilt. Re-running the normal command is idempotent.

When the source table text changes intentionally, regenerate **and review**
the new manifest using:

```powershell
python tools/table_item_icons.py --seed
python tools/table_item_icons.py
python tools/table_item_icons.py --check
python tools/qa_table_icons.py
```

The `--seed` command is **not** part of the ordinary build and should not
run automatically on GitHub Pages. It uses the public card map and explicit
table-column aliases; diacritics are compared exactly to prevent errors such
as `trứng/trúng` or `nhẫn/nhận`. Unverified reward IDs are not silently
converted into source keys. Any added SVG must be original/appropriately
licensed with its provenance declared.

`python tools/item_icons.py --reclassify` reapplies the classifier to the
committed source map after an intentional classifier change. Inspect the diff
to catch false matches before using this. In the authorized **private**
workspace only, `--seed` recreates the map from source item catalogs; do not
run this while other editors are changing the handbook and do not commit
private catalog assets.

Optional browser QA (Playwright Python + Edge installed):

```powershell
python tools/qa_item_icons.py --browser
python tools/qa_table_icons.py --browser
```

Browser mode checks search, theme, image decoding, overflow and representative
pages (#01, #02, #20, #35, #48, #59) on desktop/mobile and writes private QA
screenshots to `05_HANDBOOK/qa`. Static QA scans **all 61 pages**, **575 cards**
and all local assets; it compares prose to the Git HEAD after removing
decorative icon markup. It also checks representative semantic mappings for
Huyền Tinh, bí kíp and An Bang / Định Quốc equipment slots.
Table browser QA additionally exercises crafting, item drops, rewards and
eight collectible-letter column headers on desktop (1366 px), mobile
(390 px) and compact mobile (320 px). Wide tables scroll *within their
container* rather than crushing item labels into vertical characters.

## Limits

These are readable, stylized **illustrations**, not pixel-perfect captures
of an individual's in-game item inventory. Assets of uncertain publication
rights were intentionally not copied from the client or historical archive.
Where the underlying game table only says `Free Item`, icon choices are
disambiguated by item keys in page order; the unchanged textual label remains
as in the existing handbook. Art-specific errors should be corrected in the
mapping or original SVG source, then rebuilt and visually verified.
