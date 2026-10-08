# ADVI_COTBKF decomposition -- ROUND 16 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-07 ~19:2xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2` msg 999 (re 996): "yes, cut round 16 this tick, ONE issuance: valuation, return and monthly grade
built against stub prices, LOCAL. Unpriced days stay blank, never estimated. The tolerance for the monthly grade is stated before any
real run." The cut-ready text: `deliverables/2.0.0_SA_COO~C2/DRAFT_FWD3_DAILY_RETURNS_CUT_20261007.md` @661c50a7ac (UPDATE section).
Andrew approved both price sources (record `org/tier1_exec/2.0.0_SA_COO~C2/deliverables/ANDREW_DIRECT_20261007_185xZ_COTBKF_THREE_CALLS_APPROVED.md`).

**Rule 24.** Domain: FWD-3's C-DAILY steps 2-4 (step 1 is CB-l-1, done). Three cells, one per step; MECE over the steps.

## Measured constraints

1. Step 1 output: `commonwealth_daily_holdings.daily_holdings_table(tx)` -> columns `account, date, cusip, quantity`; 1,533 accounts,
   1,691,729 account-days, 22,547,096 non-zero holding rows; cash securities (FDIC*, CFNCASH) kept in the table.
2. Price stores Opal already holds: the six USABLE stores in `commonwealth_price_census.STORES`, read by `read_store` and matched by
   `match_security` (CUSIP before ticker; a ticker two CUSIPs share is never used). Union coverage at the census: 1,720 of 4,634
   securities, 1,318,560 of 9,630,847 security-days (13.7%). `opal-data-bd` is BARRED (CB-j-1). MDPF_SECHIST's series address is not
   yet printed; it is taken as `--sechist <s3 prefix>`, absent until dell1 announces the load.
3. Commonwealth's monthly returns: silver performance `reporting_period=Month`, 80,709 rows, every one `PerfType=TWR`, `NetGross=True`,
   `Annualize=False`; `PerfNum` is in PERCENT, given to 2 decimals; some rows are not finite (inf).
4. Signs: `commonwealth_signs.SIGN` / `NO_SHARE_MOVEMENT` (61 types). No table yet says which types are EXTERNAL FLOWS (money or
   securities entering or leaving the account) versus internal (dividends, trades, fees).

## The interfaces (fixed here so the three cells build in parallel on stubs)

| file | written by | columns |
|---|---|---|
| `account_day_value.parquet` | B | `account, date, value, holdings, priced_holdings, complete` (`complete` = every holding priced; `value` null when not complete) |
| `daily_returns.parquet` | C | `account, date, value, flow, ret, blank_reason` (`ret` a decimal; null with a reason when blank) |
| `monthly_grade.csv` | D | `account, month, computed_pct, reported_pct, diff_pct, grade, reason` (`grade` in MATCH / DIFF / UNGRADABLE) |

Large parquet files go to `--data-dir` (default `<repo>/.scratch/advi_cotbkf/fwd3/`, uncommitted); the deliverables folder gets the
report `.md` and small `.csv` files only.

## The cells

| cell | what | serves | risk | slot |
|---|---|---|---|---|
| `CB-p-1` | daily valuation: holdings x the day's close from the six stores (+ `--sechist` when given); cash at 1.0; an unpriced holding blanks its account-day | FWD-3 | LOCAL | `0.9.0_WK_ADVI_COTBKF~32` |
| `CB-p-2` | daily return: a FLOW table (each transaction type decided external flow or not, with its reason); after-fee TWR per account-day, flows out; blank propagates | FWD-3 | LOCAL | `0.9.0_WK_ADVI_COTBKF~33` |
| `CB-p-3` | monthly grade: chain daily returns per calendar month, compare with Commonwealth's Month TWR; tolerance **0.05 percentage points** (stated here, before any real run) | FWD-3 | LOCAL | `0.9.0_WK_ADVI_COTBKF~34` |

**Dependencies:** the DATA chain is B -> C -> D; the BUILDS are independent against the interfaces above. Each cell's real run on
Opal's data waits on its predecessor's output, so the issuer runs C and D on real data at the drain (the round's one real run).
**Fan-out:** `3 of 3 chains, cap 8`.
