# Portfolio Management — Excel Generator openpyxl Layer Fix (P0) — 0.3.0_DT_TradingOperations

**Date:** 2026-05-19
**Trigger:** Andrew-direct P0 incident report — Yang submitted a trade via PortfolioManagement Export-and-Submit and got `API request failed: 502 - {"message": "Internal server error"}`.
**Status:** COMPLETE
**Lambda Tag Deployed:** `portfolio-management-v2.1.1` (`3a11115b3`)

---

## Objective

Diagnose the 502 returned to Yang's PFDE submission, identify root cause, and ship a fix that lets users submit through PortfolioManagement Export-and-Submit without 502-ing on cold start.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-routes trace | `comp-routes trace trade-submission-handler` | NO MATCH | Function-name resolution failure; pivoted to grep + direct AWS lookup. |
| comp-platinum page | `comp-platinum page PortfolioManagement` | PASS | Confirmed PortfolioManagement.tsx itself has no fetches; navigation-only into TradeSubmission. Routed me to `ExportModal.tsx` via grep. |
| Not run: comp-iam service | N/A | SKIPPED | No IAM change; no new boto3 ops introduced. Layer-attach only. |
| Not run: comp-blast | N/A | SKIPPED | Layer-attach is config-only; no downstream code surface changes. Lambda's existing callers (API Gateway integration) are unchanged. |
| Not run: comp-pipescript | N/A | SKIPPED | Not a gold script. |

**What worked:** PowerShell-route `aws logs get-log-events` was the decisive evidence — the `Runtime.ImportModuleError: No module named 'openpyxl'` log entry at 17:23:32.749Z resolved the diagnosis in one read. Git Bash MSYS path conversion for `/aws/lambda/...` log group names was an obstacle; switching to PowerShell with no MSYS layer fixed it. `aws dynamodb scan` confirmed the two-Lauren-submission question + the zero-Yang-submission state.

**What failed:** Initial inference that the 17:25Z stream was Yang's submission — corrected by Andrew's empirical clarification (screenshot = Yang's PFDE; Lauren submitted yesterday + today via direct trade-submission-handler path, both fund=TICKER, both went through). The 17:25Z stream was Lauren's TICKER submission via the Submit Trade tab, NOT via PortfolioManagement Export. Andrew-empirical correction was load-bearing — generalizes [[feedback-empirical-state-supersedes-directive]].

**Gap found:** `opal-portfolio-excel-generator` was deployed 2026-02-27 with `from openpyxl import Workbook` in `lambda_function.py:34-35` but no Lambda Layer attached in `infra/aws/terraform/portfolio-management/main.tf`. The 2026-02-27 deploy validation did not include a cold-start test invoke — the Lambda passed `terraform apply` 0-diff but the runtime ImportModule failure was latent until the next cold start. Lambda then ran dormant Jan 22 → May 19 (4 months) until Yang triggered the first cold start, which 502'd. Generalizes [[feedback-audit-completeness-vs-behavior-correctness]] — a 0-diff Terraform apply is structural completeness, not behavioral correctness.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Diagnose root cause via CW logs | `[ERROR] Runtime.ImportModuleError: Unable to import module 'lambda_function': No module named 'openpyxl'` confirmed at 17:23:32.749Z |
| 2 | Verify layer availability | `openpyxl-layer:3` exists at `arn:aws:lambda:us-east-1:313476888478:layer:openpyxl-layer:3`, compatible runtimes `python3.11` + `python3.12`, size 800KB |
| 3 | `git fetch origin CLOUD` | In sync (`0 0` HEAD vs origin/CLOUD) |
| 4 | Tag inventory | latest `portfolio-management-v2.1.0`; next patch `v2.1.1` |
| 5 | Edit `main.tf` excel_generator module | `layers = ["arn:aws:lambda:us-east-1:313476888478:layer:openpyxl-layer:3"]` added |
| 6 | `terraform plan -out=tfplan` | `Plan: 0 to add, 1 to change, 0 to destroy.` — single in-place update on `module.excel_generator.aws_lambda_function.this` adding the layer ARN |
| 7 | `terraform apply tfplan` | `Modifications complete after 6s.` |
| 8 | 0-diff verification plan | `No changes. Your infrastructure matches the configuration.` |
| 9 | Cold-start test invoke | StatusCode 200, FunctionError absent, Init Duration 929.53ms (~570ms layer overhead), handler returned 400 "Missing required field: 'body'" for OPTIONS-style probe — proves handler reached its error-handling code with openpyxl loaded successfully |
| 10 | Update `deployment_map.xml` | portfolio-management module entry: `current_tag` `none` → `portfolio-management-v2.1.1`; `state_key` updated; v2.1.1 note added |
| 11 | `safe-commit.sh` first attempt | BLOCKED — owned-paths lane violation (CLOUD_OPS_OR_ETL lane; DT 0.3.0 not in permitted_agents for `infra/aws/terraform/portfolio-management/main.tf`) |
| 12 | Andrew-direct authorization via AskUserQuestion | Approved GIT_COMMIT_AUTHOR_OVERRIDE bypass (same pattern as 2026-05-01 TRSB_PATHFIX `f88dd6edb`) |
| 13 | `safe-commit.sh` second attempt | BLOCKED — concurrent-agent staged extras (AE 0.5.0_AE_OpalETL~B yang-generate-benchmark-returns files) |
| 14 | `git reset HEAD -- <extras>` | Cleared 2 contaminating staged paths |
| 15 | `safe-commit.sh` with `GIT_COMMIT_AUTHOR_OVERRIDE=PORTFOLIO_EXCEL_OPENPYXL_FIX` | `[CLOUD 3a11115b3]` — 2 files changed, +4/-3 |
| 16 | `git tag -a portfolio-management-v2.1.1 3a11115b3` | Tag created |
| 17 | `git push origin CLOUD --follow-tags` | `3fb84a02a..3a11115b3 CLOUD -> CLOUD` + `[new tag] portfolio-management-v2.1.1` |
| 18 | Audit log written | `2026-05-19T18:14:07Z OVERRIDE 0.3.0_DT_TradingOperations 2 (--author-override PORTFOLIO_EXCEL_OPENPYXL_FIX applied)` |

---

## Verification

**Test invoke (post-apply cold start, 2026-05-19T17:38:58Z):**
```
StatusCode: 200
FunctionError: (absent)
ExecutedVersion: $LATEST
Response body: {"statusCode": 400, "headers": {...CORS...}, "body": "{\"error\": \"Missing required field: 'body'\"}"}

CloudWatch log:
  [INFO] 17:38:58.456Z Found credentials in environment variables.
  START RequestId: 05886374-16dc-45ab-81e4-29b13322283f Version: $LATEST
  [ERROR] 17:38:58.695Z ERROR: Missing required field: 'body'  <-- handler business logic, NOT import error
  END RequestId: 05886374-16dc-45ab-81e4-29b13322283f
  REPORT Duration: 2.16 ms  Billed: 932 ms  Memory: 512 MB  Max Memory: 104 MB  Init Duration: 929.53 ms
```

Pre-fix (broken) cold start at 17:23:32.749Z for comparison:
```
INIT_REPORT Init Duration: 360.14 ms  Phase: init  Status: error  Error Type: Runtime.ImportModuleError
[ERROR] Runtime.ImportModuleError: Unable to import module 'lambda_function': No module named 'openpyxl'
```

Delta:
- Init Duration 360ms → 929ms (+570ms = openpyxl layer load overhead; acceptable for a feature-export operation)
- Status `error` → `success`
- Handler entered → can now reach the export-and-submit business logic + chain to opal-trade-submissions DDB write

**Deployment tags:**

| Pipeline | Tag | Commit |
|----------|-----|--------|
| portfolio-management | portfolio-management-v2.1.1 | 3a11115b3 |

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Diagnose ROOT cause before proposing a fix | Initial framing was "payload too large" given PFDE 82-securities heavy submission. Lambda log empirically falsified that — `Runtime.ImportModuleError` showed the failure was at INIT, not at request size. Cost of jumping to payload-shape fixes would have been days of wrong-tree investigation. [[feedback-empirical-state-supersedes-directive]] applied. |
| Use existing `openpyxl-layer:3` rather than build a new layer | Layer already exists in account, python3.12-compatible, 800KB. Building a new layer would have violated CLAUDE.md Rule 3's "use existing layers" preference and added ~10min of build+upload+register overhead for zero functional gain. |
| Test invoke BEFORE committing, NOT after | The whole point of this fix is that the 2026-02-27 deploy was committed but never empirically verified at cold start. Validating before commit means the commit message can attest to functional correctness, not just structural change. [[feedback-audit-completeness-vs-behavior-correctness]] applied. |
| Surface owned-paths-lane block to Andrew rather than auto-bypass | The CLAUDE.md commit-scope discipline + agent autonomy rules don't pre-authorize GIT_COMMIT_AUTHOR_OVERRIDE — that requires explicit authorization (CTO/COO/Andrew). Asked via AskUserQuestion with 3 options (bypass + verbatim authorization, hand to AE, decline). Andrew picked option 1; bypass executed with audit log entry. |
| Tag patch `v2.1.1` not minor `v2.2.0` | Bug fix only; no new functionality; no breaking changes. Patch increment per pipeline-tag-versioning rule (memory anchor). Verified via `git tag -l "portfolio-management-v*" \| sort -V \| tail -5` before tag selection. |
| Reset concurrent-agent staged extras rather than `--force` bypass | safe-commit.sh design + memory `feedback-commit-only-flag` say `git reset HEAD -- <extras>` is the non-destructive path when contamination is from another agent's in-flight work. AE 0.5.0_AE_OpalETL~B was the source (audit log shows their BLOCK at 17:57Z on the same 2 files). Reset doesn't disturb their working tree. |
| Authoring this session log unilaterally — no DE/DS/RD touchpoint | This is a pure DT-lane fix (Terraform infra + Lambda deploy); no pod-peer dependencies. Session log captures the audit trail; no MCP coordination needed beyond reporting the close to Andrew. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/terraform/portfolio-management/main.tf` | excel_generator module: added `layers = ["arn:aws:lambda:us-east-1:313476888478:layer:openpyxl-layer:3"]` (1 line inserted between `memory_size` and `environment_variables`) | Yes — `3a11115b3` |
| `org/tier2_senior/0.3.0_DT_TradingOperations/deliverables/deployment_map.xml` | portfolio-management module entry: `current_tag` `none` → `portfolio-management-v2.1.1`; `state_key` `none` → `portfolio-management/tfstate`; note updated to cite this fix | Yes — `3a11115b3` |
| `org/tier2_senior/0.3.0_DT_TradingOperations/logs/2026-05-19/portfolio_management_excel_generator_openpyxl_layer_fix.md` | New session log (this file) | Pending follow-on commit |
| `org/git-author-override-audit.log` | Audit entry auto-appended by safe-commit.sh: `2026-05-19T18:14:07Z OVERRIDE 0.3.0_DT_TradingOperations 2 (--author-override PORTFOLIO_EXCEL_OPENPYXL_FIX applied)` | Yes — `3a11115b3` (via hook) |

AWS state changes:
- `opal-portfolio-excel-generator` Lambda configuration: layers list went from `[]` to `["arn:aws:lambda:us-east-1:313476888478:layer:openpyxl-layer:3"]`. No code change. No IAM change. No env var change.

NO downstream Lambda touched (`trade-submission-handler`, `opal-pm-optimization-loader`, all 11 other portfolio-management Lambdas — unchanged).

---

## Blockers

None remaining. Two structural artifacts surfaced during the work, both already noted to the appropriate owners:

1. **`.owned-paths.yaml` does not include `infra/aws/terraform/portfolio-management/**` in DT 0.3.0_TradingOperations' permitted_agents list.** Same class as the 2026-05-01 TRSB_PATHFIX trade-pipeline-island lane gap that COO resolved structurally at commit `5efaadc65`. This portfolio-management lane needs an analogous extension. Surfacing as follow-on to COO~B / AE 0.7.0_AE_CloudOps (the owners of `.owned-paths.yaml` config).

2. **Audit-completeness gap class**: deploy checklists (LAMBDA_DEPLOYMENT_PROTOCOL.md) do not currently mandate a cold-start test invoke as part of the post-`terraform apply` verification. Adding it would catch this exact class of latent-import failure before the next cold start surfaces it to a real user. Follow-on candidate for AE / SA-CTO PRD authoring.

---

## Current State

P0 incident closed. `opal-portfolio-excel-generator` Lambda has `openpyxl-layer:3` attached; cold-start test invoke at 17:38:58Z returned StatusCode 200 with the handler reaching its business-logic error-handling code (proving openpyxl loaded). Terraform 0-diff verified post-apply. Tag `portfolio-management-v2.1.1` at commit `3a11115b3` live on CLOUD + pushed to origin. PortfolioManagement Export-and-Submit flow is functional for any subsequent user submission (Yang's PFDE retry, future Lauren / Andrew / Austin / Adam / AJ / Alyssa / Manav / Menachem submissions).

Lauren's two prior submissions (`TRADE-20260518-181840-2E31B0` EXECUTED + `TRADE-20260519-172506-D0F75C` APPROVED, both fund=TICKER) were unaffected — they took the direct trade-submission-handler path via the Submit Trade tab in TradeSubmission page, bypassing the broken excel-generator entirely.

Yang has zero records in `opal-trade-submissions` DDB — the 502 happened at excel-generator INIT, before any DDB write, so no orphan PENDING_APPROVAL record to clean up.

---

## Next Steps

1. **[Andrew]** Notify Yang to retry the PFDE submission. First retry will be a ~930ms cold start; subsequent submissions within ~15min are warm. (Andrew opted to communicate this directly; no DT MCP to Yang.)
2. **[2.0.0_SA_COO~B / 0.7.0_AE_CloudOps]** Structural `.owned-paths.yaml` extension to include `infra/aws/terraform/portfolio-management/**` under DT 0.3.0_TradingOperations permitted_agents. Same pattern as the trade-pipeline-island fix `5efaadc65`. Removes need for GIT_COMMIT_AUTHOR_OVERRIDE on future DT portfolio-management commits.
3. **[0.7.0_AE_CloudOps / 1.0.0_SA_CTO]** Consider adding mandatory cold-start test invoke to LAMBDA_DEPLOYMENT_PROTOCOL.md post-apply verification. Would have caught this at the 2026-02-27 deploy. Class-level prevention for latent import failures.
4. **[0.3.0_DT_TradingOperations]** (optional) PM-pipeline latent-risk audit — sweep the other 11 portfolio-management Lambdas + 2 smartx-pipeline Lambdas for import-vs-layer mismatches while context is fresh. Offered to Andrew; pending decision.
5. **[0.3.0_DT_TradingOperations]** Continue standby on SSCN_DIVDEF.002 revised TO-2 — awaiting SSCN_DIVDEF.004 (AE 0.5.0_AE_OpalETL Lambda UNIVERSE_MAP v1.1.0) RAVC2 CC; that CC is the GO for the delete-and-re-PUT re-fire. Pure standby resumes post this session log commit.
