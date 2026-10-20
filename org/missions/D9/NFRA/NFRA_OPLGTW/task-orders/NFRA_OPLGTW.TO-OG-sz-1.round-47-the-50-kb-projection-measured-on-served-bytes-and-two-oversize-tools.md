# NFRA_OPLGTW task order -- `OG-sz-1` -- the 50 KB projection measured on the bytes actually served (P4), never nulling a whole field (P5), and the two oversize tools projected: `mdpf_get_aggregate_aua` (P6) and `opal_discover` (P7) (round 47; round-46 analysis item 2; rows Z-S413)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-sz-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-sz-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~168</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a code and test change; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's round-46 analysis (`org/missions/D9/NFRA/NFRA_OPLGTW/ledger/ROUND_ANALYSIS.round46.md` @ad17495429), rank 2: "the 50 KB cap is measured on the bytes actually sent; trimming never nulls a whole field; the MDPF envelope and `opal_discover` are projected".
EGRESS CLASS, declared: NONE (every probe uses fakes; no network).
</preflight>

## 1. THE CELL -- `OG-sz-1` (decomposition addendum R3-T.124, round 47, workstream ENRICH-R47-A)

WHY (row Z-S413, the CRO's audit). Every typed tool's answer is supposed to fit a 50 KB projection (`harvest_typed.PROJECT_LIMIT = 51200`). Four defects: **P4** `harvest_typed._size()` measures `json.dumps(obj, default=str)` (compact separators, no indent) but the MCP server serves a dict reply pretty-printed (`indent=2`), so a reply projected to "51,100" is 64.9 KB on the wire (`portal_get_model_portfolio_timeseries`), 75.9 KB (`portal_get_model_positioning`), 55.7 KB and 59.1 KB for two others. **P5** `harvest_typed.project()` pops items off the end of the largest top-level LIST, and when no list is left it sets the largest non-list field to `None` whole: `portal_get_macro` answered `macro: null, truncated: true` over a 93 KB source; `portal_get_valuation` answered 420 bytes with `ranges: []` and `time_series: null`. **P6** `mdpf_get_aggregate_aua` (the `portal_index` integration) answered 743,469 characters: nothing projects it. **P7** `opal_discover` answered 585,084 characters for one subject (137 datasets matched): nothing projects it. A reply over the client's tool-result limit is unreadable, and an uncapped reply is also a load risk on the gateway host.

READ FIRST: `app/harvest_typed.py` (the whole file, 222 lines: `_size`, `project`, `envelope`), `app/integrations/portal_index/integration.py` lines 225-270 (`answer`, `_answer`) and 434-470 (`PortalIndexIntegration._run`), `app/integrations/opal_discover/integration.py` lines 925-958 (`opal_discover`), `tests/test_og_gt0.py` and `tests/test_og_gt5.py` (the two test files that already exercise `project`).

DO (the gateway folder is `infra/aws/ec2/opal-gateway/`):

1. **P4. In `app/harvest_typed.py` measure the size as the server serves it:** `_size(obj)` returns the UTF-8 byte length of `json.dumps(obj, indent=2, default=str)`. `projected_to_bytes` (the fixed-point count of its own digits) uses the same measure, so `projected_to_bytes` equals the indented size of the returned answer. `PROJECT_LIMIT` stays 51200. If an existing assertion in `tests/test_og_gt0.py` or `tests/test_og_gt5.py` pins a number that came from the compact measure, change ONLY that assertion to the new measure and name it in your report.
2. **P5. In `project()` never replace a whole field with `None`.** Keep the existing first move (pop items off the end of the largest top-level list) for a plain list field. When no top-level list is left and the answer is still too big, shrink the largest remaining non-envelope field INSIDE: for a dict, shrink its largest list value(s) the same way (keep a non-empty prefix; every KEY of the dict stays), recursing into nested dicts; for a string, cut it to a shorter non-empty prefix; for a dict whose values are scalars, drop entries from the end. The field stays the same type it was and is never `None` unless it was `None`. `truncated` is `true` and `projected_to_bytes` is the fixed-point size as before. Envelope keys (`as_of`, `source_keys`, `denominator`, `absent_reason`, `truncated`, `projected_to_bytes`) are never dropped or shrunk. An answer that already fits is returned equal to its input with no `truncated` key.
3. **P6. In `app/integrations/portal_index/integration.py` project the tool's answer in `PortalIndexIntegration._run`, AFTER `answer(...)` returns** (leave the module function `answer()` and `_answer()` unchanged: the existing tests and the check call it directly). The answer there is `{"status": "ok", "tool", "bucket", "key", "as_of", "as_of_field", "data": <the served object>}` (or a `no_data` dict, which is small). When its indented size is above 51200, shrink inside `data` the way item 2 does, with these rules: the top-level keys other than `data` are never touched; a list inside `data` whose elements are dicts carrying a date-like ISO key (`date`, `as_of`, `asOf`, `day` or `ts`) in ascending order keeps its NEWEST rows (cut from the front); any other list keeps its first rows (cut from the end). Then add `truncated: true`, `projected_to_bytes` (the fixed-point indented size) and `trimmed`: a dict from the dotted path of each shrunk list inside the answer (for example `data.series`) to `{"total": <original length>, "returned": <served length>, "kept": "newest" | "first"}`. Reuse `harvest_typed.project` or a shared helper you add to `harvest_typed.py`; do not write a second algorithm. The answer of every tool that goes through `_run` is projected (not only `mdpf_get_aggregate_aua`); an answer that fits is returned unchanged.
4. **P7. In `app/integrations/opal_discover/integration.py` project the answer of the `opal_discover` tool** (the lambda passed to `run_integration_tool` in `opal_discover`; `opal_describe` is left as it is). The answer's list is `matches`, ranked best first: keep the FIRST matches that fit 51200 indented bytes, in order; set `truncated: true`, `matches_total` (the original count) and `matches_returned` (the served count), and `projected_to_bytes`. The `answer` sentence is left as the function wrote it. An answer that fits is returned unchanged (no `truncated` key).
5. **The new test file `tests/test_og_sz1.py`** with at least these tests (names fixed): `test_ogsz1_p4_indented_measure`, `test_ogsz1_p5_no_whole_field_null` (dict-of-lists, long string, dict of scalars), `test_ogsz1_p6_newest_kept_and_trimmed_note`, `test_ogsz1_p7_matches_first_kept`, `test_ogsz1_small_answers_unchanged`. Fakes only; build the integrations with the same fake `mcp` and a patched `run_integration_tool` as `tests/test_opal_portal_status_id_shape.py` builds the portal one.

## 2. BOUNDS

- Write only `app/harvest_typed.py`, `app/integrations/portal_index/integration.py`, `app/integrations/opal_discover/integration.py`, `tests/test_og_sz1.py`, the two existing test files named in item 1 (one assertion each at most), `W/` and, if a row is needed, the channel. NO other product file (the callers of `project` in `client_core.py`, `mail_route.py`, `teams_route.py`, `harvest_research.py`, `mdpf_classification.py` and `typed_scope.py` get the new behaviour through `project`; do not edit them), no contract file, no release, no deploy, no Terraform, no AWS or network call.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print an account number, email address or client value.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/harvest_typed.py
infra/aws/ec2/opal-gateway/app/integrations/portal_index/integration.py
infra/aws/ec2/opal-gateway/app/integrations/opal_discover/integration.py
infra/aws/ec2/opal-gateway/tests/test_og_sz1.py
infra/aws/ec2/opal-gateway/tests/test_og_gt0.py
infra/aws/ec2/opal-gateway/tests/test_og_gt5.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~168/` (the tree convention grants it). Rows: id `NFRA_OPLGTW-Z-W168-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-sz-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/sz1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)P4 3000-row list: indented size <= 51200: ok.*P4 projected_to_bytes equals the indented size: ok.*P5 dict-of-lists field: not None, a dict, every key kept: ok.*P5 long string field: a non-empty shorter string, fits: ok.*control: a small answer is equal to its input, no truncated key: ok.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-sz-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/sz1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)P6 6000-row series: indented size <= 51200: ok.*P6 newest rows kept, a shorter non-empty series: ok.*P6 trimmed note names the path, total and kept side: ok.*P6 control: .*: ok.*P7 137 matches: indented size <= 51200: ok.*P7 truncated true, matches_total 137, matches_returned equals the length: ok.*P7 control: .*: ok.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-sz-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/sz1.AC3.sh; echo "exit=$?"</invocation><expect>(?s)new file tests/test_og_sz1.py: [1-9]\d* passed, 0 failed.*neighbours \(\d+\): [1-9]\d* passed, failed names \[\].*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the projection measure and the no-null rule (P4, P5). `AC2`: the two oversize tools (P6, P7), probed through their registered tools. `AC3`: your test file and the 16 existing files that exercise the touched modules (137 tests at the base).

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-sz-1.round-47-the-50-kb-projection-measured-on-served-bytes-and-two-oversize-tools.proof_of_spec.json`. Validate it after your last commit with `python3 -I .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` (`python3`, not `python`: ruling msg 35901). Flip the ONE `<status>` tag to `complete` only if all three PASS, and report once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 47, workstream ENRICH-R47-A, `<risk>WORLD</risk>` is the gateway-path floor. Source: the CTO's round-46 analysis (msg 36165) rank 2 (P4-P7, Z-S413) and the overlap of Z-S424 (the other three oversize tools are `OG-tp-1` and `OG-sx-1`). Z-S420 disarms on this cell and `OG-mg-3` together (the CTO's rule).
- READINGS DISCLOSED TO THE CTO: (1) the measure is the indented size because the server serves `indent=2`; the structured-content copy that a client may also receive is not counted, so a client that counts both sees about twice the figure (not changed here). (2) The new keys `trimmed`, `matches_total`, `matches_returned` are the issuer's. (3) `mdpf_get_aggregate_aua` keeps the NEWEST rows when its rows are date-ascending, which differs from `project()`'s keep-the-first default: a daily spine read newest-first is what a caller wants. (4) The projection for the `portal_index` tools sits in `_run`, so `answer()` stays what its tests call.
- Pre-cut: `AC1` base FAIL as expected (69,616 bytes for a list answer; `macro` `None`; the empty string field), `AC2` base FAIL as expected (567,025 and 447,769 bytes; the two controls hold), `AC3` base FAIL as expected (no test file). The 16 neighbour files pass at the base (137 tests).

<status>pending</status>
<status>complete</status>
<round>47</round>
<workstream>ENRICH-R47-A</workstream>
<slot>~168</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
