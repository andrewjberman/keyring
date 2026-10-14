# Deploy Completion Record
**Date opened:** 2026-10-14T00:37:04.251301+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP AMGT-ar-1: ONE list entry (amgt/harvest/gold/ai_fill/) added to local.scoped_amgt_pool_prefixes in infra/aws/terraform/harvest/scoped-amgt-api.tf, ONE targeted safe-apply of aws_iam_role_policy.scoped_amgt_api_grants; additive read grant on an empty prefix; pre-act policy 7 statements, 34 resources, sha16 77c69f8359764942; rollback is removing the one entry and the same targeted apply
**Authored by:** 0.7.0_AE_CloudOps~RA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | constant AI_FILL_GOLD_PREFIX printed and the live policy read BEFORE the act: 7 statements, 34 resources, sha16 77c69f8359764942 (check_ar1_grant.py NO 4 of 7) | printed output |  | OPEN |
| L2 | git | the one list entry added as the LAST element of local.scoped_amgt_pool_prefixes, nothing else touched | diff of the file |  | OPEN |
| L3 | verify | targeted plan of aws_iam_role_policy.scoped_amgt_api_grants shows exactly one resource changing in place: one resource added to GetObject and one prefix to the ListBucket condition, no other difference | plan JSON graded |  | OPEN |
| L4 | activation | targeted safe-apply of the saved plan of that one resource | apply output |  | OPEN |
| L5 | verify | live re-read: check_ar1_grant.py reads YES 7 of 7; pre and post sha16 printed | check output + sha16 |  | OPEN |
| L6 | verify | AC2 capture shows the function still answers for 2 names, non-200 none | capture line |  | OPEN |
| L7 | git | record, commit and report to the issuer | commit hash + message |  | OPEN |

## Log

- 20261014T003704Z OPENED by 0.7.0_AE_CloudOps~RA1 with 7 leg(s)
