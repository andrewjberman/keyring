# TO MDPF_STRATID.TO-ST-t3 -- round 1 ST-t-3: Cottonwood's additive SMA sleeves are added to Global once, overlap withheld by name
<to_id>MDPF_STRATID.TO-ST-t3</to_id>
<project>MDPF_STRATID</project>
<issued_to>0.9.0_WK_MDPF_STRATID~2</issued_to>
<issued_by>2.0.0_SA_COO~S1</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
**Directive:** D8 | **Fabric:** laptop (placement dell1) | **Decomp cell:** `ST-t-3` (`decompositions/MDPF_STRATID_DECOMP.md`, ROUND 1) |
**outcome_ref:** FWD-1 | **depends_on:** ST-t-2

---

## WORKER FACE

### THE CELL

`ST-t-3`. FWD-1: Andrew opens the Global view and sees Cottonwood's PFDE strategy under SMA > ETF Strategies, equal to Cottonwood's
own PFDE figure, and Global's total higher by exactly that amount and nothing else. Today Global never sees it: Global takes Cottonwood's
MODEL dollars only. You build the fold that adds an additive sleeve to Global once. You run AFTER `ST-t-2` in this same worktree, so
`mdpf_category_registry.sma_global_basis_of(member_id, firm_id)` exists (returns `additive` / `carve_out` / None) and
`sma_basis_of("pfde", "global")` reads `additive`.

**The estate, read at the base.**
- `data/mdpf/scripts/gold/mdpf_gold_consolidator.py`: `apply_taxsma_overlay(arts, taxsma_result)` (:1648-1754) is the one additive fold
  today (Tax only) and your prior art: it adds to `opal_aggregate_aua`, keeps the pre-additive base in `base_excluding_tax_aua`, sets
  `aggregate_basis` `INCLUDES_ADDITIVE`, puts the member in `by_model` with `cohort_class: "sma"` and `source_basis`, and gives EVERY scope
  the same extension keys (the L-1 key-set identity). Its single call site is in `build_all` (:2316). The Cottonwood-onto-Global carry
  rule there (:1704-1723) is the shape for dates.
- The category tree: `_shape_category_views(ts_doc, scope)` (:610). On a folded doc it takes `base_excluding_tax_aua` as the total and
  then ADDS every additive SMA member found in `by_model` (:671-676) -- so leave `base_excluding_tax_aua` as the pre-ALL-additive base,
  or the sleeve is counted twice. It refuses a by_model entry whose `source_basis` disagrees with `registry.sma_basis_of(member, scope)`.
- `data/mdpf/scripts/gold/dim_mdpf_aum_metrics.py`: reads `tax_additive_aua` as a labelled component (:225-235) and adds it to the firm
  total (:395-402). Your new series must be counted there once, the same way, as its own labelled component.
- Global's by_model folds only the fixed `GLOBAL_MODEL_KEYS` (`dim_mdpf_aggregate_aua_timeseries.py:158-159`); read its
  `timeseries_extension_fields` handling (:3028-3140) and change that file only if its validation refuses the new keys.
- `arts["cottonwood"]` is the Cottonwood slice: its by_model carries `pfde` as `{"cohort_class": "sma", "model_value": [...],
  "account_count": [...]}` aligned to its own `dates` (412,892.63 on 2026-10-07). A sister cell is adding `overlap_model_value` there
  (see the contract below); it is NOT in your worktree.

**Interface contract (fixed by the decomposition):**
- Input `arts["cottonwood"]["by_model"][m]["overlap_model_value"]`: list aligned to Cottonwood `dates`, float = dollars of member m's
  sleeve accounts also inside an Opal Model that date, None = not measured; key absent = not measured.
- Output on `arts["global"]`: `sma_additive_aua` (aligned to Global `dates`, None where nothing counted); `sma_additive_withheld` (list of
  `{"member_id", "firm_id", "date", "value", "reason"}`, reason `OVERLAP` or `OVERLAP_UNMEASURED`); `by_model[m]` = `{"cohort_class": "sma",
  "source_basis": "additive", "display_name", "model_value", "account_count", "inside_model_figure": False, "firms": [<firm>]}`. Every other
  scope gains `sma_additive_aua` all-None. Identity where present: `opal_aggregate_aua = base_excluding_tax_aua + tax_additive_aua +
  sma_additive_aua`.

**Build:**
1. `apply_sma_sleeve_overlay(arts: dict) -> dict` in the consolidator, called ONCE in `build_all` immediately after `apply_taxsma_overlay`.
   For each firm leg other than `49financial` and `global`, each by_model entry with `cohort_class == "sma"` whose
   `registry.sma_global_basis_of(member, firm)` is `additive`: on each Global date, counted = sleeve value - overlap (Cottonwood's value
   on that date; past Cottonwood's last measured date carry its last measured value and overlap from the same source date, as the Tax
   fold carries). Overlap unmeasured on a date -> count nothing for that member that date and record it withheld `OVERLAP_UNMEASURED`
   with the sleeve value; overlap > 0 -> record the overlap withheld `OVERLAP`. `carve_out` or None -> not added (never silently).
2. Add counted dollars to Global's `opal_aggregate_aua` and `sma_additive_aua`, and put the member in Global's `by_model` per the contract.
   A Global doc that was not yet folded (`aggregate_basis` not `INCLUDES_ADDITIVE`) gets the same treatment Tax gives it (set the basis,
   `base_excluding_tax_aua` = pre-fold total, `tax_additive_aua` None).
3. Per-firm docs (`cottonwood`, `49financial`, `inflection`) do not change except the all-None `sma_additive_aua` key.
4. `dim_mdpf_aum_metrics.py`: count `sma_additive_aua` once at the frontier as its own labelled component beside `taxsma`, and in the
   firm total, so Global's aum-metrics total equals the fold's `opal_aggregate_aua`.
5. Tests in NEW `data/mdpf/tests/stratid/test_stratid_global_fold.py` (own sys.path preamble; synthetic docs; no network), these exact
   names: `test_additive_sleeve_added_to_global_total_and_by_model`, `test_overlap_dollars_withheld_and_named`,
   `test_unmeasured_overlap_withholds_whole_member`, `test_undeclared_firm_member_not_counted` (Cottonwood `divz`: no row, population
   undeclared), `test_carve_out_member_never_added`, `test_category_tree_and_aum_metrics_count_it_once`,
   `test_cottonwood_and_49financial_views_unchanged`.

### ACCEPTANCE

<criterion id="ST1-t3-AC1" cell_refs="ST-t-3"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_STRATID_S1/R1_CHECKS/st_t3_tests.py</invocation><expect>T3-OK</expect></criterion>
`ST1-t3-AC1` -- the seven named tests pass.

<criterion id="ST1-t3-AC2" cell_refs="ST-t-3"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_STRATID_S1/R1_CHECKS/st_t3_seam.py</invocation><expect>SEAM-OK</expect></criterion>
`ST1-t3-AC2` -- the seam probe against the served Global and the live Cottonwood slice (read-only): control reshape equals served; arm A
(no overlap field) moves no total and withholds PFDE as `OVERLAP_UNMEASURED`; arm B (overlap 0) raises Global's total by exactly
Cottonwood's PFDE and shows it under SMA > ETF Strategies with Client unchanged.

<criterion id="ST1-t3-AC3" cell_refs="ST-t-3"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_STRATID_S1/R1_CHECKS/st_t3_regress.py</invocation><expect>T3-REGRESS-OK</expect></criterion>
`ST1-t3-AC3` -- the TaxSMA served-fold tests still pass (the Tax fold is unchanged).

<expected_criteria>ST1-t3-AC1 ST1-t3-AC2 ST1-t3-AC3</expected_criteria>

Run each invocation from the worktree root. At the base (2026-10-08 ~20:5xZ): AC1 `T3-BAD no file ...`; AC2 `SEAM-BAD arm=build no
apply_sma_sleeve_overlay ...`; AC3 `T3-REGRESS-OK`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **Read-only AWS only** (S3 GetObject / List on `opal-data-assets`, which AC2 does). No S3 write, no Lambda invoke, no `build_all` run
  against real S3, no deploy. The deploy and the never-widen pair are the issuer's, at the drain.
- Do not edit the registry (that was `ST-t-2`), the Cottonwood slice, or `apply_taxsma_overlay`'s behaviour.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_STRATID-W2-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the investigation file
  below, and do not weaken a check. Rows are APPEND-ONLY. Another reader of `tax_additive_aua` you find outside your paths is an
  OBSERVATION row naming it, not an edit.

<paths>
data/mdpf/scripts/gold/mdpf_gold_consolidator.py
data/mdpf/scripts/gold/dim_mdpf_aum_metrics.py
data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py
data/mdpf/tests/stratid/test_stratid_global_fold.py
org/missions/D8/MDPF/MDPF_STRATID/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_STRATID/decompositions/MDPF_STRATID_DECOMP.md</decomp_doc> (round 1, the thread), cell `ST-t-3`.
<owned_cells>ST-t-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: ST1-t3-AC1, ST1-t3-AC2, ST1-t3-AC3. Instance at `org/missions/D8/MDPF/MDPF_STRATID/deliverables/0.9.0_WK_MDPF_STRATID~2/MDPF_STRATID.TO-ST-t3.additive-sleeve-fold-into-global.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> ST1-t3-AC1 ST1-t3-AC2 ST1-t3-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output (AC2's printed figures), every reader of `tax_additive_aua` you found, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE thread round; no schedule change.
comp-iam: DECLARED-NOT-APPLICABLE the fold adds no AWS call (AC2's reads are the check's, read-only).
comp-adversary: DECLARED-NOT-APPLICABLE thread round; the hazard (a second additive series beside Tax) is named in the decomposition battery and counted by the drain's writer census.
risk: SERVED -- Global's served output moves once deployed; the deploy runs at the drain under the C-GLOBAL-PAIR.
direct_act: false -- the class is SERVED.
</preflight>

Source: PRD v0.3 ENDPOINT FWD-1, C-BASIS, C-OVERLAP, C-GLOBAL-PAIR, C-LAYERS; decomposition round 1 hops 3-4, rulings R1-R3.
