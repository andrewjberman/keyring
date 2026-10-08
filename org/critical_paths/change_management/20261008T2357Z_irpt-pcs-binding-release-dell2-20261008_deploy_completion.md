# Deploy Completion Record
**Date opened:** 2026-10-08T23:57:24.882475+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND IB-pr-378: irpt-export-render released with persisted_by + the composition-hash binding (pin 49bc13131d), THEN the Performance client statement persist route
**Authored by:** 0.7.0_AE_CloudOps~DELL2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| R1 | verify | offline differential replay (run BEFORE this ledger) | identical read-back through both zips and the altered-policy negative control refused by both | committed BEFORE this ledger at b9fccdccaa: live zip (rNjtTwcm.., 414177 B) vs built zip (7T29wPhz.., 415060 B) differ in EXACTLY custody_persist.py and custody_write.py (diff -rq, 55 members each); one retained irpt-x10-v1 ANALYSIS and one PERFORMANCE reserved through the LIVE code path read back IDENTICALLY through both zips via repository.get (get/fixture/kinds/module_files/policy_sha256 e0046398e239/policy_state ACTIVE all identical under canonical JSON); negative control (altered policy_sha256) RetentionRefused 'retention binding changed' on both fixtures in BOTH zips | CLOSED 20261008T235734Z |
| V1 | verify | export root equality reads | live CodeSha256 == built 7T29wPhz..; re-plan 0; release-census changed_members 0 at pin 49bc13131d |  | OPEN |
| B1 | activation | the ONE route POST /api/scoped/investor-reporting/custody-report on the api root | plan 1 to add and nothing else; apply from the planfile; re-plan 0; get-routes read-back filtered to that route key |  | OPEN |
| irpt-export-render | tf-lambda | module.irpt_export_render.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20261008T235724Z OPENED by 0.7.0_AE_CloudOps~DELL2 with 4 leg(s)
- 20261008T235734Z LEG R1 closed: committed BEFORE this ledger at b9fccdccaa: live zip (rNjtTwcm.., 414177 B) vs built zip (7T29wPhz.., 415060 B) differ i
