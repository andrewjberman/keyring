# PRD — MDPF 49F Daily-AUA: full-history re-derivation on Schwab canonical cohort methodology

**Author:** 1.0.0_SA_CTO · **Trigger:** Andrew visual-review ruling 2026-06-01 (briefing 4bb7a0ecc, RD~B) · **Decompose:** 2.0.0_SA_COO → TOs · **Owners:** DS-CP (gold, mdpf_aggregate_aua.py) + DE/AE (pipeline + backfill) · **Verify:** DE serving-continuity + CVO.
**Status:** DRAFT — supersedes DS~B's 1/16-forward-exact + flag-pre-1/16 scope (3f26f909a/5ae318a65) AND the earlier "no-backfill" rec. DS~B's held 1/16-forward emit stays HELD pending this PRD's TO-decomposition.

## 1. Governing ruling (Andrew sovereign, 2026-06-01)
Re-derive the **ENTIRE 49 Financial per-firm Daily-AUA time series** on the Schwab canonical cohort methodology, back through history — eliminating the post-5/15 Black-Diamond→Schwab source seam (the ~$172M step), so the trend is continuous and on one basis. Canonical 3-cohort method:
- **1a = SmartX MODEL AUA** (daily; measured).
- **1c = SmartX SMA AUA** as a **CALCULATED DAILY value, INTERPOLATED** — exact per-date historical SMA is unavailable, so 1c is interpolated (Andrew-ruled acceptable). 
- **1b = PLUG = Schwab total − 1a − 1c** (daily residual).
- Total (= Schwab custody total) = 1a + 1b + 1c, all disjoint.

## 2. Scope
- 49 Financial per-firm series only (Global needs no work; Inflection separate). Full historical date range, subject to §4 feasibility.
- Replaces the per-partition methodology_version seam (v0_8_ruling2 ≤ boundary → v0_9_1) with a single Schwab-canonical derivation across the whole series.

## 3. Method detail
- **1a (model):** SmartX model daily values — already available; use directly.
- **1c (SMA), interpolated:** define the interpolation basis explicitly (e.g. linear/forward interpolation between known SMA reference points to a per-date daily value). DS-CP specifies + documents the exact interpolation in the gold script + provenance. The interpolated nature MUST be recorded in meta/provenance (calculated, not measured) — see §6.
- **1b (plug):** Schwab daily custody total − 1a − 1c, per date.
- Carry the WS-E production-logic mechanism + the exact-vs-estimate map DS~B already built (3f26f909a) as inputs — they inform which dates are measured vs interpolated.

## 4. CRITICAL feasibility — Schwab-anchor horizon (surface to Andrew)
DS~B empirically validated the Schwab restriction: exact Schwab daily total is feasible **1/16/2026 → 5/17** (4/15: $1,556M Schwab-restricted vs $1,699M full-book; 17 unmatched ~$5.9M). **SHARPENED (COO/DS~B 171034Z):** pre-1/16 there is NO Schwab CUSTODY SOURCE AT ALL — the per-account Schwab-restriction source (BD silver/allocations) only begins 2026-01-16. So pre-1/16 it is NOT just 1c that's missing — the **Schwab custody TOTAL itself** (the 1b/total anchor) does not exist. "Schwab all the way back" is therefore under-specified: it presumes a custody source that isn't there.
- **1/16-forward:** exact Schwab total + interpolated 1c → clean canonical re-derivation. Definitely in scope.
- **Pre-1/16 (NO Schwab custody source):** the ENTIRE pre-1/16 49F series becomes a **back-cast/estimate** — requiring a specified CUSTODY back-cast method (proxy from the 1/16 Schwab base), not merely 1c-interpolation. This is consistent with Andrew's interpolate-don't-flag intent, BUT it means pre-1/16 is **fully estimated (custody + 1c), not measured** — which is a bigger honesty step than 1c-interpolation alone. DS-CP proposes the custody back-cast method; **Andrew signs off that pre-1/16 is fully-interpolated-estimate** (or rules a boundary: start-canonical-at-1/16 with pre-1/16 on old-basis/gapped). **Do NOT silently present an estimated pre-1/16 as actual.** First TO output (gate before backfill): confirm the 1/16 custody floor + put the pre-1/16 full-estimate-vs-boundary choice to Andrew.

## 5. What it replaces / supersedes
- The post-5/15 BD→Schwab seam (~$172M step) — eliminated by single-basis derivation.
- DS~B's 1/16-forward-exact-only + flag-pre-1/16 scope, and the earlier no-backfill rec — Andrew now wants the interpolated re-derivation (option ii/iii), not flag-the-gap.

## 6. Data-honesty (HARD, per session-standing bar)
The interpolated 1c (and any estimated pre-1/16 total) are Andrew-ruled-acceptable, BUT must be **labeled as calculated/interpolated in provenance**, and ideally given a render treatment (estimate marker / footnote) so the trend Andrew reads each morning never presents interpolated values as measured. DE's continuity-verify harness must check that estimated regions are flagged, not silently continuous.

## 7. Owners + verify
- **DS-CP:** the gold re-derivation logic in mdpf_aggregate_aua.py (the canonical 3-cohort calc + 1c interpolation) + the meta provenance. ds-commit-gate.
- **DE/AE:** the historical backfill pipeline + re-emit of the per-firm partitions; AE for any infra. comp-pipescript io.
- **DE:** serving-continuity verify (the harness that FAILs on the current seam, PASS post-re-derive + flags estimated regions).
- **CVO:** independent verify of the re-derived series (continuity + total-preservation + estimate-labeling) before it's presented as canonical.

## 8. Acceptance criteria
- AC1: 49F series derived by the single Schwab-canonical 3-cohort method 1/16-forward (no v0.8/v0.9 seam in that range).
- AC2: 1c is a per-date daily interpolated value with the interpolation method documented in provenance; total = 1a+1b+1c holds per date (DIFF~0).
- AC3: pre-1/16 disposition per Andrew's §4 ruling; estimated regions flagged, never shown as measured.
- AC4: the ~$172M 5/15-region step is gone (continuous trend); DE continuity-verify PASS.
- AC5: CVO independent verify PASS before the re-derived series serves to the portal.

## 9. Open items for Andrew (first-TO surface)
- §4 pre-1/16 disposition (estimate-total / old-basis / start-at-1/16).
- The 1c interpolation basis (DS-CP proposes; Andrew confirms if it materially affects the displayed numbers).
