# Deploy Completion Record
**Date opened:** 2026-09-03T09:21:55.357351+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260903T092654Z
**Deploy:** NFRA_OPSEC202609.TO-OP-S-8 -- PITR + deletion protection on the partner identity tables (module partner-firm-table, 3 instantiations); opal-users-v2 limb HELD on row Z-S15; demo limb DEFERRED to round 2 per issuer 19600
**Authored by:** 0.7.0_AE_CloudOps~S
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | module edit committed on SITEZ under 0.7.0_AE_CloudOps~S | commit hash | commit f5859c4097 on SITEZ, author 0.7.0_AE_CloudOps~S -- modules/partner-firm-table/main.tf (PITR + deletion_protection_enabled), row S14, TO status staged->pending, ledger entry; 4 files / 107 insertions / 2 deletions; row gate rc=0; no lane refusal on modules/ or partner-firms/ | CLOSED 20260903T092348Z |
| L2 | activation | safe-apply of infra/aws/terraform/partner-firms (0 add, 3 change, 0 destroy, 0 replace) | apply output | safe-apply rc=0 (comp-tagauthz PASSED, tombstone-gate CLEAN 0 creates). All three Modifying/in-place. 'Apply complete! Resources: 0 added, 3 changed, 0 destroyed.' | CLOSED 20260903T092653Z |
| L3 | verify | PITR + DeletionProtectionEnabled read ENABLED/true on all 3 partner tables, TableId identical before/after (no replace) | pasted reads | AFTER reads 2026-09-03T09:25:39Z. DeletionProtectionEnabled False->True on 49financial/cottonwood/inflection; TableId AND CreationDateTime IDENTICAL before/after on all three = updated not replaced (the S8-AC3 control); PITR ENABLED on all three with EarliestRestorableDateTime 2026-09-03T05:24:22-04:00. S8-AC4: opal-portal-auth-mfa and opal-portal-auth-throttle byte-identical before/after on DP/SSEType/KMSMasterKeyArn/TableId/CreationDateTime, and the plan showed no change on either. | CLOSED 20260903T092654Z |
| L4 | verify | partner-firms re-plan 0-diff after apply | plan output | terraform -chdir=infra/aws/terraform/partner-firms plan -detailed-exitcode -> 'no differences, so no changes are needed', rc=0. | CLOSED 20260903T092654Z |

## Log

- 20260903T092155Z OPENED by 0.7.0_AE_CloudOps~S with 4 leg(s)
- 20260903T092348Z LEG L1 closed: commit f5859c4097 on SITEZ, author 0.7.0_AE_CloudOps~S -- modules/partner-firm-table/main.tf (PITR + deletion_protection
- 20260903T092653Z LEG L2 closed: safe-apply rc=0 (comp-tagauthz PASSED, tombstone-gate CLEAN 0 creates). All three Modifying/in-place. 'Apply complete! R
- 20260903T092654Z LEG L3 closed: AFTER reads 2026-09-03T09:25:39Z. DeletionProtectionEnabled False->True on 49financial/cottonwood/inflection; TableId AN
- 20260903T092654Z LEG L4 closed: terraform -chdir=infra/aws/terraform/partner-firms plan -detailed-exitcode -> 'no differences, so no changes are needed'
- 20260903T092654Z CLOSED -- all 4 legs proven
