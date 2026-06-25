# BD 49F — Interim Cookie Solution for the DataMining REST API (no password / no login-automation)

**Author:** 3.0.0_SA_CVO · **Date:** 2026-06-25 · **Priority:** PEAK (Andrew-direct)
**For:** 1.0.0_SA_CTO (arch-gate) → 0.6/0.7 AE (build) · CVO drives + verifies · Andrew = cookie capture
**Scope:** ADVI_BDAPIMIG interim auth. The password/headless-login path (Option A/C, `cot_bd_session_fetch.py`
auto-login) is **ON HOLD per Andrew — return later.** This is the bridge that keeps 49F BD data flowing
on a MANUALLY-supplied cookie until then.

## Goal
Keep the proven DataMining REST pull (`cot_bronze_ingest.py`, bd-env) running on a manually-captured
`.bd.identity` cookie, with the **least possible manual re-capture friction** and **zero silent failure**.

## Empirical grounding (live probes, 2026-06-25, against bd3.bdreporting.com from Andrew's egress)
1. **`.bd.identity` ALONE authenticates the API** — `GET /datamining/auth/token` returns 200 with only
   `.bd.identity` (no `__cf_bm`, no antiforgery/idsrv cookies). `__cf_bm` alone → 401. So **the ONLY cookie
   to maintain is `.bd.identity`.** (The 30-min Cloudflare `__cf_bm` is a non-factor — drop it from the
   maintained secret; harmless if left.)
2. **`GET /datamining/auth/keepalive` → 204** — the session can be kept alive server-side. Per the cot
   precedent ("BD sessions last 24h+ with keepalive"), a keepalive cron **stretches the cookie's life**,
   maximizing time between manual captures.
3. The cookie does not rotate (no Set-Cookie on calls); keepalive extends validity in place.
4. **Full REST pull PROVEN on this cookie** — all 4 BD tables pulled + landed to opal-data-bd today on
   `.bd.identity` + `__cf_bm` (and #1 shows `.bd.identity` alone suffices).

## The mechanism (4 components)

```
   Andrew (manual, infrequent)                    AWS (autonomous, no password)
   ┌─────────────────────┐                       ┌───────────────────────────────────────┐
   │ capture .bd.identity │  ── paste ──▶  (D) ─▶ │ SM: blackdiamond/49f/session           │
   │ from a live 49F sess │                       │   { bd_identity, captured_at }         │
   └─────────────────────┘                       └───────────────────────────────────────┘
                                                     │                 │              │
                                              (A) keepalive      (B) REST pull   (C) freshness
                                              cron ~10min        daily cron       probe → ALERT
                                              GET /auth/keepalive  cot_bronze_      GET /auth/token
                                              (extend session)     ingest (bd env)  401 → SNS Andrew
```

- **(A) Keepalive cron** — a tiny Lambda on a ~10-15 min EventBridge schedule: reads `.bd.identity` from
  SM, `GET /datamining/auth/keepalive`. Keeps the session alive to whatever BD's absolute cap allows →
  defers manual re-capture as long as physically possible. (NEW; interim-specific.)
- **(B) Scheduled REST pull** — the PRD Phase-1 `bd-exporter` API runner: daily EventBridge → run
  `cot_bronze_ingest.py` firm-bound to bd (the 4 env vars EXPLICIT — firm-sep AC#4) on the SM cookie →
  lands `forwardfill_v2/{table}` → existing silver chain (zero-code-change, DS-confirmed). Replaces the
  dead Playwright scrape fleet. No login needed — it reads the SM cookie.
- **(C) Freshness-probe + ALERT** — before the pull (and/or a standalone ~hourly probe): `GET
  /datamining/auth/token`; on 401 (cookie dead / cap reached) → SNS to Andrew: "re-capture `.bd.identity`."
  Closes the 6-day-silent-failure gap (the original incident's compounding cause: only allocations was
  alarmed). NON-OPTIONAL, EGRESS-verified.
- **(D) Cookie-injection path** — Andrew pastes a fresh `.bd.identity` → SM `put-secret-value` (one value;
  the bundle format already exists). A 30-second action when (C) alerts. (Could be a tiny one-field internal
  page later; CLI/paste is fine for the interim.)

## The one open variable: manual re-capture cadence
How often Andrew must re-paste = the **absolute lifetime of `.bd.identity` under keepalive-only** (no
re-login). `.bd.identity` is an ASP.NET DataProtection token (opaque/encrypted — its exp is not readable
client-side), so the cap is determined EMPIRICALLY: with (A) running, observe when `keepalive`/`token`
first returns 401. Expectation from the cot precedent: **≥24h, plausibly multiple days** if the idsrv
absolute-session-lifetime is generous; worst case ~daily. Either way (C) makes it self-announcing — Andrew
re-captures only when alerted, never on a guess. **No silent staleness regardless of the cap.**

## Interim ↔ permanent boundary
This IS PRD Phase-1 (the `bd-exporter` API runner + freshness alarm) **minus the auto-login session-fetch**,
**plus** the keepalive cron (A) that the auto-login version wouldn't need. When the password/MFA path comes
off hold (Option A SS&C-exempt or B device-trust or C OTP-automation), the auto-login session-fetch replaces
(D)'s manual capture and (A) becomes belt-and-suspenders. Nothing built here is throwaway — (B)/(C) are the
permanent runner+alarm; only (D) manual-capture gets automated later.

## Lanes
- **CTO** — arch-gate (A) keepalive Lambda + (B) runner + (C) alarm; the firm-sep guard on (B) (4 env vars
  explicit + fail-closed if BD_S3_BUCKET unset — the silent-cot-default landmine).
- **AE** — build (A)/(B)/(C) (Terraform Lambdas + EventBridge + SNS; the cot-exporter pattern). Add retry/backoff
  on the pull (the transient allocations `Error` seen today).
- **Andrew** — (D) cookie capture, now + whenever (C) alerts.
- **CVO** — this design; verify (A) extends, (B) lands firm-safe, (C) alert egress-fires; co-verify the data.

## Immediate (already done by CVO this session)
- SM secret `blackdiamond/49f/session` created with the live cookie; REST pull proven (4 tables landed);
  protective `keepalive` fired (204). The cookie is good now — (A)/(B)/(C) make it sustainable.
