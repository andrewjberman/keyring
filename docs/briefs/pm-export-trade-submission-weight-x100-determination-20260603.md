# PM Export -> Trade Submission weight x100 — root-cause determination (TO PMTRDX.001)

**Author:** 0.3.1_RD_PortfolioManagement~B | **Date:** 2026-06-03 | **Class:** FIX (trace + determination)
**Reporter:** Yang (Andrew-direct) | **TO:** `org/tier3_rd/0.3.1_RD_PortfolioManagement/task_orders/PMTRDX.001.export-weight-x100-bps-as-percent.md`

## Headline (the determination the TO demanded FIRST)

**The submitted brokerage ORDER is CORRECT — this is NOT a live 100x bad-trade.** The x100
is a **stored-record + display unit-contract violation**, surfacing in the portal Trade
Details view of PM-exported submissions. A 20bps (0.20%) intent is sent to the broker
correctly as 0.20%, but the portal *renders* it as "20%".

Verified against the **actual served artifacts**, not a proxy:

| Artifact | What it holds for a 20bps DELL buy | Correct? |
|---|---|---|
| Submit-time Vident Trade CSV (`s3://opal-data-portal-v2/portfolio-management/exports/PFDE/v_12dd9834_20260602_135824_trade.csv`) — the canonical order artifact | `Proposed Weight 0.200000` (= 0.20% in Vident percent-number convention) | **YES** |
| DynamoDB `opal-trade-submissions` record `TRADE-20260602-135824-9CHHWS` (Yang, PENDING_APPROVAL) | `proposed_weight: "0.2"`, `delta: "0.2"` (string) | stored as percent-number |
| `TradeDetailsModal.tsx:172` render `proposed_weight * 100` | **"20.00%"** (and AMD current `2.12` -> "212.00%") | **NO — x100** |

## Root cause: two unit conventions collide on ONE DynamoDB field

The trade-submission domain's **canonical unit is the decimal FRACTION** (1.0 = 100%):
- `fileParser.ts:205` — explicit: *"we'll store as decimals, display as percentages"*
- `SecuritiesTable.tsx:226-239` — manual input divides by 100 on entry, multiplies by 100 on display
- `TradeDetailsModal.tsx:169-176` — multiplies by 100 to render
- **Production manual submissions confirm it:** INTU `current_weight 0.0716` (=7.16%), NVDA `0.0938` (=9.38%), BK `0.0048` (=0.48%) — all stored as fractions (numeric `N`).

The PM-optimization domain's unit is the **PERCENT-NUMBER** (0.20 = 0.20%; 1.24 = 1.24%):
- `types/portfolio-optimization.ts:29` — `// Portfolio weights (%)`
- PM grid `TradeTable.tsx:313` renders `delta.toFixed(2)%` with **NO x100** (0.20 -> "0.20%")
- `portfolio.ts` `TradeRecord` sample values (`'Final Weight': 1.239026` = 1.24%)

**The boundary that breaks:** the export-and-submit Lambda
`infra/aws/lambda/portfolio_excel_generator/lambda_function.py` →
`build_trade_securities()` (L123-144) copies PM percent-numbers **straight into** the
DynamoDB `securities[].{current_weight, proposed_weight, delta}` with **no percent->fraction
conversion**. The same percent-numbers go into the Vident CSV/Excel where they are *correct*
(Vident template expects percent-numbers), but the DynamoDB record is consumed by the
fraction-contract FE, which then renders x100.

## Recommended boundary fix (backend — AE-owned deploy)

In `build_trade_securities()` divide `current_weight`, `proposed_weight`, and `delta` by 100
(percent-number -> fraction) when writing the DynamoDB submission record. **Leave
`generate_trade_csv()` and `generate_vident_excel()` untouched** — they are Vident-facing and
correctly emit percent-numbers. This makes PM submissions consistent with manual submissions
(both fractions) and the FE render correct, with zero change to the broker order artifact.

No FE change is required — `TradeDetailsModal`/`SecuritiesTable` are already correct for the
canonical fraction contract.

## Why this exceeds a one-line patch (escalation items)

1. **Backend Lambda fix** — RD cannot deploy Lambdas (CLAUDE.md Rule 1: Terraform-only,
   AE-owned). Needs AE.
2. **Pre-existing latent inconsistency in the downstream execute/download Excel.** The
   workflow Excel generators (`trade-pipeline/trade-workflow-handler/src/excel_generator.py`
   and `trade-dashboard-api/src/excel_generator.py`) use a THIRD handling:
   `current_weight/100 + '0.00%'`, `proposed_weight` plain `'0.00'`, `delta/100 + '0%'` — i.e.
   they expect **percent-numbers**. So they are **already wrong for the fraction-convention
   MANUAL records today**, and after the PM÷100 fix they would also misrender PM records.
   A complete fix requires a **canonical-unit ruling** + aligning these generators. (Not
   Yang's reported symptom, but the same root.)
3. **Existing PENDING_APPROVAL PM submissions** (Yang's 2026-06-02 set) are stored as
   percent-numbers. After the Lambda fix, NEW submissions are correct but historical PENDING
   records still display x100 → one-time ÷100 remediation of `securities[].{current,proposed,
   delta}` for `source = portfolio_export` records.

## Regression matrix (post-fix expectations, fraction canonical)

| Intent | PM Security (percent-number) | Lambda stores (÷100, fraction) | FE display (×100) | Vident CSV (unchanged) |
|---|---|---|---|---|
| 1bps buy | 0.01 | 0.0001 | 0.01% | 0.010000 |
| 20bps buy | 0.20 | 0.0020 | 0.20% | 0.200000 |
| 250bps (2.5%) | 2.50 | 0.0250 | 2.50% | 2.500000 |
| 100% full | 100.0 | 1.0000 | 100.00% | 100.000000 |
| sell (delta<0) | -0.37 | -0.0037 | -0.37% | -0.370000 |

## Disposition

Determination complete. Fix is backend + needs canonical-unit confirmation + record
remediation → routed to COO (loop AE) and CTO (canonical-unit ruling) as RAVC2 + [BLOCKED-ASK].
