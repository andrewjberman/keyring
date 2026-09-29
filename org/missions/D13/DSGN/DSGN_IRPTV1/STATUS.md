# DSGN_IRPTV1 -- status (FAST: /closer-drive under the lease, drive-mode.log line 16)

Seat `2.0.0_SA_COO~D` (CLAUDE). Contract: PRD `org/missions/D13/DSGN/DSGN_IRPTV1/prd/DSGN_IRPTV1_PRD.md` v0.18
@5d44d0fa62. Reviewer `3.0.0_SA_CVO` (grades each landed pin after the fact). Authority: Andrew-direct 17:3xZ record
@229b3fd184; CTO placement @1d443e50db (msg 102388); LIVE_ARMS row `/canonical-drive 10m`, the FAST lease routing each
tick here. As of 2026-09-29T00:2xZ.

## Pins

| What | Value |
|---|---|
| Lease | FAST DSGN_IRPTV1, surface `portal/src/pages/InvestorReporting`, until 2026-09-29T00:52:03Z (presence-extended; read 00:23Z) |
| Working tree | the main portal checkout `C:/Users/AndrewBerman/Desktop/ajb_workspace/portal`, branch DEV |
| Portal candidate pin | DEV `84854311` (FAST item 17, AD-01 remainder) on `1f6612c8` (FAST item 16, AD-01/02 card) on `d516158f` (FAST item 15, AD-03) on `8d12987e` (FAST item 14, UIC-03) on `2febba0b` (FAST item 13, IV-e-76) on `8c6792df` (FAST item 12) on `b0acdee2` (item 10 follow-up) on `11c3fa4a` (FAST item 10) on `816eeb58` (FAST item 9) on `c77b693b` (FAST item 8) on `84519ede` (FAST item 7) on `4ded3791` (FAST item 6) on `38986671` (FAST item 5) on `921e6808` (FAST item 4) on `bfafa6c0` (FAST item 3) on `528acdcd` (FAST item 2) on `a47d3a75` (FAST item 1) on `28f5118c` (round 9 drained: IV-e-68/69/70/73/74/78/79) |
| Portal origin | origin DEV `84854311` (pushed by this seat under the lease; ls-remote read 00:2xZ); PROD `a0314f22`. CI: a47d3a75 run 36466179803 success; 528acdcd run 36472948742 success; bfafa6c0 run 36478024129 success; 921e6808 run 36480377879 success; 38986671 run 36481803879 success; 4ded3791 run 36483696942 success; 84519ede run 36484672421 success; c77b693b run 36485548594 success; 816eeb58 run 36486189794 success; 11c3fa4a run 36487434529 success; b0acdee2 run 36488804219 success; 8c6792df run 36490163869 success; 2febba0b run 36492054339 success; 8d12987e run 36495184912 success; d516158f run 36496901922 success; 1f6612c8 run 36498832251 success; 84854311 unread at this write |
| Suite on 84854311 | IR scope 911 pass / 27 skip / 5 fail = the known 5, counted line by line; tsc -b 0; eslint 0 errors |
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
| 6 | portal `4ded3791` | UIC-20 (IV-e-75): required-field message only after an attempt | iv-e-82 REQUIRED-AFTER-ATTEMPT-OK, fe-s-15 variant green; no real run (walks paused) |
| 7 | portal `84519ede` | UIC-22 (IV-e-75): loading until the snapshot read answers | iv-e-83 SNAPSHOT-LOADING-OK; no real run (walks paused) |
| 8 | portal `c77b693b` | UIC-19 (IV-e-75): title names the client and the variant | iv-e-84 TITLE-CLIENT-VARIANT-OK, iv-e-22/14 green; no real run (walks paused) |
| 9 | portal `816eeb58` | UIC-18 (IV-e-75): visible pick; the form asks what the variant needs | iv-e-85 VARIANT-ASKS-OK, fe-s-15/iv-e-22/82 green; no real run (walks paused) |
| 10 | portal `11c3fa4a` | UIC-17 (IV-e-77): scope panel dates real or omitted | iv-e-86 SCOPE-DATES-OK, iv-t-1 re-goldened, F48 green; no real run (walks paused) |
| 10 follow-up | portal `b0acdee2` | iv-e-3 IVE3-AC1 re-goldened to the formatted date | missed in item 10's own run (tail-read); CARD-FED green |
| 12 | portal `8c6792df` | UIR-45 (IV-e-77): Performance date window in the page date format | iv-e-88 PERFORMANCE-DATES-OK; three raw-ISO checks re-goldened; no real run (walks paused) |
| 13 | portal `2febba0b` | IV-e-76 (UIR-04/13/30, W35-S1): firm names from the registry view | iv-e-89 FIRM-NAMES-REGISTRY-OK, iv-e-56 re-goldened; landed after the CTO's naming-gate fix @85febf3bd1 (102449) |
| 14 | portal `8d12987e` | UIC-03 + CTO ruling 102453 (AD-15): method/source in words; codes, hashes, producer names off the face | iv-e-90 METHOD-SOURCE-WORDS-OK; F40/F47/IVE63 re-goldened; no real run (walks paused) |
| 15 | portal `d516158f` | AD-03: Holdings loses Allocation, Report details, Unique accounts / source dates | iv-e-91 HOLDINGS-PANELS-REMOVED-OK; iv-e-19 re-goldened; no real run (walks paused) |
| 16 | portal `1f6612c8` | AD-01/02 card: L-1 accounts -> Models / SMAs / Client from served amounts | iv-e-92 L0-CARD-OK; the shape is not served yet (~M next round), so today's data keeps the previous path |
| 17 | portal `84854311` | AD-01 remainder: the card is the drill, tree map + table at rest; W17-S1 + F39-AC6/AC7 re-homed onto the card (CTO 102488); negative / unsupplied rows named under the card (UIC-12/UIR-34) | iv-e-93 HOLDINGS-TWO-COMPONENTS-OK; 14 pins re-goldened, each named in the commit; no real run (walks paused) |

Round 9 at the boundary (@f42e1b00fa): IV-e-68/69/70/73/74/78/79 terminal and drained; IV-e-71/72/75/76/77
superseded by this lease, unbuilt, their rows carried into Next.

## Next (in order; Andrew-direct via CTO 102455 -- docs/briefs/irpt-master-guidance-brief-20260928.md Part VI)

Record: org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_222xZ_OPEN_CALLS_1_2_APPROVED_3_HOLDINGS_BASED_PERFORMANCE.md
@391ab19331 (call 1). The one-slice pie (IV-e-71's other half) and the page-local ACCOUNT_PALETTE items are DROPPED;
the MDPF card renders navy as Andrew's screenshot (C3 departure recorded by the CTO); commodities-gold lands in the
shared colour registry as a separate change the CTO reads first.

1. **AD-04 + AD-05:** port Positioning's tree map and table; commodities colour waits on the CTO, the GLD class on ~M.
2. **AD-06..AD-09:** the Analysis three-page flow, the canonical modals, readable results (~Y owns result content).
3. **AD-10..AD-13:** account labels (with ~M), search only, clients that open (with ~P/~M), remove About this scope.
4. **AD-14:** on ~P in parallel (name the COT dependency, then make each firm answer).
5. Carried: UIC-21 (1440 px truncation) waits on a browser run.

## Write claims

`portal/src/pages/InvestorReporting/tabs/analysis/` composer.ts, GenerateComposer.tsx, VariantCards.tsx, AnalysisTab.tsx (item 1 of Next, IV-e-75 rows).

## Next proof

AD-04/05: Holdings' tree map and table are Positioning's own components, fed from the served snapshot. A render test on
the Holdings tab naming the ported component slots.

## Dependencies

| Needs | From (owner) | Interface / pin | State |
|---|---|---|---|
| Holdings shape: L-1 ACCOUNT (total), L0 CATEGORY nodes Models / SMAs / Client per account (amounts served), L1 leaves, L2 securities; no Rebalancer-strategy wrapper | 2.0.0_SA_COO~M | msg 102476 (CTO 102473/102475); next-round cell, pin at serve | AWAITED (card adapter built against it, item 16) |
| K8 re-run window (adapter RENDER_DELEGATE fix + R11 RUNNING answer) | 2.0.0_SA_COO~P | served export path | AWAITED |
| K10 re-run window (irpt-status rebuild 3) | 2.0.0_SA_COO~P | served status path | AWAITED |

## Parked

| Question (off-thread) | Owner | Un-parks when |
|---|---|---|
| The one-line FAST notice to the CVO ("FAST from 17:47Z; pins graded after the fact") | 3.0.0_SA_CVO | the CVO is seated (not LIVE at 17:5xZ) |
| NEW-01 (49F YTD -100%, HIGH) | 2.0.0_SA_COO~P | ~P's first post-reboot item (CTO 102358) |
| All 11 cowdin accounts read "****8774 / UTMA" (the producer's display.label, inferred): row IRPT_BCKEND-S182 @cd42e57b61 | 2.0.0_SA_COO~M | ~M reads the served snapshot; a distinct producer label returns it here as a page item |
| UIC-23's variant word on each history row: the served OwnedAnalysisRequestWire carries identity + accepted_at only | 1.0.0_SA_CTO (wire field, ~Y intake surface) | a variant field lands on the history wire, or the CTO rules the row names no variant |
| W35-S2 (Export on Analysis): the page holds no answer-bearing Analysis report to export -- the live list read (listAnalysisRequests) is refused, so AnalysisTab's report is always null, and the owned-report view (AnalysisReportSliceView) carries sections but not the binding buildAnalysisSubmitRequest needs (input revision, configuration, artifact hash). Export on Analysis correctly stays closed | 2.0.0_SA_COO~Y (analysis read surface) with 1.0.0_SA_CTO | a served read returns an answer-bearing Analysis report with its binding, or the owned report carries the binding fields |
| UIC-14 (Holdings source line in client words): the producer names embed firm tokens (49f/inf/cot), so a hand-typed producer-to-source map is refused by the LGIC naming gate (ENFORCE, DEC-6: read through lookup()). It needs the registry-generated view, the same path CTO 102351 set for IV-e-76, in lib/opal_naming.py outside this lease's surface. Build and test parked at .runtmp/parked/iv-e-87.source-client-words.test.ts (local) | 1.0.0_SA_CTO (ruled, CTO 102444: no function-name-to-vendor map; ~M's Holdings snapshot will carry its source vendor keys, rendered as words from a registry vendor view) | 2.0.0_SA_COO~M serves the snapshot's source vendor keys (and the registry vendor view lands) |
| AD-01's account picker removal and the tree map / table re-scoping to the card's selection: CategoryViewTree (portal/src/components, shared with Model Portfolios) exposes no selection callback | 1.0.0_SA_CTO (surface) | the lease surface widens to CategoryViewTree for an additive onSelect prop, or the CTO rules another carrier |
| IV-e-71's one-slice ALL CATEGORIES pie: an additive prop on the shared CategoryViewTree.tsx | 1.0.0_SA_CTO (surface) | the lease surface widens to that file, or a FULL round cuts it |

## Limits

No FAST pin is graded yet. The round-9 judgment criteria (AC2 rows) wait on the CVO's grade of the landed pins. PROD
promotion stays gated. Any deploy is WORLD and runs under the deploy ledger.
