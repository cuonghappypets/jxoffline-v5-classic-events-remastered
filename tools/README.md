# CGPT handbook item illustrations

This is the **public, reproducible icon layer** for the 61-event player
handbook in `docs/`. It does not modify addon code, reward values or prose.

## Data and provenance

- `item_icon_map.json` is the committed, ordered map of **575 visible cards** to
  their client-004 reference key, display name and selected original SVG family.
  There are 390 distinct labels and 400 different referenced item keys. The
  distinction matters: names repeat, especially the three `Free Item` cards.
- `../docs/assets/item-icons/*.svg` contains 64 original CGPT family
  illustrations and 37 deterministic color/filling/grade variants. These are
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
python tools/item_icons.py --check
python tools/qa_item_icons.py
```

The illustrator maps each card to a local SVG **statically**, without remote
requests or JavaScript dependency. The converter refuses to proceed if any
display name or card count differs from its versioned source map, or if an SVG
is missing. Running it again produces no further HTML edits. Unlike the former
runtime emoji/category heuristic, exact item keys can disambiguate duplicate
names within and across events.

`python tools/item_icons.py --reclassify` reapplies the classifier to the
committed source map after an intentional classifier change. Inspect the diff
to catch false matches before using this. In the authorized **private**
workspace only, `--seed` recreates the map from source item catalogs; do not
run this while other editors are changing the handbook and do not commit
private catalog assets.

Optional browser QA (Playwright Python + Edge installed):

```powershell
python tools/qa_item_icons.py --browser
```

Browser mode checks search, theme, image decoding, overflow and representative
pages (#01, #02, #20, #35, #48, #59) on desktop/mobile and writes private QA
screenshots to `05_HANDBOOK/qa`. Static QA scans **all 61 pages**, **575 cards**
and all local assets; it compares prose to the Git HEAD after removing
decorative icon markup. It also checks representative semantic mappings for
Huyền Tinh, bí kíp and An Bang / Định Quốc equipment slots.

## Limits

These are readable, stylized **illustrations**, not pixel-perfect captures
of an individual's in-game item inventory. Assets of uncertain publication
rights were intentionally not copied from the client or historical archive.
Where the underlying game table only says `Free Item`, icon choices are
disambiguated by item keys in page order; the unchanged textual label remains
as in the existing handbook. Art-specific errors should be corrected in the
mapping or original SVG source, then rebuilt and visually verified.
