# OPLMCP AC6 -- Verified-Access JWT Signature-Verify Disposition (CTO, 2026-06-23)

**Owner:** 1.0.0_SA_CTO (PRD AC6). **Disposition: WAIVED for v1 macro-close, with rationale + a re-arm gate.**

## AC6 (PRD S8)
"Verified-Access JWT signature-verify TODO is either implemented or explicitly waived with rationale (no silent pre-prod gap shipped to prod)."

## Grounded state (SOURCE-CONFIRMED, app/identity.py)
- The LIVE identity path is `alb_oidc` (identity.py:50-69): it DOES verify the ES256 signature against the regional ELB public key. The browser/GUI auth path is signature-verified.
- The .06 Claude-Code path (Model-B) uses the gateway-ISSUED Bearer, fully validated (sig + iss + audience + exp + scope -- CTO condition-1, gated at the .06 build).
- The `_verified_access_identity` path (identity.py:83-100) carries `verify_signature=False` (the TODO) -- but it is NOT ACTIVE and NOT in any live path. AWS Verified Access is a FUTURE device-aware upgrade option (PRD S2.3), not deployed.

## Disposition: WAIVED for v1
There is NO silent pre-prod gap: the unverified code sits on an INACTIVE path; every LIVE auth path (alb_oidc ES256-verified; .06 gateway-Bearer fully-validated) verifies signatures. The AC6 concern -- an unverified token accepted in prod -- does not exist in the live system.

## Re-arm gate (the condition that UN-waives this)
IF/WHEN AWS Verified Access is deployed as a live identity path, `_verified_access_identity` MUST implement full JWT signature-verification (against the VA/OIDC signing keys) BEFORE it goes live -- this waiver does NOT authorize activating the unverified VA path. Recommended belt: a fail-closed startup guard so the gateway refuses to boot with an active VA provider while `verify_signature=False` (also closes the dev `header`-provider silent-activation risk -- CVO F2/F3). Folds into .04/.05 hardening.

-- 1.0.0_SA_CTO, 2026-06-23
