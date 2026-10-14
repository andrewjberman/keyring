# AMGT_RESAPP task order -- `AMGT-fc-4` -- THE RE-VALIDATE COMMAND: EVERY STORED DOCUMENT AGAINST THE CURRENT CONTRACT, COUNTS PRINTED (FWD-41 ROUND 105; A BUILD)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md</decomp_doc>
<owned_cells>AMGT-fc-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~433</issued_to>
<issued_by>2.0.0_SA_COO~R2</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-fc-4.the-revalidate-command-checks-every-stored-document</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing is scheduled; a library module and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- the cell writes and tests local Python only; in production use the command reads S3 and the served routes (GET) under the box's own role, and the checks use fakes.
comp-adversary: RUN at the cut -- `check_fc4_revalidate.py` is a prepared acceptance check (11 arms: good documents pass, a narrated document is refused by name, a missing document is reported, the name-mangling finder through the served inputs, unreadable inputs leave a name unchecked, the json output, the census-file names, the BLOCKED stop, one read per name, the current contract, ASCII with no network); at the base it fails with `ImportError: cannot import name 'revalidate'`, the build check failing as expected.
EGRESS CLASS, declared: NONE by the cell and its checks (fake reader and fake served-inputs reader).
</preflight>

**Your worktree:** `C:/dev/wk-resapp-433` (branch `wk-AMGT_RESAPP-433`, cut from the merged head that carries cell fc-2 (the issuer cuts this worktree after fc-2 merges)). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-433`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-fc-4` (round 105, workstream AIFILL, decomposition `org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md`)

The CTO's ruling (round-104 analysis, item 2): "a full re-validate of all 95 stored documents against the new contract, printing pass/refuse counts. 0 refused is the gate" for the page to land. You build that command: `python -m lib.research.aifill.revalidate`. One new module plus tests.

### Why this cell exists (measured by the CVO on the stored documents, C-S133; the CTO's round-104 analysis, `ledger/ROUND_ANALYSIS.round104.AIFILL.md`)
The producer stored 11 blocks across 10 names that open with the MODEL'S NARRATION, glued to the real answer with no space: `I'll research this now.MUFG announced ...` (8306 JP, 9433 JP, 939 HK, ICT PM, NESN SW, PWR US, RIO LN, SHOP CN, UNVGY US), and stored `Nestl` for `Nestle`
(a non-ASCII letter was DROPPED, not transliterated). Neither has reached a person (the page is not landed) but both are served by the API. The CTO's ruling: the disarm is in the PRODUCER, never by hand-editing documents; the page does not land until a full re-validate of all 95 stored
documents against the new contract reads 0 refused. Round 104's cells are merged; this round changes four of their files.

### `lib/research/aifill/revalidate.py` -- exact interface
- `main(argv=None, reader=None, inputs_reader=None) -> int` (and `if __name__ == "__main__": sys.exit(main())`).
- Arguments (argparse): `--names A,B,...`; `--census-file FILE` (a JSON file whose `result` object keys are the names, as `census_sections.json` has them; the names are taken sorted and are added to `--names`); `--with-inputs`; `--function NAME` (the served function's name; default the environment variable `AIFILL_SERVED_FUNCTION`; never typed in the module); `--json OUT`. No names at all -> print `BLOCKED: no names (pass --names or --census-file)` and return 2.
- `reader(key) -> dict | None` defaults to `lib.research.aifill.store.read_document` (imported inside `main`). `inputs_reader(key, function_name=...) -> {"overlay", "thesis", "errors"}` defaults to `lib.research.aifill.inputs.served_inputs` (imported inside `main`, only when `--with-inputs`; if `--with-inputs` and no function name is given, print `BLOCKED: the served function name is not set (pass --function or set AIFILL_SERVED_FUNCTION)` and return 2).
- Per name, in order, each name read ONCE even if listed twice: `doc = reader(name)`; `None` -> the name is MISSING. Otherwise `problems = contract.validate_document(doc)` (call it THROUGH the `contract` module so the check can patch it); with `--with-inputs`, `inputs = inputs_reader(name, function_name=fn)`: when `inputs["overlay"]` or `inputs["thesis"]` is not None the name is NAME-CHECKED, and the names to test are `overlay.display_name`, `overlay.name` and every `thesis.management.officers[].name` that is a non-empty string; for every block with text, add each string of `contract.name_mangling_problems(text, names)` to the problems prefixed with the block id. Both inputs None -> the name is not name-checked (no refusal for it).
- A name with any problem is REFUSED. Print one line per refused name `REFUSED <name>: <the first problem>` and one per missing name `MISSING <name>`, in name order, then the final line EXACTLY: `AIFILL REVALIDATE: checked N, passed P, refused R, missing M, name-checked C` where N is the count of distinct names, P those with a document and no problem, R refused, M missing, C name-checked (C is 0 without `--with-inputs`). Return 0 only when R == 0 and M == 0, else 1.
- `--json OUT` writes `{"checked": N, "passed": P, "refused": {name: [all problems]}, "missing": [names], "name_checked": C}`; the file is ASCII JSON.
- The module imports only the standard library at module level; no model call, no network call of its own; ASCII source.

### Tests
A new test module `lib/research/aifill/tests/test_revalidate.py` (no `__init__.py`): a fake reader and fake served-inputs reader; every behaviour above, the exit codes, the final line's exact form. Python 3.9, ASCII.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W433-S<k>`, `disarm_owner` `2.0.0_SA_COO~R2`.

## 2. BOUNDS


1. Write ONLY `lib/research/aifill/revalidate.py` and `lib/research/aifill/tests/test_revalidate.py`. You import the merged package and edit none of it.
2. You never run the command against S3 or the live function: the tests and the checks use fakes. The issuer runs it live.
- Leave `lib/research/management/`, `lib/research/filings/`, `lib/research/posture/` and every existing module untouched.
- No network, no AWS, no real model call, no `pip install`: every model call in your tests is a stub or the recorded response. The `anthropic` package is never imported (the installed 0.45.0 crashes on web-search blocks).
- Python 3.9 syntax (`from __future__ import annotations`, `typing.Optional`, no `X | Y` unions evaluated at runtime, no `match`); ASCII-only source files (write non-ASCII characters as `\uXXXX` escapes); stdlib only.
- Run the commit gate before you commit: `bash .tools/commit-gate.sh <each .py you wrote>` (it runs `py_compile` and `ruff`); a finding there is yours to fix.

## 3. SURFACES

<paths>
lib/research/aifill/revalidate.py
lib/research/aifill/tests/test_revalidate.py
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-fc-4"><invocation>cd C:/dev/wk-resapp-433 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round105_aifill_prep/checks/check_fc4_revalidate.py" | tail -4; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `AIFILL FC-4 ARMS: YES (N of N)` with N equal to 11, no `FAIL` arm line above it; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-fc-4"><invocation>cd C:/dev/wk-resapp-433 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python -m pytest -q --color=no -p no:cacheprovider lib/research/aifill/tests/test_revalidate.py | tail -3; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the last non-empty line before `exit=` reads `N passed` (N at least the count your test module's functions define) with no `failed` and no `error` in the last 3 lines; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~433 <0.9.0_WK_AMGT_RESAPP~433@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~433/AMGT_RESAPP.TO-AMGT-fc-4.the-revalidate-command-checks-every-stored-document.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character; each criterion's `expect` recorded as an ordered regex of the printed lines when the prose has regex-active characters.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.
Report once:
- the commit hash;
- each criterion's deciding output line (verbatim) and the arm count;
- the arm lines of AC1 that read FAIL, if any, and the pytest summary line.
- any row.
The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** STAGED behind `AMGT-fc-2` (the command calls `contract.name_mangling_problems` and the refusing `validate_document`). The re-validate is the GATE the CTO named for the landing: 0 refused and 0 missing across the 95. Run live by the issuer after the re-run of the refused names, with `--with-inputs` (the served routes are read, GET, for the names the page knows).

<status>staged</status>
<round>105</round>
<workstream>AIFILL</workstream>
<slot>0.9.0_WK_AMGT_RESAPP~433</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
