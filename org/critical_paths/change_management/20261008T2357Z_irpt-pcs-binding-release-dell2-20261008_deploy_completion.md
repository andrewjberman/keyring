# Deploy Completion Record
**Date opened:** 2026-10-08T23:57:24.882475+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261009T000748Z
**Deploy:** IRPT_BCKEND IB-pr-378: irpt-export-render released with persisted_by + the composition-hash binding (pin 49bc13131d), THEN the Performance client statement persist route
**Authored by:** 0.7.0_AE_CloudOps~DELL2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| R1 | verify | offline differential replay (run BEFORE this ledger) | identical read-back through both zips and the altered-policy negative control refused by both | committed BEFORE this ledger at b9fccdccaa: live zip (rNjtTwcm.., 414177 B) vs built zip (7T29wPhz.., 415060 B) differ in EXACTLY custody_persist.py and custody_write.py (diff -rq, 55 members each); one retained irpt-x10-v1 ANALYSIS and one PERFORMANCE reserved through the LIVE code path read back IDENTICALLY through both zips via repository.get (get/fixture/kinds/module_files/policy_sha256 e0046398e239/policy_state ACTIVE all identical under canonical JSON); negative control (altered policy_sha256) RetentionRefused 'retention binding changed' on both fixtures in BOTH zips | CLOSED 20261008T235734Z |
| V1 | verify | export root equality reads | live CodeSha256 == built 7T29wPhz..; re-plan 0; release-census changed_members 0 at pin 49bc13131d | export root re-plan after the apply: 'No changes. Your infrastructure matches the configuration.'; release-census irpt-export-render --pin 49bc13131d: changed_members=0 (built_members=66 live_members=66) | CLOSED 20261009T000139Z |
| B1 | activation | the ONE route POST /api/scoped/investor-reporting/custody-report on the api root | plan 1 to add and nothing else; apply from the planfile; re-plan 0; get-routes read-back filtered to that route key | planned TARGETED after Part A's live read showed 7T29wPhz..: 1 to add, 0 to change, 0 to destroy (plan text committed d36bb1aac5); safe-apply from the committed planfile, naming-plan-gate PASS; Creation complete id=jtwlf6l; re-plan of the SAME target 'No changes'; live read-back via get-routes on api 7k3ed8px20 AUTO-PAGINATED with the denominator printed (116 routes, exactly 1 exact match): RouteId jtwlf6l, RouteKey 'POST /api/scoped/investor-reporting/custody-report', Target integrations/61aupci, AuthorizationType CUSTOM, AuthorizerId naqxlm. NOTE: a first read with --no-paginate returned [] -- the CLAUDE.md pagination hazard; the route is beyond page 1 and the empty page would have read as a failed apply | CLOSED 20261009T000710Z |
| irpt-export-render | tf-lambda | module.irpt_export_render.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | safe-apply from the COMMITTED planfile (plan text at 9c455bb94a; Apply complete 0 added 1 changed 0 destroyed); live CodeSha256 RE-READ = 7T29wPhzbU/FlJpeT3MNSJ5jFWcEmi7bvHiSKECkyns= = built sha; s3_object_version WiLXOyzMQ8_U42fSAeTIOwyMyw9.A9X3 -> QK8IR0k6Ek7HmbMvA.GqjpfTGNKmDKdi | CLOSED 20261009T000138Z |

## Log

- 20261008T235724Z OPENED by 0.7.0_AE_CloudOps~DELL2 with 4 leg(s)
- 20261008T235734Z LEG R1 closed: committed BEFORE this ledger at b9fccdccaa: live zip (rNjtTwcm.., 414177 B) vs built zip (7T29wPhz.., 415060 B) differ i
- 20261009T000138Z LEG irpt-export-render closed: safe-apply from the COMMITTED planfile (plan text at 9c455bb94a; Apply complete 0 added 1 changed 0 destroyed); live Cod
- 20261009T000139Z LEG V1 closed: export root re-plan after the apply: 'No changes. Your infrastructure matches the configuration.'; release-census irpt-e
- 20261009T000710Z LEG B1 closed: planned TARGETED after Part A's live read showed 7T29wPhz..: 1 to add, 0 to change, 0 to destroy (plan text committed d3
- 20261009T000748Z CLOSED -- all 4 legs proven
