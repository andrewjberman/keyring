# IRPT Holdings -- status

Seat `2.0.0_SA_COO~M` (CLAUDE, successor to the Codex seat since 2026-09-23 ~22:47Z). Contract
`org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md` v1.4. Reviewer `3.0.0_SA_CVO~M` (not live).
As of 2026-09-23T23:45Z.

Standing directive (Andrew-direct ~22:4xZ, record `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260923_224xZ_COO_M_GOAL_HOLDINGS_SNAPSHOT_MODEL_OVERLAY_LOOP_20M.md` @6890584d29; Step 1b-F row landed by the CTO @d78fdb2f1c):
Holdings end to end for every 49 Financial and Inflection client, meshed across SmartX/Schwab and Eclipse/Orion, with a
SNAPSHOT model overlay (which clients own which models, what assets are in those models; NO model time series), and a
structurally correct Cottonwood pipeline bounded by Black Diamond's data window. `/loop 20m` armed at this seat (cron fcf016cf).

## Pins

| What | Value |
|---|---|
| Working branch / worktree | `codex/irpt-m-completion` at `../ajb_irpt_m` |
| Workspace candidate pin | this commit (49F meshed builder + tests + receipts); prior 5f3651db41 (COT receipt) |
| Portal candidate pin | own UI `codex/irpt-m-ui` e5604c03cb at `../ajb_irpt_m_portal`; P integration c70855f30d at `../portal-local-live-20260923` |
| Deployed artifact pin | irpt-holdings Lambda: repaired loader 3e913e9ce9 APPLIED by P 23:00:52Z (CodeSha l/GQrFcE...), CTO-verified d78fdb2f1c |
| Accepted COT publication | revision 93f930c265ed242d7e38cb48a7ed4baf267025e8c4dfd06ff39739c6a8f55217, index version grwnbLkeu_OeYL6AcOR33ec9mO51dTBJ, CTO-verified d78fdb2f1c |
| 49F candidate (UNPUBLISHED) | revision 1d0b700b7d1ad9f4511497f3d88b109ddfb822dbd4cc633e5da00cec8646e696, business date 2026-09-22, overlay 2026-09-23, local only |
| Push state | LOCAL; origin/CLOUD b475b96309 (ls-remote read 23:27Z by CTO); shared pushes are 0.0.0_AB_MSTR's |

## Live thread

State: LIVE AT HOP 3 of 4 (source -> accepted publication -> deployed reader library). Hop 3 exercised this turn:
`COT_DEPLOYED_READER_MATRIX_20260923.json` runs the Lambda's own reader module (the bytes P installed) against live S3:
0698 / d486 / combined at default and 2026-09-22 READ_OK, 2026-09-23 refused, excluded account refused. Hop 4, the
signed-in Anna selection + Holdings screen + reload at localhost:5174, is Andrew's act (last real attempt 22:17Z FAILED
NOT_READY against the pre-repair loader and the d486-only publication; both are now replaced). Not exercised by this seat:
the authorizer/selection hops and the browser.

## Acceptance IDs

| ID | State | Evidence |
|---|---|---|
| M1 census incl. non-model/zero/closed/missing | COT CANDIDATE @a509946936 (live); 49F CANDIDATE @1d0b700b (7,522 accounts, 8 drills withheld, 17+2 absent-from-custody reported) | census JSONs in this folder |
| M2 unique positions, supported grain | COT live (13,793); 49F CANDIDATE (row-grain Schwab positions, SmartX assets as TARGET) | HOLDINGS_49F_MESHED_CANDIDATE_20260923.json |
| M3 Models/SMAs/Client(plug) reconciliation | COT: Client plug; 49F CANDIDATE: 5,908 Models / 7 Tax / 1,607 Client, reconcile to the cent, difference control discriminates | same |
| M4 accepted Gold -> Platinum, atomic index | COT LIVE @93f930c265 (CTO-verified); 49F REFUSED until currency attested | receipts |
| M5 grants / exact subset / API | COT: reader library PASS on the deployed bytes; authorizer hop not exercised | COT_DEPLOYED_READER_MATRIX_20260923.json |
| M6 visible taxonomy + drill on screen | NOT LIVE (Andrew's re-test pending) | -- |
| M7 fresh source -> screen, three firms | COT at hop 3; 49F at hop 1 (candidate); INF NOT STARTED (currency + membership) | -- |
| Snapshot model overlay (Andrew 22:4xZ) | 49F CANDIDATE: 7 models, client -> model -> assets projected (`HOLDINGS_49F_MODEL_SNAPSHOT_20260923.json`); INF/COT not started | model_snapshot() in holdings_49f.py |

Offline-only work grades nothing until the live thread is live.

## Write claims

`data/assets/scripts/gold/investor_reporting/holdings_49f.py`, `holdings_snapshot.py` (BUILDERS + run_firm refusal), `tests/test_holdings_49f.py`,
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/*`. Next: `inf_positions.py` (attested-currency path, mirroring COT's validator) and an
INF Eclipse membership overlay. No shared auth/schema/package/IAM edits (P).

## Next proof

(1) Andrew's signed-in Anna Holdings screen at localhost:5174 (hop 4). (2) On Andrew's currency attestation for 49F and INF
(same one-line form as ANDREW_COT_USD_20260923.md; the binder accepts only ANDREW_ATTESTATION), publish the 49F candidate
through the existing publisher under CTO review, then the 49F reader matrix. (3) INF: attested-currency path in
inf_positions.py, Eclipse portfolio -> model membership plus models/model_composition as the snapshot assets, candidate census.

## Dependencies

| Needs | From (owner) | Interface / pin | State |
|---|---|---|---|
| 49F + INF firm report currency attestation | Andrew (via P's CurrencyAuthorities.json) | firm-currency-attestation-v1 record | ASKED at the M terminal |
| Review of 49F candidate + reader matrix | 1.0.0_SA_CTO | this commit | HANDED OFF |
| NOT_READY reason render with a defined code | 2.0.0_SA_COO~P | CTO d78fdb2f1c item 3 | AWAITED |
| Independent journey review | 3.0.0_SA_CVO~M | pinned candidate | seat not live |
| Eclipse account-membership batch read | Andrew per-use word via 4.0.0_SA_CRO | accounts/simple/list | NOT AUTHORIZED; portfolio-grain membership used instead |

## Parked

| Question (off-thread) | Owner | Un-parks when |
|---|---|---|
| Models > Primary / Custom placement for SmartX models (crosswalk) | 2.0.0_SA_COO~M | first live 49F screen |
| Tax runtime (store d3a8c3e7e3, runner c354c33a92); Tax membership read from CRO~M's retained workbook projection | 2.0.0_SA_COO~M | canonical Silver landing of the workbook |
| 140 COT refused accounts | 2.0.0_SA_COO~M | BD lands active rows (CRO re-check October 2026) |
| 2 traded Tax accounts absent from custody; 17 SmartX accounts absent from Schwab 0833 | 4.0.0_SA_CRO~M | a landed master or source correction |

## Limits

No authenticated browser PASS. 49F candidate carries units "USD" on nodes while the manifest says UNATTESTED; it cannot be
published. SmartX valuations never tie to Schwab to the cent (0 of 5,912), so multi-model leaf dollars are apportioned and
claimed inferred (2,862 of 7,475 leaves). 8 accounts' Schwab drills withheld (position rows do not tie to net_mv_positions).
INF has no candidate yet. No CVO verdict on any ID. No shared CLOUD push by this seat.
