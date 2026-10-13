# IRPT_DASHBD: remediations, round 92

<sweep_watermark>2026-10-13T16:48Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-13T16:48:00Z. Follows ADJUDICATION_v56. L8 input: `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND92_B_DRAIN_END_20261013.md @b67ea51d2c` (msg 7079). No judgment criterion.
Graduated, round label v93: 1 row, OPEN, BLOCKING, owner `1.0.0_SA_CTO~DELL2`: the ENDPOINT decision on 3 accounts (a card to Andrew), and whether a
reason whose test and correction are one identity counts as a stated reason.

```json
[
 {
  "id": "IRPT_DASHBD-D2-W138-S1",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "Under RULE_EXCL.md as committed, BD_EXCLUDES_SERVED_INCOME takes 13 of the 23 differing days (its test holds on the same 13, and every one re-corrects within 0.01 pp); 4 of 7 windows re-close at 0.35 pp, 3 stay open with 10 UNEXPLAINED days (offsets and sizes in world_is).",
  "evidence": [
   "investigation row D2-W138-S1",
   "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND92_B_DRAIN_END_20261013.md @b67ea51d2c",
   "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~138/EXCLUDES_INCOME_23_DAYS.json (this seat's read: per-account sums 23 differing = 13 taken + 10 UNEXPLAINED; test_held_days 13; rule d8a3f1fa58 committed 12:29 before the record 12:38 -04:00)"
  ],
  "remedy": "FWD-8 is NOT REALIZED for 3 accounts (1, 5, 6 of the round-90 list; 10 UNEXPLAINED days) and met for the other 83. The next act is an ENDPOINT decision, not another read, so it is the CTO's to carry to Andrew as a card: accept FWD-8 with those 3 accounts named as known oracle gaps, or not. Two points for that card: (1) BD_EXCLUDES_SERVED_INCOME's test and its correction are one identity, so the 4 re-closed windows close by construction where the test holds; the information is that the test holds on 13 days and that whole windows then re-close. The CTO rules whether such a descriptive reason is a 'stated reason' under FWD-8. (2) Account 5's three UNEXPLAINED days are all under 0.07 pp.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v93",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v93"
  },
  "closed": false
 }
]
```
