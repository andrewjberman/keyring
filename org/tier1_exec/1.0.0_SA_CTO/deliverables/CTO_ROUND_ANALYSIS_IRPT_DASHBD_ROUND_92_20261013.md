# CTO ROUND-92 ANALYSIS -- IRPT_DASHBD (workstream B) -- answering the round-91 L10 slug (2026-10-13 ~16:3xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** 3.0.0_SA_CVO msg 7061, `surprise-channel/remediations/REMEDIATION_v38.md` @5e23f18556. Row
`IRPT_DASHBD-D2-W137-S1` (BLOCKING, INERT) is owed to this seat. **Prior:** round-91 analysis @3a44c65c3e. **No PRD addendum.**

## 1. What round 91 did

DB-b-171 read the ledger rows behind the 23 differing days:
- Black Diamond's landed transactions: 925 rows;
- the served custody store: 261 rows;
- S3 only, with no vendor call. The variance from "the per-account call" is stated and accepted, because the rows were already landed.

The rule (@e90aabb4cb) was committed before the read. Result: 0 of 23 days reasoned, 0 of 7 windows re-closed. The COO reproduced the
counts from fresh reads. The worker's measured pattern:
- 12 days carry Black Diamond income that is a whole multiple (3x to 6x) of the served income, spread over 3 to 25 rows;
- **on 8 of those 12, the day gap equals minus the served income over the prior day's value, to within 0.01pp.**

## 2. Rulings on the three questions

1. **The two readings of `BD_INCOME_PER_LOT`: Reading B is the meaning.** The test is "at least two income rows whose sum is a whole
   multiple of the served income". The list's author meant several lot rows of one dividend, and Reading A's demand for two distinct
   transaction identifiers was a drafting error. The worker's addendum is adopted as the reading of record. It takes no day either,
   so no count moves.
2. **What a served day shows when only the oracle disagrees: the served figure stands, and the disagreement lives in the tie-out
   record.** FWD-8's first clause ("a day the data cannot support says so") is about OUR inputs: a missing price, an unreconciled
   flow, a large flow. The contract's `day_quality` members already mark those. A day on which our inputs are whole but Black
   Diamond computes differently is not "a day the data cannot support". It is a tie-out disagreement, and it is recorded with its
   reason or `UNEXPLAINED` in the tie-out record. Nothing on the served page changes, and no new `day_quality` member is added.
3. **A further read: yes, one, built on the measured pattern rather than a new vendor call.** "Gap equals minus the served income over
   the prior value" is the signature of Black Diamond's day return EXCLUDING the income that our return includes. Typical causes are
   that it recognises the income on another day, or treats it as leaving the account. That is a testable reason, and it is written
   before a fresh read:
   - `BD_EXCLUDES_SERVED_INCOME`. Test: on the day, the gap is minus the served income over the prior value, within 0.01pp.
     Correction: remove that income from the served day's return, then re-compute the window. The reason is taken only if the
     window re-closes within 0.35pp.
   - Negative arm: the uncorrected windows still miss.
   - The other 15 days are re-tested under the full list, B reading included, after the 8 are corrected.

   A vendor read of Black Diamond's own transaction listing is not wanted: its landed rows were already read, and a second copy of
   the same rows proves nothing new.

## 3. ENRICHMENT LIST for round 92 (ONE issuance)

1. **Ledger leg L7**, carried (2026-10-14 11:41Z).
2. **The `BD_EXCLUDES_SERVED_INCOME` read** (one LOCAL cell over the same stored rows, rule committed before the read). Report per
   account: windows re-closed, days still `UNEXPLAINED` by offset and size. Counts only.
3. **FWD-8 grade** in the drain-end. If any account remains open after item 2, its days come back to this seat once more, and the
   next ruling is on the endpoint, not on another read: whether FWD-8 is accepted with those accounts named as known oracle gaps.
   That decision changes a DONE WHEN, so it would be carried to Andrew as a card.

## 4. Acts only Andrew can do

None now.

-- 1.0.0_SA_CTO~DELL2
