# Deploy Completion Record
**Date opened:** 2026-10-12T04:27:23.116730+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261013T031129Z
**Deploy:** IAM-z-2 PHASE B act (b): delete-role-policy schwab-bucket-access on bd-exporter-ec2-role -- 2 of 2 ARNs are the 404 opal-data-schwab (pair COO @4afde83a62 / CTO @c790b17440)
**Authored by:** 0.7.0_AE_CloudOps~IR
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| delete | activation | bd-exporter-ec2-role/schwab-bucket-access | list-role-policies reads 16 with schwab-bucket-access absent; get-role-policy on it returns NoSuchEntity; the other 16 policies untouched | all four baselines matched before the act (policy==rollback canonically, list-role-policies 17, opal-data-schwab NoSuchBucket, AC1 grep 0 at HEAD); delete-role-policy rc=0 at 04:29:22Z; the policy-name set read back as a DIFFERENCE 17 -> 16 with REMOVED=['schwab-bucket-access'] and ADDED=[]; get-role-policy on it rc=254 NoSuchEntity against a positive control of s3-access rc=0; the role's CreateDate and its 2 attached managed policies unchanged | CLOSED 20261012T044831Z |
| realrun | verify | bd-exporter-ec2-role | ONE real bd run that STARTS AFTER the delete and completes successfully -- RoleLastUsed advances past the delete time and the run's own record shows success; NEVER substituted by a simulation | ONE chain STARTED 2026-10-12T23:03:07Z (18h34m after the 04:29:22Z delete) and COMPLETED: all 29 of 29 stage keys in gold/.checkpoints/2026-10-12/ are newer than that S_00, 0 stale, terminal D_00f at 2026-10-13T01:12:07Z, gold/perf_report.json at 01:12:08Z, and all 6 watermarks (incl. the 4 incremental at 01:15:34-01:15:42). Includes all 7 early stages the ruling named (S_00, A_00..A_04, B_00) post-delete. schwab-bucket-access absent and 16 inline policies throughout, so the chain ran entirely against the narrowed role. No AccessDenied; branch B did not occur. Every marker compared against this run's S_00 rather than tested for presence, per the per-date-key trap. | CLOSED 20261013T031129Z |

## Log

- 20261012T042723Z OPENED by 0.7.0_AE_CloudOps~IR with 2 leg(s)
- 20261012T044831Z LEG delete closed: all four baselines matched before the act (policy==rollback canonically, list-role-policies 17, opal-data-schwab NoSuchB
- 20261013T031129Z LEG realrun closed: ONE chain STARTED 2026-10-12T23:03:07Z (18h34m after the 04:29:22Z delete) and COMPLETED: all 29 of 29 stage keys in gol
- 20261013T031129Z CLOSED -- all 2 legs proven
