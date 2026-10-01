# AMGT_CORPUS -- ROUND 28 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-10-01 ~08:5xZ

**Input:** CVO slug msg 27671, `ADJUDICATION_v33.md` @46a4402b2a (3 of 3 terminal plus the ad-4 ledger CLOSED; ad-3 AC4
PARTIAL). PRD v0.7 ADMITTED. CONTRACT amendment 1: `ModelTab.tsx` is CORPUS's through the freeze (22:00Z).

## 1. WHAT THE ROUND DELIVERED

BA's Model tab now has the analyst sheet's SHAPE:
- one fiscal grid, 2016-2025 plus 2026E-2028E;
- the EBITDA block;
- the team-case lines.

The score tiles, rule lines and "Other lines" are gone. The 5 formerly null rows carry figures. DPS shows (ad-4: refused
fiscal figures 364 -> 10).

**Round 28 is CLOSED.**

## 2. RULINGS (the three face items, CVO v33 section 1)

| # | ruling | why |
|---|---|---|
| 1 | **Label the E columns as consensus.** The header sentence "nothing estimated in its place" is REMOVED. The 2026E-2028E columns carry the label "Consensus (Bloomberg)", and the header reads "Reported figures and Bloomberg consensus estimates, from the model block". | The columns ARE Bloomberg BEST consensus fields. A sentence that denies estimates above estimate columns is a contradiction on the demo face. |
| 2 | **Fix decimals per row type, for display only; values unchanged.** Amounts in millions: 0 dp, with thousands separators. Per-share figures: 2 dp. Multiples (P/E, P/B, EV/EBITDA): 1 dp with "x". Percentages and margins: 1 dp with "%". A row whose type the sheet does not name falls back to 2 dp. | The analyst's sheet fixes decimals per row; the served value stays the full float, and the tooltip may show it |
| 3 | **State the currency once per name.** It comes from the block's MEASURED reporting currency in the Model header (e.g. "USD"), and row labels drop currency words. A row whose currency the block marks UNMEASURED carries one footnote mark, with a single footnote line ("currency not stated by the source for marked rows"), never the words repeated per row. | A value carries its claim, and it is stated once. No row claims a currency the block did not measure. |

Z-S74 is CARRIED (inert). FWD-22's scheduled re-pull still waits on Andrew's standing word.

## 3. THE ENRICHMENT LIST -- round 29, `2.0.0_SA_COO~X`, ONE issuance

One face cell in `ModelTab.tsx` and `modelSheet.ts` carries rulings 1-3. Its criteria:
1. BA's Model PNG shows "Consensus (Bloomberg)" on the E columns and no "nothing estimated" sentence.
2. No figure on BA's grid prints more decimals than its row type allows, and the full values are still in the served
   payload.
3. One currency statement in the header; 0 repeated "currency not stated" phrases; one footnote line where any row is
   marked.

**L9 (CVO, as a person):** the PNG reads like the analyst's sheet. **Land it on portal DEV before 22:00Z.**

## 4. ACTS ONLY ANDREW CAN DO (cited)

1. **A standing word for the scheduled CORPUS re-pull** (CLAUDE.md vendor per-use word; FWD-22).
2. **Sign in to the Bloomberg Terminal on site Z** (his login).
