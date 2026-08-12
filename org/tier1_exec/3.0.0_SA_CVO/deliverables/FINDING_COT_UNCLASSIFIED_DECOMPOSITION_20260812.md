# FINDING -- the Cottonwood UNCLASSIFIED mass, decomposed at the security level
## + A CORRECTION TO MY OWN BROADCAST CLAIM ("not a code fix" was WRONG for ~6% of it)

**Author:** 3.0.0_SA_CVO · **2026-08-12 ~1330Z** · **archetype:** VALIDATE (ad-hoc QA read, run-and-read,
nothing standing). **For:** Andrew-direct ("for securities im looking into it with CVO now", relayed COO
132807Z) -- this is the substance behind the decision.
**Method:** the SHIPPED `classify()` (imported from `a07_dim_asset_classification.py`, the ported
classifier) run against Cottonwood's LIVE silver holdings (`s3://opal-data-assets/blackdiamond/cottonwood/
silver/fact_holdings/date=2026-08-10/data.parquet`), DynamoDB `bd-securities` materialized at read
(9,393 items / 7,620 aliases). **GRAIN LAW HONORED:** collapsed to unique (AccountID, AssetID) BEFORE any
sum (relationship-grain double-count; 2 duplicate rows dropped of 17,140).

## ⛔ THE CORRECTION I OWE FIRST
I told COO (and it reached Andrew, and it is in the arbiter's WHAT-ANDREW-SHOULD-HEAR section):
*"The $113.2M UNCLASSIFIED is a data-curation decision, NOT a code fix."* **The "not a code fix" clause is
WRONG for ~$4.3M of it.** There is a genuine, reproducible classifier BUG. My two-delta conclusion (that
the mass is classification CONTENT, not carry MECHANICS) still holds for ~87% -- but I overstated it into
"no code fix exists," and that framing went to Andrew. **The measurement below is what I should have run
before making the claim: I concluded from two deltas' failure that no code remedy existed, without
enumerating the securities themselves.** Absence of a remedy I had tried is not absence of a remedy.

## THE MEASURED PICTURE (2026-08-10 partition)
Book (account-grain) **$482,567,772.65**; UNCLASSIFIED **$76,122,795.21 = 15.77%**, 276 positions, 141
distinct securities. Top 10 names = 83.7% of the mass. *(~B measured $75.09M on an earlier partition --
same population, different date.)* Class split: equity $233.7M / fixed_income $129.3M / **UNCLASSIFIED
$76.1M** / alternatives $25.1M / cash $18.3M.

| # | Family | Dollars | % | Kind of remedy |
|---|---|---|---|---|
| C | **"Voya"** -- ONE line, 4 positions, ticker `4175_VOYA`, no fund detail | $25,973,104 | 34.1% | **VENDOR LOOKTHROUGH** (no content to classify) |
| B | **CCA private LPs** (Eiger, Eiger III, Saxum, FC Houston "Opportunity LP Capital Values") | $20,180,720 | 26.5% | **RULE or CURATION** -- unambiguously alternatives |
| A | **Held-away personal assets** (`CXMANUAL_*`: Home, LLC, Trust, Brokerage, Primary Residence, Insurance, Investment Property, Car, IRA, Bank Account, 401K) | $19,972,032 | 26.2% | **TAXONOMY DECISION** -- see below |
| E | Retirement-plan fund units (synthetic `BD*`/`BA-` tickers, `3665 MFS Growth Fund R6`) | $5,004,461 | 6.6% | CURATION |
| D | **Bank CDs / notes** (`VALLEY NATL BK PASSAIC N J 3.9% 2026`) | $3,556,935 | 4.7% | ⚠ **CODE BUG** |
| F | Long tail (incl. `BERKSHIRE HATHAWAY INC DEL CL A` $793,815) | $1,435,542 | 1.9% | mixed; ~$0.79M code |

## ⚠ THE CODE BUG (family D, $3,556,935 / 44 names) -- AND IT IS LIVE IN THE SERVED MIX TODAY
`_RE_FI` carries the alternative `\b\d+\.?\d*%\b`. **The TRAILING `\b` after `%` can never match when a
space follows** (`%` is non-word, space is non-word -> no boundary), so every `<rate>% <year>` name falls
through. EXERCISED, positive-controlled:
- shipped pattern on `VALLEY NATL BK PASSAIC N J 3.9% 2026` -> **False**
- same pattern with the trailing `\b` dropped -> **True**
- NEGATIVE CONTROL `Investor Manual Asset - Car` -> False under BOTH (the fix does not over-match)
**Because the A_07 port is byte-identical to `data/black_diamond/scripts/gold/lib/etf_classifier.py` (I
verified that on the A_07 cert), THE CURRENTLY-SERVED MIX CARRIES THE SAME BUG** -- Cottonwood's served
fixed-income is under-stated by ~$3.56M today. New and served AGREE precisely because they share the
defect: shared-derivation agreement masking a shared defect, which is my own parity bar's
MATCH-KNOWN-WRONG class. The A_07 PARITY-VS-SERVED control could not have caught it -- that control asks
"does the port RECLASSIFY," and a faithfully-ported bug answers no.
**SECOND, SMALLER (family F, $793,815):** the equity fallback is `re.fullmatch(r'[A-Z]{1,5}', ticker)`, so
a DOTTED share-class ticker (`BRK.A`) fails it -- Berkshire Hathaway Class A, with a valid CUSIP, lands
unclassified.

## THE THREE GENUINE DECISIONS (Andrew's, not mine)
1. **Family C, $26.0M (34%) -- the "Voya" lookthrough.** A third of the mass is ONE undifferentiated line.
   No classification rule can classify a line with no content; this is a question about what Black Diamond
   delivers (or a manual tag).
2. **Family A, $20.0M (26%) -- held-away personal assets are a TAXONOMY question, not a coverage gap.**
   Primary residences, cars, bank accounts, LLCs, insurance. **Forcing a client's house into
   equity/fixed-income/alternatives is wrong in all three directions.** The honest remedy is likely a
   FOURTH class (held-away / real assets), which is a Rule-24 axis decision about what the mix chart
   represents -- product, not validation. ⛔ Note the interaction: the served 49F convention EXCLUDES
   unclassified from the top-level 3-class mix, so a fourth class is a served-shape question too.
3. **Family B, $20.2M (26%)** -- the CCA LPs are unambiguously alternatives; the only question is rule vs
   curation. `_RE_ALT` has no `LP` / `Opportunity` term.

## WHAT I AM NOT DOING
Not routing a fix, not opening a curation workstream, not pre-building rules (COO is holding AE + DS off
the same line; the next word is Andrew's or mine, and I asked him). This record exists so the decision is
made on the securities themselves rather than on an aggregate. Full 141-row list:
`C:\Users\ANDREW~1\AppData\Local\Temp\claude\C--Users-AndrewBerman-Desktop-ajb-workspace\cd125c37-ff8a-45d2-9404-e3c2d647bc80\scratchpad\cot_unclassified_full.csv`
(session-scratchpad, fragile -- say the word and I land it as a committed deliverable).

-- 3.0.0_SA_CVO
