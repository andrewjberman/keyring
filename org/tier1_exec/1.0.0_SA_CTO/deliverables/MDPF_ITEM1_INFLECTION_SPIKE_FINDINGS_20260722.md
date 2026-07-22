# MDPF_REVAMP Item 1 -- Inflection "jumping around Jul 6/7 + other odd spikes"

**Author:** 1.0.0_SA_CTO | **Date:** 2026-07-22 ~1215Z | **Trigger:** Andrew-direct ~1205Z (relayed by MSTR)
**Status:** **SUPERSEDED IN PART AT 1231Z -- SEE SECTION 0a. A REAL DEFECT WAS FOUND INSIDE THE
FROZEN-9. THE CO-SIGN VOIDS. FIX BEFORE FLIP.**

## 0. Verdict as first written (1215Z) -- CORRECT ON THE VALUE AXIS ONLY

The Jul 6/7 jumping is a **defect in the LEGACY served artifact**, not in the revamp. The revamp
already fixes it, plus three more legacy defects. **No defect was found in the frozen-9**, so the
2-of-3 never-widen co-sign pinned to those ETags does **not** void.

## 0a. CORRECTION (1231Z) -- THE ABOVE IS WRONG ON THE COUNT AXIS

**The Model Portfolios trend has a VALUE mode and a COUNT mode. Everything in section 0 is the VALUE
axis. On the COUNT axis the revamp REPRODUCES Andrew's complaint, on his exact dates.**

Found by `0.4.0_DS_ClientPlatform` (its own producer -- brought, not fixed, with a separately-run
positive control). **Independently reproduced by CTO before acceptance** -- a producer's self-report
on the producer's own artifact is not evidence, including a good one.

Frozen-9 `inflection/aggregate_aua_timeseries.json` (`cec5a0d6`), COUNT axis:

| date | count | value |
|---|---|---|
| 2026-07-02 | 474 | 122,227,270 |
| **2026-07-06** | **540** | 122,866,034 *(value CORRECT)* |
| 2026-07-07 | 474 | 123,562,809 |
| 2026-07-08 | 475 | 125,450,227 |

**+66 then revert, on July 6 and July 7 -- Andrew's sentence, verbatim, produced by the revamp.**
CTO positive control, run SEPARATELY: revamp count == legacy count at 07-02 / 07-07 / 07-08
(474/474/475) -- the test is not vacuous.

**MECHANISM (source-confirmed by DS, closes the Rule-22 gap):** the producer imports `account_count`
from the **LEGACY served artifact by date-join** (`:476-500`, wired `:812`) and **discards the count
it already computes** at `:427`. Legacy's date axis is the very thing section 3 proves is broken.
**So the artifact reads its VALUE axis from eclipse and its COUNT axis from legacy -- two axes of one
artifact, read from different days.**

**Full sweep, denominator stated:** of 427 revamp dates only **38** carry an eclipse partition
(eclipse starts at the 05-15 launch) -- 26 agree, 7 honest-None, **5 disagree**. Four are genuine
count-axis date defects (05-27, 05-28, 06-24, **07-06**); the fifth (07-20, 534 vs 546) is the
declared FUNDED-basis frontier rule, excluded from the defect set but flagged as a **basis seam** on
the same line. **Pre-05-15 the instrument is blind -- that is stated, not closed.**

**CTO RULINGS:** (1) COUNT is in cutover scope -- the tracker's own pre-push conditions require
VALUE+COUNT full-depth clean on all 3 firms; **ship-with-it-NAMED REFUSED.** (2) The FLAG-2 PRESERVE
tie to served **breaks, and that is correct -- parity with a known defect is not a virtue**; carried
by a test that could have failed (eclipse-derived == served EXACTLY at 44/44 common non-mis-stamped
dates). This changes a CTO+Andrew co-signed decision; CTO owns it and names it to Andrew. (3) **The
2-of-3 never-widen co-sign VOIDS** -- fresh pin, fresh 3-pass, fresh CTO+COO+Andrew limbs. (4) DS
must sweep the 49F/global residual (same import path `:628`, structurally present, **UNMEASURED --
unmeasured is not clean**) BEFORE the rebuild.

**A FIFTH LEGACY DEFECT, from DS's source sweep:** eclipse's first partition is 2026-05-15 with an
Opal sum of `94,546,459.54`; the revamp carries that exactly. **Legacy carries 0.0 on 05-15** and only
picks the launch up on 05-18 -- legacy reports ZERO where source has $94.5M.

**PROCESS NOTE, banked:** CTO's headline generalized from a pass that was inflection-only and
model-only. COO caught the `non_model` axis; CTO corrected it; **the corrected claim then generalized
again across the value/count axis and was wrong the same way, one axis out.** Correcting a
wrong-axis error does not immunize the next claim. The gate -- not the care -- is what held this
off the served surface.

## 1. What Andrew is looking at -- GROUNDED, not assumed

He is necessarily on the **LEGACY** view. Two independent grounds:
- Live applied CF `EVTSA9VEHNZVH`: 24 behaviors / 7 origins / **no** `S3-opal-data-assets` origin /
  **zero** exact-9 behaviors / catch-all `/api/general/*` -> `S3-opal-data-portal-v2-json`.
- Revamp FE `6287847c` sits on portal **DEV**, 6 commits ahead of `origin/PROD`, never promoted.

No revamp render reaches him. (This is the "enumerate what the number is OF" step -- COO and MSTR
both asked that it be answered before any mechanism reasoning. It was.)

## 2. Method + DENOMINATORS (stated, per verification-law 10)

Artifacts compared: `s3://opal-data-portal-v2/json/mdpf/{inflection,global}/aggregate-aua-timeseries.json`
(SERVED) vs `s3://opal-data-assets/gold/mdpf_revamp/{inflection,global}/aggregate_aua_timeseries.json`
(frozen-9, `cec5a0d6` / `c27e1f37`).

| pass | scope | evaluated | flagged >=5% |
|---|---|---|---|
| inflection `model_aua` | LEGACY | 37 transitions (429 dates) | 4 (5 at 3%) |
| inflection `model_aua` | REVAMP | 33 transitions (427 dates, 421 non-null) | 2 |
| inflection `by_model` bands | REVAMP | 231 band-day transitions / 7 models | 18 |
| global `model_aua` | LEGACY / REVAMP | 428 / 416 | 3 / 3 |
| global `non_model_aua` | LEGACY / REVAMP | 428 / 416 | **29 / 14** |

Decisive mechanism test used throughout: `model_aua` vs `non_model_aua` vs `partner_custody_total`
vs `account_count`. A **reclassification** is zero-sum (model up == non-model down, custody flat);
**new assets** move the custody total.

## 3. FOUR LEGACY DEFECTS -- all absent from the revamp

1. **07-06 DATE-MISLABEL** (= Andrew's "july 6 july 7"). Legacy stamps the 07-10 snapshot onto Mon
   07-06, then reverts 07-07: **+11.97% then -9.72%**. Signature is exact on **two independent
   fields**: legacy 07-06 `model 136,859,722 / non_model 65,461,006` == revamp 07-10
   `model 136,859,722 / non_model 65,461,006`, byte-identical pair (legacy accounts 540 -> 474 on the
   revert). Revamp carries `122,866,034` on 07-06. **This CONFIRMS CVO @88851665d at the values
   rather than accepting it on say-so.**
2. **07-09..07-15 SEVEN-DAY HOLE** in legacy -> the ongoing reclassification surfaces as a single
   **+10.05% cliff on 07-16**. This is an "other odd spike" and **CVO's verdict did not cover it**
   (MSTR flagged that gap correctly).
3. **SATURDAY DATAPOINT.** Legacy's last date is **2026-07-18 = a Saturday**, value `137,170,029`.
   Revamp places that same value on **Mon 2026-07-20**. Trading calendar resolved FIRST per NEVER#1
   (07-18 Sat / 07-19 Sun / 07-20 Mon). Legacy stamps a non-trading day; revamp's trading-day axis is
   correct and also fresher.
4. **06-09 +3.17%** legacy-only, same class.

## 4. THE REAL BUSINESS EVENT -- correct in both, must NOT be "fixed"

Inflection is progressively reclassifying accounts **out of non-model into Opal models**,
~06-03 through ~07-10. `partner_custody_total` is **FLAT ~$200-206M** throughout while `model_aua`
rises `96.7M -> 137.2M` and `non_model_aua` falls `109.8M -> 64.5M`. It is a **mix shift, not inflows.**

06-03 composition: `dModel +16,961,432 / dNonModel -16,894,373 / dCustody +67,059 / dAccounts +44`
-- zero-sum across 6 of 7 bands simultaneously. CTO + COO measured this **independently and converged.**

**CVO's word "one-time" does not survive** (COO's catch): 06-03 and 07-10 are the same mechanism class
five weeks apart. There are at least TWO. The right question is no longer "what was the one-time
event" but "the mechanism recurs -- is EACH occurrence correctly dated?"

## 5. OPEN THREADS -- why this is ANSWERED, not CLOSED

**(a) The 06-03 DATE is not independently established.** My `accounts +44` evidence comes from the
**same producer on the same axis** as the dollars. If a batch is assigned to a wrong as-of, the count
moves to that wrong date too and the artifact stays perfectly self-consistent -- **which is exactly
what legacy did at 07-06.** So +44 establishes THE EVENT, not THE DATE. The 07-06 finding is stronger
precisely because it compares **across two artifacts**; the 06-03 one does not have that property.
Closing it needs a source **outside the producer axis** (eclipse/silver as-of, or modelId assignment
timestamps). COO's catch; I accept it. -> DS.

**(b) `non_model` moves in the GLOBAL view -- RESOLVED 1225Z, was the largest open population.**
My first passes were **inflection-only and model-only**; the chart is **STACKED**, so `non_model` is a
visible band. COO ran the axis I skipped and MSTR escalated the decisive question: **do those steps
PERSIST into the revamp, or are they legacy-only?** Nobody had run it. I ran it across all 3 firms:

| firm | LEGACY non_model hits | REVAMP hits | persist (both) | legacy-only (flip REMOVES) | revamp-only |
|---|---|---|---|---|---|
| GLOBAL | 29 / 428 | **14 / 416** | 2 | **27** | 12 |
| 49FINANCIAL | 55 / 428 | **15 / 426** | 6 | **49** | 9 |
| INFLECTION | 6 / 428 | **4 / 416** | 1 | **5** | 3 |

**ANSWER: neither purely -- the flip strictly IMPROVES the picture but does NOT produce a spike-free
chart.** It removes 27 of 29 Global and 49 of 55 49F legacy non-model steps. What remains is **not
unexplained**: applying the mechanism test to all 14 Global steps classifies **7 COMPOSITIONAL**
(offset by an equal-and-opposite model move, total ~flat = mix shift) and **7 GENUINE NET MOVES**
(real money moved -- e.g. 2025-10-01 `+$53.2M`), with **0 UNKNOWN**. The largest, 2025-01-16
(`dNonModel -89,423,521 / dModel +88,381,655`) and 2025-10-21 (`-69,534,374 / +65,966,590`), are
compositional reclassifications, not defects.
**So "the flip fixes what Andrew sees" is TRUE for every defect he named and for 27/29 Global
non-model steps -- but he WILL still see real steps in the non-model band afterward, because some of
them are real events. That must be said plainly and not smoothed.**

**STRUCTURAL CONFIRMATION nobody had checked:** the revamp's **GLOBAL and 49FINANCIAL `non_model`
series are NUMERICALLY IDENTICAL, value for value.** That is exactly what Andrew's EXCLUDE/B ruling
specifies (enterprise non-model rebased 49F-only) -- so this is the rebase **verified in the served
bytes**, not merely declared in a ledger. The 49F-only extra hit is 2026-07-13, which Global carries
as honest-None.
**CONFOUND -- do not diff raw:** legacy vs revamp `non_model` are on **DIFFERENT BASES**. Levels
differ ~2x. Date-set overlap is meaningful; magnitude comparison across bases is NOT.

**Inflection onset now fully explained:** models launch **2026-05-15** (`dNonModel -93,711,583 /
dModel +94,546,460`, compositional), then progressive reclassification 06-03 (`+$17.0M`) and 07-10
(`+$11.8M`). One coherent arc, custody flat throughout.

**(c) The revamp's OWN 07-13/14/15 hole** -- three consecutive trading days (Mon/Tue/Wed) immediately
after the 07-10 event, inside Andrew's exact window. Plus 05-21, 06-01, 07-01 = 6 honest-Nones.
**49F has ZERO nulls; every gap is inflection-origin and propagates to global.** Honest-None is not a
fabrication, but "better than legacy" is not "explained," and no co-signed item covers this run.

**(d) UNGROUNDED, flagged so it is not lost:** Global `model_aua` flags legacy **2026-05-18** (+6.28%,
from `1,349,270,403`) vs revamp **2026-05-15** (+5.78%, from `1,349,270,859`) -- near-identical
pre-level, adjacent trading days (Fri/Mon). MAY be the same event dated differently (same class as #1
and #3) or may be two things. **INFERRED from a level coincidence; not source-confirmed; authorizes
nothing** (Rule 22).

## 6. Grounding discipline

**MEASURED:** every number above, from the artifacts, by two independent limbs (CTO + COO) that
converged. **INFERRED:** that the mechanism *is* a modelId reclassification -- **neither COO nor I
have read the producer source or silver.** Per Rule 22 that hypothesis **cannot authorize a fix or a
cert**; DS is the party who can source-confirm it.

## 7. Consequence for the gate

- **Pin intact.** No write to `gold/mdpf_revamp/*`. The 0645Z 2-of-3 (CTO+COO) **stands**; no re-fire,
  no fresh 3-pass. MSTR discharged the pin-void gate for item 1 on the condition not firing.
- **RE-ARMED for item 2:** Cottonwood-into-Global **necessarily rewrites `c27e1f37`**, the anchor of
  the pinned 9. The current co-sign is not at-risk from item 2 -- it is **structurally doomed by it**.
  Andrew buys a second never-widen co-sign either way; the only question is whether he also buys weeks
  of a chart we have measured to be wrong.
