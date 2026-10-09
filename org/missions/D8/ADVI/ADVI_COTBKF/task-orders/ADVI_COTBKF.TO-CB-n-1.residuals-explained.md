# TO ADVI_COTBKF.TO-CB-n-1 -- round 14 CB-n-1: the 5 remaining fractional residuals explained and classed

<to_id>ADVI_COTBKF.TO-CB-n-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~30</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>14</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-n-1` (`decompositions/ADVI_COTBKF_DECOMP.round14.md`) |
**outcome_ref:** FWD-3 (C-DAILY step 1) | **depends_on:** none

---

## WORKER FACE

### THE CELL

`CB-n-1`, FWD-3: the daily-holdings rebuild (`data/assets/scripts/silver/commonwealth_daily_holdings.py`), signing every transaction type
through ONE table (`data/assets/scripts/silver/commonwealth_signs.py`), leaves exactly 5 account-security pairs holding a non-zero fraction
under one share after their last transaction (`fractional_residuals=5`, listed with their type histories in
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~29/fractional_residuals.csv`):
- acct#fa82ce1d and acct#3b5864a2, both on CUSIP 74440B405 (0.029 and 0.02);
- acct#9bd1ed4d and acct#87772861, both on 07399D345 (0.00086 each, after CAF rows);
- acct#2f33cbcc on 60934N500 (0.003, from a single `li`).

Explain each from its transaction rows in the applied silver transactions
(`opal_naming.address("commonwealth", <cottonwood scope via opal_naming.lookup>, "silver", "transactions", "date=2026-06-23")`) and class it
as exactly one of:
- **SIGN_GAP** -- a type the one table signs wrongly or not at all moves this pair. The remedy is a change to `commonwealth_signs.py`, then
  the type census (`data/assets/scripts/analysis/commonwealth_tx_types.py`) and the rebuild re-run, with the snapshot still 381 of 381 equal.
  Never a per-account patch.
- **VENDOR_ROUNDING** -- the delivered quantities themselves do not net to zero (for example a sale recorded to fewer decimals than the
  buy); cite the rows.
- **SOURCE_GAP** -- a row the pair needs is not in the delivery (for example a fractional share sold or delivered out with no transaction
  row); cite what is missing and why the rows imply it.

Build `data/assets/scripts/analysis/commonwealth_residuals_explain.py`, read-only, which reads the residual list (re-derived from the
rebuild, not read from the CSV), prints each pair's rows and its class with a one-line reason, writes `RESIDUALS_EXPLAINED.md` to `--out`,
and prints as its LAST line exactly:
`RESIDUALS explained=<e> of <n> sign_gap=<a> vendor_rounding=<b> source_gap=<c>`.

**Tests** `data/assets/scripts/analysis/tests/test_commonwealth_residuals_explain.py` (stubs, no AWS): one stub pair per class is classed
correctly; a pair with no residual is not listed (the control).

### ACCEPTANCE

<criterion id="CB14n1-AC1" cell_refs="CB-n-1"><invocation>python data/assets/scripts/analysis/commonwealth_residuals_explain.py --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~30</invocation><expect>RESIDUALS explained=5 of 5</expect></criterion>
`CB14n1-AC1` -- every residual named and classed from its rows (the per-class counts on the same line are recorded, not presumed). If a
SIGN_GAP is fixed in the one table, the residual count it reports is the rebuild's after the fix, with the census and the snapshot check
re-run and recorded in the report.

<criterion id="CB14n1-AC2" cell_refs="CB-n-1"><invocation>python -m pytest -q data/assets/scripts/analysis/tests/test_commonwealth_residuals_explain.py</invocation><expect>passed</expect></criterion>
`CB14n1-AC2` -- the classing on stubs, one arm per class and the no-residual control.

<expected_criteria>CB14n1-AC1,CB14n1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scratch under `.scratch/`, uncommitted.
- **Read-only on S3.** No apply, no vendor call, no download of any kind, never bun.
- **A sign change only through `commonwealth_signs.py`**, with its reason beside the type, and only for a measured SIGN_GAP.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `ADVI_COTBKF-D2-W30-S<k>`, `"fabric": "dell2"`, a real `surfaced_at`), and do not weaken the test.

<paths>
data/assets/scripts/analysis/commonwealth_residuals_explain.py
data/assets/scripts/analysis/tests/test_commonwealth_residuals_explain.py
data/assets/scripts/silver/commonwealth_signs.py
data/assets/scripts/silver/tests/test_commonwealth_signs.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round14.md</decomp_doc> (round 14), cell `CB-n-1`.
<owned_cells>CB-n-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB14n1-AC1, CB14n1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~30/ADVI_COTBKF.TO-CB-n-1.residuals-explained.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB14n1-AC1,CB14n1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the RESIDUALS line, each pair's class and reason in one line, any sign change with its census and snapshot re-run, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a one-time read.
comp-iam: DECLARED-NOT-APPLICABLE reads under the dell2 identity on opal-data-assets; denominator 1 bucket; BLIND: none needed.
comp-adversary: RUN -- residuals re-derived from the rebuild, not read from a file; a sign fix only through the one table with the census and snapshot re-run; BLIND: corporate actions the delivery never recorded.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-13 analysis @d9877f9754, E2.
