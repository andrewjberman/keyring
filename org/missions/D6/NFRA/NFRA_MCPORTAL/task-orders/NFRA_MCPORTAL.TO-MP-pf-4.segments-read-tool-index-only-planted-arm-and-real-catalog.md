# NFRA_MCPORTAL task order -- `MP-pf-4` -- WORKSTREAM PF ROUND 3: the segment compute reads the tool_index block only, shown by a planted arm and by the real catalog

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-pf-4</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-pf-4</to_id>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~34</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- offline tests; no cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the tests plant their own catalog.
comp-adversary: DECLARED-NOT-APPLICABLE -- the negative arm of AC1 IS the adversary: an owning-firm `firm:` key on rows outside tool_index must never make a segment.
EGRESS CLASS, declared: none. Make no network call.
</preflight>

## 1. THE CELL -- `MP-pf-4` (workstream PF round 3, decomposition section PF3.1)

You work in the workspace worktree `C:/tmp/mp-pf-34`, branch `wk-NFRA_MCPORTAL-pf-34`. Commit with `.tools/safe-commit.sh --author "0.9.0_WK_NFRA_MCPORTAL~34 <0.9.0_WK_NFRA_MCPORTAL~34@opal.agent>" -F <msgfile> -- <paths>`
(the message file written with a non-shell writer). Never push. Make no network call.

**Why this cell exists.** The gateway's `/gateway` page breaks each `opal-data-assets` and `opal-data-bd` bucket into segments, one per (vendor, firm) pair. The pair of a tool is read from ONE place: the
`serves` list on that tool's row of the catalog's top-level `tool_index:` block (the catalog is `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml`; the readers are `_declared_source_groups` and `_segment_fields_for` in
`infra/aws/ec2/opal-gateway/app/admin_gateway_breakdown.py`). The same catalog also carries 273 mappings elsewhere (channel-artifact rows, silver rows, portal rows) with a `firm:` key whose value is an OWNING firm: the same key name,
a different meaning. A segment built from one of those is a wrong-object segment. The handler does not do that today; the tests below keep it from ever doing so.

Read first: `app/admin_gateway_breakdown.py` lines 97-201 (`_catalog_read_tool_rows` reads `read_tool` rows; the two readers above read only `tool_index`), and in `tests/test_admin_gateway_breakdown.py` the helpers
`_plant_catalog`, `_seg_row`, `_seg_catalog`, `_segments`, `_plant`, `_get`, `_chan` and the tests `test_assets_bucket_splits_into_vendor_firm_segments` and `test_missing_vendor_or_firm_reads_unresolved` (lines 449-460 and 666-735).

Build, two tests appended to `tests/test_admin_gateway_breakdown.py`, by these exact names (the file's own fixtures `app_mods`, `as_identity`, `world`; plant the catalog with `_plant_catalog`):
1. `test_channel_row_firm_key_never_makes_a_segment`: the planted catalog text holds a `tool_index:` list with ONE row for `zz_asset_alpha` carrying `source_group: {id: opal-data-assets, name: opal-data-assets, kind: bucket}` and NO `serves`;
   and, as further top-level keys, a channel-artifact row and a silver row that each carry `read_tool: zz_asset_alpha` and `firm: cottonwood` (mirror the shapes `_catalog_read_tool_rows` walks: a mapping with `read_tool` and an `entity` or `key`).
   Plant the tool with `_plant`. Assert the `opal-data-assets` channel's `segments` equals exactly `[{"vendor": "unresolved", "firm": "unresolved", "tools": ["zz_asset_alpha"]}]`, and that no segment has `firm` `cottonwood`.
2. `test_tool_index_serves_pair_makes_a_segment`: the SAME catalog text with `serves: [{vendor: schwab, firm: cottonwood}]` added to the `tool_index` row; assert `segments` equals exactly `[{"vendor": "schwab", "firm": "cottonwood", "tools": ["zz_asset_alpha"]}]`.
   (The owning-firm rows stay in the catalog in this test, which is what makes test 1 not vacuous.)

If a test shows the handler really does read a `firm` from outside `tool_index`, fix `_segment_fields_for` or `_declared_source_groups` minimally so the test passes, run the whole gateway admin suite, and say so in your report; otherwise do not touch the handler.

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. No other gateway file, no Terraform, no manifest, no catalog file. Make no deploy and no network call.
2. Do NOT flip this order's `<status>`: the order file is outside your `<paths>` and the issuer flips it. (This face overrides the worker rule that says to flip.)
3. If a criterion cannot be met without a file outside section 3, REFUSE it with what you measured and file a BLOCKING row. Never repair a criterion; the check scripts and the proof lines are the issuer's.
4. The served arm of this cell (the live page after the gateway release) is NOT yours and is not a criterion here.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/tests/test_admin_gateway_breakdown.py
infra/aws/ec2/opal-gateway/app/admin_gateway_breakdown.py
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~34/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: every other file, and `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pf/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id `NFRA_MCPORTAL-Z-W34-S<k>` (k from 1).
`surfaced_at` = `date -u +%FT%TZ` at filing. `disarm_owner` on an ARMED row is `2.0.0_SA_COO~MP`.

## 4. PROOF OF SPEC (literal; run from your worktree root `C:/tmp/mp-pf-34` after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-pf-4"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pf/checks/pf4.AC1.sh; echo "exit=$?"</invocation><expect>named tests PASSED 2 of 2.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-pf-4"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pf/checks/pf4.AC2.sh; echo "exit=$?"</invocation><expect>firm_keys_outside_tool_index=[1-9][0-9]* .*extra_pairs=0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~34/NFRA_MCPORTAL.TO-MP-pf-4.segments-read-tool-index-only-planted-arm-and-real-catalog.proof_of_spec.json`,
run `proof-of-spec-check.py` on it as the worker rules say, commit it with your tests, and report once, with:
- the check output of AC1 and AC2;
- the workspace commit hash;
- whether you changed the handler (file, lines) or not;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut at the PF round-3 issuance (decomposition v13) from the CTO's round-2 analysis @bfe9f3549c (cell S1, items i and iii) and the CVO's Z-C-S41. Checks dry-run at the base:
pf4.AC1 FAIL as expected (31 passed, named tests PASSED 0 of 2); pf4.AC2 PASS as expected (a bound: real catalog `tool_index_rows=99 firm_keys_outside_tool_index=273 pairs_from_tool_index=0 pairs_returned=0 extra_pairs=0`).
THE SERVED ARM (item ii) is NOT a worker criterion: `pf4.served.sh` is the issuer's, run at close once OG-ap-23 reads deployed; it FAILs at the base (deployed d577e0e7297b does not descend from 54a75d46ba). Item iii (live screenshots at 1280 and 390, graded by the CVO)
rides that run. S1 is NOT REALIZED until then. Risk is WORLD because the gate floors any `infra/` path at WORLD (a first cut at SERVED was refused); the worker's own work is offline tests.

<status>pending</status>
<status>complete</status>
<round>3</round>
<workstream>PF</workstream>
<slot>~34</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
