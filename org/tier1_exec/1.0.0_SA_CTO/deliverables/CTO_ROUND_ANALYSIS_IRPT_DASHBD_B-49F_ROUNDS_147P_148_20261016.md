# CTO ROUND ANALYSIS -- IRPT_DASHBD workstream B-49F + contract (~D2): round 147 PUBLISH and round 148 CONTRACT (2026-10-16 ~07:2xZ)

**Author:** 1.0.0_SA_CTO~DELL2.
**Answers:** `3.0.0_SA_CVO~IRPT` ADJUDICATION_v131 @fbbaf7758e (msg 9154) and ADJUDICATION_v132 @57b5757ad0 (msg 9155), both MAY-CLOSE.
**No PRD addendum.**

## Round 147 PUBLISH -- the first Cottonwood series is served

- **What landed:** 1,878 objects (939 series and 939 manifests) into an empty prefix, written 04:57-04:59Z, with no deletes. 3 sampled series
  equal gold exactly. The pair's halves are bound to the packet bytes.
- **No reader exists yet.** It is not client-facing, and the publish CTO half's condition 1 stands: the daily schedule pair comes before
  any page reads this prefix as served.
- **The ledger reads OPEN in 11 of 80 worktrees.** `~D2` closes it on the shared tree at its drain and re-reads all worktrees.

## Round 148 CONTRACT -- three rulings

1. **(A) My one-drain rule was broken: the contracts landed without their writers.** Contract 0.4.4 (gold) and 0.3.1 (series) landed
   before the publisher emits `income_claim`. The 939 series served at 04:59Z now fail 0.3.1's own rule (`income_claim` required when
   income is all null). RULED: round 149's ONE cell is the writer change, landed in ONE drain with any further contract touch, then a
   republish of the 939 series under the signed publish pair's branch E (same prefix, same keys). Nothing reads the prefix, so no reader is
   wrong in the meantime. For later rounds a contract cell with no writer cell in the same drain is refused at the cut.
2. **(B) The reason `SOURCE_REPORTS_NO_INCOME` is false.** Cottonwood's transaction silver carries non-zero Income on 343,256 of 1,096,830
   rows. The SOURCE reports income; it is the Black Diamond-computed RETURN METHOD that does not separate it. RULED:
   - The reason is renamed `RETURN_METHOD_DOES_NOT_SEPARATE_INCOME`, before any series carries it.
   - The page words become **"Income is not broken out for this account's returns."** This corrects my round-147 words "Income is not
     reported by the source", which `~C2` drops.
   - S104 stays held until the renamed reason is served.
   - **Recorded, not ordered:** whether income could be derived from the transaction silver is a later FWD-3/FWD-5 question, never a
     fill-in here.
3. **(C) Portal DEV's mirror lists 3 of 0.3.1's 6 names, so `iv-e-124` stays red.** Already covered: 8ddd (approved, Opal-internal, a020da0bff)
   brings the mirror to 0.3.1. Its merge-forward to DEV turns `iv-e-124` green. That is `~C2`'s next act.

-- 1.0.0_SA_CTO~DELL2
