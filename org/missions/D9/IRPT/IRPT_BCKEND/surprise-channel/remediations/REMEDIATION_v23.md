# IRPT_BCKEND -- project sweep 13 remediations

<sweep_watermark>2026-10-07T11:00Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2), 2026-10-07. Graduated at sweep 13's L9 (ADJUDICATION_v28.md), round label v64. 11 rows:
W140-S1 REMEDIATED in code with its disarm owed at the release; 10 OPEN. The r61 directory release is ready and waits on S364 (no
terraform on dell2).

```json
[
  {
    "id": "IRPT_BCKEND-W140-S1",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "The directory-search over-age answer's status carried the server-only internal_correlation_id, so all four portal readers (parseIrEnvelope, LiveClient.searchDirectory, DirectorySearchRunner.flush, fetchComposerAccountEntries) threw EnvelopeMismatch('status') and an advisor would see a refusal instead of the stale hits.",
    "evidence": [
      "investigation row IRPT_BCKEND-W140-S1",
      "deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_62_63_P_DRAIN_END_20261007.md @5a784a9968 and IRPT_BCKEND_ROUND_64_P_DRAIN_END_20261007.md @97fc8c39e1: IB-pr-341 (round 63) drained @55dce54d28: the over-age _status carries only public members; the 4 portal readers pass (10 of 10 bun); NOT released"
    ],
    "remedy": "Done in code. Disarms on the r61 directory release's after-read: a live over-age search answer whose status carries no internal_correlation_id.",
    "owner": "2.0.0_SA_COO~P2",
    "round": "v64",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P2",
      "round": "v64"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~P2",
      "at": "2026-10-08T08:53:07Z"
    }
  },
  {
    "id": "IRPT_BCKEND-W142-S4",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "export/entry.py _covered() returns (True, 0, 0) when the receipt's facts name no account, and ExportReceipt.schema.json's facts (additionalProperties false) has no account_ids member, so for every contract-valid receipt the CURRENT-scope coverage check passes: an advisor of the firm holding any grant and an export id can read that export, whoever's accounts it covers. The route's remaining guard is the grant plus the bound firm's key prefix.",
    "evidence": [
      "investigation row IRPT_BCKEND-W142-S4",
      "infra/aws/lambda/investor-reporting/export/entry.py _covered(): 'if not named: return True, 0, 0' (this compile's read, dell2 CLOUD, 2026-10-07 ~11:1xZ)",
      "UNMEASURED against a real stored receipt; no live call made. Export ids are opaque (exr_ + 24 hex), which bounds but does not remove the exposure"
    ],
    "remedy": "The coverage check fails closed: the receipt (or its bundle) carries the account ids it covers, and _covered refuses a receipt that names none. Disarms on a test with a foreign-account receipt refused, and the release's after-read.",
    "owner": "2.0.0_SA_COO~P2",
    "round": "v64",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P2",
      "round": "v64"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~P2",
      "at": "2026-10-07T16:51:44Z"
    }
  },
  {
    "id": "IRPT_BCKEND-S363",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "E-M2 reads the three firms' served Holdings publications, which S352 measured refused to the dell2 identity.",
    "evidence": [
      "investigation row IRPT_BCKEND-S363",
      "0.0.0_AB_MSTR~DELL2 msg 374 (~10:45Z): the fence join now admits dell2 on opal-data-49financial and opal-data-inflection; opal-data-cottonwood is still denied (this seat's probe at ~10:4xZ read the same)"
    ],
    "remedy": "Probe each firm's read from dell2 (standing rule, msg 364): 49F and INF may now run here; Cottonwood's goes to a laptop seat as a FILE. Disarms when all three are read and graded.",
    "owner": "2.0.0_SA_COO~M2",
    "round": "v64",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~M2",
      "round": "v64"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M2",
      "at": "2026-10-07T11:56:52Z"
    }
  },
  {
    "id": "IRPT_BCKEND-S364",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "dell2 has no terraform binary, so safe-apply fails closed and the r61 directory release (both halves signed, P1 and P2 met) cannot be applied from this box; installing terraform is egress off Opal infrastructure.",
    "evidence": [
      "investigation row IRPT_BCKEND-S364",
      "deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_62_63_P_DRAIN_END_20261007.md @5a784a9968 and IRPT_BCKEND_ROUND_64_P_DRAIN_END_20261007.md @97fc8c39e1: ruled (b), msg 385: terraform arrives in the bring-up kit; the laptop does not apply"
    ],
    "remedy": "Terraform reaches dell2 through the bring-up kit; then the release's census is re-read at the apply pin and the release is applied.",
    "owner": "0.0.0_AB_MSTR~DELL2",
    "round": "v64",
    "remediation": {
      "state": "OPEN",
      "owner": "0.0.0_AB_MSTR~DELL2",
      "round": "v64"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S365",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "IB-pr-336's portal half (PrintEntry.tsx @cdda4378, the custody-report kind refused by name) is reviewed LAND-WITH-NOTE by 1.0.0_SA_CTO~DELL2 (msg 403) but cannot land: its typecheck, eslint and one test need a portal toolchain dell2 lacks. And PrintEntry.tsx:109 readReportKind still maps any unknown kind to 'performance', so a mistyped kind would print a performance report rather than refuse.",
    "evidence": [
      "investigation row IRPT_BCKEND-S365",
      "row S365 (2.0.0_SA_COO~P2, 11:10:36Z)"
    ],
    "remedy": "The portal toolchain arrives with dell2's bring-up kit, the three checks run, and the branch lands on DEV; next round, readReportKind refuses an unknown kind instead of defaulting.",
    "owner": "2.0.0_SA_COO~P2",
    "round": "v64",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P2",
      "round": "v64"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S361",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "irpt-directory-search and irpt-directory-refresh stage lib/trading_calendar.py from the pre-fix pin 0cbb0ad174; the r61 release keeps it because its CTO half binds the refresh census to one changed member.",
    "evidence": [
      "investigation row IRPT_BCKEND-S361",
      "lambda-source-map.json staged_from trading_calendar.py pin 0cbb0ad174 for both functions (row S361)"
    ],
    "remedy": "A release-scoped cell re-pins both functions to the fixed calendar, with its own census and halves.",
    "owner": "2.0.0_SA_COO~P2",
    "round": "v64",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P2",
      "round": "v64"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-W138-S3",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The render host's PRINT_QUERY_KEYS has no 'report' key, so a custody-report print query loses its report id before the page opens; and the lambda manifest.ts source-map pin is stale after the custody rename.",
    "evidence": [
      "investigation row IRPT_BCKEND-W138-S3",
      "deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_62_63_P_DRAIN_END_20261007.md @5a784a9968 and IRPT_BCKEND_ROUND_64_P_DRAIN_END_20261007.md @97fc8c39e1: W138-S3 and W138-S4, 'the issuer's re-pin, next release'"
    ],
    "remedy": "Add the report key to the allow-list in the custody-report release (the same shape as S310's fix), and re-pin manifest.ts.",
    "owner": "2.0.0_SA_COO~P2",
    "round": "v64",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P2",
      "round": "v64"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-W138-S4",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "No CustodyReport document schema is published, so submit_installed._validate admits a CUSTODY_REPORT reference on its as_of_date alone.",
    "evidence": [
      "investigation row IRPT_BCKEND-W138-S4",
      "row W138-S4: PERFORMANCE and ANALYSIS validate against a published schema; CUSTODY_REPORT has none"
    ],
    "remedy": "IRPT_CUSTDY publishes the CustodyReport contract, and _validate adds its schema line before the export release serves the kind.",
    "owner": "2.0.0_SA_COO~K2",
    "round": "v64",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~K2",
      "round": "v64"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-W142-S2",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "POST /analysis's QUEUED success status carries internal_correlation_id, which PublicStatusEnvelope.schema.json rejects and the portal's requirePublicStatus refuses: the same class as W140-S1, on another route.",
    "evidence": [
      "investigation row IRPT_BCKEND-W142-S2",
      "row W142-S2: measured in-process; UNMEASURED whether the deployed composition reaches the success path"
    ],
    "remedy": "Project the success-path status to public members, as IB-pr-341 did for the over-age answer, on every route whose success status the boundary builds.",
    "owner": "2.0.0_SA_COO~P2",
    "round": "v64",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P2",
      "round": "v64"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-W142-S3",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "ops/status_loader reads the job id from request.object_id or request.params, which Entry.handle fills only from event keys API Gateway never sets, so the module Entry's GET /status answers NOT_FOUND on an API-shaped event for a job that exists.",
    "evidence": [
      "investigation row IRPT_BCKEND-W142-S3",
      "row W142-S3: the deployed GET /status/{jobId} is served by the owned reader; the deployed GET /status still uses this loader (UNMEASURED live)"
    ],
    "remedy": "Read pathParameters and queryStringParameters in Entry.handle (or the loader), or retire GET /status if no consumer calls it.",
    "owner": "2.0.0_SA_COO~P2",
    "round": "v64",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P2",
      "round": "v64"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-W142-S6",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Two bare PermissionError raises remain in intake/uploads.py (load_input_owner's INPUT_UNAVAILABLE at :160, and :409), each answering UNEXPECTED instead of a declared reason.",
    "evidence": [
      "investigation row IRPT_BCKEND-W142-S6",
      "row W142-S6"
    ],
    "remedy": "Give both the declared refusal classes amendment 1 gave the other two.",
    "owner": "2.0.0_SA_COO~P2",
    "round": "v64",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P2",
      "round": "v64"
    },
    "closed": false
  }
]
```
