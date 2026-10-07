# MDPF_SECCLASS -- who gets 200 on the Books client and advisor pages (read-only trace, 2.0.0_SA_COO~M1, 2026-10-07 ~17:1xZ)

Asked by 1.0.0_SA_CTO~DELL1 msg 475: FWD-1 grades on a real advisor's 200 read of a client page. The laptop CVO's walker got 403. This
trace reads code at round head aed1090344 only. No request was sent and no login was used.

## The path, gate by gate

| step | where | rule | denies with |
|---|---|---|---|
| 1 | edge `infra/aws/lambda-edge/auth-validator-edge/index.mjs` ~:400-425 (ADVI_ROLGAT tier gate) | runs only on `/api/scoped/advisor-intelligence/*`; NOT on `/api/scoped/partners/books/*` | 401 |
| 2 | edge `.004a` ~:428-447 + `getAllowedAdvisorIds` ~:219-227 | `/api/scoped/partners/books/advisor/{id}/...`: `role==admin` or `firmRole==admin` -> all advisors; else `{id}` must equal `jwt.advisorId`; no `advisorId` and not admin -> 403 | **403** |
| 3 | edge `.004c` ~:450-520 | `/api/scoped/partners/books/relationship/{id}/...` (the CLIENT page): `role==admin` or `firmRole==admin` bypass. Else it needs `jwt.advisorId` + `jwt.firmId` (else 403 missing_identity_claims), the firm's ownership map (fetch fail 503, schema 500), the advisor in `map.advisors` (else 403), and `{id}` in that advisor's relationships (else 403 rule=004c) | **403** |
| 4 | API `infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/lambda_function.py` ~:1811-1860 | the firm must be in the JWT's allowed firms (`is_authorized`), else 401. `_required_tier_for_path` returns None for `/scoped/partners/books/*`, so the lambda's tier and L1 checks do NOT run there; the advisor scope is the edge's alone | 401 / 404 |

## Which identities get 200 on a client page (`.../books/relationship/{clientId}/platinum-summary`)

- **YES:** a JWT with `role == "admin"` or `firmRole == "admin"` (a partner-firm admin, e.g. the 49 Financial firm admin the edge's own
  comment names), for a firm in its allowed firms.
- **YES:** a non-admin advisor whose `jwt.advisorId` is in that firm's ownership map, with `{clientId}` among that advisor's
  relationships.
- **NO (403 by design):** an identity with neither admin flag nor `advisorId`. This includes `tier == "internal"` and
  `userType == "Dev"`: those pass the tier gate (step 1) but are NOT in `.004a` / `.004c`'s bypass set. That is the most likely cause of
  the walker's 403, though it is inferred: the walker's JWT claims were not read here.

## What this means for FWD-1

- The walker's 403 is the scoping design working, not a FWD-1 break, PROVIDED the walker identity carries no admin flag and no
  `advisorId`. The laptop CVO can confirm by reading its own JWT claims, `role` / `firmRole` / `advisorId`, with no new login.
- The grade needs one of the two YES identities. Both are real people's logins (a firm admin or an advisor). Using one, or minting a
  test identity with those claims, is not this seat's to do silently: it is a call for 1.0.0_SA_CTO and, for a person's login, Andrew.
- A YES identity that still gets 403 on a client it owns would be a break, and a cell.
