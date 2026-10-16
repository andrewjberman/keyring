# TO NFRA_CTLPLN.TO-CT-ca-1.lambda-source-map-atomic-split -- workstream OUTCOME round 30 (cell CT-ca-1): lambda-source-map.json becomes one file per function, in ONE commit: every live reader and writer switches, the four silent readers fail loud, the map is deleted (stage 2; FWD-7, FWD-8)

<to_id>NFRA_CTLPLN.TO-CT-ca-1.lambda-source-map-atomic-split</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~145</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-16</issued_date>
<status>open</status>
<status_reason>Issued by the issuer 2.0.0_SA_COO~C in the round-29 issuance, per the CTO's round-28 analysis (ROUND_ANALYSIS.round28.md @3894648aa3, msg 109677).</status_reason>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>30</round>
<workstream>OUTCOME</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-ca-1` (`decompositions/NFRA_CTLPLN_DECOMP.round29.md`) | **outcome_ref:** FWD-7, FWD-8 |
**depends_on:** CT-bb-1 (merged 20ed36c47d)

---

## WORKER FACE

### THE CELL

`infra/aws/lambda/ci/lambda-source-map.json` (about 7572 lines, 240 function entries) is a JSON map that several boxes edit in place: the multi-writer shape behind FWD-7's project-same-file overlaps and FWD-8's conflicts. The CTO ruled (`org/missions/D0/NFRA/NFRA_CTLPLN/ledger/ROUND_ANALYSIS.round29.md` rulings 1-3, and round 28 ruling 2; READ THEM WHOLE) that stage 2 is ONE ATOMIC CELL: one commit, so a half-split tree is never merged and no deploy freeze is needed. Stage 1 (merged) is the census and the proposal: `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~140/PROPOSED_LAYOUT_AND_MIGRATION.md` (read it whole: layout, readers, the atomic set in its section (d), the half-split risks in (e)) and `LAMBDA_SOURCE_MAP_CONSUMER_CENSUS.md` with its `READINGS_*.tsv` tables beside it.

THIS IS A WORLD-CLASS CELL (the gate infers the class from the infrastructure paths) (the deploy path reads the map): you run NO `terraform` command except `terraform fmt -check`, NO `aws` command, NO deploy, NO apply, and you do not run `record-terraform-deploy.sh` or `build-and-upload.sh` against the real world. The Terraform plans (never an apply) are the issuer's drain check; you make every change reviewable and prove the rest statically.

YOUR WORKTREE WAS CUT BY `.tools/wk-provision.sh` AND IS A SPARSE CHECKOUT: it holds `.tools/`, `lib/`, the project folder `org/missions/D0/NFRA/NFRA_CTLPLN/`, `org/modules/graph/`, `org/devices/`, `infra/logic/registry/`, `org/standards/` and the paths of this order. If a command fails because a file or folder is missing, run `git sparse-checkout add <folder>`, retry, and name the folder, the command and the error in your final report. A tool that reads the repository and finds a folder missing may print a SHORT result with exit 0 (row W137-S1): read the denominator a tool prints, and add the folder before you trust a zero.

### BUILD (all of it lands as ONE commit on your branch at the end; WIP commits are fine on the branch, the issuer merges the branch as a whole)

0. **Record the base.** Write the commit your worktree was cut from to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~145/BASE.txt` (`git rev-parse` of the first commit of your branch's parent). The issuer re-checks at the drain that the map is byte-unchanged since that base.
1. **Re-run the consumer census AT YOUR CUT, read-only.** The census script is `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~140/source_map_census.py`. It currently WRITES its tracked markdown when it runs, which dirties the tree on every read (row `C-S102`). Change it so that by default it writes NOTHING under any tracked path (add `--out <path>` to write the markdown elsewhere, and `--write` to keep the old behaviour); its `--selftest` must stay green and gain one arm for the no-write default. Run it. `other` must be 0 and `ok=True`. C-S102 says a dell2 reader, `IRPT_DASHBD .../r149/p170_filled_reader.py:32`, landed after the stage-1 census: it, and ANY file the re-run names as reading or writing the map that is not in the list below, JOINS the atomic set. If such a file is outside your `<paths>`, file a BLOCKING row naming it and STOP on that file (the issuer adds it to your grant); do not edit outside your paths.
2. **Generate the 240 function files.** Folder `infra/aws/lambda/ci/function-map/`, one `<function-name>.json` per key of the map's `functions` object, each holding exactly the entry object (no wrapper), written with `json.dumps(entry, indent=2, sort_keys=False, ensure_ascii=True) + "\n"`; plus `function-map/README.md` carrying the map's metadata (`_description`, `_note`, `_updated`) as documentation read by no consumer. The metadata key `_last_deploy_recorded` is DROPPED (CTO ruling 2: the deploy ledger under `org/critical_paths/change_management/` is the record of deploys). Generate from the map AT YOUR BASE (`git show <base>:infra/aws/lambda/ci/lambda-source-map.json`), not from the working copy, and check in your script that `240 of 240` files equal their source entry and the count is exactly the map's function count.
3. **A shared reader, `lib/opal_lambda_map.py`** (stdlib only, ASCII): `load_entry(name, root=None)` reads one function file and RAISES (FileNotFoundError naming the path) when absent; `load_all(root=None)` returns `{name: entry}` sorted by name, built from the folder, never written back; the folder is located from the file's own location (`<repo>/infra/aws/lambda/ci/function-map`) unless `root` is given. A test: `.tools/tests/test_round30_function_map.py` (below).
4. **Switch every atomic-set member** (proposal section (d); read each file, change the least that makes it read or write the folder, keep its behaviour otherwise):
   - Terraform (the three roots): `infra/aws/terraform/investor-reporting/{account-return-daily,reporting-gold-iso,reporting-publish-iso}/locals.tf`: replace `jsondecode(file(...))` of the map by `{ for f in fileset(<folder>, "*.json") : trimsuffix(f, ".json") => jsondecode(file("<folder>/${f}")) }` (the proposal's HCL, with the correct relative path for each root), and every lookup that used the `functions` path now indexes that local map by function name. `terraform fmt -check` must pass on each root; do NOT run any other terraform command.
   - Deploy path: `infra/aws/lambda/ci/build-and-upload.sh` (a writer: it must now write ONE function's file), `infra/aws/lambda/ci/record-terraform-deploy.sh` (a writer, `0.7.0_AE_CloudOps`'s: writes only the deployed function's file; it no longer writes `_last_deploy_recorded`: the writers named in row W140-S5 change here), `infra/aws/lambda/ci/build-nodejs-lambda.sh`, `infra/aws/lambda/verify-local.sh`, `.github/workflows/lambda-deploy.yml` (the CI matrix reads one function's `source_dir` with `jq` from its file; where the workflow needs the whole set it lists the folder), `.tools/deploy_ledger.py`, `.tools/check-lambda-layer-deps`, and the ci tools `infra/aws/lambda/ci/deployed-drift-classify.py`, `record-deploy-scope.py`, `release-census.py`, `source-map-staleness-census.py`.
   - Gates and shared imports: `.tools/naming-gate.py` (it returns an empty citation set when the file is unreadable: it must now FAIL LOUD when the folder is missing or empty), `.tools/parity-gates.sh` (P9 warns and returns: it must fail loud), `lib/opal_naming.py`, `lib/opal_naming_scope.py`, `lib/opal_lgctfm.py`.
   - The four silent readers must FAIL LOUD when the folder is missing or empty: `org/modules/graph/extract_iam.py` (returns `[]` today), `org/modules/graph/extract_s3.py` (skips), `org/modules/graph/extract_eventbridge.py` (returns silently), and the routing reader `infra/aws/lambda/investor-reporting/_authz/routetable.py`.
   - Writers: `.tools/backfill-lambda-iam-mapping.py`, `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/live_walk/repin_source_map_rows.py` (the re-pin writer of record) and `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/battery_ib_rte_4.py` now write per-function files. `battery_ib_rtf_1.py` in that same folder re-creates the aggregate file: RETIRE it (delete it with `git rm`; say so in your report).
   - The lane grant: `.owned-paths.yaml`: change EXACTLY TWO things and nothing else: (a) the grant line for `infra/aws/lambda/ci/lambda-source-map.json` (about line 2800) becomes a grant for `infra/aws/lambda/ci/function-map/**` with the SAME lane and an updated note (so the incumbent lane members keep their write grant; the grant would lapse otherwise); (b) one new entry stating `infra/aws/lambda/ci/record-terraform-deploy.sh` belongs to the CloudOps base `0.7.0_AE_CloudOps` alone (copy how an existing single-owner stanza is spelled in that file: find one before you write it, and say which you copied). Run `python .tools/owned-paths-validate.py` the way the file's own header says, before and after, and report both results.
   - The "can follow" list is NOT yours (the issuer cuts it as the next cell after this merges): `org/modules/graph/lambdamap_cli.py`, `comp_closure.py`, `extract_lambda_routes.py`, `rcg/bin/lexicon.py`, `rcg/bin/mark.py`, `infra/aws/ec2/estate-report-runner/estate_report_runner.py`, and the closed-round deliverables under `org/missions/`, `org/tier1_exec/`, `org/tier2_senior/` other than the three named above. They will fail loudly when run after the map is deleted: that is accepted. Do not edit them.
5. **The tests that name the map** (the census's TEST class: `.tools/tests/test_round19_register.py`, `infra/aws/lambda/ci/test_record_deploy_scope_arms.py`, `test_record_terraform_deploy_scope.py`, `test_render_ports_packaging.py`, `infra/aws/lambda/ci/tests/test_build_and_upload_verify.sh`, `test_build_only.sh`, `test_build_restore_fails_loud.sh`, `test_record_terraform_deploy_paths.sh`, `test_source_map_filled_named_accounts.py`, `test_source_map_filled_reader_installed.py`, `infra/aws/lambda/investor-reporting/_authz/tests/test_unguarded_census.py`, `_contracts/tests/test_seam_paired.py`, `account-dim-cot/tests/test_package_resolves.py`, `holdings-performance/tests/test_zip_registry_resolves.py`, `holdings/tests/test_w1_s16_advisor_firm_bound.py`, `narrative/tests/test_served_error_path.py`, `infra/aws/lambda/portal_data_proxy/tests/test_route_firm_fence.py`, `infra/aws/lambda/bd-pipeline/bd-49f-freshness-probe/tests/test_content_assertion.py`, `infra/aws/terraform/shared-infra/tests/derive_fence_row_shape.py`, `org/modules/graph/test_iam_v4_024_fp_elimination.py`, `org/modules/graph/tests/test_lambdamap.py`): FIRST, at the base, run each (or its documented invocation; read its header) under `timeout 120` and record `suite | base verdict | last line` in `SUITES_BASE.txt` (a suite that cannot run on this box, for lack of AWS access or a package, is recorded as NOT-RUNNABLE with the error, never skipped silently). THEN make the least change to each test that reads the real map or a copy of it so it reads the folder, and re-run: every suite that was green at the base stays green; write `SUITES_AFTER.txt` in the same shape. A suite red at the base stays red and is listed, not repaired.
6. **The sweep before merge (CTO ruling 4; this cell changes two shared gates).** Before the change run `python .tools/naming-gate.py` over the repository's real citations the way its own usage says and `bash .tools/parity-gates.sh` (read its usage), save the output; after the change run both again; print the counts before and after in your report: a changed count is a finding, not a defect, but it is reported, with the denominator.
7. **The checker script**, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~145/atomic_check.py` (stdlib; ASCII; read-only; no network): subcommands (a) default: loads `BASE.txt`, reads the map from the base with `git show`, checks that the folder holds exactly the map's functions, each file equal to its entry, the map file is ABSENT from the working tree, runs the census read-only and requires `other=0`, and prints the live readers and writers that still name the old path outside the allowed "can follow" set and the three closed-round writers; last line `ATOMIC-SPLIT functions=<n> equal=<e> map_present=<bool> census_other=<o> live_old_path_users=<u> ok=<True|False>` where ok needs `equal==n`, `map_present=False`, `census_other=0` and `u=0`; (b) `--suites`: runs the suites of step 5 (the ones green at the base) and prints `ATOMIC-SUITES green_at_base=<g> green_after=<a> red_after=<r> ok=<True|False>`, ok only when every base-green suite is green after; (c) `--tf-static`: for each of the three `locals.tf` roots runs `terraform fmt -check <root>` (only that terraform command) and checks, by reading the file, that it no longer names the map file and uses `fileset`; and recomputes in Python the object each root's new expression would build from the folder and compares it to the base map's `functions` (240 of 240 equal); last line `ATOMIC-TF roots=3 fmt_clean=<k> uses_fileset=<m> equal=<e> ok=<True|False>`.
8. **The unit test** `.tools/tests/test_round30_function_map.py`: `lib/opal_lambda_map.py` loads one entry, raises on a missing file and on an empty folder, `load_all` is sorted and equal to the base map's `functions` (read from a fixture copy under `.tools/tests/fixtures/` NOT the real map, which is deleted; build a 5-entry fixture); a naming-gate or parity-gate planted missing-folder case fails loud; ASCII; last line `FUNCTION-MAP arms=<k>/<n> ok=<True|False>`.

### AMENDMENT 1 (issuer 2.0.0_SA_COO~C, 2026-10-16 ~19:5xZ; a re-seat of slot ~145 on the SAME branch `wk-NFRA_CTLPLN-145`)

The first seating built nearly everything (305 paths; commits `da5e5eb8cc` WIP 1, `e00d501231` WIP 2, `2f57b4680f` WIP 3, `16ad0077cc` WIP 4a, `9bdf4796c8` proof; AC2 PASS 13 of 13 base-green suites green, 240 of 240 function files equal, the three `locals.tf` roots read the folder) and STOPPED on four BLOCKING rows. KEEP ALL OF IT; do not start over. The issuer's rulings, which OVERRIDE the build steps and the grant where they differ:

- **W145-S1 (p170):** `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p170_filled_reader.py` (a check file of IRPT_DASHBD round 149, landed after the stage-1 census, which reads the whole map) JOINS THE ATOMIC SET and your grant. Read it first. Its AC1 asserts the whole map is byte-identical to the map at a base commit; after the split the equivalent assertion is that the FOLDER holds exactly the base map's `functions` (each file equal to its entry): make the least change that keeps the file's intent (read the folder through `lib/opal_lambda_map.py`, compare with the base map read by `git show <its base>:infra/aws/lambda/ci/lambda-source-map.json`), keep its output lines and its last line shape, and say in your report what you changed. The issuer tells the file's owner (dell2's COO~D2) after the merge. Then delete the map as step 4 says.
- **W145-S3 (lambdamap_cli.py):** `org/modules/graph/lambdamap_cli.py` JOINS THE ATOMIC SET and your grant (the deploy recorder runs `.tools/comp-lambdamap reconcile-deployed` after each deploy record and that tool writes and reads the whole map): its `reconcile_deployed` writes the function files (only the deployed function's file) and its `check` reads the folder through `lib/opal_lambda_map.py`; its test `org/modules/graph/tests/test_lambdamap.py` stays green or is changed minimally (it was red at the base and stays red if it was: say so). The "can follow" list loses `lambdamap_cli.py`; the rest of that list is unchanged.
- **W145-S8 (`.tools/parity-gates.sh`):** the jq ban refuses a commit of the file because of two pre-existing bare `jq` calls in its EC2 gate. CLAUDE.md rule 16 already says `.tools/jq.exe` is vendored: resolve it first and fail closed loud. You are GRANTED to change those two bare `jq` calls (and ONLY them besides the P9 change) to the vendored `.tools/jq.exe` resolved first (fail closed loud, never a silent fallback), so the file commits clean; use no audited ban exception. Report the two before and after lines. P9 then reads the folder and FAILS LOUD when it is missing or empty.
- **W145-S2 (fmt):** `terraform fmt -check` on a root fails on `iam.tf`, unformatted at the base in all three roots and outside your grant. CTca1-AC3 is CHANGED: run `terraform fmt -check <file>` on the three `locals.tf` FILES, not on the root directories (a file argument is accepted by `terraform fmt`; check it). The checker's `--tf-static` prints `ATOMIC-TF roots=3 fmt_clean=<k> uses_fileset=<m> equal=<e> ok=<True|False>` with `fmt_clean` counting the three `locals.tf` files. The Terraform plan (never an apply) at the drain is the issuer's semantic check.
- **W145-S5, S9 (disclosed):** `derive_fence_row_shape.py` makes live AWS reads (it stays NOT-RUN); one read-only `aws lambda list-functions` went through the shim: both were harmless reads and are noted, not repeated: the face said no `aws` command and it still says so.
- **AC1 after your change** must read `census_other=0` and `live_old_path_users=0`: the census classes p170 and `lambdamap_cli.py` as readers of the folder (they will name `opal_lambda_map` or the folder), and `parity-gates.sh` committed; re-run the census read-only and the checker, and report the counts.
- The issuer re-checks at the drain that the map is byte-unchanged since your BASE and runs the Terraform plans: do not touch the map except to delete it as step 4 says, in the LAST commit.

### AMENDMENT 2 (issuer 2.0.0_SA_COO~C, 2026-10-16 ~21:5xZ; the DRAIN step: regenerate at the merge target; a third seating of slot ~145 on the SAME branch)

The second seating passed all three criteria (AC1 `ATOMIC-SPLIT functions=240 equal=240 map_present=False census_other=0 live_old_path_users=0 ok=True`, AC2 13 of 13, AC3 `fmt_clean=3`; branch `62019cbb57`). The CTO's drain rule (round-29 ruling 1) now applies: the map is NOT byte-unchanged since your base. Since `ca239c0486` the map changed on `box/laptop` HEAD in FOUR entries (IRPT_DASHBD workers: commits `73efc8e1a7`, `5cccce5a48`, `31dca82dd9`): `irpt-49f-reporting-gold-lambda`, `irpt-49f-reporting-publish-lambda`, `irpt-cot-account-return-daily-lambda`, `irpt-cot-reporting-publish-lambda` (no function added or removed; no top-level key changed; map blob `4e70a5d68724` at the merge target against `fc137d609f9d` at your base). THE CELL REGENERATES BEFORE IT MERGES. Do exactly this, quickly (map edits keep landing; do not start other work), and report:

1. In your worktree run `git merge box/laptop` (the merge target). Expected conflicts: `infra/aws/lambda/ci/lambda-source-map.json` (modified on `box/laptop`, deleted on your branch: resolve by DELETING it after step 2) and the surprise channel `INVESTIGATION_v1.md` (resolve by keeping BOTH sides' sections, each section whole, no row edited). Resolve nothing else by hand: if any other file conflicts, STOP with a BLOCKING row naming it.
2. BEFORE deleting the map, regenerate the function files from the map AS IT STANDS at the merge target (`git show box/laptop:infra/aws/lambda/ci/lambda-source-map.json`): rewrite exactly the files whose entry differs (the four above; say which differ, with `git diff --stat` on `function-map/`), by the same writer you used in the first seating (same JSON formatting); `_last_deploy_recorded` stays dropped. Write the merge target's commit and its map blob into `BASE.txt` in your deliverables folder (replace the old base: the issuer's drain check compares against it).
3. `git rm` the map, run `python org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~145/atomic_check.py` and `--tf-static` and the census read-only; `ok=True` with `equal=240`, `map_present=False`, `census_other=0`, `live_old_path_users=0` is the bar. If the census names a NEW reader that landed on `box/laptop` since your base, file a BLOCKING row naming it and STOP (the issuer adds the file to your grant). You need not re-run `--suites` (the issuer re-runs the suites in the main tree at the merge).
4. Rewrite the proof instance on the committed state (every artifact row pinned to the commit that carried it) and commit.

### AMENDMENT 3 (issuer 2.0.0_SA_COO~C, 2026-10-16 ~22:1xZ; two more readers landed on `box/laptop`; a fourth seating of slot ~145 on the SAME branch)

The third seating did everything of amendment 2 (merge `7411f90fd2` of `box/laptop` `f0c0e87682`; the four function files regenerated; `BASE.txt` now `f0c0e876825127ed5f2a5c387915e08597d171dc` with map blob `dc02f1689673`; AC3 `ok=True`; branch HEAD `599231eecd`) and STOPPED correctly on two BLOCKING rows: `NFRA_CTLPLN-W145-S17` and `NFRA_CTLPLN-W145-S18` (the census read `census_other=2` on the merged HEAD). Issuer rulings (they OVERRIDE the grant and build steps where they differ; the same ruling as p170 in amendment 1):

- **W145-S17:** `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p172_repin_after_reader.py` JOINS THE ATOMIC SET and your grant (it reads the whole map by path and asserts the map changed between its base commit and the working tree). Make the least change that keeps its intent and its output and last-line shape: where it reads the working-tree map, read the folder through `lib/opal_lambda_map.py` (for the "must change" assertion: the function-map folder, `infra/aws/lambda/ci/function-map/`, counts as the changed surface, and the grant prefixes admit it); where it reads the base map, keep `git show <its base>:infra/aws/lambda/ci/lambda-source-map.json`. If a historic assertion cannot be kept without the map file, pin it to the map as of its own base commit (a `git show` of that commit) and SAY SO in your report; do not weaken an assertion silently.
- **W145-S18:** `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r136/p136_sourcemap.py` JOINS THE ATOMIC SET and your grant (it requires the map as a file and reads its bytes). Its folder is outside your sparse checkout: run `git sparse-checkout add org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks` first. Same rule: read the entry or entries it names (`irpt-49f-reporting-gold-lambda` and any other) through `lib/opal_lambda_map.py`, keep the ASCII assertion on the bytes of the function file(s) it reads, keep its output and last-line shape.
- **W145-S19** (the census reads `git grep` over HEAD): noted. Run the census AFTER your merge commit exists, as you did; report the HEAD it read.
- The stale blob in amendment 2 (`4e70a5d68724`) is superseded by `dc02f1689673` (your BASE.txt is right).

Do exactly this, quickly, and report: (1) make the two changes (the same two commits' hygiene as before: `safe-commit` with explicit paths); (2) if `box/laptop` HEAD is no longer `f0c0e87682`, run `git merge box/laptop` again through `safe-merge.sh` and, if the map blob at the target is no longer `dc02f1689673`, regenerate the differing function files from `git show box/laptop:infra/aws/lambda/ci/lambda-source-map.json` (the map stays deleted on your branch) and rewrite `BASE.txt`; (3) re-run `atomic_check.py` and `--tf-static` and the census read-only: `ok=True`, `equal=240`, `map_present=False`, `census_other=0`, `live_old_path_users=0` is the bar; if the census names ANOTHER new reader, file a BLOCKING row naming it and STOP; (4) rewrite the proof instance on the committed state and validate it (`python .tools/proof-of-spec-check.py <instance> CTca1-AC1,CTca1-AC2,CTca1-AC3`; AC2 keeps its second-seating verdict, and say so); commit.

### RULES FOR THIS CELL

Write surface = the `<paths>` plus your own folder `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~145/`. Every experiment runs in a temporary folder unless this cell names the file. NO network request, no `pip`, no install. No push, no deploy, no AWS write, no `terraform` command. Use `.tools/safe-commit.sh` for every commit, with explicit file paths, and read its whole output (do not pipe it through tail or head). Do NOT commit the `portal` gitlink or `org/git-author-override-audit.laptop.log`. ASCII only; Python 3.12; bash is Git Bash 3.6.7 (default utilities only). CLAUDE.md and org/XXX.md are LOCKED. COMMIT A WORK-IN-PROGRESS COMMIT AS SOON AS A FILE EXISTS, and again after each criterion passes. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~134/NFRA_CTLPLN.TO-CT-av-1.intake-signed-waiver-for-a-failed-check.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W145-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working. A WARN from safe-commit that the client-data check had no account-id list is the standing WARN-only state (ruled): quote it in your report, file no row for it. When your own change turns a neighbouring suite red, say so in your report with the suite's whole last line: the issuer re-runs every suite that imports what you changed at the merge. The grant for edits is exactly your `<paths>`; a file the census names that is outside them is a BLOCKING row and a stop on that file. Editing `.owned-paths.yaml`: change only the two things in step 4. NEVER run a deploy, an apply, an `aws` write, or `record-terraform-deploy.sh` / `build-and-upload.sh` against the real world.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTca1-AC1" cell_refs="CT-ca-1"><invocation>python org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~145/atomic_check.py</invocation><expect>ok=True</expect></criterion>
`CTca1-AC1` -- 240 of 240 function files equal the base map's entries, the map is gone, the re-run census reads `other=0`, and no live reader or writer still names the old path (base: the script does not exist); report the whole last line with its denominator.

<criterion id="CTca1-AC2" cell_refs="CT-ca-1"><invocation>python org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~145/atomic_check.py --suites</invocation><expect>ok=True</expect></criterion>
`CTca1-AC2` -- every suite that named the map and was green at the base is green after (base: the script does not exist); report the whole last line and the list of suites red at the base.

<criterion id="CTca1-AC3" cell_refs="CT-ca-1"><invocation>python org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~145/atomic_check.py --tf-static</invocation><expect>ok=True</expect></criterion>
`CTca1-AC3` -- the three `locals.tf` files are fmt-clean (checked as FILES: amendment 1), read the folder through `fileset`, and build the same 240 objects the map held (base: the script does not exist); report the whole last line.
</proof_of_spec>

<expected_criteria>CTca1-AC1,CTca1-AC2,CTca1-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 280` (`--suites` may need more: run each suite under its own `timeout 120` inside the script and say so; if the whole run hits the bound, run it a second time and report both). Also run `python .tools/tests/test_round30_function_map.py` and the census's `--selftest` and report their whole last lines. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~145/NFRA_CTLPLN.TO-CT-ca-1.lambda-source-map-atomic-split.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTca1-AC1,CTca1-AC2,CTca1-AC3` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round30.md</decomp_doc>
<owned_cells>CT-ca-1</owned_cells>
</decomp_ref>

<paths>
infra/aws/lambda/ci/function-map/
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/lambda/ci/build-and-upload.sh
infra/aws/lambda/ci/record-terraform-deploy.sh
infra/aws/lambda/ci/build-nodejs-lambda.sh
infra/aws/lambda/ci/deployed-drift-classify.py
infra/aws/lambda/ci/record-deploy-scope.py
infra/aws/lambda/ci/release-census.py
infra/aws/lambda/ci/source-map-staleness-census.py
infra/aws/lambda/verify-local.sh
infra/aws/lambda/investor-reporting/_authz/routetable.py
infra/aws/terraform/investor-reporting/account-return-daily/locals.tf
infra/aws/terraform/investor-reporting/reporting-gold-iso/locals.tf
infra/aws/terraform/investor-reporting/reporting-publish-iso/locals.tf
.github/workflows/lambda-deploy.yml
.tools/deploy_ledger.py
.tools/check-lambda-layer-deps
.tools/naming-gate.py
.tools/parity-gates.sh
.tools/backfill-lambda-iam-mapping.py
lib/opal_lambda_map.py
lib/opal_naming.py
lib/opal_naming_scope.py
lib/opal_lgctfm.py
org/modules/graph/extract_iam.py
org/modules/graph/extract_s3.py
org/modules/graph/extract_eventbridge.py
org/modules/graph/lambdamap_cli.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p170_filled_reader.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p172_repin_after_reader.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r136/p136_sourcemap.py
org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/live_walk/repin_source_map_rows.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/battery_ib_rte_4.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/battery_ib_rtf_1.py
org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~140/source_map_census.py
org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~140/LAMBDA_SOURCE_MAP_CONSUMER_CENSUS.md
.owned-paths.yaml
.tools/tests/test_round30_function_map.py
.tools/tests/fixtures/
.tools/tests/test_round19_register.py
infra/aws/lambda/ci/test_record_deploy_scope_arms.py
infra/aws/lambda/ci/test_record_terraform_deploy_scope.py
infra/aws/lambda/ci/test_render_ports_packaging.py
infra/aws/lambda/ci/tests/test_build_and_upload_verify.sh
infra/aws/lambda/ci/tests/test_build_only.sh
infra/aws/lambda/ci/tests/test_build_restore_fails_loud.sh
infra/aws/lambda/ci/tests/test_record_terraform_deploy_paths.sh
infra/aws/lambda/ci/tests/test_source_map_filled_named_accounts.py
infra/aws/lambda/ci/tests/test_source_map_filled_reader_installed.py
infra/aws/lambda/investor-reporting/_authz/tests/test_unguarded_census.py
infra/aws/lambda/investor-reporting/_contracts/tests/test_seam_paired.py
infra/aws/lambda/investor-reporting/account-dim-cot/tests/test_package_resolves.py
infra/aws/lambda/investor-reporting/holdings-performance/tests/test_zip_registry_resolves.py
infra/aws/lambda/investor-reporting/holdings/tests/test_w1_s16_advisor_firm_bound.py
infra/aws/lambda/investor-reporting/narrative/tests/test_served_error_path.py
infra/aws/lambda/portal_data_proxy/tests/test_route_firm_fence.py
infra/aws/lambda/bd-pipeline/bd-49f-freshness-probe/tests/test_content_assertion.py
infra/aws/terraform/shared-infra/tests/derive_fence_row_shape.py
org/modules/graph/test_iam_v4_024_fp_elimination.py
org/modules/graph/tests/test_lambdamap.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing; the deploy path it edits is exercised by the issuer's plans, not by the worker.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no network request by the worker; the Terraform roots are edited as text and checked with `terraform fmt -check` only; the issuer runs `terraform plan` (read-only) on the three roots before the merge.
comp-adversary: RUN -- a half-split tree merged (the cell is ONE commit; the issuer merges the whole branch; the drain re-checks the map is byte-unchanged since the base and regenerates if a Lambda deploy merged mid-cell); a consumer missed (the census re-run at the cut must read `other=0` and `live_old_path_users=0`; a file the census names outside the grant is a BLOCKING stop); a silent reader still silent (the four named readers and the two gates fail loud: unit-tested); a writer re-creating the aggregate (`battery_ib_rtf_1.py` retired; the map absent is an AC1 condition); the Terraform expression building a different map (AC3 recomputes 240 of 240 from the folder); a suite red by the change (AC2); the lane grant lapsing (`.owned-paths.yaml` re-pointed to the folder; validate before and after); the worker editing a policy, a deploy or a running thing (forbidden); BLIND: a reader outside this repository (a runtime S3 reader, an external CI, another repository) is not seen: accepted by the CTO (round-29 ruling 3), the first real Lambda deploy after the merge is the live proof and the issuer reads it.
risk: WORLD -- the deploy path (build, record, CI workflow), the Terraform locals of three production roots and two commit-time gates read this map; no apply, deploy or AWS call is made by the cell, and the Terraform effect is checked by plan before the merge.
lane: the <paths> block IS the grant (worker RULING 1) for every listed file, including `.owned-paths.yaml` for exactly the two lines named in step 4. The CTO ruled the design, the one-commit atomicity, `_last_deploy_recorded` dropped and the owner entry (round-29 analysis rulings 1-3, msg 109721).
</preflight>

Base checks, dry-run by the issuer before the cut: CTca1-AC1 FAIL as expected (the script does not exist); CTca1-AC2 FAIL as expected (the script does not exist); CTca1-AC3 FAIL as expected (the script does not exist).
Source: CTO round-29 analysis rulings 1-3 and enrichment item 1; stage-1 census and proposal (CT-bb-1, merged 20ed36c47d); rows W140-S2, W140-S3, W140-S5 and C-S102.
