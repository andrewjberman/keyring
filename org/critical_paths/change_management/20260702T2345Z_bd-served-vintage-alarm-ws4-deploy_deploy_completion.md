# Deploy Completion Record -- bd-served-vintage-alarm (ADVI_BDAPIMIG P1 (d), WS-4 fail-loud served-vintage PAGE layer)

**Date opened:** 2026-07-02T23:45Z (apply-start)
**Date closed:** 2026-07-02T23:58Z -- CLOSED. All legs proven end-to-end: apply 15-add/0-change/0-destroy (== reviewed) + 0-diff re-plan ("No changes") + firm-sep IAM LIVE (DenyCotPlane + bd-platinum-only + namespace-scoped metric, Rule-22a) + FUNCTIONAL invoke (200, all 5 keys checked=true tdb=1 stale=false any_stale=false) + METRIC LANDED (ContentVintageStale=0 + ContentVintageTradingDaysBehind=1 in CloudWatch, verified live not rc=0) + all 7 alarms present/wired/OK + non-false-page sanity (07-01 = 1 trday behind < page 2 = stale 0). Tagged bd-v2.46.0.
**Deploy:** The WS-4 ENFORCEMENT layer (COO drive-to-completion 223155Z): a scheduled Lambda (`bd-served-vintage-alarm`, rate 1h) reads each bd platinum SERVED artifact's data_as_of via DE's single-source `lib/served_vintage.served_vintage_lag_from_s3` (08bce489c) + `lib/trading_calendar`, emits `Opal/ServedFreshness ContentVintageStale` per served key; a CloudWatch alarm pages `opal-bd-49f-cookie-alerts`. Keyed on CONTENT vintage (data_as_of), NOT the runner exit code -- closes the exact bd-49f freeze class (mtime moved on re-emit while data_as_of stood still @06-29). Config-driven single-source (yamldecode gold_freshness_config.yaml), full served-key coverage (5), fail-loud triad.
**Authored by:** 0.6.0_AE_PartnerETL
**Class:** deploy-completion (NEVER rule -- opened at apply-start, closed at completion; no half-land)

## Authorization
- Andrew-direct sovereign RATIFIED (2026-07-02T182117Z cookie-REST go-forward; WS-4 alarm is the (d) completion piece of the same P1).
- CTO GATE-1 BLESSED the quartet incl. (d) fail-loud alarm shape (195658Z).
- COO DRIVE-to-completion (223155Z): "the WS-4 ENFORCEMENT layer -- the detection (oracle) is CVO-certed conditional; your alarm makes it a hard gate. Drive it."
- Full-apply constraint LIFTED (0.5.0 234319Z): bd-TF drift #1 CTO 0-diff arch-signed CLOSED; full bd-applies safe (no re-enable landmine).

## Pre-apply state (all GREEN)
- Source committed af4c9ab2f (Lambda config-driven + TF + source-map + vendored libs); sha-bump f1dcfc61a.
- Artifact built+uploaded: bd-pipeline/bd-served-vintage-alarm.zip (SHA256 kc3BThbDWZeBlRXk3RdB81874JEqgG607wWksc2x7nk=, 12K; lambda_function+served_vintage+trading_calendar).
- DE deps LIVE: lib/served_vintage.py (08bce489c) + lib/trading_calendar.py; gold_freshness_config.yaml 5 trading-day-frontier served entries (frontier_page_trading_days=2).
- `terraform validate` = Success; `terraform console` confirmed the yamldecode filter -> exactly the 5 served keys; SERVED_KEYS_JSON correct.
- REVIEW PLAN: **15 to add, 0 to change, 0 to destroy** -- EXACTLY the (d) resources, NO drift swept (fallback landmine confirmed gone).

## The deploy
- `safe-apply` (HALTGT) infra/aws/terraform/bd-pipeline: adds module.bd_served_vintage_alarm (Lambda + log group) + aws_iam_role.bd_served_vintage_alarm(+policy+attach) + event rule/target/permission + 5x aws_cloudwatch_metric_alarm.bd_served_vintage_stale (for_each) + absence alarm + errors alarm.
- Expected: 15 adds, 0 change, 0 destroy.

## Verification bar (Rule-22a applied-layer, verify SERVED/live not rc=0)
1. Apply plan == the reviewed 15-add/0-change/0-destroy (no unexpected drift).
2. Apply 0-diff (second plan = No changes).
3. FIRM-SEP IAM LIVE: `aws iam get-role-policy --role-name bd-served-vintage-alarm-role` shows DenyCotPlane + ReadBdServedPlatinum (opal-data-bd platinum) + namespace-scoped PutMetricData (Rule-22a applied-layer, LIVE not comp-iam DESIRED).
4. FUNCTIONAL: manual `aws lambda invoke` -> returns any_stale + per-key results; CloudWatch `Opal/ServedFreshness ContentVintageStale` datapoints published for all 5 served keys (verify the metric actually landed, not just rc=200).
5. ALARMS EXIST + wired: 5 per-key + absence + errors alarms present, alarm_actions = opal-bd-49f-cookie-alerts; EventBridge rule ENABLED.
6. NON-FALSE-PAGE sanity: with served 07-01 (<=2 trading days behind frontier), stale should be 0 (not a cry-wolf); an intentionally-absent key would read stale=1 (fail-loud).

## Rollback
`terraform destroy -target` the new resources (or revert af4c9ab2f + re-apply). NO data mutation (read-only S3 GET + PutMetricData). No existing resource touched (0 change/0 destroy). The scrape/ingest/gold paths are untouched.

## Status log
- 2026-07-02T23:45Z OPENED at apply-start. Pre-apply GREEN. Review plan = 15 add / 0 change / 0 destroy. Running safe-apply.
