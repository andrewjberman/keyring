# NFRA_MCPINDEX task order -- `MX-g-1` -- the census reducer and the grants extractor: a served `/gateway` breakdown body becomes the frozen channel census and the per-employee grants file

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round22-GATEWAY.md</decomp_doc>
<owned_cells>MX-g-1</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-g-1.census-reducer-and-grants-extractor</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~58</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule; one new script and one new test file.
comp-iam: DECLARED-NOT-APPLICABLE -- local files only; no AWS call, no grant.
comp-adversary: DECLARED-NOT-APPLICABLE -- the base dry-runs (all three criteria FAIL at the base) and the planted arms inside the criteria are the control.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-g-1` (round 22, workstream GATEWAY; PRD v0.18 FWD-23, FWD-24, FWD-25)

Work in your own worktree (cut from `box/sitez`; every path below is relative to its root). Round 22 builds, for ONE gateway channel, a thread of four small scripts in a NEW folder `workflows/gateway_battery/`: a census reducer, a coverage gate, a tool battery and a cheat-sheet generator. They share frozen data contracts and never call each other, so you build yours alone. You build **`gateway_census.py`** and its test file.

**What to build.** `workflows/gateway_battery/gateway_census.py` with two subcommands, `census` and `grants`, exactly as the contract says. `census` reduces the body of the gateway's `GET /api/admin/gateway/breakdown` (channels of every kind, the tools under each, the tools' catalog `indexes`, the (vendor, firm) `segments` of the two segmented buckets, and the `holders`) into the committed census; `grants` extracts who may call what. Both read ONE file and write ONE file; neither opens the network. The census is the denominator FWD-23, FWD-24 and FWD-25 count against, so its counts are exact and its refusals (exit 2) are loud.

### The contract (verbatim from the decomposition; it is the whole specification)

**CENSUS** `gateway_surface_census/1`, written by `python workflows/gateway_battery/gateway_census.py census --breakdown FILE --out FILE`:
```
{"schema":"gateway_surface_census/1","claim":"measured","source":"admin_gateway_breakdown body","read_at":<breakdown.read_at>,
 "channels":[{"id","name","kind","min_tier","tools":[sorted names],"segments":[{"vendor","firm","tools"}] (only when the breakdown channel has it)}],   // breakdown order
 "tools":[{"name","access","write_class","data_class","indexes":[sorted],"channels":[sorted ids]}],                                             // sorted by name
 "counts":{"channels","by_kind":{"bucket","store","integration","native","undeclared"},"segments","tools_distinct","tool_channel_pairs","tools_unindexed"}}
```
`by_kind` always carries all five keys. `segments` counts the entries of every channel's `segments`. `tools_unindexed` counts distinct tools whose `indexes` is empty. First stdout line: `CENSUS channels=N bucket=a store=b integration=c native=d undeclared=e segments=S tools=T pairs=P unindexed=U`. Exit 2 (one `ERROR:` line) on a missing or non-JSON file, a body with an `error` key, no `channels` list or an empty one, a channel without `id`, `kind` or a `tools` list, or a tool without `name`.

**GRANTS** `gateway_grants/1`, written by `... gateway_census.py grants --breakdown FILE --out FILE` (same exit 2 rules):
```
{"schema":"gateway_grants/1","claim":"measured","read_at":...,
 "principals":[{"who","how":[sorted distinct],"tools":[sorted union],"channels":[sorted ids where he or she is a holder],"by_channel":{"<id>":[sorted tools held there]}}],   // sorted by who
 "population":{"tools":[sorted union],"channels":[sorted ids]},
 "counts":{"principals","population_tools"}}
```
A holder whose `who` holds neither `@` nor `/` is the population row (the signed-in population); it goes to `population`, never to `principals`. Stdout: `GRANTS principals=N population_tools=K`.

### Fixtures you read (the criteria drive your script with them; you do NOT edit them)

- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/fixtures/breakdown_sample.json`: a small breakdown body (6 channels, one of each of the five kinds plus a second bucket, 9 distinct tools, one tool in two channels, one `segments` list, 3 holder rows incl. the population row).
- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/fixtures/expected_census.json` and `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/fixtures/expected_grants.json`: the files your `census` and `grants` commands must reproduce (compared as parsed JSON; key order is free).

### Steps

0. From the worktree root, `git rev-parse --show-toplevel` is your root. If `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/` or `workflows/` is missing, run `git sparse-checkout add <folder>` once (the only sparse change you may make). `python -m pytest --version` works.
1. Read the fixtures named above and `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/checks/g_check.py` (the arms for your cell). Make the script and its test file. The test file holds at least 6 tests of its own: they exercise the script as a subprocess or by importing it with `importlib` from its path, on small inputs you write inside the test with `tmp_path` (not the issuer's fixtures; those are the criteria's). There is no `__init__.py`: scripts are run by path.
2. Run the three criteria in section 4 until each prints `RESULT: PASS`.


## 2. BOUNDS

1. You change only the files in `<paths>`. Do NOT edit the issuer's fixtures, checks or decomposition, any other file under `workflows/`, any gateway file under `infra/`, the catalog, `members.yaml`, the emitter, a registry file or the PRD. No AWS call, no network call, no grant, no deploy, no push. Your script reads local files only.
2. Python 3.9, standard library plus `yaml` (PyYAML, already installed) only. ASCII only in code, comments, strings and output. No type syntax newer than 3.9 (no `X | Y` annotations, no `match`). The commit gate runs `py_compile`, the naming gate and `ruff` for py39.
3. No tool name, channel id, firm or vendor is typed as a whole-string literal in the script (the five channel kinds, the verdict words and the fail-class words of the contract are fixed vocabulary and may be literals); tests under `tests/` are exempt.
4. The contract in section 1 is the whole specification. Where it is silent, do the smallest thing and say which in your report; do not widen the output.
5. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project: your proof instance is one (commit it with, or before, the last code commit).
6. The checks are `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/checks/g1.AC1.sh`, `.AC2.sh` and `.AC3.sh` (they run `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/checks/g_check.py`). Read `g_check.py` for exactly what each arm grades; it is the executable form of section 1. Do not edit any of them.
7. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
workflows/gateway_battery/gateway_census.py
workflows/gateway_battery/tests/test_gateway_census.py
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~58/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W58-S<k>`;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp (`date -u +%FT%TZ` at filing).

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 2)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-g-1" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/checks/g1.AC1.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line; census rc 0; the stdout line `CENSUS channels=6 bucket=2 store=1 integration=1 native=1 undeclared=1 segments=2 tools=9 pairs=10 unindexed=4`; the census JSON equals `expected_census.json` -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-g-1" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/checks/g1.AC2.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line; grants rc 0; the stdout line `GRANTS principals=2 population_tools=1`; the grants JSON equals `expected_grants.json`; an error body, an empty `channels`, a non-JSON file and a channel without `tools` each exit 2 from BOTH subcommands -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-g-1" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/checks/g1.AC3.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line (pytest rc=0, at least 6 passed) for `test_gateway_census.py` -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~58/NFRA_MCPINDEX.TO-MX-g-1.census-reducer-and-grants-extractor.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance. In its artifact rows, pin each produced file to the commit that carried it (the checker refuses `PENDING-THIS-COMMIT` for a file committed before the instance): commit the script and the test first, then write the instance naming those commit hashes.
2. Append `<status>complete</status>` to this order only if all three criteria PASS (if the commit gate refuses the flip, leave it and say so).
3. Commit through `.tools/safe-commit.sh` in two commits: (i) the script and the test file; (ii) the proof instance (and the status flip).
4. Report once, with: what you built by part; the three `RESULT:` lines and the `DENOMINATOR:` line of each criterion verbatim; the unit-test count; your commit shas; every place the contract was silent and what you did.

The issuer then merges, runs the real data through your script at the drain and keeps the artifact.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 22, workstream GATEWAY, worker ~58. Source: PRD v0.18 @4b8dcf3b86 (CTO msg 35988). Decomposition `org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round22-GATEWAY.md` (the contracts R22.2 are frozen at the cut). Base dry-runs 2026-10-19: `g1.AC1`, `.AC2`, `.AC3` all FAIL as expected (script and test file absent). The issuer's reference implementation (scratch, not committed) passes `g1.AC1` and `g1.AC2`, so the arms are satisfiable. Gate limb that graded this order: the L6 gate at the issuance commit.

<status>issued</status>
<round>22</round>
<workstream>GATEWAY</workstream>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>
