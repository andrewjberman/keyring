# IRPT_CUSTDY -- round 2 remediations

<sweep_watermark>2026-10-07T09:40Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2), 2026-10-07 ~09:5xZ. Graduated at this compile (ADJUDICATION_v2.md): 3 rows, all OPEN, round label
v3. W5-S1 is IRPT_BCKEND's seam file and goes to the CTO; S4 is a laptop read owed as a file; S5 is a provisioning word.

```json
[
 {
  "id": "IRPT_CUSTDY-W5-S1",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "infra/aws/lambda/investor-reporting/_ids/data/custodian_key_seam.json holds 826 values as the string 'None' (a null schwab_account_id stringified when the file was written), and ids.py's project() guard 'if mapped is not None' passes the string to the mint, which refuses it: 482 of 7,022 granted 49 Financial accounts are uncovered for that reason alone.",
  "evidence": [
   "investigation row IRPT_CUSTDY-W5-S1",
   "custodian_key_seam.json: 826 of 6,218 leaf values equal the string 'None' (this compile's read, dell2 CLOUD, 2026-10-07 ~09:5xZ)",
   "infra/aws/lambda/investor-reporting/_ids/ids.py:385-388 (if mapped is not None: return base('account', mapped)) (this compile's read, dell2 CLOUD, 2026-10-07 ~09:5xZ)",
   "org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/2.0.0_SA_COO~K2/IRPT_CUSTDY_ROUND_2_DRAIN_END_20261007.md @48a4904aae: CU-b-1 AC3 NONE-SOURCE refused=482 distinct=7022 via_none=482; the writer is not in the repo (47f21dab95 adds the artifact only)"
  ],
  "remedy": "IRPT_BCKEND's: the seam file carries a null as absent (or the guard treats 'None' and 'nan' as absent), then the 482 are re-read; how many have a real key is the measure. Routed by the issuer to the CTO.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v3",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v3"
  },
  "closed": false
 },
 {
  "id": "IRPT_CUSTDY-S4",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "opal-data-49financial explicitly denies the dell2 identity, so CU-b-3's figures (hop 3) cannot read the real returns gold from dell2; the read is relayed to a laptop seat as a script, with no file back yet.",
  "evidence": [
   "investigation row IRPT_CUSTDY-S4",
   "org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/2.0.0_SA_COO~K2/IRPT_CUSTDY_ROUND_2_DRAIN_END_20261007.md @48a4904aae: CU-b-3 NOT RUN on real data; laptop read relayed (msgs 234/235, script @b97c663aa9)"
  ],
  "remedy": "The laptop seat returns the read as a FILE and 2.0.0_SA_COO~K2 files it; no policy is widened.",
  "owner": "2.0.0_SA_COO~K2",
  "round": "v3",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~K2",
   "round": "v3"
  },
  "closed": false
 },
 {
  "id": "IRPT_CUSTDY-S5",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "E3 (the portal cell) is held: dell2 has no portal node_modules, and installing them is npm egress off Opal infrastructure.",
  "evidence": [
   "investigation row IRPT_CUSTDY-S5",
   "org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/2.0.0_SA_COO~K2/IRPT_CUSTDY_ROUND_2_DRAIN_END_20261007.md @48a4904aae: E3 HELD, not cut"
  ],
  "remedy": "Provision dell2's portal dependencies on Andrew's word through its fabric manager, or cut E3 on a box that has them.",
  "owner": "0.0.0_AB_MSTR~DELL2",
  "round": "v3",
  "remediation": {
   "state": "OPEN",
   "owner": "0.0.0_AB_MSTR~DELL2",
   "round": "v3"
  },
  "closed": false
 }
]
```
