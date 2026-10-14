# NFRA_MCPINDEX task order -- `MX-c-10` -- the catalog's one writer gives EVERY indexed tool a correct history-depth claim under v0.10's cases (graded per tool), discover answers each measured depth at answer time, and each research table is reached by its own questions

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-c-10</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-c-10</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~35</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- catalog sources, the emitter, the regenerated catalog and discover only; read-only S3 reads of ONE named date field per object, and read-only partition listings for served windows.
comp-adversary: DECLARED-NOT-APPLICABLE -- the battery dry-run plus planted PASS and FAIL arms on live S3 are the control (decomposition R12.1).
EGRESS CLASS, declared: NONE beyond Opal's own AWS (read-only S3).
</preflight>

## 1. THE CELL -- `MX-c-10` (round 12; PRD v0.10 item 2; `ledger/ROUND_ANALYSIS.round11.md` rulings 1 and 2)

Work in your own worktree, cut from `box/sitez`. Every path below is relative to its root. The one catalog file is
`infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml`, written ONLY by `workflows/atom_decomposition/emit_catalog_v02.py`.

**What the user sees at the base.** The gateway serves `43088464f5`. Of the 11 member-(a) tool_index entries, only
`mdpf_get_aggregate_aua` reads depth `measured` (2024-11-01, answered at answer time). The other 10 read `absent`. But
their artifacts carry dates: aum-metrics carries `total.series_start` 2024-11-01, and etfs positioning carries
`data_as_of` 2026-10-09 (the CVO's read).
- "security analysis research dossier" reaches `harvest_packs`, not a research dossier table.

### Part 1 -- depth for EVERY (a) tool (ruling 1)

For each of the 11 (a) entries, set `history_depth` by v0.10's cases:

| case | claim | carries |
|---|---|---|
| the served object carries a first-date field, or a dated series whose first element is a date | `measured` | `value`, `basis: s3://<bucket>/`, `row`, `scope` (when the row key holds `{scope}`; `global` where it exists), `field` (dotted path), `method: body-field` or `series-first` |
| the served object is a snapshot with an as-of date | `measured` | the same, `method: snapshot-asof` |
| a live-queried row (silver, vendor API) whose served window can be read from its partition listing | `inferred` | `value` (the window, e.g. `2026-09-14..2026-10-13`), `basis` (the bucket/prefix the listing read), `source` (how) |
| no served artifact carries any date | `absent` | `reason`, and `row` naming the artifact checked |

- **A multi-index query tool** (`gateway_query_catalog`, `opal_asker_query`) takes `history_depth: {claim: per-link,
  links: [...]}`. There is one element per row it links, each graded by the same cases.
- **Reading object bodies is allowed** for ONE named date field per object. Print and store only the date.
- **Answer time.** In `infra/aws/ec2/opal-gateway/app/integrations/opal_discover/integration.py`, every row with a
  measured depth answers `history_depth` at answer time from the served object, through the existing bounded get, with
  its claim. That is the AUA mechanism, generalised from `as_of_first` to the entry's own `field`. A read that fails says
  `absent` with a reason.

### Part 2 -- per-table routing for the research tables (ruling 2)

Each of the seven `harvest_datasets` rows under `amgt/harvest/gold/research*` gets `example_questions` written in the
words an asker would use, so that each question reaches THAT table FIRST among harvest matches.
- "security analysis research dossier" must reach `harvest_research-dossier` or `harvest_research_dossier` FIRST.
- "research sector template passages" must reach `harvest_research-sector-template` FIRST.
- If the own-text rule cannot separate two tables (the two dossier tables), say so in a row. Never add a word-specific
  mapping in discover.

## 2. BOUNDS

1. You change only the files in `<paths>`. Print the catalog diff summary by section.
2. No tool, grant, route, role or `.env` change, and no new AWS resource name. No deploy (that is MX-r-13). No push.
3. Grade the gateway suite by failing-ID DELTA (`suite_delta.py`). The known failures (rows Z-S97, Z-S107) are listed,
   never fixed here. At the drain, the issuer re-baselines (Z-S107).
4. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project
   (row Z-W34-S8).
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
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~35/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W35-S<k>`;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-c-10" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round12/checks/c10.AC1.sh; echo "exit=$?"</invocation><expect>DEPTH (a) tools graded N of N; valid N of N (every measured AGREES with the aws CLI; no absent on a dated or unresolvable artifact) -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-c-10" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round12/checks/c10.AC2.sh; echo "exit=$?"</invocation><expect>ROUTING research rows 7; rows reached by every own question 7 of 7; anchors 2 of 2 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-c-10" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round12/checks/c10.AC3.sh; echo "exit=$?"</invocation><expect>ANSWER-TIME measured rows m; answered measured and equal m of m; anchors measured 2 of 2 -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~35/NFRA_MCPINDEX.TO-MX-c-10.depth-every-tool-research-routing.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance.
2. APPEND `<status>complete</status>`.
3. Commit everything together.
4. Report once, with:
   - the per-tool depth table (tool, claim, value, field or basis);
   - the answer-time lines;
   - the routing lines;
   - the catalog diff summary;
   - the suite delta;
   - your commit sha.

The issuer then cuts MX-r-13.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 12, chain head, worker ~35. Source: `ledger/ROUND_ANALYSIS.round11.md`
@05caf1144b (msg 33989), with PRD v0.10 unchanged. Standing battery clause 3 (grade every member) applies. Battery at the
base and the planted arms: decomposition R12.1.

<status>issued</status>
<round>12</round>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>complete</status>
