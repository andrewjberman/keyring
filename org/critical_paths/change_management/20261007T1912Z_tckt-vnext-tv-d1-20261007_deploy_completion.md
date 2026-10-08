# Deploy Completion Record
**Date opened:** 2026-10-07T19:12:08.854784+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261007T194302Z
**Deploy:** TCKT_VNEXT TV-d-1: opal-ticket-api code y0UF... + ROUTING_MATRIX analysis_request + POST /api/scoped/tickets/{ticketId}/report. SCOPE: the live Ticket Center for every portal (PROD; Environment=Production, shared portal API 7k3ed8px20), not DEV. Halves: COO @41443247bb, CTO @b9b072decd. Before-read: opal-tickets Count 12, 7 ticket routes.
**Authored by:** 2.0.0_SA_COO~V2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | opal-313476888478-lambda-artifacts ticket-center/opal-ticket-api.zip | upload sha256 y0UF... + head-object | build-and-upload.sh ticket-center opal-ticket-api at HEAD (source = da43155418, git diff empty): SHA256 y0UFtRIfZxu3x6BCFSGLjXsNgScCl/GPuWNHbmZV7BI=, s3://opal-313476888478-lambda-artifacts/ticket-center/opal-ticket-api.zip write VERIFIED size=24726 sha256 metadata match | CLOSED 20261007T191852Z |
| L2 | activation | safe-apply ticket-center | re-plan 1/1/0 + rc=0 | safe-apply rc=0 on saved plan tckt-d1.tfplan read 1/1/0 (route report added; opal-ticket-api source_code_hash /38K...->y0UF..., ROUTING_MATRIX +analysis_request); Apply complete 1 added 1 changed 0 destroyed; route id qv4t6vr; 2026-10-07T19:21Z | CLOSED 20261007T193411Z |
| L3 | verify | get-function-configuration + get-routes | CodeSha256 y0UF... and 8 ticket routes incl report | get-function-configuration opal-ticket-api from dell2: CodeSha256 y0UFtRIfZxu3x6BCFSGLjXsNgScCl/GPuWNHbmZV7BI=, LastModified 2026-10-07T19:21:15Z, Successful, ROUTING_MATRIX carries analysis_request; get-routes api 7k3ed8px20: 8 /api/scoped/tickets routes (7 before) incl POST .../{ticketId}/report | CLOSED 20261007T193412Z |
| L4 | verify | CTO condition 2a/2b/2c | opal-tickets Count 12 unchanged; client claim 403; existing-type create field set unchanged | 2a: dynamodb scan opal-tickets Select COUNT = 12 before and 12 after (twice). 2b: direct invoke of the deployed function, client principal (firm inflection) POST .../TCK-20990101-deadbeef/claim -> 403 'CLAIM is not permitted to principal class client-human'; client POST .../report -> 403; internal control same id -> 404 not found (no writes). 2c: old source 481dde1dbf vs deployed zip bytes (S3 object sha256 y0UF...) run locally on one in-memory table, notifier stubbed: CREATE and SUBMIT for all 4 existing types -> 8 of 8 identical (status + stored field set); negative control planting one field -> 0 of 8, FAIL as expected. No PROD create was made, so no ticket and no DL email | CLOSED 20261007T193413Z |
| L5 | verify | terraform plan | No changes (0-diff) | terraform plan -detailed-exitcode infra/aws/terraform/ticket-center from dell2 after apply: No changes, exit 0 | CLOSED 20261007T193415Z |
| L6 | verify | CTO condition 3 | notification record: no test ticket created at deploy; TV-r-1 names who is notified | CTO condition 3: no test ticket was created during the deploy, so nobody was notified; the first test ticket is TV-r-1's, titled with a [TEST TCKT_VNEXT] marker, and its ledger names Manav and Alyssa (ROUTING_MATRIX primaries) plus the DL as notified | CLOSED 20261007T193415Z |

## Log

- 20261007T191208Z OPENED by 2.0.0_SA_COO~V2 with 6 leg(s)
- 20261007T191852Z LEG L1 closed: build-and-upload.sh ticket-center opal-ticket-api at HEAD (source = da43155418, git diff empty): SHA256 y0UFtRIfZxu3x6BC
- 20261007T193411Z LEG L2 closed: safe-apply rc=0 on saved plan tckt-d1.tfplan read 1/1/0 (route report added; opal-ticket-api source_code_hash /38K...->y
- 20261007T193412Z LEG L3 closed: get-function-configuration opal-ticket-api from dell2: CodeSha256 y0UFtRIfZxu3x6BCFSGLjXsNgScCl/GPuWNHbmZV7BI=, LastModi
- 20261007T193413Z LEG L4 closed: 2a: dynamodb scan opal-tickets Select COUNT = 12 before and 12 after (twice). 2b: direct invoke of the deployed function
- 20261007T193415Z LEG L5 closed: terraform plan -detailed-exitcode infra/aws/terraform/ticket-center from dell2 after apply: No changes, exit 0
- 20261007T193415Z LEG L6 closed: CTO condition 3: no test ticket was created during the deploy, so nobody was notified; the first test ticket is TV-r-1's
- 20261007T194302Z CLOSED -- all 6 legs proven
