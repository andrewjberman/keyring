# TO MDPF_SECCLASS.TO-SC-e64 -- round 10 SC-e-64: PRD v0.14 / ruling 2.4: Cash is a sub-class of cash only; the constituents seeder's CASH row and the contract follow

<to_id>MDPF_SECCLASS.TO-SC-e64</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~45</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>10</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL1) | **Decomp cell:** `SC-e-64` (`decompositions/MDPF_SECCLASS_DECOMP_R10.md`) |
**outcome_ref:** FWD-17, FWD-2 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SC-e-64`. CTO round-9 analysis ruling 2.4 (PRD ADDENDUM v0.14): "`Cash` is a sub-class of `cash` only. `fixed_income` carries no `Cash`
sub-class, and a screen that folds cash into fixed income states it as its FWD-16 mapping. The canonical `CASH` row
(`fixed_income/UltraShortDuration`, `legacy`, read live 12:5xZ) is corrected to `cash` through the seed source."

**Measured at the base:**
- The seed source is `infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-constituents.py`. Its
  `build_row("CASH", "Cash & Cash Equivalents", "Fixed Income", "Ultra Short Duration", ts)` returns `fixed_income/Ultra Short Duration`.
- The contract `org/standards/MDPF_SECCLASS_CONTRACT.json` `fields.sub_asset_class.values_by_class` lists `Cash` under both `cash`
  (`[Cash, Money Market, T-Bill]`) and `fixed_income`.
- The tests that build the CASH row: `infra/aws/lambda/v2_portal/_shared/tests/test_seed_fields.py` (~:129-134) and
  `infra/aws/lambda/v2_portal/_shared/tests/test_classified_by_v2.py` (~:269).

**Build:**
1. The seeder maps the CASH residual line (the ticker `CASH`, and `CASH_USD` if it is treated the same way) to `asset_class` `cash` and
   `sub_asset_class` `Cash`, whatever class and sub-class the feed gives it. Every other row is unchanged: a money-market fund (SALXX) keeps
   its mapping.
2. The contract drops `Cash` from `values_by_class.fixed_income`. Note the change in that field's `source_by_class` or `rule24_record`,
   citing PRD v0.14, and bump the contract's version by one minor step.
3. Update the CASH assertions in the two test files to the new class. Every pin test of the contract that reads the fixed_income list is
   updated to the new list, not removed.

### ACCEPTANCE

<criterion id="SC10-e64-AC1" cell_refs="SC-e-64"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R12_CHECKS/sc_e64_cash_row.py</invocation><expect>SC-E64 ok=True</expect></criterion>
`SC10-e64-AC1` -- the seeder's CASH row is `cash/Cash`, the contract lists Cash under cash only, and SALXX does not move (control).

<criterion id="SC10-e64-AC2" cell_refs="SC-e-64"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/r10_pytest_ok.py infra/aws/lambda/v2_portal/_shared/tests/test_seed_fields.py infra/aws/lambda/v2_portal/_shared/tests/test_classified_by_v2.py</invocation><expect>PYTEST-OK</expect></criterion>
`SC10-e64-AC2` -- the two seed and contract test files pass under the new rule. At the base they are a control (45 passed under the old
rule); your edits make them the build check.

<expected_criteria>SC10-e64-AC1,SC10-e64-AC2</expected_criteria>

Dry-run at the base (277fc76bc2, 2026-10-07): SC10-e64-AC1 FAIL as expected (`cash_row=fixed_income/Ultra Short Duration contract_cash_in_fixed_income=True`); SC10-e64-AC2 PASS as expected (control, 45 passed).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, bun install, curl or tool fetch, into any environment;
  rows S49, S54).
- No table write and no seeder run against AWS. The live CASH row's correction is an issuer act under its own pair (condition 5 of the
  SC-e-42 half). No deploy. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W45-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test.

<paths>
infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-constituents.py
org/standards/MDPF_SECCLASS_CONTRACT.json
infra/aws/lambda/v2_portal/_shared/tests/test_seed_fields.py
infra/aws/lambda/v2_portal/_shared/tests/test_classified_by_v2.py
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R10.md</decomp_doc> (round 10), cell `SC-e-64`.
<owned_cells>SC-e-64</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC10-e64-AC1, SC10-e64-AC2. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~45/MDPF_SECCLASS.TO-SC-e64.cash-subclass-of-cash-only.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC10-e64-AC1,SC10-e64-AC2` BEFORE the flip. A judgment criterion is recorded
`UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming 3.0.0_SA_CVO, never PASS or FAIL.
</proof_of_spec>

**REPORT:** the seeder rule before and after, the contract diff and version, each test assertion changed, AC1/AC2 outputs, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the seeder is run by hand under a pair; no schedule changes.
comp-iam: DECLARED-NOT-APPLICABLE no role or grant changes.
comp-adversary: RUN -- a fold that moves money-market funds too (AC1's SALXX control); a pin test removed instead of re-stated (refusal clause); BLIND: the live CASH row (the issuer's write under its pair).
lane: the <paths> block IS the grant.
</preflight>

Source: round-9 analysis @9b6348f15e section 2.4, section 3 item 6; PRD ADDENDUM v0.14; DECOMP_R10.
