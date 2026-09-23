# Opal and partner directory context candidate

Authority: CTO `LOCAL_LIVE_PARTNER_SCOPE_20260923.md`, CONTRACT.md and
13:23:33Z design admission. Candidate only: no cloud apply or promotion.

The directory bootstrap now admits an explicit `selected_tenant=global` request
only for an authenticated edge subject with verified CloudFront origin and the
existing aggregate gate predicate: JWT firm `opal-capital` OR user type `Dev`.
Renderer principals remain excluded. Partner admin alone grants no Global or
foreign-firm access. The boundary evaluates each invocation separately and passes
the eligible subject through a request-local resolver roster; the warm Entry's
roster is never changed. No static email list or new identity service exists.

Identity freshness remains the current edge signature/expiry verification contract.
This does not claim immediate revocation of an otherwise unexpired identity token.
Directory, ownership and entitlement artifacts are still read by the actual guard.

## Wire

- `selected_tenant` is registry intent, accepted in query or body. Conflicting
  carriers refuse before artifact reads. Every restated firm must agree.
- Global is valid only for directory resolve. Its response has `firm_id: global`
  and `data.context_kind: GLOBAL`; this is a context marker, not an opaque firm ID.
- Each context member states tenant, READY/UNAVAILABLE, an actual guarded
  ResolvedScope or null, and a reason. COMPLETE/PARTIAL/UNAVAILABLE records whether
  every configured tenant resolved. Failed firms are retained explicitly.
- Single-firm scopes preserve issued opaque identity and add `registry_tenant`.
  Global never mints a union account-set or a scope for downstream reports.
- Browse/selection/report requests carry the selected registry tenant separately
  from opaque IDs. Selection intent belongs in the query for strict domain bodies.
- Existing retained selection references remain content-bound references, not
  bearer grants. Every use rechecks the current principal's entitlement, directory
  revision and tenant. Browser confirmation/cache state is identity-bound.

The authoritative possible-tenant list is the existing Terraform registry-derived
`IRPT_DIRECTORY_BUCKET_MAP`; no browser list controls which buckets are read.
No new route, environment member, IAM grant or edge rewrite is proposed.

## Checks so far

- 13 new actual warm-Entry controls pass: Global/per-firm, Dev, partner admin
  negatives, subject/origin/renderer negatives, explicit partial outcomes,
  conflicting selectors, cursor tenant/principal changes and accepted selection.
- Existing bootstrap/browse/selection controls pass (28 tests).
- Baseline shared-auth suite at `69d50fbd64` independently reproduced five failures:
  two legacy directory positive fixture failures and three stale route-count
  assertions (12 expected; 14 guarded routes actual). 173 baseline tests pass.
  The candidate shared-auth run retains those same five failures; no blanket PASS.

Packaging and paired browser evidence are recorded in the final handoff. Changes
to shared served.py require explicit dependency repins in each selected consumer
artifact; changing directory source alone cannot update report Lambdas.
Current-owner prospect/history rules remain unchanged and do not acquire a new
Opal ownership grant from this directory repair.
