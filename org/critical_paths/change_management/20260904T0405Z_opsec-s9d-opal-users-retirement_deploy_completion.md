# Deploy Completion Record
**Date opened:** 2026-09-04T04:05:35.248799+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260904T041559Z
**Deploy:** TO-OP-S-9D: destroy the legacy opal-users table THROUGH TERRAFORM by removing its declaration (Andrew-authorised 2026-09-04 ~03:4xZ, 'Recs approved')
**Authored by:** 0.7.0_AE_CloudOps~X
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | PRE-ACT re-read at this vintage: snapshot AVAILABLE 12 items 4506 bytes expiry null, table 12 of 12 rows UNMOVED, fixture login captured | live reads with timestamps | PRE-ACT re-reads at 2026-09-04T04:02:06Z, taken at the vintage of the act rather than inherited. SNAPSHOT opal-users-retire-snapshot-20260904T004712Z: AVAILABLE, USER, 12 items, 4,506 bytes, BackupExpiryDateTime null -- matching the live table on BOTH count and size. TABLE: scan --select COUNT = 12 / ScannedCount 12; describe-table ItemCount 12, TableSizeBytes 4506, ACTIVE. THE ROW COUNT HAD NOT MOVED since the grant removal, which was the STOP condition. FIXTURE BEFORE at 04:05:32Z: POST /auth/refresh 200, GET /auth/me 200 with the full demo user payload. | CLOSED 20260904T041557Z |
| L2 | git | SITEZ commit removing the aws_dynamodb_table.opal_users declaration from portal-auth/dynamodb.tf | commit hash | commit 051d5034c0 on SITEZ: the aws_dynamodb_table.opal_users declaration (dynamodb.tf:145-165) replaced by a tombstone recording the authorisation, the method, the state at the moment of the act, the honest rollback shape, and the correction of the block's own stale us-east-2 claim. GUARDED EDIT: the script refused to run unless the block was byte-exact AND carried neither prevent_destroy nor deletion_protection. ASCII-only; the two non-ASCII lines in the file are pre-existing and were verified against HEAD as not mine. | CLOSED 20260904T041557Z |
| L3 | activation | safe-apply performs the DESTROY through Terraform; plan read as its own artifact showing EXACTLY ONE resource destroyed | plan + apply output | DESTROY PERFORMED BY TERRAFORM, not by console, CLI or state rm. Plan read as its own artifact BEFORE the act: '# aws_dynamodb_table.opal_users will be destroyed (because ... is not in configuration)', with 'grep -c will-be-destroyed' returning exactly 1, and the plan body independently confirming deletion_protection_enabled = false -> null. Apply: 'aws_dynamodb_table.opal_users: Destroying... [id=opal-users]' / 'Destruction complete after 7s' / 'Apply complete! Resources: 0 added, 0 changed, 1 destroyed.' TARGETED to the table so the root's documented perpetual WAF churn (3 minus-rule against 3 identical plus-rule blocks, 0 forces-replacement) could not ride this ledger or author line; verification deliberately UNSCOPED. | CLOSED 20260904T041558Z |
| L4 | verify | POST: describe-table returns ResourceNotFoundException; UNSCOPED re-plan proposes NO re-creation; fixture login AFTER matches its before | live reads pasted | POST, all at 2026-09-04T04:13:19Z. (a) describe-table opal-users -> ResourceNotFoundException. CONTROL, so the refusal is the table being gone and not a broken probe: the same call on opal-users-v2 returns ACTIVE with 75 items. (b) UNSCOPED re-plan: 'Plan: 0 to add, 1 to change, 0 to destroy' -- ZERO to add, so NO proposal to re-create, and the resource address appears 0 times anywhere in the plan, meaning nothing is orphaned in state. The single change is the pre-existing WAF churn, unchanged. (c) FIXTURE AFTER: POST /auth/refresh 200, GET /auth/me 200, and the /auth/me payload BYTE-IDENTICAL to the before captured at 04:05:32Z. (d) The SNAPSHOT survives the table: still AVAILABLE, 12 items, 4,506 bytes -- the data remains recoverable. ROLLBACK'S REAL SHAPE, stated honestly: restore-table-from-backup produces a NEW TABLE NAME and is NOT a byte-for-byte undo; re-adopting it would need a fresh declaration and an import. The DATA is recoverable; THIS EXACT RESOURCE is not. | CLOSED 20260904T041559Z |

## Log

- 20260904T040535Z OPENED by 0.7.0_AE_CloudOps~X with 4 leg(s)
- 20260904T041557Z LEG L1 closed: PRE-ACT re-reads at 2026-09-04T04:02:06Z, taken at the vintage of the act rather than inherited. SNAPSHOT opal-users-ret
- 20260904T041557Z LEG L2 closed: commit 051d5034c0 on SITEZ: the aws_dynamodb_table.opal_users declaration (dynamodb.tf:145-165) replaced by a tombstone 
- 20260904T041558Z LEG L3 closed: DESTROY PERFORMED BY TERRAFORM, not by console, CLI or state rm. Plan read as its own artifact BEFORE the act: '# aws_dy
- 20260904T041559Z LEG L4 closed: POST, all at 2026-09-04T04:13:19Z. (a) describe-table opal-users -> ResourceNotFoundException. CONTROL, so the refusal i
- 20260904T041559Z CLOSED -- all 4 legs proven
