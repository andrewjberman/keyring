# FIND_INSURE Phase 2B Cross-Board Analytics Framework

| | |
|---|---|
| **Author** | 0.1.0_DS_MarketIntelligence~D |
| **Date** | 2026-05-27 |
| **TO** | FIND_INSURE.028 AC4 (ws COO dispatch 23:28Z) |
| **Parent PRD** | `docs/architecture/FIND_INSURE.md` v0.7 §4 Phase 2 Part B + §4 Phase 3 (serving consolidation) |
| **Sister artifacts** | `docs/reference/job-board-channel-architecture-matrix.md` (AC1) · `docs/briefs/find-insure-phase2b-multi-board-design-v0.1.md` (AC2) · `docs/reference/find-insure-phase2b-stage-routing-matrix.md` (AC3) |
| **Downstream consumer** | Phase 3 `serving/scoring.json` `hiring_signal_class` field per CVO ADDITIVE-1 (DS~E lane FIND_INSURE.023) |

---

## 0. Framing — why cross-board analytics

**Per-board gold tier** (`data/find/imo/scripts/gold/score_jobs_gold.py` per `.025` AC6) produces per-IMO `aggregate.json` per board with role_class distribution + Series-license aggregate + investment-keyword density + hiring-velocity. **Cross-board analytics tier** consumes those per-board aggregates ACROSS boards and produces per-IMO unified signals that no single board surfaces alone.

**The cross-board value proposition** rests on five orthogonal signals only computable at the cross-board layer:

1. **Multi-board syndication signal** — the same posting visible on 3+ boards = high-conviction hiring (employer paying for / coordinating distribution)
2. **Hiring-velocity acceleration** — cross-board normalized hiring count over 30/90/180-day windows; cross-board observation smooths per-board sampling noise
3. **Signal-class consistency** — investment-keyword density per IMO consistent across boards = high-conviction signal; divergent across boards = ambiguous signal (warrants Phase 3 IR-team review)
4. **Series-license requirement frequency** — Series-65/66 requirement frequency across boards directly maps to RIA-pivot intent (the FIND_INSURE definition-of-target)
5. **Corp-finance + tech-hire forward-signal class** (per CVO ADDITIVE-1) — corp-finance + tech hires beget M&A + platform-buildout activity → forward-leading indicator of asset-mgmt transition

This document defines the analytic computations for all 5 signals + the cross-IMO serving table integration that feeds Phase 3.

---

## 1. Signal #1 — Cross-board syndication (multi-board posting visibility)

**Definition:** the same posting appearing on N boards (deduped via composite-key per AC2 §6) carries `cross_board_observation_count = N` and `seen_on_boards = [board_1, ..., board_N]`. The hiring intensity signal is monotonic in N — an employer willing to pay LinkedIn premium + Indeed sponsorship + Glassdoor partner attribution for ONE role is committing more aggressively than one posting it only on Indeed.

**Per-posting metric:**

```
cross_board_visibility_score = log2(cross_board_observation_count + 1)
```

**Per-IMO aggregate:**

```
multi_board_postings_count = count(deduped_postings WHERE cross_board_observation_count >= 2)
multi_board_postings_pct   = multi_board_postings_count / total_deduped_postings
mean_cross_board_visibility = mean(cross_board_visibility_score across all deduped postings)
top_syndicated_posting     = posting with MAX(cross_board_observation_count)
```

**Decision-relevance class threshold:**

- `multi_board_postings_pct >= 0.40` AND `total_deduped_postings >= 5` → **HIGH-CONVICTION-SYNDICATION** signal
- `multi_board_postings_pct in [0.15, 0.40)` → MEDIUM-CONVICTION
- `multi_board_postings_pct < 0.15` → low syndication; either narrow distribution OR small posting universe

---

## 2. Signal #2 — Hiring-pace metrics (cross-board normalized hiring velocity)

**Definition:** hiring-velocity windows aggregated across boards smooth per-board sampling noise (some boards refresh nightly, others weekly; cross-board union captures the true posting universe).

**Per-IMO aggregate:**

```
hiring_velocity_30d   = count(deduped_postings WHERE posted_date >= run_date - 30 days)
hiring_velocity_90d   = count(deduped_postings WHERE posted_date >= run_date - 90 days)
hiring_velocity_180d  = count(deduped_postings WHERE posted_date >= run_date - 180 days)
hiring_velocity_360d  = count(deduped_postings WHERE posted_date >= run_date - 360 days)
hiring_velocity_acceleration = (hiring_velocity_90d / 3) / (hiring_velocity_180d / 6)
                              # ratio of recent-90d-monthly-pace to prior-90d-monthly-pace
                              # > 1.0 = accelerating; < 1.0 = decelerating
```

**Decision-relevance class threshold** (calibrated post-empirical; v0.1 candidates):

- `hiring_velocity_180d >= 10` AND `hiring_velocity_acceleration >= 1.3` → **ACCELERATING-BUILDOUT** signal (>50% pace bump in recent quarter)
- `hiring_velocity_180d >= 5` AND `hiring_velocity_acceleration in [0.8, 1.3]` → STEADY-HIRING
- `hiring_velocity_180d < 5` → low-activity (either small IMO or hiring-quiet phase)
- `hiring_velocity_acceleration < 0.5` AND `hiring_velocity_180d >= 5` → DECELERATING (potential signal class — but historically common at year-end / between-quarters)

---

## 3. Signal #3 — Investment-keyword density consistency (cross-board signal-class agreement)

**Definition:** the per-board investment-keyword density (count of `investment_title_hits` + `investment_description_hits` per posting) should be roughly consistent across boards for a true asset-management-transition IMO. Divergent density across boards indicates EITHER (a) board-specific sampling artifact OR (b) the IMO is selectively posting investment-role on certain boards only — a noisy signal worth Phase 3 IR-team review.

**Per-IMO cross-board statistic:**

```
per_board_investment_density[board] =
    sum(investment_title_hits per posting) + sum(investment_description_hits per posting)
    / count(postings)
    for each board where IMO has >=2 postings

cross_board_density_std = std(per_board_investment_density.values())
cross_board_density_mean = mean(per_board_investment_density.values())
cross_board_density_cv = cross_board_density_std / cross_board_density_mean
                         # coefficient of variation; low = consistent; high = divergent
```

**Decision-relevance class threshold:**

- `cross_board_density_mean >= 2.0` AND `cross_board_density_cv <= 0.3` → **HIGH-CONFIDENCE-INVESTMENT-FOCUS** (signal consistent + strong)
- `cross_board_density_mean >= 2.0` AND `cross_board_density_cv > 0.3` → INCONSISTENT-INVESTMENT-FOCUS (signal strong on some boards but not others → Phase 3 IR-team review)
- `cross_board_density_mean in [0.5, 2.0)` → MODERATE-INVESTMENT-PRESENCE
- `cross_board_density_mean < 0.5` → LOW-INVESTMENT-PRESENCE (background noise; not an asset-mgmt-transition candidate)

**Per-board breakdown surfaced in `aggregate.json`:**

```json
"per_board_investment_density": {
  "linkedin-jobs": 3.2,
  "indeed": 2.8,
  "efinancialcareers": 4.5,
  "insurancejobs-com": 0.8
}
```

The InsuranceJobs.com low-density entry above is informative — it would indicate this IMO's InsuranceJobs.com postings are insurance-only roles while LinkedIn/Indeed/eFinancialCareers carry the investment-role concentration.

---

## 4. Signal #4 — Series-license requirement frequency (RIA-pivot intent)

**Definition:** Series-65/66 explicit requirements are the cleanest single signal of RIA-pivot intent (Series 65 = IAR-class; Series 66 = combined IAR + state-securities). Series-7/24 indicate broker-dealer track or compliance-officer hiring; weaker signal for RIA-pivot. Cross-board aggregation surfaces requirement-pattern consistency.

**Per-IMO cross-board aggregate:**

```
series_65_required_count   = count(deduped_postings WHERE 65 in series_licenses_required)
series_66_required_count   = count(deduped_postings WHERE 66 in series_licenses_required)
series_65_or_66_required   = count(deduped_postings WHERE (65 in series_licenses_required OR 66 in series_licenses_required))
series_7_required_count    = count(deduped_postings WHERE 7 in series_licenses_required)
series_24_required_count   = count(deduped_postings WHERE 24 in series_licenses_required)

# Cross-board distinct boards observing each license requirement
series_65_observed_on_boards = distinct(board for posting WHERE 65 in series_licenses_required)
series_66_observed_on_boards = distinct(board for posting WHERE 66 in series_licenses_required)
```

**Decision-relevance class threshold:**

- `series_65_or_66_required >= 3` AND `len(series_65_observed_on_boards | series_66_observed_on_boards) >= 2` → **STRONG-RIA-PIVOT-SIGNAL** (cross-board confirmation of IAR-track hiring intent)
- `series_65_or_66_required in [1, 2]` → MODERATE-RIA-INTEREST (single-board signal; warrants Phase 2A LushaAI enrichment for current-state confirmation)
- `series_65_or_66_required == 0` AND `series_7_required_count >= 3` → BROKER-DEALER-TRACK-NOT-RIA (signal class divergent from FIND_INSURE thesis)

**Cross-reference to Phase 2A LinkedIn channel:** Phase 2A (LushaAI) surfaces current-state Series-license holders ON LinkedIn (employees already at the IMO). Phase 2B surfaces forward-looking Series-license requirements (employees the IMO is trying to hire). High consistency between the two = high-conviction; divergence = signal class disagreement worth Phase 3 IR-team review.

---

## 5. Signal #5 — Forward-signal hiring (corp-finance + tech-hire; CVO ADDITIVE-1)

**Definition (per Andrew direct 2026-05-27 + CVO ADDITIVE-1):** corp-finance hires (CFO / VP Finance / Controller / M&A / FP&A) + tech hires (CTO / Director of Engineering / Data Engineering / Platform) signal that the IMO is investing in the **underlying organizational infrastructure that begets asset-mgmt transition**. These don't DIRECTLY indicate asset-mgmt but indicate growth + platform-buildout + M&A activity that often PRECEDES the asset-mgmt pivot.

**Per-IMO cross-board aggregate:**

```
corp_finance_hires_count   = count(deduped_postings WHERE role_class == "corporate-finance")
tech_hires_count           = count(deduped_postings WHERE role_class == "technology")
corp_finance_hires_180d    = count(deduped_postings WHERE role_class == "corporate-finance" AND posted_date within 180d)
tech_hires_180d            = count(deduped_postings WHERE role_class == "technology" AND posted_date within 180d)

# Forward-signal index (composite)
forward_signal_index = (corp_finance_hires_180d * 1.0) + (tech_hires_180d * 0.7)
                        # corp-finance weighted higher (more direct M&A signal)
                        # tech weighted 0.7 (signal class but more diffuse)
```

**Decision-relevance class threshold:**

- `forward_signal_index >= 3.0` → **HIGH-FORWARD-SIGNAL** (growth + platform-buildout activity material)
- `forward_signal_index in [1.0, 3.0)` → MODERATE-FORWARD-SIGNAL
- `forward_signal_index < 1.0` → LOW-FORWARD-SIGNAL (steady-state ops)

**Decision-relevance integration:** IMOs with HIGH forward_signal_index + low current investment-professional density may be MORE interesting targets than IMOs with HIGH investment-professional density alone — the forward-signal IMOs are mid-transition, the early-stage targets the IR team can engage BEFORE the pivot completes.

---

## 6. `aggregated_hiring_signal_class` — unified Phase 3 enum (CVO ADDITIVE-1)

**Definition:** the unified per-IMO `aggregated_hiring_signal_class` enum that feeds Phase 3 `serving/scoring.json` per CVO ADDITIVE-1. Synthesizes Signals #1-#5 into a single decision-relevance label.

**Enum:**

| Class | Definition | Trigger conditions |
|---|---|---|
| `high-conviction-buildout` | IMO actively building asset-mgmt capability with multi-axis confirmation | (Signal #3 HIGH-CONFIDENCE-INVESTMENT-FOCUS) AND (Signal #4 STRONG-RIA-PIVOT-SIGNAL OR Signal #2 ACCELERATING-BUILDOUT) |
| `medium-conviction-growth` | IMO showing growth + investment-tilt signals but not yet conclusive | (Signal #3 MODERATE-INVESTMENT-PRESENCE OR Signal #4 MODERATE-RIA-INTEREST) AND (Signal #2 STEADY-HIRING OR Signal #5 MODERATE-FORWARD-SIGNAL) |
| `forward-signal-mid-transition` | IMO showing forward-signal activity (corp-finance + tech-hire) but NOT yet showing direct investment-role hiring | (Signal #5 HIGH-FORWARD-SIGNAL) AND (Signal #3 LOW or MODERATE-INVESTMENT-PRESENCE) |
| `low-signal-baseline` | IMO showing minimal job-board activity OR insurance-only hiring | (Signal #3 LOW-INVESTMENT-PRESENCE) AND (Signal #5 LOW-FORWARD-SIGNAL) |
| `quiet` | No deduped postings observed across all boards | total_deduped_postings == 0 |
| `inconsistent-needs-review` | Signal class disagreement across boards or other ambiguity | Signal #3 INCONSISTENT-INVESTMENT-FOCUS OR (Phase 2A LushaAI current-state signal disagrees with Phase 2B job-postings forward signal) |

**Integration with Phase 3 `serving/scoring.json`** (per CVO ADDITIVE-1; DS~E lane FIND_INSURE.023):

```json
{
  "imo_slug": "advisors-excel",
  "imo_canonical_name": "Advisors Excel",
  "phase1_web_signal_score": 78,
  "phase1_wm_classification": "present",
  "phase2a_linkedin_employee_count": 142,
  "phase2a_series_licensed_employee_count": 17,
  "phase2b_hiring_signal_class": "high-conviction-buildout",
  "phase2b_total_postings_deduped": 23,
  "phase2b_multi_board_postings_pct": 0.47,
  "phase2b_hiring_velocity_180d": 14,
  "phase2b_hiring_velocity_acceleration": 1.6,
  "phase2b_series_65_or_66_required_count": 5,
  "phase2b_corp_finance_hires_180d": 2,
  "phase2b_tech_hires_180d": 3,
  "phase2b_forward_signal_index": 4.1,
  "phase2b_per_board_observed": ["linkedin-jobs", "indeed", "efinancialcareers", "insurancejobs-com", "wealthmanagementjobs-com"],
  "phase2b_AUM_band_observed": "$500M-$1B AUM",
  "phase2b_top_signals": [...]
}
```

**Companies-table integration:** `serving/companies.{json,parquet}` per Phase 3 deliverable joins Phase 1 (web-scrape) + Phase 2A (LinkedIn) + Phase 2B (job-postings) signals. Companies-table rows for IMOs with `phase2b_hiring_signal_class in (high-conviction-buildout, medium-conviction-growth)` rank above background population in IR-team-facing presentation.

---

## 7. `serving/hiring_signals.json` — cross-IMO ranked table (per AC4 deliverable)

**Path:** `s3://opal-data-imo/serving/hiring_signals.{json,parquet}`

**Schema:**

```json
[
  {
    "imo_slug": "advisors-excel",
    "imo_canonical_name": "Advisors Excel",
    "aggregated_hiring_signal_class": "high-conviction-buildout",
    "total_postings_deduped": 23,
    "multi_board_postings_count": 11,
    "multi_board_postings_pct": 0.47,
    "hiring_velocity_30d": 4,
    "hiring_velocity_90d": 11,
    "hiring_velocity_180d": 14,
    "hiring_velocity_acceleration": 1.6,
    "investment_keyword_density_mean": 3.4,
    "investment_keyword_density_cv": 0.18,
    "series_65_or_66_required_count": 5,
    "series_65_or_66_observed_on_boards": 3,
    "forward_signal_index": 4.1,
    "corp_finance_hires_180d": 2,
    "tech_hires_180d": 3,
    "AUM_band_observed": "$500M-$1B AUM",
    "per_board_observed": ["linkedin-jobs", "indeed", "efinancialcareers", "insurancejobs-com", "wealthmanagementjobs-com"],
    "top_3_signal_postings": [
      {"posting_id": "linkedin-jobs:3724891234", "title": "Senior Wealth Advisor", "board": "linkedin-jobs", "score": 47.2},
      {"posting_id": "efinancialcareers:abc123", "title": "Portfolio Manager - RIA Platform", "board": "efinancialcareers", "score": 41.8},
      {"posting_id": "wealthmanagementjobs-com:def456", "title": "Director of Investment Operations", "board": "wealthmanagementjobs-com", "score": 38.5}
    ],
    "scoring_version": "v0.1",
    "computed_at": "2026-05-28T03:00:00Z"
  },
  ...
]
```

**Cross-IMO ranking:** sorted by composite rank score = `0.4 * normalized_investment_density + 0.3 * normalized_series_65_or_66_freq + 0.2 * normalized_hiring_velocity_acceleration + 0.1 * normalized_forward_signal_index`. Composite rank-score weights v0.1 are designed for empirical-first-run tuning by IR team — hand-adjustable.

---

## 8. Build-pipeline integration (where the cross-board layer runs)

**Lambda:** `data/find/imo/scripts/gold/aggregate_cross_board_signals.py` (NEW gold-tier Lambda; sister to per-board gold scoring)

**Inputs:**

- `s3://opal-data-imo/corp/{slug}/gold/job-postings/{board}/{run-date}/aggregate.json` (per-board per-IMO aggregate) — one per (board, IMO, run-date)

**Output:**

- `s3://opal-data-imo/corp/{slug}/gold/job-postings/{run-date}/cross_board_aggregate.json` (per-IMO cross-board aggregate)
- `s3://opal-data-imo/serving/hiring_signals.{json,parquet}` (cross-IMO table for Phase 3)

**Pipeline position:** AFTER all per-board gold-tier Lambdas complete (EventBridge dependency); BEFORE Phase 3 `serving-build` Lambda. EventBridge rule: `find-insure-cross-board-aggregate-trigger` fires when per-board gold scripts emit `gold-complete` telemetry for ≥4 boards (Wave 1 minimum); cross-board aggregate fires + writes cross_board_aggregate.json + updates hiring_signals serving table.

**Dispatch source:** orchestrator Lambda (Phase 1 pattern) OR direct invocation via per-IMO fan-out from refresh-source-list.

---

## 9. Empirical-first-run calibration plan

**v0.1 thresholds are EMPIRICAL-FIRST-RUN posture** per sister-pattern to PRD §3.8 Q-C3 (cost-budget overshoot tolerance) and PRD AC2a (bronze-tier completeness gate). All decision-relevance thresholds bind at first-99-IMO Phase 2B run; calibration happens at RAVC2 time.

**Specific calibration triggers:**

| Threshold | v0.1 value | Calibration signal |
|---|---|---|
| `multi_board_postings_pct >= 0.40` (HIGH-CONVICTION-SYNDICATION) | 0.40 | If >30% of universe hits HIGH on first-empirical, tighten to 0.50; if <5% hits HIGH, loosen to 0.30 |
| `hiring_velocity_180d >= 10` (ACCELERATING-BUILDOUT floor) | 10 | If 99-IMO median posting count is <5, lower floor to 5 |
| `cross_board_density_mean >= 2.0` (HIGH-CONFIDENCE-INVESTMENT-FOCUS) | 2.0 | Calibrate against Phase 1 wm_classification=present IMOs — should >80% of Phase-1-present IMOs also hit Phase 2B HIGH-CONFIDENCE; if not, threshold mis-calibrated |
| `series_65_or_66_required >= 3` (STRONG-RIA-PIVOT-SIGNAL) | 3 | If <10% of universe meets this, lower to 2 to surface more pivot candidates |
| `forward_signal_index >= 3.0` (HIGH-FORWARD-SIGNAL) | 3.0 | Calibrate against IR-team qualitative review of high-forward-signal IMOs at Phase 3 |
| Composite rank-score weights `[0.4, 0.3, 0.2, 0.1]` | as above | Hand-adjustable post-IR-team-review-pass |

**Calibration ownership:** RAVC2 author (DS lane authoring `aggregate_cross_board_signals.py`) reports first-empirical distribution + proposes threshold calibration at RAVC2-Request. ws CTO + ws COO ratify thresholds at RAVC2-Accept. IR-team review at Phase 3 produces final binding calibration.

---

## 10. Cross-references

- **AC1 board architecture matrix:** `docs/reference/job-board-channel-architecture-matrix.md` (sister this TO; 12-board universe + HAR-priority)
- **AC2 multi-board parser system design:** `docs/briefs/find-insure-phase2b-multi-board-design-v0.1.md` (sister this TO; cross-board dedup composite-key)
- **AC3 Stage Bα/Bβ routing matrix:** `docs/reference/find-insure-phase2b-stage-routing-matrix.md` (sister this TO)
- **`.025` HAR parser execution TO:** `org/tier2_senior/0.1.0_DS_MarketIntelligence~D/task_orders/FIND_INSURE.025.dsd-phase2b-stage-ba-har-parser.md` (per-board parser + per-IMO aggregate.json schema per AC7)
- **`.023` Phase 3 serving consolidation (DS~E lane):** `org/tier2_senior/0.1.0_DS_MarketIntelligence~E/task_orders/FIND_INSURE.023.dse-serving-consolidation-w3.md` — `serving/scoring.json` `hiring_signal_class` field consumer
- **CVO ADDITIVE-1 (`hiring_signal_class` field origin):** Phase 3 serving consolidation CVO contribution at FIND_INSURE.023 design
- **Parent PRD:** `docs/architecture/FIND_INSURE.md` v0.7 §4 Phase 2 Part B + §4 Phase 3 (serving consolidation) + §3.8 Q-C3 (EMPIRICAL-FIRST-RUN posture sister-pattern)
- **JobBoardParser silver schema:** `data/find/imo/scripts/_util/job_board_parser_base.py` (DS~D `97c32ffa4`) — consumes cross-board taxonomies uniformly

---

## 11. Authoring lineage

- **v0.1** 2026-05-27 — initial cross-board analytics framework per FIND_INSURE.028 AC4 ws COO dispatch 23:28Z. Defines 5 orthogonal signals (#1 syndication + #2 hiring-velocity + #3 keyword-density-consistency + #4 Series-license freq + #5 forward-signal) + unified `aggregated_hiring_signal_class` enum + `serving/hiring_signals.json` cross-IMO table schema + empirical-first-run calibration plan. v0.2 follow-on on first-empirical run will refine thresholds + introduce IR-team-feedback iteration loop per Phase 3 RAVC2.
