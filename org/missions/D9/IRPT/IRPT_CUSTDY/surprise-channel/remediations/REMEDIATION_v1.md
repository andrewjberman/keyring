# IRPT_CUSTDY -- round 1 remediations

<sweep_watermark>2026-10-07T08:52Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2), 2026-10-07 ~09:0xZ. Graduated at this compile (ADJUDICATION_v1.md): 3 rows, all OPEN, round label
v2 (the round after round 1). S3 (BLOCKING) is round 2's first item and blocks FWD-1's hop 1. W1-S1 (BLOCKING, ruled inside the round)
leaves a PRD text and a registry row with the CTO. W4-S1 is a contract question for the CTO and blocks FWD-1's hop 5.

```json
[
 {
  "id": "IRPT_CUSTDY-S3",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "CU-a-1's --pick raises on live data: 482 of 7,022 granted accounts in the live 49 Financial ownership map are refused by the custodian-key projection, and the refusal escapes instead of being counted as uncovered. This compile's read narrows the cause: the refused raw key is a 4-character string that _check_raw rejects as empty, which given ids.py:202-204 is the literal 'None' or 'nan', i.e. a null stringified upstream of the mint.",
  "evidence": [
   "investigation row IRPT_CUSTDY-S3",
   "org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/2.0.0_SA_COO~K2/IRPT_CUSTDY_ROUND_1_DRAIN_END_20261007.md @4b15819af3: 482 of 7,022 refused, 31 of 190 advisors",
   "python data/assets/scripts/gold/irpt_custody/advisor_client_list.py --pick --as-of 2026-09-30 --ownership s3://opal-data-bd/platinum/49financial/ownership_map.json: rc 1, ids.IdRefused 'a raw key must be a non-empty value; got str(len=4, opaque-text)' raised from _ids/ids.py:204 (this compile's read, dell2 CLOUD, 2026-10-07 ~08:5xZ-09:0xZ)",
   "infra/aws/lambda/investor-reporting/_ids/ids.py:202-204: text.lower() in ('nan', 'none') raises 'must be a non-empty value'"
  ],
  "remedy": "Round 2's first item, as the issuer cut it: count a refused account as uncovered and print the count. Separately, find where the projection turns a missing custodian key into the string 'None' (the crosswalk or _ids.projection_for_firm); 482 accounts may be uncovered for that reason alone, not because they lack a key.",
  "owner": "2.0.0_SA_COO~K2",
  "round": "v2",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~K2",
   "round": "v2"
  },
  "closed": true
 },
 {
  "id": "IRPT_CUSTDY-W1-S1",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "The PRD's S01 says the advisor list comes from the directory, but a directory entry carries no advisor; the advisor-to-accounts source is the firm ownership map, whose address is not in the naming registry.",
  "evidence": [
   "investigation row IRPT_CUSTDY-W1-S1",
   "org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/2.0.0_SA_COO~K2/IRPT_CUSTDY_ROUND_1_DRAIN_END_20261007.md @4b15819af3: W1-S1 RULED by the issuer (the map is hop 1's source); the PRD's S01 text and a naming-registry row for the map's address carried to 1.0.0_SA_CTO~DELL2"
  ],
  "remedy": "The CTO corrects S01 to name the ownership map, and the map's address gets a registry row so builder output can name it (CLAUDE.md rule 30); --ownership then defaults to the builder's address.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v2",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v2"
  },
  "closed": false
 },
 {
  "id": "IRPT_CUSTDY-W4-S1",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "irpt-export-render cannot take a client-report document or a template body as it stands (accepts_document=False): no submit-export field carries a document or its address to the bundle freeze, the host input carries a template NAME only, and the third gap (a print page that lays out a document from a data template) was not read.",
  "evidence": [
   "investigation row IRPT_CUSTDY-W4-S1",
   "render_export.cjs:226-234: IRPT_TEMPLATE is a name with the default 'performance-landscape-letter' (this compile's read, dell2 CLOUD, 2026-10-07 ~08:5xZ-09:0xZ)",
   "org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/2.0.0_SA_COO~K2/IRPT_CUSTDY_ROUND_1_DRAIN_END_20261007.md @4b15819af3: 2.0.0_SA_COO~P2 (IRPT_BCKEND) agrees with the reading (msg 167) and sends the contract question to the CTO"
  ],
  "remedy": "A contract ruling: which project owns the document input to the render path (IRPT_BCKEND's export, or a new path for IRPT_CUSTDY), then a cell in that project. Hop 5 of FWD-1 waits on it.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v2",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v2"
  },
  "closed": false
 }
]
```
