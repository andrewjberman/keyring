# COT data-injected render -- P1 served-data gap CONFIRMED (delta since d26ddf807)
**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE

**Agent:** 0.4.0_DE_ClientPlatform · **Window:** 2026-06-22 ~18:46Z -> ~19:05Z · **Task:** COT ADVI v1 go-live FE render smoke (Andrew HIGHEST-PRIORITY), COO-directed data-injected render (option a) · 0 code commits · ~6 significant MCP.

## Current State
Per COO steer (option a), ran the data-injected local render to empirically resolve: does the COT Distribution surface degrade-to-snapshots (by-design-fine) or go-EMPTY (P1 gap) when partner_analytics_quarterly is absent? ANSWER (pixel-confirmed): goes EMPTY -> P1 SERVED GAP. Routed CVO for the by-design ruling.

## The finding chain (all grounded)
- [SERVED-CONFIRMED, boto3 whole-bucket]: partner_analytics_quarterly.json + header_metrics_fresh.json ABSENT from opal-data-cot (2080 keys); inf serves both. cot has the gold SCRIPT (code/gold/D_01.partner_analytics.py) but no emitted artifact.
- [SOURCE-CONFIRMED]: DistributionTab distribution data = `rawData = activeView?.data ?? []` from getPlatinumPartnerAnalytics ONLY (L854/1398); nnaViews/periodView likewise (L2584). NO snapshot fallback. header_metrics_fresh absence is GRACEFUL (?? fallback to header_metrics; = the AC8 pmv-degrade).
- [OBSERVED, data-injected render]: cottonwood session, real 06-18 artifacts served from dev public/_cot_smoke/, partner_analytics_quarterly left absent. innerText capture:
  - Header RENDERS: "TOTAL AUM $395M as of Jun 18, 2026", NEW CLIENTS $395M. ✓
  - SEGMENT ANALYTICS / Distribution (Cohort GEO): "Analytics data unavailable" -- EMPTY, graceful (no crash/blank/error-boundary). ✗
  - Disabled-surface NON-LEAKAGE confirmed pixel-side: Cohort = GEO only (no ADV/OFC), Snapshot/Continuous view, no Advisors/Books tabs. Matches OUTCOME-B.
  - Data Source footer: "Last update: N/A".

## VERDICT
COT v1 Distribution surface (the ONLY v1 tab) goes EMPTY without partner_analytics_quarterly -> render-NOT-ready = a P1 served gap, NOT a clean degrade. Header surface + disabled-non-leakage + graceful-degrade behavior all GREEN. Resolution: CVO design-intent ruling (expected-for-COT vs by-design-empty); if expected -> DS/AE emit partner_analytics_quarterly for COT (inf already serves it), I re-smoke, launch. Caught PRE-provisioning (smoke-first working).

## CAVEAT (faithfulness, Rule 22)
Vite dev SPA-fallback serves index.html (200, HTML) for missing public/ files, NOT a clean 404 -> the FE's response.json() parse-fails -> react-query error -> the SAME "Analytics data unavailable" graceful state as a live CF 404. So the empty-Distribution + graceful message faithfully reproduce real behavior; the render is decision-valid. (Distinguish present-vs-absent by content, not HTTP status, under this method.)

## Blockers
None blocking my leg (delivered). COT go-live is BLOCKED on the partner_analytics_quarterly emit IF CVO rules it expected (CVO ruling pending). My prior gates still event-pending (TO-2 served-verify/DS, P2-1/AE P2-2).

## Next Steps
- **[3.0.0_SA_CVO]** design-intent ruling: partner_analytics_quarterly expected-for-COT (=> DS/AE emit) or by-design-absent.
- **[2.0.0_SA_COO]** on CVO ruling, dispatch DS/AE emit (P1); I re-smoke post-emit.
- **[0.4.0_DE]** re-render COT once partner_analytics_quarterly is served -> confirm Distribution populates.

## Compiler Tools
| Tool | Run | Result |
|---|---|---|
| boto3 list/get (not raw-aws-CLI) | opal-data-cot whole-bucket (2080 keys) + bd/inf compare | partner_analytics_quarterly + header_metrics_fresh ABSENT for cot, PRESENT for inf -- the gap |
| Grep/Read (native, rail-ok) | DistributionTab + endpoints data-flow | DistributionTab distribution sourced SOLELY from getPlatinumPartnerAnalytics, no snapshot fallback |
| playwright (browser) | data-injected render, dev public/ inject + auth-stub | header $395M renders; Distribution "Analytics data unavailable" (empty); disabled-non-leakage confirmed |

Compiler note: comp runs this window mis-attribute to AE0.7's TO_ID in compiler-tools-log (concurrent shared `.comp-graph/.agent_context`, AE0.7 active COTETL). Left intact; serial correct.

## MCP traffic (this window)
~6: COO option-(a) GO; my finding-routing to CVO+COO (185511Z/185520Z); source-confirmed conclusion to CVO (185705Z); pixel-result RAVC to COO (190427Z) + CVO (190434Z).
