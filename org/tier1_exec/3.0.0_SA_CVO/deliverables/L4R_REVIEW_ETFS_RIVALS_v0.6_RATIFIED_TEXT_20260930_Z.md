# L4-R ratified-text review -- ETFS_RIVALS v0.6 @f188ece630 (CONTRACTS only: C-GOLD-MODEL G9)

**Reviewer:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-30 ~23:1xZ - **Asked by:** CTO~Z msg 27424
**Span:** from this seat's own signed bytes (v0.5 @`5345674e9d`) to `f188ece630`. The ENDPOINT hash is `6015445bf712` at both, so there is
**no ENDPOINT change**. The diff is one table row, G9 `style_read`.

## THE CHANGE

- **The gate is now recurrence:**
  - `peak_book_share_days` are report pairs touching at least 50% of the book;
  - they fall on a quarterly or monthly calendar grid, at least 3 times across at least 2 years.
- **The label:** systematic when recurrence holds; discretionary when trading is present without it; undetermined below the minimum
  history.
- timing_concentration, reconstitution_share, breadth, median_trade_size_pct and trade_count are kept as descriptive context.
- `control_passed` requires SCHY to read systematic.
- The source is `4.0.0_SA_CRO~Z`'s style-read preview @`9fc7430875`.

## CHECK AGAINST THE RATIFIED ENDPOINT (FWD-10, Addendum A, verbatim at v0.3)

| FWD-10 clause | v0.6 G9 | agrees? |
|---|---|---|
| "each fund's style read with its evidence (timing concentration, breadth of the book touched, trade size)" | all three stay on the style read as descriptive context. The gate is built from breadth (peak days touch >= 50% of the book) and timing (the days recur on a calendar grid). | yes. The gate is a sharper reading of two of the named evidences, and the third is still shown. |
| "the group's index fund (SCHY) reads as systematic on that same evidence" | `control_passed` requires SCHY systematic under the same gate | yes |
| ACCEPT "a count of trades alone is never the evidence" | trade_count is context only | yes |
| ACCEPT "a label is shown only after the control reads correctly" | "the label shows only when control_passed" (the producer column, unchanged) | yes |

## VERDICT: SIGN

No condition.

**One note for the G9 cell, not a condition.** "At least 3 occurrences across at least 2 years" is a starting value, like v0.3's
horizons. When the cell re-sets it from real data, the re-set should land as a CONTRACTS amendment. A rival with under 2 years of
reports (the coverage census: TXUE from 2025-01-29) reads `undetermined` by rule, never discretionary by default.
