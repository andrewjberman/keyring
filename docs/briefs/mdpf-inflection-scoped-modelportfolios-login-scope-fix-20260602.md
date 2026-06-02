# Scoping Brief — Inflection-scoped Model Portfolios login-scope fix (MDPF_SCOPED)

**Author:** 1.0.0_SA_CTO (ws CTO)
**Date:** 2026-06-02
**Anchor:** Andrew direct 2026-06-02 — "When I sign in to the portal as peter@inflectionwealth.com, I'm not seeing the scoped Inflection Wealth Management Model Portfolios page; I see the Global (All) view that was designed for Opal. That needs to be fixed. Scope it and hand off a document for COO to decompose and have MSTR spawn any necessary agents."
**Project:** MDPF_SCOPED (active) — final FE-scope defect on the close path
**Handoff:** -> 2.0.0_SA_COO to decompose into TO(s); MSTR to spawn the FE lane.

---

## 1. Defect

An external partner user (`peter@inflectionwealth.com`, Inflection Wealth Management) logs into the portal, opens **Model Portfolios**, and sees the **Global (All)** view (designed for Opal/internal) instead of the **firm-scoped Inflection Wealth Management** view (7 Inflection models, per-firm donut / trend / bell-curve).

## 2. Root cause — SINGLE, portal-side (case b: firm mapped, page doesn't consume it)

`portal/src/pages/ModelPortfolios.tsx`:
- **L257-258:** `const { isInternal, isDev } = useAuth(); const internal = isInternal() || isDev()` — destructures ONLY `isInternal`/`isDev`. **Never reads `claims` / `claims.firmId`.**
- **L259:** `const [selectedFirmId, setSelectedFirmId] = useState<string>('global')` — scope **unconditionally defaults to `'global'`** for every user.
- **L696:** the partner selector (the only control that mutates `selectedFirmId`) renders **only when `internal` is true** (`actions={internal ? (...selector...) : undefined}`).
- Every per-firm data branch keys off `selectedFirmId !== 'global'` (L267, L277, L380, L452, L568, L641, ...). A non-internal user can never move `selectedFirmId` off `'global'`, so they are **permanently pinned to Global (All)**.

This is **not Inflection-specific** — ANY external partner user (e.g. a 49 Financial external user) hits the same wall on Model Portfolios. The fix must be general (consume the auth-resolved firm), not an Inflection special-case.

## 3. Proven in-repo fix pattern (this is the key de-risk)

`portal/src/pages/AdvisorIntelligence/index.tsx:37-42` already does this **correctly** and is live:
```ts
const { isInternal, isDev, claims } = useAuth()        // <-- also destructures claims
const internal = isInternal() || isDev()
const [selectedFirmId, setSelectedFirmId] = useState<string>('49financial')
const firmId = internal ? selectedFirmId : (claims?.firmId ?? '49financial')
```
ModelPortfolios is missing exactly this `internal ? selectedFirmId : claims.firmId` resolution. The fix is to mirror it (with the `'global'` adaptation in §5).

## 4. What is NOT broken (verified — no backend/DE/auth work in scope)

- **Backend provisioning is correct.** `opal-users-v2` authoritative base-table record for `peter@inflectionwealth.com` carries `firmId: "inflection"` (name "Peter Lee", tier advisor, status active, lastLogin 2026-06-02T14:29Z). *(Note for whoever re-checks: the `email-index` GSI is `KEYS_ONLY`, so a GSI query returns `firmId: null` — a projection artifact, NOT the real value. Read the base table via `PK=USER#<email>, SK=PROFILE`.)*
- **`claims.firmId` flows end-to-end.** Proven transitively: the AdvisorIntelligence page already renders the Inflection-scoped partner view for external Inflection users off `claims.firmId` (`AdvisorIntelligence/index.tsx:28-31,42`). If `claims.firmId` were not populated, AdvisorIntelligence would also be broken — it is not. So the auth -> claims pipeline is healthy.
- **Inflection tenant config + data plumbing already exist:** `inflection` is in `ALL_MDPF_PARTNER_FIRMS` (`ModelPortfolios.tsx:154`), `firmAccess.ts` allows `/portfolios` for inflection (L31-43) + maps the domain (L92), and the per-firm endpoints are typed for `'inflection'` (`getMdpfAggregateAUATimeSeriesByFirm` L266, `getAccountDistributionByFirm('49financial'|'inflection')` L277). The Inflection-scoped Model Portfolios data path is ready; only the default-scope wiring is missing.

**Net: this is a one-file portal/FE fix, no backend, no data, no infra.**

## 5. Fix shape (for the implementing lane)

Mirror the AdvisorIntelligence pattern, adapting for the synthetic `'global'` id (which is NOT in `claims.firmId` space — claims is `'inflection'` | `'49financial'` | `'opal-capital'`):
```ts
const { isInternal, isDev, claims } = useAuth()
const internal = isInternal() || isDev()
const [selectedFirmId, setSelectedFirmId] = useState<string>('global')   // internal selector state
// effective scope: internal users drive it via the selector; external users are locked to their firm.
const effectiveFirmId = internal ? selectedFirmId : (claims?.firmId ?? 'global')
```
Then route all downstream data-scoping reads through `effectiveFirmId` instead of `selectedFirmId` (every `selectedFirmId !== 'global'` branch, the two per-firm queries, the donut/trend/bell-curve scoping). Keep the selector gated to `internal` (external users get no selector — correct; they are locked to their firm). `internal` users keep today's behavior (selector + Global default).

Implementer nuance to confirm during build: `'opal-capital'` always satisfies `isInternal()`, so external `claims.firmId` is only ever a partner slug that already matches the page's id space (`'inflection'`/`'49financial'`). No id translation needed beyond the internal->`'global'` default. Verify no other code path assumes `selectedFirmId` is the *selector* state where it should now read `effectiveFirmId`.

## 6. Proposed decomposition (COO to finalize)

- **TO-1 (FE, primary):** Wire `ModelPortfolios.tsx` to consume the auth-resolved firm for external users (§5). Generalize (all external partners, not Inflection-only). Owner: the MDPF FE lane — **0.4.2_RD_AdvisorIntelligence~B** is the natural owner (authored the MDPF_SCOPED S1 partner-mode scaffold + the 2026-05-29 reopen D1/D2/D3 fixes, and owns the AdvisorIntelligence reference page). Effort: small (single-file, proven pattern).
- **TO-2 (verification, gating):** Visual smoke gate per scoped view (see §7). Not a data-layer check.

No AE/DE/DS TO required (backend + data verified clean). If during build the implementer finds `claims.firmId` is *not* arriving in the `/auth/me` payload (contradicting the AdvisorIntelligence evidence), that single contingency would add a small AE task to project `firmId` into `/auth/me` — flagged as a low-probability contingency only.

## 7. Acceptance / closure gate (VISUAL smoke — not data-layer)

Per the portal-closure discipline (correct data + broken FE passes every data gate but fails the user — `feedback_portal_closure_needs_visual_smoke_not_just_data_verification`), this is a **rendered-pixel** defect and MUST close on a visual smoke gate (Andrew or /frontend-dev), not S3/data verification:
- [ ] AC1 — Log in as `peter@inflectionwealth.com` -> Model Portfolios shows the **Inflection Wealth Management scoped** view (7 Inflection models; per-firm donut + trend + bell-curve re-scoped), NOT Global (All).
- [ ] AC2 — A **49 Financial external** user lands on the 49F-scoped view (generality check), NOT Global.
- [ ] AC3 — An **internal/Opal** user (or isDev) still gets the partner selector + Global (All) default (no regression).
- [ ] AC4 — External user sees **no** partner selector (locked to their firm); switching is internal-only.
- [ ] AC5 — typecheck/lint green; portal DEV `ci.yml` GREEN before any PROD promotion (deploy via the canonical 5-phase "deploy prod" procedure; Rule 19 worktree).

## 8. Blast radius / risk

- Low. Single file, additive logic, mirrors a live page. The only behavior change for INTERNAL users is none (they keep selector + Global default). External users move from Global -> their firm scope (the intended fix). React-Query keys already include `selectedFirmId`; switching the scoping variable to `effectiveFirmId` must be threaded consistently so cache keys reflect the effective scope (avoid a stale Global cache bleeding into a firm view) — call out in the TO.
- Touches `portal/` (submodule, DEV). Deploy follows the canonical "deploy prod" 5-phase procedure once Andrew/visual-smoke approves.

## 9. References
- Bug site: `portal/src/pages/ModelPortfolios.tsx:257-259, 696`
- Reference pattern: `portal/src/pages/AdvisorIntelligence/index.tsx:37-42`
- Auth/claims: `portal/src/contexts/AuthContext.tsx:110-142, 551-553`; `AuthContext.context.ts:26-32`
- Firm config: `portal/src/lib/firmAccess.ts:31-43, 90-97`; `ModelPortfolios.tsx:151-155`
- Backend verify: `opal-users-v2` PK=`USER#peter@inflectionwealth.com` SK=`PROFILE` -> firmId=`inflection`
- Project: MDPF_SCOPED (this is the last FE-scope defect on the close path; sits alongside the 2026-05-29 reopen D1/D2/D3 lineage)
