# IRPT_BCKEND~P (Performance) -- status

Seat `2.0.0_SA_COO~P` (CLAUDE). Contract `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`
(COO_P.md, CONTROL.md apply). Reviewer `3.0.0_SA_CVO` (grades landed pins after the fact while the lease is FAST).
Drive: the 20m goal loop (cron f599225b, :07/:27/:47), reading `python .tools/drive-mode.py read IRPT_BCKEND~P` each tick
(C11, CTO 100817). Lease FAST until 2026-09-24T21:14:15Z at 18:25Z. Goal:
`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260923_224xZ_COO_P_GOAL_PERFORMANCE_REPORTING_THREE_FIRMS_LOOP_20M.md`.
As of 2026-09-24T22:1xZ. Detail history: `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/STATUS.md` (09:4xZ; branch-resident).

## Pins

| What | Value |
|---|---|
| Working branch / worktree | `irpt-smoke-p-backend-20260923` at `C:/Users/AndrewBerman/Desktop/irpt-smoke-p-backend-20260923` @55b39f2d11 |
| Publish worktree (source map + recorder) | `irpt-p-publish-20260923` @25d91fb405 |
| Workspace candidate pins today | A1 `_authz` log line 4fffe13f01; Y pin abb74dc689; C1 aa3aabe2ca; series-window fix dd1811bbaa; viewer seam 19b38e2f22; hops 2+3 composition a58859baa7; grants 54bc1359f4; M registry 0e8b5da51b; Y 522afcfd17; 49F/INF named refusal 7f6b5589f6; S125 refresh fix 82679477a6; upload contract a47102cc8f (on CLOUD aa21133b67) |
| Portal candidate pin | candidate 8 237bdfda LANDED on DEV by `2.0.0_SA_COO~D` (origin DEV 92d16efc, msg 100835) |
| Deployed artifact pins | irpt-performance-adapter `YPSX1+nS..` 21:28:08Z (49F on our engine + retention grants, ledger `irpt-performance-49f-engine-20260924` S1 open; plan unchanged; before it l3NswChj.. 20:26Z named refusal; the fix NuIaCuqn.. 18:46Z, receipt `IRPT_MVP_P/PERFORMANCE_WINDOW_REARM_APPLY_20260924.json`); irpt-directory-refresh `d5fqVJ0f..` 20:13:37Z (S125, ledger S1 on the 09-25 fire; refresh.py granted to ~M from here, CTO 100876); irpt-ycharts-generate `LdjdnnLh..` 19:49:52Z; resident package f624e8a72f 19:43:01Z (ledger `irpt-upload-hop2-20260924`, S1 open) |
| One-use plan | ARMED, unspent at 18:47Z: plan sha 99052771.., acc_d486fc94.., 2026-01-01..2026-09-24, expires 2026-09-25T00:00Z (Andrew f0bd1c267e) |
| Push state | LOCAL (both worktrees); MSTR pushes |

## Live thread

State: COT journey ARMED, awaiting Andrew's browser act (before 8 PM ET). The first use (106eaa0e..) was SPENT at 13:47:53Z and
refused by the adapter's own series-window equality check; fixed and served at dd1811bbaa / NuIaCuqn... Next failing hop is
unknown until the run: the provider call -> retained report -> reopen -> export.

## Acceptance (goal Done criteria)

| # | Criterion | State | Evidence |
|---|---|---|---|
| 1 | Signed-in journey login -> selection -> provider calc -> retained -> reopen -> export, per firm | COT ARMED; 49F SERVED on our engine (awaiting a signed-in run); INF NOT BUILT live ("Cottonwood calculation only" in bd_selected; 49F/INF requests answer INVALID_INPUT "mapping firm unsupported", log 13:47Z) | ledger `irpt-performance-window-rearm-20260924` S1 |
| 2 | Every active account at each firm resolvable in Performance | NOT MEASURED | none |
| 3 | COT structurally sound, window disclosed not padded | CODE: dates.actual_* = provider window beside requested_* (dd1811bbaa) | test_bd_selected 32/32 |

## Write claims

Item in hand: none building. Waiting on S1 (Andrew). Next claim: the next-list item 2 surface (`performance/`), on the tick
after S1 reads.

## Next-list (in order)

1. S1: read Andrew's run (PERFORMANCE_USE#99052771.. row, PERFORMANCE_ACCEPTED# row, the adapter log); close or fix.
2. 49F Performance SERVED on our engine (21:28Z): f49_engine 94cf4cd61e + retained 4573b3e3e3 + grants 55b39f2d11;
   contract provider OPAL_ENGINE (on CLOUD 69cac32dce, ~D told). YTD/QTD/1Y, one account; real read-only run: median
   account YTD +6.72%, 182 days linked. BD cross-check DONE on a 300-account sample (ed9ea1ba55,
   `IRPT_MVP_P/F49_BD_CROSSCHECK_20260924.json`): 244 of 293 within 10bp, 286 within 100bp, median 3.3bp, 7 divergent
   (parked below). ~D verified OPAL_ENGINE renders (100895). OPEN: S1 (Andrew's signed-in 49F request); `--all` census.
3. INF (Orion): inf_selected 312e4be3a0 (captured Scope grammar scoped to one account; orion_adapter parse; identity +
   window gates; 7 tests); mapping 55ccf7e99f (reverse of the directory mint; 25/25 served directory ids map back) --
   next: Orion transport (JWT by name), per-firm one-use gate, retained branch, grants. Card @925835306a -- mapping direct
   (accounts_v2.account_id), JWT auto-refreshed 09:51Z/21:01Z, request grammar reconstructed (one live proof needed:
   Andrew's per-use word, or a cheaper Orion Performance-screen HAR first). 49F/INF answer UNSUPPORTED_OPERATION
   by name until each lands (7f6b5589f6, served 20:26Z).
4. Criterion 2 census: every active account per firm resolvable in Performance.
5. Retained report -> reopen -> export verified on the served route after the COT run.
6. Y compositions: hops 2+3 SERVED (ledger `irpt-upload-hop2-20260924`, S1 = Y's live 12.03 acceptance); hop 4 custody
   (admitted_firms under the ledgered plan naming all three firms' objects, CTO 100712) remains.
7. C-S219 (round 18): a complete offline served-route chain for V1 verification (may be superseded by the live trace).
8. A1 `_authz` log-line fix (4fffe13f01): SERVED on irpt-ycharts-generate; rides the next rebuild of the others.

## Dependencies

| Needs | From (owner) | Interface / pin | State |
|---|---|---|---|
| The COT browser run | Andrew | plan 99052771.. before 2026-09-25T00:00Z | AWAITED |
| A per-use word for 49F and for INF | Andrew | card 2 shape, one each | NOT ASKED (build first) |
| Portal renders dates.actual_* | 2.0.0_SA_COO~D | PerformanceReport v1 dates block | UNREAD |

## Parked

| Question (off-thread) | Owner | Un-parks when |
|---|---|---|
| `build-and-upload.sh` removes tracked `performance/*.py` from the publish worktree's working tree on every irpt-performance-adapter build (18:41Z and 20:2xZ; restored from HEAD each time; generate/refresh builds do not) | 1.0.0_SA_CTO to route (ci/ owner) | the next performance build |
| `_authz/tests/test_unguarded_census.py` 7 failures: declared entry modules not on disk in the installation (generate_installed.py, status_installed.py) | 2.0.0_SA_COO~P | the next `_authz` edit |
| 49F engine vs BD: 7 of 293 DIVERGENT (3 engine coverage gaps of 35-98 neutral days; 1 in-kind signature +4452% vs +96%, the open ADVI_49F.c02-CFINPUT clause; 3 fully linked at 108-496bp), receipt F49_BD_CROSSCHECK_20260924.json | 1.0.0_SA_CTO to route to the 49F engine lane (DS) | the engine lane's next c02 act |
| portal `bun test src/pages/InvestorReporting` 89 fail on origin/DEV 5e339ffd (87 unique), not CI-run | 2.0.0_SA_COO~D | ~D's S6/S7 rows |

## Limits

Only the COT account acc_d486fc94.. has a live calculation path. No vendor call is made by this seat; the one use fires only
on Andrew's signed-in request. Nothing here is pushed.
