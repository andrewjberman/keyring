# TO MDPF_SECCLASS.TO-SC-e5 -- round 2 SC-e-5: advisor-positions-canonical

<to_id>MDPF_SECCLASS.TO-SC-e5</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~7</issued_to>
<issued_by>2.0.0_SA_COO~M</issued_by>
<issued_date>2026-09-30</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>~M</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `SC-e-5` (`decompositions/MDPF_SECCLASS_DECOMP_R2.md`) |
**outcome_ref:** FWD-4, FWD-2 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SC-e-5`, analysis item E5 (row W3-S3). `data/black_diamond/scripts/gold/D_04.client_portal_summary.py`
`build_advisor_positions` (:2705) carries its own `_classify_ticker` closure (:2766), a fourth classify site outside
the one library, and writes `platinum/advisors/{id}/positions.json` (:2888). Its wire contract is in
`docs/architecture/ADVI_49EXEC.md`. Round 1 moved the rest of D_04 onto the library (`lib/etf_classifier.py`, which
reads etf-classifications through the one client).

**Build (LOCAL build + record: no upload, no deploy):**
1. `_classify_ticker` goes, and positions classify through the library: canonical class and sub-class, no fold, no
   guess, unknown unclassified by name.
2. **positions.json.** Add `asset_class_canonical`, `sub_asset_class_canonical` and `class_source` only if the wire
   contract admits additive fields. Read ADVI_49EXEC.md; do not edit it. If it does not admit them, keep the shape,
   change only the values' source, and say so.
3. **Tests** in `data/black_diamond/scripts/gold/tests/test_advisor_positions_canonical.py`.
4. **Census** from a REAL local build of the positions artifacts on the latest BD day. Write
   `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R2_POSITIONS_CENSUS_20260930.json` as `{"table_rows_at_build", "rows", "class_sources", "guessed": 0,
   "unclassified", "unclassified_names", "contract_additive": true|false}`. If the contract forbids additive fields,
   `contract_additive` is false and the check fails: file a row and stop there, rather than changing the contract.

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

<criterion id="SC2-e5-AC1" cell_refs="SC-e-5"><invocation>python -m pytest data/black_diamond/scripts/gold/tests/test_advisor_positions_canonical.py -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
`SC2-e5-AC1` -- positions classify through the one library.

<criterion id="SC2-e5-AC2" cell_refs="SC-e-5"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R2_CHECKS/r2_evidence.py positions</invocation><expect>POSITIONS-CENSUS</expect></criterion>
`SC2-e5-AC2` -- a real positions build sourced from the canonical table, additive to its contract.

<expected_criteria>SC2-e5-AC1,SC2-e5-AC2</expected_criteria>

Dry-run at the base 2026-09-30 03:1xZ (@30727a9413): SC2-e5-AC1 no tests ran; SC2-e5-AC2 NOT-MET (evidence absent) -- FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Build scaffolding goes under
  `.scratch/`, uncommitted.
- **LOCAL build + record.** No table write (dry-run only), no upload, no deploy, no IAM apply, no outside-model call.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W7-S<k>`), and do not weaken the test to pass.

<paths>
data/black_diamond/scripts/gold/D_04.client_portal_summary.py
data/black_diamond/scripts/gold/tests/test_advisor_positions_canonical.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R2_POSITIONS_CENSUS_20260930.json
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R2.md</decomp_doc> (round 2), cell `SC-e-5`.
<owned_cells>SC-e-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC2-e5-AC1, SC2-e5-AC2. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~7/MDPF_SECCLASS.TO-SC-e5.advisor-positions-canonical.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC2-e5-AC1,SC2-e5-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the change, the contract reading, the census, the pytest line, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched
comp-iam: DECLARED-NOT-APPLICABLE -- no grant is changed
comp-adversary: RUN -- 1 analysis read (ROUND1_ANALYSIS_MDPF_SECCLASS_20260930.md @151c890591, item E5), 1 table read (etf-classifications 2,309 rows after release step 2); BLIND: the inputs this cell names or measures are unmeasured at the cut (its census measures them).
lane: the <paths> block IS the grant.
</preflight>

Source: CTO round-1 analysis @151c890591 (msg 103116), item E5; Andrew-direct 2026-09-30 ~02:2xZ.
