# NFRA_MCPINDEX task order -- `MX-y-4` -- the link rule of the routing table also routes a store row to a store or integration source named for its table, a templated `<firm>` prefix, and prefixes that differ only in `-` against `_`

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round25-GATEWAY.md</decomp_doc>
<owned_cells>MX-y-4</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-y-4.link-rule-nons3</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~87</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule; an edit to one existing script and one new test file.
comp-iam: DECLARED-NOT-APPLICABLE -- local files only; no AWS call, no grant.
comp-adversary: DECLARED-NOT-APPLICABLE -- the base dry-runs (the new-behavior arms of AC1 and AC2 FAIL at the base, the regression arms pass there, AC3 FAILs) and the planted negatives inside the criteria are the control.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-y-4` (round 25, workstream GATEWAY; PRD v0.19 FWD-23; CTO round-24 analysis `ledger/ROUND_ANALYSIS.round24.md` item 6, "the 7 remaining link misroutes")

Work in your own worktree (cut from `box/sitez`; every path below is relative to its root). The routing emitter `workflows/gateway_battery/routing_table.py` (merged, rounds 23 and 24) grades every (tool, linked catalog row) pair with the LINK rule: the row's `bucket` equals an `s3` source's `bucket` and one of the two prefixes starts with the other. On the round-24 inputs 7 tools read MISROUTED of class `link`, for three reasons the rule cannot see: (a) the row is a STORE row (its `bucket` is the word `dynamodb`, and later `amgt-scoped-api`) and the tool's source is of kind `store` or `integration`, never `s3`; (b) the row prefix carries a `<firm>` template (`mdpf/feeds/model_composition/<firm>/`) while the source names a concrete firm; (c) the row and the source name the same prefix with `-` in one and `_` in the other (`research-continuation` against `research_continuation`). You EDIT the script and add one new test file; you change only how a pair is matched.

**First step.** Run `git sparse-checkout add infra/aws/ec2/opal-gateway/app workflows/atom_decomposition workflows/gateway_battery` (the only sparse change you may make): the catalog and the source-set files are read by the criteria.

**What to build.** In `workflows/gateway_battery/routing_table.py` add the link matching below and use it in `grade_pairs` (the pair grade) and in the `link` plant of `apply_plant`. Read the script first. Add `workflows/gateway_battery/tests/test_routing_links.py` with at least 6 tests of your own. Nothing else changes: `build_serves` keeps using the existing `s3_matches` (the serves output stays byte-identical), the output keys of a pair (`row`, `row_source` with exactly the keys `bucket` and `prefix`, `verdict`, `class`) do not change, and the existing `tests/test_routing_table.py` and `tests/test_routing_serves.py` must keep passing unchanged.

### The contract (verbatim from the decomposition; it is the whole specification)

**Y4 LINK RULE FOR NON-S3 SOURCES AND TEMPLATED OR TWIN PREFIXES.** In `routing_table.py`: a pair (tool, row) is ROUTED when (i) the row's `bucket` is a store word (`dynamodb`, `graph`, `amgt-scoped-api`) and the tool has a source of kind `store` or `integration` whose name (`store` or `integration` field) equals the row's `table` after lower-casing and treating `-` and `_` as equal; (ii) the row prefix holds a `<firm>` (or any `<...>`) segment and an `s3` source has the same bucket and a prefix that matches the row prefix with each `<...>` segment standing for exactly one path segment; (iii) the row prefix and an `s3` source prefix of the same bucket are equal after treating `-` and `_` as equal. Everything else is unchanged: the round-24 table on the round-24 inputs differs only in the pairs these three rules now route (`counts` and the `link` class move; `code` and `display` do not), shown by a before/after diff in the cell report. The three `--plant` modes still fire on the fixtures.

### Four clarifications the issuer has settled (follow them)

1. **The row's table.** A catalog row may carry a `table` field (the store rows do). Read it in `catalog_info` into the row records and into the link lookup (`by_entity`) as an INTERNAL key; do NOT add it to the emitted `row_source` (the output of a pair keeps exactly `bucket` and `prefix`).
2. **A source `table` field.** A `store` or `integration` source MAY also carry a `table` string (the table or route the named store resolves to by default; the news store sources are env-var names such as `NEWS_KEYWORD_TABLE`, which can never equal a table name). Rule (i) compares the row's `table` with the source's `store`/`integration` name AND, when present, with the source's `table`, each normalised the same way (lower-case, `_` as `-`); either equal routes the pair. A source with no `table` is graded on its name alone. Nothing requires the field; the issuer adds it to the source sets at the drain.
3. **Rule (iii) is an overlap, like the exact rule.** After replacing `_` by `-` in both prefixes, the two prefixes route when one starts with the other (the same overlap the existing rule uses), not only when they are equal. Rule (ii) compares path segments: split both prefixes on `/`, ignore trailing empty segments, and over the length of the shorter list each row segment that is a `<...>` template matches any ONE non-empty source segment and every other row segment equals the source segment (with `-` and `_` equal); a source prefix shorter than the row prefix therefore overlaps it, and a wildcard never spans two segments.
4. **The link plant.** `--plant link` appends to the tool one catalog row from a bucket the tool's `s3` sources do not read. With the new rules a candidate row can be one the new matching routes for that tool (a store row named for the tool's own store). The planted row must never be one the tool's sources route: skip such a candidate and take the next, so the planted defect is still read back as MISROUTED `link` (the issuer's check plants on a store tool).

### Inputs you read (you do NOT edit them)

- The merged script `workflows/gateway_battery/routing_table.py` and its tests `workflows/gateway_battery/tests/test_routing_table.py` and `test_routing_serves.py` (the model for a test file: scripts are run by path as subprocesses on small inputs written inside the test with `tmp_path`).
- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round25/fixtures/y4_census.json`, `y4_catalog.yaml` and `y4_sources.json` (the fixture of criterion AC1: 16 tools over 9 catalog rows) and `y4_r1_base_table.json`, `y4_r1_base_serves.json` (the base outputs on the round-23 r1 fixtures, which AC2 compares byte for byte).
- For criterion AC2 the real inputs it runs on: the prospective census `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round24/evidence/census_prospective_20261020.json`, the catalog `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml` (md5 `2bfc456e20600cdfacb6c7a6070961fb`), the six source-set files `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~71/source_sets_assets.json` through `~76/source_sets_m365.json`, and the committed round-24 outputs `round24/evidence/ROUTING_TABLE_20261020b.json` and `GATEWAY_SERVES_20261020b.json`.

### Steps

0. From the worktree root, `git rev-parse --show-toplevel` is your root. Do the sparse step above first.
1. Read `routing_table.py` (`catalog_info`, `s3_matches`, `grade_pairs`, `apply_plant`, `prefix_overlap`) and `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round25/checks/y4_check.py` (the executable form of this section; read what each arm grades). Make the changes, then the test file: at least 6 tests of your own, on small catalogs and source sets you write inside the test (not the issuer's fixtures; those are the criteria's). They cover at least: a store row routed by an exact store name, by `_` for `-` and by a source `table` field; a store-word row on an `s3`-only tool staying MISROUTED; a `<firm>` template routing one segment and refusing a wildcard that would span two; twin prefixes routing in the same bucket and not in another; and the `row_source` keys staying `bucket` and `prefix`.
2. Run the three criteria in section 4 until each prints `RESULT: PASS`.

## 2. BOUNDS

1. You change only the files in `<paths>`. Do NOT edit the issuer's fixtures, checks or decomposition, `members.yaml`, `pending_members.yaml`, the catalog or its row files, the source-set files, the emitter (`emit_catalog_v02.py`), any file under `infra/`, the PRD, the round-23 or round-24 evidence, or any other file under `workflows/`. No AWS call, no network call, no grant, no deploy, no push. The criteria write their outputs under a temporary directory.
2. Python 3.9, standard library plus `yaml` (PyYAML, installed) only. ASCII only in code, comments, strings, output and data files. No type syntax newer than 3.9 (no `X | Y` annotations, no `match`). The commit gate runs `py_compile`, the naming gate and `ruff` for py39.
3. No tool name, channel id, firm or vendor is typed as a whole-string literal in the script; the three store words and the template pattern are the contract's fixed words and may be constants. Tests under `tests/` and data files are exempt.
4. The contract and the four clarifications in section 1 are the whole specification. Where they are silent, do the smallest thing and say which in your report; do not widen the output (no new key in the routing table or the serves, no new option).
5. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project: your proof instance is one (commit it with, or before, the last code commit).
6. The checks are `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round25/checks/y4.AC1.sh`, `.AC2.sh` and `.AC3.sh` (they run `y4_check.py` in the same folder). Do not edit any of them. If a criterion cannot be met as written, REFUSE it and report the arm text and your measurement (the issuer settles the contract).
7. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
workflows/gateway_battery/routing_table.py
workflows/gateway_battery/tests/test_routing_links.py
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~87/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-y-4.link-rule-nons3.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W87-S<k>` (`k` the next unused number of your slot);
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp (`date -u +%FT%TZ` at filing).

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 2)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-y-4" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round25/checks/y4.AC1.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line; on the 16-tool fixture the store and integration pairs named for their table, the templated prefixes and the twin prefixes are ROUTED and the planted negatives stay MISROUTED link; the ROUTING line reads routed_pairs=9 link=7; row_source keeps its two keys; two runs give the same bytes; the three --plant modes on a store tool fire -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-y-4" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round25/checks/y4.AC2.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line; the r1 fixture table and serves are byte-identical to the base outputs and the three r1 plants fire; on the live round-24 inputs the ROUTING line reads link=4 and routed_pairs=196 and only the three expected tools and four expected pairs differ from the committed table; the live serves are byte-identical; with a table field on the three news store sources the line reads link=1 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-y-4" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round25/checks/y4.AC3.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line (pytest rc=0, at least 6 passed) for `test_routing_links.py` -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~87/NFRA_MCPINDEX.TO-MX-y-4.link-rule-nons3.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance. In its artifact rows, pin each produced file to the commit that carried it (the checker refuses `PENDING-THIS-COMMIT` for a file committed before the instance): commit the work first, then write the instance naming those commit hashes.
2. Append `<status>complete</status>` to this order file only if every criterion PASSes (if the commit gate refuses the flip, leave it and say so).
3. Commit through `.tools/safe-commit.sh` in two commits: (i) the work; (ii) the proof instance and the status flip.
4. Report once, with: what you built by part; every `RESULT:` line and `DENOMINATOR:` line of each criterion verbatim; the before/after diff of the live table (which tools and pairs flipped); the unit-test count; your commit shas; every place the contract was silent and what you did.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 25, workstream GATEWAY, worker ~87. Source: the CTO's round-24 analysis (`1.0.0_SA_CTO~Z`, 2026-10-20 ~15:4xZ, msg 36225) item 6 and PRD v0.19 @7c42c0c743. Decomposition `org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round25-GATEWAY.md` (contract R25.3 Y4, frozen at the cut). Base dry-runs 2026-10-20: `y4.AC1` FAIL (7 of 13 arms ok: the controls, the negatives, row_source, determinism and the link/code plants pass; every ROUTED arm of the three rules and the display plant fail), `y4.AC2` FAIL (9 of 14 ok: the r1 bytes, the r1 plants, the input checks and the serves-untouched arm PASS at the base as regression arms; the four live-delta arms and the corrected-sources arm FAIL), `y4.AC3` FAIL (test file absent). The issuer's scratch reference (about 45 added lines in `routing_table.py` plus six tests, outside the repository) passes all three; three mutants of it (no plant filter, a wildcard that spans segments, the serves rule switched to the new matching) each fail the arm built for them. **What the contract does on the live inputs, and what is deliberately left for the drain:** rules (ii) and (iii) route `harvest_get_research` (two twin-prefix pairs) and `mdpf_get_model_composition` (the `<firm>` row); rule (i) routes `mdpf_get_security_classification` (source `etf-classifications` equals the row table) but NOT the three news tools, whose store sources are env-var names, nor the published-analysis row, whose catalog row still carries bucket `opal-data-harvest` until cell MX-y-3 lands: live link 7 becomes 4. Clarification 2 (the optional source `table`) lets the issuer add the tables to the news source sets at the drain (link 4 becomes 1), and the published-analysis pair follows MX-y-3's re-bucketed row. Gate limb that graded this order: the L6 gate at the issuance commit.

<status>issued</status>
<round>25</round>
<workstream>GATEWAY</workstream>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
