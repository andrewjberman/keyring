# AMGT_RESAPP task order -- `AMGT-rk-100` -- `--no-analyze` on the filings BATCH path (0 model calls with the flag, today's behaviour without it), and the BATTERY half recorded as a MEASURED NEGATIVE (no model call is reachable from `run_battery`); CODE ONLY

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-100</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~100</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order edits one library module and adds one test file; it arms no
  cron, alarm, monitor or cadence, reads no schedule and writes none. The DISABLED `OpalResearch-FilingsAnalyzer`
  Windows task is neither read nor changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or grant is read or changed; no AWS call of any kind is made by
  this order (every test stubs the fetch, the model caller and the writers).
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~100`.** Work ONLY in the worktree whose absolute path is given in your spawn prompt.
Your first act prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and tests that `org/`,
`.tools/` and the paths in section 3 exist (the new test file excepted); if any is absent, STOP with a BLOCKING row.
Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~100;`. **NEVER RUN AN INSTALL.** Never read, show,
diff or check out branch `wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50` -- it holds an exposed credential.

## 1. THE CELL, inlined in full -- `AMGT-rk-100` (round 26, ahead of the B2 run)

**The rulings of record, verbatim.**

1.0.0_SA_CTO~Z msg 24204, 2026-09-22T11:38:55Z, file
`org/mcp/inbox/2.0.0_SA_COO/~Z/read/20260922T113855Z_1.0.0_SA_CTO_Z__ROUND-25_ANALYSIS__AMGT_RESAPP__04f5188.md`,
lines 11-12:

> ROUND 26, cut in one issuance by 2.0.0_SA_COO~Z. Both cells are code only: no pair, no word.
> - (a) `--no-analyze` in lib/research/filings/batch.py. With the flag, a stub that counts calls reads 0 calls to
> analyze.analyze_source. Without it, behaviour is unchanged.

1.0.0_SA_CTO~Z msg 24207, 2026-09-22T11:39:58Z, file
`org/mcp/inbox/2.0.0_SA_COO/~Z/read/20260922T113958Z_1.0.0_SA_CTO_Z_Re_24206__cell__b__RULED__i__--_repeatab.md`,
lines 14-18:

> RULING, cell (a): re-aim it. Your read shows B2 runs through the BATTERY, not batch. So --no-analyze must cover the
> path B2 actually runs:
> - Read whether run_battery, or anything it calls, reaches analyze.analyze_source or any other paid model call.
> - If it does, add the flag to the battery CLI, with this criterion: a stub that counts calls reads 0 with the flag,
> and behaviour is unchanged without it.
> - If it does not, the battery half is a recorded negative: the grep denominator and 0 callers go on the record face.
> - batch.py gets the flag as well, since batch is the CIK path a later run may use. It costs one line.

**THE BATTERY HALF, MEASURED AT THE CUT: A NEGATIVE.** At SITEZ `04f518851d`, an AST read of every import and every
call in the six modules `run_battery` reaches (`lib/research/filings/battery.py` 1363 lines, `fetch.py` 576,
`document.py` 1009, `passages.py` 230, `lib/research/identity/crosswalk.py` 1008,
`integrations/bloomberg/mcp/blp_client.py` 363), against the pattern
`analyze_source|\banalyze\b|anthropic|bedrock|invoke_model|openai|messages\.create`, found **0 model imports and 0
model calls across 6 of 6 files**. `fetch.py`'s lazy imports reach `lib.research.harvest` (store and writers), which is
not a model client. **So the battery CLI gets NO flag in this order.** AC0 re-measures it with its own instrument; if
YOUR read finds ANY model import or call reachable from `run_battery`, STOP with a BLOCKING row. That is a scope change
for the CTO, and you do NOT add a battery flag yourself.

**THE MEASURED STATE of the batch half, at `04f518851d` (SITEZ; `lib/` byte-identical to `8dd72465b6`). RE-READ every
line at your branch HEAD before editing:**

- `lib/research/filings/batch.py` (655 lines):
  - `run_group(group, write_pool, client=None, caller=None, bronze_sink=None)` (`:377`). It fetches once
    (`fetch.build_source_object`, `:397`). For a non-RESOLVED source it returns the UNRESOLVED results (`:399-412`).
    For a RESOLVED source it makes the model call `analysis = analyze.analyze_source(source_object, caller=caller)`
    (`:413`), builds the drafting document (`:414`) and calls `analyze.write_outputs(...)` once per key (`:418`),
    which writes `.analysis.json` and the drafting document (and NOT the source object: that is `fetch.persist`'s job
    since AMGT-rk-91).
  - `main` (`:478`) has flags `--universe --limit --dry-run --plan-only --print-task --write-pool --write-bronze
    --security-key --register-task-xml --skip-fetch`. The fetch loop is `:594-612`, calling
    `run_group(group, args.write_pool, bronze_sink=bronze_sink)` at `:598`, then printing `RAN: <json>` per result and
    the `BATCH DONE: ...` summary at `:609-612`.
- **Tests at the cut** (one pytest call per directory): `lib/research/filings/tests` **86 passed**; `test_batch.py`
  **11 passed**. `test_batch.py:153` calls `batch.run_group(group, write_pool=False, caller=stub)`, so that signature
  must keep working unchanged.
- **Encoding at the cut:** `batch.py` has 0 CRLF and 0 non-ASCII characters.

**ISSUER RULINGS (L5), what you build:**

1. `run_group` gains a keyword `no_analyze=False`, AFTER `bronze_sink`. With `False`, the function is byte-for-byte
   today's path. With `True`, for a RESOLVED source:
   - `analyze.analyze_source`, `analyze.build_drafting_document` and `analyze.write_outputs` are NOT called;
   - one result per key is returned: `{"security_key": key, "status": "FETCHED", "cik": group["cik"], "accession":
     source_object.get("accession"), "analyzed": False, "shared_cik_with": [k for k in keys if k != key]}`.

   The fetch itself, and the bronze sink it carries, are unchanged. The UNRESOLVED branch is unchanged either way.
2. `main` gains `--no-analyze` (`store_true`, default False), passed as `run_group(..., no_analyze=args.no_analyze)`.
   - Without the flag, every printed line is today's.
   - With the flag, the `BATCH DONE` line is replaced by exactly:
     `"BATCH DONE (--no-analyze): %d of %d fetched, 0 analyzed, 0 model calls, %d UNRESOLVED-SOURCE (%d distinct CIK fetched, %d duplicate key(s) served from the same fetch)"`,
     over the `FETCHED` results, all results, the non-`FETCHED` results, `planned["distinct_cik"]` and
     `planned["duplicate_keys"]`.
   - `--dry-run`, `--plan-only`, `--skip-fetch` and the unresolved-write loop are untouched.
3. **Tests**, in ONE new file `lib/research/filings/tests/test_no_analyze.py`. Use pytest style with QUALIFIED imports
   `lib.research.filings.batch` / `lib.research.filings.analyze` / `lib.research.filings.fetch` (W85-S1).
   `fetch.build_source_object` is monkeypatched to return a fixed RESOLVED (or UNRESOLVED) object, and the analyze
   functions are replaced by call-counting stubs. No network, no boto3 client, no model. Names must match AC1:
   - `test_default_run_group_calls_analyze_once_per_resolved_group` -- without the flag, over a 2-key RESOLVED group:
     `analyze_source` is called 1 time, `build_drafting_document` 1 time and `write_outputs` 2 times; statuses are "OK".
   - `test_no_analyze_run_group_makes_zero_model_calls` -- the same group with `no_analyze=True`: `analyze_source`
     0 calls, `build_drafting_document` 0, `write_outputs` 0; 2 results with status "FETCHED", `analyzed` False, and
     the accession carried.
   - `test_no_analyze_unresolved_branch_unchanged` -- an UNRESOLVED source returns the same result list with and
     without the flag (compared as values), with 0 analyze calls either way.
   - `test_main_no_analyze_defaults_off` -- argparse over `main`'s parser: `--no-analyze` defaults False; with it True.
   - `test_main_no_analyze_prints_zero_model_calls` -- `batch.main` over an in-memory universe (monkeypatch
     `batch.load_universe` as the existing `test_bronze_wiring.py` does), with `run_group`'s fetch stubbed. With
     `--no-analyze`, stdout carries `BATCH DONE (--no-analyze):` and `0 model calls`, and the counting stub reads 0.
     Without the flag, stdout carries today's `BATCH DONE: ` line and the stub reads the group count.
   - `test_battery_import_reaches_no_analyze_module` -- in a SUBPROCESS (a fresh interpreter, so no other test's
     import leaks in), `import lib.research.filings.battery` and print whether `lib.research.filings.analyze` is in
     `sys.modules`. It must print False. This is the battery negative, held as a test.

**What this cell does NOT change:** `battery.py` (a WALL -- the negative gives it no flag), `fetch.py`, `analyze.py`,
`document.py`, `lib/research/harvest/**`, every existing test file, the DISABLED Windows task, and any S3 object. No
network call, no model call, no AWS call.

## 2. WHERE THIS CAME FROM

**ROUND 26**, decomposition s.34 (cut by `2.0.0_SA_COO~Z`), on the CTO's round-25 analysis (msg 24204,
`ledger/ROUND_ANALYSIS.round25.md` @`04f518851d`) as amended by msg 24207, which answers the COO's correction msg
24206. The B2 RUN cell (held, on Andrew's word) passes `--no-analyze` wherever it runs `batch.py`; the CTO's msg 24200
(a) keeps model spend off Andrew's card. Andrew-direct ~15:12Z governs one-slug issuance.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/filings/batch.py
lib/research/filings/tests/test_no_analyze.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~100/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-100.filings-no-analyze.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** Reads need no grant. In particular, `battery.py` (which a sibling cell
  of this round is editing) and every existing test file are walls. If an existing test must change to stay green,
  STOP and REFUSE with a row. Scratch is `<your worktree>/.scratch/r100/` only, never committed. The only shared file
  is `INVESTIGATION_v1.md` (append-only; do not isolate it).
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~100 <0.9.0_WK_AMGT_RESAPP~100@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by the Write tool). Never push, merge, rebase, `checkout --`, `stash` or `clean`.

## 4. BOUNDS

**CODE ONLY.** No network call, no EDGAR fetch, no model call, no AWS call of any kind, and no deploy. Never run
`batch.main` or `battery.main` against the live network.
- **Imports in tests use the QUALIFIED `lib.<pkg>.<mod>` names** (W85-S1).
- **Run each test directory in its OWN pytest call.**
- **A script that carries a backslash is a FILE** you write from this order's text verbatim, never an inline
  `python -c` (W84-S1). `ac0.py` carries one (its regex); every script below is a file.
- **The discriminating comparison is pinned to commit `04f518851d`** (Z-S193), never HEAD or a merge-base.
- **THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
  repaired, widened, or satisfied by a route this order did not name, and never by editing a WALL.
- **A COUNT BAR IS READ AT SPAWN AND PRINTS its denominator.** AC0 re-measures every baseline before you edit; every
  later bar is "AC0's value plus N" or "equal to AC0's value", never a number typed here.
- **SURPRISE ROWS:** `AMGT_RESAPP-Z-W100-S<k>`, with `<k>` from 1; `"project": "AMGT_RESAPP"`, `"fabric": "site-z"`.
  Append by textual splice inside the one fenced JSON array; never edit an existing row. A worker names the issuer
  (`2.0.0_SA_COO~Z`) as `disarm_owner`.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 600)

**Script files.** Write each block below to the named file under `<your worktree>/.scratch/r100/`, byte-for-byte,
then run it from the worktree root as the criterion states.

`.scratch/r100/ac0.py`:
```
import ast, re, subprocess
print("pin_object", subprocess.run(["git", "cat-file", "-t", "04f518851d"], capture_output=True, text=True).stdout.strip())
FILES = ["lib/research/filings/battery.py", "lib/research/filings/fetch.py", "lib/research/filings/document.py",
         "lib/research/filings/passages.py", "lib/research/identity/crosswalk.py", "integrations/bloomberg/mcp/blp_client.py"]
PAT = re.compile(r"analyze_source|\banalyze\b|anthropic|bedrock|invoke_model|openai|messages\.create")
imports = calls = 0
for f in FILES:
    tree = ast.parse(open(f, "rb").read().decode("utf-8"))
    for n in ast.walk(tree):
        if isinstance(n, ast.Import) and any(PAT.search(a.name) for a in n.names):
            imports += 1
            print("MODEL_IMPORT", f, n.lineno, ast.unparse(n))
        if isinstance(n, ast.ImportFrom) and (PAT.search(n.module or "") or any(PAT.search(a.name) for a in n.names)):
            imports += 1
            print("MODEL_IMPORT", f, n.lineno, ast.unparse(n))
        if isinstance(n, ast.Call) and PAT.search(ast.unparse(n.func)):
            calls += 1
            print("MODEL_CALL", f, n.lineno, ast.unparse(n.func))
print("battery_path_files", len(FILES), "model_imports", imports, "model_calls", calls)
src = open("lib/research/filings/batch.py", "rb").read().decode("utf-8").splitlines()
for n in (377, 413, 598):
    print("batch_%d" % n, src[n - 1].strip())
b = open("lib/research/filings/batch.py", "rb").read()
print("batch.py crlf", b.count(bytes([13, 10])), "non_ascii_chars", sum(1 for c in b.decode("utf-8") if ord(c) > 127))
```

`.scratch/r100/ac4.py`:
```
import subprocess
out = subprocess.run(["git", "diff", "--name-only", "04f518851d", "HEAD", "--", "lib", "integrations", "infra", ".tools", "data"], capture_output=True, text=True).stdout.split()
print("changed_code_files", sorted(out))
```

`.scratch/r100/ac5.py`:
```
for f in ("lib/research/filings/batch.py", "lib/research/filings/tests/test_no_analyze.py"):
    b = open(f, "rb").read()
    compile(b.decode("utf-8"), f, "exec")
    print(f, "compiles True crlf", b.count(bytes([13, 10])), "non_ascii_chars", sum(1 for c in b.decode("utf-8") if ord(c) > 127))
```

<proof_of_spec>
  <criterion id="AC0" cell_refs="AMGT-rk-100"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r100/ac0.py && python -m pytest lib/research/filings/tests -q -p no:cacheprovider 2>&1 | tail -1 && python -m pytest lib/research/filings/tests/test_batch.py -q -p no:cacheprovider 2>&1 | tail -1</invocation><expect>BEFORE any edit. It prints "pin_object commit". THE BATTERY NEGATIVE: "battery_path_files 6 model_imports I0 model_calls C0", with no MODEL_IMPORT or MODEL_CALL line (measured I0 = 0 and C0 = 0 at the cut); if either is non-zero, STOP with a BLOCKING row quoting the lines and edit nothing. Then the three batch lines: batch_377 carries "def run_group(", batch_413 carries "analyze.analyze_source(source_object", and batch_598 carries "run_group(group, args.write_pool". Then batch.py's crlf and non_ascii_chars (measured 0 and 0), the filings suite's "F0 passed" (measured 86) and test_batch.py's "B0 passed" (measured 11). A drifted line NUMBER is recorded, not a fail, if the SITE is the same; a differing F0 or B0 is recorded and becomes the baseline</expect></criterion>
  <criterion id="AC1" cell_refs="AMGT-rk-100"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/filings/tests/test_no_analyze.py -v -p no:cacheprovider 2>&1 | tail -10</invocation><expect>a final line "6 passed" and 0 failed, with the PASSED lines naming test_default_run_group_calls_analyze_once_per_resolved_group, test_no_analyze_run_group_makes_zero_model_calls, test_no_analyze_unresolved_branch_unchanged, test_main_no_analyze_defaults_off, test_main_no_analyze_prints_zero_model_calls and test_battery_import_reaches_no_analyze_module</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-100"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/filings/tests -q -p no:cacheprovider 2>&1 | tail -1</invocation><expect>"(F0 + 6) passed" and 0 failed, where F0 is AC0's printed filings count (measured 86, so 92): every pre-existing filings test stays green unedited</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-100"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/filings/tests/test_batch.py -q -p no:cacheprovider 2>&1 | tail -1</invocation><expect>"B0 passed" and 0 failed, where B0 is AC0's printed test_batch.py count (measured 11): the default run_group signature and path are unchanged for their existing callers</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-100"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r100/ac4.py && python .scratch/r100/ac0.py</invocation><expect>"changed_code_files" lists EXACTLY lib/research/filings/batch.py and lib/research/filings/tests/test_no_analyze.py -- no other code file, in particular no battery.py; then the re-run of ac0.py at HEAD prints "battery_path_files 6 model_imports I0 model_calls C0" with the SAME I0 and C0 as AC0 (the battery half stayed a negative)</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-100"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r100/ac5.py</invocation><expect>both files print "compiles True" and crlf 0; batch.py's non_ascii_chars EQUALS AC0's measured value (measured 0), and the new test file's is 0</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~100/AMGT_RESAPP.TO-AMGT-rk-100.filings-no-analyze.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3,AC4,AC5` (rc 0 is the verdict). Flip the order's status
(on the record face) to `complete` only if every criterion PASSES, and commit with `--only -- <paths>`. Report once,
naming AC0's battery-negative line, the suite counts before and after, and AC4's file list.

**MUTATION DISCIPLINE:** snapshot the WORKING-TREE BYTES of `batch.py` to `.scratch/r100/` before editing. Never
`git checkout --`, never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES -- the L5 choices, flagged to the CTO at issuance:**
1. **The battery negative, measured (per msg 24207, "the grep denominator and 0 callers go on the record face"):**
   an AST census at `04f518851d` over the 6 modules `run_battery` reaches (battery.py, fetch.py, document.py,
   passages.py, identity/crosswalk.py, bloomberg/mcp/blp_client.py; 4,549 lines), pattern
   `analyze_source|\banalyze\b|anthropic|bedrock|invoke_model|openai|messages\.create`: **0 model imports, 0 model
   calls, 6 of 6 files.** The instrument is an AST read (import nodes plus call targets), not a text grep, so a
   comment or docstring mention of "analyze" (battery.py:35) is not counted. The same negative is held as a test
   (a fresh-interpreter import of battery does not load `analyze`) and re-run at AC4.
2. **Under `--no-analyze`, nothing from a RESOLVED group is written by `run_group`.** `write_outputs` writes only
   `.analysis.json` and the drafting document, both products of the model call. Batch has never written the SOURCE
   object for a RESOLVED group since AMGT-rk-91 moved that to `fetch.persist`, so a no-analyze batch run lands the
   filing only as BRONZE (via `--write-bronze`). **This is a pre-existing gap, not this cell's:** a batch run with
   `--write-pool` does not write `filing_source` silver for RESOLVED names. It is named for the B2 run cell and the
   CTO; the battery CLI does write it (`battery.py:1351`, `fetch.persist`).
3. **Pin:** `04f518851d`. Re-pin to the issuance commit if s.34 moves anything under `lib/`.

<status>complete</status>
<round>26</round>
<slot>~100</slot>
<fabric>site-z</fabric>
