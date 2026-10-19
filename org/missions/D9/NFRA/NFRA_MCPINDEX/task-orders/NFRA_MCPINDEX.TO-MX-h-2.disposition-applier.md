# NFRA_MCPINDEX task order -- `MX-h-2` -- the applier: the real census, the tool-index text, the measured windows and the dispositions become the new members text, preserving every comment and every untouched entry byte for byte

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round23-GATEWAY.md</decomp_doc>
<owned_cells>MX-h-2</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-h-2.disposition-applier</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~63</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule; one new script and one new test file.
comp-iam: DECLARED-NOT-APPLICABLE -- local files only; no AWS call, no grant.
comp-adversary: DECLARED-NOT-APPLICABLE -- the base dry-runs (every criterion FAILs at the base) and the planted arms inside the criteria are the control.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-h-2` (round 23, workstream GATEWAY; PRD v0.18 FWD-23; CTO round-22 analysis @44e6950a24)

Work in your own worktree (cut from `box/sitez`; every path below is relative to its root). Round 23 moves the whole gateway census, not one channel, toward FWD-23 (every channel indexed), FWD-24 (every tool tested) and FWD-25 (a sheet per employee). The census it counts against is `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/evidence/GATEWAY_SURFACE_CENSUS_20261019_v2.json` (14 channels, 127 tools, read from the gateway host on 2026-10-19). This is the cell that moves 56 indexed member-b tools to member a without anyone typing a claim, and records the judged remainder.

**What to build.** `workflows/gateway_battery/apply_disposition.py` exactly as the APPLY contract says. The hard part is the text edit: `members.yaml` has a long comment header, comments between entries, and a SECOND list at the end (`buckets:`) whose entries also start `- tool:`. A YAML round trip would destroy the comments, so edit the text: find each changed entry's block inside the top-level `members:` list only, replace that block with the new one, and leave every other line as it was. Compose the claims from the WINDOWS file with the rules in the contract, and check each against the emitter's `validate_claim` (import `workflows/atom_decomposition/emit_catalog_v02.py` by path with `importlib`; it is a pure function and its sibling modules are in the same folder; do not edit it). The issuer runs it on the real members file at the drain.

### The contract (verbatim from the decomposition; it is the whole specification)

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

(The WINDOWS file is the input `--windows`; its `rows[].entity` is the id a census `indexes` entry names.)

**DISPOSITION** `gateway_disposition/1`: `{"schema":"gateway_disposition/1","scope":<free text>,"tools":[{"tool","member":"b"|"c","owner"?,"reason"}]}`. It covers ONLY tools with no catalog index (an indexed tool is made `a` by the applier without a disposition). `c`: `reason` non-empty, no `owner`. `b`: `owner` (a project code or `unowned`) and `reason` (why no row exists and what would create one), both non-empty. A `reason` is ASCII, at least 40 characters, and ENDS with a source reference `[app/<file>.py:<line>]` naming a real line of the gateway source (`infra/aws/ec2/opal-gateway/app/`) where the tool's definition or the code it reaches sits.

**APPLY** `python workflows/gateway_battery/apply_disposition.py --census F --members F --windows F --dispositions F [F ...] --out F [--report F]`:
- Reads the census (`gateway_surface_census/1`), the members file text, the WINDOWS file and the disposition files. Writes the NEW members text to `--out` (never edits `--members` in place) and a report `{"changes":[{"tool","rule"}]}`.
- Only entries inside the top-level `members:` list are edited. The file also has a top-level `buckets:` list whose entries start `- tool:` too; they, the header comments, every comment line between entries and every entry it does not change stay byte for byte. Entry order is unchanged. A changed entry is replaced by its new block (same two-space indentation as the file's other entries).
- Rule `auto_a` (no disposition needed): a `member: b` entry whose census `indexes` is non-empty becomes `{tool, member: a, index: <first of the sorted indexes>, links: <sorted indexes>, history_depth, freshness}` plus the old entry's `bucket` and `bucket_source` if it had them (the old `owner` is dropped).
  - One linked row: `freshness` = the row's WINDOWS entry if `dated`: `{claim: measured, value: <latest>, basis: "s3://<row bucket>/", method: key-date, read_at: <windows read_at>}`; `history_depth` = `{claim: inferred, value: "<earliest>..<latest>", basis: "s3://<row bucket>/", source: "first-level partition listing of the row <entity>", method: partition-listing, read_at: <windows read_at>}`. If the row is not `dated` or has no WINDOWS entry, both are `{claim: absent, reason: <why: not dated at the first level, or no windows entry>}`.
  - Several linked rows: `freshness` = `{claim: absent, reason: "a multi-index tool: each linked row has its own freshness"}`; `history_depth` = `{claim: per-link, links: [one element per linked row in links order, each carrying "row": <entity> and the inferred or absent claim of that row as above]}`.
  - Every composed claim passes `validate_claim` of `workflows/atom_decomposition/emit_catalog_v02.py` (import it by path with importlib; it is a pure function; do not edit that file); a claim that fails is a bug in the applier, exit 2.
- Rule `disposed_b` / `disposed_c`: a tool named in a disposition. A `b` entry becomes `{tool, member: b, owner, reason}` and a `c` entry `{tool, member: c, reason}`, each plus the old `bucket` and `bucket_source` if present. A `member: b` entry named in no disposition and with no index is untouched.
- Refused with exit 2 and NO output file: a disposition tool the census does not serve; one that has census indexes (an indexed tool is never disposed); `member: a` or any member letter but b or c; a `c` with an empty reason; a `b` with no owner or no reason; the same tool in two dispositions or twice; an unreadable windows, census or disposition file.
- Stdout `APPLY auto_a=N disposed_b=B disposed_c=C untouched_b=U`. Same input gives the same bytes.

### Inputs you read (you do NOT edit them)

- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/fixtures/h2_members.yaml`: a members file with a comment header, a comment between entries, five `b` entries, one `a`, one `c` and a trailing `buckets:` list that repeats `- tool: tA1`.
- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/fixtures/h2_census.json`: 7 tools; tA1 has one index, tA2 two, tC1 one, the rest none.
- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/fixtures/h2_windows.json`: rowA dated (2026-09-01..2026-10-08), rowB undated, rowC dated.
- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/fixtures/h2_disp.json`: tA3 as `b`, tB1 as `c`.
- Real inputs you do NOT run: `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/evidence/GATEWAY_SURFACE_CENSUS_20261019_v2.json` (the census), `workflows/atom_decomposition/tool_index/members.yaml` and `workflows/atom_decomposition/tool_index/pending_members.yaml`.

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
6. The checks are `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/checks/h2.AC1.sh`, `.AC2.sh` and `.AC3.sh` (they run `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/checks/h_check.py`). Read `h_check.py` for exactly what each arm grades; it is the executable form of section 1. Do not edit any of them.
7. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
workflows/gateway_battery/apply_disposition.py
workflows/gateway_battery/tests/test_apply_disposition.py
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~63/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-h-2.disposition-applier.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W63-S<k>` (`k` the next unused number of your slot);
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp (`date -u +%FT%TZ` at filing).

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 2)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-h-2" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/checks/h2.AC1.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line; rc 0; `APPLY auto_a=2 disposed_b=1 disposed_c=1 untouched_b=1`; the header, the between-entry comment and the buckets list kept byte for byte; tB2, tC1 and tD byte-identical; entry order unchanged; tA1 becomes a with a measured key-date freshness and an inferred partition-listing window; tA2 a with two links, absent freshness and a per-link depth; tA3 b with owner and reason; tB1 c with reason; every claim passes validate_claim; the report lists the four changes -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-h-2" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/checks/h2.AC2.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line; eight refusal arms (a tool the census does not serve; a for a tool with no index; c without reason; b without owner; b without reason; the same tool twice; a tool that already has an index; an unknown member letter) each exit 2 with no output file; an unreadable windows file exits 2; two runs give the same bytes; a linked row missing from the windows reads absent with a reason -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-h-2" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/checks/h2.AC3.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line (pytest rc=0, at least 8 passed) for `test_apply_disposition.py` -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~63/NFRA_MCPINDEX.TO-MX-h-2.disposition-applier.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance. In its artifact rows, pin each produced file to the commit that carried it (the checker refuses `PENDING-THIS-COMMIT` for a file committed before the instance): commit the work first, then write the instance naming those commit hashes.
2. Append `<status>complete</status>` to this order file only if every criterion PASSes (if the commit gate refuses the flip, leave it and say so).
3. Commit through `.tools/safe-commit.sh` in two commits: (i) the work; (ii) the proof instance and the status flip.
4. Report once, with: what you built by part; every `RESULT:` line and `DENOMINATOR:` line of each criterion verbatim; the unit-test count (code cells); your commit shas; every place the contract was silent and what you did.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 23, workstream GATEWAY, worker ~63. Source: the CTO's round-22 analysis @44e6950a24 (msg 35997) and PRD v0.18 @4b8dcf3b86, cut on the CORRECTED census. Decomposition `org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round23-GATEWAY.md` (the contracts R23.2 are frozen at the cut). Base dry-runs 2026-10-19: every criterion of this order FAILs as expected (the script, test file or deliverable is absent, or the gate lacks the explained field). The issuer's scratch reference passes `h2.AC1` and `h2.AC2` (it first failed `h2.AC1` on the `buckets:` trap, which is why the arm exists). Gate limb that graded this order: the L6 gate at the issuance commit.

<status>issued</status>
<round>23</round>
<workstream>GATEWAY</workstream>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>
