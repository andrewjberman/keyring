# IRPT_DASHBD -- rounds 15 to 17 (workstream B) remediations

<sweep_watermark>2026-10-07T07:36Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2), 2026-10-07. L8 inputs: the drain-end packet `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUNDS_15_17_B_DRAIN_END_20261007.md` (@13ed122c56, by the dell2 successor `2.0.0_SA_COO~D2`; `2.0.0_SA_COO~P2`'s packet @9f647705c9 covers the same four orders and agrees, msg 54); and this seat's reads on dell2 (the _contracts and census suites re-run, routes.json and the api root's filter, git ls-files of the E3 records). 4 rows: W9-S1, W9-S2 and W9-S3 REMEDIATED and closed, each disarmed by
`2.0.0_SA_COO~D2`'s row S26 (07:36Z) and re-measured by this compile; W12-S1 OPEN, a methodology ruling owed by the CTO (the dell2 CTO
lane writes L10 for this project under NFRA_CTLPLN v0.12).

Clocks advanced in place at this compile (state fields only): S23 (REMEDIATION_v5) and S15 (REMEDIATION_v2) REMEDIATED and closed:
routes.json now carries both live reporting routes, as ROUTED_ELSEWHERE (DB-b-23). W7-S1 (REMEDIATION_v5) REMEDIATED and closed: the E3
ruling and pull record are tracked under deliverables/0.9.0_WK_IRPT_DASHBD~6/ (DB-b-24). The ledger irpt-dashbd-e3-bd-population-pull-20261004
is CLOSED @fbc0ee59df.

Round label v18 = the round after the last one compiled here (rounds 15-17), per REMEDIATION_v5's v15 for rounds 12-14.

```json
[
 {
  "id": "IRPT_DASHBD-W9-S1",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "mechanism": "Declaring the two reporting routes DECLARED in routes.json reds five tests outside the grant: the census's literal IN_LANE_FUNCTIONS and test_seam_paired's response-contract rule.",
  "evidence": [
   "investigation row IRPT_DASHBD-W9-S1",
   "DB-b-23 amendment 1 @a414382a19: the two rows are ROUTED_ELSEWHERE; drained @487429cb60",
   "docs/contracts/investor-reporting/v1/routes.json: 21 routes, 19 DECLARED, 2 ROUTED_ELSEWHERE (the two reporting routes) (this compile's read, dell2 CLOUD df7865f720, 2026-10-07 ~08:1xZ-08:2xZ)",
   "pytest -q _contracts in infra/aws/lambda/investor-reporting: 190 passed; pytest -q _authz/tests/test_unguarded_census.py: 9 passed (this compile's read, dell2 CLOUD df7865f720, 2026-10-07 ~08:1xZ-08:2xZ)",
   "investigation row IRPT_DASHBD-S26: the disarm"
  ],
  "remedy": "Done: both routes are declared ROUTED_ELSEWHERE, the census and the seam suite pass.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v18",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v18"
  },
  "closed": true,
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~D2",
   "at": "2026-10-07T07:36:00Z"
  }
 },
 {
  "id": "IRPT_DASHBD-W9-S2",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "routes.json is the one carrier the api Terraform root reads; a DECLARED row whose handler is outside route_functions would break its next plan, and the reporting-read root already creates the same route_keys.",
  "evidence": [
   "investigation row IRPT_DASHBD-W9-S2",
   "infra/aws/terraform/investor-reporting/api/routes.tf:40-43 builds irpt_routes only from rows with status DECLARED (this compile's read, dell2 CLOUD df7865f720, 2026-10-07 ~08:1xZ-08:2xZ)",
   "docs/contracts/investor-reporting/v1/routes.json: 21 routes, 19 DECLARED, 2 ROUTED_ELSEWHERE (the two reporting routes) (this compile's read, dell2 CLOUD df7865f720, 2026-10-07 ~08:1xZ-08:2xZ)",
   "investigation row IRPT_DASHBD-S26: the disarm",
   "not run: a terraform plan of the api root"
  ],
  "remedy": "Done: the two rows are ROUTED_ELSEWHERE, which the api root does not build from.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v18",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v18"
  },
  "closed": true,
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~D2",
   "at": "2026-10-07T07:36:00Z"
  }
 },
 {
  "id": "IRPT_DASHBD-W9-S3",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "Two out-of-grant contract tests asserted no_handler_at_head == total - declared, which counts every non-DECLARED row as handler-less.",
  "evidence": [
   "investigation row IRPT_DASHBD-W9-S3",
   "DB-b-23 amendment 2 @bf68fca0ed",
   "pytest -q _contracts in infra/aws/lambda/investor-reporting: 190 passed; pytest -q _authz/tests/test_unguarded_census.py: 9 passed (this compile's read, dell2 CLOUD df7865f720, 2026-10-07 ~08:1xZ-08:2xZ)",
   "investigation row IRPT_DASHBD-S26: the disarm"
  ],
  "remedy": "Done: the _contracts suite passes with 19 DECLARED and 2 ROUTED_ELSEWHERE rows and no_handler_at_head 0.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v18",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v18"
  },
  "closed": true,
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~D2",
   "at": "2026-10-07T07:36:00Z"
  }
 },
 {
  "id": "IRPT_DASHBD-W12-S1",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The E2 tie-out grades 9,078 segments: 2,103 within 0.35 pp and 6,975 outside, 6,250 of them UNEXPLAINED by the closed reason set; 4,905 of those fall within tolerance once Black Diamond's own reported fees are netted, a class the set lacks. 3,395 segments carry BD's +1 day over 2025-01-09, the market closure.",
  "evidence": [
   "investigation row IRPT_DASHBD-W12-S1",
   "DB-b-26 drained @0685c40ec0 (DB17-1-AC1..AC3 PASS, re-run by the issuer); ledger irpt-dashbd-e3-bd-population-pull-20261004 CLOSED @fbc0ee59df (P1 5,252 of 5,252; G1 the tie-out)",
   "IRPT_BCKEND_ROUNDS_52_60_P_DRAIN_END_20261007.md: 'The fee question ... is put to 1.0.0_SA_CTO'"
  ],
  "remedy": "A ruling on the comparison basis: Opal's served 49F return is gross of fees and is compared to BD net of fees with fees added back, or a FEES reason joins the closed set. Then the 1,345 segments left unexplained after fees are the residue to read.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v18",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v18"
  },
  "closed": false
 }
]
```
