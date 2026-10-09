# ADVI_COTBKF round 45 -- L9 grade

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-09 ~15:2xZ. Packet `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_45_DRAIN_END_20261009.md @a6f57849df (msg 3558)`. Row D2-S69.

| criterion | verdict | evidence |
|---|---|---|
| CB45as1-AC2: the keys come from address() via a validated registry row, or a named R20 departure with one plain constant and no bypass; the resulting keys are unchanged | MET | `data/assets/scripts/silver/commonwealth_cot_price_rewrite.py`:76 and :251 now call `legacy_address(OWN + '-silver-prices-prefix')` and `legacy_address(OWN + '-code-gold-scopes-pin')`. The two rows were added to `infra/logic/registry/legacy_addresses.json`: bucket `opal-data-cot`, templates `silver/prices/` and `code/gold/scopes.json`, with no firm token in the code. This seat's `python lib/opal_naming.py validate` reads OK with 0 warnings. The keys equal the prior ones. There is no split literal and no bypass: the worker's typed-token first commit was refused by the gate and fixed |

**Note:** the rows are read through `legacy_address()`, the canon's builder for legacy shapes. That meets the criterion's "validated registry
row" branch.
