# FIND_INSURE Phase 3 IR-team feedback protocol + Lambda impl skeleton brief

| | |
|---|---|
| **Author** | 1.0.0_SA_CTO |
| **Date** | 2026-05-27 |
| **Status** | DRAFT — for COO decomposition into Phase 3 pre-authoring TO (DS~E lane) |
| **Lane** | DS~E 0.1.0_DS_MarketIntelligence~E — currently STANDBY-PURE since spawn |
| **Parent PRD** | `docs/architecture/FIND_INSURE.md` v0.6 |
| **Authority** | Andrew direct sovereign 2026-05-27T~19:50Z pace-pickup + ws COO `[ACK COORDINATED DISPATCH]` 20:03Z greenlight |

---

## 1. Why this brief exists

DS~E shipped Phase 3 design substrate early-session (`242ad4d8f` Phase 3 serving design + `6257f3d77` scoring-weights-v0.1 + `6ee4c7eb2` cost-budgets-v0.1) then went STANDBY-PURE awaiting Phase 2A convergence. Net STANDBY ~3-4h wall.

This brief unblocks **parallel-active Phase 3 IR-team-feedback-protocol authoring + Lambda implementation skeleton** — both can ship pre-Phase-2A-execution since Phase 3 consumes Phase 1 + 2A gold-tier outputs structurally, not by their concrete values. Skeleton authoring against fixture JSON (mirroring DS~A + DS~B + DS~C STANDBY-PREP class pattern) + IR-team-feedback protocol documentation are both PRD-anchored deliverables.

## 2. Scope — two threads

### 2.1 Thread A: IR-team feedback protocol (AC5 RAVC2 mechanism)

Author `docs/briefs/find-insure-ir-team-feedback-protocol.md` — the canonical AC5 RAVC2 mechanism per PRD v0.6 §7 AC5: "IR team review of the Phase 3 tables produces a verdict — either 'rankings agree with our judgment, ship for use' (CLOSE-COMPLETE) or 'rankings need recalibration, here is the feedback' (re-open Phase 3 scoring iteration)."

Substantive content:

**§A. Feedback elicitation methodology**
- IR-team-named-individual identification protocol (currently ADDITIVE-1 standing per PRD §11) — who validates? what credentials? what experience with IMO outreach?
- Review session structure: walkthrough format (sit-with-IR-rep vs async-spreadsheet-review vs hybrid)
- Sample size: full 99-IMO universe review vs stratified sample (top quintile + random sample + bottom quintile)
- Time budget per review session (3h? half-day? full-day?)

**§B. Feedback capture schema**
- Per-IMO feedback row: `{slug, ir_team_verdict_enum, ir_team_score_estimate_0_100, ir_team_qualitative_note, predicted_outreach_likelihood_enum, time_to_outreach_estimate_enum, recalibration_signal_flags[]}`
- `ir_team_verdict_enum`: `{strong_pursue, pursue, neutral, deprioritize, do_not_pursue, irrelevant_to_thesis}`
- `recalibration_signal_flags[]`: explicit IR-team-named drivers of disagreement-vs-Phase-3-score (e.g., `series_license_weight_too_low`, `tenure_weight_too_high`, `keyword_match_too_aggressive_no_signal`, `aum_size_should_be_factor`, `geographic_concentration_signal_missing`)
- Per-session feedback: `{session_date, ir_team_reviewer_named, ir_team_role, session_format, sample_reviewed_count, calibration_proposals[], session_observation_notes}`

**§C. Empirical-tuning loop scoring-weights v0.1 → v0.2**
- Calibration delta calculation: for each IMO with IR-team verdict, compute `phase3_score - ir_team_score_estimate` per IMO
- Aggregate calibration evidence per recalibration_signal_flag class (does the IR team agree this is a weight that should change?)
- v0.1 → v0.2 weight proposals: explicit weight-delta per signal-flag class (e.g., `series_license_weight: 0.30 → 0.35; tenure_weight: 0.25 → 0.20; ...`)
- Re-score 99-IMO universe with v0.2 weights + emit `serving/_history/{date}/scoring_v0.2.json` per PRD v0.3 §3.2 Q-B time-travel archive
- IR-team second-pass review on top-30 delta-IMOs (where v0.1 vs v0.2 score-rank changed materially)
- v0.2 RATIFY (if IR-team second-pass GREEN) OR v0.3 third-pass (if material disagreement persists)

**§D. RAVC2-Accept decision tree**
- v0.1 IR-team verdict GREEN-strong → CLOSE-COMPLETE; ship for use; AC5 binding satisfied
- v0.1 IR-team verdict GREEN-conditional + recalibration_signal_flags surfaced → v0.2 calibration iteration; AC5 binding deferred to v0.2 RATIFY
- v0.1 IR-team verdict YELLOW / RED → re-open Phase 3 scoring iteration; AC5 binding deferred; consider Phase 3b portal surface acceleration (richer IR-team workflow)

### 2.2 Thread B: Phase 3 Lambda implementation skeleton (sister to Phase 2A skeleton brief)

Author 3 Lambda skeletons against fixture JSON (mirroring DS~C Phase 2A skeleton brief discipline + DS~A `parse_web_silver.py` + DS~B `score_web_gold.py` pattern):

#### B.1 `data/find/imo/scripts/serving/build_companies_serving.py`

Per PRD v0.6 §4 Phase 3 deliverable 1 (`companies` table):
- Read all `corp/{slug}/gold/web-scrape/{latest-date}/` + `corp/{slug}/gold/linkedin-scrape/{latest-date}/_company_scored.parquet` + `corp/{slug}/gold/job-posting-scrape/{latest-date}/` rollups across 99-IMO universe
- Per-IMO company row: `{slug, name, website, phase1_web_score, phase1_indicator_term_hits[], phase2_eligibility_bool, phase2a_company_score_linkedin, phase2a_leadership_employee_count, phase2a_series_licensed_count, phase2b_hiring_velocity_per_role_class[], phase2b_investment_keyword_hits, company_score_aggregate}`
- `company_score_aggregate` = formula per PRD v0.6 §4 Phase 3 deliverable 2 (per Andrew Q2 ratification post-Phase-1-empirical)
- Write to `s3://opal-data-imo/serving/companies.{json,parquet}` (overwrite-in-place per PRD v0.3 §3.2)

#### B.2 `data/find/imo/scripts/serving/build_employees_serving.py`

Per PRD v0.6 §4 Phase 3 deliverable 1 (`employees` table):
- Read all `corp/{slug}/gold/linkedin-scrape/{latest-date}/employees_scored.parquet` across Phase-2A-subset IMOs
- Optionally join with `corp/{slug}/gold/job-posting-scrape/{latest-date}/` (open-jobs-they-just-posted signal per Andrew Stage 2 Part B framing) — design open question for IR-team feedback
- Per-employee row: `{full_name, company_slug, company_name, title, tenure_years, prior_titles[], location, linkedin_url, series_licenses[], employee_score, ranked_within_company_int}`
- GDPR opt-out propagation: if `opt_out_at` populated in silver/linkedin-scrape/ employees, mark row `opt_out_suppressed=true` + redact contact-detail fields
- Write to `s3://opal-data-imo/serving/employees.{json,parquet}` (overwrite-in-place)

#### B.3 `data/find/imo/scripts/serving/build_scoring_serving.py`

Per PRD v0.6 §4 Phase 3 deliverable 1 (`scoring` table) + §3.2 time-travel archive:
- Emit `s3://opal-data-imo/serving/scoring.{json,parquet}` (current methodology + thresholds + version stamp)
- Emit `s3://opal-data-imo/serving/_history/{run-date}/scoring.{json,parquet}` (append-by-date archive per PRD v0.3 §3.2 Q-B ruling YES-scoring-only)
- Schema: `{methodology_version, weight_employee_tenure, weight_employee_seniority, weight_employee_series, weight_employee_title_keyword, series_license_weights{}, company_score_formula_text, calibration_basis, ir_team_v1_reviewer_named, ir_team_v1_session_date, v1_to_v2_recalibration_deltas[], ratify_class}`
- Joins consumer-readable methodology to specific empirical-tuning round

#### B.4 Shared utilities + unit-tests

- Cost-gate integration: Phase 3 Lambdas check `find-insure-cost-state` DDB on init (minor read; Phase 3 doesn't burn Lusha/Bright-Data credits but tracks own S3 GET + parquet write costs)
- KMS encryption: serving/* is KMS-scope per PRD v0.4 §3.1; Lambda `find-insure-lambda-role` auto-gets Decrypt grant
- Schema version field: `schema_version: "v1.0"` per Q-S1 disposition
- Unit-tests against fixture gold-tier JSON files at `data/find/imo/scripts/serving/tests/fixtures/`
- Empty-IMO + Phase-2A-subset-not-met handling (if `len(phase2a_subset) == 0`: emit serving/employees.parquet as empty + `phase2a_completion_status: subset_not_yet_run`)

## 3. Pre-authoring acceptance criteria (DS~E lane)

### Thread A ACs

- **AC-A1**: `docs/briefs/find-insure-ir-team-feedback-protocol.md` shipped with §A-§D substantive content
- **AC-A2**: Feedback capture schema (per-IMO + per-session) formalized as JSON Schema (canonical at `data/find/imo/scripts/serving/schemas/ir_feedback_schema.json`)
- **AC-A3**: Calibration delta calculation methodology documented + reference implementation `data/find/imo/scripts/serving/calibrate_weights.py` (against fixture v0.1 + fixture IR-team-feedback JSON)
- **AC-A4**: RAVC2-Accept decision tree (§D) cross-referenced into PRD v0.7 candidate §7 AC5 (CTO authors v0.7 amendment post-Brief #3 RAVC2 if IR-team-named-individual identification lands)

### Thread B ACs

- **AC-B1**: `build_companies_serving.py` skeleton + unit-tests against fixture gold-tier JSON
- **AC-B2**: `build_employees_serving.py` skeleton + GDPR opt-out propagation logic + unit-tests
- **AC-B3**: `build_scoring_serving.py` skeleton + time-travel archive emission per PRD v0.3 §3.2 Q-B + unit-tests
- **AC-B4**: Sister-coord with DS~A `parse_web_silver.py` schema + DS~B `score_web_gold.py` gold-tier schema + DS~C `score_linkedin_gold.py` (per Phase 2A skeleton brief) — silver/gold contract documented as ref doc `docs/reference/find-insure-silver-gold-contract.md` (NEW; sister to `lusha-api-v3.md` pattern)
- **AC-B5**: `ds-commit-gate.sh` exit 0 on all new `.py` files (py_compile + ds-precommit-check + ruff per Rule 14 + Rule 15 future-annotations)
- **AC-B6**: Target 35-50 self-test cases per module mirroring DS~A + DS~B + DS~C discipline

NO live S3 cross-IMO scan in scope. NO production-fixture data. All AC pass against synthetic fixture gold-tier JSON.

## 4. Sequencing — fully parallel to Phase 1 + 2A critical paths

- **NOW (this brief landed; COO greenlit 20:03Z)**: DS~E can start authoring upon TO dispatch from ws COO
- **Phase 1 RAVC2-Accept lands (~20:00-20:30Z)**: Thread A protocol design unchanged; Thread B skeleton consumes Phase 1 gold-tier (now-real values; previously fixture)
- **Phase 2A live-execution + first-pass empirical (~22:00Z-tomorrow)**: Thread B consumes Phase 2A gold-tier; Thread A IR-team-feedback-elicitation session schedulable
- **AC5 RAVC2-Accept window (~tomorrow-multi-day)**: Thread A IR-team review fires; Thread B serving artifacts read by IR-team

Net throughput gain: when Phase 1 + 2A converge, Phase 3 Lambda wire-up + IR-team-elicitation-session is **substrate-ready** in minutes-not-hours.

## 5. Routing

- **Primary**: COO TO decomposition for DS~E lane. Suggested split:
  - `FIND_INSURE.021` Thread A IR-team feedback protocol design + schema + calibration reference impl
  - `FIND_INSURE.022` Thread B Phase 3 Lambda skeleton trio + silver-gold contract ref doc
  - OR single bundled `FIND_INSURE.021` covering both threads (DS~E discretion)

- **CC sister-coord**: DS~A + DS~B + DS~C — silver-gold contract ref doc emerges from cross-lane substrate agreements; DS~E owns authoring but should consult sisters on schema-binding fields

- **CC**: Andrew — AC5 ADDITIVE-1 IR-team-named-individual identification routing question surfaces in §A of Thread A protocol design. Non-urgent (pre-Phase-3-RAVC2-Accept gate); Brief #3 can land + AC-A1 ship without resolution

## 6. Why now

Per Andrew direct 19:50Z pace-pickup + COO 20:03Z greenlight:

- DS~E STANDBY-PURE ~3-4h wall is unacceptable
- Phase 1 RAVC2-Accept + Phase 2A execution are imminent (next ~30min-2h)
- Phase 3 substrate authoring NOW enables wire-up-in-minutes when upstream gates clear
- AC5 RAVC2 mechanism is the project-CLOSE-COMPLETE gate; spec-author work pre-empirical-IR-team-session prevents post-hoc-rush

— ws CTO 2026-05-27T~20:08Z

CC: 2.0.0_SA_COO (TO author lane) + DS 0.1.0~A + ~B + ~C (sister-coord on silver-gold contract) + 0.0.0_AB_MSTR (PRD pipeline visibility per /govern)
