# MDPF Cohort-1c — Serving-Data Continuity Verify (5/18 boundary)

**Author:** 0.4.0_DE_ClientPlatform
**Date:** 2026-06-01
**archetype:** VALIDATE
**secondary_archetypes:** TRACE, DIAGNOSE
**Dispatch:** COO (2.0.0_SA_COO) redirect — data-side check pairing RD~B's per-firm trend rollup fix. Asked: "confirm in the SERVING data that combined (1b+1c) non_model is genuinely continuous across the 5/18 boundary (total AUA unchanged pre/post) so RD's FE rollup has correct numbers to sum."
**Verdict:** **CONDITIONAL** — the ~$25M SMA(1c) is real & present (RD has a correct number to surface), BUT the "combined 1b+1c non_model continuous across 5/18 / total unchanged" premise does NOT hold against the serving data, and the ~$25M lives in **model/SMA-sleeve space**, not non_model.

> **RESOLUTION (2026-06-01, post-reconcile — see §Reconciliation below):** Andrew-direct ruling = **"fold SMA everywhere"** (displayed non_model = `non_model_aua + sma_aua`). This SUPERSEDES the F5-stack recommendation originally in this brief. My data **validates the fold**: because `sma_aua` is additive-separate (NOT already inside `non_model_aua`, confirmed to the dollar by DS~B), the fold does not double-count; and it keeps SMA inside non_model on BOTH sides of the seam, so it avoids introducing an SMA-step on top of the methodology seam (which the F5-stack would have added). The real `-$172M` item is a Black-Diamond->Schwab source change (routed DS~B). DS~B confirmed both data flags + withdrew its earlier non_model-fold-of-the-residual rec.

## Artifacts read (live S3, not assumed)
- `s3://opal-data-portal-v2/json/mdpf/49financial/aggregate-aua-timeseries.json` (91,886 B, generated `2026-06-01T13:34:20Z`)
- `s3://opal-data-portal-v2/json/mdpf/global/aggregate-aua-timeseries.json` (36,798 B, same gen)
- Schema (per-firm): `dates[]`, `model_aua[]`, `sma_aua[]`, `non_model_aua[]`, `partner_custody_total[]`, `by_model{model_id:{display_name,cohort_class,model_value[]}}`, `meta`. Global adds `opal_aggregate_aua[]`; lacks `by_model`/`partner_custody_total`.

## Finding 1 — decomposition is exact to the dollar; SMA is NOT inside non_model
`by_model` has 7 entries: 5 `cohort_class='model'` (the base models) + 2 `cohort_class='sma'` (`opal_div_sma`, `opal_growth_sma`). On the latest date:
- `Σ(5 base model_value) − model_aua = $0`
- `Σ(2 SMA sleeve model_value) − sma_aua = $0`
- `Σ(all by_model) = model_aua + sma_aua` (SMA sleeves are **additive siblings of the base models**, not a slice of non_model).

=> The ~$25M SMA(1c) is **model-stack space**. `non_model_aua` (1b) does not contain it.

## Finding 2 — SMA(1c) trajectory across the boundary: null -> $24.9M (3 regimes)
| Regime | dates | sma_aua |
|---|---|---|
| Historical backfill | 2024-11-01 .. ~late-2025 | flat ~$19.67M (the `.031`-A4 re-derived value; = the `.032`-probe seam figure $19,673,469.29) |
| Recent live, pre-breakout | ~2026-04-28 .. 2026-05-15 | **null** (not broken out) |
| Live breakout | 2026-05-18 -> | $24,903,349 -> $25,101,900 (real per-sleeve) |

So crossing 5/18 the SMA series goes **null -> $24.9M**. RD has a correct **live** number from 5/18 onward, but there is a **null-gap immediately pre-5/18** (4/28-5/15) — a naive "sum 1b+1c across the boundary" has nothing to add on the left side.

## Finding 3 — non_model (1b) is NOT continuous across 5/18 (documented methodology seam)
49financial, daily:
| date | model_aua | non_model_aua | sma_aua | partner_custody_total |
|---|---:|---:|---:|---:|
| 2026-05-15 | 1,349,270,403 | 455,549,313 | null | 1,804,819,716 |
| 2026-05-18 | 1,340,415,278 | 283,529,330 | 24,903,349 | 1,648,847,957 |
| delta | -8,855,125 | **-172,019,983** | +24,903,349 | **-155,971,759** |

- non_model **-$172M** at 5/18 = the **largest non_model day-over-day step in the entire 402-date series**. `non_model+sma` still steps **-$147M**. partner_custody_total **-$156M**.
- Global: non_model **-$270M**; headline `opal_aggregate_aua` only **-$62M** (≈ normal — the series-max headline step is **-$142M on 2026-04-03**, not 5/18). So 5/18 is an **internal re-decomposition** (value reattributed model<->non_model) at a methodology seam, with the cross-firm headline ~continuous.
- Root cause (meta `cohort0_historical_backfill`): historical partitions `2026-01-17..2026-05-17` were re-run on the **v0.8 / Ruling-2** basis (MDPF_ASSETS_016); `>=5/18` is **live v0.9** (`mdpf_assets_029_v0_9_rps_calibrated`, `mdpf_assets_031_v0_9_2024depth`). The v0.9 live basis measures non_model ~$172M lower (49f).

=> Adding the ~$25M SMA does **not** close the 5/18 seam (off by ~1 order of magnitude). The seam is real and documented; it will remain visible in any trend drawn continuously across 5/18.

## Finding 4 — narrative-vs-data tension (flag to DS~B)
`meta` states *"Cohort 1c (SMA) is a non-additive sub-slice of 1b."* The serving `by_model` treats the SMA sleeves as **separate additive `cohort_class='sma'` models** (= `sma_aua`, sitting alongside `model_aua`, not inside `non_model_aua`/1b). These two statements conflict. Same provenance-contradiction class as today's FIND_INSURE dormant-vs-active table fix — worth DS~B reconciling so the contract narrative matches the emitted structure.

## Implication for the RD~B FE fix
- **Correct fix = F5 (already flagged by RD~B in the merged matrix):** drive the trend stacked-chart model iteration from the **per-firm `by_model` key-set** so the 2 SMA sleeves (`cohort_class='sma'`, ~$25M) are STACKED in firm view — closing the post-5/18 ~$25M stacked-total gap. This is model-stack space and matches the data to the dollar.
- **Do NOT fold `sma_aua` into the non_model band** (the literal "add 1c back into non_model" phrasing): it would numerically close the stacked total but **mis-attribute SMA as non-model** (it is `cohort_class='sma'`), and it adds nothing pre-5/18 (sma null there). The Non-Model band already reads `non_model_aua` correctly ("FIT" in the merged matrix).
- The **5/18 methodology seam** (the ~$172M non_model re-level) is a separate, documented item. If a visible step at 5/18 is undesirable in the trend, that is a **DS-methodology / CTO** decision, not an FE rollup fix.

## Recommendations (routed)
- **RD~B:** implement F5 (per-firm key-set trend iteration incl. SMA sleeves), not a non_model fold. SMA sleeves render from 5/18 (when the live breakout begins) — acceptable given the null-gap.
- **DS~B (CC):** reconcile meta-narrative ("1c non-additive sub-slice of 1b") vs serving by_model (SMA = additive `cohort_class='sma'`); confirm the pre-5/18 sma null-gap (4/28-5/15) is intended (live region not broken out) vs a backfill miss.
- **COO/CTO:** the "total unchanged across 5/18" premise holds for the GLOBAL headline (~-$62M, normal) but NOT for per-firm component bands; any continuous trend will show the documented seam.

## Finding 5 — source-partition corroboration (definitive: per-date `methodology_version` flip)
The rollup `build_aggregate_aua_timeseries.py` is a pure pass-through bundler — it copies `model_aua`/`sma_aua`/`non_model_aua`/`by_model`/`cohort_class` straight from each per-date partition `platinum/mdpf/aggregate_aua/{date}.json` and captures each partition's `methodology_version`. Reading the source partitions directly settles the data-model at the producer:

| field | 5/14, 5/15 (pre) | 5/18, 5/19 (post) |
|---|---|---|
| `methodology_version` | `v0_8_ruling2` | `v0_9_1` |
| `meta.backfill_method` | `process_derived_v0_8_rulingII_20260520_MDPF_ASSETS_016` | `null` (live) |
| `sma_aua` | `None` | $24.9M |
| `by_model` | 5 (`cohort_class='model'`) | 7 (5 model + 2 `cohort_class='sma'`: `opal_div_sma` $19.76M, `opal_growth_sma` $5.15M) |
| `headline_formula` | "1a+1b+2a; **1c (SMA) is a non-additive sub-slice of 1b**" | "**1a+1b+1c+2a** = partner_aua_subtotal - cohort_2b_audit" |
| 49f `non_model_aua` | 455.5M (SMA-inclusive) | 283.5M (SMA-exclusive) |
| `cohort_2b_audit` | 203.8M | 106.1M |

The tag flips **exactly at 5/18**. So the 49f `-$172M` non_model step decomposes precisely: **-$25M** SMA breaks out of the 1b residual into additive 1c (the reclassification) **+ -$147M** the v0.9 basis re-levels the 1b residual itself (the source change). The `headline_formula` itself changes (1c moves from non-additive-sub-slice to additive term), which is why the rollup-level `meta.cohort0_historical_backfill` narrative (still the v0.8 wording) is stale against the v0.9 partitions.

## Reconciliation (with DS~B 0.4.0_DS_ClientPlatform~B) + final dispositions
DS~B independently confirmed both flags on live 5/29 data and corrected its earlier consolidated scope:
- **ITEM #1 (additive vs narrative):** CONFIRMED — `model_aua + sma_aua = Σ(by_model)` to the dollar; SMA sleeves are `cohort_class='sma'`; `non_model` excludes them. The meta "1c = non-additive sub-slice of 1b" is **stale v0.8 framing**. **DS-lane fix:** DS~B updates the producer meta narrative to the additive `cohort_class='sma'` reality (or scopes it to the pre-v0.9 region). [DS~B owns — producer script is DS lane.]
- **ITEM #2 (pre-5/18 history):** classified — pre-Mar-10 history is the **bandaid estimate** (`build_mdpf_v0_bandaid_backfill.py`: weekly-interp, synthetic accounts, self-labeled "no production source historically"); Mar-11..May-15 null = bandaid-coverage-vs-live-cutover seam, not recoverable real data. Fine for the FE (sleeves render from 5/18). Exact real historical 1c is unavailable (estimate only).
- **FE fix:** **Andrew-direct = fold** (displayed non_model = `non_model + sma`). Validated by the data (no double-count; keeps SMA in non_model both sides of the seam). DS~B withdrew its non_model-fold-of-residual rec and the F5-stack alternative is moot — Andrew's word governs. RD~B proceeding.
- **The `-$172M` seam:** CONFIRMED as the real backend item — a **Black-Diamond (pre-5/18) -> Schwab (post)** source change (Andrew-direct canonical = `Schwab - SmartX-model - SmartX-SMA`). Routed to DS~B (`mdpf_aggregate_aua.py` owner) for backend re-derivation. **DE serving-side support offered:** re-run this continuity verify on the re-derived artifacts to confirm the seam closes. This is a DS-methodology item, distinct from the 1c display.

**Net agreed scope:** NO 1c backfill (the fold handles live sleeves; historical real 1c unavailable). Meta-narrative reconcile = clean DS fix. v0.8->v0.9 (Black-Diamond->Schwab) seam = separate DS backend re-derivation.

## Compiler Tools
- N/A this cycle — task was a read-only serving-data correctness probe against live S3 JSON + source partitions (no gold-script edit, no portal-component change, no fetch/endpoint change). Decomposition reconciled directly from the artifact arrays + source partitions (`model_aua`/`sma_aua`/`non_model_aua`/`by_model`/`methodology_version` to-the-dollar). comp-* tools apply when RD's fold lands a portal-component change (then `comp-transform schema-check ModelPortfolios`).
