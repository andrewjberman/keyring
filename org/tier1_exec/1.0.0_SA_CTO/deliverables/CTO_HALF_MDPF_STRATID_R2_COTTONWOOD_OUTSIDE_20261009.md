# CTO half -- MDPF_STRATID round-2 never-widen pair (Cottonwood declared OUTSIDE)

**Seat:** `1.0.0_SA_CTO` (laptop; MDPF_GLOBAL owner). **Date:** 2026-10-09 ~17:2xZ.
**Pair:** `org/missions/D8/MDPF/MDPF_STRATID/deliverables/2.0.0_SA_COO~S1/NEVER_WIDEN_PAIR_R2_COTTONWOOD_OUTSIDE.md` @c4fdec2ec7 (box/dell1),
COO half signed by `2.0.0_SA_COO~S1`. Read by `1.0.0_SA_CTO~DELL1`: `ledger/CTO_DELL1_READ_R2_COTTONWOOD_OUTSIDE_PAIR_20261009.md`.
Carried by `0.0.0_AB_MSTR` msg 108054 (relay `RELAY_20261009_165xZ_THREE_CARRIES_FOR_CTO.md` @9c30fb0a96). Written here, not in the pair
file, because the pair lives on box/dell1 and a cross-box edit of one file collides (today's XB-4849 hold).

## What this half signs

The two deploy acts D1 (box/dell1 push safe-deploying `mdpf_gold_consolidator.py` and `mdpf_category_registry.py` to
`s3://opal-data-mdpf/code/scripts/gold/`) and D2 (`mdpf-gold-lambda` rebuilt at pin `f1deec74b1`, targeted safe-apply), with the blast
radius of pair section 4 and the rollback per key of section 2.

## Read

- Writers of the property: N = 5 (`build_global_artifact`, `apply_taxsma_overlay`, `apply_sma_sleeve_overlay`, `_shape_category_views`,
  `dim_mdpf_aum_metrics`), all read; round 2 adds none; two change behaviour.
- Both branches come from the fold's own rule (overlap == value -> held out as OVERLAP and named; overlap < value -> adds the difference;
  overlap unmeasured -> OVERLAP_UNMEASURED). On today's data the Global total is UNCHANGED at 2,147,378,054.74 (divz 1,369,280.57 held
  out); the planted arm shows the other branch.
- May move: the three Global served views; gains fields only on `by_model` and the SMA tree; does not move Models, Client, Tax or any
  per-firm figure.

## SIGNED -- `1.0.0_SA_CTO`, with these conditions

1. **Dell1 CTO point 1:** the check-A baseline (ruling @5a151aacea) grades this fire; a per-firm move on the prior frontier date is the
   daily restatement, measured against the control, not this fold's.
2. **Dell1 CTO point 2:** a held-out sleeve stays VISIBLE by name and value (`held_out`); the real run's page read shows the divz row with
   its held-out line, or the outcome is not met.
3. **Import closure before D1** (the 14:51Z `rebalancer_schemas` break, row D1-S4 @363e025233): before the push, list every module the two
   files import and read each from `s3://opal-data-mdpf/code/` (and from the D2 package manifest); any absent module ships first or the act
   does not start.
4. **Change-management entry** opened before D1 and naming both keys and the function (CLAUDE.md NEVER-2), closed at completion.
5. **No client data in the evidence:** the after-run read committed under `deliverables/2.0.0_SA_COO~S1/` carries totals, counts and sha256
   only, never an account id (dell2 containment ruling item 6; `client-data-check.py` @8c1d8a1966).
