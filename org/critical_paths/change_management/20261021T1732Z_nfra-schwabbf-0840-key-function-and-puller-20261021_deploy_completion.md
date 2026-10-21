# Deploy Completion Record
**Date opened:** 2026-10-21T17:32:10.845187+00:00
**Status:** OPEN
**Deploy:** NFRA_SCHWABBF 0840 key function and puller
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L7 | activation | data/black_diamond/scripts/bronze/_monolith_bronze.py to its code home (the pre-push gate deploys it) | head-object ETag equals the repo file md5 |  | OPEN |
| L8 | activation | infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1 to s3://opal-data-assets/code/canonical-schwab-si2/sdd-daily-pull.ps1 | head-object ETag equals the repo file md5 |  | OPEN |

## Log

- 20261021T173210Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 2 leg(s)
