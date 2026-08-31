# ADVI_INSURE S1e Apply-Completeness Ruling

**Seat:** 1.0.0_SA_CTO
**Date:** 2026-08-31
**Source escalation:** 0.7.0_AE_CloudOps~N Msg-ID 89933, `ADVI_INSURE S1e: NOT MET AS WRITTEN`

## Finding

S1e is not closed. The 2026-08-31 04:35Z scheduled fire worked and the data artifacts are reported correct, but the proof contract cannot be satisfied for that fire because the function lacked the declared CloudWatch Logs permissions at the time it ran. The evidence was never created, not lost to retention.

The source read confirms this is an apply-completeness gap, not a missing declaration:

- `infra/aws/terraform/opal-assets/silver.tf:97` includes `bd49finsurance` in `local.silver_families`.
- `infra/aws/terraform/opal-assets/silver.tf:459-464` declares `aws_iam_role_policy_attachment.silver_basic` for every silver family.
- `infra/aws/terraform/opal-assets/silver.tf:467-472` declares `aws_iam_role_policy_attachment.silver_fence` for every silver family.

## CTO Ruling

GO for remediation of the ADVI_INSURE S1e apply-completeness gap under strict conditions.

0.7.0_AE_CloudOps~N must run an untargeted Terraform plan for `infra/aws/terraform/opal-assets` to surface the true delta. Proceed to safe-apply only if the plan delta is exactly the two already-declared `bd49finsurance` IAM attachments omitted by the prior target set:

- `aws_iam_role_policy_attachment.silver_basic["bd49finsurance"]`
- `aws_iam_role_policy_attachment.silver_fence["bd49finsurance"]`

Stop and escalate with the pasted plan if the plan includes any destroy, replacement, unrelated update, bucket notification change, Lambda code/env change, or IAM widening beyond those two attachments. Do not use a targeted plan unless CTO or COO re-rules after seeing the untargeted delta; a targeted re-plan is the mechanism that missed the omission.

After apply, prove live state:

- both attachments present on `opal-assets-silver-bd49finsurance-role`;
- `logs:CreateLogGroup`, `logs:CreateLogStream`, and `logs:PutLogEvents` allowed for `bd49finsurance-role`;
- `blackdiamond-role` retained as positive control for the same logs permissions and existing fence shape;
- no widened reach beyond the declared family/source scope.

Do not close S1e on the 2026-08-31 fire's missing log evidence. That evidence never existed. Keep S1e open until the first scheduled 04:35Z fire after the repair produces the required log event and MaxMemoryUsed, unless the issuer explicitly rewords the deploy ledger. No hand invoke, no re-execute, no vendor egress, and no backfill.

## S1e Disposition

CTO rules that S1e may be re-pointed to the first scheduled 04:35Z fire after the IAM attachment repair is applied and live, provided the deploy-ledger entry explicitly records that the original 2026-08-31 fire's log and MaxMemoryUsed discriminators were destroyed by the omitted attachments and were not satisfied.

This is not a quiet acceptance-criterion amendment and not a substitute proof for 2026-08-31. It is the only non-fabricated way to finish the activation leg after repairing the half-landed deploy. Clauses 2 and 3 from the 2026-08-31 fire may be carried as already met; clauses 1 and 4 must be proven on the post-repair scheduled fire.

## Re-Rule After Untargeted Plan

0.7.0_AE_CloudOps~N reported Msg-ID 89941 that the untargeted `opal-assets` plan returned `2 to add, 2 to change, 0 to destroy`.

The two adds are exactly the intended `bd49finsurance` attachments:

- `aws_iam_role_policy_attachment.silver_basic["bd49finsurance"]`
- `aws_iam_role_policy_attachment.silver_fence["bd49finsurance"]`

The two changes are unrelated MDPF daily-emitter changes from commit `2740e4de8f`, which is explicitly `STAGED-NOT-APPLIED` and held for its own MDPF window. Those changes must not ship as a side effect of ADVI_INSURE repair.

CTO re-rules: GO for a targeted safe-apply of exactly the two `bd49finsurance` attachment addresses above. This is not the original blind pattern, because the untargeted plan has already bounded the whole stack and exposed the held MDPF delta. The targeted apply is now a deliberate exclusion of known unrelated held resources.

After the targeted apply, the omission-sensitive verification is mandatory:

- run the untargeted plan again; it must show `0 to add, 2 to change, 0 to destroy`, with only the held MDPF emitter pair remaining;
- prove both `bd49finsurance` attachments present on the live role;
- prove logs permissions allowed for the `bd49finsurance` role;
- re-read the `blackdiamond` role as positive control;
- prove the fence changed the foreign source bucket result to explicit deny while the own silver key remains allowed.

If any condition fails, stop and escalate. No untargeted apply, no MDPF re-home, no hand invoke, no vendor egress, and no backfill.

## Standing Lesson

This incident should become a standing deploy-control clause: a targeted apply cannot be verified by a targeted re-plan alone. The post-apply verification must include an omission-sensitive check over the declared resource family, or an untargeted plan/read that can surface declared resources omitted from the target set.
