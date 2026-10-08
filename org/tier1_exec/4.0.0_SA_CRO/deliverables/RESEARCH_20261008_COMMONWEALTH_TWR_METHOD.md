# RESEARCH -- what Commonwealth's computed TWR includes: fees, dividend dating, sweeps and cash (ADVI_COTBKF round 24)

**archetype:** EXPLORE
**Author:** 4.0.0_SA_CRO~DELL2, 2026-10-08
**Ask:** 1.0.0_SA_CTO~DELL2 msg 1708 ([SELF-DRIVE dell2] design fork). Ref:
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~45/divfee/sweep_regrade.md`, read in worktree
`C:/dev/wk-cotbkf-45` @73c3c05d3b (not yet on the shared tree).
**Read here:** the bronze ClientDelivery zip (`commonwealth/cottonwood/bronze/portfolio_accounting/date=2026-06-23/`).
No Commonwealth or Advent methodology document is in the delivery or the repo. Every rule below is inferred from the bytes,
and each says so.

## Recommendation (one method)

Rebuild Commonwealth's monthly figure as a **daily-valued, geometrically linked TWR on the whole account, cash and sweeps
included, net of investment-management fees only, with dividend income recognized on the ex-date.** Then prove the
dividend-date leg with ONE discriminating arm (section 2) before adopting it.

| leg | rule | claim |
|---|---|---|
| fee: `man` | a return drag inside the account, not a flow | inferred (measured fit: `man` turns 112 DIFF months MATCH) |
| fee: `ManAltT` / `ManAltF` | `ManAltT` (fee owed by this account, paid elsewhere) = drag on the owing account; `ManAltF` (paying account's withdrawal) = external flow out | inferred (paired 1,012 / 1,012 rows) |
| fee: `ManCheck` | drag on the owing account (the fee is still the account's, paid by check) | inferred, untested (124 rows) |
| other charges: `fch` IRA maintenance, `genmain`, `fee` IRA expense, `misc`, `csltfee`, `pcf` | external flows (withdrawals), not drags | inferred (measured fit: `fch` never turns a DIFF month MATCH, 0 of 24, and turns 25 MATCH months DIFF) |
| `12b1` (1,466 rows, all credits to cash) | income | inferred, untested |
| dividends `dv`/`dvr`/`dvlt`/`dvst`, interest `int` | income; dividends recognized at **ex-date** (to be proved, section 2) | the file dates them by pay date (measured) |
| sweeps (`FDIC66606`, `FDIC66853`) and `CFNCASH` | one cash position at par inside the account; moves between them are internal | inferred |
| flows | `li`/`lo`, `ci`, `trfi`/`trfo`/`TRFIR`/`trci`/`trco`, `ManAltF`, the charges above | measured codes; treatment inferred |

## 1. "NetofFees": net of investment-management fees only

- **The file carries only one side.** All 88,654 rows read `PerfType=TWR`, `NetGross=True`, `Annualize=False`. Periods:
  Month 80,709; Year 6,425; InceptionToDate 1,520; 1,519 accounts. There is no gross series, so the fee cannot be
  measured by difference (measured).
- **The figures are a true linked TWR.** Values are percent to 2 decimals. For 4,054 full calendar years with all 12
  months, the compounded months equal the Year row within 0.1 point in 4,050 and within 0.02 point in 3,759; the residual
  is rounding (measured). So a monthly grade at tolerance 0.05 sits just above rounding error.
- **Which fees.** Every fee is a debit on the cash line (`Security_Description` "Cash Credit (Debit) Balance"): `man`
  19,753 rows (18,769 debits, 984 credits, the credits being refunds), `fch` 2,301, `ManAltF`/`ManAltT` 1,012 each,
  `genmain` 872, `fee` 281, `ManCheck` 124 (measured). The round-24 variants table (`sweep_regrade.md:1309-1318`) is the
  evidence: `man` alone fits, and adding `fch` only hurts. That is the GIPS definition of net of fees: gross less
  **investment-management** fees, where custody and administrative charges (an IRA maintenance fee) are not deducted from
  performance (held: the standard, not read from a Commonwealth document). The two together say: "NetofFees" means net of
  advisory fees only, and every other charge is a withdrawal.

## 2. Dividends: the file dates them by PAY date; the reported TWR most likely recognizes them at EX-date

**The file has one date per dividend, and it is the pay date** (measured). For `dv`/`dvr`, `Trade_Date = Cost_Date =
Settle_Date` on over 99.9% of 780,592 rows. The dates match public pay dates, not ex-dates:

| security | Commonwealth dividend dates (2025-26) | public pattern |
|---|---|---|
| MSFT | 03-13, 06-12, 09-11, 12-11 | pays Mar/Jun/Sep/Dec; goes ex in Feb/May/Aug/Nov |
| SPY | 01-31, 04-30, 07-31, 10-31 | pays end of Jan/Apr/Jul/Oct; goes ex in Dec/Mar/Jun/Sep |
| KO | 04-01, 07-01, 10-01, 12-15 | pay dates |
| JNJ | 03-04, 06-10, 09-09, 12-09 | pay dates |

(The public pattern is held knowledge, not read from a vendor.)

**Why the +46/-28 swing is this.** When the ex-date and pay date fall in different months (MSFT Feb/Mar, SPY Mar/Apr),
the price drops at the ex-date. A pay-date rebuild books that month low (price down, no income) and the next month high.
A paired swing of opposite sign across adjacent months is the signature of a dating mismatch. The reported series behaves
like an accrual book: income recognized at the ex-date, carried as a receivable to the pay date. That is the GIPS and
portfolio-accounting default (held) and what an Advent-style book (the transaction vocabulary in section 3 of
`RESEARCH_20261008_COMMONWEALTH_FILES_VS_SCHWAB_FACT_TABLES.md`) produces.

**The discriminating arm (one run, the rule stated before the run):** grade only the account-months that hold a
security whose dividend's ex-date and pay date fall in different months, both ways:
- (A) income at the ex-date;
- (B) income at the pay date, as delivered.

The arm with more MATCH wins; a tie leaves B, the delivered dating. Ex-dates come from the Yahoo dividend series that the
price backfill already pulls (`RESEARCH_20261008_COTTONWOOD_YAHOO_PRICE_BACKFILL_STRUCTURE.md` section 3), equity and ETF
first. For mutual funds the ex, reinvest and pay dates usually coincide, so B and A agree there.

## 3. Sweeps and cash

- The two bank deposit sweeps on the declared list (`FDIC66606` "Bank Deposit Sweep Program", 143,357 rows;
  `FDIC66853` "Advisory Retirement Sweep Program", 80,939 rows), plus `CFNCASH`, are the account's cash. They are valued at
  par and stay inside the TWR. A sweep buy or sell paired with a trade is an internal move, never a flow; sweep interest
  (`int`) is income (inferred; the standard total-account treatment).
- Money-market funds (Fidelity Government Cash Reserves `316067107`, 232 accounts) stay priced holdings, as the round-20
  ruling has it; at a stable $1.00 NAV, treating them as cash or as a holding gives the same return.
- `Position_Type=CASH` is not a cash flag. It is on 1,408,059 of 1,416,497 rows (`sweep_regrade.md` section 1), so it must
  not drive any rule.

## 4. What this does not settle

- Only one side (net) is delivered, so the fee rule is a best fit, never a reconciliation. Asking Commonwealth for its
  performance methodology statement, or one account's gross series, would make it measured.
- 79,010 of 82,593 account-months are UNGRADABLE today (`sweep_regrade.md:664`), mostly for missing prices. Every rule
  above is tested on about 4% of the history until the price backfill lands.
