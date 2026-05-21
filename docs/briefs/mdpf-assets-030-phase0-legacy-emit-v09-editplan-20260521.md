# MDPF_ASSETS.030 Phase 0 — legacy-emit v0.9 re-scope: edit plan + live-page delta

**Agent:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-05-21
**TO:** MDPF_ASSETS.030 (GO'd by COO~B; amendment A1 — Phase 5 historical backfill)
**Routed to:** 2.0.0_SA_COO~B (direct) + 1.0.0_SA_CTO~B (separate send)
**Non-mutating:** Phase 0 — analysis only.

---

## TL;DR

- The legacy emitter is on the **CEO-direct 2026-05-19 "broader" full-BD-book
  basis** (`method=ceo_directive_20260519_v1`), not a generic stale basis. It
  computes 1b via `compute_49f_broader_custody` (no custodian filter — full
  Black-Diamond book) and **explicitly overrides** the platinum partition's
  Schwab-only 1b. v0.9 (Andrew Mandate Change 3, 2026-05-20) supersedes it.
- **Live-page delta: −$150.18M** on the headline `enterprise_total`
  (2026-05-20: $1,898.21M → $1,748.03M) = −$91.3M (Cohort 0 out of headline)
  + −$58.9M (broader → Schwab 49F).
- The re-scope is **contained**: .028 + .029 already made the platinum
  partitions v0.9, so the emitter inherits v0.9 by *reading them* — the edit is
  to **stop overriding**, drop Cohort 0 from the headline, retag.
- **aum-timeseries.json carries no 1b-basis-dependent field** (model-side only)
  — verify-only for the v0.9 re-scope, per CTO~B's precision (one caveat, §4).

---

## (a) Current-state finding

`build_legacy_compat_emit.py` emits `non_model_assets.json` (the live Model
Portfolios page's source). Its CUTOVER_DATE-onward (2026-01-16+) logic:

1. `derive_49f_from_platinum()` reads the platinum `aggregate_aua/{date}.json`
   partition — extracts 1a, 1b (`non_model_aua`), by_model, etf_public_residual.
2. **It then OVERRIDES** 1b: `compute_49f_broader_custody()` re-sums BD
   `silver/allocations` with **no custodian filter** (Schwab + ByAll Accounts +
   Fidelity IWS + DST + unmatched) minus liabilities/misc — the CEO-direct
   2026-05-19 "broader" methodology. `1b = broader_custody − 1a − 1c`.
3. `enterprise_total = total_49f + inf_2a + cohort_0` — **Cohort 0
   (`etf_public_residual`) IS currently IN the headline.**

So the live page is on basis (2) of the PRD history (full-BD-book ~$1.81B-class)
+ Cohort 0 in the headline. v0.9 = basis (3): full **Schwab** 49F book, Cohort 0
audit-only. The 2026-05-19 "broader" CEO-direct predates Andrew's 2026-05-20
Mandate Change 3 (PRD v0.9) by one day — v0.9 is the superseding ruling, and
.030 is the TO to land it.

## (b) The v0.9 edit plan

| # | Edit | Detail |
|---|------|--------|
| **A** | Remove the broader-custody override | Delete `compute_49f_broader_custody()` + its 2 call sites (main loop + extension leg). Use the platinum partition's v0.9 `non_model_aua` (1b) + `sma_aua` (1c) directly — `.028`/`.029` already made every partition v0.9, so the emitter inherits the v0.9 1b by simply *reading* it. `total_49f = 1a + 1c + 1b`. |
| **B** | Cohort 0 out of the headline | `enterprise_total = total_49f + inf_2a` (drop `+ cohort_0`, line 616). `etf_public_residual` stays as the audit-only field (line 628). Adjust the `non_model_aum` derivation accordingly. |
| **C** | Retag | `method`/`methodology_version` → `v0_9` (was `ceo_directive_20260519_v1`). |
| **D** | Remove dead constants | `LIABILITY_TYPES_BROADER`, `MISC_ACCOUNT_TYPES_BROADER`, `MISC_ACCOUNT_NAME_PATTERN` — used only by the removed function. |
| **E** (Phase 5) | Extend the rebuild range | `CUTOVER_DATE` is `2026-01-16`; the emitter passes through pre-CUTOVER verbatim. `.029` backfilled the platinum partitions to **2025-12-23**. To bring the full `.029` range onto v0.9 in `non_model_assets.json`, move `CUTOVER_DATE` → `2025-12-23` (or extend the rebuild window) so the emitter rebuilds the full `.029` span from the v0.9 partitions. |

**Re-confirmed vs the predecessor .026 findings (now on the v0.9 basis):**
- The emitter's 1b is **already SMA-exclusive** at source (`1b = custody − 1a −
  sma_aua`, line 499) — structurally identical to v0.9's `1b = Schwab_whole −
  1a − 1c`. Only the custody *input* changes (broader → Schwab). No SMA-term
  rework.
- Cohort 0 **is** in the headline today (line 616) — Edit B removes it, per
  v0.9 / the .024-line ruling. (The .026-era finding holds.)

## (c) Live-page delta

| date | field | current (live) | v0.9 | delta |
|------|-------|----------------|------|-------|
| 2026-05-20 | `enterprise_total` | $1,898,213,922.32 | $1,748,030,393.45 | **−$150,183,528.87** |
| 2026-05-20 | `model_aum` | $1,349,272,608.00 | $1,349,272,608.00 | $0 (model side unchanged) |

Decomposition of the −$150.18M:
- **−$91.34M** — Cohort 0 (`etf_public_residual` $91,335,123.78) removed from
  the headline (Edit B).
- **−$58.85M** — the broader → Schwab 49F re-scope (Edit A): the full-BD book
  (ByAll Accounts / Fidelity IWS / DST / unmatched) is no longer counted.

**This is a large, deliberate move of a live CEO-facing number** (~$150M down).
COO~B's GO resolved the `<live_page_note>` — v0.9 is Andrew's final ruling, no
separate Andrew sign-off gate — so this is documented, not a blocker; flagging
the magnitude explicitly per the TO's quantify-the-delta requirement.

## (d) CTO~B precision — aum-timeseries.json basis-dependence

`build_legacy_compat_emit.py` co-writes `aum-timeseries.json`. Its content:
`aggregate[].aum = 1a + inflection_2a` and `by_model[]` = per-model 1a +
inflection per-model — **model-side only. It carries no 1b / custody /
non-model field.** v0.9 changed only the 1b basis → **aum-timeseries.json is
NOT basis-dependent on the v0.9 re-scope → VERIFY-ONLY, no historical write
for the basis change.**

**One caveat for CTO~B:** re-running the emitter for Phase 5 reads 1a from the
now-`.029`-rewritten platinum partitions — so it would refresh
`aum-timeseries.json`'s 1a for 2026-05-15/18/19 to the `.029`-**smoothed**
values. That is a *1a-smoothing* refresh, not a 1b-basis change — and it is
**desirable** (the chart's model layer should match the smoothed platinum
series; leaving aum-timeseries.json with the raw 1a spike would re-introduce
the anomaly in the chart's model layer). Recommend it be in scope as a
consistency refresh. CTO~B's call.

## (e) Phase 5 — the historical backfill is near-automatic

Once Edit A removes the override, the emitter rebuilds `non_model_assets.json`'s
`time_series` for the whole CUTOVER-onward range *from the v0.9 platinum
partitions*. So Phase 5 ≈ "run the re-scoped emitter" — it re-materializes the
historical 1b series on v0.9 with no extra logic. Edit E extends CUTOVER back to
2025-12-23 so the full `.029` range is covered. Each historical
`non_model_assets.json` row then reconciles against its `.029`-rewritten v0.9
`aggregate_aua/{date}.json` partition by construction (same 49F source) — AC5.
Phase 5 gates on `.029` Phase 1 (COMPLETE) — clear to proceed after Phases 0-4.

## Proposed sequence

Phases 1-4 (daily-forward re-scope: Edits A-D) → Phase 2 reconciliation
to-the-cent vs the .028 v0.9 platinum → Rule 13 deploy → Phase 5 (Edit E +
re-run, historical `non_model_assets.json` on v0.9) → RAVC2 to COO~B CC CTO~B.

**Phase 0 deliverable — this brief. Proceeding to Phase 1** (the edits are
contained + the methodology is fully Andrew-ruled; no Phase-0 hard-stop in the
TO). Flag now if the −$150M live-page delta warrants a pause.
