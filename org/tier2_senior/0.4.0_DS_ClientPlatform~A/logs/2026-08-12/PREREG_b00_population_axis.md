# PRE-REGISTRATION -- the B_00 basis repair is a POPULATION change, banded as one

**Written 2026-08-12 ~15:24Z, BEFORE any code change**, per CTO 152134Z: *"A VALUE PIN CANNOT
SEE A POPULATION CHANGE ... pre-register the affected COUNTS on the population axis BEFORE you
build, not after, or the downstream instruments will read their own correct adjustment as a
regression."* Scope ruled: the 08-11 basis ruling (b) RAW portfolio-domain currentValue
EXTENDS to B_00; discriminator-preservation rec ADOPTED verbatim.

## THE CHANGE

`b00_canonical_valuation.py`: `ending_mv := roster currentValue` + an `ending_mv_source`
provenance column, exactly as `build_billing_dim.py` was repaired. The discriminator
(`ZERO-CONTRADICTED-BY-POSITIONS` / `ZERO-CORROBORATED` / `SOURCE-ABSENT`) is **PRESERVED** --
it stops being the VALUE path and becomes the PROVENANCE RECORD. Deleting it because the
value moved would remove the instrument that proves the move was coverage and not meaning.

## POPULATION COUNTS -- measured on the 2026-08-12 partition BEFORE the build

*Stated approximation, deliberately: these are SAME-DAY counts used as a proxy for the
prior-trading-day BMV population C_02 actually keys on. Exact per-day counts will differ
slightly; the CLASS SIZES are what is being pinned, not a per-day figure.*

| Instrument | Population | BEFORE | AFTER (predicted) | Reading it correctly |
|---|---|---|---|---|
| **C_02** twr_engine | UNCOMPUTABLE (zero/absent BMV -> `daily_r` returns None) | **423** | **111** | **SHRINKS BY 312 -- this is the CORRECT adjustment, NOT a regression.** 312 accounts stop being refused because they now have a real base; the 111 that remain are genuinely empty and must still be refused |
| **B_03** valuation_integrity | VARIANCE-EXPLAINED via `ZERO-CONTRADICTED-BY-POSITIONS` | **312** | **0 from this class** | The 312 LEAVE the explained class. A drop to zero here is EXPECTED and correct -- the class is empty because the defect it explained is gone, not because the instrument stopped working |
| **B_03** | NEW unexplained variances created by the repair | 0 | **0 (predicted)** | **All 312 freed accounts tie to positions TO THE CENT** (312/312 within $0.01, max abs delta $0.00) -- they land CLEAN, so the repair introduces no new variance population |
| **any** | `SOURCE-ABSENT` | unchanged | unchanged | the repair does not create activity rows; this class is untouched |

## THE COROBORATION THAT MAKES THE BASIS CHOICE SOUND (measured, not assumed)

On the 312 accounts where the activity plane reads 0.00, **roster currentValue == the
positions sum EXACTLY** (312 of 312, max delta $0.00). Two independent vendor planes agree to
the cent on precisely the accounts where the third plane was blank. That is why the ruled
basis is right and not merely bigger.

## FAILURE MODES DECLARED IN ADVANCE

1. **C_02 UNCOMPUTABLE does NOT shrink to ~111** -> the repair did not reach C_02's BMV read
   (it resolves prior-day fair_value; check the vintage path, not the value).
2. **B_03 shows NEW unexplained variances** -> contradicts the 312/312 tie measured here;
   investigate the tie vintage before assuming the repair is wrong.
3. **The 111 stop being refused** -> a REAL regression: genuinely-empty accounts must still
   be UNCOMPUTABLE. Absence serves as ABSENT, never as a computable zero.
4. **Total moves off $209,225,005.59** (same vintage) -> the repair did more than re-basis.
5. **The discriminator column disappears** -> the provenance instrument was deleted; the
   repair becomes undefendable even if its numbers are right.

## SCOPE

P1 SCRIPTS-phase emitter. Built in-lane, stays UNDEPLOYED pending normal P-phase sequencing.
The SERVED surface is already correct (it already computes on the roster basis, delta $0.00),
so this repair makes an undeployed emitter agree with the truth already being served -- it
changes no user-facing number.

## ⛔ PIN CORRECTED ~15:31Z, BEFORE THE BUILD -- 109 -> 111

The AFTER pin read **109**; the correct figure is **111**. Found by forcing the partition to
account for its own total: 312 + 109 = 421, but the zero class is 423. **312 + 111 = 423.**
Corrected in the table above before any code was written, so the pin this build is graded
against is the right one. The same error had propagated into my RESULT file and into reports
to Andrew and COO, where it also produced a FALSE identification of the separate 109-account
served-classification gap -- retracted there.

**Why it matters here specifically:** this is a POPULATION pin. Had the build been graded
against 109, the correct outcome (111) would have read as a 2-account regression -- the exact
failure CTO's pre-registration requirement exists to prevent, arriving through the pin itself
rather than through the instrument.
