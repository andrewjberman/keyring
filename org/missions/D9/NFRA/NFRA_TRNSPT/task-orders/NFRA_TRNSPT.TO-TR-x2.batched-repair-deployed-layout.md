# TO NFRA_TRNSPT.TO-TR-x2 -- the batched repair: package-qualified imports, universal newlines, listing fakes, proved in the deployed layout

<to_id>NFRA_TRNSPT.TO-TR-x2</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~1</issued_to>
<issued_by>2.0.0_SA_COO~T</issued_by>
<issued_date>2026-09-30</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>transcripts</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `TR-x-2` (`decompositions/NFRA_TRNSPT_DECOMP_R2.md`) |
**outcome_ref:** FWD-1, FWD-7 | **depends_on:** TR-f-2, TR-d-2, TR-w-2, TR-v-2 (all drained to CLOUD and merged into your branch before this order is released)

---

## WORKER FACE

### THE CELL

`TR-x-2`, the round's one batched repair cell (CTO analysis ruling 6): "The collision (two packages each exposing top-level
`land_bronze` and `pull`) is the same shape as a deployed Lambda importing both; the fix is package-qualified imports or unique module
names, and the criterion imports the Lambda's modules from its built bundle (the deployed-layout issuer rule, 103370-103374), not only a
green pytest. S6's CRLF fixture split and S8's missing `list_objects_v2` on the fakes ride the same cell." CTO rule 103374: "any cell whose
diff changes an import in a script that runs from a deployed code prefix ... carries one criterion that imports the module from the deployed
layout itself, on the runner or on an exact extract of what the deploy ships, printed."

**Measured at the cut (c31230ea02):**
- `python -m pytest data/transcripts/scripts/tests` in ONE process: `SUITE-RED passed=95 failed=23` (each file green alone except the S6/S8
  cases). Cause (S7): `teams/pull.py` and `outlook/pull.py` put their own directories on `sys.path` and `import land_bronze` (and
  `gateway_client`, `criterion`) as BARE top-level modules; the tests do the same; the first loaded shadows the other.
- S6: `test_teams_parse_silver.py::test_missing_metadata_cue_leaves_wall_clock_null_with_warning` splits a fixture on a bare `"\n\n"`; on
  this `core.autocrlf=true` checkout every fixture reads CRLF, so it finds no boundaries. Every test fixture under
  `data/transcripts/scripts/tests/fixtures/` reads CRLF here.
- S8: `test_teams_pull.py` (`FakeS3`) and `test_pull_handler.py` (`_MemS3`) lack `list_objects_v2`; with `parse_silver` now beside
  `pull`, `pull.run(with_silver=True)` runs the silver hop, whose `parse_and_write` lists the bronze prefix.
- The Lambda bundle (`infra/aws/lambda/transcripts-pull/build.sh` -> `dist/transcripts-pull.zip`, with `data/transcripts/scripts/` inside it)
  loads bare `criterion`, `gateway_client` and `land_bronze` when `handler` and both pulls are imported from an extract of the zip.
  `handler.py` imports `from data.transcripts.scripts.teams import pull` then `import gateway_client` / `import land_bronze` bare.

**Build:**
1. Every module under `data/transcripts/scripts/teams/` and `.../outlook/` imports its siblings package-qualified
   (`from data.transcripts.scripts.teams import land_bronze`, etc.) and no module inserts its own directory into `sys.path`. Keep each
   CLI runnable as `python data/transcripts/scripts/<pkg>/<module>.py ...` from the repo root (a small repo-root `sys.path` insert at
   the top of a `__main__` block is acceptable; a sibling-directory insert is not). Every existing CLI line and exit code is unchanged.
2. Tests import package-qualified, never bare; `handler.py` imports package-qualified; `build.sh` unchanged unless the bundle needs a
   file it lacks (state why).
3. **AMENDED 2026-09-30 ~23:0xZ by the issuer (grant widened to `.gitattributes`):** add ONE block to the repo's `.gitattributes`
   (append only; never edit an existing line) with a comment naming this order and rows S6 / W1-S6 / the assets lock:
   `data/transcripts/assets/** text eol=lf` and `data/transcripts/scripts/tests/fixtures/** text eol=lf`. Measured at the amendment:
   every pinned asset's sha256 in `data/transcripts/assets/ASSETS.lock.json` equals the committed LF blob and differs from this
   `core.autocrlf=true` checkout's CRLF bytes, so `test_assets_lock.py::test_every_pinned_sha_matches` fails here for the same reason as
   S6's fixture split. After adding the rule, re-materialise those paths in YOUR worktree (`git rm -r --cached -q` + `git checkout --`
   on the two directories, or delete the files and `git checkout --` them) so they read LF, and state the command in the report.
   Keep universal-newline reads where a test splits on newlines, too (defence in depth).
6. **AMENDED:** round 1's `test_outlook_bronze.py::test_tables_source_recorded` asserts the retired tables label; TR-f-2 made the label
   `assets+registry` (row W1-S6). Update that assertion to the new label; change nothing else in that test.
4. Both test fakes gain `list_objects_v2` (with `Prefix` and pagination fields), and the seam is ASSERTED: a test runs
   `pull.run(..., apply=True, with_silver=True)` over the TR-t-1 fixture on the fake S3 and asserts a silver parquet key for each landed
   transcript (S8), replacing the round-1 SILVER-SKIPPED assumption.
5. Do not change any module's behaviour beyond imports, newline handling and the fakes; every round-1 and round-2 test must pass in one
   process.

### ACCEPTANCE

<criterion id="TR2-x2-AC1" cell_refs="TR-x-2"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T/R2_CHECKS/r2_suite_check.py</invocation><expect>SUITE-GREEN</expect></criterion>
`TR2-x2-AC1` -- the whole transcripts suite passes in ONE pytest process.

<criterion id="TR2-x2-AC2" cell_refs="TR-x-2"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T/R2_CHECKS/r2_bundle_import_check.py</invocation><expect>BUNDLE-IMPORT-OK</expect></criterion>
`TR2-x2-AC2` -- the deployed layout (CTO rule 103374): build.sh's zip, extracted exactly, imports handler and both sources' pull modules as
distinct modules with no bare top-level sibling loaded. (Read the check first: it builds with Git Bash via `.tools/git_bash_resolver.py`.)

<expected_criteria>TR2-x2-AC1,TR2-x2-AC2</expected_criteria>

Dry-run at the base c31230ea02: AC1 `SUITE-RED passed=95 failed=23`; AC2 `BUNDLE-IMPORT-FAIL AssertionError: bare top-level modules loaded:
['criterion', 'gateway_client', 'land_bronze']` -- FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **WORLD by path (the Lambda handler); NOTHING is applied.** Never `terraform apply`, never `safe-apply`, never deploy; `dist/` is a
  build product and is never committed.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `NFRA_TRNSPT-W1-S<k>`, next unused), and do not weaken a test to pass.

<paths>
data/transcripts/scripts/teams/
data/transcripts/scripts/outlook/
data/transcripts/scripts/tests/
infra/aws/lambda/transcripts-pull/handler.py
infra/aws/lambda/transcripts-pull/build.sh
.gitattributes
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP_R2.md</decomp_doc> (round 2), cell `TR-x-2`.
<owned_cells>TR-x-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR2-x2-AC1, TR2-x2-AC2. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~1/NFRA_TRNSPT.TO-TR-x2.batched-repair-deployed-layout.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR2-x2-AC1,TR2-x2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the import scheme chosen, the files touched, the SUITE and BUNDLE lines, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule touched; TR-i-1's desired rule is unchanged and unapplied.
comp-iam: RUN -- infra/aws/terraform/transcripts/main.tf read at the cut: 1 KMS key policy with 2 statements and 1 reader principal (Andrew's IAM user), 1 bucket policy with 2 Deny statements; BLIND: the live IAM plane outside this root (0 of the account's roles read). This cell writes no bucket and applies nothing.
comp-adversary: RUN -- the union's two measured failures (suite 23 red; the bundle's bare modules) are its criteria, dry-run at the base.
lane: the <paths> block IS the grant; infra/aws/** is the AE lane at APPLY, which this order never reaches.
</preflight>

Source: CTO round-1 analysis @acd1033e60 ruling 6 and section 4 item 3; rows S6, S7, S8; CVO Q2; CTO rule 103374; decomposition round 2 cell TR-x-2.
