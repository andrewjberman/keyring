# AMGT_CORPUS -- ROUND 37 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-10-05 ~14:4xZ

**Input:** CVO slug msg 29601, `surprise-channel/adjudications/ADJUDICATION_v43.md` @d4ca4f440f (precondition MET; ARMED 0). The packet
is `ROUND37_DRAIN_END_PACKET.md` @6f0c754b3e.

## 1. WHAT THE ROUND DELIVERED

- **am-1:** every money figure carries its currency (Z-W2-S20 widened).
- **am-2:** the SERVED re-derive of 96 blocks with a currency on every money figure. Its ledger `amgt-corpus-r37-am2` is CLOSED
  (Branch A) @ab5337b876, under CTO half @a8ccfc4f88.
- **am-3:** in-row gap reasons, on portal DEV.
- **The `--pick` no-write fix** (Z-W4-S4).
- **am-5:** a read of the 10-05 13:00Z fire.

**Round 37 is CLOSED.**

## 2. GRADES (CVO L9)

| item | grade |
|---|---|
| am-1 AC3: each money field's side | **PASS** on every money field. TSM EPS/DPS read as TWD by magnitude (about 17x P/E). HISTORICAL_MARKET_CAP reads as reporting-currency values. **One wrong label:** `IS_SH_FOR_DILUTED_EPS`, a share count, carries the reporting currency on BA, SAP and BABA (Z-W1-S35). |
| am-3 AC3: gap reasons on the page (FWD-20 limb 1) | **PASS** (1299 HK Model tab) |
| am-3 AC3: currency on the page (FWD-20 limb 2) | **NOT READ.** The only capture predates the re-derive. |
| am-2: served census | 0 unlabelled money over 96 blocks; CVO's TSM read agrees |
| am-5: the 10-05 13:00Z fire | **REFUSED by Bloomberg's daily capacity** (row Z-S87: 96 of 96 refused, rc 1). The cause is ETFS_RIVALS-Z-S24, the overnight backfill. FWD-22's regression read moves to the 2026-10-06 fire. |

**FWD-20 stays open** on its currency limb. FWD-22 stays REALIZED (round 35), with its regression read carried.

## 3. RULINGS

| # | item | ruling | why |
|---|---|---|---|
| 1 | **Z-W1-S35:** a share count carries a currency | **Round-38 cell, SERVED (pair):** a count field (shares, volume) and a ratio field carry NO currency, labelled by the field's unit and never by the block's reporting currency. The census over 96 blocks reads 0 count or ratio fields with a currency. A served re-derive needs its pair. | A currency on a share count is a false claim on the page. |
| 2 | **FWD-20's currency limb on the page** | **A round-38 read:** a signed-in walk on TSM and one EUR name after the re-derive, every money row showing its currency, with a positive control (a USD row). | The served state is right (am-2); only the page read is owed. |
| 3 | **Z-S87: today's fire was refused** | **A recovery run of TODAY's fire once Bloomberg answers again.** It goes on COO~RV's hourly one-query probe, and it runs AFTER MSTR~Z re-runs the firm's daily vehicle (production order). It is the same pinned fire re-invoked for the 10-05 as-of, not a new pipeline. If the capacity does not return today, the 10-06 13:00Z fire carries the data and the gap is one trading day, served with its stale reason. | A refused scheduled fire is recovered, not waited out. The production order keeps the firm's models first. |
| 4 | **Z-W1-S34:** HISTORICAL_MARKET_CAP's basis text says "trading", but the values are reporting | INERT. The producer now labels it reporting. **No cell.** | Already cured by the label. |

## 4. ENRICHMENT LIST (round 38, ONE issuance by `2.0.0_SA_COO~X`)

1. **Count and ratio fields carry no currency** (ruling 1): a SERVED re-derive under a pair, with the census over 96 blocks.
2. **FWD-20's currency limb read on the page** (ruling 2).
3. **FWD-22's regression read on the 2026-10-06 13:00Z fire** (pin `3ffe37a57a`): 96 pulled, rc 0, 0 pointer units.
4. **Today's recovery run** (ruling 3), if the capacity returns; otherwise it is struck at the 10-06 fire.

## 5. ACTS FOR ANDREW (cited)

None. Nothing in this round needs his act. The Bloomberg capacity is not a sign-in issue (MSTR~Z's P0 probe, msg 29539).
