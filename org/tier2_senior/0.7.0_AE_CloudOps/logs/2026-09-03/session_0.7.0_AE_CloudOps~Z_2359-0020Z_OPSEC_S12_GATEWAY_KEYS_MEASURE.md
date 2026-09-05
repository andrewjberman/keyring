# Session log -- 0.7.0_AE_CloudOps~Z -- 2026-09-03/04 2359-0020Z

**Archetype:** MEASURE + ENUMERATE, then a HELD build decision on internet-facing production
auth. **Scope:** NFRA_OPSEC202609 ONLY. **TO:** `NFRA_OPSEC202609.TO-OP-S-12` (FWD-12) --
deliverables 1-2 measured; the caller-enumeration gate closed; deliverable 3-4 (the expiry
cutover) surfaced to the issuer rather than executed, for the reason below.

## DISPATCH NOTE

TO-OP-S-10 is NOT mine (`issued_to 0.7.0_AE_CloudOps~V`) and its gate already fired (both JWT
consumers single-slot, Z-S100). I corrected my own earlier "S-10 next" misstatement to the COO.
TO-OP-S-12 is mine; the COO GO'd it directly (20042) despite its written "GO after S-10
terminal" dispatch line, which is a per-seat serialization clause moot now that S-10 left my
lane.

## S12-AC1 -- LOGGING HALF SERVED (verified, not rebuilt)

ALB `opal-gateway` access logs ON: `opal-data-security` / `waf-logs/alb-opal-gateway`,
`deletion_protection.enabled=false`. Delivered objects under the prefix on today's UTC
partition (00:05Z, 00:10Z), keys + LastModified read -- delivery, not just `get-attributes`
(C-15's lesson). OP-s-5 built this; this face verifies it. Claiming to build it would be an
explicit S12-AC1 FAIL.

## S12-AC2 -- THE SHARED MACHINE KEYS, CHARACTERISED WITH A DERIVED DENOMINATOR

**The credential each route accepts is a STATIC 32-byte capability bearer, constant-time
compared (`hmac.compare_digest`), with NO expiry claim.** Source-cited @97b8103069:
- `/otp/fetch` -> `otp.check_bearer` (otp.py:56-72) over `OTP_BEARER` (a whitespace list).
- `/ms/*` -> `ms_ingest.check_bearer` (ms_ingest.py:53-67) over `MS_INGEST_BEARER`.
- Both fed by the deploy (deploy-to-ec2.sh:129-142) from per-firm SM secrets.

**THE FACE'S FLOATED CANDIDATE IS THE WRONG CREDENTIAL.** `opal/mcp/opal-gateway-jwt`
(GATEWAY_JWT, deploy:115) is the RS256 signing key for the `/mcp` path (`_bearer_email` ->
`oauth_as.validate_access_token`, server.py:91-106) -- NOT what `/otp` or `/ms` accept. The
routes accept the static capability bearers. Confirmed as the face asked.

**THREE static secrets, no expiry, single-slot, never rotated** (`describe-secret`:
LastChanged == created, `RotationEnabled` null, one `AWSCURRENT` stage, no `DeletedDate`):
`blackdiamond/49f/otp-gateway-token`, `blackdiamond/cot/otp-gateway-token`,
`opal/mcp/ms-ingest-token`.

**CALLER DENOMINATOR = 5 holdings across 3 secrets, derived from the secret->caller wiring:**
| secret | callers |
|---|---|
| 49f/otp-gateway-token | bd-49f-auto-login box (`/otp/fetch`, secret-ids.env) + `opal-otp-liveness` Lambda (`/otp/health`, otp-liveness.tf:84) |
| cot/otp-gateway-token | bd-cot-auto-login box (`/otp/fetch`, secret-ids.env) |
| ms-ingest-token | globgrph NFRA_MSGRAPH nightly derive (`/ms/*`) + `opal-ms-ingest-liveness` Lambda (`/ms/health`, ms-ingest.tf:87) |

The liveness Lambdas were NEARLY missed -- the repo names (`m365-*`) 404 live; the deployed
names are `opal-otp-liveness` / `opal-ms-ingest-liveness`. Excluding them would have been the
exact "census excluded a named consumer" trap the issuer warned about.

**Wire refusal positive control:** `/otp/health`, `/otp/fetch`, `/ms/health` at
`https://mcp.opalinvest.dev` each return **401 `{"error":"unauthorized"}`** with no bearer.

## WHY DELIVERABLE 3-4 IS HELD, NOT EXECUTED, THIS SESSION

The expiry cutover is a live change on internet-facing production auth, and the face's own
`S12-AC4` gate binds: *every enumerated caller must be shown reaching the gateway successfully
AFTER the cutover, or the old credential STAYS live and this files UNCOMPUTABLE.* Of the 5
callers, only the 2 liveness Lambdas are on-demand verifiable (`lambda invoke`). **The two
auto-login boxes fire on real BD login events and the derive runs nightly -- none can be driven
on demand.** A same-session RETIREMENT of the static bearers would therefore retire a key on an
unverified caller list, which the face forbids in terms.

The honest path is the overlap the face mandates: deploy the new expiring credential accepted
ALONGSIDE the static bearers (nothing breaks), migrate each caller, and verify each via the
ALB access logs (which AC1 just confirmed are ON) as it fires over its natural cadence within
the overlap window -- a MULTI-SESSION shape, not a shortfall. The design, the per-caller
migration, and the overlap-window question are put to the issuer (message 000... to
2.0.0_SA_COO~Z) before any live gateway-auth deploy, because that deploy is outward-facing and
the retirement is structurally gated on caller verification.

## STATE AT CLOSE

Deliverables 1-2 measured; no write performed; no proof filed and face NOT flipped (the outcome
is not yet served). Surfaced to the issuer with the design and the AC4 verification constraint.
**PUSH STATE: LOCAL** (origin/SITEZ `001709c96e`). No commit this face yet -- measurement only.
