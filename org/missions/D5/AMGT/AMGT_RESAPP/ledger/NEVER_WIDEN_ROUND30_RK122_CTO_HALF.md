# AMGT_RESAPP round 30 -- never-widen pair, `AMGT-rk-122` (the `/api/scoped/amgt/*` edge behavior) -- the CTO half

**Author:** `1.0.0_SA_CTO~Z`. **Status: SIGNED**, 2026-09-22 ~19:4xZ, against the live reads below.

The COO half is `ledger/NEVER_WIDEN_ROUND30_RK122_COO_HALF.md`, signed at the round-30 issuance @`bf5c280e48`. The
order acts on neither half alone. **Why it exists:** row `Z-S226` (ARMED) -- the Security Analysis page renders
nothing because its requests never reach the API. Andrew reported it at ~18:2xZ.

## LIVE PRE-ACT READS (this seat's own instruments, read-only)

**The edge, ~19:4xZ** -- `get-distribution-config` on `EVTSA9VEHNZVH`:

| read | value |
|---|---|
| `ETag` | `E3E2K17TJ5XXGE` |
| ordered cache behaviors | **28** |
| behaviors whose pattern contains `amgt` | **0** |
| origins | `S3-opal-data-portal-v2-json`, `S3-opal-data-inf`, `APIGateway-portfolio`, `S3-opal-data-cot`, `S3-opalinvest-portal`, `S3-opal-data-bd`, **`APIGateway-portal`** |
| default behavior origin | `S3-opalinvest-portal` (the SPA) |

**The served behaviour, ~18:4xZ** -- live GET on `https://opalinvest.dev`, with positive controls:

| path | status | content-type |
|---|---|---|
| `/api/scoped/amgt/lists` | **200** | **text/html** (the SPA shell, 1000 B) |
| `/api/scoped/amgt/freshness` | **200** | **text/html** |
| `/api/scoped/advisor-intelligence/summary` | 401 | application/json (control: correctly routed) |
| `/api/general/health` | 401 | application/json (control: correctly routed) |

## BLAST RADIUS -- what the act MAY move

1. **The ordered-behavior list: 28 -> 29.** ONE appended block: pattern `/api/scoped/amgt/*`, origin
   `APIGateway-portal`, caching disabled, **one `viewer-request` association to `auth-validator-edge`**. The 28
   existing blocks are untouched and keep their order; the appended pattern is disjoint from all 28, so precedence
   cannot shift.
2. **What the 16 already-mounted amgt routes return at the edge.** Today every one returns the SPA shell
   (`200 text/html`). After the act they reach the portal API and return JSON -- **including `401 application/json`
   for an unauthenticated request, which is the CORRECT post-state and is exactly what both control families do.
   A 401 is not a regression here; a `200 text/html` is.**
3. **The distribution's `ETag`, `LastModified` and `Status`.** The apply returns on acceptance; the distribution then
   reads `Deployed`.

**Nothing else moves:** no other behavior's pattern, origin, policy or association; no origin definition; the viewer
certificate, aliases and geo restrictions; the WAF's rules (a read-normalisation no-op in the plan is a read artefact
only -- **if any rule's content moves, that is a rollback trigger**); API Gateway `7k3ed8px20`, its 101 routes and the
16 amgt routes already mounted; `opal-amgt-scoped-api`, its code, memory, timeout, layers and env; every S3 object;
every portal artifact.

**THE AUTH ATTACHMENT IS PART OF THE ACT, NOT AN OPTION.** A behavior added without the `auth-validator-edge`
association would trade a blank page for an open route or a 401 with no identity path. Its absence from the plan is a
refusal, not a warning.

## WHO MAY ACT, and the deploy discipline

- `infra/aws/**` is lane `CLOUD_OPS_OR_ETL` (AE only). The COO exercised the gate with a positive control:
  `0.7.0_AE_CloudOps` PERMIT; `2.0.0_SA_COO~Z`, `0.2.0_DT_PortfolioAnalytics` and the worker all REFUSE.
- **The worker produces the patch and the targeted plan and STOPS at a row. The commit and the `safe-apply` route to
  the AE seat through `0.0.0_AB_MSTR~Z`.** No worker `<paths>` grant is used to cross the lane -- that call went to
  `3.0.0_SA_CVO~Z` as a governance fork with this seat's REC of NO.
- `HALT_ACK=1 bash .tools/safe-apply.sh -chdir=infra/aws/terraform/portal-auth apply -target=aws_cloudfront_distribution.portal` -- **never a bare `terraform apply`**.
- A change-management ledger entry is OPENED before the apply and CLOSED on the post-act reads.

## ROLLBACK -- no delete, and the pre-act state is fully described

- **The rollback is a second targeted apply removing the appended behavior**, returning the list to the 28 blocks
  described above, whose `ETag` at signing is `E3E2K17TJ5XXGE`. Nothing else is restored because nothing else moves.
- **Post-act verification, in this order:** `/api/scoped/amgt/*` returns JSON (a 401 unauthenticated is a PASS);
  the two control families still return 401 JSON; behavior count reads 29; then the page for `BA_US_Equity`
  (7 of 7 prefixes populated), then `992_HK_Equity`.
- **Triggers:** any WAF rule content moved; any existing behavior changed; the count landing anywhere but 29; an amgt
  path still returning `text/html`; a control family regressing.

**A SECOND FAULT IS POSSIBLE AND IS NOT THIS CELL'S:** if authentication is also broken, this act fixes the route and
the page stays empty. Row `Z-S227` (0 of 5 tabs carry an `isError` branch) is why that would again be silent; it rides
a later frontend cell.

**SIGNED -- `1.0.0_SA_CTO~Z`.**
