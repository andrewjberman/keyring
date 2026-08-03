# MDLP_MONPUB.W9b: opal-scoped-advisor-by-firm DefaultTTL 86400 -> 60 -- DEPLOYED + verified

**archetype:** DEPLOY
**secondary_archetypes:** DIAGNOSE

**Serial:** `0.7.0_AE_CloudOps~F` -- Window: 2026-08-03T17:12Z-1725Z
**Authorization:** CTO widening GO 171214Z + three-verdict amendment 171327Z (no TO file; the
CTO messages are the tasking record, filed in my inbox read/). Same MDLP_MONPUB family,
Andrew-watched (ST removed from Bloomberg at source per Andrew ~17:05Z at CTO terminal;
caching/monotonicity family continues through fix).

---

## The discriminating check (CTO amendment: ground the REFRESH CONTRACT, three verdicts)

**VERDICT (a) -- config-disagreement.** Grounded:

- `shared-advisor-router-response` STAMPS `Cache-Control: public, max-age=60, must-revalidate`
  on every 2xx artifact response (`index.mjs:169-171`); the `isArtifact` gate (`:122-126`)
  matches the REWRITTEN `/gold/*` + `/platinum/*` key forms ending `.json` -- i.e., the entire
  designed data path of these behaviors. (The gate's history is itself the caution: matching
  only `/api/scoped/` once made the whole handler a production no-op, caught by live smoke
  2026-06-11 -- recorded in-source.)
- Deployed == repo: attached version `shared-advisor-router-response:4` has CodeSha256
  `ZVtzzi4VSEF+...` == `$LATEST` (list-versions-by-function). Live invocation 17:09:57Z
  (stream `2026/08/03/[4]1993e...`, clean START/END/REPORT, no firm-guard error).
- Verdict (c) [24h-is-the-designed-contract] is STRUCTURALLY EXCLUDED: the stamp overrides
  DefaultTTL on every designed-path response, so 24h cannot be the operative refresh contract.
  DefaultTTL 86400 was dead config on the designed path and a 24h staleness trap on any
  unstamped one -- the same class W9 closed on /api/general/*.

**Blast radius denominator (live get-distribution-config): exactly 4 behaviors** use policy
`45eb7514` -- `/api/scoped/advisor-intelligence/{artifacts/*/*, artifacts/*, entities/*/*,
*.json}` -- all in scope; the policy is shared with nothing else. **Corrects my own "5" in the
1710Z flag to CTO** (denominator discipline: the 5 was recalled, the 4 is measured).

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Discriminating check | Verdict (a); evidence above |
| 2 | TF edit | `cloudfront.tf` `opal_scoped_advisor_by_firm` `default_ttl` 86400 -> 60 ONLY; cache-key params (X-Firm-Id + firm query whitelists, firm-isolation load-bearing) untouched; W9b comment block added |
| 3 | Plan gate | `0 to add, 1 to change, 0 to destroy` -- policy in-place, ZERO distribution changes; saved w9b.tfplan |
| 4 | Commit before apply | `c6f8eaf9e8` (safe-commit -F) |
| 5 | safe-apply w9b.tfplan | comp-tagauthz PASSED, tombstone CLEAN, applied |
| 6 | 0-diff re-plan | `No changes.` |
| 7 | Live verify | Policy 45eb7514 live: DefaultTTL 60 / Min 1 / Max 31536000; Headers whitelist [X-Firm-Id] + Query whitelist [firm] INTACT |
| 8 | Tag | `portal-auth-v1.22.0` on c6f8eaf9e8; push leg to MSTR (integrator discipline) |

## Deployment Tags

| Pipeline | Tag | Commit |
|---|---|---|
| portal-auth | portal-auth-v1.22.0 | c6f8eaf9e8 |

## Verification (actual output)

```
$ aws cloudfront get-cache-policy --id 45eb7514-712c-42c5-9fd6-40909b9f0347
{ "Name": "opal-scoped-advisor-by-firm", "DefaultTTL": 60, "MinTTL": 1, "MaxTTL": 31536000,
  "Headers": whitelist ["X-Firm-Id"], "Query": whitelist ["firm"] }     <- params INTACT

$ terraform plan (post-apply)
No changes. Your infrastructure matches the configuration.
```

**Named residual (same shape as W9, same honesty):** an authenticated end-user GET observing a
2xx with the max-age=60 header + Age cycling under 60s was not exercisable from this seat (the
behaviors sit behind the JWT gate; bare probes short-circuit at the validator). Covered by:
stamp at source on the deployed-SHA-matched version + live invocation + the in-source 06-11
live-smoke record + config DefaultTTL 60 read live. A token-holding seat (DT's W6 exercise, or
any portal session hitting Advisor Intelligence) closes it end-user-side for free.

## Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| terraform plan (gate) | -out=w9b.tfplan | PASS: 0/1/0, policy-only, zero distribution changes |
| safe-apply (comp-tagauthz + tombstone-gate) | apply w9b.tfplan | PASS both gates; applied clean |
| 0-diff re-plan | post-apply | PASS: No changes |

comp-routes/comp-blast not re-run: the behavior/policy topology was grounded live 40 minutes
ago in W9's Phase 1 (same distribution, same session, live get-distribution-config re-read
fresh for the 4-behavior denominator here); the known cache-policy coverage gap is already at
CVO. No new boto3/IAM surface (config-only TTL change).

## MCP traffic

3 significant this window: CTO widening GO ack (171305Z); CTO amendment received 171327Z
(three-verdict, adopted); close evidence to CTO + COO (next message, cites this log's hash).

## Blockers

None. Push leg at MSTR (routed).

## Current State (zero-context handoff)

- LIVE: policy 45eb7514 (opal-scoped-advisor-by-firm) DefaultTTL 60; the 4 advisor-intelligence
  S3 behaviors' effective TTL regime now config+stamp-agreed at 60s; firm-isolation cache-key
  params untouched; 0-diff. Cache-policy updates propagate without a distribution redeploy.
- Repo: c6f8eaf9e8 + this log local on CLOUD; tag portal-auth-v1.22.0; push pending MSTR.
- W9 family status: W9 CLOSED (COO 171132Z), W9b deployed+verified (this log), both residuals
  (Age observation, W9 + W9b) converge on the same closure path: any authenticated header
  capture, DT's W6 exercise being the first scheduled one.

## Next Steps

1. **[0.0.0_AB_MSTR]** Push leg: CLOUD + portal-auth-v1.22.0 --follow-tags.
2. **[1.0.0_SA_CTO + 2.0.0_SA_COO]** W9b close evidence (message follows this commit).
3. **[0.2.0_DT_PortfolioAnalytics]** W6 header capture now closes BOTH residuals (60s here,
   300s on /api/general/*) in one pass -- noted in the close message.
