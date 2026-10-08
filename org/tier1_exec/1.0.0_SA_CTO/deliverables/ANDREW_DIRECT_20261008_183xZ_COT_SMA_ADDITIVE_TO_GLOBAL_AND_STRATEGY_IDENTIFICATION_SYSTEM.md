# Andrew-direct 2026-10-08 ~18:3xZ at the dell1 `1.0.0_SA_CTO~DELL1` terminal -- Cottonwood SMA dollars additive to Global; a strategy identification system

**Context:** `1.0.0_SA_CTO~DELL1` answered his question 3 (does the Cottonwood rebalancer pull find new Opal Models and SMAs; why the PFDE
SMA and Muni SMA do not reach the Global Aggregate view). Read-only findings, measured on the served 2026-10-07 `category-views` and
`aggregate-aua-timeseries` (`opal-data-assets/portal/gold/mdpf/{global,cottonwood}/`):
- PFDE shows at Cottonwood under ETF Strategies ($412,892.63) and is absent at Global. Cottonwood's SMA sleeves are kept out of Global on
  purpose, pending a ruled basis (`data/assets/scripts/gold/build_cottonwood_mdpf_slice.py:354-357`, commit 85dd7adc26). Cottonwood's DIVZ
  is absent from Global for the same reason.
- Muni SMA is absent at both levels. The registry row `("muni", "muni", "Muni SMA", True, "ALT Strategies", carve_out)`
  (`data/mdpf/scripts/gold/mdpf_category_registry.py:357`) is never reached: `OPAL_SMA_NAME_RULES`
  (`data/assets/scripts/silver/rebalancer_schemas.py:218-234`) has no Muni rule. Opal_Muni_Sleeve ($550,823.07) is a Custom model, and
  Opal_Muni_Income ($64,119,753.85, 1 account, auto_classified) sits in the Custom catch-all, a figure to verify.
- Global's model set is the fixed `GLOBAL_MODEL_KEYS` (`data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py:133-159`).

The card put to him: Cottonwood SMA dollars enter Global (a) additive, with an overlap check like the Tax SMA fold
(`data/mdpf/tests/taxsma/test_taxsma_cot_global_fold.py`), or (b) carve-out. REC (a).

## VERBATIM

> "Ok im cool with items 1 and 2, so let's go into 3. Rebalancer self-repair, new Models SMAs, and so on. Regarding the Cottonwood SMA
> dollars, that should be additive because those are outside of the Models. Beyond that, we need to figure out how to set up
> identification where when SMA Strategies (Tax or Muni for ALT thus far), and all the Opal ETFs for ETF Strategies, we need to make sure
> we have a system that gets those identified and sent over for counting in the global aggregate."

## What it rules

1. **Basis ruled: ADDITIVE.** Cottonwood's SMA dollars are outside its Models, so they add to Global (option (a)). This settles the basis
   that `build_cottonwood_mdpf_slice.py:354-357` held open.
2. **A new requirement:** a system that IDENTIFIES strategy holdings and SENDS them to the Global aggregate for counting:
   - SMA Strategies -> ALT Strategies: Tax and Muni, "thus far" (the list is open-ended).
   - Every Opal ETF -> ETF Strategies.
   That is identification at intake, not a hand-kept list, so a new SMA or Opal ETF reaches Global without a code edit.

"Items 1 and 2" (the MDPF_SECCLASS context and the MDPF_SECHIST wait) are accepted as reported.

## Routing (this seat)

- New scope enters the canonical loop at L1: brief asked of `4.0.0_SA_CRO~DELL1`. The L2 DONE WHEN goes to Andrew to confirm.
- The aggregate's owner is `1.0.0_SA_CTO` (laptop; `org/projects/MDPF_GLOBAL.json`), and the project is not placed on a box: the ruling and
  a placement request go laptop-ward through `0.0.0_AB_MSTR~DELL1`. REC: place the build on dell1 (Dells carry the work), seated when a
  dell1 COO lane frees (MDPF_HEALGAP is in its last round).
