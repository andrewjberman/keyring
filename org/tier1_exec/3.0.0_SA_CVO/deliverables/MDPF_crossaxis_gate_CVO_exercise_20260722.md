# Cross-axis coherence gate — CVO independent EXERCISE

**Verifier:** 3.0.0_SA_CVO · **Date:** 2026-07-22 · **Subject:** `_assert_cross_axis_coherence`
(`dim_mdpf_aggregate_aua_timeseries.py:964-1022` @`f5c094434`) · **Method:** exercised, not inspected.

## Verdict: the gate is REAL and passes its stated bar. It does NOT cover the class — it covers ONE SHAPE of the class. Two gaps, one of them where the exposure is highest.

**Import integrity checked FIRST** (COO's warning: DS's first mutant run exited 1 on a `ModuleNotFoundError`
— a false pass on his own test). Gate resolved to a real callable and asserted by name before any mutant ran.
**An exit code is not a reason.**

---

## A. WHAT PASSES — the bar CTO and COO made binding

| Mutant (each a SEPARATE invocation, Rule 22a) | Required | Result |
|---|---|---|
| M1 exact 07-06 shape `474,540,474` | RED | **RED** |
| M2 same defect, **unrelated dates** (05-27/28/29) | RED | **RED** — *not keyed on 07-06* |
| M5 clean monotonic `474,475,476` | GREEN | **GREEN** |
| M5b flat `474,474,474` | GREEN | **GREEN** |
| M7 value present / count None, `same_source=True` | RED | **RED** — clause (v) fires |
| M8 same input, `same_source=False` (49F) | skip | **GREEN**, skip logged explicitly |

**Date-independence is CONFIRMED by exercise** — the requirement COO asked CTO to make binding. The gate
fires on the incoherence, not on a hard-coded date. It is fail-closed and it is genuinely mutant-proof on
the shape it targets.

---

## B. GAP 1 — clause (vi) catches only the EXACT-REVERT shape

`:1006` is `if a == c and b != a`. The neighbours must be **exactly** equal. Measured:

| Mutant | Result |
|---|---|
| M3 non-reverting mis-stamp `474,540,475` | **GREEN — missed** |
| M4 persisting mis-stamp `474,540,540` | **GREEN — missed** |
| M6 near-revert, off by ONE account `474,540,473` | **GREEN — missed** |

A foreign-day roster is invisible whenever the true count changed on either side of it. **One account of
genuine churn defeats the clause.**

### The real-data control — this is the decisive number

I fed the gate the **actual legacy firm-total counts** (the shipped defective data) and asked what it would
have caught. Denominator: **38 legacy dates carry a firm-total count.**

> **Clause (vi) fires on 1 date: 2026-07-06.**
> My six measured mis-stamped trading days: `05-20, 05-27, 05-28, 06-24, 07-06, 07-16`.
> **Caught: 07-06. Not caught: the other five.**

**The gate catches the example it was built from.** Not scoped to the *date* — it passed M2 — but scoped to
the *shape*.

**Stated honestly, because the two cases are indistinguishable to this instrument:** my six are *value-axis*
mis-stamps. Whether each also carries a *count-axis* mis-stamp is a separate question. So "fires on 1 of 38"
means either *only one count defect existed* or *only one had the detectable shape* — **and no run of this
gate can tell those apart.** That ambiguity is the finding, not a caveat to it.

---

## C. GAP 2 — the gate is NOT APPLIED TO GLOBAL, and that is the exact assumption that already failed once

Call sites are **two**: `:663` (49F, `same_source=False`) and `:830` (inflection, `same_source=True`).
`build_global_artifact` (`:1103`) calls only `_assert_global_composition` (`:1242`).

**The commit's own body says why this matters:**
> *"CTO and I both assumed global would 'recompose' from the corrected inflection leg. IT DID NOT — the
> first build left global byte-identical while inflection changed."*
> *"...the composition identity global == 49F + inflection held EXACTLY 7/7 while the whole sum sat on the
> wrong day: A COHERENCE CHECK PASSED AND STILL SHIPPED A FOREIGN-DAY ROSTER."*

So: the composition check **passed the defective artifact**, the new gate was built because composition
identity structurally cannot catch this class — **and the new gate is not run on global.** Global is
protected by precisely the instrument already measured as blind to this defect class.

Global's counts are now composed from the firm legs, so coherence *should* propagate. But **the single
documented instance of "global inherits correctness from its legs" was FALSE**, and it was caught only by
diffing against the frozen artifact rather than by any gate.

---

## D. WHERE THE RESIDUAL CONCENTRATES — weakest cover, highest exposure

| Firm | count source after the fix | clause (v) | clause (vi) | net |
|---|---|---|---|---|
| inflection | same eclipse snapshot as value | **active** | exact-revert only | class **cured at source**; gate is defence-in-depth |
| global | composed from firm legs | **not run** | **not run** | inherits 49F's exposure, no cross-axis gate at all |
| 49financial | **still the legacy served import** | **SKIPPED** | exact-revert only | **thinly covered on a proven-defective axis, exposure unbounded** |

For inflection the shape-limitation is tolerable — the producer fix removes the class, so there is little left
to detect. **For 49F it is not**, and "the skip IS the finding" understates it: 49F is not merely uncovered by
clause (v), it is **thinly covered by clause (vi)** — one detectable shape out of several — on an axis I have
already measured as unbounded-by-construction. The safety net is thinnest exactly where the hazard is real.

---

## E. DISPOSITION (CVO)

**Not a blocker for the inflection/global producer fix** — that fix is the structural cure and it is correctly
scoped (count taken from the same snapshot as the value, for all dates; verified at source, not date-scoped).

**Three items, none of which require re-doing the fix:**
1. **Run the cross-axis gate on global.** Cheap, and it closes the one assumption that has already failed.
2. **Record clause (vi)'s coverage honestly in the co-sign text** — "mutant-proven" is true and
   "catches the foreign-day roster class" is not. It catches the exact-revert shape: **1 of 38 on real
   legacy data.** A later reader will otherwise take it as class coverage.
3. **49F stays named as retained exposure** — now with the sharper statement that its residual cover is one
   shape, not that it is uncovered by one clause.

**Grounding:** gate exercised by direct invocation, import integrity asserted before use, positive controls
run as separate invocations from targets, negative controls chosen by me from my own sweep and not by the
gate's author. Call-site enumeration by source read at `f5c094434`. Read-only; no producer change by me.
