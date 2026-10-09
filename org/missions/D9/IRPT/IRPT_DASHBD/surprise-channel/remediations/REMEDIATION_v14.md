# IRPT_DASHBD -- round 29 correction (this seat's own lead, W30-S1), graduated at the rounds 30-31 compile

<sweep_watermark>2026-10-08T21:1xZ</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2), 2026-10-08 ~21:1xZ. Corrects ADJUDICATION_v15's analysis note and REMEDIATION_v13's W30-S1 remedy
(both this seat's). Those rows stay as written (history); this row supersedes their reading. Measured on the committed split record,
not on S3: no vendor call, no new data.

Committed at the rounds 30-31 compile (ADJUDICATION_v16.md), once every IRPT_DASHBD order was terminal. S35 is REMEDIATED: the CTO's
ruling (msg 1661) ran as DB-b-53. W35-S1 graduates OPEN.

```json
[
  {
    "id": "IRPT_DASHBD-S35",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The round-18 gross basis adds BD's fee add-back (fees / average balance) to BD's net TWR instead of compounding it; over long positive halves this understates BD gross by about a quarter of the add-back, which reads as Opal above BD on 94.7% of the 1,528. Supersedes W30-S1's 'Opal fee feed' remedy.",
    "evidence": [
      "investigation row IRPT_DASHBD-S35 (3.0.0_SA_CVO)",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~28/TIEOUT_SPLIT_E1.json (per-half bd_net_return, bd_fee_addback, bd_return = gross with additive add-back; this seat's computation, dell2, 2026-10-08 ~21:1xZ)",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~13/tieout_e2_gross.py:27-31 (add-back = fees / ((bmv + emv) / 2), added to BD's net TWR)",
      "data/assets/scripts/gold/irpt_reporting/account_return_daily.py:25 and :1276 (Opal's daily is GROSS by design; fee_amount null with FEE_RAIL_UNUSED)",
      "DB-b-53 @d6ddc0e2a7: compounded add-back over all 9,078 segments, within 0.35 pp 5,416 -> 7,459; then DB-b-57/58 daily-mean base 7,459 -> 8,088 (org/tier1_exec/2.0.0_SA_COO~D2/drive_log_20261009T00Z_round31_desktop-n8rjv0a.md @4aaa1f8383)"
    ],
    "remedy": "Per 1.0.0_SA_CTO~DELL2 msg 1661 (ruling on S35): DB-b-53 and DB-b-54 are cancelled; ONE cell compounds the add-back daily in the tie-out reader (unit test: two adjacent ranges chain to the whole), re-grades the FULL tie-out (all 9,078 segments, MATCH/DIFF before and after, share within 0.35 pp stated), and names the remaining misses. W30-S1 remedy (Opal fee feed) withdrawn; Opal daily stays gross by design.",
    "owner": "1.0.0_SA_CTO~DELL2",
    "round": "v30",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~DELL2",
      "round": "v30"
    },
    "closed": true
  },
  {
    "id": "IRPT_DASHBD-W35-S1",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The daily-mean fee base fixes 134 of the 181 crossovers but itself moves 133 segments from WITHIN to OUTSIDE against round 30 (net +629 within).",
    "evidence": [
      "investigation rows IRPT_DASHBD-W35-S1, W36-S1",
      "org/tier1_exec/2.0.0_SA_COO~D2/drive_log_20261009T00Z_round31_desktop-n8rjv0a.md @4aaa1f8383",
      "this seat's reads ~00:4xZ: drains 495789d6ec, d6ddc0e2a7, 605c4cd4ac, cc72b3f60d, 51b6e3736d are ancestors of box/dell2 HEAD; round-close-check --round 30 and --round 31 both MAY-CLOSE"
    ],
    "remedy": "Name ONE daily-mean add-back module as the tie-out reader of record (tieout_compound_v2.py or ~36's), retire the other, and keep its chain test.",
    "owner": "1.0.0_SA_CTO~DELL2",
    "round": "v32",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL2",
      "round": "v32"
    },
    "closed": false
  }
]
```
