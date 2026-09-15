# TO POSN_AGGFIX.TO-A1-1 -- THE FIVE READS THE PRODUCER CHANGE STANDS ON: the gap in Opal's assets-by-model file explained, the writers and readers of the shared file counted, the running producer diffed against its build input, the producer role's two grants simulated, and the two blend constituents checked against a definition (AF1-s-1, AF1-s-2, AF1-s-5, AF1-s-9, AF1-s-17; FWD-4, FWD-6, FWD-7, FWD-8)

<to_id>POSN_AGGFIX.TO-A1-1</to_id>
<project>POSN_AGGFIX</project>
<issued_to>0.9.0_WK_POSN_AGGFIX~1</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-15</issued_date>
<status>staged</status>

**Directive:** D4 - **Macro:** POSN - **Fabric:** site-z - **PRD:** `org/missions/D4/POSN/POSN_AGGFIX/prd/POSN_AGGFIX_PRD.md` **v0.2**
@`cbd85e5cff` (C-GAP-EXPLAINED, C-NEVER-WIDEN, C-FIVE-BOOKS-UNCHANGED, C-MEMBERS) - **Decomp cells:** `AF1-s-1`, `AF1-s-2`, `AF1-s-5`,
`AF1-s-9`, `AF1-s-17` - **Issuance:** round 1, slot `~1`, FIRST of three orders in this slot's queue (then TO-A2-1, then TO-A3-1).
**READ-ONLY ORDER: nothing is built, deployed or written outside your deliverables folder and the channel.**
**AMENDED ~19:5xZ at the partial drain @`11f402ef1e` (issuer cut defects, rows W1-S4 and W1-S2):** `A1-AC2`'s expectation now names the
producer file's TWO put sites (the handler :2623-2630 and `main()`'s `--upload` :2501-2508); `A1-AC6`'s `--query` now selects
`ResourceSpecificResults`. RE-RUN those two criteria only; A1-AC1, A1-AC3, A1-AC4, A1-AC5, A1-AC7, A1-AC8 and A1-AC9 stand as recorded.

---

## IDENTITY AND THE FIRST ACT

You are `0.9.0_WK_POSN_AGGFIX~1`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_POSN_AGGFIX~1;`. Your worktree is
`/c/tmp/wk-aggfix-1-1` (branch `wk-posn_aggfix-1-1`, a sparse cone cut by the COO from SITEZ; do NOT re-create it). First act:
`git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`. Commit ONLY via
`bash .tools/safe-commit.sh --author "0.9.0_WK_POSN_AGGFIX~1 <0.9.0_WK_POSN_AGGFIX~1@opal.agent>" -F <msgfile> -- <paths>` (msgfile by
the Write tool, PURE ASCII). Never push, merge, rebase, `checkout --`, `clean`. Scratch in `/c/tmp/wk-aggfix-1-1/.scratch/` only. Every
AWS read uses the `.tools/aws` shim or boto3 under the box credentials; no secret is needed in this order.

## THE CELLS (verbatim from the decomposition @`605c03f81f`)

**`AF1-s-1` -- the gap between the per-model rows and Opal's own total, explained (S1, C-GAP-EXPLAINED).** Read
`data/mdpf/scripts/gold/dim_mdpf_aum_metrics.py` (MEASURED: `total.model_aum` is the fold's own `model_aua` frontier :27-28, :374, :488,
"NOT sum(by_model)" :457; `by_model` is the fold's per-key frontier :501, cohort `model` only :31-32) and the served
`platinum/mdpf/global/aum-metrics.json` (VersionId at read time printed). Reproduce the gap arithmetically from the file
(`total.model_aum - sum(by_model[].aum)`, the 2026-09-14 figure 8,324,465.16) and from the gold fold input the producer reads, and write
ONE explanation note (what the gap is, measured, and whether it is a defect) to the worker's deliverables; the producer's aggregate file
cites it as `reconciliation.gap_explanation_ref`. A defect is a surprise row naming the MDPF producer's owner; this project edits nothing
there.

**`AF1-s-2` -- writers and readers counted (S2, C-NEVER-WIDEN, C-FIVE-BOOKS-UNCHANGED).** Three censuses, each with its denominator
printed and a positive control: (a) every WRITER of `json/positioning/positioning_data.json` and of `current_holdings.AGG` (L5 read: one,
the producer :2529/:2627; `build_satellites_characteristics.py:142` is a READER); (b) every READER of a book's `aum`
(`current_holdings.<code>.aum`) and of the shared file outside `portal/src/pages/Positioning`, across the repo AND the portal at
`edf85ce503` (L5 read: 32 portal files at PROD, no book-level `aum` reader, type declarations only at `portal-proxy.ts:1113-1114`; the
per-holding `aum` at `HoldingsTab.tsx:966/:1582` is ETF AUM, a different field); (c) every reader of `current_holdings.AGG` (L5 read: the
satellites `yang_index` walks it). A census uses an instrument different from the L5 read.

**`AF1-s-5` -- the running producer against its build input (S5, C-NEVER-WIDEN).** `yang-generate-positioning`'s deployed code
(get-function `CodeSha256`, `LastModified`, and the code bundle's `lambda_function.py` fetched through the function's own code location)
diffed against `lambda_function.py` at the commit `lambda-source-map.json` records as last deployed and against SITEZ HEAD; every commit
between the two on that directory listed. That list is what rides AF1-s-10's deploy.

**`AF1-s-9` -- the producer role already holds what the re-point and the new key need (S9, C-NEVER-WIDEN).** `yang-pipeline-lambda-role`:
`s3:GetObject` on `arn:aws:s3:::opal-data-portal-v2/platinum/mdpf/global/aum-metrics.json` and `s3:PutObject` on
`arn:aws:s3:::opal-data-portal-v2/json/positioning/opal_aggregate.json` both `allowed` by an IAM policy simulation (a different instrument
from the PRD's `comp-iam` read of `iam.tf:34-46`), with a negative control that is `implicitDeny`.

**`AF1-s-17` -- the blend constituents verified (S17, C-MEMBERS).** Find a DEFINITION of `opal_blend_5050_int_ltc` and
`opal_blend_5050_st_int` (a model definition, target-allocation or crosswalk artifact that states constituents, not a name), census with
its denominator, and record CONFIRMED / CONTRADICTED / NO-DEFINITION-FOUND per blend against the standard. CONTRADICTED is a BLOCKING row
(the standard and the PRD bump); NO-DEFINITION-FOUND is recorded with the census and the standard's `inferred` claim stands for the L9
judgment.

**The standard you check against:** `org/standards/POSN_AGGREGATE_MODEL_SET.json` v1.0 (`opal_blend_5050_int_ltc` = INT 0.5 + LT 0.5,
`opal_blend_5050_st_int` = ST 0.5 + INT 0.5, both `claim: inferred`).

**Measured by the issuer at L5 -- read each back, never trust this text:** the served shared file VersionId
`aJ7nhwRKko3H_AMRzsNvvwkf1NiO9aou` (11:06:20Z, `data_as_of` 2026-09-14) carries books UST 52,360,822.93 / ST 129,227,888.01 / INT
444,315,640.92 / LT 804,605,507.26 / ULT 206,634,320.89, each EQUAL to `json/portfolios/aum-metrics.json`'s row (VersionId
`2xsIhWJmoBR96Qy5NzsEpT8ZG5daawKe`, period 2026-07-22) and to NONE of `platinum/mdpf/global/aum-metrics.json`'s rows (VersionId
`OVcFBOpgjFywfYJGYjowX2VSVwLdiyez`, period 2026-09-14). The served objects are gzip-encoded: decompress before parsing. `comp-find
"positioning/positioning_data" --band DEF` returned 17 DEF hits across 61,858 files, two of them code (the producer :2529 and the
satellites script :142), the rest deliverables and the portal proxy :1142.

## YOUR ACT

1. `<GAP_EXPLAIN_A1>`: a script in your deliverables folder that prints the served file's head (VersionId, LastModified) and `period`,
   `total.model_aum`, `sum(by_model[].aum)` and their difference; reads the gold object `dim_mdpf_aum_metrics.py` names as its input for
   that period and prints the fold's `model_aua` frontier and per-key frontiers; reproduces the gap from those inputs; runs the control
   arm (one `by_model` row raised by 1.00 in memory); and writes `AF1_S1_GAP_EXPLANATION.md` beside itself (what the gap is, by
   measurement, and a `DEFECT` or `NOT-A-DEFECT` line with the reason).
2. `<CENSUS_A1>`: one script taking `--writers`, `--book-aum-readers` or `--agg-readers`. Instrument: `git grep -n` over the tracked
   workspace files at your HEAD, and `git -C "/c/Users/Opal Bloomberg/Desktop/ajb_workspace/portal" grep -n <pattern> edf85ce503 -- src`
   for the portal (the portal is NOT checked out in your cone; read its objects from the main tree's portal repo). Each hit is classified
   WRITER / READER / FIXTURE / DELIVERABLE / TYPE-DECLARATION by reading its line; the denominator (files searched) is printed.
3. `<DEPLOYED_VS_SOURCE_A1>`: a script printing get-function-configuration (`CodeSha256`, `LastModified`), the function's code location
   fetched to `.scratch/` and unzipped, the sha256 of its `lambda_function.py` against the same file at the `last_deployed_commit`
   `infra/aws/lambda/ci/lambda-source-map.json` records for `yang-generate-positioning` and against HEAD, and
   `git log --oneline <that commit>..HEAD -- infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/`.
4. `<BLEND_DEFINITION_CENSUS_A1>`: a script printing the census (patterns `opal_blend_5050`, `Opal Blend 5050`, `5050`) over tracked
   files under `data/mdpf/`, `org/standards/`, `lib/`, `integrations/` with its denominator, then for each definition candidate the lines
   that state constituents, then per blend ONE verdict line `CONFIRMED | CONTRADICTED | NO-DEFINITION-FOUND` citing the definition
   path@commit (or S3 key@VersionId).
5. Commit the deliverables, record every criterion, file rows for anything off-cell, keep working.

### REFUSAL CLAUSE

A criterion you cannot satisfy as written is REFUSED with its measurement, never repaired, widened or satisfied by another route.

## SURPRISE ROWS

ONE row per off-cell finding, id `POSN_AGGFIX-Z-W1-S<k>` (start at S1; class OBSERVATION or BLOCKING only; pure ASCII), inside the
fenced json array of `org/missions/D4/POSN/POSN_AGGFIX/surprise-channel/investigations/INVESTIGATION_v1.md` per
`org/surprise_channel/schemas/investigation_item.schema.json` (`project` POSN_AGGFIX, `fabric` site-z, `disposition` UNDER_INVESTIGATION;
`hazard_standing` ARMED needs a `disarm_owner`: use `2.0.0_SA_COO~Z`). Keep working.

## CRITERIA -- structured, one clause each

<criterion id="A1-AC1" cell_refs="AF1-s-1"><invocation>timeout 600 python <GAP_EXPLAIN_A1></invocation><expect>the served file's VersionId and period printed; total.model_aum minus sum(by_model[].aum) printed (8,324,465.16 on the 2026-09-14 file, or the figure the file carries at your read with its period); the same gap reproduced from the gold fold input to within 0.01 with the gold object's key and VersionId printed; AF1_S1_GAP_EXPLANATION.md written carrying a DEFECT or NOT-A-DEFECT line; the CONTROL arm printed, where one by_model row raised by 1.00 moves the computed gap by exactly 1.00.</expect></criterion> `A1-AC1` -- THE GAP, REPRODUCED AND EXPLAINED.

<criterion id="A1-AC2" cell_refs="AF1-s-2"><invocation>timeout 600 python <CENSUS_A1> --writers</invocation><expect>a table of every hit for the shared key json/positioning/positioning_data.json and for current_holdings AGG writes, each classified, with the files-searched denominator for the workspace and for the portal at edf85ce503 printed; a line `WRITERS 2` for the shared key naming the producer file's two put sites -- the Lambda handler's put_object (lambda_function.py:2623-2630, OUTPUT_KEY :2529), which is the positive control, and main()'s --upload put_object (:2501-2508, s3_key_output :2496) -- and no other literal-key writer (the two restore writers that address json/ by prefix are counted by rule in the never-widen halves, row POSN_AGGFIX-Z-S2).</expect></criterion> `A1-AC2` -- THE WRITERS, COUNTED.

<criterion id="A1-AC3" cell_refs="AF1-s-2"><invocation>timeout 600 python <CENSUS_A1> --book-aum-readers</invocation><expect>a table of every reader of a model book's aum (current_holdings.<code>.aum) and of the shared file outside portal/src/pages/Positioning, workspace and portal@edf85ce503, each hit classified, denominators printed, and a `BOOK-AUM READERS <n>` line; per-holding ETF aum hits listed in their own class and excluded from n by reading the line.</expect></criterion> `A1-AC3` -- WHO READS A BOOK'S AUM.

<criterion id="A1-AC4" cell_refs="AF1-s-2"><invocation>timeout 600 python <CENSUS_A1> --agg-readers</invocation><expect>a table of every reader of current_holdings AGG (or of every book of current_holdings, AGG included), workspace and portal@edf85ce503, denominators printed, an `AGG READERS <n>` line, with data/assets/scripts/gold/build_satellites_characteristics.py yang_index present as the positive control.</expect></criterion> `A1-AC4` -- WHO READS THE AGGREGATE BLOCK.

<criterion id="A1-AC5" cell_refs="AF1-s-5"><invocation>timeout 600 python <DEPLOYED_VS_SOURCE_A1></invocation><expect>CodeSha256 and LastModified of yang-generate-positioning printed; the deployed bundle's lambda_function.py sha256 printed EQUAL to the same file at the source map's last_deployed_commit (a difference is printed and filed as a BLOCKING row instead); its diff stat against HEAD printed; the commit list between last_deployed_commit and HEAD on the function's directory printed with its count.</expect></criterion> `A1-AC5` -- THE RUNNING BYTES AGAINST THE BUILD INPUT.

<criterion id="A1-AC6" cell_refs="AF1-s-9"><invocation>timeout 120 .tools/aws iam simulate-principal-policy --policy-source-arn arn:aws:iam::313476888478:role/yang-pipeline-lambda-role --action-names s3:GetObject s3:PutObject --resource-arns arn:aws:s3:::opal-data-portal-v2/platinum/mdpf/global/aum-metrics.json arn:aws:s3:::opal-data-portal-v2/json/positioning/opal_aggregate.json --query "EvaluationResults[].{action:EvalActionName,per_resource:ResourceSpecificResults[].[EvalResourceName,EvalResourceDecision]}" --output json # rail-checked: comp-iam reads the DESIRED policy text; this criterion needs the live policy evaluator</invocation><expect>two action objects, each carrying its per-resource pairs for both ARNs (four pairs printed); the s3:GetObject pair on the platinum aum-metrics ARN reads `allowed` and the s3:PutObject pair on the opal_aggregate ARN reads `allowed`.</expect></criterion> `A1-AC6` -- THE TWO GRANTS, EVALUATED LIVE.

<criterion id="A1-AC7" cell_refs="AF1-s-9"><invocation>timeout 120 .tools/aws iam simulate-principal-policy --policy-source-arn arn:aws:iam::313476888478:role/yang-pipeline-lambda-role --action-names s3:PutObject --resource-arns arn:aws:s3:::opal-data-bd/posn-aggfix-negative-control.json --query "EvaluationResults[].[EvalActionName,EvalResourceName,EvalDecision]" --output text # rail-checked: comp-iam reads the DESIRED policy text; the negative control needs the live policy evaluator</invocation><expect>one result line reading `implicitDeny` (or `explicitDeny`) -- the evaluator can say no. An `allowed` here is recorded as the output and filed as an OBSERVATION row: the role is wider than the PRD read, and A1-AC6 then proves nothing about this project's grant.</expect></criterion> `A1-AC7` -- THE EVALUATOR'S NEGATIVE CONTROL.

<criterion id="A1-AC8" cell_refs="AF1-s-17"><invocation>timeout 600 python <BLEND_DEFINITION_CENSUS_A1></invocation><expect>the census printed with its denominator (files searched per root) and every hit; the lines of each definition candidate that state constituents; exactly two verdict lines, one per blend, each `CONFIRMED`, `CONTRADICTED` or `NO-DEFINITION-FOUND` with the cited definition; the standard's own two names found by the census as the positive control.</expect></criterion> `A1-AC8` -- THE BLEND CONSTITUENTS AGAINST A DEFINITION.

<criterion id="A1-AC9" cell_refs="AF1-s-1,AF1-s-17" judgment="true"/> `A1-AC9` -- **JUDGMENT, GRADED BY `3.0.0_SA_CVO~Z` AT L9:** whether AF1_S1_GAP_EXPLANATION.md EXPLAINS the gap or only reproduces it; and, where a blend reads NO-DEFINITION-FOUND, whether its name-inferred constituents may be served as members. Record the readings and offer NO verdict.

<expected_criteria>A1-AC1, A1-AC2, A1-AC3, A1-AC4, A1-AC5, A1-AC6, A1-AC7, A1-AC8, A1-AC9</expected_criteria>

<placeholders>GAP_EXPLAIN_A1, CENSUS_A1, DEPLOYED_VS_SOURCE_A1, BLEND_DEFINITION_CENSUS_A1</placeholders>

<paths>
org/missions/D4/POSN/POSN_AGGFIX/task-orders/POSN_AGGFIX.TO-A1-1.verify-gap-writers-readers-deployed-bytes-grant-blends.md
org/missions/D4/POSN/POSN_AGGFIX/deliverables/0.9.0_WK_POSN_AGGFIX~1/
org/missions/D4/POSN/POSN_AGGFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D4/POSN/POSN_AGGFIX/decompositions/POSN_AGGFIX_DECOMP.md</decomp_doc> round 1 @`605c03f81f`.
<owned_cells>AF1-s-1 AF1-s-2 AF1-s-5 AF1-s-9 AF1-s-17</owned_cells>
Read-dependencies, NOT claimed: none upstream. DOWNSTREAM: `AF1-s-6`, `AF1-s-7`, `AF1-s-8` (TO-A2-1, your next order) read your gap note,
your census and your blend verdicts; `AF1-s-10` (TO-A3-1) reads your deployed-bytes commit list.
</decomp_ref>

<preflight>
comp-schedule: RUN at the cut (2026-09-15 ~18:3xZ) -- 7 armed gates, 0 POSN; 6 open deploy-ledger entries, 0 POSN; 12 standing NEVER clauses; this order deploys nothing and opens no ledger entry.
comp-iam: RUN -- `comp-iam service yang-generate-positioning` (PRD s.9): 7 operations, 1 GRANTED, 6 UNRESOLVABLE-RESOURCE (runtime bucket/key args); BLIND on those 6; A1-AC6 answers the two resources this project needs by the live evaluator and A1-AC7 is its negative control.
comp-adversary: RUN on the decomposition (5 complement sources run, 4 declared-excluded). NOT covered, stated: (1) the issuer has not read the gold fold input for the 2026-09-14 period, so whether the gap reproduces from it is unknown; (2) no blend definition search has run; (3) the deployed bundle has not been fetched on this device; (4) the portal is not checked out in your cone, so every portal read goes through the main tree's portal repo objects at edf85ce503.
</preflight>

<proof_of_spec>
org/missions/D4/POSN/POSN_AGGFIX/deliverables/0.9.0_WK_POSN_AGGFIX~1/POSN_AGGFIX.TO-A1-1.verify-gap-writers-readers-deployed-bytes-grant-blends.proof_of_spec.json
</proof_of_spec>
