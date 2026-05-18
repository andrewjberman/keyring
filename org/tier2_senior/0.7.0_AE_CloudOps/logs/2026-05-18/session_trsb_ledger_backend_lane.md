# AE 0.7.0 Session Log — 2026-05-18 — TRSB_LEDGER backend lane

**Agent:** 0.7.0_AE_CloudOps
**Trigger:** COO~B sequence GO — TRSB_LEDGER backend serial lane (TO-0..TO-8)
**Project:** TRSB_LEDGER — Trade Submission executor-authorization + audit-trail hardening
**Status:** IN PROGRESS — TO-0 complete; TO-1 next (serial lane).

This log covers the TRSB_LEDGER backend lane. The concurrent RUNDATE-DISPATCH-IMPL +
INFGRO chain-coordination work is logged separately in `session_rundate_dispatch_impl.md`.

---

## TO-0 — Identity & Seeding Probe — COMPLETE

Read-only Phase-0 probe. Confirms/refutes the two assumptions Phase 1 locks against.
Brief: `docs/briefs/trsb-ledger-to0-identity-seeding-probe-20260518.md`.

### Findings

- **§3.4 / A5 (authorizer identity): YES, holds.** The `/api/general/trades/*` routes sit behind
  `portal-jwt-authorizer` (REQUEST authorizer, payload format 2.0, `enable_simple_responses=true`,
  backed by `opal-portal-authorizer` / `infra/aws/lambda/portal_authorizer/index.mjs`, Node.js).
  It RS256-verifies the JWT and returns `context:{email,name,tier,role,firmId,...}` — delivered to
  the backend Lambda at `event.requestContext.authorizer.lambda.email`. Empirically confirmed:
  authorizer log group live, last event 16:42Z, real `Token verified successfully` events.
  workflow_handler.py:100 confirmed reading `user_email` from the request BODY, never from the
  authorizer context. **§7-Q5 fork NOT triggered** — TO-2 proceeds to the standard repoint.
- **§3.1 (groups seeding): YES, holds.** `aws dynamodb scan trade-users` — 9 live rows, ALL with a
  populated `groups` list (values: `approvers`, `executors`; 4 approvers, 9 executors, 4 both, 0
  neither). No seeding/backfill needed before TO-1.
- **NEW high-severity finding:** `/api/public/trades/*` routes are `authorization_type=NONE` and
  hit the SAME integrations as the authenticated `/api/general/` twins — trade-workflow-handler is
  reachable unauthenticated. TO-2 must hard-reject requests lacking `requestContext.authorizer`,
  and/or the public routes get removed. Flagged in the brief §3 for COO~B routing — distinct from
  the (un-triggered) §7-Q5 fork.

### Acceptance criteria
- AC1 PASS — brief shipped at docs/briefs/trsb-ledger-to0-identity-seeding-probe-20260518.md.
- AC2 PASS — authorizer passes a usable acting-party identity (verified email); evidence in brief §1.
- AC3 PASS — 9 trade-users rows, all `groups`-populated, distribution reported (brief §4).
- AC4 N/A-by-result — §7-Q5 fork not triggered (authorizer DOES pass identity). Reported either way.
- AC5 PASS — no emoji; this session log; RAVC2 to 2.0.0_SA_COO~B.

### Compiler Tools
| Tool | Use | Result |
|------|-----|--------|
| comp-blast / comp-iam / comp-routes | trade-* Lambdas | Not modeled (PRD §5) — direct Terraform + source read is the TO-sanctioned substitute. |
| Direct read | apigateway.tf, apigateway-portal/{main,routes}.tf, portal_authorizer/index.mjs, workflow_handler.py, email_utils.py | Authorizer identified; body-trust of user_email confirmed at workflow_handler.py:100. |
| aws dynamodb scan trade-users | §3.1 census | 9 rows, all groups-populated (read-only). |
| aws logs (boto3) /aws/lambda/opal-portal-authorizer | authorizer liveness | Active; last event 16:42Z. |

Phase 3 compiler mandate: N/A — probe deliverable is a brief, no code commit, no AWS surface change.

## TO-1 — Group-auth enforcement — COMPLETE

`workflow_handler.py`: new `require_group()` helper; `handle_approve`/`handle_reject` require
`approvers`, `handle_execute` requires `executors` (groups list, PRD 3.1). `role` untouched (Q1);
dev gets no group bypass. Stale "No role restriction" comments removed. 10/10 unit tests pass
(`tests/test_group_auth.py`); ds-commit-gate clean. Commit 144c2e187.

Deploy mechanism — trade-workflow-handler was on `placeholder.zip` + `lifecycle ignore_changes`
(TF managed config only, not code). Andrew-directed: migrate it to the S3-backed pattern the
other 2 trade Lambdas already use. Migrated (commit 85773bf7f — `aws_s3_object` data source,
source-map `tf_file`/`artifact_s3_key`); build-and-upload + terraform apply (0 add, 1 change,
0 destroy; 0-diff; live CodeSha256 jCEKq9G6ez+... matches). trade-pipeline-v1.10.0.

Phase-3 deployed smoke (AC5): self-contained fixture — created a temp non-executor user
(groups=[]) + a temp APPROVED submission, invoked the DEPLOYED trade-workflow-handler with
action=execute -> HTTP 403 "User ... is not in the executors group and cannot execute trades";
the trade did NOT advance (status still APPROVED — the 403 returns before update_submission).
Both temp fixtures deleted. The group gate is confirmed wired + enforced in the deployed
runtime. AC1-6 all PASS.

## TO-010a — Remove unauthenticated workflow route — COMPLETE (P0 EXPEDITE)

CTO~B ruled on the TO-0 §3 finding: the unauthenticated `POST /api/public/trades/workflow`
route is indefensible — removed expedited, ahead of the serial queue.

- Removed route `r_5qmxcef` from `shared-infra/apigateway-portal/routes.tf`; shared integration
  `i_xkuchu9` retained (the authenticated `/api/general/trades/workflow` route depends on it).
- terraform plan: `0 add, 0 change, 1 destroy` (only r_5qmxcef); apply clean; 0-diff verified.
  Commit bab59c8d8; shared-infra-v1.12.0.
- Smoke: `POST /api/public/trades/workflow` -> HTTP 401 (route gone — request now falls through
  to `$default`, which is CUSTOM-authorizer-protected (authorizer naqxlm), verified via
  get-routes; it no longer reaches trade-workflow-handler unauthenticated — pre-010a it would
  have hit the handler and returned a 400-class handler response). `POST /api/general/trades/
  workflow` -> HTTP 401, route intact (CUSTOM auth). get-routes confirms the public workflow
  route is absent and 73 routes remain. Exposure closed.
- Note: AC3 expected 404; actual is 401 because `$default` (authorizer-protected) catches the
  path — a safe catch, arguably stronger than 404. Reported in the RAVC2.

## TO-2 — Actor-identity binding — COMPLETE

§7-Q5 fork did NOT trigger (TO-0 confirmed the authorizer passes a verified
`email`). Standard repoint executed. `workflow_handler.py` `lambda_handler`: the acting
party is now derived from `event.requestContext.authorizer.lambda.email` (the verified JWT
principal), never the body. AC2b — a request with NO authorizer context is hard-rejected 403
(the structural catch for the unauthenticated `/api/public/trades/*` twin; no body fallback).
AC2 — a body `user_email` conflicting with the JWT principal -> 403 mismatch; matching/absent
accepted. Commit 7d02fb663. 6/6 unit tests (`tests/test_actor_identity.py`); TO-1 tests still
10/10. Deployed S3-backed via terraform apply (0 add, 1 change, 0 destroy; 0-diff; live
CodeSha256 G55O991ZA74u... matches); trade-pipeline-v1.11.0.

Phase-3 deployed smoke (AC4) — synthetic-event invokes of the deployed Lambda: jwt!=body ->
403 "Acting-party identity mismatch"; no-authorizer-context -> 403 "no verified acting-party
identity"; JWT-resolved actor (no body email) -> passes identity, 404 on a fake submission.
ALL PASS. AC1-4/6 PASS; AC5 N/A (fork not triggered).

## Current State

| Item | Status |
|------|--------|
| TRSB_LEDGER TO-0 | COMPLETE — brief shipped; RAVC2 accepted by COO~B |
| TRSB_LEDGER TO-010a | COMPLETE — unauth route removed, shared-infra-v1.12.0; RAVC2 to COO~B + CC CTO~B |
| TRSB_LEDGER TO-1 | COMPLETE — trade-pipeline-v1.10.0; AC1-6 PASS, deployed smoke 403; RAVC2 to COO~B |
| TRSB_LEDGER TO-2 | COMPLETE — trade-pipeline-v1.11.0; AC1-4/6 PASS, deployed smoke ALL PASS; RAVC2 to COO~B |
| TRSB_LEDGER TO-3..TO-5/TO-8 | PENDING — serial lane, TO-3 next |
| opal-data-mdpf bucket (DS~B request) | PENDING — shared-infra TF add, slotted after TO-2 startup |
| TRSB_LEDGER TO-9 | STAGED — droppable stretch, do NOT start |
| TRSB_LEDGER TO-10 | STAGED — gated on Andrew legacy-form supersession confirm; do NOT start |

## Next Steps

1. TO-1 — group-auth enforcement (next in the serial lane).
2. TO-5 dynamodb.tf: AE 0.5.0's TO-6 lands first (durability attrs); rebase the by-approver GSI
   stanza on top. Coordination open with 0.5.0.
3. COO~B routing decision owed on the `/api/public/trades/*` NONE-auth bypass (brief §3).
