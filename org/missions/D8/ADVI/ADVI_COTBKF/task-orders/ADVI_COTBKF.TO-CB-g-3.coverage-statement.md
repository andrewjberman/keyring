# TO ADVI_COTBKF.TO-CB-g-3 -- round 7 CB-g-3: the FWD-6 coverage statement -- one page, per table, what the backfill covers and does not

<to_id>ADVI_COTBKF.TO-CB-g-3</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~23</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>7</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-g-3` (`decompositions/ADVI_COTBKF_DECOMP.round7.md`) |
**outcome_ref:** FWD-6 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`CB-g-3`, FWD-6: someone who was not told can read, on one page, what the Cottonwood 10-year backfill from Commonwealth holds and what it
does not. The backfill's tables live at `opal_naming.address("commonwealth", "cottonwood", <tier>, <table>, "date=2026-06-23")`:
silver -- account_links, coverage, crosswalk, document_index, documents, performance, positions, transactions (8); bronze -- imaging,
manifest, portfolio_accounting (3). The existing `data/assets/scripts/silver/commonwealth_coverage.py` builds the silver `coverage` table;
read it and use it where it already answers a question.

You build `data/assets/scripts/analysis/commonwealth_coverage_statement.py`, read-only, which writes ONE page `COVERAGE_STATEMENT.md` to
`--out`, with one section per table (all 11), each giving: what it covers, with counts read from the APPLIED table (rows, accounts, date
span, distinct securities or documents as fits); and a NOT COVERED list where each line names its REASON and its ROW id from the project's
surprise channel (`org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/`). Known gaps to state, each with its row (verify each row id
exists in the channel; never invent one):
- the CRM zip is NOT in the backfill yet: behind C-RESTRICTED (rows S7, W19-S1);
- prices: 1,720 of 4,634 securities priced from Opal's own stores; 1,297,651 of 9,388,961 security-days covered (row S17); the pull
  waits on another project's store;
- the 21 near-matches are not linked, awaiting a person (row W14-S2 or the near-match rows you find);
- any other gap you find from the tables, with its row, or a new surprise row if none exists.
The script prints as its LAST line exactly:
`COVERAGE-STATEMENT tables=<n> every_not_covered_has_reason_and_row=<True|False> rows_cited=<k> rows_missing=<m>`,
where `rows_missing` counts cited row ids not found in the channel.

**Tests** `data/assets/scripts/analysis/tests/test_commonwealth_coverage_statement.py` (stubs, no AWS): a stub of 2 tables with one gap
citing an existing row prints `tables=2 every_not_covered_has_reason_and_row=True rows_missing=0`; the same stub citing a row id absent
from a stub channel prints `rows_missing=1` and `every_not_covered_has_reason_and_row=False` (the control).

### ACCEPTANCE

<criterion id="CB7g3-AC1" cell_refs="CB-g-3"><invocation>python -m pytest -q data/assets/scripts/analysis/tests/test_commonwealth_coverage_statement.py</invocation><expect>passed</expect></criterion>
`CB7g3-AC1` -- the statement on stubs, with the missing-row control.

<criterion id="CB7g3-AC2" cell_refs="CB-g-3"><invocation>python data/assets/scripts/analysis/commonwealth_coverage_statement.py --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~23</invocation><expect>COVERAGE-STATEMENT tables=11 every_not_covered_has_reason_and_row=True</expect></criterion>
`CB7g3-AC2` -- the real tables, every gap with its reason and an existing row.

<criterion id="CB7g3-AC3" cell_refs="CB-g-3" judgment="true"/>
`CB7g3-AC3` -- JUDGMENT, graded by `3.0.0_SA_CVO` at L9: the page reads for someone who was not told (FWD-6's DONE WHEN).

<expected_criteria>CB7g3-AC1,CB7g3-AC2,CB7g3-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scratch under `.scratch/`, uncommitted.
- **Read-only.** No S3 write. Do not edit `commonwealth_coverage.py`.
- **No typed bucket or key.**
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `ADVI_COTBKF-W23-S<k>`), and do not weaken the test.

<paths>
data/assets/scripts/analysis/commonwealth_coverage_statement.py
data/assets/scripts/analysis/tests/test_commonwealth_coverage_statement.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round7.md</decomp_doc> (round 7), cell `CB-g-3`.
<owned_cells>CB-g-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB7g3-AC1, CB7g3-AC2, CB7g3-AC3 (judgment: UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming 3.0.0_SA_CVO; never PASS
or FAIL). Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~23/ADVI_COTBKF.TO-CB-g-3.coverage-statement.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB7g3-AC1,CB7g3-AC2,CB7g3-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the COVERAGE-STATEMENT line, the rows cited, any new row filed, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a one-time read.
comp-iam: DECLARED-NOT-APPLICABLE reads under the dell2 identity on opal-data-assets; denominator 1 bucket; BLIND: opal-data-cottonwood (fenced; nothing of this backfill lives there yet).
comp-adversary: RUN -- every gap cites a row that exists, with a control that a missing row is caught; counts from the applied tables; BLIND: the CRM zip's contents (behind C-RESTRICTED).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-6 analysis @1c9c98e652, E3; FWD-6 in the PRD.
