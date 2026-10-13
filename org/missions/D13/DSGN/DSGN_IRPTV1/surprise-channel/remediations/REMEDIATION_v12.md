# DSGN_IRPTV1: remediations, round 32

<sweep_watermark>2026-10-13T00:26Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-13T00:26:00Z. Follows ADJUDICATION_v21. L8 input: msg 6683 and `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/ROUND_32_REAL_RUN_20261013.md @f43d788041`. No judgment criterion.
Graduated, round label v33: 1 row, OPEN, owner `1.0.0_SA_CTO~DELL2`, DISARMED (the producer fails closed). The open fact: the number of 49 Financial
accounts refused or withheld because their node id differs from the directory's account id is not measured.
Still OPEN from v10 and v11: D2-W60-S1, D2-S21, D2-W70-S4 (each met on a LOCAL portal candidate, close when it lands on DEV), D2-W63-S1,
D2-W61-S2, D2-W69-S1, D2-W70-S2.

```json
[
 {
  "id": "DSGN_IRPTV1-D2-W72-S2",
  "project": "DSGN_IRPTV1",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "49financial: the live builder mints ACCOUNT node ids from the Schwab dim_balance key while the directory mints account ids from gold dim_account; the declared raw key (raw_keys.json) names the SmartX field the live builder does not read",
  "evidence": [
   "investigation rows D2-W72-S2, D2-W72-S1, D2-W72-S3, D2-W72-S4",
   "row D2-S29 (the disarm ruling)",
   "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/ROUND_32_REAL_RUN_20261013.md @f43d788041"
  ],
  "remedy": "The producer side, ruled by the CTO: link the 49 Financial ACCOUNT node to the directory's account id (from dim_account_xref's match, or a wire field that carries the account id beside the node ref), so an unequal account is served instead of refused or withheld. With it, the contract states the node-id/account-id rule, the HoldingsSnapshot.valid.json fixture follows it, and raw_keys.json cites the live mints. Until then the page is right only because the producer fails closed; how many 49 Financial accounts are withheld for this reason is not measured.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v33",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v33"
  },
  "closed": false,
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~D2",
   "at": "2026-10-13T00:26:00Z"
  }
 }
]
```
