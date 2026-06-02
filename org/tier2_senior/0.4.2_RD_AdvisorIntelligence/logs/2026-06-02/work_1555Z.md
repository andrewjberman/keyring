# work_1555Z — 0.4.2_RD_AdvisorIntelligence~B — 2026-06-02

## Tick outcome: MDPF_SCOPED.S5 IMPL_DONE (substantive)

**Session start:** /watcher healed (was NOT REGISTERED + no watcher process) → registered LIVE (PID 34988), tracked watcher relaunched. /work cron armed (737ad2a6, 7,27,47 * * * * = 20m). Consumed 2 banked COO msgs (DRIVE log-committed-under-base FYI; CTO MDPF v0.9 canonical-basis FYI) + the GO dispatch (20260602T154549Z).

**TO:** MDPF_SCOPED.S5 — external-partner login-scope fix for ModelPortfolios (Andrew-direct; CTO brief 9de86aae3; FE-only, 1-file).

**Defect:** external partner users (peter@inflectionwealth.com / Inflection) pinned to Global(All) — `selectedFirmId` defaults to `'global'` and the only control that mutates it (partner selector, L696) renders for `internal` users only.

**Fix (portal/src/pages/ModelPortfolios.tsx):**
- Added `claims` to `useAuth()` destructure + `const effectiveFirmId = internal ? selectedFirmId : (claims?.firmId ?? 'global')`.
- Routed ALL 16 downstream data-scoping/display reads through `effectiveFirmId`: both per-firm queries (timeseries + distribution) incl. React-Query cache keys (threaded consistently — no stale-Global bleed), 2 useMemo guards + dep arrays, totalAUM, Non-Model legend gate, isPerFirm, selectedFirmName, both unfunded footers, both chart re-mount keys, data-source firm label.
- `selectedFirmId` now references ONLY: useState decl, effectiveFirmId derivation, selector value/onChange. Selector stays gated to `internal` (external = no selector, locked to firm). Internal unchanged → no regression. Generalizes to any external partner.

**Contingency cleared:** claims.firmId present in /auth/me (AuthContext.tsx:136); AdvisorIntelligence index.tsx:42 already scopes external off it. No AE task.

**Verification (AC5 GREEN):** `tsc -b --noEmit` exit 0; `eslint .` exit 0 (0 errors, 0 new warnings — only pre-existing L74 unused-var).

**Commit/push:** portal 99d049d9 (origin/DEV, caebae0d..99d049d9). D-1 adapter-threading gate PASS (no-op; no api/endpoints/*.ts changed). [First push attempt was blocked by an `MSYS_NO_PATHCONV=1` path-conversion bug in the pre-push hook's gate-script resolution — NOT a real adapter violation; succeeded without it.]

**Closure:** = VISUAL SMOKE GATE (AC1-AC4 rendered-pixel) by Andrew / CTO-with-Andrew (headless-Chrome FE smoke fabric-down). PROD promotion HELD per Rule 19 until visual-smoke approves. RAVC2'd to CTO + COO (155534Z / 155543Z).

**Out-of-scope deferred:** account-distribution donut MODEL(1a)-scope "model accounts" label note (COO flagged "don't scope-creep; S5 ACs are the gate") — not a trivial static-string add (donut center label is state-driven); left as separate FE-presentation follow-up.

**Blockers:** none.
