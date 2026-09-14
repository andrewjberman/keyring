# DSGN_REBRND round 2 -- card texture and the light-mode inversion: what was, what is, what it implies

**Asked by:** Andrew-direct ~18:1xZ 2026-09-14 at the `2.0.0_SA_COO~D` terminal (record @e7051143e2):
*"look into that request i made before ... diff the current changes to component color ... with the original request
... hex+opacity"* and *"establish the implications"* of the light-mode inversion.
**By:** `2.0.0_SA_COO~D`.
**Feeds:** `1.0.0_SA_CTO`'s round-2 PRD addendum, then this seat's recut.
**Every number is measured.** Instruments: `git grep` at the refs named; native Grep and Read on the feature worktree
@a1d0a7451c (portal @086371dd).

## 0. The two earlier words this answers

- **The hex+opacity request** is Andrew's correction of 2026-09-11, recorded in commit `401ad3b961`: *"consolidating is
  not flattening. Flattening removes the ability to direct the eye to a subheader or a panel title and leaves
  everything flat."* His method: diff RB-s-3's colour edits against the prior state to recover a MAP of what was at
  what colour/opacity. That map is `design/brand/portal-layer-map.json`. His forward rule was ONE opacity. The ladder
  proposed from it is `design/brand/portal-opaque-ladder.json`.
- **The inversion** is his word of 2026-09-11 (commit `1bedb59788`): *"broadly establishing A but with a defined logic
  from outset on how you want to invert the hex+opacity diffs from light on dark to dark on light."* That logic is
  `design/brand/inversion-rule.json`: preserve the contrast RATIO and the ROLE, re-derive the value, opacity 1.0.

## 1. TEXTURE -- what the variants were, and what is left

### What a panel WAS (portal @748384e4, before the flattening)

A panel was a STACK of distinct planes:

| plane | token | value | carriers |
|---|---|---|---|
| title strip, fixed rows, sidebar | `--bg-header` = `--navy-dark` | ~11% lightness | 491 uses; `PanelHeader`, `DarkCard` |
| content body (Panel `chart`/`mixed`) | `--semantic-background-contentPanel` | `hsl(221 28% 25%)` | the Panel default |
| nested tiles, stat tiles | `--bg-medium` / `--navy-medium` | ~13% | `NestedCard` |
| content areas, chart containers | `--bg-card` = `--navy-light` | ~14% (the layer map measures `#2E3952`) | 33 uses |
| tooltip | `--bg-tooltip` = `--navy-tooltip` | `#0E1525` | 4 uses |
| input / hover / hover-light | own tokens | `#18243E` / `#1B2946` / lighter | |
| light nested (Panel `nested`/`heatmap`) | literal | `hsl(222 15% 74%)` | |

On top of every plane sat white overlays:
- `bg-white/N`: 662 occurrences in 132 files;
- `border-white/N`: 771 in 136 files;
- `text-white/N`: 1,993 in 146 files.

At 5, 10, 20 and 50 percent, those overlays on 5-6 dark planes made **24 distinct effective hues** from 7 opaque
tokens (`portal-layer-map.json`), a 3.4x multiplier. **That is the texture:** a header strip visibly darker than its
body, a tile inset from its panel, a subheader lifted one step, each overlay reading differently on each plane.

### What a panel IS (feature head @086371dd)

- `portal/src/index.css:115-121`: `--bg-header`, `--bg-medium`, `--bg-card`, `--bg-dark`, `--bg-medium-alt`,
  `--bg-tooltip` and `--bg-tooltip-alt` **all alias `--bg-band` (`#0A1733`)**. Only `--bg-input` (221 44% 17%),
  `--bg-hover` (19%) and `--bg-hover-light` (21%) keep their own lightness.
- `Panel.tsx:62-67`: `chart` and `mixed` resolve to the band; `nested` and `heatmap` resolve to white.
- **The overlays largely SURVIVE:** `bg-white/N` 634, `border-white/N` 757, `text-white/N` 1,894. But they now
  composite onto ONE base, so the 24 hues fall to about 4.
- The body plane fell from 25% lightness to about 12%, the same as the header strip. The header, body, tile and
  tooltip planes are now one value.

**The 09-11 opaque ladder was proposed and never adopted.** `portal-opaque-ladder.json` has five dark rungs
(`band-deepest #0B111D`, `band #101828`, `band-raised #152037`, `band-hover #1B2946`, `band-inset #223358`) and four
light rungs (`canvas`, `surface`, `surface-sunken #E9EDF6`, `hairline`). Round 1 aliased every tier to one band
instead.

### How to represent texture properly -- three options

- **A. Restore the tiers now, on the opaque ladder.** Map strip -> `band-deepest`, body -> `band-raised`, tile ->
  `band-inset`, hover -> `band-hover`. Re-derive each `white/N` overlay to its nearest opaque rung (ONE opacity). This
  brings the texture back on the dark panels without waiting for the inversion, but it builds it only in the world
  Option A retires.
- **B. Build texture only in the light world.** Invert the 24 effective hues by the inversion rule's SURFACE clause
  (preserve each plane's separation ratio as a light plane). The texture carries over by RATIO. It lands only when
  the inversion lands.
- **C (recommended). Define texture as ROLES, each with a rung in BOTH worlds.** One role table: page, section strip,
  panel body, tile, inset, hover, selected, tooltip. Each role has an opaque dark rung (for the band) and an opaque
  light rung (for panels), with the SAME separation ratio between neighbouring roles in each world.
  - The cells build the roles once.
  - The inversion becomes a token swap per role, not 4,887 hand edits.
  - The texture survives the inversion because the ratios are the spec.

## 2. THE LIGHT-MODE INVERSION -- the state of it, and the gap Andrew named

- **Law: ratified.** Option A (09-11): white panels on the canvas, one deliberate band per page
  (`COLOR_ARCHETYPES.md`, `portal/DESIGN.md` C3/C5).
- **Rule: written.** `inversion-rule.json` has 8 clauses, with worked examples: `text-white` -> `#0E2047`,
  `text-white/70` -> `#1D4397`, `bg-white/10` -> `#D1D8E6`, `border-white/10` -> `#D8DEEA`.
- **Applied: NO.** 4,887 light-on-dark idioms in 171 files of `src/pages/` still assume a dark container. That is
  why `chart`/`mixed` and the former tiers stay band-valued, and why the pack shows dark-on-dark bodies (row S2 and
  six siblings, covered by no round-1 cell).

**The gap: STATE.** The rule maps each static idiom by its RESTING ground. It says nothing about what happens when an
interaction changes the ground under the text. **345 state idioms** (`hover:bg-`, active/selected/highlighted
ternaries that set a background) sit in 120 files. That is the population his example lives in.

**The state rule, proposed: ink follows the ground of the CURRENT state, never the component's resting ground.**
Every interactive role gets a state table: rest, hover, selected/highlighted, focus, disabled. Each state is a (ground,
ink) pair, and its contrast is measured PER PAIR (4.5:1 text, 3:1 non-text, WCAG 2.1 SC 1.4.3/1.4.11). Consequences:
- **On a dark band,** a highlight that paints a LIGHT fill flips its text DARK. That is Andrew's example exactly.
- **On a light panel,** a highlight that paints a dark or indigo fill flips its text WHITE. A highlight that only
  steps to a slightly darker light plane keeps navy ink.
- **Everything inside the highlighted element flips with the text:** icons, badges, deltas, chart labels. A
  red/green delta takes its semantic role target against the NEW ground (inversion clause 7).
- **No state relies on a translucent overlay.** Each state's ground is a named opaque rung (ONE opacity). So "hover =
  `bg-white/10`" becomes "hover = the role's hover rung", with its ink computed against that rung.
- **Implementation shape:** state tokens per role (e.g. row: `--row-bg-selected` / `--row-ink-selected`), not per-call
  ternaries. The 345 call sites move onto the tokens, and a checker can prove every pair.

**Scale for the plan:** the static inversion is 4,887 idioms in 171 files; the state rule is 345 idioms in 120 files,
largely the same files. Delivered by route family, the three pack routes (`/market`, `/positioning`,
`/portfolio-management`) are a natural first slice.

## 3. INDIGO ACCENTS (secondary)

- **Restored:** the five identity sites and the indigo favicon, @086371dd; the issuer's checker reads 7 of 7.
- **Open, at Andrew:**
  - the sidebar rail's faint indigo edge (row W2-S19, outside the closed set): keep or drop;
  - the Fear & Greed "Neutral" label renders indigo.
- Continuity beyond the five needs his word; the set is "extended only by his word".

## 4. TOOLTIPS (tertiary)

- **Four implementations:** `src/components/Tooltip.tsx`, `src/components/DataTooltip.tsx`,
  `src/components/HelperTip.tsx` and `src/pages/AdvisorIntelligence/_shared/charts/ChartTooltip.tsx`. Chart-library
  tooltips are also configured per chart. There are 654 "tooltip" mentions across 92 files.
- `--bg-tooltip` was its own darker tier (`#0E1525`) and now aliases the band.
- **Selective edit:** one tooltip role (ground + ink + border + radius) and one component. Chart tooltips point their
  content renderer at it.

## 5. DECISIONS FOR ANDREW

1. **Texture:** C, the role table in both worlds (recommended); A, restore the dark tiers now; or B, light world only.
2. **The state rule:** confirm "ink follows the ground of the current state" as the law.
3. **Inversion delivery:** all at once, or by route family, the three pack routes first (recommended).
4. **Sidebar edge (W2-S19):** keep or drop.
5. **Tooltips:** which of the four is canonical.

## 6. WHAT IT DOES NOT CLAIM

- **Which rung each specific old component should land on.** That is the round-2 cells' census, per role, with a
  denominator.
- **That every one of the 345 state idioms breaks today.** On the current dark band, only 3 selected-state idioms paint
  a light overlay (all `bg-white/10`-style on the band, `DistributionTab.tsx:1710/3313/3550`). The state rule is the
  precondition for the inversion, not a list of live defects.
- **Anything about the portal's DEV or PROD.** All of this is on `feature/d13-visual-elevation`, LOCAL; the portal
  freeze stands.
