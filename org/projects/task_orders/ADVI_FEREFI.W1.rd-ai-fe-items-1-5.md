<task_order>
<metadata>
  <to_id>ADVI_FEREFI.W1</to_id>
  <project>ADVI_FEREFI</project>
  <title>RD-AI FE: Advisor Intelligence refinements items 1-5 (pure FE) + #6-FE-tail (gated on W2 DS)</title>
  <assigned_to>0.4.2_RD_AdvisorIntelligence</assigned_to>
  <issued_by>2.0.0_SA_COO</issued_by>
  <issued_date>2026-06-03</issued_date>
  <status>dispatched</status>
  <dispatch_held>false</dispatch_held>
  <priority>HIGH — Andrew-direct live product walk; bundles into next portal promote behind Andrew smoke.</priority>
  <references>
    <ref type="prd">docs/architecture/ADVI_FEREFI_PRD.md (v0.1, a2ba67707) — CTO code-verified all 6 citations vs live DEV</ref>
    <ref type="rule">CLAUDE.md Rule 19 (portal main tree stays DEV; this TO is DEV-only — NO promote). No MSYS_NO_PATHCONV on git push (mangles VALGATE hook).</ref>
    <ref type="bundle">Rides next DEV->PROD promote with footnote 548c9d7d; CTO tracks manifest; HELD for Andrew GO.</ref>
  </references>
</metadata>

<scope>
Five pure-FE Advisor Intelligence refinements (Andrew-direct 2026-06-03), all on portal DEV. Plus the #6-FE tail which is GATED on W2 (DS real fee sub-streams) — do items 1-5 first, then the #6-FE tail once W2 lands.

OPEN-Q PRE-RESOLUTIONS (COO confirmed from type defs — do NOT introduce new literals):
- Item 1: PartnerAnalytics.tsx `GranularityOption` admits `'annually'`; `TimeWindow` admits `'3Y'`. Use those exact spellings.
- Item 4: AdvisorAnalytics.tsx `Interval` admits `'yearly'`; `WindowKey` admits `'max'`. Use those exact spellings.
- Item 5: when `prev === 0` (can't compute %), render the % cell as "—" but still show the $ delta; first period (no prior) -> omit both delta rows.

## ITEM 1 — Assets Overview defaults -> Year + 3Y  [_shared/components/PartnerAnalytics.tsx]
- L124 `useState<GranularityOption>('quarterly')` -> `'annually'`
- L125 `useState<TimeWindow>('1Y')` -> `'3Y'`
- Accept: panel loads Year interval + 3Y window; toggles still work; no fetch-shape regression (panel fetches own (granularity, firm) triple).

## ITEM 2 — Remove 4 user-visible "(pseudonymized)" spans (keep logic)
- Remove ONLY the rendered span at: ClientDetail/ClientDetailPage.tsx:99; DistributionTab.tsx:1623, :2255, :3289.
- DO NOT touch pseudonymization logic (canSeeCleartext() gating, server-side display_name, firmOverride=undefined->"Client N"). LEAVE comments at DistributionTab.tsx:643 + :2832.
- Accept: no "(pseudonymized)" text renders for any firm/role; pseudonymization behavior byte-unchanged; tsc/eslint clean.

## ITEM 3 — Remove Segment-Analytics category search bar (BOTH Inflection + 49F)  [_shared/tabs/DistributionTab.tsx]
- Remove the search input + results-dropdown at BOTH blocks: ~1685-1733 (under `{!drillChild && (...)}` ~1677) and ~2305-2360 (under guard ~2305).
- Remove the now-unused `categorySearch`/`setCategorySearch` state declarations (:1256 + :1905) + their reset sites (:1281 + :1944) to keep eslint green. VERIFY no other reader of categorySearch remains before deleting each state.
- Accept: no search bar renders in Segment Analytics for either firm; cohort switching + category list still render/function; eslint clean (no orphaned state/unused-var).

## ITEM 4 — Lifetime Activity defaults -> Max + Year  [_shared/components/AdvisorAnalytics.tsx]
- L179 `useState<Interval>('quarterly')` -> `'yearly'`
- L180 `useState<WindowKey>('1Y')` -> `'max'`
- Accept: Lifetime Activity loads Max window + Year interval; toggles work; renders for AUA/AUM + NNA modes at new defaults.

## ITEM 5 — Lifetime Activity AUM-mode tooltip: add period-over-period Δ$ + Δ%  [_shared/components/AdvisorAnalytics.tsx]
- AUA/AUM Recharts tooltip ~L579-601 currently renders per-series rows + Total, NO delta.
- REUSE the prev-period pattern already at L358-374 (NNA deltas: `allPeriods.slice(1).map(([key,curr],i)=>{const [,prev]=allPeriods[i]; ...})`). Extend to AUM: prev-period value, `$delta = curr-prev`, `%delta = (curr-prev)/prev`.
- Add two tooltip rows in AUM mode: "$ change" (signed currency) + "% change" (signed percent) vs immediately-prior period. Guard first-period + prev===0 per pre-resolution above.
- Accept: hovering an AUM-mode period shows current + Δ$ + Δ% vs prior; first period graceful; AUA + NNA tooltips unchanged; sign convention matches chart (gain positive); numbers reconcile vs chart series.

## ITEM 6 — FE tail (GATED on W2 DS) — drop the synthetic "approx"  [_shared/components/AdvisorAnalytics.tsx + lib/feeBucket.ts]
- DO NOT START until W2 (DS) emits real per-period *_fee_paying/*_no_fee sub-streams (so `hasFeeSplitSeries===true`).
- Then: the AdvisorAnalytics.tsx:458-462 synthetic branch (`approx (N% of book)`) no longer fires -> remove the "approx" span. If `computeSyntheticFeeRatio` (feeBucket.ts:209) becomes fully unused fabric-wide, retire it; ELSE leave as fallback for any firm still lacking the split.
- Accept: fee-paying toggle shows real per-period split (no "approx") for both firms; Inflection pre-July-2025 reflects back-attributed classification (W2).
</scope>

<acceptance>
- [ ] Items 1-5 landed on portal DEV; tsc -b clean; eslint clean.
- [ ] Cross-tenant regression: 49F + Inflection + demo all render Advisor Intelligence correctly (asymmetric-bug discipline) — items 1/3/4/5 affect shared components used by all firms.
- [ ] Item 6 FE tail completed AFTER W2 DS lands (or explicitly carried if W2 not yet ready at promote time).
- [ ] RAVC2 to COO with commit SHAs + per-item confirmation; flag any open-Q that needed an Andrew call (e.g., item5 %-base display preference if you disagree with the "—" default).
- [ ] Rule 19: main tree stays DEV; NO promote (CTO owns the bundled promote).
</acceptance>
</task_order>
