# IRPT_DASHBD: remediations, round 90

<sweep_watermark>2026-10-13T15:33Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-13T15:33:00Z. Follows ADJUDICATION_v54. L8 input: `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND90_B_DRAIN_END_20261013.md @0ff19e814e` (msg 7027). No judgment criterion.
Graduated, round label v91: 1 row, OPEN, owner `1.0.0_SA_CTO~DELL2`: the 7 accounts after the day-grain read, with the measured income and flow multiples.

```json
[
 {
  "id": "IRPT_DASHBD-D2-W136-S1",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "Under the day rule committed before the read, all 23 differing days of the 7 UNEXPLAINED segments stay UNEXPLAINED; no account's window re-closes at 0.35 pp, so FWD-8 is not realized for any of the 7 accounts.",
  "evidence": [
   "investigation row D2-W136-S1",
   "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND90_B_DRAIN_END_20261013.md @0ff19e814e"
  ],
  "remedy": "FWD-8 stays NOT REALIZED for 7 accounts: at day grain 23 of 103 days differ (about 0.03 pp to 32 pp), none takes a closed-list reason, and only 3 are flow days. The data point to a measured pattern that is not yet a reason: on 12 days Black Diamond's income is a whole multiple (3x to 6x) of the served income, on 2 days its flow is 3x or 4x. The CTO rules: a ledger-row read for those 23 days against the series (testing a duplicate or a different booking date in one source), a further closed-list reason with a test, or a ruling on the 7. Also the CTO's: whether 11b's day clause owes a day read for the 7 windows already reasoned at window grain.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v91",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v91"
  },
  "closed": false
 }
]
```
