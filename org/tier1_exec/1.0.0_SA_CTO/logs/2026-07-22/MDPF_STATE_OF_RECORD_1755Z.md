# MDPF — STATE OF RECORD, 2026-07-22 1755Z

**archetype:** SCRIBE
**Author:** `1.0.0_SA_CTO` | **Purpose:** a clean, restart-safe statement of where MDPF stands, backend and
frontend. **Every line below is a measurement taken at 1755Z, not a recollection.**

**READ THIS FIRST:** this document contains **no process history** — no sequence of who found what, no
corrections, no superseded positions. **It is the state, not the story.** Prior planning documents
(`MDPF_EXECUTION_PLAN_20260722.md`, `MDPF_CONSOLIDATED_PLAN_20260722.md`) contain rulings that remain valid;
they also contain narrative. **If the two disagree, re-measure — do not adjudicate between them.**

---

## 1. SERVED SURFACE — unchanged all session

| | value |
|---|---|
| CloudFront `EVTSA9VEHNZVH` | **24 behaviors / 7 origins** |
| `mdpf` or `portfolios` behaviors live | **0** |
| serving source | legacy `opal-data-portal-v2` via the `/api/general/*` catch-all |

**Nothing from the revamp has ever been served. No deploy is half-landed. Both deploy ledgers from this
session's earlier work are closed.**

> **⛔ STANDING HAZARD: `infra/aws/terraform/portal-auth/` DECLARES 9 mdpf/portfolios behaviors + an assets
> origin + an OAC THAT ARE NOT LIVE.** An **untargeted `terraform apply` in that root serves the revamp with
> no co-sign.** The divergence is deliberate. **Any apply in that root is `-target`ed and named. A drift
> report on this root is EXPECTED and is not an action item.**

---

## 2. BACKEND — DATA STATE

### 2.1 Staged artifacts (`s3://opal-data-assets/gold/mdpf_revamp/`)
10 objects. **Staged only — not published, not served. The publisher is OFF.**

| object | ETag | note |
|---|---|---|
| `inflection/aggregate_aua_timeseries.json` | `5e7b684d` | rebuilt 12:54Z |
| `global/aggregate_aua_timeseries.json` | `08f9720e` | rebuilt 12:54Z |
| `portfolios/aum-timeseries.json` | `ca0c6d1c` | rebuilt 13:04Z |
| `49financial/aggregate_aua_timeseries.json` | `aa5c5b85` | |
| `portfolios/aum-metrics.json` | `529b7c21` | |
| `global/non_model_assets.json` | `8a195549` | |
| `49financial/account_distribution.json` | `865919f2` | |
| `inflection/account_distribution.json` | `afb964c4` | |
| `global/account_distribution.json` | `b946d836` | |
| `global/non_model_assets_precutover_frozen.json` | `da2260f6` | reference, not in the publish map |

**Co-sign status: 0 of 3.** No pin is taken. **These ETags are a checkpoint, not a pin** — folding Cottonwood
rewrites `global/aggregate_aua_timeseries.json` again.

### 2.2 Inflection
- **2026-07-06 is CORRECT on both axes** in the staged artifact: value `122,866,034`, count `474`. The
  previously-served figure (`136,859,722 / 540`) was 07-10's snapshot carried on 07-06.
- **07-09 and 07-10 are present** (value + count).
- **07-13, 07-14, 07-15 are absent** in both source feeds.
- **07-01 is absent** in eclipse.
- **Root cause of the whole class:** the LEGACY served date axis is not a trading-day axis — it carries
  points on market-closed days and omits real trading days. The revamp axis is trading-day clean.

### 2.3 49 Financial
- **427 dates, 2024-11-01 → 2026-07-20, ZERO nulls, no monthly gaps.** 2 day-over-day moves ≥5% in 426
  transitions.
- **Sources:** model AUA from **SmartX** `fact_model_aum_daily`; custody from **Schwab RPS** `fact_rps_s2`.
- **Frontier values: model `$1,401,200,883` · custody `$1,675,868,804`.** **This is the SCHWAB-RPS basis, not
  the 0824 blended-preferred basis (~$1.62B model).** **Two quantities, not a shortfall. Which basis the page
  should carry is an open business decision.**
- **49F's count axis is imported from the legacy served artifact.** No per-date 49F account-count source
  exists. **One measured disagreement (2026-07-17, −10 accounts); mechanism undetermined. No rate is
  quotable from n=2.**

### 2.4 Cottonwood
- **Ingestion: live and firing unattended.** Integrity gates pass.
- **Gold `dim_model_portfolio` EXISTS** — partitions `date=2026-07-21`, `date=2026-07-22`.
- **It is on the ARCHETYPAL basis. No "Satellite" name appears in gold. Nothing nulls** — 0 of 9 rows have
  zero/null value; 4 of 447 accounts lack a value.

| model | is_opal | accounts | value |
|---|---|---|---|
| Opal Intermediate-Term | ✓ | 223 | $74,760,166.55 |
| Opal Conservative Growth | ✓ | 96 | $30,991,060.30 |
| Opal Short-Term | ✓ | 104 | $16,246,582.01 |
| Opal Ultra Short-Term Income | ✓ | 7 | $1,259,943.23 |
| Opal - Income | ✓ | 2 | $1,242,005.29 |
| Opal Long-Term Aggressive | ✓ | 12 | $1,118,257.64 |
| Sleeve - Equity / Tax-Free Bond / Core Money Market | ✗ | 1 each | $763,213.84 total |

**Opal subtotal: 444 accounts / $125,618,015.02.** Decomposition conserves: 296 accounts' own holdings sum
`$126,381,228.84` vs dim sum `$126,381,228.86` — **$0.02, per-row rounding.**
- **Model-assignment history is TWO DAYS (07-21, 07-22).** The Rebalancer endpoint we consume returns
  live state. **Holdings reach back to 2026-06-08; allocations to 04-22; transactions to 03-09.** *Value
  history extends further back than assignment history.*
- **>> WHY THE HISTORY IS SHORT — Andrew-direct, and it is NOT a platform limitation: <<**
  > ***"Cottonwood does not have full lookback yet because they are in the process of migrating their data
  > to Black Diamond, so I would not get too indebted to what they have or don't have yet. Our goal is just
  > to get whatever we have access to cleanly and explainably."***
  **COTTONWOOD IS MID-MIGRATION INTO BLACK DIAMOND.** The absent history is **neither a BD platform limit
  nor a Cottonwood data defect — it is a migration in progress, and more history is expected to arrive on
  its own.** **Do not treat any current depth as a ceiling and do not build against one.**
  > ### ⛔ BINDING DESIGN CONSTRAINT
  > **Whatever we build must be ADDITIVE AND NON-CONFLICTING WITH DATA THAT ARRIVES LATER. No synthesized
  > rows. No frozen backfill. NO HARDCODED SERIES START. The series must extend backwards ON ITS OWN as the
  > migration lands more history.**
  > **Anything that writes a value where real data will later appear is a future contradiction we authored
  > ourselves** — and it would have to be reconciled against ground truth that is still arriving.
  **Consequence: the goal is not to reconstruct history. It is to read what is actually there, correctly,
  and let it grow.**
- **The MDPF runner CANNOT currently read `blackdiamond/cottonwood/silver/*`** — the grant enumerates five
  ARNs and Cottonwood is not among them. A two-statement additive fix is in flight.

### 2.5 July source coverage — 15 expected trading days
| feed | missing |
|---|---|
| `eclipse fact_portfolios_full` | **07-01, 07-13, 07-14, 07-15** (+07-22 pending) |
| `orion fact_assets` | **07-13, 07-14, 07-15** |
| `schwab 0824 fact_rps_s2` | 07-22 only |
| `cottonwood fact_holdings` | 07-21, 07-22 |
| `cottonwood fact_model_assignment` | all but 07-21, 07-22 |
| `smartx fact_model_aum_daily` | **none** — run-date partitioned, full history inside each partition |

### 2.6 Orion backfill — **SOURCE REPAIRED, NOT YET PROPAGATED** *(verified independently 1810Z)*
`s3://opal-data-inf/bronze/assets/` — raw `.jsonl.gz` present for all five gap dates, **as-of rosters**:

| date | bytes | roster | rows | MV |
|---|---|---|---|---|
| 07-11 | 2,176,938 | 318 | 34,935 | $202,843,646 |
| 07-12 | 2,175,913 | 318 | 34,935 | $202,843,646 |
| 07-13 | 2,172,954 | 318 | 34,935 | $201,601,607 |
| 07-14 | 2,176,843 | 319 | 34,942 | $202,375,855 |
| 07-15 | 2,180,491 | 319 | 34,942 | $202,880,787 |

*(Positive control 07-16 = 2,166,565 bytes present; negative control 07-99 = 0.)*
**FAITHFULNESS PROVEN, not asserted:** 07-15 vs the SAME-DAY 07-16 capture — **client sets byte-identical**
(319 = 319, empty both ways), **309 of 319 clients identical row counts**, and the entire +103 row delta
localises to **10 named clients**. That is real position movement between two trading days, **not a
methodology difference. The backfill is methodologically equivalent to a same-day capture.**
**17a intact** — raw `.jsonl.gz` only; pre-existing `.parquet` untouched and never used as a source.
**Never-overwrite intact.** **A backfill must pin the household roster PER-DATE — using the current roster
yields correct prices on the wrong book.**

> **⚠ NOT PROPAGATED. DO NOT READ A SILVER LISTING AS THE VERDICT.** Monolith bronze and silver for 07-13 are
> both **ABSENT** (control: silver 07-16 present). The mirror is **POLLING**, and today's pass ran before
> these landings. **Propagation is the next scheduled pass. Orion SOURCE is repaired; the SERVED artifact is
> not.** Nothing is to be hand-fired — validate on the scheduled artifacts.

### 2.7 Eclipse — census exists; recoverability NOT settled here
A full sweep of **848/848 portfolios, zero failures** (span 05-01..07-22) quantifies what each gap date would
carry — **portfolios changed: 06-01 → 0 · 07-01 → 2 · 07-13 → 14 · 07-14 → 1 · 07-15 → 7.**
**Eclipse recoverability is under active investigation and is deliberately NOT concluded in this document.**
**Standing prohibition regardless of outcome: the eclipse puller's `--date` is a FILENAME, not a query — it
fetches CURRENT state and files it under the requested date. It must not be used for backfill.**

---

## 3. FRONTEND — STATE

**Portal main tree: `DEV` @ `08c6d8b2`. DEV is 8 commits ahead of `origin/PROD`. Nothing promoted.**

**LANDED on DEV:**
- Absent-vs-zero fix on the MDPF page (the `Total AUM $0` beside a populated donut).
- Removal of a false *"values rolled forward from last known data"* methodology claim for a firm with no
  history.
- Source attribution resolves correctly to Black Diamond Rebalancer for Cottonwood.
- Global monthly-axis label fix (already shipped to PROD separately as `v2.1.141`).

**OPEN, confirmed by rendering the page and reading the image — not by type-check:**
1. **Both trend charts render COMPLETELY BLANK for a Cottonwood advisor** while the legend names the models
   and the donut draws them at full value. Cause: the chart's series list is a **closed literal**; the legend
   and donut are data-driven. A model outside that literal is computed, stored, and then dropped because no
   series was ever mounted. **Every guard on that page was built for a VALUE being absent; none for a SERIES
   being absent.**
2. **Two Cottonwood models collapse to the SAME COLOUR** in donut and legend — visually indistinguishable.
3. **`Total AUM` and `Total AUA` appear side by side in one panel** — firm-wide, live for 49F and Inflection
   today, not Cottonwood-specific.

**Day-one Cottonwood renders as 1–2 points at the right edge of a 21-month chart** — its assignment history
starts 07-21 and the existing series ends 07-20, so **there is zero date overlap.**

---

## 4. DECISIONS ALREADY MADE (Andrew, this session — these are settled)

1. **One flip.** Cottonwood is inside the finalization gate; everything ships together.
2. **`cottonwood_opal_conservative_growth` MERGES to `opal_long_term_conservative`.** No new key.
3. **`Opal - Income` is NON-MODEL.** No canonical key, no crosswalk entry; it does not become a row.
4. **Satellites get no label. Label PRIMARY KEYS ONLY.** The labelled key space is the archetypal ladder;
   partner strategies decompose into it and get no row of their own.
5. **Gates and hooks are in scope during consolidation; ALERTS (SES/SNS/CloudWatch) are not.**
6. **"Not yet tracked"** is the absent-value token. Hiding the tile is refused.
7. **July completeness per channel is Step 1**, and precedes the rest.

---

## 5. OPEN DECISIONS — none of these is an engineering call

| # | decision |
|---|---|
| 1 | **Which 49F basis the page carries** — Schwab-RPS (~$1.40B) or 0824 blended-preferred (~$1.62B). |
| 2 | **Disposition of permanently-absent Inflection dates**, if recovery is confirmed impossible. |
| 3 | **Whether Cottonwood ships at its current depth.** *(Reframed: it is not "ship now vs wait for lookback" — the migration will deepen it on its own. The question is whether the current depth is presentable, given the series must be built to extend backwards without rework.)* |
| 4 | **Whether the 49F count axis ships as-is** — it has one measured defect, no source to fix it, and no assurance instrument. |

---

## 6. KNOWN DEFECTS NOT YET FIXED

| where | defect |
|---|---|
| publisher | `PUBLISH_MAP` is a hardcoded 9-entry dict with **no Cottonwood entry**. At cutover it reports `9/9, all_present=True` **and Cottonwood is never served.** |
| freshness gate | the partner set is a **one-element dict**; Cottonwood's staleness is never evaluated, so **its feeders are never skipped when stale** and the anti-fabrication guard does not reach it. |
| global composition | **six fold sites**; four would null **every pre-2026-07-21 row** if a firm with no history is added naively — **and it would render as honest nulls, not as an error.** |
| producer | orchestration is **fixed at two firms** (arg choices, want set, 2-arg compose, report loop). Helpers and gates are already N-firm generic. |
| audit wiring | built and **reverted**; preserved as a patch. Re-applies with the completion-marker fold gating on **coverage numbers, not exit code** — an empty artifact currently returns success. |
| 49F count | imported from the legacy artifact; **no source exists to decouple it.** |
| FE | the three items in §3. |

## Compiler Tools
| tool | result |
|---|---|
| `aws cloudfront get-distribution-config` | applied-truth serve state (24/7, 0 mdpf behaviors) |
| `aws s3api list-objects-v2` | staged ETags + per-date source coverage across 5 feeds |
| `git -C portal` | FE branch/ahead-count |
**Why these:** the question is *what is true right now* across CF, S3 and two git trees; no single comp-tool
spans those three. Rail markers carried on each raw call.

## Next
Restart-safe. **No agent needs this session's history to act on the above.**
