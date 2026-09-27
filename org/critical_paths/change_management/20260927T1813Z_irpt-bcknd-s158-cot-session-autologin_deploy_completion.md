# Deploy Completion Record
**Date opened:** 2026-09-27T18:13:46.059552+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND-S158: cot BD session auto-login succeeds again (log-on-failure + named cause fix)
**Authored by:** 0.6.2_AE_PartnerETL~S
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | read the box's own /tmp/cot-session-autologin-*.log via SSM and name the cause per failed day | ssm:<command_id> + the deliverable JSON path |  | OPEN |
| L2 | git | ssm.tf step uploads the log on failure (exit code captured without set -e aborting first) committed on CLOUD | commit hash + push state |  | OPEN |
| L3 | activation | safe-apply of aws_ssm_document.cot_bd_session_fetch so the LIVE document carries the log-on-failure step | aws ssm get-document read of the live Content |  | OPEN |
| L4 | ec2-baked-asset | the named cause fixed inside the grant and S3->box deployed to /opt/bd-cot-auto-login | SSM cat/md5 of the RUNNING path |  | OPEN |
| L5 | verify | ONE Success of opal-cot-bd-session-fetch that moves blackdiamond/cot/session AWSCURRENT | ssm:<command_id> Success + the new AWSCURRENT version id/CreatedDate |  | OPEN |

## Log

- 20260927T181346Z OPENED by 0.6.2_AE_PartnerETL~S with 5 leg(s)
