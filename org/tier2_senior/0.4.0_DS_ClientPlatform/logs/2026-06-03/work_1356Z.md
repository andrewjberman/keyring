# Findings Brief — ADVI Cost Basis & Tax Status: "Unrealized" / "Realized" bubbles

**Author:** 0.4.0_DS_ClientPlatform
**Date:** 2026-06-03T1356Z
**Dispatch:** COO ad-hoc investigation (Andrew-direct 2026-06-03), Advisor Intelligence FE refinements
**Type:** read-only data trace + semantic analysis (no code change)

---

## TL;DR

1. **CONFIRMED — both bubbles are piped from Orion**, raw, with NO semantic transform. The only gold-layer operation is a **SUM rollup** (account-grain → household → advisor). Andrew's belief is correct.
2. **Realized** = realized capital gains/losses from positions **sold/disposed YTD** (calendar Jan 1 → snapshot date).
3. **Unrealized** = **current** paper gain/loss on **positions still held**, as of the daily snapshot (`data_as_of`).
4. Each bubble carries **both** cost basis (LT/ST/Total) **and** gain/loss (LT/ST/Total) — they are Orion's tax/cost-basis report columns, summed.
5. Inflection-only: 49F does not emit these (uses taxable/tax-deferred/tax-free reg buckets instead). `tax_structure_reason='ira_no_cost_basis_tracking'` legitimately zeroes cost-basis for tax-deferred IRA-type accounts (~80% of silver rows) — Orion doesn't track lot cost basis there.

---

## Full source trace (FE → API → gold → silver → bronze → Orion)

| Layer | Artifact | Role |
|---|---|---|
| **FE** | `TaxCostBasisPanel.tsx:150-151` | renders `tax.unrealized` / `tax.realized` (presentational only) |
| FE type | `_shared/types.ts:1385` `ClientTaxRealizedUnrealized` (7 core fields) | shape definition |
| **Gold** | `data/orion/scripts/gold/INF_D_02.advisor_client_detail.py` | aggregates silver dims → `summary.tax.{realized,unrealized}` in `platinum/clients/{hh}/detail.json` + `platinum/advisors/{key}/book.json` |
| **Silver** | `data/orion/scripts/silver/build_tax_dim.py` → `silver/api_dims/tax_{realized,unrealized}/` | type-coerce + INFGRD rep filter, no semantic transform |
| **Bronze** | `infra/aws/lambda/inf-pipeline/inf-tax-daily/orion_tax_dim.py` → `bronze/orion-api/{date}/tax_{realized,unrealized}.csv` | direct Orion ExcelReports API pull |
| **Source** | **Orion ExcelReports API** `api.cloud.orionadvisor.com`, saved queries **"Tax Unrealized Dim" (cbo=0)** and **"Tax Realized Dim" (cbo=1)**, DB 4698 | system of record |

**Production cadence:** `inf-tax-daily` Lambda, EventBridge cron `55 12 * * ? *` (12:55 UTC daily). Invokes `orion_tax_dim --upload-bronze --window-realized ytd` → realized=**YTD**, unrealized=**3y default** (not overridden).

### Is it raw-passthrough? YES.
- **Bronze**: verbatim CSV from Orion's report API.
- **Silver** (`build_tax_dim.py`): only `parse_dollar`/`parse_percent`/`parse_date` type coercion, INFGRD rep filter (`rep_id IN {3,11,12}`), `coerce_silver_ids` Int64. No fillna, no row-drop, no business logic. Orion column `LT Gain/Loss` → `lt_gain_loss`, `Total Cost Basis` → `total_cost_basis`, etc. (1:1).
- **Gold** (`INF_D_02`): per-household SUM of the account-grain silver rows — `total_cost_basis`, `lt/st_cost_basis`, `total_gain_loss`, `lt/st_gain_loss`, `account_count_with_tax` (rounded 2dp). At the advisor book level the FE further sums households. **No re-derivation; the $ values are Orion's, just aggregated.**

---

## Semantic definitions (precise)

### "Realized" bubble
- **What:** realized capital gain/loss on lots **sold/disposed during the period**.
- **Window:** **YTD** — calendar year start (Jan 1 of current year) → snapshot date. (Orion query cbo=1, daterange `/y` → `0d`; PROD passes `--window-realized ytd` explicitly.)
- **The $:** the bubble shows **both** — `total_cost_basis` (cost basis of the SOLD lots) **and** `total_gain_loss` (realized proceeds − basis), each LT/ST split.

### "Unrealized" bubble
- **What:** **current** unrealized (paper) gain/loss on positions **still held**.
- **As-of:** the daily snapshot date (`data_as_of` in the artifact; pulled 12:55 UTC daily). Point-in-time, not a period sum.
- **The $:** `total_cost_basis` (cost basis of CURRENTLY-HELD lots) and `total_gain_loss` (current market value − cost basis), each LT/ST split.
- **Window param:** the Orion query carries a 3y daterange (cbo=0); the displayed unrealized G/L is a current snapshot at period-end. ⚠️ **One residual exactness caveat** (below).

### Differs by firm / tax structure?
- **By firm:** YES — **Inflection only.** 49F emits flat reg-classified buckets (taxable / tax-deferred / tax-free) and the realized/unrealized blocks silently no-op for it.
- **By tax structure:** `tax_structure_reason='ira_no_cost_basis_tracking'` — for tax-deferred reg types (IRA/Roth/401k/403b/SEP/SIMPLE) with zero cost basis, Orion does **not** track lot-level cost basis (legitimate upstream; ~80% of silver tax rows). Gold emits the sentinel; FE renders the "not applicable to IRA accounts" tooltip instead of a misleading $0 panel. Not a data defect.

---

## One caveat worth flagging
The **unrealized 3y daterange**: I've confirmed from source that unrealized is a *current snapshot* (Orion cbo=0, end-date `0d`), and the code comments label it "Unrealized current snapshot (3y default)." What I cannot 100%-resolve from code alone is whether Orion's report **excludes lots acquired before the 3y start** from the current unrealized total. The dominant/intended semantic is "all currently-held positions' paper G/L," and that's how the FE presents it. If Andrew wants byte-exact certainty on the 3y boundary effect, I can run a one-off live pull comparing 3y vs 5y windows against the same held book — ~15 min. Flagging rather than asserting.

---

## SECONDARY (item #6 fee-data feasibility) — quick read, fuller dig pending the PRD TO
- **Inflection fee floor = 2025-07-01** (confirmed: FE tooltip `TaxCostBasisPanel.tsx:213-219` + DS-confirmed 2026-05-28). `inflecBilling.total_fee_amount` is cumulative-since-7/1/2025 (~11mo), NOT trailing-12. Source: `silver/api_dims/billing/` via `build_billing_dim.py` ← Orion billing report.
- **49F**: fees served via the separate `FeeSummaryPanel` (Lambda path); history depth not yet traced this session.
- **"fee-paying since inception" feasibility**: for Inflection, "inception" of *fee record* can be no earlier than 2025-07-01 (Orion's data floor) regardless of true account age — so a "since-inception fee-paying" marker would be bounded by data availability, not account history. Recommend the marker read "fee-paying since {first fee record date}" rather than implying true inception. Full per-period history feasibility (49F depth + per-account first-fee-date extraction) → defer to the formal DS TO with the PRD.

---

## Notes / non-blocking observations
- `build_tax_dim.py` `TAX_COLUMN_MAP` drops bronze columns not listed ("lean schema") — a mild CLAUDE.md Rule-17 (silver-no-field-slimming) tension. NOT relevant to this investigation (all realized/unrealized fields map through), flagging only for opportunistic future cleanup; no action requested.
