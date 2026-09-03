# HOLD -- no UNSCOPED apply of `infra/aws/terraform/shared-infra` until ten DESIRED != APPLIED drifts are declared

**Opened:** 2026-09-03 ~16:50Z by `1.0.0_SA_CTO` (owner of the shared-infra module; gate on its applies).
**Class:** never-widen (CLAUDE.md s.5): an unscoped apply of this root today would move ten resources nobody ordered
moved, one of them a served users table's delete guard and nine of them the authorization of served API routes.
**Source of the measurement:** the UNSCOPED control plan run by `0.8.0_AE_CloudComp~K` under
`NFRA_GLOBGRPH.TO-MSHEAT-EXPIRY` after its target-scoped lifecycle apply (row `NFRA_GLOBGRPH-S2` @28b9a1e4d6;
plan text `org/tier2_senior/0.8.0_AE_CloudComp~K/deliverables/NFRA_GLOBGRPH.TO-MSHEAT-EXPIRY.unscoped-post-plan.txt`
@49c49c218f, UTF-16): `Plan: 0 to add, 10 to change, 0 to destroy.`

## The ten, and where each remedy lives

| # | address | live | declared (CLOUD) | direction, measured | remedy owner |
|---|---|---|---|---|---|
| 1 | `aws_dynamodb_table.opal_users_v2` `deletion_protection_enabled` | `true` | **DECLARED on both sides as of 16:4xZ** (corrected 17:1xZ): `0.8.0_AE_CloudComp~K` landed the one line on CLOUD @14fbeace00 under `TO-USERS-DELPROT` (scoped plan 0/0/0, no-op apply, ledger closed) minutes before the "superseded" reading reached the issuer; `origin/SITEZ` declares the same line at the same position under an eight-line OPSEC comment (OP-s-8) | the module no longer lags; **this row is CLOSED on CLOUD**. Merge note for 0.0.0_AB_MSTR: the two sides add overlapping regions (CLOUD one line; SITEZ the identical line plus its comment) -- if git does not merge it clean, take SITEZ's hunk, the superset with the identical declaration |
| 2-10 | `module.apigateway_portal.aws_apigatewayv2_route.{r_as2dsme, r_c0k8rl0, r_gwygx58, r_m8wdq80, r_mxus2bs, r_o2xr1ct, r_ruzaqhq, r_sogv7z9, r_t81twif}` -- `GET /v1/health/data-availability`, `GET /v1/market/rsi`, `GET /v1/market/rsi/details`, `GET /v1/sentiment/fear-greed`, `GET /v1/sentiment/fear-greed/details`, `GET /v1/sentiment/keywords`, `POST /v1/sentiment/keyword-intelligence`, `GET /metadata/yang`, `GET /v1/metadata/yang` | `authorization_type = CUSTOM`, `authorizer_id = naqxlm` (the module's own `portal_jwt` authorizer) | `authorization_type = "NONE"` | **out of band**: only `shared-infra` declares these keys (census of every TF root: no second writer); `origin/SITEZ` does not touch `routes.tf`; the 2026-08-03 consolidation moved 20 `/api/scoped/partners/...` routes, not these; the NFRA_OPSEC202609 channel and PRD do not name them. The three public routes the hand LEFT open (`ANY /auth/{proxy+}`, `OPTIONS /auth/{proxy+}`, `OPTIONS /{proxy+}`) are exactly the auth handshake and CORS preflight -- the shape of a deliberate hardening, not a slip. Actor and time unknown from the repo; CloudTrail `UpdateRoute` on the API is the instrument that names them. | the security project's own loop (`NFRA_OPSEC202609`, site Z), routed via `0.0.0_AB_MSTR` -> `0.0.0_AB_MSTR~Z`; the safe declaration is what is LIVE (`CUSTOM` + the authorizer) -- un-hardening a public endpoint is a decision for its owner, never a plan side effect |

## What this hold binds

- **No unscoped `terraform apply` of `shared-infra` by any seat** until the unscoped plan reads `0 / 0 / 0`. Every apply in
  this root is `safe-apply` with `-target` declared in its own ledger entry, and its acceptance is an UNSCOPED re-plan
  afterwards that reads exactly the drifts this table still lists and nothing else (a scoped apply verified by a scoped
  re-plan is the measured trap).
- The lifecycle entry `20260903T1418Z_shared-infra-ms-heat-snapshots-expire-60d_deploy_completion.md` closes on
  DISCLOSURE (the lifecycle change is gone from the unscoped plan; live reads two rules; this hold carries the rest) --
  the issuer's amendment @ee688a660b, agreed.
- Andrew's word at the COO terminal 2026-09-03 ~16:2xZ ("We are only working COMPEFFICACY and CLDGRPH on this device")
  bounds this device: no new NFRA_GLOBGRPH order is cut here for rows 2-10; the finding travels to the owning project's
  loop as spine v2.4 prescribes.

## Closes when

The unscoped plan of `shared-infra` reads `0 to add, 0 to change, 0 to destroy` at HEAD, cited with its output file and
vintage, after (1) the SITEZ merge leg lands the `dynamo.tf` declaration and (2) the nine routes are declared as live by
their owning project. Closed by the module owner (`1.0.0_SA_CTO`) on that read.
