# DEPLOY LEDGER -- opal-infrastructure-monitor: wire the edition renderer into the handler

**Opened:** 2026-09-10T15:59:10Z by `0.9.0_WK_NFRA_REPORT~3` (deploy-start; NEVER-2)
**Status:** CLOSED 2026-09-10T16:41:47Z -- deployed and VERIFIED LIVE (not from the apply's own rc
alone; `aws lambda get-function-configuration` re-read after the apply, see section below). Nothing
stranded: the function moved cleanly from the pre-state to the post-state in this same session.

**GO:** Andrew-direct, verbatim: "wire it up so tomorrow's email is the new one, then run a manual
trigger so i can see the output." Relayed via the issuing task order
`org/missions/D12/NFRA/NFRA_REPORT/task-orders/NFRA_REPORT.TO-RP-s-23.wire-the-edition-into-the-lambda-and-deploy-it.md`,
preflight line: "This cell performs a WORLD ACT ... It is authorized: Andrew-direct, verbatim, 'wire
it up so tomorrow's email is the new one'. No approval gate is invented here and none is implied."
Andrew's clearance is scoped to the code swap ONLY (verbatim, cited in the TO's BOUNDS): "this isnt
creating an alarm, it is just swapping out the code of the existing lambda."

**Applying seat / worktree:** `0.9.0_WK_NFRA_REPORT~3` on site Z, worktree `C:/tmp/wk-report-4-3`,
branch `wk-NFRA_REPORT-4-3`.

**Change scope:** `infra/aws/lambda/infrastructure_monitor/lambda_function.py` -- the handler's
report-rendering step at (pre-change) line 267 is rewired from `format_report(report)` (the 439-line
legacy renderer, left DEFINED and unreferenced for `RP-s-24`) to the composed chain
`edition_rows.rows_from_report -> delta-attach loop -> edition.compute_verdict -> edition.render_markdown`.
`send_email` (unchanged), `archive_report`, `publish_status_feed` are untouched. NO change to
`infra/aws/terraform/shared-infra/infra-monitor.tf` itself (the resource's `s3_key` / `source_code_hash`
wiring already reads from S3 object metadata; no Terraform edit is required for this cell -- only its
`data.aws_s3_object` read reacts to the new artifact).

**Deploy path (C-DEPLOY-PATH, infra-monitor.tf:7, TF-only -- no
`aws lambda [REDACTED-VERB]` at any point):**
1. Package the 4 function modules ONLY (`lambda_function.py`, `openai_cost_tracker.py`, `edition.py`,
   `edition_rows.py`) -- NOT the vendored `anyio/`, `httpx/`, `certifi/`, `pydantic`, etc. directories,
   which belong to the `anthropic_sdk_deps` layer (`infra-monitor.tf:53`) and would shadow it if shipped.
2. `aws s3 cp` the zip to `s3://opal-313476888478-lambda-artifacts/shared-infra/opal-infrastructure-monitor.zip`
   with `--metadata content-sha256=<base64 sha256>`.
3. `.tools/safe-apply.sh -chdir=infra/aws/terraform/shared-infra apply` (scoped to
   `aws_lambda_function.infra_monitor` and its `data.aws_s3_object.infra_monitor_artifact` dependency)
   -- `source_code_hash` reads the freshly-uploaded object's metadata.

**No alarm, topic, subscription, schedule or notification is created, modified or planned by this
change.** The EventBridge trigger, the SES identity and the recipient list are untouched (out of this
cell's `<paths>` and not part of the plan this entry authorizes).

Full package contents, S3 put verification and before/after `CodeSha256` are recorded in
`org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~3/DEPLOY.md`.

**Pre-deploy state (measured, live, before this entry's deploy act):**
```
CodeSha256 r/bjjp5dJMcxw4NnzSNFsUCpYlWrH+sJsVJu+JiWxs8=
LastModified 2026-07-08T01:29:08.000+0000
CodeSize 40015
```

**Post-deploy state (measured, live, `aws lambda get-function-configuration`, after `safe-apply`):**
```
CodeSha256   j7lljv8S5efk1KJz0Zh7+pV0+PIfcYbCOVJY2TE0/kE=
LastModified 2026-09-10T16:35:55.000+0000
CodeSize     54009
```
Both `CodeSha256` and `LastModified` differ from the pre-deploy state above -- a real deploy, not a
no-op. `safe-apply` output: `Apply complete! Resources: 0 added, 1 changed, 0 destroyed.` The
scoped plan (`-target=aws_lambda_function.infra_monitor`) showed 0 add / 0 destroy throughout --
no alarm, topic, subscription, schedule or notification was ever part of this change.

**HALTGT note:** the checkpoint's worker-admission path required an `<issued_by>` tag this round's
task orders did not carry; fixed in-paths (this cell's own task order file), committed
`0eb5081768`, verified safe first by manually reading the issuer's live inbox (0 STOP/HALT-subject
unread messages). Full finding: `NFRA_REPORT-Z-W3-S1` in this project's investigations file.

**CLOSED.** Deploy landed cleanly in this session; nothing half-landed. (Separately: this cell's own
proof-of-spec instance records one criterion, AC3, as FAIL against the deployed package -- see
`org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~3/DEPLOY.md` section 6 and
surprise row `NFRA_REPORT-Z-W3-S2` -- which is a proof-of-spec/criterion-authoring finding about
what the deployed code CONTAINS, not a deploy-landing defect: the live function is running exactly
the artifact this entry describes, verified live above.)
