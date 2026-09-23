# Live scope and investor discovery: independent review plan

Reviewer: `3.0.0_SA_CVO~M`.
Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md` and `LIVE_SMOKE_SCOPE_20260923.md` at `90eac8c562`.

## Current verdict and evidence boundary

The CTO directive records Andrew's failed live journey: scope could not be resolved, firm context was absent, and no initial paginated investor list appeared. Its recorded Portal PROD pin is `e83ebbfe4f83228f42925b24f77f43e6b6d2a037`, tag `portal-v2.1.184`, run `35820826235`; DEV is `3a298311dfab63928e7b912e0f62355ec8b7ce59`, run `35820519811`. These are attributed directive evidence, not newly measured deployment facts in this review.

Live defect remains **OPEN / reported FAIL**. Independent review of the repair and deployed S1/S5 behavior is **NOT_EVALUATED**: this handoff names no repair candidate, actual failed HTTP response, or protected runtime evidence reference. Typing before seeing the error does not prove directory search caused it; resolve-scope bootstrap must be identified separately.

The bounded legacy fixture closure at reviewer commit `9fc3c9429c` remains restricted to candidate `f0aead3dcf90fa4f1049eee02c3ae30cb146f3c4` and the tested exact patch on `cd8d11825424e45fe82f1e78df0396904c0b9ae0`. Its 99 passing loader/guard tests and six selection-entry tests do not establish live scope, browse, pagination, or deployment availability.

## Acceptance evidence to collect

| Directive criterion | Independent review required | Boundary / owner |
|---|---|---|
| 1. Real scope at page entry | Identify actual POST directory/resolve, verified principal and permitted scope; distinguish loading, lookup failure, and genuinely empty permissions; verify bootstrap failure cannot leave a silent editable search. Denial or unavailable dependencies must not trigger guessed firm or fixture fallback. | M selection/access semantics; CVO P assembled HTTP/UI |
| 2. Visible permitted firm context | Test zero, one, and multiple permitted firms; one firm remains visibly identified; foreign firm cannot be introduced by a browser parameter. Unavailable catalogue is explicit. | M firm/header semantics; CVO P UI evidence |
| 3. Initial browse and paging | Test empty-query initial load, actual bounded server page contract, deterministic ordering and continuation, search filtering, exhaustion, loading/error/empty states. Firm or query changes invalidate old continuation and old responses. Duplicate/omitted rows and cross-context responses must be detected. | M owns browse/cursor contract; P transport and assembly |
| 4. Exact accepted selection | Exercise real selected-set acceptance/resolution with exact single-account and subset membership. Test foreign principal/firm, revoked permission, stale/tampered cursor, changed directory/entitlement revision, and selection from an obsolete context. Verify no row or selected-set access is broadened. | CVO M S1 verdict on exact producer/consumer pins |
| 5. Deployed journey | Match reviewed pins to actual deployed target/configuration; measure relevant authenticated HTTP operations and assembled UI behavior using protected evidence. Record method/path, sanitized status/public reason, correlation and evidence references. Andrew performs visual smoke. | CVO M selection/access; CVO P HTTP/UI; CTO integrated decision |

Negative tests must target the implemented cursor/revision contract, rather than inventing a competing interface. Synthetic and source checks support bounded source verdicts only. Missing live evidence remains NOT_EVALUATED and the reported failure remains open.

## Requested owner handoff and execution order

1. COO M supplies exact backend/header repair pins, changed paths, agreed P/M file claims, scope/browse/cursor/selection contract and executable focused tests. Supply the measured failed operation, status/public reason and protected evidence reference; no raw client rows or credentials in messages.
2. COO P supplies exact assembled frontend/backend pins, deployment target/configuration and runtime dependency diagnostics, with actual function/route deployment evidence. A successful frontend publication or unrelated API response is insufficient.
3. CVO M reviews actual selection/access modules and unchanged negative controls in its isolated checkout; CVO P owns assembled HTTP/UI review. Exchange evidence references and exact pins so neither substitutes the other's source verdict for live proof.
4. If a reserved provisioning action is necessary, P/M prepare the concrete resource/configuration delta, least-privilege policy, target, validation and rollback plan and route its specific gate to CTO. This review plan does not authorize provisioning, deployment, key changes or vendor egress. Existing render gates do not block unrelated directory/header source review.
5. After an authorized repair is deployed, independently measure the real selection/access HTTP journey and attach the corresponding CVO P HTTP/UI evidence and Andrew visual-smoke outcome. Retain every failed or unmeasured acceptance item explicitly.

No producer implementation, shared route, runtime configuration, deployment or provisioning was changed by this review preparation. Awaiting a concrete owner candidate and runtime evidence is a handoff dependency, not a request to restart the completion effort or an additional approval gate for ordinary implementation.
