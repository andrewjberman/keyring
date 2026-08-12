# VALIDATION VERDICT -- the two classifier bug fixes @bd2a8f854a (Andrew-direct routing)

**Validator:** 3.0.0_SA_CVO · **2026-08-12 ~1450Z** · **archetype:** VALIDATE
**Subject:** DS base's fix of the two defects I surfaced, routed by Andrew-direct ~1430Z
(ANDREW_DIRECT_20260812_ROUTE_CLASSIFIER_BUGS_TO_DS.md @7802de0d5f).
**Method:** I re-exercised the OLD and NEW patterns MYSELF from git (`bd2a8f854a~1` vs `bd2a8f854a`) --
not the producer's reported results.

## VERDICT: VALIDATED. All four controls I stated in advance are met, verified independently.

| Control (mine, stated pre-fix) | Verified |
|---|---|
| **1. MANDATORY NEGATIVE -- no over-match** | **5/5 hold False under NEW**: `Investor Manual Asset - Car`, `...- Home`, `BERKSHIRE HATHAWAY INC DEL CL A`, `APPLE INC`, `Voya`. **This was the control that mattered most** -- over-classifying cash-like paper INTO fixed income would have been worse than the bug -- and it passes. |
| **2. BOTH FILES in lockstep** | `git show --stat` confirms ONE commit touches `data/black_diamond/scripts/gold/lib/etf_classifier.py` (the lib feeding the SERVED mix) AND `.../runners_49f/a07_dim_asset_classification.py`. So `PARITY-VS-SERVED` re-ties rather than correctly failing -- the deliberate branch, not the discovered one. |
| **3. PRE-DECLARED BAND** | `V35-CLASSIFIER-HEAL-INVERTED` registered in `predeclared_divergences_49f.json`, carrying my inversion VERBATIM ("divergence from the old served value is the PASS, reproducing it is the FAIL"), with surfaces, field_paths, measured impact, and an EXPIRY condition. Correctly formed. |
| **4. MEASURE THE 49F SIDE** | Done, and **NOT zero** -- the answer I told them not to assume: **$2,428,594.60 / 5 names**, all UNCLASSIFIED -> fixed_income, zero equity moves. 56% of the Cottonwood figure. |

## DS'S HEADLINE CLAIM IS TRUE, AND IT IS STRONGER THAN MY FINDING -- verified
I framed the trailing `\b` as failing when a SPACE follows. **It also fails at END-OF-STRING** (the string
edge after a non-word char is not a boundary either), so the standalone-coupon alternative was
**effectively DEAD since the file was authored, not merely space-sensitive**. The proof is in the source:
**the pattern failed the example written in its own adjacent comment.** Exercised by me, both directions:
| input | OLD | NEW |
|---|---|---|
| `BNP PARIBAS SA 0%` **(the lib's OWN docstring example)** | **False** | True |
| `VALLEY NATL BK PASSAIC N J 3.9% 2026` | False | True |
| `RIO TINTO FIN 4.875%` | False | True |
**A regex that cannot match the example printed beside it had been shipping unnoticed.** That is a sharper
statement of the class than mine: the DOCSTRING was itself an unexercised assertion, sitting inches from
the code it described. *(Pattern length 260 -> 258: exactly the two characters removed.)*

## BUG-2 SIZING -- exercised against adversarial inputs, 9/9 correct
DS chose `[A-Z]{1,5}(\.[A-Z])?` and declined a wider variant that "bought nothing measured" -- correct
discipline. My own adversarial battery: ACCEPTS `BRK.A` `BRK.B` `BF.B` `AAPL`; REJECTS `912828XY`
(CUSIP fragment), `SPY123` (alphanumeric), `BRK.A.X` (multi-dot), `ABCDEF` (>5), `BRK.` (trailing dot).

## SCOPE OF WHAT I VERIFIED (do not over-read)
- **Cottonwood $3,556,935 / 44 names: INDEPENDENTLY CONFIRMED** -- it matches MY OWN prior measurement
  exactly (I computed it with the fixed pattern before DS did), so two derivations agree.
- **49F $2,428,594.60 / 5 names: NOT re-derived by me.** Reported by DS; the named securities (BNP Paribas
  0% 30F, two Barclays, Rio Tinto Fin 4.875%, Gladstone Cap 6.25% PFD) are unambiguously fixed income and
  the figure is plausible, but plausible is not verified. **Stated rather than absorbed.**
- **BAND ORDERING:** the band is in the SAME commit as the fix, so git alone cannot prove registry-preceded-
  evidence. My §4 concern (a pre-declaration written alongside results RATIONALIZES them) is materially
  weaker here because this band declares an INTENDED heal rather than excusing an unexpected divergence --
  accepted on that basis, with the ordering named.
- **Gate-required extra, disclosed by DS:** the lib predates ADHC_DSFLOW.004 and needed
  `from __future__ import annotations` to pass the universal gate. Benign (a compiler directive, no runtime
  effect on these patterns), and DS re-ran the control battery AFTER adding it rather than assuming the
  earlier run stood -- the right instinct.

## WHAT I OWE NEXT (post-deploy)
The fix is committed, not yet deployed. **On deploy, the V35 band inverts my normal grading:** an emitter
still reporting these names UNCLASSIFIED has NOT picked up the heal and FAILS; the healed values are the
PASS. Estate-wide this reclassifies **~$6.78M** ($4.35M cot + $2.43M 49F) from UNCLASSIFIED into
fixed_income. I validate that at the served surface, and the band expires when the pins re-base.

-- 3.0.0_SA_CVO
