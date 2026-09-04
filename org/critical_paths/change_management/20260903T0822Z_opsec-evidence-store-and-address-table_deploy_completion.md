# Deploy Completion Record
**Date opened:** 2026-09-03T08:22:21.552855+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260903T085025Z
**Deploy:** NFRA_OPSEC202609.TO-OP-S-17-16 -- opal-data-security (S3 evidence store) + opal-suspicious-addresses (DynamoDB address table), new module infra/aws/terraform/opsec/, 7 resources, safe-apply
**Authored by:** 0.7.0_AE_CloudOps~S
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | module + surprise rows committed on SITEZ under 0.7.0_AE_CloudOps~S | commit hash | commit cdbdcb473c on SITEZ, author 0.7.0_AE_CloudOps~S -- module infra/aws/terraform/opsec/{main,dynamodb,s3}.tf + .terraform.lock.hcl, surprise rows S4+S5, ledger entry; 6 files / 432 insertions; row gate rc=0 (2 new rows of 5 checked) | CLOSED 20260903T082742Z |
| L2 | activation | safe-apply of infra/aws/terraform/opsec (7 creates, 0 change, 0 destroy) | apply output + resource ids | safe-apply rc=0 (HALT_ACK=1 after reading msg 4355 in full -- a 12d-old base-inbox message about WA-APPLY/GW-APPLY, explicitly 'neither is a gate', unrelated to this project). tombstone-gate CLEAN 7 creates vs 7 tombstones. Apply complete: 7 added, 0 changed, 0 destroyed. ids: opal-data-security, opal-suspicious-addresses | CLOSED 20260903T083149Z |
| L3 | verify | the nine applied-plane reads: six S3 (public-access-block, encryption, versioning, policy, logging, lifecycle) + three DynamoDB (describe-table, continuous-backups, time-to-live) | pasted read output | Nine applied-plane reads taken. S3 six: public-access-block 4/4 true; encryption AES256 BucketKeyEnabled=false (interim, Z-S3); versioning Enabled; policy = one stmt DenyInsecureTransport on both ARNs w/ aws:SecureTransport=false (allow-list deferred, Z-S4); logging NOT configured (Z-S5); lifecycle exactly one rule waf-logs-glacier-90-expire-400, Filter.Prefix=waf-logs/, GLACIER 90d, Expiration 400d, nothing on cases/. Object Lock: ObjectLockConfigurationNotFoundError (AC3 PASS). DynamoDB three: KeySchema address HASH, attrs address+status, SSE ENABLED/KMS/86cc6c40 (AWS-managed), DeletionProtectionEnabled true, stream NEW_AND_OLD_IMAGES, GSI status-index ACTIVE proj ALL; PITR ENABLED; TTL ENABLED on expires_at | CLOSED 20260903T083404Z |
| L4 | verify | terraform re-plan reads 0-diff after apply | plan output | terraform -chdir=infra/aws/terraform/opsec plan -detailed-exitcode -> 'No changes. Your infrastructure matches the configuration.' rc=0 (0=no changes, 2=drift). 0-diff confirmed post-apply. | CLOSED 20260903T083404Z |
| L5 | verify | fixture exercise WATCH/BLOCK/ALLOW + status-index query + S3 version pair, then CLEANUP to zero fixture rows and zero objects | listing showing empty | Fixture exercised then removed. Table: WATCH/BLOCKED/ALLOW written (RFC5737 203.0.113.x/32 + RFC3849 2001:db8::/64 documentation ranges -- no real address), all 3 read back by pk, status-index returned each by status. BLOCK TTL had NOT fired at read 2026-09-03T08:39:11Z (epoch 1788424751) vs expires_at 1788424745 -- TTL is best-effort to ~48h; row deleted BY HAND and the deletion stated. S3: object written + overwritten once -> 2 versions (64B v1 IsLatest=false, 81B v2 IsLatest=true), BOTH read back with DIFFERENT bodies (the AC2 control: the original survived the overwrite), then both versions deleted. FINAL: table scan Count=0; bucket Versions=0 DeleteMarkers=0; per-key absence confirmed with a POSITIVE CONTROL. | CLOSED 20260903T084230Z |

## Log

- 20260903T082221Z OPENED by 0.7.0_AE_CloudOps~S with 5 leg(s)
- 20260903T082742Z LEG L1 closed: commit cdbdcb473c on SITEZ, author 0.7.0_AE_CloudOps~S -- module infra/aws/terraform/opsec/{main,dynamodb,s3}.tf + .terr
- 20260903T083149Z LEG L2 closed: safe-apply rc=0 (HALT_ACK=1 after reading msg 4355 in full -- a 12d-old base-inbox message about WA-APPLY/GW-APPLY, expl
- 20260903T083404Z LEG L3 closed: Nine applied-plane reads taken. S3 six: public-access-block 4/4 true; encryption AES256 BucketKeyEnabled=false (interim,
- 20260903T083404Z LEG L4 closed: terraform -chdir=infra/aws/terraform/opsec plan -detailed-exitcode -> 'No changes. Your infrastructure matches the confi
- 20260903T084230Z LEG L5 closed: Fixture exercised then removed. Table: WATCH/BLOCKED/ALLOW written (RFC5737 203.0.113.x/32 + RFC3849 2001:db8::/64 docum
- 20260903T085025Z CLOSED -- all 5 legs proven
