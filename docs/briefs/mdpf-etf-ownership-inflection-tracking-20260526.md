# Inflection ETF Ownership Tracking — Ad-Hoc Brief for PRD Authoring

**Author:** 0.4.0_DS_ClientPlatform (base)
**Date:** 2026-05-26
**Audience:** 1.0.0_SA_CTO (PRD-author target); CC 2.0.0_SA_COO + 0.0.0_AB_MSTR
**Source ask:** Andrew sovereign direct, 2026-05-26 (three sequential asks during a /work cycle interrupt)
**Status:** DS findings + analysis complete; CTO to absorb into a project PRD (suggested code: `MDPF_OWNTS` — MDPF ETF Ownership Time-Series)

---

## TL;DR

Three sequential asks rolled in one Andrew direct:

1. **Snapshot:** Inflection Wealth Management's % ownership of total NAV for the four Opal-sponsored ETFs (PFDE, PFOE, DIVZ, IDVZ) — most-recent platinum snapshot.
2. **MTD average:** Average of those daily % values across the calendar month, treating each day as one observation.
3. **Productionize:** A recurring scheduled compute (EC2 — "variation on the INF-gold-runner with smaller CPU") that maintains the snapshot + the timeseries on an ongoing basis.

Asks 1 and 2 are **answered inline below** (data already exists in the daily MDPF platinum artifact — no new compute required for the back-look). Ask 3 is **a productization design** — two scoped options (lean/no-new-EC2 vs. dedicated-runner) for CTO to pick.

---

## Ask 1 — Snapshot (latest day, 2026-05-26)

### Method

Pulled `s3://opal-data-portal-v2/platinum/mdpf/aggregate_aua/2026-05-26.json` (the daily MDPF aggregate-AUA platinum, methodology version `v0_9`, generated 2026-05-26T18:15:30Z by `data/mdpf/scripts/gold/mdpf_aggregate_aua.py`). The artifact already exposes a section `etf_decomposition` with one record per Opal ETF carrying `etf_total_net_assets` + `held_by_partner[{firm_id, held}]` + `public_residual`.

ETF NAVs source: `s3://opal-data-etfs/silver/netassets_daily.parquet` (Filepoint issuer CSV ingest; consolidated daily series; PFDE/PFOE NAV history starts 2026-05-18 per the Filepoint integration onboarding).

Inflection model-attribution basis: `target_weight v1` (per `build_mdpf_wsc_inflection_feeder.py:32` — "ETF attribution basis is target_weight v1 (ruling iii); actual_weight is null"). Each Inflection account's `model_value` × `model_composition.target_weight` aggregates to the firm-level holding for each ticker.

49Financial attribution basis (shown for context): `rps_actual` from Schwab RPS — actual position values, not target weights.

### Findings

| Ticker | ETF NAV ($M) | Inflection $ | **Inflection % of NAV** | 49F $ | 49F % |
|--------|-------------:|-------------:|------------------------:|------:|------:|
| DIVZ   |      248.18  |       0.00   |  **0.000%**             | 172,061,172.18 | 69.33% |
| IDVZ   |      161.45  |       0.00   |  **0.000%**             | 149,153,521.39 | 92.38% |
| PFDE   |      133.71  |  9,913,473.70|  **7.414%**             | 121,455,791.19 | 90.83% |
| PFOE   |       79.36  |  5,744,888.34|  **7.239%**             |  70,679,902.82 | 89.07% |

**Interpretation note:** DIVZ/IDVZ = 0% is correct, not a missing-data artifact. Inflection's Eclipse-administered models do not include DIVZ or IDVZ in their target-weight composition; PFDE and PFOE are in Inflection's blended models (Long-Term Conservative, Intermediate, blends). This is per construction of the WS-C feeder — if a future Inflection model adds DIVZ/IDVZ targets, the value will start appearing automatically.

---

## Ask 2 — MTD average (May 2026)

### Method

Listed all available May 2026 snapshots under `s3://opal-data-portal-v2/platinum/mdpf/aggregate_aua/` (16 snapshots: 5/04, 5/05, 5/06, 5/07, 5/08, 5/11, 5/12, 5/13, 5/14, 5/15, 5/18, 5/19, 5/20, 5/21, 5/22, 5/26 — weekdays only). For each snapshot pulled `etf_decomposition[ticker].etf_total_net_assets` and the Inflection entry in `held_by_partner`, computed daily ownership % per ticker, then averaged.

**Window cut:** Inflection's MDPF partner onboard date is 2026-05-18 (see `mdpf_aggregate_aua.py:90 INFLECTION_PARTNER_ONBOARD_DATE`); PFDE/PFOE NAV history likewise begins 2026-05-18 per Filepoint integration. Pre-5/18 dates have Inflection % = 0 for all four ETFs because Inflection was not yet a partner in the aggregate. The **meaningful averaging window is 2026-05-18 → 2026-05-26 (n=6 dates)**.

### Findings

**Per-day Inflection ownership % (post-onboard window):**

| Date       | DIVZ   | IDVZ   | PFDE   | PFOE   |
|------------|-------:|-------:|-------:|-------:|
| 2026-05-18 | 0.000% | 0.000% | 7.420% | 7.232% |
| 2026-05-19 | 0.000% | 0.000% | 7.428% | 7.240% |
| 2026-05-20 | 0.000% | 0.000% | 7.362% | 7.296% |
| 2026-05-21 | 0.000% | 0.000% | 7.354% | **5.013%** |
| 2026-05-22 | 0.000% | 0.000% | 7.502% | **5.100%** |
| 2026-05-26 | 0.000% | 0.000% | 7.414% | 7.239% |

**MTD averages (n=6, post-onboard window):**

| Ticker | Avg % | Daily range |
|--------|------:|:-----------:|
| DIVZ   | **0.000%** | flat 0% |
| IDVZ   | **0.000%** | flat 0% |
| PFDE   | **7.413%** | 7.354% – 7.502% |
| PFOE   | **6.520%** | **5.013% – 7.296%** |

**Anomaly flag — PFOE 5/21 + 5/22 dip:** PFOE ownership dropped from 7.296% on 5/20 to 5.013% on 5/21 (a 2.28 pp drop in one day), held at 5.100% on 5/22, and recovered to 7.239% by 5/26. PFDE and the other three series do not show a parallel discontinuity, so it is not a generalized data-pipeline outage. Could be (a) a real Inflection holding change (model rebalance or composition update), (b) a one-day PFOE NAV jump from a creation/redemption event widening the denominator, or (c) a transient data-emit anomaly. **Not in scope for this brief to root-cause; flagging for CTO's awareness in case the PRD wants a sentinel.** Drill-down available on request.

**Pre-onboard full-month context** (for completeness): including the pre-5/18 zero days, the full-May average is PFDE 7.413% / PFOE 6.520% (n=6 nonzero of 16 total). Averaging methodology in the PRD should explicitly choose between (i) post-onboard-only mean, (ii) full-window-with-zeros mean, (iii) Inflection-only-emit-days mean — these will diverge as more months ship.

---

## Ask 3 — Productionize as a recurring schedule (design options for CTO)

### Context the PRD inherits

The underlying compute already runs daily as part of the MDPF chain (`mdpf_aggregate_aua.py` on the MDPF EventBridge schedule; outputs `s3://opal-data-portal-v2/platinum/mdpf/aggregate_aua/{date}.json`). The platinum artifact already contains both the numerator (`held_by_partner[firm_id=inflection].held`) and the denominator (`etf_total_net_assets`) — what is **missing** for productionization is:

1. A **derived `ownership_pct` field** (or an equivalent derived artifact) so consumers don't need to recompute the ratio.
2. A **timeseries view** (`{ticker}.json` keyed by date) so a portal/dashboard can render the historical track without scanning N daily snapshots.
3. A **monthly rollup** (running avg over a chosen window) consistent with Andrew's Ask 2 framing.
4. Optionally, **other partners** as Inflection partners onboard.

Andrew's framing — "create a schedule in EC2 that will manage this, maybe use a variation on the INF-gold-runner with smaller CPU" — implies he envisions Option B below. The leaner Option A is also viable and may be the better engineering call; CTO to choose.

### Option A — Extend existing MDPF chain (lean; zero new infra)

- **Change 1:** Modify `mdpf_aggregate_aua.py` to emit a derived `ownership_pct` per `held_by_partner` entry inside `etf_decomposition`. Cost: ~4 lines + one fixture update. No schedule change, no new EC2.
- **Change 2:** New small gold script `build_mdpf_etf_ownership_timeseries.py` that reads the last N daily platinums and emits `s3://opal-data-portal-v2/platinum/mdpf/etf_ownership_timeseries/{ticker}.json` (a date-keyed series + MTD/YTD rollups). Wired into the existing MDPF dispatch chain at the post-aggregate step.
- **Runner:** Existing `inf-gold-layer-runner` (it runs the MDPF chain today). No new EC2.
- **Schedule:** Existing daily MDPF cron.
- **Total work:** ~1 day DS author (script + fixtures + comp-validate config) + ~1 day AE wire (chain integration + dispatch step) + ratification cycle.
- **IAM:** Existing `inf-gold-runner-ec2-role` already has write to `opal-data-portal-v2` and read of `opal-data-mdpf` — no new policy.

### Option B — Dedicated runner (closer to Andrew's framing)

- **New EC2 instance** `mdpf-ownership-runner` modeled on `inf-gold-qa-runner` but smaller:
  - Instance type: **t3.small (2 vCPU / 2 GB)** or **t3.medium (2 vCPU / 4 GB)** — the compute is trivial (read 1 platinum JSON; write 1 derived JSON + 1 timeseries JSON). t3.small likely sufficient.
  - Mirror the inf-pipeline S3-pull dispatcher pattern (`run-gold-layer.sh` boot dispatcher → `s3://opal-data-mdpf/code/...` for the ownership-runner code).
- **Terraform workspace:** New module under `infra/aws/terraform/mdpf-pipeline/` (or merge into existing if MDPF has its own; verify with CTO/AE), per CLAUDE.md Rule 9 (Terraform owns the instance + role + SG + profile).
- **EventBridge cron:** Daily at ~14:30Z (after MDPF aggregate emits at ~14:15Z), per the inf-gold-runner pattern.
- **Output artifacts:**
  - `s3://opal-data-portal-v2/platinum/mdpf/etf_ownership/{date}.json` — daily snapshot with `ownership_pct` for each partner × ticker.
  - `s3://opal-data-portal-v2/platinum/mdpf/etf_ownership_timeseries/{ticker}.json` — per-ticker date-keyed series + MTD/YTD running avgs.
- **EC2_MANIFEST.json entry** + `safe-ec2-deploy.sh` wrapper, per CLAUDE.md Rule 7-12.
- **IAM:** New role `mdpf-ownership-runner-ec2-role` with read on `opal-data-portal-v2/platinum/mdpf/aggregate_aua/*` and write on `opal-data-portal-v2/platinum/mdpf/etf_ownership*` + `etf_ownership_timeseries*`.
- **Total work:** ~3-4 days — DS author + AE Terraform + IAM + EC2 bootstrap + dispatch wiring + ratification cycle.

### DS recommendation

**Option A** is the right shape if the only consumer is the Inflection ownership question + a portal time-series. The compute is genuinely trivial; a dedicated EC2 would spend 99% of its life idle. The cleanest engineering move is to make the existing MDPF chain emit one more derived artifact.

**Option B** becomes the right shape if any of these are true (CTO judgment):
- The ownership tracking will expand to **other ETFs** outside the four Opal ones (i.e., the metric is general "what % of any ETF's NAV does each Opal partner own" — would need wider data sources).
- The ownership tracking will expand to **other partners** beyond Inflection + 49F at a scale where chain-integration becomes brittle.
- There's a desired isolation property (own runner / own role / own access scope) that Option A's reuse of the inf-gold-runner role doesn't satisfy.
- A near-real-time or sub-daily compute cadence is anticipated.

If any of those are in scope for the PRD, B's overhead is justified.

---

## Open questions for CTO (PRD scoping)

1. **A vs. B?** (see DS recommendation above)
2. **Which averaging methodology** for the headline number — post-onboard-only mean, full-window-with-zeros mean, or emit-days-only mean? (See Ask 2 note.)
3. **Scope of partners** — Inflection-only, or all current/future MDPF partners (49F, Inflection, and any new ones)?
4. **Scope of ETFs** — Opal-four-only (DIVZ/IDVZ/PFDE/PFOE), or any ETF for which an Opal partner has measurable ownership (would imply a broader NAV feed)?
5. **PFOE 5/21–5/22 anomaly** — does PRD want a sentinel (e.g., DoD-change > X pp = ERROR-gate or audit-flag)?
6. **Portal consumer** — is there a planned portal surface (page/widget) that needs the timeseries shape locked in? If so, the JSON shape should be PRD-ratified up front.
7. **Project code** — suggesting `MDPF_OWNTS` (MDPF ETF Ownership Time-Series); CTO to confirm or rename.

---

## References

- **This brief:** `docs/briefs/mdpf-etf-ownership-inflection-tracking-20260526.md`
- **Daily MDPF aggregate (data source):** `data/mdpf/scripts/gold/mdpf_aggregate_aua.py`; output prefix `s3://opal-data-portal-v2/platinum/mdpf/aggregate_aua/`
- **Inflection feeder (target-weight basis source):** `data/mdpf/scripts/gold/build_mdpf_wsc_inflection_feeder.py`
- **ETF NAV silver feed:** `s3://opal-data-etfs/silver/netassets_daily.parquet`
- **MDPF aggregation contract:** `docs/architecture/MDPF_ASSETS_WSA_CONTRACT.md` (RATIFIED 2026-05-18, AMENDMENT 1 ratified 2026-05-18 `7d8934ff2`)
- **Existing runner pattern (Option B reference):** `infra/aws/terraform/inf-pipeline/inf-gold-qa-runner.tf` + `infra/aws/ec2/EC2_MANIFEST.json` entry `inf-gold-qa-runner`
- **Deployment discipline (for Option B):** CLAUDE.md Rules 7-13
- **Pulled platinum snapshots used for v2 analysis:** `.runtmp/mdpf_may/*.json` (16 May 2026 dates)

---

## DS standing posture

Analysis complete; productionization on hold pending CTO PRD ratification + ws COO TO routing. Available to author the DS-side gold script (Option A or B) under a properly-routed TO; will not deploy EC2 work without the Rule 7-13 chain (Terraform + safe-ec2-deploy.sh + EC2_MANIFEST.json + COO/AE coordination).
