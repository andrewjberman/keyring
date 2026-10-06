# CTO render review: portal candidate 6de76f05 (/freshness, AMGT_RESAPP ax-2 over aw-4) -- APPROVED for one DEV push

**Reviewer:** `1.0.0_SA_CTO~Z`, 2026-10-06 ~18:1xZ. This review was owed since the round-75 analysis (handoff
`ctoZ_2026-10-06_1352Z.md`). It became addressable when the Bloomberg hold lifted (Andrew-direct @8555ce7e12).

## What lands

`origin/DEV` (cf3f10c6, fetched at review)..6de76f05 = **3 commits**: 8adcf3f7 (aw-4 page), fb939c4a (App.tsx route + Tools nav
entry), 6de76f05 (ax-2 fixes).
- They touch **6 files**, +597/-0: `App.tsx`, `api/endpoints/amgt-lead-panel.ts`, and `pages/Freshness/` (4 files).
- `git merge-tree --write-tree origin/DEV 6de76f05` is clean.
- The shared tree's local `DEV` (a3ab197f) is behind origin. Measured against it, the delta reads 42 commits. 39 of those are
  DSGN_REBRND commits that are already on `origin/DEV`. Grade against origin.

## The render

- **Build:** `vite build` of the worktree at 6de76f05 (`C:/tmp/r76-262/portal`, clean), served by `scripts/ui-smoke.mjs --dist`.
- **Fixture:** the DEPLOYED `GET /api/scoped/amgt/freshness` body the ax-2 worker captured
  (`0.9.0_WK_AMGT_RESAPP~253/freshness_body.json` @f3d2a9e60d). FIXTURES-MATCH 1 of 1.
- **Captures read:** (1) the default view ("Stalest first"); (2) after clicking "Company name". In both, LOC is `/freshness` and
  CANVAS is `rgb(244, 246, 250)`.

| check | read |
|---|---|
| C3 canvas, white hairline panel, navy ink, no band on the page | pass |
| no light text or ghost-white fill off the band | pass |
| C8: one `#5F3BE3` primary, and it is the active sort; the actions sit in the panel header | pass, both captures |
| the sorts reorder | pass: "Company name" reorders A-Z (Adobe, AIA, Air Liquide, Alibaba ...); "Stalest first" puts Never ahead of 2026-09-11 |
| the research pack is read from its own field | pass: 2026-10-04 on every row |
| an input collected for no covered name is stated once | pass: "Web search is not collected yet." in the header, and the Stale column does not flag it |
| the header denominator | "95 of 95 covered companies have an input that is stale" |

## Verdict: APPROVED for one DEV push of 6de76f05

The push itself is Andrew's word, queued behind DSGN rounds 43+44 (1d6d2573).

**Round-77 enrichment items (do not gate the push):**
1. The Web search COLUMN still prints "Not collected" on all 95 rows, although the header states it once. Hide the column
   while no covered name has the input.
2. The company labels mix formats ("ASML Na", "GSK Ln", "Visa", "UBS", "Alphabet GOOGL US"). This is a producer-side display
   name, not a page defect.
