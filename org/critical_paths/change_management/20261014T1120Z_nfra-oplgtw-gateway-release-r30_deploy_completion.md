# Deploy Completion Record
**Date opened:** 2026-10-14T11:20:21.736053+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-ap-14 B2: the r30 gateway release (OG-pf-1 + OG-tg-1 + OG-bd-2 + OG-sh-1) to opal-gateway, release 90967e39ba on live 43088464f5
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | box/sitez and rel-nfra-oplgtw-r30c carry release 90967e39ba4bdca17c6f84d9806c29cc67f8482e; EC2_MANIFEST deployed_commit and file_checksums come from the release blobs; runbook 7.2 names the new live release | the deploy commit hash plus rb.AC2 PASS |  | OPEN |
| L2 | ec2-baked-asset | /opt/opal-gateway on i-07dccb1615503ac99 runs the release bytes | one SSM md5 read of the RUNNING path over app/, deploy/, dashboard/ equal to the release blobs (an S3 or repo read is NOT valid proof for this leg) |  | OPEN |
| L3 | verify | the served read through the INSTALLED code: AP14_SERVED.json's nine fields, including C2's bbg_identity_admitted_8 = 8 and objects_written 0 | the ssm_command_id plus the nine fields, then ap14.AC2.sh PASS |  | OPEN |

## Log

- 20261014T112021Z OPENED by 0.7.0_AE_CloudOps~Z with 3 leg(s)
