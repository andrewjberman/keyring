# Deploy Completion Record
**Date opened:** 2026-08-20T19:34:11.168837+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260820T200531Z
**Deploy:** D7 TO-D: mint svc-analyst-intake service token (30d) + custody secret opal/ticketing/svc-analyst-intake, per CTO~Z U4 spec
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | mint RS256 svc-analyst-intake JWT (30d) + create Secrets Manager opal/ticketing/svc-analyst-intake | secret ARN + describe (name only) | MINTED RS256 svc-analyst-intake JWT (sub=svc-analyst-intake, userType=service, iss=opal-portal-auth, aud=opal-portal-api, TTL 30d exp 2026-09-19, rotate_by 2026-09-10) via opal/auth/jwt-private-key; CUSTODY SECRET created opal/ticketing/svc-analyst-intake (ARN suffix -HGzn67), value=JSON{token,...} consumer reads .token; value never printed; first-mint (was ResourceNotFound) | CLOSED 20260820T193609Z |
| L2 | verify | live pairs each own invocation: analyst LIST 200 / CREATE 201 / GET 403 / METRICS 403 / CLAIM 403; svc-ticket-form READ 403; marker-control name-without-service 403; test ticket cleaned | HTTP rows | CLOSED ON (b) (CTO~Z ruling msg 2741): stored credential LIST-scoped. FINAL token (version 77bf1488, no allowedFirmIds/tier claim -- honest to its authority) exercised on the EXACT stored bytes: LIST 200; GET 403; METRICS 403; CLAIM 403; svc-ticket-form LIST 403; marker-control (sub=svc-analyst-intake NO service marker) 403 UNRESOLVABLE; CREATE 400 (LIST-scoped, DEFERRED). SCOPE PIN (verbatim): CREATE has ZERO live consumers today (the duty is read+buzz); FIRST CONSUMPTION of CREATE routes through the CTO~Z gate as its own exercised row -- via the (c) ticket-scoped-attribution design in the Lambda, NEVER tier=internal. CREATE->201 was mechanism-VERIFIED on a 15-min UNSTORED token (tier=internal, 201, cleaned, zero residue) then held off the stored credential; CTO~Z self-corrected (a)-literal-vs-deployed-authorizer, (a) falsified by the mutant 400. Zero board residue. | CLOSED 20260820T200531Z |

## Log

- 20260820T193411Z OPENED by 0.7.0_AE_CloudOps with 2 leg(s)
- 20260820T193609Z LEG L1 closed: MINTED RS256 svc-analyst-intake JWT (sub=svc-analyst-intake, userType=service, iss=opal-portal-auth, aud=opal-portal-api
- 20260820T194352Z HELD-SOVEREIGN-GATED gate=external/CREATE-firm-attribution: the U4 token spec (CREATE+LIST action scope) omitted a 
- 20260820T195723Z HELD-SOVEREIGN-GATED gate=external/CREATE claim-breadth: verified tier=internal achieves CREATE->201 (deployed auth
- 20260820T200530Z HOLD RELEASED -> OPEN
- 20260820T200531Z LEG L2 closed: CLOSED ON (b) (CTO~Z ruling msg 2741): stored credential LIST-scoped. FINAL token (version 77bf1488, no allowedFirmIds/t
- 20260820T200531Z CLOSED -- all 2 legs proven
