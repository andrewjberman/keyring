# DEPLOY LEDGER -- opal-infrastructure-monitor: revert to format_report + add RESOURCE REFERENCE table

**Opened:** 2026-09-17T14:20:00Z by `4.0.0_SA_CRO~N` (deploy-start; NEVER-2)
**Status:** OPEN

**GO:** Andrew-direct (via `1.0.0_SA_CTO~Z` relay, msg 23534, same-hour record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260917_13xxZ_NFRA_REPORT_SPAWN_CRO_N_RESEARCH.md`
s.3): *"The NFRA_REPORT shouldnt even be that hard to do, i dont think we even need canonical-workflow
for this, there should be enough prior art at this point, id have CRO~N just finish the project end to
end."* -- `4.0.0_SA_CRO~N` builds, deploys and verifies the ratified target spec itself, no L4/L5/L6.
Ratified spec: `org/tier1_exec/4.0.0_SA_CRO~N/deliverables/ANDREW_DIRECT_20260917_1345Z_NFRA_REPORT_TARGET_SPEC_RATIFIED.md`
@da2c3c479a, items a-e (old-style prose body; both cost sections; a 3-column ID/name/description
table; stopgap revert authorized verbatim "Yeah we can use the old one"; audience Andrew only).

**Applying seat:** `4.0.0_SA_CRO~N`, main checkout, no worker/worktree (Andrew's word retires the
L1-L10 workflow for this project; estate NEVER-law still binds -- Terraform-only, safe-apply,
safe-commit, this ledger).

**Change scope:** `infra/aws/lambda/infrastructure_monitor/lambda_function.py` --
1. The handler's report-rendering step reverts from the round-4 `edition_rows.rows_from_report ->
   delta-attach loop -> edition.compute_verdict -> edition.render_markdown` chain back to
   `format_report(report)` (item a: old-style prose body; item b: format_report already renders both
   `aws_costs` and `cost_depth` in full -- verified in a local dry-render below, not assumed).
2. `import edition` / `import edition_rows` removed from the module (the two files stay in the repo,
   UNCHANGED, as a historical artifact -- not deleted, not shipped in the new package).
3. NEW: `build_resource_glossary(report)` + `KNOWN_RESOURCE_GLOSSARY` + `_live_resource_description()`
   (item c) -- collects every Lambda/SNS/EC2 identifier this run's report actually names (errors,
   deploy drift, SNS egress gaps, EC2 right-size, OpenAI cost) and pairs each with a business name +
   description (hand-curated where this project's own prior research grounds it -- ALERT_DELIVERY.md
   for the 7 known alert topics -- else a bounded-timeout LIVE AWS lookup, else an honest "(no
   description on record)"; never fabricated). Rendered as a new "RESOURCE REFERENCE" table
   immediately after the existing STATUS SUMMARY block.
4. `send_email`, `archive_report`, `publish_status_feed` are UNTOUCHED. No change to
   `infra/aws/terraform/shared-infra/infra-monitor.tf` (same `data.aws_s3_object` / `source_code_hash`
   wiring as the round-4 deploy; no Terraform edit required).

**Local verification, BEFORE deploy (per 1.0.0_SA_CTO~Z's flagged risk that a dry render was
unmeasured):** `format_report()` + `build_resource_glossary()` run locally against TODAY's real
archived report (`s3://opal-data-portal-v2/infrastructure/reports/2026-09-17/13-00-09.json`, the
actual 13:00Z scheduled run's own collector output) -- renders cleanly, 38,088 chars / 534 lines, AWS
COSTS + COST DEPTH + OPENAI COST + RESOURCE REFERENCE sections all present, zero
QUOTED/COMPUTED/GENERATED state-table artifacts. Harness + output: `.scratch/nfra_report_test/`
(local scratch, not committed).

**No alarm, topic, subscription, schedule or notification is created, modified or planned by this
change.** The EventBridge trigger `infrastructure-monitor-daily` (`cron(0 13 * * ? *)`, fires
EVERY day incl. weekends, next fire 2026-09-18T13:00Z), the SES identity and the recipient list are
untouched.

**Deploy path (C-DEPLOY-PATH, infra-monitor.tf:7, TF-only -- no `aws lambda update-function-code` at
any point):**
1. Package the function modules only -- now 2 files (`lambda_function.py`, `openai_cost_tracker.py`;
   `edition.py`/`edition_rows.py` are no longer imported and are excluded from the zip) -- NOT the
   vendored `anyio/`, `httpx/`, `certifi/`, `pydantic`, etc. directories (the `anthropic_sdk_deps` layer).
2. `aws s3 cp` the zip to `s3://opal-313476888478-lambda-artifacts/shared-infra/opal-infrastructure-monitor.zip`
   with `--metadata content-sha256=<base64 sha256>`.
3. `.tools/safe-apply.sh -chdir=infra/aws/terraform/shared-infra apply` scoped to
   `aws_lambda_function.infra_monitor`.

**Pre-deploy state (measured live, before this entry's deploy act):**
```
CodeSha256   j7lljv8S5efk1KJz0Zh7+pV0+PIfcYbCOVJY2TE0/kE=
LastModified 2026-09-10T16:35:55.000+0000
CodeSize     54009
```
(unchanged since the round-4 deploy one week ago -- confirmed by this seat's own earlier drift check.)

**Post-deploy state:** TO BE FILLED after `safe-apply`, read live, never from the apply's own rc alone.
