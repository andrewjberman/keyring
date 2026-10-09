# TO NFRA_TRNSPT.TO-TR-h14 -- H2 derives holdings_categories from the normalized input the composition names

<to_id>NFRA_TRNSPT.TO-TR-h14</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~2</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>14</round>
<workstream>communications</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `TR-h-14` (`decompositions/NFRA_TRNSPT_DECOMP_R14.md`) |
**outcome_ref:** FWD-10 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`TR-h-14`: ~P2 (msg 1849) measured that the IRPT analysis composition has NO holdings category weights, but "holdings sit in the normalized-input
artifact the composition names as a retention dependency, and H2 derives weights from it". Today `entry.abstract_request` reads
`holdings_categories` only from an optional `commentary_basis` (synthetic) and emits `{}` otherwise.

**Read (do not edit):** `infra/aws/lambda/investor-reporting/ycharts/generate/normalized_input.py` and its tests (the normalized input's shape:
what a position row carries -- asset class / category and weight or value), `docs/contracts/investor-reporting/v1/` (the composition's
retention dependency that names the normalized input), `data/transcripts/scripts/commentary/entry.py` (`abstract_request`,
`ABSTRACT_KEYS`).

**Build:**
1. `entry.py`: `abstract_request(ready_event, composition_reader, *, normalized_input_reader=None)`. When `normalized_input_reader` is given,
   resolve the normalized input the composition names, sum position weights (or market values, normalised to 100) by the category field the
   normalized input carries, and emit `holdings_categories` as category -> whole percent (largest-remainder rounding to sum 100). No ticker, no
   account id, no position-level row leaves the function (abstract fields only, C-KIMI). Without the reader, or when the composition names no
   normalized input, keep today's behavior. `ABSTRACT_KEYS` is unchanged.
2. `data/transcripts/scripts/tests/test_commentary_entry.py`: add `test_holdings_categories_from_normalized_input` (a synthetic normalized input
   with 3 categories and planted tickers / account ids -> exact percentages summing to 100; no planted ticker or id anywhere in the output),
   and a test that a missing normalized input yields `{}`. All existing entry tests stay green.

### ACCEPTANCE

<criterion id="TR14-h14-AC1" cell_refs="TR-h-14"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R14_CHECKS/r14_checks.py h14</invocation><expect>R14-H14-OK</expect></criterion>
`TR14-h14-AC1` -- the derivation test passes by name and the entry suite is green.

<expected_criteria>TR14-h14-AC1</expected_criteria>

Dry-run at the base (box/dell2 1440a9d3d1): `R14-H14-FAIL missing test_holdings_categories_from_normalized_input` -- FAIL as expected.

## BOUNDS

- **Grant.** The two paths below, this order's file, your deliverables folder. IRPT code and docs are READ only.
- **LOCAL.** No AWS, HTTP or model call; synthetic fixtures only.
- **Refusal clause.** If the normalized input carries no category field, derive nothing (keep `{}`), say so in the report, and file a surprise row
  (id `NFRA_TRNSPT-D2-W2-S<k>`, next unused across every document under `surprise-channel/`). Never invent a category.

<paths>
data/transcripts/scripts/commentary/entry.py
data/transcripts/scripts/tests/test_commentary_entry.py
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP_R14.md</decomp_doc> (round 14), cell `TR-h-14`.
<owned_cells>TR-h-14</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR14-h14-AC1. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~2/NFRA_TRNSPT.TO-TR-h14.holdings-categories.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR14-h14-AC1` BEFORE the flip. Commit code first, then pin each artifact to a
commit that contains it.
</proof_of_spec>

**REPORT:** the category field used and its source line, the rounding rule, the test names, the check line, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a pure function change.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call.
comp-adversary: RUN -- 3 sources read (normalized_input.py, the v1 contract docs, entry.py); BLIND to a real normalized input file. Traps: tickers or account ids leaking into the abstract request, percentages not summing to 100, an invented category; the face forbids each.
lane: entry.py, its test, the investigation file.
</preflight>

Source: ~P2 msg 1849; `/next-calls NFRA_TRNSPT --drive`; decomposition round 14 cell TR-h-14.
