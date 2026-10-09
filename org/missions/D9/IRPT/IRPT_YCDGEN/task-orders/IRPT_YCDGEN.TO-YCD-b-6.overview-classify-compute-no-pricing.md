# IRPT_YCDGEN task order -- `YCD-b-6` -- ROUND 6 (THREAD): THE OVERVIEW'S CLASSIFY AND COMPUTE HOPS: THE TABLE'S NAMES AND CLASSES, WEIGHTS FROM AMOUNTS, NO PRICING

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R6.md</decomp_doc>
<owned_cells>YCD-b-6</owned_cells>
</decomp_ref>
<to_id>IRPT_YCDGEN.TO-YCD-b-6.overview-classify-compute-no-pricing</to_id>
<issued_to>0.9.0_WK_IRPT_YCDGEN~1</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE thread round; no schedule, trigger or EventBridge rule is added or read
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell; the resident host's role is proved by the issuer's close run
comp-adversary: DECLARED-NOT-APPLICABLE thread round; the lens runs on the enrichment round that touches this surface
</preflight>

**Project:** IRPT_YCDGEN (D9/IRPT, fabric laptop) -- the Analysis report made in house, Opal-branded, with no YCharts call. **Round 6** builds one thread: Andrew submits a Cottonwood portfolio for an Overview and opens an Opal-made report. The first version carries no pricing (returns, risk, benchmark and risk-free print not available, reason `NOT_IN_THIS_VERSION`). No worker calls a vendor, writes the store, deploys or grants: the issuer makes every live act at close. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the round-6 decomposition)

### `YCD-b-6` -- the overview's classify and compute hops: the table's names and classes, weights from amounts, no pricing (hops 4 Classify, 6 Compute; FWD-1, FWD-15 (read half), FWD-9)
- `ycharts/research/layout_overview.py`: R1 (classification read through `ETFClassifier`, the module's own `_scan_classifications` path removed from the Overview path) and R2 (weights from accepted dollar amounts; allocation by asset class and by sub asset class; every price-based element NOT_AVAILABLE with `NOT_IN_THIS_VERSION`; the 0.95 coverage rule on aggregates).
- Tests in `ycharts/research/tests/test_layout_overview.py`, fixtures under `ycharts/research/tests/fixtures/opal_overview/` (structure only, invented values).
- Keep every existing test in that file passing.

## 2. THE CONTRACTS YOU BUILD AGAINST (inlined from the decomposition and IRPT_BCKEND PRD v0.28)

**R1 Classification through the client.** Every security's printed name, asset class and sub asset class is read through `ETFClassifier` (`infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py`; `get_classification`, `classify_holdings`; record fields `ticker`, `asset_class`, `sub_asset_class`, `name`). A holding with no row prints as `not yet classified`. Yahoo's or any outside label is never printed in place of the table's. The Overview path no longer scans the table by itself.

**R2 No pricing in this version (PRD C-V1).** Return, risk-statistic, benchmark and risk-free elements print NOT_AVAILABLE with reason `NOT_IN_THIS_VERSION`, value null. No price history is read. Holding weights are the accepted dollar amounts renormalized over the holdings that carry an amount; the method says so. Two states only: a value, or NOT_AVAILABLE with a reason from the closed set `COVERAGE_BELOW_0.95`, `STALE_INPUT`, `INPUT_MISSING:<name>`, `NOT_IN_THIS_VERSION`. An aggregate prints only when the holdings with an answer are at least 0.95 of the portfolio by weight.

## 3. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD at the issuance commit)

- Read first: `layout_overview.py` `compute_element` (618), `compute_all` (651), `load_held_rows` (721), `_scan_classifications` (702), `_compute_opal_held` (588), `build` (901), `render` (953), and `held_data.py`. Holdings come from `run_doc["holdings"]` (`_holdings`, 241): keep that input shape; the producer (a-6) passes it.
- `ETFClassifier` takes the table name `etf-classifications` and a region; tests inject a fake with the same methods, never a live table.
- This cell does not write `held_data.py`; if it needs a change there, file a surprise row.
- Module home and test layout: tests sit beside the code, no `conftest.py`, paths inserted at the top of each test file (as `ycharts/session/tests/test_resident_session.py:9`). Python tests run with `python -m pytest <file> -q -p no:cacheprovider` from your worktree root. Encoding: ASCII only in code and logs; no client figure and no secret in any committed file (C-FIRM, C-SECRET).

## 4. SURFACES AND BOUNDS

You READ (never edit): everything outside your `<paths>`, including `lib/`, `infra/logic/`, `docs/`, `org/missions/D9/IRPT/IRPT_YCDGEN/` (the PRD, the decompositions). NEVER: a vendor call (YCharts, Yahoo, Bloomberg or any other), an S3 or DynamoDB write, a live AWS call of any kind, a deploy, a Terraform command, a cookie, token or session value in any file, a figure value from a client file in any committed file, and none of another cell's files. A check you cannot satisfy inside your `<paths>` is a surprise row appended to `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md` (one `## <ROW-ID> -- <title>` section with a fenced json row; ids `IRPT_YCDGEN-W1-S<k>`, next unused k; `surfaced_at` the real UTC time), never an edit outside them.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_layout_overview.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/fixtures/opal_overview/
org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 5. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- a holding's printed name, asset class and sub asset class equal the injected classifier's row (tests -k classification_through_client, >= 1 passed)
- **AC2** -- a holding with no classifier row prints 'not yet classified' (tests -k unclassified_not_yet_classified, >= 1 passed)
- **AC3** -- every price-based element is NOT_AVAILABLE with reason NOT_IN_THIS_VERSION and a null value (tests -k not_in_this_version, >= 1 passed)
- **AC4** -- allocation weights equal each holding's amount over the sum of amounts (tests -k allocation_from_amounts, >= 1 passed)
- **AC5** -- the Overview path makes no table scan of its own (tests -k no_second_classification_read, >= 1 passed)
- **AC6** -- the whole test file passes (tests, all, no failure)

<proof_of_spec>
  <criterion id="AC1" cell_refs="YCD-b-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ycharts/research/tests/test_layout_overview.py -q -p no:cacheprovider -k classification_through_client</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC2" cell_refs="YCD-b-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ycharts/research/tests/test_layout_overview.py -q -p no:cacheprovider -k unclassified_not_yet_classified</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC3" cell_refs="YCD-b-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ycharts/research/tests/test_layout_overview.py -q -p no:cacheprovider -k not_in_this_version</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC4" cell_refs="YCD-b-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ycharts/research/tests/test_layout_overview.py -q -p no:cacheprovider -k allocation_from_amounts</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC5" cell_refs="YCD-b-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ycharts/research/tests/test_layout_overview.py -q -p no:cacheprovider -k no_second_classification_read</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC6" cell_refs="YCD-b-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ycharts/research/tests/test_layout_overview.py -q -p no:cacheprovider</invocation><expect>^[0-9]+ passed</expect></criterion>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Write the instance at `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~1/IRPT_YCDGEN.TO-YCD-b-6.overview-classify-compute-no-pricing.proof_of_spec.json` with `to_id` `IRPT_YCDGEN.TO-YCD-b-6.overview-classify-compute-no-pricing`. Report once: each mechanical criterion's verdict line with the output above it; files written; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~Y):** round 6 cut from PRD v0.5 @e6a801f7f0 section 2 (the thread) and IRPT_BCKEND PRD v0.28 @3a8950aa20 items 29-31; CTO ruling msg 105387 (all cells in one issuance); decomposition round 6 revision 1.0 (`IRPT_YCDGEN_DECOMP_R6.md`). Chain `~1`, first order; no dependency. Risk WORLD: the gate's floor for infra paths and portal product files; nothing live moves inside the cell.

**DRAIN (2.0.0_SA_COO~Y, 2026-10-05 ~21:5xZ):** worker 0.9.0_WK_IRPT_YCDGEN~1 @ef6c379f52, merged 9cbfbf2215 (the append-only investigations file conflicted with the s-6 drain and was resolved as a union, one shared closing fence restored); b-6.AC1-AC6 PASS on the merged tree (AC6: 38 passed, the 32 existing plus 6 new). Rows: W1-S3 ARMED and DISARMED by the a-6 amendment (the producer builds with pricing=False; criterion AC7); W1-S4 and W1-S5 INERT, accepted (`_scan_classifications` stays as a retired function an existing test calls; a plain YCharts-call element is not price-marked, and the Opal producer reads no YCharts call).

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>6</round>
<slot>~1</slot>
<fabric>laptop</fabric>
