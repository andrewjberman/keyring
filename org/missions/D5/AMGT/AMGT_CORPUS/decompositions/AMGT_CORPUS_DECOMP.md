# AMGT_CORPUS -- L5 decomposition v33.0 -- ROUND 33 (Z-S81: the percent family decided by a ground, never by magnitude)

**Issuer:** `2.0.0_SA_COO~X`, 2026-10-02 ~16:5xZ.

**Source:** `1.0.0_SA_CTO~Z` round-32 analysis `ledger/ROUND_ANALYSIS.round32.md` @`ac45eeeef8`, which closes round 32.
- **Enrichment list:** 1 item, Z-S81 per rulings 1 and 2.
- **Ruling 1:** each mnemonic is decided by a GROUND. EQY_DVD_YLD_IND reads against EQY_DPS / PX_LAST. The returns and the margin
  read their statement inputs, or the series-median rule where a series exists. Where no ground exists, the label becomes
  UNRESOLVED, not DECIMAL.
- **Ruling 2:** the act shape copies ah-3 -- a dry run over every key, the per-key map diff, a scoped remeasure, negative arms,
  and the reach named in the COO half.
- **Ruling 3:** the disarm owner is this seat; the CTO half is owed on the dry run.

Round 32's decomposition is kept as `AMGT_CORPUS_DECOMP.round32.md`. Base: CLOUD `a0a7214220`.

## 0. What this round IS

| # | item | cell | path | risk |
|---|---|---|---|---|
| 1 | The ground reads in `build_unit_map` for a percent-family value under the 0.3 line | `CRPS-ai-1` | **DIRECT ACT** | LOCAL |
| 2 | A scoped remeasure of the 11 DECIMAL-labelled names, ONE re-derive each, and their dossiers | `CRPS-ai-2` | the issuer's paired act after ai-1 | SERVED |

There is one chain, `ai-1 -> ai-2`: ai-2's map reads ai-1's code.

## 1. Measured at the cut (`build_unit_map.load_raw_for_key` per name, `series_median_abs`, the map entries; read 16:4xZ)

| figures | names | the ground | expected label |
|---|---|---|---|
| 30 | BP/ LN: RETURN_ON_ASSET, RETURN_COM_EQY, RETURN_ON_TANGIBLE_ASSETS | **the series-median rule (round 26)**. Series medians are 1.33, 3.78 and 1.48. The map entries are single samples from 09-16 (0.0196, 0.0962, 0.0212) that a clean MEASURED entry never re-reads. | PERCENT |
| 10 | JD_US: OPER_MARGIN | the series median: 1.06 (the entry sampled 0.2119) | PERCENT |
| 20 | ORA_FP and RWE_GR: RETURN_ON_INV_CAPITAL | the series median: ORA 4.47; RWE's series reads -18.2 .. 4.0 | PERCENT |
| 13 | HEI, MELI and PWR: EQY_DVD_YLD_IND | **NEW in ai-1:** each fiscal row's own identity, EQY_DPS / PX_LAST, both carried per row. Series medians are 0.13, 0.19 and about 0.3, under the line. | decided by the rows |
| 4 | AZN, RKT, TTE and ULVR: SI_PERCENT_EQUITY_FLOAT (header only, 0.006 .. 0.020) | **none.** SHORT_INT_RATIO x VOLUME_AVG_30D over the free float gives AZN 4.15% (0.0415) against the served 0.0101, so it reconciles neither way. | **UNRESOLVED** (ruling 1) |

So 60 of the 77 need no new rule: they need the remeasure the series rule already implies.

## 2. The cells

**CRPS-ai-1 (the ground reads).**
- `classify_unit` gains an optional `hist_rows`, which `build_entries` passes.
- In the percent branch, for 0 < |v| < 0.3:
  - BEST_DIV_YLD keeps ah-2's identity.
  - EQY_DVD_YLD_IND reads its fiscal rows. Each row carrying a non-zero yield, a positive EQY_DPS and a positive PX_LAST is tested
    against `EQY_DPS / PX_LAST x 100` (PERCENT) and `EQY_DPS / PX_LAST` (DECIMAL) within `RECONCILE_TOLERANCE`, on the same-currency
    gate.
  - The label is the hypothesis every computable row agrees on. No computable row, or a split, gives UNRESOLVED with the cause.
  - Every other percent field under the line gives **UNRESOLVED** ("magnitude under 0.3 does not discriminate percent vs decimal;
    no ground is defined for <mnemonic>").
- |v| >= 0.3, an exact zero and the series-median input are unchanged.
- Check: `checks/round33/ai1_check.py`. At base: build 0/4 + control 4/4 (as expected). The act must reach build 4/4 + control 4/4,
  with the build_unit_map tests green.

**CRPS-ai-2 (the paired SERVED act).** After ai-1:
1. A serializing dry run over every key with `--securities <the 11> --remeasure`: HEI, MELI, PWR, JD, ORA, RWE, BP/ LN, AZN, RKT,
   TTE, ULVR.
2. The COO half names the dry run's whole reach, every mnemonic of those 11 names, as ah-3 named GOOGL.
3. The CTO half, owed by `1.0.0_SA_CTO~Z` (ruling 3).
4. One NEVER-2 entry, `amgt-corpus-r33-ai2`, with the legs ah-3 used: gate, a, b, c, d, v.

The negative arms include a figure whose ground confirms DECIMAL staying DECIMAL. One is printed if the dry run finds one;
otherwise the arm is named as having no member, with its count.

## 5. Close

- `fanout: 0 worker chains of 1, cap 3, reason: ai-1 is one LOCAL cell under the size floor (the issuer's direct act); ai-2 is the issuer's paired act and spawns no worker.`
- `checks: ai1 base: build FAIL 0/4 + control PASS 4/4 as expected (checks/round33/ai1_check.py).`
- **Real run:** ai-2's served census over 100 keys. DECIMAL-by-magnitude must reach 0 for the 77, beside the negative arms. The
  L8 packet then goes to `3.0.0_SA_CVO~Z`.
