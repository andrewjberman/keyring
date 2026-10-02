# Deploy Completion Record
**Date opened:** 2026-10-02T13:26:37.447215+00:00
**Status:** OPEN
**Deploy:** IRPT_DASHBD DB-b-8: apply the reporting-publish root (publisher function + 08:15 ET weekday schedule); packet blob 38a6eb19a1, COO half + CTO half (c272931fcf, batch 168)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 80.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | terraform plan of infra/aws/terraform/investor-reporting/reporting-publish | 7 to add, 0 to change, 0 to destroy | terraform plan -lock=false 13:2xZ, fresh (root files unchanged since dd3d644cd6): Plan: 7 to add, 0 to change, 0 to destroy; schedule cron(15 8 ? * MON-FRI *) America/New_York; artifact s3_object_version qnGujQo2HF4N3sAKb.wbB5mIYO9DtCOo, source_code_hash gZM/pgyLqFICfadTwYF5VkNQDwhoFJbR2YGmjsmbzis=; saved dbb8.tfplan | CLOSED 20261002T132940Z |
| D1 | activation | targeted safe-apply of the saved plan | Apply complete 7/0/0 | HALT_ACK=1 safe-apply dbb8.tfplan 13:32Z: Apply complete! Resources: 7 added, 0 changed, 0 destroyed (log group, 2 roles, 2 policies, function irpt-49f-reporting-publish-lambda, schedule irpt-49f-reporting-publish-daily) | CLOSED 20261002T133439Z |
| V1 | verify | get-function-configuration irpt-49f-reporting-publish-lambda + get-schedule + re-plan | CodeSha256 = gZM/pg..., schedule ENABLED cron(15 8 ? * MON-FRI *) America/New_York, re-plan No changes | get-function-configuration: CodeSha256 gZM/pgyLqFICfadTwYF5VkNQDwhoFJbR2YGmjsmbzis= (= map artifact), LastModified 13:32:58Z, Active, Successful, role irpt-49f-reporting-publish-role; get-schedule: ENABLED cron(15 8 ? * MON-FRI *) America/New_York -> the function; re-plan No changes | CLOSED 20261002T133440Z |
| Q1 | verify | ONE ad hoc QA invoke, no arguments (CTO half, batch 168) | 12 new versions as_of 2026-10-01; page Data through moves 09-28 -> 10-01 | Run 1 (13:35:40Z) wrote account=0010783709's 2 keys then 403 HeadObject (role had no GetObject; row IRPT_DASHBD-S21) -> rolled back per the signed half (copy from 02:30Z versions, ETags equal). Amendment 1 (both halves: packet blob 2baec1651d, CTO batch 172 @f48e62aadb) applied 0/1/0 ~13:5xZ, re-plan No changes. Run 2 (13:56:08Z, payload {}): StatusCode 200, {ok: true, accounts: 6, refused: []}; list-object-versions: 12 of 12 keys new versions 13:56:29-30Z; 6 manifests as_of 2026-10-01, built_at 13:56:28-29Z, series sizes 17761/4810/4619/2299/4561/3480 = the artifact's dry run. Branch B as measured. Page not looked at by this seat (served manifests read). | CLOSED 20261002T135823Z |
| A1 | verify | first scheduled fire Monday 2026-10-05 08:15 ET, no seat starting it | 12 keys as_of T-1 (2026-10-02 by branch A); page Data through that date |  | OPEN |

## Log

- 20261002T132637Z OPENED by 2.0.0_SA_COO~P with 5 leg(s)
- 20261002T132940Z LEG P1 closed: terraform plan -lock=false 13:2xZ, fresh (root files unchanged since dd3d644cd6): Plan: 7 to add, 0 to change, 0 to dest
- 20261002T133439Z LEG D1 closed: HALT_ACK=1 safe-apply dbb8.tfplan 13:32Z: Apply complete! Resources: 7 added, 0 changed, 0 destroyed (log group, 2 roles
- 20261002T133440Z LEG V1 closed: get-function-configuration: CodeSha256 gZM/pgyLqFICfadTwYF5VkNQDwhoFJbR2YGmjsmbzis= (= map artifact), LastModified 13:32
- 20261002T135823Z LEG Q1 closed: Run 1 (13:35:40Z) wrote account=0010783709's 2 keys then 403 HeadObject (role had no GetObject; row IRPT_DASHBD-S21) -> 
