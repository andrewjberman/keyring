# Style-read preview (ETFS_RIVALS FWD-10 / PRD G9): the control passes only with a recurrence measure

Author: 4.0.0_SA_CRO~Z. September 30, 2026, ~21:xx UTC. Andrew's "Go" on `/next-calls` option 1. Local data only:
- the IDVZ-group Bloomberg census (`.runtime/etfs-rivals-idvz-20260930/daily`);
- the PFOE-group Bloomberg census (`.runtime/amgt-reconn-daily-census-20260929`);
- GQGU's issuer archive;
- the IDVZ-group dividend history for corporate actions.

Script: `scripts/style_read_preview.py`. Rules as the trade schedule: 0.2% floor, 5-share floor, pro-rata flow removed,
cash and currency lines excluded, share-changing corporate actions removed where dividend history exists.

## 1. The G9 measures as written do not isolate the index fund

Research window 2025-10-01 to 2026-09-29:

| Fund | Trades | Entries+exits | Timing concentration (top 4 weeks) | Reconstitution share (busiest month) | Median trade size | Turnover |
|---|---:|---:|---:|---|---:|---:|
| SCHY (index) | 1,924 | 97 | 0.618 | 0.577 (2026-03) | 1.87% | 1.54 |
| INEQ | 1,001 | 219 | 0.912 | 0.251 (2025-12) | 1.13% | 1.63 |
| ETFT | 175 | 31 | 0.702 | 0.516 (2026-06) | 18.04% | 2.04 |
| PCLG | 201 | 29 | 0.598 | 0.345 (2026-06) | 6.46% | 0.98 |
| TSEL | 223 | 24 | 0.580 | 0.292 (2026-06) | 8.98% | 1.36 |
| IDVZ | 352 | 27 | 0.465 | 0.185 (2026-01) | 2.91% | 0.91 |
| GQGU | 1,148 | 163 | 0.364 | 0.313 (2026-07) | 12.56% | 5.13 |
| TXUE | 412 | 29 | 0.255 | 0.276 (2026-03) | 4.94% | 0.56 |
| BIDD | 673 | 50 | 0.261 | 0.180 (2025-10) | 2.36% | 1.51 |
| CGIC | 5,133 | 181 | 0.202 | 0.144 (2026-03) | 1.50% | 1.44 |
| BASG | 683 | 16 | 0.188 | 0.188 (2026-03) | 0.95% | 0.94 |
| WCMG | 63 | 5 | 0.914 | 0.800 (2026-09) | 2.82% | 0.27 |

SCHY is not the extreme on either concentration measure: INEQ's timing concentration is higher, and ETFT's busiest-month
share is close. The June 2026 clusters (ETFT, PCLG, TSEL) are not identifier churn: a value-matched check found 0
probable ID swaps in every fund. A label gated on these measures would fail its own control. (WCMG's window is short,
since Bloomberg's history starts 2026-04-23, and it has only 5 entries or exits.)

## 2. The separator: whole-book trading days that recur on a calendar grid

Report pairs in which the fund traded at least 50% of its book, across each fund's full census span:

| Fund | Whole-book days (share of book, date) | Reading |
|---|---|---|
| **SCHY** | 0.93 2024-12-23 · 0.88 2025-03-24 · 0.69 2025-06-23 · 0.67 2025-09-22 · 0.95 2025-12-22 · 1.02 2026-03-23 · 0.96 2026-06-22 · 0.95 2026-09-21 (and 0.71 2026-01-15) | **Quarterly, on the Monday after the third Friday of Mar/Jun/Sep/Dec: an index rebalance. Control passes.** |
| **INEQ** | 0.72 2025-02-28 · 0.99 2025-05-30 · 0.65 2025-08-29 · 1.00 2025-09-02 · 0.92 2025-09-04 · 0.67 2025-11-28 · 0.52 2025-12-01 · 0.93 2026-03-02 · 0.88 2026-06-01 · 0.75 2026-09-01 · 0.65 2026-09-03 (and 0.58 2024-11-29) | **Quarterly around quarter-month end: a rules-based rebalance. Reads systematic.** |
| GQGU | 0.84 2026-01-06 · 0.65-0.79 on four days in July 2026 | event-driven rotations, no calendar recurrence |
| TSEL | five scattered days, 0.52-0.89 | no recurrence |
| CGIC | 0.53 2026-02-19 · 0.52 2026-08-06 | no recurrence |
| BIDD | 0.95 2024-11-15 | launch build, once |
| ETFT | 0.67 2026-06-29 | once |
| BASG | 0.50 2026-07-17 | once |
| IDVZ, TXUE, PCLG, WCMG | none | no whole-book days |

## 3. Proposed G9 change (for the CTO's PRD)

Add `peak_book_share_days` (every report pair touching at least a threshold share of the book, with dates) and
`recurrence`: whether those days fall on a regular calendar grid (quarterly or monthly spacing), at least three
occurrences across at least two years.
- **Label systematic** when recurrence holds.
- **Label discretionary** when trading is present without recurrence.
- **Label undetermined** below a minimum history.

The control is that SCHY must read systematic, and on this data it does. Timing concentration, reconstitution share,
breadth and size stay as descriptive context, not as the gate. Thresholds (50% of book, three occurrences) are this
preview's settings, to be fixed in the PRD.

## 4. Gaps

- **PFOE (home fund) is not measured.** Its one-year Bloomberg census (`.runtime/etfs-rivals-pfoe-home-20260930/`)
  returned `#N/A Connection` on every date because the Bloomberg connection was down during the run (checked
  afterwards: no blpapi session on 127.0.0.1:8194, Terminal not logged in). This is a connection failure, not a coverage
  finding.
- PFOE-group corporate actions were not applied (no dividend pull for that group yet).
- INEQ's style comes from its holdings pattern alone; its stated process was not checked.
