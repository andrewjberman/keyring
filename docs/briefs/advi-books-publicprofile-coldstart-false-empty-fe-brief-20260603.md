# ADVI Books Tab + AdvisorPublicProfile — Cold-Start "No Data" Root Cause + FE Fix Brief

**archetype:** DIAGNOSE
**secondary_archetypes:** TRACE
**Author:** 0.7.0_AE_CloudOps
**Date:** 2026-06-03
**For:** RD (FE implementer) — handed off by Andrew
**Companion to:** `docs/briefs/fe-driven-lambda-keep-warm-feasibility-20260603.md` (the keep-warm mechanism + backend `?warm=1` branch)
**Status:** ANALYSIS — RD-actionable; FE fix is two small, surgical changes

---

## Symptom (Andrew, observed)

> "Some of the data on ADVI is nested. If you click halfway through a drilldown, then come back
> ~10 min later and try to click something, it'll say it has **no data** — because the Lambda
> timed out and you're not actually making requests that deep in the tabs anymore."

This is **not** "the spinner is slow." It is a **false empty-state**: a real error response from a
cold Lambda is being rendered as "no data," with no retry and no cached fallback. It affects the
**deep drilldowns specifically** (the L3 client detail / L4 account composition in the Books tab,
and the drilldown queries in AdvisorPublicProfile) — not the book/profile overview.

---

## Root cause

All ADVI drilldown data is served by a single backend Lambda, **`opal-partners-data`** (2048 MB,
pandas/awswrangler imported at module load → **median cold-start ~5.4 s**, measured; cold on nearly
every page load given low steady-state traffic). The FE behavior around it is the bug.

### Layer 1 — the global QueryClient config is *correct* (`portal/src/main.tsx:37-60`)

```ts
new QueryClient({ defaultOptions: { queries: {
  staleTime: Infinity,   // never stale mid-session
  gcTime:    Infinity,   // cached until logout (queryClient.clear())
  retry: (failureCount, error) => {        // <-- smart retry, purpose-built for cold-starts
    if (failureCount >= 2) return false
    if (err?.name === 'AbortError') return true            // cold-start abort -> retry
    if (err?.message?.includes('Failed to fetch')) return true
    if (err?.message?.match(/\b(4\d{2})\b/)) return false  // 4xx -> don't retry
    return true                                            // 5xx (incl 503) -> retry
  },
  retryDelay: (i) => Math.min(1000 * 2 ** i, 30000),
}}})
```

Under these defaults a cold-Lambda 503/abort **retries and recovers**, and data stays cached all
session. `api-client.ts` throws on any non-OK response (`api-client.ts:170-172`), so a 503 surfaces
as an error the retry logic catches. The contract is all there — **the L2 book/profile overview
queries use these defaults and are fine.**

### Layer 2 — the deep drilldowns *opt out* of both safety nets (this is the bug)

For PII reasons the deepest queries override the global defaults with `gcTime: 0` (evict on unmount)
**and** `retry: false`. The `gcTime: 0` serves a legitimate PII posture; the `retry: false` is the
problem.

| File | Query (line approx) | Override | Issue |
|---|---|---|---|
| `AdvisorBookView.tsx` | L2 advisor book (`:167`) | *(inherits global)* | OK — cached + smart-retry |
| `AdvisorBookView.tsx` | **L3 client detail (`:186`)** | `gcTime: 0, retry: false` | **No cache + no retry → false-empty on cold** |
| `AdvisorBookView.tsx` | **L4 account composition (`:202`)** | `gcTime: 0, retry: false` | **Same** |
| `AdvisorBookView.tsx` | inflec account timeseries (`:212`) | `gcTime: 0, retry: false` | Same |
| `AdvisorBookView.tsx` | per-account rfs `useQueries` (`:234`) | `retry: false` | Same (fan-out → higher cold-hit odds) |
| `AdvisorPublicProfile.tsx` | drilldown-summary (`:294`) | `retry: false` | Same |
| `AdvisorPublicProfile.tsx` | exec-summary (`:303`) | `retry: false` | **OK as-is** — 404 normalized to empty bullets by `getAdvisorExecSummary` (by design) |
| `AdvisorPublicProfile.tsx` | canonical NNA (`:318`) | `staleTime: 5m` (inherits gcTime ∞ + smart-retry) | OK |

### Why this reproduces the exact symptom

1. Drill into a client/account (L3/L4) → fetches fine (Lambda warm from active clicking).
2. Navigate up/away → because `gcTime: 0`, that data is **evicted immediately**. No cached copy.
3. Pause ~10 min → the deep routes go cold (not being hit) and there is **no cache fallback**.
4. Click back into the drilldown → **fresh** fetch (cache empty) → lands on a **cold**
   `opal-partners-data` → cold-start 503/abort → **`retry: false`** → React Query gives up on
   attempt #1 → component renders **"no data."**

The L2 overview never does this (cached all session + retries). That is precisely why the symptom
appears only when going **deep**. Net effect: the deepest, most PII-sensitive views are stripped of
both the cache *and* the retry safety net — so they are the **most** exposed to a cold Lambda, which
is the opposite of desired.

### The key insight

`gcTime: 0` and `retry: false` do **two different jobs**, and only one serves PII:
- **`gcTime: 0`** = the PII control (evict sensitive roster/tax-lot data on unmount). **Keep it.**
- **`retry: false`** does **nothing** for PII — retrying a fetch does not make data linger in memory
  any more than the first attempt. It defeats both the backend's deliberate **503-for-retry**
  contract (`opal-partners-data` changelog v2.3: returns 503 not 200 on empty/invalid "to enable
  frontend retry logic") and the global smart-retry built for cold-starts. **Safe to remove.**

---

## The fix — two surgical layers

### FIX 1 (FE, RD) — re-arm retry on the deep drilldown queries; KEEP `gcTime: 0`

Remove the `retry: false` override on the Lambda-backed deep queries so they inherit the global
smart-retry. **Do not touch `gcTime: 0`** — the PII eviction posture stays exactly as-is.

- `AdvisorBookView.tsx`: L3 client detail (`:186`), L4 account composition (`:202`), inflec account
  timeseries (`:212`), per-account rfs `useQueries` (`:234`) — delete the `retry: false` line in
  each (keep every other option, including `gcTime: 0`).
- `AdvisorPublicProfile.tsx`: drilldown-summary (`:294`) — delete `retry: false`.
  - **Leave exec-summary (`:303`) as-is** — its 404→empty normalization is intentional; retrying it
    buys nothing.

Effect: a cold-start 503/abort on a deep click now retries (≤2×, exp backoff) and recovers —
spinner → data — instead of a false "no data." This is correctness, independent of warming.

**Optional polish:** distinguish *error* from *empty* in the drilldown render path so a still-retrying
query shows a spinner/retry affordance rather than the empty state. (Today `isError`/empty collapse to
the same "no data" view in these panels.) Not required for the fix, but it removes the last visual
ambiguity.

### FIX 2 (FE hook, RD/DE + AE backend) — keep the Lambda warm for the session

The latency half, from the companion brief. Because **every L3/L4 drilldown is the same Lambda**, a
single quiet heartbeat keeps the whole drilldown tree warm — so the deep click lands on a warm
container and returns instantly (and for `gcTime: 0` queries, a warm Lambda is the *only* thing that
makes the single uncached attempt fast).

- **FE (`useLambdaKeepWarm`):** on session-auth / route into Advisor-Intelligence (or Portfolios) /
  tab refocus / ~4-min heartbeat, fire a lightweight authenticated ping to `opal-partners-data`.
  Presence-gated (`document.visibilityState === 'visible'` + view mounted), debounced (~60 s),
  jittered. Reuse the authenticated `api-client` fetch wrapper; natural home is alongside the
  existing proactive token-refresh timer in `api-client.ts`.
- **Backend (AE, separate TO):** a no-op `?warm=1` / `/api/health/ping` early-return in
  `opal-partners-data` (before any DynamoDB/S3 I/O), behind the existing edge auth (rides the user's
  JWT — no anonymous endpoint). TF-deployed.

**Why both:** FIX 2 (warm) means the deep click is *instant* and the 503 basically stops happening;
FIX 1 (retry) means even a rare cold hit *self-heals* instead of false-emptying. Warm kills latency;
retry kills the false-empty. Neither alone fully closes the scenario — together they do.

---

## Acceptance / test guidance

- **Repro (pre-fix):** open a Books-tab client→account drilldown; navigate up; wait ≥ ~10 min (or
  force the Lambda cold by waiting past idle eviction); re-open the same drilldown → observe "no data."
- **FIX 1 verified:** same repro now recovers — a transient cold-start 503/abort retries and the panel
  populates (watch Network: a 503 followed by a successful retry). PII unchanged: confirm the L3/L4
  data is still evicted on unmount (`gcTime: 0` intact — React Query devtools shows the query removed
  on unmount).
- **FIX 2 verified:** with the warm hook running, a deep click after a 10-min pause returns in
  ~sub-second (no cold-start), and CloudWatch shows the periodic warm pings with no `Init Duration`
  between them (container stayed warm).
- Run `/frontend-dev` (visual smoke) on the Books tab + AdvisorPublicProfile after the FE change per
  the portal visual-gate discipline.

---

## Ownership split (for the PRD)

| Lane | Work |
|---|---|
| **RD (FE)** | FIX 1 (remove `retry: false`, keep `gcTime: 0`) + FIX 2 FE `useLambdaKeepWarm` hook + optional error-vs-empty render polish |
| **AE/CloudOps (me)** | FIX 2 backend `?warm=1` no-op branch in `opal-partners-data` (+ data-proxy), TF-deployed; on PRD GO |

Both fixes are small and independent; FIX 1 can ship immediately (pure FE, no backend dependency) and
delivers the correctness win on its own. FIX 2 adds the latency win.

---

## Appendix — evidence

- Global config: `portal/src/main.tsx:37-60`.
- Overrides: `portal/src/pages/AdvisorIntelligence/_shared/AdvisorBookView.tsx` (`:167,:186,:202,:212,:234`);
  `portal/src/pages/AdvisorIntelligence/_shared/AdvisorPublicProfile.tsx` (`:294,:303,:318`).
- FE error surfacing: `portal/src/api/api-client.ts:165-172` (throws on non-OK; 401-only refresh-retry;
  no AbortController/timeout).
- Backend 503-for-retry contract: `infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/lambda_function.py`
  changelog v2.3 (`:46-49`) + validation path (`:384-412`).
- Cold-start measurement: `aws logs filter-log-events` on `Init Duration`, 7-day window, us-east-1
  (median ~5.4 s; see companion keep-warm brief).
