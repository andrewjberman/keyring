# TO POSN_ASTTAX.TO-V2-1 -- EMIT `holdings.json` beside `registry.json`: per satellite, ONE total weight per ticker from Black Diamond summed across sleeves, labelled from the served ETFClassifier table; re-deploy the producer through Terraform (AT5-s-2, B2; FWD-1/FWD-2 on the Satellites mode)

<to_id>POSN_ASTTAX.TO-V2-1</to_id>
<project>POSN_ASTTAX</project>
<issued_to>0.9.0_WK_POSN_ASTTAX~20</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-14</issued_date>
<status>staged</status>

**Directive:** D4 - **Macro:** POSN - **Fabric:** site-z - **PRD:** `../prd/POSN_ASTTAX_PRD.md` **v0.7** @`99cc431075`
(C-SATELLITE-SOURCE) - **Decomp cell:** `AT5-s-2` - **Issuance:** round 5, wave 1. **GATES `AT5-s-4` (B4), `AT5-s-7` (F3), `AT5-s-8` (R1).**

---

## IDENTITY AND THE FIRST ACT

You are `0.9.0_WK_POSN_ASTTAX~20`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_POSN_ASTTAX~20;`. First act:
`git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; a missing tree is a BLOCKING row and your
final report. Commit only via `bash .tools/safe-commit.sh --author "0.9.0_WK_POSN_ASTTAX~20 <0.9.0_WK_POSN_ASTTAX~20@opal.agent>"
-F <msgfile> -- <paths>`, msgfile by the Write tool, PURE ASCII. Never push, merge, rebase, `checkout --`, `clean`.

## THE CELL

Andrew ~17:2xZ: *"they should be summed ... it is to see total GLD listed as Commodity Asset, Metals Sub-Asset, and to see Total
VXX ... as Structured Asset, Hedge Sub-Asset."* Measured by `4.0.0_SA_CRO~Z` (81 rebalancer files, 2026-09-14): every Opal
Satellite has 0 securities at its root; GLD/VXX sit inside Black Diamond's copy of each model; the portal blends YANG's copy and
loses them (wrong on gold for 7 of 9 satellites).

**The producer today:** the trigger `infra/aws/lambda/cot-pipeline/cot-satellites-registry-producer/lambda_function.py` (128 lines)
vendors the REAL producer `data/assets/scripts/gold/build_satellites_registry.py` out of git at a REQUIRED `--pin`
(`build_package.py`, repo-mirroring layout; read its header before touching the member list). `build_books` (`:158-198`) reads
`DETAIL_KEY = "blackdiamond/cottonwood/bronze/rebalancer_model_detail/%s/%s.json"` (`:91`) from `opal-data-assets`; `publish`
(`:223-234`) writes `platinum/satellites/registry.json` (`:92`) to `opal-data-cot`. `satellites_registry.py` beside it is a
CONFORMANCE ORACLE that "never decides" and **MUST NOT be converted** -- if a holdings oracle is needed, it is a sibling.
Scheduled `cron(0 7 * * ? *)` UTC, 59 minutes after the measured 06:00:43Z upstream landing.

**Your act, in order:**
1. Extend the producer (or add a sibling `build_satellites_holdings.py` -- the build ladder says EXTEND; state which and why) so
   the same scheduled run ALSO publishes `platinum/satellites/holdings.json`:
   ```
   {as_of, source, claim: "measured",
    satellites: {<code>: {holdings: [{ticker, weight, asset_class, sub_asset_class, sleeves: [{book, weight}]}],
                          coverage: {labelled: n, unlabelled: m}}}}
   ```
   `weight` = the SUM of `absoluteAllocation` across the satellite's sleeves for that `metadata.symbol` (BD's figure; **Yang's
   copy is NEVER added** -- LT VXX reads 1.87, not 3.37). `asset_class` / `sub_asset_class` come from the served DynamoDB table
   `etf-classifications` through `infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py` (vendored by PIN in
   `build_package.py`, never a copy). A ticker with no row carries `asset_class: null`, `sub_asset_class: null` and is COUNTED in
   `coverage.unlabelled` -- never guessed, never dropped. Today the table still serves the PRE-retag labels (GLD `hedge`/`Gold`);
   that is CORRECT for this cell -- R1 changes the table later and your artifact follows on its next fire with no code change.
2. `infra/aws/terraform/cot-pipeline/satellites-registry-producer.tf`: a SECOND pinned `s3:PutObject` resource
   (`arn:aws:s3:::${local.cot_bucket}/platinum/satellites/holdings.json` -- the key, never the prefix) and a `dynamodb:GetItem` +
   `dynamodb:BatchGetItem` statement on the `etf-classifications` table ARN; re-measure `memory_size`/`timeout` from a local dry
   run (the file's own comment forbids inherited numbers); MIRROR the cross-firm deny, never widen it.
3. Build (`build_package.py --pin <your commit>`), plan, `safe-apply`, 0-diff, ledger.
4. Prove the artifact ON DEMAND with a QA invocation, then prove the SCHEDULE is the standing mechanism.

### THE TWO HALVES

Read `org/missions/D4/POSN/POSN_ASTTAX/ledger/NEVER_WIDEN_ROUND5_COO_HALF.md` (@`f381f6f402`) and `.../NEVER_WIDEN_ROUND5_CTO_HALF.md`
(@`af667548d1`) before the first command. `registry.json`'s PAYLOAD must be content-identical for the same partition after your
deploy (both halves say so); the rollback is the artifact bucket VersionId `qXzZE63fhPXwG2dXU86eLbTh48cFn0vQ`. A deploy leg
reached without both halves at HEAD is refused with a row.

### REFUSAL CLAUSE

A criterion you cannot satisfy as written is REFUSED with its measurement, never repaired, widened or satisfied by another route.

## SURPRISE ROWS

ONE row per off-cell finding, `POSN_ASTTAX-Z-W20-S<k>`, appended to
`org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/investigations/INVESTIGATION_v1.md`; keep working.

## CRITERIA -- structured, one clause each

<criterion id="V2-AC1" cell_refs="AT5-s-2"><invocation>timeout 60 git ls-tree HEAD -- org/missions/D4/POSN/POSN_ASTTAX/ledger/NEVER_WIDEN_ROUND5_COO_HALF.md org/missions/D4/POSN/POSN_ASTTAX/ledger/NEVER_WIDEN_ROUND5_CTO_HALF.md</invocation><expect>both blobs listed. Absent either: STOP, row.</expect></criterion> `V2-AC1` -- THE HALVES ARE AT HEAD.

<criterion id="V2-AC2" cell_refs="AT5-s-2"><invocation>timeout 120 python .tools/deploy_ledger.py open --slug posn-round5-b2-satellites-holdings --title "POSN_ASTTAX B2: cot-satellites-registry-producer emits holdings.json beside registry.json" --author 0.9.0_WK_POSN_ASTTAX~20 --leg "L1|git|SITEZ commit of producer + trigger + build_package + tf|hash" --leg "L2|s3-prefix|opal-313476888478-lambda-artifacts cot-pipeline/cot-satellites-registry-producer.zip|sha256" --leg "L3|verify|plan scoped|summary" --leg "L4|activation|safe-apply|summary" --leg "L5|verify|0-diff|No changes" --leg "L6|verify|QA invocation lands holdings.json|s3api head + content read" --leg "L7|verify|schedule enabled with the function as target|describe-rule + list-targets" --leg "L8|verify|next scheduled 07:00Z fire lands holdings.json organically (the negative arm; recorded by the COO, not waited on here)|s3api head after the fire"</invocation><expect>the entry path printed with 8 legs OPEN, opened before any code change. L8 is the ORGANIC arm and is NOT yours to wait on: you close L1-L7 and leave L8 OPEN by design, named in your report.</expect></criterion> `V2-AC2` -- THE LEDGER, WITH THE ORGANIC ARM NAMED AS NOT-A-WAIT.

<criterion id="V2-AC3" cell_refs="AT5-s-2"><invocation>timeout 180 bash .tools/commit-gate.sh</invocation><expect>clean on every changed .py and .tf, output cited, both ASCII limbs read. `git diff --stat -- data/assets/scripts/gold/satellites_registry.py` reads 0 lines (the oracle untouched).</expect></criterion> `V2-AC3` -- THE CODE, GATED; THE ORACLE UNTOUCHED.

<criterion id="V2-AC4" cell_refs="AT5-s-2"><invocation>timeout 600 python <LOCAL_DRY_RUN_HOLDINGS></invocation><expect>nine satellites; for `Opal Satellite 15` the GLD row reads weight 8.34 with one sleeve (ST 8.34); for `Opal Satellite 30` GLD reads 7.25 with sleeves ST 6.26 + INT 1.00 (the CRO's measured example); every ticker appears ONCE per satellite; `asset_class`/`sub_asset_class` equal the table's CURRENT served values (GLD: hedge / Gold today) -- never a value the table does not serve; `coverage.labelled + coverage.unlabelled` equals the row count per satellite. Print the nine coverage pairs.</expect></criterion> `V2-AC4` -- THE ARTIFACT'S ARITHMETIC AND LABELS, EXERCISED LOCALLY FIRST.

<criterion id="V2-AC5" cell_refs="AT5-s-2"><invocation>timeout 300 python <NEGATIVE_CONTROL_SAME_BUILDER></invocation><expect>LT VXX would read 3.37 (1.87 + 1.50) under the summed-both-sources arm, and reads 1.87 under your builder -- the two arms DIFFER, proving the builder does not add Yang's copy. If both arms read the same, the control is not discriminating: say so and do not report the result.</expect></criterion> `V2-AC5` -- YANG NEVER ADDED, PROVED BY THE ARM THAT WOULD ADD IT.

<criterion id="V2-AC6" cell_refs="AT5-s-2"><invocation>timeout 600 python infra/aws/lambda/cot-pipeline/cot-satellites-registry-producer/build_package.py --pin <COMMITTED_HASH></invocation><expect>the zip built from GIT at your pin (never the working tree); its member list printed and includes data/assets/scripts/gold/&lt;your builder&gt;.py and infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py at the repo-mirroring layout; a deliberately WRONG pin (a moving ref) is REFUSED by the builder (its own control).</expect></criterion> `V2-AC6` -- THE PACKAGE, FROM GIT AT A PIN.

<criterion id="V2-AC7" cell_refs="AT5-s-2"><invocation>timeout 300 comp-iam gaps</invocation><expect>the new .tf statements resolve: the second PutObject key and the DynamoDB read on etf-classifications are GRANTED to cot-satellites-registry-producer-role; no wildcard resource introduced; the cross-firm deny still present; the tool's DESIRED-plane caveat quoted (it cannot see APPLIED).</expect></criterion> `V2-AC7` -- THE GRANTS, ON THE DESIRED PLANE, NARROW.

<criterion id="V2-AC8" cell_refs="AT5-s-2"><invocation>timeout 600 terraform -chdir=infra/aws/terraform/cot-pipeline plan -target=module.cot_satellites_registry_producer -target=aws_iam_role_policy.cot_satellites_registry_producer_s3 -out=.scratch/b2.tfplan</invocation><expect>0 to add, exactly 2 to change (the function's artifact version, the s3 policy), 0 to destroy; any other resource is a STOP with a row.</expect></criterion> `V2-AC8` -- THE PLAN, SCOPED.

<criterion id="V2-AC9" cell_refs="AT5-s-2"><invocation>timeout 900 .tools/safe-apply.sh -chdir=infra/aws/terraform/cot-pipeline apply .scratch/b2.tfplan</invocation><expect>Apply complete! Resources: 0 added, 2 changed, 0 destroyed; the HALTGT checkpoint output pasted.</expect></criterion> `V2-AC9` -- THE APPLY.

<criterion id="V2-AC10" cell_refs="AT5-s-2"><invocation>timeout 600 terraform -chdir=infra/aws/terraform/cot-pipeline plan -target=module.cot_satellites_registry_producer -target=aws_iam_role_policy.cot_satellites_registry_producer_s3</invocation><expect>No changes.</expect></criterion> `V2-AC10` -- 0-DIFF.

<criterion id="V2-AC11" cell_refs="AT5-s-2"><invocation>timeout 300 .tools/aws lambda invoke --function-name cot-satellites-registry-producer --payload '{}' .scratch/b2_invoke.json</invocation><expect>StatusCode 200 and the response body naming both keys written; then `s3api head-object` on platinum/satellites/holdings.json returns 200 with an `as_of` of 2026-09-14 inside the body, and `registry.json`'s body is CONTENT-IDENTICAL to its pre-deploy version `sDM2rbJ.m2yyArr8utwAaleSJyntdVbj` for the same partition (diff printed, empty). This is the ON-DEMAND proof; it is QA, never production evidence.</expect></criterion> `V2-AC11` -- THE MECHANISM DRIVEN DELIBERATELY: THE KEY EXISTS BECAUSE YOU MADE IT EXIST.

<criterion id="V2-AC12" cell_refs="AT5-s-2"><invocation>timeout 120 .tools/aws events describe-rule --name cot-satellites-registry-producer-daily --query '{state:State,expr:ScheduleExpression}' --output json</invocation><expect>State ENABLED, ScheduleExpression cron(0 7 * * ? *); then list-targets-by-rule names the function ARN. The SCHEDULE is the standing mechanism; the organic fire is ledger leg L8, recorded by the COO after 07:00Z tomorrow, NOT waited on by you.</expect></criterion> `V2-AC12` -- THE SCHEDULE, MEASURED, NOT ASSUMED.

<criterion id="V2-AC13" cell_refs="AT5-s-2"><invocation>timeout 300 bash infra/aws/lambda/ci/record-resource-deploy.sh cot-pipeline</invocation><expect>the deploy recorded per that script's contract (if this pipeline is recorded by record-terraform-deploy.sh instead, run that with --plan .scratch/b2.tfplan and say so); legs L1-L7 closed with proofs; L8 left OPEN by design and named.</expect></criterion> `V2-AC13` -- RECORDED; L8 OPEN ON PURPOSE.

<criterion id="V2-AC14" cell_refs="AT5-s-2" judgment="true"><invocation>JUDGMENT -- no invocation; graded at L9</invocation><expect>Whether holdings.json's per-ticker totals are what an analyst would call "what the satellite holds" -- the sleeve sum, nothing added, nothing dropped -- and whether coverage.unlabelled is disclosed where it should be. Record the readings and offer NO verdict.</expect></criterion> `V2-AC14` -- **JUDGMENT, GRADED BY `3.0.0_SA_CVO~Z` AT L9.**

<expected_criteria>V2-AC1, V2-AC2, V2-AC3, V2-AC4, V2-AC5, V2-AC6, V2-AC7, V2-AC8, V2-AC9, V2-AC10, V2-AC11, V2-AC12, V2-AC13, V2-AC14</expected_criteria>

<placeholders>COMMITTED_HASH, LOCAL_DRY_RUN_HOLDINGS, NEGATIVE_CONTROL_SAME_BUILDER</placeholders>

<paths>
org/missions/D4/POSN/POSN_ASTTAX/task-orders/POSN_ASTTAX.TO-V2-1.holdings-json-beside-registry-json.md
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~20/
org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/investigations/INVESTIGATION_v1.md
data/assets/scripts/gold/build_satellites_registry.py
data/assets/scripts/gold/build_satellites_holdings.py
infra/aws/lambda/cot-pipeline/cot-satellites-registry-producer/lambda_function.py
infra/aws/lambda/cot-pipeline/cot-satellites-registry-producer/build_package.py
infra/aws/terraform/cot-pipeline/satellites-registry-producer.tf
infra/aws/terraform/cot-pipeline/CHANGELOG.json
infra/aws/lambda/ci/lambda-source-map.json
org/critical_paths/change_management/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D4/POSN/POSN_ASTTAX/decompositions/POSN_ASTTAX_DECOMP_round5.md</decomp_doc> round 5, cell `AT5-s-2`.
<owned_cells>AT5-s-2</owned_cells>
Read-dependencies, NOT claimed: none upstream. DOWNSTREAM: `AT5-s-4` (B4) reads holdings.json and its schema; `AT5-s-7` (F3)
binds the schema; `AT5-s-8` (R1) reads the served key. Your schema line is inlined into their faces verbatim -- do not change it
after your commit without a row.
</decomp_ref>

<preflight>
comp-schedule: RUN at the cut -- 2 armed gates, neither POSN; 7 open ledger entries; the NEVER clauses bind: safe-apply only,
never-widen (halves at HEAD), no monitor, publish-the-empty-never-delete.
comp-iam: RUN -- 474 .tf files scanned, 404 policy blocks attached, 26 NOT ATTACHED, deny overlay 2 unparsed; BLIND on this producer: 0 boto3 call sites in the trigger (the logic is vendored by pin), so its verdict is computed from nothing. V2-AC7 grades the .tf on the DESIRED plane and V2-AC11 exercises the grant on the APPLIED plane.
comp-adversary: RUN on the decomposition. NOT covered, stated: (1) the issuer has not measured the producer's runtime with a
DynamoDB read added -- V2's memory/timeout re-measure is the first; (2) the issuer has not confirmed `build_package.py`'s member
grammar admits a `_shared/` path -- read its header; a refusal is a row, not a workaround; (3) the sleeve-sum equals BD's own
per-satellite figure is the CRO's claim on 81 files, exercised by V2-AC4 on the live partition.
</preflight>

<proof_of_spec>
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~20/POSN_ASTTAX.TO-V2-1.holdings-json-beside-registry-json.proof_of_spec.json
</proof_of_spec>
