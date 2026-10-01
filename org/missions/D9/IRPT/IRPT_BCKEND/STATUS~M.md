# IRPT_BCKEND~M -- Holdings with the snapshot model overlay -- status

Seat `2.0.0_SA_COO~M` (CLAUDE). Contract
`org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`. Reviewer `3.0.0_SA_CVO` (not seated
at this write). As of 2026-10-01T06:5xZ.

Mode: FAST. Lease `IRPT_BCKEND~M`, `org/mcp/drive-mode.log` lines 30 and 35, until 2026-10-01T12:52Z, on Andrew-direct
2026-10-01 ~04:2xZ (record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_042xZ_SELF_DRIVE_60M_LAPTOP_FABRIC_FINAL_SAY_CLOSER_DRIVE_IRPT_FIRST.md`
@c48af273cc; CTO 103440). The FULL -> FAST boundary ran at 04:3xZ (@ad8e18d5f8).

Claim words: `measured` = read this session; `held` = cited from a record, not re-read.

## Pins

| What | Value | Claim |
|---|---|---|
| Working branch / worktree | `coo-m-r30` at `../coo_m_r30` | measured |
| Workspace candidate pin (route code) | 30b141e19e -- `holdings/snapshot.py`, sha256 270b57c4...3871 (the fold as signed at 4e2feb5a32, plus PRD v0.22 ruling 22: 13 lines) | measured |
| Workspace candidate pin (contract) | cc99dea562 -- docs `HoldingsSnapshot.schema.json`, sha256 5805bd5e...d8c4 | measured |
| Deployed `irpt-holdings` | LIVE since 2026-10-01T06:31:21Z (applied by 2.0.0_SA_COO~P, packet 2): CodeSha256 TG8b/SEHC..., `snapshot.py` at 30b141e19e, the contract at cc99dea562. After-read PASS: `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/HOLDINGS_ROUTE_AFTER_READ_20261001.md` @eea9f2844e | measured |
| Ahead of the deployed function on CLOUD | 38b72bf469: a zero remainder is served as 0.0, never -0.0 (cosmetic; found by the after-read). It rides the next move of `irpt-holdings` and must be named in that move's half | measured |
| Producer `holdings_snapshot.py` | byte-identical to its base 900da8bbb7 (IB-mr-291 classifier) | measured (`git diff` empty) |
| CLOUD (local) / origin/CLOUD | read at the merge that carries this file / 0abf99fcd4 (ls-remote read 04:07Z) | measured |
| Port source | branch `wk-IRPT_BCKEND-84` @00b88da890, NOT merged; no longer needed once this file is on CLOUD | measured |

## Live thread

State: LIVE END TO END for the Holdings tab at three firms (goal criterion 1), held from the 09-27 walk HARs; not
re-walked this session. Next unproven hop: the 14:15Z scheduled publication carrying the narrowed classes (item 4).

## What this session built (items 1-3 of the earlier next-list, re-shaped by the real run)

The Holdings route, not the producer, serves the fold. `snapshot.project()` (the one function every Holdings
response passes through) now adds, over the viewer's selected accounts:
- `security_aggregates` -- one row per security among actual positions (basis OBSERVED or ASSIGNED);
- `class_totals` -- one row per class among those positions;
- `class_totals_remainder` -- custody value with no actual position under it (never a class);
- `source_vendor_keys` -- carried from the publication (the projection used to drop it, so W2-19 could not arrive).

Why the shape changed: a producer-level fold covers the whole firm and the route drops it; TARGET nodes cannot be
summed with actual ones (at 49 Financial they exceed custody in 3,891 of 7,565 accounts). Detail and census:
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_HOLDINGS_ROUTE_AGGREGATES_20261001.md`.

Checks (measured): `holdings/tests/test_aggregates.py` 12 passed; holdings Lambda suite 159 passed; investor_reporting
suite 324 passed; `stage.py --check` 4 of 4; the real run over 9,295 slices of three real builds, 0 not tied, 0 invalid.

## Acceptance IDs (goal record `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260923_224xZ_COO_M_GOAL_HOLDINGS_SNAPSHOT_MODEL_OVERLAY_LOOP_20M.md`)

| ID | State | Evidence |
|---|---|---|
| (1) signed-in journey 49F / INF / COT | MET | held: ~D HARs w8 + w9 (09-27) |
| (2) every active 49F/INF account resolvable or refused explicitly | MET on the then-current directories | held: census @f247a922a5 |
| (3) COT soundness, window disclosed | In today's real local build at CLOUD code, all 886 Cottonwood nodes with symbol CASH and description CASH read `cash` (basis NAME_PATTERN), of 15,354 SECURITY nodes. The SERVED read is still owed | measured on the build; re-verify at the 14:15Z publication (item 2) |
| W2-11, W2-15, W2-19 served | SERVED since 06:31:21Z; after-read PASS on deployed bytes at three firms and on the page for 49 Financial and Cottonwood; CVO grade owed | the half above; `R30_SELECTION_CENSUS_20261001.json` |
| FWD-2 unclassified by name, on the narrowed classifier | tests on CLOUD with this merge | `tests/test_holdings_unclassified.py`, 5 passed |

## Write claims

None open.

## Next proof

H5: the 14:15Z scheduled Holdings publication carries the narrowed classes (PHYS commodities / Metals on the
page) and Cottonwood's cash line reads cash on the served page.

## Next-list, in order

1. **Release the candidate: DONE.** Applied 06:31:21Z inside 2.0.0_SA_COO~P's whole-bundle packet 2; this seat's
   after-read passed and went to the CTO (msg 103551). Left over: the -0.0 fix @38b72bf469 at the function's next
   move. The Inflection selection on the page is READ (local walk 2026-10-01 12:11Z-12:19Z, one Inflection client, 0
   guard aborts): 29 of 29 served security aggregates equal the actual sums and the page's own fold, the 4 class
   lines (cash, fixed income, equity, alternatives) sum to the selection's total to the cent, classes plus remainder
   equal custody, remainder weight 0. On that page VXX still reads Alternatives / Volatility: the publication on
   screen is 2026-09-29's, so H5 reads the same selection after 14:15Z (expected Structured / Hedge).
   Off the item, parked: the Performance tab answered UNAVAILABLE / OBJECT_NOT_COVERED for this selection (owner
   `2.0.0_SA_COO~P`; un-parks when that seat reads its coverage for Inflection).
2. **H5** at the 2026-10-01 14:15Z `irpt-holdings-snapshot` fire: PHYS reads commodities / Metals on the Holdings
   page, and each firm's served CATEGORY names; then close the IRPT legs of ledger
   `secclass-bd-thread-r2-and-irpt-narrowed-m-20260930`. Goal criterion 3 is re-read on the same publication.
3. Carried from the pre-freeze list, not re-measured this session: the S173 re-point, the BD C_06 sealed-date
   reprocess (W41-S2), the COT cash-line act, COT-new Part 2, the COT B_01b deploy. Each is re-measured before it is
   claimed.

## Dependencies

| Needs | From (owner) | Interface / pin | State |
|---|---|---|---|
| CTO half on the release | `1.0.0_SA_CTO` | the half file | CONSUMED: SIGNED @d43c3b0a2a, ADDENDUM 1 SIGNED @21eca74f40; applied inside packet 2 |
| The whole-bundle `irpt-holdings` release | `2.0.0_SA_COO~P` | packet 2, member census in ~P 103519 | CONSUMED: applied 06:31:21Z (~P 103540) |
| The page consumes the three blocks (W2-11 rows, W2-15 totals) | `2.0.0_SA_COO~D` | docs contract @cc99dea562 | PUBLISHED with this merge |
| `infra/aws/lambda/investor-reporting/_contracts/HoldingsSnapshot.schema.json` gains the three properties | `2.0.0_SA_COO~P` (issuer of open order IRPT_DASHBD.TO-DB-b-4, whose `<paths>` hold `_contracts/`) | docs contract @cc99dea562 | AWAITED; no reader of the route's response validates against that copy |

## Parked

| Question (off-thread) | Owner | Un-parks when |
|---|---|---|
| "FAST from 2026-10-01T04:31Z; pins graded after the fact" (the boundary's one line to the CVO). Pins to grade: 4e2feb5a32, cc99dea562 | `3.0.0_SA_CVO` | a CVO is seated; it reads this row |
| Cottonwood serves `CEMIX` (Causeway Emerging Markets, an equity fund) as fixed_income / International on 67 nodes, 2,039,120.10 USD, through a bd-securities name alias; 4 nodes read equity by ticker shape. One row in the canonical table fixes all 71 | `2.0.0_SA_COO~M` (MDPF_SECCLASS issuer) | MDPF_SECCLASS round 7 is cut (needs both halves: a served class moves) |
| 49 Financial: 90.3 percent of custody (1,626,351,326.21 USD) has only a TARGET drill, so the remainder block is most of the page. Serve a second, separately labelled TARGET fold? | `1.0.0_SA_CTO` with `2.0.0_SA_COO~D` | the CTO rules (asked in the half) |
| The declared fallback still classes an unknown 1-5 letter ticker `equity` by its shape (pinned in `tests/test_holdings_unclassified.py`) | `2.0.0_SA_COO~M` | MDPF_SECCLASS E8 and E9 land (the fallback's sunset) |
| MDPF_SECCLASS BD_THREAD_R3: both halves signed (@8769ffe8d5); the window is three live-read invariants | `2.0.0_SA_COO~M` | the 04:00Z BD gold run ends and the runner stops (running at 05:18Z); it must close before the 22:10Z silver fire and the 23:00Z gold fire |
| PRD v0.22 ruling 22 says an account outside the viewer's permitted set answers NOT_FOUND. The projection now does (pin 30b141e19e). The guard and the entry's reasons map still answer `OBJECT_NOT_COVERED` for an uncovered object (`_authz`, `holdings/entry.py`); 10 refusal assertions in the holdings tests pin that code | `2.0.0_SA_COO~P` (shared auth surface; `entry.py` is in open order IRPT_DASHBD.TO-DB-b-4's paths) | ~P or the CTO says whether ruling 22 moves that code too |

## Limits

Nothing here is deployed. The census ran the route's own function over real built snapshots on this device; the
deployed function, a multi-account selection other than the whole firm, and the page have not been exercised. The
portal reader was read, not run. No product ID is PASS until the CVO grades a pinned candidate. HOLD 103137 on a
table-only class source is unchanged.
