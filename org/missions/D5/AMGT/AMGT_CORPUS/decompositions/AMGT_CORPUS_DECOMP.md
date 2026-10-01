# AMGT_CORPUS -- L5 decomposition v29.0 -- ROUND 29 (one face cell)

**Issuer:** `2.0.0_SA_COO~X`, 2026-10-01 ~09:0xZ. **Source:** `1.0.0_SA_CTO~Z`'s round-28 analysis
`ledger/ROUND_ANALYSIS.round28.md` @`bd50135e57` (msg 27674, READ-acked), s.2 rulings 1-3 and s.3 enrichment list (CVO v33: ad-3
AC4 PARTIAL). Round 28's decomposition is kept as `AMGT_CORPUS_DECOMP.round28.md`. Base: CLOUD `463e30ded8`, portal DEV `e8a20ba9`.
CONTRACT amendment 1 holds: `ModelTab.tsx` is CORPUS's through the freeze. **Land on portal DEV before 22:00Z.**

## 0. What this round IS

| # | item (analysis s.3) | cell | slot | FWD |
|---|---|---|---|---|
| 1 | One face cell carrying rulings 1-3: the E columns labelled "Consensus (Bloomberg)" and the header sentence replaced; decimals fixed per row type (display only); the currency stated once per name, with unmeasured rows marked and footnoted once | `CRPS-ae-1` | `~1` (worker) | 12, 20, 21 |

**Not cut:** FWD-22 (Andrew's standing word). Z-S74 carried (inert).

## 1. The rectangle

| cell | `<risk>` | write set | the build |
|---|---|---|---|
| `CRPS-ae-1` | LOCAL | `portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx`, `portal/src/pages/SecurityAnalysis/modelSheet.ts`, `__harness__/modelPattern.harness.cjs` and `__harness__/tabs.harness.cjs` (NECESSARY re-anchors only) | per the analysis s.2: header "Reported figures and Bloomberg consensus estimates, from the model block"; E columns "Consensus (Bloomberg)"; millions 0 dp with separators, per-share 2 dp, multiples 1 dp "x", percent 1 dp "%", unnamed rows 2 dp; the currency once in the Model header from the block's measured currency; rows without a measured currency marked "*" with one footnote line "currency not stated by the source for marked rows"; the full served value stays in `data-model-cell` |

## 1a. Re-grounding at L5 (measured at base; `deliverables/2.0.0_SA_COO~X/checks/round29/`)

- `face29.cjs` 2 of 6 at base. Arms 3 (full values kept) and 6 (round 28's face.cjs 9/9 and sheet.cjs 6/6) are the controls and
  pass. The decimals arm grades 144 cells over 15 printed rows. The fixture is a capture from before ad-4, so BA's DPS and some P/E
  years still read refused there; refused rows print no figure and are skipped.
- Today the face carries 4 "currency not stated" phrases, 1 row label with USD (EBITDA adjusted), 0 USD statements before the
  sheet, and no marks or footnote.
- Bound 4 of 4 at base; tsc -b rc 0.

## 5. The round -- one issuance, fan-out as data

- `fanout: 1 of 1 chains, cap 3, reason: one face cell; two files that read each other (row types belong to modelSheet.ts, display to ModelTab.tsx).`
- **Drain:** re-grade with pins read by blob; fast-forward local portal DEV; the ONE REAL RUN is BA's Model tab on 5174 (MSTR merges
  DEV into the walk checkout; ARM and DISARMED posted to `0.0.0_AB_MSTR~Z`); the L8 packet then goes to `3.0.0_SA_CVO~Z`.
- **Judgment (L9):** the CVO reads the PNG as a person: the sheet reads like the analyst's.
- Surprise rows from `Z-S76`. Worker rows are `AMGT_CORPUS-Z-W<n>-S<k>`, with `disarm_owner 2.0.0_SA_COO~X`.
