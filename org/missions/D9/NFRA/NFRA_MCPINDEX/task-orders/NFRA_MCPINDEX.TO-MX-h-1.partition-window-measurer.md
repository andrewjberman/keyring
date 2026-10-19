# NFRA_MCPINDEX task order -- `MX-h-1` -- the partition-window measurer: a list of catalog rows becomes the first-level date window of each row's S3 table, read by listing alone

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round23-GATEWAY.md</decomp_doc>
<owned_cells>MX-h-1</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-h-1.partition-window-measurer</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~62</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule; one new script and one new test file.
comp-iam: DECLARED-NOT-APPLICABLE -- local files only; no AWS call, no grant.
comp-adversary: DECLARED-NOT-APPLICABLE -- the base dry-runs (every criterion FAILs at the base) and the planted arms inside the criteria are the control.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-h-1` (round 23, workstream GATEWAY; PRD v0.18 FWD-23; CTO round-22 analysis @44e6950a24)

Work in your own worktree (cut from `box/sitez`; every path below is relative to its root). Round 23 moves the whole gateway census, not one channel, toward FWD-23 (every channel indexed), FWD-24 (every tool tested) and FWD-25 (a sheet per employee). The census it counts against is `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/evidence/GATEWAY_SURFACE_CENSUS_20261019_v2.json` (14 channels, 127 tools, read from the gateway host on 2026-10-19). This cell is the measurer that lets a tool's depth and freshness be MEASURED instead of typed.

**What to build.** `workflows/gateway_battery/partition_windows.py` exactly as the ROWS and WINDOWS contract says. For each catalog row it lists the row's table prefix in S3 (list calls only, first level, every page) and reports the earliest and latest date partition. It never reads, writes, copies or deletes an object. The issuer runs it live with the default `boto3` client; you test it only with `--fake`.

### The contract (verbatim from the decomposition; it is the whole specification)

**ROWS** (input to the measurer): `{"rows":[{"entity","bucket","prefix"}]}`; a row's `prefix` is the S3 key prefix of its table (the catalog row's `prefix` field).

**WINDOWS** `partition_windows/1`, written by `python workflows/gateway_battery/partition_windows.py --rows FILE --out FILE [--fake FILE] [--now UTC_STAMP]`:
```
{"schema":"partition_windows/1","read_at":<--now, else the UTC clock to the second, form YYYY-MM-DDTHH:MM:SSZ>,"claim":"measured",
 "rows":[{"entity","bucket","prefix","kind":"dated|undated|empty|error","partition_key","earliest","latest","partitions","error"?}]}
```
- Each row is listed with `list_objects_v2(Bucket, Prefix, Delimiter="/")`, every page (`ContinuationToken` while `IsTruncated`). The measurer calls `list_objects_v2` and nothing else: no object read, write, copy or delete.
- A first-level common prefix whose tail (after the row prefix) is `<key>=YYYY-MM-DD/` (a valid calendar date) is a date partition; `partition_key` is the first such `<key>`; `earliest` and `latest` are the minimum and maximum dates; `partitions` counts them. Other folders and bad dates are ignored.
- `dated`: at least one date partition. `undated`: entries came back but no date partition. `empty`: nothing under the prefix. `error`: the listing raised; `error` holds `<ExceptionName>: <text>`; the other fields are null and `partitions` is 0.
- `--fake FILE` replaces the S3 client with a fake that answers from `{"<bucket>|<prefix>": [page, page, ...]}` (a page is a `list_objects_v2` response dict, returned in order per call; a missing key raises `KeyError`, which reads as `error`). Without `--fake` the client is `boto3.client("s3")`. Tests and the criteria use `--fake`; only the issuer runs it live.
- Stdout `WINDOWS rows=N dated=a undated=b empty=c error=d`. Exit 0 iff `error` is 0, 1 otherwise (the file is written either way), 2 on an unreadable rows file, no `rows`, an empty list, or a row without `entity`, `bucket` or `prefix`. Same input and `--now` give the same bytes.

### Inputs you read (you do NOT edit them)

- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/fixtures/h1_rows.json` and `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/fixtures/h1_fake_listings.json`: 7 rows and the fake pages they read (two pages for one row; an `as_of` key; a prefix mixing a good date, a bad date and a non-date folder; a row of security folders; an empty one; one with no fake listing; one with only objects).
- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/fixtures/h1_expected` is not a file: the arms in `h_check.py` hold the expected values.

### Steps

0. From the worktree root, `git rev-parse --show-toplevel` is your root. The worktree already carries the sparse folders `workflows/gateway_battery`, `workflows/gateway_battery/tests`, `workflows/atom_decomposition` and `infra/aws/ec2/opal-gateway/app`; if another folder you need is missing, `git sparse-checkout add <folder>` is the only sparse change you may make.
1. Read the fixtures named above and `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/checks/h_check.py` (the arms for your cell). Make the script and its test file. The test file holds at least 6 tests of its own: they exercise the script as a subprocess or by importing it with `importlib` from its path, on small inputs you write inside the test with `tmp_path` (not the issuer's fixtures; those are the criteria's). There is no `__init__.py`: scripts are run by path.
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
workflows/gateway_battery/partition_windows.py
workflows/gateway_battery/tests/test_partition_windows.py
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~62/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-h-1.partition-window-measurer.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W62-S<k>` (`k` the next unused number of your slot);
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp (`date -u +%FT%TZ` at filing).

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 2)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-h-1" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/checks/h1.AC1.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line; rc 1 with the file written; `WINDOWS rows=7 dated=3 undated=2 empty=1 error=1`; the header; the two-page window 2026-09-28..2026-10-08 with 4 partitions; the as_of key; the mixed prefix; undated and contents-only; empty; the error row with its text -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-h-1" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/checks/h1.AC2.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line; two runs give the same bytes; the source names no object read, write, copy or delete call; a missing rows key, a row without prefix, a row without bucket, an empty list and an absent file each exit 2 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-h-1" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/checks/h1.AC3.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line (pytest rc=0, at least 6 passed) for `test_partition_windows.py` -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~62/NFRA_MCPINDEX.TO-MX-h-1.partition-window-measurer.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance. In its artifact rows, pin each produced file to the commit that carried it (the checker refuses `PENDING-THIS-COMMIT` for a file committed before the instance): commit the work first, then write the instance naming those commit hashes.
2. Append `<status>complete</status>` to this order file only if every criterion PASSes (if the commit gate refuses the flip, leave it and say so).
3. Commit through `.tools/safe-commit.sh` in two commits: (i) the work; (ii) the proof instance and the status flip.
4. Report once, with: what you built by part; every `RESULT:` line and `DENOMINATOR:` line of each criterion verbatim; the unit-test count (code cells); your commit shas; every place the contract was silent and what you did.
5. When you finish, the issuer may continue you with a second order (`MX-h-6`) on the same worktree; its face arrives as your next message.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 23, workstream GATEWAY, worker ~62. Source: the CTO's round-22 analysis @44e6950a24 (msg 35997) and PRD v0.18 @4b8dcf3b86, cut on the CORRECTED census. Decomposition `org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round23-GATEWAY.md` (the contracts R23.2 are frozen at the cut). Base dry-runs 2026-10-19: every criterion of this order FAILs as expected (the script, test file or deliverable is absent, or the gate lacks the explained field). The issuer's scratch reference passes `h1.AC1` and `h1.AC2`. Gate limb that graded this order: the L6 gate at the issuance commit.

<status>issued</status>
<round>23</round>
<workstream>GATEWAY</workstream>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
