# NFRA_MCPINDEX task order -- `MX-c-29` -- a regeneration that would DROP a registry row REFUSES, naming each dropped row

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-c-29</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-c-29</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~52</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or grant change; the generator and its checks run in temp folders and read repo files and git objects.
comp-adversary: DECLARED-NOT-APPLICABLE -- the checks plant a drop and require a refusal that names it; a run with a short allow file is the control.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-c-29` (round 21, R21-1 of the round-20 analysis)

Work in your own worktree (cut from `box/sitez`; its sparse cone already holds `workflows`, `lib`, `.tools`, `infra/aws/ec2`, `infra/logic` and the project folder; you may add nothing else). Every path is relative to its root. The file you change is `workflows/atom_decomposition/gen_silver_rows.py`.

**Why.** `gen_silver_rows.py` can write two registry files when given `--registry-file` (`infra/logic/registry/legacy_addresses.json`, whose `catalog-*` rows it owns and replaces) and `--fork-registry-file` (`catalog_fork_keys.json`, which since round 20 it merges). The naming gate admits a catalog literal only as a whole string held in these files at HEAD, so a regeneration that silently REMOVES a row can make the next catalog commit fail. The issuer measured today's tracked state: a regeneration with `--registry-file` drops 36 of the 143 `catalog-*` rows. The CTO ruled (round-20 analysis): the regeneration must REFUSE when any registry row that existed before is absent after, naming each dropped row; detecting it afterwards is not enough.

**What to build** (in `gen_silver_rows.py`):

1. **The guard.** For each registry file named on the command line (`--registry-file`: a row's id is its `key`; `--fork-registry-file`: a row's id is its hashed contract id in `rows`), compute the document the run is about to write, then the set of row ids present in the EXISTING file and absent from that document. Do this for both files BEFORE writing either. If any row would be dropped and is not allowed, print one line per such row to stdout, exactly `REGISTRY-DROP <file name> <row id>` (the file's base name, one space, the id), write NOTHING to either registry file, and exit 2. The entries folder is written as today (a refusal concerns the registries only), but a refusal must leave both registry files byte-equal to before.
2. **The escape.** New option `--allow-registry-drop FILE`: a JSON list of row ids (strings) the issuer accepts the run to drop. A row id in the list is dropped silently (print one summary line `REGISTRY-DROP-ALLOWED <n>`); a row not in the list is refused as above. A file that does not exist or does not parse as a JSON list of strings exits 2 with a message. An id listed but not dropped is ignored.
3. A run that drops nothing behaves exactly as today (no extra output beyond a one-line `REGISTRY-DROP none`).
4. **Tests**: a NEW file `workflows/atom_decomposition/tests/test_registry_drop_guard.py` with at least 6 tests on small inline fixtures (temp folders; copy or create tiny registry files): a drop is refused and named; a refusal writes nothing; an allowed drop passes and is summarised; an allow file listing only some of the dropped rows still refuses the rest, naming exactly those; a bad allow file exits 2; a run that drops nothing is unchanged.

### Steps

0. Control (must pass before you start): `cd workflows/atom_decomposition && PYTHONPATH=. python -m pytest -q -p no:cacheprovider tests/test_gen_silver_rows.py tests/test_regen_preserves.py`.
1. Make the change and the tests. Run the same line with `tests/test_registry_drop_guard.py` added (all pass).
2. Run the three criteria in section 4 (each runs the generator into TEMP folders, about 10 seconds; they pass `--hand-overlay` and both registry flags on temp COPIES).

## 2. BOUNDS

1. You change only the files in `<paths>`. NEVER run the generator with `--out` or a registry flag pointing into the repo's `catalog_entries/` or `infra/logic/registry/`; use temp folders and copies. No entry file, no registry file, no catalog, no emitter change. No deploy. No push.
2. No firm or product name is typed as a whole-string literal in code (the naming gate refuses a new hand-kept token). Run `python .tools/naming-gate.py --diff <your diff> --enforce --staged-paths <file>` on your code commit before you make it; it must exit 0.
3. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project (row Z-W34-S8): your proof instance is one.
4. The checks are `deliverables/2.0.0_SA_COO~MI/round21/checks/c29.AC1.sh`, `c29.AC2.sh`, `c29.AC3.sh` (python `c29_check.py`). Read them for exactly what is graded. Do not edit them.
5. Another worker (`~53`) edits the catalog emitter, `members.yaml` and two test files at the same time (no shared file).
6. Do not overwrite another worker's `session_log.json` in a shared deliverables folder: name yours `session_log_MX-c-29.json`.
7. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
workflows/atom_decomposition/gen_silver_rows.py
workflows/atom_decomposition/tests/test_registry_drop_guard.py
workflows/atom_decomposition/tests/test_gen_silver_rows.py
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~52/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W52-S<k>`;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp (`date -u +%FT%TZ` at filing).

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 1)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-c-29" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round21/checks/c29.AC1.sh; echo "exit=$?"</invocation><expect>run 1 (no allow file): exit 2; REGISTRY-DROP rows printed 36; run 2 (allow file = the printed keys): exit 0; rows really dropped from legacy_addresses.json 36; run 3 (allow file lacks one key): exit 2; every CHECK ok -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-c-29" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round21/checks/c29.AC2.sh; echo "exit=$?"</invocation><expect>planted run: exit 2; every CHECK ok -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-c-29" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round21/checks/c29.AC3.sh; echo "exit=$?"</invocation><expect>pytest rc=0 on test_registry_drop_guard.py, test_gen_silver_rows.py and test_regen_preserves.py; the new file holds at least 6 tests -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~52/NFRA_MCPINDEX.TO-MX-c-29.regeneration-refuses-to-drop-a-registry-row.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance. (The expect fields are prose; the checker matches `expect` as a regex against your recorded output: encode the literal printed tokens, replacing digits with `[0-9]+` where counts may differ, and disclose that in a row. Pin each artifact row to the commit that carried it, not `PENDING-THIS-COMMIT`, when the file was committed before the instance.)
2. Do NOT flip the order's status; the issuer does.
3. Commit through `.tools/safe-commit.sh`, message files written with the Write tool, each ending `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>` and stating push state LOCAL, in two commits: (i) `gen_silver_rows.py` and the test file; (ii) the proof instance.
4. Report once, with: the change by function; the AC1 to AC3 DENOMINATOR and CHECK lines verbatim; the first three printed `REGISTRY-DROP` lines; the test count; the two commit shas.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 21, worker ~52, an independent chain. Source: CTO round-20 analysis @3f03a45f83 (R21-1, msg 35237) on the CVO slug ADJUDICATION_v16 @b0966935f7. The base dry-run, in a SPARSE worktree cut like the worker's: `c29.AC1` FAIL (the option does not exist: the base run drops 36 rows silently), `c29.AC2` FAIL, `c29.AC3` FAIL (no test file). The 36 are `catalog-*` rows of `legacy_addresses.json`; the fork registry loses none since MX-c-27 (it merges).

**AMENDMENT A1 (2.0.0_SA_COO~MI, 2026-10-16 ~20:4xZ; no gate limb graded it: a path grant and a worker-face note on an issued order).** Worker ~52 finished with AC3 FAIL and filed `NFRA_MCPINDEX-Z-W52-S3`: two `IntegrationTests` in `tests/test_gen_silver_rows.py` (`test_rc_zero_and_180_files_with_unique_names`, `test_contract_ids_are_hashed_and_registry_holds_one_entry_per_row`) run the generator on the round-14 pinned fixture against a COPY of the tracked `legacy_addresses.json`; that fixture makes 180 rows, so the guard now refuses the 36 other `catalog-*` rows (exit 2). The guard is right and the fixture predates it. The test file is added to `<paths>`. Remedy for the worker re-seated on this slot (its commits `4e9017ac2f` and `cf8dae11e3` are inherited state on the branch): in `IntegrationTests.setUpClass` only, write an allow file into `cls.tmp` holding every `key` of the copied `legacy_addresses.json` that starts with `catalog-`, and pass it as `--allow-registry-drop <file>`; change no assertion and no other test. Then re-run c29.AC1 to AC3 (all three must PASS), refresh the proof instance rows for AC3 (and pin every row to the commit that carried it), and commit the test change and the instance in two commits as before. Row S3 is dispositioned by this amendment.

<status>issued</status>
<round>21</round>
<workstream>ASSETS</workstream>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

**ISSUER RULING (2.0.0_SA_COO~MI, 2026-10-16 ~20:5xZ) -- MX-c-29 COMPLETE.** Worker ~52 added to `gen_silver_rows.py` `plan_registry` and `plan_fork_registry` (the document a run is about to write, no write), `load_allow_drop`, `dropped_rows`, `check_registry_drops` and `write_registries` (the guard runs before any registry byte is written; a refusal prints `REGISTRY-DROP <file> <id>` per row and returns 2), and the option `--allow-registry-drop FILE`; 9 tests in `test_registry_drop_guard.py` (`4e9017ac2f`). It finished AC1 PASS, AC2 PASS, AC3 FAIL (2 of 60): row Z-W52-S3, the order's own omission of the integration-test fixture from its paths. A1 (`e48fe1117d`) granted the file; the slot was re-seated and `setUpClass` now passes an allow file (`a1e42d21dc`, proof `c49ea30171`). Drained by `safe-merge.sh` at `28d19f4834` (6 files, 0 foreign). Issuer re-run on the merged tree: c29.AC1 PASS (36 rows named, 36 really dropped with the allow file, one key withheld refuses naming exactly that key), c29.AC2 PASS (the planted `catalog-planted-row-c29` refused alone), c29.AC3 PASS (60 passed, 9 new); the atom_decomposition suite 372 passed; ruff clean; the proof instance VALID inside the worker tree. Rows S3 and S4 are dispositioned by `NFRA_MCPINDEX-Z-S134`. The CTO's hold on the catalog emit (until R21-1) is released by this flip. Gate limb that graded this ruling: the flip-needs-a-VALID-instance limb of to-pipeline-gate.

<status>complete</status>
