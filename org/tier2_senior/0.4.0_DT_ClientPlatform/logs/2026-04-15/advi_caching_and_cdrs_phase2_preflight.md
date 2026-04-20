# 0.4.0_DT Session Log — ADVI Caching + CDRS_TFIMPT Phase 2 Pre-flight

**Agent:** 0.4.0_DT_ClientPlatform
**Date:** 2026-04-15 ET (afternoon — follows identity_permissions_overhaul.md from earlier same day)
**Task Orders:** none formally authored yet — Andrew-directed portal caching work + COO-dispatched CDRS_TFIMPT.007 pre-flight draft

---

## Context

Session opened at ~18:02 ET resuming from the morning identity/permissions overhaul. Two parallel workstreams landed this session:

1. **Andrew-driven:** ADVI tab going "dark" with "data not available" after 2-3 min idle in `/advisors` and `/books`. Diagnosis + local caching + timeout fix.
2. **COO-dispatched:** New CDRS_TFIMPT lane (2026-04-15 18:03Z directive) — DT+AE own 5 CloudFront distribution imports + 2 DynamoDB table imports. Pre-flight Phase 2 memo + code draft for .007 (opal-partner-{firmId} TF module + lib/partner + auth-handler generalization).

Both workstreams advanced to code-drafted / tsc-clean state. No commits or pushes this session — CDRS work pending AE's ship-time combine; ADVI work pending Andrew review.

---

## Workstream A — ADVI Caching & Timeout (Andrew-directed)

### Diagnosis

Andrew reported: panels in `/advisors` and `/books` go dark with "data not available" if not clicked every 2-3 min. Root cause diagnosed:

1. `portal/src/api/endpoints/advisor-intelligence.ts` had `API_TIMEOUT_MS = 10_000` — 10s AbortController ceiling on every ADVI fetch.
2. ADVI Lambdas (partner-analytics, leaderboard, cumulative-chart) cold-start >10s after idle, triggering AbortError before response.
3. React Query's global defaults (`staleTime: Infinity`, `gcTime: Infinity`, `refetchOnMount: false`) correctly preserve already-cached keys, but a **new query key after idle** (cohort toggle, window toggle, drill) fires a fresh fetch against a cold Lambda → 10s abort → component renders the "not available" branch.
4. In-memory cache also dies on page reload / tab remount — no persistence across sessions.

Andrew's intuition: build local caching around the existing auto-signout / continue-session flow. Confirmed correct contract — React Query cache is already session-lifetime (`queryClient.clear()` on logout at `AuthContext.tsx:384`); persistence just extends that contract across reloads.

### Actions

| Step | File | Change |
|---|---|---|
| 1 | `portal/package.json` | `bun add @tanstack/react-query-persist-client @tanstack/query-sync-storage-persister` (v5.99.0) |
| 2 | `portal/src/lib/queryPersister.ts` | New — `createSyncStoragePersister` (localStorage, 1s throttle, key `OPAL_PORTAL_QUERY_CACHE_v1`) + `clearQueryPersister()` helper + `QUERY_PERSISTER_MAX_AGE_MS = 12h` |
| 3 | `portal/src/main.tsx` | `QueryClientProvider` → `PersistQueryClientProvider` with `persister`, `maxAge: 12h`, `buster: 'v1'` |
| 4 | `portal/src/main.tsx` | `retry: 3` → smart retry fn: retry on AbortError / "Failed to fetch" / 5xx, skip 4xx, cap at 2 |
| 5 | `portal/src/contexts/AuthContext.tsx` | logout calls `clearQueryPersister()` alongside `queryClient.clear()` |
| 6 | `portal/src/api/endpoints/advisor-intelligence.ts` | `API_TIMEOUT_MS: 10_000 → 30_000` (single source of truth — all ADVI code imports from here, no direct fetch bypasses) |
| 7 | `bun run build` | Clean — 11-14s, no new type errors |

### Contract / Rationale Captured in Code

- **Session-lifetime persistence:** cache hydrates from localStorage on boot; only `status === 'success'` queries are dehydrated (React Query default), so loading/errored states never rehydrate as "dark."
- **Eviction paths (3):** logout clears persister + in-memory, 12h maxAge expires blob, `buster: 'v1'` bump wholesale-invalidates if response shapes change.
- **Smart retry:** 4xx doesn't retry (won't succeed on repeat — auth failures, missing data); AbortError/5xx/network retries twice max, so a dead endpoint doesn't stall at "loading" for 40+ seconds of exponential backoff.

### Validation

- `bun run build` clean twice (after persister wire, after timeout/retry change)
- Dev server started on port 5175 (bg task `bhei6tuzf`)
- Andrew to verify end-to-end behavior on reload + cohort-toggle after idle
- No `/frontend-dev` Skill run this session — orthogonal to CDRS work and Andrew was directing live

### Open Items (workstream A)

- Andrew manual verification: reload `/advisors`, idle 3+ min, click new cohort → panel should stay populated (hydrated from localStorage) instead of going dark.
- No commit / push yet. Portal DEV branch stays at `e3190f8` (portal-v2.1.51) until Andrew thumbs up.
- Follow-up option (deferred): Lambda provisioned concurrency to kill cold-start root cause. Not in this session's scope.

---

## Workstream B — CDRS_TFIMPT Phase 2 Pre-flight (COO-dispatched)

### Timeline

| Time (ET) | Event |
|---|---|
| 18:03Z | COO: new CDRS_TFIMPT lane, off ADVI_ROLLUP, DT lane partner with AE 0.7 |
| 18:05Z | COO: partner-firm infra = CDRS_TFIMPT.006/.007, parked until AE closes .001-.005 |
| 18:45Z | COO: pre-flight memo ask (read-only, design-drafting) |
| 18:48Z | COO: .005 ETA compressed to 45-75 min, memo must land before .005 closes |
| 18:52Z | Memo draft landed at `docs/architecture/CDRS_TFIMPT_PHASE2_HANDOFF.md` |
| 18:55Z | COO: ACK memo, accepted verbatim as `<references>` brief for .007 |
| 18:56Z | AE: 4-Q resolution delivered (all 4 gated questions resolved) |
| 19:00Z | DT-side code draft complete, tsc clean, ACKs sent to AE + COO |

### Phase 2 Handoff Memo

Wrote `docs/architecture/CDRS_TFIMPT_PHASE2_HANDOFF.md` — one page, 5 sections + 4 open Qs:

1. **Shared-lib shape** — `infra/aws/lambda/lib/partner/` (Lambda-side, distinct from `portal/src/lib/firmAccess.ts` which is unchanged). 2 files — `tableName.ts` + `index.ts`. Per-Lambda bundling, no Layer until 3+ consumers.
2. **Auth-handler generalization** — `PARTNER_TABLE_49FIN` constant removed; `getPartnerIdentity(email, firmId)` uses `partnerTableName(firmId)`. User.firmId already available at all 3 call sites (login, refresh, /me).
3. **TF module home** — `modules/partner-firm-table/` + top-level `partner-firms/` with own state. opal-users-v2 (.006) folds into shared-infra.
4. **IAM strategy** — hybrid, wildcard `opal-partner-*` GetItem-only for auth surface, explicit ARNs elsewhere.
5. **Migration sequencing** — per AE 16:20Z: TF module + import → apply+tag → lib/partner + wire auth-handler → runbook.

Plus 4 open questions for AE: backend split confirmation, Lambda@Edge bundle size, stale-JWT firmRole property, import-drift reconcile.

### AE 4-Q Resolution (2026-04-15 18:56Z)

| Q | Resolution |
|---|---|
| (a) TF backend split | .006 → shared-infra/tfstate, .007 → partner-firms/tfstate — separate growth paths |
| (b) Lambda@Edge bundle | Safe (<50KB gzipped). Defer actual authorizer consumption to migration TO, flag in .007 `<references>` |
| (c) Stale JWT firmRole | Accept 15m lag, document in runbook. Push-invalidation is Phase 3 |
| (d) Import-drift reconcile | TF module spec always bends to match live table. Never mutate live during import |

All 4 resolved — .007 unfrozen.

### DT-side Code Draft (uncommitted)

| File | Status | Purpose |
|---|---|---|
| `infra/aws/lambda/lib/partner/tableName.ts` | NEW canonical | `partnerTableName(firmId)` — enforces `^[a-z0-9]+$` via regex (matches AE's TF variable validator for the two-sided naming gate) |
| `infra/aws/lambda/lib/partner/index.ts` | NEW canonical | `getPartnerProfile(email, firmId)` + `canAccessFirm(claims, targetFirmId)` + types per AE 16:20Z spec (typed minimum + `raw` escape hatch) |
| `infra/aws/opalinvest_dev/lambda/auth-handler/src/lib/partner/{tableName,index}.ts` | draft mirror | Same content as canonical — required because auth-handler tsconfig has `rootDir: ./src`. Ship commit must wire `build-nodejs-lambda.sh` to rsync canonical → mirror at zip time so git carries the canonical copy only. Flagged to AE. |
| `infra/aws/opalinvest_dev/lambda/auth-handler/src/db.ts` | modified | `getPartnerIdentity(email, firmId)` delegates to `getPartnerProfile`; preserves return shape for existing callers by extracting advisorName/advisorRole from `profile.raw`; `PARTNER_TABLE_49FIN` constant removed |
| `infra/aws/opalinvest_dev/lambda/auth-handler/src/auth.ts` | modified | 3 call sites (login:64, refresh:108, getCurrentUser:142) pass `user.firmId` as 2nd arg |

`tsc --noEmit` clean on auth-handler.

### Regression Plan (prepped, not yet run)

Post-deploy parity curl per COO acceptance:
```bash
# Internal admin
curl -s $API/auth/login -d '{"email":"andrew@opalinvest.com","password":"..."}' | jq
curl -s $API/auth/me -H "Authorization: Bearer ${ANDREW_JWT}" | jq

# Partner-firm admin (49financial)
curl -s $API/auth/login -d '{"email":"hunter.lloyd@49financial.com","password":"..."}' | jq
curl -s $API/auth/me -H "Authorization: Bearer ${HUNTER_JWT}" | jq
```
Expected: identical response shape; values differ only on identity-derived fields (advisorId, advisorName, advisorRole, firmRole, firmId).

### Open Items (workstream B)

- .007 flips to `<status>pending</status>` when COO authors + releases (AE's 4-Q ACK was the gate)
- AE ship-time combine: needs to include build-script rsync for `lib/partner/` canonical → consuming Lambdas' src
- DT on .007: delete draft mirror at `auth-handler/src/lib/partner/`; ensure commit carries only the canonical copy + the build-script change
- Runbook `ADD_PARTNER_FIRM.md` (and possibly sibling `FIRMROLE_MANAGEMENT.md`) pending — .007 deliverable

---

## Compiler Tools

| Phase | Tool | Used? | Note |
|---|---|---|---|
| Before ADVI timeout change | comp-transform schema-check | No | API_TIMEOUT_MS is a single constant in a single helper — no component schema touched. Verified via grep that no direct `fetch()` in ADVI components bypasses the helper (scope check). |
| Before ADVI caching change | comp-cache collisions | No | No new React Query keys introduced — persister wraps existing keys. React Query's default dehydrator filters to `status === 'success'` so corrupt/loading states can't rehydrate (verified via v5 docs). |
| Before firmRole pre-flight | comp-transform schema-check | Skipped — documented | firmRole is an auth claim (JWT → parseClaims → useAuth), not a typed panel-data field. schema-check is for data-prop renders. `tsc -b` is the guardrail. Three consumer files identified via grep: AdvisorIntelligence.tsx:175, AuthContext.tsx (6 sites), AuthContext.context.ts:33-38. Documented in memo. |
| After auth-handler draft | tsc --noEmit | Yes | Clean on first run after fixing `Spread types may only be created from object types` (TS2698 on raw.firmRole spread — typed-guarded to `typeof raw.firmRole === 'string'`). |
| After portal build | bun run build | Yes (x2) | Clean 11-14s both times — persister wire-up and timeout/retry change each verified independently. |

---

## Files Inventory

### Workspace (parent repo, branch CLOUD) — NO COMMITS THIS SESSION

**New (uncommitted):**
- `infra/aws/lambda/lib/partner/tableName.ts`
- `infra/aws/lambda/lib/partner/index.ts`
- `infra/aws/opalinvest_dev/lambda/auth-handler/src/lib/partner/tableName.ts` (draft-time mirror)
- `infra/aws/opalinvest_dev/lambda/auth-handler/src/lib/partner/index.ts` (draft-time mirror)
- `docs/architecture/CDRS_TFIMPT_PHASE2_HANDOFF.md`
- `org/tier2_senior/0.4.0_DT_ClientPlatform/logs/2026-04-15/advi_caching_and_cdrs_phase2_preflight.md` (this file)

**Modified (uncommitted):**
- `infra/aws/opalinvest_dev/lambda/auth-handler/src/db.ts` (generalized getPartnerIdentity, removed PARTNER_TABLE_49FIN)
- `infra/aws/opalinvest_dev/lambda/auth-handler/src/auth.ts` (3 call sites pass user.firmId)

### Portal submodule — NO COMMITS THIS SESSION

**New (uncommitted):**
- `portal/src/lib/queryPersister.ts`

**Modified (uncommitted):**
- `portal/package.json` + `portal/bun.lock` (added @tanstack/react-query-persist-client + @tanstack/query-sync-storage-persister v5.99.0)
- `portal/src/main.tsx` (PersistQueryClientProvider, smart retry)
- `portal/src/contexts/AuthContext.tsx` (clearQueryPersister on logout)
- `portal/src/api/endpoints/advisor-intelligence.ts` (API_TIMEOUT_MS 10s → 30s)

### AWS — NO DEPLOYMENTS THIS SESSION

No Lambda deploys, no DynamoDB writes, no Terraform applies.

---

## Cross-agent Messages Sent

| Time (ET) | To | Subject |
|---|---|---|
| 18:03Z | 2.0.0_SA_COO | ACK CDRS_TFIMPT lane — partner-firm infra conflict flag |
| 18:03Z | 0.7.0_AE_CloudOps | RE: Partner-firm infra design — converged, parked pending CDRS_TFIMPT |
| 18:05Z | 0.7.0_AE_CloudOps | UPDATE: Partner-firm infra = CDRS_TFIMPT.006/.007 (post .005) |
| 18:52Z | 2.0.0_SA_COO | Phase 2 handoff memo DRAFT landed |
| 19:00Z | 0.7.0_AE_CloudOps | ACK 4-Q resolution — .007 DT-side prep done, tsc clean |
| 19:00Z | 2.0.0_SA_COO | .007 DT-side prep DONE — tsc clean, all 4 Qs resolved by AE |

---

## Current State

- **ADVI caching/timeout/retry** — code landed in portal working tree, builds clean, dev server running on 5175, awaits Andrew verification
- **CDRS_TFIMPT.007 DT-side** — draft complete, tsc clean, all design Qs resolved by AE, awaits COO's pending flip + AE's ship-time combine
- **CDRS_TFIMPT.006** — AE firing solo (opal-users-v2 import into shared-infra)
- **ADVI_ROLLUP** — paused per Andrew directive while CDRS_TFIMPT active
- **Partner-firm infra conversation** — fully converged with AE on all 4 open questions; memo captured as `<references>` brief for the .007 TO

## Next Steps

- [Andrew] Verify ADVI dark-panel issue resolved post-persister/timeout changes. Thumbs up → DT commits portal changes + bumps submodule.
- [2.0.0_SA_COO] Flip .007 to `<status>pending</status>` now that AE's 4-Q resolution is in
- [0.7.0_AE_CloudOps] .006 solo ship (opal-users-v2 → shared-infra); then .007 combined commit with DT draft
- [0.4.0_DT] On .007 pending: pair with AE on ship-time combine — ensure build-script rsync lands; drop the draft mirror; execute regression curls (Hunter + Andrew /auth/me parity); tag `partner-firms-v1.0.0` with AE

---

— 0.4.0_DT_ClientPlatform
