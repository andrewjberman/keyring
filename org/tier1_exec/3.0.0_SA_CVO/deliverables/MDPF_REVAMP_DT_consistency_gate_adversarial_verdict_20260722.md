# CVO Adversarial Verify — DT internal-consistency gate — ACCEPTED-CVO (2 items)

**Verifier:** 3.0.0_SA_CVO (main CVO) · **Date:** 2026-07-22 · **Target:** `mdpf_parity_check.py --consistency` @3e557741e (0.2.0_DT_PortfolioAnalytics)
**Context:** Layer 2 of the MDPF re-flip defense-in-depth (DS producer-validate / DT harness / CVO Layer-3 re-derive). DT requested adversarial refutation (builder cannot certify own instrument).

## Verdict: ACCEPTED-CVO as Layer 2. Item 1 CLOSED+re-verified (@f64797340); Item 2 routed to DS.

**Grounding = exercised, not read:** DT `--self-test` (20+ mutant clauses) PASS + ruff clean; live `--consistency --published-prefix gold/mdpf_revamp` (staged) and `--consistency --served` (legacy) reproduced (both rc=1); a **generated** boundary/edge mutation sweep against `_consistency_violations`/`_crossfirm_violations` (a generated control measures the instrument; a hand-chosen one measures the author).

**Vintage note (retrieval discipline):** the verified commit was `3e557741e`. Item 1 (NaN) was a real false-PASS at that vintage; DT fixed it in `f64797340` mid-review. A transient contradiction in my own harness (NaN "MISS" then "caught" across two runs) was the file advancing `3e557741e -> f64797340` between runs — *pin the vintage, not just the file*. Confirmed via `git show 3e557741e` (no guard) vs working tree (guard present).

## The 4 refutation targets

| Target | Result |
|---|---|
| **Q1 tolerance ($1.00 abs / $1.01 floor)** | **DEFENSIBLE.** Generated sweep: RED iff \|diff\|>$1.00, symmetric both signs (green@0.999, red@1.001). Accounting identity; $1 sits ~6 orders above float64 noise at $1e9. No matters-at-scale defect below $1. Absolute (not relative) tol is correct for an exact identity. |
| **Q2 discrimination** | Discriminates cleanly at the boundary. **ONE break constructed → ITEM 1:** a **non-finite (NaN)** component → `diff=nan` → `abs(nan)>tol` is **False** → MISSED and counted checked-clean (inf IS caught). `json.loads` parses `NaN` by default, so a producer NaN slips a silent false-PASS on the gated axis — violates the gate's own UNCHECKABLE≠PASS. |
| **Q3 cross-firm companion** | **KEEP — not scope creep.** It is the LOCALIZER (CROSSFIRM_PASS both sides pins the P0 to `opal_aggregate` composition, not the rollup) and closes part of the per-firm blind spot: a compensating error (model+X/non_model−X, total unchanged) **MISSES** the per-firm total identity (confirmed) but a firm/rollup shift is caught cross-firm. Per-firm + cross-firm both green ≡ my Layer-3 component re-derive transitively. **Residual frontier (out of scope, name it):** a compensating error identical at firm AND global level evades both — only a deeper-source (cohort/account) re-derive catches that. |
| **Q4 PARTIAL_NULL over-fire?** | **NO — catching a real REVAMP REGRESSION → ITEM 2.** Staged inflection 2026-05-21 = custody $202.04M, model/non_model **None**; legacy served 2026-05-21 HAS model $93.08M + non_model $105.63M (ties custody $198.72M). The revamp DROPPED a decomposition the legacy serves. A named exemption would HIDE it (opposite of cohort_provenance, which is genuinely revamp-only/FE-unconsumed/lineage-verified). 2026-06-01/07-01 = served-ABSENT, custody-only → suspect, not honest. |

## The 2 items

1. **[DT — CLOSED @f64797340, CVO re-verified]** `NON_FINITE` guard added (`_is_finite_num`), verdict before the diff test, `n_checked` NOT inflated, and extended to the **cross-firm** roll-up (DT's own catch — I flagged only per-firm; `sum(parts)` with a NaN is NaN, same false-clean). CVO re-verify @f64797340: nan/inf/-inf/str/**bool** × all 3 fields → NON_FINITE with `checked=2` (15/15), finite control no over-fire, staged global unchanged (421 SUM_MISMATCH — no regression). bool→NON_FINITE is deliberate (a bool is not a dollar amount; `True+1` would evaluate silently). DT self-test MUTANT-3c PASS. **Item 1 satisfied → DT's gate cleared to be standing.**
2. **[DS, re-stage]** RESTORE inflection 2026-05-21 model/non_model decomposition (re-derive from source — do not copy legacy dollars; revamp custody $202.04M differs from legacy $198.72M by ~$3.3M). Explain/​re-source 06-01/07-01. Do NOT exempt or zero-fill. Distinct from + in addition to the enterprise-composition all-421-dates fix.

## DT's 4 findings — all independently CONFIRMED (re-derived, not taken on trust)

- Rollback does NOT clear the bug: served global FAILS 429/429 from 2024-11-01 (predates the revamp).
- Firm-sum CORRECT: CROSSFIRM_PASS both sides → defect is `opal_aggregate_aua` composition, not the rollup.
- Hole range $64.4M–$203.8M; **median independently = $163,093,838.09** (DT's "$163.1M", exact).
- Served 49f fails 2025-12-26 (−$43,157,544.80); staged 49f PASSES → the revamp fixes it.

## Battery status

DS producer-validate + DT harness (post NaN-guard) + CVO Layer-3 re-derive (`@f3c202256`) — all full 421-date series, per-date, all-firm, mutant-proven, printed-denominator. **CVO Layer-3 live re-derive HELD** for DS's corrected re-stage (enterprise composition all-dates + 05-21 decomposition restore); re-run on the re-stage. RV-0054 stays post-re-land.

*Evidence harness: `deliverables/mdpf_revamp_cvo_adversarial_dt_gate_harness.py` (reproducible).*
