# ANDREW-DIRECT 2026-09-11 ~04:2xZ -- "ETFClassifier is the real one"; the Positioning page is the instrument

**archetype:** SCRIBE

**Received at:** the `2.0.0_SA_COO~Z` terminal · **Recorded by:** `2.0.0_SA_COO~Z`, same turn
**Subject:** `POSN_ASTTAX` / `ASSETCLASS_TAXONOMY` -- `C-ONE-SOURCE`, the FWD-5 source adjudication

## VERBATIM -- three consecutive messages, quoted whole, not paraphrased

> **"make sure you get the canonical one between these"**
>
> **"I think ETFClassifier is the real one"**
>
> **"check to see what is already hooked up to Positioning page thats how youll kow for sure"**

## Scope, relayed and NOT adjudicated wider or narrower

He ruled on **which classification source is canonical**, and -- more valuably -- **named the
instrument that settles it**: what the Positioning page is already wired to. He did not rule on the
five classes, the membership edges, the rename, or the D4 enum.

## EXECUTED SAME TURN. His prior is CONFIRMED, and the instrument he named is what confirmed it.

**`infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py`**

```
  :25   from etf_classifications_dynamodb import ETFClassifier
  :31   etf_classifier = ETFClassifier()
```

`yang-generate-holdings-attribution` vendors the same module. **Both Positioning lambdas run
ETFClassifier. He is right.**

⭐ **AND THE INSTRUMENT HE NAMED BEAT THE ONE I WAS USING.** I had been reading the two modules'
own headers, and **both of them claim to be the single source of truth** --
`etf_classification.py:39` ("This is the single source of truth for ETF asset class classification")
and `etf_classifications_dynamodb.py:7` ("This replaces scattered inline hardcoded mappings with a
single source of truth"). Two self-reports, flatly contradictory, and no way to choose between them
from the text. **The consumer settles what the producers' self-descriptions cannot** -- which is
CLAUDE.md's own "never trust a producer's self-report" arriving as a one-line instruction.

## ⛔ AND FOLLOWING HIS INSTRUMENT ALL THE WAY CORRECTED MY OWN DRAFT

I had written that these are **two independent competing sources**. That is what their headers say. It
is **wrong**, and the seed script is what shows it:

```
  infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-classifications.py
  :58   "asset_class": ETF_CLASSIFICATIONS.get(ticker, "unknown"),
```

`ETF_CLASSIFICATIONS` is the hardcoded dict from `etf_classification.py`. So the real shape is **ONE
CHAIN, NOT A FORK**:

```
   etf_classification.py            the hardcoded ETF_CLASSIFICATIONS dict     [AUTHORING source]
            |
            |  seed-etf-classifications.py   WRITES
            v
   DynamoDB  etf-classifications                                               [STORE]
            |
            |  ETFClassifier (etf_classifications_dynamodb.py)   READS
            v
   Positioning page                                                            [SERVING source]
```

**Both halves of his sentence are therefore true at once:** ETFClassifier IS the real one -- it is what
Positioning runs -- **and** the hardcoded module is not a rival to be retired, it is the thing that
SEEDS what ETFClassifier serves.

⛔ **THE CONSEQUENCE FOR FWD-5, WHICH IS THE OUTCOME THIS DECIDES.** FWD-5's bar is *"a person changes
an asset-class definition once, in one place, and everywhere reflects it."* Today there are **two
different "one places" with different failure modes**, and the record states both rather than choosing:
- change the **DynamoDB table** (what ETFClassifier reads) -> serves immediately, and **the next seed
  run silently overwrites it from the hardcoded dict**;
- change the **hardcoded dict** -> durable, but **nothing serves it until the seed is re-run**, and the
  seed's trigger was not measured here.
**Neither is "one place" as FWD-5 means it.** That is the substance S1-a must settle, and it is now a
decision with its facts on the table rather than a search.

## Two further measurements taken while the instrument was in hand

⚠ **THE LIVE POSITIONING VOCABULARY IS FOUR VALUES AND MATCHES NO DOCUMENT.** In
`yang-generate-positioning/lambda_function.py` the live branch set is **`cash | fixed_income | equity |
hedge`** (`:362-368`) -- `cash` is its own class, and `unknown` is not branched at all. The hardcoded
module documents **three** (`'fixed_income' | 'equity' | 'other'`, `:38`); the DynamoDB module documents
**four** (`fixed_income | equity | hedge | unknown`, `:91`). Three documents, three different
vocabularies, none of them the PRD's ratified five.

⛔ **THREE UNKNOWN-TICKER DEFAULTS IN ONE FILE, AND THEY DISAGREE WITH EACH OTHER.**
`:209` defaults unknown -> **`fixed_income`** ("Default to FI if unknown"); `:360` and `:520` default
unknown -> **`equity`**. Same handler, same run, opposite fallbacks. This lands directly on **FWD-1**
(*every holding in exactly one class*) and on **FWD-2** (*vol/hedge no longer inflating equity*): an
unrecognised volatility product is absorbed into Equity by `:360` today, with nothing to see. It is a
cause of the Cottonwood symptom that is **independent of the vol/hedge mapping** the PRD's
`C-VOL-HEDGE-STRUCTURED` addresses -- fix the mapping alone and this remains.

## What this record does NOT do

No cell cut, no task order, no code changed, no source retired, no PRD amendment proposed. The D4 enum
record @`425b11ccb1` and the rename remain as they were. `C-MEMBERSHIP-AT-L5` is untouched -- the edges
stay the cells'.

**Push state:** LOCAL at authorship; `0.0.0_AB_MSTR~Z` holds all pushes.
