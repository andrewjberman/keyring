# IRPT_YCDGEN task order -- `YCD-h-6` -- ROUND 6 (THREAD): THE OPAL PAGE NAMES NO VENDOR: BUILDER-ONLY AND CALL-SOURCED ELEMENTS, AND THE FOOTER, UNDER PRICING OFF

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R6A.md</decomp_doc>
<owned_cells>YCD-h-6</owned_cells>
</decomp_ref>
<to_id>IRPT_YCDGEN.TO-YCD-h-6.opal-page-no-vendor-wording</to_id>
<issued_to>0.9.0_WK_IRPT_YCDGEN~4</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE thread round; no schedule, trigger or EventBridge rule is added or read
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell; the resident host's role is proved by the issuer's close run
comp-adversary: DECLARED-NOT-APPLICABLE thread round; the lens runs on the enrichment round that touches this surface
</preflight>

**Project:** IRPT_YCDGEN (D9/IRPT, fabric laptop) -- the Analysis report made in house, Opal-branded, with no YCharts call. **Round 6** builds one thread: Andrew submits a Cottonwood portfolio for an Overview and opens an Opal-made report. The first version carries no pricing (returns, risk, benchmark and risk-free print not available, reason `NOT_IN_THIS_VERSION`). No worker calls a vendor, writes the store, deploys or grants: the issuer makes every live act at close. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the round-6 decomposition)

### `YCD-h-6` -- the opal page names no vendor: builder-only and call-sourced elements, and the footer, under pricing off (hops 7 Render (page wording); FWD-1)
- `ycharts/research/layout_overview.py`: R8, under `pricing=False` only (the `pricing=True` research path is unchanged).
- Tests added to `ycharts/research/tests/test_layout_overview.py`; keep every existing test passing (38 at the base).

## 2. THE CONTRACTS YOU BUILD AGAINST (inlined from the decomposition and IRPT_BCKEND PRD v0.28)

**R8 No vendor wording on the Opal page (PRD C-BRAND, C-BUILDERONLY).** Under `pricing=False` (the Opal producer's mode) the printed Overview names no YCharts source: a builder-only element prints 'Not available in this version.' (the reason NOT_IN_THIS_VERSION that `run.json` and the AnalysisReport document already carry), a vendor-call element prints the same line, and the page footer credit does not read 'Data: YCharts'. With `pricing=True` (the research path) the printed page is unchanged. Worker row IRPT_YCDGEN-W1-S8 measured the defect: `layout_overview.py` lines 56-59, 67, 943 and the footer in `build` (about 1088); on the real Overview map 65 BUILDER_ONLY and 22 call-sourced elements are not classed price-based, so the page prints the YCharts and time-budget lines while the record says NOT_IN_THIS_VERSION.

**R2 No pricing in this version (PRD C-V1).** Return, risk-statistic, benchmark and risk-free elements print NOT_AVAILABLE with reason `NOT_IN_THIS_VERSION`, value null. No price history is read. Holding weights are the accepted dollar amounts renormalized over the holdings that carry an amount; the method says so. Two states only: a value, or NOT_AVAILABLE with a reason from the closed set `COVERAGE_BELOW_0.95`, `STALE_INPUT`, `INPUT_MISSING:<name>`, `NOT_IN_THIS_VERSION`. An aggregate prints only when the holdings with an answer are at least 0.95 of the portfolio by weight.

## 3. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD at the issuance commit)

- Code lives under `infra/aws/lambda/investor-reporting/ycharts/research/`. Read first: the worker row IRPT_YCDGEN-W1-S8 in `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md`, then `layout_overview.py` (the wording lines and `build`'s footer it names, `_price_based`, the `pricing` parameter b-6 added) and `opal_producer.py` (merged from a-6; read only: how it calls `build` and maps layout reasons to the closed set with `closed_reason`).
- Print no figure and no vendor text on an Opal page; a research page keeps its footer. Tests use invented values and injected classifiers, never a live table.
- Module home and test layout: tests sit beside the code, no `conftest.py`, paths inserted at the top of each test file (as `ycharts/session/tests/test_resident_session.py:9`). Python tests run with `python -m pytest <file> -q -p no:cacheprovider` from your worktree root. Encoding: ASCII only in code and logs; no client figure and no secret in any committed file (C-FIRM, C-SECRET).

## 4. SURFACES AND BOUNDS

You READ (never edit): everything outside your `<paths>`, including `lib/`, `infra/logic/`, `docs/`, `org/missions/D9/IRPT/IRPT_YCDGEN/` (the PRD, the decompositions). NEVER: a vendor call (YCharts, Yahoo, Bloomberg or any other), an S3 or DynamoDB write, a live AWS call of any kind, a deploy, a Terraform command, a cookie, token or session value in any file, a figure value from a client file in any committed file, and none of another cell's files. A check you cannot satisfy inside your `<paths>` is a surprise row appended to `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md` (one `## <ROW-ID> -- <title>` section with a fenced json row; ids `IRPT_YCDGEN-W4-S<k>`, next unused k; `surfaced_at` the real UTC time), never an edit outside them.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_layout_overview.py
org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 5. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- a page rendered with pricing off contains no 'YCharts' text, in any case (tests -k opal_page_no_vendor_wording, >= 1 passed)
- **AC2** -- a builder-only element prints 'Not available in this version.' under pricing off (tests -k builder_only_not_in_this_version_line, >= 1 passed)
- **AC3** -- a page rendered with pricing on keeps its YCharts wording and footer unchanged (tests -k research_page_unchanged, >= 1 passed)
- **AC4** -- the whole test file passes (tests, all, no failure)

<proof_of_spec>
  <criterion id="AC1" cell_refs="YCD-h-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ycharts/research/tests/test_layout_overview.py -q -p no:cacheprovider -k opal_page_no_vendor_wording</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC2" cell_refs="YCD-h-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ycharts/research/tests/test_layout_overview.py -q -p no:cacheprovider -k builder_only_not_in_this_version_line</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC3" cell_refs="YCD-h-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ycharts/research/tests/test_layout_overview.py -q -p no:cacheprovider -k research_page_unchanged</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC4" cell_refs="YCD-h-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ycharts/research/tests/test_layout_overview.py -q -p no:cacheprovider</invocation><expect>^[0-9]+ passed</expect></criterion>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Write the instance at `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~4/IRPT_YCDGEN.TO-YCD-h-6.opal-page-no-vendor-wording.proof_of_spec.json` with `to_id` `IRPT_YCDGEN.TO-YCD-h-6.opal-page-no-vendor-wording`. Report once: each mechanical criterion's verdict line with the output above it; files written; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~Y):** round 6 cut from PRD v0.5 @e6a801f7f0 section 2 (the thread) and IRPT_BCKEND PRD v0.28 @3a8950aa20 items 29-31; CTO ruling msg 105387 (all cells in one issuance); decomposition round 6 revision 1.0 (`IRPT_YCDGEN_DECOMP_R6.md`). Chain `~4`, first order; addendum A cell (decomposition IRPT_YCDGEN_DECOMP_R6A.md), cut by the issuer as a second workstream (`<workstream>R6A_PERSIST_AND_PAGE</workstream>`, the gate's provision for a disjoint second set of orders in a round; the round-collision limb reads no override) to disarm worker row W1-S8, which the issuer did not accept as INERT because it breaks C-BRAND on the page Andrew opens; depends on a-6 and b-6 (merged). Its write set (layout_overview.py and its test) is b-6's, terminal and merged, and no other order of the round writes it. Risk WORLD: the gate's floor for infra paths and portal product files; nothing live moves inside the cell.

**DRAIN (2.0.0_SA_COO~Y, 2026-10-05 ~22:4xZ):** worker 0.9.0_WK_IRPT_YCDGEN~4 @fc018ca6c7, merged f2b8972f9b; h-6.AC1-AC4 PASS on the merged tree (AC4: 41 passed, 38 base plus 3 new), instance VALID. Under pricing=False the page prints 'Not available in this version.' for builder-only, unanswered and outside-budget elements and the footer reads 'Data: Opal Capital'. Worker's judgment call ACCEPTED: a call-sourced element that holds a kept answer still prints its value under pricing off; the Opal producer keeps no vendor answers, so it never arises there. Row W1-S8 DISARMED by this cell.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>6</round>
<workstream>R6A_PERSIST_AND_PAGE</workstream>
<slot>~4</slot>
<fabric>laptop</fabric>
