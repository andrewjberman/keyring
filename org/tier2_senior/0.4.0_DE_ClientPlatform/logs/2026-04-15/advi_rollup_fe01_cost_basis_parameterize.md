# 0.4.0_DE_ClientPlatform — ADVI_ROLLUP.FE01 cost-basis year bucket parameterize

**Date:** 2026-04-15 (ET)
**Portal DEV commit:** `7b56698`
**TO:** `org/tier2_senior/0.4.0_DE_ClientPlatform/task_orders/ADVI_ROLLUP.FE01.de-cost-basis-year-bucket-parameterize.md`
**Status:** complete

## Change

`portal/src/pages/AdvisorIntelligence/panels/TaxCostBasisPanel.tsx`

Replaced hardcoded `EARLIEST_YEAR = 2020` with a derived value:

```ts
const RECENT_YEARS_TO_SHOW = 7
const EARLIEST_YEAR = new Date().getFullYear() - RECENT_YEARS_TO_SHOW
```

With N = 7 and currentYear = 2026, EARLIEST_YEAR = 2019 (vs. previous hardcoded 2020 — net effect: 2019 lots that previously rolled into the bucket now show as their own per-year row; 2020 is unchanged on/after 2027). Bucket label / badge already format from `EARLIEST_YEAR` and `held = currentYear - year`, so derived constant flows through unchanged.

Also updated two inline comments to reference `{EARLIEST_YEAR}` instead of literal `2020`.

## Optional secondary (not shipped)

TO offered: drop Short/Long badge on `currentYear` and `currentYear - 1` rows (mixed-term lots). Skipped to keep visual + math identical to commit `ae7b377` and minimize regression surface for the presentation. Easy follow-on if Andrew wants it — DS already emits `short_term_gain` / `long_term_gain` separately so the badge could be replaced with a Mixed pill on those rows.

## Compiler Tools

| Phase | Tool | Run | Expect | Observed | Pass/Fail |
|-------|------|-----|--------|----------|-----------|
| 1 | comp-transform schema-check | `comp-transform schema-check TaxCostBasisPanel` | Clean (no MISSING / no UNUSED) | "All rendered fields match their response types." | PASS |
| 2 | tsc | `bunx tsc --noEmit` | exit 0 | exit=0 | PASS |
| 2 | comp-transform schema-check | `comp-transform schema-check TaxCostBasisPanel` | Still clean post-edit | (re-run identical to phase 1) | PASS |
| 3 | frontend-dev Skill | `python .tools/frontend-dev.py --constitution portal/.frontend-dev/testing/cost_basis_panel.json` | PASS — bucket label '& Earlier', badge '>= N yrs', no console errors, Travis L2 panel renders | PASS on iteration 2 (iteration 1 selector miss — Travis row is a `<div class="cursor-pointer">`, not button; fixed selector to `div.cursor-pointer:has-text("Travis Penfield")`) | PASS |

Constitution authored new: `portal/.frontend-dev/testing/cost_basis_panel.json` (cost_basis_panel did not exist in `portal/.frontend-dev/testing/`).

Screenshots: `.frontend-dev-results/20260415T163152Z/` (3 PNGs: books-tab-baseline, advisor-book-l2, final-cost-basis-panel).

## Inbox + reconciliation

Session 29 startup found stale CTO + COO messages telling me to "EXECUTE NOW" all 7 ADVI_FNTEND Wave C FE TOs. Ground-truth check: all 8 ADVI_FNTEND TOs (B1/B2/B3/B4/B5/B6/B8 + D7) carry `<status>complete</status>` from the prior session (commits `1d7aa76`..`37a6cc2`). Notified both CTO and COO. No new Wave C work executed.

Then COO sent a fresh GO for ADVI_ROLLUP.FE01 — that's this log.

## Open

- `ADVI_ROLLUP.B9.de-small-account-count-column.md` — staged, awaiting DS B9 artifact landing on DEV
- PROFAU.006 — staged, gate clear, awaiting DS GO
- PROFAU.007 — staged, awaiting DS Q2 TO
