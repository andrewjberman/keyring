# ADVI_FIRMBKTS task order -- `FB-f-8` -- WINDOW ACT 1: DEPLOY THE advTenant BUILD (shared-advisor-router and shared-advisor-router-response)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R3.md</decomp_doc>
<owned_cells>FB-f-8</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~17</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>ROUTER_VERSION, GUARD_VERSION, ROUTER_SHA256, GUARD_SHA256, ROUTE_FETCH_CHECK</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, rule, schedule or cadence is added or changed.
comp-iam: RUN by the issuer -- iam:SimulatePrincipalPolicy on user/cloudops-dell1-agent-user reads allowed for lambda:PublishVersion, lambda:UpdateFunctionCode, lambda:GetFunctionConfiguration, cloudfront:GetDistributionConfig and cloudfront:UpdateDistribution (5 of 5, resource *); the role the Terraform apply runs under is read by the amendment. No grant is created.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut -- every criterion names a value that exists only after the act (a version, a hash, a second manifest) or a check the amendment writes; at the cut each reads FAIL by construction. The amendment writes each scripted check, dry-runs it at the base and tests it against a mutant BEFORE the GO.
EGRESS CLASS, declared: NONE.
</preflight>

## 0. THIS ORDER IS STAGED. IT IS NOT A SPAWNABLE FACE UNTIL THE ISSUER'S AMENDMENT SAYS SO.

Un-park conditions, all required, each read from a file at HEAD:
1. `FB-f-7` is `complete`, its proof instance VALID, and its commit merged.
2. The never-widen pair for this act exists and reads SIGNED in both halves:
   `org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/NEVER_WIDEN_ROUND3_ACT1_ADVTENANT_COO_HALF.md` and `..._CTO_HALF.md`. A half
   names the act's BLAST RADIUS (what it may touch and the rollback per key), reads the new behavior's expected outcome
   from the build's own rule, and covers BOTH branches.
3. The actor's change-management entry for this act is OPEN (`python .tools/deploy_ledger.py open ...`), committed with its
   `.open_deploys/` sentinel BEFORE the first act.
4. The issuer's amendment commit fills the five placeholders' meaning (section 4), names the executor, and sets
   `<status>pending</status>`.

## 1. THE CELL -- `FB-f-8` (round 3, enrichment item 1, step 1)

Deploy the two edge functions `FB-f-7` built, as one act: `shared-advisor-router` and `shared-advisor-router-response`,
through Terraform only (`infra/aws/terraform/portal-auth/lambda-edge.tf`, `safe-apply`, never `aws lambda
update-function-code`). The deploy moves every CloudFront behavior that carries them, for every partner firm; the build is
dormant by construction (`FB-f-7` AC3: every decision equals today's), so no request changes. Steps, and the traps the
2026-08-21 act recorded (`org/tier2_senior/0.7.0_AE_CloudOps/logs/2026-08-21/session_1531-1712Z_p4r3_route_act.md`):
1. Open the change-management entry first (condition 3).
2. Build both zips with the repository's `build-nodejs-lambda.sh`, upload the artifacts the `aws_s3_object` data sources
   read, and read the plan's JSON: the function resource MUST change and `aws_cloudfront_distribution` MUST update the
   association. A plan that publishes a version while the distribution reads NO-OP is the `qualified_arn` pin defect: STOP.
3. Apply through `safe-apply`. Read back the live association's version per behavior and the function's `CodeSha256`.
4. Make the exercised fetch through the page's own route (section 4, `ROUTE_FETCH_CHECK`): the firm's own tenant, the
   declared alias and the staff proxy are served; a foreign tenant is refused 401; the guard does not 502.
5. A post-apply plan reads no changes. Close the entry with the evidence.

## 2. BOUNDS

1. The only writes are the artifact objects the Terraform data sources name, the Terraform apply of the two functions and
   their distribution association, and the ledger. No policy, bucket, schedule or other function changes; no second apply.
2. If the plan or the live read differs from the pair's blast radius: STOP before the apply and file a BLOCKING row.
3. Rollback is the previous published version of each function re-associated through Terraform, named in the pair.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~17/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

(The amendment adds the Terraform paths and the executor's worktree. The `.tf` files are read by `safe-apply`; they do
not change in this act unless the plan says the pin must drop, which is a STOP.)

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~17/ADVI_FIRMBKTS.TO-FB-f-8.act1-deploy-advtenant.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-f-8"><invocation>.tools/aws lambda get-function-configuration --function-name shared-advisor-router --qualifier <ROUTER_VERSION> --region us-east-1 --query CodeSha256 --output text</invocation><expect><ROUTER_SHA256></expect></criterion>
  <criterion id="AC2" cell_refs="FB-f-8"><invocation>.tools/aws lambda get-function-configuration --function-name shared-advisor-router-response --qualifier <GUARD_VERSION> --region us-east-1 --query CodeSha256 --output text</invocation><expect><GUARD_SHA256></expect></criterion>
  <criterion id="AC3" cell_refs="FB-f-8"><invocation><ROUTE_FETCH_CHECK></invocation><expect>ROUTE CHECK: own tenant 200, alias 200, staff proxy 200, foreign tenant 401, guard 502 count 0</expect></criterion>
</proof_of_spec>

Placeholders at the amendment: `ROUTER_VERSION` and `GUARD_VERSION` are the published Lambda versions the apply reads back;
`ROUTER_SHA256` and `GUARD_SHA256` are the build artifacts' `CodeSha256`; `ROUTE_FETCH_CHECK` is one issuer-written
script, dry-run at the base before the GO, that makes the five exercised requests through the page's route and prints the
one result line.

## 5. WHEN YOU ARE DONE

Close the change-management entry with the three outputs; flip `<status>` to `complete` in the SAME commit as the proof
instance; report once: the pair's two blob ids, the plan's resource summary, the live associations per behavior, the three
outputs, the post-apply plan line, the entry's path and the commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** staged. Class WORLD: a deploy of a shared function. The CTO's round-2 analysis item 1 names this step
and orders it first ("the advTenant remedy lands first": `_shared/firm-config.mjs` header). The executor is the amendment's
call: the same lane that did the 2026-08-21 act is `0.7.0_AE_CloudOps` (a lane on this project needs seating). The
`ROUTE_FETCH_CHECK` needs sessions for a firm, its alias and the staff proxy; if none can be obtained, the amendment says
so and the CTO's exercised read is the oracle (as in 2026-08-21's "exercised fetch").

<status>staged</status>
<round>3</round>
<to_id>ADVI_FIRMBKTS.TO-FB-f-8</to_id>
<slot>~17</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
