# IRPT_DASHBD: remediations, rounds 78 to 82 (workstream B)

<sweep_watermark>2026-10-11T22:30Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T22:30:21Z. Input: msgs 5880, 5882, 5916, 5954, 5956, 5967 and 5975 (IRPT_DASHBD rounds 78 to 82, all terminal; orders DB-b-148 to DB-b-157).
Graduated, round label v83: 6 rows, OPEN, INERT, all owned on another box by the CTO's placement. This seat made no read of its own.

**For the CTO's analysis:**
1. **What these five rounds found is about stores and readers this project does not own.** Each step is one worker's read and no
   served figure was recomputed in any of them:
   - a served price is a median over rows that repeat per portfolio group; on one day 34 of 160 medians move when each id is counted
     once, 2 by more than 1 percent (row D2-W122-S1); and that day's canonical rows were rewritten twice afterwards, so 'the final
     served price' has no single answer (row D2-W125-S1);
   - the original transactions store was rewritten after its copy was taken; the two sampled days' rows were MOVED to files dated two
     days earlier, not lost (rows D2-W124-S1, D2-W126-S1). This seat's round 79 note said 'may be data loss'; that was wrong;
   - three SERVED readers key on the file's day alone and so now place those rows on a different day (row D2-W126-S1). Whether they
     re-ran since, and whether any served figure changed, is not established.
2. **The timing classes are ruled:** the served end-of-day convention closes against the custodian's return in 0 of 51 contested
   segments; 51 close when restated under another timing. Whether that convention stays is the method question you said you owe.
3. Row D2-W113-S2 stays OPEN on the two price paths. The tie-out reads 185 classed, 51 contested, 8 unclassed; not closed.
4. The issuer reports row D2-W124-S1 closed by your msg 5969; this seat has not seen that message and leaves the row OPEN here.

```json
[
 {
  "id": "IRPT_DASHBD-D2-W122-S1",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DB-b-149: on one day, 34 of the 160 per-asset medians the two price paths take over the original Black Diamond store change when each transaction id is counted once (26 under 0.1 percent, 6 between 0.1 and 1 percent, 2 over 1 percent); the Lambda path serves them, so the owner decides which weighting a price should carry.",
  "evidence": [
   "investigation row IRPT_DASHBD-D2-W122-S1",
   "msgs 5880, 5882, 5916, 5954, 5956, 5967 and 5975 (IRPT_DASHBD rounds 78 to 82, all terminal; orders DB-b-148 to DB-b-157)"
  ],
  "remedy": "Owned by the Black Diamond pipeline's fabric, where the CTO placed it: the cause is read from that pipeline's own run record and the effect on each served reader is measured, or the row is closed there with its reason.",
  "owner": "1.0.0_SA_CTO~DELL1",
  "round": "v83",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL1",
   "round": "v83"
  },
  "closed": false
 },
 {
  "id": "IRPT_DASHBD-D2-W122-S2",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DB-b-149: infra/aws/ec2/EC2_MANIFEST.json says the bd_price_update.py script is invoked at the end of the opal-bd-allocation-download SSM sequence, but the repo's SSM document has no price step, and the live Lambda it 'replaces' is the one that ran on 2026-10-11.",
  "evidence": [
   "investigation row IRPT_DASHBD-D2-W122-S2",
   "msgs 5880, 5882, 5916, 5954, 5956, 5967 and 5975 (IRPT_DASHBD rounds 78 to 82, all terminal; orders DB-b-148 to DB-b-157)"
  ],
  "remedy": "Owned by the Black Diamond pipeline's fabric, where the CTO placed it: the cause is read from that pipeline's own run record and the effect on each served reader is measured, or the row is closed there with its reason.",
  "owner": "1.0.0_SA_CTO~DELL1",
  "round": "v83",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL1",
   "round": "v83"
  },
  "closed": false
 },
 {
  "id": "IRPT_DASHBD-D2-W124-S1",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DB-b-151: the original silver transactions day objects of 2026-08-22 and 2026-08-23 now hold 0 rows where the silver_legacy copy holds rows (4545 and 1035 distinct ids, none in common), and 2026-08-24 is the reverse; the original was rewritten after the copy (bucket versions), and the copy is the only store that still holds the first two days' rows as of the copy.",
  "evidence": [
   "investigation row IRPT_DASHBD-D2-W124-S1",
   "msgs 5880, 5882, 5916, 5954, 5956, 5967 and 5975 (IRPT_DASHBD rounds 78 to 82, all terminal; orders DB-b-148 to DB-b-157)"
  ],
  "remedy": "Owned by the Black Diamond pipeline's fabric, where the CTO placed it: the cause is read from that pipeline's own run record and the effect on each served reader is measured, or the row is closed there with its reason.",
  "owner": "1.0.0_SA_CTO~DELL1",
  "round": "v83",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~DELL1",
   "round": "v83"
  },
  "closed": true
 },
 {
  "id": "IRPT_DASHBD-D2-W125-S1",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DB-b-154: the 34 moved medians of 2026-10-09 are the served price in the daily price file and in the first canonical write of that day, but the canonical object's rows for that day were rewritten the same evening (all 34 now linear_interpolation) and again later (28 of 34 yahoo_finance), so 'the final served price' has no single answer.",
  "evidence": [
   "investigation row IRPT_DASHBD-D2-W125-S1",
   "msgs 5880, 5882, 5916, 5954, 5956, 5967 and 5975 (IRPT_DASHBD rounds 78 to 82, all terminal; orders DB-b-148 to DB-b-157)"
  ],
  "remedy": "Owned by the Black Diamond pipeline's fabric, where the CTO placed it: the cause is read from that pipeline's own run record and the effect on each served reader is measured, or the row is closed there with its reason.",
  "owner": "1.0.0_SA_CTO~DELL1",
  "round": "v83",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL1",
   "round": "v83"
  },
  "closed": false
 },
 {
  "id": "IRPT_DASHBD-D2-W125-S2",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DB-b-154: whether the bd_price_update.py script runs today is NOT_ESTABLISHED: the Lambda is shown to write the daily price files, the SSM document is a retired no-op, no rule targets the Lambda, ssm:ListDocuments is denied, and the writer of the four-times-daily canonical rewrites is unidentified.",
  "evidence": [
   "investigation row IRPT_DASHBD-D2-W125-S2",
   "msgs 5880, 5882, 5916, 5954, 5956, 5967 and 5975 (IRPT_DASHBD rounds 78 to 82, all terminal; orders DB-b-148 to DB-b-157)"
  ],
  "remedy": "Owned by the Black Diamond pipeline's fabric, where the CTO placed it: the cause is read from that pipeline's own run record and the effect on each served reader is measured, or the row is closed there with its reason.",
  "owner": "1.0.0_SA_CTO~DELL1",
  "round": "v83",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL1",
   "round": "v83"
  },
  "closed": false
 },
 {
  "id": "IRPT_DASHBD-D2-W126-S1",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DB-b-156: served readers of the original silver transactions store key on the FILE's day (B_03.account_gains.py line 327; bd_price_update.py line 265 and its lambda twin line 143), and all 5580 ids of 2026-08-22 and 2026-08-23 now sit in the files two days earlier, so those three readers place the same ids on a different day than before; owner of the readers is the Black Diamond gold and silver pipeline.",
  "evidence": [
   "investigation row IRPT_DASHBD-D2-W126-S1",
   "msgs 5880, 5882, 5916, 5954, 5956, 5967 and 5975 (IRPT_DASHBD rounds 78 to 82, all terminal; orders DB-b-148 to DB-b-157)"
  ],
  "remedy": "Owned by the Black Diamond pipeline's fabric, where the CTO placed it: the cause is read from that pipeline's own run record and the effect on each served reader is measured, or the row is closed there with its reason.",
  "owner": "1.0.0_SA_CTO~DELL1",
  "round": "v83",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL1",
   "round": "v83"
  },
  "closed": false
 }
]
```
