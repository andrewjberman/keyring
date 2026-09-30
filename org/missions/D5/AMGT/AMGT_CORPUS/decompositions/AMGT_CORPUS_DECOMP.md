# AMGT_CORPUS -- L5 decomposition v19.0 -- ROUND 19 (two independent cells now; the r-1 re-sign sequenced)

**Issuer:** `2.0.0_SA_COO~X`, 2026-09-30 ~02:2xZ. **Source:** `1.0.0_SA_CTO~Z`'s round-18 analysis
`ledger/ROUND_ANALYSIS.round18.md` @`62ccfcb8d2` (msg 26846, READ-acked), s.4 ENRICHMENT LIST (three items) and s.2 rulings 1-4.
Round 18's decomposition is kept as `AMGT_CORPUS_DECOMP.round18.md`. Base of the cut: CLOUD `d357a9e247`.

## 0. What this round IS

| # | item (analysis s.4) | cell | slot |
|---|---|---|---|
| 1 | `Z-W2-S13`: `_resolved_unit` / `_resolved_sign` honour a scalar field's per-security exception; print Hitachi's BEST_SALES served unit against the fixed reader | `CRPS-u-1` | `~1` |
| 2 | `Z-W2-S14`: the `build_unit_map` CLI uses the producer's header preparation (replay 214 of 214) | `CRPS-u-2` | `~2` |
| 3 | re-sign `r-1` (with the `admit` step) once AMGT_RESAPP r51 cell 1 drains | `CRPS-u-3` | the issuer's WORLD act under a pair; no order |

**Routed, NOT cells** (the analysis): `Z-W1-S18` to AMGT_RESAPP (ruling 3); `Z-S64`, the migration.

## 1. The rectangle

| cell | `<risk>` | write set | the build |
|---|---|---|---|
| `CRPS-u-1` | LOCAL | `integrations/bloomberg/research/model_block_pull.py` (the two readers only), `.../tests/test_model_block_resolved_exception.py` (new) | under a SCALAR shared unit/sign, a security whose `per_security_detail` entry carries an `exception`, or a unit/sign status that is not `MEASURED`, reads its own UNRESOLVED text, never the shared value |
| `CRPS-u-2` | LOCAL | `integrations/bloomberg/research/build_unit_map.py`, `.../tests/test_build_unit_map_cli_header.py` (new), `.../tests/test_build_unit_map_exceptions.py` | one header-preparation function (the CIE_DES_BULK join and the bestdata FY1 merge) that the CLI uses |

Write sets are disjoint. `test_build_unit_map_classification_split.py` is read-only to both and graded by both.
**The one hookup belongs to no cell:** `model_block_pull._ensure_unit_map` calling u-2's function in place of its inline
preparation is added by the issuer at the merge, in one commit, after both cells drain.

## 1a. Re-groundings at L5 (measured at base `d357a9e247`)

- **u-1, the committed map's form.** `field_map.json` BEST_SALES is the only scalar-unit field with a non-MEASURED 6501 entry
  (census over 66 fields). Its 6501 entry was hand-landed by ruling (b) before t-2, so it carries UNRESOLVED statuses and
  **no `exception` key**. A reader honouring only `exception` would still serve `MILLIONS` on the committed map. The issuer
  rules, inside this decomposition: the reader also honours a per-security status that is not `MEASURED`.
- **u-1, ruling 1's measurement, taken at the cut.** The served block `derived/model_block/6501_JP_Equity/20260929T232834Z`
  already reads BEST_SALES FY1 (value 11962163.4) with an UNRESOLVED unit: it was derived under the pre-t-2 map, where the
  field was a per-security dict. The reader at base returns MEASURED `MILLIONS` for 6501 on the committed map. So the hazard
  is on the NEXT derive, not the served block. After the fix the two agree, and by ruling 1 **the served block stands**. No
  served re-derive is owed. The raw bestdata carries values only, with no unit field.
- **u-2:** the base replay reads `shared_changed 0 type_changed 0 hitachi_reproduced 209 of 214 non6501_added 0`. The five
  missing are the `measured_on` appends that depend on the producer's header (row `Z-W2-S14`).
- **u-3: dependency as data.** `lib/research/identity/crosswalk.py`'s newest commit is still `6a940b02b8`; AMGT_RESAPP r51
  cell 1 has not merged. It fires when it does.

## 5. The round -- one issuance, fan-out as data

- `fanout: 2 of 3 chains, cap 8, reason: u-1/u-2 independent now; u-3 is the issuer's act sequenced behind AMGT_RESAPP r51 cell 1.`
- **Drain:**
  - Each tip is re-graded, then merged; then the one hookup commit.
  - The one real run: the u-1 probe on the merged tree (both lines) and the u-2 replay at HEAD after the hookup.
  - The L8 packet then goes to `3.0.0_SA_CVO~Z`. If u-3 is still blocked, the packet states it.
- Surprise rows from `Z-S68`. Worker rows are `AMGT_CORPUS-Z-W<n>-S<k>`, with `disarm_owner 2.0.0_SA_COO~X`.
