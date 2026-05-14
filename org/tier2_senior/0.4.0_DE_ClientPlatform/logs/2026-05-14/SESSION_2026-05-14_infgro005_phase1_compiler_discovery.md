# Session — ADVI_INFGRO.005 Phase 1 compiler discovery

**Agent:** 0.4.0_DE_ClientPlatform
**Date:** 2026-05-14
**Workspace CLOUD HEAD at start:** `3b6c0718e` (post catch-up log commit)
**TO:** `ADVI_INFGRO.005` — Portal GRO decomposition: AdvisorsTab side-by-side display
**Phase:** 1 of 2 (parallel-OK while DS base lane ships .001-.004; Phase 2 blocks on DS~A .004 leaderboard.json extension)

---

## Scope

Phase 1 per TO `<scope>` step 1: run compiler tools, note all UNUSED/MISSING/WARN, identify what type extensions are needed. Phase 2 (type extension + UI implementation) gates on DS~A's leaderboard.json schema ship — exact field names per TO directive "do NOT guess names from PRD; use actual JSON".

---

## Compiler Tools

| Tool | Result | Action |
|------|--------|--------|
| `comp-transform schema-check AdvisorsTab --feature gro_decomposition` | 5 type fields / 1 rendered. UNUSED (2): `available_windows: string[]`, `windows: Record<string, PlatinumLeaderboardWindow>`. Feature token did NOT escalate any UNUSED to WARN — meaning no fields named after `gro_decomposition` exist yet (expected — DS .004 unships). | Type extension pending DS .004 |
| `comp-transform ternary-audit AdvisorsTab` | 3 ternary gaps at L1021 (`metric === 'nna'`), L1029 (`metric === 'aua'`), L1037 (`metric === 'gro'`). Each handles ONE LeaderboardMetric union member; the other two route to else branch. | Architectural: PRD §3.3 says "render all three always" — the toggle-driven HERO/SEC pattern needs to flip to all-three-HERO. See "Architecture findings" below. |
| `comp-routes trace getFirmLeaderboard` | Clean: `/api/scoped/advisor-intelligence/platinum/firm/leaderboard.json` -> CloudFront -> S3-opal-data-bd. Edge JWT. shared-advisor-router. 4 consumers (49F index, Inflection index, AdvisorsTab, ClientsTab). | No route changes needed for Phase 2. New JSON fields flow through existing fetcher. |
| `comp-cache collisions` | 4 shared keys org-wide. `['firm-leaderboard', 'firmOverride']` shared across 3 consumers (49F index, AdvisorsTab, ClientsTab) — all consume `PlatinumLeaderboardResponse`. Same type = no collision risk. | When I extend PlatinumLeaderboardResponse with GRO fields, all 3 consumers get the fields free. No new collision risk. |

`.agent_context` set to `TO_ID=ADVI_INFGRO.005` — comp-* runs auto-log to `org/compiler-tools-log.md`.

---

## Architecture findings

### Current AdvisorsTab structure (entries from `portal/src/pages/AdvisorIntelligence/_shared/tabs/AdvisorsTab.tsx`)

| Line | Element | Notes |
|------|---------|-------|
| L236 | `const [metric, setMetric] = useState<LeaderboardMetric>('aua')` | 3-state toggle: 'aua' \| 'nna' \| 'gro' |
| L271-272 | `if (metric === 'gro' && period === 'max') setPeriod('ytd')` | MAX disabled in GRO mode (matches TO-006 spec — kept disabled until .006 fires) |
| L275-276 | `lockedPeriods = metric === 'gro' ? new Set<PeriodKey>(['max']) : new Set<PeriodKey>()` | MAX button locked when GRO active |
| L525 | `<ToggleGroup options={LEADERBOARD_METRIC_OPTIONS} value={metric} onChange={setMetric} />` | The user-facing metric toggle |
| L539 | `<Top3Highlights ... metric={metric} ...>` | Top-3 ranking is metric-driven |
| L576-600 | Panel 2 Leaderboard `{metric === 'nna' && ...}{metric === 'aua' && ...}{metric === 'gro' && ...}` | Three exclusive branches |
| L1015-1041 | `LeaderboardRow` per-advisor columns — ALL THREE rendered side-by-side already | NNA / AUA / GRO columns. Active metric gets HERO (text-2xl font-black); others get SEC (text-sm font-medium) |

### Current `PlatinumLeaderboardEntry` shape (`types.ts:1982-1999`)

```typescript
export interface PlatinumLeaderboardEntry {
  name: string
  advisor_id: string
  roles: string[]
  total_aua: number
  nna: number
  inflows: number
  outflows: number
  aua_growth_pct: number | null  // current "GRO" column source (AUA-delta %, null when below GRO floor)
  new_clients: number
  client_count: number
  account_count: number
  role_breakdown: Record<string, PlatinumRoleBreakdown>
  fee_breakdown?: { fee_paying: PlatinumFeeBreakdown; no_fee: PlatinumFeeBreakdown }
  period_start_aua?: number | null
}
```

### Phase 2 type-extension targets (pending DS .004 exact names)

Per TO §scope step 3:
```typescript
advisor_return_pct_twr: number | null         // AUA-weighted TWR%
advisor_nna_dollar: number | null              // may map to existing `nna` field — confirm w/ DS
advisor_epsilon_dollar: number | null
advisor_epsilon_data_quality: "GREEN" | "YELLOW" | "MISSING_PERF"
```

Open questions for DS~A (do NOT pre-answer; wait for leaderboard.json ship):
1. Is `advisor_nna_dollar` a new field or a rename of existing `nna`? Existing usage at AdvisorsTab L1022 formats `entry.nna` as `$`-suffixed currency — appears to already be dollar units. Likely same data, possibly retained name `nna`.
2. Does `aua_growth_pct` stay (PRD shows AUA delta as one of three hero cards) or get replaced by `advisor_aua_delta_dollar`? PRD §3.3 talks about "AUA delta" not "AUA growth %" — could be either.
3. Per-firm hero card values: do hero cards read from the new platinum/firm/leaderboard.json `summary` block, or a separate aggregate? `PlatinumLeaderboardSummary` currently has only `total_aua` and `total_nna` (types.ts L2001-2004) — likely needs extension too.

### Architectural decision — toggle-vs-always-hero

PRD §3.3 (per TO context) says:
> "Three hero cards at the top: AUA delta / Return (TWR%) / NNA (no toggle between them)"
> "Per-advisor columns in the table: AUA / Return / NNA / epsilon (side-by-side, not stacked)"
> "NO toggle between GRO mode and other modes — render all three always"

Per-advisor columns are ALREADY rendered side-by-side at L1015-1041 — the toggle currently only affects HERO/SEC font styling, not visibility. PRD seems to want: drop the metric toggle entirely (or repurpose it), render all three column values in equal HERO weight, add epsilon as a 4th column with quality-indicator tooltip.

Two implementation options, deferred to DS~A leaderboard ship + Andrew/CTO check at Phase 2:

| Option | Behavior | Cost |
|--------|----------|------|
| A — Drop toggle, all HERO | Remove `LEADERBOARD_METRIC_OPTIONS` ToggleGroup at L525. Per-advisor row: every column gets HERO weight. Top3Highlights default ranking by `total_aua` (or a composite). Panel 2 Leaderboard renders all three panels stacked. | Cleanest match to PRD literal; loses Top3 metric-driven ranking ability |
| B — Keep toggle for ranking only | ToggleGroup stays; controls Top3 ranking + Panel 2 Leaderboard active panel. Per-advisor row: all four columns get HERO weight (drop the SEC/HERO distinction). | Less PRD-pure but preserves "rank by GRO" navigation aid for Inflection |

Recommend B for Phase 2 implementation (preserves ranking utility), confirm w/ CTO before merging.

### Epsilon quality indicator

Per TO §scope step 4c: column header info-circle icon + tooltip:
> "epsilon: $X [GREEN/YELLOW] — accounting residual not attributable to NNA or Return"

Color-coded dot: green = GREEN, yellow = YELLOW, grey = MISSING_PERF. Pattern matches existing `HelperTip` usage at L1009-1011 (advisor-name "Unassigned" tooltip). No new component needed — re-use `HelperTip` + `Info` icon from `lucide-react`.

---

## Files Modified

None this phase — Phase 1 is discovery only.

---

## Current State

| Item | Status |
|------|--------|
| Inbox | Empty (filesystem + broker) |
| Portal DEV HEAD | `38dfc497` (v2.1.86 — DT 0.4 emergency cut) |
| Workspace CLOUD HEAD | `3b6c0718e` (catch-up log committed) |
| INFGRO.005 Phase 1 | COMPLETE — compiler baseline + architecture analysis documented |
| INFGRO.005 Phase 2 | BLOCKED on DS~A .004 leaderboard.json ship (exact field names + epsilon emit) |
| INFGRO.006 | BLOCKED on .005 + DS~A coverage proof at MAX horizon |
| Watcher | LIVE (`bepeqbgo8`) |

---

## RAVC Ledger

| Step | Direction | Timestamp (Z) | Subject |
|------|-----------|---------------|---------|
| RAVC2 | DS~A -> DE | ~13:00 | INF_D_00c:620 dtype fix SHIPPED `fd11a33c2` + INFGRO cascade field names enumerated |
| RAVC2 ACK | DE -> DS~A | 13:01:50 | Field names noted; holding Phase 2 type extension until live JSON validation post chain #30 |

If Phase 2 needs Architecture Option A/B ruling, RAVC1 -> CTO before type extension.

---

## Decisions Made

1. **Phase 1 closure without messaging DS~A** — DS~A has the .004 TO; he will signal when leaderboard.json extension ships. Pre-emptive ping = noise. Standby is correct.
2. **Defer Option A vs B to Phase 2 start** — both are viable; the ruling depends on whether the metric toggle still drives Top3 ranking after the all-three-HERO flip. CTO + DS~A leaderboard.json shape will inform.
3. **Re-use HelperTip + Info icon for epsilon quality indicator** — no new component needed; matches existing tooltip pattern at L1009-1011.

---

## Next Steps

- [DS~A] Ship INFGRO.004: extend `platinum/firm/leaderboard.json` with per-advisor GRO fields (advisor_return_pct_twr, nna decomposition, advisor_epsilon_dollar, advisor_epsilon_data_quality) + per-window summary block extension if needed. MCP signal to DE when JSON is live on S3.
- [DS base lane] INFGRO.001-.003 — pre-req to DS~A .004.
- [DE/INFGRO Phase 2] On DS~A signal: extend `PlatinumLeaderboardEntry` + `PlatinumLeaderboardSummary` types with exact field names; implement Option A or B per CTO ruling; wire epsilon column + tooltip; /frontend-dev visual test.
- [DE/INFGRO.006] After Phase 2 ships + DS~A MAX-horizon coverage proof: conditional MAX-window TWR re-enable + Peter Lee spot-check.
- [DE backlog] L2 useEffect migration (`getPlatinumAdvisorSummary` at `ClientsTab.tsx:368-405`) — parallel-OK while INFGRO Phase 2 waits.
- [DE backlog] Activity-lens window threading on DS~B per-window `activity_scan_{qtd,ytd,1y,max}.json` ship.

---

## Appendix — post-write DS~A reply (13:00Z)

DS~A pushed coordination reply on my earlier INF_D_00c:620 ping that landed mid-session-write. Material implications for INFGRO.005 Phase 2:

**INF_D_00c:620 dtype fix shipped:** `fd11a33c2` pushed + S3-synced to `s3://opal-data-inf/code/gold/INF_D_00c.portal_leaderboard.py` (ETag `08b64c2b6b31ac1c9adc55e4a7140afa`, 12:58:40Z). Single-site cast at line 620 — pre-existing latent dtype divergence (INF_C_02 emits household_id Int64, INF_C_07 emits str). No FE shape change.

**Chain #30 ball with AE 0.6.1.** Once chain #30 mode=full lands:
- Mixed-state platinum resolves to clean fresh end-to-end
- **INFGRO.003+.004 cascade fields flip from null graceful-degrade to live numbers**
- INFFIN #8 (HH 283 tax_structure_reason) lights up via INF_D_02 refire
- `6ccbfc0c` spread-fallback FE guard becomes inactive (safe to leave for defense-in-depth)

**Phase 2 type-extension field names (provisional, validate against actual JSON post chain #30):**

DS~A enumerated the cascade fields:
- `advisor_return_pct_twr` (matches TO scope step 3)
- `advisor_nna_$` (likely `advisor_nna_dollar` in actual emit — `$` not legal in JSON keys)
- `advisor_return_$` (NEW — not in TO scope step 3; second return field in dollar terms)
- `advisor_epsilon_$` (likely `advisor_epsilon_dollar`)
- firm_* equivalents (likely `firm_return_pct_twr`, `firm_nna_dollar`, etc. — for the three hero cards)

`advisor_return_$` (dollar) was not in the TO scope but appears to be part of the canonical decomposition (return contribution in absolute terms, complementing the % twr). Phase 2 plan extends to include both.

`PlatinumLeaderboardSummary` (types.ts L2001) currently only has `total_aua` + `total_nna` — will need `firm_return_pct_twr`, `firm_nna_dollar`, `firm_epsilon_dollar` extensions for the hero cards.

**Out-of-lane NaN cleanup:** lines 526-538/556-568 (advisor/firm_return_pct_twr divide-by-zero) routed to DS~C. My FE NaN-strip `e60ebf1a` remains the working guard.

**Phase 2 readiness:** field names provisional → can sketch type extensions but should validate against live leaderboard.json before commit. Phase 2 still gates on chain #30 mode=full landing.

**RAVC ACK** sent to DS~A 13:01:50Z — confirmed receipt + standby posture.
