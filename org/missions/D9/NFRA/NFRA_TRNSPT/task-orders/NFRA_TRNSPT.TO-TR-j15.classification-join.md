# TO NFRA_TRNSPT.TO-TR-j15 -- H2 holdings categories from the canonical per-security table (coverage + unclassified named)

<to_id>NFRA_TRNSPT.TO-TR-j15</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~1</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>15</round>
<workstream>communications</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `TR-j-15` (`decompositions/NFRA_TRNSPT_DECOMP_R15.md`) |
**outcome_ref:** FWD-10 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`TR-j-15` (CTO ruling msg 2191 on row NFRA_TRNSPT-D2-W2-S3): "joins security_id to etf-classifications asset_class, printing coverage (classified of
total weight) and naming every unclassified holding, never guessed." Round 14 built `entry.abstract_request(..., normalized_input_reader=...)` which
sums weights by a row-level `category` -- but the IRPT v1 normalized input has no category: a position row is `security_id` + `analysis_dollars` +
`original{identifier, quantity, source_*}` (`docs/contracts/investor-reporting/v1/examples/RequestComposition.synthetic.json:134-182`,
`docs/contracts/investor-reporting/v1/AnalysisRequest.schema.json:159-237`, `infra/aws/lambda/investor-reporting/ycharts/generate/normalized_input.py`).

**Inputs (read-only):** `data/transcripts/scripts/commentary/classification_source_20261009.json` (the issuer's snapshot of DynamoDB
`etf-classifications`: `classifications: [{ticker, asset_class, sub_asset_class}]`, 11,361 rows); `data/transcripts/scripts/commentary/entry.py`; the
v1 docs above (to establish what `security_id` is -- a ticker or an internal id -- and, if not a ticker, which field is).

**Build:**
1. `data/transcripts/scripts/commentary/classification.py` (new): `load_classifications(path=<the snapshot>) -> dict` (ticker, upper-cased ->
   asset_class); `categorize(rows, classifications, *, id_field) -> (holdings_categories, holdings_coverage)` where `holdings_categories` is asset
   class -> whole percent of CLASSIFIED weight (largest-remainder rounding to 100; empty when nothing is classified) and `holdings_coverage` is
   `{"total_weight", "classified_weight", "coverage_pct", "unclassified": [{"identifier", "weight"}...]}`. An identifier not in the table is
   UNCLASSIFIED -- never guessed, never mapped by a heuristic.
2. `entry.py`: when a `normalized_input_reader` is given and the rows carry no `category`, use `classification.categorize` with the id field you
   measured; `abstract_request` keeps `ABSTRACT_KEYS` (only `holdings_categories` reaches the model); add `holdings_coverage` to `ticket_context`
   only if it fits that output's purpose, otherwise return it beside the request from `handler` for the record -- say which in the report.
3. `data/transcripts/scripts/tests/test_commentary_classification.py` (new), on synthetic rows and a tiny synthetic classification map:
   `test_categories_from_canonical_join` (3 tickers in 2 classes -> exact percentages); `test_unclassified_named_never_guessed` (an unknown
   identifier is listed in `unclassified` with its weight and contributes to no class); `test_coverage_reported` (coverage_pct = classified /
   total, two decimals); and a test that no identifier appears in `abstract_request`.

### ACCEPTANCE

<criterion id="TR15-j15-AC1" cell_refs="TR-j-15"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R15_CHECKS/r15_checks.py j15</invocation><expect>R15-J15-OK</expect></criterion>
`TR15-j15-AC1` -- the join, the unclassified-named and the coverage tests pass by name.

<expected_criteria>TR15-j15-AC1</expected_criteria>

Dry-run at the base (box/dell2 b5f34fd947): `R15-J15-FAIL absent` -- FAIL as expected. Keep every `test_commentary_*.py` green.

## BOUNDS

- **Grant.** The paths below, this order's file, your deliverables folder. IRPT code, docs and the snapshot are READ only.
- **LOCAL.** No AWS, HTTP or model call; synthetic fixtures only.
- **Refusal clause.** If neither `security_id` nor any field the composition carries is a ticker, keep everything unclassified (coverage 0), say so,
  and file a surprise row (id `NFRA_TRNSPT-D2-W1-S<k>`, next unused across every document under `surprise-channel/`). Never invent a mapping.

<paths>
data/transcripts/scripts/commentary/classification.py
data/transcripts/scripts/commentary/entry.py
data/transcripts/scripts/tests/test_commentary_classification.py
data/transcripts/scripts/tests/test_commentary_entry.py
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP_R15.md</decomp_doc> (round 15), cell `TR-j-15`.
<owned_cells>TR-j-15</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR15-j15-AC1. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~1/NFRA_TRNSPT.TO-TR-j15.classification-join.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR15-j15-AC1` BEFORE the flip. Commit code first, then pin each artifact to a
commit that contains it.
</proof_of_spec>

**REPORT:** what `security_id` is (with its source line) and the id field used, where `holdings_coverage` goes, the test names, the check line,
commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a pure function and a data snapshot.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker; the issuer read the table (read-only scan).
comp-adversary: RUN -- 4 sources read (the snapshot, entry.py, the v1 contract docs, normalized_input.py); BLIND to a real normalized input file. Traps: a guessed class for an unknown id, an identifier leaking into the model prompt, coverage computed over classified weight only; the face fixes each.
lane: one new module, entry.py, two tests, the investigation file.
</preflight>

Source: CTO ruling msg 2191; row NFRA_TRNSPT-D2-W2-S3; decomposition round 15 cell TR-j-15 and issuer rulings 1-3.
