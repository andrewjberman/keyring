# CVO Exercise-Cert — NFRA_INTEGRATIONS P3 (firm-sep enforcement): PASS — closes 3/3

**Date:** 2026-07-07T05:58Z
**Agent:** 3.0.0_SA_CVO
**Context:** P3 STORAGE schema CTO-arch-gate APPROVED (STANDARD.md sec9 v1.3, commit 4679bd61e). Since NO integration persists data today (YCharts read-only-passthrough; kuzu/nessie/iceberg read-only in-estate), the contract-BITE = firm-separation ENFORCEMENT (not a write/read round-trip). Two legs, both EXERCISED/applied-grounded (not config-read).
**Verdict:** PASS -> NFRA_INTEGRATIONS 3/3 (P1 done, P2 CERT-PASS 07-06, P3 now).

## LEG-1 (deploy-gate) -- EXERCISED live
Ran `safe_deploy_core.file_to_s3_target` (the deployed gate) with firm + adversarial inputs:
- black_diamond -> opal-data-bd | cot -> opal-data-cot | inf -> opal-data-inf  (each firm -> its OWN bucket ONLY)
- FOREIGN data/acme -> None | FOREIGN data/schwab -> None | bd-ALIAS typo data/bd/ (not the real 'black_diamond' key) -> None  (REJECTED-not-defaulted; an unrecognized/mistyped tree does NOT fall through to a firm bucket)
- PIPELINE_MAP buckets distinct (opal-data-{bd,inf,cot}); ZERO cross-firm route in any case
- structural no-override: signature = (rel_path) ONLY -> a caller CANNOT pass a bucket/firm arg to force a cross-firm target. Separation by-construction, not by-convention.
=> deploy-time firm-sep BITES.

## LEG-2 (runtime IAM Deny) -- Rule 22a DESIRED + APPLIED, no drift
- APPLIED (live `aws iam get-role-policy --role-name cot-gold-layer-ec2-role --policy-name cross-firm-bucket-deny`):
  Sid="DenyCrossFirmBuckets", Effect="Deny", Action="s3:*", Resource=[arn:aws:s3:::opal-data-bd, /*, arn:aws:s3:::opal-data-inf, /*].
- DESIRED (infra/aws/terraform/cot-pipeline/iam.tf:192-210): byte-for-byte identical (Sid/Effect/Action/all 4 ARNs).
- APPLIED == DESIRED -> the Deny is genuinely LANDED on the live role, NOT just TF-declared. NO drift.
- Deny-overrides-Allow (IAM semantic) => cot-gold-layer physically CANNOT touch opal-data-bd or opal-data-inf even under any future Allow-drift.
=> runtime firm-sep BITES.
- EXERCISED (behavioral) limb: available-but-not-required. CTO specified the applied-policy-check as the cert; the Deny-overrides-Allow guarantee is deterministic (an explicit s3:* Deny on those ARNs categorically blocks all S3 ops from the role). A stronger belt (assume-role -> HeadObject opal-data-bd -> expect AccessDenied) is offered if assume-role is feasible + wanted; per Rule 22a IAM-hard-withhold, DESIRED+APPLIED is the standard for a STATE/IAM claim.

## Verdict
NFRA_INTEGRATIONS P3 = PASS. Firm-separation enforced at BOTH deploy-time (file_to_s3_target, exercised) AND runtime (DenyCrossFirmBuckets, applied==desired, Deny-overrides-Allow). The persisted-data firm-sep invariant (STANDARD.md sec9.2) holds by-construction even though nothing persists today -- so it's future-proof for when an integration DOES persist. Closes NFRA_INTEGRATIONS 3/3. No drift finding. First NFRA+SCTY-DRIVE completion cert.
