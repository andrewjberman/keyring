# CTO~Z RULING -- THE DISPLAY-NAME ARCHITECTURAL HOME (Rule 17b), 2026-08-25 ~09:0xZ

**Seat:** `1.0.0_SA_CTO~Z` | **Assignment:** MSTR~Z 07:38Z spawn brief, Defect B, verbatim:
*"`1.0.0_SA_CTO~Z`: name the ARCHITECTURAL HOME first (Rule 17b -- display naming is SERVING-tier,
not bd-securities, not gold business logic) and make it GENERALISE. DS builds to that."*
**Builder:** `0.4.0_DS_ClientPlatform~Z`. **Fence:** Andrew 07:3xZ *"this and only this."*

---

## 0. THE RULING IN ONE LINE

> **The display-name map lives in `data/etfs/scripts/gold/etf_positioning_publisher.py` (STAGE 2,
> the platinum publisher), applied at the single existing `name` shaping site `:234`, keyed by
> constituent `ticker`, defaulting to THE INCOMING VENDOR STRING.**
> Gold keeps the issuer's string unchanged. No new table, no config object, no IAM grant, no monitor.

⭐ **RATIFIED, AND IT IS AN INDEPENDENT CONVERGENCE, NOT AN ENDORSEMENT.** `0.4.0_DS_ClientPlatform~Z`
reached this home from their own measurements (msg 8589, 07:56Z) while I reached it from mine, and
**neither seat had read the other when they wrote.** Where their evidence is stronger than mine I
have adopted theirs and said so (s.3). Where I hold something they do not, it is s.4 and s.6.

---

## 1. WHY THIS HOME -- THE ESTATE ALREADY BUILT IT; THIS IS THE FIRST NAMING QUESTION PUT TO IT

Rule 17b as amended 2026-08-11 already has a two-stage implementation for this exact product, and
both files say so in their own headers:

```
etf_positioning_gold.py       STAGE 1  -> opal-data-etfs/gold/{table}/date={D}/   PARQUET
etf_positioning_publisher.py  STAGE 2  -> opal-data-portal-v2/platinum/etfs/positioning_data.json
```
`etf_positioning_gold.py:7-9`, verbatim: *"gold is PARQUET and the platinum PUBLISHER is the estate's
ONLY JSON producer. That is what makes one-producer-per-served-key hold BY CONSTRUCTION."*

Rule 17b's serving clause names **display naming** explicitly as platinum-tier work. **So this is not
a new architectural decision -- it is the first time the existing architecture has been asked a
naming question, and its answer is unambiguous.** DS~Z adds the corroborating detail that the
publisher already carries this exact pattern with its own Rule-17b rationale in its own words
(`_weight_out` / `_aum_out` / `_active_out`, `:98` *"WHY THE CONVERSION LIVES HERE AND NOT IN GOLD"*).

**MEASURED CONVENIENCE, not merely legality:** the publisher shapes `name` at exactly **two** lines
in 458 -- `:234` (holding) and `:254` (book). One insertion point:

```python
:234    "name": _n(h["name"]),          ->    "name": _display_name(h["ticker"], h["name"]),
```
`:254` (book) is **NOT** touched -- s.5, all four book names already render correctly.

---

## 2. THE FOUR REJECTED HOMES

| # | home | verdict |
|---|---|---|
| 1 | `bd-securities` row | **FALSIFIED overnight.** Producer never reads it; it stores RAW vendor strings (`"APPLE INC COM"`) -- 142 of 150 names WORSE, 0 better. |
| 2 | gold business logic (`etf_positioning_gold.py:822`) | **RULED OUT, Rule 17b.** Doing a later layer's job early, and IRREVERSIBLE: gold parquet would stop carrying the issuer string, destroying re-derivability. Rule 17a's spine one tier up. |
| 3 | `etf-classifications` DynamoDB | **RULED OUT -- s.3. It is a different universe, and it is not even reachable.** |
| 4 | a title-case / string transform | **FALSIFIED ON LIVE BYTES -- s.4.** |

---

## 3. WHY `etf-classifications` IS THE WRONG TABLE -- AND THIS ANSWERS ANDREW'S ACTUAL QUESTION

His words: *"the SALXX state street money market entry that was adjusted in the etf-classification
table didnt seem to take, is that a missing terraform apply or something."*

**It is not a terraform apply. The deeper answer is that SALXX does not belong in that table at all.**

**(a) DIFFERENT UNIVERSE -- DS~Z's measurement, which is stronger than the grain argument I had
drafted, so I adopt it and retire mine.** I was going to rule on Rule-24(i) MECE grounds ("a
money-market fund is not an ETF"). That is true but weaker than what DS~Z measured:

```
ETF_NAME_OVERRIDES keys (etf_classification.py:661)                        116
ETF-mode served distinct tickers (platinum/etfs/positioning_data.json)     169
INTERSECTION                                                                 0
```
**Zero of 116 x 169.** `ETF_NAME_OVERRIDES` is the MODELS universe (models hold ETFs); ETF mode's
holdings are the UNDERLYING EQUITIES of DIVZ/IDVZ/PFDE/PFOE plus two money funds. **Wiring the ETF
path to that map would import 116 entries to use exactly 0 of them.** That is not one canonical
source; it is one bag with two disjoint contents. *A scope argument can be argued with; a
zero-intersection measurement cannot.*

**(b) NOT REACHABLE ANYWAY -- deployed bytes, not the tree (Rule 22a CODE layer).** DS~Z downloaded
the package: `etf-positioning-producer` contains exactly **2 members** (`etf_positioning_gold.py`,
`etf_positioning_publisher.py`), both raw-sha identical to their repo files. **`_shared/etf_classification.py`
is not in the package.** Using it needs a PACKAGING change to a Lambda that reached PROD tonight --
out of proportion to the fence, for 0 shared keys.

**(c) IT IS ALREADY A TWO-CARRIERS DIVERGENCE SURFACE, DOCUMENTED IN ITS OWN SOURCE.**
`etf_classification.py:672-676` records that `seed-etf-classifications.py` writes
`name=OVERRIDES.get(ticker, ticker)`, that 59 ticker-as-name placeholders were seeded and remediated
on 2026-08-18, and instructs *"keep both in sync"* by hand. **Adding a third consumer widens a
divergence surface whose own maintainers wrote down that it drifts.** *(Live instance now measured --
s.6 item 2.)*

⛔ **AND THIS IS WHY REMEDY 3 WAS THE DANGEROUS ONE.** `seed-etf-classifications.py:62` defaults to
**the ticker**, so a miss writes the literal `"SALXX"` -- **strictly worse than today, and it looks
like it worked.** Inverting that default is R3 below and it is the load-bearing requirement.

---

## 4. THE CLASS IS NOT "ALL-CAPS" -- THE TWO INSTRUMENTS FAIL BY DIFFERENT MECHANISMS

Read from `s3://opal-data-portal-v2/platinum/etfs/positioning_data.json`
(`generated_at 2026-08-25T04:53:48Z`, `data_as_of 2026-08-24`, 187 holding rows, 4 books):

```
SALXX  'STATE STREET INST U.S. GOVERNMENT MMKT ADMN CLASS'    <- all-caps issuer house style
FXFXX  'First American Treasury Obligations Fund 01/01/2040'  <- ALREADY CORRECTLY TITLE-CASED.
                                                                 A FABRICATED MATURITY DATE on a
                                                                 money-market fund, which has none.
positive control  AAPL          -> 'Apple Inc'   (readable -- the instrument discriminates)
negative control  ZZZNOSUCH9999 -> ABSENT        (the probe discriminates)
```

>> **A TITLE-CASE TRANSFORM FIXES NEITHER, AND THE TWO FAILURES ARE NOT THE SAME KIND OF THING.**
On SALXX it yields *"State Street Inst U.S. Government Mmkt Admn Class"* -- wrong three ways at once
(INST kept, MMKT de-capitalised, ADMN CLASS kept). On FXFXX it is a **NO-OP**, because FXFXX is
already correctly cased and its defect is a **fabrication**, not a casing. **You cannot transform
your way out of a fabricated substring.** <<

This converts CVO's overnight caution (*"the all-caps set is 7, not 6, and it is NOT homogeneous"*)
from a warning into a measurement. **The class is UNREADABLE VENDOR DISPLAY STRINGS, and its members
fail by at least three distinct mechanisms** -- casing, fabricated tokens, and truncation (s.6
item 1). **One map, N mechanisms: that is the shape a map is for and an algorithm is not.**

---

## 5. THE COHORT IS BOUNDED -- 6 rows, 3 tickers, only 2 need an override

```
DIVZ  SALXX       STATE STREET INST U.S. GOVERNMENT MMKT ADMN CLASS   -> OVERRIDE
IDVZ  SALXX       STATE STREET INST U.S. GOVERNMENT MMKT ADMN CLASS   -> OVERRIDE
PFDE  FXFXX       First American Treasury Obligations Fund 01/01/2040 -> OVERRIDE
PFOE  FXFXX       First American Treasury Obligations Fund 01/01/2040 -> OVERRIDE
PFDE  CASH&OTHER  Cash & Other       -> NO OVERRIDE. Readable, AND it is a SENTINEL rather than a
PFOE  CASH&OTHER  Cash & Other          security (gold's VENDOR_CASH_SENTINELS). Overriding a
                                        sentinel would give a bookkeeping line a security's name.
```
**BOOK names: all four already correct** (`Polen Dividend Income ETF`, `Polen International Dividend
Income ETF`, `Pathfinder Disciplined US Equity ETF`, `Pathfinder Focused Opportunities ETF`).
**Do not touch `:254`.** *(One caveat filed at s.6 item 2 -- it is NOT a licence to edit `:254`.)*

---

## 6. FILED, NOT FIXED -- fence holds. To `2.0.0_SA_COO~Z` + `3.0.0_SA_CVO~Z`. No action tonight.

1. **A THIRD FAILURE MECHANISM IN THE SAME FIELD: VENDOR TRUNCATION AT 30 CHARS.**
   `IDVZ ICT -> 'International Container Termin'` -- cut mid-word at exactly 30 characters (measured,
   live served bytes). Named by nobody tonight, and **it proves the class is wider than the two
   instruments in scope.** The map absorbs it the day someone adds a row; no design change needed,
   which is the point of ruling for a map rather than a transform.
2. **TWO SERVING SURFACES DISAGREE ON A CLIENT-FACING FUND NAME.** ETF positioning serves
   `DIVZ = 'Polen Dividend Income ETF'`; models-side `ETF_NAME_OVERRIDES` carries
   `DIVZ = 'Opal Dividend Income ETF'` with the inline comment *"Opal-branded (registry + served
   canon; ex TrueShares label)"*. Same fund, two homes, two names. **I cannot tell from here which is
   correct -- it is a branding question, not an engineering one.** This is exactly the two-carriers
   hazard s.3(c) predicts, now measured live. ⛔ **NOT a warrant to edit `:254` tonight.**
3. Leftover promote worktree directories -- already filed by MSTR~Z; I add nothing.

---

## 7. THE SPEC DS BUILDS TO -- R3 is load-bearing

**R1 HOME.** `etf_positioning_publisher.py`; module-level `DISPLAY_NAME_OVERRIDES: dict[str, str]`
beside the other ADDRESSES constants. **Nothing in `etf_positioning_gold.py` changes.**

**R2 KEY.** Constituent `ticker`, normalised the way gold already normalises at `:805`
(`str(...).strip().upper()`). **Do not invent a second normalisation.**

**R3 DEFAULT -- INVERT THE FALSIFIED REMEDY.**
```python
def _display_name(ticker, vendor_name):
    return DISPLAY_NAME_OVERRIDES.get(_norm(ticker)) or vendor_name
```
**The fallback is THE INCOMING VENDOR STRING -- never the ticker, never None, never a placeholder.**
A miss degrades to *exactly today's behaviour*, so the 167 untouched tickers are byte-identical **by
construction, not by care**. `seed-etf-classifications.py:62` falls back to the KEY; this falls back
to the NAME. **Same idiom, opposite blast radius** (DS~Z's formulation, adopted).

**R4 SCOPE OF EFFECT.** `name` ONLY -- never `ticker`, `cusip`, or any join/sort key. A display
concern that reaches an identity field becomes an identity defect. `:234` only.

**R5 VALUES -- TWO tickers.**
```python
"SALXX": "State Street U.S. Government MMKT",   # Andrew's ruled string, not in question
"FXFXX": "First American Treasury Obligations Fund",   # RULED, s.8
```

**R6 EXERCISE, DO NOT ASSERT.** A test that fails if the map is wrong: the override fires for
SALXX/FXFXX **and** an absent key returns the vendor string unchanged -- **write the refuse fixture;
name the input that makes it fall through.** A map never exercised on a MISS has not been tested,
and the miss path is the one carrying the entire safety property.

**R7 NO NEW INFRASTRUCTURE.** No DynamoDB, no S3 config, no seeder, no IAM grant, no alarm/monitor
(07-28 moratorium). Build-ladder rung 2 is satisfied by reusing the estate's **PATTERN** without
reusing its **TABLE**. An S3 config would add a fetch that can fail *at serving time*, converting a
cosmetic concern into a serving-path dependency; an in-code dict deploys atomically with its only
reader, diffs in review, and has no second home to diverge from.

---

## 8. DS~Z'S TWO HELD QUESTIONS -- BOTH ANSWERED, NEITHER HELD

**(1) Z-S48 divergence (BP / GSK / MPLX, and JPM / MRVL / VZ): DS~Z IS CORRECT. TWO tickers, not
four or six.** Andrew named SALXX; MSTR~Z added FXFXX as same-class; *"this and only this"* is the
fence. **Flagging the divergence from the published oracle rather than silently narrowing it is the
right act and I am ratifying it, not merely permitting it.** `2.0.0_SA_COO~Z` owns Z-S48 and re-scopes
it; the acronym-company fork (an acronym is not an unreadable string -- `BP` is the company's actual
name) is a product call that stays at Andrew.

**(2) FXFXX's target string: I RULE IT, and I am naming which half is which.**
DS~Z flagged it as *"a product judgment wearing a measurement's clothes"* -- correct and well
caught, so I split it:
- **Dropping `01/01/2040` is a CORRECTNESS fix, not a naming preference.** A money-market fund has
  no maturity date; the token is fabricated. Removing fabricated data from a client-facing field
  needs no product ruling.
- **The residue -- "First American Treasury Obligations Fund" -- is a naming judgment**, and it is
  Andrew's SALXX pattern (issuer + fund, no share-class suffix) applied to the sibling.
**SHIP IT.** I am RULING rather than carding it, because the alternative is serving a fabricated
date for another day, and **his instruction was to fix it now**. ⭐ **It goes to Andrew as an FYI,
overridable in one word** -- not as a gate on anyone (NEVER#5).

---

## 9. THE RUNG THAT IS NOT MINE, RESTATED SO IT DOES NOT FALL IN A SEAM

`2.0.0_SA_COO~Z` is right that a code fix does not move served bytes. **This ruling is discharged
when the ARTIFACT carries the string, not when the code does.** Rung 2 (`DS~Z`+`AE~Z`) is an
**ad-hoc QA publish**, expressly permitted by CLAUDE.md -- **its artifact is PROOF, never production
evidence; `cron(0 13)` remains the production number.** Rung 3 (production render) is
`0.2.0_DT_PortfolioAnalytics~Z`'s and **is not discharged by anyone's local screenshot.**

---

## 10. GROUNDING (denominators printed, Rule 22)

| claim | instrument | result |
|---|---|---|
| served names + cohort | `aws s3 cp` live platinum key -> python | 187 rows / 4 books; SALXX+FXFXX as quoted; controls AAPL present, ZZZNOSUCH9999 absent |
| `sub_asset_class` on every holding | same artifact | 13 values / 187 rows -- **re-derives MSTR~Z's distribution exactly** (IT 35 / Fin 31 / HC 23 / Ind 21 / Staples 16 / Comms 15 / Disc 14 / Util 10 / Energy 9 / UltraShort 4 / Materials 4 / Cash&CE 2 / null 3). **Defect A is frontend-only, CONFIRMED at a second seat on the live bytes.** |
| zero intersection of the two universes | DS~Z msg 8589, re-stated here | 116 x 169 -> **0** |
| `_shared/` not in the deployed package | DS~Z, `lambda get-function` package download | 2 members, both raw-sha identical to repo |
| SALXX/FXFXX absent from both models maps | `comp-find -i` | 219 / 26,447 and 132 / 26,447 files scanned; zero in either map |
| the two `name` shaping sites | `grep -n` on the publisher | `:234` holding, `:254` book -- 2 of 458 lines |
| vendor raw string | `.runtmp_ac4/divz.csv:2`, `idvz.csv:33` | `STATE STREET INST U.S. GOVERNMENT MMKT ADMN CLASS` |
| the DDB hand-sync obligation | `etf_classification.py:672-676` | verbatim *"keep both in sync"*; 59 placeholders remediated 2026-08-18 |

**Vintage:** repo citations at `10750a9a7c` (= `origin/SITEZ`, 0 ahead, no MERGE_HEAD). Live reads
2026-08-25 ~08:5x-09:0xZ, **UTC plane** (`s3 cp` + python -- not `s3 ls`, which renders LOCAL time
with no marker).

-- `1.0.0_SA_CTO~Z`
