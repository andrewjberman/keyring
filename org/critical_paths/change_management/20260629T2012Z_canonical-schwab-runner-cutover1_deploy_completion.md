# Deploy Completion Record
**Date opened:** 2026-06-29T20:12:09.887845+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260629T203810Z
**Deploy:** CUTOVER-1 S4/S6b/S8: stand up canonical-schwab-runner (role+instance+trigger+alarm) + first-build proof
**Authored by:** 0.6.0_AE_PartnerETL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD code commit (runner bundle+TF) pushed | hash pushed | code commits 537359cca + 15e3a25b9 + be0b76358 pushed to CLOUD (runner bundle + TF + controlled-rollout tweak) | CLOSED 20260629T201349Z |
| L2 | s3-prefix | opal-data-bd code/canonical-schwab-runner/ AE runner code | s3 ls staged objects | s3 ls opal-data-bd/code/canonical-schwab-runner/: run-canonical.sh(3616) s8_gate.py(5084) setup-instance.sh(3585) user-data.sh(855), AES256 | CLOSED 20260629T201544Z |
| L3 | verify | safe-apply role+instance+trigger+alarm | apply summary + post-apply 0-diff plan | safe-apply: 12 added 0 changed 0 destroyed; instance i-06b81054307cfb02c; post-apply plan = No changes (0-diff) | CLOSED 20260629T201836Z |
| L4 | verify | runner role live get-role-policy = pinpoint (schwab 01_raw-only, bd reads, AES256 put, sns:Publish) | get-role-policy output | live get-role-policy: schwab=01_raw-only(GetObject), bd reads=canonical/schwab+code/canonical/schwab+code/canonical-schwab-runner+schwab/silver/account_xref+silver/allocations+silver/fees, WriteCanonicalSSE=PutObject canonical/schwab w/ AES256 condition, ListBd prefix-scoped -- pinpoint confirmed | CLOSED 20260629T201836Z |
| L5 | verify | controlled SSM --dry-run validates the chain (no 403, role reads complete) | SSM RunCommand output | SSM dry-run on i-0ed92ce2e72f505dc: DEPS_OK, aws-cli 1.45.37 (pip, no opsworkscm), CODE_SYNCED (role reads code+canonical+01_raw OK), orchestrator date=2026-06-24, account_gains window computed, 25/25 steps planned | CLOSED 20260629T203516Z |
| L6 | verify | controlled live run produces a real canonical gold partition in S3 (NEVER#7) | s3 ls canonical/schwab/gold partition | LIVE build 25/25 OK on i-0ed92ce2e72f505dc; S3-verified: 14 gold partitions date=2026-06-24, portal_aggregates LastModified 20:36:37Z size 20585 SSE=AES256 -- real fresh encrypted partition, builder reads (xref/allocations/fees) all OK no 403 | CLOSED 20260629T203810Z |

## Log

- 20260629T201209Z OPENED by 0.6.0_AE_PartnerETL with 6 leg(s)
- 20260629T201349Z LEG L1 closed: code commits 537359cca + 15e3a25b9 + be0b76358 pushed to CLOUD (runner bundle + TF + controlled-rollout tweak)
- 20260629T201544Z LEG L2 closed: s3 ls opal-data-bd/code/canonical-schwab-runner/: run-canonical.sh(3616) s8_gate.py(5084) setup-instance.sh(3585) user-d
- 20260629T201836Z LEG L3 closed: safe-apply: 12 added 0 changed 0 destroyed; instance i-06b81054307cfb02c; post-apply plan = No changes (0-diff)
- 20260629T201836Z LEG L4 closed: live get-role-policy: schwab=01_raw-only(GetObject), bd reads=canonical/schwab+code/canonical/schwab+code/canonical-schw
- 20260629T203516Z LEG L5 closed: SSM dry-run on i-0ed92ce2e72f505dc: DEPS_OK, aws-cli 1.45.37 (pip, no opsworkscm), CODE_SYNCED (role reads code+canonica
- 20260629T203810Z LEG L6 closed: LIVE build 25/25 OK on i-0ed92ce2e72f505dc; S3-verified: 14 gold partitions date=2026-06-24, portal_aggregates LastModif
- 20260629T203810Z CLOSED -- all 6 legs proven
