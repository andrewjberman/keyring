# Post-Incident Note: TRSB_LEDGER P0 -- First Live Trade-Approve Failure

- **Date:** 2026-05-18
- **Author:** 2.0.0_SA_COO~B (incident command)
- **Reviewed by:** 1.0.0_SA_CTO~B
- **Severity:** P0 (first live trade-approve attempt failed; UX-blocking portal-wide)
- **Outcome:** RESOLVED. Zero data harm. Both root causes fixed and deployed.
- **Project:** TRSB_LEDGER (Trade Submission: Executor Authorization Enforcement + Audit-Trail Integrity)

## 1. Summary

On 2026-05-18, during the first-ever live test trade on the Trade Submission portal,
Andrew's APPROVE action failed with a browser error:

> Action Failed -- Unexpected token '<', "<!doctype "... is not valid JSON

This was a two-layer failure. The trade backend behaved **correctly**; the portal
delivery layer corrupted a correct backend response into unparseable HTML. There was
no handler defect. Both layers are now fixed.

## 2. Root Causes

### Layer 1 -- Correct authorization 403 (working as designed, NOT a bug)

Andrew approved as `andrew@opalinvest.com`. That account was in the `executors`
trade-users group only, not `approvers`. TO-1 group-auth enforcement (shipped earlier
this session) correctly returned `403 {"message": "...not in the approvers group..."}`.

This is the intended behavior of the new authorization model -- the segregation-of-duties
enforcement Andrew directed as Pillar A. The 403 itself was not the incident. The
incident was that Andrew never saw a readable denial message.

Operational unblock: `andrew@opalinvest.com` trade-users `groups` set to
`[approvers, executors]` (AE 0.7.0, Andrew-direct authorization 2026-05-18 18:45Z).

### Layer 2 -- CloudFront distribution-global error-masking (the real defect)

Portal CloudFront distribution `EVTSA9VEHNZVH` carried a **distribution-global**
`custom_error_response` mapping HTTP 403 and 404 to `200 /index.html`. This existed to
support single-page-app deep links (a user hitting `opalinvest.dev/advisor-intelligence/...`
directly must get `index.html`, not an S3 403).

`custom_error_response` cannot be scoped per-cache-behavior -- it is distribution-global.
So it **also** caught `/api/*` responses: a clean Lambda `403 {"message": ...}` was
replaced edge-side with `200 <!doctype html>`. The portal's `fetch().json()` then
crashed on the HTML, producing the "Unexpected token '<'" error.

This defect was portal-WIDE: **every API auth-denial on every portal page** was
unreadable to the user, not just trade submission. `comp-routes behaviors` had already
flagged the rule ("Lambda 403 auth-denials will be swallowed").

## 3. Fix

**TO-11 (`ae-cloudfront-spa-fallback-api-error-fix`, AE 0.7.0):**

- Removed the distribution-global `custom_error_response` (both the 403 and 404 entries)
  from `EVTSA9VEHNZVH`.
- Replaced the SPA deep-link fallback with a **CloudFront Function (viewer-request)**
  attached to the **default (S3) cache behavior only** -- it rewrites extensionless URIs
  to `/index.html`. Extensioned asset paths and all `/api/*` behaviors pass through
  untouched, so API 4xx now reach the front-end with their real status and JSON body.
- S3 website error-document was explicitly rejected -- incompatible with the OAC-backed
  origin (CTO~B ruling).
- Deployed via terraform apply; CloudFront `/*` invalidation issued post-apply.
  Tag `portal-auth-v1.15.9`.
- Regression smoke 3/3 PASS: SPA deep-link resolves, static asset loads, API 403 returns
  real JSON.

Result: the portal can now render a readable "you are not authorized -- speak to your
admin" message on any auth-denial, which is what Andrew explicitly asked for.

## 4. Second Finding -- STOP-Delivery Gap (process)

During incident command, a P0 STOP issued to AE 0.6.1 (then mid-destructive-deploy of
the unrelated TO-10) **did not surface until after that deploy completed**. The agent
was watcher-dark / turn-occupied through the heads-down window; the STOP landed in the
inbox but was only read post-completion.

The `inbox-check-before-landing` discipline (`memory/feedback_inbox_check_before_landing.md`)
is **cultural, not structurally enforced**. It fails under exactly the long heads-down
destructive operation where a STOP matters most. Outcome here was zero-harm by luck --
TO-10 was confirmed structurally unrelated to the P0.

### Recommendation (for whoever eventually builds the structural gate)

CTO~B is escalating the structural fix to Andrew as a finding + recommendation -- it is
a workspace-wide change to every agent's deploy flow (org-standards / ADHC-class
org-hardening), outside the TRSB_LEDGER charter, so it is **not** authored as a
TRSB_LEDGER TO. Andrew rules on whether it becomes a separate project.

Implementation constraints for the eventual builder:

1. **Mechanism must be filesystem, not MCP.** A shell wrapper or git hook cannot invoke
   the MCP `check_inbox` tool. The gate must read the filesystem inbox directory
   directly (`org/mcp/inbox/{serial}/` plus the base-serial directory) and act on what
   is there.
2. **Do NOT hard-block every apply/push on any inbox message.** Routine CC traffic would
   make the gate noise, and a noisy gate gets muscle-memoried past (the classic
   dead-gate failure). Design it as **surface-and-require-acknowledgement**, or filter
   specifically for urgent / STOP-flagged messages. That nuance is the difference
   between a gate that holds and one that is ignored.

Interim: AE 0.6.1 has owned the miss cleanly and adopted a personal pre-apply/pre-push
inbox check. That is the right interim posture until/unless Andrew greenlights the
structural version.

## 5. Status

- Layer 1: operational unblock done (`andrew@` groups -> `[approvers, executors]`).
- Layer 2: TO-11 deployed (`portal-auth-v1.15.9`), regression smoke 3/3 PASS.
- TRSB_LEDGER: 11 of 12 TOs shipped + RAVC-accepted (TO-7 dropped per Andrew Q4).
  Pillars A + B + C all closed and deployed.
- Final end-to-end confirmation pending: Andrew's live approve-retry.
