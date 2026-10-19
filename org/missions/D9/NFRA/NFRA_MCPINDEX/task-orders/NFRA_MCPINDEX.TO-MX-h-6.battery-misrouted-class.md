# NFRA_MCPINDEX task order -- `MX-h-6` -- the battery learns the misrouted class: an answer must come from the source the row's code names, and a planted wrong source must read FAIL misrouted

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round23-GATEWAY.md</decomp_doc>
<owned_cells>MX-h-6</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-h-6.battery-misrouted-class</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~62</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule; an edit to one existing script and one new test file.
comp-iam: DECLARED-NOT-APPLICABLE -- local files only; no AWS call, no grant.
comp-adversary: DECLARED-NOT-APPLICABLE -- the base dry-runs (every criterion FAILs at the base) and the planted arms inside the criteria are the control.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-h-6` (round 23, workstream GATEWAY; PRD v0.18 FWD-24; CTO round-22 analysis @44e6950a24)

Work in your own worktree (cut from `box/sitez`; every path below is relative to its root). Round 23 moves the whole gateway census, not one channel, toward FWD-23 (every channel indexed), FWD-24 (every tool tested) and FWD-25 (a sheet per employee). The census it counts against is `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/evidence/GATEWAY_SURFACE_CENSUS_20261019_v2.json` (14 channels, 127 tools, read from the gateway host on 2026-10-19). `tool_battery.py` and its tests already exist (round 22, merged); you EDIT the script and add one new test file. Andrew asked why the gateway page shows Black Diamond on Schwab tools and wants every tool call proven to reach the right source; this is the answer-side half of that proof.

**What to build.** Apply the BATTERY delta to `workflows/gateway_battery/tool_battery.py`: read the script first (`grade_case` decides a case's verdict, `cmd_plant` is the model for the new `plant-route` subcommand, `build_parser` and `HANDLERS` register commands). Keep the change small: the source check inside the existing PASS branch, the new subcommand and its parser entry. Add `tests/test_tool_battery_route.py` with at least 5 tests. The existing `tests/test_tool_battery.py` must keep passing unchanged, and so must the round-22 criteria `g4.AC1` and `g4.AC2`.

### The contract (verbatim from the decomposition; it is the whole specification)

**CASES and RESULTS delta** (PRD v0.19, FWD-24 `misrouted`):
- A case MAY carry `"expect_source": "<string>"`: the bucket id, key prefix, store or integration source that the tool's OWN CODE reads for that case, taken from the catalog row's `bucket` and `prefix` or `key`, or from the code's `bucket_source` line, NEVER from the tool's name.
- A result MAY carry `"answer_source": ["<string>", ...]`: the source fields the response itself carries (its `source_keys` entries, bucket, prefix, or its integration or source field), copied as the signed-in session recorded them.

**BATTERY delta** (the round-22 `tool_battery.py` gains the misrouted class; everything else stands):
- In `grade`, a case that has `expect_source` and would otherwise be a PASS (`expect: nonempty`, `ok` with rows, `source_check.agrees` true) needs the answer to come from the routed source: `answer_source` must be a non-empty list in which at least one element CONTAINS the `expect_source` string. A missing or empty `answer_source` is FAIL `source_unchecked`; a non-empty list with no matching element is FAIL `misrouted`. A case without `expect_source` is graded exactly as before, whatever its `answer_source`.
- New subcommand `plant-route --cases F --results F --case CASE_ID --out F`: copies RESULTS with that case's `answer_source` replaced by the single element `planted/wrong/source/` (the PRD's planted wrong link); it exits 2 (`REFUSED:` on stderr, no output file) when the case does not exist or has no `expect_source`; stdout `PLANT-ROUTE case=<id>`. Grading the planted file must read that tool FAIL `misrouted`.

The round-22 BATTERY contract that stands (verdict rules, `plan`, `grade`, `plant`):

**BATTERY** `python workflows/gateway_battery/tool_battery.py`:
- `plan --census F --cases F [--channel ID ...] --out F` writes `{"schema":"gateway_battery_plan/1","tools_in_scope":[...],"cases":[the cases of in-scope tools],"tools_without_case":[...]}`; stdout `PLAN tools=T cases=C tools_without_case=K`; exit 0 iff K is 0 (the file is written either way).
- `grade --census F --cases F --results F [--channel ID ...] --out F` writes `gateway_battery_graded/1`: `{"run":<the results' run>,"cases":[{"case_id","tool","question","verdict","fail_class"}],"tools":[{"tool","verdict","fail_class","cases":[ids]}] (sorted by tool),"counts":{PASS,EMPTY-CORRECT,REFUSED-CORRECT,PREVIEW-ONLY,FAIL} (over TOOLS),"case_counts":{same keys over cases},"preview_only":[tool names],"fails":[{"tool","fail_class"}]}`. Stdout `GRADE tools=T PASS=a EMPTY-CORRECT=b REFUSED-CORRECT=c PREVIEW-ONLY=d FAIL=e`, then `PREVIEW-ONLY TOOLS: <comma list or empty>`. Exit 0 iff FAIL is 0.
- Case verdict: `expect nonempty`: status `error` -> FAIL `tool_error`; `refused` -> FAIL `unexpected_refusal`; `ok` with rows > 0 -> PASS only when `source_check.agrees` is true (`source_check` null -> FAIL `source_unchecked`; agrees false -> FAIL `source_disagrees`); any other `ok` (rows 0 or null) -> FAIL `unexpected_empty`. `expect empty`: `ok` with rows 0 and `agrees` true -> EMPTY-CORRECT (agrees missing or false -> FAIL `source_unchecked`); `error` -> FAIL `tool_error`; any other -> FAIL `unexpected_nonempty`. `expect refused`: status `refused` -> REFUSED-CORRECT, else FAIL `not_refused`. `expect preview`: `sent` true -> FAIL `sent`; status `preview` -> PREVIEW-ONLY; else FAIL `tool_error`. A planned case with no result -> FAIL `not_run`. An in-scope tool with no case -> tool FAIL `no_case`.
- Tool verdict: FAIL if any of its cases FAIL (its `fail_class` is the first failing case's, in case order); else the first present of PASS, EMPTY-CORRECT, REFUSED-CORRECT, PREVIEW-ONLY.
- `plant --cases F --results F --tool NAME --out F` copies RESULTS with every case of that tool set to status `error`, `rows` null, `error_text` `planted`, `source_check` null (the PRD's planted broken tool).

### Inputs you read (you do NOT edit them)

- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/fixtures/h6_cases.json` and `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/fixtures/h6_results.json`: 4 cases over 4 tools (R1 and R2 carry `expect_source`; R3 and R4 do not) and their green results (R2's `answer_source` lists a gold and a silver key). The census used is the round-22 fixture `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/fixtures/expected_census.json`, scoped with `--channel opal-data-harvest --channel opal-data-assets`.
- The round-22 criteria `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/checks/g4.AC1.sh` and `g4.AC2.sh` (they must still pass).

### Steps

0. From the worktree root, `git rev-parse --show-toplevel` is your root. The worktree already carries the sparse folders `workflows/gateway_battery`, `workflows/gateway_battery/tests`, `workflows/atom_decomposition` and `infra/aws/ec2/opal-gateway/app`; if another folder you need is missing, `git sparse-checkout add <folder>` is the only sparse change you may make.
1. Read the fixtures named above and `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/checks/h_check.py` (the arms for your cell). Make the script and its test file. The test file holds at least 5 tests of its own: they exercise the script as a subprocess or by importing it with `importlib` from its path, on small inputs you write inside the test with `tmp_path` (not the issuer's fixtures; those are the criteria's). There is no `__init__.py`: scripts are run by path.
2. Run the three criteria in section 4 until each prints `RESULT: PASS`.

## 2. BOUNDS

1. You change only the files in `<paths>`. Do NOT edit the issuer's fixtures, checks or decomposition, `members.yaml`, `pending_members.yaml`, the catalog or its row files, the emitter (`emit_catalog_v02.py`), any file under `infra/`, the PRD, or any other file under `workflows/`. No AWS call, no network call (the measurer's live S3 path is written but never run by you; you test it with `--fake`), no grant, no deploy, no push.
2. Python 3.9, standard library plus `yaml` (PyYAML, installed) only; the measurer imports `boto3` only inside the live path. ASCII only in code, comments, strings, output and data files. No type syntax newer than 3.9 (no `X | Y` annotations, no `match`). The commit gate runs `py_compile`, the naming gate and `ruff` for py39.
3. No tool name, channel id, firm or vendor is typed as a whole-string literal in a script (the contract's fixed words are fine); tests under `tests/` and data files are exempt.
4. The contract in section 1 is the whole specification. Where it is silent, do the smallest thing and say which in your report; do not widen the output.
5. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project: your proof instance is one (commit it with, or before, the last code commit).
6. The checks are `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/checks/h6.AC1.sh`, `.AC2.sh` and `.AC3.sh` (they run `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/checks/h_check.py`). Read `h_check.py` for exactly what each arm grades; it is the executable form of section 1. Do not edit any of them.
7. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
workflows/gateway_battery/tool_battery.py
workflows/gateway_battery/tests/test_tool_battery_route.py
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~62/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-h-6.battery-misrouted-class.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W62-S<k>` (`k` the next unused number of your slot);
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp (`date -u +%FT%TZ` at filing).

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 2)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-h-6" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/checks/h6.AC1.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line; the green grade reads `GRADE tools=4 PASS=4 ... FAIL=0`; an answer from another source reads FAIL misrouted; an answer with no source field or an empty list reads FAIL source_unchecked; a case with no expect_source ignores its answer_source; one matching element among several is enough -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-h-6" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/checks/h6.AC2.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line; plant-route exits 0, changes only the named case and leaves no element that names the expected source; grading the planted file reads FAIL misrouted; plant-route on a case with no expect_source exits 2; the round-22 criteria g4.AC1 and g4.AC2 still PASS -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-h-6" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/checks/h6.AC3.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line (pytest rc=0, at least 5 passed) for `test_tool_battery_route.py` -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~62/NFRA_MCPINDEX.TO-MX-h-6.battery-misrouted-class.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance. In its artifact rows, pin each produced file to the commit that carried it (the checker refuses `PENDING-THIS-COMMIT` for a file committed before the instance): commit the work first, then write the instance naming those commit hashes.
2. Append `<status>complete</status>` to this order file only if every criterion PASSes (if the commit gate refuses the flip, leave it and say so).
3. Commit through `.tools/safe-commit.sh` in two commits: (i) the work; (ii) the proof instance and the status flip.
4. Report once, with: what you built by part; every `RESULT:` line and `DENOMINATOR:` line of each criterion verbatim; the unit-test count (code cells); your commit shas; every place the contract was silent and what you did.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 23, workstream GATEWAY, worker ~62. Source: the CTO's round-22 analysis @44e6950a24 (msg 35997) and PRD v0.18 @4b8dcf3b86, cut on the CORRECTED census. Decomposition `org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round23-GATEWAY.md` (the contracts R23.2 are frozen at the cut). Base dry-runs 2026-10-19: every criterion of this order FAILs as expected (the script, test file or deliverable is absent, or the gate lacks the explained field). The issuer's scratch reference (a patch of the merged script) passes `h6.AC1` and `h6.AC2`. Gate limb that graded this order: the L6 gate at the issuance commit.

<status>issued</status>
<round>23</round>
<workstream>GATEWAY-ROUTE</workstream>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
