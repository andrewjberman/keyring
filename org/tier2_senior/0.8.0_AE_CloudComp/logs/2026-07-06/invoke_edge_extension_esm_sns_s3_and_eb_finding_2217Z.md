# Invoke-edge extension (ESM/SNS + S3-notif, LIVE-grounded) + EventBridge-in-modules finding

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, VALIDATE

## Summary
Window 1851Z->2217Z. Extended comp-blast/comp-iam blast-radius coverage to the remaining non-code
Lambda-invoke mechanisms, LIVE-grounded per Andrew-direct. Companion to SFNBRIDGE (which added Step
Functions this session). Net: comp-blast now sees SFN + SQS/stream(ESM) + SNS + S3 = all non-code invoke
mechanisms. Then verified + banked an EventBridge-in-modules coverage gap as a deliberate design-fork TO
(correctly did NOT rush a SEV1-pass redesign at the marathon tail). All 3 commits RAVC-accepted by COO;
CTO confirmed the dual-edge design; genuine standby COO-accepted.

## What happened

### extract_event_invoke.py (Pass 8) -- LIVE-derived, 11 edges (commits 22862b811, 515287343, 7ad3334aa)
Scoped-first (the discipline that paid off): of ~14 aws_sns_topic_subscription in TF, only 1 is
protocol=lambda -- naive bridging would have emitted ~13 FALSE edges (email/sms/sqs, incl the bd-49f
cookie-alerts email-sub Andrew flagged).
- Andrew-STEER: ground on LIVE, not static .tf. This CAUGHT A PHANTOM -- the served-guard-49f ESM is
  declared-in-TF-but-NOT-deployed-live; a static parse would have added a false 49f blast edge. Deploys
  are TF-only (TF-declared front-runs live), so LIVE = the truly-deployed blast grain.
- Pass 8 bridges 3 mechanisms via read-only boto (list_event_source_mappings + list_subscriptions +
  per-bucket get_bucket_notification_configuration), dual-direction edges (EVENT/SNS/S3_INVOKES +
  _INVOKED_BY, mirroring SFN + CALLS/CALLED_BY), graceful no-op without creds:
  - 3 ESM: SQS opal-cot/inf-served-guard-recheck -> guards; opal-globgrph-incremental-events -> updater.
  - 1 SNS(protocol=lambda): inf-otp-alert -> inf-ec2-retry-launch.
  - 7 S3 bucket-notification (LIVE-VERIFY found a real gap on CORE lambdas): opal-data-bd ->
    bd-allocation-processor/bd-gold-trigger/bd-silver-merge; opal-data-inf -> inf-portal-publisher/
    inf-silver-aggregator; opal-data-portal-v2 -> yang-pipeline-trigger/opal-security-scanner-processor.
- CTO note folded: provenance="live-derived" on every edge/node + a could-not-verify WARN when the live
  calls can't run (a creds-less rebuild's MISSING edge reads as could-not-verify, not nonexistence --
  the honest-vintage discipline on the SEV1 surface).
- Exercised (Rule 22, built cache = 11 edges): comp-blast inf-ec2-retry-launch -> SNS_TOPIC(1) inf-otp-
  alert; opal-globgrph-incremental-updater -> SQS_QUEUE; bd-gold-trigger -> S3_BUCKET(1) opal-data-bd;
  yang-pipeline-trigger -> opal-data-portal-v2. comp-surface-check CLEAN before+after every commit.

### EventBridge-in-modules VERIFY -- real ~14-edge gap, BANKED as a deliberate TO (not built)
Live EventBridge->Lambda = ~45 edges; static extract_eventbridge (scans only pipeline_dir/eventbridge.tf)
has ~31 -> MISSES ~14 (incl the module-embedded opal-cot/inf-served-guard-on-write I predicted, plus
value-parity/freeze-monitor/tool-activity-freshness/seeking-alpha/trade-parquet/volatility/yang-refresh/
security-sweep). Root cause = same static-misses-live lesson as the 49f phantom, now on EventBridge.
JUDGMENT: unlike ESM/SNS/S3 (net-new mechanisms), this OVERLAPS an EXISTING SEV1 pass -> a design fork
(a: migrate-to-live / b: live+dedup / c: broaden-static), regression-risky. Correctly did NOT rush a
SEV1-pass redesign at the marathon tail; RAVC'd the finding + recommendation to COO, who BANKED it as a
deliberate CTO-design-decided TO. COO: "the right call, not a coast."

## Compiler Tools
| Tool | Command | Result |
|---|---|---|
| (live-verify) | aws lambda list-event-source-mappings; sns list-subscriptions (protocol=lambda); s3 per-bucket get-bucket-notification-configuration x35; events list-rules->targets | Grounded the real invoke edges LIVE; caught the 49f phantom + the 7 S3 + the ~14 EB-gap |
| comp-blast | before/after on inf-ec2-retry-launch, opal-globgrph-incremental-updater, bd-gold-trigger, yang-pipeline-trigger | invokers now surfaced (SNS/SQS/S3 in blast radius) |
| comp-surface-check | check --file extract_event_invoke.py/trace_graph.py (each commit) | CLEAN (no critical-surface regression on comp-blast/comp-iam) |
| comp-build | rebuild x2 (ESM/SNS, then +S3) | 11 invoke edges in built cache, no phantom 49f |
| ds-commit-gate | extract_event_invoke.py / trace_graph.py (each commit) | PASS (+ own log-open-lint block-mode clean on the new files) |

**What worked:** scope-then-live-verify BEFORE building -- caught a phantom (49f) + a bigger-than-est gap
(7 core-lambda S3 edges) + the ~14-edge EB gap, all without emitting a false edge. **What failed:** two
safe-commit timeouts (surface-check graph-load / lock contention) -- commit landed each time, push lagged,
re-pushed. **Gap found + banked:** extract_eventbridge misses ~14 live EB->Lambda (module-embedded + non-
eventbridge.tf rules) -> deliberate live-migration TO.

## Blockers
None on me. Genuine standby (COO-accepted). Open threads = REAL external/design gates: async CVO certs
(SFNBRIDGE + all invoke-edges, owner-dormant on ~A oracle + CVO~B), TH-C (external DRV-flip/D1-GREEN gate),
EB-live-migration (banked TO, CTO design-pending a/b/c).

## Current State
- extract_event_invoke.py (org/modules/graph/, Pass 8 in trace_graph.build_graph) LIVE + committed
  (7ad3334aa): 11 live-derived invoke edges (3 ESM + 1 SNS + 7 S3), dual-direction, provenance-labeled,
  could-not-verify WARN. comp-blast now covers SFN + SQS/stream + SNS + S3.
- SFNBRIDGE (extract_sfn.py, Pass 7) LIVE + CTO-design-confirmed (dual-edge); cert async.
- utf-8-log lint (org/modules/graph/compproof/log_open_lint.py) LIVE in ds-commit-gate BLOCK-MODE.
- HEAD 7ad3334aa synced to origin/CLOUD.

## Next Steps
1. **[2.0.0_SA_COO]** dispatch the async certs on owner spin-up: ~A 26-invoke oracle re-diff (SFNBRIDGE) +
   CVO cert (SFNBRIDGE + all invoke-edges); route CTO the EB-live-migration design call (a/b/c) when scoped.
2. **[me]** on cert-return: close SFNBRIDGE + invoke-edges. On EB-TO GO: build the extract_eventbridge
   live-migration (fresh pass, design-decided, regression-guard the 31-edge static coverage).
3. **[external]** TH-C parked on the COMPLEARN DRV-flip/D1-GREEN unlock.
