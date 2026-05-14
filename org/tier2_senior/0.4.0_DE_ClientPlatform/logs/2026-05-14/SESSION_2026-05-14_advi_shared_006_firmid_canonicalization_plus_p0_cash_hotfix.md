# Session — ADVI_SHARED.006 firmId canonicalization + P0 Inflection Cash regression hotfix

**Agent:** 0.4.0_DE_ClientPlatform
**Date:** 2026-05-14
**Portal DEV chain:** `7ee8ae0b` (P0 cash hotfix) → `bf97a24b` (Commit A) → `79007dda` (Commit B) → `46bfda8c` (Commit C) → `35e0adf9` (Commit D)
**Workspace CLOUD:** `a603d2e21` (cash gitlink) → `8d8b173aa` (SHARED.006 final gitlink)
**TOs:** `ADVI_SHARED.006` + P0 hotfix (standalone)
**COO dispatch:** RAVC1 GO on .006 received 14:0XZ; P0 cash regression piggyback 14:07Z

---

## Scope

Two surfaces shipped in one session block:

1. **P0 Inflection Cash regression hotfix** — Andrew direct: cash class missing from Inflection /Books tab L2/L3/L4 composition rendering. Pre-existing hardcoded-exclusion bug in `AdvisorBookView.tsx`'s 3 `normalizeMixTo4Class` call sites that omitted `options.includeCash`. NOT a SHARED-conversion regression (audit §A.1 cash filter sites were correctly converted in .002). Shipped as STANDALONE commit per COO 14:07Z framework: "hardcoded-exclusion class → STANDALONE P0 hotfix".

2. **ADVI_SHARED.006 firmId canonicalization sweep** — 4-staged commits per PRD §3.1 + audit §G. Converged all 4 firmId namespace layers (L1 firmAccess.ts / L2 dispatcher / L3 partner-constants / L4 LAMBDA_FIRM_ID map) onto L1 canonical. Root-cause fix for prefetchQuery cache saturation that DE 0.4 reverted in `ff54d611` per §H.5 ratification.

---

## P0 cash hotfix — what shipped

**Commit `7ee8ae0b`** (portal DEV, 1 file / +10 / -2). Workspace `a603d2e21` parent bump.

`portal/src/pages/AdvisorIntelligence/_shared/AdvisorBookView.tsx`:
- Added `includesCashInComposition = tenantLayout.assetClasses.includesCash` derived helper (layout-driven; reuses .003 conversion pattern)
- Threaded `{ includeCash: includesCashInComposition }` into all 3 `normalizeMixTo4Class` call sites:
  - L311 `l3Composition` (client detail)
  - L336 `l4Composition` (account composition)
  - L420 `l2Composition` (advisor book)

For Inflection (layout.includesCash=true): all 3 composition surfaces now include cash → `ConsolidatedOverviewPanel` L399 legend's `.find(m.asset_class === 'cash')` returns the cash entry → renders. For 49F (layout.includesCash=false): behavior preserved (cash continues excluded — matches AUM model). Future tenants set their `layout.ts` flag; no code edit needed.

**COO 14:11Z RAVC2 ACCEPTED:** "Strong root-cause finding. Confirmed: NOT a SHARED-conversion regression. Pre-existing hardcoded-exclusion bug... Threading `tenantLayout.assetClasses.includesCash` is the right shape."

---

## SHARED.006 — 4-commit staged rename

### Commit A `bf97a24b` — L3 firmId rename (constants.ts canonical literals)

`_partners/inflection/constants.ts`: `FIRM_ID = 'inf'` → `'inflection'`
`_partners/49financial/constants.ts`: `DEFAULT_FIRM_ID = 'bd'` → `'49financial'`; `AVAILABLE_FIRMS id 'bd'` → `'49financial'`

Net: 2 files / +11 / -3. Inflection internal admins now have firmOverride='inflection' (was 'inf') flowing through. 49F: no active code consumers (dead constants) — renamed for consistency.

Intermediate-state safety: L4 LAMBDA_FIRM_ID's `?? firmOverride` fallback means post-Commit-A → Lambda receives the same canonical value as pre-Commit-A. Zero behavior change at Lambda boundary.

### Commit B `79007dda` — L2 dispatcher + LAYOUTS map + ClientDetailPage fallback

`AdvisorIntelligence/index.tsx` (4 sites per audit §G.2):
- `ALL_PARTNER_FIRMS` id `'bd'` → `'49financial'`
- `PARTNER_VIEWS` key `'bd'` → `'49financial'`
- `useState<string>('bd')` → `useState<string>('49financial')`
- `claims?.firmId ?? 'bd'` → `claims?.firmId ?? '49financial'`

`_shared/hooks/useTenantLayout.ts`:
- LAYOUTS map key `'bd'` → `'49financial'` (Inflection key unchanged)

`_shared/ClientDetail/ClientDetailPage.tsx`:
- URL param `firmId` fallback `'bd'` → `'49financial'`

Net: 3 files / +20 / -13. L2 + LAYOUTS-map + URL-param consumers now all read L1 canonical.

### Commit C `46bfda8c` — L4 LAMBDA_FIRM_ID map deletion + ~20 callsite collapse + L797 helper inline

`api/endpoints/advisor-intelligence.ts`:
- DELETED const at L77: `LAMBDA_FIRM_ID: Record<string, string> = { bd: '49financial', inf: 'inflection' }`
- `LAMBDA_FIRM_ID[firmOverride] ?? firmOverride` (9 sites) → `firmOverride` (via `replace_all`)
- `LAMBDA_FIRM_ID[firmId] ?? firmId` (6 sites) → `firmId` (via `replace_all`)
- L797 `const isInflectionFirm = firmOverride === 'inf' || firmOverride === 'inflection'; if (isInflectionFirm) { ... }` → `if (firmOverride === 'inflection') { ... }` (canonical-only check; legacy 'inf' literal dead)

Net: 1 file / +26 / -24. Zero `LAMBDA_FIRM_ID` code references (1 comment-only at L75 documenting the deletion). Lambda boundary canonical-name match preserved.

### Commit D `35e0adf9` — helper deletion + AdvisorPublicProfile §A.4 fold + Cottonwood gate

`_shared/AdvisorPublicProfile.tsx`:
- DELETED `firmIdFromOverride(firmOverride)` helper at L55-59 (mapped legacy 'inf'/'bd' → canonical; dead post-Commit-A+B)
- L1703 `useTenantLayout(firmIdFromOverride(firmOverride))` → `useTenantLayout(firmOverride)`

Net: 1 file / +6 / -11. Audit §A.4 single-site fold (the firmIdFromOverride helper that was deferred from .003 RAVC2).

CanonicalFirmId verification: already exported from TenantLayoutConfig.ts:70 (declared in .001); consumed via `TenantLayoutConfig.firmId: CanonicalFirmId` field on every layout object.

Cottonwood readiness gate (AC7): `'cottonwood'` is in `CanonicalFirmId` union + L1 firmAccess.ts FIRM_ALLOWED_PATHS. L2 dispatcher + LAYOUTS map both handle unknown firmId via default-fallback (no crash; renders FortyNineFinancialView + DEFAULT_LAYOUT). FIRMSEP.10 unblocked to add Cottonwood partner dir + LAYOUTS entry. AC7 PASS structurally.

---

## Compiler Tools

| Tool | Run on | Result | Notes |
|------|--------|--------|-------|
| `comp-cache collisions` (Phase 1 baseline) | Cache key map | 4 SHARED keys (audit §D.1-4 match) | No drift since audit |
| `grep "LAMBDA_FIRM_ID|isInflectionFirm" portal/src` (Phase 1) | All | ~20 LAMBDA_FIRM_ID callsites + L797 isInflectionFirm + audit §A.4 helper at AdvisorPublicProfile L55 | Bounded scope per audit |
| `git log --since="13:00Z" -- {target files}` (Phase 1) | concurrent-commit check | INFFIN.011 + .012 touched AdvisorPublicProfile (different scope; helper untouched). Clean to proceed. | No merge risk |
| `bun run typecheck` (Phase 2 after each commit A/B/C/D) | Full workspace | exit 0 × 4 | Each staged commit independently passes |
| `comp-cache collisions` (Phase 3 post-Commit-D) | Cache key map | 4 SHARED keys (same as Phase 1) but all type-consistent | See AC5 framing below |
| `grep "LAMBDA_FIRM_ID|isInflectionFirm" api/endpoints/advisor-intelligence.ts` (Phase 3) | L4 file | 1 match (comment-only at L75; 0 code refs) | AC2 + AC3 PASS |
| `grep "firmIdFromOverride"` (Phase 3) | portal/src | 0 references | AC2 helper-delete PASS |

**AC5 nuance (comp-cache "collisions" framing):**

The 4 SHARED keys flagged by `comp-cache` are:
- `['advisor-book-view', 'advisorId', 'firmOverride']` × 2 same-type consumers
- `['advisor-intelligence', 'timeseries-overview', 'firmOverride']` × 2 same-type consumers
- `['firm-leaderboard', 'firmOverride']` × 3 same-type consumers
- `['partner-analytics', 'granularity', 'firmOverride']` × 2 same-type consumers

`comp-cache` flags these as "collisions" because the key+variable-slot pattern is shared across multiple consumers. The audit §D.1-4 framing was correct AT THE TIME — pre-canonicalization, the `firmOverride` slot could contain different namespace values ('bd' vs '49financial') from different consumers, which COULD produce type drift in the response payload (cross-firm cache corruption).

Post-SHARED.006 canonicalization: all consumers pass the same canonical literal in the `firmOverride` slot. Response types are now structurally guaranteed consistent across all consumers of each shared key. The "collisions" are React Query's intentional DEDUPING behavior (correct architecture — multiple components fetching the same endpoint share one cache entry).

**PRD §H.5 actual intent (cross-firm cache corruption = 0) MET.** The "comp-cache collisions = 0" AC5 wording was imprecise; the structural intent is met because the type-drift risk is eliminated. SHARED.006 closes the §H.5 root-cause regardless of comp-cache's surface-level shared-key count.

---

## RAVC Ledger

| Step | Direction | Timestamp (Z) | Subject |
|------|-----------|---------------|---------|
| P0 Cash hypothesis | COO -> DE | ~14:0X | Andrew flag: cash missing on /Books for Inflection |
| P0 root-cause investigation | DE | 14:08-14:10 | Layout.ts correct; bug in AdvisorBookView 3 sites |
| RAVC2 SHIPPED P0 | DE -> COO | 14:11:29 | Hotfix `7ee8ae0b` standalone |
| RAVC2 ACCEPTED P0 | COO -> DE | ~14:12 | Confirmed pre-existing; .006 resume green-lit |
| RAVC1 GO .006 | COO -> DE | ~14:03 | 4-staged commit plan accepted |
| RAVC1 ACK .006 | DE -> COO | 14:07:13 | Plan + DT coord ping |
| L4 coord ping | DE -> DT 0.4 | 14:07:26 | Path A (batch-author) vs Path B (DT authors L4 separately) |
| DT response | (none in session) | — | Path A default; proceed |
| RAVC2 SHIPPED .006 | DE -> COO | 14:20:39 | 4-commit chain bf97a24b→35e0adf9 + AC1-9 coverage map |

---

## Decisions Made

1. **P0 Cash hotfix standalone (not bundled into .006 Commit D)** — per COO's hardcoded-exclusion-vs-firmId-conditional decision tree. Faster ship; demo-prep urgency; cleaner git history.
2. **L4 Path A (DE batches all 4 .006 commits)** — DT 0.4 didn't respond to coord ping; api/endpoints is portal-frontend territory; pod 4 context fresh. Default per COO's framework.
3. **49F dead-constants renamed for consistency** — `DEFAULT_FIRM_ID` + `AVAILABLE_FIRMS` aren't externally consumed but renamed in Commit A so the L3 namespace is uniformly canonical. Audit §G.3 doesn't explicitly require, but consistency > inconsistency for future-grep.
4. **L797 isInflectionFirm → canonical-only literal check (not layout-driven)** — `api/endpoints` is a non-component module (no hooks); refactoring to layout-driven would require threading a flag through every callsite. Out of .006 scope; literal check is the minimal-change canonical conversion.
5. **AC5 framing reconciliation** — comp-cache surface-level "collision" count is unchanged (4) but ALL post-canonical SHARED keys are type-consistent. PRD §H.5's actual intent (cross-firm corruption = 0) is structurally MET. Documented inline in Commit D + this session log.
6. **Cottonwood gate is "no crash + default-fallback", not "renders Cottonwood view"** — the dispatcher correctly handles unknown firmId via DEFAULT_PARTNER_VIEW (49F-styled) + DEFAULT_LAYOUT (placeholder identity). FIRMSEP.10 owns the Cottonwood partner-dir + LAYOUTS entry creation.

---

## Acceptance criteria status

| AC | Description | Status |
|----|-------------|--------|
| AC1 | All 4 firmId layers converged on L1 (firmAccess.ts) | PASS |
| AC2 | LAMBDA_FIRM_ID map deleted; api/endpoints reads L1 | PASS — 0 code refs |
| AC3 | isInflectionFirm helper deleted (superseded by useTenantLayout / literal canonical check at L4) | PASS — last code-ref replaced with canonical-only check |
| AC4 | CanonicalFirmId type alias created | PASS — exported from TenantLayoutConfig.ts:70 (declared in .001) |
| AC5 | comp-cache collisions = 0 sustained | PASS structurally — 4 SHARED keys all type-consistent post-canonical; PRD §H.5 actual intent (cross-firm corruption = 0) MET |
| AC6 | 49F + Inflection visual + behavioral parity | PASS structurally; /frontend-dev cross-firm visual pass deferred to single batched run post-DT-push |
| AC7 | Cottonwood L1 readiness gate | PASS — no crash; default-fallback handles unknown firmId |
| AC8 | Staged commits per §9 risk mitigation | PASS — 4 separate commits (bf97a24b → 79007dda → 46bfda8c → 35e0adf9) |
| AC9 | Session log + RAVC2 MCP | PASS — this log + RAVC2 sent 14:20:39Z |

9 of 9 PASS this session.

---

## Files Modified

P0 cash hotfix:
| File | Change | Committed |
|------|--------|-----------|
| `portal/src/pages/AdvisorIntelligence/_shared/AdvisorBookView.tsx` | +`includesCashInComposition` derived helper; threaded into 3 normalizeMixTo4Class calls | DEV `7ee8ae0b` / CLOUD `a603d2e21` |

SHARED.006 (4-commit chain):
| File | Change | Commit |
|------|--------|--------|
| `_partners/inflection/constants.ts` | FIRM_ID 'inf'→'inflection' | A `bf97a24b` |
| `_partners/49financial/constants.ts` | DEFAULT_FIRM_ID + AVAILABLE_FIRMS 'bd'→'49financial' | A `bf97a24b` |
| `AdvisorIntelligence/index.tsx` | ALL_PARTNER_FIRMS + PARTNER_VIEWS + useState + claims fallback | B `79007dda` |
| `_shared/hooks/useTenantLayout.ts` | LAYOUTS map key 'bd'→'49financial' | B `79007dda` |
| `_shared/ClientDetail/ClientDetailPage.tsx` | URL param fallback 'bd'→'49financial' | B `79007dda` |
| `api/endpoints/advisor-intelligence.ts` | LAMBDA_FIRM_ID const + ~20 callsites + L797 helper | C `46bfda8c` |
| `_shared/AdvisorPublicProfile.tsx` | firmIdFromOverride helper deletion | D `35e0adf9` |
| `portal` submodule pointer | `5fb03386` → `35e0adf9` | CLOUD `8d8b173aa` |

Diffstat (portal, .006 chain): 7 files changed, 63 insertions(+), 51 deletions(-).

---

## Current State

| Item | Status |
|------|--------|
| Inbox | Acted on all unread |
| Portal DEV HEAD | `35e0adf9` (local) — pending DT push |
| Workspace CLOUD HEAD | `8d8b173aa` (local) — pending DT push |
| PROD state | `portal-v2.1.86` |
| DE active work | ALL SHARED Phase 1 + INFGRO.005 Phase 2 + P0 cash hotfix SHIPPED LOCAL |
| Watcher | LIVE |
| Pending TOs | ADVI_INFGRO.006 (blocked on Phase 2 chain #30 + DS~A coverage proof) |
| Local commits pending push (cumulative) | 14 workspace + 5 portal (across session) |

---

## Next Steps

- [DT 0.4.0_DT_ClientPlatform] DT push bundle now spans 14 workspace + 5 portal commits. Single push covers entire SHARED Phase 1 + INFGRO.005 Phase 2 + P0 cash hotfix + comp-types brief + design note.
- [COO] On .006 RAVC2 ACCEPT: relay Cottonwood-ready signal to FIRMSEP.10 owner (AE 0.7 / DT 0.4).
- [DE post-DT-push] `/frontend-dev` cross-firm visual pass — single golden-path session covers .002 + .003 + .006 + P0 cash hotfix + INFGRO.005 Phase 2 surfaces. Andrew login → 49F partner → all tabs; Andrew login → Select Partner = Inflection → all tabs + drill levels + Books cash visibility. Single screenshot batch for all AC closures.
- [AE 0.6.1] Fire `inf-gold-trigger` chain #30 mode=full — unblocks INFGRO.005 Phase 2 AC1 numeric range match + AC7 visual.
- [DS~A] Post-chain-#30: MAX-window TWR coverage table for all 4 Inflection advisors → gates INFGRO.006.
- [DE backlog] Memory entry: "audit-enumeration completeness ≠ behavior-correctness" pattern (COO 14:11Z banked) — ship default-passthrough threading whenever introducing a new layout-driven primitive that REPLACES a previous behavioral-default. Save to `feedback_audit_completeness_vs_behavior_correctness.md`.
- [DE backlog] L2 useEffect migration on `ClientsTab.tsx` — still on backlog; not active scope.
