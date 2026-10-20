# NFRA_MCPINDEX task order -- `MX-w-1` -- the source comparison: for each tool with an ok result, list the routed source and compare the answer's as-of date with the dates the source holds

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round24-GATEWAY.md</decomp_doc>
<owned_cells>MX-w-1</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-w-1.source-compare</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~77</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule; one new script and one new test file.
comp-iam: DECLARED-NOT-APPLICABLE -- local files only; the live S3 listing path is written but never run by you (you test it with --fake); no grant.
comp-adversary: DECLARED-NOT-APPLICABLE -- the base dry-runs (every criterion FAILs at the base) and the planted arms inside the criteria are the control.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-w-1` (round 24, workstream GATEWAY; PRD v0.19 FWD-24; CTO round-23 analysis, item 1)

Work in your own worktree (cut from `box/sitez`; every path below is relative to its root). Round 23 graded the FWD-24 battery over the 127-tool gateway census: 35 tools read FAIL `source_unchecked`, meaning the answer came back but no second instrument compared it with its source. This cell builds that second instrument as a script: for each tool with an ok result, read the tool's ROUTED source (list-only) and compare the answer's as-of date with the dates the source holds. The issuer runs it live at the drain over the real results; you build and test it offline.

**What to build.** `workflows/gateway_battery/source_compare.py` and `workflows/gateway_battery/tests/test_source_compare.py` (at least 6 tests of your own). The script imports the listing client and the input helpers of the merged `workflows/gateway_battery/partition_windows.py` (`import partition_windows`; scripts are run by path and the folder is on `sys.path`; read that file first: `FakeClient`, `build_client`, `load_json_object`, `Refused`, and how `list_row` pages with `ContinuationToken`). It never reads or writes an object.

### The contract (verbatim from the decomposition; it is the whole specification)

**W1 SOURCE COMPARE** `python workflows/gateway_battery/source_compare.py --census F --routing F --results F --cases F --out F [--fake F]`. Writes `gateway_source_compare/1`: `{"schema","tools":[{"tool","case_ids":[...],"source":{"kind","bucket","prefix"}|null,"instrument":str,"answer_as_of":str|null,"source_dates":[sorted date strings seen under the source],"agrees":true|false|null,"reason":str}],"counts":{"tools","agrees","disagrees","unreadable"}}`, tools sorted by name, one entry per census tool that has at least one RESULT with `status` ok. Source choice: the tool's `source_set` entry of kind `s3` whose bucket/prefix overlaps (one prefix starts with the other) an `answer_source` string of the result; else the first `s3` source of the set in file order; no `s3` source -> `source` is the first source of the set and `agrees` null with a `reason` that names its kind ("store", "integration" or "graph") and says it is not read here. For an `s3` source the instrument lists keys under bucket+prefix (list only, never a get) by importing the listing helper of `partition_windows.py`; `source_dates` are the `YYYY-MM-DD` / `date=YYYY-MM-DD` / `YYYYMMDD` tokens found in the listed keys. `agrees` is true when the result's `as_of` date is among `source_dates`, false when `source_dates` is non-empty and it is not, and null with reason when the result has no `as_of` or the listing has no date token ("undated"), or the listing is empty. `--fake` is a JSON `{"<bucket>|<prefix>": [page, ...]}` of key lists in place of S3 (the format `partition_windows.py --fake` already reads). Same input, same bytes. A tool in the results that is not in the census, or a missing routing entry, exits 2. Stdout `SOURCE tools=T agrees=A disagrees=D unreadable=U`; exit 0 iff `D` is 0.

### Clarifications fixed by the issuer at the cut (the checks grade exactly these; they resolve what the contract leaves open)

1. **The fake format** is the one `partition_windows.py --fake` reads: each page is a `list_objects_v2` response dict (`{"CommonPrefixes":[{"Prefix":...}],"Contents":[{"Key":...}],"IsTruncated":bool,"NextContinuationToken":str}`), and a key's pages are returned in call order. List every page (`ContinuationToken` while `IsTruncated`) with `Delimiter` "/" as `list_row` does; the date tokens are searched in every `CommonPrefixes[].Prefix` and every `Contents[].Key`. A calendar-invalid date (month 13) is not a token. A `YYYYMMDD` token is written in `source_dates` as `YYYY-MM-DD`. `source_dates` is the sorted set, no duplicates.
2. **Results carry no tool name.** Join each result to its tool through the CASES file (`case_id` -> `tool`). `case_ids` of an entry are the case ids of that tool's ok results, in results-file order. A result with another status (error, refused, preview) is ignored. A result whose case maps to a tool not in the census exits 2.
3. **Which result gives `answer_as_of`:** the first ok result, in results-file order, that carries a non-empty `as_of`; if none carries one, `answer_as_of` is null.
4. **Overlap with `answer_source`:** the answer_source strings of ALL the tool's ok results are pooled; a string is compared with `<bucket>/<prefix>` of the source (a leading `s3://` is ignored): they overlap when one starts with the other. The full form `bucket/prefix...` is the one the checks use.
5. **Reasons** (lower-case substrings the checks look for): an `s3` source whose keys hold no date token -> `undated`; an empty listing -> `empty`; a result with no `as_of` -> `as_of`; a source of kind store, integration or graph -> its kind and `not read here`; a routing entry with an empty `source_set` -> `source` is null and the reason says `no source`. `reason` is a string for every entry (empty string allowed when `agrees` is true or false). `instrument` is a non-empty string (for an `s3` source it names a list of bucket and prefix; for a source that is not read, any text such as `none`).
6. **Unreadable** in the counts means `agrees` null. A listing that raises reads `agrees` null with a reason that starts `listing error:`, never an exit and never a false.
7. Exit 2 (stderr line `REFUSED: ...`, NO output file written) for: an unreadable or non-object input file, a `--fake` file that does not exist, a result that maps to a tool outside the census, and a tool with an ok result but no entry in the routing table.

### Inputs you read (you do NOT edit them)

- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round24/fixtures/w1_census.json`, `w1_cases.json`, `w1_results.json`, `w1_routing.json` and `w1_fake.json`: the criteria's fixtures (12 census tools, 12 cases, 12 results, 12 routing entries, 6 fake listings). Read them to see the shapes; the real inputs have the same shapes: `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/evidence/GATEWAY_SURFACE_CENSUS_20261019_v2.json` (tools under `tools[].name`), `.../round23/evidence/ROUTING_TABLE_20261019.json` (`tools[].tool`, `tools[].source_set[]` with `kind`, `bucket`, `prefix`), `.../round23/evidence/results_all_20261019.json` and `cases_all_20261019.json`.
- `workflows/gateway_battery/partition_windows.py` and `workflows/gateway_battery/tests/` (the style of the tests of the other scripts).

### Steps

0. From the worktree root, `git rev-parse --show-toplevel` is your root. The worktree already carries the sparse folder `workflows/gateway_battery`; if another folder you need is missing, `git sparse-checkout add <folder>` is the only sparse change you may make.
1. Read `partition_windows.py` and the five fixtures. Write the script and its test file. The test file holds at least 6 tests of its own: they exercise the script as a subprocess or by importing it with `importlib` from its path, on small inputs you write inside the test with `tmp_path` (not the issuer's fixtures; those are the criteria's). There is no `__init__.py`.
2. Run the three criteria in section 4 until each prints `RESULT: PASS`. Read `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round24/checks/w1_check.py` for exactly what each arm grades; it is the executable form of section 1.

## 2. BOUNDS

1. You change only the files in `<paths>`. Do NOT edit the issuer's fixtures, checks or decomposition, `partition_windows.py`, `members.yaml`, `pending_members.yaml`, the catalog or its row files, the emitter (`emit_catalog_v02.py`), any file under `infra/`, the PRD, or any other file under `workflows/`. No AWS call, no network call (the live S3 path is written but never run by you; you test it with `--fake`), no grant, no deploy, no push.
2. Python 3.9, standard library plus `yaml` only; `boto3` is imported only by the helper's live path. ASCII only in code, comments, strings, output and data files. No type syntax newer than 3.9 (no `X | Y` annotations, no `match`). The commit gate runs `py_compile`, the naming gate and `ruff` for py39.
3. No tool name, channel id, firm or vendor is typed as a whole-string literal in the script (the contract's fixed words are fine); tests under `tests/` and data files are exempt.
4. The script lists and never gets: no call to `get_object`, `download_file`, `put_object`, `delete_object`, `copy_object` or `upload_file`, and the word `list_objects_v2` appears in it (the check reads the source text).
5. The contract in section 1 is the whole specification. Where it is silent, do the smallest thing and say which in your report; do not widen the output.
6. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project: your proof instance is one (commit it with, or before, the last code commit).
7. The checks are `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round24/checks/w1.AC1.sh`, `.AC2.sh` and `.AC3.sh` (they run `.../round24/checks/w1_check.py`). Do not edit any of them.
8. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
workflows/gateway_battery/source_compare.py
workflows/gateway_battery/tests/test_source_compare.py
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~77/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-w-1.source-compare.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W77-S<k>` (`k` the next unused number of your slot);
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp (`date -u +%FT%TZ` at filing).

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 2)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-w-1" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round24/checks/w1.AC1.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line; on the fixtures the stdout line reads SOURCE tools=10 agrees=2 disagrees=1 unreadable=7 and the exit is 1; the output holds one entry per tool with an ok result, sorted, with an error-only tool and a tool with no result absent; the date found across two listing pages reads true, a date off the listing reads false, undated keys, a store, an integration, a graph source, a missing as_of, an empty listing and an empty source set read null with their reasons; the source named by the answer_source string is chosen over the first -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-w-1" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round24/checks/w1.AC2.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line; a planted answer date moves tA from true to false and the counts follow; a planted dated listing moves tC from null to true; no disagreement exits 0; a result for a tool outside the census, a missing routing entry, a missing --fake file and an unreadable results file each exit 2 with no output file; two runs give the same bytes; the script text holds no object read or write call -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-w-1" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round24/checks/w1.AC3.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line (pytest rc=0, at least 6 passed) for `test_source_compare.py` -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~77/NFRA_MCPINDEX.TO-MX-w-1.source-compare.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance. In its artifact rows, pin each produced file to the commit that carried it (the checker refuses `PENDING-THIS-COMMIT` for a file committed before the instance): commit the work first, then write the instance naming those commit hashes.
2. Append `<status>complete</status>` to this order file only if every criterion PASSes (if the commit gate refuses the flip, leave it and say so).
3. Commit through `.tools/safe-commit.sh` in two commits: (i) the work; (ii) the proof instance and the status flip.
4. Report once, with: what you built by part; every `RESULT:` line and `DENOMINATOR:` line of each criterion verbatim; the unit-test count; your commit shas; every place the contract was silent and what you did.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 24, workstream GATEWAY, worker ~77. Source: the CTO's round-23 analysis `ledger/ROUND_ANALYSIS.round23.md` (`1.0.0_SA_CTO~Z`, 2026-10-20 ~12:3xZ), item 1 (`source_unchecked`, 35 tools), and PRD v0.19 @7c42c0c743. Decomposition `org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round24-GATEWAY.md` (the contracts R24.3 are frozen at the cut; the clarifications in section 1 are the issuer's reading of what W1 leaves open and the checks grade exactly them). Base dry-runs 2026-10-20: w1.AC1 base: FAIL as expected (script absent); w1.AC2 base: FAIL as expected (script absent); w1.AC3 base: FAIL as expected (test file absent). A scratch reference implementation kept outside the repository (it imports the merged `partition_windows.py`) passes w1.AC1 (14 of 14 arms), w1.AC2 (9 of 9) and w1.AC3 (7 tests); a planted mutant that ignores `answer_source` when choosing the source FAILs w1.AC1 on three arms. The checks prove the comparison and its refusals on fixtures, not that a live listing is dated the way the fixtures are, which the live run finds. Gate limb that graded this order: the L6 gate at the issuance commit.

<status>complete</status>
<round>24</round>
<workstream>GATEWAY</workstream>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
