# TO MDPF_SECCLASS.TO-SC-e1 -- round 2 SC-e-1: contract-and-legacy-label

<to_id>MDPF_SECCLASS.TO-SC-e1</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~5</issued_to>
<issued_by>2.0.0_SA_COO~M</issued_by>
<issued_date>2026-09-30</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>~M</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `SC-e-1` (`decompositions/MDPF_SECCLASS_DECOMP_R2.md`) |
**outcome_ref:** FWD-4, FWD-7 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SC-e-1`, analysis item E1. The CTO's C-WRITER ruling makes `classified_by` a four-value set. 238 live rows carry no
label: the ones written before the contract.

**Build (LOCAL build + record: no table write):**
1. **Contract.** `org/standards/MDPF_SECCLASS_CONTRACT.json` goes to `contract_version` `0.2.0`. `classified_by.values`
   becomes `["seed", "scheduled", "constituents", "legacy"]`, each with the definition the ruling gives, plus the
   precedence rule (`seed` wins; `scheduled` and `constituents` write only where no row exists; a missing label reads
   as `legacy`). Keep the rule-24 record current.
2. **Constituents seeder.** `infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-constituents.py` sets
   `classified_by = "constituents"` on every row it writes. Its condition stays: the row does not exist, or carries no
   label.
3. **The legacy label.** A new script, `infra/aws/lambda/v2_portal/yang_pipeline/label-legacy-classified-by.py`, does
   ONE additive conditional update per unlabelled row: `SET classified_by = legacy` on
   `attribute_not_exists(classified_by)`, touching no other attribute, with `--dry-run`. Run it in dry-run only.
4. **Tests** in `infra/aws/lambda/v2_portal/_shared/tests/test_classified_by_v2.py`:
   - the contract lists the four values;
   - the constituents seeder labels its rows `constituents`;
   - the label update touches only `classified_by`, and a labelled row is refused.
5. **Census and half.** Write `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R2_LABEL_CENSUS_20260930.json` as `{"table_rows_at_build", "contract_version":
   "0.2.0", "classified_by_values": [...], "unlabelled_rows", "would_label", "other_attributes_touched": 0,
   "overwrites": 0}`. Write the half `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_LEGACY_LABEL_20260930.md` for the label
   write (the rows, the readers of `classified_by`, rollback by `REMOVE classified_by` per written key).

**Standing rulings (carried from the round-2 decomposition):**
- Andrew-direct 2026-09-30 ~02:2xZ: "yes, bd-securities values can seed new rows. THey just don't overwrite existing rows."
  So a bd-securities value may seed a NEW row and never writes into an EXISTING one. A write to an existing row from a
  bd-securities value is outside his word: stop, and name it in the half for his decision.
- CTO C-WRITER ruling (analysis @151c890591, section 1): `classified_by` is `seed` / `scheduled` / `constituents` /
  `legacy`; `seed` always wins; `scheduled` and `constituents` write only where no row exists; a missing label reads as
  `legacy`.
- The live `etf-classifications` holds 2,309 rows (release step 2, ledger CLOSED @f13cddd058). Read and print its row
  count at build time as `table_rows_at_build` in your evidence file.

### ACCEPTANCE

<criterion id="SC2-e1-AC1" cell_refs="SC-e-1"><invocation>python -m pytest infra/aws/lambda/v2_portal/_shared/tests/test_classified_by_v2.py -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
`SC2-e1-AC1` -- four values, constituents labelled, the label update additive only.

<criterion id="SC2-e1-AC2" cell_refs="SC-e-1"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R2_CHECKS/r2_evidence.py label</invocation><expect>LABEL-CENSUS</expect></criterion>
`SC2-e1-AC2` -- the dry-run label census: every unlabelled row, nothing else touched.

<criterion id="SC2-e1-AC3" cell_refs="SC-e-1"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_CHECKS/r20_half_ready.py org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_LEGACY_LABEL_20260930.md</invocation><expect>HALF-READY</expect></criterion>
`SC2-e1-AC3` -- the label write's half.

<expected_criteria>SC2-e1-AC1,SC2-e1-AC2,SC2-e1-AC3</expected_criteria>

Dry-run at the base 2026-09-30 03:1xZ (@30727a9413): SC2-e1-AC1 no tests ran; SC2-e1-AC2 NOT-MET (evidence absent); SC2-e1-AC3 NOT-READY -- FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Build scaffolding goes under
  `.scratch/`, uncommitted.
- **LOCAL build + record.** No table write (dry-run only), no upload, no deploy, no IAM apply, no outside-model call.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W5-S<k>`), and do not weaken the test to pass.

<paths>
org/standards/MDPF_SECCLASS_CONTRACT.json
infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-constituents.py
infra/aws/lambda/v2_portal/yang_pipeline/label-legacy-classified-by.py
infra/aws/lambda/v2_portal/_shared/tests/test_classified_by_v2.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R2_LABEL_CENSUS_20260930.json
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_LEGACY_LABEL_20260930.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R2.md</decomp_doc> (round 2), cell `SC-e-1`.
<owned_cells>SC-e-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC2-e1-AC1, SC2-e1-AC2, SC2-e1-AC3. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~5/MDPF_SECCLASS.TO-SC-e1.contract-and-legacy-label.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC2-e1-AC1,SC2-e1-AC2,SC2-e1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the contract diff, the seeder change, the label census, the pytest line, the half's path, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched
comp-iam: DECLARED-NOT-APPLICABLE -- no grant is changed
comp-adversary: RUN -- 1 analysis read (ROUND1_ANALYSIS_MDPF_SECCLASS_20260930.md @151c890591, item E1), 1 table read (etf-classifications 2,309 rows after release step 2); BLIND: the inputs this cell names or measures are unmeasured at the cut (its census measures them).
lane: the <paths> block IS the grant.
</preflight>

Source: CTO round-1 analysis @151c890591 (msg 103116), item E1; Andrew-direct 2026-09-30 ~02:2xZ.
