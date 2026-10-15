# Andrew-direct 2026-10-15 ~15:2xZ (dell1, `1.0.0_SA_CTO~DELL1` terminal) -- Muni is a Custom Model, Cottonwood included

## VERBATIM

> "Muni is in Custom Models, yes"

It answers held call `dell1-20261015T152025Z-494e`: Cottonwood's Opal Muni Income (about $64M, one account) moves from Other AUM to Custom
Models. Option (a). It also resolves the conflict with his 2026-09-21 rule, which routed newly discovered, auto-classified Opal-named models
non-model at Cottonwood (`data/assets/scripts/gold/build_cottonwood_mdpf_slice.py:933`). For Muni, the 10-14 word "muni is just a custom
model" governs every view.

## What it decides

- In the Cottonwood slice, Opal Muni Income counts in Custom Models (`by_model` / `model_aua`), not in `income_non_model_residual`. About $64M
  moves Other -> Custom at Cottonwood and, through the Global sums, Other/non-model -> Custom at Global.
- This is a served change. It goes under a never-widen pair, through the Cottonwood Trend addendum (CRO spec `MDPF_CANON_COTTONWOOD_AUM_TREND_UPGRADE_SPEC_20261015.md`
  @21caa664be) in MDPF_CANON.
- Other auto-classified Opal-named models keep the 09-21 rule. Only Muni is named.

-- 1.0.0_SA_CTO~DELL1
