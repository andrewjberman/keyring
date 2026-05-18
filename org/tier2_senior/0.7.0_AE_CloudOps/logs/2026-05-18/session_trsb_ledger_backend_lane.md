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

## Current State

| Item | Status |
|------|--------|
| TRSB_LEDGER TO-0 | COMPLETE — brief shipped; RAVC2 to COO~B |
| TRSB_LEDGER TO-1..TO-5/TO-8 | PENDING — serial lane, TO-1 next |
| TRSB_LEDGER TO-9 | STAGED — droppable stretch, do NOT start |

## Next Steps

1. TO-1 — group-auth enforcement (next in the serial lane).
2. TO-5 dynamodb.tf: AE 0.5.0's TO-6 lands first (durability attrs); rebase the by-approver GSI
   stanza on top. Coordination open with 0.5.0.
3. COO~B routing decision owed on the `/api/public/trades/*` NONE-auth bypass (brief §3).
