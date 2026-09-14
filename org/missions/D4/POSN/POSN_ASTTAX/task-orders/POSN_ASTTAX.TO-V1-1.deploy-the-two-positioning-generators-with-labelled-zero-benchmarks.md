# TO POSN_ASTTAX.TO-V1-1 -- DEPLOY the two positioning generators (hardened five-class generator + labelled-zero benchmark rows in BOTH functions), through Terraform, under the two never-widen halves (AT5-s-1, B1; FWD-1/FWD-2/FWD-5)

<to_id>POSN_ASTTAX.TO-V1-1</to_id>
<project>POSN_ASTTAX</project>
<issued_to>0.9.0_WK_POSN_ASTTAX~19</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-14</issued_date>
<status>staged</status>

**Directive:** D4 - **Macro:** POSN - **Fabric:** site-z - **PRD:** `../prd/POSN_ASTTAX_PRD.md` **v0.7** @`99cc431075`
(C-BENCHMARK, C-DONE) - **Decomp cell:** `AT5-s-1` - **Issuance:** round 5, wave 1. **GATES `AT5-s-8` (R1).**

---

## IDENTITY AND THE FIRST ACT

You are `0.9.0_WK_POSN_ASTTAX~19`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_POSN_ASTTAX~19;`. Your
worktree path is in your spawn prompt. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools &&
echo TREE-OK`; a missing tree is a BLOCKING row and your final report. Commit only via
`bash .tools/safe-commit.sh --author "0.9.0_WK_POSN_ASTTAX~19 <0.9.0_WK_POSN_ASTTAX~19@opal.agent>" -F <msgfile> -- <paths>`,
msgfile by the Write tool, PURE ASCII. Never push, merge, rebase, `checkout --`, `clean`.

## THE CELL

Two Lambda functions in `infra/aws/terraform/yang-pipeline/lambdas.tf:162-184` (`module.generate_positioning`,
`module.generate_allocation_summary`) run bytes older than their source:
- `yang-generate-positioning`: live `CodeSha256 PRg64EGzQtLw7/HAhyN/jNP6rd01PrcLK4wKqCHAKfQ=`, `LastModified 2026-08-18T18:34:43Z`.
  FOUR commits ride this deploy (`git log 69b867c4eb..HEAD -- infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/`):
  `7f247caae0`, `c34eab85dc`, `07c046fa63` (POSN rounds 2-3) and `b0e1f33471` (ETFS_INGEST TO-9-DS display-name beautification,
  NOT a POSN commit -- it ships with you and both halves name it).
- `yang-generate-allocation-summary`: live `LastModified 2026-08-04T22:17:48Z`; ZERO source commits since its build.

**Your code change (C-BENCHMARK, Andrew "Call 5 Yes"):** the three new classes' benchmark rows are an EXPLICIT zero labelled
"no benchmark", in BOTH functions:
- `infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py`: `BENCHMARK_ETFS` (`:178`)
  holds three classes and `benchmark_etf_info` (`:186-203`) FALLS BACK TO CASH with a WARN for a class it does not hold -- a silent
  wrong. Replace the fallback for `structured`, `commodities`, `alternatives` with an explicit zero row carrying the label
  "no benchmark"; `benchmark_allocation_for(**weights)` (`:513`) carries the three keys at 0.0. Every other line of that file
  is NOT yours.
- `infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-allocation-summary/lambda_function.py`: `BENCHMARK_ALLOCATIONS`
  (`:46`) gains the three classes at an explicit 0.0 with the same label. `aggregate_by_asset_class` (`:233`) is NOT yours.

**The deploy path is Terraform and nothing else.** `deploy.sh` in the positioning directory is a BARE `aws lambda
update-function-code` and is BANNED (CLAUDE.md NEVER). The path: source committed -> `bash infra/aws/lambda/ci/build-and-upload.sh
yang-pipeline <function>` (one per function; it refuses uncommitted source) -> `terraform plan` scoped to the two modules ->
`.tools/safe-apply.sh -chdir=infra/aws/terraform/yang-pipeline apply <plan>` -> 0-diff re-plan -> `bash infra/aws/lambda/ci/
record-terraform-deploy.sh yang-pipeline --plan <plan> --author "<your serial> <<your serial>@opal.agent>"` -> regenerate the
served artifacts -> read them. The 2026-08-18 ledger entry
`org/critical_paths/change_management/20260818T1845Z_naming-centralization-phase1-positioning_deploy_completion.md` is the
leg shape; open yours FIRST with `python .tools/deploy_ledger.py open`.

### THE TWO HALVES, AND THE BRANCH RULE THEY BIND YOU TO

`org/missions/D4/POSN/POSN_ASTTAX/ledger/NEVER_WIDEN_ROUND5_COO_HALF.md` (@`f381f6f402`) and
`.../NEVER_WIDEN_ROUND5_CTO_HALF.md` (@`af667548d1`) name the write set, the four property writers, the rollback VersionIds
(artifact bucket `opal-313476888478-lambda-artifacts`, versioning ENABLED: positioning `xN0rrqJbABARS6vz9NqOS1zYfjxcIsFw`,
allocation-summary `XLszMw8nztf6cFmPkv069UtzZGhZJ7H_`) and **THE BRANCH RULE**: before `safe-apply`, run the positioning
generator at `69b867c4eb` and at your HEAD locally against the SAME live input and diff the two outputs per key. **Branch A**:
the delta is confined to three change classes -- display names (`b0e1f33471`), the unrecognised-security label (`c34eab85dc`),
the labelled-zero benchmark rows and the five-class allocation keys (`07c046fa63` + yours) -- proceed. **Branch B**: ANY other
difference (a weight, a subtotal, a holding appearing or vanishing) -- STOP, row, no apply. Read both halves before the first
command; cite both by path@commit in your instance.

### REFUSAL CLAUSE

A criterion you cannot satisfy as written is REFUSED with its measurement, never repaired, widened or satisfied by another
route. A deploy leg reached without both halves at HEAD is refused with a row.

## SURPRISE ROWS

Off-cell findings: ONE row appended to `org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/investigations/INVESTIGATION_v1.md`
as `POSN_ASTTAX-Z-W19-S<k>` (the site-Z coordinate is part of the id), cite path@commit, keep working.

## CRITERIA -- structured, one clause each

<criterion id="V1-AC1" cell_refs="AT5-s-1"><invocation>timeout 60 git log -1 --format='%h %an %s' -- org/missions/D4/POSN/POSN_ASTTAX/ledger/NEVER_WIDEN_ROUND5_COO_HALF.md org/missions/D4/POSN/POSN_ASTTAX/ledger/NEVER_WIDEN_ROUND5_CTO_HALF.md</invocation><expect>one commit line printed and BOTH files present at HEAD (`git ls-tree HEAD -- <each path>` lists both). Absent either: STOP, row, no further criterion.</expect></criterion> `V1-AC1` -- THE HALVES ARE AT HEAD BEFORE ANYTHING MOVES.

<criterion id="V1-AC2" cell_refs="AT5-s-1"><invocation>timeout 120 python .tools/deploy_ledger.py open --slug posn-round5-b1-positioning-generators --title "POSN_ASTTAX B1: deploy yang-generate-positioning + yang-generate-allocation-summary with labelled-zero benchmark rows" --author 0.9.0_WK_POSN_ASTTAX~19 --leg "L1|git|SITEZ commit of both lambda_function.py|commit hash" --leg "L2|s3-prefix|opal-313476888478-lambda-artifacts yang-pipeline/ both zips|build-and-upload sha256 lines" --leg "L3|verify|plan scoped to the two modules|plan summary 0 add 2 change 0 destroy" --leg "L4|activation|safe-apply|apply summary" --leg "L5|verify|0-diff re-plan|No changes" --leg "L6|git|record-terraform-deploy|commit hash" --leg "L7|verify|served positioning_data.json + allocation_summary.json regenerated|five-class keys + labelled-zero rows, non-class payload byte-identical"</invocation><expect>the ledger entry path printed under org/critical_paths/change_management/ with 7 legs OPEN. Opened BEFORE any code change.</expect></criterion> `V1-AC2` -- THE LEDGER OPENS AT START (NEVER leave a deploy half-landed).

<criterion id="V1-AC3" cell_refs="AT5-s-1"><invocation>timeout 180 bash .tools/commit-gate.sh</invocation><expect>clean on BOTH changed .py files, output cited; both ASCII limbs checked (the commit-MESSAGE arm is BLOCKING, the staged-.py arm is WARN-ONLY and ships -- say which you read). The diff touches ONLY the benchmark structures named in THE CELL; print `git diff --stat` for both files.</expect></criterion> `V1-AC3` -- THE CODE CHANGE, GATED, AND NO WIDER THAN THE CELL.

<criterion id="V1-AC4" cell_refs="AT5-s-1"><invocation>timeout 900 python <DELTA_HARNESS_RUN_GENERATOR></invocation><expect>the per-key delta between the 69b867c4eb build and your HEAD build on the same input, classified per key into: display-name, unrecognised-security-label, benchmark-row/allocation-key, OTHER. OTHER must be EMPTY (print its count). Non-empty OTHER is Branch B: STOP, row, no apply. Name the input you used (bucket/key/date) so the run is repeatable.</expect></criterion> `V1-AC4` -- THE BRANCH RULE, EXERCISED BEFORE THE APPLY. **This is what makes the halves cover both branches.**

<criterion id="V1-AC5" cell_refs="AT5-s-1"><invocation>timeout 900 bash infra/aws/lambda/ci/build-and-upload.sh yang-pipeline yang-generate-positioning</invocation><expect>the script's own gate passes (no uncommitted source under infra/aws/lambda/), the artifact uploaded to yang-pipeline/yang-generate-positioning.zip with its base64 sha256 printed, and lambda-source-map.json updated. Print the s3api head-object of the key afterwards: LastModified, VersionId, Metadata content-sha256.</expect></criterion> `V1-AC5` -- BUILD + UPLOAD, FUNCTION 1.

<criterion id="V1-AC6" cell_refs="AT5-s-1"><invocation>timeout 900 bash infra/aws/lambda/ci/build-and-upload.sh yang-pipeline yang-generate-allocation-summary</invocation><expect>the same shape for yang-pipeline/yang-generate-allocation-summary.zip: sha256 printed, source map updated, head-object printed.</expect></criterion> `V1-AC6` -- BUILD + UPLOAD, FUNCTION 2.

<criterion id="V1-AC7" cell_refs="AT5-s-1"><invocation>timeout 600 terraform -chdir=infra/aws/terraform/yang-pipeline plan -target=module.generate_positioning -target=module.generate_allocation_summary -out=.scratch/b1.tfplan</invocation><expect>Plan: 0 to add, 2 to change, 0 to destroy -- exactly the two aws_lambda_function resources updated in place (s3_object_version / source_code_hash). Any other resource in the plan is a STOP with a row.</expect></criterion> `V1-AC7` -- THE PLAN, SCOPED, AND EXACTLY TWO.

<criterion id="V1-AC8" cell_refs="AT5-s-1"><invocation>timeout 900 .tools/safe-apply.sh -chdir=infra/aws/terraform/yang-pipeline apply .scratch/b1.tfplan</invocation><expect>Apply complete! Resources: 0 added, 2 changed, 0 destroyed. The HALTGT checkpoint output is pasted above the apply line.</expect></criterion> `V1-AC8` -- THE APPLY, THROUGH THE GATE.

<criterion id="V1-AC9" cell_refs="AT5-s-1"><invocation>timeout 600 terraform -chdir=infra/aws/terraform/yang-pipeline plan -target=module.generate_positioning -target=module.generate_allocation_summary</invocation><expect>No changes. Your infrastructure matches the configuration.</expect></criterion> `V1-AC9` -- 0-DIFF RE-PLAN.

<criterion id="V1-AC10" cell_refs="AT5-s-1"><invocation>timeout 120 .tools/aws lambda get-function-configuration --function-name yang-generate-positioning --query '{LastModified:LastModified,CodeSha256:CodeSha256}' --output json</invocation><expect>CodeSha256 EQUALS the sha256 V1-AC5 printed for the positioning zip and LastModified is after your apply; then the same read for yang-generate-allocation-summary EQUALS V1-AC6's sha256. Both pasted.</expect></criterion> `V1-AC10` -- DEPLOYED BYTES == BUILT BYTES, BOTH FUNCTIONS (running-bytes-older-than-built passes every other rung).

<criterion id="V1-AC11" cell_refs="AT5-s-1"><invocation>timeout 900 python <REGENERATE_START_YANGDATAPIPELINE_LAST></invocation><expect>the regeneration completes; the served s3://opal-data-portal-v2/json/positioning/positioning_data.json (gzip body) now carries, for all five models, allocation keys including structured, commodities, alternatives, and benchmark rows for those three reading an explicit 0 labelled "no benchmark"; allocation_summary.json likewise; the membership (tickers per model) is IDENTICAL to the pre-deploy read (VersionId 4Q1qjgD52FSKZ38EfHGqdKGHyJ_ktlka) and every non-class, non-name payload byte is identical -- print the diff summary. Any OTHER key the SFN rewrote reads byte-identical to its prior version (the control).</expect></criterion> `V1-AC11` -- THE SERVED READ. The bar is the ARTIFACT, never the apply's rc=0.

<criterion id="V1-AC12" cell_refs="AT5-s-1"><invocation>timeout 300 bash infra/aws/lambda/ci/record-terraform-deploy.sh yang-pipeline --plan .scratch/b1.tfplan --author "0.9.0_WK_POSN_ASTTAX~19 <0.9.0_WK_POSN_ASTTAX~19@opal.agent>"</invocation><expect>the recorder commits lambda-source-map.json with last_deployed_commit for exactly the two functions; commit hash printed. Then every ledger leg L1-L7 closed with its proof via `python .tools/deploy_ledger.py close-leg` and the entry closed; print the entry's final status line.</expect></criterion> `V1-AC12` -- RECORDED AND CLOSED, NO STRANDED LEG.

<criterion id="V1-AC13" cell_refs="AT5-s-1" judgment="true"><invocation>JUDGMENT -- no invocation; graded at L9</invocation><expect>Whether V1-AC4's classification of the delta was honest -- whether anything filed under the three permitted classes was in fact an OTHER. Record the readings and offer NO verdict.</expect></criterion> `V1-AC13` -- **JUDGMENT, GRADED BY `3.0.0_SA_CVO~Z` AT L9.**

<expected_criteria>V1-AC1, V1-AC2, V1-AC3, V1-AC4, V1-AC5, V1-AC6, V1-AC7, V1-AC8, V1-AC9, V1-AC10, V1-AC11, V1-AC12, V1-AC13</expected_criteria>

<placeholders>DELTA_HARNESS_RUN_GENERATOR, REGENERATE_START_YANGDATAPIPELINE_LAST</placeholders>

<paths>
org/missions/D4/POSN/POSN_ASTTAX/task-orders/POSN_ASTTAX.TO-V1-1.deploy-the-two-positioning-generators-with-labelled-zero-benchmarks.md
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~19/
org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py
infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-allocation-summary/lambda_function.py
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/terraform/yang-pipeline/CHANGELOG.json
org/critical_paths/change_management/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D4/POSN/POSN_ASTTAX/decompositions/POSN_ASTTAX_DECOMP_round5.md</decomp_doc> round 5, cell `AT5-s-1`.
<owned_cells>AT5-s-1</owned_cells>
Read-dependencies, NOT claimed: none upstream. DOWNSTREAM: `AT5-s-8` (R1) reads your V1-AC10/AC11 evidence; `AT5-s-6` (F2) reads
the five-class served keys your regeneration lands. You do not touch them.
</decomp_ref>

<preflight>
comp-schedule: RUN at the cut (2026-09-14 ~17:4xZ) -- 2 armed gates, neither POSN (G-3 inf never-widen sentinel, G-7 BD calendar
guard); 7 open deploy-ledger entries (yours will be the eighth, opened at V1-AC2 and closed at V1-AC12); 12 standing NEVER clauses
bind this cell: Terraform only, safe-apply, never-widen (both halves at HEAD), no monitor.
comp-iam: RUN -- `comp-iam service yang-generate-positioning`: 7 calls across 13 statements, 1 GRANTED, 6 UNRESOLVABLE-RESOURCE (bucket/key are runtime args); BLIND on those 6; this cell changes NO grant; the blindness is stated, not remedied.
comp-adversary: RUN on the decomposition (5 sources / 4 declared exclusions). NOT covered, stated: (1) the issuer has NOT run the
69b867c4eb-vs-HEAD delta -- V1-AC4 is the first run and its OTHER count is unknown to the issuer; (2) the SFN regeneration rewrites
keys beyond the two named -- V1-AC11's control reads them byte-identical or you file a row; (3) the issuer has not exercised
build-and-upload.sh on this device since the reboot.
</preflight>

<proof_of_spec>
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~19/POSN_ASTTAX.TO-V1-1.deploy-the-two-positioning-generators-with-labelled-zero-benchmarks.proof_of_spec.json
</proof_of_spec>
