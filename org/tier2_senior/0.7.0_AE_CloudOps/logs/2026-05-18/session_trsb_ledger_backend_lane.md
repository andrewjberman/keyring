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

## TO-3 — Append-only audit_events — COMPLETE

Closes B1 (no event log — state was a destructive `SET` overwrite) and B3 (the execute
failure path silently erased the failed attempt). Embedded `audit_events` list per the
CTO~B Q3 ruling — atomicity with the status update, not a separate table.

- `workflow_handler.py`: `build_audit_event()` (PRD §3.2 7-field schema); `update_submission()`
  gained an `audit_event` param that appends via `list_append(if_not_exists(#audit_events,
  []), [event])` — atomic with the status SET, single `update_item`, no dual-write/lost-update
  window. `handle_approve` appends APPROVED; `handle_reject` appends REJECTED (detail =
  rejection reason); `handle_execute` appends EXECUTED on the success path (the COMPLETE
  `final_updates` write — only after the brokerage send succeeds). Failure path (B3 fix):
  the except block appends EXECUTION_FAILED (outcome FAILURE, detail = the error) **atomically
  with** the status revert — one `update_item`, so the failed attempt can never be lost
  between two writes. (TO scope said "before the revert"; atomic-with is strictly stronger —
  noted in the RAVC2.)
- `submission_handler.py`: row is created with the SUBMITTED event already in `audit_events`;
  `get_user` + `build_audit_event` helpers added; initiator `groups` snapshotted at
  submission time (B7).
- Each event snapshots `actor_groups` — `build_audit_event` copies the list so a later change
  to the executors/approvers lists cannot rewrite history.
- `tests/test_audit_events.py` 5/5 (schema, groups-snapshot copy, list_append expression,
  no-event omission); TO-1 `test_group_auth` 10/10 + TO-2 `test_actor_identity` 6/6 still
  green. ds-commit-gate clean. Commit 7f81306e1.

Deploy mechanism — `trade-submission-handler` was still on `placeholder.zip` + `lifecycle
ignore_changes` (config-only; code deployed out-of-band via `aws lambda
update-function-code`, which CLAUDE.md Rule 1 bans). TO-3 Phase 3 mandates terraform apply,
so that one resource block was flipped to the S3-backed `aws_s3_object` pattern — the same
flip TO-1 did for `trade-workflow-handler`, and the `trade-submission-handler` slice of the
planned TRSB_TFIMPT.W3 migration done early. Parity verified first: deployed code is
content-identical to the repo src (line-endings only) — no divergence reclaimed. Commit
db386bc13 (lambdas.tf + source-map). Both Lambdas built + uploaded; terraform apply
0 add / 2 change / 0 destroy; 0-diff verified; live CodeSha256 matches both uploads
(submission `r1dqGn2+...`, workflow `DdCmbyi6...`). record-terraform-deploy 5a3e43e08.
trade-pipeline-v1.12.0.

Phase-3 deployed end-to-end smoke (AC3/AC5) — `.runtmp/to3_smoke_probe.py`, self-contained,
19/19 checks PASS. Two full trade lifecycles through the DEPLOYED Lambdas:
- SUCCESS: submit -> approve -> execute(vident) -> `audit_events` == [SUBMITTED, APPROVED,
  EXECUTED], status COMPLETE; actor_groups snapshots [] / ['approvers'] / ['executors'].
- FAILURE: submit -> approve -> execute(brokerage not in BROKERAGE_EMAILS -> ValueError in
  the execute try-block) -> `audit_events` == [SUBMITTED, APPROVED, EXECUTION_FAILED],
  status reverted to APPROVED. **B3 confirmed fixed** — the failed attempt (actor, time,
  error in `detail`, outcome FAILURE) is durably recorded despite the row reverting.
- Email isolation: the deployed handlers broadcast approval/execution-request emails to
  every active trade-users row (all 9 are real Opal staff, all SES-verified). The smoke
  temporarily set the 9 real rows `active=False` + created 3 temp `@opal.test` users, so
  the broadcasts resolved only to unverified addresses (SES sandbox rejects -> handler
  try/except swallows -> nothing delivered). Real `active` values restored in the `finally`
  block, restoration verified (check 19 PASS). Only one real email delivered: the brokerage
  email for the success trade -> andrew@opalinvest.com (BROKERAGE_EMAILS, SES-verified).
- Cleanup: 3 temp users + 2 temp submissions deleted. Two `executed_trade.xlsx` artifacts
  remain under test-submission-scoped S3 keys in `opal-data-trade-submissions`
  (`submissions/2026-05-18/TRADE-20260518-1751{31,34}-*/`) — orphaned test artifacts, left
  in place (S3 object deletion is a confirmation-gated op, out of this smoke's scope).

AC1-6 all PASS.

### Compiler Tools
| Tool | Use | Result |
|------|-----|--------|
| comp-* | trade-* Lambdas | Not modeled (PRD §5) — direct Terraform + source read is the TO-sanctioned substitute. |
| Direct read | workflow_handler.py, submission_handler.py, email_utils.py, excel_generator.py, config.py, dynamodb.tf, lambdas.tf | Confirmed item schemaless beyond keys (`audit_events` = new top-level list, no TF schema change); located the handle_execute revert block; confirmed send_brokerage_email raises ValueError on an unknown brokerage (the forced-failure trigger). |
| build-and-upload.sh | trade-workflow-handler + trade-submission-handler | Built + uploaded both artifacts to s3://opal-313476888478-lambda-artifacts/trade-pipeline/. |
| terraform plan/apply | trade-pipeline | 0 add / 2 change / 0 destroy; 0-diff verified post-apply. |
| Deployed-Lambda parity probe | trade-submission-handler | Confirmed deployed code == repo src (content-identical) before the S3-backed migration. |

## TO-4 — Compliance JSON snapshot + EXECUTED-rests — COMPLETE

Closes B4 (compliance JSON snapshot never written — `json_s3_key` always null) and B2
(EXECUTED status never durably rests). Retires `COMPLETE` per Andrew Q2 ruling 2026-05-18.

- Phase 1 — `iam.tf` confirmed: `s3:PutObject` on `opal-data-trade-submissions` (+`/*`)
  already granted (S3Access sid). No IAM change.
- `workflow_handler.py` `handle_execute`, after a successful back-office handoff (Excel
  generated + S3-archived + brokerage email sent):
  - B4: writes the immutable compliance snapshot — the full row INCLUDING `audit_events` —
    as `submission.json` to `opal-data-trade-submissions` under
    `submissions/{date}/{submission_id}/submission.json`, and sets `json_s3_key` on the row.
    The snapshot is the ALL_NEW row returned by the audit-append update, so it is complete
    and self-describing (carries its own `json_s3_key`). Previously `json_s3_key` was always
    null — `handle_execute` never called the only code (`excel_generator.lambda_handler`)
    that wrote it.
  - B2: the same-invocation auto-advance to `COMPLETE` is removed. The first
    `update_submission` already set status=EXECUTED; the row now RESTS there. No
    `completed_at` auto-write. A table query can finally observe an EXECUTED row.
- `config.py`: `COMPLETE` removed from the `Status` enum. No backend path in the
  trade-workflow-handler bundle produces or asserts `COMPLETE`.
- Scope boundary (per the TO + data_reprocess_scope): `dashboard-api` retains its `COMPLETE`
  references intentionally — legacy-row read-tolerance, TRSB_LEDGER.008b scope. The FE
  `completeSubmission` removal is also TO-8b. `trade-submission-handler` /
  `trade-parquet-batch-export` config.py copies keep a now-dead unused `COMPLETE` constant
  (not asserted) — left untouched, out of this TO's deploy unit. Legacy `COMPLETE` rows in
  the table are left as-is. Reported in the RAVC2.
- ds-commit-gate clean; unit tests green (test_audit_events 5/5, test_group_auth 10/10,
  test_actor_identity 6/6). Commit b7782b9fc.

Deploy — build-and-upload + terraform apply (0 add / 1 change / 0 destroy; 0-diff verified;
live CodeSha256 `zyjQKOZJ...` matches the upload). Source-map 87f601b55; record
66eea17fe. trade-pipeline-v1.13.0.

Phase-3 deployed empirical execute run (AC4) — `.runtmp/to4_smoke_probe.py`, 14/14 PASS.
One trade through the DEPLOYED Lambdas submit -> approve -> execute(vident):
- B2: execute response + row status both `EXECUTED` (not COMPLETE); `completed_at` is
  None / not auto-written; `executed_at` set. The row rests at EXECUTED.
- B4: `json_s3_key` non-null on the row; the S3 object exists in
  `opal-data-trade-submissions`; the snapshot contains the full row, status EXECUTED, and
  `audit_events` == [SUBMITTED, APPROVED, EXECUTED]; the snapshot is self-describing
  (carries its own `json_s3_key`).
- Email isolation identical to the TO-3 smoke (9 real users active=False for the window +
  3 temp @opal.test users; restored + verified in the finally block — check 14 PASS).
- Cleanup: temp users + temp submission deleted. Executed S3 artifacts (`.xlsx` +
  `submission.json` under the test-submission key) left in place.

AC1-5 all PASS.

### Compiler Tools
| Tool | Use | Result |
|------|-----|--------|
| comp-* | trade-* Lambdas | Not modeled (PRD §5) — direct Terraform + source read is the TO-sanctioned substitute. comp-iam N/A (uninstrumented). |
| Direct read | iam.tf | Confirmed s3:PutObject on opal-data-trade-submissions already granted (S3Access sid) — no IAM change. |
| Grep | trade-pipeline backend for COMPLETE / completed_at / json_s3_key | Mapped every reference; retired the workflow-handler bundle's; documented the deliberately-retained dashboard-api refs (TO-8b legacy-tolerance) + the dead unused constants in other Lambda config.py copies. |
| build-and-upload.sh + terraform plan/apply | trade-workflow-handler | 0 add / 1 change / 0 destroy; 0-diff verified; CodeSha256 match. |

## TO-5 — by-approver GSI repoint — COMPLETE

Closes B5 (rejected trades fall out of the by-approver GSI — the approver's decision history
is incomplete by construction). PRD R3 HIGHEST-CARE item — a GSI key-schema change, executed
as the mandatory create-new -> backfill -> cutover -> drop-old sequence (DynamoDB does not
permit an in-place key-schema change; one GSI op per UpdateTable).

Root cause confirmed empirically: the old `by-approver` GSI ranged on `approved_at`, which a
REJECTED trade never carries -> 11 indexed items vs 17 decided rows (6 rejected trades absent).

### GSI cutover step log (ordered)

1. **Handler decided_at (trade-pipeline-v1.14.0)** — `workflow_handler.py` `handle_approve` +
   `handle_reject` both write `decided_at` (= the decision timestamp); `approved_at` /
   `rejected_at` retained. Deployed FIRST so all new decisions carry `decided_at` before the
   new GSI is created. Commit ef7cc2d1f; build faf907ba6; apply 0/1/0, 0-diff; tag v1.14.0.
2. **Backfill (committed, idempotent)** — `tools/trsb_ledger_005_backfill_decided_at.py`
   scans `opal-trade-submissions`: writes `decided_at` on every decided row lacking it
   (= existing `approved_at`/`rejected_at`); appends a synthetic `MIGRATED` audit event
   (PRD R1, 7-field schema, outcome INFO) to every row with no `audit_events` list. Commit
   38a649f47. Ran from the local repo (Rule 12 — boto3, no EC2/SSM). Result: 17 rows, all
   17 backfilled both ways (all predate TO-3). Post-backfill verification re-scan: 17/17
   decided rows carry `decided_at`; every row carries an `audit_events` list.
3. **Create GSI (separate apply)** — `dynamodb.tf`: added `decided_at` attribute +
   `by-approver-decided` GSI (hash=approver_email, range=decided_at). Commit c72ea81c9;
   plan isolated to the single GSI add (0/1/0); apply 4m16s (DynamoDB index backfill);
   0-diff after. GSI reached IndexStatus ACTIVE. Verified: `by-approver-decided` indexes
   17 items (6 REJECTED + 11 COMPLETE) vs the old `by-approver`'s 11 — the 6 rejected
   trades are now indexed.
4. **Cutover (trade-pipeline-v1.15.0)** — `dashboard_api.py`: `get_by_approver` AND
   `get_approver_dashboard` repointed to `by-approver-decided`. BOTH query sites moved —
   the TO names `get_by_approver`, but `get_approver_dashboard` runs the same
   approver-history query and would (a) also omit rejected trades and (b) break at runtime
   once the old GSI is dropped. Also removed 2 pre-existing unused imports (`Attr`, `Role`)
   flagged by the ds-commit-gate ruff check. Commit 531ec823a; build a1468fd2a; apply
   0/1/0, 0-diff. Deployed-Lambda verification: `get_by_approver` for andrew@opalinvest.com
   returned 15 trades including all 6 REJECTED — pre-cutover it returned only the COMPLETE
   ones.
5. **Drop old GSI (separate apply)** — `dynamodb.tf`: removed the `by-approver` GSI + the
   now-orphaned `approved_at` attribute declaration (`approved_at` remains a stored data
   field; only its index-key declaration is removed). Commit 85ada4473 (before apply);
   plan isolated to the single GSI removal (0/1/0); apply 4s; 0-diff after.

### Phase 3 — end-state verification
Query of `by-approver-decided` for andrew@opalinvest.com (a known-rejected-trade approver):
15 trades, 6 REJECTED, known rejected trade `TRADE-20260106-224805-0A54BD` present. The
table now carries 4 GSIs (by-date, by-initiator, by-approver-decided, by-status); `by-approver`
is gone. B5 closed.

Coordination: TO-6 (AE 0.5.0, point_in_time_recovery + deletion_protection) already landed
(trade-pipeline-v1.9.0); MCP'd 0.5.0_AE_OpalETL before editing dynamodb.tf — they ACK'd
dynamodb.tf clear, no concurrent edit. Every TO-5 plan was isolated to its own single change.

AC1-6 all PASS. record f153bd61f; trade-pipeline-v1.14.0 + v1.15.0.

### Compiler Tools
| Tool | Use | Result |
|------|-----|--------|
| comp-* | trade-* Lambdas / GSI | Not modeled (PRD §5) — direct Terraform + source read is the TO-sanctioned substitute. |
| Direct read | dynamodb.tf, dashboard_api.py get_by_approver, workflow_handler handle_approve/reject | by-approver = hash approver_email / range approved_at confirmed; found get_by_approver AND get_approver_dashboard both query it. |
| terraform plan (x2) | create-GSI apply + drop-GSI apply | Each plan isolated to the single GSI op (Phase-2 gate) — no base key schema / billing change. |
| aws dynamodb describe-table / query | GSI status + populations | Empirically proved B5 (11 vs 17), GSI ACTIVE, post-cutover rejected trades returned. |

## Current State

| Item | Status |
|------|--------|
| TRSB_LEDGER TO-0 | COMPLETE — brief shipped; RAVC2 accepted by COO~B |
| TRSB_LEDGER TO-010a | COMPLETE — unauth route removed, shared-infra-v1.12.0; RAVC2 to COO~B + CC CTO~B |
| TRSB_LEDGER TO-1 | COMPLETE — trade-pipeline-v1.10.0; RAVC2 accepted |
| TRSB_LEDGER TO-2 | COMPLETE — trade-pipeline-v1.11.0; RAVC2 accepted |
| TRSB_LEDGER TO-3 | COMPLETE — trade-pipeline-v1.12.0; RAVC2 accepted |
| TRSB_LEDGER TO-4 | COMPLETE — trade-pipeline-v1.13.0; RAVC2 accepted |
| TRSB_LEDGER TO-5 | COMPLETE — trade-pipeline-v1.14.0 + v1.15.0; AC1-6 PASS; RAVC2 to COO~B |
| TRSB_LEDGER TO-8 | PENDING — serial lane, TO-8 next (last in the lane) |
| TRSB_LEDGER TO-9 | STAGED — droppable stretch, do NOT start |
| TRSB_LEDGER TO-10 | REASSIGNED to AE 0.6.1 (COO~B 2026-05-18) — off my lane |
| opal-data-mdpf bucket | DONE by 0.5.0_AE_OpalETL (MDPF_ASSETS.012) — off my queue |

## Next Steps

1. TO-8 — /api/general/trades/users/me endpoint (last TO in the serial lane).
