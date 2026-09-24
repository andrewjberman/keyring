# ANDREW-DIRECT 2026-09-24 ~20:5xZ -- 49F Performance runs on our own GIPS engine, cross-checked against Black Diamond

**Channel:** the 1.0.0_SA_CTO terminal, in answer to 2.0.0_SA_COO~P msg 100884 ("may 49F use its Black Diamond route
as PRIMARY now, SmartX later?"). **Recorded by:** 1.0.0_SA_CTO, same turn.

## His words, verbatim

1. On the question as asked: "Look at the DATA_PLATFORM and DATA_ANALYTICS solutions, there should absolutely be a
   smartx endpoint and associated research we've gone through this before. If there really is not, we can use Black
   Diamond but i know its there."
2. Minutes later: "Yeah honestly, to be fair, SmartX is actually retarded when it comes to most things, it is probably
   better for us to use 49 Financial as an opportunity to actually just run the necessary performance analytics
   ourselves (which we had an entire project around developing the calculations necessary and they're already done)
   and we just cross-check against Black Diamond for 49."
3. Then: "yes look for the ADVI GIPS prior art. I know we did all of it already, the key is now basically using
   "Black Diamond" as a way to jump start our performance recording engine, because we just match the same shape
   and compare against Black Diamond, and this project is the perfect opportunity to continue that work."

## What it binds

- **49F Performance is computed by our engine, not SmartX and not Black Diamond.** Primary source: the 49F GIPS
  chain in `data/assets/scripts/gold/runners_49f/` (`c00_flow_ledger.py` -> `c02_twr_engine.py` ->
  `c03_twr_lineage.py`; entry `chain_49f_entrypoint.py`).
- **Black Diamond is the cross-check only**, which is what `infra/aws/lambda/investor-reporting/performance/tenants.py`
  `VERIFICATION_ROUTES` already says. The use he named is that comparison for 49F; serving a Black Diamond figure as
  the 49F answer is not covered.
- **Match Black Diamond's shape.** Our output takes the fields of BD `performancePeriod` per date range (BMV/EMV with
  accrual separate, netAdditions, fees, income, daysHeld, time-weighted and money-weighted return) so the two compare
  field for field. That comparison is how the performance recording engine is brought up; IRPT is the project that
  continues that work.
- **SmartX is not the 49F Performance source.** The estate does hold SmartX (credential `smartx/credentials/*`, JWT
  refreshed 2026-09-24 13:00Z, `docs/architecture/DATA_PLATFORM_D4_smartx_endpoint_sweep.md`), but it is model-grain
  and `opal7` is refused the 49F enterprise account list (`docs/briefs/mdpf-assets-027-smartx-49f-coverage-probe-20260520.md`).
  The "no endpoint or credential" line in 100884 was wrong; the decision does not rest on it.

## Prior art (measured 2026-09-24 ~20:5xZ)

- **Engine output is live:** `s3://opal-data-49financial/gold/advi/canonical/twr_daily/` holds 557 date partitions,
  2024-07-08 through 2026-09-23 (s3api list, delimiter `/`); `canonical/twr_periods` beside it. Schema 1.2.
- **The comparison harness exists:** `org/tier1_exec/4.0.0_SA_CRO~A/deliverables/BD_PERFORMANCE_ENDPOINT_VS_GIPS_ENGINE_COMPARISON_20260819.md`
  (BD `performancePeriod` as oracle, matched-window linking against `twr_daily`). The BD pull is the deployed
  `opal-assets-bd49f-reporting-pull` Lambda.
- **Fixes landed since that comparison:** in-kind flow valuation (`ADVI_49F.c02-CFINPUT`, deployed @21170203c5);
  gross-leg vintage (`c02-VINTAGE`); negative-BMV refusal (`c02-NEGBMV` @ac7792ac50); 535-partition re-emission
  (`c02-REEMIT`, accepted 2026-08-30).
- **One clause still open:** `c02-CFINPUT` CF-2 clause 2, "since-inception ties BD in-band" on the in-kind-funded
  specimen, stands UNMEASURED. The IRPT cross-check is the instrument that measures it.
- Spec: `org/tier1_exec/3.0.0_SA_CVO/deliverables/SPEC_49F_GROUP_C_TWR_ENGINE_20260811.md`. The registry carrier
  `org/projects/ADVI_TWR.json` was closed 2026-08-25 in the spring clean ("we can reinvent a project"); this order
  runs inside IRPT_BCKEND, not as a revived project.

## Who does what

- **2.0.0_SA_COO~P** (IRPT_BCKEND): the 49F Performance read path over `twr_daily` / `twr_periods`, shaped to BD
  `performancePeriod`, and the per-account comparison against BD. The engine's own code stays in its DS lane.
- **Inflection (Orion)** is unaffected: ~P's build continues as stated in 100884.
</content>
</invoke>
