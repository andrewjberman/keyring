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

---

# ADDENDUM (same session) — verified against the STAGED rebuild, and a stop-work result

## F. DS's fix INDEPENDENTLY VERIFIED on the staged artifacts (`5e7b684d` / `08f9720e`)

- **07-06 firm-total count 540 -> 474.** The excursion is gone; the 540 now sits on **07-10**, where the
  reclassification actually happened. Count axis and value axis now agree about which day it is.
- **Presence matrix perfect:** 421 dates carry BOTH, zero value-only, zero count-only.
- **REGRESSION CONTROL — the result that licenses believing the GREEN:** the OLD pinned artifact
  (`cec5a0d6`) goes **RED, 2737 presence disagreements across 391 dates.** *It is not a gate that only
  passes.*

## G. THE GLOBAL RED — and what the 20 dates turned out to be

Running the gate on staged global at `same_source=True`: **RED, 94 per-band disagreements across 20 dates.**
Those 20 dates are:

    2025-12-24, 12-30, 12-31, 2026-01-02, 02-02, 03-02, 04-01, 05-01, 06-01, 06-08,
    06-26, 06-29, 06-30, 07-01, 07-09, 07-10, 07-13, 07-14, 07-15, 07-20

> **That is EXACTLY, item for item, the 20 real trading days the legacy axis omits** — the same 20 from the
> Item-1 root cause. Global carries VALUES there and NO COUNTS, because the 49F leg reads the legacy artifact
> and **the legacy artifact has no row for those days at all.**
> **The count-axis defect and the calendar-axis defect are the SAME defect surfacing in two places.**

Consequence, accepted by CTO: **the 49F decouple is a PREREQUISITE for global's cross-axis coverage**, not a
post-cutover tidiness item. CTO ruled `same_source=True` with the 20 dates as an **enumerated exemption LIST,
never a predicate** — a predicate would silently re-admit the class the moment legacy loses another day.

**Coverage fractions (defect-capable population):** inflection NEW clause (v) **421/427** (was 31); global NEW
clause (v) **30/427** — *global is the least-covered artifact and it is the one feeding the Global view.*
Clause (vi)'s real reach on fixed inflection is **30 positions, not 411** — the pre-launch all-zero stretch
inflates the naive count and must not enter the co-sign text.

## H. STOP-WORK RESULT — neither shape nor grain moves 1-of-38

DS's v2 widened clause (vi) from exact-revert to a parameter-free round-trip test, and hypothesised the
remaining gap was **grain** (05-27 invisible at firm-total because two bands offset). **I built the per-band
clause (vi) that hypothesis implies and ran it:**

| grain | hits on real legacy data |
|---|---|
| firm-total (current) | `07-06 (474,540,474)` |
| **per-band** | 07-06 across **5 bands** — **same single date, zero new dates** |

**And DS's mechanism for 05-27 is wrong in a way that makes the limit worse.** Measured:

    2026-05-26   161/127/55/21/10/23/5   total 402
    2026-05-27   161/127/55/21/10/23/5   total 402   <-- BYTE-IDENTICAL to 05-26
    2026-05-28   162/126/55/21/10/23/5   total 402

The offsetting move is the 05-27 -> 05-28 *transition*. The defect **at** 05-27 is that it carries 05-26's
roster unchanged — **staleness, not an excursion.** Nothing moves at all, at any grain.

> **A DUPLICATED ROSTER IS INDISTINGUISHABLE FROM A GENUINELY UNCHANGED ROSTER WITHIN THE COUNT SERIES.**
> Copying yesterday's roster onto today, and the roster simply not changing today, produce identical bytes.
> No shape and no grain separates them.

**Therefore: v1->v2 closed SHAPE, per-band would close GRAIN, and NEITHER moves real-data coverage off 1 of
38.** Further widening of clause (vi) is wasted effort. The three jobs are distinct and only one is a gate:

| instrument | job |
|---|---|
| clause (v) + same-source derivation | **CLOSES** the class (the actual cure) |
| clause (vi) | a shape **BACKSTOP** — 1 of 38; describe it as such |
| eclipse per-model cross-reference | the **AUDIT** — the only thing that sees staleness |

This is DS's own 49F sentence generalized and now proven: *"a frozen count reads exactly like a stable
roster."* It is not a 49F quirk — **it is the fundamental limit of any artifact-internal count check.**

## I. OUTSTANDING — exemption-list exercise (mine, on CTO's binding condition)

When DS lands the enumerated exemption I will run, as **separate invocations**: (1) the 20 PASS; (2) a 21st
injected date goes RED, tested both non-adjacent AND adjacent to a listed date (off-by-one in list membership
is the likely defect); (3) **removing** one date from the list makes that date go RED — without (3), a no-op
exemption and a working one are indistinguishable; (4) source read confirming an enumerated literal, not a
predicate — the binding condition a test cannot prove.

---

# ADDENDUM 2 — enumerated exemption EXERCISED (CTO binding condition, DISCHARGED)

Subject: `GLOBAL_CROSS_AXIS_EXEMPT_DATES` + gate `@77d297819`. Run by me as **separate invocations**, against
the real staged global (`08f9720e`). DS asked to be broken rather than trusted; this is that attempt.

**Integrity asserted before any mutant:** gate resolved by name; exemption extracted by **AST of the CONSTANT
itself** and confirmed `frozenset`, `len == 20`. **CTO's binding condition — enumerated literal, never a
predicate — is satisfied at source**, and the prohibition is carried inline at `:969-976`.

| # | Control | Result |
|---|---|---|
| 1 | full 20-date list, run alone | **GREEN** — as required |
| 2 | 21st offending date, NON-adjacent (`2026-03-11`) | **RED**, naming exactly that date |
| 3 | 21st offending date ADJACENT to listed `07-15` (= `2026-07-16`) | **RED** — no off-by-one in membership |
| 4 | **remove `2026-07-10`** from the list | **RED on exactly `2026-07-10`** |
| 4b | **remove `2026-06-01`** from the list | **RED on exactly `2026-06-01`** |
| 5 | *(my addition)* EMPTY list | **RED on all 20** — absorption is real, not a no-op |
| 6 | *(my addition)* BLOATED list (20 + `2099-01-01`) | **GREEN** + stale-list WARN (`:1085-1088`) |

**Controls 4/4b are the decisive pair: they prove the list is CONSULTED.** Without them a working exemption
and a no-op one are indistinguishable — the gate would read GREEN either way. **Control 5 is the converse**
and closes the remaining hole: with no list at all the gate fires on all 20, so the GREEN in control 1 is
earned by the exemption rather than by the check being inert.

**VERDICT: the exemption PASSES independent exercise. CTO's binding condition is DISCHARGED.** Detection is
preserved at full strength for any 21st date; the known bound is declared, enumerated, and self-reporting
when stale.

**Standing residual, unchanged:** the list exists only because 49F's count axis reads the legacy artifact.
**Retire it when the decouple lands** — it is a declared bound, not a fix.

## Corrections accepted FROM me, this session (recorded because they cut against my own limbs)

- My **boundary hypothesis** on COO's month/quarter cluster: **refuted 7 of 8** by COO's index-adjacency test
  on the clean axis. Correct on the 8th only.
- DS's **05-27 mechanism correction** was accepted by DS and traced by them to a worse failure than a
  mis-measurement: *their own earlier sweep had already printed the correct evidence* and the narration
  diverged from it hours later. Nothing in their output would have flagged it; independent re-measurement was
  the only detector.
- 49F **`-10` at 07-17**: DS grounded it as **NOT** a mis-stamp and **NOT** a duplicated roster — matches no
  roster date, distributed across 4 of 7 bands. **Mechanism UNDETERMINED and explicitly not guessed.** It
  must be recorded as *a known defect of undetermined mechanism*, not folded into the duplicated-roster class.
