# IRPT Holdings -- status

Seat `2.0.0_SA_COO~M` (CLAUDE, successor to the Codex seat since 2026-09-23 ~22:47Z). Contract
`org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md` v1.4. Reviewer `3.0.0_SA_CVO~M` (not live).
As of 2026-09-24T00:30Z. CTO 3c8392cf2f: 49F, INF and COT-overlay candidates ACCEPTED as source candidates; its three
bounded findings (Tax conflict, taxonomy path, INF valuation clock) are closed in the commit that carries this line.

Standing directive (Andrew-direct ~22:4xZ, record `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260923_224xZ_COO_M_GOAL_HOLDINGS_SNAPSHOT_MODEL_OVERLAY_LOOP_20M.md` @6890584d29; Step 1b-F row landed by the CTO @d78fdb2f1c):
Holdings end to end for every 49 Financial and Inflection client, meshed across SmartX/Schwab and Eclipse/Orion, with a
SNAPSHOT model overlay (which clients own which models, what assets are in those models; NO model time series), and a
structurally correct Cottonwood pipeline bounded by Black Diamond's data window. `/loop 20m` armed at this seat (cron fcf016cf).

## Pins

| What | Value |
|---|---|
| Working branch / worktree | `codex/irpt-m-completion` at `../ajb_irpt_m` |
| Workspace candidate pin | this commit (INF meshed builder; its two pre-LGIC silver prefixes are read through the producers' own key builders because the naming gate refuses them as new hand-kept carriers); 21f696e19a (49F meshed builder + COT reader matrix); 5f3651db41 (COT receipt) |
| Portal candidate pin | own UI `codex/irpt-m-ui` e5604c03cb at `../ajb_irpt_m_portal`; P integration c70855f30d at `../portal-local-live-20260923` |
| Deployed artifact pin | irpt-holdings Lambda: repaired loader 3e913e9ce9 APPLIED by P 23:00:52Z (CodeSha l/GQrFcE...), CTO-verified d78fdb2f1c |
| Accepted COT publication | revision 93f930c265ed242d7e38cb48a7ed4baf267025e8c4dfd06ff39739c6a8f55217, index version grwnbLkeu_OeYL6AcOR33ec9mO51dTBJ, CTO-verified |
| 49F candidate (UNPUBLISHED) | revision a860115ecaf5336ac5db4491d76cf5b60780f8a9c257c579defaf62351ba6a1f, business date 2026-09-22 / overlay 2026-09-23 (CTO findings 3c8392cf2f closed) |
| INF candidate (UNPUBLISHED) | revision 21279569b08d40ce53e163143b2f829f78c7466f6b25c6a024c57e601b4ef441, business date 2026-09-22 (Orion key 2026-09-23 holds the prior close) / overlay 2026-09-23 |
| Push state | LOCAL; origin/CLOUD b475b96309 (ls-remote read 23:27Z by CTO); shared pushes are 0.0.0_AB_MSTR's |

## Live thread

State: COT LIVE AT HOP 3 of 4 (source -> accepted publication -> deployed reader library, `COT_DEPLOYED_READER_MATRIX_20260923.json`).
Hop 4, the signed-in Anna selection + Holdings screen + reload at localhost:5174, is Andrew's act (asked at the M terminal;
last real attempt 22:17Z FAILED NOT_READY against the pre-repair loader and the single-account publication, both replaced).
49F and INF are at hop 1 (candidates built on real data, reconciled, schema-valid, publication refused until the firm
report currency is attested).

## Acceptance IDs

| ID | State | Evidence |
|---|---|---|
| M1 census incl. non-model/zero/closed/missing | COT live; 49F CANDIDATE (7,522 accounts); INF CANDIDATE (876 accounts; 82 accounts / 1,709 positions outside the census reported) | HOLDINGS_*_MESHED_CANDIDATE_20260923.json |
| M2 unique positions, supported grain | COT live (13,793); 49F candidate (Schwab rows, SmartX assets TARGET); INF candidate (30,881 native Orion rows) | same |
| M3 Models/SMAs/Client(plug) reconciliation | 49F: 5,908 / 7 / 1,607; INF: 518 whole + 71 split / 0 / 287; both reconcile to the cent, difference control discriminates | same |
| M4 accepted Gold -> Platinum, atomic index | COT LIVE; 49F and INF REFUSED until attested | receipts |
| M5 grants / exact subset / API | COT: reader library PASS on deployed bytes; authorizer hop not exercised | COT_DEPLOYED_READER_MATRIX_20260923.json |
| M6 visible taxonomy + drill on screen | NOT LIVE (Andrew's re-test pending) | -- |
| M7 fresh source -> screen, three firms | COT hop 3; 49F hop 1; INF hop 1 | -- |
| Snapshot model overlay (Andrew 22:4xZ) | 49F: 7 models (assets TARGET at SmartX clock); INF: 17 Eclipse models with OBSERVED Orion assets; COT: 46 Rebalancer models over the ACCEPTED publication (462 of 841 accounts assigned, 379 unnamed), assets OBSERVED, blend composition TARGET | HOLDINGS_49F/INF/COT_MODEL_SNAPSHOT_20260923.json |

Offline-only work grades nothing until the live thread is live.

## Write claims

`data/assets/scripts/gold/investor_reporting/{holdings_49f.py, holdings_inf.py, inf_positions.py, holdings_snapshot.py}` and their tests;
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/*`. No shared auth/schema/package/IAM edits (P).

## Next proof

(1) Andrew's signed-in Anna Holdings screen (hop 4). (2) On Andrew's currency attestation for 49F and INF (the binder
accepts only ANDREW_ATTESTATION; P writes the records), publish both candidates through the existing publisher under
CTO review, then their reader matrices. (3) Fold the COT membership into the tree as MODEL_LEAF children under CTO
review (a re-publication, so a new GO), so the screen can show it; the projection artifact carries it today. (4) Own-UI
read of the Holdings tab against MODEL_LEAF children and withheld-drill facts.

## Dependencies

| Needs | From (owner) | Interface / pin | State |
|---|---|---|---|
| 49F + INF firm report currency attestation | Andrew (via P's CurrencyAuthorities.json) | firm-currency-attestation-v1 record | ASKED at the M terminal |
| Review of 49F and INF candidates + reader matrix | 1.0.0_SA_CTO | 21f696e19a + this commit | HANDED OFF |
| NOT_READY reason render with a defined code | 2.0.0_SA_COO~P | contract addendum 2cdbe2bd60 (P 99816) | IN CTO REVIEW |
| Independent journey review | 3.0.0_SA_CVO~M | pinned candidates | seat not live |
| Eclipse account-membership batch read | Andrew per-use word via 4.0.0_SA_CRO | accounts/simple/list | NOT AUTHORIZED; one-to-one portfolio grain used |

## Parked

| Question (off-thread) | Owner | Un-parks when |
|---|---|---|
| Models > Primary / Custom placement for SmartX and Eclipse models (crosswalk) | 2.0.0_SA_COO~M | first live 49F or INF screen |
| Tax runtime (store d3a8c3e7e3, runner c354c33a92); Tax membership read from CRO~M's retained workbook projection | 2.0.0_SA_COO~M | canonical Silver landing of the workbook |
| 140 COT refused accounts | 2.0.0_SA_COO~M | BD lands active rows (CRO re-check October 2026) |
| 2 traded Tax accounts absent from custody; 17 SmartX accounts absent from Schwab 0833; 82 Orion accounts outside accounts_v2 | 4.0.0_SA_CRO~M | a landed master or source correction |
| SmartX prefix "smartx/platform/silver/" grades RAISE at the naming gate ('platform' is not a tier) | 1.0.0_SA_CTO (registry) | registry row |

## Limits

No authenticated browser PASS. 49F and INF candidates carry units "USD" while their manifests say UNATTESTED; neither can
be published. 49F multi-model leaf dollars are apportioned and claimed inferred (2,862 of 7,475). INF: 71 split accounts'
drills withheld, 60 model-named accounts in Client because their excluded part does not tie. No CVO verdict on any ID.
No shared CLOUD push by this seat.
