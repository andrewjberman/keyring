# Holdings Breakdown — center group headers + freeze header rows as a pane (Andrew-direct)
**archetype:** IMPLEMENT

**Portal DEV commit:** `84b24af8`
**Workspace CLOUD commit:** (this log)

## Ask (Andrew-direct, ad-hoc — item 2 of the Positioning-page pass)
On the Positioning page, "Holdings Breakdown" panel table:
1. The first label row ("Basic Info", "Model Breakdown", "ETF Characteristics") — **center**
   the "Model Breakdown" and "ETF Characteristics" titles in their cells (were left-aligned).
   Basic Info left as-is.
2. **Freeze** that label row AND the row beneath it (the column-header row) as a frozen pane,
   so they stay fixed while the user scrolls the holdings list. Same freeze-pane pattern as the
   Positioning Summary panel (item 1, `3b516623`).

## Change
`portal/src/pages/Positioning/tabs/HoldingsTab.tsx` only. 3 edits, +10/-4.

**(a) Centering** — the two group-header `<th>` cells: `text-left` -> `text-center`
(MODEL BREAKDOWN, colSpan=5, orange; ETF CHARACTERISTICS, colSpan=7, green). The `<span>`
inside is inline, so `text-center` on the `<th>` centers it. BASIC INFO unchanged.

**(b) Freeze the two-row header** — the table's `<thead>` holds both the group-header row and
the column-header row. Made the whole `<thead>` `sticky top-0 z-30` and bounded the scroll
wrapper so the body scrolls under it:
- wrapper `overflow-x-auto max-w-full scrollbar-none` -> `overflow-auto max-w-full` +
  `style={{ maxHeight: 'clamp(360px, 62vh, 760px)' }}` (adds the vertical scroll region;
  keeps horizontal scroll; drops scrollbar-none so the vertical scrollbar is hover-discoverable).
- `<thead>` -> `<thead className="sticky top-0 z-30">`.

**Why sticky the whole `<thead>` (not per-row):** sticking each row needs the 2nd row's `top`
to equal the 1st row's rendered height — fragile hardcoded-px math. Sticking the thead as one
unit pins both rows together at `top:0`, no offset needed. Modern Chrome/Edge (the internal
portal browser) support thead sticky (Chrome 91+).

**Why z-30:** the table already freezes its first column horizontally via `sticky left-0`
(`z-20` on the Asset Class header, `z-10` on body first-column cells) — pre-existing, in prod,
which is also the proof that sticky + `border-collapse` renders fine in THIS table. z-30 keeps
the whole frozen header above those body sticky-left cells when the body scrolls under it. Both
freeze axes (sticky-top thead + sticky-left first column) share the bounded wrapper as their
scroll container and compose into a standard row+column freeze.

**Border-collapse note:** header rows carry opaque `contentPanel` backgrounds (on the `<tr>`s)
so the body never shows through the frozen header; even if a collapsed border glitched under
scroll (a known Chromium quirk), the header stays legible + separated. The existing sticky-left
header already renders its borders fine here, so no shadow/border workaround was needed.

## Verify
- `tsc -b --noEmit` (portal): **PASS** (exit 0). [First pass caught a JSX error — I'd placed the
  freeze-pane block comment in the ternary's `) : (` expression slot where `{/* */}` isn't valid;
  moved it inside the `<div>` as a JSX child. Re-ran: clean.]
- `eslint src/pages/Positioning/tabs/HoldingsTab.tsx`: **PASS** (exit 0).
- **Live pixel-eyeball: BLOCKED for me** — portal auth wall, no creds (same standing limit as
  item 1). Sticky-header + border-collapse is exercised in prod in this very table (the
  sticky-left first column), which de-risks it; still wants a visual confirm on the authed page:
  (1) both group titles centered; (2) both header rows stay pinned while the holdings list
  scrolls; (3) the freeze-window height feels right (tunable).

## Compiler Tools
| Tool | Result | Note |
|---|---|---|
| (none applicable) | — | Pure CSS/layout on an existing table — no data props, no new cohort/metric/mode, no deletion. `comp-transform schema-check` (DE minimum for data-prop changes) is N/A; HoldingsTab is not in the comp-transform registry (recharts/table presentational, same GAP class logged 2026-06-26). Mechanical gates = tsc + eslint (both PASS). |

## Files Modified
| File | Change | Committed |
|------|--------|-----------|
| portal/src/pages/Positioning/tabs/HoldingsTab.tsx | Center MODEL BREAKDOWN + ETF CHARACTERISTICS group headers; freeze two-row thead (sticky top-0 z-30) + bound scroll wrapper | Yes — DEV `84b24af8` |

## Current State
Committed to portal **DEV `84b24af8`**, mechanically verified. Second of two Positioning-page
ad-hoc items this session (item 1 = Positioning Summary freeze-pane, DEV `3b516623`). Both
FE-only, no backend/Lambda. Not a structural change -> `pod_inventory.xml` untouched. DE cannot
push -> DT batches the promote.

## Next Steps
- [0.2.0_DT_PortfolioAnalytics] Push DEV + (on Andrew's GO) promote both `3b516623` + `84b24af8`
  DEV->PROD via `/prod-deploy` in one batch. FE-only, no yang/Lambda touch.
- [Andrew/operator] Pixel-eyeball on the authed Positioning page (Holdings Breakdown): group
  titles centered; both header rows pinned while the holdings list scrolls; window height OK.

## Blockers
None. Pixel-eyeball residual is the credential/auth-wall limit (handed to operator/DT), not a
correctness gap — mechanically verified + pattern already exercised in-prod in this table.

---

## Follow-up — frozen-header bleed-through fix (portal DEV `7e8baa70`)
Andrew observed the scrolling holdings rows showing THROUGH the frozen header rows.
**Cause:** the sticky `<thead>` cells relied on the `<tr>` background or used translucent
`bg-*-500/10` tints, and a **row-level background does not paint behind a sticky header in a
`border-collapse` table** — so those cells were see-through. The tell: the Asset Class cell,
the only one carrying its OWN opaque cell-level `bg-[...]`, was the only one that did NOT bleed.

**Fix (mechanism-agnostic):** give every rendered header cell its own opaque background
(mirrors Asset Class). Added module-level helpers — `solidHeaderStyle` (opaque navy =
`--semantic-background-contentPanel`) for plain cells, and `tintHeaderStyle(rgba)` (opaque
navy base + the color tint as a `linear-gradient` overlay) for the color-coded cells, so the
exact tinted look is preserved while being fully opaque. Applied to all header cells that
render in the two live views (characteristics group + column headers; performance group +
period columns). Asset Class left as-is (already opaque). The dead `selectedPeriod!=='Current'`
branch (never renders — `selectedPeriod` is a `'Current'` literal) left untouched.

**Why not `border-separate`** (the usual 2-line sticky-table fix): the body's row dividers are
`border-b`/`border-t` on `<tr>` elements, which do NOT render in the `border-separate` model —
it would erase the holdings row separators. The opaque-cell fix stays contained to the header;
the body border grid + `border-collapse` are unchanged.

tsc -b --noEmit clean; eslint clean. Still auth-wall-blocked from a self pixel-eyeball →
operator/DT confirm at promote. Now three DEV commits in the batch: `3b516623` (Positioning
Summary freeze-pane) + `84b24af8` (Holdings center+freeze) + `7e8baa70` (Holdings bleed-through).
