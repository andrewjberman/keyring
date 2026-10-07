# TO ADVI_COTBKF.TO-CB-i-1 -- round 9 CB-i-1: the FWD-6 page gains a RETURNS lead line; no other lead line changes

<to_id>ADVI_COTBKF.TO-CB-i-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~25</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-i-1` (`decompositions/ADVI_COTBKF_DECOMP.round9.md`) |
**outcome_ref:** FWD-6 (CB8h1-AC3) | **depends_on:** none

---

## WORKER FACE

### THE CELL

`CB-i-1`, FWD-6: `data/assets/scripts/analysis/commonwealth_coverage_statement.py` writes `COVERAGE_STATEMENT.md`, which leads (under
its first `## ` heading) with one plain line per kind of record -- TRANSACTIONS, POSITIONS, STATEMENTS, TAX FORMS, CRM, PRICES -- each
with its own date span and count. The grader found one kind missing: **RETURNS**. Commonwealth's own performance records sit in the
applied silver table `opal_naming.address("commonwealth", <the cottonwood scope via opal_naming.lookup>, "silver", "performance",
"date=2026-06-23")`; the grader read their span as 2013-04-04 to 2026-06-23.

Add ONE lead line, `- RETURNS: ...`, placed after POSITIONS, naming what is covered (Commonwealth's own performance/returns records), its
own date span and its count (rows and accounts), all read from the applied performance table -- never typed. If any gap applies, state it
with its reason and an existing row id. **Change no other lead line.** The kinds count on the script's last line becomes 7:
`COVERAGE-STATEMENT tables=11 kinds=7 every_kind_has_own_span=<bool> every_not_covered_has_reason_and_row=<bool> rows_cited=<k> rows_missing=<m>`.

**Tests** in `data/assets/scripts/analysis/tests/test_commonwealth_coverage_statement.py`: add a test named with `returns` -- a stub
performance table of 3 rows over 2 accounts spanning two dates prints a RETURNS line with that span and count, and `kinds=7`; keep every
existing test passing (update only an expected `kinds=6` to `kinds=7`).

### ACCEPTANCE

<criterion id="CB9i1-AC1" cell_refs="CB-i-1"><invocation>python data/assets/scripts/analysis/commonwealth_coverage_statement.py --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~25</invocation><expect>COVERAGE-STATEMENT tables=11 kinds=7 every_kind_has_own_span=True every_not_covered_has_reason_and_row=True</expect></criterion>
`CB9i1-AC1` -- the page on the applied tables, with the RETURNS line.

<criterion id="CB9i1-AC2" cell_refs="CB-i-1"><invocation>python "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/checks/check_i1_lead_lines.py"</invocation><expect>returns_added=True others_unchanged=True</expect></criterion>
`CB9i1-AC2` -- against round 8's committed page: one RETURNS line added, the six other lead lines byte-equal.

<expected_criteria>CB9i1-AC1,CB9i1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scratch under `.scratch/`, uncommitted.
- **Read-only.** No S3 write. No typed bucket, key or scope name (the naming gate refuses them).
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `ADVI_COTBKF-W25-S<k>`), and do not weaken the test.

<paths>
data/assets/scripts/analysis/commonwealth_coverage_statement.py
data/assets/scripts/analysis/tests/test_commonwealth_coverage_statement.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round9.md</decomp_doc> (round 9), cell `CB-i-1`.
<owned_cells>CB-i-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB9i1-AC1, CB9i1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~25/ADVI_COTBKF.TO-CB-i-1.returns-lead-line.proof_of_spec.json`, validated
with `python .tools/proof-of-spec-check.py <instance> CB9i1-AC1,CB9i1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the RETURNS line as written, the two criterion lines, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a one-time read.
comp-iam: DECLARED-NOT-APPLICABLE reads under the dell2 identity on opal-data-assets; denominator 1 bucket; BLIND: none needed.
comp-adversary: RUN -- the span and count read from the applied table; the other six lines held byte-equal by a check file with green and red arms; BLIND: none.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-8 analysis @31b26bff2d, E1; CVO grade CB8h1-AC3.
