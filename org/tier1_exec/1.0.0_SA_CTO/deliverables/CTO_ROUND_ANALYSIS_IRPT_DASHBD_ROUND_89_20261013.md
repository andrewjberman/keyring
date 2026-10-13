# CTO ROUND-89 ANALYSIS -- IRPT_DASHBD (workstream B) -- answering the round-88 L10 slug (2026-10-13 ~13:5xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** 3.0.0_SA_CVO msg 6954, `surprise-channel/adjudications/ADJUDICATION_v52.md` @50d8780e32:
1 row dismissed (D2-W132-S1, an issuer check defect closed by amendment @a47ba859cd), nothing graduates, ARMED 0.
**Prior:** the round-88 analysis @e53edd32d7. **PRD addendum:** v0.12, decision 11a. It changes no ENDPOINT text, so no half re-opens.

## 1. What round 88 did

DB-b-166 (LOCAL; counts over the stored tie-out set; no vendor call; nothing served moved) computed the tie-out under both flow
conventions over the 88 flow-bearing gradable segments:

| convention | segments it closes that the other misses |
|---|---|
| vendor default | 76 |
| all-end | 0 |

Neither closes 12. Verdict, by the rule written before the count: `BD_DEFAULT`. The negative arm holds: the all-end convention misses
all 76. All 12 that neither closes are outside the contested 51.

## 2. Measured by this seat

Nothing re-run. The module reads private client tables; the COO read it line by line and re-ran DB88-1-AC1 (PASS), and the CVO read
the ancestry. This analysis rests on those reads and says so.

## 3. Ruling (PRD v0.12, decision 11a)

The tie-out reads Black Diamond under `BD_DEFAULT`, measured by the count, not taken from a vendor statement. A disagreeing day the
default explains carries "flow timing" as its stated reason. The 12 segments neither convention closes still owe a reason: FWD-8's
ACCEPT requires "every day they disagree carries a stated reason".

## 4. ENRICHMENT LIST for round 89 (ONE issuance)

1. **Ledger leg L7** (`2.0.0_SA_COO~D2`), carried: the 2026-10-14 11:41Z fire closes the thresholds-swap ledger, or rollback.
2. **The 12 unexplained segments** (one read-only cell, LOCAL, over the same stored set):
   - Give each of the 12 one stated reason from a closed list written into the criterion before the read: missing price, income
     dated off the flow day, a flow on a non-trading day, a flow absent on one side, or `UNEXPLAINED`.
   - Each reason is shown by a count or a date pair from the stored rows, never asserted.
   - Negative arm: a segment that gets a reason is re-computed with that cause corrected, and it closes within 0.35pp. A reason whose
     correction does not close the segment is not a reason, and the segment stays `UNEXPLAINED`.
   - `UNEXPLAINED` above 0 is reported per account. It means FWD-8 is not met for that account, and it goes in a surprise row.
3. **FWD-8 grade read** after item 2, by the COO in its drain-end: per account and window, agreement within 0.35pp under `BD_DEFAULT`,
   and every disagreeing day carrying a stated reason. The label and guard clauses of FWD-8 are graded where their own cells already
   proved them; cite those cells, not re-run them.

## 5. Acts only Andrew can do

None.

-- 1.0.0_SA_CTO~DELL2
