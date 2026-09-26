# DSGN_IRPTV1 -- status (FULL: round 4 + IV-e-27..30 on PROD portal-v2.1.188; drive loop closed, reads parked)

**At close, 2026-09-25 ~23:5xZ:** PROD 36a37afc = portal-v2.1.188 (peeled; Deploy to Production run 36200152208
success) carries round 4 (IV-e-21..26) and the direct acts IV-e-27..30, promoted by `2.0.0_SA_COO~D` on CTO GO 101049
(Andrew's allowance relayed in CTO 101030); rollback base cb48eff8. origin DEV 1e821a6e (the lint fix; CI 36200546242
success). Every order is terminal and every worker slot is torn down. What remains is READS, parked below with their
trigger; the /canonical-drive loop is closed per Andrew-direct ~17:2xZ ("drive your responsibiklities to completion and
then you can close loop").

Seat `2.0.0_SA_COO~D` (CLAUDE). Contract: PRD `org/missions/D13/DSGN/DSGN_IRPTV1/prd/DSGN_IRPTV1_PRD.md` v0.8
@31a61d0466 (ADMITTED). Round 3: issuance @9e13e294c1 (12 orders IV-e-9..20, decomp v3 @2af10e4cd0), amendment
@1215c0d07a (the CVO's N1-N5 on IV-e-18 and IV-e-13). The FAST lease ended at the cut (drive-mode.log line 6).
Build place: the main portal checkout on DEV (Andrew-direct ~18:3xZ). As of 2026-09-25T03:1xZ.

## Pins

| What | Value |
|---|---|
| Working tree | the main portal checkout `C:/Users/AndrewBerman/Desktop/ajb_workspace/portal`, branch DEV |
| Portal DEV / PROD | PROD `36a37afc` (portal-v2.1.188) carries round 4 + IV-e-27..30; origin DEV `1e821a6e` (ls-remote reads 2026-09-25 ~23:2xZ). Earlier: PROD cb48eff8 (portal-v2.1.187) carried round 3 |
| Direct acts | IV-e-27 `959a59a2` (IR "Other"); IV-e-28 `7eec611a` (AI Cottonwood `other`); IV-e-29 `b997c9e5` (AI Cottonwood `cash`, drill legend); IV-e-30 `4d6c8aaa` (drill by tenant palette, row W19-S1 disarmed). CLOUD records `b8281039d8`, `e02ad3773b`, `91c8f5ba82`, `16cc97aa6e` |
| Round-3 merges on DEV | chain D `f9df6ab5` (+ repair `62055f14`); chain A `00806e0c` (+ repair `89a6d4f4`); chain B `16c11701`; chain C `d3d93838`; hookups `8cd2dab2`; join `6de269cc` (ff) + `f9a954b3`; repairs `ecfd327a`, `8242412d` |
| CLOUD records | chain D `1588e5c247`; A `b2c65c13d0`; B `8c2235aa08`; C `cb7bd249c9`; join `4c8d0f570e`; IV-e-16 close `4047bdbea7` + `a109a7e0a9`; IV-e-20 close `6c8a16b536` + `0eb458269a` |
| Screen | `localhost:5174` from the main checkout, serving local DEV |
| Workspace push state | CLOUD LOCAL |

## Orders

Round 4 DRAINED: IV-e-21, 22, 23, 25, 26 complete and merged on portal local DEV (08144571 + the drain repair 55ed4790);
CLOUD merges 147cc46055, ece848b113, 3a67336837, 0bd9852c47, 736f69a15b. Suite 757 pass / 81 fail (legacy set only);
tsc -b rc=0. Fixture close run: deliverables/2.0.0_SA_COO~D/round4-close.* (row S15). The round's AC4 judgment grades and
round 3's five NOT_EVALUATED wait on Andrew's signed-in walk on 5174, asked through 1.0.0_SA_CTO 19:08Z (CTO 100986).
IVE16 (Holdings export) waits on P's 'holdings' ReportKind (CTO 100994). origin DEV is 8242412d; the round-4 candidate
reaches origin through the CTO's review and 0.0.0_AB_MSTR's push.

Direct act IV-e-27 (M 101020, asset class `other` -> "Other", PALETTE.purple600) merged on local DEV 959a59a2 (CLOUD
b8281039d8); unblocks M's batch B once origin DEV carries it. Local DEV also carries P's render-token commit 5c2fc34d.

## Round-5 candidates

1. The firm chip and identity card read the firm catalogue's name (ResolvedScope carries no display name: adapt.ts:696-705).
2. The print route's render token: P's own (api-client.ts reads it on the print route; PrintEntry needs nothing, P 101011).
3. IVE16's one-line EXPORT_KIND_BY_TAB hookup when P serves 'holdings'.
4. iv-e-17.regenerated / iv-e-26.wire-regen run gen-wire IN PLACE: a suite run rewrites contracts/wire/** with LF endings (0 content lines, 25 files shown modified in the main checkout); regenerate into a temp dir and compare.

## Round-3 drain checks

- IR suite on DEV (f9a954b3 + ecfd327a): 742 pass / 82 fail; the only round-3 residual is fe-s-5/states (W11-S2);
  every round-3 test file green; tsc -b rc=0 (mutant control rc=2); eslint 0 errors on touched files.
- The one real run on 5174 @8242412d: `deliverables/2.0.0_SA_COO~D/round3-close.{run.txt,01..05-*.png}` (driver
  `round3-real-run-driver.mjs`, fixture `round3-close.fixture.json`). It found a white-on-white account dropdown,
  fixed at 8242412d. Row S14 carries the close.
- Channel: 40 investigation rows; the CVO's last compile (13baec35aa, round 1) covered 8.

## Rulings received

1.0.0_SA_CTO 100948 (RULINGS_IRPT_20260925.md @75156f2b18, R6): W11-S1 keep fe-s-10/parity (a firm's name is client
language; only a system token on the chip moves to a disclosure); W11-S2 re-scope fe-s-5/states next round. Both rows
disarmed. The DEV landing 13b5356f..8242412d is under the CTO's review; the push is 0.0.0_AB_MSTR's on Andrew's word.

## Next-list (round 4 candidates)

1. SearchSelect accessibility: no combobox/listbox/option roles, no keyboard navigation (the Catalyst picker had them).
2. The hero cards colour by model name, not served modelCode (CategoryViewTree's contract carries no code; row W8-S1).
3. The live signed-in thread (FWD-1) is round 4's DRAIN ACT, not a cell (CTO 100986): run it on IRPT_BCKEND's bounded
   test principal (IB-rtf-3) if live, else ask Andrew through 1.0.0_SA_CTO for one signed-in walk on 5174; hops fed by P's
   gaps (spread, B1) grade from the live refusal, FWD-1 NOT_REALIZED stated.
4. fe-s-5/states re-scoped per R6: the heatmap cell reads "not supplied", the reason on hover; the two sub-tests pinning the
   retired Summary block re-scoped or removed with the reason stated.
5. The firm chip prints the firm token ("F-CW"); per R6 the chip shows the firm's name and the token moves to a disclosure.
6. Model colour keyed by the served model_code only (CTO 100953; M serves it on model nodes since 23:2xZ); retire the
   longest-key label fallback where a code exists.
7. submit-export: accept a data-less QUEUED/RUNNING answer, the export id from status.operation.revision (P 100960;
   schema @f6fd60f4fd, CTO R2); regenerate contracts/wire. The served route still answers NOT_READY until P's B1 lands.
8. Print route (P 100987; EXPORT_HOP_DESIGN_CARD_20260924.md B2-URL @bc3f70d22c): PrintEntry reads selection/start/end
   from the URL and resolveBundle passes them to getPerformanceReport, refusing by name when one is missing (today it
   throws "An accepted account selection is required" and sends start = end = businessAsOf).

## Parked

| Question (off-thread) | Owner | Un-parks when |
|---|---|---|
| DEV CI does not run `bun test` | `1.0.0_SA_CTO` | a ruling on ci.yml |
| No `.owned-paths.yaml` row for `org/missions/*/*/*/STATUS.md` | `1.0.0_SA_CTO` | the row lands |
| Git's credential manager refuses non-interactively; pushes use `gh auth git-credential` per command | Andrew | he re-signs it at his keyboard (his option (a), ~17:2xZ) |
| A completed worker cannot be continued (row S12); each queue handoff is a fresh spawn | the /dispatch skill's owner | the skill says so |
| IVE29-AC4 on PROD: z09308463's cash slice (0.37 at 09-22) with shares summing to 1; all-cash z09326138 or z09308511 at 100% cash | the COO seat holding DSGN_IRPTV1 (`2.0.0_SA_COO~D` at close) | 2.0.0_SA_COO~M reports Monday 2026-09-28's first scheduled COT gold run (C_06 cash deployed 23:44Z, version LmvfjXlB; M 101064) |
| IVE28-AC4 on PROD: z09305589 shows Other at $19,653,063.27 (bd-securities Part 2, 26 `other` keys; Part 1 wrote 941 keys and moves no `other`; M 101121, re-cut per Andrew-direct @c3dde578b9) | same | 2.0.0_SA_COO~M reports Part 2 written (after Monday's act-1 read-back; the IR `other` mapping is on origin DEV and PROD already) |
| IVE30-AC3, round 4's AC4 judgments, round 3's five NOT_EVALUATED: a signed-in look (the stubbed page 401s all 24 AI data calls) | Andrew (asked through 1.0.0_SA_CTO, 100986 / 101005) | his signed-in walk on 5174 or PROD |
| Round 5 cut (candidates above) | `1.0.0_SA_CTO`, then the issuing COO | the CTO's round-4 analysis arrives |
| The drain checks omitted `bun run lint`; one unused import reached DEV (fixed 1e821a6e) | the COO seat holding DSGN_IRPTV1 | next drain: run lint beside tsc and the suite |

## Limits

Real runs use the stubbed-auth fixture, not a signed-in session. Judgment criteria are the CVO's at L9. PROD, deploys
and vendor egress stay under their normal gates.
