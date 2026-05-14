# DT Session — P0 AuthContext audit-gap fix-forward (8b71292f)

**Author:** 0.4.0_DT_ClientPlatform
**Date:** 2026-05-14
**Driver:** Andrew empirical break post-DT-push → CTO P0 escalation
**Duration:** ~14:31Z – 14:40Z (~9min wall from break-discovery to push-live)

---

## Current State

**P0 RESOLVED via FIX-FORWARD (no revert executed).**

- Portal DEV: `8b71292f` LIVE (push: `d9882117..8b71292f`)
- Parent CLOUD: `cabf3d01d` LIVE (DE submodule bump `9766b6956` + AE 0.6.1 docs `cabf3d01d`)
- Both refs zero-diff vs origin
- Andrew dev-smoke unblocked

**SHARED.006 architecture intact.** No rollback. The destructive-op envelope (`--force-with-lease`) pre-granted by CTO went unused.

---

## Incident Timeline

| Time (Z) | Event |
|---|---|
| ~14:23 | DT push of 16-commit bundle landed on portal DEV @ `35e0adf9` + parent CLOUD @ `96fdd2e7f` (RAVC2 CLOSE) |
| ~14:28 | SHARED.005 `d9882117` push (1-commit follow-on, pure refactor; RAVC2 CLOSE) |
| ~14:31 | **Andrew empirical:** AdvisorIntelligence broken on DEV. Console: `[INFFIN#10] getClientsTab failed: SyntaxError: Unexpected token '<'... at JSON.parse` + `401` + `[auth/refresh] 401` |
| ~14:33 | CTO P0 MCP'd DT 0.4: hypothesis = SHARED.006 Commit C `46bfda8c` LAMBDA_FIRM_ID deletion. Pre-granted `--force-with-lease` revert envelope. |
| ~14:34 | DT RAVC1 ACK + diagnostic in flight. Accountability framing: pre-push L4 reviewer approval gap (DT reviewed `46bfda8c` on author's claim, did NOT run `comp-routes trace`). |
| ~14:36 | DT diagnostic surfaces: `?firm=` vs `?firmId=` two-pattern analysis. 8 `?firm=` S3-router callsites flagged as POSSIBLE culprit. CloudWatch 4xx rate pulled. Sent to CTO + DE + COO. |
| ~14:37 | DE 0.4 root-cause: **`AuthContext.tsx:35`** — internal Opal admin path had hardcoded `firmOverride = 'bd'`. Audit §G's literal-census scoping rule covered ONLY `src/pages/AdvisorIntelligence/` subtree; AuthContext lives in `src/contexts/`, outside census. Pre-Commit-C the `LAMBDA_FIRM_ID` map translated `'bd' → '49financial'`; post-Commit-C the api passes `'bd'` raw to Lambda → 401. |
| ~14:38 | DE ships `8b71292f` (1-LOC fix: `'bd' → '49financial'` + 4 JSDoc cleanups). Local typecheck PASS. |
| ~14:38 | CTO P0 RESOLUTION message: **FIX-FORWARD ratified**. Revert authorization rescinded. Standard non-destructive push of `8b71292f` authorized. |
| ~14:39 | DT typecheck (with cache reset) PASS. `git push origin DEV` `d9882117..8b71292f`. |
| ~14:39 | Parent CLOUD already covered by DE's `9766b6956` bump (authored + pushed in parallel with the hotfix commit). |
| ~14:40 | DT RAVC2 CLOSE to CTO + COO + DE with push hashes. |

**Break-to-resolve wall time: ~9 minutes.**

---

## Root Cause

```ts
// src/contexts/AuthContext.tsx:35 (pre-fix)
const firmOverride = internal ? 'bd' : undefined

// fix (8b71292f)
const firmOverride = internal ? '49financial' : undefined
```

`AuthContext` fires `prefetchAdvisorIntelligence` on every internal Opal admin session (warm-cache prefetch). Pre-SHARED.006 Commit C, the chain was:

```
AuthContext.tsx:35  firmOverride='bd'
  → api/endpoints/advisor-intelligence.ts L429  params = URLSearchParams({ firmId: LAMBDA_FIRM_ID[firmId] ?? firmId })
  → LAMBDA_FIRM_ID['bd'] = '49financial'
  → Lambda receives firmId='49financial' ✓
```

Post-Commit-C:
```
AuthContext.tsx:35  firmOverride='bd'  ← UNMAPPED CONSUMER
  → api/endpoints/advisor-intelligence.ts L429  params = URLSearchParams({ firmId })
  → Lambda receives firmId='bd' ✗  (not a valid DDB partition key)
  → Lambda returns 401
  → CloudFront custom_error_response 401/403 → 200 /index.html (HTML SPA shell)
  → frontend JSON.parse(HTML) → SyntaxError: Unexpected token '<'
```

---

## Diagnostic Retrospective (for ADVI_SHARED post-mortem)

### What worked

1. **CTO P0 escalation in <2min** of Andrew's empirical break — fast triage call to DE 0.4 + DT 0.4 parallel.
2. **DE 0.4's targeted grep at L4** — 3-min root-cause: `git grep "'bd'" src/` over the ENTIRE portal/src/ tree (not just AdvisorIntelligence/ subtree) caught AuthContext.tsx:35 immediately.
3. **Pre-granted destructive-op envelope** — CTO authorized `--force-with-lease` upfront so DT could execute revert without an authorization round-trip if needed. Envelope went unused (fix-forward chosen) but reduced theoretical-rollback latency to ~2min.
4. **Defense-in-depth diagnostics** — DT's `comp-routes behaviors` + `?firm=` callsite analysis + CloudWatch 4xx pull converged on the SAME mechanism (Lambda receives bad firmId → 401 → HTML masquerade) even though it targeted a different culprit-surface than DE's hit. Two independent paths corroborating the mechanism reduced time-to-confidence on root cause.
5. **Fix-forward over revert** — 1-LOC AuthContext patch beats 4-commit surgical revert + force-push. Preserves entire morning's ship pile (16 commits + SHARED.005).

### What needs fixing

1. **L4 pre-push reviewer protocol gap.** DT 0.4 reviewed `46bfda8c` (Commit C) pre-push on the author's claim ("zero behavior change at Lambda boundary") plus a read of the canonicalization sequence (A+B canonicalize upstream → C deletes now-identity translation). DT did NOT independently:
   - Run `comp-routes trace` on a representative Lambda-boundary endpoint
   - Invoke `git grep -rE "firmOverride.*=.*['\"](inf|bd)['\"]" portal/src/` across the FULL portal source tree (not just the file being changed)
   - Probe AuthContext-tier prefetch consumers
   The author-claim review pattern works for refactors with closed in-file scope; it fails for Lambda-boundary refactors with cross-tree consumers.

   **Protocol delta (CTO will write into post-mortem):** Lambda-boundary-touching refactors require comp-routes trace + Lambda invocation test + cross-tree literal grep as MANDATORY L4 reviewer steps. The existing TO `<compiler_tools_mandate>` block needs an "L4 cross-domain review supplement" for any commit that touches `src/api/endpoints/` OR `infra/aws/lambda-edge/` OR `infra/aws/lambda/`.

2. **Audit §G scoping gap.** SHARED.006 audit literal census was scoped to `src/pages/AdvisorIntelligence/` subtree (where the firmId rename impact was expected to concentrate). `AuthContext.tsx` lives in `src/contexts/` — outside the census. The audit found the right literals in the right places but missed an unmapped CONSUMER calling INTO those literals from outside the subtree.

   **Audit protocol delta for future canonicalization PRDs:** literal-census-by-subtree must be paired with cross-tree-consumer-discovery (`git grep -rE "{old_literal}" portal/src/` outside the subtree). If a consumer outside the subtree references the old literal, it gets ADDED to the rename scope before Commit-A ships.

3. **CloudFront custom_error_response 401/403 → 200 /index.html masking.** The HTML masquerade made the symptom presentation harder (`JSON.parse` error in the frontend rather than a clean 401 in the network tab). DT's `comp-routes behaviors` output already flagged this as a WARN; the bug class is well-known but the masking still cost diagnostic time.

   **Possible follow-up (separate scope):** CF behavior rule — preserve 401/403 status code on JSON-content-type paths (`/api/*`); only rewrite-to-200-HTML on SPA-routing paths (`/`, `/dashboard`, etc.). Requires Lambda@Edge routing-by-path classification; non-trivial. File as ADHC if appetite.

### What was banked but didn't matter

DT's `?firm=` vs `?firmId=` two-pattern analysis correctly identified the L75-comment mechanism (S3 router uses bucket-suffix `inf/bd`; Lambda DDB uses canonical `inflection/49financial`) but landed on the WRONG culprit surface (8 `?firm=` S3-router callsites in api/endpoints). All 8 of those callsites were actually FINE because their input `firmOverride` came from canonicalized-by-A+B sources. The actual culprit was a single 9th consumer in a different file. Banking this for the post-mortem under "mechanism-correct, culprit-wrong" diagnostics — useful for ruling things in/out but not sufficient on its own.

---

## Verification

**Portal DEV remote state at session end:**
- `git ls-remote origin DEV` -> `8b71292fcd738fe18c3e673a01b8b1c1d72cebb4`
- Local `DEV` rev-parse identical
- Zero-diff

**Parent CLOUD remote state at session end:**
- `git ls-remote origin CLOUD` -> `cabf3d01dab688e58662b11d972267ceb0`
- Local HEAD rev-parse identical
- Submodule pointer `portal` = `8b71292f`
- Zero-diff

**Andrew dev-smoke unblocked.** Browser hard-refresh post-push should resume INFFIN v0.1 close validation against the remote DEV state.

---

## Next Steps

- [Andrew] Resume dev-smoke. Validate: P0 Cash hotfix (was already in the previous push), INFFIN Surface #2 platinum data (gated on chain #131842 recovery wrap), INFGRO.005 GRO hero cards, SHARED.006 canonicalization-driven dispatch.
- [CTO] Author post-mortem on L4 pre-push reviewer protocol delta (Lambda-boundary touching refactors require comp-routes trace + cross-tree literal grep as mandatory L4 reviewer steps).
- [COO] Add audit-protocol delta to ADVI_SHARED retrospective: literal-census-by-subtree must be paired with cross-tree-consumer-discovery for canonicalization PRDs.
- [DT/CTO future] CF behavior rule: preserve 401/403 status code on JSON-content-type paths to remove the HTML-masquerade diagnostic friction (file as ADHC if appetite).
- [DT 0.4] Standing by for SHARED.007/.008 / INFINC Phase 2 / FIRMSEP.10 Cottonwood / PROD-promote signal.
