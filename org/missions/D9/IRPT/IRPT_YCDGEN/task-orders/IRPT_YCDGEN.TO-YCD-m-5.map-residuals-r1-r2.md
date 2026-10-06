# IRPT_YCDGEN task order -- `YCD-m-5` -- ROUND 5 (ENRICHMENT): THE TWO MAPS' RESIDUALS (W4-S4 R1 AND R2)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R5.md</decomp_doc>
<owned_cells>YCD-m-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_IRPT_YCDGEN~4</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, trigger or EventBridge rule is added or read; the project runs on demand only (PRD C-SCOPE)
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE nothing is returned at the cut; the issuer's evidence context is this order's check files
</preflight>

**Project:** IRPT_YCDGEN (D9/IRPT, fabric laptop) -- YCharts direct-API generation, Opal-branded: every YCharts answer of a research run kept in the client firm's store with no secret in it, each report element traced to the answer it comes from, and Opal's own script making the report in Opal's branding. **Round 5** cuts the Overview to a 12-request plan (Andrew's bar: the report in one sitting), feeds the held-data elements from data Opal already holds, wires the six risk statistics, keys the change flag on the request, and closes the two maps' residuals. No worker calls YCharts, writes the store, deploys or grants: the issuer makes every live call at close. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the round-5 decomposition)

### `YCD-m-5` -- the map residuals (E5; FWD-3, FWD-4)
- 5.5 on `map_pdf.py` and the two maps, re-run on the two retained PDFs (OS temp only, as m-4 did).

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

### 5.5 The map residuals (YCD-m-5; W4-S4 R1 and R2)

- **R1:** Multi p9's third-security Bond Credit Quality row ("No data available") is listed as an element. It reads not available,
  with its source on the comparison call at key_index 2.
- **R2:** each of the seven placeholder labels "row" (Comparison p5.e17 and p9.e04; Multi p5.e12-e14, p9.e03 and p9.e04) takes
  the name the PDF prints on the line above. That name comes from `map_pdf`'s rule, not from map-side repair.
- Ids are never renumbered.

## 3. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD at the issuance commit)

- The CVO's round-4 grade (`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_YCDGEN_ROUND4_L9_GRADE_20261005.md`): every value row is listed (Comparison 178 of 178, Multi 221 of 221) and 0 figure values; m-4.AC3 fails on two residuals only. R1: Multi page 9's third-security Bond Credit Quality row prints 'No data available' and eight '--' under its stacked name, and no element lists it. R2: seven labels read the placeholder 'row' -- Comparison p5.e17 and p9.e04; Multi p5.e12, p5.e13, p5.e14, p9.e03 and p9.e04 -- where the PDF prints each name on the line above the values.
- The retained PDFs (read-only, into OS temp, deleted after): Comparison `REQ-7ea49c2d9b27957d0ea8888f`, Multi `REQ-329a56182b2668d44a28c8d7`; locate each as `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/live_walk/case_trace.py` does, with the main tree's `C:/Users/AndrewBerman/Desktop/ajb_workspace/.tools/aws` shim. Client data: labels and coordinates only.
- Base counts: comparison_map.json 574 elements, multi_map.json 423. Ids never renumber; a new element takes the next free id on its page. Put fixtures under `tests/fixtures/maps/`. Keep every existing test passing (test_map_pdf.py: 18 at the base).

## 4. SURFACES AND BOUNDS

You READ (never edit): `infra/aws/lambda/investor-reporting/` outside your `<paths>`, `lib/`, `infra/logic/`, `docs/`, `org/missions/D9/IRPT/IRPT_YCDGEN/` (the PRD, the decompositions, the maps you do not own). NEVER: a YCharts call (or any vendor call), an S3 or DynamoDB write, a deploy, a Terraform command, a portal change, a cookie, token or session value in any file, a figure value from a client file or a vendor answer in any committed file (C-FIRM), and none of another cell's files. Read-only AWS reads your order names use the main tree's shim `C:/Users/AndrewBerman/Desktop/ajb_workspace/.tools/aws`, into your OS temp directory only, deleted when done. Tests run with `python -m pytest <file> -q -p no:cacheprovider` from your worktree root. A check you cannot satisfy inside your `<paths>` is a surprise row appended to `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md` (one `## <ROW-ID> -- <title>` section with a fenced json row; ids `IRPT_YCDGEN-W<slot>-S<k>`, next unused k; `surfaced_at` the real UTC time), never an edit outside them.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/map_pdf.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_map_pdf.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/fixtures/maps/
org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/comparison_map.json
org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/multi_map.json
org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 5. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- neither map carries a placeholder 'row' label, and the Multi map lists page 9's 'No data available' row (`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round5/checks/m-5.AC1.py`)
- **AC2** -- the label rule takes a row's name from the line above when the row prints none (tests -k line_above in test_map_pdf.py, >= 1) (`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round5/checks/m-5.AC2.py`)
- **AC3** (judgment) -- W4-S4 re-graded by 3.0.0_SA_CVO against the two PDFs: every row listed, labels read right, no figure value

<proof_of_spec>
  <criterion id="AC1" cell_refs="YCD-m-5"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round5/checks/m-5.AC1.py</invocation><expect>m-5.AC1 RESULT: PASS</expect></criterion>
  <criterion id="AC2" cell_refs="YCD-m-5"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round5/checks/m-5.AC2.py</invocation><expect>m-5.AC2 RESULT: PASS</expect></criterion>
  <criterion id="AC3" cell_refs="YCD-m-5" judgment="true"/>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Write the instance at `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~4/IRPT_YCDGEN.TO-YCD-m-5.map-residuals-r1-r2.proof_of_spec.json` with `to_id` `IRPT_YCDGEN.TO-YCD-m-5.map-residuals-r1-r2`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~Y):** round 5 cut from the CTO's round-4 analysis @a1b47e6b3f sections 2-3 (E1-E6) and REMEDIATION_v4 (W3-S6, S7) with W4-S4; decomposition round 5 v1.0 (`IRPT_YCDGEN_DECOMP_R5.md`); PRD v0.1 @8b364d6d94; Andrew's egress word @ce20ca6854 (the issuer's live calls only). Chain `~4`. Risk WORLD: the gate's floor for infra paths. Checks dry-run at the base: m-5.AC1 FAIL as expected; m-5.AC2 FAIL as expected.

**DRAIN (2.0.0_SA_COO~Y, 2026-10-05 ~11:4xZ):** worker 0.9.0_WK_IRPT_YCDGEN~4 @3951983575, merged bb0c22bd1e; m-5.AC1 PASS (0 placeholder labels; Multi p9.e08 lists the 'No data available' row), m-5.AC2 PASS (4) on the merged tree. The seven labels come from the rule (map edited by id, labels from the rule's output; a section-label guard and its test keep Multi p13.e08). The rule also marks the portfolio's own p9.e03 no_data; the map does not carry that flag this round. AC3 is the CVO's judgment at L9.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>5</round>
<slot>~4</slot>
<fabric>laptop</fabric>
