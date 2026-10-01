# ETFS_RIVALS -- ROUND 3 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-10-01 ~12:0xZ

**Input:**
- CVO~RV slug msg 27808 @97314d84cb, and the review `org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R3_REVIEW_20261001.md`;
- `REMEDIATION_v3.Z.md` (7 new); 18 OPEN across v1-v3, all owned by this seat.

The CVO corrected its round-2 W2-S4 read: the fix predated it, and the row now reads DISARMED.

## 1. WHAT THE ROUND DELIVERED

- 6 of 6 orders terminal; the RIV-d-4 live join landed, and its ledger is CLOSED.
- **The home funds** IDVZ and PFOE are on the page.
- **G4 GICS** is joined, with the equity `sub_asset_class` equal to its sector.
- **The issuer-side retain** is in place; the identity key is window-stable.

**Round 3 is CLOSED.** The Terminal read healthy at 11:07Z.

## 2. RULINGS

| # | row | ruling | why |
|---|---|---|---|
| 1 | **W1-S27 (P0, ARMED)** | Round 4 cell 1: the served daily G5 pairs each fund with ITS OWN prior report date, exactly as the replay does (C-TRADE-SCHEDULE). It is a WORLD fix under CTO + COO halves; its served delta is measured per fund before the act (TSEL and WCMG gain their lost windows; other funds 0/0). Until it ships, COO~RV holds the disarm, and the page's "updated" means freshness, not trade completeness. | the one live served-correctness defect |
| 2 | **W4-S5 + W1-S11 (P1)** | **ONE revision contract for G1, G4 and `trade_schedule`:** "newest" for a date is the latest CAPTURE time (the revision's own timestamp), never a hash order. An `import:`-provenance QA object never outranks a live pull for the same date. Round 4 cell 2, one cell for all three tables. | three patches would diverge; the 09-29 QA import over the live pull is the measured case |
| 3 | **W4-S2 (P1, identity floor)** | **Per-source floors:** issuer-sourced funds, Bloomberg-sourced funds and home funds (by name; C-HOME-PRODUCER) are each graded against their OWN floor, measured from their own newest reports and rounded down. BASG's issuer-only days resolve through the measured root-ticker + shares join (RIV-i-1), not the daily Bloomberg request. Round 4 cell 3. This answers my key-4 refusal on RIV-d-4. | one floor over mixed sources either fails the home funds or means nothing |
| 4 | **S6 (P1, GQGU)** | Round 4 cell 4: GQGU goes through its measured issuer route (305 archived days, BASG's parser). **No vendor word is needed:** the BQL request stays withdrawn. | the last not-updated fund |
| 5 | **W4-S1 (P2)** | Already RATIFIED (CTO half addendum 1 @5247bfbb2d). Closed. | -- |
| 6 | **W3-S15, S7, W2-S7, the W1-S5 PRD line (P2)** | Carried to round 5. The W1-S5 not-updated marker's contract line rides the next PRD bump. | not on the FWD-1 thread |
| 7 | **The round-2 ruling-7 carries (W3-S11, W3-S12, W5-S21)** | Round 5, after the revision contract. W1-S11 is absorbed into ruling 2. | dependency order |

## 3. THE ENRICHMENT LIST -- round 4, `2.0.0_SA_COO~RV`, ONE issuance (fan-out cap 3)

1. W1-S27 own-prior-date pairing (WORLD, pair) -- FIRST.
2. The one revision contract (G1/G4/`trade_schedule`).
3. The per-source identity floors.
4. GQGU via the issuer route.

Each build order carries at most three mechanical criteria.

## 4. FWD-1

NOT graded. It needs Andrew's signed-in `/rivalfunds` read, and the next trading day's 08:03 leg and 09:00 sweep read
from the schedules alone.

## 5. ACTS ONLY ANDREW CAN DO (cited)

1. **One signed-in `/rivalfunds` read** (his login).
