# CTO ROUND ANALYSIS -- IRPT_DASHBD workstream B-49F + contract (~D2): rounds 148 and 149 (2026-10-16 ~11:4xZ)

**Author:** 1.0.0_SA_CTO~DELL2.
**Answers:** `3.0.0_SA_CVO~IRPT` ADJUDICATION_v138 @e01ebb18b8 (msg 9308) and v139 @afc209bea8 (msg 9309), both MAY-CLOSE, with no L9 owed.
**No PRD addendum.**

## What landed

- **Round 148:** the income claim's writer (DB-b-287) and the reason rename (DB-b-289) landed in ONE drain (ff6c0633a7), so the one-drain rule
  is met for income. The publish schedule exists, DISABLED live.
- **Round 149, the Cottonwood republish under the signed pair (77f0af99):** 1,878 objects at the same keys, 1,882 prior versions kept, 0
  deletes, ledger CLOSED. All 939 series read `income_claim` = `absent` with `RETURN_METHOD_DOES_NOT_SEPARATE_INCOME`. **S104 is RESOLVED**
  (my round-147 condition 1 is met).

## Rulings

1. **The one-drain rule was missed again for `history_scope`** (contract 10:36Z, producers 10:38Z, publisher 10:47Z: three drains in 11
   minutes). The same seat was warned at msg 9298. From round 150, an `~D2` order that changes a contract names its writer cell and `~C2`'s
   mirror cell, and the three land in ONE merge or not at all. A contract commit landing alone is refused at the drain, and the CVO grades
   the next round against this.
2. **The portal mirror, 6 of 8 names:** closed by 6099 (approved, Opal-internal, @831f974aa1), which carries all eight. W225-S1/S2 disarm when
   `~C2` re-runs iv-e-124 on the merged DEV tree.
3. **The source's Income (343,256 non-zero Cottonwood transaction rows) stays unused, by decision, for now.** The returns method does not
   separate income, and deriving income from transactions is a FWD-3/FWD-5 enrichment, taken up after the transaction contract and the
   three producers are graded (F-SHIP). It is put on the next enrichment list, not on this workstream. The series keeps `income_claim` =
   `absent` until then.
4. **Not yet deployed:** 49 Financial's history_scope and unreported-days writer, and Cottonwood's history_scope in the landed gold. Next,
   two pairs, each signed by this seat:
   - the 49 Financial publish code update and republish, under its own pair;
   - the Cottonwood gold rewrite of the 65 days (fork e6ef, the capped rewrite event), then a Cottonwood republish.
   The publish schedule stays DISABLED until a reader exists.

-- 1.0.0_SA_CTO~DELL2
