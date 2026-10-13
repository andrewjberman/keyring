# IRPT_BCKEND: remediations, round 175 (workstream ~P)

<sweep_watermark>2026-10-13T07:16Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-13T07:16:00Z. Follows ADJUDICATION_v76. L8 input: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_175_P_DRAIN_END_20261013.md` (159c5a343b, msg 6837). No judgment criterion.
Graduated, round label v176: 1 row, OPEN, ARMED, owner `2.0.0_SA_COO~P2`. Still ARMED where they stand: D2-W345-S3 (v47, the temp-file fix not on the
host) and D2-W348-S2 (v48, the holdings schema at HEAD's other changes). The portal generator rows are closed on the DEV landing.

```json
[
 {
  "id": "IRPT_BCKEND-D2-W359-S1",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "IB-pr-507's premise does not hold: holdings_49f.py and holdings_inf.py are not among the twelve members of investor-reporting.tar.gz (the object the census reads); they reach the host inside the per-firm package investor-reporting-holdings.tar.gz, which this census did not read.",
  "evidence": [
   "investigation row D2-W359-S1",
   "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_175_P_DRAIN_END_20261013.md"
  ],
  "remedy": "Census the per-firm holdings packages read-only (investor-reporting-holdings.tar.gz, named by IRPT_HOLDINGS_BUNDLE_MAP, fetched at refresh_dispatch.py:65): which firms, the S3 keys, members against HEAD, and commits since each object was written. Only then write the host-bundle pair (the 49F temp-file fix plus account_id), applied at the host's next scheduled Online. Until then D2-W345-S3 stays ARMED.",
  "owner": "2.0.0_SA_COO~P2",
  "round": "v176",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~P2",
   "round": "v176"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~P2",
   "at": null
  }
 }
]
```
