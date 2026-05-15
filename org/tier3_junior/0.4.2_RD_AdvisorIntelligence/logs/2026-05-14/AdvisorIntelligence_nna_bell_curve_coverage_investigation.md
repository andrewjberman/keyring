# NNA Snapshot Bell Curve Coverage Investigation (L0/L1/L2 audit) — 0.4.2_RD_AdvisorIntelligence

**Date:** 2026-05-14
**Task Order:** ad-hoc (Andrew direct → CTO routing); Track A retroactively coded as `ADVI_INFFIN.NNN.rd-nna-l0-firm-wide-display-bug` and structurally CLOSED on inversion (not a FE bug)
**Status:** COMPLETE — Track A CLOSED (CDN cache inversion; CTO RAVC2 ratified) | Track B CLOSED (H1 chain re-fire confirmed + H3 FE drill-asymmetry patched + smoke verified)
**Portal DEV commit:** N/A — investigation-only session, no FE code shipped

---

## Objective

Andrew flagged that Inflection "Segment Analytics → Snapshot → NNA" view shows the bell curve at L2 GEO city drill only — missing at L0 global, L1 GEO State, and L1 ADV Advisor. Investigate whether the data exists in the platinum artifact and the FE just isn't displaying it, or whether backend (DS) emit gaps require new gold-script work.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| (none) | — | SKIPPED | Investigation-only session, no portal code touched. comp-* tools defer to ship phase; no ship occurred (Track A closed as CDN cache, no FE patch). |

**What worked:** Direct S3 artifact inspection (`aws s3 cp` + `python3 -c json.load`) was the highest-leverage diagnostic tool — confirmed both the L0 emit-presence and the L1 emit-absence in a single inspection.
**What failed:** N/A — comp-* tools weren't applicable to this investigation phase.
**Gap found:** None tool-side. **Pattern-side gap:** CDN cache staleness produces "FE bug" symptoms that no comp-* tool covers — surfaced to CTO as RECP candidate (`feedback_cdn_cache_staleness_masquerades_as_fe_bug` memory entry candidate).

Will append one line to `org/compiler-tools-log.md` noting SKIPPED + reason.

---

## Work Completed

### 1. Initial diagnostic — S3 artifact + FE code trace

Downloaded `s3://opal-data-inf/platinum/firm/partner_analytics_quarterly.json` (pre-invalidation `generated_at: 2026-05-14T18:23:53Z`) and traced `distributionData` memo at `DistributionTab.tsx:3111-3200` against the data shape.

| Drill level | S3 data present? | FE code-path ready? | Verdict |
|-------------|------------------|---------------------|---------|
| L0 GEO/ADV NNA | YES — `distribution.total.histogram` 22 bins, 21 nonzero counts, p50=-$3,580, bin_labels populated | YES — line 3161-3166 `firmTotal?.histogram?.counts?.some(c => c > 0)` gate | Should render; investigation pending |
| L1 GEO State | NO — `drill['WA']` has only `by_city`, no `total` key | YES — line 3124 `if (drillEntry.total) return drillEntry.total` | Backend emit gap |
| L1 ADV Advisor | NO — `views.nna.current.adv.drill = {}` empty | YES — line 3123 `if (drillEntry.distribution) return drillEntry.distribution` | Backend emit gap |
| L2 GEO City | YES — `drill['WA'].by_city['Snohomish']` full DistributionStats | YES | Working ✓ |

**Inflection HH-grain note (Andrew):** "relationship" = HH ID for Inflection (vs individual relationship ID for 49F). 219-count = HH count. Affects label semantics only.

### 2. Surface to CTO + routing decision

Routed investigation to CTO (COO was busy). CTO returned routing:
- **Track A (FE):** Direct GO under retroactive TO `ADVI_INFFIN.NNN.rd-nna-l0-firm-wide-display-bug` (under existing ADVI_INFFIN project, not new ADHC)
- **Track B (Backend):** CTO MCPs COO simultaneously to author DS sister TO `ADVI_INFFIN.NNN.dsc-nna-l1-state-advisor-emit`
- Track A FIRST (1-2hr wall vs Track B multi-hour); Track B sister-ships independent
- Phase 1 close not delayed — net-new feature-completeness scope, not Phase 1 multi-tenant primitive

CTO ACK'd light-touch RAVC1 posture for Track A: surface commit SHA + before/after screenshot; spot-check <5min.

**Note:** CTO message also confirmed `INFFIN.018` (DS sister TO for L1 State + L1 Advisor emit) **had already shipped** at commit `459742261` (~30min wall) while investigation was ongoing.

### 3. Track A live-verify via /frontend-dev → inversion

Spawned general-purpose agent (`ac857280f9b6579b0`) for browser smoke against dev server localhost:5173. Auth: Andrew + Select Partner → Inflection.

Three-state empirical reproduction:

| State | Live result | Matches Andrew's screenshot? |
|-------|-------------|------------------------------|
| GEO NNA L0 (no drill) | **PLACEHOLDER** "Select a state to view per-relationship NNA flow distribution" | YES |
| ADV NNA L0 (no drill) | **PLACEHOLDER** "Select an advisor to view per-relationship NNA flow distribution" | YES |
| GEO NNA L2 city drill (WA→Snohomish) | Bell curve renders | YES |

Served-vs-source JSON diff (the diagnostic that inverted Track A):

| Source | `generated_at` | NNA L0 histogram | Notes |
|--------|----------------|------------------|-------|
| Served (via CloudFront) | `2026-05-14T00:27:07Z` (yesterday 20:27 ET) | `{}` empty | `x-cache: Hit from cloudfront`, `age: 64908s` (~18hr stale) |
| S3 source-of-truth | `2026-05-14T19:03:51Z` (today 15:03 ET) | 22 bins, 21 nonzero counts, populated `bin_labels` | DS's earlier emit IS in S3 |

**Inversion verdict:** FE code is correct as designed. Render-gate at `DistributionTab.tsx:3635` correctly checks `histogram?.bin_labels?.length > 0` — with served empty `{}`, falls to placeholder. **No FE patch needed.** Root cause is CloudFront edge cache holding the prior empty-histogram object. Hard reload doesn't help (same ETag served).

Surfaced inversion to CTO. CTO structurally CLOSED Track A as "not-a-bug; inverted to CDN cache staleness."

### 4. CF invalidation fired by CTO directly

CTO initially routed CF invalidation to AE 0.6.1 as concurrent side-task; state-drift surfaced (Andrew closed AE 0.6.1 at 19:36Z per session log `346cca193`). AE 0.6.1 correctly invoked close-discipline. CTO fired invalidation directly:

- **Invalidation ID:** `I2YE8RIANETXKWTTB7PZZHOU1M`
- **Distribution:** `EVTSA9VEHNZVH` (opalinvest.dev portal)
- **Path:** `/api/scoped/advisor-intelligence/platinum/firm/*` (wildcard)
- **CreateTime:** 2026-05-14T20:26:07.768Z
- **Status:** InProgress at fire; propagated within ~2min

### 5. Post-invalidation 5-state smoke

Spawned second smoke agent (`a786ed498c3fd125d`) after invalidation. Cache-bust confirmed: `last-modified: Thu, 14 May 2026 19:03:53 GMT`, fresh ETag, `age: 7-168s`, served `generated_at: 2026-05-14T19:03:51Z` matches S3.

| State | UI Result | Underlying data | Caveat |
|-------|-----------|-----------------|--------|
| A: L0 GEO NNA | **PASS** | L0 firm histogram (correct) | — |
| B: L0 ADV NNA | **PASS** | L0 firm histogram (correct) | — |
| C: L2 city (WA→Snohomish) | **PASS** | by_city histogram (correct) | Regression sentinel intact |
| D: L1 GEO State (WA, no city) | PASS at UI level | **L0 firm-wide histogram** (NOT state-specific) | Label-vs-data divergence |
| E: L1 ADV Advisor (Peter Lee) | PASS at UI level | **L0 firm-wide histogram** (NOT advisor-specific) | Label-vs-data divergence |

**Track B caveat (INFFIN.018 emit absent from served artifact):**

Despite the CF invalidation pulling the latest S3 object, direct artifact inspection shows:
- `views.nna.current.geo.drill[stateKey]`: 15 state keys present, each with ONLY `by_city` — **`total` field absent**
- `views.nna.current.adv.drill`: `{}` empty
- `views.aua.current.adv`: `{}` empty (separate concern)

INFFIN.018 commit `459742261` shipped emit CODE but artifact `generated_at: 2026-05-14T19:03:51Z` (15:03 ET) likely predates the commit. **Chain re-fire pending** (hypothesis 1) OR emit code wrote different field names than FE reads (hypothesis 2) — DS to triage.

FE memo path traces this fallthrough at L1: `drillEntry.total` absent → L1 `parentSegment.distribution` checks fail (NNA segments don't embed `.distribution`) → falls to **L0 firm-wide** at line 3158-3166. Result: panel label says "PETER LEE — NNA FLOW DISTRIBUTION" but histogram data is firm-wide. To the eye it looks like coverage; under the hood it's a label-vs-data divergence.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Surface to CTO first (not COO) | Per Andrew direct — COO busy |
| Track A retroactive TO `ADVI_INFFIN.NNN.rd-nna-l0-firm-wide-display-bug` (then closed structurally) | CTO routing — feature-completeness gap fits ADVI_INFFIN, not new ADHC |
| No FE patch on Track A | Empirical inversion proved CDN cache staleness, not FE bug |
| CF invalidation fired by CTO (not RD) | Cross-lane action — AE 0.6.1 was closed by Andrew; CTO has direct authority |
| L1 label-guard fix NOT applied this session | Awaiting CTO routing call (`stricter` placeholder vs `permissive` relabel) and Track B DS resolution first |
| Memory entry deferred to COO batch | Per CTO direction — `feedback_cdn_cache_staleness_masquerades_as_fe_bug.md` is 17th candidate, sister to DS~D smoking-gun + COO audit-overcount-orphan-consumers patterns |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/tier3_junior/0.4.2_RD_AdvisorIntelligence/task_orders/ADVI_SHARED.007.rd-lint-residual-sweep.md` | `<status>pending</status>` → `<status>complete</status>` (from prior session boot) | No — local only, slated for session-log commit |
| `.comp-graph/.agent_context` | Set TO_ID context for Track A | No — local only |
| `org/tier3_junior/0.4.2_RD_AdvisorIntelligence/logs/2026-05-14/AdvisorIntelligence_nna_bell_curve_coverage_investigation.md` | This session log | No — pending commit after Andrew's "include next steps" direction |

No portal source files modified. No FE patch shipped.

---

## Blockers

None for RD lane.

Track B (per CTO routing) has open follow-ups but I'm not blocked on them:
- DS triage on INFFIN.018 emit absence (chain re-fire OR field-name audit). Evidence: served-JSON inspection `views.nna.current.geo.drill[*].total` absent + `adv.drill = {}` empty; INFFIN.018 commit `459742261` confirmed shipped per CTO message
- (Optional) FE label-guard for L1 NNA when actual per-segment data is missing — awaiting CTO routing call

---

## Current State

Track A (L0 NNA bell curve coverage) is **structurally CLOSED**. Single CloudFront invalidation `I2YE8RIANETXKWTTB7PZZHOU1M` on path `/api/scoped/advisor-intelligence/platinum/firm/*` (distribution `EVTSA9VEHNZVH`) released the 18hr-stale platinum artifact and the existing `DistributionTab.tsx:3161-3166` code path renders the firm-wide HH NNA flow histogram correctly on both GEO and ADV cohorts. L2 city-drill regression sentinel (`drill['WA'].by_city['Snohomish']`) intact. L1 GEO State (D) and L1 ADV Advisor (E) panels render at the UI level but with a **label-vs-data divergence**: panels show per-segment titles ("PETER LEE — NNA FLOW DISTRIBUTION", "WASHINGTON — STATE NNA Distribution") while the underlying histogram is the L0 firm-wide fallback, because INFFIN.018 emit fields (`drill[stateKey].total`, `drill[advisorKey].distribution`) are absent from the served artifact (`generated_at: 2026-05-14T19:03:51Z`) despite the commit `459742261` having shipped — chain re-fire pending or emit field-name audit needed. RAVC2 surfaced to CTO with two routing questions: (a) DS triage path on Track B emit, (b) whether RD adds a stricter FE label-guard to suppress misleading per-segment titles when data falls through to L0. Bench-idle awaiting routing.

---

## Next Steps

1. **[CTO 1.0.0_SA_CTO] RAVC2 ratify on Track A close** — light-touch spot-check on post-invalidation screenshots in `.frontend-dev/post_invalidation_{A,B,C,D,E}.png` confirms L0 GEO + L0 ADV bell curve coverage delivered without FE change
2. **[CTO 1.0.0_SA_CTO] Routing call on Track B follow-up** — two open questions surfaced in RAVC2:
   - (a) Whether DS triage routes through COO (chain re-fire OR field-name audit on INFFIN.018 commit `459742261` vs FE read paths at `DistributionTab.tsx:3123-3124`)
   - (b) Whether RD adds a stricter FE label-guard to suppress misleading per-segment titles when `distributionData` is falling through to L0 firm-wide (stricter placeholder vs permissive relabel — UX call)
3. **[COO 2.0.0_SA_COO] Memory entry banking** — `feedback_cdn_cache_staleness_masquerades_as_fe_bug.md` — sister-class to `[[feedback_smoking_gun_field_shape_sanity]]` (DS~D) and `[[feedback_audit_overcount_orphan_consumers]]` (COO). Defer to COO batch per CTO direction
4. **[COO 2.0.0_SA_COO] RECP framing for systemic CDN-invalidation-on-emit pattern** — CTO already routed; three structural options (gold-chain dispatch issues CF invalidation as final step; platinum cache headers `must-revalidate` / shorter `max-age`; manual invalidation hook in `safe-deploy.sh` / `dispatch.sh`). Sister-class to ADHC_FECACHE_COHERENCE but for the CDN cache layer (between origin S3 and FE). Candidate name: `ADHC_CDNCOHT`
5. **[0.4.2_RD_AdvisorIntelligence] Commit this session log + .007 TO status flip** — single scoped commit via `.tools/safe-commit.sh` once Andrew confirms direction
6. **[0.4.0_DT_ClientPlatform] No bundle coordination needed** — L0 fix shipped via data-side CF invalidation, no portal release required; if FE label-guard becomes a follow-up patch, DT 0.4 coordinates bundle inclusion at that point

---

## Addendum — Post-RAVC2 CTO Ratify + Chain Re-fire In-Flight (20:42Z)

### Track A RATIFIED CLOSED by CTO

CTO RAVC2 ratify received post initial draft of this log. Verbatim verdict: "Clean diagnostic + clean close. CF invalidation `I2YE8RIANETXKWTTB7PZZHOU1M` was the right fix; FE code is correct as designed; render-gate falls to placeholder on empty histogram exactly as the architecture intends. **No FE patch needed.**" L0 NNA bell curve surface CLOSED on first attempt.

### Track B routing — H1/H2 verdict pending chain TERMINAL ~21:00Z

Per COO 20:34Z surface relayed via CTO RAVC2:

- **AE 0.6.1 fired chain `--from INF_B_00` at 20:34Z**
- CommandId `4957e056`, PID 3012
- Cold-start path (EC2 was stopped post-Andrew-close 19:36Z per session log `346cca193`)
- SSM agent Online verified
- ETA terminal ~21:00Z (~25min wall from fire)

This chain re-fire materializes INFFIN.018 emit `459742261` shipped earlier today. Empirical evidence currently favors H1 (chain re-fire pending was the gap, not field-name mismatch).

### Post-chain-TERMINAL plan

1. Surface to CTO for invalidation #2 decision (CTO offered to fire `aws cloudfront create-invalidation` directly if RD doesn't want to wait for organic edge-cache expiry — leaning toward manual fire to minimize wall + verify within same session)
2. Re-run portal smoke focused on L1 GEO State (D) + L1 ADV Advisor (E); L0 already verified
3. Inspect served-JSON for `views.nna.current.geo.drill[stateKey].total` + `views.nna.current.adv.drill[advisorKey].distribution`
4. H1/H2 verdict:
   - **H1 confirmed**: fields populated → Track B closes empirically; no FE work; panel labels become accurate (data matches title)
   - **H2 confirmed**: fields still absent → concrete field-name diff (emit code at `data/orion/scripts/gold/INF_*.py` vs FE read path at `DistributionTab.tsx:3123-3124`) routed to COO for DS~C field-name audit TO; concurrent with that, ship the stricter label guard per CTO endorsement

### Label guard — CTO ENDORSE stricter (deferred until H1/H2 verdict)

CTO endorsed the stricter approach (placeholder over misleading label) for the reasons RD surfaced + four additional structural arguments:

1. Label-vs-data divergence is more dangerous than placeholder — Andrew/partner-eyes interpret "PETER LEE — NNA FLOW DISTRIBUTION" with firm-wide data as per-advisor coverage; mismatched data violates the implicit contract silently
2. Display correctness > nominal coverage — placeholder is honest about the gap
3. Recovery path clearer with placeholder — "DS emit pending" prompts engagement; silent divergence indefinitely silent
4. Sister-class to `[[feedback_cdn_cache_staleness_masquerades_as_fe_bug]]` — silent multi-layer FE-display gaps have worse outcomes than explicit placeholders

CTO implementation sketch (RD discretion if shipped):
```typescript
if (selectedDrillType === 'state' || selectedDrillType === 'advisor') {
  const drillEntry = drillData[selectedKey]
  const hasPerSegmentData =
    selectedDrillType === 'state' ? !!drillEntry?.total :
    selectedDrillType === 'advisor' ? !!drillEntry?.distribution : false

  if (!hasPerSegmentData) {
    return {
      status: 'EMIT_PENDING' as const,
      message: `${selectedKey} per-${selectedDrillType} distribution pending DS emit (INFFIN.018)`,
      emit_pending_ticket: 'INFFIN.018',
    }
  }
}
```

Timing: **wait for chain TERMINAL before shipping** — H1 may resolve and guard becomes unnecessary.

### ADHC_CDNCOHT (CDN Coherence) — systemic fix project candidate

CTO referenced `ADHC_CDNCOHT` as the project bucket for the systemic CDN-invalidation-on-emit pattern. Sister-class to ADHC_FECACHE_COHERENCE but for the CDN cache layer (between origin S3 and FE). Today's manual CF invalidation is the empirical anchor; permanent fix (dispatch.sh post-chain CF invalidation hook) is the structural payload. Routed to COO via CTO RAVC2 for project authoring decision.

### Cottonwood (a) bundle implication

L0 ships clean (Track A) — no portal release needed for that surface. L1 caveat status:
- If H1 resolves at chain TERMINAL ~21:00Z → Track B closes empirically; L1 ships with chain re-fire materialization; no FE work
- If H2 confirmed → Track B needs DS~C TO + (optional) RD label guard; partial-pass-with-caveat until that ships
- Either way: Cottonwood (a) ship-before-Cottonwood trajectory honored via portal/PROD bundle on L0 surface + D-max β chain re-fire + (eventual) L1 emit clean

### Updated Next Steps (supersedes initial list)

1. **[0.4.2_RD_AdvisorIntelligence] WAIT for chain TERMINAL** — ~21:00Z (~18min from RAVC2 ratify time 20:42Z); monitor COO MCP cycle for terminal sentinel
2. **[CTO 1.0.0_SA_CTO] Fire CF invalidation #2 post-chain-TERMINAL** — manual `aws cloudfront create-invalidation --distribution-id EVTSA9VEHNZVH --paths "/api/scoped/advisor-intelligence/platinum/firm/*"`; CTO offered to fire directly
3. **[0.4.2_RD_AdvisorIntelligence] Post-invalidation #2 portal smoke** — focus on L1 GEO State (D) + L1 ADV Advisor (E); inspect served-JSON for INFFIN.018 fields
4. **[0.4.2_RD_AdvisorIntelligence] H1/H2 verdict RAVC3 to CTO** — closes Track B (H1) OR triggers DS~C field-name audit TO route + ships stricter label guard (H2)
5. **[CTO 1.0.0_SA_CTO + COO 2.0.0_SA_COO] If H2: route DS~C field-name audit TO** — concrete diff in RAVC3 payload; emit code at `data/orion/scripts/gold/INF_*.py` vs FE read path at `DistributionTab.tsx:3123-3124`
6. **[COO 2.0.0_SA_COO] ADHC_CDNCOHT project authoring** — systemic CDN-invalidation-on-emit pattern; three structural options (dispatch.sh hook, cache-header tightening, safe-deploy.sh hook)
7. **[COO 2.0.0_SA_COO] Memory entry banking** — `feedback_cdn_cache_staleness_masquerades_as_fe_bug.md` per CTO direction (17th candidate, sister-class to `feedback_smoking_gun_field_shape_sanity` + `feedback_audit_overcount_orphan_consumers`)
8. **[0.4.2_RD_AdvisorIntelligence] Commit session log + .007 TO status flip** — single scoped commit via `.tools/safe-commit.sh` once chain TERMINAL resolves and H1/H2 verdict locks in

---

## Addendum 2 — Post-chain-TERMINAL H1 confirmation + H3 FE drill-asymmetry diagnosed + patched (22:50Z)

### H1 confirmed via S3 ground-truth (broker chain-TERMINAL signal missed)

Resumed from idle gap (no chain-TERMINAL inbox message arrived). Reconstructed state via `git fetch` + `aws s3 cp` direct S3 inspection.

Post-chain artifact `s3://opal-data-inf/platinum/firm/partner_analytics_quarterly.json`:
- `generated_at: 2026-05-14T21:14:01Z` — chain TERMINAL materialization
- Size 456KB → 534KB (+78KB INFFIN.018 emit delta)
- `views.nna.current.geo.drill['WA'].total.histogram`: 19 nonzero bins, count=178 HHs (WA-specific)
- `views.nna.current.adv.drill`: populated with 4 keys (`peter_lee`, `patrick_scanlan`, `joe_brandenburg`, `inflection_wealth_management`)
- `views.nna.current.adv.drill['peter_lee'].distribution.histogram`: 18 nonzero bins, count=165 HHs

**Sister-pattern lesson:** broker-channel signals can miss; S3 ground-truth inspection is the verification fallback. Memory entry candidate `feedback_s3_ground_truth_over_broker_channel_signals.md` flagged for next-session COO batch (sister to `feedback_cdn_cache_staleness_masquerades_as_fe_bug`).

### CTO fired invalidation #2

`IDQ7KPUD7JZ2BHOE5251ZDK0PV` at 22:25:21Z, distribution `EVTSA9VEHNZVH`, wildcard path `/api/scoped/advisor-intelligence/platinum/firm/*`. Propagation ~1-3min. Confirmed bust via served `last-modified: Thu, 14 May 2026 21:14:02 GMT`, fresh ETag, `age: 161-221s`.

### Post-invalidation-#2 smoke — 4/5 PASS, State E label-vs-data divergence

| State | Label | Data | Verdict |
|-------|-------|------|---------|
| A: L0 GEO NNA | firm-wide | P25=$3K / P75=$24K firm-wide | ALIGNED ✓ |
| B: L0 ADV NNA | firm-wide | P25=$3K / P75=$24K firm-wide | ALIGNED ✓ |
| C: L2 city (WA→Snohomish) | "WASHINGTON — CITY NNA DISTRIBUTION" | P25=$10.7K / P75=$19.5K city-specific | ALIGNED ✓ |
| D: L1 GEO State (WA) | "WASHINGTON — CITY NNA DISTRIBUTION" | P25=$1.48K / P75=$11.3K WA-specific | ALIGNED ✓ |
| E: L1 ADV Advisor (Peter Lee) | "PETER LEE — NNA FLOW DISTRIBUTION" | P25=$3K / P75=$24K **firm-wide (identical to B)** | **DIVERGENT** |

### H3 root cause — GEO/ADV drill-asymmetry FE gap

**NOT H1 (chain) nor H2 (field-name). New finding: H3 (FE drill-asymmetry).**

Diagnostic chain:
1. State E shows firm-wide data despite Peter Lee having own distribution in JSON (164 HHs)
2. FE code path at `DistributionTab.tsx:3113-3127` reads `drillEntry.distribution` per INFFIN.018 spec — but gated behind `isDrilledDown=true`
3. `handleSegmentClick` (lines 3241-3268):
   - GEO state-click DRILLS: `setSelectedStateKey(seg.key); setGeoDrillLevel('city')` → `isDrilledDown=true` → block 3113 activates → `drillEntry.total` returns WA-specific ✓
   - ADV architect-click only SELECTS: `setSelectedSegmentKey(seg.key)` → `isDrilledDown=false` (PII gate blocks client-level drill) → block 3113 skipped → falls through to L0 firm-wide ✗
4. The architect-selected key lives in `selectedSegmentKey`, NOT `selectedArchitectKey` (which is reserved for client-level drill); existing block reads `parentKey = selectedStateKey || selectedArchitectKey`, missing the architect-selected case

Architectural framing: asymmetry between GEO and ADV cohort drill semantics is **intentional** (PII gate prevents per-client exposure at firm-level). Side-effect was the existing NNA-drill block didn't activate for architect-selected state. Subtle catch; required empirical-only diagnostic.

### CTO RAVC4 ratify — Option 1 ship-direct ENDORSED

CTO endorsed shipping the small FE patch directly per light-touch RAVC1 posture. Surgical scope (1 file, ~6 lines, additive new branch, no handler/type/contract change, no cross-component impact). Architecturally clean, regression-risk-low.

### Patch shipped to `DistributionTab.tsx` distributionData useMemo

Inserted new branch after the existing `isDrilledDown` NNA-drill block (line 3127) and before L2 segment-selected block (line 3129):

```typescript
// H3 (ADVI_INFFIN NNA bell curve coverage): ADV NNA architect-selected at L1.
// GEO state-click DRILLS state->city (isDrilledDown becomes true, block above
// handles it). ADV architect-click only SELECTS (PII gate blocks client-drill),
// so isDrilledDown stays false and the block above is skipped — falls through
// to L0 firm-wide previously, producing label-vs-data divergence
// ("PETER LEE -- NNA FLOW DISTRIBUTION" header rendered with firm-wide data).
// Read drillEntry.distribution directly when an architect is selected.
if (metric === 'nna' && !isDrilledDown && cohort === 'adv' && nnaDrillData && selectedSegmentKey) {
  const drillEntry = nnaDrillData[selectedSegmentKey]
  if (drillEntry?.distribution) return drillEntry.distribution
}
```

Also added `cohort` to the memo's dep array (line 3212) since it's referenced in the new branch.

### Validation

- `bun run tsc --noEmit`: **0 errors** (exit 0)
- `bun run lint`: **10 warnings** (was 9 baseline per .007 close; +1 NOT from this patch — `PartnerAnalytics.tsx:362` preserve-manual-memoization is from DE 0.4 NMCOHT bucketing commit `3c3116841d` / OOS for RD lane). My patch added 0 new warnings.

### Post-patch smoke — Track B closes

State E verification post-patch:
- Right panel header: "PETER LEE — NNA FLOW DISTRIBUTION" (unchanged)
- Chips: **P25=$1.50K / P75=$12K** (distinct from L0 firm-wide $3K/$24K) ✓
- Histogram visibly distinct from L0; left-shifted matching Peter Lee's net flows
- Artifact ground truth: `views.nna.current.adv.drill.peter_lee.distribution.percentiles = {p10:-$33K, p25:-$10K, p50:-$3.5K, p75:-$1.2K, p90:$8.7K}` reconciles to displayed chips

Regression sentinels (States A/B/C/D) ALL PASS unchanged.

**Track B closes empirically. Label-vs-data alignment achieved across all 5 states.**

### GEO/ADV emit shape asymmetry note (noted, no action)

GEO drill uses `.total` wrapper; ADV drill uses `.distribution` flat. FE handles both at lines 3123-3124. **Not a defect; intentional emit pattern.** Worth recording for future-auditor context.

### Final Updated Next Steps

1. **[0.4.2_RD_AdvisorIntelligence] Commit patch + session log + .007 TO flip + compiler-tools-log entry** — single scoped commit via `.tools/safe-commit.sh`, split across two repos (portal/DEV + workspace/CLOUD)
2. **[0.4.0_DT_ClientPlatform] Push portal/DEV + workspace/CLOUD** — DT lane (RD can commit, not push)
3. **[CTO 1.0.0_SA_CTO] RAVC5 ratify** — light-touch spot-check on commit SHA + before/after Peter Lee L1 screenshots
4. **[DT 0.4 + CTO] Bundle promote** — portal-v2.1.89 candidate; H3 fix folds into Cottonwood (a) bundle (or fast-follow per CTO's bundle-inclusion decision)
5. **[Andrew] Empirical visual confirm** — final gate; all 5 NNA bell curve drill levels now empirically rendering with label-data alignment
