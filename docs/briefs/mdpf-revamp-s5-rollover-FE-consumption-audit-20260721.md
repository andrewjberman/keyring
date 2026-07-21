# MDPF_REVAMP.S5-ROLLOVER — FE-Consumption Audit (Deliverable §5)

**Author:** 0.4.0_DE_ClientPlatform · **Date:** 2026-07-21 · **TO:** MDPF_REVAMP.S5-ROLLOVER · **Gate:** 1.0.0_SA_CTO · **Tandem:** 0.7.0_AE_CloudOps (cutover mechanics)
**Frame (Andrew-direct, CTO-confirmed):** models-only by design; data-side is CORRECT; roll-over is **frontend alignment** to the revamp schema; ETFs future; numbers-changing vs the old page is EXPECTED + FINE.
**Fills §5 of** `docs/briefs/mdpf-revamp-s5-rollover-compare-20260721.md` (AE seed doc).

---

## 0. HEADLINE (grounded, verify-not-assume)

**The FE already consumes the revamp's flat, model-focused schema for ALL 7 keys. Required FE code changes: ZERO.** The roll-over is a **CONTENT/serving cutover** (AE's lane), not a frontend rewrite. The brief's premise — "the FE currently reads the LEGACY nested shape (aggregate.*/partners/etf_decomposition)" — is **grounded on dead code** and does not hold: the function that reads the nested shape has **zero call sites**.

Three grounding corrections to the seed doc's starting pointers (AE explicitly asked me to verify, not trust):

1. **The nested global function is uncalled.** `getMdpfAggregateAUATimeSeries()` (portal-proxy.ts:485 → `/api/general/mdpf/aggregate-aua-timeseries.json` → `s3://opal-data-portal-v2/json/mdpf/aggregate-aua-timeseries.json`, **443,868 B**, nested `aggregate`/`partners`/`etf_decomposition`/`methodology_version`) has **0 call sites** across `portal/src`. Its interface `MdpfGlobalTimeSeries`/`MdpfAggregateAUATimeSeries` is **vestigial dead code**.
2. **The FE's real global read is the FLAT slice.** ModelPortfolios fetches the global via `getMdpfAggregateAUATimeSeriesByFirm('global')` (ModelPortfolios.tsx:378, typed `MdpfPerFirmTimeSeries` = flat) → `/api/general/mdpf/global/aggregate-aua-timeseries.json` → `s3://opal-data-portal-v2/json/mdpf/global/aggregate-aua-timeseries.json` (**161,772 B**, FLAT). **This served flat global slice is field-identical to the revamp global.**
3. **`rawTimeSeriesData.aggregate` (ModelPortfolios.tsx:428/480/633) is NOT the mdpf json.** It is the separate legacy SmartX source `getAUMTimeSeries` (array-of-`{period,aum,account_count}` records). It is already the FALLBACK — `globalMdpfData` is primary (L611). Out of scope for this mdpf roll-over.

**Sole FE consumer of all 7 keys: `portal/src/pages/ModelPortfolios.tsx`.** No other page (ADVI et al.) reads any of them.

---

## 1. Per-key audit (all 7 served keys)

Served keys read by the FE today, the exact fields accessed, and the revamp schema match (all schemas pulled live 2026-07-21 from `opal-data-portal-v2` [served] and `opal-data-assets` [revamp] and diffed field-by-field).

| # | Served key (FE reads) | FE consumer / queryFn | Fields the FE actually reads | Revamp schema (gold/mdpf_revamp/) | FE change |
|---|---|---|---|---|---|
| 1 | `json/mdpf/global/aggregate-aua-timeseries.json` (161,772B, FLAT) | `globalMdpfData` = `getMdpfAggregateAUATimeSeriesByFirm('global')` | `as_of_last`; `dates`; `by_model.{cohort_class,display_name,model_value[],account_count[]}`; `opal_aggregate_aua[]`; `model_aua[]` | `global/aggregate_aua_timeseries.json` (165,635B) — **key set IDENTICAL** (served-only=∅, revamp-only=∅) | **NONE** |
| 2 | `json/mdpf/49financial/aggregate-aua-timeseries.json` (156,730B) | `perFirmMdpfData` = `...ByFirm(firmId)` | `dates`; `partner_custody_total[]`; `non_model_aua[]`; `by_model.{cohort_class,display_name,model_value[],account_count[]}`; `as_of_last` | `49financial/aggregate_aua_timeseries.json` (152,920B) — **key set IDENTICAL** | **NONE** |
| 3 | `json/mdpf/inflection/aggregate-aua-timeseries.json` (122,801B) | `perFirmMdpfData` (same as #2) | same as #2 | `inflection/aggregate_aua_timeseries.json` — **key set IDENTICAL** (verified directly, not extrapolated) | **NONE** |
| 4 | `json/mdpf/49financial/account-distribution.json` | `perFirmDistribution` = `getAccountDistributionByFirm('49financial')` | `total.account_count`; `by_model.{...DistributionStats}`; `generated_at`; histogram/percentiles | `49financial/account_distribution.json` — **+ additive `basis` key** (served-only=∅) | **NONE** (`basis` not in `AccountDistribution` type → ignored) |
| 5 | `json/mdpf/inflection/account-distribution.json` | `perFirmDistribution` | same as #4 | `inflection/account_distribution.json` — **+ additive `basis` key** | **NONE** (ignored) |
| 6 | `json/portfolios/account-distribution.json` (7,708B) | `distributionData` = `getAccountDistribution()` | `total.{account_count,...}`; `by_model`; `generated_at`; `period` | `global/account_distribution.json` (6,962B) — **key set IDENTICAL** | **NONE** |
| 7 | `json/portfolios/non_model_assets.json` (114,616B) | `nonModelData` = `getNonModelAssets()` | `latest.non_model_aum`; `time_series[].{period,enterprise_total,model_aum,non_model_aum,non_model_pct}` | `global/non_model_assets.json` (82,101B) — **key set IDENTICAL** (`latest`+`time_series`+`generated_at`+`meta`) | **NONE** |

**The ONLY schema delta across all 7 keys** is the additive `basis` key on the two per-firm account-distributions (#4/#5). The FE's `AccountDistribution` interface (portal-proxy.ts) has no `basis` field; extra JSON keys are inert. **FE-neutral.**

Non-schema differences (all FE-neutral): date depth (revamp uses a trading-day calendar and is more recent — 427/433 vs 429/455 rows), and the internals of `meta` and `source_vintage_last` (revamp carries `trading_days_behind`/`slice`/`named_deltas`; served carries `age_hours_at_generation`/`backfill_methods`). **No FE component reads `meta`, `source_vintage_last`, or `methodology_version`** (portal-wide grep: only `import.meta.env` matches). So those differences never reach a render.

---

## 2. Deliver-(2): the exact FE changes

**None are required to consume the revamp.** Every field, every by_model sub-key, every per-firm and non-model field the FE reads exists in the revamp with identical shape. Confirmed by tracing every read site in ModelPortfolios.tsx:
- Global trend/bars/count: L479, L611-627, L646-655, L917-927 → `as_of_last, dates, by_model.*, opal_aggregate_aua, model_aua`.
- Per-firm: L479, L501-512, L573-598, L759-760, L841, L898-905, L1209 → `dates, partner_custody_total, non_model_aua, by_model.*`.
- Distributions: L433-436, L860, L870-877, L1292 → `total, by_model, generated_at, period`.
- Non-model: L438-441, L762-763, L846-851 → `latest.non_model_aum, time_series`.

**Optional (not required for cutover) cleanup, separately gated:** delete the vestigial nested path — `getMdpfAggregateAUATimeSeries()` (aum.ts:449, portal-proxy.ts:485) + the `MdpfAggregateAUATimeSeries`/`MdpfGlobalTimeSeries`/`MdpfPartnerSeries`/`MdpfEtfSeries` interfaces. This removes the only FE code that references `partners`/`etf_decomposition`/`methodology_version`. **Precondition:** confirm no NON-FE consumer reads `json/mdpf/aggregate-aua-timeseries.json` (the 443KB nested artifact) before it stops being maintained — that's a backend/AE check, not an FE one. I recommend deferring this cleanup to a follow-up so it does not gate the cutover.

---

## 3. Deliver-(3): is any legacy-only field load-bearing for a MODELS view?

**NO.** `partners`, `etf_decomposition`, `methodology_version`, and the nested `aggregate.*` object exist **only** in the vestigial 443KB nested artifact, read **only** by the uncalled `getMdpfAggregateAUATimeSeries()`. No component, transform, or queryFn reads any of them for the models view or any other view. They are safe to shed (which the revamp already does, by design). **No surface to escalate on this item.**

---

## 4. CTO's SMA-sleeve nuance (msg 184412Z) — RESOLVED

**Q: does any component/transform READ the by_model SMA-sleeve entries?**

**A: NO — no component reads their VALUES.** The revamp global `by_model` has 9 entries: 5 core (`cohort_class='model'`), **2 SMA sleeves** (`cohort_class='sma'`: `opal_growth_sma`, `opal_div_sma`), 2 blends (`cohort_class='model'`). (The **served** flat global has the identical 9 — the SMA listing is not revamp-introduced. Inflection has **no** SMA sleeves at all: 7 entries, all `model`.)

Every FE iteration of the aggregate `by_model` **filters `cohort_class==='sma'` OUT** — 4 sites: ModelPortfolios.tsx **L505** (donut/legend set), **L586** (per-firm trend), **L613** (global trend + bars), **L648** (global union count). The FE reads the SMA entries' `cohort_class` field *only to exclude them*; their `model_value`/`account_count` are never summed, plotted, or rendered. Their AUA is already folded into `non_model_aua` at the producer (YANG_SITTW.TO-1, comments L838/L893).

**Per CTO's tree → the "NO" branch: dropping the 2 SMA sleeves is data-neutral and FE-safe** (the filters become no-ops; totals unchanged; no slice/line/legend/count ever existed for them). The FE renders identically whether the sleeves are present-and-filtered or absent — so this is fully consistent with the "no producer changes / FE-alignment" frame: **the FE is already aligned regardless.**

**One caveat to protect against a mis-read of "5-core-only":** the 2 **blends** (`opal_blend_5050_int_ltc`, `opal_blend_5050_st_int`) are `cohort_class='model'` and **ARE load-bearing** — they are rolled into their archetype models via `rollBlendsIntoArchetypeSeries` / `BLEND_ARCHETYPES` (L677-683). "5-core-only" must mean **drop `cohort_class='sma'` (2 entries); KEEP all `cohort_class='model'` (incl. the 2 blends)**. Dropping blends would break the Inflection global rollup.

---

## 5. AE's Option-1-vs-2 decider (msg 182856Z) — ANSWER: URLs STAY → Option 2

**The FE fetch URLs do NOT change.** The FE already fetches the exact served keys the publisher would target, and the revamp schema is field-identical. So the lower-blast path is **Option 2 (content-swap into the existing portal-v2 served keys, same `/api/general/*` URLs, zero FE change, no L@E/router change; rollback = version-restore those keys)** — strictly lower blast than Option 1 (origin repoint), which changes nothing observable but adds router surface.

**Publisher serving-target mapping (revamp gold key → served key the FE reads), for AE's publisher (`opal-assets-mdpf-portal-publisher`):**

| Revamp gold key (opal-data-assets) | → Served key (opal-data-portal-v2, FE URL) |
|---|---|
| `gold/mdpf_revamp/global/aggregate_aua_timeseries.json` | `json/mdpf/global/aggregate-aua-timeseries.json` |
| `gold/mdpf_revamp/49financial/aggregate_aua_timeseries.json` | `json/mdpf/49financial/aggregate-aua-timeseries.json` |
| `gold/mdpf_revamp/inflection/aggregate_aua_timeseries.json` | `json/mdpf/inflection/aggregate-aua-timeseries.json` |
| `gold/mdpf_revamp/global/account_distribution.json` | `json/portfolios/account-distribution.json` |
| `gold/mdpf_revamp/49financial/account_distribution.json` | `json/mdpf/49financial/account-distribution.json` |
| `gold/mdpf_revamp/inflection/account_distribution.json` | `json/mdpf/inflection/account-distribution.json` |
| `gold/mdpf_revamp/global/non_model_assets.json` | `json/portfolios/non_model_assets.json` |

**Note the filename convention flip:** revamp uses `aggregate_aua_timeseries.json` (underscore); served uses `aggregate-aua-timeseries.json` (hyphen). The publisher must map names, not just prefixes. The nested `json/mdpf/aggregate-aua-timeseries.json` (443KB) is **not** in this map — the FE does not read it; leave it frozen (see §2 precondition before any removal).

---

## 6. Render-check criterion note (NOT a surface / NOT a blocker): the cutover changes VALUES, not only shape

**The value change is SETTLED-FINE** (Andrew via CTO 184412Z + 185126Z: models-only numbers-changing "is EXPECTED + FINE," "that does not matter"). I am **not** surfacing it for a ruling and **not** challenging data-parity — data-side is Andrew-co-signed correct and out of my lane. This is purely a heads-up so the render-check gate uses the right criterion.

For the record (measured on the 407 common dates): revamp differs from legacy-served — `opal_aggregate_aua` ~0.03–6.7% (median 2.4%), `non_model_aua` ~0.08–27.6% (median 8.4%), `model_aua` nearly ties on the newest dates but diverges historically. The `opal_aggregate_aua − (model_aua + non_model_aua)` offset is **byte-identical (−64,602,681.60)** in both on 2026-07-17 → consistent underlying structure; the divergence is the intended **models-only scope redefinition**.

**Consequence for the gate:** the mandatory `/frontend-dev` render-check criterion must be **"ModelPortfolios renders the revamp (correct) values cleanly,"** NOT "matches the legacy page pixel-for-pixel." Flagging only so the intended value shift is not mistaken for a render regression during the check.

---

## 7. Residuals / open items

- **[AE]** confirm no NON-FE consumer of the 443KB nested `json/mdpf/aggregate-aua-timeseries.json` before it stops being maintained (gates the optional §2 cleanup, not the cutover).
- **[DE+AE]** pair on the `/frontend-dev` render-check against the revamp artifacts (Global + 49F + Inflection views), with the §6 value-shift criterion.
- **[CTO]** ratify the SMA §4 disposition (FE-neutral either way; blends must be retained) + the Option-2 §5 serving-target map.
- Date-depth: revamp is a trading-day calendar (fewer rows) and more recent (as_of 07-20 vs 07-18). FE-neutral (FE keys off `dates[]` + `as_of_last`), noted for the render-check x-axis sanity.

---

## 8. Render-check verdict (route-injection vs revamp content, pre-serving)

Ran the `/frontend-dev` headless harness (ModelPortfolios `/portfolios`) with Playwright route-injection fulfilling all 7 mdpf URLs with the live revamp artifacts (+ real `aum-metrics.json`/`aum-timeseries.json` from portal-v2 to clear the loading gate). This proves the revamp content renders BEFORE any serving change, independent of the Option-A mechanism. Screenshots in the session scratchpad (`render_global.png`, `render_49f.png`, `render_inflection.png`).

| View | Verdict | Evidence |
|---|---|---|
| **Global (All)** | **PASS** | Donut Total AUA $1.81B, quarterly cards, bell curve (7,729 holdings), Daily AUA trend full-depth to **2026-07-20 (revamp `as_of_last`)** — no blank/crash; 5 core models + Non-Model AUA (SMA correctly filtered); all dark panels, **no silver-canvas color-law violation**; as-of stamps read "July 20th, 2026" confirming revamp drove the render. |
| **49 Financial** | **PASS** | Firm-select drove `perFirmMdpfData` (revamp #2/#4); Total AUM $1.68B, bell curve 7,016, Daily AUM trend smooth full-depth to 2026-07-20; SMA filtered; color-law clean. |
| **Inflection** | **RENDERS — one data caveat (NOT FE, NOT color-law)** | Donut $202M, bell curve 713, Orion sourcing, 2026-07-20 vintage all clean. BUT the **Daily AUM chart shows a picket-fence** (sparse spikes + gaps) in the post-onset region. |

**The Inflection picket-fence — grounded, and it is a DATA characteristic, not an FE defect:**
- The FE renders Global + 49F smoothly with **identical code**; the FE's uniform `?? 0` null-handling faithfully drops the stack to zero on any null date.
- **Served** inflection (what the FE renders TODAY): model onset 2026-05-18, **zero post-onset nulls** → smooth.
- **Revamp** inflection: onset 2026-05-15 (earlier), but **6 post-onset None gaps** (2026-05-21, 06-01, 07-01, 07-13/14/15) + 16 interspersed zeros in the last 60 trading days → the picket-fence. The pre-05-15 all-Non-Model region is the known/named model-onset asymmetry (expected).
- **So the cutover would visibly degrade the Inflection daily chart** (smooth today → gappy on revamp), driven entirely by post-onset gaps in the revamp inflection `by_model.model_value`.

**SURFACE (DS/CTO ruling, not mine):** is the revamp-inflection post-onset model_value gappiness (likely the in-flight Eclipse/DS finalization) EXPECTED/acceptable-for-cutover, or a data gap DS closes before the push? Two dispositions:
1. **Data fix (preferred if gaps are unintended):** DS fills the post-onset inflection model_value gaps → chart renders smooth, no FE change. (In-lane with "data-side is being finalized.")
2. **FE null-carry-forward (only if the gaps are EXPECTED-but-should-render-smooth):** a small, in-scope FE-alignment change to carry-forward the last non-null per series instead of `?? 0`-dropping. I can make this if CTO/Andrew rules the gaps are real-and-permanent. NOT defaulting to it — a carry-forward would MASK a real data gap, so it's only correct if the gap is deliberate.

**GATE STATUS:** Global + 49F **PASS** the pre-serving render-check. **Inflection HELD** on the DS/CTO data-gap ruling above (the FE + color-law are clean; the hold is purely the inflection data). No FE code change is required for any view to consume the revamp schema (§0-§7 stand); the Inflection item is a data-finalization question surfaced by the visual gate.
