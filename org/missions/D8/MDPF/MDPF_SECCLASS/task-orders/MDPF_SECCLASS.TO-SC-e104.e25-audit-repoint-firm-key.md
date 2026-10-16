# TO MDPF_SECCLASS.TO-SC-e104.e25-audit-repoint-firm-key -- round 26 SC-e-104: E_25 reads the key C_06 writes (`firm`), so the audit stops erroring on every run (row W92-S4)

<to_id>MDPF_SECCLASS.TO-SC-e104</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~94</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>26</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SC-e-104` (`decompositions/MDPF_SECCLASS_DECOMP_R26.md`) |
**outcome_ref:** FWD-1 (instrument hygiene, W92-S4) | **depends_on:** none | **source:** CTO round-25 analysis section 2 item 2; row MDPF_SECCLASS-D1-W92-S4

---

## WORKER FACE

### THE CELL

`SC-e-104`. `data/black_diamond/scripts/gold/E_25.aua_decomposition_audit.py`, function `load_mix_summary_latest` (about lines 130-167), reads `summary.get('firm_daily', {})` from `gold/views/mix_daily_summary.json`. No writer produces that key: C_06 writes `{'firm': ..., 'advisors': ..., 'restated_through': ...}`, so the function returns `{'error': 'firm_daily key missing from mix_daily_summary'}` on every run (row `MDPF_SECCLASS-D1-W92-S4`). E_25 is in no gold chain and no infrastructure; the repo copy is the record, so nothing is deployed. **Ruling (the issuer's): REPOINT, not retire.** The row for one firm date is `{'equity': ..., 'fixed_income': ..., 'alternatives': ..., 'commodities': ..., 'structured': ..., 'cash': ..., 'unclassified': ..., 'other': ..., 'total': ...}` (class dollars plus `total`).

**What you build:**
1. In `load_mix_summary_latest`: read `summary.get('firm', {})`; error text `'firm key missing from mix_daily_summary'` when it is empty.
2. Keep every key the function returns today (`date`, `equity`, `fixed_income`, `alternatives`, `total`, `pct`, `note`) and ADD `classes`: a dict of EVERY class in the row except `total`, value rounded to 2 places. Add to `pct` the percentage (2 places, of `total`) of every class in `classes`, not only the three. Replace the `note` text, which says cash is classified as fixed income and there is no Cash or Other bucket (false now): say that the classes are exactly those C_06 publishes, with cash and unclassified as their own classes.
3. Read every caller of `load_mix_summary_latest` inside E_25 and keep each working (the test below covers the function; report each caller with file:line).
4. A new test file `data/black_diamond/scripts/gold/tests/test_e25_firm_key_r26.py` that loads E_25 without side effects (read how a sibling test in that folder loads a gold script; stub the S3 client with an object whose `get_object` returns the JSON bytes) and shows: (a) a summary with `firm` for three dates returns the LATEST date's classes, `total` and a `pct` that covers every class; (b) the DIFFERENCE CONTROL: a summary that carries only the OLD key `firm_daily` returns the `error` result, so the test can tell the two apart; (c) an empty `firm` returns the error; (d) the `note` no longer contains the words `Cash/sweep classified as fixed_income`.
Do not touch any other file.

### ACCEPTANCE

<criterion id="SC26-e104-AC1" cell_refs="SC-e-104"><invocation>python -m pytest data/black_diamond/scripts/gold/tests/test_e25_firm_key_r26.py -q --tb=short</invocation><expect>passed</expect></criterion>
`SC26-e104-AC1` -- the new test passes, including the difference control (b).

<criterion id="SC26-e104-AC2" cell_refs="SC-e-104"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R26_CHECKS/check_e25_real_body.py</invocation><expect>E25-REAL ok=True</expect></criterion>
`SC26-e104-AC2` -- the repointed function reads a committed copy of a REAL C_06 body (2,297 firm dates) and returns its latest date with every non-zero class.

<expected_criteria>SC26-e104-AC1, SC26-e104-AC2</expected_criteria>

Dry-run at the base (dell1 box/dell1 HEAD, 2026-10-16 ~03:5xZ): AC1 FAILS as expected (the test file is absent); AC2 FAILS as expected (`E25-REAL ok=False error=firm_daily key missing from mix_daily_summary`).

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, curl or tool fetch). pandas, pyarrow and boto3 are already installed.
- **No AWS call of any kind.** Nothing is deployed.
- **Never edit** anything outside the `<paths>` block; the check scripts under `R26_CHECKS/` are READ-ONLY to you. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and file a surprise row (id `MDPF_SECCLASS-D1-W94-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing). Do not weaken a check, and do not edit a check to make it pass.
- Run every invocation under `timeout 120`; the checks end well inside it.

<paths>
data/black_diamond/scripts/gold/E_25.aua_decomposition_audit.py
data/black_diamond/scripts/gold/tests/test_e25_firm_key_r26.py
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R26.md</decomp_doc> (round 26), cell `SC-e-104`.
<owned_cells>SC-e-104</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC26-e104-AC1, SC26-e104-AC2. Write the instance at
`org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~94/MDPF_SECCLASS.TO-SC-e104.e25-audit-repoint-firm-key.proof_of_spec.json`.
Validate it BEFORE the flip with `python .tools/proof-of-spec-check.py <instance> SC26-e104-AC1,SC26-e104-AC2`.
</proof_of_spec>

**REPORT:** the exact diff of E_25 (it must stay inside `load_mix_summary_latest` and its note), each criterion's output verbatim, each caller with file:line, commits, rows.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE nothing is scheduled; nothing ships.
comp-iam: DECLARED-NOT-APPLICABLE only the reads the seat's role already makes.
comp-adversary: RUN -- a test that passes with the old key (the difference control (b) must show the old key errors); a repoint that returns only three classes while the row carries seven (AC2 compares the class set); a change that reaches beyond the function (the issuer reads the diff). BLIND: whether anything outside the repo runs E_25 by hand (it is in no chain).
lane: the <paths> block IS the grant.
</preflight>

Source: CTO round-25 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_25_20261016.md`, msg 6457); DECOMP_R26.
