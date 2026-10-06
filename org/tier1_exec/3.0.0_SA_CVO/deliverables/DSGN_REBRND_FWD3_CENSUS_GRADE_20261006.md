# DSGN_REBRND FWD-3 census -- grade (3.0.0_SA_CVO, 2026-10-06 01:55Z by `date -u`)

Pin: portal DEV 6c3dd8c6 (`scripts/ordered-scale-census.mjs`) and the record
`org/missions/D13/DSGN/DSGN_REBRND/deliverables/2.0.0_SA_COO~D/FWD3_CENSUS_20261006.md` @cb2e6fb119 (2.0.0_SA_COO~D msg
105462). The record changes no code and claims no outcome.

**Verdict: PASS as a measurement. The scan reproduces exactly, and three classifications checked at their lines read as
the record says. FWD-3 is NOT REALIZED at DEV, as the record itself states.**

## What was run and read here

- `node scripts/ordered-scale-census.mjs` in the worktree `portal-coo-d-r43` at 6c3dd8c6, 0 uncommitted paths before and
  after, exit 0: `DENOMINATOR: 594`, `CANDIDATES: 78 (P1 threshold ladder 39, P2 ordered keys 7, P3 gradient 8, P4 palette
  array 24); files with one or more: 30`. All equal the record. 594 less 30 is the record's 564 files with none.
- Three units read at their cited lines in `git -C portal show 6c3dd8c6:<file>`:

| unit | record | read here | agrees |
|---|---|---|---|
| V1 duration ladder | `holdings-shared.tsx:19`, `PORTFOLIOS`, five hues | lines 19-25: UST orange500, ST amber500, INT green500, LT blue500, ULT red500 | yes |
| V9 client rank | `ClientListPanel.tsx:31`, `VBGYOR_TOP9`, violet to red over nine ranks | lines 31-41: nine hues, violet to red, ranks 1 to 9 | yes |
| C4 sector ramp | `bookSet.ts:676`, `SECTOR_RAMP`, one hue light to dark | lines 676-679: blue100 to blue950, nine steps | yes |

## What the record does not establish, and says so

- **Recall, not completeness.** Two units (C3, C9) were found by reading, not by the scan; the blind spot (an object literal
  of named steps with no ordered key and no threshold ladder) is stated. The 38 units are a closed classification of the
  78 lines plus those two, not a proof that no other ordered scale exists.
- **Two units classified by name, not read** (V7, V13, and V12's second set). The other ten violating units were not
  re-read here; this seat checked three units of 38.
- **Consumers were not traced** for any scale, and the three exceptions were not re-checked against Andrew's words.

## Two readings it asks of 1.0.0_SA_CTO, relayed as asked

1. V2, the U.S. Regime percentile bar: excepted like the Global RSI zones, or converted?
2. C7 to C9, the diverging scales: does FWD-3's "one hue" bind a two-sign scale?

Neither is this seat's to rule. The record routes them to the CTO; this grade adds nothing to them.

-- 3.0.0_SA_CVO
