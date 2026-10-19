# NFRA_MCPINDEX task order -- `MX-r-1` -- the routing-table emitter: every (tool, linked row) pair is ROUTED or MISROUTED against the tool's traced source set, with the intent and display checks and three planted negatives

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round23-GATEWAY.md</decomp_doc>
<owned_cells>MX-r-1</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-r-1.routing-table-emitter</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~70</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule; one new script and one new test file.
comp-iam: DECLARED-NOT-APPLICABLE -- local files only; no AWS call, no grant.
comp-adversary: DECLARED-NOT-APPLICABLE -- the base dry-runs (every criterion FAILs at the base) and the planted arms inside the criteria are the control.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-r-1` (round 23, workstream GATEWAY; PRD v0.18 FWD-23; CTO round-22 analysis @44e6950a24)

Work in your own worktree (cut from `box/sitez`; every path below is relative to its root). Round 23 moves the whole gateway census, not one channel, toward FWD-23 (every channel indexed), FWD-24 (every tool tested) and FWD-25 (a sheet per employee). The census it counts against is `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/evidence/GATEWAY_SURFACE_CENSUS_20261019_v2.json` (14 channels, 127 tools, read from the gateway host on 2026-10-19). Andrew asked why the gateway page shows Black Diamond indexes on Schwab tools. The PRD's answer is one committed, re-runnable script that emits the table of every tool's source line, linked rows and verdict.

**What to build.** `workflows/gateway_battery/routing_table.py` exactly as the ROUTING TABLE contract says, reading SOURCE SETS files that other cells write (you test with the issuer's small fixtures). Three checks and one precedence: link (is each linked row inside a source the tool reads), intent (does the tool read only vendors its declared scope allows) and display (is it listed only under vendors it reads), classed link, code and display. The three `--plant` modes are part of the deliverable: each applies one defect in memory to a tool and must be detected with its own class; they are how the table proves it can fail. It never opens the network and never changes its inputs.

### The contract (verbatim from the decomposition; it is the whole specification)

**SOURCE SETS** `gateway_source_sets/1` (the TRACE of what each tool's code can read; a data file written by a worker who read the code):
```
{"schema":"gateway_source_sets/1","scope":<free text>,"tools":[{"tool","vendors":[sorted distinct vendors of its sources],
  "sources":[{"kind":"s3"|"store"|"integration"|"graph","bucket"?,"prefix"?,"store"?,"integration"?,"graph"?,"vendor","cite":"app/<file>.py:<line>"}]}]}
```
- One entry per tool of the cell's scope, once. One source per dispatch branch the code can take (a multi-vendor `client_*` tool has one source per vendor branch).
- `s3` carries `bucket` (the bucket id, resolved from the constant or config key the code uses) and `prefix` (the key prefix that branch reads; the empty string only when it reads the whole bucket); `store` carries `store`; `integration` carries `integration`; `graph` carries `graph` (the Microsoft Graph endpoint family).
- `vendor` is the data's owner: the catalog's own vendor values (`schwab`, `blackdiamond`, `orion`, `eclipse`, `smartx`, `commonwealth`, `gateway`, `market`) or `opal` (Opal's own non-client data), `ycharts`, `microsoft`, `bloomberg`, `other`.
- `cite` is `app/<file>.py:<line>` of the line that names the source or the branch that selects it; the cited file must contain the bucket, store, integration or graph string. `bucket_source` in `members.yaml` and the tool's linked rows are index CLAIMS: the trace is checked against them and never copied from them; a disagreement is a surprise row.

**ROUTING TABLE** `gateway_routing_table/1`, emitted by `python workflows/gateway_battery/routing_table.py --census F --catalog F --sources F [F ...] --out F [--channel ID ...] [--plant link|code|display --tool NAME]`:
- Inputs: the CENSUS (channels, `segments`, each tool's `indexes`), the catalog (rows from `silver_datasets`, `portal_datasets` and `harvest_datasets` with `entity`, `bucket`, `prefix`, `vendor`; channel artifacts `channels[].artifacts[]` with `entity` and `key` take the catalog's top-level `bucket` and the `key` as their prefix), and one or more SOURCE SETS files (a source with no `cite` or no `kind` is refused, exit 2).
- Per census tool (all, or the `--channel` ones), an entry `{"tool","channel","declared_vendors":[sorted],"source_set":[the tool's sources],"pairs":[{"row","row_source":{"bucket","prefix"}|null,"verdict":"ROUTED"|"MISROUTED"|"UNRESOLVED","class":null|"link"}] (sorted by row),"verdict":"ROUTED"|"MISROUTED"|"UNTRACED","class":null|"link"|"code"|"display"}`, sorted by tool, plus `"counts"` (`tools`, `pairs`, `routed_pairs`, `link`, `code`, `display`, `untraced`, `unresolved`).
- **Link check**, per (tool, linked row) pair: the row's source is its `bucket` and `prefix`; the pair is `ROUTED` when some `s3` source of the tool has the same `bucket` and one of the two prefixes starts with the other; otherwise `MISROUTED` (class `link`). A linked id that names no catalog row is `UNRESOLVED` (counted, never a defect).
- **Intent check**, per tool: `declared_vendors` is the set of `vendor` values of the census `segments` entries that list the tool, plus the tool's channel id when that id is itself a vendor name (a vendor value of any catalog row, or `ycharts`). When `declared_vendors` is not empty, every vendor of the tool's sources must be in it, else the tool is `MISROUTED` (class `code`): it reads outside its declared scope. The tool's name is never consulted.
- **Display check**, per tool: every vendor of a census `segments` entry that lists the tool must be a vendor of the tool's sources, else `MISROUTED` (class `display`): the page lists it under a segment it does not serve.
- Tool verdict and class, in this order: `UNTRACED` when no source set names the tool; else `code` if the intent check fails; else `link` if any pair is `MISROUTED`; else `display` if the display check fails; else `ROUTED`.
- **Planted negatives**: `--plant KIND --tool NAME` applies ONE defect to that tool in memory (the real inputs are not changed) and writes the table for the planted state: `link` appends a catalog row, from a bucket that none of the tool's sources names, to the tool's linked rows; `code` appends an `s3` source with bucket `planted-bucket`, an empty prefix, cite `app/planted.py:1` and a vendor that none of the tool's sources has; `display` adds a `segments` entry listing the tool under a vendor that none of its sources has. It prints `PLANT kind=K tool=T verdict=MISROUTED class=K` and exits 0 when the table reads that tool `MISROUTED` of class K; it prints `PLANT-MISSED kind=K tool=T` and exits 3 otherwise; it exits 2 when the tool is not in the census.
- Stdout without `--plant`: `ROUTING tools=T pairs=P routed_pairs=R misrouted_tools=M link=a code=b display=c untraced=u`. Exit 0 iff `M` and `u` are 0, 1 otherwise (the file is written either way), 2 on unreadable input. The same input gives the same bytes.

### Inputs you read (you do NOT edit them)

- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/fixtures/r1_census.json`: 4 channels (an integration `schwab`, an integration `blackdiamond`, a bucket `assets` with two vendor segments, a native one), 7 tools.
- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/fixtures/r1_catalog.yaml`: 3 rows (Schwab, Black Diamond, market).
- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/fixtures/r1_sources.json`: source sets for 6 of the 7 tools, among them a Schwab tool whose linked rows include the Black Diamond row (a link defect), a Schwab tool whose code reads a Black Diamond source (a code defect) and a tool listed under a vendor segment it does not read (a display defect); `tU1` has no source set.

### Steps

0. From the worktree root, `git rev-parse --show-toplevel` is your root. The worktree already carries the sparse folders `workflows/gateway_battery`, `workflows/gateway_battery/tests`, `workflows/atom_decomposition` and `infra/aws/ec2/opal-gateway/app`; if another folder you need is missing, `git sparse-checkout add <folder>` is the only sparse change you may make.
1. Read the fixtures named above and `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/checks/h_check.py` (the arms for your cell). Make the script and its test file. The test file holds at least 8 tests of its own: they exercise the script as a subprocess or by importing it with `importlib` from its path, on small inputs you write inside the test with `tmp_path` (not the issuer's fixtures; those are the criteria's). There is no `__init__.py`: scripts are run by path.
2. Run the three criteria in section 4 until each prints `RESULT: PASS`.

## 2. BOUNDS

1. You change only the files in `<paths>`. Do NOT edit the issuer's fixtures, checks or decomposition, `members.yaml`, `pending_members.yaml`, the catalog or its row files, the emitter (`emit_catalog_v02.py`), any file under `infra/`, the PRD, or any other file under `workflows/`. No AWS call, no network call (the measurer's live S3 path is written but never run by you; you test it with `--fake`), no grant, no deploy, no push.
2. Python 3.9, standard library plus `yaml` (PyYAML, installed) only; the measurer imports `boto3` only inside the live path. ASCII only in code, comments, strings, output and data files. No type syntax newer than 3.9 (no `X | Y` annotations, no `match`). The commit gate runs `py_compile`, the naming gate and `ruff` for py39.
3. No tool name, channel id, firm or vendor is typed as a whole-string literal in a script (the contract's fixed words are fine); tests under `tests/` and data files are exempt.
4. The contract in section 1 is the whole specification. Where it is silent, do the smallest thing and say which in your report; do not widen the output.
5. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project: your proof instance is one (commit it with, or before, the last code commit).
6. The checks are `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/checks/h1.AC1.sh`, `.AC2.sh` and `.AC3.sh` (they run `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/checks/h_check.py`). Read `h_check.py` for exactly what each arm grades; it is the executable form of section 1. Do not edit any of them.
7. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
workflows/gateway_battery/routing_table.py
workflows/gateway_battery/tests/test_routing_table.py
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~70/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-r-1.routing-table-emitter.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W70-S<k>` (`k` the next unused number of your slot);
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp (`date -u +%FT%TZ` at filing).

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 2)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-r-1" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/checks/r1.AC1.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line; rc 1 with the table written; `ROUTING tools=7 pairs=8 routed_pairs=7 misrouted_tools=3 link=1 code=1 display=1 untraced=1`; clean tools ROUTED; the Black Diamond row linked on a Schwab tool is MISROUTED (link) and its Schwab row ROUTED; a Schwab tool whose code reads Black Diamond is MISROUTED (code) with a ROUTED link; a tool listed under a vendor it does not read is MISROUTED (display); a tool with no source set is UNTRACED; every traced tool carries its source set with a cite per member; the counts -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-r-1" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/checks/r1.AC2.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line; the three planted negatives on tS1 (link, code, display) each print their PLANT line and exit 0 with the planted tool MISROUTED of that class; two runs give the same bytes; a plant on a tool the census does not serve, a source with no cite and an absent census each exit 2 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-r-1" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/checks/r1.AC3.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line (pytest rc=0, at least 8 passed) for `test_routing_table.py` -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~70/NFRA_MCPINDEX.TO-MX-r-1.routing-table-emitter.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance. In its artifact rows, pin each produced file to the commit that carried it (the checker refuses `PENDING-THIS-COMMIT` for a file committed before the instance): commit the work first, then write the instance naming those commit hashes.
2. Append `<status>complete</status>` to this order file only if every criterion PASSes (if the commit gate refuses the flip, leave it and say so).
3. Commit through `.tools/safe-commit.sh` in two commits: (i) the work; (ii) the proof instance and the status flip.
4. Report once, with: what you built by part; every `RESULT:` line and `DENOMINATOR:` line of each criterion verbatim; the unit-test count (code cells); your commit shas; every place the contract was silent and what you did.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 23, workstream GATEWAY, worker ~70. Source: the CTO's round-22 analysis @44e6950a24 (msg 35997) and PRD v0.18 @4b8dcf3b86, cut on the CORRECTED census. Decomposition `org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round23-GATEWAY.md` (the contracts R23.2 are frozen at the cut). Base dry-runs 2026-10-19: every criterion of this order FAILs as expected (the script, test file or deliverable is absent, or the gate lacks the explained field). The issuer's scratch reference passes `r1.AC1` and `r1.AC2`. Gate limb that graded this order: the L6 gate at the issuance commit.

<status>issued</status>
<round>23</round>
<workstream>GATEWAY-TRACE</workstream>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
