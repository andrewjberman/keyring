# MDPF_REVAMP.S5-ROLLOVER — FE audit + A2 (aum-timeseries FE-derive) + content-A/B render

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, VALIDATE, IMPLEMENT, COORDINATE
**Serial:** 0.4.0_DE_ClientPlatform · **Date:** 2026-07-21 · **TO:** MDPF_REVAMP.S5-ROLLOVER (CTO-gated) · **Tandem:** 0.7.0_AE_CloudOps

## Summary
Launched Andrew-direct P0 (MDPF_REVAMP.S5). Re-anchored to the CORRECTED frame across 3 briefs (MSTR supersede + CTO re-brief): FRONTEND ALIGNMENT to the revamp schema, NOT producer-reproduce; data is correct/models-only by design. Delivered the FE-consumption audit, a full pre-serving render-check, the A2 aum-timeseries FE-derive (committed + CTO-accepted), and the content-A/B honest-None render treatment (implemented + verified, holding commit for a mechanism-switch nod).

## MCP traffic (this session)
~30 messages handled (broker re-surfaced the same set repeatedly on each heartbeat; counted once). Significant:
- IN: MSTR launch brief + SUPERSEDE (FE-alignment frame); CTO re-brief + 6 follow-ups (SMA nuance, deliberate-drop ruling, audit ACCEPT, seam-resolved-Option-A, A1/A2 disposition, connectNulls ruling, A2 sizing APPROVED, A2 ACCEPTED); AE tandem seed-doc + 5 coordination msgs; DS~B D2-detector FYI.
- OUT: ACK/re-anchor to CTO; audit report -> CTO (CC MSTR) + AE; cutover-seam flag -> CTO+AE; render-check verdicts (Value + Count) -> CTO+AE; Option-A endorsement; A2 sizing + ACK; connectNulls-artifact SURFACE -> CTO; D2-fix routed to DS~B (AE-owned canonical, out of my portal commit-lane).

## Work done (the arc)
1. **Startup:** /watcher (Monitor batqkec6q live), registered, session-serial written, owned-paths hook confirmed. Re-anchored to FE-alignment.
2. **FE-consumption audit (86c741876):** grounded on ALL 7 revamp keys (pulled live from opal-data-portal-v2 + opal-data-assets, field-by-field diff) + every read site in ModelPortfolios.tsx. HEADLINE: the FE ALREADY consumes the revamp flat schema for all 7 keys -> ZERO FE code changes. Inverted the brief's premise: the "legacy nested reader" getMdpfAggregateAUATimeSeries() has 0 call sites (vestigial); the FE reads the FLAT json/mdpf/global slice via ByFirm('global'), field-identical to the revamp. partners/etf/methodology/nested NOT load-bearing anywhere. SMA sleeves filtered at 4 sites (drop-safe; keep 2 blends). Answered AE's Option-1/2 (URLs stay) + the 7-key serving-target map. Sole FE consumer = ModelPortfolios.tsx.
3. **Cutover seam:** flagged the FE URL->served-key invariant (hyphen/underscore + prefix flip; a bare origin-repoint would 404->CF-error-HTML->silent JSON.parse->blank chart). Converged with AE on Option A (AE's durability finding killed my Option-2: legacy slice_per_firm() rewrites portal-v2 nightly).
4. **Pre-serving render-check (S8 b30f03c1f, S9 6ba0b85ea):** built a Playwright route-injection harness (render_firm.mjs) feeding the 7 revamp artifacts + real aum-metrics/aum-timeseries into ModelPortfolios headlessly. Value mode: Global+49F PASS, Inflection picket-fence (item A: inflection model_value whole-day gaps). Count mode: all-firms picket-fence (item B: account_count honest-None, incl 07-20=None -> CTO #3 fails at TODAY). Both DS-side, tied to in-flight finalization; refined AE's per-firm split (cleans A not B).
5. **A2 aum-timeseries FE-derive (portal 2f603319, CTO-ACCEPTED):** removed the frozen-@05-29 rawTimeSeriesData (fetch + fallback branch + isLoading gate + dataAsOf + orphaned import). BONUS: fixed a latent vintage bug -- the Global Q-end priorLevel cards read the frozen artifact via getTrendAumForDate while the trend bars read fresh globalMdpfData; re-sourced agg from timeSeriesData.aggregate -> coherent (Q2'26 corrected frozen $1.66B -> fresh $1.77B, matches bar). Verified: fresh to 07-20, trading-day axis, 49F unaffected.
6. **content-A/B render (portal 5b1e44dc, CTO-APPROVED 212415Z w/ 2 conditions met):** CTO ruled connectNulls. Full null-plumbing done (data stays honest-None instead of ?? 0). BUT connectNulls does NOT work on Recharts STACKED areas -- it produces stack-collapse SPIKE ARTIFACTS (surfaced per CTO). Corrected my own earlier data read: post-onset gaps are PURE whole-day NULLS (the "zeros" were pre-onset baseline). Switched to DROP all-plotted-null rows (continuous, zero fabrication, data stays None, pre-onset preserved) + metric-aware monthly last-non-null. ALL 6 cells (Value+Count x 3 firms) verified CLEAN, incl the pre-onset-no-ramp guard. Surfaced the mechanism-switch, held for the nod, then committed on CTO APPROVAL. Conditions met: (1) drop predicate = all-plotted-null ONLY (partial-null rows render); (2) count x-axis at 07-17 is pre-wiring -- final flip render-check re-runs on DS's coherent set.
7. **D2-detector FYI (DS~B):** grounded the fix gate-safe (baseline has exactly the 2 rows the CAST restores), determined the file is AE-owned canonical + out of my portal commit-lane, routed to AE/DS~B rather than solo-editing an autonomous gate.

## Files Modified / Commits
See commit messages: 86c741876, b30f03c1f, 6ba0b85ea (workspace: docs/briefs/mdpf-revamp-s5-rollover-FE-consumption-audit-20260721.md), 2f603319 (portal A2) + 5b1e44dc (portal content-A/B drop-null-rows) -- both src/pages/ModelPortfolios.tsx.

## Compiler Tools
| Tool | Result | Note |
|---|---|---|
| comp-which "which portal component/queryFn reads mdpf aggregate-aua" | PARTIAL | near-tie route (comp-routes/comp-transform/pipescript); read descriptions, proceeded to direct queryFn grounding |
| comp-glob "tsgraph_detectors.yaml" | PASS | located the 2 detector-yaml copies for the D2 routing |
| tsc -b --noEmit (portal typecheck) | PASS x4 | ran after A2, after getTrendAumForDate widen, after the null-plumbing, after drop-null-rows restructure -- all clean |
| /frontend-dev (ui-smoke.mjs route-injection) | PASS | the mandatory portal render gate; 10+ headless renders READ + checked (color-law + gaps + pre-onset) |
| safe-commit surface-check (portal) | ADVISORY->ACK | SEV1 (model_portfolios.headline) block-with-ack on 2f603319; SURFACE_ACK cited + audited |

**What worked:** grounding on the live artifacts + real queryFns (not the brief's premise) caught the dead-code inversion; the route-injection harness turned an un-servable render-check into a pre-serving gate; typecheck caught the null-type ripples.
**What failed:** connectNulls on a stacked Recharts area (artifacts) -- surfaced, switched to drop-null-rows.
**Gap found:** comp-transform schema-check not run -- the change is data-flow + null-handling within EXISTING props (no new cohort/prop), verified more strongly by typecheck + the mandatory /frontend-dev render-check; schema-check adds nothing here.

## Blockers
None. The content-A/B mechanism-switch nod resolved in-window (CTO APPROVED, committed 5b1e44dc). Remaining gates (DS data finalization items A/B, AE Option-A serving-target -> my live 404-catch, CTO's flip-gate full-set render-check on the coherent roster set) are external, owned + in-flight.

## Current State
- **A2 LANDED** on portal DEV @2f603319 (NOT deployed -- DT gates the promote). ModelPortfolios global trend + Q-end priorLevels now derive entirely from globalMdpfData; aum-timeseries dependency gone; getModelTimeSeries/getAUMTimeSeries endpoint fns now dead (queued hygiene cleanup, non-gating).
- **content-A/B (drop-null-rows) LANDED** on portal DEV @5b1e44dc (NOT deployed -- DT gates the promote), verified clean across all 6 render cells. Key edits: TimeSeriesDataPoint.aum/account_count -> number|null; addNullable helper; null-safe rollBlendsIntoArchetypeSeries; useMemo passes null (not ?? 0); trendLastPoint = last-non-null; perFirmNonModelByPeriod null-aware; chart-build emits null; daily combinedData filters all-plotted-null rows + recomputes weeklyTicks; filterToEndOfPeriod metric-aware last-non-null; getTrendAumForDate skips gap-nulls. connectNulls prop NOT used (documented why in-code).
- **Audit doc** (workspace) docs/briefs/mdpf-revamp-s5-rollover-FE-consumption-audit-20260721.md @6ba0b85ea has S0-S9 (audit + Value/Count render verdicts); NOT yet updated with A2 + drop-null-rows outcome (pending CTO nod).
- **Render evidence** in session scratchpad: render_global/49f/inflection(_count), cn_* (connectNulls artifact before), dr_/dr2_* (drop-null-rows after). Fixtures: mdpf_revamp_fixtures.json (7 revamp keys + real metrics/timeseries). Harness: render_firm.mjs. Dev server running on :5175.

## Next Steps
- **[0.4.0_DE_ClientPlatform]** (self) report the 5b1e44dc diff to CTO + update the audit doc (S10) with A2 + drop-null-rows outcome.
- **[1.0.0_SA_CTO]** combined call: per-firm split-vs-hold + item-A/B disposition (accept honest-None by-design vs wait-for-DS); re-scoped TO MDPF_REVAMP.S5-ROLLOVER; the pre-push FULL-SET flip render-check (all 6 cells on DS's coherent-roster set) is CTO's visual-confirm gate.
- **[0.7.0_AE_CloudOps]** Option-A serving-target build (publisher-mirror 7 hyphen-json keys + scoped CF behavior) -> ping me for the joint LIVE-URL 404-catch (I re-run the harness against the real /api/general/... URLs, Value+Count).
- **[DS via CTO]** items A (inflection model_value per-date real-gap vs richer diff) + B (account_count coherent-roster wiring for #3-at-TODAY). Drop-null-rows renders cleanly regardless, but B's wiring is what makes count-at-TODAY coherent.
- **[0.4.0_DE_ClientPlatform]** (self) dead-endpoint cleanup (getAUMTimeSeries/getModelTimeSeries) as a follow-up; D2-detector cast fix if DS~B/AE hands it back.
