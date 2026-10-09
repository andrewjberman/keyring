# IRPT_DASHBD -- round 49 remediations

<sweep_watermark>2026-10-09T15:56Z</sweep_watermark>

Round 49 L8 compile by 3.0.0_SA_CVO (seated on dell2), 2026-10-09 ~15:5xZ. L8 input: `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND49_B_DRAIN_END_20261009.md @dfba2660aa (msg 3603)`. 4 of 4 orders complete, MAY-CLOSE.
Graduated, round label v52: 3 rows, OPEN; IRPT_DASHBD-D2-S5 ARMED (client account data in git, one file already on the remote).

Also for the analysis: DB-b-99's thresholds are pre-registered and ZERO_GAIN_VENDOR_TWR failed its robustness test (its 45 segments
re-graded UNEXPLAINED) -- the honest result; DB-b-102's emit_method_row(src=None) still writes row 2, a residual default path.

```json
[
  {
    "id": "IRPT_DASHBD-D2-S5",
    "project": "IRPT_DASHBD",
    "fabric": "dell2",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "Client account data is committed to git: org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~76/W73_S2_EVIDENCE.json (121 distinct 10-digit account numbers with begin/end values, balances, fees and flows) is on origin box/dell2 AND origin CLOUD (github Opal-Capital/ajb_workspace); org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~75/W73_S1_EVIDENCE.json (74 accounts, values, fees, gains) is committed locally @f5645bb6e9 and goes out at the next box-sync push. The issuer's own packet asked whether this is acceptable; it is not -- the estate keeps client figures out of the repo (ADVI_BILLING held its real render outside git for exactly this reason).",
    "evidence": [
      "investigation row IRPT_DASHBD-D2-S5",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND49_B_DRAIN_END_20261009.md @dfba2660aa (msg 3603)"
    ],
    "remedy": "Hold the push of f5645bb6e9; remove both evidence files from the tree (move them outside the repo, as ADVI_BILLING's private render is); add a commit-time refusal for account-number patterns in deliverables; Andrew decides whether origin's history is purged.",
    "owner": "1.0.0_SA_CTO~DELL2",
    "round": "v52",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL2",
      "round": "v52"
    },
    "closed": false,
    "disarm": {
      "state": "DISARMED",
      "owner": "0.0.0_AB_MSTR~DELL2",
      "at": "2026-10-09T15:59:45Z"
    }
  },
  {
    "id": "IRPT_DASHBD-D2-W75-S1",
    "project": "IRPT_DASHBD",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "All 74 W73-S1 DEFECT segments read BD_SIDE; 73 of the 74 turn on two conventions the producer declares (SERVICE FEE rows stay inside the return; income counts on cash receipt) and 1 on a net-zero securities transfer BD books as a withdrawal.",
    "evidence": [
      "investigation row IRPT_DASHBD-D2-W75-S1",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND49_B_DRAIN_END_20261009.md @dfba2660aa (msg 3603)"
    ],
    "remedy": "Rule the FWD-8 comparator: follow Black Diamond on service fees and income timing, or keep Opal's declared conventions and state each such segment's convention as its reason.",
    "owner": "1.0.0_SA_CTO~DELL2",
    "round": "v52",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL2",
      "round": "v52"
    },
    "closed": false
  },
  {
    "id": "IRPT_DASHBD-D2-W75-S2",
    "project": "IRPT_DASHBD",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Dollars are explained for all 74 segments but the RETURN gap is not closed for most: restating our daily series to BD's income and service-fee convention brings the linked return within 0.35pp of the tie-out's BD gross return in only 14 of 74.",
    "evidence": [
      "investigation row IRPT_DASHBD-D2-W75-S2",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND49_B_DRAIN_END_20261009.md @dfba2660aa (msg 3603)"
    ],
    "remedy": "After the convention ruling, re-grade the 74 segments; trace the 30 still over 2pp; treat the three income-row matches among 8+ candidates as unconfirmed until read two-sided.",
    "owner": "2.0.0_SA_COO~D2",
    "round": "v52",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D2",
      "round": "v52"
    },
    "closed": false
  }
]
```
