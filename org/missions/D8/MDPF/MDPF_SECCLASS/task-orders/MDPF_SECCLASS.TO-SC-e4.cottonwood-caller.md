# TO MDPF_SECCLASS.TO-SC-e4 -- round 2 SC-e-4: cottonwood-caller

<to_id>MDPF_SECCLASS.TO-SC-e4</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~6</issued_to>
<issued_by>2.0.0_SA_COO~M</issued_by>
<issued_date>2026-09-30</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>~M</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `SC-e-4` (`decompositions/MDPF_SECCLASS_DECOMP_R2.md`) |
**outcome_ref:** FWD-2, FWD-7 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SC-e-4`, analysis item E4 (row S2, ARMED). The round-1 backfill census found no ticker-keyed Cottonwood source
(`opal-data-cot` gold/positions_cube has no ticker column), while the IR Holdings build reads about 1,300 Cottonwood
securities with symbols. The scheduled classification module is
`infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py` (plan_rows / write; conditional put on absence),
and BD's `E_18.detect_new_securities.py` is its first caller (round 1). Cottonwood has its own
`data/cot/scripts/gold/E_18.detect_new_securities.py` in its own tree (C-FIRM).

**Build (LOCAL build + record: no table write):**
1. **Find Cottonwood's ticker-bearing holdings source** in its own tree: the one the IR Holdings COT build reads, or
   another. Name it.
2. **Wire COT's E_18** to feed its new tickers to the scheduled module the way BD's does. Keep its detection, and
   retire any bd-securities stub write it has.
3. **Tests** in `data/cot/scripts/gold/tests/test_e18_scheduled_caller.py`:
   - the caller plans only absent tickers;
   - a GLD overwrite is refused;
   - no outside model is called.
4. **Dry-run census.** Write `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R2_COT_CALLER_CENSUS_20260930.json` as `{"table_rows_at_build", "firm":
   "cottonwood", "source", "held_tickers", "already_present", "seed_pending", "would_write", "unresolved": [...],
   "overwrites": 0, "vendor_calls": 0, "rows": [...]}`.

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

<criterion id="SC2-e4-AC1" cell_refs="SC-e-4"><invocation>python -m pytest data/cot/scripts/gold/tests/test_e18_scheduled_caller.py -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
`SC2-e4-AC1` -- absent-only planning, GLD refused, no outside model.

<criterion id="SC2-e4-AC2" cell_refs="SC-e-4"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R2_CHECKS/r2_evidence.py cot</invocation><expect>COT-CALLER</expect></criterion>
`SC2-e4-AC2` -- a ticker-keyed Cottonwood dry run: every held ticker accounted for.

<expected_criteria>SC2-e4-AC1,SC2-e4-AC2</expected_criteria>

Dry-run at the base 2026-09-30 03:1xZ (@30727a9413): SC2-e4-AC1 no tests ran; SC2-e4-AC2 NOT-MET (evidence absent) -- FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Build scaffolding goes under
  `.scratch/`, uncommitted.
- **LOCAL build + record.** No table write (dry-run only), no upload, no deploy, no IAM apply, no outside-model call.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W6-S<k>`), and do not weaken the test to pass.

<paths>
data/cot/scripts/gold/E_18.detect_new_securities.py
data/cot/scripts/gold/tests/test_e18_scheduled_caller.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R2_COT_CALLER_CENSUS_20260930.json
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R2.md</decomp_doc> (round 2), cell `SC-e-4`.
<owned_cells>SC-e-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC2-e4-AC1, SC2-e4-AC2. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~6/MDPF_SECCLASS.TO-SC-e4.cottonwood-caller.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC2-e4-AC1,SC2-e4-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the source named, the caller change, the census (held, present, would-write, unresolved), the pytest line, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched
comp-iam: DECLARED-NOT-APPLICABLE -- no grant is changed
comp-adversary: RUN -- 1 analysis read (ROUND1_ANALYSIS_MDPF_SECCLASS_20260930.md @151c890591, item E4), 1 table read (etf-classifications 2,309 rows after release step 2); BLIND: the inputs this cell names or measures are unmeasured at the cut (its census measures them).
lane: the <paths> block IS the grant.
</preflight>

Source: CTO round-1 analysis @151c890591 (msg 103116), item E4; Andrew-direct 2026-09-30 ~02:2xZ.
