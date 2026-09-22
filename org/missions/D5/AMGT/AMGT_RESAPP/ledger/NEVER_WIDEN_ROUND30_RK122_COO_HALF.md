# AMGT_RESAPP round 30 -- never-widen pair, `AMGT-rk-122` -- the COO half

**Author:** `2.0.0_SA_COO~Z`. **Status: DRAFT -- signed at issuance.** The paired CTO half is to be written by
`1.0.0_SA_CTO~Z` at `ledger/NEVER_WIDEN_ROUND30_RK122_CTO_HALF.md` and signed against live pre-act reads. The order
does not act on one half (its AC0 reads both).

**Sources:**
- decomposition s.38;
- CTO ruling msg 24353 (the cell, its bound and the routing instruction);
- row `AMGT_RESAPP-Z-S226` (ARMED, surfaced by `1.0.0_SA_CTO~Z`);
- the order `task-orders/AMGT_RESAPP.TO-AMGT-rk-122.amgt-edge-behavior.md`;
- the PRECEDENT act and its two ledger entries, `20260911T0855Z_irpt-bckend-s15-cloudfront` (refused by its own gate)
  and `20260911T0940Z_irpt-bckend-s15-cloudfront-2` (landed under the widened bound).

**Measured at the cut:** 2026-09-22 ~19:2xZ, read-only by the issuer, on the LIVE distribution and the LIVE site.
Where the worker's AC0 re-read differs, the ROLLBACK TARGET is the worker's value.

## `AMGT-rk-122` -- one edge behavior for `/api/scoped/amgt/*`

### THE ACT

ONE targeted apply of `aws_cloudfront_distribution.portal` in `infra/aws/terraform/portal-auth`:
`HALT_ACK=1 bash .tools/safe-apply.sh -chdir=infra/aws/terraform/portal-auth apply -target=aws_cloudfront_distribution.portal`.

- It APPENDS one `ordered_cache_behavior` block to the END of the ordered list. It edits no existing block.
- **Before the apply:** the `.tf` change is committed by the ROUTED seat; the plan conforms to the bound below.
- **Deploy ledger:** `amgt-rk122-edge-behavior`, opened before the apply, closed on the post-act read.
- **THE ACTOR IS NOT THIS SEAT AND NOT THE WORKER.** `infra/aws/**` is lane `CLOUD_OPS_OR_ETL`; the issuer exercised
  the gate and measured PERMIT for `0.7.0_AE_CloudOps` and REFUSE for `2.0.0_SA_COO~Z`,
  `0.2.0_DT_PortfolioAnalytics` and `0.9.0_WK_AMGT_RESAPP~122`. The commit and the apply are ROUTED to an AE seat
  through `0.0.0_AB_MSTR~Z`.

### BLAST RADIUS

What the act MAY move, and nothing else:

- **(B1) `EVTSA9VEHNZVH`'s ordered-behavior list: 28 -> 29.** One appended block, `path_pattern`
  `/api/scoped/amgt/*`, origin `APIGateway-portal`, caching DISABLED, one `viewer-request` association to
  `auth-validator-edge` (live version `:20`). The 28 existing blocks are untouched and keep their order; the append
  cannot shift precedence because the new pattern is disjoint from all 28.
- **(B2) What the 16 already-mounted amgt routes return at the edge.** Today every one returns the SPA shell
  (`200 text/html`, 1000 bytes). After the act they reach the portal API and return JSON -- **including `401
  application/json` for an unauthenticated request, which is the CORRECT post-state and is what the two control
  families already do.** A 401 is not a regression here; a 200 text/html is.
- **(B3) The distribution's `ETag`, `LastModified` and `Status`.** The apply returns after the update is accepted;
  the distribution then reads `Deployed`.
- **(B4) THE CLASSIFIED WAF READ-NORMALISATION NO-OP.** The portal-auth plan carries
  `aws_wafv2_web_acl.opal_cloudfront_protection` with 3 managed-rule blocks removed and 3 re-added, differing ONLY in
  the hidden `version` attribute (`''` vs `null`). It is a DURABLE read artefact of this root, not this cell's change,
  and its owner is `0.7.0_AE_CloudOps` per the CTO's durable item. **It is admitted to the bound and to this blast
  radius EXPRESSLY, exactly as the precedent's ruling admitted it, and the act must PROVE it is a no-op** (rule names
  identical both sides; all 6 visible fields per block diffed; ZERO differing fields; `get-web-acl` Rules JSON
  identical before and after, LockToken excepted).
- **(B5) Edge propagation.** A CloudFront update is global and takes time to propagate; a WARM EDGE may serve the
  prior answer briefly. A single post-apply read that still shows HTML is re-read once before being called a failure.

**NOT moved** (asserted by the order's AC1 and AC3):
- any of the 28 existing behaviors, their order, their origins, cache policies or Lambda@Edge associations;
- the default behavior and the SPA origin;
- `aws_cloudfront_function.spa_fallback` (measured clean today: disk 0 CRLF / 26 LF, identical to its HEAD blob);
- the WAF's actual RULES (B4 is a read artefact only -- if any rule's content moves, that is a ROLLBACK trigger);
- every origin, the viewer certificate, the geo restrictions and the distribution's aliases;
- the API Gateway `7k3ed8px20`, its 101 routes and the 16 amgt routes already mounted;
- `opal-amgt-scoped-api`, its code, memory, timeout, layers or env;
- the portal bundle and every S3 object;
- the served DATA for any security -- this act changes ROUTING, never content.

### WRITER CENSUS

- **The distribution's behavior list:** N = 1 writer in the repo,
  `infra/aws/terraform/portal-auth/cloudfront-distribution.tf:103` (`aws_cloudfront_distribution.portal`). The
  declared `path_pattern` count (28) EQUALS the live `CacheBehaviors.Quantity` (28), so no second writer has drifted
  the live list away from the file.
- **The auth attachment:** N = 1 rule, `local.auth_validator_edge_arn`, the same local every sibling scoped family
  references. This cell mints no function and pins no new version.
- **The amgt route table:** N = 1 writer, `infra/aws/terraform/harvest/scoped-amgt-api.tf`, and it is NOT touched --
  the routes already exist.
- **The act's own write set, one call deeper:** `terraform init` writes only the local `.terraform/` directory; the
  apply calls `UpdateDistribution` once and, per B4, `UpdateWebACL` once; the portal-auth state object is updated.
  0 S3 object writes outside the state backend; 0 IAM writes; 0 Lambda publishes.

### EXPECTED OUTCOME -- read from the rule and from the precedent, BOTH branches covered

- **The served CONTENT:** unchanged. No producer, no object and no adapter response body is touched.
- **The served ROUTING:** the 16 amgt routes stop returning the SPA shell. An UNAUTHENTICATED request returns
  `401 application/json` (the edge validator refusing), exactly as `/api/scoped/investor-reporting/*` did on the
  precedent's difference control. An AUTHENTICATED request from the page reaches the adapter, whose handler this seat
  measured healthy on 2026-09-22 (Lenovo and CAT both 200 with real payloads on a direct invoke, msg 24327).
- **Branch KEEP:** the plan conformed, the apply reports `0 added, N changed, 0 destroyed` with N matching the bound,
  the live behavior count reads 29 with exactly one amgt pattern LAST carrying the validator, BA_US_Equity then
  992_HK_Equity both return JSON (not HTML), and the two control families are unmoved. The behavior stays.
- **Branch ROLLBACK:** any trigger below fires. The behavior is REMOVED in a NEW commit and the SAME targeted apply
  runs; nothing is deleted and the distribution is never disabled.

### PER-KEY ROLLBACK

- **The behavior list:**
  1. a NEW commit removing the one appended block from `cloudfront-distribution.tf` (never a revert of history);
  2. the SAME targeted apply, run by the SAME routed AE seat;
  3. `get-distribution-config` must read the AC0 count (28) with the amgt pattern count back to 0, and the targeted
     plan must then read `No changes.` (modulo B4's durable WAF artefact);
  4. the same propagation window as B5 applies to the rollback.
- **The WAF (B4):** nothing to roll back -- it is a read normalisation. If its RULES moved, that is a rollback
  trigger for this act AND an immediate BLOCKING row to `0.7.0_AE_CloudOps`, because this cell does not own that
  resource.
- **Everything else:** not moved, so there is nothing to roll back. If the post-act read shows one moved, that IS a
  rollback trigger.
- **ROLLBACK TRIGGER (any one):**
  - the post-act behavior count is not AC0's count + 1, or the amgt pattern count is not exactly 1, or it is not LAST;
  - the new behavior's origin, cache policy or Lambda@Edge association differs from behavior 15's;
  - ANY of the 28 pre-existing patterns changed, moved or disappeared;
  - either control family (`/api/scoped/advisor-intelligence/*`, `/api/general/*`) stops returning
    `401 application/json`;
  - the WAF's `get-web-acl` Rules JSON differs before vs after (LockToken excepted);
  - an amgt path still returns `text/html` after the propagation re-read.

### NOT COVERED

The following are NOT covered by this half, and each needs its own pair:
- any SECOND behavior, or any edit to an existing behavior;
- a Lambda@Edge function change, publish or version re-pin (including `auth-validator-edge` itself);
- a WAF RULE change (as distinct from B4's classified no-op);
- an origin, certificate, alias or geo-restriction change;
- an API Gateway route, authorizer or integration change;
- any adapter code, memory, timeout or layer change;
- any portal bundle or frontend change -- in particular `Z-S227`'s missing `isError` branches;
- any S3 write or delete, and any distribution delete or disable.

**Signature (COO):** to be signed `2.0.0_SA_COO~Z` at the round-30 issuance (the issuance commit's hash is the
signature's vintage).
