# Deploy Completion Record
**Date opened:** 2026-07-23T20:36:16.995946+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260723T210717Z
**Deploy:** Key-scoped disable of legacy smartx Step-4/producer write to json/portfolios/account-distribution.json (CTO 201005Z/202659Z -- 3-firm bell clobber kill)
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| opal-smartx-ingestion-pipeline | tf-lambda | aws_lambda_function.ingestion_pipeline | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | Output set grounded FIRST (condition 1): save_results() writes exactly 2 keys -- portal bell json/portfolios/account-distribution.json (now gated) + legacy opal-data-smartx-v2/views/account_distribution.json (untouched); nothing keys on the portal write's completion (handler status derives from main() succeeding, lambda_function.py:53-61; still succeeds on skip path). TF-only (condition 2): DISABLE_PORTAL_BELL_WRITE=1 via environment block, commit a14ae124d BEFORE apply, artifact rebuilt via ci/build-and-upload.sh (upload sha-VERIFIED), safe-apply -target=aws_lambda_function.ingestion_pipeline, live get-function-configuration ties CodeSha256 WCYA9UaS/x7XkU0e3kGnyS8Kgl/DWVmAKqwMNuOjVj0= + env flag PRESENT, re-plan No-changes 0-diff. Source comments citing CTO 201005Z/202659Z + producer conflict in BOTH .py copies (canonical + lambda build source, synced) + lambdas.tf (condition 3). BEHAVIORAL EXERCISE both directions (stubbed S3): flag SET -> portal put ABSENT + legacy put fired; flag UNSET -> portal put FIRED (the mutant proving the gate can fail). Schedule grounded: EventBridge cron(30 11)Z daily, eventbridge.tf:45 -- disable lands before tomorrow's run. Tag smartx-pipeline-bell-disable-v1.0.0. COO byte-verifies the bell key past tomorrow's 11:30Z window (bell ETag must remain the revamp's). Flagged, not actioned: same clobber class on json/portfolios/aum-{metrics,timeseries}.json via the third producer; pre-existing smartx-workspace bundle drift (3 files); pre-existing smartx-model-monthly-pull build parity failure. | CLOSED 20260723T210717Z |

## Log

- 20260723T203616Z OPENED by 0.7.0_AE_CloudOps with 1 leg(s)
- 20260723T210717Z LEG opal-smartx-ingestion-pipeline closed: Output set grounded FIRST (condition 1): save_results() writes exactly 2 keys -- portal bell json/portfolios/account-dis
- 20260723T210717Z CLOSED -- all 1 legs proven
