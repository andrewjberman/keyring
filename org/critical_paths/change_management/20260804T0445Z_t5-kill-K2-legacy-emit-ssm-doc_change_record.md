# T5 DEAD-CONSUMER KILL K2 -- mdpf-legacy-emit-on-demand SSM doc + never-attached invoker policy (change record + rollback note)

**Executor:** 0.7.0_AE_CloudOps~F | **Opened:** 2026-08-04T04:45Z | **Status:** CLOSED 2026-08-04T04:53Z (destroy verified)
**Authorization:** COO GO 20260804T042634Z (CTO split-gate 042600Z, Andrew categorical). Kill-list row 10
(on-demand half) @b877dbc0f5; CVO census item 7 accessory, "dead-dead" class.

## WHAT DIES (exactly, nothing else)

The whole of `infra/aws/terraform/mdpf-pipeline/legacy-emit-ssm.tf` (2 resources):
1. `aws_ssm_document.mdpf_legacy_emit_on_demand` (SSM doc, on-demand legacy-compat emit bridge)
2. `aws_iam_policy.mdpf_legacy_emit_invoker` (managed policy `MDPFLegacyEmitInvoker`)

## WHY DEAD (reader evidence)

- Doc: ZERO invocations in the retained SSM command history (list-commands filter, empty -- window
  honestly ~30d, the SSM retention bound). Its write targets are denied (P0 deny pair) + reader-less
  (rows 6/9). The RUNNER CHAIN's in-dispatch Stage 3.5 does NOT use this doc (it runs the script
  directly from the dispatch) -- killing the doc does not touch the live chain.
- Policy: **ZERO attachments live** (list-entities-for-policy: no groups/users/roles -- the DS
  workstation attachment step its own comment describes NEVER HAPPENED). A never-attached policy
  granting SendCommand on a dying doc = dead grant, row-17 class.

## MECHANISM

TF-managed, mdpf-pipeline root -> whole-file source removal + targeted safe-apply (2 destroys).
No TF cross-references (iam.tf:122 mentions the doc in a comment only; the policy's reference to
aws_instance.mdpf_daily_runner is outbound-only -- the instance is untouched).

## ROLLBACK

`git revert` of the removal commit + targeted apply recreates both byte-identically (fully
source-declared). Historical definition at legacy-emit-ssm.tf@ce77c1107.

## POST-KILL VERIFY (filled at close)

- `aws ssm describe-document --name mdpf-legacy-emit-on-demand` -> InvalidDocument: **CONFIRMED 04:53Z**
  (positive control: opal-schwab-archive-01raw resolves on the same call shape).
- `aws iam list-policies` no MDPFLegacyEmitInvoker: **CONFIRMED 04:53Z** (empty result).
  Apply: 0/0/2 destroyed. Tag: mdpf-pipeline-v2.0.1 (covers K1+K2).
- Access window: zero invocations in retained SSM history pre-kill (stated above); policy had zero
  attached principals, so zero possible users.
