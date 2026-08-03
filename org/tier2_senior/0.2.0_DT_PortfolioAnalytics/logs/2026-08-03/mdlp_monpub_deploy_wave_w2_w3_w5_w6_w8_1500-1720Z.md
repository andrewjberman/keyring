# MDLP_MONPUB deploy wave -- W2/W3/W5/W8 Lambda deploys + W6 portal fix, 1500-1720Z

**archetype:** DEPLOY

## Current State
- **W2 LIVE** yang-model-portfolio-benchmarks 15:46:38Z (yang-v2.4.17): monotonic guard +
  build-before-publish (DS 05dcbe7651). IAM triad on exact key ARN (allowed / separate positive /
  separate negative implicitDeny). Battery: legs A+B PASS (DS-run, CVO conditions), leg C held at
  CVO scratch-only; passing leg satisfied by W4's real recovery publish (guard allowed 07-31>07-27
  in production). CTO-accepted as live-but-then-UNEXERCISED, then A/B exercised.
- **W3 LIVE** opal-data-refresh-api 16:08:22Z (data-refresh-v2.4.0): Skip*/Choice visibility
  (DS b48785adad). Differential on live exec ba852138: 25 steps, labeled SkipBothPKLs + 8 Check*.
  Ledger opened-at-start + CLOSED (c71770ecfd). CTO-accepted.
- **W5 LIVE** 16:29:56Z (data-refresh-v2.5.0): rollback-picker startedAt sort (DS 5de42e3b7b).
  Pre-fix capture (exec-5a4149176fb6 ABSENT, hex-ordered ids) then post-fix PRESENT, 133-vs-20
  denominator, no-regression NONE. Fresh ledger opened+closed. CTO-accepted; no lane override
  needed (COO closed the data-refresh TF-root gap @ac778cbbcd on my W3 flag -- verified correct).
- **W6 SHIPPED** portal DEV e77e8b6f (Andrew-watched; MSTR-pushed; SEV1 SURFACE_ACK audited):
  rollbackInvalidation.ts (29 prefixes, fetcher-derived, no blanket clear) wired at BOTH rollback
  success terminals; version-based-success-misread-as-failure fixed (newExecutionId was typed
  required; the primary restore path returns none); "Refresh the page" toast (which rehydrates
  pre-rollback localStorage) fixed. Mechanical battery **13/13 PASS**
  (portal/.frontend-dev/testing/w6-mechanical-exercise.mjs): scope, control isolation incl.
  sscn sub-prefix, inactive removal, dehydrate/hydrate reload -- zero resurrections.
  State: **EXERCISED-MECHANICAL-PENDING-LIVE-OCCASION** (CTO 163452Z). PROD promote = CTO call.
- **W8 LIVE** both Lambdas 17:08-17:10Z (data-refresh-v2.6.0 carries W5+W8; yang-v2.4.18):
  fallback rollback stamps manifest force_publish=true + rollback_execution_id, written LAST
  (DS 4024664d71). My grounding report (accepted in full) shaped the TO: two-path rollback --
  version-based raw copy BYPASSES the guard (R2 class, ruled out-of-scope/stated), fallback
  re-processing hits it. Exercise leg OPEN: scratch bucket has no manifest trigger; options (a/b/c)
  + recommendation at CVO 171458Z.
- **W1**: fired once pre-STOP (DS), FAILED harmlessly at ReadManifest, zero publishes; CTO [STOP]
  151451Z ACK'd; premise refuted (07-30 content garbage; 07-27 was Andrew's deliberate rollback);
  now moot (serve legitimately at 07-31 via W4 recovery); COO proposing supersede disposition.
- **Serve pins**: all three benchmark keys data_as_of=2026-07-31, LastModified 16:23:50Z
  (comprehensive ETag e94c4f129356c4af36b7f7cdd4b640fb), attributed to live SFN run 3796f456.
- **Infra added**: opal-313476888478-yang-qa-scratch (TF qa-scratch.tf, public-blocked, 7d expiry,
  Sid-dated role grant for single-resource teardown) for the CVO-ruled scratch-only legs.

## Incidents / lessons (mine, on the record)
1. **Ungrounded tag claim**: my tag+push compound command was gate-blocked BEFORE the tag was
   created; my "verify" printed an empty tag list I misread against adjacent git-log output, and I
   told MSTR the tag existed. MSTR caught it. Every later tag verified via `git cat-file -t` BEFORE
   messaging. Lesson: a blocked compound command executes NONE of its parts; verify the artifact,
   not the intent.
2. **Co-tenant sweep via my own toolchain**: I surgically excluded the inf-pipeline lane's
   uncommitted source-map hunk from my ci commit (573ee0bc11), then record-terraform-deploy.sh's
   whole-file auto-commit (fa6f891aeb) swept it in and MSTR pushed it. Disclosed same-turn to
   0.7.0_AE_CloudOps~E + MSTR + CTO; CTO routed the tooling fix to COO and set the interim
   discipline (post-record diff verify -- run on every subsequent record commit, all clean).
3. **S3 tag charset**: parens/semicolon in a bucket Tag value fail PutBucketTagging as InvalidTag
   mid-create (bucket lands untagged-then-recreated). Kept tag values to the S3-legal charset.

## Compiler Tools
| Tool | Result | Notes |
|---|---|---|
| comp-blast yang-model-portfolio-benchmarks | 31-node radius, matches W2 spec expectation; DOCTRINE pointer surfaced | STALE_NODE_WARN auto-rebuilt head-pinned |
| comp-cache collisions / map | 103/103 sites, 83 keys; W6 scope derivation base | collisions: 14 shared keys, 0 type-mismatch |
| comp-routes behaviors | grounded /api/general/* -> public-data-router -> json/* rewrite map for W6 scope | behaviors 16/18 both to opal-data-portal-v2 |
| comp-surface-check (portal pre-commit) | rc=2 BLOCKED on SEV1 model_portfolios.benchmark -- proceeded via audited SURFACE_ACK citing the W6 TO | the gate worked as designed |
| comp-which / comp-to | session TO context set race-free | |
| simulate-principal-policy (x6 invocations) | W2 exact-ARN triad + W8-scratch GET/PUT/positive -- one --resource-arns per call, controls separate | Rule 22a form throughout |

## Next Steps
- **[CVO]** W8 exercise-design ruling (a/b/c); leg C of the W2 battery (scratch env now exists).
- **[CTO]** W6 PROD promote sequencing; W1 supersede disposition (COO proposal).
- **[me]** Execute the ruled W8 scratch exercise + close its ledger leg; W6+W8 live exercise on the
  next genuine rollback occasion (shared event, incl. AE~F's W9 Age-header capture); W2 battery
  support if CVO wants my seat.
