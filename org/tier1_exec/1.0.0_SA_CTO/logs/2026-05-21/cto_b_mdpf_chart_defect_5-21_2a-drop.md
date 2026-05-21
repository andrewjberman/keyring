# CTO~B Session Log — MDPF Daily AUA chart defect (5-21 Inflection-2a drop)

**Agent:** 1.0.0_SA_CTO~B
**Date:** 2026-05-21
**Trigger:** Andrew manual smoke-test of the Model Portfolios "Daily AUA Analysis" chart (post-MDPF_ASSETS close).

---

## Current State

Andrew's 5/21 smoke of the live Daily AUA chart found a ~$95M overnight drop on 2026-05-21 ($1.75B -> ~$1.65B) — "for no reason." CTO~B diagnosed it by direct S3 artifact read: **the headline data is correct; the chart-feed artifact is wrong.** A DS~B emitter-fix TO is dispatched (3 phases). MDPF_ASSETS re-opened for the hotfix.

## The finding

The "Daily AUA Analysis" chart shows yesterday (5-20) ~$1.75B (correct) and today (5-21) ~$1.65B — a fake ~$95M cliff. 2026-05-21 15:00Z was the **first automated v0.9 daily chain run** (every prior live value was the `.028` manual re-emit).

## Diagnosis — localized to the legacy emitter

Read both artifacts directly off S3:

- **Platinum `s3://opal-data-portal-v2/platinum/mdpf/aggregate_aua/2026-05-21.json` — CORRECT.**
  `opal_aggregate_aua` = **$1,744,192,354.67**; Inflection 2a present (~$93.08M); ~flat vs 05-20's $1.748B. The headline did NOT drop.
- **Chart-feed `s3://opal-data-portal-v2/json/portfolios/aum-timeseries.json` — WRONG.**
  `aggregate.aum` for 2026-05-21 = **$1,347,808,273.25** = the 49F partner's `model_aua` = **1a only**. The 05-18/19/20 points are ~$1,441-1,443M (1a **+** Inflection 2a). The 2026-05-21 point **dropped the ~$93M Inflection 2a layer** every prior point carries.
- **=> the portal faithfully renders a wrong artifact.** Not a portal bug, not a data-drop in the headline — the legacy emitter's daily-forward path.

**Root cause (for DS~B to confirm + fix):** `build_legacy_compat_emit.py`, on the daily-forward path, built the `aum-timeseries.json` 2026-05-21 aggregate point without folding in the Inflection 2a. Strong candidate: `.030` treated `aum-timeseries.json` as "verify-only" (v0.9 changed only the 1b basis) — the daily-forward 2a-handling was never exercised/verified. This is exactly the gap `0.7~B`'s first-v0.9-chain readiness check explicitly did NOT cover ("downstream gold-runner completion is DS-side, not verified by this check").

## 5-18 cross-reference validation (Andrew-directed)

**Q1 — is the 5-18 point T-1 (5-15 data)?** No. The 2026-05-15 partition is **49F-only** (no Inflection partner; `cohort_2b_audit: 0`); 2026-05-18 is the **first** partition with the Inflection partner. The onset is genuinely at the 05-18 label — not 5-15 carried forward. The exact data-vintage (does the chain run T-1 — what calendar date the 05-18 Inflection block is as-of) -> DS~B Phase C.

**Q2 — the ~$93.6M Inflection by_model breakdown.** The 2026-05-18 platinum Inflection partner `by_model`:

| Model | Value | Accts |
|---|---|---|
| Intermediate (pure) | $56,928,080.04 | 159 |
| 50/50 INT/LTC | $20,246,950.90 | 127 |
| Long-Term Conservative | $6,120,468.20 | 54 |
| 50/50 ST/INT | $6,006,529.13 | 21 |
| Short-Term | $2,396,689.47 | 10 |
| Long-Term Aggressive | $1,517,283.07 | 23 |
| Ultra Short-Term | $387,054.64 | 5 |

The platinum **correctly keeps the blends as distinct labeled rows** (`50/50 INT/LTC`, `50/50 ST/INT`) — NOT dumped into Intermediate. But the chart's `aum-timeseries.json` `by_model` has only the **5 pure Opal-model buckets** — so the emitter must fold the blends into those 5. Andrew's observation "virtually all the Inflection money went to INT" -> suspected: the emitter folds `50/50 INT/LTC` + `50/50 ST/INT` **wholesale into Intermediate** (pure-INT $56.9M + the two blends $26.3M ≈ $83M *looking* like INT). Andrew directive: the 50/50 blends must be **split 50/50** into their pure-model components — `50/50 INT/LTC` -> ½ Intermediate + ½ LTC; `50/50 ST/INT` -> ½ Short-Term + ½ Intermediate.

## Dispatch

DS~B emitter-fix TO authored via COO~B (CTO~B msg 172611Z) — `build_legacy_compat_emit.py`, 3 phases:
- **A (urgent):** fix the daily-forward 2a fold; re-emit the 2026-05-21 chart-feed point(s); verify the ~$95M cliff is gone; regression-check tomorrow's 15:00Z run.
- **B:** the Inflection `by_model` 50/50-blend fold — split the blends 50/50 into pure-model components; also check `non_model_assets.json` for the same daily-forward-path defect class.
- **C:** characterize the T-1 / data-vintage of the 5-18 Inflection onset.

MDPF_ASSETS re-opened for the hotfix (closed-with-an-open-hotfix; same discipline as the `.032`/`.031`-A4 1c fix).

## Next Steps

| Recipient | Item |
|-----------|------|
| **2.0.0_SA_COO~B** | Author + GO the DS~B emitter-fix TO (3 phases A/B/C). Re-open MDPF_ASSETS for the hotfix. |
| **0.4.0_DS_ClientPlatform~B** | Execute the fix; RAVC2 to COO~B CC CTO~B. |
| **1.0.0_SA_CTO~B (self)** | Output-validate the fix RAVC2 — chart cliff gone, the Inflection 50/50 by_model split correct, the T-1 vintage stated. |

## Process note

`0.7~B`'s first-v0.9-chain readiness check (3/3 PASS) verified the EventBridge trigger fired with v0.9 code — but explicitly NOT the downstream chain OUTPUT ("downstream gold-runner completion is DS-side"). The defect landed exactly in that uncovered gap. The first automated run of a re-scoped pipeline should have its OUTPUT artifact-verified, not just its trigger — a sharper readiness check would have caught the 2a-drop before Andrew's smoke.
