# IRPT_BCKEND: remediations, round 167 (workstream ~P)

<sweep_watermark>2026-10-12T21:08Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-12T21:08:00Z. Follows ADJUDICATION_v68. L8 input: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_167_P_DRAIN_END_20261012.md` (blob 0322ee98d6, msg 6555). No judgment criterion.
Graduated, round label v168: 1 row, OPEN, owner `2.0.0_SA_COO~P2`; ARMED 0 (D2-W337-S2 disarmed: it fails safe at the digest gate).
Still OPEN from REMEDIATION_v41: D2-W321-S1 (C-VALUEFACTS: the portal reader, step 1, is a candidate on branch wk-IRPT_BCKEND-338-portal
@183860ba, unpushed; bd_adapter's rename, step 2, is merged and unapplied. This seat's v0.50 condition holds: the reader lands on PROD
before the Lambda half applies, and a PROD push of the Reporting tab waits on Andrew).
For the CTO: the IB-pr-482 CTO half is unsigned; nothing is applied.

```json
[
 {
  "id": "IRPT_BCKEND-D2-W337-S2",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "lambda-source-map.json still pins irpt-performance-adapter's holdings_gold.py at 361c44fa9d (sha256 d41e861212a7); a build from the REAL map reproduces the live bytes, not the signed ones, until the apply order lands the one re-pin.",
  "evidence": [
   "investigation row D2-W337-S2",
   "row D2-S111 (disarm evidence)",
   "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_167_P_DRAIN_END_20261012.md"
  ],
  "remedy": "The IB-pr-482 apply order's FIRST criterion re-pins holdings_gold.py in lambda-source-map.json to 05219b8444's bytes (sha256 5be3ce009412...), and names the live artifact's S3 object version before any upload. Until then a build from the real map reproduces the live bytes and the BUILD_ONLY digest gate aborts.",
  "owner": "2.0.0_SA_COO~P2",
  "round": "v168",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~P2",
   "round": "v168"
  },
  "closed": false,
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~P2",
   "at": "2026-10-12T21:08:00Z"
  }
 }
]
```
