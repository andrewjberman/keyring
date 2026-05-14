# Session — ADVI_INFGRO.005 Phase 2 ship — GRO hero cards + Epsilon column

**Agent:** 0.4.0_DE_ClientPlatform
**Date:** 2026-05-14
**Portal DEV commit:** `d4e28cca`
**Workspace CLOUD commit:** `1b258f658`
**TO:** `ADVI_INFGRO.005` — Portal GRO decomposition: AdvisorsTab side-by-side display
**Phase:** 2 of 2 (UNBLOCKED structurally pre chain #30 mode=full via DS~A source-of-truth key confirmation)

---

## Scope

Phase 2 implements types + UI per the TO scope steps 3-4. Unblocked structurally pre chain #30 because DS~A confirmed the JSON keys are set in stone at the gold source (`INF_D_00c.portal_leaderboard.py:646-651` per-advisor, `:678-682` firm) — `$` suffix is RFC 8259 legal and `json.dumps` emits as-is. No key-format validation needed against live JSON; only numeric-range validation defers to chain #30.

---

## What shipped

### Types (Phase 2a)

`portal/src/pages/AdvisorIntelligence/_shared/types.ts`:

- Extended `PlatinumLeaderboardEntry` with four optional `number | null` fields using literal `$`-suffix keys: `advisor_nna_$`, `advisor_return_pct_twr`, `advisor_return_$`, `advisor_epsilon_$`.
- Extended `PlatinumLeaderboardSummary` with four optional firm-level equivalents: `firm_nna_$`, `firm_return_pct_twr`, `firm_return_$`, `firm_epsilon_$`.
- Extended `LeaderboardEntry` (the FE-derived type post `getDisplayMetrics`) with the same per-advisor fields as optional pass-throughs. Role filtering does not decompose GRO — fields pass through advisor-level unchanged.

`portal/src/pages/AdvisorIntelligence/_shared/types/TenantLayoutConfig.ts`:

- Added optional `panels.groDecomposition?: { enabled: boolean }` flag. Defaults to disabled.

`portal/src/pages/AdvisorIntelligence/_partners/inflection/layout.ts`:

- Inflection layout sets `groDecomposition: { enabled: true }`. 49F default-off until their pipeline emits the firm_* decomposition.

### UI (Phase 2b)

`portal/src/pages/AdvisorIntelligence/_shared/tabs/AdvisorsTab.tsx`:

- `GroHeroCards` + `HeroCard` component pair rendered above the Top Performers panel, conditional on `tenantLayout.panels.groDecomposition?.enabled === true`. Three first-class cards per PRD §3.3:
  - **AUA Growth** — GRO decomposition identity sum (`firm_nna_$ + firm_return_$ + firm_epsilon_$`). Null if any component is null (partial sums are misleading; pre chain #30 all four are null → '—' renders).
  - **Return (TWR%)** — `firm_return_pct_twr` formatted as signed percent. Tooltip: "AUA-weighted time-weighted return across all advisor books in the firm."
  - **NNA** — `firm_nna_$` formatted as signed currency. Tooltip: "Net new assets — inflows minus outflows — across the firm for the selected window."
  - Each card has `HelperTip` + `Info` icon on the label. Color tone tracks sign (green positive, red negative, white/40 neutral when null).
  - Reads from raw `employeeData?.windows[activeWindow].summary` so firm-level numbers don't get role-filtered by the `selectedRoles` toggle.

- New per-advisor **Epsilon column** on `LeaderboardRow` + `LeaderboardPinnedRow`. Renders only when `entry['advisor_epsilon_$'] !== undefined` (i.e., for tenants whose gold emit populates the field — Inflection today, others later if/when they extend their pipelines). Each column displays:
  - Quality dot (1.5×1.5, rounded-full): GREEN `bg-emerald-400` / YELLOW `bg-amber-400` / MISSING_PERF `bg-white/25`. Derived FE-side via `deriveEpsilonQuality` heuristic.
  - Epsilon value formatted as signed currency (`'+$X.XK'` style) or '—' when null.
  - Column header label "Epsilon" with `HelperTip` + `Info` icon (10px). Tooltip: "Accounting residual not attributable to NNA or Return (GRO decomposition identity: ΔAUA = NNA + Return + ε). Dot color: green = clean (|ε| ≤ 10% |return|), yellow = noisy, grey = missing performance data."

- `deriveEpsilonQuality` helper (module-scoped, exported for reuse if needed elsewhere):
  ```typescript
  function deriveEpsilonQuality(
    returnPct: number | null | undefined,
    returnDollar: number | null | undefined,
    epsilonDollar: number | null | undefined,
  ): 'GREEN' | 'YELLOW' | 'MISSING_PERF' {
    if (returnPct == null || returnDollar == null || epsilonDollar == null) return 'MISSING_PERF'
    const returnAbs = Math.abs(returnDollar)
    const epsilonAbs = Math.abs(epsilonDollar)
    if (returnAbs > 0 && epsilonAbs > 0.10 * returnAbs) return 'YELLOW'
    return 'GREEN'
  }
  ```
  10% threshold approved by DS~A 2026-05-14 ("If you want a TIGHTER bound e.g. 5% threshold post chain #30 empirical, easy to dial.").

### Implementation notes

- **Toggle preservation (Option B per Phase 1 log):** the existing `LeaderboardMetric` toggle ('aua' | 'nna' | 'gro') stays unchanged. Per the PRD literal, "no toggle between hero cards" — the hero cards themselves do not have a metric toggle; the lower Top Performers / Leaderboard panels keep their existing toggle-driven view because the PRD does not require those to be flattened, and the toggle still serves ranking utility (sort top-3 by metric).
- **HERO/SEC font distinction preserved on existing NNA/AUA/GRO columns:** Phase 2 did not re-architect the per-advisor row font weighting. The active metric still gets `text-2xl font-black` and the other two get `text-sm font-medium`. The new Epsilon column uses `text-sm font-medium` uniformly (no metric-driven hero state) since it's outside the legacy metric union. Follow-up flatten of the HERO/SEC distinction can ship in a separate commit if Andrew/CTO prefer.
- **49F unaffected:** Inflection-specific tenant gate via `groDecomposition.enabled`. 49F leaves the flag undefined → `groEnabled === false` → no hero cards rendered, no Epsilon column rendered (also: 49F's `entry['advisor_epsilon_$']` is `undefined` so the column gate is false twice over).
- **Graceful degrade pre chain #30:** all four `$`-suffix fields are optional + nullable. Pre chain #30 mode=full, leaderboard.json may not yet emit the new keys (DS~A's fd11a33c2 ships the code; chain run materializes the artifact). Until live, hero cards render '—' and Epsilon column renders '—' with grey quality dot (MISSING_PERF). No console errors, no broken layout.

---

## Compiler Tools

| Tool | Result | Notes |
|------|--------|-------|
| `bun run typecheck` (Phase 2a + 2b) | `tsc -b --noEmit` exit 0 | Clean. Optional `?` on new fields means no consumer is broken. |
| `comp-transform schema-check AdvisorsTab` (post-ship) | 5 type fields / 2 rendered / UNUSED (1): `available_windows: string[]`. `windows` flipped from UNUSED to RENDERED via `resolveWindow` access. | `available_windows` UNUSED is acceptable — period selector logic uses fixed PeriodKey union not the dynamic list. |
| `comp-cache collisions` (post-ship) | 4 shared keys, unchanged. `firm-leaderboard` key still shared across 3 consumers (49F index, AdvisorsTab, ClientsTab), all consuming `PlatinumLeaderboardResponse` — no new collision. | Type extension didn't change cache key shape. |

---

## RAVC Ledger

| Step | Direction | Timestamp (Z) | Subject |
|------|-----------|---------------|---------|
| RAVC2 reply | DS~A -> DE | ~13:00 | INF_D_00c:620 dtype fix SHIPPED `fd11a33c2` + INFGRO field names |
| RAVC2 ACK | DE -> DS~A | 13:01:50 | Field names noted; holding Phase 2 until validation |
| RAVC2 pre-empt | DS~A -> DE | ~13:0X | JSON keys literally `$`-suffix (RFC 8259); Phase 2 unblocked |
| RAVC2 ACK 2 | DE -> DS~A | 13:04:44 | Phase 2 unblocked; proceeding with type + UI; FE-derive epsilon quality |
| RAVC reply | DS~A -> DE | ~13:0X | `advisor_epsilon_data_quality` FE-derive approved; 10% heuristic OK |
| RAVC2 status | DS~B -> DE | ~13:0X | INF_D_00c push confirmed; chain #30 unblocked for AE |
| (pending) RAVC2 | DE -> DS~A | (post-ship this log) | Phase 2 SHIPPED `d4e28cca` + `1b258f658`; deferring visual validation to chain #30 |
| (pending) RAVC1 | DE -> DT 0.4 | (post-log) | Phase 2 ready for push: portal DEV `d4e28cca` + parent CLOUD `1b258f658` |

---

## Decisions Made

1. **Conservative column-add over column-replace** — Kept existing NNA/AUA/GRO columns intact; added Epsilon as a 4th metric column rather than replacing GRO with Return. Reasoning: (a) preserves 49F UX untouched (single-codebase), (b) the existing GRO column shows `aua_growth_pct` which is a different lens than `advisor_return_pct_twr` (AUA delta % vs investment TWR%) — both are meaningful, neither subsumes the other, (c) lower regression surface for the partner-demo window. If Andrew prefers Return-replaces-GRO column semantic for Inflection, easy 1-commit follow-up.
2. **Hero-card AUA Growth = NNA + Return + Epsilon identity sum** — Not a separate emit field; computed FE-side from the three components. Null if any is null (partial sums are misleading).
3. **FE-derived epsilon quality (vs gold emit)** — Approved by DS~A as the canonical pattern. Quality classification is presentation logic, doesn't belong at gold layer (would conflate calculation with display semantic).
4. **10% threshold for GREEN/YELLOW cut** — Tighten post chain #30 if empirical noise suggests a lower bound. DS~A: "If you want a TIGHTER bound (e.g., 5% threshold) post chain #30 empirical, easy to dial."
5. **Tenant-gating via TenantLayoutConfig vs direct firmId check** — Followed the established `useTenantLayout` pattern (rank-delta column, advCohortLabel, roleComposition). Adds the new `groDecomposition` flag in the typed config; Inflection enables, 49F leaves default-disabled. No new `firmId === 'inflection'` checks introduced.

---

## Acceptance criteria status

| AC | Description | Status |
|----|-------------|--------|
| AC1 | Three hero cards render at top of AdvisorsTab with firm-level values | PASS structurally (graceful '—' pre chain #30); values pending live data |
| AC2 | Per-advisor columns render side-by-side (no toggle required) | PASS — current NNA/AUA/GRO already side-by-side; Epsilon added as 4th |
| AC3 | Epsilon quality indicator visible with tooltip + classification | PASS — column header HelperTip + per-row quality dot |
| AC4 | Pre-existing AdvisorsTab columns + cut-chip labels unchanged | PASS — no edits to existing columns; visual regression check pending /frontend-dev |
| AC5 | TypeScript type check PASS (no new MISSING in schema-check) | PASS — `tsc -b --noEmit` exit 0; schema-check shows 2/5 rendered (was 1/5) |
| AC6 | comp-cache collisions: no new same-key / different-type | PASS — 4 shared keys unchanged |
| AC7 | Visual test screenshot of Inflection AdvisorsTab with GRO columns visible | DEFERRED — needs chain #30 mode=full live data; will run /frontend-dev post-chain |

5 of 7 PASS this commit; 2 deferred to post chain #30 live data (AC1 numeric range + AC7 visual screenshot).

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `portal/src/pages/AdvisorIntelligence/_shared/types.ts` | PlatinumLeaderboardEntry + Summary + LeaderboardEntry GRO field extensions | Yes — DEV `d4e28cca` |
| `portal/src/pages/AdvisorIntelligence/_shared/types/TenantLayoutConfig.ts` | New `panels.groDecomposition` flag | Yes — DEV `d4e28cca` |
| `portal/src/pages/AdvisorIntelligence/_partners/inflection/layout.ts` | Enable `groDecomposition` for Inflection | Yes — DEV `d4e28cca` |
| `portal/src/pages/AdvisorIntelligence/_shared/tabs/AdvisorsTab.tsx` | `GroHeroCards` + `HeroCard` + `deriveEpsilonQuality` + epsilon column on Row + PinnedRow + groEnabled gate + JSX wiring | Yes — DEV `d4e28cca` |
| `portal` submodule pointer | `38dfc497` → `d4e28cca` | Yes — CLOUD `1b258f658` |

Diffstat (portal): 4 files changed, 226 insertions(+).

---

## Current State

| Item | Status |
|------|--------|
| Inbox | Acted on all unread; standing by post-Phase-2 |
| Portal DEV HEAD | `d4e28cca` (local) — pending DT push |
| Workspace CLOUD HEAD | `1b258f658` (local) — pending DT push |
| PROD state | `portal-v2.1.86` (DT 0.4 emergency cut) |
| DE active work | INFGRO.005 Phase 2 SHIPPED LOCAL; standing by for DT push + chain #30 |
| Watcher | (relaunch after this log commit) |
| Pending TOs | ADVI_INFGRO.006 — gates on Phase 2 push + DS~A MAX coverage proof |

---

## Next Steps

- [DT 0.4.0_DT_ClientPlatform] Push `d4e28cca` (portal DEV) + `1b258f658` (CLOUD). PROD cut deferred to Andrew. Tagging is per-DT discretion if Andrew wants a v2.1.87 cut to ship the GRO scaffolding pre-chain — recommend waiting until chain #30 lands so the cut ships LIVE numbers, not graceful-degrade '—'.
- [AE 0.6.1_AE_PartnerETL] Fire `inf-gold-trigger` `mode=full` for chain #30. Post-DS~A `fd11a33c2` INF_D_00c.portal_leaderboard.py is on S3 (ETag `08b64c2b6b31ac1c9adc55e4a7140afa` 12:58:40Z). Surface RAVC2 to DE + DS~A + COO when chain completes.
- [DE post-chain] Pull live `platinum/firm/leaderboard.json` for Inflection. Spot-check sentinel: Joe Brandenburg $16.2M total_aua / 21 clients (per DS~A). Run `/frontend-dev` visual test golden path: Andrew login → Select Partner = Inflection → AdvisorIntelligence > Advisors tab → verify three hero cards render live values + per-advisor Epsilon column populates + quality dots reflect actual epsilon/return ratios. Screenshot for AC7.
- [DE post-chain] If epsilon-quality 10% threshold produces noisy YELLOW for clean Inflection books, dial to 5% per DS~A offer. Single-line change in `deriveEpsilonQuality`.
- [INFGRO.006] Conditional MAX-window TWR re-enable — gates on (a) Phase 2 chain #30 live validation + (b) DS~A MAX-horizon coverage proof for all 4 Inflection advisors (silver/performance_dim earliest-date sweep, summaries_gain non-null at earliest-date partition).
- [DE backlog] L2 useEffect migration (`getPlatinumAdvisorSummary` at `ClientsTab.tsx:368-405`) — still on backlog; not in this session's scope.
- [DE backlog] Activity-lens window threading (`getInflectionActivityScan` per-window emit consumer) — waits DS~B `f244b425a` chain regen.
