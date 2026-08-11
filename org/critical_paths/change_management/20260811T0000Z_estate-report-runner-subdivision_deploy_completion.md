# DEPLOY COMPLETION LEDGER -- estate-report-runner SUBDIVISION

**Opened:** 2026-08-11T00:00Z by `1.0.0_SA_CTO~A`
**Status:** CLOSED 2026-08-11T00:08Z -- both legs verified, hashes match

## What

Deploy commit `959236f60d` (the subdivided Kimi call architecture, SPEC @58505c291,
Andrew-direct "No bridge, move to the subdivision now" 08-06, re-GO'd 08-10 ~23:1xZ,
executed at CTO~A per Andrew closing the ~B lane) to the one production leg:

- `s3://opal-estate-report/code/estate_report_runner.py`
  (the EC2 service pulls this key at every start -- `instance.tf:215` ExecStartPre;
  no TF change needed: no env vars added, schedule untouched, instance untouched)

## Pre-state (verified live before upload)

- Deployed object: 99,270 bytes, ETag `d292af7eb17250c50eb0382cef5372db`,
  LastModified 2026-08-07T09:45:47Z (the monolith)
- Repo file post-commit: `infra/aws/ec2/estate-report-runner/estate_report_runner.py`
  @959236f60d

## Legs

1. [x] `aws s3 cp` repo file -> `s3://opal-estate-report/code/estate_report_runner.py`
       (uploaded 2026-08-11T00:08:06Z)
2. [x] head-object verify: ContentLength 120,980 == local 120,980; ETag
       `223b3103204100c17063fe48f2f90af1` == local md5 `223b3103204100c17063fe48f2f90af1`

## Close condition

Both legs checked, hashes match. First live exercise = next scheduled 09:00 ET fire
(EventBridge Scheduler `estate_report_0900et`, untouched). CVO verifies the landing
against the 7-day baseline per their standing role. NO new watcher/monitor armed
against the fire (moratorium).
