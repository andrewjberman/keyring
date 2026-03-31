# ADHC_HISTRY -- Schwab Silver TRN Layer + Transaction Forensics -- 0.6.0_AE_PartnerETL

**Date:** 2026-03-31
**Start Time:** 4:30 PM ET
**End Time:** 7:15 PM ET

## Objective

Investigate the $349M FIFO overshoot (gold $1.935B vs silver $1.586B). Run transaction
forensics to find root cause, then build a queryable Schwab TRN silver layer for
cross-referencing BD's missing sell transactions against the raw Schwab custodian feed.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | RC1 fast cycle (SSM 25588e70) | DIVZ name aliasing. Quality tiers: 45.3% A+B, $736M |
| 2 | RC1+RC2 fast cycle (SSM 9bfcf753) | Tiers collapsed to 11.5% A+B. Reverted. |
| 3 | 03 synthetic lots (SSM d21de601) | Holdings lots $2.2B -- way too high vs $1.59B reality |
| 4 | RC2-final (SSM 118beee5) | Conservative cube + lot injection |
| 5 | ADHC_HISTRY.001 forensics (SSM 53c2ed97) | Confirmed 50K sold positions missing sells ($513M) |
| 6 | ADHC_HISTRY.002 FIFO walkthrough (SSM a4d2e153) | Account traces -- all overshooting accounts have BD unrealized=0 |
| 7 | ADHC_HISTRY.003 structural causes (SSM 1f9a4a56) | Cash/type reclassification CLEAN. Transfer asymmetry 139M units. |
| 8 | ADHC_HISTRY.004 realized crossref (SSM 7488cda9) | $513M sold+missing, $177M vanished. After removal: -$341M (we undershoot confirmed-open) |
| 9 | Schwab TRN upload to opal-data-schwab/01_raw/ | 60 TRN + 60 RLD files, 2026-01-20 to 2026-03-30 |
| 10 | Schwab TRN converter (local) | 337 Parquet partitions -> opal-data-schwab/silver/TRN/ |
| 11 | IAM policy added to bd-exporter-ec2-role | EC2 gold runner now has opal-data-schwab read/write |

---

## Key Findings

### What the forensics proved

| Finding | Evidence |
|---------|----------|
| Dedup is correct | 100% of duplicate txn_ids are identical re-deliveries. Zero retroactive edits. |
| Cash Deposit/Withdrawal don't hit FIFO | Confirmed in script 02 -- not in BUY_TYPES/SELL_TYPES/PASSTHROUGH |
| Transfer In asymmetry: +139M net units | 69K Transfer In rows vs 28K Transfer Out -- but likely legitimate (accounts transferred IN to 49F) |
| Missing sell transactions: $513M | BD realized confirms 50,887 positions were sold but we have no sell in our transaction feed |
| Vanished accounts: $177M | 10,832 positions in neither realized nor unrealized -- left our universe entirely |
| After removing sold+vanished: -$341M | Confirmed-open FIFO positions ($1.245B) undershoot silver ($1.586B) -- we're MISSING buys |
| FIFO logic is correct | For the transactions we have, FIFO accumulates correctly. The data feed is incomplete. |

### RC1 is the only proven fix

- RC1 (NAME_ALIASES for DIVZ consolidation): committed `db591a12`, 45.3% A+B quality tiers
- RC2 (per-position injection): degraded tiers, holdings overshoot -- reverted
- RC3/RC4: not deployed

### Schwab silver layer

- **`opal-data-schwab/silver/TRN/`** -- 337 daily Parquet files
- Coverage: 2026-01-16 through 2026-03-30 + 2024 non-Glacier dates
- 2024-09 through 2025-11 is Glacier archived (requires restore to access)
- Key fields: Order_ID, Trade_Date, Trade_Type_Code, CUSIP, Ticker_Symbol, Quantity, Net_Amount, Account_Number

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `data/black_diamond/scripts/gold/02_build_positions_cube.py` | RC1: NAME_ALIASES applied to FIFO and buy injection | Yes -- `db591a12` (DS commit) |
| `data/black_diamond/scripts/bronze/convert_schwab_trn_to_parquet.py` | New: TRN->Parquet converter | No -- local only |
| `data/black_diamond/scripts/diagnostics/adhc_histry_001_txn_forensics.py` | New: forensics script | No -- local only |
| `data/black_diamond/scripts/diagnostics/adhc_histry_002_fifo_walkthrough.py` | New: FIFO walkthrough | No -- local only |
| `data/black_diamond/scripts/diagnostics/adhc_histry_003_structural_causes.py` | New: structural analysis | No -- local only |
| `data/black_diamond/scripts/diagnostics/adhc_histry_004_realized_crossref.py` | New: realized cross-reference | No -- local only |

---

## Current State

**Status:** IN PROGRESS
**Active branch:** `CLOUD`

Forensics complete. Root cause established: BD's transaction feed is missing ~50,887 sell
transactions worth $513M (confirmed by realized report). The sell injection in script 02
handles these via synthetic sells from the realized report -- that mechanism is working.
The remaining $341M undershoot (confirmed-open FIFO vs silver) is from missing buy
transactions for accounts that transferred in or had buys not delivered by BD's feed.

Schwab TRN silver layer is live at `opal-data-schwab/silver/TRN/` (337 dates). The EC2
gold runner has IAM access. Next step is ADHC_HISTRY.005: cross-reference the SOLD_MISSING_SELL
accounts against Schwab TRN to determine whether BD dropped sells from their feed, or whether
the sells occurred before our Schwab data coverage begins.

---

## Next Steps

1. **[0.4.0_DS_ClientPlatform] Write ADHC_HISTRY.005 script** -- Cross-reference top overshooting
   accounts' sell dates (from BD realized) against Schwab TRN silver. For each SOLD_MISSING_SELL:
   does Schwab TRN have the sell near that date? If yes = BD dropped it. If no = pre-2024 or transfer.
2. **[0.6.0_AE_PartnerETL] Upload and run .005 on EC2** -- EC2 has opal-data-schwab access now.
3. **[0.6.0_AE_PartnerETL] Commit diagnostic scripts and converter** -- These are currently local only.
4. **[0.6.0_AE_PartnerETL] Rename 01_raw/ -> bronze/ in opal-data-schwab** -- Folder naming cleanup.
5. **[2.0.0_SA_COO] ADHC_HISTRY project needs formal registration** -- Create project JSON and REGISTRY.md entry.

**Files to touch next:**
- `data/black_diamond/scripts/diagnostics/adhc_histry_005_schwab_trn_crossref.py` -- DS writes this
- `infra/aws/terraform/bd-pipeline/iam.tf` -- optionally codify the schwab bucket policy in Terraform

**Do NOT:**
- Deploy RC2/RC3/RC4 without Andrew's explicit direction
- Run full gold layer until ADHC_HISTRY investigation confirms root cause
- Restore Glacier files without checking cost first (~$0.03/GB for retrieval)

## Deployment Tags

| Pipeline | Tag | Commit |
|----------|-----|--------|
| bd-pipeline | `bd-v2.20.0` (unchanged) | No new deployment this session |
