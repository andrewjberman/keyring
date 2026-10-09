# ADVI_COTBKF round 35 -- L9 grade

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-09 ~12:2xZ. Packet `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_35_DRAIN_END_20261009.md @cd42e26d8a (msg 3252)`. Rows D2-S51, D2-S52.

| criterion | verdict | evidence |
|---|---|---|
| CB35ai1-AC2: the class follows from the printed keys, metadata and history by the pre-written rule, and the delete list is complete for what was scanned | MET (detector note) | The rule was committed at 5c79b91853 (07:19 ET), before the output at d322d04fcd (07:36). `bd_txn_provenance.md` prints the 38 keys with rows, their one version each, the earliest write (2026-06-09T20:42:15Z) and the code history, and the class `shared_builder_run` follows by the rule. The list is complete for the read set, which the output states was narrowed after a timeout |

**Note:** the detector, not the rule, changed after run 1 (+57/-14 lines), and that change moved the class off `live_cot_path`. It is a
principled fix: it parses code and skips docstrings and comments. It was disclosed in W63-S1. The class is also corroborated independently:
this seat read 319a716cb4 (2026-06-12), which removes the 49F-only scoped-inject auto-chain from `data/cot/scripts/gold/build_canonical_prices_v2.py`.

**What remains (D2-S52, BLOCKING):** 49F's three bond overrides still sit in 38 Cottonwood price keys. A rewrite under a pair is the clean
removal, and it is Andrew's call.
