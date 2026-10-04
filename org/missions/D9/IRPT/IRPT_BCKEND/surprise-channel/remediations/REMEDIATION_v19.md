# IRPT_BCKEND -- project sweep 8 remediations

<sweep_watermark>2026-10-04T03:05Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-10-04 (DRAFT). Graduated at sweep 8's L9 (ADJUDICATION_v23.md), round label v47 (the round after IRPT_BCKEND round 46). 7 rows: 6 REMEDIATED and closed on a served or committed read (S307, S310, S311, S316, W114-S1, W115-S1); 1 OPEN (S318). 4 ARMED rows arrive DISARMED: S307, S310 and S311 by 2.0.0_SA_COO~P's rows S309, S313 and S314, and S316 by 2.0.0_SA_COO~Y's Y-5 V1 READY run @1afe081ac4, which CTO batch 237 item 2 records as the cure (no disarm row was filed for it). 1 stays ARMED with no disarm: S318 (a READY corrected-upload analysis reads Unavailable on the page). S308 (ARMED) is dismissed into S310 at C-S285.

Clocks advanced in place at this compile (state fields only):
- S288 (REMEDIATION_v18): disarm DISARMED at 2026-10-03T22:45:00Z, by row S315 (2.0.0_SA_COO~Y), which measures the row's
  own disarm condition (fence 25; securities_info answered at 20:55:33Z and 22:28:06Z); S306 (16:36Z) is the first record.
  remediation REMEDIATED and closed: the session was re-captured from Andrew's HAR without option A (ledger
  irpt-signin-har-20261003 CLOSED 4/4), and Y-3 (17:03:14Z) and Y-5 V1 (02:28:20Z) reached READY on it.
S284 (REMEDIATION_v18) is not moved: its named proof, Y-5 V1, read READY at 02:28:20Z, but its disarm owner
(2.0.0_SA_COO~Y) has filed no disarm row. It is read at the next compile.

Seen at this compile's read and not filed here (this draft writes no row): the source map's deploy record for
irpt-ycharts-generate reads deployed_code_sha256 FgZcBjJu.. (last_deployed_at 2026-10-04T00:27:55Z), while live is
uFTONal.. since 2026-10-04T01:57:24Z (irpt-y5d D1). CTO batch 234's class remedy (the close leg records the moved function
with --function) did not run on that ledger. It needs its own row; owner 2.0.0_SA_COO~Y.

Clock advanced in place at this compile (state fields only): S288 (REMEDIATION_v18) -- disarm DISARMED at 2026-10-03T22:45:00Z by its disarm owner 2.0.0_SA_COO~Y (row S315, measured on the row's own condition: fence 25 and an authenticated securities_info read answering 200); remediation REMEDIATED, closed.

```json
[
  {
    "id": "IRPT_BCKEND-S307",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "opal-portal-authorizer (V2) held no reporting-series entry in RENDER_ROUTE_CLAIMS, so a 49F PATH B export's render-delegate series read was denied 403 after the edge (V3) admitted it, and every 49F export refused DEPENDENCY_UNAVAILABLE once PATH A was retired (B3, 18:44:32Z).",
    "evidence": [
      "investigation row IRPT_BCKEND-S307",
      "investigation row IRPT_BCKEND-S309 (2.0.0_SA_COO~P, 20:20Z): the disarm; CTO RULINGS batch 226 (fix forward, no rollback), batch 227 (the authorizer half SIGNED) and batch 228 item 1 (S307 DISARMED)",
      "IB-pr-307 drained @79db37c149; ledger irpt-authorizer-series-render-20261003 CLOSED, all 6 legs proven (org/critical_paths/change_management/20261003T1946Z_irpt-authorizer-series-render-20261003_deploy_completion.md)",
      "lambda get-function-configuration opal-portal-authorizer: CodeSha256 gQp2IooA.., LastModified 2026-10-03T19:52:32Z (this compile's read, 2026-10-04 ~20:0xZ-20:3xZ)",
      "infra/aws/users/lambda/portal-authorizer/index.mjs:56-66 at CLOUD HEAD 96f17cdbe9: the series route entry {param account_id, claim accountSetId, require which == series}; node --test tests/test_render_reporting_series.mjs: 9 pass, 0 fail (this compile's read, 2026-10-04 ~20:0xZ-20:3xZ)"
    ],
    "remedy": "Done and served: IB-pr-307 admits the render-delegate token on the 49F reporting series route only, pinned to the token's own account; a foreign-account token is refused 403 and the human path is byte-unchanged.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v47",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P",
      "round": "v47"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~P",
      "at": "2026-10-03T20:20:00Z"
    }
  },
  {
    "id": "IRPT_BCKEND-S310",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "The export render host's allow-list, render_export.cjs:83 PRINT_QUERY_KEYS, copied only bundle, tenant, revision, kind, selection, start and end, so a PATH B print lost account and version before navigation and the PROD print refused it; no 49F export reached READY (S308's re-point, CTO batch 229).",
    "evidence": [
      "investigation row IRPT_BCKEND-S310",
      "investigation row IRPT_BCKEND-S313 (2.0.0_SA_COO~P, 22:30Z): the disarm; CTO RULINGS batch 229 (the re-point) and batch 230 items 1-2 (the render-host half SIGNED; R1 READY disarms)",
      "IB-pr-308 drained @fb310203e5; ledger irpt-render-host-print-query-20261003 CLOSED, all 4 legs proven",
      "s3api head-object and get-object opal-313476888478-lambda-artifacts ec2/investor-reporting-export/render_export.cjs: current VersionId lLkKsNvY.., 16,434 B, sha256 9684b4b9.., byte-equal to the blob at CLOUD HEAD 96f17cdbe9, whose PRINT_QUERY_KEYS adds account, version and request (this compile's read, 2026-10-04 ~20:0xZ-20:3xZ)",
      "s3 get-object opal-data-ycharts firms/49financial/generations/EXP-e29b5415a06f90f943481c41a1a4821b/receipt.json: job_state READY, facts.frozen_as_of 2026-10-01, page_count 11, validation_status PASSED, LastModified 2026-10-03T22:13:15Z (this compile's read, 2026-10-04 ~20:0xZ-20:3xZ)"
    ],
    "remedy": "Done and served: the host forwards account, version and request, and the 22:13Z PROD export of ****0090 rendered to a READY receipt that names the frozen as_of.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v47",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P",
      "round": "v47"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~P",
      "at": "2026-10-03T22:30:00Z"
    }
  },
  {
    "id": "IRPT_BCKEND-S311",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "With the host forwarding account and version, the render's page read PATH B through readDashboard, which fetches the manifest as well as the series; render tokens are admitted on the series only (IB-pr-304), so the edge refused the manifest and resolveBundle refused 'selection is required'.",
    "evidence": [
      "investigation row IRPT_BCKEND-S311",
      "investigation row IRPT_BCKEND-S314 (2.0.0_SA_COO~P, 22:30Z): the disarm; CTO RULINGS batch 231 ruling (a), batch 232 (the promote's other riders) and batch 233 item 1 (Andrew's word on the promote of DEV dddaf3a1)",
      "portal git ls-remote origin: PROD dbd29c6320; 1f42eb08 ('a frozen export print reads the series alone') is an ancestor of it, and so is the positive control 98a98e70fb (this compile's read, 2026-10-04 ~20:0xZ-20:3xZ)",
      "s3 get-object opal-data-ycharts firms/49financial/generations/EXP-e29b5415a06f90f943481c41a1a4821b/receipt.json: job_state READY, facts.frozen_as_of 2026-10-01, page_count 11, validation_status PASSED, LastModified 2026-10-03T22:13:15Z (this compile's read, 2026-10-04 ~20:0xZ-20:3xZ)",
      "render 123e754c Success, 20 requests, 0 foreign; 2.0.0_SA_COO~D msg 104799: READY at 22:13:41Z on the page (S314's grounding)"
    ],
    "remedy": "Done and on PROD: under a render (a print carrying a frozen version) the page reads the series alone and never requests the manifest; IB-pr-304's series-only token rule stands unwidened at V2 and V3.",
    "owner": "2.0.0_SA_COO~D",
    "round": "v47",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~D",
      "round": "v47"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~P",
      "at": "2026-10-03T22:30:00Z"
    }
  },
  {
    "id": "IRPT_BCKEND-S316",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "Y-5 V1's holdings upload POST answered 200 and recipe.step_upload's exact Decimal reconciliation refused the vendor's echo: amounts in the easy file carried 12-15 decimal places (float noise) and the echo rounds them, so the job went ATTENTION VENDOR_UPLOAD_REFUSED with no counts journaled (the cause measured by the Y5C run, CTO batch 236).",
    "evidence": [
      "investigation row IRPT_BCKEND-S316",
      "CTO RULINGS batch 235 item 1 (Y5C half: dollars sent and reconciled at cents, half up; a counts-only refusal line), batch 236 item 1 (Y5D half: 'The Y5C run measured S316's cause as float noise'; the binding uses the same cents rule, and its refusal is the named ATTENTION VENDOR_UPLOAD_BINDING_REFUSED) and batch 237 item 2 ('S316 is measured end to end ... cents in the upload and its binding cured it')",
      "deploys 3ce7808103 (Y5C: irpt-ycharts-generate FgZcBjJu.., resident 136ee09e9f-st20) and 26aaeef8ea (Y5D: uFTONal.., resident 3f29017cfc-st21); ledgers irpt-y5c-20261003, irpt-y5d-20261004 and irpt-y5v-20261003 CLOSED, all 5 legs proven each",
      "infra/aws/lambda/investor-reporting/ycharts/generate/recipe.py:473 (cents, ROUND_HALF_UP) and resident_worker.py:100 (VENDOR_UPLOAD_BINDING_REFUSED) at CLOUD HEAD 96f17cdbe9; lambda get-function-configuration irpt-ycharts-generate: CodeSha256 uFTONal.., LastModified 2026-10-04T01:57:24Z (this compile's read, 2026-10-04 ~20:0xZ-20:3xZ)",
      "2.0.0_SA_COO~Y @1afe081ac4 (2026-10-04T02:30:33Z): Y-5 V1 READY at 02:28:20Z (REQ-a618aa83, RPT-ffe600359a7b), ledgers irpt-y5, irpt-y5v, irpt-y5c and irpt-y5d CLOSED; dynamodb get-item irpt-jobs (tenant cottonwood) REQ-a618aa83407689bc95193a01: state READY (this compile's read, 2026-10-04 ~20:0xZ-20:3xZ). The disarm owner filed no disarm row; the clock rests on its run commit and CTO batch 237 item 2"
    ],
    "remedy": "Done and served: holdings dollars are sent, reconciled and bound at cents (half up), a refused echo journals its closed counts, and Y-5 V1 reached READY on the served build.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v47",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v47"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": "2026-10-04T02:30:33Z"
    }
  },
  {
    "id": "IRPT_BCKEND-S318",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "A READY analysis whose upload carried a user correction (Y-5: TIMXX named SGOV) reads 'Unavailable -- analysis status date basis unavailable' on the page: ops/owned_status.py maps READY to UNAVAILABLE when prospect dates do not derive, and the undated-input proof most likely fails because the corrected rows no longer match the raw file (inferred by the filer, not measured).",
    "evidence": [
      "investigation row IRPT_BCKEND-S318",
      "infra/aws/lambda/investor-reporting/ops/owned_status.py:24 at CLOUD HEAD 96f17cdbe9: READY -> (UNAVAILABLE, ANALYSIS_STATUS_DATE_BASIS_UNAVAILABLE) unless derive() returns dates (:57-58); git log of ops/owned_status.py and ops/prospect_dates.py: last commit 4c23ef5d98 (2026-10-02), none since the row (this compile's read, 2026-10-04 ~20:0xZ-20:3xZ)",
      "dynamodb get-item irpt-jobs (tenant cottonwood) REQ-a618aa83407689bc95193a01: state READY (this compile's read, 2026-10-04 ~20:0xZ-20:3xZ); the job and its report are unaffected, and the page's words are the only effect",
      "2.0.0_SA_COO~D msg 104892 (read-only walk tmp/ui-walk/20261004T023652Z) and drive log e95d732753: READY-read-as-Unavailable routed to 2.0.0_SA_COO~Y"
    ],
    "remedy": "Measure the failing branch by running prospect_dates.input() offline on REQ-a618aa83's retained input, then extend the undated-input proof to map a corrected row back through its disclosed from_value, and serve it under its own never-widen half. Disarm: the page's status read of a READY corrected-upload analysis (REQ-a618aa83, or Y-4's typo run) answering READY with its date basis.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v47",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v47"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-W114-S1",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "safe-commit's naming limb (ENFORCE) refused IB-pr-311's source-map edit: the live names irpt-49f-holdings-performance-role and the Inflection row's strings read as new hand-kept firm-token carriers, so the 49F iam_role correction and the irpt-inf-holdings-performance-lambda row could not land and IB45-1-AC1 failed.",
    "evidence": [
      "investigation row IRPT_BCKEND-W114-S1",
      "this seat's rulings 7b38f056ca (a source-map resource-name literal passes iff lib/opal_naming.py name() reproduces it) and ce84132d29 (a tf_resource cites a declared Terraform address); implemented by 1.0.0_SA_CTO @1c3fc41a4d and @7de9db9085, graded as matching (c0293187f9)",
      "IB-pr-312 drained @d37e19e3ba; IRPT_BCKEND_ROUND_46_P_DRAIN_END_20261004.md: 'W114-S1 | BLOCKING, INERT | resolved by this order'; the edit commit bb620b6df5 read NAMING-GATE: PASS 0 graded",
      "infra/aws/lambda/ci/lambda-source-map.json at CLOUD HEAD 96f17cdbe9: irpt-holdings-performance-lambda iam_role irpt-49f-holdings-performance-role; irpt-inf-holdings-performance-lambda row with iam_role irpt-inf-holdings-performance-role and deployed_code_sha256 0PuFBxdJ..; lambda get-function-configuration of both functions: CodeSha256 0PuFBxdJ.. and those two roles (this compile's read, 2026-10-04 ~20:0xZ-20:3xZ)"
    ],
    "remedy": "Done: the naming limb admits a builder-reproduced name cited in the source map, and IB-pr-312 committed the 49F role correction and the Inflection row, both equal to live.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v47",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P",
      "round": "v47"
    },
    "closed": true
  },
  {
    "id": "IRPT_BCKEND-W115-S1",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "The naming limb refused the deploy recorder's CHANGELOG.json entry for irpt-inf-holdings-performance-lambda (the function name read as a new 'inf' carrier, and the source-map carve-out did not reach CHANGELOG files), so only the source-map half of that deploy record was committed.",
    "evidence": [
      "investigation row IRPT_BCKEND-W115-S1",
      "investigation row IRPT_BCKEND-S319 (2.0.0_SA_COO~P, 03:05Z): the entry committed @236f660bb6 with the naming limb PASS 0 graded",
      "this seat's second follow-on ruling in org/tier1_exec/3.0.0_SA_CVO/deliverables/CVO_RULING_NAMING_LIMB_SOURCE_MAP_CITATION_NOT_MINT_20261004.md (8d9ca4d27e): a builder-reproduced function name is admitted in a recorder CHANGELOG's function-name fields only; implemented by 1.0.0_SA_CTO @df94193739, graded as matching (67a969202d)",
      "infra/aws/terraform/investor-reporting/CHANGELOG.json at CLOUD HEAD 96f17cdbe9: entry untagged-bb620b6d with functions_updated ['irpt-inf-holdings-performance-lambda'] (this compile's read, 2026-10-04 ~20:0xZ-20:3xZ)"
    ],
    "remedy": "Done: the recorder's CHANGELOG entry for the Inflection function is committed under the narrow carve-out, so both halves of that deploy record are on CLOUD.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v47",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P",
      "round": "v47"
    },
    "closed": true
  }
]
```
