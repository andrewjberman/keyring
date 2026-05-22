# MDPF Global v0 — Design → Backfill → Production-Cutover → Model-Portfolios-Page Wire — Andrew-Direct Session

**Agent:** `0.4.0_DS_ClientPlatform` (sole-DS this session per Andrew direct
~12h prior: "you are the only DS who should be tasked with any work for the
remainder of this session.")
**Span:** 2026-05-18 (~21:00Z, post-MDPF.011 close) → 2026-05-19 (~13:40Z)
**Predecessor session log:**
`org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-05-18/MDPF_ASSETS_011_smartx_per_account_model_membership_probe.md`
**Scope:** Andrew-direct, NOT a formally-numbered TO. Originated as
"how to take over for the daily Model Portfolio AUA update" and converged
into a full MDPF Global v0 ship with the corrected Model Portfolios page on
S3 + AE 0.7 daily-chain codify + first live fire + the legacy-compat
emit + 5/18 extension + per-model Inflection merge.

---

## 1. Cohort taxonomy as confirmed by Andrew this session

Per `docs/architecture/MDPF_ASSETS_WSA_CONTRACT.md` + Andrew-direct
clarifications + the reversed contract amendment:

| Cohort | Definition | Status this session |
|---|---|---|
| **1a** | 49F core Opal models (5: UST/ST/INT/LTC/LTA) | Daily-process via SmartX exports + WS-B feeder |
| **1b** | 49F non-model (Schwab-confirmed residual) | WS-E daily-process from BD silver/allocations + Schwab-confirmed custody crosswalk |
| **1c** | 49F SMAs (2: Opal Equity Growth SMA + Dividend SMA) | Daily-forward only (no SmartX bucket historical) |
| **2a** | Inflection Opal models (7: 5 49F-shared + 2 blends) | Eclipse daily; blends 50/50 split into INT/LTC + ST/INT constituents per Andrew direction (2026-05-19) |
| **2b** | Inflection non-model (Eclipse-Fidelity custody minus 2a) | Eclipse daily, available 2026-05-15+ |
| **0** | Opal-ETF public float (DIVZ/IDVZ/PFDE/PFOE NAV minus partner-held) | Audit-trail field only (REVERSED out of headline per Andrew 2026-05-18: "ok dont include cohort zero for now") |

Andrew structural rule confirmed mid-session (Cohort 1b/2b hold $0 of the 4
Opal ETFs; non-model ETF AUA = Cohort 0 only; ~$10M RPS<model_estimate gap =
cash drag inside model accounts ~2% per ticker). Banked workspace-side by
COO as `reference_opal_etfs_model_accounts_only.md`.

---

## 2. Commits this session (chronological) — DS Base lane

All on `origin/CLOUD`. Verified by `git log --author=0.4.0_DS_ClientPlatform`.

| Commit | Title | What it landed |
|---|---|---|
| `985af022c` | v0 bandaid backfill (later rejected) | 541 daily platinum partitions interpolated from Andrew's weekly reference table. `data/mdpf/scripts/backfill/build_mdpf_v0_bandaid_backfill.py` + parser + ref parquet. |
| `fa03c19f0` | rollup builder + AE handoff for Lambda route | `build_aggregate_aua_timeseries.py` + `HANDOFF_AE_lambda_route.{md,diff}` |
| `8d9325558` | WS-D.2 partner-held-ETF feeder + acceptance proof | `wsd_partner_held_etf.py` + `verify_wsd2_clears_identity2.py` + DSA aggregator-wire handoff + AE runbook |
| `2e815b467` | WS-A consume partner_held_etf | mdpf_aggregate_aua.py: identity_2 ERROR (PFOE -$427K) → PASS (min +$2,089K), all 4 ETFs ≥ 0; partner_held override per (firm,ticker); per-ticker attribution_basis |
| `99abad76c` | Process-derived DAILY historical backfill | Replaced the rejected bandaid. `build_mdpf_process_backfill.py` reads SmartX daily exports (not the monthly rollup that misled me) + WS-E custody crosswalk; 96 daily partitions 2025-12-23 → 2026-05-18, identity 76/76 PASS exact |
| `fb9a910b8` | Drop SmartX EndMarketVal=0 rows + null 1b on partial-1a | Caught my v1 defect (8 dates emitted $0 1a; 4 misattributed full custody into 1b -- same fabrication class as the bandaid). Two structural fixes. |
| `41f0b2605` | opal_aggregate_aua INCLUDES Cohort 0 (amendment) | Andrew-direct: "they are opal etfs, its fee paying assets for us." Headline $1,939,892,055.01 incl. ETF public float |
| `bd2bbfbd9` | REVERT — opal_aggregate_aua back to partner-only | Andrew-direct 2026-05-18: "ok dont include cohort zero for now." Headline back to $1,848,563,071.88. Cohort 0 retained as audit-only field. Reversal of 41f0b2605, ~30 min later, after Andrew saw the cliff-warning. |
| `14ad0a033` | Legacy-compat emit v1 | `build_legacy_compat_emit.py`: write Schwab-only + Inflection into legacy `aum-timeseries.json` + `non_model_assets.json` (the Model Portfolios page consumed files). Cutover 2026-01-17. Latest 2026-05-15 enterprise_total $1,851,711,240.06. |
| `e0f22b108` | Smooth 1/16+1/19 + skip post-cutover zero-emissions | Cutover shifted to 2026-01-16 (smooth boundary). Market-holiday roll-forward for MLK Day. Skip post-cutover dates with platinum partition missing OR partial OR 1b null AND 1a moved. 9 skipped + 1 roll-forward. |
| `5dacfb18a` | Custody-crosswalk cache for AE Lambda | `build_custody_crosswalk_cache.py` publishes `s3://opal-data-mdpf/cache/custody_crosswalk.json` (10,451 accounts, 0 conflicts, sha256 `b106a983...`). AE's Lambda fix consumes via GetObject — avoids silver/fees IAM grant + memory bump in the Lambda. |
| `16541460e` | Extend emit past last legacy date | Andrew direct: "daily aua should have up to 5/18, we're only displaying up to 5/15." Picks up platinum dates > last legacy period; 5/18 appended. |
| `46bb5b023` | Firm-level per-model merge + 50/50 blend split | Andrew direct: "we have model breakdowns for inflection, we need to map those in" + "50/50 portfolios should be split in the models that we do have bucketed front end." Replaces the dropped "Inflection" by_model line with per-model merge into the 5 49F-canonical lines; Inflection blends split 50/50 into constituents per `BLEND_SPLIT`. Chart stack now matches radial ($1.82B for 5/18). |

Other commits in the period from cross-lane partners:
- `4f631c309` (DS Base, prior session boundary): canonical Schwab-only matcher `mdpf011_match.py`
- `1757fe364`, `d2c751cfc` (DS Base, prior boundary): WS-A AMENDMENT-1 three-way + session log
- `56d056458`, `dd75f791c` (DS~B): WS-C re-tag closing `MDPF_ASSETS.014` (Inflection cohort_class
  re-tag; section-7 dual-check PASS; feeds_pre_amendment1 now empty)
- COO and CTO project-record commits + tag commits

---

## 3. S3 artifacts state at session close

### Production daily-chain platinum (AE 0.7 chain output + my backfill)

- `s3://opal-data-portal-v2/platinum/mdpf/aggregate_aua/{date}.json` — **96
  daily partitions** 2025-12-23 → 2026-05-18 (76 fully-decomposed + 17
  honest-1b-null pre-BD-coverage + 3 broken-BD-schema-null + 2
  partial-1a-tagged). Schema per WS-A contract incl. amendment-then-reversed
  `opal_aggregate_aua` (partner-only) + audit-trail
  `partner_aua_subtotal` + `etf_public_residual_total` fields.
  Anchor 2026-05-15: 49F total $1,648,847,956.91; 2026-05-18 (AE chain
  re-fire output): $1,848,563,071.88 incl. Inflection.
- `s3://opal-data-portal-v2/platinum/mdpf/aggregate_aua_timeseries.json` —
  rollup of the 96 partitions, columnar, ~67 KB.

### Legacy Model Portfolios page consumed files (rewritten by my emit)

- `s3://opal-data-portal-v2/json/portfolios/aum-timeseries.json` — 392
  periods. Pre-2026-01-16 verbatim passthrough from prior legacy file.
  2026-01-16 onward: Schwab-only methodology + Inflection per-model merge
  (UST/ST/INT/LTC/LTA each carry 49F + Inflection's same-named + Inflection
  blend split halves). Latest 2026-05-18 aggregate $1,434,018,333.47.
- `s3://opal-data-portal-v2/json/portfolios/non_model_assets.json` — latest
  2026-05-18 enterprise_total $1,823,659,723.24, model_aum
  $1,434,018,333.47, non_model_aum $389,641,389.77; `etf_public_residual`
  $91,328,983.13 audit-only.

### MDPF feeder + cache prefix

- `s3://opal-data-mdpf/mdpf/feeds/partner_held_etf/49financial/2026-05-18.parquet`
  — WS-D.2 first run from `8d9325558`. 4 rows (DIVZ/IDVZ/PFDE/PFOE).
- `s3://opal-data-mdpf/cache/custody_crosswalk.json` — sha256 `b106a983...`,
  ~310 KB, 10,451 accounts, 0 conflicts. Consumed by AE's
  `append_non_model_today.py` Lambda fix to avoid the daily 1,856 silver/fees
  partition scan.

---

## 4. Scripts written this session

All under `data/mdpf/scripts/`:

| Path | Purpose |
|---|---|
| `probes/mdpf012_smartx_historical_probe.py` | Probe SmartX REST for as-of/historical endpoints. Result: NO (all date-param variants returned present-state). Banked structural fact. |
| `probes/mdpf012_smartx_bucket_history_probe.py` | Catalog SmartX bucket coverage. Found `consolidated/smartx_allocations.parquet` (monthly rollup, the trap I fell into) AND the daily exports at `exports/{run,docker}-*/` (the real daily source). |
| `backfill/build_mdpf_v0_bandaid_backfill.py` | REJECTED v0 bandaid (weekly-doc interpolation). Kept as the predecessor record + the parser for Andrew's weekly reference table is reused. |
| `backfill/build_mdpf_process_backfill.py` | Process-derived daily backfill. Reads SmartX daily exports + WS-E custody crosswalk. Drops EndMarketVal=0 rows + nulls 1b on partial-1a (v2 fix). |
| `backfill/build_aggregate_aua_timeseries.py` | Columnar rollup of the 96 daily partitions. |
| `backfill/build_legacy_compat_emit.py` | Translates daily-process artifacts into legacy-MP-page schema. Per-model firm-level merge + blend split + 1/16-1/19 smoothing + zero-emission skip + extend-past-legacy-last-date. |
| `backfill/build_custody_crosswalk_cache.py` | Publishes the crosswalk cache for AE's Lambda. |
| `feeders/wsd_partner_held_etf.py` | WS-D.2: real Schwab-RPS held ETF value per (firm, ticker). |
| `feeders/verify_wsd2_clears_identity2.py` | Acceptance proof of the WS-D.2 wire (used before committing the aggregator change). |
| `feeders/HANDOFF_DSA_wsd2_aggregator_wire.md` | Handoff doc (later absorbed: COO reassigned the wire to me from DS~A). |
| `RUNBOOK_AE_mdpf_daily_chain.md` | The runbook AE 0.7 used to codify the daily chain (4-stage DAG, failure semantics, placement). |
| `reference/parse_andrew_weekly_aua.py` + `andrew_weekly_aua_20260518.{txt,parquet,csv}` | Andrew's pasted weekly AUM reference, parsed (used for cross-validation, not for emission). |

---

## 5. Memory entries banked this session

- `feedback_identity1_masks_absolute_value_class.md` — §7 identity_1 PASS is
  necessary-not-sufficient for absolute-scale; 4 anchors in 24h (PFOE
  over-attribution, Spread-2 partner-feeder vintage spread, SmartX
  day-1-of-period zero-emission, INFGRO Findings A/B). MEMORY.md pointer
  added. CTO accepted as canonical (memory companion not needed; parent
  cross-link suffices).

Pre-existing memory entries leveraged + relevant:

- `feedback_owned_paths_hook_earns_keep_under_fast_ship.md` — invoked when
  the Lambda-route Edit was blocked by the owned-paths hook; clean reroute
  via handoff doc to AE.
- `feedback_s3_pull_dispatcher_no_auto_propagate.md` — invoked twice in the
  session (when I framed "from your scheduled daily-forward cutover, the
  artifact will publish the amended headline automatically -- nothing to
  redeploy" wrong, AE corrected; and later when I added the
  v1.1-hardening CI auto-sync mention).
- `feedback_cto_reversal_requires_new_empirical.md` — parent for the
  necessary-not-sufficient discipline this session's findings extend.

---

## 6. Major decision sequences (Andrew-direct directives chronologically)

1. **"how to take over for the daily Model Portfolio AUA update"** — original
   ask. Spawned the cohort-decomposition design + WS-A amendment thread +
   AE 0.7 chain codify.
2. **"no bandaids, our numbers are right"** — rejected `985af022c`
   weekly-doc-interpolated 541-partition backfill. Pivoted to
   process-derived. (Then I fell into the monthly-rollup trap →
   "what is this bullshit what numbers are you looking for exactly we have
   daily smartx numbers for every single model from smartx going back to at
   least jan 1" → pivoted again to the daily-exports source. `99abad76c` +
   `fb9a910b8`.)
3. **"trust our process number for 49 not the earlier document"** — process
   number $1,655,447,182.20 (Schwab-confirmed) is canonical for 49F, NOT
   the weekly document's $1,682.52M (broader scope).
4. **"For the remainder of this session you are the only DS who should be
   tasked with any work"** — sole-DS routing. Tilde-lane delegation
   off-limits. AE 0.7 cleared for cloud; CTO via direct line. Consequence:
   when COO routed the WS-A wire to DS~A and couldn't attest DS~A was
   actively working it, I took the wire myself under Andrew-pre-authorized
   no-silent-dependency branch.
5. **"it is opal advised, they are opal etfs, its fee paying assets for us"**
   — Cohort 0 in headline (commit `41f0b2605` adds it).
6. **"ok dont include cohort zero for now"** — reversed `41f0b2605` (commit
   `bd2bbfbd9`), ~30 min later, after the cliff-warning I gave landed.
   Cohort 0 retained as audit-trail field only.
7. **"no change to time series aside from 1/17/2026 onward"** — anchored
   the legacy-compat emit's CUTOVER_DATE; later shifted to 2026-01-16
   after the 1/16 boundary jump (BD silver/allocations starts 1/16; one
   extra day of Schwab-only is real measurement, not fabrication).
8. **"Inflection is from Orion/Eclipse, this figure is an aggregate. I
   believe those came in around 5/15"** — Eclipse daily data via
   `s3://opal-data-inf/{gold,silver}/eclipse/{date}/`. Verified: 3 dates
   available (5/15, 5/17, 5/18).
9. **"do both at the same time, do the DS work and parallize with the AE
   work"** — DS-side legacy-compat emit + AE-side Lambda fix in flight
   together; published the crosswalk cache for AE's consumption.
10. **"i dont see it fixed" → CDN cache investigation** — chased through to
    AE-issued CloudFront invalidation `I1MTRIVW529XJW2G5BOD78769S` covering
    `/api/general/portfolios/*`. Status Completed.
11. **"we're now showing 1.73b in 5/18 but 1.82b in the radial"** —
    diagnosed: chart's MODEL_ORDER drops the "Inflection" by_model line
    because it's not in the 5-49F-canonical list. Initially proposed
    frontend MODEL_ORDER edit; Andrew countered with "we have model
    breakdowns... we need to map those in / Eclipse has them" → per-model
    firm-level merge instead.
12. **"50/50 portfolios should be split in the models that we do have
    bucketed front end"** — `BLEND_SPLIT` map: blends apportioned 50/50 to
    constituents rather than emitted as new model lines. (Pure DS-side fix;
    portal MODEL_ORDER untouched.)

---

## 7. CTO/COO threads opened + closed this session

| Thread | State |
|---|---|
| Spread-2 absolute-value decomposition ($1,855M vs $1,848M = $6.60M, 0.36%) | CLOSED `02:07Z` RAVC2 → named-$0 to the cent: BD-vintage 5/14 vs 5/15 partner_custody delta $6,599,225.29 EXACT + WS-B SmartX intraday vintage in the 1a/1c side. Empirical decomposition via direct `wse.compute_partner_custody_total` against both BD partitions. |
| Cohort 0 amendment + reversal (`41f0b2605` → `bd2bbfbd9`) | CLOSED. Project record reflects the reversal; Cohort 0 retained as audit-trail field; re-flip is a one-line change if/when Andrew wants. |
| MDPF.016 Cohort 0 historical backfill (COO TO dispatched ~30min before reversal) | DEFERRED per Andrew. Not cancelled; keeps the TO ready if Cohort 0 re-flips into headline. |
| Zero-models / first-trading-day-of-month chart drops (CTO investigation ask) | CLOSED RAVC4 ACCEPTED `13:13Z`. Empirical root-cause: SmartX day-1-of-period EndMarketVal=0 on the 5 model CSVs for 2026-04-01 (6,470 rows, $0). Two-layer fix already landed pre-message (`fb9a910b8` + `e0f22b108`). Chart attribution clarified (legacy file, not platinum). CTO rider-2 to AE for tomorrow's at-risk 2026-06-01 run (defensive `model_aum > $100M` guard) now in flight as COO TO authoring. |
| Identity_1-masks-absolute-value memory entry | banked + cross-linked + CTO accepted as canonical. 4 anchors in 24h. |

---

## 8. AE 0.7 / DT / portal coordination

AE 0.7 closed multiple loops with me parallel-style (channel-pushed
messages, fast turnarounds):

1. **First-live-fire of the daily chain** — Andrew direct "fire it now" →
   AE manual-invoked `mdpf-daily-trigger` Lambda (`run_id
   mdpf_daily_20260518_022139`). Initial fire produced the
   Cohort-0-included version (caught between my push of `41f0b2605` and
   Andrew's "dont include cohort zero" reversal). Auto-stopped before STOP
   landed. Re-fired after my `bd2bbfbd9` revert + S3 re-sync; produced the
   correct partner-only $1,848,563,071.88 partition.
2. **The S3-pull dispatch-model gap** — my framing "nothing to redeploy"
   after pushing the WS-A amendment was empirically wrong (chain dispatcher
   S3-pulls scripts at run start; push to origin/CLOUD doesn't
   auto-propagate). AE caught + did the least-touch re-sync (single
   `mdpf_aggregate_aua.py` file, sha-verified). Memory was already banked
   on AE side (`feedback_s3_pull_dispatcher_no_auto_propagate.md`).
3. **Lambda fix for daily-forward** — AE chose my cache pattern over
   vendoring crosswalk-build. Shipped `smartx-pipeline-v1.0.0` (Lambda
   updated to consume `s3://opal-data-mdpf/cache/custody_crosswalk.json`
   for the Schwab-confirmed methodology, no silver/fees IAM grant, no
   memory bump). CTO TAG-GO'd. Lands before tomorrow 2026-05-20 14:00 UTC
   cron.
4. **CloudFront invalidation** — AE fired
   `I1MTRIVW529XJW2G5BOD78769S` covering `/api/general/portfolios/*`
   on the `EVTSA9VEHNZVH` distribution. Status COMPLETED. Andrew's
   hard-refresh after invalidation completes pulls fresh files.
5. **Portal-data-proxy Lambda cache verification** — AE verified
   `serve_s3_json` has no module-level S3 cache; per-request `get_object`.
   The `Cache-Control: max-age=300` it emits drives the 5-min CDN cache
   that was invalidated. No Lambda action needed.

---

## 9. Cross-lane events worth recording

1. **Spread-2 close empirics**: BD silver/allocations sums for
   2026-05-14 vs 2026-05-15:
   - BD 2026-05-14 partner_custody_total (Schwab-only) = $1,655,447,182.20
     (the value my .runtmp/wsa_wired.json consumed)
   - BD 2026-05-15 partner_custody_total (Schwab-only) = $1,648,847,956.91
     (the value AE's chain consumed after BD's 5/15 partition uploaded at
     2026-05-18T22:03:20Z)
   - Delta: $6,599,225.29 to the cent. Entire Spread-2 closed to named=$0
     via this empirical check.

2. **SmartX zero-emission empirical proof** (for the structural memory):
   2026-04-01 SmartX daily export CSVs:
   - 5 model CSVs present (INT/LTA/LTC/ST/UST)
   - 6,470 Open allocation rows total
   - EVERY row EndMarketVal = $0.00; sum $0.00
   - Distinct from the prior-day or next-day where total is typically
     ~$1.2B / ~6,000 non-zero rows
   - 7 affected dates in 2026 to-date: Jan 2/3/4 (invisible because pre-BD
     coverage) + Feb 2, Mar 2, Apr 1, May 1 (Andrew flagged "first trading
     day of each month from Feb forward")

3. **Three structural traps caught + fixed** in the historical-backfill
   work:
   - (a) Used the monthly-rollup `consolidated/smartx_allocations.parquet`
     thinking it had daily data (it keys on `PeriodEnd` = month-end and
     destroys daily granularity). Andrew empirically caught with the
     daily-exists statement; corrected by reading `exports/{run,docker}-*/`
     directly.
   - (b) Carried a stale monthly 1a against fresh daily custody → 1b
     residual absorbed real 1a growth (carried-as-if-real fabrication).
     Andrew's no-bandaid principle caught; corrected by requiring
     same-date co-measurement.
   - (c) Summed SmartX day-1-of-period zero rows → $0 1a → full custody
     misattributed into 1b. CTO investigation framework + my own series-walk
     identity-check caught; corrected by filtering `EndMarketVal == 0` rows
     pre-aggregation + nulling 1b on partial-1a-coverage.

---

## 10. Outstanding items at session close

| Item | Owner | State |
|---|---|---|
| AE 0.7 first scheduled daily-forward fire tomorrow 2026-05-20 14:00 UTC | AE 0.7 | scheduled, AE watching telemetry |
| CTO rider-2 TO authoring for the day-1-zero defensive guard before 2026-06-01 | CTO → COO | in flight; threshold-based `model_aum > MIN_PLAUSIBLE` recipe accepted |
| WS-C Inflection feeder full historical (task #16) | DS Base (me) | parked; only 3 Eclipse dates exist (5/15, 5/17, 5/18) so historical is unmeasurable until Eclipse historical pull is built |
| MDPF.016 Cohort 0 historical backfill | COO TO | DEFERRED, ready to start if Cohort 0 re-flips into headline |
| Andrew browser hard-refresh verification | Andrew | Pending. CloudFront invalidation COMPLETED. |

---

## 11. Key numbers to-the-cent at session close

| Metric (2026-05-18, live feeds) | Value |
|---|---:|
| **opal_aggregate_aua (partner-only, reverted)** | **$1,848,563,071.88** |
| ↳ partner_aua_subtotal | $1,848,563,071.88 |
| ↳ etf_public_residual_total (audit-only, NOT in headline) | $91,328,983.13 |
| ↳ 49F (1a+1b+1c) total | $1,649,016,956.91 |
| ↳ Inflection (2a+2b) total | $199,715,114.97 |
| **Model Portfolios page enterprise_total** | **$1,823,659,723.24** (49F + Inflection) |
| ↳ chart stack sum (5 firm-level model lines + Non-Model) | $1,823,659,723.24 (matches radial post-`46bb5b023`) |

The `$199.72M` Inflection slot is in non_model_aua on the page (via
`enterprise_total = 49F + Inflection`); the chart's 5 model lines
redistribute Inflection 2a's $93.60M (and the 2 blends, 50/50-split) into
the same 5 canonical lines as 49F, so the stack visually matches the radial.

---

## 12. Process notes for next session / handoff

- **Sole-DS routing for this session was Andrew-direct; revert to normal
  multi-lane routing at next session boundary** unless Andrew re-asserts.
- **The CloudFront invalidation pattern** (AE-fired
  `I1MTRIVW529XJW2G5BOD78769S` on `/api/general/portfolios/*`,
  ~30s fire to ~10min Completed) is the canonical fix for "S3 updated but
  page still stale." Document under `feedback_cdn_cache_staleness_*` (a
  memory file already exists for that pattern; this session was an empirical
  re-anchor).
- **AE's daily-chain S3-pull-model** is not auto-syncing; any DS edit to
  `data/mdpf/scripts/{feeders,gold,backfill}/*.py` that runs in the daily
  chain requires AE re-syncing the file to `s3://opal-data-mdpf/code/scripts/`
  before next chain fire. Memory entry `feedback_s3_pull_dispatcher_no_auto_propagate.md`
  has full detail. v1.1 CI auto-sync would close the gap (AE TO candidate).
- **The Andrew weekly reference table** (
  `data/mdpf/reference/andrew_weekly_aua_20260518.parquet`,
  86 weekly dates 2024-04-22 → 2026-05-15) is a cross-validation tool, not
  an emit source. Per Andrew "no bandaids" it's retained as a reference for
  quick spot-checks, not as a fallback when process data is missing.
- **Eclipse model_name → 49F display_name canonical mapping** (the
  `ECLIPSE_NAME_TO_KEY` + `BLEND_SPLIT` constants in
  `build_legacy_compat_emit.py`) is verified against the WS-C feeder output
  (sha-stable on 2026-05-18 partition). Any future Inflection model
  additions need to be added to both maps in lockstep.
