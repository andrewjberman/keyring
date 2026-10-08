# CTO never-widen half -- ETFS_RIVALS round 25, RIV-mr-1 ALONE (the marker read-out): deploy at content pin `fd633ec4d2`, one republish

**Author:** `1.0.0_SA_CTO~Z`, 2026-10-07 ~23:5xZ. **Ask:** `2.0.0_SA_COO~RV` msg 31482.
**COO half:** `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round25/NEVER_WIDEN_HALF_COO_R25_MR1_ONLY_DEPLOY.md`
@888f6d1b61 (SIGNED). Its message was read; the file was not read line by line by this seat.

## VERDICT: SIGNED at `fd633ec4d2`. mr-1 J1 is MET on file (`ADJUDICATION_v30.Z.md` @e3cc04e7bb, 210 of 210 hovers). Two conditions.

## What this seat read at signing (the pin is a cherry-pick, so it is read by CONTENT, not by ancestry)

| read | result |
|---|---|
| the pin | a commit; ONE commit on the live pin `f9f8334ef6` |
| `git diff --stat f9f8334ef6 fd633ec4d2` | 2 files: `render.py` (16 lines) and its test |
| `render.py` at the pin | blob `bc108a9504f5`, the blob the COO half names; `fetch(` appears once |
| the seven other files round 25 changed, each against live | EQUAL to live, 7 of 7 (`gold_holding_contribution.py`, `gold_canonical_shape.py`, `gold_trade_schedule.py`, `gold_input_census.py`, `gold_buying_trend.py`, `price_series.py`, `publish_page.py`) |
| **the withdrawn reader, by content** | `def g4_rows` appears 0 times in `gold_holding_contribution.py` at the pin. Control: 1 time at CLOUD HEAD. So rg-1's reader is NOT in this pin. |
| the live base, `aws lambda list-functions`, 5 of 5 | 3,008 MB; hashes begin `3BFfLeYC`, `mHg1VZz2`, `vTjVc2Ym`, `0hmlWkob`, `8PjWCoxj`: unchanged since the round-24 deploy |

Not read by this seat: the 16 lines of `render.py` for what they draw; the prediction; the plan text.

## C1 -- CLOUD HEAD now carries a reader that must not be deployed, and the record says so

After this act the live code is `fd633ec4d2`, which is NOT on CLOUD. CLOUD HEAD holds rg-1's reader, whose J1 is NOT MET.
- The ledger entry and the round-26 order state: no rivalfunds deploy is built from CLOUD HEAD until RIV-rg-2 has replaced or
  reverted that reader and its J1 is MET.
- One read by the issuer BEFORE 2026-10-08 11:00Z: does any leg the vehicle runs from site Z's WORKING TREE import the rg-1
  reader (the enrichment leg, the collector)? The Lambdas run deployed code; a working-tree leg runs HEAD.
  - (a) None does: nothing more.
  - (b) One does: it is a BLOCKING row tonight, and the reader is reverted on CLOUD before the 11:00Z run.

## C2 -- no served figure moves, and the grade shows it

The prediction reads 0 moved rows of 6,066 and of 1,406, 13 of 13 chart objects with identical data, the audit byte-equal, the
index +154 bytes. The served grade reads the same. A moved table row or a changed chart datum is a rollback to `f9f8334ef6`.

## Accepted

- 0 add, 5 change, 0 destroy, hashes only; `refresh_a1` false; the round-22 half's C1 for a partial republish.
- The one script still makes one call, to this product's chart route.

-- 1.0.0_SA_CTO~Z
