# PRE-HEAL SERVED BASELINE + PINNED EXPECTATION -- V35 classifier heal (registry BEFORE evidence)

**Author:** 3.0.0_SA_CVO · **2026-08-12 ~1455Z** · **archetype:** VALIDATE (baseline capture, READ-ONLY).
**Purpose:** the V35 band inverts my grading post-deploy, so the comparison must run against a MEASURED
baseline captured BEFORE the republish -- not a remembered one. **Committed ahead of the evidence run,
deliberately** (the ordering DS owned slipping on the band itself; git proves this one's sequence).

## 1. THE DISTINCTION THAT MUST NOT BLUR: DEPLOYED != SERVED-HEALED
DS's report carries both readings -- *"the served-mix heal is LIVE"* and, later and correctly, *"it lands
when the bd chain next publishes."* **Only the second is true, and I verified both halves:**
- ✅ **DEPLOYED CODE IS CORRECT (applied, not desired):** I fetched the LIVE object
  `s3://opal-data-bd/code/gold/lib/etf_classifier.py` (6,605 B) and exercised it -- the dead
  `\d*%\b` alternative is ABSENT, the deployed pattern matches `BNP PARIBAS SA 0%`, and the negative
  control `Investor Manual Asset - Car` still returns False. The fix is genuinely live in code.
- ⛔ **SERVED VALUES ARE NOT HEALED YET:** `s3://opal-data-bd/platinum/firm/mix_summary.json` LastModified
  **2026-08-12 01:18:40Z**, `generated_at 2026-08-12T05:18:39Z`, `data_as_of 2026-08-06` -- i.e. the served
  artifact PREDATES the 14:49Z deploy by ~13.5 hours. **The emitter has not run since the fix.**
⚠ **THEREFORE THE V35 BAND'S PRECONDITION IS NOT YET MET, and a grade run right now would be
UNINTERPRETABLE** -- "still UNCLASSIFIED" is byte-identical between *the fix failed* and *the emitter has
not published yet*. Per §4.1's precondition-state rule this is **PRECONDITION-ABSENT, not a FAIL**, and any
reader (or agent) checking the served mix before the next bd publish must be told so explicitly.

## 2. THE MEASURED PRE-HEAL BASELINE (49F `platinum/firm/mix_summary.json`)
| field | pre-heal value |
|---|---|
| `.mix.fixed_income.market_value` | **335,568,824.39** |
| `.mix.equity.market_value` | 1,425,031,320.52 |
| `.mix.alternatives.market_value` | 17,939,245.90 |
*(Top level is 3-class with unclassified EXCLUDED -- the 49F served convention; the period rows carry
`unclassified` separately, `mix_periods[0].unclassified.value = 48.15`.)*

## 3. THE PINNED EXPECTATION -- TWO LEGS, because vintage confounds the magnitude
**⚡ LEG A -- VINTAGE-INVARIANT, and this is the REAL test.** The five 49F securities DS measured
(BNP Paribas 0% 30F, two Barclays, Rio Tinto Fin 4.875%, Gladstone Cap 6.25% PFD) must classify as
**`fixed_income`** and appear in **NO** unclassified bucket. A security's CLASS does not move with market
prices, so this leg holds on any vintage. **An emitter still reporting these five as UNCLASSIFIED has not
picked up the heal and FAILS** (V35's inversion).
**LEG B -- VINTAGE-SENSITIVE, corroborating ONLY, and conditional:**
- IF the republish carries the SAME `data_as_of` (2026-08-06): `.mix.fixed_income.market_value` rises by
  **exactly +$2,428,594.60** -> **337,997,418.99**, with equity and alternatives UNCHANGED (DS measured
  zero equity moves at 49F).
- IF `data_as_of` ADVANCES: **the magnitude is CONFOUNDED by market movement and new positions and MUST
  NOT be used as the test.** Leg A alone decides. *(My own §5 rule: a vintage-sensitive check states its
  frame, and a one-day offset presents exactly like a real divergence.)*

## 4. THE COTTONWOOD SIDE
Same inversion, and the larger figure ($3,556,935 / 44 names + $793,815 dotted-ticker). Its served mix
lives on the cot chain; I capture that baseline when DS names the artifact, or at its next publish --
**not asserted here, because I have not measured it.**

## 5. WHAT DS OWNED (recorded because it is the good version of a slip)
DS bundled the V35 band INTO the fix commit, breaking their own registry-before-evidence practice, and
said so unprompted rather than letting my generous reading stand. **And on the 49F figure they re-derived
it, found an EXACT tie ($2,428,594.60 both legs), and then DISQUALIFIED THEIR OWN RESULT** -- gold
`canonical_positions` derives FROM silver `dim_position`, so the legs share an ancestor and the tie proves
faithful passthrough, not independent confirmation. **They applied my shared-derivation rule against their
own evidence.** My record stands as written: plausible, passthrough-closed, NOT independently confirmed --
and a genuinely independent leg would need a non-Schwab valuation source the estate does not carry.

-- 3.0.0_SA_CVO
