# NFRA_MCPINDEX task order -- `MX-g-2` -- the FWD-23 coverage gate: the census, the tool index and the catalog rows produce the refusal set that says what is not indexed

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round22-GATEWAY.md</decomp_doc>
<owned_cells>MX-g-2</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-g-2.fwd23-coverage-gate</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~59</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule; one new script and one new test file.
comp-iam: DECLARED-NOT-APPLICABLE -- local files only; no AWS call, no grant.
comp-adversary: DECLARED-NOT-APPLICABLE -- the base dry-runs (all three criteria FAIL at the base) and the planted arms inside the criteria are the control.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-g-2` (round 22, workstream GATEWAY; PRD v0.18 FWD-23, FWD-24, FWD-25)

Work in your own worktree (cut from `box/sitez`; every path below is relative to its root). Round 22 builds, for ONE gateway channel, a thread of four small scripts in a NEW folder `workflows/gateway_battery/`: a census reducer, a coverage gate, a tool battery and a cheat-sheet generator. They share frozen data contracts and never call each other, so you build yours alone. You build **`index_coverage.py`** and its test file.

**What to build.** `workflows/gateway_battery/index_coverage.py` exactly as the COVERAGE contract says. It answers one question per run: for the in-scope channels of a census, which catalog rows and which tools break the FWD-23 rule (every row under a channel names a served tool; every tool is linked to a row, or is `c` with a stated reason; member `b` is 0; an `undeclared` channel holds nothing but stated `c` tools; a bucket or store channel with no row and a data tool refuses)? The planted channel with no row MUST refuse. It reads three files and a catalog and writes one file; it fixes nothing.

### The contract (verbatim from the decomposition; it is the whole specification)

**COVERAGE** (the FWD-23 refusal set), `python workflows/gateway_battery/index_coverage.py --census FILE --members FILE [--pending FILE] --catalog FILE [--channel ID ...] --out FILE`:
- Inputs: the CENSUS; `members.yaml` (top-level `members` list of `{tool, member a|b|c, owner?, reason?, index?, links?}`; the top-level `buckets` list is ignored) plus the optional `pending_members.yaml` (top-level `pending` list, same entry shape; an entry already present in members wins); the catalog's three row sections `silver_datasets`, `portal_datasets`, `harvest_datasets` (rows with `entity`, `bucket`, `read_tool`, optional `retired`; the same sections `round18/discover_buckets.py` reads).
- A row is UNDER a channel when it is not `retired`, carries a `bucket` and `bucket` equals the channel id. A row without a `bucket` is under no channel.
- Refusal classes, each `{"class","channel","subject","detail"}`: `row_no_read_tool` (a row under an in-scope channel whose `read_tool` is absent or not a CENSUS tool; subject = the row's `entity`); `tool_unclassified` (an in-scope tool with no members entry); `tool_member_b` (members says `b`; detail = the `owner`); `tool_c_no_reason` (`c` with an empty `reason`); `tool_a_unlinked` (`a` while the CENSUS `indexes` of the tool is empty); `channel_no_row` (a `bucket` or `store` channel with no row under it and at least one tool that is not `c` with a reason; subject = the channel id); `undeclared_tool` (a tool of an `undeclared` channel that is not `c` with a reason; emitted IN ADDITION to any other refusal for that tool). A tool in several channels is judged once, under the first in-scope channel that holds it.
- Output file: `{"schema":"index_coverage/1","denominator":{"channels","tools","rows"},"refusals":[sorted by (class, channel, subject)]}`. Denominator: in-scope channels; distinct tools in them; rows under them. Stdout: `COVERAGE channels=N tools=T rows=R refusals=K`, then one `REFUSE <class> <channel> <subject>` line per refusal (at most 200 lines; the file holds all). Exit 0 iff K is 0, 1 if K > 0, 2 on unreadable input.

### Fixtures you read (the criteria drive your script with them; you do NOT edit them)

- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/fixtures/expected_census.json`: the census the criteria use (6 channels; read its `indexes` per tool).
- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/fixtures/members_min.yaml`, `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/fixtures/pending_min.yaml`, `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/fixtures/catalog_min.yaml`: the tool-index and catalog shapes the gate reads (the catalog fixture also holds a `retired` row and a row with no `bucket`; neither counts).

### Steps

0. From the worktree root, `git rev-parse --show-toplevel` is your root. If `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/` or `workflows/` is missing, run `git sparse-checkout add <folder>` once (the only sparse change you may make). `python -m pytest --version` works.
1. Read the fixtures named above and `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/checks/g_check.py` (the arms for your cell). Make the script and its test file. The test file holds at least 6 tests of its own: they exercise the script as a subprocess or by importing it with `importlib` from its path, on small inputs you write inside the test with `tmp_path` (not the issuer's fixtures; those are the criteria's). There is no `__init__.py`: scripts are run by path.
2. Run the three criteria in section 4 until each prints `RESULT: PASS`.

Note on the real inputs, which the criteria do not use: the real members file is `workflows/atom_decomposition/tool_index/members.yaml` and `pending_members.yaml`, and the real catalog is `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml` (the gateway's `app/admin_gateway_breakdown.py` lines 98-119 show how it maps a row to the tool named in its `read_tool`). The issuer runs your script on them at the drain; do not run it on them unless you only read (never write) and report what it printed.


## 2. BOUNDS

1. You change only the files in `<paths>`. Do NOT edit the issuer's fixtures, checks or decomposition, any other file under `workflows/`, any gateway file under `infra/`, the catalog, `members.yaml`, the emitter, a registry file or the PRD. No AWS call, no network call, no grant, no deploy, no push. Your script reads local files only.
2. Python 3.9, standard library plus `yaml` (PyYAML, already installed) only. ASCII only in code, comments, strings and output. No type syntax newer than 3.9 (no `X | Y` annotations, no `match`). The commit gate runs `py_compile`, the naming gate and `ruff` for py39.
3. No tool name, channel id, firm or vendor is typed as a whole-string literal in the script (the five channel kinds, the verdict words and the fail-class words of the contract are fixed vocabulary and may be literals); tests under `tests/` are exempt.
4. The contract in section 1 is the whole specification. Where it is silent, do the smallest thing and say which in your report; do not widen the output.
5. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project: your proof instance is one (commit it with, or before, the last code commit).
6. The checks are `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/checks/g2.AC1.sh`, `.AC2.sh` and `.AC3.sh` (they run `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/checks/g_check.py`). Read `g_check.py` for exactly what each arm grades; it is the executable form of section 1. Do not edit any of them.
7. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
workflows/gateway_battery/index_coverage.py
workflows/gateway_battery/tests/test_index_coverage.py
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~59/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W59-S<k>`;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp (`date -u +%FT%TZ` at filing).

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 2)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-g-2" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/checks/g2.AC1.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line; the green inputs exit 0 with `COVERAGE channels=6 tools=9 rows=4 refusals=0`; `--channel opal-data-harvest` prints `COVERAGE channels=1 tools=2 rows=1 refusals=0`; an unreadable census exits 2 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-g-2" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/checks/g2.AC2.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line; the five planted arms (channel with no row; member b; row naming a non-census tool; unclassified tool; undeclared tool plus an empty c reason) each exit 1 with EXACTLY the expected refusal set, the refusal records carry class, channel and subject, and the denominator block is present -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-g-2" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/checks/g2.AC3.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line (pytest rc=0, at least 6 passed) for `test_index_coverage.py` -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~59/NFRA_MCPINDEX.TO-MX-g-2.fwd23-coverage-gate.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance. In its artifact rows, pin each produced file to the commit that carried it (the checker refuses `PENDING-THIS-COMMIT` for a file committed before the instance): commit the script and the test first, then write the instance naming those commit hashes.
2. Append `<status>complete</status>` to this order only if all three criteria PASS (if the commit gate refuses the flip, leave it and say so).
3. Commit through `.tools/safe-commit.sh` in two commits: (i) the script and the test file; (ii) the proof instance (and the status flip).
4. Report once, with: what you built by part; the three `RESULT:` lines and the `DENOMINATOR:` line of each criterion verbatim; the unit-test count; your commit shas; every place the contract was silent and what you did.

The issuer then merges, runs the real data through your script at the drain and keeps the artifact.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 22, workstream GATEWAY, worker ~59. Source: PRD v0.18 @4b8dcf3b86 (CTO msg 35988). Decomposition `org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round22-GATEWAY.md` (the contracts R22.2 are frozen at the cut). Base dry-runs 2026-10-19: `g2.AC1`, `.AC2`, `.AC3` all FAIL as expected (script and test file absent). The issuer's reference implementation (scratch, not committed) passes `g2.AC1` and `g2.AC2`, so the arms are satisfiable. Gate limb that graded this order: the L6 gate at the issuance commit.

<status>issued</status>
<round>22</round>
<workstream>GATEWAY</workstream>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>
