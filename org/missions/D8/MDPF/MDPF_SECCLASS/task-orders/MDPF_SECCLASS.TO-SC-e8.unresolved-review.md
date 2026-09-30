# TO MDPF_SECCLASS.TO-SC-e8 -- round 2 SC-e-8: unresolved-review

<to_id>MDPF_SECCLASS.TO-SC-e8</to_id>
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

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `SC-e-8` (`decompositions/MDPF_SECCLASS_DECOMP_R2.md`) |
**outcome_ref:** FWD-2, FWD-7 | **depends_on:** SC-e-6 (queued on slot ~7)

---

## WORKER FACE

### THE CELL

`SC-e-8`, analysis item E8. The round-1 backfill census left 884 names unresolved (bd 207, 49financial 601,
inflection 76), each listed by name in `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R1_BACKFILL_CENSUS_20260929.json` (`unresolved`). Most had only a fold
value in bd-securities, or no ticker.

**Build (LOCAL record only: no table write, no seed-source edit):**
1. **Review each name.** Give either a proposed canonical class (asset_class, sub_asset_class, instrument_kind) WITH
   the evidence source (an existing estate field, a Bloomberg or Schwab field, or the security's own registry name),
   or a stated reason it cannot be classified from held sources. The reason may be: cash or a sweep, a bond with no
   ticker, a private fund, a fold-only value, a delisted security, or other. No outside model, and no guess presented
   as a class.
2. Write `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R2_UNRESOLVED_REVIEW_20260930.json` as `{"table_rows_at_build", "denominator": 884, "entries":
   [{"firm", "name", "ticker", "proposed_class": {...} | null, "source", "reason"}]}`, where every entry has a class
   or a reason. Landing the proposed classes is a later seed-source act.

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

<criterion id="SC2-e8-AC1" cell_refs="SC-e-8"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R2_CHECKS/r2_evidence.py unresolved</invocation><expect>REVIEW-COMPLETE</expect></criterion>
`SC2-e8-AC1` -- all 884 names reviewed: a sourced class or a stated reason each.

<expected_criteria>SC2-e8-AC1</expected_criteria>

Dry-run at the base 2026-09-30 03:1xZ (@30727a9413): SC2-e8-AC1 NOT-MET (evidence absent) -- FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Build scaffolding goes under
  `.scratch/`, uncommitted.
- **LOCAL build + record.** No table write (dry-run only), no upload, no deploy, no IAM apply, no outside-model call.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W7-S<k>`), and do not weaken the test to pass.

<paths>
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R2_UNRESOLVED_REVIEW_20260930.json
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R2.md</decomp_doc> (round 2), cell `SC-e-8`.
<owned_cells>SC-e-8</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC2-e8-AC1. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~7/MDPF_SECCLASS.TO-SC-e8.unresolved-review.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC2-e8-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** the review counts (classed, by reason), the sources used, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched
comp-iam: DECLARED-NOT-APPLICABLE -- no grant is changed
comp-adversary: RUN -- 1 analysis read (ROUND1_ANALYSIS_MDPF_SECCLASS_20260930.md @151c890591, item E8), 1 table read (etf-classifications 2,309 rows after release step 2); BLIND: the inputs this cell names or measures are unmeasured at the cut (its census measures them).
lane: the <paths> block IS the grant.
</preflight>

Source: CTO round-1 analysis @151c890591 (msg 103116), item E8; Andrew-direct 2026-09-30 ~02:2xZ.
