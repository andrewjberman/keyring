# AMGT_CORPUS -- L5 decomposition v30.0 -- ROUND 30 (one page-only cell, taken as the issuer's DIRECT ACT)

**Issuer:** `2.0.0_SA_COO~X`, 2026-10-01 ~09:5xZ. **Source:** `1.0.0_SA_CTO~Z`'s round-29 analysis
`ledger/ROUND_ANALYSIS.round29.md` @`499e53e2bf` (msg 27720, READ-acked): round 29 CLOSED, O5 MET; ruling 1 = round 30. Round 29's
decomposition is kept as `AMGT_CORPUS_DECOMP.round29.md`. Base: portal DEV `1f059ad1`.

## 0. What this round IS

| # | item | cell | path | FWD |
|---|---|---|---|---|
| 1 | Replace the footer "147 of 342 fiscal figure(s) on the block rendered; 0 sheet row(s) not in the pack" with "Showing 147 fiscal figures from the model block". Nothing on the face says "not in the pack" or reads as a loss | `CRPS-af-1` | **DIRECT ACT** (LOCAL, one file, 4 lines; under the size floor) | 12, 20 |

**Deferred past Friday (analysis s.2):** BEST_DIV_YLD's "DECIMAL" producer label (it needs a pair; the page is value-correct), and
Z-S74. FWD-20's 49 template rows and FWD-22 wait on Andrew's vendor words.

## 1. The cell, as done

- `portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx` (portal `2a0e1b7a` on branch `wk-AMGT_CORPUS-291-portal`; local DEV
  fast-forwarded 1f059ad1 -> 2a0e1b7a). The analysis names one phrase. The same presupposition sat in two sibling lines of the
  same footer, so all three were neutralised, with every anchored attribute kept:
  - the count: "Showing N fiscal figures from the model block" (`data-model-fiscal-cells` unchanged);
  - the estimate-years line: "...: no consensus estimates are served for this name; the model block carries fiscal years A to B"
    (`data-model-absence` unchanged);
  - the absent-rows footnote: "No figures served for: X" (`data-model-absent-footnote` and its row names unchanged).
- **Graded by `checks/round30/face30.cjs`:**
  - base 1f059ad1: 1 of 4 (arm 4, round 29's face29.cjs, is the control);
  - after: 4 of 4;
  - full page suite 15 of 16 (posture RED on DEV too); tsc -b rc 0.

## 5. Close

- `fanout: 0 worker chains, cap 3, reason: the one cell is under the size floor and LOCAL -- the issuer's direct act.`
- **Real run:** BA's Model tab on 5174 once the walker is free (the laptop walks first, MSTR msg 27721) and MSTR merges DEV
  2a0e1b7a into the walk checkout. ARM and DISARMED are posted to `0.0.0_AB_MSTR~Z`. The L8 packet then goes to `3.0.0_SA_CVO~Z`.
