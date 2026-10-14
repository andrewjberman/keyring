# NFRA_MCPINDEX task order -- `MX-c-9` -- the catalog's one writer re-reads each indexed tool's history depth from its served artifact (and discover answers it at answer time), makes the tool_index link key durable, and adds harvest rows for every prefix list v4 serves

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-c-9</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-c-9</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~34</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- catalog sources, the emitter, the regenerated catalog, discover and one token of MC Portal's breakdown reader; no role, grant or tool change. S3 reads are read-only, one named date field per object, under the seat's own credentials.
comp-adversary: DECLARED-NOT-APPLICABLE -- the MX-c-8 pattern; the battery dry-run plus planted PASS and FAIL arms are the control (decomposition R11.3).
EGRESS CLASS, declared: NONE beyond Opal's own AWS (read-only S3).
</preflight>

## 1. THE CELL -- `MX-c-9` (round 11; PRD v0.10 @301af339c7 FWD-20 item 2, FWD-21 item 1; decomposition section ROUND 11)

Work in your own worktree, cut from `box/sitez`. Every path below is relative to its root. The gateway is
`infra/aws/ec2/opal-gateway/`. The one catalog file is `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml`, written
ONLY by `workflows/atom_decomposition/emit_catalog_v02.py`.

**What the user sees at the base.**
- The deployed gateway (`7eff14b2e6`) indexes all 67 served tools. Every one of the 11 tools that names an index reads
  history depth `absent`, yet the AUA timeseries object carries `as_of_first` = 2024-11-01 (row Z-W33-S1).
- discover answers freshness for a portal row and never its depth.
- The 11 indexed entries repeat their index row's `entity`, so one id appears twice in the file (row Z-S106).
- The catalog rows 11 of list v4's 24 top-level harvest prefixes.

### Part 1 -- FWD-20 depth, read from the served artifact (PRD v0.10 item 2)

For each member-(a) tool_index entry, set `history_depth` from what its index row's SERVED artifact carries:
- **`measured`:** the object carries a first-date field (e.g. `as_of_first`) or a dated series whose first element is a
  date. Carry:
  - `value` (`YYYY-MM-DD`);
  - `basis: s3://<bucket>/`;
  - `row` (the index row's `entity`);
  - `scope` (one real scope when the row key holds `{scope}`; `global` where it exists);
  - `field` (the dotted path you read; a list's first element is taken);
  - `method: body-field`;
  - `read_at` (a full UTC timestamp).
- **`inferred`:** a live-queried row (silver, vendor API) whose served window is known but not read. Carry the window as
  `value` and its source as `basis`.
- **`absent`:** only where no served artifact carries any date. Carry `reason`.

`mdpf_get_aggregate_aua` must read `measured`.

**Body reads are now ALLOWED for ONE named date field per object** (this supersedes MX-c-8's bound 4). Read the field;
print and store only the date. Never print, store or copy any other value of any object.

**Answer time.** In `infra/aws/ec2/opal-gateway/app/integrations/opal_discover/integration.py`, a match on a row whose
(a) entry carries a measured depth answers `history_depth` at ANSWER TIME:
- read from the served artifact through discover's existing bounded get;
- the same rule as `freshness.latest_value` (FWD-13);
- with its claim, and `absent` with a reason when the read fails.

The proof question is the AUA row's own example, "What is the AUA trend over time for a firm?". Its
`mp.03.aggregate-aua-timeseries` match must carry `history_depth` `measured` 2024-11-01 for the `global` scope.

### Part 2 -- the durable link key (row Z-S106)

- An (a) entry carries `read_tool: <tool>` and `index: <index row id>`, and NO `entity` and NO `key`. Its identity is
  `tool`. Every other member carries neither.
- MC Portal's breakdown reader must still resolve each (a) tool to its index. In
  `infra/aws/ec2/opal-gateway/app/admin_gateway_breakdown.py:109`, change ONLY
  `rid = node.get("entity") or node.get("key")` to `rid = node.get("entity") or node.get("key") or node.get("index")`.
  This is NFRA_MCPORTAL's file: that one token and nothing else.
- Keep `tests/test_admin_gateway_breakdown.py` passing, and add one test that an `index`-carrying mapping is read.

### Part 3 -- FWD-21 on list v4 (PRD v0.10 item 1, row Z-S105)

The list is `org/tier1_exec/1.0.0_SA_CTO/deliverables/SERVABLE_PREFIXES_OPAL_DATA_HARVEST_20261013.md` AT ITS v4 PIN
@7e0da2dfee (`git show 7e0da2dfee:<path>`). All 24 top-level prefixes SERVE to Opal principals.

**Coverage.** Every one of them is covered by at least one `harvest_datasets` row whose `prefix` starts with it. The 13
not covered at base are:
- `barrons/`, `bloomberg/`, `drafting/`, `ft/`, `issuer-site/`, `lib/`, `management/`;
- `publications/`, `raw/`, `sec/`, `seeking-alpha/`, `social/`, `wsj/`.

**Row 12b.** Its seven `amgt/harvest/gold/` research tables each get a row: `research-backlog`, `research-continuation`,
`research-dossier`, `research_dossier`, `research-fund-form`, `research-model-typecast`, `research-sector-template`.

**Constraints:**
- Keep the 16 round-10 rows.
- No row on the whole `amgt/harvest/gold/` prefix, and no duplicate prefix.
- `firm_scope_rule: opal-internal-only` on every row.
- Each row's `business_meaning` and `example_questions` come from the list's own content column.

**The reader.**
- If the deployed commit at your census serves a tool that reads `opal-data-harvest`, every row names it as
  `read_tool`. NFRA_OPLGTW's `harvest_read`/`harvest_list` are in trunk at issuance, not deployed.
- Otherwise every row keeps `read_tool: null` and `gap_owner: NFRA_OPLGTW`.

Use the source family and emitter from round 10 (`catalog_entries/harvest_<slug>.yaml`).

**Census.** Run `workflows/atom_decomposition/tool_census.py` against the deployed commit the manifest names, with
`--overlay-ref` on your own branch for the files you change (the Z-S112 lesson).

**AMENDED A1 (2.0.0_SA_COO~MI, 2026-10-14 ~01:1xZ) -- H1's denominator lists `amgt/`'s sub-prefixes explicitly (the
CVO's carried note, CTO msg 33847).**
- Besides the seven research tables, give EACH of these its own row: `amgt/harvest/bronze/`, `amgt/harvest/silver/`,
  `amgt/harvest/state/` (list rows 12 and 13; v4 serves them inside `amgt/`).
- c9.AC2 now also reads `amgt bronze/silver/state rowed 3 of 3`. The amended `round11/checks/c11_harvest.py` is on
  `box/sitez`; merge `box/sitez` into your branch before you run AC2.
- Gate limb that graded this modification: none. LIMB 6 does not fire on a modification, and `<placeholders>NONE`, so
  GATE (viii) does not grade it.

**AMENDED A2 (2.0.0_SA_COO~MI, 2026-10-14 ~02:0xZ, at the drain @435958cd7c) -- AC2 re-cut for six rows HELD on the
naming gate (row Z-W34-S6, ruled by the row that follows it).**
- The commit-time naming gate (LGIC ENFORCE) refuses six existing hyphenated research-table prefixes as new
  out-of-pattern S3 key literals: `amgt/harvest/gold/research-backlog/`, `-continuation/`, `-dossier/`, `-fund-form/`,
  `-model-typecast/` and `-sector-template/`. A departure from the naming canon is an R20 register entry Andrew
  acknowledges (CLAUDE.md rule 30), so the issuer does not waive it.
  - It is queued as call `sitez-20261014T015958Z-a63a`, REC yes.
- **AC2 now counts a research table as HELD** when its written row file exists under
  `deliverables/0.9.0_WK_NFRA_MCPINDEX~34/blocked_harvest_rows/` and names that exact prefix. Rowed + held must equal 7.
  - Issuer's run at the merged index: top-level 24 of 24, research rowed 1 + held 6 of 7, amgt bronze/silver/state 3 of
    3, gold 6 of 6, RESULT: PASS.
  - FAIL arm: one held file removed gives 1 + 5, rc=1.
- **On the call's YES, the six rows land as ONE act** (row Z-W34-S6 notes): copy the six files into `catalog_entries/`,
  empty `HARVEST_NAMING_PENDING`, re-emit, and set the test counts to 39. It ships in the next gateway release. The
  project's un-park condition (d) is that YES.
- AC1 and AC3 are unchanged, and PASS at the merged index (partition 67 of 67, identity 0; AUA depth 2024-11-01 measured
  and answered at answer time).
- Gate limb that graded this modification: none. LIMB 6 does not fire on a modification, and `<placeholders>NONE`, so
  GATE (viii) does not grade it.

**AMENDED A3 (2.0.0_SA_COO~MI, 2026-10-14 ~02:2xZ) -- RE-OPENED: call a63a RULED NOT an R20 (`1.0.0_SA_CTO~Z`
@d5e0b1a0b6, `ledger/CTO_RULING_A63A_LEGACY_ADDRESS_ROWS_NOT_R20_20261014.md`). The six rows land NOW through
`legacy_addresses.json`. This supersedes A2's HELD allowance.**
- Add six rows to `infra/logic/registry/legacy_addresses.json`, one per hyphenated table (`research-backlog`,
  `research-continuation`, `research-dossier`, `research-fund-form`, `research-model-typecast`,
  `research-sector-template`). Use the closed field set `key, bucket, template, shape, params, reader, evidence, note`:
  - `bucket: opal-data-harvest`;
  - `template: amgt/harvest/gold/<table>/`;
  - `shape: prefix`;
  - `params: []`;
  - `reader: NFRA_MCPINDEX`;
  - `key`: a lowercase kebab key per table;
  - `evidence`: the read-only `list-objects-v2 --prefix` read that shows the prefix exists (a count, no content);
  - `note`: "AMGT_HARVST owns any rename (R19)".
  Follow the ADVI_COTBKF precedent rows already in the file.
- The catalog names each of the six keys THROUGH `lib/opal_naming.py legacy_address()`: the emitter resolves the
  prefix from the row. Never type the literal. Then:
  1. copy the six held files from `deliverables/0.9.0_WK_NFRA_MCPINDEX~34/blocked_harvest_rows/` into
     `catalog_entries/`;
  2. empty `HARVEST_NAMING_PENDING`;
  3. re-emit with the same overlay;
  4. set the test counts to 39.
- If the validator refuses `bucket` because `opal-data-harvest` is not a bucket `scopes.json` knows, add that one
  registry row the same way (in `scopes.json` or `bucket.standing_shared`). Never use an R20 or an override.
- **c9.AC2 now requires** `python lib/opal_naming.py validate` exit 0 AND research tables rowed 7 of 7 (no held
  allowance). AC1 and AC3 are unchanged and are re-run.
- `<paths>` gain `infra/logic/registry/legacy_addresses.json` and `infra/logic/registry/scopes.json`.
- Gate limb that graded this modification: none. LIMB 6 does not fire on a modification, and `<placeholders>NONE`, so
  GATE (viii) does not grade it.

**AMENDED A4 (2.0.0_SA_COO~MI, 2026-10-14 ~02:5xZ) -- the naming gate honours a registered legacy address (row
Z-W34-S7; `1.0.0_SA_CTO~Z` ruling msg 33936; laptop CTO conditions msg 33943). LGIC_ENFORCE is CLOSED, so this
project lands the gate branch. It is folded into this order because round 11 has one issuer.**
- **Why.** `.tools/naming-gate.py` `judge()` never reads `infra/logic/registry/legacy_addresses.json`. So the six
  emitted `prefix:` values grade NEW OUT-OF-PATTERN, and A3's catalog commit is refused.
- **One branch in `judge()`.** A literal that EQUALS `lib/opal_naming.py legacy_address(key)` for a registry row whose
  `reader` is the COMMITTING PROJECT grades CONFORMANT. Any other literal grades exactly as before. The same literal
  under a row whose `reader` is ANOTHER project stays REFUSED.
- **The committing project is DERIVED mechanically, never a free field** (laptop CTO condition 1). Derive it from the
  staged paths' project home (`org/missions/D*/<MACRO>/<CODE>/...`), or from the staged task order's project. In
  `--diff` mode, the diff's own file headers are the staged paths. No staged path under a project home means no
  committing project, so the branch does not apply. Never decide from the commit message.
- **Commit order: gate + registry rows FIRST, catalog SECOND.**
  1. Commit the gate branch together with the six `legacy_addresses.json` rows already in your tree. The gate reads its
     carriers from committed HEAD, and a commit cannot grant itself a pass.
  2. Then commit A3's catalog, the source files and the tests; that commit must pass the real gate.
- **Self-test arms** (laptop CTO condition 2). Add `ARM legacy_address_own_reader CONFORMANT` and
  `ARM legacy_address_other_reader REFUSE` to `--self-test`. Every existing arm must still read as before (print the
  before and after arm lists).
- **c9.AC2 gains two limbs:**
  - `round11/checks/g1.AC1.sh` (self-test rc=0 with both arms);
  - `round11/checks/g1.AC2.sh` (an independent planted diff: under NFRA_MCPINDEX's home rc=0 with 0 refusals; under
    NFRA_OPLGTW's home rc=1 with at least 6 refusals).
- **`<paths>` gain `.tools/naming-gate.py`.**
- **MERGE HOLD:** the issuer does not drain before dell1's answer on the shared-gate change arrives, or until 03:40Z
  passes with none (CTO~Z msg 33943). At the drain, the gate commit and its test result go to `2.0.0_SA_COO~C`
  (NFRA_CTLPLN, the gate's owner) through `0.0.0_AB_MSTR~Z` (condition 3).
- Gate limb that graded this modification: `.tools/to-pipeline-gate.py` refused a NEW order for this cell (one issuer
  per round), so it is cut here as a modification. LIMB 6 does not fire on a modification, and `<placeholders>NONE`, so
  GATE (viii) does not grade it.

## 2. BOUNDS

1. You change only the files in `<paths>`. Print the regenerated catalog's diff summary by top-level section.
2. No tool, grant, route, role or `.env` change, and no new AWS resource name. No deploy (that is MX-r-12). No push.
3. Grade the gateway suite by failing-ID DELTA (`suite_delta.py`). The 12 known failures (rows Z-S97, Z-S107) are
   listed, never fixed here. A NEW failing ID is yours to fix.
4. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
workflows/atom_decomposition/tool_census.py
.tools/naming-gate.py
infra/logic/registry/legacy_addresses.json
infra/logic/registry/scopes.json
workflows/atom_decomposition/emit_catalog_v02.py
workflows/atom_decomposition/validate_catalog_v02.py
workflows/atom_decomposition/catalog_entries/
workflows/atom_decomposition/tool_index/
workflows/atom_decomposition/tests/
infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml
infra/aws/ec2/opal-gateway/app/integrations/opal_discover/integration.py
infra/aws/ec2/opal-gateway/app/admin_gateway_breakdown.py
infra/aws/ec2/opal-gateway/tests/test_opal_discover.py
infra/aws/ec2/opal-gateway/tests/test_admin_gateway_breakdown.py
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~34/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W34-S<k>`; re-read the file for the next free k at commit time;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-c-9" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round11/checks/c9.AC1.sh; echo "exit=$?"</invocation><expect>PARTITION sums N of N with every member valid (index named valid a of a through MC Portal's reader), definitions located N of N, duplicate entries 0, tool_index entries carrying a row identity 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-c-9" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round11/checks/c9.AC2.sh; echo "exit=$?"</invocation><expect>top-level prefixes covered 24 of 24; research tables rowed + held 7 of 7 (A2); round-10 gold tables kept 6 of 6; amgt bronze/silver/state rowed 3 of 3; whole gold prefix 0; duplicates 0; rows outside the 24 0; rows with neither read_tool nor gap_owner 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-c-9" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round11/checks/c9.AC3.sh; echo "exit=$?"</invocation><expect>PART1 depth claims valid a of a, measured >= 1, verified by the second instrument m of m, mdpf_get_aggregate_aua measured; PART2 the AUA answer carries an answer-time depth, claim measured, equal to part 1 -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~34/NFRA_MCPINDEX.TO-MX-c-9.depth-durable-key-v4-rows.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance at the `<instance_path>`.
2. Flip `<status>` to complete by APPENDING the tag after the last `<status>` line, and commit everything together.
3. Report once, with:
   - each (a) tool's depth claim and source;
   - the AUA answer-time depth;
   - the durable-key change and the MC Portal reader's result;
   - the new harvest rows, each with its `read_tool` or `gap_owner`;
   - the catalog diff summary;
   - the suite delta.

The issuer then continues you with MX-r-12's PHASE A.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 11, chain head, worker ~34. Source: `ledger/ROUND_ANALYSIS.round10.md`
@301af339c7 (msg 33843) on PRD v0.10, ADMITTED (msg 33847). Battery dry-run at the issuance base (`round11/checks/`):
- c9.AC1 FAIL (links 0 of 11, 11 identity entries);
- c9.AC2 FAIL (11 of 24, 0 of 7);
- c9.AC3 FAIL (measured 0; the AUA answer carries no depth).
- The planted PASS and FAIL arms are in decomposition R11.3.

<status>issued</status>
<status>complete</status>
<status>issued</status>
<status>complete</status>
<round>11</round>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
