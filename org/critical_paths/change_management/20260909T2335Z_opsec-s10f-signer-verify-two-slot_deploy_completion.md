# Deploy Completion Record
**Date opened:** 2026-09-09T23:35:53.518031+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260909T235021Z
**Deploy:** NFRA_OPSEC202609.TO-OP-S-10F: the SIGNER's PUBLIC read gains two slots; its PRIVATE read stays single-CURRENT. opalinvest-auth-handler is ALSO a verifier -- verifyAccessToken and verifyRefreshToken both read the public key, /auth/refresh is live, and refresh tokens live 7 DAYS, so a single-key read there turns the rotation into a week-long sign-out of every returning user (row Z-S160). PRE-CHANGE BASELINE: CodeSha256 ZrHoxMzn0YsK5oA1lq0OMcsoaL9xzN3RkYFxY9Opjyk=, LastModified 2026-09-09T22:38:20Z. ROLLBACK = git restore src/jwt.ts, rebuild, re-apply the same single -target. NOTHING IS ROTATED
**Authored by:** 0.7.0_AE_CloudOps~V
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | the PAIRED change committed: the public read moves to getJwtKeySlots + verifyWithSlots, the private read is UNTOUCHED at single-CURRENT. Either half alone is the defect -- a two-slot private read is what S10E correctly barred, a single-key public read is what this face fixes | the diff plus a per-READ census showing which call sites sign and which verify | THE PAIRED CHANGE, ONE FILE, AND THE PER-READ CENSUS THAT JUSTIFIES ITS SHAPE. src/jwt.ts only: 43 insertions / 14 deletions.

THE PHASE-1 MANDATE WAS RUN AS AN ENUMERATION, per READ rather than per component, which is the obligation the new face installs. Every call site of a key value in this function:

  jwt.ts:144  getJwtPrivateKey  in getMfaCodeSealKey     -> HKDF input (neither signs nor verifies)
  jwt.ts:162  getJwtPrivateKey  in generateAccessToken   -> SIGNS
  jwt.ts:229  getJwtPrivateKey  in generateRefreshToken  -> SIGNS
  jwt.ts:251  public read       in verifyAccessToken     -> VERIFIES
  jwt.ts:268  public read       in verifyRefreshToken    -> VERIFIES
  mfa.ts:223  getMfaCodeSealKey in sealCode              -> encrypts
  mfa.ts:243  getMfaCodeSealKey in unsealCode            -> decrypts

ALL THREE PRIVATE READS ARE NON-VERIFYING, so single-CURRENT is correct for every one of them and stays untouched. BOTH PUBLIC READS VERIFY, so both need two slots. The census found no further role, which is the point of running it rather than reasoning about the component.

THE CHANGE: getJwtPublicKey (single-CURRENT) is REPLACED by getJwtVerifySlots, which returns getJwtKeySlots() -- the same shared module and the same idiom the other three verifiers carry. verifyAccessToken and verifyRefreshToken now call verifyWithSlots(jwt, token, slots, opts) instead of jwt.verify(token, publicKey, opts). getJwtPrivateKey is BYTE-UNCHANGED and still returns getCurrentKey(JWT_PRIVATE_KEY_SECRET_ID).

RESIDUAL CENSUS: getJwtPublicKey reads 0 -- fully gone. getCurrentKey survives with exactly its three private call sites. The now-orphaned local JWT_PUBLIC_KEY_SECRET_ID constant was REMOVED rather than left dangling, with a note saying why: the shared module owns that id (it is the same secret the other three verifiers read), so a local copy would be a second declaration free to drift from the one that does the reading. The PRIVATE id stays local because getCurrentKey is generic over the secret and the caller names it.

THE COMMENT THAT WAS WRONG IS KEPT AND CORRECTED IN PLACE rather than deleted. The old docstring read "It stays SINGLE-KEY deliberately -- this function is the signer ... widening the accept path here is not this face's job." Every clause of that is about THE COMPONENT and none is about THE READ, which is exactly how the defect entered. The replacement says so, so the next reader meets the error and its cause at the file. | CLOSED 20260909T235020Z |
| L2 | activation | build via build-nodejs-lambda.sh and deploy through TERRAFORM ONLY; auth_handler resolves its hash through a data lookup so the upload alone should move the plan -- verify that rather than assume it | safe-apply output + the live CodeSha256 equal to the independently recomputed artifact sha | BUILT AND DEPLOYED THROUGH TERRAFORM ONLY. Build: build-nodejs-lambda.sh portal-auth opalinvest-auth-handler, zip sha sJyR6xk2CIZDJIFQBqVqqfTMOtQ4v1asHfin4/GjXuw=, uploaded as VersionId tDmDpVsQDJ03avoF5u7i6C0PSj3LyNTH. INDEPENDENTLY VERIFIED BEFORE THE APPLY: the object was downloaded and its sha RECOMPUTED locally to the same value, equal also to the S3 metadata content-sha256.

THE DATA-LOOKUP PATTERN WAS RE-VERIFIED RATHER THAN ASSUMED from yesterday's reading. auth_handler resolves both s3_object_version and source_code_hash through data.aws_s3_object.auth_handler_artifact, so the upload alone SHOULD move the plan -- unlike session-analytics, which hardcodes the hash and plans as "No changes" until the line is edited. It did move: this was read off the plan, not inferred from the resource shape.

PLAN MEASURED: "Plan: 0 to add, 1 to change, 0 to destroy", 0 forces-replacement, 0 wafv2 resources, and the change set is exactly THREE attributes -- last_modified to (known after apply); s3_object_version EGaYFb8t6aCbIi2FAhfF0YtzM_cqIMiW to tDmDpVsQDJ03avoF5u7i6C0PSj3LyNTH; source_code_hash ZrHoxMzn0YsK5oA1lq0OMcsoaL9xzN3RkYFxY9Opjyk= to sJyR6xk2CIZDJIFQBqVqqfTMOtQ4v1asHfin4/GjXuw=.

APPLY: HALT_ACK=1 safe-apply on the SAVED plan. rc captured before any pipe = 0. "Apply complete! Resources: 0 added, 1 changed, 0 destroyed", modifications complete after 6s. EQUALITY TEST AGAINST A PREDICTED VALUE: live CodeSha256 reads sJyR6xk2CIZDJIFQBqVqqfTMOtQ4v1asHfin4/GjXuw=, equal to the prediction and different from the baseline; State Active, LastUpdateStatus Successful, LastModified 2026-09-09T23:39:18Z. The function's own deploy.sh path was not used. | CLOSED 20260909T235020Z |
| L3 | verify | S10F-AC2 GRADED AS ONE PAIRED CRITERION on the DEPLOYED bytes: verifyWithSlots present AND reachable from both verify functions, AND the private read still selecting one CURRENT key | both halves quoted from the post-deploy artifact | S10F-AC2 GRADED AS ONE PAIRED CRITERION ON THE DEPLOYED BYTES. Both halves quoted; either alone would be a FAIL.

HALF A -- THE PUBLIC READ REACHES A TWO-SLOT ACCEPT PATH, AND IT IS REACHABLE FROM BOTH VERIFY FUNCTIONS:

  function E8(q,$,Z,Q){ try{ return q.verify($,Z.current,Q) }
    catch(z){ if(!Z.previous\|\|z.name==="TokenExpiredError") throw z;
              try{ return q.verify($,Z.previous,Q) } catch(J){ throw z } } }        <- verifyWithSlots

  async function A6(q){ let $=await lZ(); return E8(cq.default,q,$,{algorithms:["RS256"],issuer:pZ,audience:cZ}) }
  async function nZ(q){ let $=await lZ(), Z=E8(cq.default,q,$,{algorithms:["RS256"]});
                        if(Z.type!=="refresh") throw Error("Invalid token type"); return Z }

A6 is verifyAccessToken (it carries issuer and audience) and nZ is verifyRefreshToken (it carries the type!=="refresh" guard). BOTH obtain slots from lZ (getJwtVerifySlots) and BOTH call E8. Reachability is shown by the call sites, not asserted.

HALF B -- THE PRIVATE READ STILL SELECTS ONE CURRENT KEY:

  async function k8(){ return await mZ(B3) }          B3 = "opal/auth/jwt-private-key"
  ...{current:J}=uZ(z.SecretString); return bZ.set(q,{value:J,atMs:$}),J     <- getCurrentKey, CURRENT only
  async function iZ(q){ let $=await k8(); ... cq.default.sign(Z,$,{algorithm:"RS256",expiresIn:O3}) }   <- SIGNS with k8

So signing resolves through k8 (one CURRENT key) and verifying through lZ (two slots). That is exactly the pairing, and it is the distinction whose half-application created this face.

A CORRECTION ON MY OWN INSTRUMENT, RECORDED BECAUSE IT NEARLY PRODUCED A FALSE FAIL. My first probe searched the deployed bundle with a regex built on an ASSUMED minified shape and reported "verifyWithSlots in the bundle: False" -- which, taken at face value, would have said this deploy failed. The regex was wrong, not the artifact. Re-run against LITERAL markers instead of guessed structure, the picture is unambiguous: the parseKeySlots literals each appear once, TokenExpiredError appears 3 times, and every one of the 7 ".previous" occurrences was enumerated with context -- 1-3 inside parseKeySlots's return shape, 4-5 inside E8 itself, 6-7 inside the ORIGIN secret's pre-existing overlap. A MATCHER BUILT AGAINST A FORMAT ONE HAS NOT READ RETURNS A CLEAN ZERO, and on a minified bundle the format is never the one in your head.

THE ORIGIN-VERIFY CACHE IS UNTOUCHED, as in the previous face: occurrences 6-7 are its two-slot check, unchanged. | CLOSED 20260909T235020Z |
| L4 | verify | /auth/refresh EXERCISED, not merely unbroken -- it is the surface this face is about. Plus login, the invocation count, and whether a cold start on the new bundle occurred | the probes + log read + CloudWatch counts | /auth/refresh EXERCISED, NOT MERELY UNBROKEN -- and the first attempt to exercise it FAILED TO REACH THE PATH, which is why the discriminator matters.

THE FIRST PROBE PUT THE TOKEN IN THE JSON BODY and got {"error":"No refresh token"} -- byte-identical to the no-token answer. Two arms returning the SAME string is not evidence of anything, and reading that as "the path was exercised" would have been a false pass. Cause, read at source: index.ts:88 extractRefreshToken pulls the token from a COOKIE named refresh_token, never from the body.

RE-PROBED THROUGH THE COOKIE, three arms with a working discriminator:
  no cookie                     -> {"error":"No refresh token"}     guard, path NOT reached
  refresh_token=<bogus JWT>     -> {"error":"Internal server error"} path REACHED
  refresh_token=not-a-jwt       -> {"error":"Internal server error"} path REACHED
The two reached arms differ from the guard arm, which is what makes "reached" a measurement.

THE LOG SAYS WHAT HAPPENED INSIDE, and it is the accept path behaving correctly:
  ERROR Error: W6 [JsonWebTokenError]: invalid signature      <- the bogus JWT
  ERROR Error: W6 [JsonWebTokenError]: jwt malformed          <- the not-a-jwt value
The first is verifyWithSlots trying `current`, failing, finding `previous` null (the secret is still a bare PEM), and RETHROWING the current-key error -- exactly as designed.

THE 500 IS PRE-EXISTING ROUTE BEHAVIOUR AND NOT A REGRESSION I INTRODUCED, checked rather than assumed. index.ts:233-241 handles POST /auth/refresh with no specific catch around `await refresh(refreshToken)`, so ANY verify throw has always surfaced through the outer handler as a 500. I did not touch index.ts. AND THE BEHAVIOUR IS BYTE-EQUIVALENT WHILE previous IS NULL: before, jwt.verify threw JsonWebTokenError directly; now verifyWithSlots catches it, sees previous is null, and rethrows THE SAME ERROR OBJECT. With no previous slot the new path is observably identical to the old one, which is the safest possible shape to deploy ahead of a rotation.

LOGIN STILL WORKS, exercising the SIGNING path that must NOT have changed: a real committed credential returns 200 with mfaRequired true and a challengeId, which can only be produced by running sealCode -> getMfaCodeSealKey -> getJwtPrivateKey.

THE COUNTS, so silence from a dead function cannot pass as health: 32 log events over a complete window (nextToken ABSENT), 7 Invocations, 0 on the CloudWatch Errors metric, and 1 INIT_START -- a cold start on the new bundle, where a MODULE_NOT_FOUND on the changed import would have fired. NOTE THE DISCRIMINATOR ON THAT ZERO: Errors reads 0 even though two probes received a 500, because the outer handler RETURNS a 500 payload rather than failing the invocation. A handled 500 and a Lambda failure are different objects and the metric separates them. | CLOSED 20260909T235020Z |
| L5 | verify | NOTHING ROTATED on either secret, and the WAF ride measured absent from the plan | describe-secret on both + the plan's wafv2 count | NOTHING ROTATED ON EITHER SECRET, AND THE WAF RIDE MEASURED ABSENT.

Re-measured after the apply and identical to the session-start baseline. opal/auth/jwt-private-key: 1 version, LastChangedDate 2026-04-06T13:31:00.251000-04:00, RotationEnabled unset, no DeletedDate. opal/auth/jwt-public-key: 1 version, LastChangedDate 2026-04-06T13:31:00.259000-04:00, RotationEnabled unset, no DeletedDate. No keypair minted, no PutSecretValue, no signing switch. Both timestamps carry their true -04:00 offset rather than a typed Z.

THE PUBLIC SECRET IS STILL A BARE PEM -- measured, 450 bytes, one BEGIN block, does not start with "{". That is what makes S10F-AC3's two-KEY limb uncomputable here: there is no previous slot to accept from until the rotation writes the envelope.

WAFV2 RESOURCES IN THE PLAN: 0. Z-S156's ride is a property of the DISTRIBUTION's dependency on the web ACL and this target is a Lambda function, so it should not apply -- but the criterion asks for a measurement and "should not" is an inference, so the plan text was searched. 0 to add, 1 to change, 0 to destroy, 0 forces-replacement. | CLOSED 20260909T235020Z |

## Log

- 20260909T233553Z OPENED by 0.7.0_AE_CloudOps~V with 5 leg(s)
- 20260909T235020Z LEG L1 closed: THE PAIRED CHANGE, ONE FILE, AND THE PER-READ CENSUS THAT JUSTIFIES ITS SHAPE. src/jwt.ts only: 43 insertions / 14 delet
- 20260909T235020Z LEG L2 closed: BUILT AND DEPLOYED THROUGH TERRAFORM ONLY. Build: build-nodejs-lambda.sh portal-auth opalinvest-auth-handler, zip sha sJ
- 20260909T235020Z LEG L3 closed: S10F-AC2 GRADED AS ONE PAIRED CRITERION ON THE DEPLOYED BYTES. Both halves quoted; either alone would be a FAIL.

HALF A
- 20260909T235020Z LEG L4 closed: /auth/refresh EXERCISED, NOT MERELY UNBROKEN -- and the first attempt to exercise it FAILED TO REACH THE PATH, which is 
- 20260909T235020Z LEG L5 closed: NOTHING ROTATED ON EITHER SECRET, AND THE WAF RIDE MEASURED ABSENT.

Re-measured after the apply and identical to the se
- 20260909T235021Z CLOSED -- all 5 legs proven
