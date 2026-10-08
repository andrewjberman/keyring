# MDPF_STRATID decomposition -- ROUND 1, the THREAD (issuer 2.0.0_SA_COO~S1, dell1; cut 2026-10-08 ~21:0xZ)

**Status: CUT** (issued in one issuance in the next commit). Seat: `2.0.0_SA_COO~S1`, spawned ~20:45Z by `0.0.0_AB_MSTR~DELL1` on
Andrew-direct ~20:4xZ "yes, spawn the fourth COO for MDPF_STRATID" (record @aea2b86eae).

**Cut on:** PRD v0.3 @bc78f393ff (L4-R ADMITTED: ratified-text half SIGNED by `3.0.0_SA_CVO`, current by ENDPOINT hash; brief half
admitted because the CRO wrote the brief). Brief `docs/briefs/mdpf-strategy-identification-into-global-brief-20261008.md` @68aa9dbe9e.

## The thread (PRD FWD-1) and its hops, measured at the base 2026-10-08 ~20:5xZ

FWD-1: Cottonwood's PFDE strategy is counted in the Global view. ACCEPT: the PFDE figure under ETF Strategies in Global equals
Cottonwood's own PFDE figure, and Global's total rises by that amount and nothing else.

| hop | what | today (measured) | cell |
|---|---|---|---|
| 1 identify | the Rebalancer sleeve named PFDE / "Pathfinder Disciplined" becomes SMA member `pfde` | WORKS: `rebalancer_schemas.opal_sma_member_of` (:226), read by `build_cottonwood_mdpf_slice.build_slice` (:622). Served slice `gold/mdpf_revamp/cottonwood/aggregate_aua_timeseries.json` by_model `pfde` = cohort `sma`, 412,892.63 on 2026-10-07, 4 accounts. Served Cottonwood category view: SMA > ETF Strategies > PFDE 412,892.63 | none |
| 1b overlap | which PFDE dollars are also inside a Model figure (C-OVERLAP) | NOT MEASURED: the slice works on model-level rows (dollars, account_count per model name); account identities never reach it. Assignment rows exist in Rebalancer silver (`rebalancer_schemas.ASSIGNMENT_COLUMNS` :164, `account_id` -> model). Prior art: the TaxSMA BASE_OVERLAP control against Cottonwood's model-assigned population (`test_taxsma_cot_global_fold.py`) | `ST-t-1` |
| 2 basis | `pfde` at Cottonwood counts ADDITIVE at Global | NOT DECLARED: `SMA_MEMBERS` declares `pfde` carve_out (:368); `SMA_BASIS_BY_SCOPE` has only `("tax","cottonwood")` (:385); no firm dimension. Probe 2026-10-08: the Global category shaper REFUSES an additive `pfde` by_model entry while the registry says carve_out ("Two declarations of the same fact disagree") | `ST-t-2` |
| 3 fold | Cottonwood's PFDE dollars added once to Global (total + by_model) | ABSENT: `build_global_artifact` folds only `GLOBAL_MODEL_KEYS` (`dim_mdpf_aggregate_aua_timeseries.py:158-159`) and takes Cottonwood MODEL dollars only; the slice's comment (`build_cottonwood_mdpf_slice.py:354-357`) holds the sleeves out pending a ruled basis (now ruled: ADDITIVE). The only additive fold is `apply_taxsma_overlay` (`mdpf_gold_consolidator.py:1648`), Tax only | `ST-t-3` |
| 4 shown | Global tree shows PFDE under SMA > ETF Strategies | WORKS once 2+3 land. Probe 2026-10-08 on the served 2026-10-07 Global timeseries, registry row `("pfde","global")` additive patched in-process, PFDE injected additive: tree PFDE 412,892.63; SMA 47,756,353.41 -> 48,169,246.04; Client 270,465,346.53 unchanged; L1 sum 2,148,075,366.71 -> 2,148,488,259.34 (delta 412,892.63 exactly). Control: the served view reshaped from the served timeseries equals served | none |
| 5 read | Andrew reads it after a scheduled run | the issuer's one real run at close | none |

Baseline (served 2026-10-07, `process_time` 2026-10-08T13:30:37Z): Global total 2,148,075,366.70; Global ETF Strategies 21,117,463.07
(divz 17,060,798.54 + pfoe 4,056,664.53, 49financial only); Global PFDE null. Cottonwood ETF Strategies 1,782,298.71 (divz 1,369,406.08,
pfde 412,892.63).

## Rulings the issuer makes inside this decomposition (step 7)

- **R1. Round 1 declares exactly one additive (member, firm) row: `("pfde","cottonwood")`.** Cottonwood's FIRM population is left
  UNDECLARED this round, so under C-BASIS its other sleeves (divz 1,369,406.08) are not counted. This is the contract's own override
  path, and it is what makes FWD-1's "and nothing else" readable on the first run. Declaring Cottonwood's population OUTSIDE (FWD-2) is
  round 2's first item. 49financial's population is declared INSIDE (its measured state, `mdpf_category_registry.py:343-345`).
- **R2. The category tree validates one basis per (member, scope).** So round 1 also carries `("pfde","global")` additive in the
  scope table. A member with dollars on BOTH bases at Global (divz: 49financial carve-out + Cottonwood additive) cannot be served by
  one scope row; that is FWD-2's design question and goes in the round-1 drain-end read, not this round.
- **R3. Unmeasured overlap withholds.** Until the slice carries `overlap_model_value`, the fold withholds the whole member and names it
  `OVERLAP_UNMEASURED` (C-OVERLAP; never assume zero).
- **R4. Eclipse census rides round 1** as a read-only cell because PRD OPEN ITEM 1 names it for round 1's first cell; it builds nothing.

## Rule 24

Domain: the FWD-1 thread, hops 1-5 above, plus the PRD's open-item-1 read. Hops 1 and 4 work today (measured); hop 5 is the issuer's.
The remainder is three write sets with one intent each: the overlap measurement where the sleeve is first named (`ST-t-1`, the
Cottonwood slice), the per-firm basis declaration (`ST-t-2`, the registry), the fold into Global (`ST-t-3`, the consolidator and the
two readers of the additive series). `ST-t-4` writes one document. No remainder. Same grain: each cell is one adapter of the thread.
State coherence: `ST-t-1` moves no served figure (a new field only); `ST-t-2` moves no served figure on its own (the tree reads the
row only when a by_model entry carries it); `ST-t-3` moves Global's total and SMA node only, never a per-firm view, never Models or
Client; none moves Muni, the ETF list, the matcher, the unidentified list or the Eclipse path.

## The cells

| cell | what | serves | status | placement | risk | chain / slot |
|---|---|---|---|---|---|---|
| `ST-t-1` | `measure_sma_overlap(s3, value_date)` in the Cottonwood slice: per Opal SMA member, the sleeve's accounts, how many also carry an Opal Model assignment that date, and those accounts' sleeve dollars; `build_slice` writes `overlap_model_value` (aligned to `dates`, None where unmeasured) on every `cohort_class: sma` by_model entry | FWD-1 | NOT-EVALUATED | dell1 code; deployed by the issuer at the drain | SERVED | A, `0.9.0_WK_MDPF_STRATID~1` |
| `ST-t-2` | The registry's per-firm basis at Global: `SMA_FIRM_POPULATION` (firm -> inside / outside / undeclared), `SMA_BASIS_AT_GLOBAL_BY_FIRM` ((member, firm) -> basis), resolver `sma_global_basis_of(member, firm)` -> additive / carve_out / None (None = not counted, listed); round-1 rows per R1/R2; import check refuses an invalid row | FWD-1 | NOT-EVALUATED | dell1 code | SERVED | B, `0.9.0_WK_MDPF_STRATID~2` |
| `ST-t-3` | `apply_sma_sleeve_overlay(arts)` in the consolidator, called once right after `apply_taxsma_overlay`: for each firm leg other than 49financial, each `sma` by_model member whose `sma_global_basis_of` is additive is added to Global (`by_model[member]` additive, `opal_aggregate_aua`, new `sma_additive_aua`), less its overlap dollars; withheld amounts in `sma_additive_withheld`; the category tree and aum-metrics count it once | FWD-1 | NOT-EVALUATED | dell1 code; deployed by the issuer at the drain under the C-GLOBAL-PAIR | SERVED | B (after t-2), `~2` |
| `ST-t-4` | READ-ONLY census of Eclipse (Inflection) silver sleeve/model names carrying an Opal ETF ticker as a whole word or a full fund name, denominator printed | FWD-5 (open item 1) | NOT-EVALUATED | dell1, document only | LOCAL | C, `0.9.0_WK_MDPF_STRATID~3` |

## Interface contracts between cells (fixed here; each cell builds against them)

- **Slice -> fold:** `by_model[<member>]["overlap_model_value"]`: list aligned to the slice's `dates`; float dollars of that member's
  sleeve accounts that also carry an Opal Model assignment on the date; `None` = not measured. Absent key = not measured.
- **Registry -> fold:** `mdpf_category_registry.sma_global_basis_of(member_id, firm_id) -> "additive" | "carve_out" | None`.
- **Fold -> readers:** on `arts["global"]`: `sma_additive_aua` (list aligned to Global `dates`, None where nothing counted),
  `sma_additive_withheld` (list of `{"member_id", "firm_id", "date", "value", "reason"}`, reason `OVERLAP` or `OVERLAP_UNMEASURED`),
  `by_model[<member>]` = `{"cohort_class": "sma", "source_basis": "additive", "display_name", "model_value", "account_count",
  "inside_model_figure": false, "firms": [<firm>]}`. Every other scope gains `sma_additive_aua` all-None (the L-1 key-set identity).
  Identity: `opal_aggregate_aua = base_excluding_tax_aua + tax_additive_aua + sma_additive_aua` where all three are present.

## Write sets (disjoint)

- **ST-t-1:** `data/assets/scripts/gold/build_cottonwood_mdpf_slice.py`, `data/assets/scripts/gold/tests/test_cottonwood_sma_overlap.py`
  (new), the channel.
- **ST-t-2 then ST-t-3 (one worker):** t-2 `data/mdpf/scripts/gold/mdpf_category_registry.py`, `data/mdpf/tests/stratid/test_stratid_basis.py`
  (new); t-3 `data/mdpf/scripts/gold/mdpf_gold_consolidator.py`, `data/mdpf/scripts/gold/dim_mdpf_aum_metrics.py`,
  `data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py` (only if its extension-field validation refuses the new keys),
  `data/mdpf/tests/stratid/test_stratid_global_fold.py` (new); the channel.
- **ST-t-4:** `org/missions/D8/MDPF/MDPF_STRATID/deliverables/0.9.0_WK_MDPF_STRATID~3/ECLIPSE_SLEEVE_NAME_CENSUS.md`, the channel.
- Checks (issuer's, dry-run at the base 2026-10-08 ~20:5xZ): `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_STRATID_S1/R1_CHECKS/`.
  Build checks FAIL at the base as expected (`st_t1_tests`, `st_t1_live`, `st_t2_tests`, `st_t3_tests`, `st_t3_seam`, `st_t4_census`);
  regression guards PASS at the base as expected (`st_t1_regress`, `st_t2_regress`, `st_t3_regress`).

## Edges and fan-out

`ST-t-3 depends_on ST-t-2` (t-3 imports `sma_global_basis_of`; one worker in order). `ST-t-3` consumes `ST-t-1`'s field by the contract
above and is built and seam-probed without it (R3: unmeasured overlap withholds, which the seam probe's arm A asserts on the served
slice); the two meet at the drain, not at build. `fanout: 3 of 3 chains, cap 8`.

## Battery

- `comp-schedule`: DECLARED-NOT-APPLICABLE -- thread round; no schedule moves (the slice and the consolidator already run in the
  scheduled MDPF chain: `infra/aws/ec2/mdpf-daily-runner/mdpf-daily-dispatch.sh:556`, `mdpf-gold-lambda`).
- `comp-iam`: RUN, scoped. `ST-t-1` adds one read: Rebalancer assignment silver under `s3://opal-data-assets/blackdiamond/cottonwood/silver/`,
  the bucket and prefix family the slice already reads (`build_cottonwood_mdpf_slice.py:528`, `:582`). Blindness: the slice's runtime
  is the EC2 MDPF daily runner, whose role `comp-iam roles` does not map to this script, and the tool reads the DESIRED plane only.
  The APPLIED plane is read at the drain by the real run. `ST-t-3` adds no AWS call.
- `comp-adversary`: DECLARED-NOT-APPLICABLE -- thread round; the lens runs on the enrichment round that touches its surface. The one
  hazard it would name is recorded here instead: a second additive series beside Tax is read by every consumer that today reads only
  `tax_additive_aua` (`mdpf_gold_consolidator.py:671-676`, `dim_mdpf_aum_metrics.py:225-235`, `:395-402`); the writer census (drain act 1)
  counts them before the pair.
- C-NAMES / Rule 30: no new address or resource name; new fields ride existing artifacts (existing pipeline, R19 non-application).

## The issuer's acts at the drain (not cells)

1. **Writer census (PRD open item 3), before any pair:** every writer and reader of Global's `opal_aggregate_aua`, SMA node and
   `tax_additive_aua`, printed with its denominator (NEVER-1: N writers = N rules read).
2. **Never-widen pair (C-GLOBAL-PAIR):** CTO half by laptop `1.0.0_SA_CTO` (MDPF_GLOBAL owner), COO half by `2.0.0_SA_COO~S1`, read
   first by `1.0.0_SA_CTO~DELL1`. Blast radius: `portal/gold/mdpf/global/` (aggregate-aua-timeseries, category-views, aum-metrics) for the
   run date; expected outcome, read from the fold's own rule at signing, both branches: overlap measured -> Global total + (PFDE - overlap);
   overlap unmeasured -> no total move and PFDE listed withheld. Rollback: redeploy the prior package; the next scheduled run rewrites
   the date. Per-firm views do not move (the slice gains a field only).
3. **Deploy (WORLD)** of the slice and the `mdpf-gold-lambda` package under a change-management entry, via `safe-deploy.sh` under the
   lane it admits (Rule 13; a refusal routes to the DS seat), then the deployed bytes read against the build input.
4. **The one real run of FWD-1:** the next scheduled MDPF run after the deploy; read the served Global category view (PFDE under ETF
   Strategies = Cottonwood's PFDE that date, total delta = that amount) and commit the read under `deliverables/2.0.0_SA_COO/`. An ad-hoc
   QA run first is allowed and is not the acceptance (FWD-1 DONE WHEN: after a scheduled run).
