# TO POSN_ASTTAX.TO-V1-1 -- DEPLOY the two positioning generators (hardened five-class generator + labelled-zero benchmark rows in BOTH functions), through Terraform, under the two never-widen halves (AT5-s-1, B1; FWD-1/FWD-2/FWD-5)

<to_id>POSN_ASTTAX.TO-V1-1</to_id>
<project>POSN_ASTTAX</project>
<issued_to>0.9.0_WK_POSN_ASTTAX~19</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-14</issued_date>
<status>complete</status>

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

**AMENDED AT THE DRAIN OF YOUR FIRST RUN (rows W19-S1..S7; issuer rows Z-S74..Z-S79):** (a) `V1-AC5` runs under the build
script's OWN documented per-build override `BAU_MANIFEST_SKIP=1` (`build-and-upload.sh:286-287`, 'justify in the commit
message'): the manifest gate's ABSENT arm is unreachable under `set -e` (W19-S1) and THIS package's manifest is READABLE and
declares no blobs, so the override skips a SKIP and never a check -- you PRINT that discriminator FIRST (the standalone probe:
parses clean, `declared_blobs` absent, rc=1; an rc=2 UNREADABLE is a refusal, never an override). The one-line control-flow
fix is the CI lane's (`infra/aws/**`, CLOUD_OPS_OR_ETL) and rides the round analysis, not this cell. (b) The plan file is the
ABSOLUTE native path `C:/tmp/wk-posn-5-19/.scratch/b1.tfplan` in `V1-AC7`, `V1-AC8` and `V1-AC12` (W19-S2: `-chdir` re-bases a
relative `-out`; terraform is native windows_amd64 and a drive-letter path is untouched by MSYS). (c) THE LABEL IS SERVED
(W19-S6): the cell WIDENS by ONE emit in the global benchmarks block (`:2337-2349` at `e89fca26e2`): when
`benchmark_etf_info(asset_class)` returns `ticker None`, emit `global_benchmarks['etf'][asset_class]` as `{'ticker': None,
'name': NO_BENCHMARK_LABEL, 'label': NO_BENCHMARK_LABEL, 'yield': None, 'cost': None, 'duration': None, 'beta': None}` -- so
`benchmarks.etf.structured|commodities|alternatives` are SERVED as labelled zero rows the F2 cell (`AT5-s-6`) can read. The
issuer measured the live portal at the pin reads `benchmarks.etf` NOWHERE (0 hits across 557 files under `portal/src`), so the
new keys are inert to the served page today. The WARN loop and every other line stay reserved. `allocation_summary.json` keeps
its code-level label (the row shape at `:233` is reserved): its served bytes do NOT move today, and that is `V1-AC11`'s control.
Your delta classifier ADMITS the new path shape `benchmarks.etf.<class>.*` for exactly those three classes under the
benchmark-row class, by name; OTHER stays the discriminator. (d) After EVERY writer of `infra/aws/lambda/ci/lambda-source-map.json`
(build-and-upload at `V1-AC5`, the recorder at `V1-AC12`) restore the file to PURE ASCII from HEAD's bytes with ONLY the changed
values substituted (W19-S7), and print `len(b) - len(b.decode('utf-8'))` reading 0 for the committed bytes. (e) `<paths>` now
names `org/critical_paths/.open_deploys/`: commit the sentinel the ledger tool staged, in the same commit as the next ledger
write (Z-S72 ruling). STANDS from your first run: `V1-AC1`, `V1-AC2`, `V1-AC6` (allocation-summary zip sha256
`8ok3+P8z/w2hDmcnMSLPWTmSlp5pXBEqY86hDiPl3A4=`, VersionId `BxWpvrT9AKAV4p6Bl1o9vPYcz98NESHc`, source map value already at HEAD).
RE-RECORDED on this face: `V1-AC3` (the widened diff), `V1-AC4` (the branch rule, again, on the widened HEAD), `V1-AC5`,
`V1-AC7`..`V1-AC12`, and `V1-AC13`'s readings.
**THIRD AMENDMENT (~21:1xZ, after your second run; W19-S8 disarmed Z-S94):** the deploy is LANDED (V1-AC8/AC9/AC10 stand) and
the served refresh is re-cut as the DRIVEN per-producer act both halves now name: `V1-AC11` invokes the two generators DIRECTLY
with their recorded events and then the pipeline's own invalidation lambda; the state machine is NEVER started (it consumes its
own input -- 3 of 3 absent -- and its write set of 28 Task states, an S3 delete and a CDN invalidation exceeds the signed keys).
The placeholder is renamed `<DRIVE_YANG_GENERATORS_RECORDED_EVENTS>`. `V1-AC12`'s last clause (L7 closed, the entry closed)
follows; its recorder half stands (56accb9417, the CHANGELOG entry 13ec619b49). RE-RECORDED on this face: `V1-AC11`, `V1-AC12`.

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

<criterion id="V1-AC3" cell_refs="AT5-s-1"><invocation>timeout 180 bash .tools/commit-gate.sh infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-allocation-summary/lambda_function.py</invocation><expect>OK: pre-commit gate clean for 2 of 2 file(s) -- clean on BOTH changed .py files, output cited; both ASCII limbs checked (the commit-MESSAGE arm is BLOCKING, the staged-.py arm is WARN-ONLY and ships -- say which you read). The diff touches ONLY the benchmark structures named in THE CELL; print `git diff --stat` for both files.</expect></criterion> `V1-AC3` -- THE CODE CHANGE, GATED, AND NO WIDER THAN THE CELL.

<criterion id="V1-AC4" cell_refs="AT5-s-1"><invocation>timeout 900 python <DELTA_HARNESS_RUN_GENERATOR></invocation><expect>the per-key delta between the 69b867c4eb build and your HEAD build on the same input, classified per key into: display-name, unrecognised-security-label, benchmark-row/allocation-key, OTHER. OTHER must be EMPTY (print its count). Non-empty OTHER is Branch B: STOP, row, no apply. Name the input you used (bucket/key/date) so the run is repeatable.</expect></criterion> `V1-AC4` -- THE BRANCH RULE, EXERCISED BEFORE THE APPLY. **This is what makes the halves cover both branches.**

<criterion id="V1-AC5" cell_refs="AT5-s-1"><invocation>BAU_MANIFEST_SKIP=1 timeout 900 bash infra/aws/lambda/ci/build-and-upload.sh yang-pipeline yang-generate-positioning</invocation><expect>FIRST, printed above the build: the standalone manifest probe on this package (the python block at build-and-upload.sh:301-310 run by hand on the cygpath-translated source dir) reading PARSES CLEAN, declared_blobs ABSENT, rc=1 -- the arm the gate designs as SKIP; an rc=2 is a REFUSAL of this criterion, never an override. Then, under the override, `git status --porcelain infra/aws/lambda/` EMPTY, the artifact uploaded to yang-pipeline/yang-generate-positioning.zip with its base64 sha256 printed, and lambda-source-map.json carrying the new value. Print the s3api head-object of the key afterwards: LastModified, VersionId, Metadata content-sha256. Then lambda-source-map.json RESTORED to pure ASCII from HEAD's bytes with exactly ONE value substituted (functions.yang-generate-positioning.artifact_sha256): print the detector `len(b) - len(b.decode('utf-8'))` reading 0 and the PARSED diff vs HEAD reading exactly ONE changed leaf; the byte diff (`git diff --stat`, printed) may be wider where HEAD's bytes carried inherited non-ASCII that the re-escape restores -- say so.</expect></criterion> `V1-AC5` -- BUILD + UPLOAD, FUNCTION 1.

<criterion id="V1-AC6" cell_refs="AT5-s-1"><invocation>timeout 900 bash infra/aws/lambda/ci/build-and-upload.sh yang-pipeline yang-generate-allocation-summary</invocation><expect>the same shape for yang-pipeline/yang-generate-allocation-summary.zip: sha256 printed, source map updated, head-object printed.</expect></criterion> `V1-AC6` -- BUILD + UPLOAD, FUNCTION 2.

<criterion id="V1-AC7" cell_refs="AT5-s-1"><invocation>timeout 600 terraform -chdir=infra/aws/terraform/yang-pipeline plan -target=module.generate_positioning -target=module.generate_allocation_summary -out=C:/tmp/wk-posn-5-19/.scratch/b1.tfplan</invocation><expect>Plan: 0 to add, 2 to change, 0 to destroy -- exactly the two aws_lambda_function resources updated in place (s3_object_version / source_code_hash). Any other resource in the plan is a STOP with a row.</expect></criterion> `V1-AC7` -- THE PLAN, SCOPED, AND EXACTLY TWO.

<criterion id="V1-AC8" cell_refs="AT5-s-1"><invocation>timeout 900 .tools/safe-apply.sh -chdir=infra/aws/terraform/yang-pipeline apply C:/tmp/wk-posn-5-19/.scratch/b1.tfplan</invocation><expect>Apply complete! Resources: 0 added, 2 changed, 0 destroyed. The HALTGT checkpoint output is pasted above the apply line.</expect></criterion> `V1-AC8` -- THE APPLY, THROUGH THE GATE.

<criterion id="V1-AC9" cell_refs="AT5-s-1"><invocation>timeout 600 terraform -chdir=infra/aws/terraform/yang-pipeline plan -target=module.generate_positioning -target=module.generate_allocation_summary</invocation><expect>No changes. Your infrastructure matches the configuration.</expect></criterion> `V1-AC9` -- 0-DIFF RE-PLAN.

<criterion id="V1-AC10" cell_refs="AT5-s-1"><invocation>timeout 120 .tools/aws lambda get-function-configuration --function-name yang-generate-positioning --query '{LastModified:LastModified,CodeSha256:CodeSha256}' --output json</invocation><expect>CodeSha256 EQUALS the sha256 V1-AC5 printed for the positioning zip and LastModified is after your apply; then the same read for yang-generate-allocation-summary EQUALS V1-AC6's sha256. Both pasted.</expect></criterion> `V1-AC10` -- DEPLOYED BYTES == BUILT BYTES, BOTH FUNCTIONS (running-bytes-older-than-built passes every other rung).

<criterion id="V1-AC11" cell_refs="AT5-s-1"><invocation>timeout 1800 python <DRIVE_YANG_GENERATORS_RECORDED_EVENTS></invocation><expect>the two generators this cell deployed invoked DIRECTLY, once each, in order -- yang-generate-positioning, then yang-generate-allocation-summary -- each with the event the state machine passed it on the last execution that ran it (stepfunctions get-execution-history of YangDataPipeline:20260911_v1-1c95bba7; the GeneratePositioning event at LambdaFunctionScheduled #83 is cached at .scratch/sfn_history.json; the model-PKL-branch GenerateAllocationSummary event likewise), never a hand-written event; the state machine itself is NOT started (W19-S8: it consumes its own input and its write set exceeds the signed keys). Printed BEFORE the invokes: s3api head-object (LastModified, VersionId) of positioning_data.json and allocation_summary.json, and list-objects-v2 of json/positioning/ (key, LastModified) as the second control's baseline. Each invoke: StatusCode 200, no FunctionError, the response body printed. Printed AFTER: both heads moved (LastModified after the invoke, new VersionIds). Then the served s3://opal-data-portal-v2/json/positioning/positioning_data.json (gzip body) carries, for all five models, allocation keys including structured, commodities, alternatives at an explicit 0 (allocation, benchmark.allocation, benchmark.spread.allocation, delta -- 60 leaf keys, every value 0 or 0.0, printed as a count), AND benchmarks.etf carries rows keyed structured, commodities, alternatives each reading ticker null and label "no benchmark" (print the three rows verbatim); the membership (tickers per model) is IDENTICAL to the pre-deploy read (VersionId 4Q1qjgD52FSKZ38EfHGqdKGHyJ_ktlka) and every other payload byte outside the display-name and unrecognised-security-label classes is identical -- print the diff summary with OTHER = 0. allocation_summary.json: byte-identical to its prior version except generated_at (no holding carries the three classes today; the label there is code-level by design) -- print that diff summary as the control. Any key under json/positioning/ OTHER than these two whose LastModified moved between the two list-objects reads is Branch B (the second control). Then the CDN: yang-invalidate-cloudfront invoked with ITS recorded event from the same history (the pipeline's own step; its write set is the CloudFront cache of the keys just written and NO key; both halves name it), Invalidation Id + Status printed, so the page reads the new bytes.</expect></criterion> `V1-AC11` -- THE SERVED READ, DRIVEN PER PRODUCER. The bar is the ARTIFACT, never the invoke's rc=0.

<criterion id="V1-AC12" cell_refs="AT5-s-1"><invocation>timeout 300 bash infra/aws/lambda/ci/record-terraform-deploy.sh yang-pipeline --plan C:/tmp/wk-posn-5-19/.scratch/b1.tfplan --author "0.9.0_WK_POSN_ASTTAX~19 <0.9.0_WK_POSN_ASTTAX~19@opal.agent>"</invocation><expect>the recorder's commit VERIFIED BY GIT, never by its stdout (W23-S4: the recorder exits 0 printing 'committed' on a failed write): `git show --stat HEAD` lists infra/aws/lambda/ci/lambda-source-map.json, and the source map at HEAD carries last_deployed_commit for exactly the two functions; commit hash printed. If the recorder re-encoded the source map, ONE follow-up commit restores it to pure ASCII (detector 0 printed, values unchanged). CHANGELOG.json: the recorder's JS helper CANNOT run on this device (W23-S4: record-terraform-deploy.sh:218 tests a hardcoded bun path that does not exist here, falls to python3 and hands it a .js file; its banner 'Source map + CHANGELOG.json committed' is then FALSE and is not evidence) -- write the entry YOURSELF in the helper's exact shape (the entry object built at record-terraform-deploy.sh:600-700: version, deployed_at, deployed_commit, deployed_commit_short, previous_commit, branch, agent, functions_updated, commits, artifacts, scoped to exactly the functions this cell deployed) at the HEAD of `entries`, written with json.dump(ensure_ascii=False, indent=2) plus a trailing newline in UTF-8 so the file's non-ASCII count is UNCHANGED (print `len(b) - len(b.decode('utf-8'))` before and after), and commit it under your grant. The recorder's other two device defects (a cp1252 text-mode read; an unquoted python3 path with a space) are worked around by ENVIRONMENT ONLY (PYTHONUTF8=1; a space-free python3 shim directory first on PATH), never by editing the script. Then every ledger leg L1-L7 closed with its proof via `python .tools/deploy_ledger.py close-leg` and the entry closed; print the entry's final status line.</expect></criterion> `V1-AC12` -- RECORDED AND CLOSED, NO STRANDED LEG.

<criterion id="V1-AC13" cell_refs="AT5-s-1" judgment="true"><invocation>JUDGMENT -- no invocation; graded at L9</invocation><expect>Whether V1-AC4's classification of the delta was honest -- whether anything filed under the three permitted classes was in fact an OTHER. Record the readings and offer NO verdict.</expect></criterion> `V1-AC13` -- **JUDGMENT, GRADED BY `3.0.0_SA_CVO~Z` AT L9.**

<expected_criteria>V1-AC1, V1-AC2, V1-AC3, V1-AC4, V1-AC5, V1-AC6, V1-AC7, V1-AC8, V1-AC9, V1-AC10, V1-AC11, V1-AC12, V1-AC13</expected_criteria>

<placeholders>DELTA_HARNESS_RUN_GENERATOR, DRIVE_YANG_GENERATORS_RECORDED_EVENTS</placeholders>

<paths>
org/missions/D4/POSN/POSN_ASTTAX/task-orders/POSN_ASTTAX.TO-V1-1.deploy-the-two-positioning-generators-with-labelled-zero-benchmarks.md
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~19/
org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py
infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-allocation-summary/lambda_function.py
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/terraform/yang-pipeline/CHANGELOG.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
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
