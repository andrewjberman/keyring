# DATA_PLATFORM DC-CHAR — Orion own-account API-quality characterization

**TO:** DATA_PLATFORM.DC-CHAR (per-vendor; this = the Orion supplant-side slice) · **Lane:** 0.4.0_DS_ClientPlatform~B · **Lead/integrator:** 0.4.0_DS_ClientPlatform (validate-fold -> Part-5)
**Date:** 2026-06-24 · **Status:** Orion-char COMPLETE (BD-char done; Eclipse-char GATED). RAVC2 base-DS+COO+CTO; CVO ROE-verifies.
**ROE:** OPTION-B compliant, ZERO new vendor traffic — analysis of the EXISTING own-account orion-api pulls (`opal-data-inf/bronze/orion-api`, 15,219 objects, 2020-01-01..2026-06-24) + the D3-documented own-account behaviors (base-DS-fed; `docs/architecture/DATA_PLATFORM_D3_orion_eclipse_arch_spec.md` + ADVI_ORIAPI). No new endpoint hit; no scan; polite.
**Confidence frame:** inf/Orion = **INFERRED tier** (we hold only Orion's AGGREGATED output, NOT the Fidelity-raw below it) — do NOT project to "diffable." API-quality dims are SOURCE-CONFIRMED from D3 + our pulls; the compute-reproducibility + rate-limit-at-scale are INFERRED.

---

## INTERFACE MODEL (the BD contrast)
- **Observation:** Orion is a **real REST query-API** (Orion Connect) with Session-JWT auth + async job patterns — fundamentally MORE mature than BD's batch file-export. The live API dims BD's file-model could not exercise (pagination / server-side-filter / async / auth) ARE characterizable here.
- **Evidence:** D3 S1 (9 daily dimension pull-lambdas + Trading/Models + Portfolio/Accounts + Envision saved-query lifecycle); our 15,219-object orion-api tree.
- **Inference:** Orion sits a full maturity tier above BD on interface sophistication. **Business-significance:** more API to replicate to supplant — but the decisive supplant cost is the COMPUTE it exposes (Dim 7), not the interface.

## Dim 1 — AUTH sophistication (API-maturity)
- **Observation:** Session-JWT (HS512, ~10h TTL), header `Authorization: Session <jwt>` — **NOT Bearer (a Bearer send silently 401s)**; SMS-2FA (via inf-otp-relay); CSRF headers required (App/AppPath/BrowserSessionId/Origin/Referer). Auth obtained via a DAILY Playwright JWT-harvest -> `s3://opal-data-inf/orion/jwt/current.json`.
- **Evidence:** D3 auth spec.
- **Inference:** sophisticated auth (2FA + CSRF + signed session token) but OPERATIONALLY FRAGILE — no API-key / OAuth client-credentials flow; we must browser-HARVEST a session JWT daily (10h TTL + 2FA = a recurring single-point-of-fragility).
- **CONFIDENCE:** HIGH (D3-documented; the jwt-harvest pipeline exists). **ALTERNATIVE:** Orion may offer a partner OAuth flow we don't use — possible, out of own-account scope. **Business-significance:** moderate integration cost + a daily-harvest reliability risk = an operational ding the supplanted (Schwab-direct) feed avoids.

## Dim 2 — PAGINATION (API-maturity)
- **Observation:** present — `?top=5000` cap on Portfolio/Accounts.
- **Inference:** top-N cap style, not cursor/continuation-token; functional but unsophisticated paging. **CONFIDENCE:** HIGH (D3). **Business-significance:** adequate for our volumes; a crude-but-working paging model.

## Dim 3 — SERVER-SIDE FILTERING (API-maturity) — a real DING
- **Observation:** `modelId` / `$filter` query params are **SILENTLY IGNORED** server-side -> the client must filter after the full pull.
- **Inference:** a genuine API-quality defect — silent-ignore is worse than unsupported (it's a correctness trap: a consumer believes it filtered when it didn't). **CONFIDENCE:** HIGH (D3-documented gotcha). **ALTERNATIVE:** filtering may work on endpoints we haven't exercised — but the documented ones silently ignore it. **Business-significance:** forces full-pull + client-filter (more data movement); a real operational tax + correctness risk.

## Dim 4 — ASYNC JOB PATTERN + schema-consistency (API-maturity)
- **Observation:** Envision saved-query lifecycle = list -> Verbose -> Generate (201 + Location) -> poll-Run (~60s hold); plus a **Verbose != runtime-body gotcha** (the schema discovered via Verbose differs from the runtime body).
- **Inference:** a mature async-job pattern (good) but with a real consistency ding (discovery-schema != runtime-schema = a parse trap). **CONFIDENCE:** HIGH (D3). **Business-significance:** async adds latency (~60s) + the schema-mismatch is an integration-fragility.

## Dim 5 — RATE-LIMITS (API-maturity/op) — INFERRED
- **Observation:** NONE observed at our ~9-calls/day polite volume.
- **Inference:** rate-limit behavior at scale is UNKNOWN — and per the ROE (polite, conservative) we will NOT push volume to probe it. **CONFIDENCE:** INFERRED / could-not-verify (honest, Rule-22). **Business-significance:** unverified at scale; benign at our cadence.

## Dim 6 — SURFACE BREADTH (API-maturity)
- **Observation:** BROAD typed surface — 9 daily dimension endpoints (reps/accounts-v2/unified-acct-dim/assets-v2/positions/tax/billing/performance/txn) + Trading/Models + Portfolio/Accounts + Envision; PLUS an observed-but-unused frontier (stored-proc DataSources back-door, SignalR [we poll instead], Authorization/User+Privileges, Reports/Recent, Categories, Verbose-PUT).
- **Inference:** high API-maturity (broad, typed, with latent depth). **CONFIDENCE:** HIGH (D3). **Business-significance:** Orion is a full platform API, not a feed — materially more surface than BD.

## Dim 7 — COMPUTED-PERFORMANCE / TAX EXPOSURE (the SUPPLANT-IP FRONTIER) — the decisive dim
- **Observation:** Orion EXPOSES + serves a `performance_dim` surface + `tax_realized`/`tax_unrealized` (fresh 2026-06-24 in our pulls) — Orion **COMPUTES and serves performance/attribution + tax**, UNLIKE BD (which delivers zero computed performance — residual #1).
- **Inference:** this is the genuine **T2-COMPUTE frontier** for the program. Orion's performance/attribution compute sits BELOW our reach — we hold only Orion's AGGREGATED output, NOT the Fidelity-custodian-raw to recompute from (census: no Fidelity-direct feed). So we CANNOT currently verify or reproduce Orion's performance compute. **CONFIDENCE:** INFERRED (the one place genuine vendor compute-IP plausibly lives; correctly NOT projected from the 49F/BD diffable close). **ALTERNATIVE:** Orion's perf may be a standard method (TWR/Dietz) like our C_00 — IF so it'd be replicable once we hold Fidelity-raw; unverifiable until then. **Business-significance:** Orion's supplant cost-to-work-around is HIGHER than BD's AND GATED — it requires the **Fidelity-direct custodian feed** (the census's load-bearing inf-supplant prerequisite) before the perf-compute can even be diffed.

## ATTRIBUTION DISCIPLINE (Rule-22)
The `_BRONZE_COMPLETE.json` + per-surface `_markers/*.json` in our orion-api tree are OUR ingest-pipeline's completion signals, NOT Orion API features — NOT credited to Orion's API-maturity. Same-day partition freshness (06-24 delivered 06-24 13:42Z; txn T+1 at 06-23) reflects Orion serving same-day data + our pull cadence; Orion's serve-freshness capability is real (same-day) but the marker infrastructure is ours.

---

## 6-DIM PARTNER-SCORING CONTRIBUTION (Orion) + the BD contrast
- **API-maturity: MODERATE-HIGH** (real REST, broad typed surface, sophisticated auth, async jobs, pagination) — materially HIGHER than BD (LOW-MODERATE). DINGS: silent server-side-filter-ignore, Verbose!=runtime gotcha, non-standard `Session` header, daily JWT-harvest fragility.
- **Operational-maturity: MODERATE-HIGH** (same-day serve-freshness, deep 2020-> history, the reliable Assets-snapshot pass-through surface — the TRN-reconstruct alternative corrupted 40.2% rows to $0, so the snapshot is the trustworthy surface) — higher than BD.
- **=> Orion SUPPLANT cost-to-work-around: HIGHER than BD + GATED (INFERRED).** Two drivers: (a) Orion is a richer API (more to replicate), and decisively (b) **Orion COMPUTES performance/tax/attribution we cannot reproduce below it** (no Fidelity-raw) = the genuine proprietary-compute frontier. CONTRAST: BD = low-maturity delivery + ~no compute -> cheap supplant + the supplanted version is BETTER; Orion = high-maturity + real compute below our reach -> **expensive/gated supplant, prerequisite = the Fidelity-direct custodian feed** (the census's inf-supplant lever). This is exactly CTO's "OPEN inferred IP-frontier for inf/Orion," now characterized.

## GROUNDING + RESIDUALS
- **ROE:** zero new vendor traffic (analysis of existing pulls + D3-documented behaviors). **Sources:** base-DS D3 Orion context + ADVI_ORIAPI + our orion-api own-data freshness probe.
- **Residuals (Rule-22, INFERRED tier for inf):** (1) rate-limits at scale = could-not-verify (won't push volume per ROE). (2) Orion perf-compute reproducibility = INFERRED, GATED on a Fidelity-direct feed (can't diff below Orion). (3) UI-vs-export parity = not checked. (4) Eclipse-char = GATED (DC2 crawl, Andrew risk-call) — the trade-plane frontier, separate. Do NOT project Orion's INFERRED tier as proven.
