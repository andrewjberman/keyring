# BD Cost Basis & Tax Lot Investigation — 0.4.0_DS_ClientPlatform

**Date:** 2026-03-20
**Branch:** CLOUD
**Requested by:** Yang Liu (via Andrew)

---

## Objective

Determine whether Black Diamond can serve as the source for cost basis and tax lot data needed to produce FactSet ShareLots files. A sample Schwab CSV (single account, single security) was provided as the reference, along with the target FactSet output format.

---

## FactSet ShareLots Target Format

```
SECURITY_ID,SHARES,PRICE,PURCHASE_DATE,LOT_NUMBER
```

Five required fields per lot: security ID, shares, purchase price (PIT), purchase date, and lot number.

---

## Investigation

### Step 1: Direct Account Lookup — No Match

BD account IDs follow an 11-character format (`z` + 10 digits). The Schwab account number is only 8 digits. No match found across 9,839 BD accounts by account ID, account name, or any variant.

### Step 2: Position Matching — No Match on Totals

The Schwab CSV shows 3,063.1479 shares across 21 lots. Searched all 127 accounts holding this security in the BD gold holdings_lots layer (today's snapshot, 965,709 lots across 9,433 accounts). No account was within 10% of the target share count or within 15% of the target market value ($760K).

### Step 3: DRIP Fingerprinting — Match Found

Dividend reinvestment (DRIP) lots are unique per account because fractional shares are proportional to position size. The Schwab CSV shows 5 DRIP dates (Feb, May, Aug 2025, Nov 2025, Feb 2026). Compared DRIP unit values across all 47 BD accounts that had DRIP lots on all 5 dates.

One account matched 3 of 5 DRIP values exactly, with the remaining 2 offset by exactly +2.0000 shares each (explained by an intermediate manual purchase being absorbed via FIFO):

```
                 Feb 2025   May 2025   Aug 2025   Nov 2025   Feb 2026
Schwab:          4.0552     4.7689     4.3538     1.0271     0.9429
BD:              4.0552     4.7689     4.3538     3.0271     2.9429
```

**Account identified.** Joint brokerage account, opened 2023-05-01, first transaction 2023-05-01.

### Step 4: BD Lot Detail — Transfer-In Problem

BD has only **6 lots** for this account vs Schwab's **21 lots**:

| BD Lot | Acquired | Shares | Source |
|--------|----------|--------|--------|
| 1 | 2023-05-10 | 4,170.0000 | Transfer In |
| 2 | 2025-02-13 | 4.0552 | DRIP |
| 3 | 2025-05-15 | 4.7689 | DRIP |
| 4 | 2025-08-14 | 4.3538 | DRIP |
| 5 | 2025-11-13 | 3.0271 | DRIP |
| 6 | 2026-02-12 | 2.9429 | DRIP |
| **Total** | | **4,189.1479** | |

All 15 original purchase lots (2019-2023) were collapsed into a single transfer-in lot. The original acquisition dates and cost bases are lost in BD.

### Step 5: Share Count Discrepancy

- **BD total:** 4,189.1479 shares
- **Schwab total:** 3,063.1479 shares
- **Difference:** 1,126.0000 shares

The Schwab CSV covers one account. The BD account appears to hold shares from multiple source accounts consolidated on transfer. The household has 4 BD accounts total (2 joint, 1 rollover IRA, 1 contributory IRA) but only the one joint account holds this security.

### Step 6: Fake Cost Basis Discovery

BD's transfer-in lot shows cost_per_unit of **$173.555**. This security has never traded at the implied average cost of $408.91 that would be required for the unexplained 1,126 shares. Investigation revealed that $173.555 matches the security's **market price on the transfer date** (2023-05-10), not any actual purchase price.

BD did not receive cost basis data with the transfer. It defaulted to market price on transfer day as the cost. The $723,724.35 "cost basis" in BD is simply 4,170 x $173.555 = market value on day of transfer.

### Step 7: Schwab CSV Validation

Verified the Schwab CSV is internally consistent and self-sufficient:

- **Shares x Cost per Share = Cost Basis** confirmed for all 21 lots (sub-penny rounding on DRIP lots only, $0.05 total)
- **Sum of lot shares:** 3,063.1479 -- matches CSV header
- **Sum of lot cost basis:** $268,195.66 -- matches CSV header
- **Average cost/share:** $87.56 -- matches CSV summary row
- **Unrealized gain:** $760,579.62 - $268,195.66 = $492,383.96 -- matches CSV header
- **Long-term + short-term UGL:** $492,247.48 + $136.49 = $492,383.97 -- matches within penny rounding
- **Cost per share IS the PIT (point-in-time) purchase price** -- confirmed by exact multiplication match on every lot

---

## Findings

### BD Cannot Serve as Source for Cost Basis / Tax Lot Data

Three independent problems:

1. **Lost lot history.** The transfer-in collapsed 15 original lots (spanning 2019-2023) into a single lot dated 2023-05-10. Individual acquisition dates and per-lot cost bases are gone.

2. **Wrong share count.** BD shows 4,170 shares for this account vs 3,063 in Schwab. The transfer commingled shares from multiple source accounts.

3. **Fake cost basis.** BD's cost_per_unit ($173.555) is the market price on the transfer date, not the actual weighted average purchase price ($87.56). BD overstates the cost basis by ~2x.

### Schwab CSV Is Self-Sufficient

The Schwab CSV contains all 5 fields required for the FactSet ShareLots file:

| FactSet Field | Schwab CSV Column |
|---|---|
| Security ID | Symbol (requires ticker-to-FactSet ID mapping) |
| Shares | Quantity |
| Purchase Price | Cost per Share (= PIT price, verified) |
| Purchase Date | Acquired/Opened |
| Lot ID | Sequential assignment |

The only field not directly in the CSV is the FactSet permanent security ID, which is a standard mapping Yang's team would have.

---

## Conclusion

BD is not the route for cost basis and tax lot data for accounts that transferred in without lot-level history. The Schwab cost basis CSV is the authoritative source and contains everything needed. The automation question is whether Schwab provides a programmatic way to pull these CSVs (API, SFTP, advisor portal export) rather than manual download.

For accounts that have been in BD since inception (no transfer-in), the `03_build_holdings_lots.py` gold layer script produces FIFO-reconstructed lots with acquisition dates, cost per unit, and cost basis -- but these would still reflect BD's transaction dates, which may differ from custodian-reported dates.
