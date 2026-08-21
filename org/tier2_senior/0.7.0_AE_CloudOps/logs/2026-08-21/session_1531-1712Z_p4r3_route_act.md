# OPAL_ADVIPOINTERS P4R-3 remedy (A) -- the canonical platinum/advi/{firm}/ route act

**archetype:** DEPLOY
**secondary_archetypes:** DIAGNOSE, VALIDATE

**Window:** 2026-08-21 15:31Z -> 17:12Z | **Serial:** 0.7.0_AE_CloudOps (fresh seat, PID 20756)
**Authorizing chain:** LD-0442 -- CTO arch ruling (A) 64829 + BINDING tenant-assertion amendment
64843 -- COO ruling/routing 64839. In-flight under its CURRENT spec per Rule 27's in-flight clause.

## What this was

DE's P4R-3 found the CVO-certified ADVI advisor twins UNREACHABLE from every portal route family:
shared-advisor-router resolves the origin bucket SOLELY from the validated firmId (FIRM_CONFIG
49financial -> opal-data-bd), while DS~B published the twins to the ratified CLAUDE.md 17b serving
tier, opal-data-portal-v2/platinum/advi/49financial/. Re-measured here before any edit: 10 twins in
portal-v2, and opal-data-bd has NO platinum/advi/ prefix at all. Five seats were event-gated behind
the fix.

## Deployment Sequence

1. Bucket-policy leg FIRST (inert until the route points there): OAI E139998VWH0PD granted
   s3:GetObject on arn:aws:s3:::opal-data-portal-v2/platinum/advi/* -- prefix-scoped, tighter than
   the firm buckets' whole-bucket grants. Read back live: 3 statements, both pre-existing serving
   statements BYTE-UNCHANGED; public serving re-confirmed 200 on a live json-tiered key, 403 control.
2. Router shared-advisor-router v14 -> built -> TF apply -> edge v24 on 4 behaviors.
3. Response guard shared-advisor-router-response -> edge v5 on 4 behaviors.

All applies through safe-apply.sh (NEVER#4 / Rule 18); Terraform-only (Rule 1); deploy-completion
ledger org/critical_paths/change_management/20260821T1557Z_advi-p4r3-*.md OPENED 15:57:32Z BEFORE
the first deploy act, CLOSED 16:28:12Z, 5/5.

## Verification (ACTUAL output)

    terraform plan (post-apply):  No changes. Your infrastructure matches the configuration.
    live distribution EVTSA9VEHNZVH: status=Deployed
      shared-advisor-router           v24  x4 behaviors
      shared-advisor-router-response  v5   x4 behaviors
    deployed v24 bytes: 5/5 change markers present, negative-control marker 0,
      CodeSha256 1xewzMSnrs/... == built artifact == source map

    PRE-CONTROL   no token                   -> 401 (route is auth-gated)
    POSITIVE      49financial -> own tenant  -> 200, 11,129 B
                  served sha256 23a3b2c518... == s3 sha256 23a3b2c518...  BYTE-IDENTICAL
    ALL 10 TWINS                             -> 10/10 HTTP 200, byte counts matching S3 exactly
    NEGATIVE (isolated invocation, CTO 64843):
                  49F token -> platinum/advi/inflection/ -> 401 Firm scope mismatch, zero body
    NEGATIVE (target EXISTS -- the discriminating form):
                  inflection token -> 49financial's REAL dir -> 401 Firm scope mismatch
                  same token -> its own legacy tree          -> 200 (token valid, refusal targeted)
    NEVER-WIDEN   4 HELD keys + d14 -> 200 from legacy platinum/firm/, unmoved
                  platinum/advisors/{id}/summary.json -> still blocked (PII block intact)

## The defects found on the way (worth more than the routing fix)

**1. LIFECYCLE PIN -> INERT DEPLOY.** First plan read 0 add / 1 change / 0 destroy with
aws_cloudfront_distribution explicitly NO-OP. ignore_changes = [qualified_arn] pinned the PLANNED
arn at :23, so a new Lambda version would publish while CloudFront kept serving the OLD code --
green on DESIRED (clean plan AND a true 0-diff), APPLIED (a real new version) and EXERCISED (route
runs fine, on old bytes) SIMULTANEOUSLY. Caught in the plan JSON before applying. Fixed for the 2
functions this act deploys; MEASURED the other 3 as latent-with-ZERO-current-drift rather than
guessing (pin removed from all five -> still 0/2/0, only this router repoints). Recorded at the top
of lambda-edge.tf where the next edge deploy reads.

**2. DEAD CI GATE, PRE-EXISTING SINCE 06-09.** Verified at pristine HEAD before any edit: mocha's
bin resolves yargs through the CJS loader while these packages declare type=module, throwing before
reading a single spec. The ADVI_FIRMSEP.04 gate was failing CLOSED on every invocation -- blocking
all builds of both functions while asserting NOTHING about firm routing. Runner moved to bun test
(already the build toolchain, no new dependency).

**3. THE ONE ONLY AN EXERCISED FETCH COULD FIND.** With the router deployed, grant live, plan clean
and bytes verified, the first authenticated GET returned 502 firm_isolation_guard: the
origin-RESPONSE function independently re-derives the expected bucket and did not know portal-v2 was
legitimate. NOTHING WAS MISCONFIGURED. Fixed by teaching the guard the rule BY INDEPENDENT
RE-DERIVATION (importing the router's answer would collapse two layers into one). The load-bearing
part is the else branch -- the naive "any platinum/advi may come from portal-v2" would have BLESSED
the exact cross-firm mis-route the guard exists to catch.

## Controls -- proven by MUTATION, not asserted

router 17 pass / guard 35 pass. Disarm the tenant assertion -> 7 fail (all 4 negative controls).
Drop the trailing slash -> 4 fail. Naive guard -> exactly the 2 guard negative controls fail.
RECORDED HONESTLY: my PREFIX COLLISION test passes with AND without the slash it appears to guard
(the PII branch returns first), so it does NOT control the prefix -- a separate discriminating test
was added. A control that cannot fail is not a control.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-find | key/name searches across org, infra, portal | PARTIAL | 123-file denominator over org/mcp was a TRUE count over the WRONG domain (inbox gitignored; 63,914 .md present). Positive control caught it. |
| comp-routes behaviors | CF serving path | PASS | 27 behaviors; confirmed the depth-1 .json behavior carries platinum paths into the advisor router |
| comp-routes origins | origin/OAI map | PASS | gave S3-opal-data-bd OAI E139998VWH0PD -- the identity the mutated origin carries |
| comp-routes edge-versions | pinning scanner | FAIL (tool defect) | reports all 5 as DYNAMIC [OK]; cannot see the ignore_changes that defeats it. Routed to CTO. |
| comp-iam | not used for the grant | N/A | INAPPLICABLE BY DOMAIN: grantee is a CloudFront OAI canonical user, not an IAM principal; simulate-principal-policy cannot model it -- the exercised fetch IS the oracle for that leg |
| AST sweep (authored) | constructed-key census, COO-scoped | PASS | 198 files / 272 call sites; LITERAL 30 (11.0%), GENERATIVE 147, NOT_MEASURABLE 95 |

**What worked:** comp-routes origins settled the OAI question in one call; the rail gate correctly
forced comp-routes where I had reached for raw aws.

**What failed:** comp-routes edge-versions [OK] is FALSE for a pinned function -- the exact
false-green class this estate polices, inside a comp-tool.

**Gap found:** NO comp-tool reads a LIVE CloudFront distribution (comp-routes is DESIRED-plane by
its own COVERAGE line), so every live association read this session needed a rail-checked raw aws
call. Genuine coverage gap, not an inconvenience.

## MCP traffic

~30 messages. Significant: ACK'd MSTR 64705 (D7 WA-APPLY laptop leg SUPERSEDED -- did NOT apply);
route-act report to CTO/COO/MSTR/DE; CTO 65001 ACCEPTED both surfaced interpretations; answered
PartnerETL's box-arch call (AMI-sibling, decided on the schedule-coupling rule, not the proxy
concern I originally raised); supplied DE the capture bearer; answered COO's stage-3 measurement
cell (surface 11 OPERATIVE) and ran the constructed-key sweep; corrected MSTR's Rule-27 hash
citation and COO/CVO's "five firms" count (3 firm dirs, measured live).

## Blockers

None. One SOVEREIGN CALL OPEN at Andrew: whether to build the advTenant tenant-grain remedy at all.
He questioned its value given mockadv has ZERO users (measured, opal-users scan: 12 rows, 0 mockadv,
0 demo). My recommendation is PARK. NOT building under a silent clock; CTO clarified the row reads
"owner acknowledged, disarm landed, BUILD awaiting Andrew's call."

## Current State

- ROUTE LIVE AND EXERCISED. platinum/advi/{firm}/ -> opal-data-portal-v2 on the advisor-intelligence
  family, auth-validator-edge + per-firm scoping intact. Edge v24 (router) / v5 (response guard),
  distribution EVTSA9VEHNZVH Deployed, terraform 0-diff.
- CHAIN CLEARED: DE flipped @9580e18b -> CVO POST-FLIP -> DT seated -> DE capture COMPLETE.
  LD-0441's DT trigger retired from KNOWN-UNREACHABLE by MSTR on this evidence.
- TENANT ASSERTION compares the path segment's resolved bucket against the caller's resolved bucket
  (NOT bare pathFirm === firmId, which would refuse the mockadv alias and the opal-capital staff
  proxy). CTO upheld, then COO surfaced the grain limit and CTO corrected the ground: it holds only
  while one bucket is one firm. Filed as CVO channel row S1, OBSERVATION/ARMED, disarm owner
  0.7.0_AE_CloudOps.
- DISARM LANDED (not the remediation): infra/aws/lambda-edge/_shared/firm-config.mjs carries the
  hazard, the measured mockadv evidence and the re-runnable controls at the top of the file anyone
  must edit to create the condition. ZERO deployed drift VERIFIED (controlled with/without build:
  identical 9,018-byte bundles -- comments are stripped at bundle time).
- SWEEP DELIVERABLE: org/tier2_senior/0.7.0_AE_CloudOps/deliverables/
  MDPF_PROVCANON_CONSTRUCTED_KEY_SWEEP_20260821.md @fda8d69db9, corrected @b167534ba7 (DE caught my
  "never named" overstatement; the portal registry DOES name all 15 leaves -- what is invisible is
  the COMPOSITION, which is the worse failure because a census can report the surface COVERED and
  still be wrong about what it does).
- TAG portal-auth-v1.23.0 (annotated, local). Push is integrator-only.
- Capture bearer for DE expires 2026-08-21T18:15:31Z; key material scrubbed from the scratchpad.

## Next Steps

- [Andrew] PARK or BUILD the advTenant tenant-grain remedy. Nothing blocked either way.
- [0.7.0_AE_CloudOps] if BUILD: advTenant field in FIRM_CONFIG (alias pairs DECLARED, not implied);
  an identity with NO advTenant REFUSES all platinum/advi/ reads -- fail-closed BY CONSTRUCTION
  (COO's CE question). Both routers; the guard re-derives independently. Write the negative control
  RED first.
- [1.0.0_SA_CTO] two routed items, no clock: the qualified_arn pin on the 3 remaining edge lambdas
  (latent, zero current drift), and comp-routes edge-versions reporting DYNAMIC [OK] for a pinned
  function.
- [1.0.0_SA_CTO / 0.0.0_AB_MSTR] estate-wide constructed-key INVENTORY needs an owner -- surfaced,
  deliberately NOT started; at ~11% literal it is an inventory of the normal case, not a defect sweep.
- [0.7.0_AE_CloudOps] carried, no clock: CTO's routed bd-exporter two-homes finding
  (infra/aws/ec2/bd-exporter/terraform/main.tf:84-128 duplicates the bd-exporter-ec2-role and its
  s3-access policy in a SECOND TF root, diverged from the canonical bd-pipeline copy).
