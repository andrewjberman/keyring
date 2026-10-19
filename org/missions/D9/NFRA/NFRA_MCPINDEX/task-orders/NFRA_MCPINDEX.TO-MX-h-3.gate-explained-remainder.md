# NFRA_MCPINDEX task order -- `MX-h-3` -- the coverage gate learns an explained remainder: a row with a gap owner and a b tool with an owner and a reason are listed beside the refusals and never hidden

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round23-GATEWAY.md</decomp_doc>
<owned_cells>MX-h-3</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-h-3.gate-explained-remainder</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~64</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule; an edit to one existing script and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- local files only; no AWS call, no grant.
comp-adversary: DECLARED-NOT-APPLICABLE -- the base dry-runs (every criterion FAILs at the base) and the planted arms inside the criteria are the control.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-h-3` (round 23, workstream GATEWAY; PRD v0.18 FWD-23; CTO round-22 analysis @44e6950a24)

Work in your own worktree (cut from `box/sitez`; every path below is relative to its root). Round 23 moves the whole gateway census, not one channel, toward FWD-23 (every channel indexed), FWD-24 (every tool tested) and FWD-25 (a sheet per employee). The census it counts against is `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/evidence/GATEWAY_SURFACE_CENSUS_20261019_v2.json` (14 channels, 127 tools, read from the gateway host on 2026-10-19). `index_coverage.py` and its test file already exist (round 22, merged); you EDIT the script and the existing test file and add one new test file.

**What to build.** Apply the COVERAGE delta to `workflows/gateway_battery/index_coverage.py`. Read the script first: its `compute` function builds the refusal list and `run` prints the `COVERAGE` line. Keep the change small: two new branches (a row with a `gap_owner`; a `b` with an owner and a reason), an `explained` list returned beside the refusals, the new output key, the new denominator key and the new stdout field. Then move the existing tests in `tests/test_index_coverage.py` to the new `COVERAGE` line (they pin the old one), and add `tests/test_index_coverage_explained.py` with at least 4 tests of the new behavior. The round-22 criteria `g2.AC1` and `g2.AC2` already expect the new line; they must pass.

### The contract (verbatim from the decomposition; it is the whole specification)

**COVERAGE delta** (the round-22 gate `index_coverage.py` gains an EXPLAINED remainder; its contract otherwise stands):
- A row under an in-scope channel with no served `read_tool` and a non-empty STRING `gap_owner` (after strip) is not a `row_no_read_tool` refusal; it is an explained record `{class: row_explained_gap, channel, subject: <entity>, detail: <gap_owner>}`. A blank or non-string `gap_owner` stays a refusal.
- A `member: b` tool with a non-empty string `owner` AND a non-empty string `reason` (after strip) is not a `tool_member_b` refusal; it is an explained record `{class: tool_b_explained, channel, subject: <tool>, detail: <owner>}`. A `b` without a reason stays `tool_member_b`.
- Nothing else changes: an undeclared-channel tool that is not `c` with a reason still refuses `undeclared_tool` (an explained `b` there is also listed as explained).
- The output file gains `"explained": [sorted by (class, channel, subject, detail)]` and the denominator gains `"explained": N`. The stdout line becomes `COVERAGE channels=N tools=T rows=R refusals=K explained=E`. Exit 0 iff K is 0 (explained records never fail the run), 1 if K > 0, 2 unreadable input.
- The round-22 criteria `g2.AC1` and `g2.AC2` are updated to the new line and must keep passing; the existing tests of the file move with the line.

The round-22 COVERAGE contract that stands (refusal classes and the rest):

**COVERAGE** (the FWD-23 refusal set), `python workflows/gateway_battery/index_coverage.py --census FILE --members FILE [--pending FILE] --catalog FILE [--channel ID ...] --out FILE`:
- Inputs: the CENSUS; `members.yaml` (top-level `members` list of `{tool, member a|b|c, owner?, reason?, index?, links?}`; the top-level `buckets` list is ignored) plus the optional `pending_members.yaml` (top-level `pending` list, same entry shape; an entry already present in members wins); the catalog's three row sections `silver_datasets`, `portal_datasets`, `harvest_datasets` (rows with `entity`, `bucket`, `read_tool`, optional `retired`; the same sections `round18/discover_buckets.py` reads).
- A row is UNDER a channel when it is not `retired`, carries a `bucket` and `bucket` equals the channel id. A row without a `bucket` is under no channel.
- Refusal classes, each `{"class","channel","subject","detail"}`: `row_no_read_tool` (a row under an in-scope channel whose `read_tool` is absent or not a CENSUS tool; subject = the row's `entity`); `tool_unclassified` (an in-scope tool with no members entry); `tool_member_b` (members says `b`; detail = the `owner`); `tool_c_no_reason` (`c` with an empty `reason`); `tool_a_unlinked` (`a` while the CENSUS `indexes` of the tool is empty); `channel_no_row` (a `bucket` or `store` channel with no row under it and at least one tool that is not `c` with a reason; subject = the channel id); `undeclared_tool` (a tool of an `undeclared` channel that is not `c` with a reason; emitted IN ADDITION to any other refusal for that tool). A tool in several channels is judged once, under the first in-scope channel that holds it.
- Output file: `{"schema":"index_coverage/1","denominator":{"channels","tools","rows"},"refusals":[sorted by (class, channel, subject)]}`. Denominator: in-scope channels; distinct tools in them; rows under them. Stdout: `COVERAGE channels=N tools=T rows=R refusals=K`, then one `REFUSE <class> <channel> <subject>` line per refusal (at most 200 lines; the file holds all). Exit 0 iff K is 0, 1 if K > 0, 2 on unreadable input.

### Inputs you read (you do NOT edit them)

- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/fixtures/h3_members.yaml` and `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/fixtures/h3_catalog.yaml`: `harvest_read` is `b` with owner and reason (explained); `send_email` is `b` with an owner and no reason (refused); `gap_row` has a `gap_owner` (explained); `bad_gap` names a ghost tool (refused); `gap_blank` has an empty `gap_owner` (refused). The census used is the round-22 fixture `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/fixtures/expected_census.json`.
- The round-22 criteria `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/checks/g2.AC1.sh` and `g2.AC2.sh` (already updated to the new line).

### Steps

0. From the worktree root, `git rev-parse --show-toplevel` is your root. The worktree already carries the sparse folders `workflows/gateway_battery`, `workflows/gateway_battery/tests`, `workflows/atom_decomposition` and `infra/aws/ec2/opal-gateway/app`; if another folder you need is missing, `git sparse-checkout add <folder>` is the only sparse change you may make.
1. Read the fixtures named above and `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/checks/h_check.py` (the arms for your cell). Make the script and its test file. The test file holds at least 4 tests of its own: they exercise the script as a subprocess or by importing it with `importlib` from its path, on small inputs you write inside the test with `tmp_path` (not the issuer's fixtures; those are the criteria's). There is no `__init__.py`: scripts are run by path.
2. Run the three criteria in section 4 until each prints `RESULT: PASS`.

## 2. BOUNDS

1. You change only the files in `<paths>`. Do NOT edit the issuer's fixtures, checks or decomposition, `members.yaml`, `pending_members.yaml`, the catalog or its row files, the emitter (`emit_catalog_v02.py`), any file under `infra/`, the PRD, or any other file under `workflows/`. No AWS call, no network call (the measurer's live S3 path is written but never run by you; you test it with `--fake`), no grant, no deploy, no push.
2. Python 3.9, standard library plus `yaml` (PyYAML, installed) only; the measurer imports `boto3` only inside the live path. ASCII only in code, comments, strings, output and data files. No type syntax newer than 3.9 (no `X | Y` annotations, no `match`). The commit gate runs `py_compile`, the naming gate and `ruff` for py39.
3. No tool name, channel id, firm or vendor is typed as a whole-string literal in a script (the contract's fixed words are fine); tests under `tests/` and data files are exempt.
4. The contract in section 1 is the whole specification. Where it is silent, do the smallest thing and say which in your report; do not widen the output.
5. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project: your proof instance is one (commit it with, or before, the last code commit).
6. The checks are `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/checks/h3.AC1.sh`, `.AC2.sh` and `.AC3.sh` (they run `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/checks/h_check.py`). Read `h_check.py` for exactly what each arm grades; it is the executable form of section 1. Do not edit any of them.
7. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
workflows/gateway_battery/index_coverage.py
workflows/gateway_battery/tests/test_index_coverage.py
workflows/gateway_battery/tests/test_index_coverage_explained.py
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~64/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-h-3.gate-explained-remainder.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W64-S<k>` (`k` the next unused number of your slot);
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp (`date -u +%FT%TZ` at filing).

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 2)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-h-3" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/checks/h3.AC1.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line; `COVERAGE channels=6 tools=9 rows=7 refusals=3 explained=2` with exit 1; the three refusals; the two explained records with their details; the denominator carries explained; the explained records carry class, channel, subject and detail; an explained remainder alone exits 0 with `refusals=0 explained=3` -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-h-3" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/checks/h3.AC2.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line; the round-22 criteria g2.AC1 and g2.AC2 still PASS on the new line; a blank reason and a non-string gap_owner stay refusals; an undeclared-channel tool that is an explained b still refuses as undeclared_tool -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-h-3" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/checks/h3.AC3.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line (pytest rc=0, at least 4 passed) for `test_index_coverage_explained.py` -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~64/NFRA_MCPINDEX.TO-MX-h-3.gate-explained-remainder.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance. In its artifact rows, pin each produced file to the commit that carried it (the checker refuses `PENDING-THIS-COMMIT` for a file committed before the instance): commit the work first, then write the instance naming those commit hashes.
2. Append `<status>complete</status>` to this order file only if every criterion PASSes (if the commit gate refuses the flip, leave it and say so).
3. Commit through `.tools/safe-commit.sh` in two commits: (i) the work; (ii) the proof instance and the status flip.
4. Report once, with: what you built by part; every `RESULT:` line and `DENOMINATOR:` line of each criterion verbatim; the unit-test count (code cells); your commit shas; every place the contract was silent and what you did.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 23, workstream GATEWAY, worker ~64. Source: the CTO's round-22 analysis @44e6950a24 (msg 35997) and PRD v0.18 @4b8dcf3b86, cut on the CORRECTED census. Decomposition `org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round23-GATEWAY.md` (the contracts R23.2 are frozen at the cut). Base dry-runs 2026-10-19: every criterion of this order FAILs as expected (the script, test file or deliverable is absent, or the gate lacks the explained field). The issuer's scratch reference (a patch of the merged script) passes `h3.AC1` and `h3.AC2`. Gate limb that graded this order: the L6 gate at the issuance commit.

<status>issued</status>
<round>23</round>
<workstream>GATEWAY</workstream>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>
