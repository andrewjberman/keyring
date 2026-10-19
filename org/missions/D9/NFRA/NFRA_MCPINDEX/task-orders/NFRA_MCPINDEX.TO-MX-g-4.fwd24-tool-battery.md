# NFRA_MCPINDEX task order -- `MX-g-4` -- the FWD-24 tool battery: plan the calls a signed-in session makes for every census tool, grade what came back, and plant a broken tool that must read FAIL

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round22-GATEWAY.md</decomp_doc>
<owned_cells>MX-g-4</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-g-4.fwd24-tool-battery</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~60</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule; one new script and one new test file.
comp-iam: DECLARED-NOT-APPLICABLE -- local files only; no AWS call, no grant.
comp-adversary: DECLARED-NOT-APPLICABLE -- the base dry-runs (all three criteria FAIL at the base) and the planted arms inside the criteria are the control.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-g-4` (round 22, workstream GATEWAY; PRD v0.18 FWD-23, FWD-24, FWD-25)

Work in your own worktree (cut from `box/sitez`; every path below is relative to its root). Round 22 builds, for ONE gateway channel, a thread of four small scripts in a NEW folder `workflows/gateway_battery/`: a census reducer, a coverage gate, a tool battery and a cheat-sheet generator. They share frozen data contracts and never call each other, so you build yours alone. You build **`tool_battery.py`** and its test file.

**What to build.** `workflows/gateway_battery/tool_battery.py` with three subcommands, `plan`, `grade` and `plant`, exactly as the BATTERY contract says. The script never calls the gateway: a signed-in session makes the planned calls and records RESULTS, and `grade` turns them into the per-tool verdicts FWD-24 counts (PASS, EMPTY-CORRECT, REFUSED-CORRECT, PREVIEW-ONLY, FAIL with a class). A result is a PASS only when a second instrument agreed (`source_check.agrees` is true); a tool that sends is never exercised past its preview, and a result with `sent` true is a FAIL. `plant` builds the PRD's planted broken tool: the grade of its output must read FAIL.

### The contract (verbatim from the decomposition; it is the whole specification)

**CASES** `gateway_battery_cases/1`: `{"schema":...,"cases":[{"case_id","tool","question","args":{},"expect":"nonempty|empty|refused|preview","source_hint"}]}`. `question` is the plain-English example a sheet may show.

**RESULTS** `gateway_battery_results/1`: `{"schema":...,"run":{"principal","transport","started_at"},"results":[{"case_id","status":"ok|error|refused|preview","rows":int|null,"as_of":str|null,"error_text":str|null,"sent":bool,"source_check":{"instrument","value","agrees":bool}|null}]}`. Recorded by the signed-in session that ran the cases (R22.4 ruling 1).

**BATTERY** `python workflows/gateway_battery/tool_battery.py`:
- `plan --census F --cases F [--channel ID ...] --out F` writes `{"schema":"gateway_battery_plan/1","tools_in_scope":[...],"cases":[the cases of in-scope tools],"tools_without_case":[...]}`; stdout `PLAN tools=T cases=C tools_without_case=K`; exit 0 iff K is 0 (the file is written either way).
- `grade --census F --cases F --results F [--channel ID ...] --out F` writes `gateway_battery_graded/1`: `{"run":<the results' run>,"cases":[{"case_id","tool","question","verdict","fail_class"}],"tools":[{"tool","verdict","fail_class","cases":[ids]}] (sorted by tool),"counts":{PASS,EMPTY-CORRECT,REFUSED-CORRECT,PREVIEW-ONLY,FAIL} (over TOOLS),"case_counts":{same keys over cases},"preview_only":[tool names],"fails":[{"tool","fail_class"}]}`. Stdout `GRADE tools=T PASS=a EMPTY-CORRECT=b REFUSED-CORRECT=c PREVIEW-ONLY=d FAIL=e`, then `PREVIEW-ONLY TOOLS: <comma list or empty>`. Exit 0 iff FAIL is 0.
- Case verdict: `expect nonempty`: status `error` -> FAIL `tool_error`; `refused` -> FAIL `unexpected_refusal`; `ok` with rows > 0 -> PASS only when `source_check.agrees` is true (`source_check` null -> FAIL `source_unchecked`; agrees false -> FAIL `source_disagrees`); any other `ok` (rows 0 or null) -> FAIL `unexpected_empty`. `expect empty`: `ok` with rows 0 and `agrees` true -> EMPTY-CORRECT (agrees missing or false -> FAIL `source_unchecked`); `error` -> FAIL `tool_error`; any other -> FAIL `unexpected_nonempty`. `expect refused`: status `refused` -> REFUSED-CORRECT, else FAIL `not_refused`. `expect preview`: `sent` true -> FAIL `sent`; status `preview` -> PREVIEW-ONLY; else FAIL `tool_error`. A planned case with no result -> FAIL `not_run`. An in-scope tool with no case -> tool FAIL `no_case`.
- Tool verdict: FAIL if any of its cases FAIL (its `fail_class` is the first failing case's, in case order); else the first present of PASS, EMPTY-CORRECT, REFUSED-CORRECT, PREVIEW-ONLY.
- `plant --cases F --results F --tool NAME --out F` copies RESULTS with every case of that tool set to status `error`, `rows` null, `error_text` `planted`, `source_check` null (the PRD's planted broken tool).

### Fixtures you read (the criteria drive your script with them; you do NOT edit them)

- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/fixtures/expected_census.json`: the census (6 channels, 9 tools; the `undeclared` channel holds the tool `stray_tool`, which has no case).
- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/fixtures/cases_min.json`: 9 cases over 8 tools (the criteria scope to the first five channels with `--channel`).
- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/fixtures/results_min.json`: the green RESULTS for all 9 cases.
- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/fixtures/graded_min.json`: the graded file the green RESULTS must produce (your `grade` output must agree with it on every verdict, count and `preview_only`).

### Steps

0. From the worktree root, `git rev-parse --show-toplevel` is your root. If `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/` or `workflows/` is missing, run `git sparse-checkout add <folder>` once (the only sparse change you may make). `python -m pytest --version` works.
1. Read the fixtures named above and `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/checks/g_check.py` (the arms for your cell). Make the script and its test file. The test file holds at least 6 tests of its own: they exercise the script as a subprocess or by importing it with `importlib` from its path, on small inputs you write inside the test with `tmp_path` (not the issuer's fixtures; those are the criteria's). There is no `__init__.py`: scripts are run by path.
2. Run the three criteria in section 4 until each prints `RESULT: PASS`.

Note: `grade` takes the question text from the CASES file, and a graded case carries it, because the sheet generator reads only the graded file.


## 2. BOUNDS

1. You change only the files in `<paths>`. Do NOT edit the issuer's fixtures, checks or decomposition, any other file under `workflows/`, any gateway file under `infra/`, the catalog, `members.yaml`, the emitter, a registry file or the PRD. No AWS call, no network call, no grant, no deploy, no push. Your script reads local files only.
2. Python 3.9, standard library plus `yaml` (PyYAML, already installed) only. ASCII only in code, comments, strings and output. No type syntax newer than 3.9 (no `X | Y` annotations, no `match`). The commit gate runs `py_compile`, the naming gate and `ruff` for py39.
3. No tool name, channel id, firm or vendor is typed as a whole-string literal in the script (the five channel kinds, the verdict words and the fail-class words of the contract are fixed vocabulary and may be literals); tests under `tests/` are exempt.
4. The contract in section 1 is the whole specification. Where it is silent, do the smallest thing and say which in your report; do not widen the output.
5. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project: your proof instance is one (commit it with, or before, the last code commit).
6. The checks are `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/checks/g4.AC1.sh`, `.AC2.sh` and `.AC3.sh` (they run `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/checks/g_check.py`). Read `g_check.py` for exactly what each arm grades; it is the executable form of section 1. Do not edit any of them.
7. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
workflows/gateway_battery/tool_battery.py
workflows/gateway_battery/tests/test_tool_battery.py
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~60/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W60-S<k>`;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp (`date -u +%FT%TZ` at filing).

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 2)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-g-4" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/checks/g4.AC1.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line; `plan` over the five scoped channels prints `PLAN tools=8 cases=9 tools_without_case=0` (rc 0) and over all channels `PLAN tools=9 cases=9 tools_without_case=1` (rc 1); the green `grade` prints `GRADE tools=8 PASS=6 EMPTY-CORRECT=0 REFUSED-CORRECT=1 PREVIEW-ONLY=1 FAIL=0`, `PREVIEW-ONLY TOOLS: send_email`, with the per-tool and per-case verdicts and the carried question -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-g-4" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/checks/g4.AC2.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line; the planted broken tool and the eight further planted arms (source disagrees; no source check; a send; a case not run; an unexpected empty; an ungranted principal not refused; an unexpected refusal; a census tool with no case) each exit 1 and read FAIL with the contract's fail class -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-g-4" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/checks/g4.AC3.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line (pytest rc=0, at least 6 passed) for `test_tool_battery.py` -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~60/NFRA_MCPINDEX.TO-MX-g-4.fwd24-tool-battery.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance. In its artifact rows, pin each produced file to the commit that carried it (the checker refuses `PENDING-THIS-COMMIT` for a file committed before the instance): commit the script and the test first, then write the instance naming those commit hashes.
2. Append `<status>complete</status>` to this order only if all three criteria PASS (if the commit gate refuses the flip, leave it and say so).
3. Commit through `.tools/safe-commit.sh` in two commits: (i) the script and the test file; (ii) the proof instance (and the status flip).
4. Report once, with: what you built by part; the three `RESULT:` lines and the `DENOMINATOR:` line of each criterion verbatim; the unit-test count; your commit shas; every place the contract was silent and what you did.

The issuer then merges, runs the real data through your script at the drain and keeps the artifact.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 22, workstream GATEWAY, worker ~60. Source: PRD v0.18 @4b8dcf3b86 (CTO msg 35988). Decomposition `org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round22-GATEWAY.md` (the contracts R22.2 are frozen at the cut). Base dry-runs 2026-10-19: `g4.AC1`, `.AC2`, `.AC3` all FAIL as expected (script and test file absent). The issuer's reference implementation (scratch, not committed) passes `g4.AC1` and `g4.AC2`, so the arms are satisfiable. Gate limb that graded this order: the L6 gate at the issuance commit.

<status>issued</status>
<round>22</round>
<workstream>GATEWAY</workstream>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
