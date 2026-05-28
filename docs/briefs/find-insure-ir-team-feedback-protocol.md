# FIND_INSURE IR-team Feedback Protocol — AC5 RAVC2 mechanism

| | |
|---|---|
| **Author** | 0.1.0_DS_MarketIntelligence~E |
| **Date** | 2026-05-28 |
| **Status** | DRAFT v0.1 — Thread A deliverable of FIND_INSURE.021 |
| **Parent PRD** | `docs/architecture/FIND_INSURE.md` v0.7.1 |
| **Authority** | Brief `b67ad03ec` Thread A + Andrew sovereign 2026-05-27T~19:50Z pace-pickup + ws COO greenlight 20:03Z |
| **Paired artifacts** | `data/find/imo/scripts/serving/schemas/ir_feedback_schema.json` (AC-A2) + `data/find/imo/scripts/serving/calibrate_weights.py` (AC-A3) |

---

## 0. Purpose

This document is the canonical **AC5 RAVC2 mechanism** per PRD v0.7.1 §7 AC5: IR-team review of the Phase 3 serving tables produces a verdict — either *"rankings agree with our judgment, ship for use"* (CLOSE-COMPLETE) or *"rankings need recalibration, here is the feedback"* (re-open Phase 3 scoring iteration). It defines (A) how feedback is elicited, (B) how it is captured as structured data, (C) the empirical-tuning loop that converts feedback into scoring-weight deltas, and (D) the decision tree that maps an IR-team verdict to a project-close disposition.

**Scope note (v0.1):** This is the protocol *design* — methodology + schema + reference calibration impl. It does NOT schedule a live IR-team session (gated on Phase-3-RAVC2-Accept window per PRD §11) and does NOT identify the IR-team-named individual (ADDITIVE-1 standing; surfaced in §A as an open routing question, not gated by its answer).

---

## §A — Feedback elicitation methodology

### A.1 IR-team-named-individual identification (ADDITIVE-1 — OPEN routing question)

**Open question surfaced for Andrew (NON-URGENT; pre-Phase-3-RAVC2-Accept gate):** Who is the IR-team validator?

The AC5 verdict has authority only if rendered by a reviewer with genuine IMO-outreach domain judgment. Candidate reviewer-profile criteria (Andrew to ratify the actual named individual at the Phase-3-RAVC2-Accept window):

- **Domain experience:** has personally run (or directly supervised) IMO / RIA / insurance-carrier outreach campaigns; can judge "would I actually call this firm" against a ranked list.
- **Thesis alignment:** understands the asset-management-transition thesis (the project's reason-for-being) — that the target is insurance/annuity IMOs *building or expanding* an asset-management line, not pure-annuity carriers.
- **Independence:** not the same person who authored the scoring weights (preserves verifier-vs-author separation; mirrors the CVO self-validation-mitigation discipline at the human layer).

Until Andrew names the individual, AC5 cannot bindingly CLOSE-COMPLETE; the protocol + schema + calibration impl are nonetheless fully authorable + testable against synthetic fixtures (this deliverable).

### A.2 Review session structure

Three candidate formats, ranked by recommended-default:

| Format | Description | When to use |
|---|---|---|
| **Hybrid (RECOMMENDED default)** | Async spreadsheet/portal pre-review of the full ranked list (reviewer annotates at own pace) + a live 60-90min walkthrough session on the disagreement set (IMOs where reviewer verdict diverges from Phase-3-rank) | Default — captures breadth (async) + depth (live on the contested cases) |
| Sit-with-IR-rep (live walkthrough) | Analyst sits with reviewer, walks the ranked list top-to-bottom live | High-touch; good for v0.1 first-pass when the methodology itself is being sanity-checked |
| Async spreadsheet/portal-only | Reviewer annotates the exported table independently; no live session | Lowest-cost; good for v0.2+ second-pass confirmation rounds once methodology is trusted |

### A.3 Sample size

The full universe is ~99 IMOs. Two review-coverage strategies:

- **Full-universe review** (preferred for v0.1 first-pass): reviewer renders a verdict on all ~99. Highest-confidence calibration basis; ~half-day time budget.
- **Stratified sample** (acceptable for v0.2+ confirmation passes): top quintile (top ~20 by `company_score_aggregate`) + a random ~20 from the middle + bottom quintile (~20). Catches both false-positives (high-rank-but-reviewer-deprioritizes) and false-negatives (low-rank-but-reviewer-pursues) without full-universe cost.

### A.4 Time budget per session

- v0.1 first-pass full-universe hybrid: ~half-day (async pre-review ~2-3h reviewer-own-time + live walkthrough 60-90min on disagreement set).
- v0.2+ stratified confirmation: ~60-90min total.

---

## §B — Feedback capture schema

Two record types. Canonical JSON Schema at `data/find/imo/scripts/serving/schemas/ir_feedback_schema.json` (AC-A2); this section is the human-readable spec.

### B.1 Per-IMO feedback row

```
{
  "slug": "<imo-slug>",
  "ir_team_verdict_enum": "<one of: strong_pursue | pursue | neutral | deprioritize | do_not_pursue | irrelevant_to_thesis>",
  "ir_team_score_estimate_0_100": <int 0-100>,
  "ir_team_qualitative_note": "<free text>",
  "predicted_outreach_likelihood_enum": "<one of: high | medium | low | none>",
  "time_to_outreach_estimate_enum": "<one of: immediate | this_quarter | this_year | someday | never>",
  "recalibration_signal_flags": [ "<zero or more signal-flag enum values, see B.3>" ]
}
```

`ir_team_verdict_enum` semantics:
- `strong_pursue` — clear high-conviction target; would call this week.
- `pursue` — solid target; would call this quarter.
- `neutral` — could go either way; needs more signal.
- `deprioritize` — weak target; bottom of the list.
- `do_not_pursue` — not a target; would not call.
- `irrelevant_to_thesis` — wrong universe entirely (e.g., a pure-annuity carrier with no AM-transition signal that scored high on vocabulary noise — the exact false-positive class the v0.7.1 class-diversity gate addresses).

### B.2 Per-session feedback record

```
{
  "session_date": "<YYYY-MM-DD>",
  "ir_team_reviewer_named": "<name | PENDING-ANDREW per §A.1>",
  "ir_team_role": "<role/title>",
  "session_format": "<one of: hybrid | live_walkthrough | async_only>",
  "sample_reviewed_count": <int>,
  "sample_strategy": "<one of: full_universe | stratified>",
  "calibration_proposals": [ "<zero or more free-text or structured weight-change proposals>" ],
  "session_observation_notes": "<free text>",
  "scoring_methodology_version_reviewed": "<e.g. v0.2 — the scoring-weights version the reviewed tables were generated under>"
}
```

### B.3 `recalibration_signal_flags` enum (IR-team-named drivers of disagreement)

Each flag is an explicit, named hypothesis about *which scoring lever is mis-set*. These map directly to scoring-weights config keys, so `calibrate_weights.py` can aggregate evidence per lever.

| Signal flag | Maps to config lever | Direction implied |
|---|---|---|
| `series_license_weight_too_low` | `employee_score.weights.w_series` / `series_license_weights` | increase |
| `series_license_weight_too_high` | same | decrease |
| `tenure_weight_too_high` | `employee_score.weights.w_tenure` | decrease |
| `tenure_weight_too_low` | same | increase |
| `seniority_weight_too_high` | `employee_score.weights.w_seniority` | decrease |
| `seniority_weight_too_low` | same | increase |
| `keyword_match_too_aggressive_no_signal` | `employee_score.weights.w_keyword` / `title_keyword_set` | decrease |
| `keyword_match_too_weak` | same | increase |
| `aum_size_should_be_factor` | NEW lever proposal — company-score AUM-band term | add lever |
| `geographic_concentration_signal_missing` | NEW lever proposal — geo term | add lever |
| `phase1_web_signal_overweighted` | `company_score.weights.w_phase1_signal` | decrease |
| `phase1_web_signal_underweighted` | same | increase |
| `hiring_signal_overweighted` | `company_score.weights.w_hiring_signal` | decrease |
| `hiring_signal_underweighted` | same | increase |
| `annuity_vocabulary_false_positive` | `term-taxonomy annuity-product-vocabulary` class-diversity gate (already addressed v0.7.1; flag confirms gate efficacy) | confirm gate / tighten |

The enum is **extensible**: a reviewer-named driver not in this list is captured as a free-text `calibration_proposals[]` entry on the session record and promoted to a named flag in the next protocol version if it recurs.

---

## §C — Empirical-tuning loop (scoring-weights vN → vN+1)

The loop converts the captured feedback into a concrete, auditable weight-delta proposal. Reference implementation: `calibrate_weights.py` (AC-A3).

### C.1 Per-IMO calibration delta

For each IMO with an IR-team verdict, compute:

```
calibration_delta[slug] = phase3_company_score_0_100[slug] - ir_team_score_estimate_0_100[slug]
```

- Positive delta → Phase-3 scored the IMO **higher** than the IR team (potential over-firing).
- Negative delta → Phase-3 scored it **lower** (potential under-firing / missed signal).
- |delta| near 0 → agreement.

### C.2 Aggregate evidence per recalibration_signal_flag class

For each `recalibration_signal_flag`, aggregate across all IMOs that carry that flag:
- Count of IMOs flagged.
- Mean + median signed `calibration_delta` for the flagged subset.
- Whether the delta direction is consistent with the flag's implied direction (B.3 table).

A flag is **actionable** when: (a) it is named on ≥ a quorum of IMOs (default quorum = 3, or ≥5% of reviewed sample, whichever is larger), AND (b) the mean calibration_delta direction agrees with the flag's implied direction. This guards against single-IMO idiosyncratic feedback driving a global weight change.

### C.3 vN → vN+1 weight proposals

For each actionable flag, propose an explicit weight delta. Default step size is conservative (±0.05 on a normalized 0-1 weight; ±0.05 on a per-license weight) so a single calibration round cannot swing the model violently. After applying per-flag deltas, **re-normalize** the affected weight group so `weights_sum_check == 1.00` is preserved (employee_score weights + company_score weights are each a normalized simplex).

Example proposal block (illustrative; produced by `calibrate_weights.py`):

```
series_license_weight_too_low (actionable: 6 IMOs, mean delta -14):
  employee_score.weights.w_series: 0.30 -> 0.35
tenure_weight_too_high (actionable: 4 IMOs, mean delta +9):
  employee_score.weights.w_tenure: 0.25 -> 0.20
[re-normalize employee_score.weights to sum 1.00]
```

### C.4 Re-score + archive

- Re-score the ~99-IMO universe with the vN+1 weights.
- Emit `serving/_history/{run-date}/scoring_v{N+1}.json` per PRD v0.3 §3.2 Q-B time-travel archive (scoring artifact is the only append-by-date class; methodology changes are intentional + citeable).
- Diff vN vs vN+1 rank order; surface the **top-30 delta-IMOs** (where rank changed materially) for an IR-team second-pass.

### C.5 Second-pass + ratify

- IR-team second-pass review on the top-30 delta-IMOs only (cheap; targeted).
- vN+1 RATIFY if the second-pass is GREEN (reviewer agrees the re-ranked set is better).
- vN+2 third-pass if material disagreement persists (rare; signals the disagreement is structural, not a weight-tune — escalate to a methodology review, not another weight round).

### C.6 Version-numbering note (v0.7.1 reality)

The brief §C describes a v0.1 → v0.2 transition. As of `4f557336b` the scoring-weights config is already at **v0.2** — but that bump was the PRD-v0.7.1 class-diversity-multiplier-cap change (1.5 → 1.2) + term-taxonomy annuity-class addition, which preserved the employee/company weights **verbatim from v0.1**. The IR-team empirical-tuning loop targets the **employee + company scoring weights** (the O-2 open items), so the first IR-driven weight bump will produce **scoring-weights-v0.3.json**. `calibrate_weights.py` is written version-agnostic: it reads the current weights file, computes deltas, and emits the next version — so the v0.7.1 version-numbering reality is handled without protocol change.

---

## §D — RAVC2-Accept decision tree

The AC5 verdict maps to a project-close disposition:

```
IR-team v1 verdict
├── GREEN-strong  (reviewer: "rankings agree, ship for use"; no actionable recalibration flags)
│       => CLOSE-COMPLETE. AC5 binding satisfied. Phase 3 ships for IR-team use. Project close.
│
├── GREEN-conditional  (reviewer broadly agrees BUT actionable recalibration_signal_flags surfaced)
│       => v(N+1) calibration iteration (§C). AC5 binding DEFERRED to v(N+1) RATIFY.
│          Run calibrate_weights.py -> re-score -> top-30 second-pass -> ratify.
│
└── YELLOW / RED  (reviewer: "rankings do not match my judgment; material disagreement")
        => RE-OPEN Phase 3 scoring iteration. AC5 binding DEFERRED.
           Consider Phase 3b portal-surface acceleration (richer IR-team workflow:
           interactive filtering / drill-down / signal-inspection) if the disagreement
           is rooted in the reviewer needing more than a static ranked table to judge.
```

**AC-A4 cross-reference:** this decision tree is the candidate substance for PRD §7 AC5. ws CTO folds it into a PRD amendment cycle (CTO scope) at the moment the IR-team-named-individual identification (§A.1) lands and the AC5 elicitation session is schedulable. This deliverable supplies the decision-tree text; the PRD-amendment authoring is CTO's per the verifier-gates-fixer separation.

---

## §E — Sister-coordination

- **DS~A / DS~B / DS~C:** consume `calibrate_weights.py` output if a vN → vN+1 weight amendment fires. The calibration deltas reference scoring-weights config keys they author against (DS~B score_web_gold.py reads term-taxonomy + scoring-weights; DS~C LinkedIn gold reads employee weights). CC them on any actionable calibration proposal so downstream gold re-scoring stays in lockstep.
- **DS~E (self):** scoring-weights-v0.2.json + term-taxonomy-v2.json are the current config-of-record (`4f557336b`); calibrate_weights.py reads these as the vN baseline.

---

## §F — Open items

| Item | What | Route | Trigger |
|---|---|---|---|
| IR-team-named-individual | Who validates (§A.1) | Andrew sovereign | Phase-3-RAVC2-Accept window |
| Live session scheduling | When the elicitation session runs | Andrew + ws COO | Phase 1 + Phase 2A converged + tables populated |
| AC-A4 PRD §7 AC5 fold | Decision-tree → PRD amendment | ws CTO | post-IR-team-named-individual + AC5 elicitation schedulable |

— 0.1.0_DS_MarketIntelligence~E 2026-05-28 (FIND_INSURE.021 Thread A AC-A1)
