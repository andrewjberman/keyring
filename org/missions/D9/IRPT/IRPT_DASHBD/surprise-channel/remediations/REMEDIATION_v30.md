# IRPT_DASHBD: remediations, rounds 71 to 73 (workstream B)

<sweep_watermark>2026-10-11T18:41Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T17:57:20Z. Input: msg 5485 (IRPT_DASHBD rounds 71 and 72 drained; DSGN_IRPTV1 round 23, two of three cells drained, portal DEV ca23f110).
Graduated, round label v73: 1 row, OPEN, INERT. This seat made no read of its own for this compile.

**For the CTO's analysis:**
1. **The thresholds exposure is sized as a ceiling, not a count:** 569 manifest keys by listing, 0 bodies read. Row D2-W100-S3 stays
   open in REMEDIATION_v28 until a release and a decision on the manifests already served.
2. **The tie-out is not closed:** 185 classed, 51 contested, 8 unclassed; on 18 of the 51 the custodian's flow rows do not
   reproduce the served flow day by day (row D2-W111-S1).
3. The R45 release packet, refresh 4, waits on your half.

4. **Round 73** (msg 5584, one order, DB-b-139, drained @a64fdd3311; no judgment criterion; not read by this seat): the kit on the
   six-key thresholds file reads 5 of 5 tables byte-equal; its never-widen packet is written with both halves unsigned, ordered
   after refresh 4. Whether the halves are signed now or after refresh 4's first fire is the issuer's ask to you.

Released from the HELD file at 2026-10-11T18:41:22Z: TO-DB-b-139 is terminal and no IRPT_DASHBD order is open (this seat's count of the order files).

```json
[
 {
  "id": "IRPT_DASHBD-D2-W111-S1",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DB-b-138: in 18 of the 51 flow-class segments the custodian's external-flow transaction rows (by return date) do not reproduce the served flow dollars day by day, though the same flow days appear and the segment dollars tie to Black Diamond net additions; the daily value series shows the entry DAY of a flow but no row or series read separates START, MID and END.",
  "evidence": [
   "investigation row IRPT_DASHBD-D2-W111-S1",
   "msg 5485 (IRPT_DASHBD rounds 71 and 72 drained; DSGN_IRPTV1 round 23, two of three cells drained, portal DEV ca23f110)"
  ],
  "remedy": "The 18 segments are read day by day against the custodian's flow rows until the difference has a cause, or the tie-out states them as unreconciled where it is shown.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v73",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v73"
  },
  "closed": true
 }
]
```
