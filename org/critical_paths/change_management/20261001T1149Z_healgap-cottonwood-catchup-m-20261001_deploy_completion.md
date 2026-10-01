# Deploy Completion Record
**Date opened:** 2026-10-01T11:49:38.192801+00:00
**Status:** OPEN
**Deploy:** MDPF_HEALGAP cell 1: the Cottonwood gold catch-up step rewrites FIVE existing objects under s3://opal-data-assets/blackdiamond/cottonwood/gold/dim_model_portfolio/ on its first daily run (date=2026-08-19 PCk.ZVdhC3KfTH9gK5sDpwT41hacOoCg; date=2026-08-21 jl2bwRAA95xXPXiwwRn3wz1CEPWy1fxG; date=2026-08-24 prrE6yeln3l3SIaGVXZajXh6zVz1erHO; date=2026-09-24 u842OFS3LS4zmmoOVCurbbhX8dH_WXqf; date=2026-09-25 Ie9RJF76OIhzWoMmPhU92fklkHuWLsXI -- the prior VersionIds, each the rollback target by copy-object, no delete); halves COO @e9b9650218 + CTO SIGNED @9fb81ec9f6; the call line and the mdpf-gold-lambda deploy are 4.0.0_SA_CRO's own entry
**Authored by:** 2.0.0_SA_COO~M
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 60.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P | verify | before the hookup deploys: the five prior VersionIds read live; the CTO half's sanity read (each figure in served terms beside its two nearest measured points) | head-object + served-terms run | Prior VersionIds read by head-object 11:2xZ (bucket versioning Enabled), each object last written 13:30:39Z-13:30:40Z on its own date: date=08-19 PCk.ZVdh.. ; 08-21 jl2bwRAA.. ; 08-24 prrE6yel.. ; 09-24 u842OFS3.. ; 09-25 Ie9RJF76.. (full ids in the title). CTO half item 1, the sanity read, 11:46Z-11:47Z, read-only (builder build() in memory, folded by the slice's own build_slice): CONTROL PASS -- the fold equals the served file portal/gold/mdpf/cottonwood/aggregate-aua-timeseries/2026-09-29.json on 5 of 5 neighbour dates (08-17 136,788,403.51; 08-19 139,691,291.41; 08-24 139,475,744.20; 09-22 177,115,207.38; 09-25 179,644,635.41). The five in SERVED terms (model_aua): 08-18 136,124,300.89 (outside its neighbours, 0.49% from the nearer); 08-20 139,107,569.53 (outside, 0.26%); 08-21 139,653,361.92 (between); 09-23 175,667,910.62 (outside, 0.82%); 09-24 176,412,889.04 (outside, 0.40%). None is both outside and more than 2% from the nearer, so none needs an explanation. The half's table gives the builder's Opal totals (142.4M to 198.0M), a wider measure than the served model_aua: the slice drops named non-model residuals (ratio 1.045 in August, 1.12 in late September); 0 reconcile failures on the five. | CLOSED 20261001T114938Z |
| D1 | verify | the first daily run after the hookup deploys: the family report's catchup block reads five built, 0 failed; each object carries its value date; the older dates' earliest partitions are byte-unchanged | manifest + parquet reads |  | OPEN |
| S | verify | served: one trace per date -- the Cottonwood point reads measured with the served-terms value, the Global point reads measured; 49 Financial and Inflection series byte-unchanged | served file reads |  | OPEN |
| D2 | verify | the second daily run: catchup reads 0 planned, 0 built | manifest read |  | OPEN |

## Log

- 20261001T114938Z OPENED by 2.0.0_SA_COO~M with 4 leg(s)
- 20261001T114938Z LEG P closed: Prior VersionIds read by head-object 11:2xZ (bucket versioning Enabled), each object last written 13:30:39Z-13:30:40Z on
