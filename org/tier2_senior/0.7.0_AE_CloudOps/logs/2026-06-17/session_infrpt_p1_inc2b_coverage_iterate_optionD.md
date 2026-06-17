# NFRA_INFRPT.P1 inc-2b coverage-iterate -- Option-D + comp-surface hardening verified (0.7.0_AE_CloudOps~B)

**archetype:** MIXED
**secondary_archetypes:** DEPLOY, DIAGNOSE, COORDINATE

Window: since the inc-2b deploy log (d2037d45c). Lane: 0.7.0_AE_CloudOps~B.

## Current State

inc-2b is fully iterated + verified. The DRIFT section's producer-backed legs are live, the coverage guard works, and the section caught real findings on its first full run.

- **Option-D (CTO ruling 173731Z) DEPLOYED** (`shared-infra-v1.26.0`): the CodeBuild read role = AWS-managed `ReadOnlyAccess` + an explicit DENY (`DenySensitiveDataReads`: dynamodb item-reads, logs bodies/StartQuery, kms:Decrypt, secretsmanager:GetSecretValue, ssm GetParameter*; `DenyFirmDataObjectReads`: s3:GetObject on `opal-data-*/*`). Replaced the hand-scoped read list (which had a long per-service tail). Apply 2-add/1-destroy (the destroy = the old inline read-policy rename). comp-iam 0 missing.
- **COVERAGE JUMP 6/29 (21%) -> 19/29 (66%)** on the re-run: ReadOnly cleared the per-service read-tail; the Deny held least-priv (0 modules broken -- plan needs config/metadata, not data). The guard honestly stays RED at 66% (< 0.8 floor) driven now by the config-tail (not perm gaps, not a false-clean).
- **10 REAL terraform-drift findings** (deployed != TF state), routed to COO for owner-dispatch: ~8 `aws_lambda_function [update]` (deployed-code-vs-source_code_hash; artifacts-uploaded-not-TF-reapplied; cross-corroborates the deploy-drift section; low-urgency per-pipeline reconcile) + 3 config divergences worth owner eyes (exec-summary `aws_cloudwatch_event_rule [DELETE]`, smartx `aws_instance [update]`, yang `aws_sfn_state_machine [update]`). Caveat: "update" diffs can include provider-recompute/tag-order noise -- owner confirms real-vs-noise.
- **comp-surface could-not-assess hardening LIVE-VERIFIED in CI** (via the CTO-added `workflow_dispatch`, c1a8aed6c): the dispatched run's `drift_state_comp` (commit 0176250e) = tools_failed 1, surface leg WATCH "scan loaded NO baseline (.comp-graph absent in CI) -> NO-OP; cannot assess". The rc-0-but-no-baseline false-clean is CLOSED -- a no-op scan no longer reads clean.

## Remaining continuation (not blockers -- the guard reports honest 66% meanwhile)

- Config-tail cannot-assess (10 modules): bd/cot/inf/mdpf `ec2.tf` + globgrph terraform-function errors + imo/m365/trade/seeking-alpha/shared-infra (var-requiring/plan-config). Per-module iterate.
- comp-baseline-in-CI provision: so `comp-surface-check scan` ASSESSES (loads a baseline) in CI rather than could-not-assess -- the comp-leg coverage continuation.
- The 10 drift candidates' owner adjudication (routed to COO).

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-iam | gaps (after each iam.tf change) | PASS | 0 missing (ReadOnly attach + Deny invisible to the Lambda/EC2 model) |
| ds-commit-gate.sh | drift_producer.py | PASS | comp-surface could-not-assess hardening clean |
| safe-apply.sh | -chdir=shared-infra apply | PASS | Option-D 2-add/1-destroy (policy rename); 0 infra-destroy |
| record-terraform-deploy.sh | shared-infra --version shared-infra-v1.26.0 | PASS | CHANGELOG + source-map |

**What worked:** Option-D (ReadOnly+Deny) is the right least-priv-vs-velocity synthesis -- coverage 21%->66% in one apply while preserving the sensitive-data Deny; the coverage guard correctly stays RED on the honest config-tail; the comp-surface could-not-assess hardening verified live (no-op no longer reads clean); the section surfaced 10 real-drift candidates on its first full run. **What failed:** my push didn't reliably trigger the hardened GH-Action run (shared-branch CI quirk) -- resolved by the CTO-added workflow_dispatch. **Gap:** the config-tail + the comp-baseline-in-CI (continuation).

## Blockers

None. inc-2b core + the coverage-iterate are done/verified. The continuation (config-tail + comp-baseline) is iterate-on-the-run.

## Next Steps

- **[module owners, via COO]** Adjudicate the 10 drift candidates (real-vs-noise); the exec-summary rule-delete + smartx-EC2 + yang-sfn are highest-signal. AE owns smartx + partners if routed.
- **[0.7.0_AE_CloudOps~B]** Config-tail per-module iterate + the comp-baseline-in-CI provision (comp-leg coverage). Then the deliberate queue: volatility-fetcher adjudication + stale source-map fix; deploy-role OIDC hardening. Standing: GCONTR TO-3 contract-row load.

## Files Modified

See commit messages: `f78513bb4` (Option-D ReadOnly+Deny + comp-surface hardening), `ca3da2269` (record v1.26.0). GH-Action `workflow_dispatch` added by CTO (c1a8aed6c, BASE_EXEC).
