# Deploy Completion Record
**Date opened:** 2026-06-15T20:19:28.288484+00:00
**Status:** OPEN
**Deploy:** ADHC_GLDINC/49NNAFIX D1: D_00f.advisor_nna_canonical served-movement publish + dispatcher wiring (2-lane: DS .py + AE dispatcher; CVO size-gate=never-widen sign-off 200904Z)
**Authored by:** 0.6.0_AE_PartnerETL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 24.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | DS D_00f.advisor_nna_canonical.py commit 89d4ac6a7 | commit hash pushed | commit 89d4ac6a7 pushed (DS D_00f.advisor_nna_canonical.py) | CLOSED 20260615T202055Z |
| L2 | s3-prefix | D_00f.py to opal-data-bd/code/gold/ | comp-pipescript deployed D_00f MATCH row | v2 (gzip transfer-fix, supersedes v1 4eab7327): D_00f.py gzip re-deploy commit 81798abf0, code md5==S3 ETag 668f873d2d5c42be76429f56b7250d16; comp-pipescript D_00f MATCH (repo==deployed gzip) | CLOSED 20260615T202918Z |
| L3 | verify | first served publish platinum/firm/advisor_nna_canonical.json | served object Size+LastModified+reconciliation.all_pass independently verified | v2 (gzip, supersedes v1 34MB/cd9d4e33): served platinum/firm/advisor_nna_canonical.json Size 1760321 Content-Encoding=gzip ETag d37a0ce8 LM 2026-06-15T20:26:25Z; AE-independently gunzip'd -> valid JSON parity-exact (firm MAX 1373359476.76 + all_pass present), zero data loss | CLOSED 20260615T202918Z |
| L4 | verify | CVO gate-4 DistributionTab live render-no-freeze on the 34MB json | CVO served-render verdict |  | OPEN |
| L5 | activation | PHASE_D5 wiring live in gold_dispatch.sh + runner-IAM PutObject | bash-n clean + D_00f at PHASE_D5 + deployed s3 md5==ETag + bd-exporter-ec2-role PutObject opal-data-bd/* confirmed | gold_dispatch.sh deployed code/gold/ md5==ETag c91a133579516d8706fed9d53162705c (commit 0f62f6720); PHASE_D5 (run_background D_00f + wait_phase) present in DEPLOYED copy; bash -n clean; runner-IAM bd-exporter-ec2-role s3:PutObject on opal-data-bd/* confirmed (cross-firm-deny=cot-only) | CLOSED 20260615T202055Z |

## Log

- 20260615T201928Z OPENED by 0.6.0_AE_PartnerETL with 5 leg(s)
- 20260615T202055Z LEG L1 closed: commit 89d4ac6a7 pushed (DS D_00f.advisor_nna_canonical.py)
- 20260615T202055Z LEG L2 closed: comp-pipescript deployed D_00f -> [bd-gold] D_00f MATCH (1 MATCH 0 STALE 0 MISSING); .py md5==ETag 4eab7327
- 20260615T202055Z LEG L3 closed: served object independently verified: platinum/firm/advisor_nna_canonical.json Size=34019956 LastModified=2026-06-15T20:
- 20260615T202055Z LEG L5 closed: gold_dispatch.sh deployed code/gold/ md5==ETag c91a133579516d8706fed9d53162705c (commit 0f62f6720); PHASE_D5 (run_backgr
- 20260615T202918Z LEG L2 closed: v2 (gzip transfer-fix, supersedes v1 4eab7327): D_00f.py gzip re-deploy commit 81798abf0, code md5==S3 ETag 668f873d2d5c
- 20260615T202918Z LEG L3 closed: v2 (gzip, supersedes v1 34MB/cd9d4e33): served platinum/firm/advisor_nna_canonical.json Size 1760321 Content-Encoding=gz
