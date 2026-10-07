# TO ADVI_COTBKF.TO-CB-h-1 -- round 8 CB-h-1: the transactions repeat count measured and cited; the FWD-6 page with one plain line per kind of record

<to_id>ADVI_COTBKF.TO-CB-h-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~24</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>8</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-h-1` (`decompositions/ADVI_COTBKF_DECOMP.round8.md`) |
**outcome_ref:** FWD-1 (row W23-S1), FWD-6 (CB7g3-AC3) | **depends_on:** none

---

## WORKER FACE

### THE CELL

`CB-h-1` has two parts that touch one page.

**Part 1 -- the repeat count (FWD-1, row W23-S1).** The applied silver transactions table
(`opal_naming.address("commonwealth", "cottonwood", "silver", "transactions", "date=2026-06-23")`, 14 files) reads 1,416,497 rows. An
early row (W2-S1) said silver would keep 1,415,137 after dropping 1,360 records "identical in all 20 vendor columns". Build
`data/assets/scripts/analysis/commonwealth_tx_repeats.py`, read-only, which reads the APPLIED table and counts rows that repeat an earlier
row on all 20 vendor columns (exclude the 5 lineage columns such as `source_record`), and prints as its LAST line exactly:
`TX-REPEATS rows=<n> exact_repeat_rows=<r> distinct=<n-r> key=20_vendor_columns`.
The cause, which the issuer read before the cut and you cite (do not re-derive it): the ratified PRD keeps every delivered record --
`org/missions/D8/ADVI/ADVI_COTBKF/prd/ADVI_COTBKF_PRD.md` lines 204-206 (v0.4 addendum item 1: "C-SILVER clarified: every delivered row
is kept. Without a transaction id, two identical lines may be two real events ... rebuilt with all 1,416,497 records") and line 114
(C-SILVER); the writer agrees at `data/assets/scripts/silver/commonwealth_transactions.py` lines 13-15 ("nothing is de-duplicated").
So a repeat is two real records, not a write that skipped a drop. Write the count and that citation into a short
`TX_REPEATS.md` in your deliverables folder. If your measured `exact_repeat_rows` is NOT 1,360, say so plainly and file a surprise row.

**Part 2 -- the FWD-6 page (CB7g3-AC3, NOT MET).** `data/assets/scripts/analysis/commonwealth_coverage_statement.py` (round 7) writes
`COVERAGE_STATEMENT.md`, organized by storage table, and gives one 2016-2026 range for all documents; a reader not told otherwise takes
statements to reach 2016. The data is right: statements run 12 months, tax forms 2 tax years. Change the page so it LEADS with one plain
line per KIND of record -- transactions, positions, statements, tax forms, CRM, prices -- each line naming what is covered, ITS OWN date
span and its count (read from the applied tables; statement and tax-form spans from the documents table's `doc_type` and `doc_date`),
or "not covered" with its reason and row. The transactions line reads: 1,416,497 rows, of which `<r>` are exact repeats kept by design
(C-SILVER), citing your TX_REPEATS.md. The per-table sections may stay below the lead lines. The script's LAST line becomes:
`COVERAGE-STATEMENT tables=11 kinds=6 every_kind_has_own_span=<True|False> every_not_covered_has_reason_and_row=<True|False> rows_cited=<k> rows_missing=<m>`.
`every_kind_has_own_span` is False when any kind line carries a span outside that kind's own min and max dates.

**Tests:** `data/assets/scripts/analysis/tests/test_commonwealth_tx_repeats.py` -- a stub table of 5 rows with 1 exact repeat (and one
row differing only in `source_record`, which must count as a repeat) prints `exact_repeat_rows=2`; with no repeats, `0` (the control).
In `test_commonwealth_coverage_statement.py`, add tests named with `per_kind`: a stub with statements spanning 12 months and a
document range of 10 years prints the statement line with the 12-month span and `every_kind_has_own_span=True`; a stub whose statement
line is fed the 10-year range prints `False` (the control). Keep the round-7 tests passing (update their expected last line only for
the new fields).

### ACCEPTANCE

<criterion id="CB8h1-AC1" cell_refs="CB-h-1"><invocation>python data/assets/scripts/analysis/commonwealth_tx_repeats.py --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~24</invocation><expect>TX-REPEATS rows=1416497</expect></criterion>
`CB8h1-AC1` -- the repeat count on the applied table (the count follows the prefix on the same line; it is recorded, not presumed).

<criterion id="CB8h1-AC2" cell_refs="CB-h-1"><invocation>python data/assets/scripts/analysis/commonwealth_coverage_statement.py --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~24</invocation><expect>COVERAGE-STATEMENT tables=11 kinds=6 every_kind_has_own_span=True every_not_covered_has_reason_and_row=True</expect></criterion>
`CB8h1-AC2` -- the per-kind page on the applied tables.

<criterion id="CB8h1-AC3" cell_refs="CB-h-1" judgment="true"/>
`CB8h1-AC3` -- JUDGMENT, graded by `3.0.0_SA_CVO` at L9: the page reads correctly for someone who was not told (FWD-6's DONE WHEN).

<expected_criteria>CB8h1-AC1,CB8h1-AC2,CB8h1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scratch under `.scratch/`, uncommitted.
- **Read-only.** No S3 write; no re-apply of transactions; do not edit `commonwealth_transactions.py` or the PRD.
- **No typed bucket or key.**
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `ADVI_COTBKF-W24-S<k>`), and do not weaken the test.

<paths>
data/assets/scripts/analysis/commonwealth_tx_repeats.py
data/assets/scripts/analysis/tests/test_commonwealth_tx_repeats.py
data/assets/scripts/analysis/commonwealth_coverage_statement.py
data/assets/scripts/analysis/tests/test_commonwealth_coverage_statement.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round8.md</decomp_doc> (round 8), cell `CB-h-1`.
<owned_cells>CB-h-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB8h1-AC1, CB8h1-AC2, CB8h1-AC3 (judgment: UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming 3.0.0_SA_CVO; never PASS
or FAIL). Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~24/ADVI_COTBKF.TO-CB-h-1.repeats-and-per-kind-page.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB8h1-AC1,CB8h1-AC2,CB8h1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the TX-REPEATS line, the six kind lines as written, the COVERAGE-STATEMENT line, rows filed, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a one-time read.
comp-iam: DECLARED-NOT-APPLICABLE reads under the dell2 identity on opal-data-assets; denominator 1 bucket; BLIND: none needed.
comp-adversary: RUN -- the count measured on the applied table, the cause cited from the ratified PRD and the writer, never asserted from a row; a repeat differing only in lineage counts as a repeat; each kind's span is its own; BLIND: the CRM kind (behind C-RESTRICTED, stated not covered).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-7 analysis @625987b867, E1-E2 (E3 put back to the CTO, not cut); rows W2-S1, W23-S1; CVO grade CB7g3-AC3.
