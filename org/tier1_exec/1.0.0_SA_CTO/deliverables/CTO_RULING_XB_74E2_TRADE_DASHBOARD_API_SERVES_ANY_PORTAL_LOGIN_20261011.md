# CTO ruling -- XB-20261011T171837Z-74e2: `trade-dashboard-api` serves eight of nine routes to any verified portal login

From 1.0.0_SA_CTO (laptop, cluster lead), 2026-10-11 ~17:3xZ. Finding: `1.0.0_SA_CTO~DELL2`, row IRPT_YCDGEN-D2-S60, record
`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r14/ROUTE_CENSUS_WHAT_A_SERVICE_TOKEN_OPENS_20261011.md` ADDENDUM 1
@8fdcba9a75 (read at origin/box/dell2). dell2 named three things it had not established; this seat established them.

## 1. The three unknowns, measured from the laptop (17:2xZ, read-only)

| question | answer | instrument |
|---|---|---|
| Deployed bytes = repo? | **YES.** Live `CodeSha256` `TJ/P4Nfo...WOAo=` equals the artifact's `content-sha256` (`s3://opal-313476888478-lambda-artifacts/trade-pipeline/trade-dashboard-api.zip`, 2026-07-21T16:42Z); the handler's last source change is 2026-07-14 (`b9d61307cf`, 4 commits in its history), before the build. | `lambda get-function-configuration`; `s3api head-object`; `git log -- .../dashboard_api.py` |
| Does the table hold more than one firm's trades / client data? | **It holds Opal's OWN model and fund trade blotter, not client accounts.** `opal-trade-submissions`: 33 items, key `submission_id`, GSIs by-date/by-initiator/by-approver-decided/by-status. Attribute NAMES of the items read (no values): `initiator_name, initiator_email, approver_*, submission_date, status, securities, model_securities, fund, brokerage, weight_unit, weights_as_of, proposed_trades_as_of, excel_s3_key, trade_csv_key, attestations, audit_events, trade_comments, other_comments, ...`. No `firmId`, `accountId`, `clientId`, `household` or any client-name attribute among them. | `describe-table`; `scan --limit 3 --query 'Items[].keys(@)'` |
| Can a partner-firm or client login reach the routes? | **YES, by code.** The nine routes sit on the shared portal HTTP API with the one authorizer `portal_jwt` (`opal-portal-authorizer`, `naqxlm`), which verifies any portal login's token and emits `email, tier, role, firmId, userType, allowedFirmIds, ...` as context (`infra/aws/users/lambda/portal-authorizer/index.mjs:397-415`). The router (`dashboard_api.py:38-85`) passes the event to `get_users_me` only; the other eight handlers never see the context. The portal page `/trade-submission` is `<ProtectedRoute>` with no `requireAdmin/requireInternal/requireDev` and its nav item carries no `requiresTier` (`portal/src/App.tsx:137, 514-518`), so any signed-in login sees the page and its client calls `/api/general/trades/submissions*` (`portal/src/api/endpoints/trade-submission.ts:334-371`). | `routes.tf:85-104`, `main.tf:43-50`, the three source files |

## 2. Severity, as ruled

**Confirmed exposure, MEDIUM: Opal-internal pre-trade information (the firm's own model/fund trade submissions, securities and
weights, plus the trade-users list of names/emails/roles less password and api_key) is readable by any partner-firm login
(49financial, cottonwood, inflection advisors) through the portal API.** It is NOT a cross-firm read of CLIENT data: the table carries
no client account, household or firm attribute. dell2's phrase "a cross-firm read by code" is right about the caller set and wrong
about the data class. No evidence of any such read is in hand (no log was read; CloudWatch for `/aws/lambda/trade-dashboard-api`
is the instrument if Andrew wants the history).

## 3. Remedy (ruled; the build is one cell)

1. **Lambda, the whole fix:** the router passes `event` to every handler; one helper `_require_internal(event)` reads the authorizer
   context the way `get_users_me` already does and returns 403 unless `tier == 'internal'` (or `firmId == 'opal-capital'`); every
   handler but `get_users_me` calls it first. `get_users_me` unchanged. Built and applied by Terraform in
   `infra/aws/terraform/trade-pipeline` (artifact + `source_code_hash`), `safe-apply`, NEVER-2 ledger; verified by one call per route
   with an internal token (200) and one with a partner-firm token (403). This alone closes the hole; no portal push needed.
2. **Portal, follow-on:** `/trade-submission` route and nav item gain `requireInternal` / `requiresTier: 'internal'`. Product file on a
   page partner logins can open today: DEV at will, PROD on Andrew's word (push law).
3. **Owner:** NFRA_OPSWKF's issuer (`project.json`: placement DELL2, status active; it owns the trade workflow surface in the
   tree; the pipeline itself predates the tree, TRSB ledger). `1.0.0_SA_CTO~DELL2` adds the cell as an L10 addendum (an FWD no
   cell served: "no non-internal login reads a trade submission or the trade-users list") and `2.0.0_SA_COO~O2` cuts it in its
   next issuance; the Terraform apply leg goes crossbox to the laptop's CloudOps if dell2's agent user cannot apply the
   trade-pipeline root (the packager-mint pattern, XB-282e). No hotfix outside the pipeline; no alert built.

## 4. Routing

- To dell2 (through `0.0.0_AB_MSTR` -> `~DELL2`): the three answers and the severity; row D2-S60 may cite this file; nothing for
  dell2 to do; laptop (`to`) side of XB-74e2 closed on this file.
- To Andrew: section 2 and the seat ask in section 3.3, once.
