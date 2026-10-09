# ADVI_COTBKF rounds 36 and 39 -- L9 grades

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-09 ~14:0xZ. Packet `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUNDS_36_39_DRAIN_END_20261009.md @3d68a5ab23 (msg 3412)`. Row D2-S64.

| criterion | verdict | evidence |
|---|---|---|
| CB36aj1-AC2: other_rows_identical=True on all 38; the bond rule committed before the run; no equity ticker used for a bond; the writer census complete | MET | `COT-PRICE-REWRITE ... other_rows_identical=True ... bonds_priced=0/3 writers=7 scheduled=0` and `VERIFY match=38/38`. Rule commit 4bc82c2d47 (08:44 ET) precedes the recorded run. The later fixes, fc87ae2988 (key loader) and 1a21ebbab6 (census narrowed to S3 writes on the price prefix), touch neither the bond rule nor the diff rule. rows_repriced=0, so no ticker priced a bond |
| CB39am1-AC2: the change confined to _ff_worker and what it passes; the firm label set derived, not typed; no carried price escapes the claim | MET | The diff f8b656af51..440ee24cba changes `B_00.canonical_holdings.py` (+27/-1) inside `_ff_worker`, plus the `source_firm` column it selects. `_own_firm = lookup(<tree>)['key']` is derived from the path. Every row gets `price_basis`. A prior with a present, non-Cottonwood `source_firm` is dropped from the carry, and its price and value are NaN |

**Note:** an asset that has neither a same-day nor a prior price would be stamped `carried_forward` with a NaN price. That is a label
inaccuracy, not an escape.
