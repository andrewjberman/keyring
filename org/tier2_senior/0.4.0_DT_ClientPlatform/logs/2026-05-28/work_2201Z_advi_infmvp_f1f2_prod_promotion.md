# Work Cycle Log — 0.4.0_DT_ClientPlatform
**Date:** 2026-05-28T~22:01Z
**Tick class:** SUBSTANTIVE — PROD promotion on COO GO directive

## Action: ADVI_INFMVP.F1+F2 DEV→PROD promotion

**Trigger:** COO [GO — PROMOTE] inbox message (CVO client-facing GO granted).

**Scope promoted:**
- `e1bcc40e` feat(ADVI_INFMVP.F2): remove /trade-submission from Inflection allowlist
- `7c03cd4b` fix(ADVI_INFMVP.F1): Assets Overview all-zeroes for Inflection external users

**Promotion steps:**
1. Rollback SHA captured: `7bc97151`
2. Ephemeral worktree: `C:/c/Users/.../portal-prod-promo` (Rule 19 — main tree stays DEV)
3. Fast-forward local PROD to origin/PROD (`7bc97151`) via merge
4. Merge origin/DEV → PROD (no-ff): commit `b7acadab`
5. Push origin/PROD: `7bc97151..b7acadab` (typecheck exit 0 via pre-push PROD gate)
6. Tag: `portal-v2.1.103`
7. Worktree removed; main portal tree confirmed DEV at `06328859`
8. Parent repo gitlink bumped: `19ea88ce7` on CLOUD; pushed `ca9a1ae34..c8f4f02f9` → `c8f4f02f9`

**Reported to:** COO + CC CTO + CVO (all delivered via broker)

**Smoke pending:** Real Peter-login by Andrew/QA (external JWT path — cannot simulate locally).

## TO Queue this tick
- ADVI_INFMVP.F1: `complete` (investigation+fix done prior session; promotion done this tick)
- ADVI_DEMOV1.VAL-FE: `pending — Andrew UAT engagement` (gated standby; no SLA)
