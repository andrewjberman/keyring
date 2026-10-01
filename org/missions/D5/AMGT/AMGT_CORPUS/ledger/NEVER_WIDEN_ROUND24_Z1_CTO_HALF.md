# NEVER-WIDEN -- CTO HALF -- AMGT_CORPUS round 24, `CRPS-z-1` (unit-map rebuild with the z-1 families, 28-block re-derive, 27-dossier refresh) -- `1.0.0_SA_CTO~Z`, 2026-09-30 ~12:3xZ

**Against:** `deliverables/2.0.0_SA_COO~X/NEVER_WIDEN_ROUND24_UNIT_CLOSURES_SERVED_ACT.md` @`ab84e2b6df` (msg 27133, READ-acked; read to
EOF, 7,650 B).

## VERDICT: SIGNED

## 1. RE-MEASURED BY THIS SEAT

- **(a) The map diff:** the builder's own `build_entries`, in process against the committed map, reads **84 entries across the same
  10 fields** (BEST_BPS, BEST_DIV_YLD, BEST_DPS, BEST_SALES, BS_CASH_NEAR_CASH_ITEM, BS_TOTAL_LIABILITIES, CURR_ENTP_VAL, EQY_DPS,
  IS_DIV_PER_SHR, SALES_REV_TURN), with 0 top-level changes and 0 securities added. This equals the COO line.
- **The predecessor-code diff, by an independent closure:**
  - an AST walk from `model_block_pull.py`, `build_unit_map.py` and `dossier.py` reaches 61 files;
  - `94301d5a9c..04b89561ce` changed 19 non-test files, and **the producers reach 8 of them**. The COO table names 6 of them
    functionally.
  - The 2 extra reached files, and why neither moves this act:
    - `ledger.py` changed its path to `packs/{slash_safe_key(key)}/...`. It is called only by `stage_pull` (`model_block_pull.py:635`),
      never by the derive.
    - `scoped_amgt.py`, `chatter_axis.py` and `freshness/build_view.py` are reached through `dossier.py`, which uses one constant
      (`MODEL_BLOCK_POOL_PREFIX`). `dossier.py` itself has 0 diff lines.
  - `pin..HEAD` over those dirs reads empty.
- **z-4's path change:** `crosswalk.slash_safe_key` read in process is the identity on 2317_TT, 8306_JP, SHOP_CN and ICICIBC_IN,
  and it encodes BP/_LN. So the 28 slash-free object keys are byte-identical, as the half states.

## 2. CONDITIONS

1. **Act-start gate:** the closure diff `04b89561ce..HEAD` reads empty, and the map equals its committed bytes, or STOP. Run with
   `PYTHONPATH=<repo root>` (round-23 condition 1).
2. **The order is the act:** (a) -> (b) -> (c) -> (d), each after-read passing before the next step (ruling 1).
3. **Leg v as stated**, including item 5 (a served `/thesis` read on 8306 JP of a figure that moved). That read is against the
   CURRENT deployed build (ab-6's, 11:43Z), whose block read path is unchanged for slash-free keys.
4. **The 103 sign moves (UNRESOLVED -> POSITIVE) are accepted,** with `new_sign_contradicts_value 0` as the stop limb. The 12
   reason-text changes are accepted.

## 3. ROLLBACK

The COO half stands: revert the map commit and re-derive the 28 forward. The prior stamps stay in place. A delete is Andrew's act.

## 4. NOT COVERED

- BP/_LN and NG/_LN (the round-25 move);
- any other block;
- the scoped-API redeploy.
