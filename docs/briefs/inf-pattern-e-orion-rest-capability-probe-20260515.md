# INF Pattern E — Orion REST Capability Probe

**Project:** ADVI_INFINC.005 (re-scoped probe TO)
**Author:** 0.4.0_DS_ClientPlatform~D
**Date:** 2026-05-15
**Status:** Probe complete — recommendation: TXN viable (positive), PERF no mechanism

---

## 1. Background

INFINC.005 was originally scoped as a Pattern E implementation TO (date-windowed
incremental pulls for INF_API_PULL_TXN / INF_API_PULL_PERF). DS~D's Phase 0 STOP —
upheld by CTO — found the brief §2.5 date-windowing premise contradicted by a DS~B
probe (20260430T174809Z) transcribed verbatim into both script docstrings. The TO
was re-scoped to this capability probe to determine whether *any* viable
call-count-reduction mechanism exists before an implementation TO is authored.

The wall-time bottleneck is sequential rate-limited **call count**:
- INF_API_PULL_TXN: ~1,160 per-account calls (`GET /api/v1/Portfolio/Accounts/{id}/Transactions`)
- INF_API_PULL_PERF: ~314 per-client calls (`GET /api/v1/Portfolio/Clients/{id}/Performance`)

---

## 2. Probe method

Read-only GET probes against `api.cloud.orionadvisor.com` using the live JWT
(`orion/jwt/current.json`). Test client_id=206, account_id=42. Two probe rounds
2026-05-15 ~04:25-04:30Z. Raw results: `inf_pattern_e_probe_result.json`,
`inf_pattern_e_probe2_result.json`.

---

## 3. Findings

### KEY CORRECTION — the DS~B docstring claim is FALSE

The TXN script docstring states: *"NO date params for account-level endpoint —
returns complete history in one call."* **This is empirically wrong.**

| Probe | Endpoint | Result |
|-------|----------|--------|
| Q0 baseline | `Accounts/42/Transactions` (no params) | 200, **2,194 rows** |
| Q0b | `Accounts/42/Transactions?startDate=2026-02-14&endDate=2026-05-15` | 200, **64 rows** |
| Q0c | `Accounts/42/Transactions?asOfDate=2026-02-14` | 200, 2,194 rows (asOfDate ignored) |

The account-level endpoint **does** accept `startDate`/`endDate` and **does** filter
(2,194 → 64 for a 90-day window). The DS~B docstring was stale or tested wrong param
names. The Phase 0 STOP was still procedurally correct — it triggered this probe
that found the truth.

### Q1 — Firm / batch / client-level transactions endpoints: CONFIRMED

| Probe | Endpoint | Result |
|-------|----------|--------|
| Q1a | `Clients/206/Transactions` (no params) | 200, **12,096 rows, 9 accounts** — full history, all the client's accounts in ONE call |
| Q1b | `Portfolio/Transactions` (no params) | 400 — *"Transactions without entity id require start and end date"* |
| Q1c | `Portfolio/Transactions?startDate=&endDate=` (90d) | 400 — *"Transactions without entity id cannot exceed 31 days"* |
| Q1d | `Registrations/42/Transactions` | 200, 1,232 rows |
| firm_txn_7d | `Portfolio/Transactions?startDate={today-7d}&endDate={today}` | **200, 47,401 rows, 767 distinct accounts**, dates 2026-05-08..05-14 |
| firm_txn_31d | `Portfolio/Transactions` 31-day window | 400 — *"cannot exceed 31 days"* (31 inclusive is over; safe ≤30) |
| firm_txn_30d | `Portfolio/Transactions` 30-day window | **read-timeout at 120s** — 30-day firm-wide is too large |
| client_txn_30d | `Clients/206/Transactions?startDate=&endDate=` (30d) | 200, 121 rows (12,096 → 121 — client endpoint filters, no 31-day cap) |

**Two viable TXN mechanisms confirmed:**

1. **Firm-level windowed** — `GET /api/v1/Portfolio/Transactions?startDate=&endDate=`.
   Returns the *entire firm* in one call. API caps the window at ≤30 days when no
   entity id is supplied. Empirically a 7-day firm-wide window returns in ~10s
   (47,401 rows); a 30-day firm-wide window times out at 120s. **Practical window:
   ~7-14 days per call.** Daily incremental = 1 call replaces ~1,160 account calls.

2. **Client-level windowed** — `GET /api/v1/Portfolio/Clients/{id}/Transactions?startDate=&endDate=`.
   One call per client (~314 vs ~1,160 accounts = 3.7x reduction). No 31-day cap
   (client is an entity id). Accepts any window or full-history. Slower than
   mechanism 1 but no chaining/timeout risk.

### Q2 — Modified-since / activity-delta: ABSENT

`modifiedSince` param is **silently ignored** on both the account endpoint
(2,194 rows with/without) and the client endpoint (12,096 rows with/without).
No activity-delta / change-feed capability found.

### Q3 — Concurrency headroom

`AdaptiveRateLimiter` (`data/orion/scripts/bronze/rate_limiter.py`) is architecturally
**sequential**: `throttle()` does `time.sleep(1/rate_rps)` before each call; not
thread-safe; no concurrent-call coordination. Defaults: safe_floor 2.0 rps,
step_up +0.5/clean-100-batch, step_down -1.0/failure-batch. Concurrency would
require a thread-safe limiter rewrite and carries 429 risk (N uncoordinated
threads = N× effective rate). Modest orthogonal lever; not recommended as primary.

### Q4 — None-of-the-above

No additional mechanism surfaced. The firm-level windowed endpoint (Q1) is the
decisive finding; nothing else is needed for TXN.

### PERF — no call-count-reduction mechanism

- `GET /api/v1/Portfolio/Performance` (firm-level) → **404**. No firm-level perf endpoint.
- `modifiedSince` ignored (same as TXN).
- PERF stays ~314 per-client calls. The only untested lever is whether the
  client Performance endpoint accepts a *short* date window (the docstring's
  "HARD LIMIT" documents 5y+ timeout, not short windows — and the TXN docstring
  being wrong casts doubt on the PERF one). Probing PERF windowing was explicitly
  out-of-scope for this TO; flagged as a follow-up below.

---

## 4. Recommendation

**TXN: viable mechanism confirmed — author an implementation TO (INFINC.006).**

Recommended design:
- **Daily incremental:** firm-level windowed pull, `Portfolio/Transactions` with a
  trailing ~7-day window (1 call, ~10s) — replaces ~1,160 account calls. Since the
  chain runs daily, a 7-day window covers since-last-pull plus a 7-day in-window
  backdated-correction catch.
- **In-window deeper catch:** chain ≤14-day windows to cover a 90-day trailing span
  (~7 calls) on a configurable cadence, if a wider in-window guarantee is wanted.
- **Weekly full-history backstop:** client-level endpoint, full-history, ~314 calls
  (no timeout risk) — catches out-of-window backdated corrections. The original
  TO's backstop-first sequencing invariant still applies.
- **Dedupe** by transaction `id` keeping last; **bronze shape** — account / client /
  registration / firm Transactions endpoints all return the *same* column schema
  (verified: identical key set in every probe preview), so bronze stays
  shape-stable. Implementation TO should still verify the current
  `CONFIRMED_FIELDS` subset is present (probe preview was truncated).
- Expected: TXN ~7min → ~10-60s daily. Major win.

**PERF: no clean mechanism — recommend defer for v1, OR a small follow-up probe.**
- No firm-level endpoint, no activity-delta. Call count (~314) is irreducible via
  the probed surface.
- Option: a follow-up probe of short date windows on the client Performance
  endpoint (the TXN docstring was wrong; the PERF one may be too). If short windows
  work, PERF per-call payload shrinks (faster calls) though call count stays 314.
- Otherwise PERF stays ~9min, or concurrency (Q3) is the only lever (modest, needs
  thread-safe limiter rewrite, 429 risk).

**Net:** Pattern E is **partially achievable** — the larger TXN cost (~7min) has a
confirmed clean mechanism; PERF (~9min) does not. Recommend INFINC.006 scoped to
TXN only, with PERF either deferred for v1 or routed to a separate short-window
follow-up probe. Patterns A/B/C already banked the major chain wins; TXN Pattern E
is incremental gravy and worth doing; PERF is not worth a risky implementation.

---

## 5. Acceptance criteria status

- AC1 (Q1 firm/batch TXN endpoint): **CONFIRMED** — firm-level + client-level, evidence above
- AC2 (Q2 modified-since): **CONFIRMED ABSENT** — param silently ignored
- AC3 (Q3 concurrency): quantified — sequential limiter, rewrite needed, 429 risk
- AC4 (Q4 none-of-the-above): honored — no force-fit; firm-level endpoint is the answer
- AC5: this brief
- AC6: explicit recommendation — TXN implementation TO; PERF defer/follow-up
- AC7: no date-window params implemented (probe GETs only; no script edits)
- AC8: no pull-script edits — investigation only
- AC9: no emoji
- AC10: RAVC2 to follow
