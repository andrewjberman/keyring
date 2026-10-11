# ADVI_FIRMBKTS task order -- `FB-f-8` -- WINDOW ACT 1: DEPLOY THE advTenant BUILD (shared-advisor-router and shared-advisor-router-response) -- PHASE B, THE DEPLOY

<!-- ===================== WORKER FACE -- this is the WHOLE of the actor's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R3.md</decomp_doc>
<owned_cells>FB-f-8</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~FB1</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>ROUTER_VERSION, GUARD_VERSION, ROUTER_SHA256, GUARD_SHA256</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, rule, schedule or cadence is added or changed.
comp-iam: RUN by the issuer -- iam:SimulatePrincipalPolicy on user/cloudops-dell1-agent-user reads allowed for lambda:PublishVersion, lambda:UpdateFunctionCode, lambda:GetFunctionConfiguration, cloudfront:GetDistributionConfig and cloudfront:UpdateDistribution (5 of 5, resource *). The role the Terraform apply runs under is read by the actor at step 2 (this order's `safe-apply` is the path; a refusal there is a STOP).
comp-adversary: RUN by the issuer -- the build is `TO-FB-f-7` (merged @e6ec8ce6e4) with `TO-FB-f-8` phase A (merged @acf8a16706): router gate 51 pass, guard suite 46 pass, dormancy grid router 88 of 88 and guard 396 of 396 identical to base, both files 0 non-ASCII bytes. The three criteria below read FAIL at base by construction (no new version exists).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE ACT -- `FB-f-8` phase B (round 3, enrichment item 1, step 1 of the cutover window)

You deploy two Lambda@Edge functions as ONE act, through Terraform only: `shared-advisor-router` (live version 26) and
`shared-advisor-router-response` (live version 5), each associated on 5 behaviors of CloudFront distribution
`EVTSA9VEHNZVH`. The build is dormant: for the registry as it stands every decision is identical to today's, so no
request changes. The act is signed by the never-widen pair
`org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/NEVER_WIDEN_ROUND3_ACT1_ADVTENANT_COO_HALF.md` and `..._CTO_HALF.md` (the CTO
half SIGNED @d30c5fe203); the pair's permitted set and both branches are the whole of what you may touch and when you
stop. READ BOTH HALVES FIRST, and `org/tier2_senior/0.7.0_AE_CloudOps/logs/2026-08-21/session_1531-1712Z_p4r3_route_act.md`
(the last deploy of both functions: its three defects are the traps below). Procedure: `docs/deployment/
LAMBDA_DEPLOYMENT_PROTOCOL.md`, `docs/deployment/TERRAFORM_PROTOCOL.md`, `docs/deployment/cloudfront_deployment_checklist.md`
and `cloudfront_rollback_plan.md`; load `/cloud-ops` before any AWS or Terraform act.

### 1a. The steps, in order

0. **Gate.** `git ls-tree HEAD` must list BOTH pair halves; the CTO half's verdict line must read SIGNED; the repository's
   router and guard sources must read 0 non-ASCII bytes (`FB-f-8` phase A merged). If any is not so: STOP, a BLOCKING row,
   no write to AWS.
1. **The entry.** Open the change-management entry BEFORE the first act: `python .tools/deploy_ledger.py open ...` (read its
   `--help`), naming the two functions, the distribution, all 10 associations, the previous versions (26 and 5) as the
   rollback, and the pair. Commit the entry and its `org/critical_paths/.open_deploys/` sentinel first.
2. **Read before you write.** Save the live `get-distribution-config` (ETag and the 10 associations) into the entry as the
   rollback record. Confirm the live router is version 26 and the guard version 5 on 5 behaviors each. Build both
   artifacts with the repository's `build-nodejs-lambda.sh` from the merged tree; record each artifact's SHA-256
   (`ROUTER_SHA256`, `GUARD_SHA256`: the `CodeSha256` the published version must read).
3. **Plan.** Run the Terraform plan of `infra/aws/terraform/portal-auth/` through the repository's wrapper and read the
   plan JSON. It must change EXACTLY the two functions (each a new published version) and the distribution's 10
   associations, nothing else. A plan that publishes a version while `aws_cloudfront_distribution` reads NO-OP is the
   `qualified_arn` pin defect: STOP. A plan naming any other resource, or drift outside the act: STOP.
4. **Apply** through `safe-apply` only (never a bare `terraform apply`, never `aws lambda update-function-code`). Wait for
   the distribution to read `Deployed`.
5. **Read back.** Each of the 10 associations reads the new version; `CodeSha256` of each new version equals the artifact's;
   a post-apply plan reads no changes. Record the two new version numbers (`ROUTER_VERSION`, `GUARD_VERSION`).
6. **Oracle.** Send ONE message to `1.0.0_SA_CTO~DELL1` at `Deployed`, naming the entry and the two versions: the CTO
   invokes both new versions on the 5 event classes against base, makes one live no-session request (401 expected) and
   diffs the associations. Do not close the entry before the CTO's read.
7. **Criteria and close.** Run AC1-AC3, write the proof instance in your own deliverables folder, close the entry with the
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
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

(The Terraform files under `infra/aws/terraform/portal-auth/` are read by the plan; they do not change in this act unless
the plan says a pin must drop, which is a STOP. The build artifacts are not committed.)

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/ADVI_FIRMBKTS.TO-FB-f-8.act1-deploy-advtenant.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-f-8"><invocation>.tools/aws lambda get-function-configuration --function-name shared-advisor-router --qualifier <ROUTER_VERSION> --region us-east-1 --query CodeSha256 --output text</invocation><expect><ROUTER_SHA256></expect></criterion>
  <criterion id="AC2" cell_refs="FB-f-8"><invocation>.tools/aws lambda get-function-configuration --function-name shared-advisor-router-response --qualifier <GUARD_VERSION> --region us-east-1 --query CodeSha256 --output text</invocation><expect><GUARD_SHA256></expect></criterion>
  <criterion id="AC3" cell_refs="FB-f-8"><invocation>.tools/aws cloudfront get-distribution-config --id EVTSA9VEHNZVH --query "DistributionConfig.CacheBehaviors.Items[*].LambdaFunctionAssociations.Items[*].LambdaFunctionARN" --output text</invocation><expect>shared-advisor-router:<ROUTER_VERSION></expect></criterion>
</proof_of_spec>

AC1 and AC2 read each published version's hash against the built artifact's (the pair's measure). AC3 reads the live
associations: five behaviors carry the router at the new version and five carry the guard (a bounded read of one
distribution). The criteria in the proof block of phase A (AC1-AC4 of the first face: non-ASCII 0 and 0, router gate 51
pass, guard 46 pass, dormancy grid 0 and 0) are CLOSED at `acf8a16706` and are cited, not re-run, by this act.

## 5. WHEN YOU ARE DONE

Close the change-management entry with the three outputs and the CTO's read; flip `<status>` to `complete` in the SAME
commit as the proof instance. A row id on this project carries the dell1 infix and your lane: `ADVI_FIRMBKTS-D1-W<slot>-S<k>`
is a worker form; as a seat you file `ADVI_FIRMBKTS-D1-S<k>` with the next unused `k`, `surfaced_at` from `date -u
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

**ISSUER NOTES:** class WORLD. Un-park conditions, all satisfied at this amendment: `FB-f-7` complete (@e6ec8ce6e4); phase A
merged (@acf8a16706); the pair SIGNED in both halves (@d30c5fe203); the actor's entry is opened by the actor before any
write (step 1). Not in this act: the staged `FB-f-9` (producers' mode), `FB-f-10` (delta copy), `FB-f-11` (list entry, map
value, F6 deploy). The window's order puts this act first and it changes nothing a user can see.

<status>pending</status>
<round>3</round>
<to_id>ADVI_FIRMBKTS.TO-FB-f-8</to_id>
<slot>~FB1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
