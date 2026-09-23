# IRPT Holdings -- status

Seat `2.0.0_SA_COO~M` (CLAUDE, successor to the Codex seat since 2026-09-23 ~22:47Z). Contract
`org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md` v1.4. Reviewer `3.0.0_SA_CVO~M` (not live at 23:02Z).
As of 2026-09-23T23:05Z.

Standing directive (Andrew-direct ~22:4xZ, record `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260923_224xZ_COO_M_GOAL_HOLDINGS_SNAPSHOT_MODEL_OVERLAY_LOOP_20M.md` @6890584d29):
Holdings end to end for every 49 Financial and Inflection client, meshed across SmartX/Schwab and Eclipse/Orion, with a
SNAPSHOT model overlay (which clients own which models, what assets are in those models; NO model time series), and a
structurally correct Cottonwood pipeline bounded by Black Diamond's data window. `/loop 20m` armed at this seat.

## Pins

| What | Value |
|---|---|
| Working branch / worktree | `codex/irpt-m-completion` at `../ajb_irpt_m` |
| Workspace candidate pin | dc830ad07e (source); this commit adds the publication receipt |
| Portal candidate pin | own UI `codex/irpt-m-ui` e5604c03cb at `../ajb_irpt_m_portal`; P integration c70855f30d at `../portal-local-live-20260923` |
| Deployed artifact pin | Holdings Lambda: native reader package installed by P at ee76fa545f (CTO 85434f5330); repaired loader 3e913e9ce9 NOT DEPLOYED (P owns) |
| Accepted COT publication | revision 93f930c265ed242d7e38cb48a7ed4baf267025e8c4dfd06ff39739c6a8f55217, index version grwnbLkeu_OeYL6AcOR33ec9mO51dTBJ (23:00:30Z), prior JhtDD.AAg1AO0kdvVkxVZN.zWdjwDkkA retained |
| Push state | LOCAL; origin/CLOUD b475b96309 (ls-remote read 23:02Z); shared pushes are 0.0.0_AB_MSTR's |

## Live thread

State: LIVE AT HOP 2 of 4 (source -> accepted publication). Last live trace: Andrew's real logged-in Cottonwood/Anna
Holdings request FAILED NOT_READY (CTO 22:17Z), against the earlier d486-only publication and the unrepaired loader.
First failing hop: 3, accepted publication -> deployed reader/API. Hop 4 (screen with Models/SMAs/Client drill) unexercised.

Hop 2 is now verified live: CTO GO d940022b06 executed 23:00:21-23:00:29Z through the existing publisher against real
versioned S3: 18 immutable creates (Gold, header, 15 parts, manifest) plus one index CAS on IfMatch 606126dddec555c41e711b18732d3c7f.
Every returned version and hash was read back before the index, the index read back at its exact version, the prior
index version retained. Reader matrix on the live publisher: 0698 / d486 / combined at default and date22 READ_OK
(USD 26,303,302.17 / 19,705,844.84 / 46,009,147.02; 32 / 59 / 91 nodes), date23 refused, excluded account refused.
Receipt: `COT_EXPANDED_PUBLICATION_RECEIPT_20260923.json`. Second instrument (aws s3api): 2 index versions, 17 platinum
+ 1 gold objects under the new revision, 2 + 1 under the prior. Coverage: 841 accounts / 13,793 positions / USD 548,412,662.59;
140 accounts explicitly refused (138 no active rows, 2 duplicate grain), never silently empty.

## Acceptance IDs

| ID | State | Evidence |
|---|---|---|
| M1 census incl. non-model/zero/closed/missing | CANDIDATE @a509946936 (COT only) | COT_EXPANDED_ACCOUNT_CENSUS_20260923.json; 981 -> 841 + 140 |
| M2 unique positions, supported grain | CANDIDATE @a509946936 (COT only) | candidate summary: deduplicated, 13,793 |
| M3 Models/SMAs/Client(plug) reconciliation | CANDIDATE (COT: known custody in Client, membership unattributed) | reconcile 548,412,662.59 = 548,412,662.59 |
| M4 accepted Gold -> Platinum, atomic index | LIVE CANDIDATE @93f930c265 (COT) | publication receipt, this commit |
| M5 grants / exact subset / API | AWAITED (P deploys repaired reader) | CTO c6835d130c passes repaired source in the real image |
| M6 visible taxonomy + drill on screen | NOT LIVE | last real login FAIL NOT_READY |
| M7 fresh source -> screen, three firms | NOT STARTED for 49F and INF; COT at hop 2 | -- |
| Snapshot model overlay (Andrew 22:4xZ) | NOT STARTED | client -> models -> assets in those models; 49F SmartX + Tax workbook, INF Eclipse, COT Rebalancer |

Offline-only work grades nothing until the live thread is live.

## Write claims

`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/*` (M records); `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py`
and its tests (49F/INF meshing, next); `.runtime/holdings-journey-20260923/*` (local, gitignored). No shared auth/schema/package/IAM edits (P).

## Next proof

Deployed reader matrix on the real Lambda once P installs the repaired package: 0698 / d486 / combined at default and
date22 READ_OK, date23 refused, then Andrew's real logged-in Holdings screen. In parallel: build the 49F candidate
(Schwab 0833 custody, SmartX model authority, canonical Tax SMA workbook under SMAs > ALT > Tax) and the INF candidate
(Orion custody at the supported grain, Eclipse membership where retained) through the same publisher, and the snapshot
model-overlay projection (client -> models -> assets) from the accepted nodes.

## Dependencies

| Needs | From (owner) | Interface / pin | State |
|---|---|---|---|
| Repaired Holdings package/schema deployed, receipt | 2.0.0_SA_COO~P | 3e913e9ce9 in the real image (CTO c6835d130c) | AWAITED |
| Independent review of published versions | 1.0.0_SA_CTO | receipt in this commit | AWAITED |
| Independent journey review | 3.0.0_SA_CVO~M | pinned candidate | seat not live |
| Eclipse membership ingest (INF models) | Andrew per-use word via 4.0.0_SA_CRO | one batch accounts/simple/list | NOT AUTHORIZED |

## Parked

| Question (off-thread) | Owner | Un-parks when |
|---|---|---|
| Tax runtime (store d3a8c3e7e3, runner c354c33a92) | 2.0.0_SA_COO~M | live Holdings thread reaches the screen |
| 140 COT refused accounts | 2.0.0_SA_COO~M | BD lands active rows (CRO re-check October 2026) |
| 2 traded Tax accounts absent from custody | 4.0.0_SA_CRO~M | a landed master or workbook correction |

## Limits

No authenticated browser PASS. The deployed reader still runs the pre-repair package until P installs 3e913e9ce9.
49F and INF have no accepted publication yet. COT currency rests on Andrew's USD attestation (ANDREW_COT_USD_20260923.md).
INF six matches do not establish a general date offset. No CVO verdict on any ID. No shared CLOUD push by this seat.
