# Deploy Completion Record
**Date opened:** 2026-06-26T13:19:26.920343+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260626T133725Z
**Deploy:** ADVI_COTETL.L4-GUARD Part-A cot detection layer (keepalive + freshness-probe + SNS/alarms)
**Authored by:** 0.6.0_AE_PartnerETL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit cot detection-layer source | 33cf3ec71 pushed (+tag) | commit 33cf3ec71 (source) + 2051dbf81 (artifacts) + da9e1ff46 (core-doc) + 5553be70b (deploy-record); tag cot-pipeline-v0.5.0 pushed to CLOUD | CLOSED 20260626T133155Z |
| L2 | s3-prefix | cot-pipeline/{bd-cot-keepalive,bd-cot-freshness-probe}.zip artifacts uploaded | build-and-upload SHA256 line | bd-cot-keepalive.zip sha256=5SwJUgEincPpOYF6/HH9Fe8oT4SSN4bOa5kkyndt6sk=; bd-cot-freshness-probe.zip sha256=pznw5mLI8aZ6951zv18ExFq61oQ+JM1R0OCuueeRgMo=; uploaded to opal-313476888478-lambda-artifacts/cot-pipeline/, TF s3_object_version resolved in plan | CLOSED 20260626T133156Z |
| L3 | verify | comp-iam TF-vs-live reconcile: opal-data-bd Deny LIVE-applied on both cot roles (firm-sep, CTO condition) | comp-iam output | comp-iam service: all ops GRANTED both lambdas; comp-iam gaps: 0 gaps for new fns. AUTHORITATIVE live get-role-policy: bd-cot-keepalive-role + bd-cot-freshness-probe-role BOTH carry DenyBdPlane (Deny s3:* on opal-data-bd + /*) LIVE-applied. (comp-iam reconcile census stale 06-03 = coverage gap; live get-role-policy is ground truth.) | CLOSED 20260626T133156Z |
| L4 | activation | terraform safe-apply: 2 Lambdas + 2 EventBridge rules + SNS topic+sub + 7 alarms; 0-diff replan | apply summary + 0-diff | safe-apply (HALT_ACK=1, HALTGT passed): 25 added 0 changed 0 destroyed; 0-diff replan = 'No changes. Your infrastructure matches the configuration.' | CLOSED 20260626T133156Z |
| L5 | verify | EXERCISE detection (AC#1): a stale/missing cot session TRIPS an alarm to opal-critical-surface-alerts + egress test_alert delivers | alarm ALARM-state + delivery proof | EXERCISED LIVE (not config-only): bd-cot-freshness-probe real run detected the live cot freeze -> trading_day_lag=3 (>2) all 4 tables; 4x bd-cot-silver-stale alarms transitioned INSUFFICIENT_DATA->ALARM; CloudWatch alarm-history 'Successfully executed action' to BOTH opal-critical-surface-alerts AND opal-bd-cot-cookie-alerts; COO SQS rider opal-critical-surface-alerts-coo depth=5+2 (delivery landed). test_alert egress published:true on both lambdas. keepalive real run {ok:true,status:204} (cookie live, session extended). | CLOSED 20260626T133725Z |

## Log

- 20260626T131926Z OPENED by 0.6.0_AE_PartnerETL with 5 leg(s)
- 20260626T133155Z LEG L1 closed: commit 33cf3ec71 (source) + 2051dbf81 (artifacts) + da9e1ff46 (core-doc) + 5553be70b (deploy-record); tag cot-pipeline-v
- 20260626T133156Z LEG L2 closed: bd-cot-keepalive.zip sha256=5SwJUgEincPpOYF6/HH9Fe8oT4SSN4bOa5kkyndt6sk=; bd-cot-freshness-probe.zip sha256=pznw5mLI8aZ6
- 20260626T133156Z LEG L3 closed: comp-iam service: all ops GRANTED both lambdas; comp-iam gaps: 0 gaps for new fns. AUTHORITATIVE live get-role-policy: b
- 20260626T133156Z LEG L4 closed: safe-apply (HALT_ACK=1, HALTGT passed): 25 added 0 changed 0 destroyed; 0-diff replan = 'No changes. Your infrastructure
- 20260626T133725Z LEG L5 closed: EXERCISED LIVE (not config-only): bd-cot-freshness-probe real run detected the live cot freeze -> trading_day_lag=3 (>2)
- 20260626T133725Z CLOSED -- all 5 legs proven
