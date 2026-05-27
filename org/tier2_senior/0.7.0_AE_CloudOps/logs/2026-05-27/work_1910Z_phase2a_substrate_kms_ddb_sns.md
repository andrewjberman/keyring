# work_1910Z -- Phase 2A substrate authoring (KMS + DDB + SNS TF) per spawn-msg STANDBY-PREP

**Agent:** 0.7.0_AE_CloudOps~A
**Cycle:** /work cycle 2 (substantive — STANDBY-PREP class)
**Authority:** ws COO `[SPAWN-WITH-DIRECTION]` 2026-05-27T18:08Z + `[RAVC2-ACCEPT]` FIND_INSURE.005 2026-05-27T19:02Z; PRD `FIND_INSURE.md` v0.4 (`a9b72b942`) §3.1 + §3.5 + §3.6 + §3.7

## Inbound this cycle

| T | From | Subject | Disposition |
|---|---|---|---|
| 19:02Z | ws COO | `[RAVC2-ACCEPT] FIND_INSURE.005` | ACK; .005 closed; AE~B v0.4.0 + DS~A Followup-Stage-3 cascade unblocked downstream |

## Outbound this cycle

| T | To | Subject | Class |
|---|---|---|---|
| (this cycle) | ws COO | Phase 2A substrate authoring progress MCP | STANDBY-PREP-progress |

## Substantive artifacts shipped (STANDBY-PREP — authored + committed; apply gated on Phase 1 cascade close + Andrew subset-cut)

### 1. `infra/aws/terraform/imo-pipeline/kms.tf` — NEW

`find-insure-data-key` CMK (SYMMETRIC_DEFAULT; ENCRYPT_DECRYPT usage) per PRD v0.4 §3.1 UNK-1 Option 2:
- `enable_key_rotation = true` (annual AWS-managed rotation per condition 3)
- `deletion_window_in_days = 30` (default safety)
- Key-policy: root account = admin; `find-insure-lambda-role` = `kms:Decrypt + DescribeKey + Encrypt + GenerateDataKey + ReEncryptFrom + ReEncryptTo` (condition 2 v0.1 scope; portal/IR Phase 3b NOT granted)
- Alias: `alias/find-insure-data-key` (stable identifier across rotation generations)
- IAM amendment: `aws_iam_role_policy.find_insure_kms` attaches `kms:GenerateDataKey + GenerateDataKeyWithoutPlaintext + Decrypt + DescribeKey` to `find-insure-lambda-role` on the CMK ARN
- Outputs: `find_insure_data_key_arn` + `find_insure_data_key_alias`
- **Scope discipline:** bucket default SSE stays SSE-S3; KMS-scope prefixes (bronze/linkedin + bronze/job-posting + silver/linkedin + silver/job-posting + serving/*) handled via Lambda-code-level `ServerSideEncryption=aws:kms + SSEKMSKeyId` PUT params (DS authoring discipline). Non-PII prefixes (web-scrape bronze/silver/gold + code/config/telemetry/qa/archives) stay SSE-S3. No bucket-default change.

### 2. `infra/aws/terraform/imo-pipeline/dynamodb.tf` — NEW

`find-insure-cost-state` table per PRD v0.4 §3.5 Q-C1 + cost-gate brief v0.3 §6:
- `billing_mode = PAY_PER_REQUEST` (on-demand; ~$1/yr volume)
- `hash_key = pk` + `range_key = sk` (single-table pattern; pk/sk shape per cost-gate brief §6)
- `attribute pk + sk = S`
- `ttl.enabled = true + attribute_name = ttl` (7-day rolloff on daily/monthly items per brief §6)
- `point_in_time_recovery.enabled = true` (35-day continuous backup; trivial cost; protects against ADD/PUT corruption)
- IAM amendment: `aws_iam_role_policy.find_insure_dynamodb` attaches `dynamodb:UpdateItem + GetItem + Query + PutItem` to `find-insure-lambda-role` on the table ARN
- Outputs: `find_insure_cost_state_table_name` + `find_insure_cost_state_table_arn`
- **Schema item shape (Lambda-code authority):**
  - `pk="global", sk="daily#YYYY-MM-DD"` → `credits_used: int`
  - `pk="global", sk="monthly#YYYY-MM"` → `credits_used: int`
  - `pk="imo#{slug}", sk="total#YYYY-MM-DD"` → `credits_used: int`
  - `pk="imo#{slug}", sk="class#{class}#YYYY-MM-DD"` → `credits_used: int`
  - `pk="headers", sk="last_rate_limit"` → `{x-minute/hourly/daily-requests-left, captured_at}`

### 3. `infra/aws/terraform/imo-pipeline/sns.tf` — NEW

`find-insure-budget-alerts` SNS topic per PRD v0.4 §3.6 Q-C2:
- `kms_master_key_id = aws_kms_key.find_insure_data_key.id` (SSE-KMS at-rest for the topic; coverage extends to messages-in-flight pre-fanout)
- Optional Andrew email subscription via `var.find_insure_budget_alerts_andrew_email` (count gate — empty string skips; provisioning-time decision)
- IAM amendment: `aws_iam_role_policy.find_insure_sns` attaches `sns:Publish` to `find-insure-lambda-role` on the topic ARN
- Outputs: `find_insure_budget_alerts_topic_arn` + `find_insure_budget_alerts_topic_name`
- **Subscribers v0.1:** Andrew email default (variable-gated). Future subscribers (IR-team-budget-watcher, COO operational, CVO verification-channel) added via TF amendment per cost-gate brief §15.2.

## Apply-gating posture

**TF authored + committed; apply DEFERRED.** Per spawn-msg sequencing: "STANDBY-PREP NOW + execute post-Phase-1-RAVC2-Accept: KMS+DDB+SNS Terraform authoring (substrate-ready; can ship Terraform now, apply between Phase 1 RAVC2 + Phase 2A live-call)".

Phase 1 RAVC2-Accept: ✅ landed 19:02Z (`[RAVC2-ACCEPT] FIND_INSURE.005`).

Pending pre-apply:
- Andrew subset-cut decision (which IMOs from 99-universe ship into Phase 2A first-run)
- Andrew email binding for SNS subscription (`find_insure_budget_alerts_andrew_email` -var)
- AE~B v0.4.0 (Phase 1 .006 score-web ship) — coordinates apply window to avoid concurrent in-flight terraform-apply collisions
- Optional: `find-insure-parse-deps` layer (Phase 2A LinkedIn parsers: pyarrow + pandas + jsonschema per DS~C dep profile §3.32Z) — author + build + upload pre-apply so single `imo-pipeline-v0.X.0` apply lands all Phase 2A substrate atomically

Estimated apply-readiness: ~30-60min wall pending the above.

## Next sub-steps

- MCP ws COO with substrate-authoring progress + Andrew-email-binding ask
- Begin `find-insure-parse-deps` layer (pyarrow + pandas + jsonschema; ~110MB; manylinux2014_x86_64 wheels for python3.9) authoring — separate from KMS+DDB+SNS substrate (DS~C reciprocity 18:32Z)
- Stand-by for AE~B v0.4.0 cascade close
- Stand-by for Andrew subset-cut signal

## archetype

IMPLEMENT (TF authoring) -- apply DEFERRED to STANDBY-PREP completion + cascade green.
