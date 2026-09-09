# Deploy Completion Record
**Date opened:** 2026-09-09T21:19:03.474108+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260909T213734Z
**Deploy:** NFRA_OPSEC202609.TO-OP-S-10D: teach the THIRD verifier two slots. opal-session-analytics reads opal/auth/jwt-public-key into ONE scalar with NO time component on its DEPLOYED bytes at 52,540 invocations in 7 days, and is the last thing standing between this project and FWD-10's rotation. PRE-CHANGE BASELINE re-read at this face's own vintage: CodeSha256 TW+G6NyLoKxqCdp6CtfU5WAixRf8phcP69Kxg6kx8EU=, LastModified 2026-09-04T05:44:08Z, State Active. ROLLBACK = git restore src/auth.ts, rebuild via build-nodejs-lambda.sh, re-apply the same single -target; the pre-change artifact sha is recorded here and the old bytes remain reproducible from 9e2818276c^. NOTHING IS ROTATED and no secret is written
**Authored by:** 0.7.0_AE_CloudOps~V
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | the import swap in src/auth.ts committed -- the shared module REUSED, not a third cache hand-rolled beside it. The error-classification catch must be byte-unchanged, because that is what callers see | the diff, with the catch/return shape shown unchanged and a residual-symbol census | THE SHARED MODULE IS REUSED, NOT COPIED, AND THE BLAST RADIUS IS ONE FILE. src/auth.ts only: 31 insertions / 22 deletions, and no other file in the function's tree changed. THE CHANGE: the local scalar cache and its Secrets Manager client are GONE -- the "@aws-sdk/client-secrets-manager" import, the module-level secretsClient const, the "let cachedPublicKey: string \| null = null" declaration and the whole "async function getJwtPublicKey()" are all deleted -- and replaced by a single import of getJwtKeySlots and verifyWithSlots from "./lib/authkeys/jwtPublicKeys.mjs". That is the SAME module TO-OP-S-10B deployed to the other two verifiers, reached through the build-time mirror the canonical build already creates for any consumer with a src/ directory. NO THIRD CACHE WAS HAND-ROLLED: a second implementation in this handler would reproduce row Z-S155 exactly, because two independent caches on the same period are indistinguishable to any per-process timing signal. RESIDUAL-SYMBOL CENSUS on the file: getJwtPublicKey 0, GetSecretValueCommand 0, SecretsManagerClient 0, secretsClient 0. cachedPublicKey reads 1, and that single occurrence is INSIDE THE NEW DOCSTRING quoting the retired line, not live code -- checked rather than assumed, because a residual-symbol count that does not distinguish a comment from a call site is not a control. THE ERROR-CLASSIFICATION CATCH IS BYTE-UNCHANGED, verified by diffing for it explicitly and finding no +/- line touching TokenExpiredError, JsonWebTokenError, or any authenticated-flag return. That catch is what every caller of verifyAuth sees, and verifyWithSlots rethrows the CURRENT-key error precisely so the classification keeps working through the change. A ts-ignore carries the untyped ESM import with its reason stated inline: the canonical build BUNDLES with bun and does not type-check, so a hand-written .d.ts would be a second declaration free to drift from the module it describes. | CLOSED 20260909T213651Z |
| L2 | activation | build via build-nodejs-lambda.sh (the lawful path TO-OP-S-10C established and proved) and deploy through TERRAFORM ONLY -- never aws lambda update-function-code, and never the function's own deploy.sh which calls it | safe-apply output + the new live CodeSha256 equal to the independently recomputed artifact sha | BUILT ON THE LAWFUL PATH AND DEPLOYED THROUGH TERRAFORM ONLY. BUILD: build-nodejs-lambda.sh portal-auth opal-session-analytics -- the first-entrypoint case (src/index.ts -> dist/index.mjs) that TO-OP-S-10C established and proved with two clean builds byte-identical to the deployed artifact. Bundle 70.11 KB, handler export validated by the script, zip sha 66qB33r/6QF+jkb/lcrSbRD+UvEnDhyDVK15rdV2+Ko=, uploaded as VersionId c1HZgy6RP0gYoMvTChq7SwZYlM7mA_3V. INDEPENDENTLY VERIFIED BEFORE THE APPLY, not taken from the builder's own stdout: the object was downloaded and its sha RECOMPUTED locally to the same value, equal also to the S3 metadata content-sha256.

*** AND THE FIRST PLAN READ "No changes." WITH THE NEW ARTIFACT ALREADY IN S3. *** That is the same shape as the qualified_arn pin trap on auth-validator-edge -- a clean plan that ships nothing -- and it was caught only because the plan was READ rather than assumed. The cause is by design and documented in the file itself: source_code_hash is HARDCODED rather than read through a data aws_s3_object lookup, because such a lookup evaluates at PLAN time and errors FABRIC-WIDE when the key is absent, blocking every concurrent lane on this root. That is a measured incident on this estate, not a theoretical risk, and the file cites it. SO UPDATING THAT ONE LINE IS THE DEPLOY: TW+G6NyLoKxqCdp6CtfU5WAixRf8phcP69Kxg6kx8EU= -> 66qB33r/6QF+jkb/lcrSbRD+UvEnDhyDVK15rdV2+Ko=, edited in the SAME commit as the code with the reason recorded inline, so the next reader meets the trap at the file rather than in a ledger.

RE-PLAN AFTER THE EDIT: "Plan: 0 to add, 1 to change, 0 to destroy", 0 forces-replacement, and the change set is exactly TWO attributes and nothing else -- last_modified to (known after apply), and source_code_hash old to new. ZERO wafv2 resources were pulled into this plan: this targets the FUNCTION, not the distribution, so the structural WAF ride filed as row Z-S156 does not apply here and was confirmed absent rather than assumed.

APPLY: HALT_ACK=1 safe-apply on the SAVED plan, so what shipped is exactly what was read. rc captured before any pipe = 0. "Apply complete! Resources: 0 added, 1 changed, 0 destroyed", modifications complete after 6s.

THE POST-APPLY CHECK IS AN EQUALITY TEST AGAINST A PREDICTED VALUE, not change-detection, which is the discipline this file's own comment asks for: the build is deterministic (fixed timestamp 2020-01-01, sorted entries) so the hash was known BEFORE the apply. Live CodeSha256 reads 66qB33r/6QF+jkb/lcrSbRD+UvEnDhyDVK15rdV2+Ko= -- EQUAL to the prediction and DIFFERENT from the baseline TW+G6NyLoKxqCdp6CtfU5WAixRf8phcP69Kxg6kx8EU=. State Active, LastUpdateStatus Successful, LastModified 2026-09-09T21:26:02Z. A change-detection check cannot tell a correct deploy from a wrong one; an equality check can.

THE BANNED PATH WAS NOT USED: the function's own deploy.sh reaches for aws lambda update-function-code, which CLAUDE.md and /cloud-ops ban outright. It was read and deliberately not run. | CLOSED 20260909T213651Z |
| L3 | verify | the two-slot accept path and a BOUNDED TIME COMPONENT present in the DEPLOYED BYTES -- searched on the artifact, never on source, and never for a source-level identifier (tsc renames them: cachedPublicKey became wq) | the post-deploy artifact downloaded, unzipped and searched, with the pre-change shape quoted beside it | THE TWO-SLOT ACCEPT PATH AND A BOUNDED TIME COMPONENT ARE IN THE DEPLOYED BYTES, QUOTED. The artifact was downloaded from the live function after the apply, unzipped (one member, dist/index.mjs) and searched. NOT on source, and NOT for a source-level identifier -- that is the second instrument failure this face inherited: tsc renames, and the pre-change grep for cachedPublicKey returned 0 while the single-slot cache was very much present as wq.

BEFORE, the baseline bytes (CodeSha256 TW+G6NyLoKxqCdp6CtfU5WAixRf8phcP69Kxg6kx8EU=):
  async function lJ(){ if(wq) return wq; if(wq=(await cJ.send(new uJ({SecretId:"opal/auth/jwt-public-key"}))).SecretString\|\|"",!wq) throw Error("JWT public key not found"); return wq }
ONE scalar, NO time component, one jwt.verify against one key.

AFTER, the deployed bytes (CodeSha256 66qB33r/6QF+jkb/lcrSbRD+UvEnDhyDVK15rdV2+Ko=):
  var i2="opal/auth/jwt-public-key", n2=300000, y6=null, x4=0, f6=null;
  async function R4({now:q=Date.now(),region:Z="us-east-1"}={}){ if(y6&&q-x4<n2) return y6; if(!f6)f6=new p2({region:Z}); let $=await f6.send(new l2({SecretId:i2})), Q=r2($.SecretString); return y6=Q, x4=q, Q }
  function B4(q,Z,$,Q){ try{ return q.verify(Z,$.current,Q) } catch(J){ if(!$.previous\|\|J.name==="TokenExpiredError") throw J; try{ return q.verify(...

THE TWO CLAIMS THIS CRITERION MAKES, each visible in the quoted bytes: (1) A BOUNDED TIME COMPONENT -- the guard moved from "if(wq) return wq" to "if(y6 && q-x4 < n2) return y6" where n2 is the literal 300000 and x4 is the timestamp written back on every refresh. The single scalar became slots-plus-timestamp. (2) THE CURRENT-OR-PREVIOUS ACCEPT PATH -- verify against slots.current, and on failure fall through to slots.previous unless the error is TokenExpiredError, because a second slot must widen which KEYS are accepted and never which EXPIRIES are.

REUSE MEASURED ON THE ARTIFACT, not asserted: the shared module's distinctive literals each appear EXACTLY ONCE in the deployed bundle -- "JWT public key secret is empty" 1, "JWT public key envelope has no usable" 1, the not-valid-JSON message 1, the secret id 1, and 300000 once. One copy, not two, which is what makes this a reuse rather than a third hand-rolled cache. | CLOSED 20260909T213651Z |
| L4 | verify | the function still verifying real traffic after the deploy, with the INVOCATION COUNT stated over the window -- silence alone is not sufficient because a dead function passes an error-free check | log read + CloudWatch Invocations over the same window | STILL VERIFYING REAL TRAFFIC, AND THE COUNT IS STATED SO A DEAD FUNCTION CANNOT PASS AS A HEALTHY ONE. Over the 30 minutes after the apply: 4,490 log events with nextToken ABSENT, so the window is complete and not a page; 0 error-ish lines (no ERROR, no "Invalid token", no "not found", no Exception); CloudWatch Invocations 1,107 over the same window; CloudWatch Errors 0 over the same window.

THE DECISIVE PART IS NOT THE SILENCE, IT IS THE COLD STARTS. 14 INIT_START events appear in that window -- 14 execution environments started fresh ON THE NEW BUNDLE. A cold start is exactly where a MODULE_NOT_FOUND on the new cross-tree relative import would fire, and where a bad bundle announces itself. It did not fire, fourteen times over.

WHY THE COUNT IS QUOTED BESIDE THE ZERO: an error-free read is what a DEAD function returns too, and this criterion says in terms that silence alone is not sufficient. 1,107 invocations with 0 errors is a healthy busy function; 0 invocations with 0 errors would have been an unread instrument. The two numbers together are the claim.

BASELINE FOR SCALE, measured before the deploy: 52,540 invocations over the preceding 7 days and 291,233 over 30 days, so this function is among the busiest verifiers in the estate and a broken key path would surface immediately rather than lurking. | CLOSED 20260909T213651Z |
| L5 | verify | NOTHING ROTATED: describe-secret unchanged; and DELIVERABLE 0 closed -- the two image-packaged candidates the earlier census could not read | describe-secret output + the layer-search result with its blob denominator | NOTHING ROTATED, AND DELIVERABLE 0 IS CLOSED ON THE CODE PLANE RATHER THAN FILED UNCOMPUTABLE.

NOTHING ROTATED, re-measured after the apply: opal/auth/jwt-public-key holds ONE version, id fabe94f0-019d-455d-8c72-47b3d709bd8b at AWSCURRENT, LastChangedDate 2026-04-06T13:31:00.259000-04:00, RotationEnabled unset, no DeletedDate -- identical to the baseline this session captured at 18:3xZ before any deploy. opal/auth/jwt-private-key likewise: one version, LastChangedDate 2026-04-06T13:31:00.251000-04:00, RotationEnabled unset. This face teaches a reader; it never writes the secret. (Both timestamps carry their true -04:00 offset and NOT a typed Z -- the citation-hygiene trap commit bd6e7cb8c7 corrected on this project.)

DELIVERABLE 0 -- THE TWO IMAGE-PACKAGED CANDIDATES THE EARLIER CENSUS COULD NOT READ. The face permitted UNCOMPUTABLE-BY-CONSTRUCTION; it was not needed, because the ECR API exposes each layer blob and they were STREAMED and decompressed in memory without docker, which is not on this box.

  finbert-lambda:latest (opal-news-ai-sentiment)
      14 of 14 blobs read (13 layers + config), 0 errors, 1,164,760,079 bytes compressed
      and about 2.77 GB decompressed searched.
      opal/auth/jwt-public-key 0 \| jwt-public-key 0 \| jsonwebtoken 0 \| jwt.verify 0
  news-semantic-clustering:latest
      13 of 13 blobs read, 0 errors.
      opal/auth/jwt-public-key 0 \| jwt-public-key 0 \| jwt.verify 0 \| jsonwebtoken 1
      (that one hit is a transitive npm dependency present in the image; there is no
       reference to the secret and no verify call site.)

NEITHER IS A READER, and the zeros are real absences because every blob was read and the error count is 0 -- an incomplete read would have been reported as INCOMPLETE rather than as a zero. THE NEEDLE SET WAS DELIBERATELY WIDER THAN THE SECRET ID: searching also for the library name means even a dynamically-built secret id would very likely have surfaced as a jsonwebtoken hit in the function that verifies.

CORROBORATION ON A SECOND PLANE, and its limit stated: news-semantic-clustering shows 0 CloudWatch Invocations over 30 days and 0 CloudTrail events over 90 days with NextToken ABSENT, so it is DEAD and could not break under a rotation regardless of content. opal-news-ai-sentiment is ALIVE at 37,740 invocations over 30 days, which is exactly why its layers were read in full rather than reasoned about.

WHY THE LIVE PLANE COULD NOT SUBSTITUTE FOR THE CODE PLANE HERE, recorded because it is the reusable part: a CloudTrail GetSecretValue sweep was attempted first and THROTTLED OUT with NextToken still present -- 43 pages, 2,150 events, a PARTIAL read. Its own internal control settles the matter: opal-session-analytics, a reader PROVEN on the code plane, also read 0 in that partial window. A zero from a partial page is not an absence, and it would have been reported as one.

THE FRAME'S REMAINING LIMITS, printed rather than implied: the code plane says who CAN read and never who DOES; a reader outside the five granting roles is out of frame entirely; and a secret id assembled at runtime from fragments would defeat a literal needle in any of these searches. | CLOSED 20260909T213651Z |

## Log

- 20260909T211903Z OPENED by 0.7.0_AE_CloudOps~V with 5 leg(s)
- 20260909T213341Z LEG L1 closed: THE SHARED MODULE IS REUSED, NOT COPIED, AND THE BLAST RADIUS IS ONE FILE. src/auth.ts only: 31 insertions / 22 deletion
- 20260909T213341Z LEG L2 closed: BUILT ON THE LAWFUL PATH AND DEPLOYED THROUGH TERRAFORM ONLY. BUILD: build-nodejs-lambda.sh portal-auth opal-session-ana
- 20260909T213651Z LEG L1 closed: THE SHARED MODULE IS REUSED, NOT COPIED, AND THE BLAST RADIUS IS ONE FILE. src/auth.ts only: 31 insertions / 22 deletion
- 20260909T213651Z LEG L2 closed: BUILT ON THE LAWFUL PATH AND DEPLOYED THROUGH TERRAFORM ONLY. BUILD: build-nodejs-lambda.sh portal-auth opal-session-ana
- 20260909T213651Z LEG L3 closed: THE TWO-SLOT ACCEPT PATH AND A BOUNDED TIME COMPONENT ARE IN THE DEPLOYED BYTES, QUOTED. The artifact was downloaded fro
- 20260909T213651Z LEG L4 closed: STILL VERIFYING REAL TRAFFIC, AND THE COUNT IS STATED SO A DEAD FUNCTION CANNOT PASS AS A HEALTHY ONE. Over the 30 minut
- 20260909T213651Z LEG L5 closed: NOTHING ROTATED, AND DELIVERABLE 0 IS CLOSED ON THE CODE PLANE RATHER THAN FILED UNCOMPUTABLE.

NOTHING ROTATED, re-meas
- 20260909T213734Z CLOSED -- all 5 legs proven
