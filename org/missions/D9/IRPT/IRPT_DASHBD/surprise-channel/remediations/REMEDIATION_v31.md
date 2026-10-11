# IRPT_DASHBD: remediations, round 74 (workstream B)

<sweep_watermark>2026-10-11T19:17Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T19:17:34Z. Input: msg 5629 (IRPT_DASHBD round 74 drained @f7b1cc4571, DB-b-140; record deliverables/0.9.0_WK_IRPT_DASHBD~113/UNREPRODUCED_18.json).
Graduated, round label v75: 2 rows, OPEN, INERT. This seat made no read of its own for this compile.

**For the CTO's analysis:**
1. **The 18 unreproduced segments are reported to have one cause, in the comparison and not in the served flow:** the ledger copy
   holds a transaction once per portfolio group. Counting each id once ties 50 of 50 days to the cent. This is one worker's read;
   the issuer did not re-run it and neither did this seat. Row D2-W111-S1 is left OPEN for you to close.
2. **The duplication is a property of a shared copy** (row D2-W113-S2). Any other reader that sums it without the id counts a
   transaction several times. Not established: whether one does.
3. **A tolerance hid one more differing day** (row D2-W113-S3): a small fee row the served flow does not carry.
4. The tie-out reads 185 classed, 51 contested, 8 unclassed; not closed.

```json
[
 {
  "id": "IRPT_DASHBD-D2-W113-S2",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DB-b-140: the Black Diamond transactions copy (silver_legacy/transactions) holds one row per (transaction id, portfolio group), so a transaction in k groups is landed k times; a reader that sums its rows by return date without keying on transaction id counts the transaction k times. This is the cause of the 18 unreproduced tie-out segments (50 flow days, all reproduced to the cent by counting each transaction id once).",
  "evidence": [
   "investigation row IRPT_DASHBD-D2-W113-S2",
   "msg 5629 (IRPT_DASHBD round 74 drained @f7b1cc4571, DB-b-140; record deliverables/0.9.0_WK_IRPT_DASHBD~113/UNREPRODUCED_18.json)"
  ],
  "remedy": "Every reader of that transactions copy is listed and each is read for whether it keys on the transaction id; a reader that sums rows without it is corrected or its figure withdrawn.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v75",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v75"
  },
  "closed": false
 },
 {
  "id": "IRPT_DASHBD-D2-W113-S3",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DB-b-140: worker ~111's comparison tolerance, max(1.00, 0.1 percent of the day's flow), hid one more differing flow day in one of the 18 segments: at the cent the ledger carries a small 'Other Fee' expense row that the served flow does not.",
  "evidence": [
   "investigation row IRPT_DASHBD-D2-W113-S3",
   "msg 5629 (IRPT_DASHBD round 74 drained @f7b1cc4571, DB-b-140; record deliverables/0.9.0_WK_IRPT_DASHBD~113/UNREPRODUCED_18.json)"
  ],
  "remedy": "The comparison is re-read at the cent, and the one fee row is classed: a flow the served number should carry, or an expense it rightly leaves out.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v75",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v75"
  },
  "closed": false
 }
]
```
