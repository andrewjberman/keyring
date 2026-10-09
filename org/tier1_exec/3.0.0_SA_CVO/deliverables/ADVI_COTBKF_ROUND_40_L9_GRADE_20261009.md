# ADVI_COTBKF round 40 -- L9 grade

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-09 ~14:2xZ. Packet `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_40_DRAIN_END_20261009.md @5006e7df0d (msg 3433)`. Row D2-S65.

| criterion | verdict | evidence |
|---|---|---|
| CB40an1-AC2: source_firm from the input's address via the registry, never a token; absent never defaulted to cottonwood; the census reports absent as NOT-CLEAN | MET | `build_canonical_prices_v2.py` resolves each input in `INPUT_ADDRESSES` by its bucket, then its key prefix, through `lib/opal_naming`'s registry. This seat's diff read (eb13fd505d..ff17e59776) finds no typed `cottonwood` or `cot` in the added lines. A registry that fails to load, an unresolvable input or an ambiguous bucket returns `ABSENT`, never the own firm. The census counts a missing column, a null or `absent` as NOT-CLEAN and never as the own firm, and `mixed` or another firm as BREACH |

**Note:** as built, a production run without the registry stamps every row `absent`, which is safe but NOT-CLEAN (W68-S2). The deploy cell
must ship the registry.
