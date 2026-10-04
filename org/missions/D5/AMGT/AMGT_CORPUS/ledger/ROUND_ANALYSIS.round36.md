# AMGT_CORPUS -- ROUND 36 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-10-04 ~23:5xZ

**Input:** CVO slug msg 29334, `surprise-channel/adjudications/ADJUDICATION_v42.md` @1acdc5c60b (precondition MET; ARMED 0). al-4 is
CARRIED as a named read on the 2026-10-05 13:00Z fire (CTO msg 29322).

## 1. WHAT THE ROUND DELIVERED

- **al-1:** `read_model` serves `fiscal_unresolved`.
- **al-2:** the 49 V3 lines on the Model tab, on portal DEV `75efe9d6` (Andrew's word @40cd6d2680; CI 37241631766 success).
- **al-3:** the units judgment read. 24 family verdicts: RIGHT 19, WRONG 0, CANNOT-TELL 5, the last being true absences.
- **al-5:** one code-only redeploy, ledger CLOSED Branch A; the live CodeSha256 equals the ledger.
- **CVO grades:** al-2 AC3 PASS (every reason the page prints reads as plain words) and al-3 AC2 PASS (all 24 verdicts hold; the
  cross-reads are sound).

**Round 36 is CLOSED.**

## 2. GRADES

- **FWD-22: REALIZED** (round 35). al-4 carries the regression read of its first fire on the new pin.
- **FWD-20: still open, on two limits the CVO placed in FWD-20's scope:**
  1. A gap INSIDE a showing row (1299 HK's `--` in 2016, 2017 and 2022) gives no reason. That breaks "a row that still cannot show
     says why" in its narrow form.
  2. **Money names no currency.** On TSM's mixed-currency block (quote USD, reporting TWD), the 52's 167 figures all carry `currency`
     null, and so do **68 of the 128 OLDER MILLIONS figures** (NET_INCOME, BS_TOTAL_LIABILITIES, BEST_*). The defect covers every
     monetary field, not only the 52.

## 3. RULINGS

| # | item | ruling | why |
|---|---|---|---|
| 1 | **Row Z-W2-S20, widened:** unlabelled money | **Round-37 cell, SERVED (pair):** every monetary figure (MILLIONS, ABSOLUTE and per-share money) carries its currency. Use the block's reporting currency where the figure is a reported value, and the quote currency where it is a market value, read from the block and never assumed. The re-derive runs over all 96 blocks. **Control:** a census of money figures with a null currency over every monetary field reads 0 on all 96 blocks, with TSM's 68 + 167 as the named before-count. The page prints the currency beside each amount; that portal change is reviewed and pushed on Andrew's word. | A value must carry its claim. "96,078 million" on a non-USD name is ambiguous, and the CVO measured that the gap is not confined to the new fields. |
| 2 | **In-row gaps without a reason** (limit 1) | **Round-37 cell, LOCAL + portal:** a `--` cell inside a showing row says why, from the year's served `fiscal_unresolved` reason (al-1 already serves it), as a hover or footnote per gap year. Never a new reason invented on the page. | FWD-20's narrow form. The reason is already served, so only the page has to say it. |
| 3 | **Z-W4-S4:** `induction_request.py` writes the request file on `--pick` | **Round-37 cell, LOCAL:** `--pick` writes nothing. Plant: a `--pick` run leaves the request file's bytes unchanged. | A read-only verb that writes is the class REMEDIATION_v1 left OPEN. |
| 4 | **al-4, carried** | **A round-37 read on the 2026-10-05 13:00Z fire:** 96 pulled, rc 0, 0 pointer units. It is a Monday, so the content is Friday's close. | FWD-22 regression on the new pin. |

## 4. ENRICHMENT LIST (round 37, ONE issuance by `2.0.0_SA_COO~X`)

1. The currency on every monetary figure (ruling 1), with its census control and its pair.
2. The in-row gap reasons on the Model tab (ruling 2).
3. The Z-W4-S4 `--pick` repair (ruling 3).
4. The al-4 read on the 10-05 fire (ruling 4).
5. No vendor call beyond the scheduled daily pull.

## 5. ACTS FOR ANDREW (cited)

- The DEV push of round 37's portal candidate when it is approved (CLAUDE.md Portal).
