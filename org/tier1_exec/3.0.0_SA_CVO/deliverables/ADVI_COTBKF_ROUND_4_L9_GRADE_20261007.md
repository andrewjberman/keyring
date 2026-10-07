# ADVI_COTBKF round 4 -- L9 grades of the judgment criteria

**archetype:** VALIDATE

Grader: `3.0.0_SA_CVO` (seated on dell2), 2026-10-07 ~08:1xZ-08:4xZ. Input: the drain-end packet
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_4_DRAIN_END_20261007.md` @29479eeb61. Every read below
was made by this seat on dell2 (identity `cloudops-dell2-agent-user`) against the committed deliverables, the dell2 real-run outputs
under `.scratch/advi_cotbkf/`, and S3. Nothing was written to S3.

| criterion | grade | one line |
|---|---|---|
| CB4d1-AC3 | NOT MET | The BARRED half holds; completeness does not: 2 of 35 USABLE buckets were never listed |
| CB4d2-AC3 | MET | One line round 3 cut short now reaches its newest account on its evidence; all 123 evidence items of the 32 new links hold |
| CB4d3-AC3 | MET | 21 of 21 near-match entries are internally consistent; one entry is exact on both sides; B3S775239's row says what happened |
| CB4d5-AC3 | NOT GRADABLE YET | The criterion is graded after the issuer's apply; the run was plan only |

## CB4d1-AC3 -- NOT MET

The criterion: "the census is complete (no unnamed store that holds a per-security daily price in a USABLE bucket) and every BARRED
grade is the registry's, not the seat's."

- **The BARRED half holds.** The script grades from `infra/logic/registry/scopes.json` (`commonwealth_price_census.py:5-11, 126-133`).
  This seat loaded the registry through the script's own `firm_buckets()`: 7 firm buckets, 2 of them cottonwood (`opal-data-cot`,
  `opal-data-cottonwood`). The other 5 are exactly the census's 5 BARRED rows (`opal-data-49financial`, `opal-data-bd`, `opal-data-inf`,
  `opal-data-inflection`, `opal-data-demo`). `barred_read=0`.
- **The census covers the account.** `aws s3api list-buckets` under this identity returns 40 buckets, and the census JSON grades the same
  40, with none missing and none extra.
- **Completeness does not hold.** Two USABLE buckets were never listed: `opal-data-cottonwood` (Cottonwood's own scope bucket) and
  `opalinvest-portal`, both `LIST FAILED: AccessDenied` (row W12-S2). Neither bucket is known to hold no price store, so the criterion's
  negative claim cannot be made for them. The census prints this honestly; the criterion still asks for it.
- **One candidate this seat checked and cleared:** `opal-data-assets/commonwealth/cottonwood/silver/positions/date=2026-06-23/part-00000.parquet`
  (469 rows) has no price or market-value column (`Advisor_ID, AccountNumber, Cusip, FundCode, Symbol, Security_Description, Quantity,
  LongShort_Indicator, Position_Type, AsOfDate, Account_Status, source_*`) and one as-of date, so it is not a missed daily price store.
- **What clears it:** a principal permitted on both buckets lists them and names any price store, or the access is granted read-only
  (an access change: the laptop's under NFRA_CTLPLN v0.12 C-ROLES). Then this criterion is re-graded.

## CB4d2-AC3 -- MET

The criterion: "one client line that round 3 cut short now reaches its newest account, right on its printed evidence; a sample of the
new LINKED rows holds."

- **Round 3's table** is `s3://opal-data-assets/commonwealth/cottonwood/silver/account_links/date=2026-06-23/account_links.csv`
  (459 rows, 180 LINKED). 149 of its LINKED rows point at an account that has no row of its own, so the line stopped there; round 4
  continues 5 of those past the old stop.
- **The line graded:** `cv0QF879236 (2015-11-18..2016-02-02) -> 0QF879236 (2016-02-02..2026-05-01) -> RGY008117 (2026-04-20..2026-05-11)`.
  Round 3 stopped at 0QF879236. The new hop 0QF879236 -> RGY008117 prints 3 of 3 holdings (score 1.0). Read on the transactions
  (`.scratch/advi_cotbkf/tx_cache`, 1,416,497 rows, the round's silver table): 0QF879236 transfers out (`lo`) 50,000 of 743600D21,
  50,000 of 774280X89 and 100,000 of 91282CNT4 on 2026-04-20, and RGY008117 receives (`li`) the same quantities of the same CUSIPs the
  same day. RGY008117 sells all three on 2026-04-22 and its own row reads NOT_LINKED, "closed to cash", so the line's newest account is
  printed right and printed not open.
- **The sample, taken whole:** all 32 LINKED rows that round 3 did not have, 123 evidence items. Each was re-read on the transactions:
  the receiving account's rows of that type, CUSIP and date sum to the printed receipt quantity (within 0.001; 68 single rows, 55
  same-day sums of 2 to 253 rows), the old account held the CUSIP, and the printed end quantity equals the receipt. 123 of 123 hold.
- **Graded on the committed deliverable** (`deliverables/0.9.0_WK_ADVI_COTBKF~13/account_links_r4.csv`, the laptop worker's run: 212
  LINKED). The dell2 real run of the same script (`.scratch/advi_cotbkf/account_links_r4/account_links.csv`: 211 LINKED) differs on 3
  rows. Two of the 32 links graded above (0QF879348 -> B3S606523, B3S780328 -> B3S782287) read NOT_LINKED "closed to cash" on dell2,
  although their evidence holds on the transactions. The third, cv0QF879185, is AMBIGUOUS on the laptop and LINKED on dell2. Row S9.

## CB4d3-AC3 -- MET

The criterion: "the near-match list is readable by Andrew without the method and each entry's evidence is right; B3S775239's row now
says what happened to it."

- **Readable:** `near_matches.md` opens with three plain sentences: what a match is, the 0.80 bar, the 0.65-0.80 band, and that nothing
  below is applied. Each entry then says where each account came from, gives the score as "k of n securities", and lists every security
  with both quantities and a plain tag (EQUAL, DIFFERENT_QUANTITY, NOT_HELD).
- **Internally right:** for 21 of 21 entries, the "k of n" equals the count of EQUAL lines and the count of securities listed.
- **Right on both sources, one entry in full:** entry 1, B3S606724 -> z0927980101 (0.786). The Commonwealth side equals the 2026-06-23
  positions file for all 14 securities (the 15th row, FDIC66853, is the cash sweep). The Cottonwood side equals the account's first
  holdings with securities, 2026-09-11, in the Cottonwood holdings cache (FXNAX 1,632.476, VBITX 298.283, VTIFX 50.444, the other 11
  equal); its rows on 09-09 and 09-10 are cash only.
- **B3S775239:** the crosswalk row reads NOT_MATCHED, score 0.600, "left IN KIND on 2026-04-07 ... best current account z0926725761
  equals 3 of 5 positions", reason code NO_CURRENT_ACCOUNT_HOLDS_POSITIONS. It now says what happened.
- **Note, not a defect:** "first holdings dated" means the first date that holds a security; an account's cash-only rows before it are
  not counted. One clause in the header would say so.

## CB4d5-AC3 -- NOT GRADABLE YET

The criterion is graded "after the issuer's apply: one statement and one tax form found by account and date in the documents table and
opened". Round 4 ran plan only (`DOCUMENTS-PLAN unique=11119 ... refused=0`); no documents table was written. This grade is owed at the
apply and is neither PASS nor FAIL now.

-- 3.0.0_SA_CVO
