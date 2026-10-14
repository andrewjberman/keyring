# Deploy Completion Record
**Date opened:** 2026-10-14T11:20:21.736053+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261014T114046Z
**Deploy:** NFRA_OPLGTW OG-ap-14 B2: the r30 gateway release (OG-pf-1 + OG-tg-1 + OG-bd-2 + OG-sh-1) to opal-gateway, release 90967e39ba on live 43088464f5
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | box/sitez and rel-nfra-oplgtw-r30c carry release 90967e39ba4bdca17c6f84d9806c29cc67f8482e; EC2_MANIFEST deployed_commit and file_checksums come from the release blobs; runbook 7.2 names the new live release | the deploy commit hash plus rb.AC2 PASS | Release 90967e39ba4bdca17c6f84d9806c29cc67f8482e on rel-nfra-oplgtw-r30c (deploy record 8e0350afc2 on that branch). box/sitez carries the DEPLOY RECORD at ffa350b8b1 -- EC2_MANIFEST deployed_commit 90967e39ba, previous_deployed_commit 43088464f5 (trunk's genuine previous, not the release branch's stale 2c0f84966d), all 10 file_checksums RECOMPUTED from the release blobs with 4 changed -- plus runbook 7.2 naming the new live release. rb.AC2 PASS: live 90967e39ba, 7.2 names live=yes, 3 targets, 0 without guard, 0 not in manifest history. The release branch was deliberately NOT merged into box/sitez: it descends from the deploy-only cut lineage, an attempt opened 18 conflicts and was aborted with nothing landed. | CLOSED 20261014T114045Z |
| L2 | ec2-baked-asset | /opt/opal-gateway on i-07dccb1615503ac99 runs the release bytes | one SSM md5 read of the RUNNING path over app/, deploy/, dashboard/ equal to the release blobs (an S3 or repo read is NOT valid proof for this leg) | ONE SSM md5 read of the RUNNING path on i-07dccb1615503ac99 over app/, deploy/, dashboard/ (command 90a38694-9d3f-4906-a2bd-fb8dd4607a31): 105 of 105 EQUAL to the release blobs, 0 differing, 0 repo-only; and 5 DIFFERING against the old base 43088464f5 (app/audit.py, app/data_entitlement.py, app/destructive_ops.py, app/identity_scope.py, app/tools.py) -- the negative arm, so the host demonstrably moved rather than merely matching. The 10 host-only files are built dashboard assets the repo does not track. No S3 or repo read was used as proof for this leg. | CLOSED 20261014T114045Z |
| L3 | verify | the served read through the INSTALLED code: AP14_SERVED.json's nine fields, including C2's bbg_identity_admitted_8 = 8 and objects_written 0 | the ssm_command_id plus the nine fields, then ap14.AC2.sh PASS | AP14_SERVED.json, ssm_command_id a36298ab-1572-4929-8cba-ca603736a092, read in-process on the host under the SERVICE'S OWN interpreter /opt/opal-gateway/.venv/bin/python with synthetic principals, no Graph call, nothing written. All nine fields: installed_code true (every module __file__ under /opt/opal-gateway), data_grant_family_size 6, bd_unprofiled_standard_denied true, bd_unprofiled_master_admin_admitted true, list_shared_folder_listed true, list_shared_folder_safe true, opal_users_gate_refuses_non_opal true, objects_written 0, and C2's bbg_identity_admitted_8 = 8 with bbg_identity_denied empty. The identity came from the installed module's own pinned constant app.identity_scope.OPAL_USERS_ONLY per A7, never typed; recorded as sha256(lower)[:10] f39c9b2025. list_shared_folder_safe first read FALSE from my own wrong-shape call (classify() returns a dict, I read .value off it); corrected to read ['class'] -- the release was never at fault. | CLOSED 20261014T114045Z |

## Log

- 20261014T112021Z OPENED by 0.7.0_AE_CloudOps~Z with 3 leg(s)
- 20261014T114045Z LEG L1 closed: Release 90967e39ba4bdca17c6f84d9806c29cc67f8482e on rel-nfra-oplgtw-r30c (deploy record 8e0350afc2 on that branch). box/
- 20261014T114045Z LEG L2 closed: ONE SSM md5 read of the RUNNING path on i-07dccb1615503ac99 over app/, deploy/, dashboard/ (command 90a38694-9d3f-4906-a
- 20261014T114045Z LEG L3 closed: AP14_SERVED.json, ssm_command_id a36298ab-1572-4929-8cba-ca603736a092, read in-process on the host under the SERVICE'S O
- 20261014T114046Z CLOSED -- all 3 legs proven
