# CVO VERDICT — A9, MDPF_COTREMEDIATION cottonwood pair fix

**Author:** `3.0.0_SA_CVO` · **Rendered:** 2026-08-26 ~18:35Z
**Graded against:** `e4b4966fc3` + amendments `835ee813e5` / `b6be686905` / `970f128bba` / `5a536a1efb`
— every one committed **before** the result existed.
**Subject run:** `0.4.0_DS_ClientPlatform~T`'s ad-hoc `{"qa_local": true}` fired 18:24:37Z, after the
A-Prime apply at 18:21:12Z.

---

## VERDICT: **A9 NOT MET.** 9/12, `errors=['global']`.

**Under Andrew's conditional-YES @`666fe25b0c`, NOT-MET is NOT-GREEN, and by his own words
— *"NOT green → nothing serves, fork returns to Andrew"* — THE 08-27 13:30Z FIRE DOES NOT SERVE THE
CORRECTED SPLIT.** Stated on the face of this verdict rather than left to be derived.

---

## ⛔ AND THE VERDICT THAT MATTERS IS NOT THE HEADLINE: **THE FIX UNDER TEST IS VERIFIED**

*"The fix failed"* and *"the fix works and made a pre-existing downstream gap reachable"* are opposite
conclusions with opposite remedies, and only the second is true here.

| arm | result |
|---|---|
| **1 STATE** — vintage moved on BOTH instruments | **PASS** — `15:29:34Z → 18:21:12Z`, `3/897ecG… → LdShsMmF…`. Measured on **my own** instrument at 18:22:37Z, independently of the grading seat. `COULD-NOT-VERIFY` does not fire. |
| **2 GRAIN** — graded run post-dates the apply | **PASS** — run 18:24:37Z > apply 18:21:12Z |
| **4 DISCRIMINATION (PRIMARY)** — delta on the same comparison that failed | **PASS** — `delta = 0.0100` PRESENT; `43676557.1200` **0 occurrences**. The identity gate flipped `FAIL → PASS`. |
| **3 COVERAGE** — `errors{}` empty | **FAIL** — `errors=['global']` |

**A5, all three grains, from the LAMBDA's run and not an in-process build:**

| id | population | expected | observed |
|---|---|---|---|
| A5a Client - Opal Supervised (**served field**) | 3 accounts | $2,256,694.98 | **$2,256,694.98** MET |
| A5a′ non-Opal-parent subset | 2 accounts | $1,476,313.07 | **$1,476,313.07** MET |
| A5b SMAs → `opal_div_sma` | 1 account | $1,393,065.98 | **$1,393,065.98** MET |

Itemisation ties: sleeve $780,381.91 + unattributed-leg **$0.00** + unallocated $1,476,313.07 =
$2,256,694.98. `by_model` 6 keys incl. Fixed Income · bridge 330/330 dropped 0 · IDENTITIES PASS.

>> **THE PRIMARY ARM IS GREEN. The cottonwood repair does exactly what it was built to do, on the
running bytes, on every criterion pre-registered for it. What fails is a DOWNSTREAM composition
identity that the repair made REACHABLE — the identical shape as the original defect, where a correct
change exposed a pre-existing gap.** <<

---

## THE GLOBAL FAILURE — WHAT I INDEPENDENTLY ADD

`0.4.0_DS_ClientPlatform~T` identified the KEY with certainty and stopped, correctly, short of the
SITE: global's composition gate fails with `delta -8,442,396.92` against A3's Fixed Income
$8,442,396.91 — **one cent, float, not a coincidence.**

That seat named the closing measurement (s.7) and said plainly it was not their lane.
**I ran it — reading is not fixing:**

```
SERVED global by_model — 9 keys:
  opal_blend_5050_int_ltc · opal_blend_5050_st_int · opal_div_sma · opal_growth_sma ·
  opal_intermediate · opal_long_term_aggressive · opal_long_term_conservative ·
  opal_short_term · opal_ultra_short_term
opal_fixed_income PRESENT: False
```

**Global's `by_model` does not carry `opal_fixed_income`.** So when cottonwood's `model_aua` gains the
recovered Fixed Income dollars, global's `by_model` cohort sum does not — **the new key reaches one
side of global's composition identity and not the other**, which is exactly the delta.

⛔ **GRAIN LIMIT, STATED RATHER THAN GLOSSED:** this artifact is `as_of_last: 2026-08-24` — the
**pre-fix served object**. It establishes that global's `by_model` **has never carried the key**; it is
**NOT** a direct measurement of the failing run's internal composition. It is a **different plane**
from that seat's run log, so it CORROBORATES rather than repeats — but the site is confirmed, not
proven, and naming the exact map remains a global-producer read by its owner.

**THIRD SIGHTING TODAY OF ONE CLASS:** a key entering `by_model` must exist in every map its consumers
read, in one commit. That discipline was applied to `opal_div_sma` and **DIVZ is clean because of it.**
`opal_fixed_income` landed in the FIRST commit — **before the lesson was stated** — and is the key
nobody re-checked.

---

## WHAT I DO NOT CLAIM

- **NOT** which map is missing the entry, **NOT** that the remedy is one line.
- ~~**NOT** that 2026-08-25 is the only affected date (the gate refuses on the first of 462 dates
  scanned; whether more surface once it clears is **UNMEASURED**).~~
  ⛔ **STRUCK ~19:00Z — THIS WAS FALSE AND IT WAS MINE.** Read at source:
  `dim_mdpf_aggregate_aua_timeseries.py:1942` — `fails = partial + ident + pin49 + pininf + band +
  pincot + provfails`, raised **after** the full date loop. **The gate ACCUMULATES; it does not
  short-circuit.** So `1 band/total violation across 462 dates` is a **COMPLETE CENSUS**, the count
  IS measured, it IS one, and **nothing surfaces behind it.** I inherited "refuses on the first" from
  a peer's honest hedge and repeated it as an established property without opening the file.
  Preserved struck: a reader who saw the original must be able to tell it was overturned.
- ⚠ **AND THE SUMMARY LINE CANNOT COUNT TWO OF ITS OWN CATEGORIES:** `fails` sums **seven** lists;
  the message prints **five** counts (`pincot` and `provfails` have no counter, `FATAL:` lines cap at
  10). A run failing only on those two prints **all zeros while refusing**. So the `0/0/0/0/1` is
  consistent with exactly one failure — and the single `FATAL:` line is what establishes that it *is*
  one — **but the summary alone could not have told anyone.** Count the `FATAL:` lines, not the five
  numbers.
- **NOT** a re-derivation of A1–A8. Those are the executing seat's exercise against a pre-registered
  bar with a working PRE-FIX control; re-running them by the same method would be a **REPETITION**.

---

## AMENDMENT — 2026-08-26 ~20:00Z: **THIS VERDICT IS ABOUT THE 18:24Z RUN AND IS NOW SUPERSEDED AS CURRENT STATE**

The NOT-MET above is a true record of the **18:24Z** `qa_local` run. It is **NOT** the verdict on the
authorized real-chain exercise that followed. Recording that here so a reader landing on this file
does not take a superseded verdict as the live position.

### WHAT CHANGED

**GATE (ii): MET TO THE CENT, over the RIGHT input.**
`opal_fixed_income @2026-08-25 = 8,442,396.91` · `sum(by_model cohort=model) = 1,802,566,138.35` vs
`model_aua = 1,802,566,138.36` · identity delta **0.01** (was `-8,442,396.92`) · movement
**+8,442,396.91** against a pre-registered **+8,442,396.92**. **One cent, float.**
`model_aua` now reads **byte-for-byte the number in the original FATAL line** — the two sides of the
failed identity agree, and the side that moved is the one the fix was built to move. The probe
confirmed `SLICE READ BY THE FOLD — opal_fixed_income present: True`, which is exactly what the
earlier STOP existed to force.

**GATE (i): CLEAN — and NOT on my read.** See the instrument note below.

### ⛔ INSTRUMENT NOTE — GATE (i) IS NOT DOUBLY CONFIRMED

`1.0.0_SA_CTO` and I both took the fold-branch read `0.4.0_DS_ClientPlatform~T` asked a non-author to
take. **On the `gap = True` limb we are a REPETITION** — same file, same lines, one measurement
reported twice.

| limb | who read it | what it establishes |
|---|---|---|
| `:2490-2519` — `gap = True` fires, cell poisons to `None` | **CTO and me** (repetition) | the branch fires |
| `:2519` `gap` is LOCAL to one (key,date) cell; `:1890-1893` band/total treats a per-key `None` as a **NON-CONTRIBUTION**, `s = None if ALL None else sum(non-None)` | **CTO only** | **it does not matter** |

**ONLY THE SECOND LIMB CLOSES THE GATE, AND EXACTLY ONE SEAT READ IT.** I had the mechanism of the
firing and not the mechanism of the harmlessness. **"CVO and CTO both cleared gate (i)" is FALSE.**

**And the strongest evidence is not about code:** both sides carry zero Fixed Income on those 18
dates because **the model did not exist before 08-25**. The agreement is a fact about the world the
code faithfully represents — not a skip, not luck, and not something a re-implemented predicate could
have shown.

### ⛔ WHAT THE EXERCISE DOES NOT COVER

**THE LAMBDA.** Tonight proved the **CODE** by running it directly. The 13:30Z fire runs the
**BUNDLE**, which still carries the old 9-key `GLOBAL_MODEL_KEYS` and the old crosswalk. **Without
the rebuild, the fire re-fails at 18:24Z's exact site on a now-correct slice.** The (b) lift is GO as
of ~19:59Z. Until it lands and the lambda path re-runs, **no verdict here covers the scheduled run.**

### CARRIED FORWARD, not tonight's scope

`gap = True` is a **MISLABEL** on a not-yet-existing model's pre-existence dates — the honest state is
*"model outside its existence window"*, not *"contributing firm, missing measurement"*. Output
identical, arithmetic unaffected, **but it misleads anyone grepping gap counts.** Rides the next
deliberate touch of the fold, alongside the five-of-seven summary-counter defect recorded above.

---

## THE GATE REFUSING IS THE SYSTEM WORKING

A composition identity caught a real inconsistency **before it served.** Had A9 read 12/12 with this
gap present, the corrected split would have served tomorrow carrying an $8.44M internal disagreement.
**The bar that produced a NOT-MET is the reason that did not happen**, and `0.4.0_DS_ClientPlatform~T`
reported NOT-MET against its own bar rather than reaching for 9/12 as a partial pass, with a serve
waiting on the answer.
