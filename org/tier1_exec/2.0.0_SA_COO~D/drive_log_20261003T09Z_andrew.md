# Drive log -- 2.0.0_SA_COO~D, 2026-10-03 09Z (host andrew)

| Time | Project | Limb | Act | Outcome |
|---|---|---|---|---|
| 08:4xZ-09:1xZ | DSGN_REBRND (FAST, batch 165; IR lines all blocked: P-3/P-6 wait ~P's P-2 window, Case A waits ~Y) | round 3, row S10 | S10 built, checked, landed: portal `d8d236a0` on origin DEV (ls-remote 09:11Z) | DRIVE FORWARD |
| 09:2xZ-09:4xZ | DSGN_REBRND (FAST; IR still blocked on ~P) | round 3, Next 4b | probed and fixed the widened limb's four groups: portal `71a946e3` on origin DEV (ls-remote 09:48Z) | DRIVE FORWARD |

## S10 -- the Positioning Summary's class percentage labels

- Measured on the body rung (`--layer-body`, #192643): green500 5.899, blue500 4.069, pink500 4.242, yellow500 7.803,
  vermilion500 4.553. Two fail the 4.5:1 normal-text bar (labels are 12-20px semibold).
- Fix: `chartColors.getAssetClassInkOnDark` gives the next lighter step of the class's own hue: blue400 5.886, pink400
  5.650 (new PALETTE token). The four label sites use it. The bars and swatches are unchanged.
- Checks: pin `class-label-ink.test.ts` (3 arms, CONTROL 4.069); iv-e-51 PALETTE census and iv-e-136 pass;
  `bun run typecheck` rc=0; eslint 0 errors.
- Real run: signed-in walk `tmp/ui-walk/20261003T090209Z` (local, not committed). Labels read 5.90:1 (blue400 x4),
  5.67:1 (pink400 x3) and 5.91:1 (green500 x5) on rgb(25,38,67). Disarm REFUSED, as designed. Screenshot looked at.
- The remedy's second half: `.claude/skills/ui-walk/walk.mjs` `--contrast-table` now also grades non-interactive text
  at rest, grouped by (ink, ground, bar), hint only. Its first read found 4 more groups under their bar on /positioning
  (STATUS Next 4b; one is likely the instrument's own blind spot, to be probed).
- Row S12 disarms S10.

## Next 4b -- the widened limb's four groups

- Probe walk `20261003T092442Z`, with location hints added to the limb (tag and class names only, plus where the ground
  was read). It also skipped 200 text elements clipped inside collapsed panels. Placed:
  - the panel footer's source words (TEXT.metadata, white/40, 3.78:1) and its "|" (white/30, 2.65:1) on the band;
  - the page's white/40 labels, 3.63:1 on the body rung;
  - 46 treemap tile labels at "1.18:1": an instrument fault. The labels sit in an SVG foreignObject over a `rect` tile,
    so the ancestor walk read the panel behind the chart. The walker now reads the sibling rect's fill: gray900 on
    blue500 4.82:1, on pink500 5.03:1.
- Fix: the band secondary ink `--palette-mediumGray` (#A8B0C0). PanelFooter.tsx (every page's footer; 8.14:1 on its
  own band ground) and the eight white/40 sites on /positioning (6.87:1 body, 5.65:1 tile). Pin `secondary-ink.test.tsx`
  with a negative control against the HEAD footer.
- After-walk `20261003T094015Z`: 105 pairs, 0 under their bar. Screenshot looked at.
- Lease re-armed to 11:35Z with PanelFooter.tsx; AdvisorBookView.tsx dropped from the surface (the MDPF_SECCLASS lease
  of 2.0.0_SA_COO~M holds it; the arm refused the overlap).

## Housekeeping

- The main portal checkout carried gen-wire output for ExportReceipt/ExportBundle plus 18 line-ending-only rewrites.
  The two content files were byte-equal (CR stripped) to the held branch b847c9f0's committed copies; all 20 were
  restored. Nothing lost.
- Inbox watcher re-armed on expiry (task bzeh26sw2).
