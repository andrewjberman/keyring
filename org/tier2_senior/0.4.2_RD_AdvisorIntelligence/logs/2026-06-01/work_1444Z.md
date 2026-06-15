# /work (manual / dispatch-handling) — 0.4.2_RD_AdvisorIntelligence~B — 2026-06-01 ~1444Z

Note: /work cron stopped by Andrew this session; this tick is manual dispatch-handling (watcher-delivered COO order + Andrew GO to proceed).

## Trigger
COO [DRIVE] 20260601T144035Z — BMKAUD WS-2 routed Andrew's "Peers UST shows no 1M" symptom to RD lane. DS~B proved data faithful → FE-side. Task: diagnose, HOLD fix.

## Diagnosis (DONE — fix held)
- ROOT CAUSE: `PeersTab.tsx:143` guard `if (!data || !data.percentiles.p95)` is a truthy test. UST 1M p95 == 0.0 in served JSON (verified s3://opal-data-portal-v2/json/peers/peer_performance.json) → `!0.0===true` → "No data available", hiding present model:0.3017 / benchmark:0.1639. Falsy-zero conflation.
- UST-specific: only model with 1M p95==0.0 (ST 1M p95=0.7018).
- Secondary same-class gate at :415 (global y-scale).
- Proposed fix (HELD): `== null` presence test instead of truthy, at :143 + :415. One-liner. Held pending audit consolidation + Andrew 1M/1Q window ruling.
- Doc: docs/briefs/bmkaud-peers-ust-1m-fe-display-diagnosis-20260601.md (CLOUD 8d3252f15).
- Read-only; no code changed; portal on DEV (Rule 19).

## Routing
RAVC2 → COO; CC → CTO. Standing by for GO / window ruling to land the fix.

## State
MDPF P1 RD-leg closed (matrix accepted; F1/F2/F5 on origin/DEV; F4 held with DE). BMKAUD diagnosis delivered. No cron (Andrew-stopped); watcher live for deliveries.
