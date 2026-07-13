# OPAL_ASSETS -- ANDREW RULING, 2026-07-13: **RECORD THE COMPONENTS. THE SUM IS A PRESENTATION DECISION.**

**archetype:** COORDINATE
**Recorded + broadcast same turn per `org/XXX.md`. Relayed by `2.0.0_SA_COO`. Owner: `1.0.0_SA_CTO~B`.**

## THE RULING -- VERBATIM (Andrew -> COO, interactive, 2026-07-13 ~22:05Z)

> # ***"They're both right but for different reasons, we just need all the components granularly recorded daily, how we sum them is dependent on the presentation case."***

### ⚠️ PROVENANCE -- READ BEFORE CITING
I first put a **multiple-choice** to him and he selected *"Both -- report them separately (a fee-paying headline +
an ETF-inclusive total, each labelled)."* **He then wrote the sentence above, unprompted, and it is STRICTLY SHARPER
than my option.** My option assumed **TWO BLESSED TOTALS**. His ruling says **N COMPONENTS AND ZERO BLESSED TOTALS.**
> **The option text is MINE and is SUPERSEDED. The sentence above is HIS and BINDS.**
> **DO NOT CITE MY OPTION -- it is a worse answer wearing his authority.**
*(Same discipline CTO applied to `"8.) A."`: an option letter selected off a list an agent wrote is **not** a
sovereign sentence. Tonight's `MEMORY.md` lesson -- a verbatim quote without its scope is a future contradiction with
a citation -- has a twin: **an agent's own text, laundered into the sovereign's voice, is a future error with his
authority behind it.**)*

## THE ARCHITECTURE IT DICTATES
```
STORE   COMPONENT-GRAIN. One row per component per day -- all 14 cohorts, every partner, every fund, UN-SUMMED.
        A TOTAL IS NOT A PRIMITIVE AND IS NOT STORED AS ONE.
READ    Summation happens AT READ TIME, per PRESENTATION CASE. Different question -> different roll-up.
        EVERY emitted total DECLARES ITS CASE. An unlabelled total IS the bug.
```

## >> WHY BOTH WERE RIGHT, AND THE DEFECT THAT MADE THEM LOOK OPPOSED <<
> # **`additive=TRUE/FALSE` IS NOT A PROPERTY OF AN ASSET. IT IS A PROPERTY OF THE QUESTION.**
> **We froze a PRESENTATION decision into STORAGE.** Once `etf_fund additive=FALSE` became a stored column, the store
> had **already silently answered "which question are we asking?"** -- for every future reader, forever, without
> saying so. Manav asked a question in which Opal's own ETFs count. We asked one in which they do not. **BOTH ARE
> CORRECT.** The store could express only one, so the other surfaced as a **$685.64mm discrepancy**.
> ### **IT WAS NEVER AN ERROR. IT WAS A MISSING DIMENSION.**

**Same organ as every other bug in the 07-13 cluster: NO CHANNEL FOR "IT DEPENDS," SO A CONDITIONAL WAS RENDERED AS A
FACT** -- `comp-which`'s argmax-as-confidence; `check-inbox`'s *"No pending messages"* over a live escalation; the
halt gate's confident **wrong** principal; a REGISTRY row's 12-day-dead *"HELD, do NOT dispatch"* while the site was
serving. **Here: no channel for the QUESTION, so the ANSWER got baked in.**

## THE ARITHMETIC IT DISSOLVES (CTO, tied to Manav's sheet to 0.05%)
```
our served additive headline                                          $1,758.11 mm
  + the 4 ETF FUNDS  (etf_fund additive=FALSE; MANAV COUNTS THEM)          +685.64   <- NOT A BUG. A DIFFERENT QUESTION.
  + 49F staleness    (his 7/10 1713.23 vs our as_of 07-06 1621.25)           +91.98   <- a REAL defect
  - Inflection diff  (ours 136.86 vs his 132.50)                              -4.36   <- a REAL defect
Manav's Total Fee Paying AUM                                         $2,532.55 mm
```
**Only the 49F staleness and the Inflection diff are DEFECTS.** The $685.64mm is a **DEFINITION**, and it is now a
**DIMENSION** instead of a hidden default.

## IT ALSO PRE-SOLVES THE $290mm SMArtX GAP (DS's open item)
Ours `1400.96` vs Manav `1691.11`. Our value is approximately the **sum of the 5 Opal models (`1404.94`)** -- so we
are labelling **"the SMArtX PLATFORM total"** with what is really **"the OPAL-MODEL SUBSET of it."**
**A NAME THAT IS NOT THE COMPUTATION -- the identical defect, one cohort over.**
Under this ruling the fix is **not to pick a number**: record **BOTH components** (platform total AND Opal-model
subset) at grain and let the presentation case choose.
> ⚠️ **SMArtX is DS's and it is a HYPOTHESIS -- NOT source-confirmed.** Rule 22: a hypothesis cannot authorize a fix.
> **This ruling tells you the SHAPE of the answer, not that the answer is in hand. Do not let it close the item on a
> plausible story.**

## WHAT THIS AUTHORIZES -- AND WHAT IT EMPHATICALLY DOES NOT
- **AUTHORIZES:** a PRD/schema input to **CTO~B** (macro-project owner) -- component-grain daily store, no stored
  totals, roll-up as a labelled read-time view. **COO relays; CTO~B decomposes; DS owns the emitter lane.**
- **DOES NOT AUTHORIZE:** flipping `additive`, re-deriving served artifacts, or any gold run.
  **THE INF CHAIN STAYS HELD.** *A definitional ruling is not a pipeline authorization.*
- ⛔ **AND ABOVE ALL: IT DOES NOT AUTHORIZE "JUST REFRESHING THE STALE AUM HEADLINE."**
  OPAL_ASSETS' loudest symptom is a frozen AUM number. **DOOR 6:** `mdpf-daily-trigger` is **event-driven on the INF
  spine sentinel** -- **one `aws s3 cp` of a ~40-byte key (`opal-data-inf/gold/meta/pipeline-complete.json`)
  DISPATCHES THE HELD CHAIN**, routing around BOTH the chokepoint and the collision.
  > ### **THE AGENT ACTING ON THIS RULING IS THE AGENT MOST LIKELY TO BE HANDED THAT "FIX." DO NOT WRITE THAT KEY.**
  > *Functional, not lexical: never "does it say INF?" -- always **"would doing this ADVANCE THE INF CHAIN?"***
