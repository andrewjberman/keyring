# work-cycle 0011 — R2 opal-data-bd lifecycle (C2) APPLIED + pre-apply safety catch; GO#1 yield-curve correct-path flush

**archetype:** DEPLOY
**secondary_archetypes:** DIAGNOSE, VALIDATE, COORDINATE
**Date:** 2026-06-05 ~1606-1635Z
**Trigger:** COO Andrew-GO x3 (yield-curve flush / R2 apply / PAT cleanup)

## GO#1 — yield-curve CDN force-flush (CLOSED) + root-cause
Andrew "force fix now" — still saw stale after my first flush. ROOT CAUSE: FE fetches /api/general/macro/yield_curve_fred.json (portal/src/api/endpoints/yield-curve.ts:48), NOT the /json/macro/ S3 key path I'd invalidated. CloudFront path-rewrites; invalidating the S3-key path flushed a path the FE never requests. Invalidated the CORRECT path (IAVE3B37..., /api/general/macro/*) -> Completed. anon curl 401 = path confirmed auth-gated (not 404). RAVC2 COO. Memory saved (reference_aws_cli_leading_slash_path_args_use_powershell, +path-rewrite gotcha).

## GO#2 — R2 lifecycle (C2 destructive) — the headline + the catch
DS handed the gold/+platinum/-scoped 36d NoncurrentVersionExpiration on opal-data-bd. CTO gated: explicit Andrew apply-GO required (separate from proof-green). Staged: dedicated isolated TF root (bd-bucket-lifecycle/, minimal blast radius), import-then-modify, plan-verified -> HELD for GO.
**PRE-APPLY SAFETY CATCH:** Andrew GO'd "apply now" but DS's staged HCL (3 rules) REMOVED the whole-bucket 90d rule -> silver/bronze/schwab/code/custodian noncurrent versions would never expire = storage GROWTH (anti-cost-reduction), contradicting COO's GO text ("stay on 90d"). HELD the irreversible apply + surfaced to COO+DS. DS confirmed: my catch correct, his 3-rule HCL was a genuine error -> Option B (4 rules) authoritative.
APPLIED Option B: commit ed495558f -> safe-apply (HALTGT) 0/1/0 -> 0-diff -> LIVE 4 rules verified (whole-bucket 90d KEPT + gold/36d + platinum/36d + abort-MPU 7d).
**CTO overlap must-verify SATISFIED:** AWS doc (lifecycle-conflicts) "if two expiration policies overlap, the SHORTER is honored"; Example 3 = exact analog (empty-prefix + scoped-prefix -> shorter wins) -> gold/+platinum/ resolve to 36d (not masked by 90d). Option B delivers the ~$27/mo. Empirical = DS tracks BucketSizeBytes on the scheduled cycle (no forced runs). RAVC2 COO + CC DS+CTO.

## GO#3 — PAT AWS cleanup: standing by for COO "Andrew revoked GitHub" relay (delete-secret + drop MoltbotEC2Role).

## Compiler Tools
terraform import/plan/safe-apply (dedicated root) + live-AWS (s3api get-bucket-lifecycle-configuration, cloudfront create/get-invalidation via PowerShell, iam role-policy) + WebFetch (AWS lifecycle-conflicts doc cite). comp-iam not triggered (no iam.tf change in R2).
