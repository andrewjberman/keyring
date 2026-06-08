# 0.4.0_DE_ClientPlatform — Session Log addendum 2026-06-08 (~1350Z–1405Z)

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE

Continues `work_1348Z.md` (c09a95c50). Post-gate inbox traffic + COO redirect.

## Inbox handled (3 msgs)
- **COO RAVC2-ACCEPT** (both gates GREEN, visual-gate dependency satisfied for MDLP_DISTFIX +
  MDPF_COUNTS close) + REDIRECT: wire a firm-entitled smoke cred into .frontend-dev/auth.
- **CVO RAVC2** (gate accepted) then **CVO CORRECTION/WITHDRAW**: CVO over-flagged a reconciliation
  concern using a naive aggregate-timeseries by_model sum (7,434/6,978/456) as reference, then
  retracted — my displayed 7,465 traces cleanly to DS-verified canonical 7,301 origin + 164 blend-fold.
  I independently pulled the same served artifacts and confirmed: that by_model array carries blends
  (int_ltc 143, st_int 23) + SMAs (div 43, growth 50) as SEPARATE keys, a different basis than the
  per-account canonical distribution feed. No action; folded CVO's one-line trace-doc nicety into the
  auth README. Acked (135758Z).

## COO redirect DONE — firm-entitled smoke cred wired (portal DEV 03d719d4)
Harvested existing firm creds from `.frontend-dev/testing/*.json` (most use michael; advi_rolgat_group2/3
use `alex.bright@49financial.com` / `greg.rosner@49financial.com` pw `49demo*1076!`). Live-tested both,
then wrote `.frontend-dev/auth/`: `credentials.json` (surface-coverage manifest), `login-constitution.json`
(resolves the dangling config.json auth.constitutionFile ref), `README.md` (matrix + auth mechanics +
ADVI-403 open gap + CVO trace note).

**Empirical (live 6/08):**
- `michael` (admin/internal): Model Portfolios (all 3 firms) + Market YES; ADVI BOUNCES (firm=bd S3
  AccessDenied + /auth/refresh 401).
- `alex.bright` (49financial, advisorRole=local_ops): authenticates + HOLDS /advisor-intelligence
  (no bounce); header_metrics.json 200 + leaderboard.json 200 render (Assets Overview, Top Performers,
  Leaderboard). distribution.json / cohort_a_summary.json / book.json / advisors.json / header_metrics_fresh.json
  -> 403. The 403 is **S3 AccessDenied XML (application/xml) = missing-object or role-gated, NOT a
  Lambda@Edge auth denial** (firm JWT authenticates; routing correct — header_metrics+leaderboard 200
  under same firm prefix).

**Routed to COO** (their tracked auth/entitlement investigation): no agent-reachable cred currently
reaches the ADVI Distribution-tab data -> ADVI Distribution-percentile visual gates still rely on
Andrew eyeball + CVO RAVC2. Likely fix: confirm ADVI Distribution artifacts built at firm prefix, OR a
higher-advisorRole cred (architect/implementor vs local_ops). Working cred slots into credentials.json
when resolved.

## Commit scope / push
- Portal DEV `03d719d4` (3 files, .frontend-dev/auth/). DE cannot push -> DT picks up. Dev-harness
  tooling only (no deployed FE change, no PROD promote needed).

## Posture
IDLE: available. Both LD-0165 visual gates GREEN + RAVC2-accepted (COO+CVO); COO redirect complete;
CVO reconciliation self-withdrawn. No open blocker on my side.
