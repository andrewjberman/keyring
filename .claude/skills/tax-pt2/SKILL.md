---
name: tax-pt2
description: OPAL_TAXSMA part 2: per-account cost-basis and gains-net-of-fees assessment from the Schwab 0833 master data in s3://opal-data-assets -- no Schwab login, no browser, no credentials. `/tax-pt2 {account-number}`. Produces the lot-level CostBasis CSV (the shape /tax-pt3 consumes) and a fees/performance report into SharePoint TAX/Tax Lot/{YYYYMMDD}/. Workspace-agent operated.
---

# /tax-pt2 {account} — cost basis + gains net of fees (OPAL_TAXSMA part 2)

**Commissioning record:** Andrew-direct 2026-07-16 (this session; call with Yang recorded same day).
The 2026-07-14 ruling "step-2 stays manual / not derivable in-estate" rested on S0.1's membership
test against `opal-data-schwab` (the 0824/CRS delivery) ONLY. The 0833 monolith feed
(`s3://opal-data-assets/schwab/08335338/`) landed 2026-07-14 and carries all live Tax SMA
accounts — verified 2026-07-16 on number + name axes with a positive-controlled matcher.
**Latest word governs: part 2 is buildable and commissioned.**

**Design of record:** the 2026-07-16 viability assessment (this skill's constants are its findings)
+ `docs/briefs/PFMG_TAXSMA_S0.1_S0.3_close_20260714.md` (step-3 input contract)
+ the BD HAR analysis (bd3.bdreporting.com, Chiles account) for the reconciliation targets.

**Never:** write to any bucket (this skill is READ-ONLY on AWS); overwrite an existing SharePoint
artifact (`conflictBehavior=fail`); blend the accrual overlay into the BD-matching number; sum or
substitute 0824/0833 quantities (two masters, two business purposes — MEMORY law).

## Constants (verified 2026-07-16 against the 2026-07-15 partitions)

- **Data root:** `s3://opal-data-assets/schwab/08335338/silver/` — daily, T-1 frontier
  (resolve staleness via `lib/trading_calendar.py`, NEVER wall-clock).
- **THE FEED TRAP: unrealized lots ride `fact_ult`, NOT `fact_uln`.** The Tax SMA accounts have
  0 rows in ULN (section DL) and all their lots in ULT. A run reading ULN "succeeds" with zero
  lots — the zero-lots gate below exists because of this.
- **Tables:** `fact_ult` (open lots: ticker, cusip, current_quantity, current_market_value,
  cost_per_share, acquired_date, cost_basis_unamortized, unrealized_gain_loss, days_held),
  `fact_rps` (positions/MV), `fact_trn` (transactions: flows, dividends, MARGIN INTEREST,
  SERVICE FEE = stock borrow, ADVISOR FEE debits; history to 2024-07), `fact_rld`/`fact_rly`
  (realized), `fact_acc` (account master: status, strategy, names).
- **Fee schedules:** BD daily pull `s3://opal-data-assets/blackdiamond/49f/bronze/fees_435407/{date}/data.xlsx`
  — per-account `Account Fee Schedule` / `Basis Points` / `Fee Schedule Rate Type` ride each
  billing row. Confirmed: Chiles 27265115 = "49F - Flat 1" = 100bp flat on Total Value.
  Schedules VARY (0.9% rows exist) — read per account, never assume.
- **Roster (until Yang's xlsx is wired in):** live Tax SMA accounts + trade-start dates:
  `0027265115` Chiles (2026-04-08) · `0035940058` Bump (2026-04-08) · `0091939812` Macy (~2026-06-05).
  Trade-start is an INPUT — never BD's inception (BD anchors Since-Inception at FUNDING,
  e.g. Chiles 2026-03-16, netAdditions ~$1,047,024.72; first trade was 04-08).
- **BD reconciliation targets (from the 2026-07-16 HAR, Chiles, 04-08..06-30):**
  BMV 1,061,234.71 / EMV 978,575.04 / netGains -87,061.19 / TWR -8.2053% / MWR -8.2017% /
  income -6,566.11 / **fees 0.0**. BD identity: `netGains = EMV - BMV - netAdditions` (to the cent).

## Methodology pins (the protocol — deviate only with Andrew's word)

1. **BD-matching number (the number of record):** posted-transactions-only. BD does NOT amortize
   advisory fees — `feeMethod: NetOfFees` still reported fees=0.0 for a quarter with no posted
   advisory debit. Margin interest + borrow fees + posted ADVISOR FEE debits are already inside
   EMV/flows, so `netGains = EMV - BMV - netAdditions` nets them automatically.
2. **Accrual overlay (the honesty line, SEPARATE column):** daily accrual =
   `MV x (bp/10000) / 365` from last-billed-through date to as-of, rate per the account's BD fee
   schedule. True-up against the actual ADVISOR FEE debit when it posts; back out the implied
   rate from the first observed debit as the positive control before trusting the formula.
3. **`feesIn: NetAdditions` semantic:** when a fee posts, BD counts it inside netAdditions
   (excluding it from netGains). Mirror this in the BD-matching column or the first billed
   quarter will not reconcile.
4. **TWR:** daily chain-link off `fact_rps` MV series with `fact_trn` external flows
   (JOURNAL/TRANSFER = external; fees/interest/dividends = internal). MWR (Modified Dietz) as
   the secondary, matching BD's pair.
5. **ST/LT splits:** from `fact_ult` `acquired_date`/`days_held` (unrealized) and `fact_rld`/`fact_rly`
   (realized), matching the BD costBasis report's four cells (ST gain/loss, LT gain/loss).
   Transferred-in appreciated lots are NORMAL here (Chiles: ~$771K unrealized LT on
   ~$156K original 2005 basis) — never "fix" an old acquired_date.

## Steps

0. **Resolve inputs:** account number (arg, digits only, zero-pad to 10), as-of date (default:
   `expected_last_trading_day(today - 1 day)` — the pinned tax-pt1 recipe), window start
   (default: the account's trade-start from the roster).
1. **Account gate:** row must exist in `fact_acc` with status O + managed strategy `Opal Tax SMA*`.
   Not found / not Tax SMA -> STOP, report (protects against a typo pulling a stranger's account).
2. **Pull lots:** `fact_ult` for as-of, filtered to the account. **ZERO-LOTS GATE: 0 rows = FAIL
   LOUD** (feed break or the ULN/ULT trap) — never emit an empty artifact.
3. **Pull the window:** `fact_trn` partitions from window-start to as-of (flows, fees, dividends);
   `fact_rld`/`fact_rly` for realized; `fact_rps` for the daily MV series.
4. **Compute:** BD-matching netGains + TWR/MWR (pins 1/3/4), fee ledger (margin interest, borrow,
   advisor debits, each dated), accrual overlay (pin 2), ST/LT splits (pin 5).
5. **Emit artifacts (the audit trail — one per level, Andrew's three-step design):**
   a. `TAX/Tax Lot/{YYYYMMDD}/CostBasis_Acct_{account}.csv` — lot-level, in the exact Schwab
      "Export only lot level detail" shape (the pinned /tax-pt3 input contract; pt3 consumes
      it UNCHANGED).
   b. `TAX/Tax Lot/{YYYYMMDD}/{account} taxpt2-report.md` — window, BMV/EMV, netGains,
      TWR/MWR, fee ledger, accrual overlay (labeled), ST/LT grid, row counts + sha256s,
      and the BD-reconciliation block when BD numbers are on hand.
   Saves via the gateway site tools; `conflictBehavior=fail`; collision = already-ran signal.
6. **Verify:** `list_site_files` on the target folder — listing-based acceptance (name + size).
7. **Report:** chat + broker summary; on any failure MCP note to `0.5.0_AE_OpalETL` (project lane).

## Phases

- **Phase A (NOW):** workspace agent runs this skill (S3 reads ride the agent's AWS access).
  Operator: Andrew or any workspace agent on his word.
- **Phase B (pending two legs, CTO-routed):** (1) gold projection table
  `dim_taxsma_costbasis` (all 0833 accounts, daily, produced post-silver in the existing 0833
  conversion chain — gold because it is a parse-down, per the naming law silver=fact complete /
  gold=dim projection); (2) m365 gateway tool `taxsma_costbasis(account, asof)` reading ONLY that
  prefix, gateway EC2 role granted read on the exact ARNs (Rule 22a simulate battery, one
  --resource-arns per call), entitlement rows: andrew@opalinvest.com (master, implicit) +
  alyssa@opalinvest.com (this tool class only). Then Alyssa runs `/tax-pt2 {account}` from her
  laptop; no human holds AWS credentials; every call lands in the s3://opal-mcp-audit lake.

## Open items (surface once, via Andrew)

- Wire Yang's `Tax SMA Accounts.xlsx` (SharePoint TAX) as the roster source (inception +
  latest-trade-date columns confirmed on the 07-16 call) — replaces the pinned roster above.
- Billing frequency + in-advance/in-arrears per account: read from the first billed rows'
  Billing Start/End dates in fees_435407; Yang tiebreaks only if it won't reconcile to the cent.
- Whether the quarterly client REPORT (Yang's Q2 template: returns QTD/SI, ST/LT grid, top-10,
  sectors, benchmark) becomes /tax-pt2's second output or its own part — Andrew's call.
