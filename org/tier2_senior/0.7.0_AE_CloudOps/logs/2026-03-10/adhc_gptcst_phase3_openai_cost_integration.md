# ADHC_GPTCST Phase 3: OpenAI Cost Integration + SmartX Supervisor Fixes -- 0.7.0_AE_CloudOps

**Date:** 2026-03-10
**Start Time:** 16:00
**End Time:** 17:00

## Objective

Implement ADHC_GPTCST.001 Phase 3: wire per-function OpenAI token spend into the morning
infrastructure report, fix function name mismatches in the existing cost tracker, and apply
the two immediately actionable SmartX EC2 supervisor fixes (model downgrade + secret name bug).

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Read task order, agent context, thread receipt | Full context established |
| 2 | Check OpalETL dependency status | PENDING -- their OPENAI_USAGE work not yet started |
| 3 | Confirm canonical Lambda names vs lambda-source-map.json | 6 names confirmed |
| 4 | Check secret name pattern across all Lambda callers | `opal/external-apis` is canonical |
| 5 | Implement all code changes (4 files) | Changes written locally |
| 6 | Commit | `1f6bc00e` feat(ADHC_GPTCST): Phase 3 OpenAI cost tracking + SmartX supervisor fixes |
| 7 | terraform plan | SKIPPED -- opal-infrastructure-monitor has no Terraform resource |
| 8 | safe-ec2-deploy.sh | SKIPPED -- SmartX EC2 host unknown (no Elastic IP) |

---

## Work Completed

### 1. R1: Function Name Fixes (Unblocked)

**`lambda_function.py` -- OPENAI_LAMBDAS:**

Before:
```python
OPENAI_LAMBDAS = [
    "opal-news-layer3-curation",
    "news-trending-analysis",
    "opal-trending-image-generator",
    "opal-infrastructure-monitor"
]
```

After (canonical 6 names from lambda-source-map.json):
```python
OPENAI_LAMBDAS = [
    "news-trending-analysis",
    "opal-news-layer3-curation",
    "semantic-news-layer3-curation",
    "keyword-intelligence-generator",
    "opal-trending-image-generator",
    "opal-infrastructure-monitor",
]
```

**`openai_cost_tracker.py` -- COST_PER_CALL_BY_SERVICE key fix:**
- `trending-image-generator` renamed to `opal-trending-image-generator` (opal- prefix was missing)

### 2. R2: Token-Accurate Cost Path (Code-Complete; Awaiting OpalETL Deploy)

New additions to `openai_cost_tracker.py`:

- `MODEL_PRICING` table: gpt-4o ($2.50/$10.00 per 1M), gpt-4o-mini ($0.15/$0.60 per 1M),
  text-embedding-3-small ($0.02/1M), gpt-4-turbo-preview ($10.00/$30.00 per 1M)
- `TRACKED_LAMBDAS`: canonical list of 6 Lambda names
- `_USAGE_RE`: compiled regex for `OPENAI_USAGE function=X model=Y prompt=N completion=N total=N`
- `query_openai_usage_logs(function_name)`: queries `/aws/lambda/{function}` log group with
  filterPattern `"OPENAI_USAGE"`, handles pagination up to 5000 events, returns parsed records
- `_compute_token_cost(model, prompt_tokens, completion_tokens)`: applies pricing table;
  falls back to gpt-4o-mini for unknown models
- `get_openai_cost_section()`: orchestrates per-function cost:
  - Token-accurate path when OPENAI_USAGE lines found
  - Fallback to call-count x empirical multiplier when absent
  - Returns `{by_function, grand_total, no_usage_lines}` dict

### 3. R3: Morning Report Integration

`lambda_function.py` changes:
- Added `from openai_cost_tracker import get_openai_cost_section` import
- Added step 7 in `lambda_handler()`: `report["sections"]["openai_cost"] = get_openai_cost_section()`
- Added "OPENAI COST (Last 24h)" section in `format_report()` showing:
  - Per function: model(s), tokens (24h), est. cost
  - Fallback line for functions without OPENAI_USAGE lines (with explicit label)
  - Grand total
  - WARN list for functions with no OPENAI_USAGE lines detected

Also updated `lambda-source-map.json`: added `openai_cost_tracker.py` to
`opal-infrastructure-monitor.files[]` and added `_deploy_note` flagging missing Terraform.

### 4. R4: SmartX EC2 Supervisor Fixes

**`ai-supervisor-v2.py` changes:**

a. Model downgrade + escalation:
   - `CONFIG['openai_model']` changed from `'gpt-4o'` to `'gpt-4o-mini'`
   - Added `consecutive_failures` counter in `run_ai_agent()` loop
   - After each tool call: if result `success == False`, increment; if `success != False`, reset to 0
   - When `consecutive_failures >= 3` and current model is not already `gpt-4o`: escalate to `gpt-4o`
   - Log message: `ESCALATION: N consecutive tool failures -- upgrading to gpt-4o`

b. Secret name fix:
   - Was: `SecretId='ai/claude-api-key'` (Claude key, wrong secret entirely)
   - Now: `SecretId='opal/external-apis'`, parse JSON, return `secret_data.get('openai_api_key')`
   - Verified: `opal/external-apis` is used by semantic-news-layer3-curation,
     security-sweep-comprehensive, seeking-alpha-*, causality-* Lambdas -- confirmed canonical

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Keep `market-update-generator` in COST_PER_CALL_BY_SERVICE | Task says "add opal- prefixes where missing" -- market-update-generator name is correct; it's a valid caller tracked for cost even if not in the canonical 6 OPENAI_LAMBDAS |
| Implement token-accurate path now even without OpalETL log lines | Functions cleanly return 0 records and fall back to call-count path; code is ready the moment OpalETL deploys |
| Unknown model fallback to gpt-4o-mini in pricing | Conservative -- gpt-4o-mini is cheapest; avoids inflating cost estimates for unrecognized models |
| Do not deploy infrastructure-monitor | No Terraform resource exists; CLAUDE.md rule 1 prohibits aws lambda update-function-code |
| Do not run safe-ec2-deploy.sh for SmartX | EC2 host is null in EC2_MANIFEST.json -- instance has no Elastic IP, host changes on restart; cannot SSH without knowing current IP |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/lambda/infrastructure_monitor/lambda_function.py` | OPENAI_LAMBDAS canonical 6 names; import get_openai_cost_section; add step 7; add OPENAI COST section in format_report() | Yes -- `1f6bc00e` |
| `infra/aws/lambda/infrastructure_monitor/openai_cost_tracker.py` | Fix key prefix; add MODEL_PRICING, TRACKED_LAMBDAS, _USAGE_RE, query_openai_usage_logs(), _compute_token_cost(), get_openai_cost_section() | Yes -- `1f6bc00e` |
| `infra/aws/ec2/smartx-exporter/ai-supervisor-v2.py` | Model gpt-4o-mini default; escalation logic; fix get_openai_key() to opal/external-apis | Yes -- `1f6bc00e` |
| `infra/aws/lambda/ci/lambda-source-map.json` | Add openai_cost_tracker.py to opal-infrastructure-monitor files; add _deploy_note | Yes -- `1f6bc00e` |

---

## Blockers

- BLOCKED on deploy: `opal-infrastructure-monitor` has no Terraform resource.
  Evidence: `lambda-source-map.json` entry has no `tf_resource` or `artifact_s3_key` fields.
  Cannot deploy per CLAUDE.md rule 1. Requires 0.7.0_AE_CloudOps to create Terraform module
  for this Lambda in a future session, then deploy.

- BLOCKED on SmartX EC2 deploy: `smartx-exporter` EC2 instance has no Elastic IP.
  `ec2_host: null` in EC2_MANIFEST.json. Cannot run safe-ec2-deploy.sh without current host.
  Requires: start instance, run sync-ec2-manifest.sh to refresh host, then deploy.

- BLOCKED on R2 data: token-accurate path in openai_cost_tracker.py will produce fallback-only
  output until `0.5.0_AE_OpalETL` deploys OPENAI_USAGE log lines (their task order pending as
  of 2026-03-10, last OpalETL log is 2026-03-06 -- ADHC_GPTCST.001 not yet started).

---

## Current State

**Status:** IN PROGRESS (code complete; deploy blocked on two issues)
**Active branch:** `CLOUD`
**Commit:** `1f6bc00e`

All R1-R4 code changes are committed to CLOUD. The infrastructure_monitor Lambda source is
updated with canonical OPENAI_LAMBDAS, full token-accurate cost tracking code, and the new
report section. The SmartX supervisor is updated with gpt-4o-mini default, escalation logic,
and the correct `opal/external-apis` secret. Neither service can be deployed in this session:
infrastructure-monitor lacks Terraform, SmartX EC2 host is unknown. Once OpalETL Phase 2
deploys OPENAI_USAGE lines, the token-accurate path will activate automatically.

---

## Next Steps

1. **[0.7.0_AE_CloudOps] Create Terraform for opal-infrastructure-monitor** -- build infrastructure-monitor
   Terraform module (S3-backed, same pattern as other pipelines), add to lambda-source-map.json,
   deploy, tag. This is a prerequisite for any future code deploys to this Lambda.

2. **[0.7.0_AE_CloudOps] Deploy SmartX supervisor** -- once smartx-exporter instance is running,
   run `sync-ec2-manifest.sh` to populate ec2_host, then `safe-ec2-deploy.sh smartx-exporter`
   from repo root. Verify ai-supervisor-v2.py is on EC2 with `grep openai_model` check.

3. **[0.5.0_AE_OpalETL] Deploy OPENAI_USAGE log lines** -- their task order ADHC_GPTCST.001
   must deploy the standardized print() after every OpenAI call. Once live, CloudWatch logs
   will have OPENAI_USAGE lines and the token-accurate path in get_openai_cost_section() will
   produce real data instead of fallback estimates.

4. **[0.7.0_AE_CloudOps] Verify morning report OPENAI COST section** -- after infrastructure-monitor
   is deployed and OpalETL Phase 2 is live, trigger a test invocation and confirm the OPENAI COST
   section appears in the report with per-function token counts and cost.

**Files to touch next:**
- `infra/aws/terraform/infrastructure-monitor/` -- new module to create
- `infra/aws/lambda/ci/lambda-source-map.json` -- add tf_resource, artifact_s3_key after TF setup
- `infra/aws/ec2/EC2_MANIFEST.json` -- refresh ec2_host for smartx-exporter after instance start

**Do NOT:**
- Use `aws lambda update-function-code` to deploy infrastructure-monitor (CLAUDE.md rule 1)
- Edit ai-supervisor-v2.py directly on EC2 (EC2_CODE_DEPLOYMENT_STANDARD.md)
- Run safe-ec2-deploy.sh before ec2_host is populated in EC2_MANIFEST.json
