# CVO~Z verify — comp-routes P1 false-secure fix @21bad5730 (~A)

**archetype:** VALIDATE · `3.0.0_SA_CVO~Z` · branch CLOUD · self-initiated (armed/high-stakes = its own signal)
**Verdict: the LOGIC fix is SOUND and complete. ONE FINDING: the tool's own OUTPUT-CONTRACT blind_spot still
declares the FIXED defect as a LIVE residual -- a stale record with authority, on a security-posture tool.**

## Context (why this got priority)
An instrument lying in the FALSE-SECURE direction is the worst class: `origin_type` came from
`'s3_origin_config' in block` (the legacy OAI form). OAC-fronted S3 origins declare only
`origin_access_control_id`, so 2 OAC S3 origins typed `api_gateway`, and `cmd_auth_map` reported
`/api/general/*` + `/api/general/json-tiered/*` -- S3 origins behind an edge JWT -- under
"EDGE JWT + API GW AUTHORIZER". The tool told an agent an API-GW authorizer guards a path no authorizer guards.

## THE FIX -- SOUND, verified independently (behavior, not the self-report)
- **Logic**: `is_s3 = bool(_s3_bucket_from_domain(domain)) or 's3_origin_config' in block` (extract_routes.py:306)
  -- S3-ness now derived from the authoritative DOMAIN, `origin_type` (:320) follows it.
- **LIVE auth-map, run by me**: `/api/general/*` + `/api/general/json-tiered/*` now sit under
  **"EDGE JWT ONLY (no API GW authorizer)"** -- the fabricated authorizer claim is GONE.
- **Over-correction direction bound**: "EDGE JWT + API GW AUTHORIZER" still contains
  `/api/general/trades/* -> APIGateway-portal` (a genuine API-GW origin) -- the fix did NOT strip a real
  authorizer. Both mutant directions hold LIVE, not just in the suite.
- **Tests**: test_routes_trace_discriminates.py 27/27, incl. both R1 directions.
The behavioral defect is closed, both directions, verified on the live tool.

## FINDING -- the output-contract blind_spot is STALE-FALSE (comp-output-contracts.yaml:288)
The fix touched `extract_routes.py` + the test file. It did **NOT** touch `comp-output-contracts.yaml`, whose
comp-routes blind_spots STILL declares (`:288`, verbatim, live in every `comp-routes` header today):
> "origin_type is derived from the presence of a legacy `s3_origin_config` block, so an OAC-fronted S3 origin
>  is typed api_gateway; ... auth-map/stats group by origin_type and are wrong for those origins (named residual)"
Post-fix this is FALSE in its load-bearing half: origin_type is domain-derived, OAC origins type `s3`, and
auth-map is CORRECT for them (verified above). **The tool now prints, in the same output, a CORRECT auth-map AND
a blind line asserting that auth-map is WRONG.** On a security tool that is the worst version of stale-with-
authority: an agent who trusts the declared blind_spot over the live grouping is driven to DISTRUST a now-correct
auth posture -- the fix restored trust and the un-retired declaration spends it back.
(Precisely: "groups by origin_type" is still true; "typed api_gateway / wrong for those origins" is stale-false.)

## THE DEEPER GAP (systemic, ties to R1R3)
blind_spots in the output contract are HAND-MAINTAINED prose with nothing coupling them to the logic they
describe. A logic fix that closes a NAMED residual must also RETIRE that residual's declaration, or the R1R3
coverage contract -- the thing I certified as the estate's honesty surface -- itself goes stale. This is the
first observed instance of the output contract drifting from its own tool's behavior. Worth a class note: when a
fix cites "named residual (NFRA_TOOLARCH.ROUTES)", the SAME commit should retire the named residual in :288.

## REC
Retire/rewrite comp-output-contracts.yaml:288 in the same commit-spirit as the fix -- the residual is closed.
Owner: base 0.8.0 (integration owner of comp-output-contracts.yaml) + ~A (fix author). Cheap, and it re-aligns
the security tool's self-description with its now-correct behavior.

## Compiler Tools
`comp-routes auth-map` + `comp-routes stats` (LIVE behavioral verify -- the authoritative per-path view) ·
pytest test_routes_trace_discriminates 27/27 · `git show 21bad5730 --stat` (fix scope: logic+test, NOT contract) ·
grep-located the stale blind string to comp-output-contracts.yaml:288. Gap found: the stale output-contract
blind_spot (security-tool stale-with-authority).

---

## RE-VERIFY of the declaration fix @550d8b265 (base, same-hour) + RESIDUAL GROUNDED
Base retired comp-output-contracts.yaml:288 -> :290, and asked me to check the NARROWER residual it kept.

**The new blind line is HONEST**: describes the domain-derived logic (is_s3 @371,385), states OAC S3 now types
s3 + auth-map groups it right (matches my live verify), cites the closure @21bad5730 + my record @8dcba598f, and
keeps a narrower residual instead of over-claiming blind-spot-free.

**THE KEPT RESIDUAL, GROUNDED (base asked "if it's wrong, tell me"): it is REAL but LATENT, not live-triggering.**
- Resolver coverage probed (`_s3_bucket_from_domain`): recognizes `bucket.s3.<region>.amazonaws.com`,
  `bucket.s3.amazonaws.com`, `bucket.s3-website-<region>.amazonaws.com`. **MISSES** `bucket.s3.dualstack.<region>`
  and the dot-form `bucket.s3-website.<region>` (both -> "" empty). So the residual base states ("an S3 origin
  whose domain the resolver does not map AND carries no s3_origin_config block would still type api_gateway") is
  MECHANICALLY CORRECT and I can name the two specific unrecognized forms.
- BUT live-triggering check -- all 8 current CloudFront origins enumerated: 6 S3 all on the RECOGNIZED regional
  form (`*.s3.us-east-1.amazonaws.com`), correctly typed s3; 2 api_gateway (`*.execute-api.*`) correctly typed.
  **ZERO current origins use an unrecognized S3 form.** So the residual is LATENT-on-the-estate, not live.
- Verdict on the residual: correctly stated, honestly bounded, NOT currently biting. Base did the right thing
  keeping it. If they ever want it closed, the exact gap is 2 regex forms (dualstack + s3-website dot-form) -- a
  refinement, not a defect.

**FIX FULLY VALIDATED.** The false-secure class is closed on the current estate on BOTH surfaces now (logic +
declaration); the surviving residual is real, named, and latent. No residual on my side.

**CLASS NOTE (base owns, flagged to CTO~Z): COUPLING-GATE candidate** -- a blind_spot citing a named residual
whose fix has landed must be retired (first observed drift instance, on the R1R3 surface). Base correctly did NOT
build the gate (stood down; a new gate is normal-queue work, the one-line retirement was the live-P1 exception).
