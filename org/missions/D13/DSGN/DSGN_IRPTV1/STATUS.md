# DSGN_IRPTV1 -- status (FAST: /closer-drive under the lease, drive-mode.log line 16)

Seat `2.0.0_SA_COO~D` (CLAUDE). Contract: PRD `org/missions/D13/DSGN/DSGN_IRPTV1/prd/DSGN_IRPTV1_PRD.md` v0.18
@5d44d0fa62. Reviewer `3.0.0_SA_CVO` (grades each landed pin after the fact). Authority: Andrew-direct 17:3xZ record
@229b3fd184; CTO placement @1d443e50db (msg 102388); LIVE_ARMS row `/canonical-drive 10m`, the FAST lease routing each
tick here. As of 2026-09-28T20:5xZ.

## Pins

| What | Value |
|---|---|
| Lease | FAST DSGN_IRPTV1, surface `portal/src/pages/InvestorReporting`, until 2026-09-28T19:47:43Z (presence-extended) |
| Working tree | the main portal checkout `C:/Users/AndrewBerman/Desktop/ajb_workspace/portal`, branch DEV |
| Portal candidate pin | DEV `38986671` (FAST item 5) on `921e6808` (FAST item 4) on `bfafa6c0` (FAST item 3) on `528acdcd` (FAST item 2) on `a47d3a75` (FAST item 1) on `28f5118c` (round 9 drained: IV-e-68/69/70/73/74/78/79) |
| Portal origin | origin DEV `38986671` (pushed by this seat under the lease; ls-remote read 20:5xZ); PROD `a0314f22`. CI: a47d3a75 run 36466179803 success; 528acdcd run 36472948742 success; bfafa6c0 run 36478024129 success; 921e6808 run 36480377879 success; 38986671 UNREAD |
| Suite on 38986671 | IR scope 900 pass / 27 skip / 5 fail (the known 5); tsc -b 0; eslint 0 errors |
| Screen | `localhost:5174` (dev-live from the main checkout) |
| Workspace push state | CLOUD LOCAL; the push is 0.0.0_AB_MSTR's |

## Live thread

State: LIVE END TO END on DEV for Holdings, Performance and Analysis. Last real run: `/ui-walk --client cowdin`
on 5174 @528acdcd working tree (tmp/ui-walk/20260928T190559Z, local only). S30 disarmed by row S31, S29 by row S33.

## Landed under FAST (graded by the CVO after the fact)

| Item | Pin | Rows | Check |
|---|---|---|---|
| 1 | portal `a47d3a75` | UIC-10, UIC-12, UIC-13, S30 | iv-e-72 HOLDINGS-ANY-COUNT-OK; real run cowdin shot 017 |
| 2 | portal `528acdcd` | UIC-09, S29 | six source-age files green but the known F25 set; the walk caught no loading face (unit render is the exercised path) |
| 3 | portal `bfafa6c0` | UIR-32, UIR-49 (IV-e-71 mask half) | iv-e-71 STRATEGY-TAIL-OK; real run thiessen shot 026 caught the category-views modal before the adapter fix; the post-fix face is unit-proven only (walk killed for low memory) |
| 4 | portal `921e6808` | UIC-23 residue (row S32): date in words, no raw id | iv-e-80 HISTORY-DATE-OK; no real run (walks paused after the harness's low-memory kill) |
| 5 | portal `38986671` | UIC-11 residue (near-white account colour) | iv-e-81 ACCOUNT-PALETTE-VISIBLE-OK, iv-e-70/59 green; no real run (walks paused) |

Round 9 at the boundary (@f42e1b00fa): IV-e-68/69/70/73/74/78/79 terminal and drained; IV-e-71/72/75/76/77
superseded by this lease, unbuilt, their rows carried into Next.

## Next (in order; a defect that breaks the live thread goes first)

1. **IV-e-75 rows (UIC-18..22, W35-S2):** Analysis setup behaves like a form; Export on Analysis opens only on an
   answer-bearing report.
2. **IV-e-77 rows (UIR-45, UIC-14, UIC-17):** one client date format on Performance and the directory stamp; the
   source line in client words; the scope panel never prints 'unknown' (SCOPE AS OF still reads unknown).
3. **IV-e-76 rows (UIR-04/13/30, W35-S1):** firm display names from the registry generated view. Per CTO 102351 the
   view target lands in `lib/opal_naming.py`, outside this lease's surface: CTO reads the diff before it lands.
4. **UIC-03:** no fix of record yet.
5. CRO /ui-walk findings and Andrew's transcripts enter here as they arrive (CTO placement act 3).

## Write claims

`portal/src/pages/InvestorReporting/tabs/analysis/` composer.ts, GenerateComposer.tsx, VariantCards.tsx, AnalysisTab.tsx (item 1 of Next, IV-e-75 rows).

## Next proof

IV-e-75 rows (UIC-18..22, W35-S2): Analysis setup behaves like a form (required-field messages after an attempt, not
on load; no truncated label at 1440 px; a loading state until the snapshot read answers) and Export on Analysis opens
only on an answer-bearing report. One cell of the rows at a time, each with its own test. Real runs wait until system
memory allows a walk.

## Dependencies

| Needs | From (owner) | Interface / pin | State |
|---|---|---|---|
| K8 re-run window (adapter RENDER_DELEGATE fix + R11 RUNNING answer) | 2.0.0_SA_COO~P | served export path | AWAITED |
| K10 re-run window (irpt-status rebuild 3) | 2.0.0_SA_COO~P | served status path | AWAITED |

## Parked

| Question (off-thread) | Owner | Un-parks when |
|---|---|---|
| The one-line FAST notice to the CVO ("FAST from 17:47Z; pins graded after the fact") | 3.0.0_SA_CVO | the CVO is seated (not LIVE at 17:5xZ) |
| NEW-01 (49F YTD -100%, HIGH) | 2.0.0_SA_COO~P | ~P's first post-reboot item (CTO 102358) |
| All 11 cowdin accounts read "****8774 / UTMA" (the producer's display.label, inferred): row IRPT_BCKEND-S182 @cd42e57b61 | 2.0.0_SA_COO~M | ~M reads the served snapshot; a distinct producer label returns it here as a page item |
| UIC-23's variant word on each history row: the served OwnedAnalysisRequestWire carries identity + accepted_at only | 1.0.0_SA_CTO (wire field, ~Y intake surface) | a variant field lands on the history wire, or the CTO rules the row names no variant |
| IV-e-71's one-slice ALL CATEGORIES pie: an additive prop on the shared CategoryViewTree.tsx | 1.0.0_SA_CTO (surface) | the lease surface widens to that file, or a FULL round cuts it |

## Limits

No FAST pin is graded yet. The round-9 judgment criteria (AC2 rows) wait on the CVO's grade of the landed pins. PROD
promotion stays gated. Any deploy is WORLD and runs under the deploy ledger.
