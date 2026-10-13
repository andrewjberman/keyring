# NFRA_MCPINDEX task order -- `MX-c-8` -- the catalog's one writer adds a tool index over every tool the DEPLOYED gateway serves (each tool's member, index, history depth and freshness) and one row per servable harvest prefix, and discover reaches the harvest rows

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-c-8</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-c-8</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~33</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- catalog source files, the emitter, the regenerated catalog and discover only; no role, grant or tool change. The S3 listings for depth and freshness are read-only and run under the seat's own credentials.
comp-adversary: DECLARED-NOT-APPLICABLE -- the MX-c-7 pattern; the battery dry-run plus planted PASS and FAIL arms are the control (decomposition R10.3).
EGRESS CLASS, declared: NONE beyond Opal's own AWS (read-only S3 listings).
</preflight>

## 1. THE CELL -- `MX-c-8` (round 10; PRD v0.9 @e581c26ab4 FWD-20, FWD-21; decomposition section ROUND 10)

Work in your own worktree, cut from `box/sitez`. Every path below is relative to its root. The gateway is
`infra/aws/ec2/opal-gateway/`. The one catalog file is `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml`, and it is
written ONLY by `workflows/atom_decomposition/emit_catalog_v02.py` (never by hand).

**What the user sees at the base.**
- MC Portal's gateway breakdown finds a catalog index for 10 of the gateway's 67 served tools. No tool shows how far
  back its data goes or how fresh it is.
- `opal_discover` answers `catalogued: false` for "harvested news articles and chatter" and for "security analysis
  research pack". The catalog has no row for the `opal-data-harvest` bucket.

### Part 1 -- FWD-20: a `tool_index:` section, one entry per SERVED tool

**The denominator.** The served tools are the tools defined by the gateway code at the DEPLOYED commit, never the
trunk and never a hand-kept list:
- the deployed commit is `services.opal-gateway.deployed_commit` in `infra/aws/ec2/EC2_MANIFEST.json`
  (185dc04888 at issuance; read it again when you start);
- the set is that commit's native tools (`app/tools.py`'s tool manager) plus the tools of each integration in that
  commit's `ENABLED_INTEGRATIONS="..."` line in `deploy-to-ec2.sh`;
- measured at issuance: N = 67 (43 native + 24 from 7 integrations).

Write a census script `workflows/atom_decomposition/tool_census.py`:
- it extracts the deployed commit's `infra/aws/ec2/opal-gateway/app` with `git archive`;
- it imports `app.tools`, calls `integrations.register_enabled(mcp, <enabled ids>)`, and lists
  `mcp._tool_manager.list_tools()`;
- for each tool it records the definition `<path relative to the gateway dir>:<line>`, using `inspect` on the tool's
  function.

**One entry per served tool.** Each entry has `tool`, `definition` and `member`. Classify the member from what the
DEFINITION does, never from the tool's name:

| member | when | carries |
|---|---|---|
| `a` | it reads data that a catalog row describes | `read_tool: <the tool>`. `entity: <the id of that catalog row>`: an `entity` or `key` of a row OUTSIDE `tool_index`, picked from the rows that already name it (`read_tool`), or from the owning integration's `catalog_ref_for_tool`. `links:` lists every such row id. `history_depth` and `freshness` (below) |
| `b` | it reads data, and no catalog row describes it yet | `owner`: the project code that owns that data, or `unowned`. No `read_tool` |
| `c` | it is not a data read (it sends, writes, uploads or administers) | `reason`, one line naming what the definition does. No `read_tool` |

**`history_depth` and `freshness` on an (a) entry.** Each is a mapping:
- `claim`: `measured`, `inferred` or `absent`;
- `measured` and `inferred` carry `value` (`YYYY-MM-DD`), `basis: s3://<bucket>/<prefix>`, `method` (`key-date`: the
  date in each key; `last-modified`: the object's LastModified, UTC) and `read_at` (a full UTC timestamp);
- `absent` carries `reason`. Example: a live-queried silver row has no served artifact to list.

How to read them:
- depth = the earliest date under the index's served prefix; freshness = the latest date;
- read them with a read-only, auto-paginated S3 listing, counted client-side;
- both mappings use the SAME `basis` and `method`;
- never write a blank; say `absent` and why.

The tool_index source lives under `workflows/atom_decomposition/`, and the emitter writes it into the catalog.
discover's answer-time freshness (FWD-13) is unchanged.

### Part 2 -- FWD-21: a `harvest_datasets:` section, one row per SERVE-NOW prefix

The list is `org/tier1_exec/1.0.0_SA_CTO/deliverables/SERVABLE_PREFIXES_OPAL_DATA_HARVEST_20261013.md` AT ITS PIN
@0b2778751a. Read it with `git show 0b2778751a:<path>`, never the moving file. Its SERVE-NOW prefixes, 16 in all:
- `packs/`, `scores/v1/`, `filings/v1/`, `posture/v1/`, `peers/v1/`, `publication-links/v1/`;
- `identity/v1/`, `crosswalk/v1/`, `universe/v1/`, `derived/`;
- six gold tables: `amgt/harvest/gold/article_security_mention/`, `.../article_sentiment/`, `.../chatter_daily/`,
  `.../chatter_event/`, `.../chatter_window/`, `.../candidate_universe/`.

**Rows you never write.** No row for:
- a WITHHOLD prefix;
- `management/v1/` (it waits for its view);
- the whole `amgt/harvest/gold/` prefix;
- any prefix not on the list.

**Where rows come from.** Write one source file per prefix, `workflows/atom_decomposition/catalog_entries/harvest_<slug>.yaml`,
and extend the emitter to load that family and emit `harvest_datasets:`. Each row carries:
- `entity` (`harvest_<slug>`), `bucket: opal-data-harvest`, `prefix` (exactly as listed);
- `business_meaning` and `example_questions`, from the list's own content column (derived layers only);
- `grain`, `freshness_field`, `firm_scope_rule: opal-internal-only`, `never_sum_rules` and `producer`, using the C1
  vocabulary in `catalog_entries/README.md`;
- `read_tool` and `gap_owner`.

**The reader.** Use an existing catalog read tool first (build ladder step 2). At issuance no gateway tool reads this
bucket:
- `comp-find 'opal-data-harvest' infra/aws/ec2/opal-gateway`: 0 hits across 261 files;
- `gateway_query_catalog` reads only the catalog's one `bucket`.

Re-check both. If no tool reads the bucket, write `read_tool: null` and `gap_owner: NFRA_OPLGTW`. That project's next
round owns the asset-manager principals, the research grant and its reader.

**Example questions.** Write the asker's own words into `example_questions`, so discover's own-text rule reaches the rows:
- the chatter and article tables: "harvested news articles and chatter";
- `packs/`: "security analysis research pack".

### Part 3 -- discover reaches `harvest_datasets`

In `infra/aws/ec2/opal-gateway/app/integrations/opal_discover/integration.py`, reach `harvest_datasets` rows through
their own text, the same way `silver_datasets` rows are reached.

Each answer has:
- `channel: "harvest_datasets"`, the row's `entity` as `dataset`, and its `prefix` and `bucket`;
- `next_tool`: null when `read_tool` is null;
- a `gap` naming `gap_owner`;
- the row shown to the Opal-internal principal only (FAIL CLOSED for any firm principal, as silver rows are).

Add tests in `tests/test_opal_discover.py`. Keep these passing:
- `test_own_text_rule_does_not_catalogue_chatter`: "How's it going?" and "fees" stay uncatalogued;
- the Schwab control: "Schwab account positions" keeps its three `schwab_dim_*` silver datasets, with no harvest match.

**AMENDED A1 (2.0.0_SA_COO~MI, 2026-10-13 ~23:2xZ) -- RE-OPENED: re-derive the two `definition:` values the release
moved (row Z-S110, ruled by Z-S112).**
- **What is wrong.** Live on the host, and offline at `box/sitez` HEAD, c8.AC1 reads `definitions located 65 of 67`. The
  manifest now names the released `ad2acc0a93`. The two misses are `opal_describe` and `opal_discover`. Both are defined
  in `app/integrations/opal_discover/integration.py`, which this cell changed by +57 lines; their entries still cite the
  PRE-change lines.
- **The issuer's defect.** c8.AC1 graded definitions against the pre-release tree (`185dc04888`), so it could not see
  the cell's own shift. It now reads the released tree and FAILS as it must.
- **The act.**
  1. Merge `box/sitez` into your branch.
  2. Re-run `workflows/atom_decomposition/tool_census.py` against the deployed commit the manifest names (`ad2acc0a93`).
  3. Re-emit `DATA_CATALOG.yaml` through the one emitter.
  4. The regenerated catalog must differ from `ad2acc0a93`'s ONLY in the two `definition:` values (and the built-by
     stamp, if the emitter writes one). Print the diff.
  5. Change nothing else: no member, link, claim, harvest row or discover code.
- **The census reads the tree AS SHIPPED** (Z-S112 lesson). If `tool_census.py` reads only a base commit, also give it
  a way to overlay the cell's own changed gateway files, so a future cell that edits a definition file is graded on
  its shipped lines. One mechanism is enough, in the same paths.
- **Criteria:** AC1-AC3 unchanged and re-run. AC1 must read `definitions located 67 of 67`.
- **`<paths>`** are unchanged; your deliverables go under `deliverables/0.9.0_WK_NFRA_MCPINDEX~33/` with an `a1_` prefix.
- Then MX-r-11 A5 ships the regenerated catalog alone, as v2.
- Gate limb that graded this modification: none. LIMB 6 does not fire on a modification, and `<placeholders>NONE`, so
  GATE (viii) does not grade it.

## 2. BOUNDS

1. You change only the files in `<paths>`. The catalog is regenerated by the emitter. Print the regenerated
   catalog's diff summary by top-level section in your report.
2. No tool, grant, route, role or `.env` change, and no new AWS resource name. No deploy (that is MX-r-11). No push.
3. Grade the gateway suite by failing-ID DELTA against the MX-x-6 baseline (`suite_delta.py`), never by count. A NEW
   failing ID is yours to fix. One of the five known round-close failures (row Z-S97) is listed, never fixed here.
4. Never print an S3 object's content. Listings record keys, dates and counts only.
5. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
workflows/atom_decomposition/tool_census.py
workflows/atom_decomposition/emit_catalog_v02.py
workflows/atom_decomposition/validate_catalog_v02.py
workflows/atom_decomposition/catalog_entries/
workflows/atom_decomposition/tool_index/
workflows/atom_decomposition/tests/
infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml
infra/aws/ec2/opal-gateway/app/integrations/opal_discover/integration.py
infra/aws/ec2/opal-gateway/tests/test_opal_discover.py
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~33/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W33-S<k>`; re-read the file for the next free k at commit time;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp, never a placeholder.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-c-8" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round10/checks/c8.AC1.sh; echo "exit=$?"</invocation><expect>PARTITION a+b+c sum N of N=N with every member valid, a>0, depth and freshness claims on every a, definitions located N of N, duplicate entries 0, unserved 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-c-8" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round10/checks/c8.AC2.sh; echo "exit=$?"</invocation><expect>LIST SERVE-NOW rows 11, prefixes 16, parse agrees True; SERVE prefixes rowed 16 of 16; rows on a prefix not SERVE-NOW 0; whole gold prefix 0; duplicates 0; rows with neither read_tool nor gap_owner 0; rows not on opal-data-harvest 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-c-8" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round10/checks/c8.AC3.sh; echo "exit=$?"</invocation><expect>discover reads good 3 of 3 (both harvest subjects catalogued with harvest_datasets matches; Schwab control 3 of 3 silver, harvest 0) -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~33/NFRA_MCPINDEX.TO-MX-c-8.tool-index-and-harvest-rows.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance at the `<instance_path>`.
2. Flip `<status>` to complete, and commit the instance, the deliverables and the flip together.
3. Report once, with:
   - N and the three member counts;
   - the (c) members, each with its definition line;
   - the (a) tools whose depth or freshness reads `absent`, with the reason;
   - the 16 harvest rows, each with its `read_tool` or `gap_owner`;
   - the three discover answers;
   - the catalog diff summary;
   - the suite delta.

After this order, the issuer continues you with MX-r-11's PHASE A.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 10, chain head, worker ~33. Source: `ledger/CTO_RULING_ROUND10_Z4_ONE_SHORT_ROUND_20261013.md`
(msg 33704) on PRD v0.9 @e581c26ab4, ADMITTED (msg 33712). FWD-20 is the CVO's cure: a three-member partition summing to N.
Battery dry-run at base 08b77fd98d (`round10/checks/`):
- c8.AC1 FAIL as expected: partition sum 0 of N=67.
- c8.AC2 FAIL as expected: 0 of 16 rowed. The list parse agrees with its grant section (11 rows, 16 prefixes).
- c8.AC3 FAIL as expected: 1 of 3; the Schwab control holds.
- The planted PASS arms and planted FAIL arms of all three instruments: decomposition R10.3.

<status>issued</status>
<status>complete</status>
<status>issued</status>
<status>complete</status>
<round>10</round>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
