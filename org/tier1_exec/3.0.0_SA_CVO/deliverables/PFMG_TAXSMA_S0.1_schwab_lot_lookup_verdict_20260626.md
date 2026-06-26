# PFMG_TAXSMA S0.1 — Schwab lot-level cost-basis lookup-vs-pull VERDICT

**Author:** 3.0.0_SA_CVO · **Date:** 2026-06-26 · **Project:** PFMG_TAXSMA (S0 discovery, gating)
**Question (PRD §S0.1):** does `opal-data-schwab` already carry lot-level cost-basis for the 3 Tax
SMA accounts, T-1 current? → cheap S3 LOOKUP vs hard fresh-Schwab-pull. Blocks 0.8.0_AE S0.3 step-1.

## VERDICT: NOT A LOOKUP — fresh-pull / extend-the-ingest required (AWS-native lot data does NOT exist for these accounts today)

The existing `opal-data-schwab` lot-level table (`silver/ULN/` — unrealized lots) does NOT carry
the 3 Tax SMA accounts, and is stale. Three independent grounds, any one sufficient. The runtime
leg for step-2 must be a **fresh Schwab pull** (browser-automation, the hard credentialed path) OR
**extend the CRS ingest** to cover these accounts — NOT an S3 lookup.

## Grounding (live S3, boto3 vs the served artifacts — not self-report)

**The 3 Tax SMA accounts** (from `models/tax_strategy/Tax SMA Accounts (1).xlsx`, acct=digits-only):
| Account | acct10 | Schwab-custody status (account_xref) |
|---|---|---|
| Chiles, Colby & Nicole | 27265115 | **`bd_only_no_schwab_ACC`** — NO Schwab custody record |
| Nixon, Matthew & Malita | 84073310 | `bd+schwab` (schwab_padded_id 0084073310, master 0008242234, SmartX) — has a Schwab record |
| Bump, Dan & Kim | 35940058 | **`bd_only_no_schwab_ACC`** — NO Schwab custody record |

**(a) COVERAGE — 0 of 3 present in the lot table.** `silver/ULN/date=20260508/data.parquet`
(226,608 rows, 3,690 distinct accounts). ULN.account_id == xref.schwab_padded_id (3643/3690
overlap — confirmed it IS the Schwab custody book under master 0008242234). None of the 3 Tax SMA
accounts appear (exact, zero-padded, and substring variants all empty). Chiles + Bump have NO
Schwab ACC record at all (`bd_only_no_schwab_ACC`). Nixon HAS a Schwab record but is **absent from
ULN** at date=20260508, 20260415, AND 20260407 — verified across partitions. So even the single
account with Schwab custody is not materialized in the lot table.

**(b) FRESHNESS — stale ~7 weeks, ingest stopped.** Latest ULN partition = `date=20260508`,
LastModified `2026-05-11`. Today is 2026-06-26 → ~49 days stale, far from T-1. The ingest appears
to have HALTED after 2026-05-11 (no partition since 20260508). Even if the accounts were covered,
the data is not current.

**(c) DIFFERENT BOOK.** ULN covers the 49F-master (0008242234) SmartX custody set. At most 1 of 3
(Nixon) shares that master; 2 of 3 are BD-only with no Schwab custody footprint.

**(c-PRD "gap to export-only-lot-level") — the gap is COVERAGE+FRESHNESS, not SCHEMA.** The ULN
schema is already exactly lot-level: `account_id, cusip, ticker, current_quantity, cost_basis,
cost_per_share, unrealized_gain_loss, acquired_date, original_purchase_date` — a 1:1 match to
Yang's `convert_cost_basis.py` IN contract (symbol/qty/market_value/cost_per_share). So IF these 3
accounts were in the feed and fresh, the format-to-"Tax Lot" step would be cheap. The blocker is
purely that the accounts are not in the feed and the feed is stale.

## Recommendation (decides 0.8.0_AE's runtime leg)
- **Step-2 data leg = LOCAL/fresh-pull, NOT AWS-native-lookup** (for now). The AWS-native lot data
  does not exist for these accounts → 0.8.0_AE should architect step-1 against a fresh Schwab pull.
- **PREFERRED structural fix (per PRD, over brittle browser-automation):** EXTEND the existing CRS
  ingest to cover the 3 Tax SMA accounts + REVIVE its cadence (it stopped 2026-05-11). IF the
  Schwab CRS delivery can include these accounts, that converts step-2 to a cheap AWS-native lookup
  GOING FORWARD — the schema is already right. FEASIBILITY CAVEAT to confirm with AE/Schwab-ops: 2
  of 3 (Chiles, Bump) are `bd_only_no_schwab_ACC` — confirm they are obtainable via the CRS feed at
  all; Nixon (SmartX, master 0008242234) is the most likely to be ingestable.
- **FALLBACK (definitely works):** browser-automation Schwab-UI lot export — what Yang does
  manually today (credential-bearing, brittle; the PRD's hard path). Use only if extend-ingest is
  infeasible for these accounts.

## Caveats / residuals (honest)
- account_xref is itself `as_of 2026-04-21` (bd_last_seen 04-13..04-17); the Schwab-custody status
  of these accounts could have changed since. The COVERAGE finding (absent from ULN) is grounded on
  the live ULN partitions directly, independent of the xref vintage.
- ULN-ingest-halted (last write 05-11) is a SECONDARY finding worth its own flag — the schwab feed
  reviving is a prerequisite for ANY extend-ingest path regardless of the Tax SMA accounts.
- Access note: live S3 required a Windows-cert-store CA bundle (corporate-proxy TLS interception
  broke aws-CLI + boto3 default verify); grounded via boto3 verify=<win-ca-bundle>.

RAVC → COO + CTO + 0.8.0_AE (step-1 unblocked: architect the LOCAL/fresh-pull leg; extend-ingest is
the go-forward lookup path).

— 3.0.0_SA_CVO
