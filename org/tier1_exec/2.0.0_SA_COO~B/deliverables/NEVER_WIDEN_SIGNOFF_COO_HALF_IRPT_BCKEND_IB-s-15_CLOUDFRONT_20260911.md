# NEVER-WIDEN SIGN-OFF -- COO HALF -- IRPT_BCKEND IB-s-15, the one CloudFront behavior plus the classified WAF no-op

**Signer:** `2.0.0_SA_COO~B`, issuer of `IRPT_BCKEND.TO-IB-s-15` (round holder). **Counterpart:** the CTO half, `1.0.0_SA_CTO` msg 95933 (2026-09-11 09:33Z), as the gate over the `portal-auth` root (D0 s.6). **Act signed:** ONE `safe-apply` of `infra/aws/terraform/investor-reporting/../portal-auth` (root `infra/aws/terraform/portal-auth/`) by `0.9.0_WK_IRPT_BCKEND~2` under IB-s-15's cloudfront ledger entry. **Rows:** `IRPT_BCKEND-W2-S12`, `IRPT_BCKEND-S22`, `IRPT_BCKEND-S23`.

## Blast radius (what the act MAY touch), key by key

| key | change | rollback |
|---|---|---|
| `aws_cloudfront_distribution.portal` (EVTSA9VEHNZVH) | gains exactly ONE `ordered_cache_behavior` for `/api/scoped/investor-reporting/*` -> origin `APIGateway-portal`, caching disabled, one `viewer-request` association to `auth-validator-edge:19`, appended LAST so no existing precedence shifts; the prior 27 behaviors, origins and settings unchanged | delete the block, re-apply; 28 -> 27, the 27 identical |
| `aws_wafv2_web_acl.opal_cloudfront_protection` | an `UpdateWebACL` whose rule set is CONTENT-IDENTICAL to the live one (six rules; the three managed-rule statements differ only in `version` `""` vs `null`, a hashicorp/aws 5.100.0 read normalisation the CTO pinned by `terraform show -json`, `get-web-acl` and a state pull, serial 173); WAF propagation is atomic, no request is unprotected during it | the same config re-applied is the same no-op; nothing to reverse |
| `aws_cloudfront_function.spa_fallback` | NOT in the plan once the worktree renders the file LF (b9b3eafb6b adds `infra/aws/terraform/**/*.js text eol=lf`); if it appears in the plan, the act STOPS -- it is not signed | n/a |
| anything else in that plan | NOT SIGNED; a STOP and a BLOCKING row | n/a |

## Writers of the named properties (counted, per CLAUDE.md NEVER-1)

- `ordered_cache_behavior` list on the distribution: **1 writer**, this root (`cloudfront-distribution.tf`). No other Terraform root, script or schedule writes it (IB-s-15's Phase-1 read; the 14 existing scoped routes are API Gateway resources, not behaviors).
- WAF rule set: **1 writer**, this root. CloudTrail `UpdateWebACL` since 2026-08-28: three events, all 2026-09-03, all CloudOps~S opsec applies (CTO half, measured). Both halves read the same producer's rule; N=1 printed here.

## Expected outcome, read from the producer's rule, both branches

- Branch A (the plan reads `0 to add, 2 to change`: the distribution + the WAF): the apply lands the behavior and the no-op. Verification the worker MUST print BEFORE the flip: `get-distribution-config` behaviors 27 -> 28, the one new path present, the prior 27 unchanged IN ORDER (diff of the pattern list = one appended line); `get-web-acl` `Rules` JSON identical before and after with `LockToken` excepted (diff empty); the root then plans `0 to add, 1 to change` (the WAF read artefact recurs on every plan until the provider is bumped -- the CTO's durable item 4) or clean.
- Branch B (the plan reads anything else -- a third resource, a removed behavior, a WAF rule with a non-`version` difference): NOT COVERED by this sign-off; the worker STOPs, `safe-apply` is not invoked, and the row is re-armed with the new plan verbatim.

## What this does not cover

- No other root, no other distribution setting, no origin, no existing behavior, no existing scoped route, no edge function version.
- The durable provider bump on `portal-auth` (CTO item 4, owner `0.7.0_AE_CloudOps`, gate CTO) is not this act.
- The round's other BLOCKING item (W1-S8, the first-mint bundle) is unrelated and unchanged.

Signed at HEAD after 95933; both halves on record -> the apply is IB-s-15's own act through `.tools/safe-apply.sh` under its ledger, no rework. Push state: LOCAL (this seat never pushes; LD-0522).
