# NFRA_INFRPT.P3 -- sections C (graph-HEAD) + D (contract-integrity) + delivery upgrade: LANDED + live-verified
**archetype:** DEPLOY
**secondary_archetypes:** IMPLEMENT, VALIDATE

**Serial:** 0.7.0_AE_CloudOps | **Window:** session start (~2026-07-08T00:20Z) -> 01:10Z | **TO:** NFRA_INFRPT.P3 (COO~B GO 221505Z)

## Summary

Built + deployed + live-verified the tail of NFRA_INFRPT (the daily `opal-infrastructure-monitor`
report). Two new sections + a delivery upgrade, all under the HARD false-clean discipline:

- **C (GRAPH-HEAD freshness):** `check_graph_head()` reads the globgrph Nessie branch-head marker
  (the HEAD oracle). Absence = UNKNOWN-VINTAGE RED; stale >50h = FROZEN RED (distinct reasons ->
  the "distinguish stale from unverifiable" criterion). Lightweight, in-Lambda, marker-only.
- **D (CONTRACT-INTEGRITY):** producer/consumer seam. NEW producer
  `infra/aws/globgrph/publish_contract_integrity.py` runs the NFRA_GCONTR Q1/Q2 engine + computes
  the false-clean qualifier -> publishes `s3://opal-313476888478-globgrph/contract_integrity/latest.json`;
  the Lambda's `check_contract_integrity()` consumes it (the report Lambda cannot run the heavy
  pyiceberg engine). Absence/stale/engine-fail = RED (monitor blind), never silent-clean.
- **FALSE-CLEAN (HARD):** the bare "0 UNSANCTIONED" is ALWAYS CHECKED/BLIND-qualified. Live output:
  3 CHECKED / 0 surface-BLIND; 2 uncontracted SEV1 (advisor_intelligence + model_portfolios.headline,
  LOUD); 5 inert never-widen tripwires (forbidden_writers name 0 live IAM role); 2 grain=bucket
  ADVISORY forbidden-axes; period_defs value-check (Q3, CVO-owned) UNWIRED; EC2-WRITES-derive VISIBLE
  (06-17 fix confirmed live).
- **DELIVERY:** action-first STATUS SUMMARY header (worst-first OK/WATCH/ACT/RED) + emoji subject ->
  ASCII [RED]/[ACT]/[OK] (charmap-safe) + agent-consumable feed
  `s3://opal-data-portal-v2/infrastructure/status/latest.json` (per-section STATUS + action_required
  + red_sections/act_sections = the COO /drive signal source).

Caught + fixed a real bug during local testing: my new summary constant `_STATUS_RANK` (uppercase)
name-COLLIDED with a pre-existing module-global `_STATUS_RANK` (lowercase, used by `_worst_status`
+ freshness) -> renamed mine to `_SUMMARY_RANK`. (Local end-to-end handler test caught it pre-deploy.)

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-surface-check | `check`/`contract-selfcheck` help + Q2 source read | PASS | confirmed the Q2 (UNSANCTIONED) engine surface + subcommands |
| contract_engine (GCONTR) | `run_contract_check("latest")` (dev-box recon) | PASS | GCONTR LIVE: 3 contracts, all WATCH, grain=bucket; the section-D content |
| comp-kuzu | provenance header (killed -- DB-lock contention w/ other agents) | N/A | not needed: read the marker (`_branch_head.main.json`) directly = the same HEAD oracle |
| comp-iam | `service opal-infrastructure-monitor` + `gaps` | PARTIAL | role is by-ARN not a TF resource -> DESIRED can't model inline policies (UNKNOWN); per Rule 22a ground-truthed on live `get-role-policy` (applied) + invoke (exercised) |
| commit-gate.sh | on both new/modified .py | PASS | py_compile + ruff + AST clean, both files |
| terraform plan/safe-apply | shared-infra | PASS | 1-add/1-change/0-destroy; 0-diff re-plan = No changes |

**What worked:** running the contract engine on the dev-box (StaticTable S3 path, no in-VPC catalog
needed) gave the real Q2 verdicts + the observed-writer set = the exact false-clean inputs.
**What failed:** comp-kuzu hung on DB-lock contention (multiple agents) + the dev-box default boto3
S3 client hit a transient TLS virtual-host flake (custom-Config client + aws-cli both fine) -- both
dev-box artifacts, irrelevant in-Lambda. comp-iam can't model a by-ARN role's inline policies.
**Gap found:** comp-iam DESIRED is blind to inline policies on an ARN-referenced role -- for a fresh
IAM change the applied+exercised grounding (get-role-policy + invoke) is mandatory, as Rule 22a says.

## Deployment Sequence + Verification (AE)

1. commit source `2b45cd422` (lambda_function.py + publish_contract_integrity.py + infra-monitor.tf + ledger)
2. `build-and-upload.sh shared-infra opal-infrastructure-monitor` -> zip sha `r/bjjp5dJMcxw4NnzSNFsUCpYlWrH+sJsVJu+JiWxs8=`
3. commit source-map `e7a30eb53`
4. `terraform plan`: `Plan: 1 to add, 1 to change, 0 to destroy` (MonitorGraphHeadContractRead + code hash)
5. `safe-apply` (HALT-gate passed): `Apply complete! Resources: 1 added, 1 changed, 0 destroyed`
6. 0-diff re-plan: `No changes. Your infrastructure matches the configuration.`
7. `record-terraform-deploy shared-infra --version shared-infra-v1.42.0` -> `5af96e9f9`; tag + `push --follow-tags`
8. deploy-completion ledger opened+CLOSED (3 legs proven); ledger commit `ff935886f`

**Verification (Rule 22a desired+applied+exercised):**
- applied: `aws iam get-role-policy ... MonitorGraphHeadContractRead` -> the 2 globgrph resources landed.
- exercised: `aws lambda invoke opal-infrastructure-monitor` -> `[END] 174.6s`, emailed andrew@opalinvest.com,
  archived `.../reports/2026-07-08/00-58-43.json`, `[FEED] Published ... (overall=RED, action_required=True)`.
  Live archived report: **C graph_head = OK** (HEAD current 0.4h, no AccessDenied -> IAM works);
  **D contract_integrity = WATCH, engine=ok**, false_clean rendered (uncontracted_sev1=[advisor_intelligence,
  model_portfolios.headline], surface_blind=0, ec2_visible=True).

## Files Modified

See commit messages: `2b45cd422` (3 source files + ledger), `e7a30eb53` (source-map), `5af96e9f9`
(deploy record + CHANGELOG), `ff935886f` (ledger close). Key: `infra/aws/lambda/infrastructure_monitor/lambda_function.py`
(+2 checks, summary/feed helpers, format banners, ASCII subject, `_SUMMARY_RANK` rename);
`infra/aws/globgrph/publish_contract_integrity.py` (NEW producer); `infra/aws/terraform/shared-infra/infra-monitor.tf`
(+MonitorGraphHeadContractRead).

## MCP traffic

~6 messages. Significant: COO~B GO NFRA_INFRPT.P3 (221505Z) + GO AGENTBUS.S3 (223540Z, sequenced after P3);
CTO HOLD/SUPERSEDE on cot re-provision (Andrew-PRD in flight -- held, no action); DS~B bd-client-detail
edge-correction thread (separate lane, queued). Sent: RAVC to COO~B on P3; FYI to DS~B (producer schema +
value-check plug-in).

## Blockers

None. P3 core is complete + live-verified. One BOUNDED follow-on (not a blocker): the producer needs a
recurring schedule (right home = the nightly Fargate derive-runner; needs a Dockerfile copy + container
rebuild). The Lambda's absence-guard goes loud RED if the artifact exceeds 30h stale, so no silent-failure
risk in the interim. RAVC'd to COO for the who-takes-the-container-fold decision.

## Current State

- `opal-infrastructure-monitor` (shared-infra, python3.12, 512MB/180s) is deployed at
  `shared-infra-v1.42.0` with sections C + D + the delivery upgrade. Role `opal-portal-lambda-role`
  now carries inline policy `MonitorGraphHeadContractRead` (GetObject on the 2 globgrph keys).
- Producer `infra/aws/globgrph/publish_contract_integrity.py` published a fresh
  `s3://opal-313476888478-globgrph/contract_integrity/latest.json` (WATCH, engine=ok).
- Agent feed live at `s3://opal-data-portal-v2/infrastructure/status/latest.json`.
- Daily report fires 13:00 UTC (EventBridge `infrastructure-monitor-daily`, console-managed).

## Next Steps

- **[2.0.0_SA_COO~B]** flip NFRA_INFRPT.P3 TO to complete on the RAVC; decide who takes the producer
  container-fold into the Fargate derive-runner; wire the /drive consumer off the status feed (co-design offered).
- **[0.7.0_AE_CloudOps]** GUARD-REFILE watchdog-rearm leg-B (low-pri P3 tail), then NFRA_AGENTBUS.S3
  (COO~B GO received, sequenced after P3). Also queued: the DS~B bd-client-detail comp-trace edge-correction
  (globgrph-ingestion lane).
- **[3.0.0_SA_CVO~B]** the period_defs value-check (Q3) is the one unwired contract-integrity limb -- when
  authored+published, the producer folds it in (value_check.status -> "wired") + the Lambda renders it.
- **FLAG (pre-existing, not P3):** the report ran 174.6s vs the 180s ceiling (AI-error-analysis path is the
  driver) -- worth a follow-on timeout raise / AI-path optimization before it clips.
