# TO ADVI_COTBKF.TO-CB-ch-1.rebuild-active-set-scripts -- round 86 CB-ch-1: the lost round-85 build scripts rewritten from their record, committed, re-run from the commit, and both output files re-hashed equal to the committed V2 and V3

<to_id>ADVI_COTBKF.TO-CB-ch-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~169</issued_to>
<issued_by>2.0.0_SA_COO~C1</issued_by>
<issued_date>2026-10-15</issued_date>
<status>superseded</status>
<superseded_by>ADVI_COTBKF.TO-CB-ci-6 (round 87): V3 reproduces byte for byte and V2 to 41,793 of 41,826 rows after six repairs; the cause that remains and can be fixed (row order depends on PYTHONHASHSEED, row ADVI_COTBKF-D1-W169-S4) is the cell CB-ci-6's; the residual 33 pinned-only and 32 rebuilt-only rows are named in REBUILD_RECORD.json. Set by 2.0.0_SA_COO~C1 as issuer.</superseded_by>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>86</round>
<workstream>~C1</workstream>

**Directive:** D8 | **Fabric:** dell1 (placement DELL1) | **Decomp cell:** `CB-ch-1` (`decompositions/ADVI_COTBKF_DECOMP.round86.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**The cell.** In round 85 a worker built two CSV files from S3 tables with scripts that were never committed; the scripts are lost. The two files survive, committed and hashed. You rewrite the scripts from the written record of their rules, commit the scripts, run them FROM THE COMMIT, and compare the two outputs byte for byte with the committed files. The files are the truth; the scripts must reproduce them or say exactly where they cannot.

**Read first (all under the repository root `C:/dev/ajb_workspace`):**
1. `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~168/ACTIVE_SET_V2_RECORD.md` and `ACTIVE_SET_V2_RECORD.json` in the same folder: the definition of "open", the window rules (a Commonwealth window opens at the first non-zero running balance and closes on the trade that returns it to zero; a Black Diamond window is a run of consecutive gold keys with a non-zero row; a joined row is one (account, CUSIP) pair held on both sides), the Commonwealth predecessor chain, the cash-equivalent handling, the `not_established` rows, the `sources` list (every S3 prefix read, with its denominator), and the exact reverse-match classes.
2. `org/missions/D8/ADVI/ADVI_COTBKF/task-orders/ADVI_COTBKF.TO-CB-cg-1.set-and-reverse-match-open-accounts.md` (the round-85 order, items 1 to 5: the columns, the match bases, the reason codes) and `org/missions/D8/ADVI/ADVI_COTBKF/task-orders/ADVI_COTBKF.TO-CB-cd-1.active-set-and-reverse-match.md` (the round-82 method, items 2 and 3).
3. `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~167/NONE_REASON_LIST.md` and `NONE_REASONS_RECORD.json` (the closed list of reason codes, its tests in order, migration date M = 2026-06-23) and `data/assets/scripts/silver/commonwealth_signs.py` (the one signed-quantity rule).
4. The two target files, committed at commit `4d427d3bbb`: `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ACTIVE_COTTONWOOD_SET_V2.csv` (41,826 rows, sha256 `5cef7ab0c9e10fe299cb757d4dba31792d069bad35f7250defa76e18773046ae`) and `REVERSE_MATCH_V3.csv` in the same folder (860 rows, sha256 `0783f088aecbf29e46751aa5d80239b8aa53f16484778162e34ee1c09783c66f`). Read their headers and a few rows to fix the column order, the date format, the sort order, the line ending and the quoting. They carry raw account numbers; those never leave the two files (see BOUNDS).

**Your items.**

1. **Write the build script** `data/assets/scripts/silver/cotbkf_active_set_v2.py`, one file, no dependency beyond what the repository already imports (pandas, pyarrow, boto3, the stdlib). It reads the S3 tables the record's `sources` lists (read-only), applies the rules above, and writes the two CSVs to a directory given by `--out`. It takes no account number as input. It carries no account number, no name and no value in its source. Give it a `--out` directory argument and nothing else it must be told: the snapshot date, the migration date and the floor are constants in the file with the record's values.
2. **Write the unit test** `data/assets/scripts/silver/tests/test_cotbkf_active_set_v2.py`: small stub frames (no S3) that prove four rules, one test each: a Commonwealth window opens at the first non-zero running balance and closes on the return to zero; a Black Diamond window is a run of consecutive gold keys with a non-zero row; "open" counts cash-equivalent rows and excludes zero-unit-only accounts; a `none` row always carries a reason code from the closed list. Stubs use made-up ids like `A1`; no real account number.
3. **Commit the script and the test FIRST** (commit rule below), BEFORE running the build. Then run the build from the committed file: `python data/assets/scripts/silver/cotbkf_active_set_v2.py --out C:/dev/_cotbkf_rebuild_20261015`. Create the directory if absent. Do not run it long under a short timeout: this is a build step, not a criterion; it reads about 135 gold keys and 14 transaction parts.
4. **Compare byte for byte.** Compute the sha256 of each written file and compare with the two pins above. If both are equal, you are done with the build. If either differs, try the cheap causes first, one at a time and each re-run from a new commit of the script: row order, line ending (LF), final newline, quoting, date format, the `held_to` word `open`, the semicolon cell in `predecessor_key`. After at most three such repairs, STOP and write what differs: rows only in one file, rows only in the other, columns that differ, counted (counts and column names only, never a row or an id). A file that does not reproduce is not forced and not edited to match.
   **AMENDMENT 1 (2.0.0_SA_COO~C1, 2026-10-15, after the worker's first report): the cap in this item is raised by THREE further repairs, aimed at the measured diff.** V3 is byte-equal. V2 is 41,808 rows against 41,826: 41,487 rows equal, 339 pinned-only, 321 rebuilt-only; on the paired rows ticker differs on 285 and held_to on 48. Spend the three repairs on those: how a blank-CUSIP row is keyed and which ticker it carries (the record's `not_established` rows are keyed by ticker and name), and which side's window end wins on a joined row. Each repair is a new commit of the script; after the third, stop and report the new diff_summary. Criteria, paths and bounds are unchanged; AC1 still grades the pins.
5. **Write the record** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~169/REBUILD_RECORD.json` with exactly these top-level keys: `script_path`, `script_blob` (the output of `git rev-parse HEAD:data/assets/scripts/silver/cotbkf_active_set_v2.py` AT THE COMMIT YOU RAN FROM, after your last repair), `run_command`, `files` (a list of 2: `{"name", "path", "rows", "sha256", "pinned_sha256", "equal"}`), `out_dir`, `repairs` (a list of what each repair changed, one line each, may be empty), `diff_summary` (counts only; `null` when both files are equal), `sources_read` (each S3 prefix with the number of objects listed and read), `not_established`. Write a short `REBUILD_RECORD.md` beside it. Neither carries an account number, a name or a value.

### ACCEPTANCE

<criterion id="CB86ch1-AC1" cell_refs="CB-ch-1"><invocation>python -c "import json,hashlib;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~169/REBUILD_RECORD.json',encoding='utf-8'));pins={'ACTIVE_COTTONWOOD_SET_V2.csv':'5cef7ab0c9e10fe299cb757d4dba31792d069bad35f7250defa76e18773046ae','REVERSE_MATCH_V3.csv':'0783f088aecbf29e46751aa5d80239b8aa53f16484778162e34ee1c09783c66f'};ok=[hashlib.sha256(open(f['path'],'rb').read()).hexdigest()==pins[f['name']] for f in d['files']];print('V2-REBUILD files=%d sha256_equal=%s'%(len(d['files']),all(ok) and len(ok)==2))"</invocation><expect>V2-REBUILD files=2 sha256_equal=True</expect></criterion>
`CB86ch1-AC1` -- the two rebuilt files, read from disk now and hashed now, equal the two committed pins (the pins are typed in this invocation, not read from your record).

<criterion id="CB86ch1-AC2" cell_refs="CB-ch-1"><invocation>python -c "import json,subprocess;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~169/REBUILD_RECORD.json',encoding='utf-8'));b=subprocess.check_output(['git','rev-parse','HEAD:'+d['script_path']]).decode().strip();print('V2-SCRIPT-COMMITTED blob_equal=%s'%(b==d['script_blob']))"</invocation><expect>V2-SCRIPT-COMMITTED blob_equal=True</expect></criterion>
`CB86ch1-AC2` -- the script at HEAD is the script the record says produced the files: it is committed, and the run came from the commit.

<criterion id="CB86ch1-AC3" cell_refs="CB-ch-1"><invocation>python -m pytest data/assets/scripts/silver/tests/test_cotbkf_active_set_v2.py -q</invocation><expect>4 passed</expect></criterion>
`CB86ch1-AC3` -- the four window and definition rules hold on stubs.

<expected_criteria>CB86ch1-AC1,CB86ch1-AC2,CB86ch1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below and the folder `C:/dev/_cotbkf_rebuild_20261015/` (the two rebuilt CSVs and nothing else). You change no other file. You do not edit `ACTIVE_COTTONWOOD_SET_V2.csv`, `REVERSE_MATCH_V3.csv`, the round-82 pair, `NONE_REASON_LIST.md`, any existing script or test, or the scan test.
- **AWS: READ-ONLY, through the `.tools/aws` shim,** of exactly the prefixes `ACTIVE_SET_V2_RECORD.json` `sources` names: list each prefix once (state each listing's denominator) and read what it lists. No write, delete or serve; no other bucket or prefix; not the restricted CRM prefix. If a read is refused, record the exact error, mark that part `not_established`, and stop on the dependent items. Do not run `aws sts get-caller-identity`.
- **Account numbers and values are never printed, committed or sent**, except as they sit in the two outside CSVs. Reports and records carry counts, dates, codes and CUSIPs only. Do not list or open `C:/dev/_cotbkf_private_evidence_20261009/`. Do not look for the old salt.
- After your last commit run `env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests/test_cotbkf_no_account_ids.py -q -s` and put its DENOMINATOR line in your report. It must read zero new hits: your committed files carry no account number.
- **NEVER** `--apply`, `--remint`, an S3 write or delete, a vendor call or a Black Diamond API call. No push. No gate override and no `--force`. Do not weaken, delete, xfail or skip any test. Run outputs and scratch go under the worktree's `.scratch/` (never committed) or the one outside folder named above. A script is never left only in scratch: that loss is the reason for this cell.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id `ADVI_COTBKF-D1-W169-S<k>` (k from 1), `"fabric": "dell1"`, `surfaced_at` read from the clock (`date -u +%FT%TZ`), APPENDED to the channel file with `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with an editing tool.

<paths>
data/assets/scripts/silver/cotbkf_active_set_v2.py
data/assets/scripts/silver/tests/test_cotbkf_active_set_v2.py
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant for the repository. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round86.md</decomp_doc> (round 86), cell `CB-ch-1`.
<owned_cells>CB-ch-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB86ch1-AC1, CB86ch1-AC2, CB86ch1-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~169/ADVI_COTBKF.TO-CB-ch-1.rebuild-active-set-scripts.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB86ch1-AC1,CB86ch1-AC2,CB86ch1-AC3` BEFORE the flip. All three criteria are mechanical. An artifact already committed and not changed in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`. Declare the two outside CSVs in `declared_exclusions` if the checker refuses them as file artifacts. **YOU flip your own order `<status>` to `complete` in the commit that carries the proof instance, and only when every criterion PASSES** (the flip is inside your grant: the order's own face is lane ANY). If AC1 FAILS, leave the order `pending`, say so, and stop.
</proof_of_spec>

**REPORT:** FIRST the sha256 and row count of each rebuilt file against its pin. Then: the script's commit hash; each repair and its commit; the `diff_summary` if any; every S3 read made with its denominator; the three criterion lines; the account-id scan's DENOMINATOR line; what is not established; every gate refusal and hook denial, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read of silver and holdings tables and two files in a scratch folder; nothing is scheduled, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE read-only calls on Opal data under the existing role, as the bounds list them; no write, delete or serve, and no new permission.
comp-adversary: RUN -- the target is a byte-identical reproduction of two committed files, so the check cannot be fooled by a record the worker writes: the pins are typed in AC1's invocation, and AC2 ties the run to the committed blob; BLIND: a script that reproduces the files only because it reads them (the order forbids reading the target files as input; the worker's report names its inputs), and a source table that has changed since 2026-10-14 (the snapshot is dated; a later object would show in the listing denominator).
lane: the <paths> block IS the grant (worker RULING 1). The script and test paths are named explicitly; the outside folder holds only the two rebuilt CSVs.
</preflight>

Source: `1.0.0_SA_CTO~DELL1` ruling @f984c02191 item 1; park record `deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_PARK_RECORD_20261014.md` gap 1; surprise row `ADVI_COTBKF-D2-S137` (the lesson: a build order names its script as a committed path).
