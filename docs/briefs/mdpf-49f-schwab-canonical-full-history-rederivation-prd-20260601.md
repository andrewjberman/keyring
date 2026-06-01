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
- 49 Financial per-firm series — full historical range, subject to §4 feasibility. Replaces the per-partition methodology_version seam (v0_8_ruling2 ≤ boundary → v0_9_1) with a single Schwab-canonical derivation.
- **GLOBAL — CORRECTED (DE scope-probe 1832Z; "Global needs no work" was WRONG):** Global's pre-5/18 aggregate still sums OLD-49F, not the re-derived 49F → a **$180.75M coherence gap** (49F slice = seam-closed but Global = seam-open; a consumer comparing them sees a contradiction). Global needs a **MECHANICAL RE-AGGREGATION from the re-derived 49F partitions (TO-1b, FIX-class — not a re-derive)**. Post-5/18 Global already aggregates coherently (residual 0).
- **INFLECTION — CLASSIFICATION IN RECONCILIATION (1836Z; DO NOT build TO-1c-as-re-derive until settled).** Three reads bounced (DE distinct → DS~B same-class → COO funding-breakout); the determining fact = **were Inflection's models FUNDED ~5/18?** COO+DE arithmetic (−97.7M non_model + 93.6M model = −4.1M continuous total) says YES = a genuine model-funding breakout (pre-5/18 had NO models → all-non_model is HONEST), NOT a Schwab basis seam → NO re-derive, only an Andrew DISPLAY choice (accept honest funding-breakout vs cosmetic pre-5/18 back-decompose). PENDING DS~B's concur on the funding framing; the FINAL §2 classification + any TO-1c (display-only if so) lands on convergence — frozen until then. The struck text below is the superseded mid-flight read, retained for the trail:
- ~~**INFLECTION — RE-CLASSIFIED SAME-class (DS~B 1834Z, methodology-owner, SUPERSEDES DE's lighter total-level probe):**~~ the total IS continuous (DE correct: custody −$4.1M), BUT that MASKS a wrong pre-5/18 decomposition: pre-5/18 is BACKFILLED-history non_model (~$186-200M, `build_mdpf_inflection_history_from_spine`) on a DIFFERENT basis than post-5/18 LIVE (~$107M) — pre-5/18 lumped models into non_model (model=0), so the non_model BAND shows a FALSE −$97.7M step at the v0.9 cutover. This is the SAME-class BD→Schwab basis seam on the Inflection side, NOT a legitimate total-preserving event — Andrew reads the BANDS (model vs non_model), which step falsely. **→ TO-1c: Inflection pre-5/18 Schwab-class re-derive (mirror TO-1a's method on the Inflection cohort); near-term required (Global is Andrew's default view, the residual renders as a real false drop).** DS~B hands the exact Inflection residual numbers post its aggregate-fix verify.
- **GLOBAL CLOSE (COO scope-split):** (i) Global AGGREGATE re-propagation (DS~B emit gap — rewrote the 49F partner block not the aggregate headline; ~$143M @4/15) = IN TO-1a, fixing now (TO-1a global leg stays open until re-verified); (ii) Inflection pre-5/18 re-basis = TO-1c (above). MDPF data-half closes only after BOTH land + DE/CVO re-verify Global.
- *(Lesson: a methodology classification needs the methodology owner's read — DE's total-level probe reached "distinct/accept"; DS~B's backfill-basis read reversed it to "same-class/re-derive." Don't finalize a class on a light total-only probe.)*

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
- AC6 (folds Item-3, COO 171034Z): the re-derive's date-selection is WEEKDAY/TRADING-CALENDAR-AWARE — drops spurious weekend/holiday partitions (root cause of the 12/27/2025 Saturday anomaly: INF→$0, 49F all-into-UST) and emits ALL business days (the 12/27 backfill also dropped 12/30-31). One coherent re-emit so the spurious-weekend class can't reintroduce. (A standalone glitch-clean of the visible 12/27 spike is GO'd separately by COO now, independent of basis; this AC is the permanent class-fix.)

## 9. Open items for Andrew (first-TO surface)
- §4 pre-1/16 disposition (estimate-total / old-basis / start-at-1/16).
- The 1c interpolation basis (DS-CP proposes; Andrew confirms if it materially affects the displayed numbers).
