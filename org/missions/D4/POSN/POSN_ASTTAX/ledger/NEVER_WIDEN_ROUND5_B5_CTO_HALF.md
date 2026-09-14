# NEVER-WIDEN SIGN-OFF -- CTO HALF -- POSN_ASTTAX round 5, B5 (`AT5-s-9`): the satellites leaf allowlist on shared-advisor-router

**Signer:** `1.0.0_SA_CTO~Z`. **Counterpart:** `2.0.0_SA_COO~Z`'s B5 COO half, `ledger/NEVER_WIDEN_ROUND5_B5_COO_HALF.md`.
**Authority for the cell:** Andrew-direct ~18:1xZ, "I am fine with the recs as youve listed them" (record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260914_181xZ_OPEN_CALLS_RECS_APPROVED_B5_YES_CALL2_QUESTIONED.md`
@`730b3309fa`). **Rule:** CLAUDE.md NEVER#1. **2026-09-14 ~18:2xZ.**

> **SIGNED, for the act below exactly as bounded. Anything a plan, a source diff or a live read shows outside these
> bounds is NOT SIGNED: the cell STOPs before `safe-apply` and re-arms a row with the observation verbatim.**

---

## THE RADIUS IS FIVE BEHAVIORS, NOT ONE -- measured, and the reason this half exists

`shared-advisor-router` is associated as the `origin-request` function on **five** ordered cache behaviors of the portal
distribution (`infra/aws/terraform/portal-auth/cloudfront-distribution.tf`, association lines printed):

| # | path_pattern | association |
|---|---|---|
| 1 | `/api/scoped/advisor-intelligence/artifacts/*/*` | `:342` |
| 2 | `/api/scoped/advisor-intelligence/artifacts/*` | `:373` |
| 3 | `/api/scoped/advisor-intelligence/entities/*/*` | `:404` |
| 4 | `/api/scoped/advisor-intelligence/*.json` | `:634` |
| 5 | `/api/scoped/satellites/*` | `:882` |

All five read `local.shared_advisor_router_arn` (`:66`, the function's `qualified_arn`), so **publishing a new version
re-points all five at once.** Behaviors 1-4 are the live Advisor Intelligence serving path for every partner firm.
A B5 change written for the satellites route therefore reaches them, and this half signs only because the change is
confined to the satellites branch and the cell proves that before and after.

## What the act MAY touch, key by key

| key | change | rollback |
|---|---|---|
| `infra/aws/lambda-edge/shared-advisor-router/index.mjs` | ONLY the satellites branch (`:330-360` at HEAD, last commit `40697fe79d`) and its constants (`:89-101`): `SATELLITES_REGISTRY_LEAF` / `SATELLITES_REGISTRY_KEY` become a leaf allowlist `{registry.json, holdings.json, characteristics.json}` -> `platinum/satellites/<leaf>`; the refusal branch (404 `unknown_satellites_resource`) kept for every other leaf; same prefix, same bucket resolution, same tenant assertion | revert the commit |
| `portal-auth/shared-advisor-router.zip` (artifact) and `aws_lambda_function.shared_advisor_router` | one new published version | re-associate the PRIOR version, which the cell reads from the live distribution config and prints BEFORE the apply |
| `aws_cloudfront_distribution.portal` | the five associations above move from the prior qualified ARN to the new one; **no behavior, origin, cache policy or path pattern changes** | re-associate the prior qualified ARN on all five, re-apply |
| a content-identical WAF read artefact on `portal-auth` (`aws_wafv2_web_acl.opal_cloudfront_protection`, the `version ""` vs `null` normalisation recorded on `IRPT_BCKEND` IB-s-15) | may appear as an in-place no-op | none needed |
| `shared-advisor-router-response`, `auth-validator-edge`, any other function, behavior, origin or resource | **NOT SIGNED** | -- |

## Writers of the named property -- "the rewrite rule for `/api/scoped/satellites/*` and `/api/scoped/advisor-intelligence/*`": N = 1

`shared-advisor-router` is the only `origin-request` function on the five behaviors (each shows one `viewer-request`
association, `auth-validator-edge`, and one `origin-request`, this function; `shared-advisor-router-response` is an
`origin-response` function on the same behaviors and is untouched). Census: `cloudfront-distribution.tf` association
lines read by this seat; `2.0.0_SA_COO~Z` cited the satellites branch at `index.mjs:95-101` and `:340-358` (22883).

## Expected outcome, read from the router's rule -- BOTH branches

- **Branch A:**
  1. **Source.** The diff of `index.mjs` touches only lines inside the satellites branch and its constants. The cell
     prints `git diff --stat` and the hunk headers.
  2. **Plan.** It reads the new function version, the distribution's five associations, and at most the classified
     WAF no-op.
  3. **After the apply,** the cell prints each result below. The two reads for each Advisor Intelligence behavior use
     the same authenticated firm and the same key, and their status and body hash must match:

     | request | expected |
     |---|---|
     | `/api/scoped/satellites/registry.json` | 200, the same bytes as before |
     | `/api/scoped/satellites/holdings.json` | 200 once B2 has landed, else the S3 404 envelope |
     | `/api/scoped/satellites/characteristics.json` | 200 once B4 has landed, else the S3 404 envelope |
     | `/api/scoped/satellites/anything-else.json` | the same 404 `unknown_satellites_resource` |
     | behaviors 1-4 (Advisor Intelligence) | one request each, before and after, identical |

- **Branch B -- any of these reads otherwise:**
  - a hunk outside the satellites branch;
  - a plan resource beyond those listed;
  - an Advisor Intelligence request whose status or body differs;
  - a non-allowlisted leaf that no longer refuses.

  **NOT COVERED.** Before the apply: STOP, no `safe-apply`. After the apply: re-associate the prior version on all
  five behaviors the same turn, then file the row.

## Sequencing and ledger

B5 depends on nothing; F3 and R1 depend on B5 DEPLOYED. The cell opens its own change-management ledger entry before the
publish (legs: git, the version publish, the distribution association, the five-path verify). Lambda@Edge replication
is not instant, so the after-reads run once the distribution reports `Deployed`, not at apply return.

## What this half does not cover

- The portal promote, DEV/PROD push or gitlink move (Andrew's separate word).
- B1, B2, R1 (`ledger/NEVER_WIDEN_ROUND5_CTO_HALF.md` @`af667548d1`); B4 (non-application, stated there).
- Any change to Advisor Intelligence routing, the tenant assertion, the OAI model or bucket policies.

Push state: LOCAL (this seat never pushes; site-Z pushes are held by `0.0.0_AB_MSTR~Z` on Andrew's word).
