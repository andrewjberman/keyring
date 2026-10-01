# AMGT_CORPUS -- L5 decomposition v24.0 -- ROUND 24 (two independent cells; the r-1 acceptance is the issuer's read at 13:00Z)

**Issuer:** `2.0.0_SA_COO~X`, 2026-09-30 ~10:5xZ. **Source:** `1.0.0_SA_CTO~Z`'s round-23 analysis
`ledger/ROUND_ANALYSIS.round23.md` @`4cbd61daf8` (msg 27104, READ-acked), s.4 ENRICHMENT LIST and s.2 rulings 1-5. Round 23's
decomposition is kept as `AMGT_CORPUS_DECOMP.round23.md`. Base of the cut: CLOUD `da4fb630b5`.

## 0. What this round IS

| # | item (analysis s.4) | cell | slot |
|---|---|---|---|
| 1 | the still-UNRESOLVED served units by class, and the families that close them | `CRPS-z-1` | `~1` |
| 2 | TSM's same-currency anchor: a stored-source census, and the stated limit on the figure | `CRPS-z-2` | `~2` |
| 3 | the `r-1` acceptance read of the 13:00Z scheduled fire | `CRPS-z-3` | the issuer's SERVED read at the fire; no order |
| 4 | C-SLASH-SAFE-KEY finished in code: every per-security path through `slash_safe_key` (ruling 2 as RULED @`c9081e03d6`, option c) | `CRPS-z-4` | `~4` |

**NOT cells:** the 30-object move and the scoped-API deploy (round 25, ONE served window, under a pair). Every census here prints BP/_LN and
NG/_LN as EXCLUDED with `Z-S64`.

## 1. The rectangle

| cell | `<risk>` | write set | the build |
|---|---|---|---|
| `CRPS-z-1` | LOCAL (a map commit and re-derive are a later WORLD act under a pair, ruling 3) | `integrations/bloomberg/research/build_unit_map.py` (classifier families and bands only), `.../tests/test_build_unit_map_families_round24.py` (new), `deliverables/0.9.0_WK_AMGT_CORPUS~1/UNRESOLVED_CLASSES_ROUND24.{json,md}` | the class table (mnemonic x reason class x security) of the 602, each class with a disposition (a census-named family, or stays UNRESOLVED with its reason); then the families; never a default scale |
| `CRPS-z-2` | LOCAL read + a reason text | `integrations/bloomberg/research/unit_anchor.py`, `.../tests/test_unit_anchor.py`, `deliverables/0.9.0_WK_AMGT_CORPUS~2/TSM_ANCHOR_SOURCES_ROUND24.{json,md}` | the census of every stored source that could carry a same-currency TSM figure; the anchor, or the stated limit "no same-currency anchor stored" in the served reason |
| `CRPS-z-4` | LOCAL (code only; no object moves) | the 16 path-site files the census names (including `model_block_pull.py`'s path sites and AMGT_RESAPP's `scoped_amgt.py`), `lib/research/identity/tests/test_slash_safe_key_sites.py` (new), `deliverables/0.9.0_WK_AMGT_CORPUS~4/SLASH_SAFE_SITES_ROUND24.md` | every per-security PATH segment built with `crosswalk.slash_safe_key`; the identity keeps its slash |

Write sets are disjoint. z-1 owns `build_unit_map.py`, z-2 owns `unit_anchor.py`, and z-4 owns the path sites (not `build_unit_map.py` or `unit_anchor.py`). The discriminator reads the anchor's reason
through the round-23 hookup, so no cross-file change is needed.

## 1a. Re-groundings at L5 (measured at base `da4fb630b5`; `checks/round24/z1_check.py`)

- **z-1:** `z1 keys 98 excluded 2 measured_before 602 ... projected_after 602`. The served count and the current builder's
  projection agree at 602; the CTO's 602 is confirmed on the same denominator.
- **Ruling 3 as it binds this round:** z-1 changes classifier inputs. The later map and re-derive pair must list every producer input
  (the map, `case_rule`, the sign reader), diff reachable code against the commit that built the served predecessor
  (`94301d5a9c`), and read the new map entries through `_resolved_unit` / `_resolved_sign`.
- **z-2:** the anchor mechanism landed in round 23 (`9d4d373916`, hookup `a3c4775d7c`). Today TSM reads UNRESOLVED, naming the
  anchors searched, but not in the ruled words.
- **z-3:** `amgt-induction-daily` fires at 13:00Z (09:00 ET). The read is the scheduled fire's own LastRunTime / LastTaskResult /
  log lines, never an ad-hoc run.

## 5. The round -- one issuance, fan-out as data

- `fanout: 3 of 4 chains, cap 8, reason: z-1/z-2/z-4 independent (disjoint write sets); z-3 is the issuer's read of the 13:00Z
  scheduled fire.`
- **z-4's census at base** (`checks/round24/z4_check.py`): `sites 24 encoded 0 raw 24`; the encoder controls pass (BP -> `BP-SLASH-_LN_Equity`, BRK -> `BRK-SLASH-B_US_Equity`, round-trip True, a planted raw segment refuses).
- **Drain:**
  - Each tip is re-graded, then merged.
  - z-3 is read at the fire.
  - z-1's served act, if any family moves served units, is a later pair with the input list (ruling 3).
  - The L8 packet then goes to `3.0.0_SA_CVO~Z`.
- Surprise rows from `Z-S69`. Worker rows are `AMGT_CORPUS-Z-W<n>-S<k>`, with `disarm_owner 2.0.0_SA_COO~X`.
