# INF ADVI Staleness — Andrew-Timed P0 Recovery Report

**Author:** 0.4.0_DS_ClientPlatform (recovery lane) | **Root-cause trace:** 1.0.0_SA_CTO (graph, 2 queries)
**Date:** 2026-06-12 | **Status:** RECOVERY EXECUTED; final served-verify pending chain completion (~23:08Z)
**Symptom (Andrew, 20:37Z):** ADVI inf shows 06-11 / $202M; Orion has $204.6M today; MDPF stamps 06-12 07:30 but serves $202M.

## Clock

| Time (Z) | Event |
|---|---|
| 20:37 | Andrew GO fired (4:37p ET) |
| 20:40–21:05 | CTO detection -> root-cause (graph trace: PartnerAnalytics full-stack + inf EVENT_RULE/LAMBDA census) ~25 min |
| 20:44 | DS recovery lane start |
| 20:46–20:50 | **L1 fix:** code/bronze-runner refreshed — 8-dim orchestrator + data/inf-layout fetch script + 7 dim scripts + jwt_freshness; all ETag-verified; on-instance copies refreshed via SSM |
| 20:52:59 | EC2 transactions re-fire OK: bronze/orion-api/2026-06-12/transactions.csv (1.2MB) landed |
| 21:03 | **L2 identified:** inf-api-txn rule ENABLED + fired 13:00Z as always — but date DEFAULT = now-1d; today's run processed 06-11. The 06-12 quorum sat 8/9 (transactions only missing) |
| 21:06:51 | inf-api-txn invoked direct {"date":"2026-06-12"} -> 200, empty_day=false |
| 21:07:13–16 | Quorum 9/9 -> _AGGREGATOR_FIRED -> inf-gold-trigger dispatched (cleared the morning's 8.1h stale lock) |
| 21:12 | **L3 identified:** 21:07Z chain DIED instantly — sync_scripts() basename-collision FATAL (same as the morning chain's death) |
| 21:12–21:17 | **L3 fix:** canonical (repo==code/silver, md5==ETag) copied over stale code/gold twins; byte-identical verified; dead lock lock-full-5288d152539c cleared on NO-CHAIN-PROCESS evidence |
| 21:18:14 | Gold chain re-dispatched (command de221d6c, lock-full-816b520f05ad) |
| 21:19–21:20 | Chain verified ALIVE past the guard — REST txn pull running (864 accounts, ~200/min) |
| 21:21 | **L4 (CTO scope extension):** Eclipse bronze+silver dark at 06-11; MP model data rides Eclipse; mdpf auto-fires on pipeline-complete.json — eclipse must land first |
| 21:23–21:25:01 | Eclipse trio pre-landed via `--chain eclipse` (concurrent, no-lock verified): bronze + silver + gold/eclipse/2026-06-12/ + gold_complete sentinel; firm total $121.78M / model AUM $125.88M / orion $121.78M |
| 21:25–21:26 | **NEAR-MISS:** eclipse chain completion armed the runner's 2-min auto-shutdown WHILE the full chain ran — cancelled via SSM (`SHUTDOWN-CANCELLED`), full chain confirmed alive |
| ~23:08 (ETA) | Chain completion (06-11 precedent: 1h49m) -> pipeline-complete.json -> mdpf auto-fire (Stage 0.5 resolves today's eclipse sentinel) -> R4 served-verify BOTH pages |

## Root cause — THREE stranded layers of the 2026-06-11 cutover bundle

The v2 transactions cutover (06-11 ~12:08–16:08Z uploads) left three deploy layers inconsistent;
each independently broke a leg of today's pipeline:

**L1 — EC2 bronze-runner prefix stale (CTO's original trace).** The runner's systemd flow syncs
`s3://opal-data-inf/code/bronze-runner/`; the current 8-dim orchestrator went to `code/bronze/`
(wrong prefix, stranded-deploy / MDPF_COUNTS class). The runner ran the May-8 7-dim orchestrator
(no transactions leg, pre-DTAFLP `data/orion` paths). Compounding: the on-instance
`inf-bronze-fetch.sh` (baked at bootstrap, May-1) laid scripts at `data/orion/` while the current
orchestrator resolves `data/inf/` — syncing the orchestrator alone would have failed every dim.

**L2 — inf-api-txn D-1 default vs same-day quorum.** The 9-dim silver quorum
(`silver/_silver_complete/{date}/`) gates gold. Eight dim-Lambdas process SAME-day; `inf-api-txn`
defaults to `now-1d`. Its 13:00Z run today wrote the 06-11 sentinel (completing YESTERDAY's quorum
a day late) and left 06-12 at 8/9. Transactions is structurally the quorum laggard pending cutover.

**L3 — code/gold vs code/silver basename collision (the morning-crash cause).** The 06-11 16:08Z
`code/silver/` uploads (`_orion_api_silver_lib.py`, `build_assets_dim.py`) collided with stale
May-vintage twins in `code/gold/`. The gold runner's collision guard — correctly fail-closed —
FATAL'd `sync_scripts()`, killing today's 13:00Z scheduled chain (which died holding the dispatch
lock, no log upload, no alarm) and the 21:07Z recovery chain alike. Gold never ran today until
the 21:18Z re-dispatch.

**L4 — Eclipse rode L3 down.** Eclipse (bronze pull -> silver -> E_00 model-portfolios gold) runs as
the gold chain's POST-SENTINEL best-effort block on the gold runner — not the bronze-runner bundle.
Gold never ran today (L3), so Eclipse never ran; Model Portfolios' model leg froze at 06-11 alongside
ADVI. (Corrects the initial L1-bundle hypothesis; the gold-chain placement is the ground truth.)

Detection was human (Andrew noticing stale ADVI): the guard's FATAL is invisible — on-instance,
pre-log-upload, lock held, no CW/SNS surface.

## Recovery actions (all code = already-committed repo content; zero repo changes needed)

1. `code/bronze-runner/` refreshed: orchestrator.py, inf-bronze-fetch.sh, 7 dim scripts,
   jwt_freshness.py (md5==ETag verified each) + on-instance copies refreshed (SSM, S3-artifact model)
2. EC2 transactions re-fire (SSM, `--dims transactions`): bronze csv 06-12 landed
3. `inf-api-txn` direct invoke for 06-12: sentinel landed, quorum completed, aggregator fired
4. Collision resolution per the guard's own prescription: canonical over `code/gold/` twins
5. Dead dispatch lock cleared (holder verified dead); gold chain re-dispatched

## R4 — served verification (PENDING chain completion)

To verify on completion (Monitor armed): `platinum/firm/partner_analytics.json` +
`header_metrics_fresh` LastModified = 2026-06-12 evening; AUA ~ $204.6M (Orion ground truth).
MDPF leg: next scheduled run consumes fresh inf inputs (assess re-fire need after platinum lands).
Note for readers: today's _BRONZE_COMPLETE (orion-api/2026-06-12) was overwritten by the
transactions-scoped re-fire (1-dim manifest); the morning 7-dim manifest is in the version trail.

## Structural follow-ups (TO candidates, routed COO — none executed tonight)

a. Collapse `code/bronze/` vs `code/bronze-runner/` dual prefix (single source of truth)
b. `_BRONZE_COMPLETE` carries a REQUIRED-dim set ('success' with a dim absent = silent-partial class)
c. Extend deployed-checks (comp-pipescript) to bronze-runner prefixes (firm-scoped TO exists)
d. MDPF artifacts carry source-data vintage, not just runtime (F1-provenance class)
e. inf-api-txn D-1 default vs same-day quorum — complete the v2 cutover OR move the default;
   today = the D-1 lag colliding with the half-cutover
f. Collision-guard FATAL needs a loud channel (CW metric/SNS + lock-holder liveness check);
   today's gold outage was silent from 13:00Z until a human noticed
g. On-instance bootstrap-baked scripts (inf-bronze-fetch.sh) need a refresh path — S3 updates
   don't propagate to running instances (user-data runs once)
h. Gold-runner auto-shutdown arms on ANY chain completion without checking for OTHER running
   chains — tonight's concurrent eclipse chain nearly killed the in-flight full chain at 21:27Z
   (cancelled manually). Single-tenancy assumption needs a running-chain guard.
