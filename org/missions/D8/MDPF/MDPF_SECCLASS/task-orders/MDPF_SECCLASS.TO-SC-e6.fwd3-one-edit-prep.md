# TO MDPF_SECCLASS.TO-SC-e6 -- round 2 SC-e-6: fwd3-one-edit-prep

<to_id>MDPF_SECCLASS.TO-SC-e6</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~7</issued_to>
<issued_by>2.0.0_SA_COO~M</issued_by>
<issued_date>2026-09-30</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>~M</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `SC-e-6` (`decompositions/MDPF_SECCLASS_DECOMP_R2.md`) |
**outcome_ref:** FWD-3 | **depends_on:** SC-e-5 (queued on slot ~7)

---

## WORKER FACE

### THE CELL

`SC-e-6`, analysis item E6. FWD-3: "A person corrects or adds a security in one place, and every screen shows the
change after its next ordinary run". The CVO asks that the exercise use a ticker the fork had wrong, which shows
`seed` beats `scheduled`.

**Build (LOCAL build + record: no seed run, no deploy):**
1. **Pick ONE ticker** that has a `classified_by = scheduled` row seeded from a bd-securities value that is WRONG by
   the canonical vocabulary: a fund carried as equity, a fold-adjacent sub-asset, or similar. State the evidence that
   it is wrong, never your guess.
2. **Correct it once** in the seed source `infra/aws/lambda/v2_portal/_shared/etf_classification.py`, adding the
   ticker with its correct class, sub-asset, instrument_kind and name, the way GLD sits. The next seed run replaces
   the scheduled row with `classified_by = seed`.
3. **Plan.** Write `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R2_FWD3_PLAN_20260930.json` as `{"table_rows_at_build", "ticker", "fork_value",
   "current_row", "seed_value", "surfaces": [<every FWD-2 surface that shows this ticker today, with where it is
   read>]}`.
4. **Half.** Write `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_FWD3_20260930.md` for the seed run that lands the
   correction, with the per-surface read after each surface's next ordinary run as the acceptance.

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

<criterion id="SC2-e6-AC1" cell_refs="SC-e-6"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R2_CHECKS/r2_evidence.py fwd3</invocation><expect>FWD3-PLAN</expect></criterion>
`SC2-e6-AC1` -- a scheduled ticker the fork had wrong, corrected once in the seed source, the surfaces named.

<criterion id="SC2-e6-AC2" cell_refs="SC-e-6"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_CHECKS/r20_half_ready.py org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_FWD3_20260930.md</invocation><expect>HALF-READY</expect></criterion>
`SC2-e6-AC2` -- the correction's half.

<expected_criteria>SC2-e6-AC1,SC2-e6-AC2</expected_criteria>

Dry-run at the base 2026-09-30 03:1xZ (@30727a9413): SC2-e6-AC1 NOT-MET (evidence absent); SC2-e6-AC2 NOT-READY -- FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Build scaffolding goes under
  `.scratch/`, uncommitted.
- **LOCAL build + record.** No table write (dry-run only), no upload, no deploy, no IAM apply, no outside-model call.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W7-S<k>`), and do not weaken the test to pass.

<paths>
infra/aws/lambda/v2_portal/_shared/etf_classification.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R2_FWD3_PLAN_20260930.json
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_FWD3_20260930.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R2.md</decomp_doc> (round 2), cell `SC-e-6`.
<owned_cells>SC-e-6</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC2-e6-AC1, SC2-e6-AC2. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~7/MDPF_SECCLASS.TO-SC-e6.fwd3-one-edit-prep.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC2-e6-AC1,SC2-e6-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the ticker and its evidence, the seed-source line, the surfaces, the half's path, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched
comp-iam: DECLARED-NOT-APPLICABLE -- no grant is changed
comp-adversary: RUN -- 1 analysis read (ROUND1_ANALYSIS_MDPF_SECCLASS_20260930.md @151c890591, item E6), 1 table read (etf-classifications 2,309 rows after release step 2); BLIND: the inputs this cell names or measures are unmeasured at the cut (its census measures them).
lane: the <paths> block IS the grant.
</preflight>

Source: CTO round-1 analysis @151c890591 (msg 103116), item E6; Andrew-direct 2026-09-30 ~02:2xZ.
