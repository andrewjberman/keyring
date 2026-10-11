# ADVI_FIRMBKTS task order -- `FB-f-8` -- WINDOW ACT 1: DEPLOY THE advTenant BUILD (shared-advisor-router and shared-advisor-router-response) -- PHASE B, THE DEPLOY

<!-- ===================== WORKER FACE -- this is the WHOLE of the actor's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R3.md</decomp_doc>
<owned_cells>FB-f-8</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~FBL</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>ROUTER_VERSION, GUARD_VERSION, ROUTER_SHA256, GUARD_SHA256, WAF_ACL_NAME, WAF_ACL_ID</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, rule, schedule or cadence is added or changed.
comp-iam: RUN by the issuer AT THE WRONG GRAIN and corrected: iam:SimulatePrincipalPolicy on user/cloudops-dell1-agent-user read allowed for lambda:PublishVersion, lambda:UpdateFunctionCode, lambda:GetFunctionConfiguration, cloudfront:GetDistributionConfig and cloudfront:UpdateDistribution at resource `*`. The deploy policy's `DenyProtectedFunctions` (CT-a-1; `infra/aws/terraform/nfra-ctlpln-identity/protected_functions.json`, rule b, lambda-at-edge) NAMES both functions and denies this identity `lambda:UpdateFunctionCode` and `lambda:PublishVersion` on them: the apply was refused 403 at 07:53Z (row D1-S13). The identity that applies act 1 is the laptop CloudOps identity (CTO ADDENDUM 2 @30bdd99110); its read is step 0b, at the qualified function ARNs, and is the actor's.
comp-adversary: RUN by the issuer -- the build is `TO-FB-f-7` (merged @e6ec8ce6e4) with `TO-FB-f-8` phase A (merged @acf8a16706): router gate 51 pass, guard suite 46 pass, dormancy grid router 88 of 88 and guard 396 of 396 identical to base, both files 0 non-ASCII bytes. The three criteria below read FAIL at base by construction (no new version exists).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE ACT -- `FB-f-8` phase B (round 3, enrichment item 1, step 1 of the cutover window)

You deploy two Lambda@Edge functions as ONE act, through Terraform only: `shared-advisor-router` (live version 26) and
`shared-advisor-router-response` (live version 5), each associated on 5 behaviors of CloudFront distribution
`EVTSA9VEHNZVH`. The build is dormant: for the registry as it stands every decision is identical to today's, so no
request changes. The act is signed by the never-widen pair
`org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/NEVER_WIDEN_ROUND3_ACT1_ADVTENANT_COO_HALF.md` and `..._CTO_HALF.md` (the CTO
half SIGNED @d30c5fe203), and by their ADDENDUM 1, the WAF web ACL rider (`..._COO_HALF_ADDENDUM_1.md`, the CTO half's
addendum SIGNED @d1fe697698); the pair's permitted set and both branches are the whole of what you may touch and when you
stop. READ BOTH HALVES FIRST, and `org/tier2_senior/0.7.0_AE_CloudOps/logs/2026-08-21/session_1531-1712Z_p4r3_route_act.md`
(the last deploy of both functions: its three defects are the traps below). Procedure: `docs/deployment/
LAMBDA_DEPLOYMENT_PROTOCOL.md`, `docs/deployment/TERRAFORM_PROTOCOL.md`, `docs/deployment/cloudfront_deployment_checklist.md`
and `cloudfront_rollback_plan.md`; load `/cloud-ops` before any AWS or Terraform act.

### 1a. The steps, in order

0. **Gate.** `git ls-tree HEAD` must list BOTH pair halves; the CTO half's verdict line must read SIGNED; the two
   `index.mjs` sources must read 0 non-ASCII bytes (`FB-f-8` phase A merged); and, once built (step 2), each BUILT artifact
   must read 0 bytes above 127 (the bundle that ships: the CTO's close is "the deployed file reads 0 bytes above 127").
   `shared-advisor-router/tier_policy.mjs` carries 19 non-ASCII bytes in comments and is bundled; a minified bundle strips
   them (row D1-S11, measured by this seat), so the built artifact is the measure, not the source. If any gate is not so:
   STOP, a BLOCKING row, no write to AWS.
0b. **Identity read (CTO ADDENDUM 2).** Name your identity (`.tools/aws sts get-caller-identity`). `iam:SimulatePrincipalPolicy` for it on the two qualified function ARNs `arn:aws:lambda:us-east-1:313476888478:function:shared-advisor-router` and `arn:aws:lambda:us-east-1:313476888478:function:shared-advisor-router-response`, and each with `:*`, for `lambda:UpdateFunctionCode` and `lambda:PublishVersion`, must read `allowed` on every one of the eight pairs: the grain is the function ARN, never `*`. Any `implicitDeny` or `explicitDeny`: STOP, a BLOCKING row, no write to AWS. The act is then Andrew's (his user runs `safe-apply` from the signed plan) and nothing is drafted to widen an identity.
0c. **Checkout.** `git merge-base --is-ancestor <sha> HEAD` reads rc=0 for each of `acf8a16706` (phase A), `d1fe697698` (CTO ADDENDUM 1) and `30bdd99110` (CTO ADDENDUM 2), and this order's bytes at HEAD equal the crossbox ORDER's pinned commit (`git show <pin>:<this file>` against the file). A box behind its trunk syncs through its own scheduled sync first; no file is hand-copied.
1. **The entry.** Open the change-management entry BEFORE the first act: `python .tools/deploy_ledger.py open ...` (read its
   `--help`), naming the two functions, the distribution, all 10 associations, the previous versions (26 and 5) as the
   rollback, and the pair. Commit the entry and its `org/critical_paths/.open_deploys/` sentinel first.
2. **Read before you write.** Save the live `get-distribution-config` (ETag and the 10 associations) AND the ACL's
   `get-web-acl` JSON (`WAF_ACL_NAME`, `WAF_ACL_ID`, its `LockToken`, the 6 rules) into the entry as the rollback record. Confirm the live router is version 26 and the guard version 5 on 5 behaviors each. Build both
   artifacts with the repository's `build-nodejs-lambda.sh` from the merged tree; record each artifact's SHA-256
   (`ROUTER_SHA256`, `GUARD_SHA256`: the `CodeSha256` the published version must read) and its count of bytes above 127
   (expected 0, printed beside the SHA in the entry).
2a. **State reconciliation: MEASURED, NOT PERFORMED (amendment 6).** The Dell executor measured at `22cc1b1e75` that a refresh-only plan lists drift on the WAF ACL only: `s3_object_version` is configuration-side and the Lambda API does not return it, so a refresh-only apply would write state without moving it. The state's pre-act `s3_object_version` for the two functions (the Dell's pre-reconcile read, `fSTYD2_FNp1pEGyyGwiacP3Tz_QtztS9`) is recorded in that entry; yours is read at this step and kept in YOUR entry. Step 2's rebuild uploads a new S3 VersionId, so the plan at step 3 lists the two functions again. A plan at step 3 that reads either function NO-OP while its published version is older than the built artifact is the `qualified_arn` pin defect: STOP.
3. **Plan.** Run the Terraform plan of `infra/aws/terraform/portal-auth/` through the repository's wrapper and read the
   plan JSON. It must change EXACTLY the two functions (each a new published version), the distribution's 10
   associations, and the ADDENDUM 1 rider `aws_wafv2_web_acl.opal_cloudfront_protection` (three `version` attributes,
   `""` to `null`, on the Count-mode managed groups `common-rule-set`, `ip-reputation`, `known-bad-inputs`), nothing else. A plan that publishes a version while `aws_cloudfront_distribution` reads NO-OP is the
   `qualified_arn` pin defect: STOP. A plan naming any other resource, or drift outside the act: STOP.
4. **Apply** through `safe-apply` only (never a bare `terraform apply`, never `aws lambda update-function-code`). Wait for
   the distribution to read `Deployed`.
5. **Read back.** Each of the 10 associations reads the new version; `CodeSha256` of each new version equals the artifact's;
   the ACL's `get-web-acl` equals the pre-act read rule by rule (name, priority, action or override action, statement,
   visibility config) except the `version` representation and the `LockToken`, the three groups still read Count, and
   the default action is unchanged (the CTO's conditions); a post-apply plan reads no changes. Record the two new version numbers (`ROUTER_VERSION`, `GUARD_VERSION`).
6. **Oracle.** Send ONE message to `1.0.0_SA_CTO~DELL1` at `Deployed`, naming the entry and the two versions: the CTO
   invokes both new versions on the 5 event classes against base, makes one live no-session request (401 expected) and
   diffs the associations. Do not close the entry before the CTO's read.
7. **Criteria and close.** Run AC1-AC4, write the proof instance in your own deliverables folder, close the entry with the
   evidence, flip this order's `<status>` to `complete` in the same commit.

## 2. BOUNDS

1. The only writes are the two artifact objects the Terraform data sources read, the Terraform apply of the two functions
   and the 10 associations, and the change-management entry. No policy, bucket, schedule, IAM, secret or other function
   changes; `auth-validator-edge` is NOT redeployed; no second apply.
2. If the plan or any live read differs from the pair's permitted set: STOP before the apply and file a BLOCKING row.
3. If any post-apply read differs from Branch A of the COO half, the rollback in the pair runs at once (the prior versions
   re-associated through `safe-apply`), the order stays open, and a BLOCKING row says why.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FBL/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

(The Terraform files under `infra/aws/terraform/portal-auth/` are read by the plan; they do not change in this act unless
the plan says a pin must drop, which is a STOP. The build artifacts are not committed.)

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FBL/ADVI_FIRMBKTS.TO-FB-f-8.act1-deploy-advtenant.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-f-8"><invocation>.tools/aws lambda get-function-configuration --function-name shared-advisor-router --qualifier <ROUTER_VERSION> --region us-east-1 --query CodeSha256 --output text</invocation><expect><ROUTER_SHA256></expect></criterion>
  <criterion id="AC2" cell_refs="FB-f-8"><invocation>.tools/aws lambda get-function-configuration --function-name shared-advisor-router-response --qualifier <GUARD_VERSION> --region us-east-1 --query CodeSha256 --output text</invocation><expect><GUARD_SHA256></expect></criterion>
  <criterion id="AC3" cell_refs="FB-f-8"><invocation>.tools/aws cloudfront get-distribution-config --id EVTSA9VEHNZVH --query "DistributionConfig.CacheBehaviors.Items[*].LambdaFunctionAssociations.Items[*].LambdaFunctionARN" --output text</invocation><expect>shared-advisor-router:<ROUTER_VERSION></expect></criterion>
  <criterion id="AC4" cell_refs="FB-f-8"><invocation>.tools/aws wafv2 get-web-acl --name <WAF_ACL_NAME> --id <WAF_ACL_ID> --scope CLOUDFRONT --region us-east-1 --query "length(WebACL.Rules[?OverrideAction.Count!=`null`])" --output text</invocation><expect>^3$</expect></criterion>
</proof_of_spec>

AC1 and AC2 read each published version's hash against the built artifact's (the pair's measure). AC3 reads the live
associations: five behaviors carry the router at the new version and five carry the guard (a bounded read of one
distribution). The criteria in the proof block of phase A (AC1-AC4 of the first face: non-ASCII 0 and 0, router gate 51
pass, guard 46 pass, dormancy grid 0 and 0) are CLOSED at `acf8a16706` and are cited, not re-run, by this act.

## 5. WHEN YOU ARE DONE

Close the change-management entry with the three outputs and the CTO's read; flip `<status>` to `complete` in the SAME
commit as the proof instance. A row id on this project carries the box's coordinate, which is bare on the laptop: as a seat you
file `ADVI_FIRMBKTS-S<k>` with the next unused `k` (read the channel for the highest bare `S`), `surfaced_at` from `date -u
+%FT%TZ`. Report once to `2.0.0_SA_COO~B1`: the pair's two blob ids, the plan's resource summary, the live associations
per behavior, the three outputs, the post-apply plan line, the CTO's read, the entry's path and the commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the actor ===================== -->

**AMENDMENT 1 (2.0.0_SA_COO~B1, after the CTO's act-1 half @d30c5fe203, msg 3601):** the pair was SIGNED on one
precondition (both functions all-ASCII in one commit, the build cut from it, the grid re-read). It was a worker cell, phase
A of this order, merged @acf8a16706 (AC1-AC4 PASS: 0 and 0 non-ASCII bytes, router 51 pass, guard 46 pass, grid 88 of 88 and
396 of 396 identical; row D1-W17-S7 records the `[STOP]` spelling for U+26D4).

**AMENDMENT 2 (2.0.0_SA_COO~B1):** phase B. The executor is the CloudOps class seat, seated as a lane of this project
(`0.7.0_AE_CloudOps~FB1`): a Tier-2 seat hears an act only as a task order, and the 2026-08-21 act of these two functions
was the CloudOps seat's (three defects found only by exercising, recorded in its log). The order's `<issued_to>` moves
from the worker slot `~17` to that lane; the proof instance is the seat's own, in its own deliverables folder, and cites
phase A's merged instance for AC1-AC4. Gate limb: the criteria text and the `<issued_to>` of an order whose phase A is
complete are amended; GATE viii read `<placeholders>` at HEAD (`NONE`, amendment 1) and the four tokens now declared are
each carried by an invocation or an expect.

**AMENDMENT 3 (2.0.0_SA_COO~B1, on the seat's STOP, row D1-S11, msg 3614):** step 0 read "sources"; the executor measured
that the router bundles `tier_policy.mjs` (19 non-ASCII bytes, all in comments), which neither pair half names. The CTO's
precondition names the two `index.mjs` files and its close criterion is "the deployed file reads 0 bytes above 127"; the
built artifact reads 0 (a minified bundle, measured by the seat), so the gate now reads the built artifact. The source's
comments are a follow-up for the CTO's round-3 analysis, not a precondition of this act: a third source file would
re-open a signed act's bound. No other change to the act or its criteria.

**AMENDMENT 4 (2.0.0_SA_COO~B1, on the seat's STOP at plan, row D1-S12, msg 3621; the CTO's ADDENDUM 1 @d1fe697698, msg
3631):** the plan names a fourth change, `aws_wafv2_web_acl.opal_cloudfront_protection`, the distribution's dependency:
three Count-mode managed groups' `version` `""` to `null` (measured by the seat from the plan JSON: 6 rules before and
after, three identical, no non-rule attribute differs). Both halves of the pair addendum are files at HEAD and the CTO
half reads SIGNED, so step 3's permitted set, step 2's rollback record and step 5's read-back carry the rider, and AC4 reads
that the three Count groups stay Count (3 rules with an override action of Count). Two placeholders join
(`WAF_ACL_NAME`, `WAF_ACL_ID`, read by the seat at step 2). The CTO's conditions are step 5's. Gate limb: GATE viii read
`<placeholders>` at HEAD (four tokens) and the two new tokens are each carried by AC4's invocation.

**AMENDMENT 5 (2.0.0_SA_COO~B1, on the executor's report, row D1-S13, msg 3635):** the signed apply ran at 07:53Z and
both `lambda:UpdateFunctionCode` calls returned 403: `DenyProtectedFunctions` on the Dell group names the two functions
(rule b of `protected_functions.json`, lambda-at-edge). Live is unchanged (ETag, 10 associations, versions 26 and 5, ACL
byte-identical) but the Terraform state holds the new artifact versions, so a plan reads the functions clean over old
live code. The order's comp-iam line is corrected (the wrong grain was the issuer's). Step 2a is added: reconcile the
state first. Which identity applies is NOT decided here: the deny is CT-a-1's and Andrew's, and the question is with
`1.0.0_SA_CTO~DELL1`; the order stays open and no retry is authorized by this amendment.

**AMENDMENT 6 (2.0.0_SA_COO~B1, on the CTO's ADDENDUM 2 @30bdd99110, msg 3639; the Dell executor's measure msg 3641):** the act is applied by a non-Dell identity; no exception is sought for a Dell one. `<issued_to>` moves from the dell1 lane `~FB1` to a fresh laptop CloudOps lane `~FBL` (one project per Tier-2 seat instance; the laptop MSTR measured `~CTL` and `~ANL` encumbered, msg 3642), whose proof instance is its own. Step 0b is the CTO's grain: the identity read on the two qualified function ARNs, before any write. Step 0c is the checkout gate (the laptop box was 78 commits behind at 08:0xZ). Step 2a is replaced by what the Dell executor measured: a refresh-only reconcile moves nothing and is not performed. The pair, both addenda (the WAF rider), the plan's permitted set, both branches, the oracle (the CTO's exercised read at `Deployed`) and AC1-AC4 are UNCHANGED. The dell1 executor's entry for the refused apply closes as NOT APPLIED. Gate limb: the `<issued_to>`, `<slot>` and `<paths>` of a non-terminal order are amended by its issuer; no criterion changed and the six placeholders are carried as before.

**AMENDMENT 7 (2.0.0_SA_COO~B1, on the laptop actor's report XB-20261011T083249Z-0565, row ADVI_FIRMBKTS-S12):** the act
applied at 08:21Z-08:23Z (router 27 x5, guard 6 x5, CodeSha256 equal to the built artifacts, the ACL's 6 rules identical,
three groups Count, default Allow, LockToken unchanged); the issuer re-read each live (router 27 and guard 6 hashes,
5 + 5 associations, ACL LockToken and default action). AC4's invocation was the issuer's defect: JMESPath reads an empty
object `{}` as false, so `[?OverrideAction.Count]` returns 0 on a rule whose Count override is `{}`. The corrected query
`[?OverrideAction.Count!=`null`]` returns 3 against the live ACL (and the defective form returns 0: both read by the
issuer). The expect is unchanged (`^3$`). The post-apply plan's one ACL change is ruled in the COO half's ADDENDUM 2
(`ledger/NEVER_WIDEN_ROUND3_ACT1_ADVTENANT_COO_HALF_ADDENDUM_2.md`); the CTO's condition 4 is the CTO's to rule. Gate
limb: a criterion's invocation amended on a non-terminal order by its issuer; GATE viii read the six placeholders at HEAD
and the corrected invocation still carries `<WAF_ACL_NAME>` and `<WAF_ACL_ID>`.

**AMENDMENT 8 (2.0.0_SA_COO~B1, after the CTO's oracle read, ledger `NEVER_WIDEN_ROUND3_ACT1_ADVTENANT_CTO_HALF.md` ADDENDUM 3
@8ad3ddd43f):** the CTO read Branch A (router v27 equals v26 on 8 of 8 events, guard v6 equals v5 on 4 of 4, associations exact,
a live no-session request reads 401, the deployed bytes ASCII) and WAIVED condition 4 for the WAF ACL's `version` churn only.
Nothing further blocks the close: run AC1-AC4 (AC4 as amended), write the instance, close the change-management entry with
the three outputs and the CTO's read, and flip `<status>` to `complete` in the same commit.

**ISSUER NOTES:** class WORLD. Un-park conditions, all satisfied at this amendment: `FB-f-7` complete (@e6ec8ce6e4); phase A
merged (@acf8a16706); the pair SIGNED in both halves (@d30c5fe203); the actor's entry is opened by the actor before any
write (step 1). Not in this act: the staged `FB-f-9` (producers' mode), `FB-f-10` (delta copy), `FB-f-11` (list entry, map
value, F6 deploy). The window's order puts this act first and it changes nothing a user can see.

<status>complete</status>
<round>3</round>
<to_id>ADVI_FIRMBKTS.TO-FB-f-8</to_id>
<slot>~FBL</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
