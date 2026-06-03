# FE-Driven Lambda Keep-Warm During Active User Sessions — Feasibility / Recommendation Brief

**archetype:** DIAGNOSE
**secondary_archetypes:** TRACE, EXPLORE
**Author:** 0.7.0_AE_CloudOps
**Date:** 2026-06-03
**Requested by:** Andrew (direct) via 2.0.0_SA_COO dispatch
**Status:** RECOMMENDATION — design/feasibility only, no deploy
**Audience:** COO (2.0.0_SA_COO), CC CTO (1.0.0_SA_CTO)

---

## The question (Andrew-direct)

> "How can we subtly ping relevant Lambdas while a user is active to keep them warm for the
> duration of their activity? I feel like there's gotta be a clever FE way to manipulate that."

**Goal:** eliminate cold-start latency for portal-facing Lambdas *during an active user session*,
without paying always-on provisioned-concurrency cost when nobody is on the portal.

**Bottom line:** Andrew's intuition is correct and the mechanism is sound. A FE-driven warm-ping,
gated on user presence and targeted at the view the user is on, is **~100-150x cheaper than
provisioned concurrency**, **follows the user** (naturally warms roughly as many execution
environments as there are concurrent active users), and **costs nothing while the portal is idle**.
Recommended below as **Option (a), lightly hybridized**.

---

## 1. Enumeration — portal-facing Lambdas + cold-start exposure

The portal API is classified into three routing tiers (`portal/src/api/endpoint-mapping.ts`):

| Tier | Path prefix | Backend | Regional-Lambda cold-start exposure |
|---|---|---|---|
| **GENERAL** | `/api/general/*` | S3 origin via `public-data-router` (L@E) | None (S3) — only the edge router |
| **SCOPED** (static) | `/api/scoped/advisor-intelligence/*.json` | S3 origin via `shared-advisor-router` (L@E) | None (S3) — only the edge router |
| **SCOPED** (dynamic) | `/api/scoped/advisor-intelligence/{timeseries,snapshots,filters,clients/*}` | API Gateway → **opal-partners-data** | **HIGH** |
| **PRIVATE** | `/api/private/portfolios/*` | API Gateway → **opal-partners-data** | **HIGH** |

Measured cold-start (CloudWatch `Init Duration`, 7-day window, us-east-1):

| Lambda | Runtime | Mem | Pkg/Layer | Cold-start (median) | Cold-start (range) | Cold starts / 7d | Verdict |
|---|---|---|---|---|---|---|---|
| **opal-partners-data** | py3.12 | 2048 MB | AWSSDKPandas layer (`import awswrangler`) | **5,449 ms** | 4,456 – 7,669 ms | 196 | **PRIMARY TARGET** |
| **opal-portal-data-proxy** | py3.11 | 512 MB | 8.4 MB code | **922 ms** | 809 – 2,142 ms | 176 | Secondary |
| **opal-portal-authorizer** | node22 | 256 MB | 19 KB | 500 ms | 336 – 985 ms | 195 | Minor (gates all `/v1`) |
| auth-validator-edge | node20 | 128 MB | 20 KB | ~100-300 ms (est.) | — | — | Edge — not warmable centrally |
| public-data-router | node20 | 128 MB | 313 B | ~100 ms (est.) | — | — | Edge — negligible |
| shared-advisor-router | node20 | 128 MB | 1.8 KB | ~100 ms (est.) | — | — | Edge — negligible |

**Key facts that shape the design:**

1. **`opal-partners-data` is the whole problem.** Median cold-start **~5.4 s** (worst-case 7.7 s). It
   backs the Advisor Intelligence page (timeseries / snapshots / filters / clients / books) and the
   PRIVATE portfolios endpoints. With only 6–45 invocations/day per log stream and 196 cold starts in
   7 days, **nearly every Advisor-Intelligence page load eats a cold start.** This is the user-perceived
   lag Andrew is describing.

2. **The cold-start cost is `import awswrangler`** at module top (`lambda_function.py:61`) — it pulls
   pandas + numpy + pyarrow at init. Because it is module-level, **any** route triggers the full init.
   *Corollary:* a warm-ping to a trivial no-op route warms the container just as well as a real request
   — the 5.4 s is paid once at init, then the env is warm ~5-15 min regardless of which route hit it.

3. **None of these are VPC-attached** — so there is no ENI cold-start penalty to chase; the penalty is
   pure interpreter + dependency import.

4. **The S3-backed tiers (GENERAL/SCOPED-static) have no regional-Lambda cold start** — only the
   128 MB Node edge routers, whose cold-start is small and (being Lambda@Edge) cannot use provisioned
   concurrency and can only be "warmed" at the user's nearest PoP. Low value; out of scope for warming.

5. **There is already a precedent for FE-driven background activity** — `api-client.ts` runs a
   mutex'd *proactive token refresh* every ~10 min (`PROACTIVE_REFRESH_AGE_MS`). The warm-ping is the
   same shape and can live in the same place.

---

## 2. Options analysis

| Option | Mechanism | Warms-for-session? | Follows user / scales with concurrency? | Cost (opal-partners-data, ~20 active users) | Verdict |
|---|---|---|---|---|---|
| **(a) FE-driven warm-ping** | On presence/activity, FE fires lightweight auth'd warm request to the relevant Lambda set | **Yes** | **Yes** — each active user's pings keep ~1 env warm; N users → ~N warm envs | **~$0.15/mo** | **RECOMMENDED** |
| (b) Provisioned concurrency | Reserve N always-on warm envs | Yes (always) | Fixed N regardless of presence | **~$22/mo per unit, 24/7** (2 GB); +$5.5/mo for data-proxy; multiply for concurrency | Baseline — overpriced for our scale |
| (c) Scheduled EventBridge warmer | Cron pings Lambda every ~5 min, 24/7 | Yes | **No** — keeps only 1 env warm; 2 simultaneous users → 2nd still cold | ~$0.03/mo | Cheap but concurrency-blind + runs when idle |
| (d) Hybrid | FE presence-ping (primary) + low-freq market-hours EventBridge floor | Yes | Yes (FE) + smooths first-hit-of-day (cron) | ~$0.18/mo | Optional enhancement on (a) |

### Cost detail

- **Lambda pricing (x86, us-east-1):** $0.0000166667 / GB-s on-demand duration; $0.20 / 1M requests;
  provisioned concurrency $0.0000041667 / GB-s for the *allocation* (billed whenever allocated, 24/7).
- **(b) Provisioned concurrency, 1 unit on opal-partners-data (2 GB):**
  `2 × 0.0000041667 × 3600 × 730 ≈ $21.9/mo` — *paid every hour of every day, including nights/weekends
  when nobody is on the portal*. Add data-proxy (0.5 GB) ≈ $5.5/mo. One unit each ≈ **$27/mo**, and to
  cover concurrent users you provision more units (linear).
- **(a) FE-driven warm-ping, ~20 active users × 8 h/day × 22 days, ping every ~4-5 min:**
  ~42k pings/mo. Once warm, a no-op warm route runs ~50-80 ms.
  Duration: `42,240 × 2 GB × 0.08 s × 0.0000166667 ≈ $0.11`. Requests: `42,240 × $0.20/1M ≈ $0.008`.
  **Total ≈ $0.12-0.15/mo.** (The real ~5.4 s cold inits are paid by the user's first request *anyway*
  — the ping just moves that payment a few seconds earlier, it is not net-new cost.)
- **(c) EventBridge 24/7 every 5 min:** ~8.8k pings/mo ≈ **$0.025/mo** — cheap, but warms exactly one
  env and runs around the clock irrespective of presence.

**FE-driven warming is ~150x cheaper than provisioned concurrency AND only spends while users are
present AND scales warm-env count with concurrent users** — the property the always-on options lack.

---

## 3. Recommended design — Option (a), lightly hybridized

### 3a. Backend (AE 0.7 / CloudOps — Terraform-deployed per Rule 1)

Add a **dedicated ultra-light warm branch** to `opal-partners-data` (and optionally
`opal-portal-data-proxy`) that early-returns **before any DynamoDB/S3 I/O**:

```python
# top of handler, before routing / firm-validation / S3 reads
if event.get("queryStringParameters", {}).get("warm") == "1" \
   or event.get("rawPath", "").endswith("/api/health/ping"):
    return {"statusCode": 200,
            "headers": {"Cache-Control": "no-store"},
            "body": json.dumps({"warm": True, "v": VERSION})}
```

- This still pays the module-level `import awswrangler` on a cold env — *which is exactly what we want
  to trigger* — but adds ~zero marginal duration on a warm env.
- **Do NOT reuse the existing `/api/health/advisor-intelligence` route for warming** — it scans all
  firms (DynamoDB) + does a per-firm S3 HEAD on every call (`handle_health_check`), which amplifies
  load/cost and would muddy the health signal. The no-op `warm` branch is cleaner.
- Deploy via Terraform (`partners-api/lambdas.tf`) + `safe-apply.sh` per Rules 1/2/18. Code-only change,
  tiny diff.

### 3b. Frontend (RD/DE — portal `src/`; NOT AE scope, flagged for CTO PRD)

A small `useLambdaKeepWarm` hook layered on the existing authenticated `api-client.ts`:

- **Triggers:** (1) session authenticated (app mount with valid token); (2) route change *into* a
  Lambda-backed view; (3) `visibilitychange → visible` (tab refocus); (4) a low-frequency heartbeat
  (`setInterval`, ~4 min, **cleared on blur/hidden/unmount**).
- **Presence gate:** run only while `document.visibilityState === 'visible'` **and** a Lambda-backed
  view is mounted. Stop on blur/hidden/unmount → *warming follows the user and dies when they leave.*
- **View-targeted** (warm only what the current view will hit):
  - **Advisor Intelligence** → warm `opal-partners-data` (the 5.4 s win — highest value).
  - **Portfolios (PRIVATE)** → warm `opal-partners-data` (+ `data-proxy` if it fronts the call).
  - **Market Overview / sentiment / macro / valuation / benchmarks** (S3-backed GENERAL) → **skip**
    (no regional Lambda; only edge routers, low value).
- **Debounce:** coalesce pings within ~60 s; never ping per-keystroke. Lambda stays warm ~5-15 min, so
  a ~4-min cadence keeps it warm with comfortable margin. Add small random jitter to the interval to
  avoid synchronized fleet pings.
- **Mechanism:** reuse the api-client fetch wrapper (already attaches `Authorization: Bearer` + handles
  401 refresh-retry). `warmLambda(target)` issues `GET /api/scoped/advisor-intelligence/...?warm=1`
  (or `/api/health/ping`) with a short timeout and ignores the response body. Natural home: alongside
  the existing proactive-refresh timer.

### 3c. Optional hybrid floor (d)

A very-low-frequency EventBridge warmer (1 ping / 5 min, **weekdays 9:30-16:00 ET only**) so the
*first* user of the day doesn't eat the one 5.4 s hit. ~$0.01/mo. Optional — the FE hook already warms
on each user's session-start; the floor only smooths the very-first-hit-of-day. Recommend deferring
unless Andrew wants that last edge smoothed.

---

## 4. Footguns (and how the design handles each)

1. **Warm pings count as invocations/cost.** Quantified — ~$0.15/mo at our scale. Bounded by the
   per-user debounce + presence-gate (no pings while idle/hidden). Scales linearly with users × cadence;
   revisit cadence if user count grows 10x.
2. **Auth on the warm endpoint.** Keep the warm route **behind `auth-validator-edge`**; the FE fires it
   with the user's existing JWT (the FE is already authenticated). **Do not create an anonymous warm
   endpoint** — it is both a security hole and would 403 at the edge anyway (anon portal fetches are
   blocked — confirmed behavior). If the JWT is mid-expiry, the ping 401s harmlessly (existing
   refresh-retry covers it, or it fails silent).
3. **Thundering herd.** Not a concern at tens-of-users scale; per-user debounce + jittered interval
   prevents synchronized pings.
4. **Concurrency-follow is probabilistic, not guaranteed.** FE warming keeps ~as many envs warm as
   concurrent active users, but a user firing many parallel real requests can still spill onto a cold
   env beyond the warmed count. Warming sharply reduces P(cold) but does not guarantee 0 — that is the
   PC tradeoff (PC guarantees N at fixed always-on cost). For Opal's scale, probabilistic is the right
   call.
5. **Lambda@Edge cannot be warmed centrally.** FE pings to S3-backed routes only warm the nearest PoP
   router (128 MB Node, sub-300 ms cold) — low value. Don't over-engineer edge warming.
6. **Heartbeat-storm.** Use a debounced interval, never per-interaction firing.

---

## 5. Recommendation

**Adopt Option (a): FE-driven warm-ping, view-targeted + presence-gated**, with:
- **Backend:** a dedicated no-op `?warm=1` / `/api/health/ping` early-return branch in
  `opal-partners-data` (primary) and `opal-portal-data-proxy` (secondary) — AE-owned, Terraform-deployed.
- **Frontend:** a `useLambdaKeepWarm` presence hook on the existing authenticated api-client —
  RD/DE-owned, portal `src/`.
- **Optional:** a market-hours EventBridge floor (d) for first-hit-of-day smoothing — defer unless Andrew wants it.

**Cost delta:** ~$0.15/mo vs ~$27+/mo for provisioned concurrency — and it follows the user instead of
running 24/7. This is exactly the "clever FE" mechanism Andrew pointed at, and it is the most
cost-effective path to warm-for-session-duration.

**If promising → CTO folds the FE hook + backend warm-branch into a PRD.** The backend warm-branch is a
small AE change; the FE hook is the substantive piece (separate surface from the Advisor Intelligence FE
refinements work). I can author the backend warm-branch TO on GO.

---

## Appendix — methodology / data sources

- **Topology:** `portal/src/api/endpoint-mapping.ts`, `portal/src/api/api-client.ts`,
  `portal/src/api/endpoints/advisor-intelligence.ts`; `infra/aws/lambda/ci/lambda-source-map.json`.
- **Handler init:** `infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/lambda_function.py`
  (`import awswrangler` at L61; `handle_health_check` at L938).
- **Configs:** `aws lambda get-function-configuration` (mem/runtime/layer/VPC) for opal-partners-data,
  opal-portal-data-proxy, opal-portal-authorizer, auth-validator-edge, public-data-router,
  shared-advisor-router.
- **Cold-start measurement:** `aws logs filter-log-events` on `Init Duration` REPORT lines, 7-day
  window, us-east-1.
- **No provisioned/reserved concurrency** currently configured on any of these functions (verified).
