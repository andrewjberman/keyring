# MDPF_REVAMP.S5 -- dead-endpoint cleanup + Andrew A2->canonical-read redirect + field-identity handoff

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, VALIDATE, COORDINATE
**Serial:** 0.4.0_DE_ClientPlatform · **Date:** 2026-07-21 (2233Z) · **TO:** MDPF_REVAMP.S5-ROLLOVER (CTO-gated)
**Window:** since last log @239951086 (post content-A/B commit) -> now.

## Summary
Closed the queued FE hygiene (dead-endpoint cleanup + audit-doc S10), then handled a mid-flight Andrew redirect: A2 aum-timeseries goes from FE-derive to a CANONICAL FRESH artifact (DS-produced off the aggregate, same URL via routing). Surgically reverted the A2 FE-derive to a repoint-only canonical read while PRESERVING content-A/B; net FE vs pre-A2 = ZERO. Verified priorLevel coherence on a constructed fresh fixture; sent DS the field-identity contract for a clean first-time flip render. CTO ACCEPTED every step; FE-side A2 complete.

## MCP traffic (window)
~12 messages, all CTO except one to DS. Significant: CTO A2-ACCEPTED -> connectNulls-approval (2 conds) -> content-A/B ACCEPTED (dispositions LOCKED: HOLD-ALL split, A1=DS-builds) -> ANDREW-REDIRECT (A2->canonical-produce) -> plan-ACK -> canonical-read-ACCEPTED + field-identity-gate. OUT: field-identity contract -> 0.4.0_DS_ClientPlatform (aggregate.aum = Sum non-sma model_value; CC/routing-ask -> CTO).

## Work done
1. **Dead-endpoint cleanup (portal 1508d183):** removed getAUMTimeSeries + getModelTimeSeries (0 consumers after A2) from aum.ts + portal-proxy.ts (-107 lines). SEV1-ack. Typecheck clean; sanity-rendered.
2. **Audit doc S10 (28776ade8):** implementation-outcome section (A2 + content-A/B + cleanup + locked dispositions + flip-gate remaining step).
3. **ANDREW REDIRECT -> A2 canonical repoint-only read (portal aa8c0420):** CTO 221221Z relayed Andrew's redirect -- aum-timeseries becomes a CANONICAL FRESH artifact (DS off the aggregate, served from opal-data-assets via the same /api/general/portfolios/aum-timeseries.json URL). A plain git-revert of A2 (2f603319) would conflict with content-A/B (stacked on it), so did it SURGICALLY:
   - RESTORED: git revert --no-commit of cleanup 1508d183 (endpoints back) + manual reverse of the 6 A2-derive sites in ModelPortfolios (fetch, import, isLoading, dataAsOf, useMemo fallback branch, priorLevels agg=rawTimeSeriesData.aggregate).
   - PRESERVED content-A/B: all null-plumbing + drop-whole-day-null-rows + metric-aware monthly. THE SUBTLETY (CTO-confirmed): the restored fallback ALSO passes null (not ?? 0) -> uniform whole-day drop.
   - Net FE vs pre-A2 = ZERO (repoint-only). Vintage-bug fix STAYS FIXED via the fresh artifact (fix was "read fresh"; canonical IS fresh). Global VALUE stays globalMdpfData-PRIMARY; rawTimeSeriesData = fallback + priorLevels.
4. **Verification:** typecheck clean. Could NOT use the OLD aum-timeseries fixture (frozen-05-29 -> would show the vintage bug back), so CONSTRUCTED a FRESH fixture off the revamp aggregate (aggregate.aum = Sum non-sma model_value = DS's canonical target) and rendered: Global Value priorLevel COHERENT (Q2'26 $1.77B, matching trend bar, identical to A2-derive) + fresh to 07-20; Global Count + Inflection Value content-A/B gaps intact + pre-onset preserved. Honest caveat surfaced (fixture=simulation; definitive check = flip gate on DS's live artifact). CTO accepted the claim discipline.
5. **Audit doc S11 (7d4a5bfa8):** the supersession + DEV lineage.
6. **Field-identity handoff:** sent DS the exact aum-timeseries shape + aggregate.aum computation so DS's producer targets it (flip-gate check = DS-output == fixture); routing-ask to CTO if a different DS owns the producer.

## Files Modified / Commits
See commit messages: portal 1508d183 (cleanup), aa8c0420 (A2 canonical revert, 3 files); workspace 28776ade8 (S10), 7d4a5bfa8 (S11).

## Compiler Tools
| Tool | Result | Note |
|---|---|---|
| tsc -b --noEmit (portal typecheck) | PASS x4 | after cleanup, after each revert stage -- all clean |
| /frontend-dev (ui-smoke.mjs route-injection, FRESH fixture) | PASS | Global V/C + Inflection V clean; priorLevel coherence proven on the constructed canonical fixture |
| safe-commit surface-check (portal) | ADVISORY->ACK x2 | SEV1 block-with-ack on 1508d183 + aa8c0420 (model_portfolios); SURFACE_ACK cited + audited |
**What worked:** the constructed-fresh-fixture trick proved priorLevel coherence pre-emptively (the old frozen fixture couldn't); git revert --no-commit cleanly restored the endpoints for bundling. **What failed:** nothing this window. **Gap:** no new comp-tool -- FE data-flow revert + null-handling, verified more strongly by typecheck + the mandatory /frontend-dev render than by comp-transform.

## Blockers
None. Every step CTO-ACCEPTED in-window. Remaining = external flip gate (DS live canonical set + AE serving-target).

## Current State
Portal DEV MDPF_REVAMP.S5 FE lineage: 2f603319 (A2 derive) -> 5b1e44dc (content-A/B) -> 1508d183 (cleanup) -> aa8c0420 (revert A2+cleanup, preserve content-A/B). NET = pre-A2 FE + content-A/B; whole FE is repoint-only. DT-gated for promote (not deployed). The FE reads canonical aum-timeseries (priorLevels + transient fallback) + globalMdpfData-PRIMARY trend + drop-whole-day-null-rows render. Field-identity contract for the canonical producer: aggregate.aum = Sum non-sma model_value (SMA excluded, blends included), account_count = Sum non-sma, honest-None preserved (null, not filled), periods = trading-day frontier. Fixtures/harness in session scratchpad (mdpf_fixtures_freshaum.json + render_firm.mjs); dev server on :5175. Audit doc docs/briefs/mdpf-revamp-s5-rollover-FE-consumption-audit-20260721.md @7d4a5bfa8 (S0-S11).

## Next Steps
- **[0.4.0_DS_ClientPlatform / DS producer owner via CTO]** build the canonical aum-timeseries to the field-identity contract (aggregate.aum = Sum non-sma model_value) so the flip render is coherent first-time.
- **[0.4.0_DE_ClientPlatform]** (self) FLIP-GATE full-set render-check (all 6 cells) on DS's LIVE canonical set -> extends Count to 07-20; + the live 404-catch on AE's serving-target. CTO's visual-confirm gate.
- **[0.7.0_AE_CloudOps]** Option-A serving-target (publisher-mirror + scoped CF behavior) -> ping me for the joint LIVE-URL check.
