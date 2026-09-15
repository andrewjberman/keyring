# TO POSN_AGGFIX.TO-A3-1 -- DEPLOY THE PRODUCER THROUGH ITS MODULE UNDER BOTH NEVER-WIDEN HALVES, DRIVE ONE RUN ON THE RECORDED EVENT, AND READ THE SERVED RESULT: the shared file without the aggregate and with each book's current `aum`, the Opal-only key present, and the satellites reader unmoved (AF1-s-10; FWD-4, FWD-6, FWD-7, FWD-8)

<to_id>POSN_AGGFIX.TO-A3-1</to_id>
<project>POSN_AGGFIX</project>
<issued_to>0.9.0_WK_POSN_AGGFIX~1</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-15</issued_date>
<status>complete</status>

**Directive:** D4 - **Macro:** POSN - **Fabric:** site-z - **PRD:** `org/missions/D4/POSN/POSN_AGGFIX/prd/POSN_AGGFIX_PRD.md` **v0.2**
@`cbd85e5cff` (C-NEVER-WIDEN, C-FIVE-BOOKS-UNCHANGED, C-OPAL-ONLY-DATA) - **Decomp cell:** `AF1-s-10` - **Issuance:** round 1, slot `~1`,
THIRD in this slot's queue. **Handed to you only after TO-A2-1 drained onto SITEZ.** THIS ORDER CHANGES SERVED OUTPUT.

---

## IDENTITY AND THE FIRST ACT

You are `0.9.0_WK_POSN_AGGFIX~1`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_POSN_AGGFIX~1;`. Your worktree is
`/c/tmp/wk-aggfix-1-1` (branch `wk-posn_aggfix-1-1`). First act: `git rev-parse --abbrev-ref HEAD` and
`test -d org && test -d .tools && echo TREE-OK`; bring SITEZ in if it is not an ancestor (`git merge-base --is-ancestor SITEZ HEAD ||
git merge --no-edit SITEZ`; never a rebase). Commit ONLY via `bash .tools/safe-commit.sh --author
"0.9.0_WK_POSN_AGGFIX~1 <0.9.0_WK_POSN_AGGFIX~1@opal.agent>" -F <msgfile> -- <paths>` (msgfile by the Write tool, PURE ASCII). Never
push, rebase, `checkout --`, `clean`. **Immediately before your first `safe-apply`**, run
`printf '%s\n' 0.9.0_WK_POSN_AGGFIX~1 > "/c/Users/Opal Bloomberg/Desktop/ajb_workspace/org/mcp/sessions/${CLAUDE_CODE_SESSION_ID}.serial"`
(the halt gate reads the session serial file, which every worker of this session shares; last writer wins).

**The deploy path is Terraform and nothing else.** A bare `aws lambda update-function-code` (and any `deploy.sh` wrapping one) is BANNED.

**THREE OPERATING FACTS MEASURED BY TO-C1-1's DEPLOY ON THIS DEVICE (rows W2-S5, W2-S7; added before hand-off, ~21:4xZ):**
1. **The halt gate reads the session serial file under the WORKTREE root**, not the main workspace: write the serial line to BOTH
   `/c/tmp/wk-aggfix-1-1/org/mcp/sessions/${CLAUDE_CODE_SESSION_ID}.serial` and the main-workspace path above, immediately before `safe-apply`.
2. **The gate then lists the ISSUER's unread inbox** (routine messages, measured 182 at TO-C1-1's apply). Read every listed subject, paste the
   census into your evidence, and if none begins `[STOP]` or `[HALT]`, re-run the same `safe-apply` with `HALT_ACK=1` as the gate instructs.
   Any `[STOP]` or `[HALT]` subject: STOP, BLOCKING row, no apply.
3. **`record-terraform-deploy.sh` fails on the spaced python3 path** (its :511 is unquoted). Put the short 8.3 form of the python3 directory
   FIRST on `PATH` for that one command, then run it unchanged; its CHANGELOG helper still cannot run here, so that entry is written by hand
   (A3-AC11 already says so).

## THE CELL (verbatim from the decomposition @`605c03f81f`)

**`AF1-s-10` -- the producer deployed through its module, and the served result read (S10, C-NEVER-WIDEN).** Under
`ledger/NEVER_WIDEN_ROUND1_PRODUCER_COO_HALF.md` and `..._CTO_HALF.md` (both at HEAD before any leg moves): the deploy ledger entry opened
first; `build-and-upload.sh yang-pipeline yang-generate-positioning`; `terraform init` then a plan `-target`ed to
`module.generate_positioning` reading exactly one function updated in place; `safe-apply`; a 0-diff re-plan; deployed `CodeSha256` == the
uploaded artifact's; the generator invoked DIRECTLY once with the event the state machine passed it on its last execution (never a
hand-written event, never the state machine) and the pipeline's own invalidation lambda with its recorded event; then the served reads:
the prior and new VersionIds of the shared file printed; the new shared file's five books byte-identical to the prior version in every
field except `aum`; each book's `aum` == its current row; no AGG in the shared file; the new key present, `status OK`, weights == members /
members_sum; the satellites `yang_index` run on the prior and new shared file yields identical `out` and `extra` maps and a `conflicts`
list whose difference is printed; the recorder commit verified by git; the ledger entry closed. **The key's exposure before AF1-s-11's
gate is live equals today's** (every signed-in viewer receives the AGG block in the shared file today), so no widening occurs in that
window; the halves name it.

**The two halves and the branch rule they bind you to.** Read both halves (`git show SITEZ:<path>`) before the first command and cite both
by path@commit in your instance. **Branch A:** the served delta is confined to {`current_holdings.AGG` removed from the shared file; the
five book `aum` values; `generated_at`; the new key `json/positioning/opal_aggregate.json`} -- proceed to the recorder and the close.
**Branch B:** ANY other difference (a holding, a weight, a benchmark row, another key under `json/positioning/` whose LastModified moves) --
STOP, file a BLOCKING row, and run the rollback the COO half names for each key; nothing further.

**AMENDED BEFORE HAND-OFF (issuer, ~19:2xZ, on the CTO half @`ae1c985da4` and row `POSN_AGGFIX-Z-S2`):** the shared key has THREE writers,
not one -- this producer, `yang-time-machine` (a Dev-triggered restore of every captured key under `json/` by prefix) and
`infra/aws/lambda/v2_portal/yang_pipeline/scripts/rollback-protocol.sh` (an operator restore by prefix). This act invokes neither, except its
own Branch B rollback of the shared file's prior VersionId. The ledger entry (A3-AC2) names both and the residual both halves leave unsigned:
after Branch A, a restore to any execution before the change re-serves `current_holdings.AGG` and July book `aum` until the next pipeline run.
That residual is row Z-S2's, carried to the round analysis; it is not yours to fix. **Every served comparison in A3-AC9 compares PARSED
JSON (dict key order ignored, list order compared), never raw bytes:** the producer's `portfolios.*.benchmark.spread.segment` keys come out in
hash-seed-dependent order between two Lambda runs of the same code (row W1-S7), so a byte compare would read a spurious difference. **And the producer file itself carries two write
sites of the shared key (row W1-S4):** the handler (this act) and `main()`'s `--upload` branch (a manual path, not invoked here), which
TO-A2-1 amended to write the Opal-only key beside it (A2-AC13).

**Your inputs (at SITEZ, never re-derived):** TO-A2-1's harness and its recorded event (the execution ARN it printed); TO-A1-1's commit list
between the running bytes and HEAD (every commit on that list rides this deploy and both halves name them).

### REFUSAL CLAUSE

A criterion you cannot satisfy as written is REFUSED with its measurement, never repaired, widened or satisfied by another route. A deploy
leg reached without both halves at SITEZ is refused with a row.

## SURPRISE ROWS

ONE row per off-cell finding, id `POSN_AGGFIX-Z-W1-S<k>` continuing your sequence, in
`org/missions/D4/POSN/POSN_AGGFIX/surprise-channel/investigations/INVESTIGATION_v1.md`; keep working.

## CRITERIA -- structured, one clause each

<criterion id="A3-AC1" cell_refs="AF1-s-10"><invocation>timeout 60 git ls-tree SITEZ -- org/missions/D4/POSN/POSN_AGGFIX/ledger/NEVER_WIDEN_ROUND1_PRODUCER_COO_HALF.md org/missions/D4/POSN/POSN_AGGFIX/ledger/NEVER_WIDEN_ROUND1_PRODUCER_CTO_HALF.md</invocation><expect>two blob lines, one per half. One or none: STOP before any further criterion, BLOCKING row.</expect></criterion> `A3-AC1` -- BOTH HALVES ARE FILES BEFORE ANYTHING MOVES.

<criterion id="A3-AC2" cell_refs="AF1-s-10"><invocation>timeout 120 python .tools/deploy_ledger.py open --slug posn-aggfix-r1-producer --title "POSN_AGGFIX AF1-s-10: deploy yang-generate-positioning (current weights, Opal-only aggregate key); the shared key's other writers yang-time-machine and rollback-protocol.sh restore by prefix and are NOT invoked; residual row POSN_AGGFIX-Z-S2" --author 0.9.0_WK_POSN_AGGFIX~1 --leg "L1|git|SITEZ carries TO-A2-1's lambda_function.py|commit hash" --leg "L2|s3-prefix|opal-313476888478-lambda-artifacts yang-pipeline/yang-generate-positioning.zip|sha256 + VersionId" --leg "L3|verify|plan targeted to module.generate_positioning|0 add 1 change 0 destroy" --leg "L4|activation|safe-apply|apply summary" --leg "L5|verify|0-diff re-plan and deployed CodeSha256|No changes + sha equal" --leg "L6|activation|driven generator invoke + invalidation on recorded events|VersionIds before and after" --leg "L7|verify|served reads, Branch A|five books non-aum identical, aum current, no AGG, new key OK" --leg "L8|git|record-terraform-deploy|commit hash"</invocation><expect>the ledger entry and its sentinel created under org/critical_paths/change_management/ and org/critical_paths/.open_deploys/, both committed in your next commit (git show --stat lists both).</expect></criterion> `A3-AC2` -- THE LEDGER ENTRY OPENS FIRST.

<criterion id="A3-AC3" cell_refs="AF1-s-10"><invocation>timeout 900 bash infra/aws/lambda/ci/build-and-upload.sh yang-pipeline yang-generate-positioning</invocation><expect>printed BEFORE the build: s3api head-object of yang-pipeline/yang-generate-positioning.zip (VersionId, LastModified, Metadata content-sha256) -- the ROLLBACK VersionId. The build uploads the artifact and prints its sha256; head-object after prints the new VersionId and content-sha256. If the script's manifest gate refuses on the arm TO-V1-1 measured (POSN_ASTTAX row W19-S1: the ABSENT arm unreachable under set -e), the standalone manifest probe is printed first reading PARSES CLEAN / declared_blobs ABSENT / rc 1 and the run repeats under BAU_MANIFEST_SKIP=1, justified in the commit message; an rc 2 UNREADABLE is a refusal. infra/aws/lambda/ci/lambda-source-map.json is then restored to PURE ASCII with only the changed values (detector 0 printed).</expect></criterion> `A3-AC3` -- BUILD AND UPLOAD, WITH THE ROLLBACK VERSION PRINTED FIRST.

<criterion id="A3-AC4" cell_refs="AF1-s-10"><invocation>timeout 900 bash -c "terraform -chdir=infra/aws/terraform/yang-pipeline init -input=false -no-color > .scratch/a3_init.txt 2>&1; tail -3 .scratch/a3_init.txt; terraform -chdir=infra/aws/terraform/yang-pipeline plan -input=false -no-color -target=module.generate_positioning -out=C:/tmp/wk-aggfix-1-1/.scratch/a3.tfplan"</invocation><expect>init reports success; the plan reads `Plan: 0 to add, 1 to change, 0 to destroy`, the one change the aws_lambda_function inside module.generate_positioning updated in place (s3_object_version / source_code_hash). Any other address: STOP, row.</expect></criterion> `A3-AC4` -- THE PLAN, TARGETED, EXACTLY ONE.

<criterion id="A3-AC5" cell_refs="AF1-s-10"><invocation>timeout 900 .tools/safe-apply.sh -chdir=infra/aws/terraform/yang-pipeline apply C:/tmp/wk-aggfix-1-1/.scratch/a3.tfplan</invocation><expect>`Apply complete! Resources: 0 added, 1 changed, 0 destroyed.` with the halt-gate checkpoint output pasted above it.</expect></criterion> `A3-AC5` -- THE APPLY, THROUGH THE GATE.

<criterion id="A3-AC6" cell_refs="AF1-s-10"><invocation>timeout 900 terraform -chdir=infra/aws/terraform/yang-pipeline plan -input=false -no-color -target=module.generate_positioning</invocation><expect>`No changes. Your infrastructure matches the configuration.`</expect></criterion> `A3-AC6` -- THE 0-DIFF RE-PLAN.

<criterion id="A3-AC7" cell_refs="AF1-s-10"><invocation>timeout 120 .tools/aws lambda get-function-configuration --function-name yang-generate-positioning --query "[CodeSha256,LastModified]" --output text</invocation><expect>CodeSha256 EQUAL to the base64 sha256 A3-AC3 printed for the uploaded artifact, and LastModified after the apply.</expect></criterion> `A3-AC7` -- DEPLOYED BYTES EQUAL BUILT BYTES.

<criterion id="A3-AC8" cell_refs="AF1-s-10"><invocation>timeout 1800 python <DRIVE_AND_READ_A3></invocation><expect>printed FIRST: head-object (VersionId, LastModified) of json/positioning/positioning_data.json and of json/positioning/opal_aggregate.json (absent before the first run), and list-objects-v2 of json/positioning/ with every key's LastModified; then the generator invoked once with the raw recorded input of the state machine's last GeneratePositioning event (execution ARN printed, no FunctionError) and yang-invalidate-cloudfront invoked once with its recorded event from the same execution; then the same heads and listing again; the shared file's VersionId moved and opal_aggregate.json present; every OTHER key under json/positioning/ with an unchanged LastModified (the Branch B trigger).</expect></criterion> `A3-AC8` -- ONE DRIVEN RUN ON THE RECORDED EVENT.

<criterion id="A3-AC9" cell_refs="AF1-s-10"><invocation>timeout 600 python <DRIVE_AND_READ_A3> --read-only-compare</invocation><expect>on the prior and new VersionIds of the shared file (both printed): current_holdings keys prior = UST ST INT LT ULT AGG, new = UST ST INT LT ULT; `BOOK <code> NON-AUM IDENTICAL` 5 of 5; each new book aum EQUAL to its own row of platinum/mdpf/global/aum-metrics.json at the VersionId the run read, 5 of 5; top-level keys other than generated_at and current_holdings identical; opal_aggregate.json decompressed: status OK, weights summing to 1 within 1e-9, each weight == members[code] / members_sum; a line `BRANCH A` or `BRANCH B`.</expect></criterion> `A3-AC9` -- THE SERVED RESULT, BRANCH A OR B.

<criterion id="A3-AC10" cell_refs="AF1-s-10"><invocation>timeout 600 python <DRIVE_AND_READ_A3> --satellites-reader</invocation><expect>data/assets/scripts/gold/build_satellites_characteristics.py `yang_index` imported by path and run on the prior and on the new shared file (VersionIds printed): the `out` maps identical (ticker count printed), the `extra` maps identical, and the two `conflicts` lists printed with their difference (an empty difference or the named tickers).</expect></criterion> `A3-AC10` -- THE SECOND READER, BEFORE AND AFTER.

<criterion id="A3-AC11" cell_refs="AF1-s-10"><invocation>timeout 300 bash infra/aws/lambda/ci/record-terraform-deploy.sh yang-pipeline --plan C:/tmp/wk-aggfix-1-1/.scratch/a3.tfplan --author "0.9.0_WK_POSN_AGGFIX~1 <0.9.0_WK_POSN_AGGFIX~1@opal.agent>"</invocation><expect>the recorder's commit VERIFIED BY GIT and never by its stdout: `git show --stat HEAD` lists infra/aws/lambda/ci/lambda-source-map.json with last_deployed_commit moved for yang-generate-positioning only; if the recorder re-encoded the source map, ONE follow-up commit restores pure ASCII (detector 0 printed); if its CHANGELOG helper cannot run on this device (POSN_ASTTAX row W23-S4), the infra/aws/terraform/yang-pipeline/CHANGELOG.json entry is written by hand and committed, cited.</expect></criterion> `A3-AC11` -- THE DEPLOY RECORDED.

<criterion id="A3-AC12" cell_refs="AF1-s-10"><invocation>timeout 120 python .tools/deploy_ledger.py close --slug posn-aggfix-r1-producer</invocation><expect>the ledger entry closed with every leg's evidence filled and the sentinel removed, committed (git show --stat HEAD lists the entry and the sentinel's removal).</expect></criterion> `A3-AC12` -- THE LEDGER ENTRY CLOSED.

<criterion id="A3-AC13" cell_refs="AF1-s-10" judgment="true"/> `A3-AC13` -- **JUDGMENT, GRADED BY `3.0.0_SA_CVO~Z` AT L9:** whether the served delta A3-AC9 classified as Branch A was honestly confined to the four permitted classes, and whether any `conflicts` difference A3-AC10 printed is a served change the halves did not name. Record the readings and offer NO verdict.

<expected_criteria>A3-AC1, A3-AC2, A3-AC3, A3-AC4, A3-AC5, A3-AC6, A3-AC7, A3-AC8, A3-AC9, A3-AC10, A3-AC11, A3-AC12, A3-AC13</expected_criteria>

<placeholders>DRIVE_AND_READ_A3</placeholders>

<paths>
org/missions/D4/POSN/POSN_AGGFIX/task-orders/POSN_AGGFIX.TO-A3-1.deploy-the-producer-and-read-the-served-result.md
org/missions/D4/POSN/POSN_AGGFIX/deliverables/0.9.0_WK_POSN_AGGFIX~1/
org/missions/D4/POSN/POSN_AGGFIX/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/terraform/yang-pipeline/CHANGELOG.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D4/POSN/POSN_AGGFIX/decompositions/POSN_AGGFIX_DECOMP.md</decomp_doc> round 1 @`605c03f81f`.
<owned_cells>AF1-s-10</owned_cells>
Read-dependencies, NOT claimed: `AF1-s-6`, `AF1-s-7`, `AF1-s-8` (TO-A2-1's committed bytes and harness), `AF1-s-5` (the commits riding the
deploy), `AF1-s-9` (the grants). DOWNSTREAM: `AF1-s-16` (TO-B3-1) reads your prior and new VersionIds and the live Opal-only key.
</decomp_ref>

<preflight>
comp-schedule: RUN at the cut (2026-09-15 ~18:3xZ) -- 7 armed gates, 0 POSN; 6 open deploy-ledger entries, 0 POSN (yours is opened at A3-AC2 and closed at A3-AC12); binding NEVER clauses: Terraform only through safe-apply, never-widen halves as files, no update-function-code, no monitor.
comp-iam: RUN -- the producer role's two needed grants are TO-A1-1's A1-AC6 (live evaluator) with A1-AC7 its negative control; this order changes no grant.
comp-adversary: RUN on the decomposition. NOT covered, stated: (1) the yang-pipeline root has not been initialised or planned on this device this session (the shared tree refused `Backend initialization required`), so the targeted plan's shape is the issuer's reading of lambdas.tf:162-172, not a measurement; (2) the recorded events of the latest execution are unread by the issuer; (3) whether build-and-upload.sh's manifest gate still refuses on the W19-S1 arm is unread; (4) CloudFront invalidation reaching /api/general/positioning/opal_aggregate.json depends on the invalidation lambda's recorded paths, which the issuer has not read.
</preflight>

<proof_of_spec>
org/missions/D4/POSN/POSN_AGGFIX/deliverables/0.9.0_WK_POSN_AGGFIX~1/POSN_AGGFIX.TO-A3-1.deploy-the-producer-and-read-the-served-result.proof_of_spec.json
</proof_of_spec>
