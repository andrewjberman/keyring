# Deploy-completion ledger — TCKT_CENTER P0 initial (ticket-center-v1.0.0)

**Opened:** 2026-07-14T19:58Z by 0.5.0_AE_OpalETL~A (Andrew-direct execution delegation)
**Status:** CLOSED 2026-07-14T20:0xZ — all 6 legs, evidence inline
**Scope:** NEW stack, pure-add: DynamoDB `opal-tickets` + role `opal-ticket-api-role` + Lambda
`opal-ticket-api` + integration + 6 routes on the shared portal API (7k3ed8px20) + lambda
permission. Source commit `08c2e6dfa`. NO existing resource modified. CF behavior EXCLUDED
(portal-auth shared module — surfaced to CTO, not part of this deploy).

## Legs

1. [x] artifact built + uploaded + head-object verified: `ticket-center/opal-ticket-api.zip`
       Size 3838, ETag 58abdae0af39c2acc3a5550c7cb0ed2a, metadata content-sha256
       `iHir0reiVPg5vKgk0WI6N2xZGA2SBQSJp9D3eJLzRvc=` == local sha (the yang-lambda
       source_code_hash contract — first upload missed it, plan errored, script fixed).
2. [x] terraform plan: **14 to add, 0 to change, 0 to destroy** — pure add, new-territory shape.
3. [x] safe-apply (HALTGT checkpoint passed; first attempt BLOCKED fail-closed by comp-tagauthz
       because a session-exported MSYS_NO_PATHCONV=1 mangled the gate's own launch path —
       env-scoped lesson, re-ran clean): **Apply complete 14/0/0**, then 0-diff re-plan:
       **"No changes. Your infrastructure matches the configuration."**
4. [x] 22a battery on the LIVE role (one --resource-arns per call):
       PutItem/GetItem/UpdateItem/Scan on table ARN + Query on index ARN = **5/5 allowed**;
       POSITIVE control (isolated): logs:CreateLogStream on own log group = allowed;
       NEGATIVE controls (isolated): PutItem on foreign table opal-data-refresh-executions =
       **implicitDeny**, DeleteTable on own table = **implicitDeny** (discriminates on BOTH
       the resource axis and the action axis).
5. [x] end-to-end exercise (direct invoke, apigwv2 payloads, authorizer context stamped):
       create 201 `TCK-20260714-20acba39` (routing matrix applied: service_request ->
       manav+alyssa primary) -> claim 200 (in_progress, assignee stamped) -> DOUBLE-CLAIM 409
       loud ("claim races lose loudly", current holder returned) -> complete 200 (events
       [created, claimed, completed]) -> get 200 -> list?status=completed 200 -> metrics 200
       (avg_claim_secs/avg_complete_secs derived per assignee + type, reconciles to the trail).
       Stray shell-run ticket TCK-20260714-3ec7e490 claimed+completed (board clean).
6. [x] tag `ticket-center-v1.0.0` + push --follow-tags (see git).

## Residual (deliberately out of this deploy)
- CloudFront `/api/scoped/tickets/*` behavior: portal-auth shared module (ordered behavior
  list) — exact diff surfaced to 1.0.0_SA_CTO per his collision channel. Until it lands, the
  API is live + authorizer-gated at the API Gateway; the portal page ships behind it.
- P1 sweeps/notifications + P2 intake per the registered phasing.
