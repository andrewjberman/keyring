# DSGN_IRPTV1 -- status (FULL: round 3 drained; L10 with 3.0.0_SA_CVO)

Seat `2.0.0_SA_COO~D` (CLAUDE). Contract: PRD `org/missions/D13/DSGN/DSGN_IRPTV1/prd/DSGN_IRPTV1_PRD.md` v0.8
@31a61d0466 (ADMITTED). Round 3: issuance @9e13e294c1 (12 orders IV-e-9..20, decomp v3 @2af10e4cd0), amendment
@1215c0d07a (the CVO's N1-N5 on IV-e-18 and IV-e-13). The FAST lease ended at the cut (drive-mode.log line 6).
Build place: the main portal checkout on DEV (Andrew-direct ~18:3xZ). As of 2026-09-25T03:1xZ.

## Pins

| What | Value |
|---|---|
| Working tree | the main portal checkout `C:/Users/AndrewBerman/Desktop/ajb_workspace/portal`, branch DEV |
| Portal local DEV | `8242412d` (all of round 3 + the drain's repairs and hookups); origin DEV `13b5356f` (FULL mode: product changes reach origin through `1.0.0_SA_CTO`) |
| Round-3 merges on DEV | chain D `f9df6ab5` (+ repair `62055f14`); chain A `00806e0c` (+ repair `89a6d4f4`); chain B `16c11701`; chain C `d3d93838`; hookups `8cd2dab2`; join `6de269cc` (ff) + `f9a954b3`; repairs `ecfd327a`, `8242412d` |
| CLOUD records | chain D `1588e5c247`; A `b2c65c13d0`; B `8c2235aa08`; C `cb7bd249c9`; join `4c8d0f570e`; IV-e-16 close `4047bdbea7` + `a109a7e0a9`; IV-e-20 close `6c8a16b536` + `0eb458269a` |
| Screen | `localhost:5174` from the main checkout, serving local DEV |
| Workspace push state | CLOUD LOCAL |

## Orders

All twelve round-3 orders (IV-e-9..IV-e-20) complete; every worker slot drained and torn down.

## Drain checks

- IR suite on DEV (f9a954b3 + ecfd327a): 742 pass / 82 fail; the only round-3 residual is fe-s-5/states (W11-S2);
  every round-3 test file green; tsc -b rc=0 (mutant control rc=2); eslint 0 errors on touched files.
- The one real run on 5174 @8242412d: `deliverables/2.0.0_SA_COO~D/round3-close.{run.txt,01..05-*.png}` (driver
  `round3-real-run-driver.mjs`, fixture `round3-close.fixture.json`). It found a white-on-white account dropdown,
  fixed at 8242412d. Row S14 carries the close.
- Channel: 40 investigation rows; the CVO's last compile (13baec35aa, round 1) covered 8.

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
