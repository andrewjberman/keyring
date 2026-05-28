# CVO verify — MDPF_SCOPED AUA Trend Analysis (Andrew-directed empirical, 2026-05-28 ~2330Z)

**archetype:** VALIDATE
**Trigger:** Andrew direct — 3 portal observations on Model Portfolios AUA Trend (49F + Inflection + model renames).
**Artifacts read:** s3://opal-data-portal-v2/json/mdpf/{inflection,49financial}/aggregate-aua-timeseries.json + ModelPortfolios.tsx + benchmarks.ts MODEL rename map. Source script: data/mdpf/scripts/backfill/build_aggregate_aua_timeseries.py.

## F1 — Inflection total IS correctly scoped (~$204M ≈ canonical $205.53M) — NOT full Orion (refines Andrew's hypothesis)
Latest 2026-05-28: model_aua $96,211,990 + non_model_aua $107,772,055 = partner_custody_total **$203,984,045**. MAX over the whole series = $203.98M (no date reaches 300M+). 49F by contrast = **$1.3B** (full firm). So Inflection IS Inflection-scoped at the total level — the "pulling full Orion" read is refuted by the $204M total (full Orion would be ~$1.3B-class). BUT a **~$1.5M gap** vs canonical $205.53M because MDPF sources from `platinum/mdpf/aggregate_aua/` decomposition, not the canonical transaction-history spine that Assets Overview uses. → **DS:** source MDPF Inflection AUA from the same daily-AUA spine (Assets Overview) — closes the $1.5M gap + avoids recreating decomposition (Andrew's exact ask).

## F2 — The 300M+ in the area chart is NOT in the data (max $204M) → chart stacking double-count
ModelPortfolios.tsx:335 uses partner_custody_total for the aggregate LINE (correct, $204M). The 300M+ is a render artifact: stacking the custody-total band ($204M) alongside component bands (non_model $107.77M) double-counts → $311M ≈ "300m+"; or model ($96M) + custody ($204M) = $300M. → **RD:** verify the Inflection area chart's stacked bands sum to the $204M artifact total; partner_custody_total must be a LINE only, not also a stacked band. (Empirically the data cannot produce 300M+.)

## F3 — Inflection trend 392/400 dates NULL — only 8 days (2026-05-18 → 05-28) populated
S2 rolling-365d gray non-model AUA backfill is mid-run (COO: mdpf-daily-runner PID 2493, ETA ~03:30Z). Matches Andrew "nowhere near done but a start." Not a bug — S2 backfill incomplete; trend stays sparse until it finishes. First non-null = 2026-05-18 (the Inflection funded-models date per PRD S2).

## F4 — 49F: ~$42M model/non-model RECLASSIFICATION on 2025-12-26 (the ~12/27 aberration)
Day-over-day around Andrew's 12/27: 2025-12-26 dModel **+$42,372,985** / dNonModel **−$35,862,809** / net custody +$7.29M; 12/27 itself smooth (+$343K). So the visible aberration is a model↔non-model reclassification on 12/26 (day after Christmas, thin data) — model band steps up $42M while non-model drops $36M. → **DS:** investigate the 12/26 model-tagging reclassification (likely a holiday-week classification artifact; the custody total is smooth, the model/non-model SPLIT jumps).

## F5 — Model renames NOT applied (Andrew's #3 — CONFIRMED at the data layer)
MDPF by_model `display_name` carries OLD names, not S4 canonical:
| artifact display_name | S4 canonical (should be) |
|---|---|
| Intermediate | Intermediate Term |
| Short-Term | Short Term |
| Ultra Short-Term | Ultra-Short Term |
| Long-Term Conservative | Long Term (LT) |
| Long-Term Aggressive | Ultra-Long Term (ULT) |
ModelPortfolios.tsx:346 reads `modelData.display_name` directly. The S4 rename map exists (benchmarks.ts:49-50 LTC→'Long Term', LTA→'Ultra-Long Term') but is keyed on short-codes (LTC/LTA/UST/ST/INT) used by OTHER pages — it is NOT applied to the MDPF AUA-trend artifact's long-form display_name strings. → **DS** (emit display_name with S4 canonical names in build_aggregate_aua_timeseries.py / its upstream) OR **RD** (route display_name through the S4 rename). Per S4's "display-mapping layer" intent, the canonical names must reach this surface; today they don't.

## Verdict
MDPF AUA Trend is genuinely early (S2 backfill mid-run). Correctly Inflection-scoped at the total (refutes full-Orion). 5 mechanism-specific items routed: F1+F4+F5 → DS; F2+F5 → RD; coordination → COO. None demo-blocking for ADVI (separate project); these are MDPF_SCOPED S1/S2/S4 maturation items Andrew surfaced.

— 3.0.0_SA_CVO
