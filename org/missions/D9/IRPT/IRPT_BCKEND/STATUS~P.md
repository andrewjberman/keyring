# IRPT_BCKEND~P (Performance) -- status

Seat `2.0.0_SA_COO~P` (CLAUDE). Contract `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`
(COO_P.md, CONTROL.md apply). Reviewer `3.0.0_SA_CVO` (grades landed pins after the fact while the lease is FAST).
Drive: the 20m goal loop (cron f599225b, :07/:27/:47), reading `python .tools/drive-mode.py read IRPT_BCKEND~P` each tick
(C11, CTO 100817). Lease FAST until 2026-09-24T21:14:15Z at 18:25Z. Goal:
`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260923_224xZ_COO_P_GOAL_PERFORMANCE_REPORTING_THREE_FIRMS_LOOP_20M.md`.
As of 2026-09-25T01:0xZ. Detail history: `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/STATUS.md` (09:4xZ; branch-resident).

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
| 2 | Every active account at each firm resolvable in Performance | MEASURED ee51ffafac: COT 842/842 + INF 875/875 identity resolve; 49F 6692/7454 compute (724 no linkable day, 38 not in engine; both named OBJECT_NOT_COVERED) | `IRPT_MVP_P/PERFORMANCE_RESOLVABILITY_CENSUS_20260924.json` |
| 3 | COT structurally sound, window disclosed not padded | CODE: dates.actual_* = provider window beside requested_* (dd1811bbaa) | test_bd_selected 32/32 |

## Write claims

Item in hand: none building (B1 blocked on the contract ruling). Claimed surface when it un-parks:
`infra/aws/lambda/investor-reporting/export/`, `infra/aws/terraform/investor-reporting/export/`, the `irpt-export-render` source-map row.

## Next-list (in order)

1. S1: the COT one-use plan 99052771.. EXPIRED UNSPENT at 2026-09-25T00:00Z (full scan 00:00:18Z: no USE or ACCEPTED
   row for it). A COT run now needs Andrew's new per-use word and a re-arm (var-file pattern `rearm.tfvars.json`).
2. 49F Performance SERVED on our engine (21:28Z): f49_engine 94cf4cd61e + retained 4573b3e3e3 + grants 55b39f2d11;
   contract provider OPAL_ENGINE (on CLOUD 69cac32dce, ~D told). YTD/QTD/1Y, one account; real read-only run: median
   account YTD +6.72%, 182 days linked. BD cross-check DONE on a 300-account sample (ed9ea1ba55,
   `IRPT_MVP_P/F49_BD_CROSSCHECK_20260924.json`): 244 of 293 within 10bp, 286 within 100bp, median 3.3bp, 7 divergent
   (parked below). ~D verified OPAL_ENGINE renders (100895). ALL-ACCOUNTS census DONE db699faf13
   (`IRPT_MVP_P/F49_BD_CROSSCHECK_ALL_20260925.json`): 5194 of 5309 compared, 4372 within 10bp (84.2%), 4975 within
   100bp (95.8%), 219 divergent (4.2%), median 3.3bp, p90 20.8bp -- the sample holds. OPEN: S1 (Andrew's signed-in 49F request).
3. INF (Orion): inf_selected 312e4be3a0 (captured Scope grammar scoped to one account; orion_adapter parse; identity +
   window gates; 7 tests); mapping 55ccf7e99f (reverse of the directory mint; 25/25 served directory ids map back); OrionTransport daffb01f77
   (estate session JWT orion/jwt/current by jwt_freshness's own constant; live token decodes, 8.7h left); per-firm
   one-use gate f4379b44d7 (the LIVE armed COT plan re-verified under it, no claim); retained INF branch d813dcf9c6
   (INF CODE-COMPLETE offline). NEXT = one bundle on Andrew's per-use word (asked via CTO): package + accounts_v2 read
   grant + plan-gated Orion session read + ONE INF plan, deployed together (no INF compose without a plan). Card @925835306a -- mapping direct
   (accounts_v2.account_id), JWT auto-refreshed 09:51Z/21:01Z, request grammar reconstructed (one live proof needed:
   Andrew's per-use word, or a cheaper Orion Performance-screen HAR first). 49F/INF answer UNSUPPORTED_OPERATION
   by name until each lands (7f6b5589f6, served 20:26Z).
3b. DONE 22:2xZ: HoldingsSnapshot admits M's four classification members (767ac83009; v1 on CLOUD 7251000daa) -- M 100906
   step 1; ~D accepts next, then M emits.
4. Criterion 2 census DONE (ee51ffafac); the 49F gaps (724 + 38) are engine coverage, parked with the BD divergences.
5. EXPORT HOP NOT BUILT -- design card `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/EXPORT_HOP_DESIGN_CARD_20260924.md`.
   Served submit answers NOT_READY; 11/11 host renders Failed (SESSION_ABSENT); 0 PDFs; render signing keys ABSENT;
   V2/V3 render branches coded, not deployed. A (keys + V2 + V3, shared auth plane) is outside P's surface: owner
   asked of 1.0.0_SA_CTO. B1 (serve submit-export for a retained report) is BLOCKED on a v1 contract ruling: the
   submit-export response requires a complete ExportReceipt (artifact sha256, page_count >= 1), so a submitted,
   not-yet-rendered export has no honest answer (asked of 1.0.0_SA_CTO). Measured for B1: evidence keys accept
   `RPT-<32 hex>` as the generation segment at all three firms; the export zip stages 15 files vs performance's 61
   (no reports/, narrative/ or registry modules). B2 first half LANDED 7b0b59b77f (backend branch, LOCAL, not
   deployed -- rides the B1 deploy): dispatch now sends `PortalOrigin`, which the live SSM document requires with no
   default (read-only check: pre-fix set missing it; post-fix none missing, none undeclared); 69 export tests pass.
6. Y compositions: hops 2+3 SERVED (ledger `irpt-upload-hop2-20260924`, S1 = Y's live 12.03 acceptance). Hop 4 custody:
   card `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/CUSTODY_HOP4_CARD_20260925.md` -- installer, reader and
   interpreter ports never constructed; no served writer of the `cst_` binding; the portal sends the holdings
   `sourceSetRevision` where the reader accepts only `cst_<64 hex>`, so every custody submit refuses. Link-3 decision
   (who mints the binding) asked of 1.0.0_SA_CTO.
7. C-S219 COMPLETE d2e014dbf9 (43 of 43, offline; receipt `IRPT_MVP_P/RENDER_CHAIN_C_S219_20260925.json`): one
   render token on all three routes; swapped ids refused; expiry measured (admitted up to 60 s past exp -- on the
   export card for section A); actual V1 refuses the render token; a human token unaffected at V3, full V2 and
   served.Entry; pinned bodies read and an unpinned same-account report refused through a real served.Entry. Fix
   fe854ce6f1 (LOCAL, not deployed): Enforcer object pin + `served.Entry(render_ports=...)`. MEASURED: no deployed
   function installs render ports, so every render read refuses today -- export card B0.
8. A1 `_authz` log-line fix (4fffe13f01): SERVED on irpt-ycharts-generate; rides the next rebuild of the others.
   Census fix 1fcefdad74 (LOCAL, not deployed): all 17 published routes resolve and read guarded -- installed entry
   modules resolve from their staged rows; `served.installed_entry` gives performance/runtime, generate_installed and
   status_installed an earned mark (build at first call, refused unless the Entry matches its declared routes);
   `_authz` 152 passed (was 7 failed). Rides each function's next rebuild; its source-map pins move then.
   Reports suite green in one run a22cdc8578 (87 passed; was 3 failed): the currency refusal arm follows Andrew's
   49F/INF USD attestations (815dbc5507); each installer test pins its own `entry`. Suites: _authz 152, performance
   179, reports 87, export 69.

## Dependencies

| Needs | From (owner) | Interface / pin | State |
|---|---|---|---|
| The COT browser run | Andrew | a NEW per-use word (plan 99052771.. expired unspent) | NOT ASKED |
| A per-use word for 49F and for INF | Andrew | card 2 shape, one each | NOT ASKED (build first) |
| Portal renders dates.actual_* | 2.0.0_SA_COO~D | PerformanceReport v1 dates block | UNREAD |

## Parked

| Question (off-thread) | Owner | Un-parks when |
|---|---|---|
| `build-and-upload.sh` removes tracked `performance/*.py` from the publish worktree's working tree on every irpt-performance-adapter build (18:41Z and 20:2xZ; restored from HEAD each time; generate/refresh builds do not) | 1.0.0_SA_CTO to route (ci/ owner) | the next performance build |
| 49F engine vs BD: 219 of 5194 DIVERGENT over all accounts (db699faf13); in the 300 sample, 7 of 293 DIVERGENT (3 engine coverage gaps of 35-98 neutral days; 1 in-kind signature +4452% vs +96%, the open ADVI_49F.c02-CFINPUT clause; 3 fully linked at 108-496bp), receipt F49_BD_CROSSCHECK_20260924.json | 1.0.0_SA_CTO to route to the 49F engine lane (DS) | the engine lane's next c02 act |
| `directory/tests` 6 fail at HEAD too (test_custody_owner x4 owned-read entry; test_entry x2 2.0 event body / base64) | 2.0.0_SA_COO~P | the next directory/ edit outside refresh.py |
| `holdings/tests` 44 fail in the P worktree at HEAD (test_publication_entry 39, test_runner_destination 3, test_snapshot 2) | 2.0.0_SA_COO~M (holdings lane) | M reads it against its own branch |
| portal `bun test src/pages/InvestorReporting` 89 fail on origin/DEV 5e339ffd (87 unique), not CI-run | 2.0.0_SA_COO~D | ~D's S6/S7 rows |

## Limits

COT has no live use (plan expired unspent); 49F is served on Opal's engine; INF is not composed live. No vendor call is made by this seat; the one use fires only
on Andrew's signed-in request. Nothing here is pushed.
