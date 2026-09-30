# IDVZ rival group: source census and trade-inference preview

Author: 4.0.0_SA_CRO~Z. Measured September 30, 2026, ~11:0x-11:3x ET. Andrew's direction and the source email thread are
recorded verbatim in `ANDREW_DIRECT.md` ("IDVZ rival group"). Research only; nothing was built or scheduled.

**Group (Adam Muller, 2026-09-29):** IDVZ (Opal's own fund), TXUE (Thornburg International Equity), BIDD (iShares
International Dividend Active), CGIC (Capital Group International Core Equity), INEQ (Columbia International Equity
Income), SCHY (Schwab International Dividend Equity, an index fund).

## 1. Bloomberg covers the whole group, daily, with share counts

Current holdings (Excel BQL, 2026-09-30): all six returned full books with a quantity on every row and weights summing
to 100% (IDVZ 44, TXUE 51, BIDD 49, CGIC 224, INEQ 138, SCHY 156 rows). IBM price control passed.

Daily census, one multi-fund dated request per NYSE trading day, 2024-09-30 to 2026-09-29 (501 requests, 0 errors;
script `scripts/bbg_daily_coverage_census_multi.py`; raw responses device-local under
`.runtime/etfs-rivals-idvz-20260930/daily/`):

| Fund | First date returned | Days with a report dated that day | Longest carried-forward run |
|---|---|---|---:|
| SCHY | 2024-09-30 (window start) | 501 / 501 | 0 |
| INEQ | 2024-09-30 (window start) | 498 / 501 | 1 |
| CGIC | 2024-09-30 (window start) | 496 / 501 | 4 |
| BIDD | 2024-11-12 | 464 / 470 | 1 |
| IDVZ | 2024-12-27 | 438 / 439 | 1 |
| TXUE | 2025-01-29 | 417 / 419 | 1 |

This group is far cleaner than the PFOE group (TSEL had a 37-day stale run). The first dates for BIDD, IDVZ and TXUE were
not checked against legal inception. One row per fund can carry an older report date inside an otherwise fresh day
(TXUE `9996651D`, INEQ `SUNB`, SCHY `CCH LN` at 0% weight): a lingering line, not a stale book. Keying days on the modal
report date gave identical counts.

**Consequence:** no issuer archive is needed to backfill this group; Bloomberg covers two years or each fund's full
Bloomberg history.

## 2. Issuer pages (daily route)

| Fund | Issuer file | Result |
|---|---|---|
| TXUE | Thornburg daily xlsx (`TH6452_C-holdings-etfs.xlsx`, sheet "ETF Intl Equity") | Works: as-of date, Shares, Market Value, Percent; 50 positions summing to 100%. Current day only, no archive |
| SCHY | schwabassetmanagement.com `/allholdings/SCHY` | HTTP 403 to a scripted request |
| INEQ | Columbia Threadneedle full-holdings page | Page renders client-side; no data in the served HTML |
| CGIC | Capital Group fund page | Has a "Daily Holdings" link; data endpoint not located |
| BIDD | iShares holdings CSV endpoint | Returned the HTML page, not a CSV |
| IDVZ | Opal's own | Already collected by the TrueShares route and by Bloomberg |

Only TXUE's issuer file is proven. Four more adapters would need endpoint work before an issuer-first daily run covers
this group.

## 3. Trade inference preview (same method as `TRADE_INFERENCE_FEASIBILITY.md`, 0.2% floor)

The flow model holds for all six: position ratios sit on the day's flow factor (median spread 0.0).

| Fund | Position-days explained by flow | Events per report pair | Median trade (% of position) | Median share of book traded per day | Entries+exits (window) |
|---|---:|---:|---:|---:|---:|
| TXUE | 96.66% | 1.77 | 4.0% | 2.0% | 44 |
| IDVZ | 96.53% | 1.83 | 5.0% | 2.2% | 117 |
| INEQ | 96.58% | 4.81 | 4.8% | 0.0% | 657 |
| BIDD | 92.62% | 3.60 | 3.1% | 4.2% | 151 |
| SCHY | 86.95% | 17.79 | 2.1% | 6.9% | 220 |
| CGIC | 88.21% | 23.47 | 2.3% | 10.2% | 1,199 |

**The systematic control does not look quiet.** SCHY, an index fund, trades on every report pair, because small
non-pro-rata basket adjustments clear the 0.2% floor. Its signature is timing instead: entries and exits concentrate in
March (58 in 2026-03, 44 in 2025-03), consistent with an annual index reconstitution. The discretionary managers (TXUE,
IDVZ) make fewer, larger, narrower trades. So a discretionary-versus-systematic read must use timing concentration,
breadth and size, not trade counts. Two readings need a check before they are trusted: CGIC's very high breadth (likely
Capital Group's multi-manager sleeve structure, an inference) and INEQ's 657 entries and exits against about 104 names
(possibly identifier churn or small positions flickering in and out).

## Not claimed

Legal inception dates; issuer publication times; identifier-level reconciliation; the causes of the CGIC and INEQ
patterns; any production readiness.
