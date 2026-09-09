# Deploy Completion Record
**Date opened:** 2026-09-09T22:30:42.202311+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260909T224552Z
**Deploy:** NFRA_OPSEC202609.TO-OP-S-10E: bound the SIGNER's two JWT key reads. opalinvest-auth-handler cached BOTH the private signing key and the public key in bare scalars with NO time component on its deployed bytes (row Z-S159), so a signing switch could never converge and S10-AC4 was unsatisfiable at any wait length. A BOUNDED TTL, explicitly NOT two slots -- a signer must know which key is CURRENT. PRE-CHANGE BASELINE re-read at this face's vintage: CodeSha256 X8YBkwUqnuTDLW7XvqovWT9+TujBXbTaXQaEdwHxwZc=, LastModified 2026-09-04T02:14:11Z, State Active. ROLLBACK = git restore src/jwt.ts and the shared module, rebuild, re-apply the same single -target. NOTHING IS ROTATED and no secret is written
**Authored by:** 0.7.0_AE_CloudOps~V
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | the shared module gains a bounded SINGLE-CURRENT read and the signer's two reads are wired to it, committed together. The signer must still select ONE key -- a two-slot accept path here is a FAIL, not a bonus | the diff plus a residual-symbol census, and the returned type shown to be a string rather than a slot pair | THE SHARED MODULE GAINS A BOUNDED SINGLE-CURRENT READ AND THE SIGNER'S TWO READS ARE WIRED TO IT. Diff: 2 files, 121 insertions / 34 deletions -- infra/aws/lambda/lib/authkeys/jwtPublicKeys.mjs (the new getCurrentKey plus a per-secret-id Map cache and its reset seam) and infra/aws/opalinvest_dev/lambda/auth-handler/src/jwt.ts (both key functions reduced to a call into it; the local SecretsManagerClient, GetSecretValueCommand import and both scalar caches deleted).

ONE KEY, NEVER TWO, AND THAT IS THE POINT OF THE SHAPE. getCurrentKey returns a STRING, not a slot pair: it destructures the current slot out of parseKeySlots and discards previous, so there is no fallback path here and there must never be one. A verifier accepts current-or-previous; a SIGNER must know which key is CURRENT, and a second slot would let it sign under a retired key (issuer's re-cut @dd39dab70e). It reuses parseKeySlots deliberately so the signer survives the shape change the rotation itself introduces -- the secret is a bare PEM today and becomes a current/previous envelope when the rotation writes it, and reading current is correct in both.

KEYED PER SECRET ID because this consumer reads TWO secrets through one function. A single shared scalar would hand the private key back for a public-key read -- the defect being fixed, wearing a different mask.

RESIDUAL-SYMBOL CENSUS on jwt.ts: secretsClient 0, GetSecretValueCommand 0, SecretsManagerClient 0, cachedPublicKey 0. cachedPrivateKey reads 2 and BOTH are inside the new docstring quoting the retired line -- distinguished rather than counted, because a census that cannot tell a comment from a call site is not a control. originVerify.ts keeps its OWN separate SecretsManagerClient and is untouched, which is what makes it available as this face's negative control.

EXERCISED LOCALLY BEFORE THE DEPLOY, 9 of 9, with the AWS SDK stubbed but the REAL parseKeySlots running: bare PEM returns the key; the return is a string not a slot pair; a cache HIT inside the window issues no second fetch; the cache EXPIRES at the TTL and re-reads; a CHANGED value is picked up after expiry (the rotation property this face exists to install); the private read returns the PRIVATE key rather than the public one; an envelope returns CURRENT; THE SIGNER NEVER RECEIVES previous; and an empty secret THROWS rather than returning blank.

AND THE CONTROL CAN FAIL. A mutant was planted handing the signer previous instead of current -- the exact defect S10E-AC2 calls a FAIL rather than a bonus. Result: 3 passed, 6 FAILED, rc=1, and the failing set includes "THE SIGNER NEVER RECEIVES previous". Restored: 9 of 9, rc=0. node --check passes on the shared module. | CLOSED 20260909T224551Z |
| L2 | activation | build via build-nodejs-lambda.sh and deploy through TERRAFORM ONLY. auth_handler resolves its hash through a data aws_s3_object lookup rather than a hardcoded string, so unlike session-analytics the upload alone SHOULD move the plan -- verify that rather than assume it | safe-apply output + the new live CodeSha256 equal to the independently recomputed artifact sha | BUILT AND DEPLOYED THROUGH TERRAFORM ONLY. Build: build-nodejs-lambda.sh portal-auth opalinvest-auth-handler, zip sha ZrHoxMzn0YsK5oA1lq0OMcsoaL9xzN3RkYFxY9Opjyk=, uploaded as VersionId EGaYFb8t6aCbIi2FAhfF0YtzM_cqIMiW. INDEPENDENTLY VERIFIED BEFORE THE APPLY: the object was downloaded and its sha RECOMPUTED locally to the same value, equal also to the S3 metadata content-sha256.

THE TRAP THAT DID NOT APPLY HERE, CHECKED RATHER THAN ASSUMED. session-analytics hardcodes source_code_hash, so an upload alone plans as "No changes" and updating the line IS the deploy. auth_handler is the OTHER pattern: it resolves BOTH s3_object_version and source_code_hash through data.aws_s3_object.auth_handler_artifact, so the upload alone SHOULD move the plan. It did, and that was verified by reading the plan rather than inferring it from the resource shape.

PLAN MEASURED: "Plan: 0 to add, 1 to change, 0 to destroy", 0 forces-replacement, and the change set is exactly THREE attributes -- last_modified to (known after apply), s3_object_version gHtYwhDqSYN4xFto8w7OzAEQWu25fkpF to EGaYFb8t6aCbIi2FAhfF0YtzM_cqIMiW, and source_code_hash X8YBkwUqnuTDLW7XvqovWT9+TujBXbTaXQaEdwHxwZc= to ZrHoxMzn0YsK5oA1lq0OMcsoaL9xzN3RkYFxY9Opjyk=.

APPLY: HALT_ACK=1 safe-apply on the SAVED plan, so what shipped is exactly what was read. rc captured before any pipe = 0. "Apply complete! Resources: 0 added, 1 changed, 0 destroyed", modifications complete after 6s. DEPLOYED STATE: live CodeSha256 ZrHoxMzn0YsK5oA1lq0OMcsoaL9xzN3RkYFxY9Opjyk=, EQUAL to the independently recomputed artifact and DIFFERENT from the baseline; State Active, LastUpdateStatus Successful, LastModified 2026-09-09T22:38:20Z. The function's own deploy.sh path was not used. | CLOSED 20260909T224551Z |
| L3 | verify | BOTH JWT reads carry a bounded time component in the DEPLOYED bytes and each still selects ONE key, quoted; AND the negative control -- the origin-verify bounded cache UNCHANGED, with the JWT TTL constant distinguished from its 300000 so no reader repeats the Z-S159 conflation | both regions quoted from the post-deploy artifact, plus the origin region quoted before and after | BOTH JWT READS ARE BOUNDED AND EACH STILL SELECTS ONE KEY, QUOTED FROM THE DEPLOYED BYTES.

  async function T8(q,{now:$=Date.now(),region:Z="us-east-1"}={}){
    if(!q\|\|typeof q!=="string")throw Error("getCurrentKey requires a secret id");
    let Q=yZ.get(q); if(Q&&$-Q.atMs<F3) return Q.value;          <- BOUNDED, per secret id
    if(!S8)S8=new X3({region:Z});
    let z=await S8.send(new H3({SecretId:q})),{current:J}=Y3(z.SecretString);   <- CURRENT ONLY
    return yZ.set(q,{value:J,atMs:$}),J }                        <- returns a STRING

BEFORE, on the baseline bytes: async function E8(){ if(pq) return pq; ... } and async function hZ(){ if(cq) return cq; ... } -- two bare scalars, neither with a time component. AFTER: both call sites resolve through T8 with the two secret ids present as x3="opal/auth/jwt-private-key" and U3="opal/auth/jwt-public-key".

NO TWO-SLOT ACCEPT PATH ON THE SIGNER, and this was checked properly rather than asserted because "previous" DOES appear in the bundle and a careless read would call that a FAIL. Every occurrence was enumerated with context: hits 1-5 are all inside parseKeySlots (Y3), which RETURNS a {current, previous} shape -- a parse artifact, and T8 destructures {current:J} and discards the other half. Hits 6-7 are inside isOriginVerified (f1) and belong to the ORIGIN secret's two-slot overlap, which is TO-OP-S-3's, correct, and pre-existing. THE DECISIVE TEST: verifyWithSlots is NOT bundled at all (present: False). There is no fallback on any JWT key.

NEGATIVE CONTROL -- THE ORIGIN-VERIFY CACHE IS UNCHANGED: Z2="opal/auth/origin-verify", Q2="x-opal-origin-verify", g6=null, v1=0, z2=300000; async function J2(){ let q=Date.now(); if(g6&&q-v1<z2) return g6; ... } -- guard and window both still present and still 300000, identical in shape to the baseline.

HOW THE NEW TTL IS DISTINGUISHED FROM IT, so no later reader repeats the Z-S159 conflation: the count of 300000 in the bundle moved from 1 to 2. The ORIGIN one is z2, declared inline beside "opal/auth/origin-verify" and read only by J2. The JWT one is F3, the shared module's exported JWT_KEY_TTL_MS, read only by T8 and adjacent to the two JWT secret ids. Distinct variables, distinct adjacency, distinct readers -- so the discriminator is structural rather than a value difference. The two windows are the same NUMBER deliberately (one convergence window for a runbook to reason about), and that is exactly why the number alone can never tell them apart. | CLOSED 20260909T224551Z |
| L4 | verify | LOGIN STILL WORKS: no new error class, the invocation count stated over the window so a dead function cannot pass as healthy, and whether a cold start on the new bundle was observed | log read + CloudWatch Invocations and Errors over the same window | LOGIN STILL WORKS, AND THE CHANGED CODE PATH WAS EXERCISED END TO END RATHER THAN MERELY LEFT UNBROKEN.

ARM 1, the refusal: POST https://opalinvest.dev/auth/login with bad credentials returns 401, so the handler is alive and refusing.

ARM 2, AND THIS IS THE LOAD-BEARING ONE: a REAL committed credential returns 200 with mfaRequired true, channel email and a challengeId. That response can only be produced by running sealCode, which calls getMfaCodeSealKey, which calls getJwtPrivateKey -- THE EXACT READ THIS FACE REPLACED. So the new bounded read executed successfully on a real request against the live login path, and a broken key read would have surfaced as a 500 rather than a challenge.

THE LOG, over a complete window (nextToken ABSENT): 29 events in 20 minutes. TWO INIT_START events -- two COLD STARTS on the NEW bundle, which is precisely where a MODULE_NOT_FOUND on the new cross-tree relative import would fire. It did not.

THE ONE ERROR-CLASS LINE IS MINE AND IS THE EXPECTED REFUSAL, stated rather than reported as a defect: "ERROR Error: Invalid email or password" at 22:40:33Z is arm 1's own bad-credentials probe working correctly. THE DISCRIMINATOR THAT SETTLES IT: the CloudWatch Errors metric reads 0 over the same window, so that line is a HANDLED application-level refusal and not a Lambda invocation error. No new error class attributable to the key read.

THE COUNT, stated because silence is what a dead function returns: 6 Invocations over the window against 0 Errors. This is a login endpoint rather than a high-traffic API, so the absolute number is small by nature -- what matters is that it is NON-ZERO and includes the two probes plus a real credential login, so the zero-error reading is a live function's and not an unread instrument's. | CLOSED 20260909T224551Z |
| L5 | verify | NOTHING ROTATED: describe-secret on both JWT secrets unchanged; and Z-S156's WAF ride MEASURED ABSENT by reading the plan rather than assumed absent because this is not Lambda@Edge | describe-secret output + the plan's wafv2 count | NOTHING ROTATED, AND Z-S156's WAF RIDE MEASURED ABSENT RATHER THAN ASSUMED.

NOTHING ROTATED, re-measured after the apply and identical to the baseline this session captured at 18:3xZ before any deploy. opal/auth/jwt-private-key: 1 version, LastChangedDate 2026-04-06T13:31:00.251000-04:00, RotationEnabled unset, no DeletedDate. opal/auth/jwt-public-key: 1 version, LastChangedDate 2026-04-06T13:31:00.259000-04:00, RotationEnabled unset, no DeletedDate. No keypair minted, no PutSecretValue, no signing switch. This face teaches the signer WHEN to re-read; it never changes WHAT it reads. Both timestamps carry their true -04:00 offset and not a typed Z, per the trap bd6e7cb8c7 corrected on this project.

THE WAF RIDE IS ABSENT AND THAT WAS MEASURED. Row Z-S156 established that repointing CloudFront pulls the WAF chain into the plan because the distribution depends on the web ACL. This target is a LAMBDA FUNCTION, not the distribution, so the ride should not apply -- but "should not" is an inference and the criterion asks for a measurement. The plan was searched: wafv2 resources appear 0 times. "Plan: 0 to add, 1 to change, 0 to destroy", 0 forces-replacement. A non-zero count would have been a STOP; it is zero, read rather than assumed. | CLOSED 20260909T224552Z |

## Log

- 20260909T223042Z OPENED by 0.7.0_AE_CloudOps~V with 5 leg(s)
- 20260909T224551Z LEG L1 closed: THE SHARED MODULE GAINS A BOUNDED SINGLE-CURRENT READ AND THE SIGNER'S TWO READS ARE WIRED TO IT. Diff: 2 files, 121 ins
- 20260909T224551Z LEG L2 closed: BUILT AND DEPLOYED THROUGH TERRAFORM ONLY. Build: build-nodejs-lambda.sh portal-auth opalinvest-auth-handler, zip sha Zr
- 20260909T224551Z LEG L3 closed: BOTH JWT READS ARE BOUNDED AND EACH STILL SELECTS ONE KEY, QUOTED FROM THE DEPLOYED BYTES.

  async function T8(q,{now:$
- 20260909T224551Z LEG L4 closed: LOGIN STILL WORKS, AND THE CHANGED CODE PATH WAS EXERCISED END TO END RATHER THAN MERELY LEFT UNBROKEN.

ARM 1, the refu
- 20260909T224552Z LEG L5 closed: NOTHING ROTATED, AND Z-S156's WAF RIDE MEASURED ABSENT RATHER THAN ASSUMED.

NOTHING ROTATED, re-measured after the appl
- 20260909T224552Z CLOSED -- all 5 legs proven
