# ANDREW-DIRECT 2026-08-12 (~1430Z, CVO terminal) -- route the two classifier bugs to DS

## VERBATIM
> **"route the two classifier bugs to DS, tell MSTR that we need DS online"**

**SCOPE (his words, nothing wider):** the TWO DEFECTS I surfaced -- NOT the curation/taxonomy questions,
which remain at him (Voya lookthrough, held-away-assets fourth-class, CCA LP rule-vs-curation). This
DISCHARGES the routing question I put to him at ~1345Z and supersedes COO's standby ("if he says nothing I
will dispatch") -- COO informed same turn so the fix is not dispatched twice.
**Grounded on receipt:** DS base is LIVE (PID 16056) with an EMPTY queue, ~A and ~B both LIVE and idle.
So "we need DS online" is SATISFIED at this moment -- relayed to MSTR anyway, unnarrowed, with the measured
state attached, because reading a sovereign instruction as already-satisfied is not my call to make.

## THE ROUTED WORK (what I handed DS)

### BUG 1 -- `_RE_FI` trailing word-boundary. $3,556,935 / 44 names (Cottonwood, measured).
`|\b\d+\.?\d*%\b` -- the TRAILING `\b` after `%` can never match when a space follows (`%` non-word, space
non-word -> no boundary), so every `<rate>% <year>` name falls through. **Fix: drop the trailing `\b`.**
**BOTH FILES, deliberately:** `data/black_diamond/scripts/gold/lib/etf_classifier.py` (the ORIGINAL, which
feeds the SERVED mix) and `data/assets/scripts/gold/runners_49f/a07_dim_asset_classification.py:102-111`
(the byte-identical port). Exercised: shipped=False / fixed=True on `VALLEY NATL BK PASSAIC N J 3.9% 2026`.

### BUG 2 -- dotted-ticker equity fallback. $793,815 (Berkshire Hathaway Class A).
`classify()`'s final fallback is `re.fullmatch(r'[A-Z]{1,5}', t)`, so a share-class ticker (`BRK.A`) fails
it and lands UNCLASSIFIED with a valid CUSIP present. DS sizes the pattern; **do not over-widen.**

## THE FOUR CONTROLS I WILL VALIDATE AGAINST (stated in advance so they build to them)
1. **NEGATIVE CONTROL, MANDATORY:** a name with NO rate must still NOT classify `fixed_income`. I verified
   `Investor Manual Asset - Car` stays False under the one-character fix. **A wider rewrite can over-match,
   and over-classifying cash-like paper INTO fixed income is a WORSE defect than the one being fixed.**
2. **BOTH FILES OR THE PARITY CONTROL BREAKS -- deliberately, not by discovery.** A_07's
   `PARITY-VS-SERVED` asserts port == lib (3,784/3,784). Fix the port ONLY and that control CORRECTLY
   fails; fix both and it re-ties. Either is acceptable; being surprised by it is not.
3. **PRE-DECLARED BAND (registry BEFORE evidence).** This is an INTENTIONAL served-value change -- 44 names
   move UNCLASSIFIED -> fixed_income. Per the parity bar's inversion, on this band **DIVERGENCE from the
   old served value is the PASS and reproducing the old value is the FAIL** (a MATCH-KNOWN-WRONG heal, the
   same shape as the fee-earning-heal band). It must be registered as a band, never arrive as a diff.
4. **MEASURE THE 49F SIDE TOO.** I decomposed Cottonwood only. The fix may move 49F names as well --
   **report the number; do not assume it is zero.**

**NOT A GATE:** this is a defect fix on DS's normal commit -> QA -> deploy cycle. I am stating the property
that it changes client-facing served mix values so it is handled knowingly -- I am NOT manufacturing an
approval step, and no seat needs to sign before DS proceeds.

## WHY THE PORT-FIDELITY CONTROL COULD NOT HAVE CAUGHT THIS
The port is byte-identical to the lib, so it reproduces the lib's defects perfectly and its parity control
answers *"did it reclassify?"* -- correctly, NO. Doctrine: `docs/doctrine/CONTROLS_OVER_CARE.md` SS "You
compared the thing TO ITSELF" (a faithful port is maximal parity evidence and zero correctness evidence).
The defect was found by enumerating the OUTPUT POPULATION, which no code diff could have done.

-- 3.0.0_SA_CVO
