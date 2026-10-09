# TO MDPF_STRATID.TO-ST-u1 -- round 2 ST-u-1: every Cottonwood sleeve is counted once at Global or held out by name; one member on two bases validates per firm
<to_id>MDPF_STRATID.TO-ST-u1</to_id>
<project>MDPF_STRATID</project>
<issued_to>0.9.0_WK_MDPF_STRATID~7</issued_to>
<issued_by>2.0.0_SA_COO~S1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
**Directive:** D8 | **Fabric:** laptop (placement dell1) | **Decomp cell:** `ST-u-1` (`decompositions/MDPF_STRATID_DECOMP_R2.md`) |
**outcome_ref:** FWD-2 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`ST-u-1`. FWD-2 says every Cottonwood strategy outside its Models is added to Global, in the same group, once. Round 1 added Cottonwood's
PFDE sleeve to Global through a per-firm basis registry and a fold. Two gaps remain:

1. **Cottonwood has no population row.** Its other sleeves (today `divz`, 1,369,280.57 on 2026-10-08) get basis None and are
   dropped silently, with no record.
2. **A member can sit on two bases at Global.** 49financial's `divz` is a carve-out (inside Global already), while Cottonwood's
   would be additive. The Global category tree validates ONE basis per (member, scope), so the build raises `SystemExit` the first
   day a Cottonwood divz dollar is counted.

You close both. The rulings are fixed by the decomposition (R1, R2, R4 below); you implement them.

**The estate, read at the base (all paths are under the worktree root).**
- `data/mdpf/scripts/gold/mdpf_category_registry.py`:
  - `SMA_MEMBERS` (:342-369), `SMA_BASIS_BY_SCOPE` (:381-387), `SMA_FIRM_POPULATION` (:399-401, only `49financial: inside`),
    `SMA_BASIS_AT_GLOBAL_BY_FIRM` (:405-407, only `("pfde","cottonwood"): additive`);
  - `sma_global_basis_of(member, firm)` (:469-483): row, else firm default (outside -> additive, inside -> carve_out), else None;
  - `sma_basis_of(member, scope)` (:486-494).
- `data/mdpf/scripts/gold/mdpf_gold_consolidator.py`:
  - the tree `_shape_category_views(ts_doc, scope)` (~:610). Its basis check is at :778-786 ("Two declarations of the same fact
    disagree") and :793-801;
  - `apply_sma_sleeve_overlay(arts)` (~:1760-1880). It folds only an exact `additive` result (:1794), withholds `OVERLAP` and
    `OVERLAP_UNMEASURED` (:1846-1850), and writes Global `by_model[member]` with `firms` (:1863-1877).
- **How Global keys 49financial's sleeves.** Global's served `by_model` carries them as `opal_div_sma` (tree member `divz`) and
  `opal_growth_sma` (tree member `pfoe`), with no `firms`. Read how the tree maps a by_model key to a member id before you build.
- **Round 1's tests** live in `data/mdpf/tests/stratid/test_stratid_global_fold.py`. Its `test_undeclared_firm_member_not_counted`
  uses Cottonwood as the undeclared firm.

**Rulings you implement (decomposition R1, R2, R4):**
- **R1, per-firm validation.**
  - A Global `by_model` SMA entry that carries `firms` validates against `sma_global_basis_of(member, firm)` for each listed firm.
    An entry without `firms` validates as today, against `sma_basis_of(member, "global")`.
  - The tree shows ONE member row per member id. Its `aum` is the sum of the counted dollars of every entry mapping to it, for
    example 49financial's `opal_div_sma` plus Cottonwood's additive `divz`.
  - The row carries `by_firm: [{"firm_id", "basis", "value"}]`, where `firm_id` is `49financial` for an entry with no `firms` at
    Global.
  - Only additive parts are added to Global's total, exactly as round 1 adds PFDE.
  - **Key-collision hazard.** If Cottonwood's additive `divz` and 49financial's carve-out share a by_model key in any path, the
    later write must never overwrite the earlier one.
- **R2, held out.** An additive member whose counted value on a date is 0.0 (value equals overlap) adds nothing that date and is named
  in `sma_additive_withheld` with reason `OVERLAP` and the overlap value. Every Cottonwood `cohort_class: "sma"` member is either
  counted or named withheld on every Global date it has a value. None is dropped silently.
- **R4, the round-1 test.** `test_undeclared_firm_member_not_counted` keeps its name and intent. Re-point it to a firm that is still
  undeclared (`inflection`). Weaken no other round-1 test.

**Build:**
1. In the registry, set `SMA_FIRM_POPULATION["cottonwood"] = "outside"`. Keep the `("pfde","cottonwood")` override. Comment it with
   the PRD reference "C-BASIS; decomposition R2 R1".
2. In the consolidator, implement R1 and R2 above. Change nothing in `apply_taxsma_overlay`'s behaviour.
3. Create NEW tests in `data/mdpf/tests/stratid/test_stratid_round2_firm_basis.py`, with its own sys.path preamble, synthetic docs
   and no network, using these exact names:
   - `test_cottonwood_declared_outside`
   - `test_fully_overlapped_member_held_out_by_name_not_added`
   - `test_two_basis_member_validates_per_firm`: 49financial carve-out `opal_div_sma` plus Cottonwood additive `divz` with overlap
     0, in one Global doc. The tree shapes, the `divz` row sums both, the total rises by Cottonwood's part only, and `by_firm` names
     both.
   - `test_zero_overlap_member_counted_in_its_bucket`
   - `test_undeclared_firm_still_not_counted`
4. Re-point the round-1 test per R4.

### ACCEPTANCE

<criterion id="ST2-u1-AC1" cell_refs="ST-u-1"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_STRATID_S1/R2_CHECKS/st_u1_tests.py</invocation><expect>U1-OK</expect></criterion>
`ST2-u1-AC1` -- the five named tests pass.

<criterion id="ST2-u1-AC2" cell_refs="ST-u-1"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_STRATID_S1/R2_CHECKS/st_u1_seam.py</invocation><expect>SEAM-OK</expect></criterion>
`ST2-u1-AC2` -- the seam probe on real data (read-only S3). Cottonwood is declared outside. Arm A: with the served slice folded into
Global's pre-fold doc, every Cottonwood sma member is counted or named withheld, and the tree shapes. Arm B: with Cottonwood divz's
overlap planted at 0, the tree's Dividend SMA equals 49financial's plus Cottonwood's, the total rises by exactly Cottonwood's divz, and
Client does not move.

<criterion id="ST2-u1-AC3" cell_refs="ST-u-1"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_STRATID_S1/R2_CHECKS/st_u1_regress.py</invocation><expect>U1-REGRESS-OK</expect></criterion>
`ST2-u1-AC3` -- round 1's seven Global-fold tests and the TaxSMA check still pass.

<expected_criteria>ST2-u1-AC1 ST2-u1-AC2 ST2-u1-AC3</expected_criteria>

Run each invocation from the worktree root. At the base (2026-10-09 ~16:08Z):
- AC1: `U1-BAD no file ...`
- AC2: `SEAM-BAD arm=build SMA_FIRM_POPULATION['cottonwood'] = None, want 'outside'`
- AC3: `U1-REGRESS-OK`

## AMENDMENT 1 (issuer 2.0.0_SA_COO~S1, 2026-10-09 ~16:4xZ) -- rulings on rows D1-W7-S1..S4; one re-point owed

The issuer re-ran all six R2 checks and the stratid suite on `c95ee45507`. All six checks pass; the suite reads 1 failed, 24 passed.

- **S1 (the failure): R4 is extended to `data/mdpf/tests/stratid/test_stratid_basis.py`, now granted in `<paths>`.**
  - `test_undeclared_firm_population_is_not_counted` keeps its name and its `inflection` half unchanged.
  - Its Cottonwood half asserted round 1's state. Delete that half, and assert the declared state in its place:
    - `SMA_FIRM_POPULATION["cottonwood"] == "outside"`;
    - `sma_global_basis_of("divz", "cottonwood") == additive`.
  - Edit no other test.
  - Criterion: `python -m pytest -q data/mdpf/tests/stratid` reads 0 failed. AC1-AC3 still pass.
- **S2: ACCEPTED.** The sleeve fold skips the Tax leaf, which `apply_taxsma_overlay` owns. The skip is pinned by its test.
- **S3: ACCEPTED.** The changed `by_firm` assertion is now stronger.
- **S4: ACCEPTED.**
  - A tree row's `inside_model_figure` is True only for a measured overlap above zero.
  - An `OVERLAP_UNMEASURED` amount is named in `held_out` with that reason, and the bool reads False.
  - The `by_model` entry's `inside_model_figure` reads None where the overlap is unmeasured. The row's reason carries that
    distinction.

Gate limb that graded this amendment: none fires on a modification here (GATE viii: `<placeholders>NONE</placeholders>`).

## BOUNDS

- **Grant.** Your write grant is the `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes
  under `.scratch/` and is not committed.
- **Read-only AWS only.** The seam does S3 GetObject and List on `opal-data-assets`. No S3 write, no Lambda invoke, no `build_all`
  against real S3, no deploy. The deploy and the never-widen pair are the issuer's, at the drain.
- **Client data, hard bound (0.0.0_AB_MSTR~DELL1 msgs 2721, 2748, 2767).** Do NOT open, search, copy, `git show` or `git log -p`:
  - any `org/**/W73_S*_EVIDENCE.json` or `W73_S2_RESOLUTION.json`;
  - anything under `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/`;
  - any COTBKF or cottonwood account manifest of other workers.

  Search only inside the files named in this order.
- **Refusal clause.** If a criterion cannot be met as written:
  - stop and write the reason in your report;
  - append a surprise row to the investigation file below: id `MDPF_STRATID-W7-S<k>`, `fabric` `dell1`, `surfaced_at` =
    `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`. Rows are APPEND-ONLY;
  - do not weaken a check.

<paths>
data/mdpf/scripts/gold/mdpf_category_registry.py
data/mdpf/scripts/gold/mdpf_gold_consolidator.py
data/mdpf/tests/stratid/test_stratid_round2_firm_basis.py
data/mdpf/tests/stratid/test_stratid_global_fold.py
data/mdpf/tests/stratid/test_stratid_basis.py
org/missions/D8/MDPF/MDPF_STRATID/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_STRATID/decompositions/MDPF_STRATID_DECOMP_R2.md</decomp_doc> (round 2, workstream 1), cell `ST-u-1`.
<owned_cells>ST-u-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: ST2-u1-AC1, ST2-u1-AC2, ST2-u1-AC3. Instance at `org/missions/D8/MDPF/MDPF_STRATID/deliverables/0.9.0_WK_MDPF_STRATID~7/MDPF_STRATID.TO-ST-u1.cottonwood-outside-counted-or-held-out.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> ST2-u1-AC1 ST2-u1-AC2 ST2-u1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output (AC2's printed arm lines), commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule change; the consolidator runs in the scheduled mdpf-gold-lambda.
comp-iam: DECLARED-NOT-APPLICABLE the fold adds no AWS call (the seam's reads are the check's, read-only).
comp-adversary: RUN in the decomposition battery (silent drop, double count, build break), each answered by a seam arm. -- coverage: scanned 2 of 2 Cottonwood sma members on the served slice (divz, pfde) and 4 Global SMA by_model entries; blind to Inflection and any firm whose slice is not folded into Global today.
risk: SERVED -- Global's served output moves once deployed; the deploy runs at the drain under the C-GLOBAL-PAIR.
direct_act: false -- the class is SERVED.
</preflight>

Source: PRD v0.3 ENDPOINT FWD-2, C-BASIS, C-OVERLAP, C-GLOBAL-PAIR; decomposition round 2 rulings R1, R2, R4.
