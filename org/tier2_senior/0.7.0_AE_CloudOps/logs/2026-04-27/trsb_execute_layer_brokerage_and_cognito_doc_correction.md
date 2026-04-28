# Session Log -- TRSB Execute Layer + Brokerage Internal + Cognito Doc Correction

**Agent:** 0.7.0_AE_CloudOps
**Date:** 2026-04-27 (late evening)
**Status:** WORK SHIPPED TO AWS; PENDING COMMIT (3 logical units)
**Tag (planned):** trade-pipeline-v1.6.3

---

## Live-test surface area

Andrew continued live-testing the trade flow on the portal after `trade-pipeline-v1.6.2` (timestamp + DASHBOARD_URL fix). Two new failures surfaced plus one doc-quality issue:

1. **Execute click 500** -- `Failed to generate Excel: No module named 'openpyxl'`
   - First failure path was `trade-workflow-handler` (excel_generator.py imports `openpyxl`)
   - Layer fix attached -> retry exposed the same error from a DIFFERENT Lambda: `trade-dashboard-api` (`/submissions/{id}/excel` route)
   - Both Lambdas import `openpyxl` for the Excel render path; both needed the layer

2. **Execute click 500 (after openpyxl fix)** -- `Execution failed: No email configured for brokerage: internal`
   - Trade was submitted with `brokerage='internal'` (form selection)
   - `BROKERAGE_EMAILS` dict in `config.py` had only vident/schwab/fidelity/interactive_brokers
   - 4 config.py files (sub, wf, dashboard, parquet) all need the same dict; mirrored

3. **Doc poisoning** -- agent prompts/READMEs/threads reference Cognito as the auth model
   - Andrew quote: "Why do you keep bringing up Cognito JWT? We have never used that."
   - Empirical check: `aws cognito-idp list-user-pools` returns empty in account 313476888478
   - Actual auth: custom RS256 JWT verified by Lambda@Edge `auth-validator-edge` against public key in Secrets Manager `opal/auth/jwt-public-key`
   - 25+ files in repo carry the wrong language; my own `prompt.md` is one of them and is the propagation source for me specifically

## Actions

### Unit A -- TRSB infra (openpyxl + 'internal' brokerage) -- LIVE in AWS, uncommitted

| Step | Detail | Result |
|------|--------|--------|
| Attach openpyxl-layer:3 to `trade-workflow-handler` (TF) | `layers = [arn:aws:lambda:us-east-1:${local.account_id}:layer:openpyxl-layer:3]` | terraform apply 1 changed |
| Attach openpyxl-layer:3 to `trade-dashboard-api` (TF) | same ARN | terraform apply 1 changed |
| Add `'internal'` to `BROKERAGE_EMAILS` in 4 config.py files | sub, wf, dashboard, parquet | ds-commit-gate.sh PASS on all 4 |
| Rebuild + deploy submission-handler zip | `aws lambda update-function-code` (placeholder.zip + lifecycle ignore_changes pattern) | codeSize 6980 Active |
| Rebuild + deploy workflow-handler zip | same path | codeSize 14365 Active |
| Rebuild + S3-upload dashboard-api zip with `--metadata content-sha256=` | required because raw `aws s3 cp` doesn't set content-sha256 metadata; TF references it via `data.aws_s3_object.metadata["content-sha256"]` -> "Invalid index" error first apply, fixed by re-upload with metadata | second apply Modifications complete after 13s |
| 0-diff TF plan post-apply | `No changes. Your infrastructure matches the configuration.` | PASS |

Live in AWS:
```
trade-workflow-handler:  layers=[openpyxl-layer:3]
trade-dashboard-api:     layers=[openpyxl-layer:3]
all 4 BROKERAGE_EMAILS dicts: includes 'internal' -> [andrew@opalinvest.com]
```

### Unit B -- prompt.md Cognito correction -- DONE, uncommitted

- `org/tier2_senior/0.7.0_AE_CloudOps/prompt.md:100` (Auth flow paragraph) -- replaced Cognito wording with custom RS256 JWT + Secrets Manager public-key flow + explicit "Never write 'Cognito'" injunction
- `org/tier2_senior/0.7.0_AE_CloudOps/prompt.md:155` (Issue #8) -- replaced "Cognito user pool not in any TF module" with "JWT public key in Secrets Manager not in any TF module"
- Feedback memory created: `memory/feedback_no_cognito_custom_jwt.md`, indexed at top of MEMORY.md Feedback section
- Memory includes empirical re-verify commands so future agents can ground-truth in 30 seconds

Out of scope per Andrew's directive but flagged for next session: `deliverables/pipeline_inventory.xml` (4 occurrences) + `deliverables/infrastructure_inventory.xml` (1 occurrence) carry the same wrong language. These are MY core docs but were not in tonight's edit scope.

Broader sweep of the other ~20 files org-wide is COO/CTO call -- not dispatched.

### Unit C -- ADHC_OWNPTH.009 tilde-form alias fix -- NEW, not yet started

CTO dispatched ~30-60min effort:
- Bug: owned-paths hook receives commit author `0.4.0_DS_ClientPlatform_B` (underscore) but YAML config has `0.4.0_DS_ClientPlatform~B` (tilde). Membership check fails, fires spurious WARN every tilde-lane commit.
- Fix: 5-line `normalize_serial` helper in `.tools/git-hooks/owned-paths-check.sh` that converts `~X` -> `_X` before comparison
- Why now: Phase 1 WARN mode masks the bug today; ADHC_OWNPTH.005 Phase 2 fail-closed flip will BLOCK every tilde-lane commit unless this lands first
- Validated: hook source has zero `normalize_serial`/tilde/underscore handling currently; not deprecated

## Validation that work is not redundant

| Unit | Empirical check | Result |
|------|----------------|--------|
| A | `aws lambda get-function-configuration ...layers` on workflow + dashboard | `openpyxl-layer:3` present (live, current session); `git status` shows lambdas.tf + 4 config.py modified+unstaged |
| A | `terraform plan` post-apply | `No changes` |
| B | `git log --oneline -- prompt.md` | last touch 754593d5 (org refresh, before Cognito text was current); my edit is unique; `git status` shows prompt.md modified |
| B | `aws cognito-idp list-user-pools` | empty (no user pools exist); confirms doc was wrong, not just stale |
| C | `grep -E "normalize_serial|tilde" .tools/git-hooks/owned-paths-check.sh` | no matches; fix not shipped |

## Compiler Tools

| Tool | Result |
|------|--------|
| `ds-commit-gate.sh` (py_compile + AST + ruff) | PASS x4 (all config.py files) |
| `terraform plan` (pre-apply) | 1-2 changes per apply, expected |
| `terraform plan` (post-apply) | 0-diff confirmed |

## Commit plan

Three logical units; ship as three commits to keep blast-radius small:

1. **Commit A (TRSB infra):** lambdas.tf + 4 config.py + plan to tag `trade-pipeline-v1.6.3`
2. **Commit B (doc):** prompt.md only -- no tag, no infra change
3. **Commit C (hook fix):** new TO ADHC_OWNPTH.009 -- separate commit, separate tag class (no pipeline tag)

All three use `safe-commit.sh --force` because the shared worktree index has 60+ COMP_LEARNS pod files staged by sibling agents (same as ADHC_OWNPTH.007 and trade-pipeline-v1.6.2 ships earlier in this session). FORCE-BYPASS audit entries serve as the trail.

## Open Items / Next Steps

- Commit A -> tag `trade-pipeline-v1.6.3` -> push --follow-tags
- Commit B -> push (org doc only, no tag)
- ADHC_OWNPTH.009 (CTO TO) -- start after commits A+B; gates ADHC_OWNPTH.005 Phase 2 flip
- `deliverables/pipeline_inventory.xml` + `infrastructure_inventory.xml` Cognito cleanup -- next session
- TRSB_TFIMPT.W3 (S3-backed migration for sub + wf handlers) -- still staged
- Decommission orphaned trade-form-ui (S3 + d1sqgm6c3x3jxy CloudFront + w8jnzvs21g API GW) -- new TO needed
- SES production-access form (Andrew action; packet ready)

## Cross-agent inbox

- COO 2.0.0 -- ADVI_ORIAPI.002 staged for ~B lane (gates AE 0.6.1~B Phase 0 RAVC); base lane no action
- COO 2.1.0 (COMP_LEARNS) -- routing nudge; my RAVC routing is already correct, informational only
- CTO 1.0.0 -- ADHC_OWNPTH.009 dispatch (Unit C above)
