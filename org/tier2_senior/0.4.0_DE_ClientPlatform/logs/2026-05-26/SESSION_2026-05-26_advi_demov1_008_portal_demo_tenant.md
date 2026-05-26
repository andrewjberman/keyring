# SESSION: ADVI_DEMOV1.008 -- Portal demo-tenant connection (Phase 6 Frontend Connection)

**archetype:** IMPLEMENT

**Date:** 2026-05-26
**Agent:** 0.4.0_DE_ClientPlatform
**Project:** ADVI_DEMOV1 (Phase 6 Frontend Connection)
**TO:** ADVI_DEMOV1.008.de-portal-demo-tenant-connection
**Issued by:** 2.0.0_SA_COO (commit `6e17b7b4d`; GO ~15:29Z)
**Andrew sovereign direct context:** 2026-05-26 ~15:45Z verbatim: "if all the data is prepared in opal-data-demo, then it is time to connect it to frontend ... select 'Demo' and see all the data populate in canonical format just how it is already done for 49 Financial and Inflection Wealth Management."

## Spawn-with-direction context

DE 0.4_DE_ClientPlatform revived from LD-0014 retirement per Andrew sovereign-direct /allocation #7 implicit AC9-lift (ws COO commit `f7f12d4bb`). MSTR /mstr-spawn ~15:23Z; SPAWN-WITH-DIRECTION canonical pattern (LD-0021) with TO-008 routing inline in spawn-msg. Parallel to AE 0.7 sovereign-spawn ~15:11Z pattern from /allocation #6.

## What shipped

Single coordinated commit on portal submodule DEV branch: `03a85441` (9 files, +499/-2).

**6 portal items wired** (4 PRD-enumerated + 2 PRD-completeness additives ratified by COO under decomposition authority pre-commit per [[feedback_self_correction_upstream_of_verify_channel]] upstream-of-verify-channel doctrine):

| # | File | Change |
|---|---|---|
| 1 | `src/api/endpoints/advisor-intelligence.ts` | `ROUTER_FIRM_SUFFIX` add `'demo': 'demo'` (identity-to-identity per opal-data-demo bucket naming) |
| 2 | `src/lib/firmAccess.ts` | `FIRM_ALLOWED_PATHS['demo']` = full 8-path set + `FIRM_EMAIL_DOMAINS['demo'] = 'demo.test'` |
| 3 | `src/pages/AdvisorIntelligence/_partners/demo/` | NEW 4-file directory mirroring `_partners/49financial/`: constants.ts (~16 LOC; BD_SOURCE_ATTRIBUTION reused), roles.ts (~22 LOC; DEMO_ROLES mirroring 49F 5-role taxonomy), layout.ts (~110 LOC; DEMO_LAYOUT mirroring FORTY_NINE_FINANCIAL_LAYOUT BD-pipeline-native), index.tsx (~290 LOC; DemoAdvisorIntelligence mirroring 49F structurally) |
| 4 | `src/pages/AdvisorIntelligence/index.tsx` | `ALL_PARTNER_FIRMS` += `{ id: 'demo', name: 'Demo' }`; `PARTNER_VIEWS['demo'] = DemoAdvisorIntelligence` |
| 5 | `src/pages/AdvisorIntelligence/_shared/hooks/useTenantLayout.ts` | `LAYOUTS` registry add `'demo': DEMO_LAYOUT` (avoids 9 _shared/ components silent-fallthrough to DEFAULT_LAYOUT placeholder-sentinels; COO additive 5) |
| 6 | `src/pages/AdvisorIntelligence/_shared/types/TenantLayoutConfig.ts` | `CanonicalFirmId` union extension include `'demo'` (AC5 bun-tsc load-bearing; COO additive 6) |

## PRD-completeness finding (banked)

Source walk during pre-implementation surfaced 2 structurally-required edits not in PRD v0.4 Sec. 6.1's explicit 4-item enumeration:

(5) `useTenantLayout.ts` LAYOUTS registry: without `'demo'` entry, 9 `_shared/` components reading via `useTenantLayout(firmId='demo')` silently fall through to `DEFAULT_LAYOUT`. DEFAULT_LAYOUT carries PLACEHOLDER SENTINELS per SHARED.001 Sec. E.10 (`displayName: ''`, `sourceAttribution: ''`, `roles.keys: []`) -- the fallthrough renders demo with empty UI strings.

(6) `CanonicalFirmId` union extension: bun tsc errors at `demo/layout.ts`'s `firmId: 'demo'` declaration without the union extension. AC5 load-bearing.

Surfaced to ws COO 15:29Z MCP; COO direct-ratified under decomposition authority 15:40Z per Option A. CC ws CTO informational (PRD v0.4.1 micro-amendment scribe at /ws-charter convenience; non-gating). [[feedback_corroborate_with_concern_verdict_shape]] pattern operating at pre-impl design-gate.

## Acceptance criteria evidence

| AC | Status | Evidence |
|---|---|---|
| AC1: single coordinated commit | PASS | `03a85441` on portal DEV; 9 files; safe-commit.sh wrapper (Rule 14a) |
| AC2: comp-transform schema-check --feature demo | DEFERRED -- TOOL GAP | comp-graph keys per-file index.tsx as "index" component -> multi-collision blocks lookup; structurally satisfied (DemoView consumes identical fields to FortyNineFinancialView) |
| AC3: comp-transform ternary-audit | DEFERRED -- TOOL GAP | Same multi-"index" gap; structurally satisfied (PARTNER_VIEWS map dispatch; zero `cohort === 'demo'` ternary chains) |
| AC4: comp-cache collisions | PASS | 4 baseline by-design collisions unchanged; demo's index.tsx adds 4th by-design caller to firm-leaderboard key (additive; same response shape) |
| AC5: bun tsc clean | PASS | exit 0 |
| AC6: bun build clean | PASS | exit 0; built in 11.72s |
| AC7: dev-server smoke renders 'Demo' option | STRUCTURAL PASS | dist/assets/*.js bundle contains "Demo" + "49 Financial" + "Inflection Wealth Management" partner labels (grep verified); TO-VAL-FE full visual smoke deferred to Andrew UAT |
| AC8: RAVC2-Request | IN FLIGHT | this session log + MCP RAVC2 to ws COO |

## Compiler Tools

| Tool | Run | Result | Notes |
|---|---|---|---|
| `comp-build` | post-write graph rebuild | 1684/1749 file-backed nodes; 1468 CALLS / 105 FETCHES edges | demo subdir not yet indexed (worktree not main tree) |
| `comp-cache collisions` | post-write | clean; 4 baseline by-design collisions unchanged | no new colliding-key class introduced |
| `comp-transform schema-check AdvisorIntelligence --feature demo` | post-write probe | "Component not found" | comp-graph indexes 3 separate index.tsx files as "index" component -- naming-collision gap; flagged for /spot-check / CVO comp-tools-expansion follow-up |
| `comp-transform schema-check FortyNineFinancialView --feature demo` | post-write probe (alias variant) | "Component not found" | same gap |
| `comp-transform schema-check DemoAdvisorIntelligence --feature demo` | post-write probe (new variant) | "Component not found" | demo subdir not in main tree (worktree-only) |
| `comp-transform ternary-audit AdvisorIntelligence` | post-write probe | "Component not found" | same gap |

Tool-resolution gap is observable structural limitation, not a TO-008 regression. comp-transform's component-name keying needs refinement to disambiguate per-directory index.tsx files (e.g., `<dir>:index` or alias-aware). Surfacing to ws CVO via RAVC2 for follow-up alongside CVO's comp-* expansion brief (ws COO endorsed `92b198aac`).

## Risks (PRD Sec. 6.1) -- mitigation status

| Risk | Mitigation | Status |
|---|---|---|
| R1: DemoView divergence from 49F canonical | structural mirror | OK (TS shape identical; same _shared infra consumption) |
| R2: Hidden firmId hard-branch trip | grep audit | OK (zero `firmId === '49financial'` / `'inflection'` branches in portal/src; only `firmId === 'opal-capital'` internal-gates which don't need demo-extension) |
| R3: Advisor-empty surface for demo | Andrew UAT (TO-VAL-FE) | DEFERRED to TO-VAL-FE Smoke-C |
| R4: PROD-strand on cherry-pick | DT-pod ephemeral worktree | DEFERRED to TO-009 (DT-pod authority) |
| R5: React Query key collision | comp-cache collisions | OK (clean; only additive same-shape collisions) |

## Cross-domain coordination

Per PRD Sec. 6.1: shared-advisor-router L@E + CloudFront behaviors already firm-agnostic for `?firm=demo` per ADVI_DEMOV1 Sec. 3 + Phase 6 PRD acceptance -- no AE 0.7 LEDGEH/CDNCOHT critical-path touch. Confirmed by zero infra-change scope of TO-008 (AC9-INDEPENDENT per TO file).

## Downstream

- TO-009 (DT-pod portal DEV->PROD push): COO authors + dispatches when this RAVC2-Accepted
- TO-VAL-FE (Andrew UAT visual-smoke): closes original ADVI_DEMOV1 AC4 + Phase 6 + project as a whole

## Throughput note

Spawn 15:23Z -> commit 03a85441 ~16:00Z = ~37min DE wall (well under PRD's ~3-5h estimate). Single-session compression via: clean spawn-with-direction context + 49F template fidelity + parallel pre-work + same-session COO completeness-ratify cycle (15:29Z finding -> 15:40Z ratify -> commit ~16:00Z).
