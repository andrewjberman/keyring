# IRPT_YCDGEN task order -- `YCD-m-4` -- ROUND 4 (ENRICHMENT): THE MAP LABEL RULE AND THE TWO MAPS' MISSING ROWS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R4.md</decomp_doc>
<owned_cells>YCD-m-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_IRPT_YCDGEN~4</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, trigger or EventBridge rule is added or read; the project runs on demand only (PRD C-SCOPE)
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE nothing is returned at the cut; the issuer's evidence context is this order's check files
</preflight>

**Project:** IRPT_YCDGEN (D9/IRPT, fabric laptop) -- YCharts direct-API generation, Opal-branded: every YCharts answer of a research run kept in the client firm's store with no secret in it, each report element traced to the answer it comes from, and Opal's own script making the report in Opal's branding. **Round 4** gives the runner a per-window call budget (the firewall challenges the 7th request of any run), finds which held-data figures Opal already holds, adds six risk statistics, and fixes the two maps' missing rows. No worker calls YCharts, writes the store, deploys or grants: the issuer makes every live call at close. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the round-3 decomposition)

### `YCD-m-4` -- the map label rule and the two maps' rows (E2; FWD-3, FWD-4)
- `ycharts/research/map_pdf.py`: 4.4's rule, with a test named `test_lowercase_*` (a label starting `iShares` is kept).
- Re-run on the two retained PDFs (as m-3 did, OS temp only): `comparison_map.json` and `multi_map.json` gain the 21 and 29
  rows that m-3.AC2 found missing. The Multi's third-security rows go on the comparison calls at `key_index` 2; the holdings
  rows are BUILDER_ONLY data rows. The Comparison's p8 Bond Maturity chart is listed, and p8.e03 sourced to its key. p22.e16-e19
  are masked. Element ids are never renumbered.

## 2. THE CONTRACTS YOU BUILD AGAINST (inlined verbatim from the decompositions)

### 2.3 The element map (C-MAP) -- `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/overview_map.json`

```json
{
 "schema": "irpt-ycdgen-map-v1", "report_type": "OVERVIEW", "template_id": "14141822",
 "source_pdf": {"bucket": "opal-data-irpt", "artifact_prefix": "ART-<first 12 hex>", "pages": 4},
 "calls": [{"name": "snake_case", "method": "GET", "path": "/charts/general_data.json",
            "params": {"securities": "id:{security_id},include:true,,", "metrics": "id:total_return,include:true,,"}}],
 "elements": [{"id": "p1.e01", "page": 1, "kind": "number | table | chart | text", "label": "printed label text",
               "source": {"call": "snake_case", "field": "JSONPath into the kept body_json"},
               "claim": "inferred | measured", "note": "one line"},
              {"id": "p3.e04", "page": 3, "kind": "chart", "label": "...", "source": "BUILDER_ONLY",
               "claim": "inferred", "note": "computed only inside YCharts' report builder"}]
}
```

- Labels are printed label text only. **No figure value from the PDF enters git** (C-FIRM): no number read from a figure's
  position, no dollar amount, no percentage value.
- `params` placeholders: `{security_id}` (the portfolio's typed id), `{start}`, `{end}`.

### 2.4 Module home and run environment

- Package: `infra/aws/lambda/investor-reporting/ycharts/research/` (new): `keeper.py`, `runner.py`, `layout_overview.py`,
  `render_pdf.cjs`, `map_pdf.py`, and `tests/`. Tests follow the sibling layout: beside the code, no `conftest.py`, paths
  inserted at the top of each test file (as `ycharts/session/tests/test_resident_session.py:9`).
- The runner imports the served session modules as top-level modules, so it puts `ycharts/session` and `ycharts/generate`
  on `sys.path` (`resident_session.py` imports `broker`, `transport`, `deadline_transport`).

### 4.4 The map label rule (built by YCD-m-4)

`map_pdf`'s label rule keeps a label containing a lowercase-initial word (`iShares`, `iPath`); a label is dropped only for a
reason that is not its case. The two maps' rows come from the rule, with no map-side repair. The m-3 rows W4-S4 names are added.

## 3. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD at the issuance commit)

- `map_pdf._prose_label` (around lines 291-296) drops any label holding a lowercase-initial word, so `iShares` and `iPath` rows vanish: 21 rows on the Comparison map and 29 on the Multi (the CVO's m-3.AC2 grade, `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_YCDGEN_ROUND3_L9_GRADE_20261005.md`). The Multi map today carries 27 labels repaired map-side by round 3 (row W4-S4); after your rule they must come from the rule.
- The retained PDFs (read-only, into OS temp, deleted after): Comparison `REQ-7ea49c2d9b27957d0ea8888f`, Multi `REQ-329a56182b2668d44a28c8d7`. Locate them as `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/live_walk/case_trace.py` does. Use the main tree's `C:/Users/AndrewBerman/Desktop/ajb_workspace/.tools/aws` shim. Client data: labels and coordinates only.
- Base counts: comparison_map.json 552 elements (32 pages), multi_map.json 394 (34 pages). Ids never renumber; new elements take the next free id on their page.

## 4. SURFACES AND BOUNDS

You READ (never edit): `infra/aws/lambda/investor-reporting/` outside your `<paths>`, `lib/`, `infra/logic/`, `docs/`, `org/missions/D9/IRPT/IRPT_YCDGEN/` (the PRD, the decompositions, the maps you do not own). NEVER: a YCharts call (or any vendor call), an S3 or DynamoDB write, a deploy, a Terraform command, a portal change, a cookie, token or session value in any file, a figure value from a client file or a vendor answer in any committed file (C-FIRM), and none of another cell's files. Read-only AWS reads your order names use the main tree's shim `C:/Users/AndrewBerman/Desktop/ajb_workspace/.tools/aws`, into your OS temp directory only, deleted when done. Tests run with `python -m pytest <file> -q -p no:cacheprovider` from your worktree root. A check you cannot satisfy inside your `<paths>` is a surprise row appended to `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md` (one `## <ROW-ID> -- <title>` section with a fenced json row; ids `IRPT_YCDGEN-W<slot>-S<k>`, next unused k; `surfaced_at` the real UTC time), never an edit outside them.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/map_pdf.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_map_pdf.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/fixtures/
org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/comparison_map.json
org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/multi_map.json
org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 5. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the label rule keeps a lowercase-initial name (tests -k lowercase in test_map_pdf.py, >= 1) (`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round4/checks/m-4.AC1.py`)
- **AC2** -- the maps gain the missing rows: comparison >= 573 elements, multi >= 423 (`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round4/checks/m-4.AC2.py`)
- **AC3** (judgment) -- m-3.AC2 re-graded by 3.0.0_SA_CVO against the PDFs: every row listed, labels read right, no figure value

<proof_of_spec>
  <criterion id="AC1" cell_refs="YCD-m-4"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round4/checks/m-4.AC1.py</invocation><expect>m-4.AC1 RESULT: PASS</expect></criterion>
  <criterion id="AC2" cell_refs="YCD-m-4"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round4/checks/m-4.AC2.py</invocation><expect>m-4.AC2 RESULT: PASS</expect></criterion>
  <criterion id="AC3" cell_refs="YCD-m-4" judgment="true"/>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Write the instance at `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~4/IRPT_YCDGEN.TO-YCD-m-4.map-label-rule-and-rows.proof_of_spec.json` with `to_id` `IRPT_YCDGEN.TO-YCD-m-4.map-label-rule-and-rows`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~Y):** round 4 cut from the CTO's round-3 analysis @033795b666 sections 2-3 (E1-E6); decomposition round 4 v1.0 (`IRPT_YCDGEN_DECOMP_R4.md`); PRD v0.1 @8b364d6d94; Andrew's egress word @ce20ca6854 (the issuer's live calls only). Chain `~4`. Risk WORLD: the gate's floor for infra paths. Checks dry-run at the base: m-4.AC1 FAIL as expected; m-4.AC2 FAIL as expected.

**DRAIN (2.0.0_SA_COO~Y, 2026-10-05 ~06:3xZ):** worker 0.9.0_WK_IRPT_YCDGEN~4 @c73a8fae30, merged c3b266a60a (channel conflict resolved as base plus both appendices); m-4.AC1 PASS (4), m-4.AC2 PASS (comparison 574, multi 423) on the merged tree. Rows W4-S5 and W4-S6 ACCEPTED (the seven Multi third-security stat names and Comparison p8.e33 remain map-side, named; 129 ordinal labels renumbered with ids and sources kept). AC3 is the CVO's judgment at L9.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>4</round>
<slot>~4</slot>
<fabric>laptop</fabric>
