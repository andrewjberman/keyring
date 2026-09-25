# DSGN_IRPTV1 -- status (FULL: round 3 draining)

Seat `2.0.0_SA_COO~D` (CLAUDE). Contract: PRD `org/missions/D13/DSGN/DSGN_IRPTV1/prd/DSGN_IRPTV1_PRD.md` v0.8
@31a61d0466 (ADMITTED). Round 3: issuance @9e13e294c1 (12 orders IV-e-9..20, decomp v3 @2af10e4cd0), amendment
@1215c0d07a (the CVO's N1-N5 on IV-e-18 and IV-e-13). The FAST lease ended at the cut (drive-mode.log line 6).
Build place: the main portal checkout on DEV (Andrew-direct ~18:3xZ). As of 2026-09-25T01:5xZ.

## Pins

| What | Value |
|---|---|
| Working tree | the main portal checkout `C:/Users/AndrewBerman/Desktop/ajb_workspace/portal`, branch DEV |
| Portal local DEV | `8cd2dab2` (chains A-D merged + the drain's repairs and hookups); origin DEV `13b5356f` (FULL mode: product changes reach origin through `1.0.0_SA_CTO`) |
| Round-3 merges on DEV | chain D `f9df6ab5` (+ repair `62055f14`); chain A `00806e0c` (+ repair `89a6d4f4`); chain B `16c11701`; chain C `d3d93838`; hookups `8cd2dab2` |
| CLOUD records | chain D `1588e5c247`; A `b2c65c13d0`; B `8c2235aa08`; C `cb7bd249c9`; IV-e-16 close `4047bdbea7` + `a109a7e0a9` |
| Screen | `localhost:5174` from the main checkout, serving local DEV |
| Workspace push state | CLOUD LOCAL |

## Orders

| Order | Slot | State |
|---|---|---|
| IV-e-9, IV-e-10 (chain A) | ~7 | complete, merged |
| IV-e-11, IV-e-12, IV-e-13 (chain B) | ~8 | complete, merged |
| IV-e-14, IV-e-17 (chain C) | ~9 | complete, merged |
| IV-e-15, IV-e-16 (chain D) | ~10 | complete, merged (IVE16-AC1 passed after the merge repair) |
| IV-e-18 | ~11 | complete on the slot branch (portal df5e41b5), not yet merged |
| IV-e-19, IV-e-20 | ~11 | IV-e-19 executing; IV-e-20 queued |

## Drain checks

- IR suite on DEV: 85 fail at 16c11701 (legacy set), 85 at 8cd2dab2 before the colour fix with iv-e-16 now PASS; every
  round-3 test file green; tsc -b rc=0 (mutant control rc=2); eslint 0 errors on touched files.
- Interim real run on 5174 @8cd2dab2 (`deliverables/2.0.0_SA_COO~D/round3-real-run-driver.mjs`,
  `round3-close.fixture.json`, `r3-interim*.png`): tabs Performance/Holdings/Analysis; one header Export, no per-tab;
  sample view marked Sample with one prompt; the Generate panel reads the header's client (N1); the Holdings account
  filter names both accounts. Raw ISO on Holdings is IV-e-18's N3 (fixed on the slot branch).

## Rows owed a ruling (drain-end message)

- W11-S1: fe-s-10/parity pins the firm chip's visible name; moving it to a disclosure needs the test re-scoped.
- W11-S2: fe-s-5/states pins "UNAVAILABLE" in the heatmap, which FWD-15 (v0.8) bars.

## Next-list (round 4 candidates)

1. SearchSelect accessibility: no combobox/listbox/option roles, no keyboard navigation (the Catalyst picker had them).
2. The hero cards colour by model name, not served modelCode (CategoryViewTree's contract carries no code; row W8-S1).
3. The live signed-in thread (FWD-1): every real run so far is fixture-driven.

## Parked

| Question (off-thread) | Owner | Un-parks when |
|---|---|---|
| DEV CI does not run `bun test` | `1.0.0_SA_CTO` | a ruling on ci.yml |
| No `.owned-paths.yaml` row for `org/missions/*/*/*/STATUS.md` | `1.0.0_SA_CTO` | the row lands |
| Git's credential manager refuses non-interactively; pushes use `gh auth git-credential` per command | Andrew | he re-signs it, or keeps the gh route |
| A completed worker cannot be continued (row S12); each queue handoff is a fresh spawn | the /dispatch skill's owner | the skill says so |
| Leftover folders `C:/tmp/dsgn-irptv1-fast`, `-base` | Andrew | his OK for a recursive delete |

## Limits

Real runs use the stubbed-auth fixture, not a signed-in session. Judgment criteria are the CVO's at L9. PROD, deploys
and vendor egress stay under their normal gates.
