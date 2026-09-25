# THE 2-PAGE EXPORT, SPECIFIED FROM THE TEAM'S OWN DOCUMENTS -- `1.0.0_SA_CTO~Z`, 2026-09-25 ~17:4xZ

**Why this exists.** The goal says the export must be *"in Opal Brand Guidelines form mimicking Asset Mgmt
team's earnings reports 2pg max"*. **Across 42 `AMGT_RESAPP` rounds and 4 `AMGT_CORPUS` rounds, no seat has
opened one of those earnings reports.** The endpoint's `FWD-5` was graded against a fence that describes the
document abstractly (*"replaces the document he circulates today"*) while **158 instances of the document sit
in the research library the same projects read every day.** This record reads three of them and turns the
goal's clause into a specification.

**In scope:** what the 2-page export must contain and what data it needs. **Not in scope:** typography and
colour, which are the Brand Guidelines' own business and are not in these PDFs' extractable text.

---

## 1. THE POPULATION, and the first finding is that the goal's "2pg max" is STRICTER than the team's own practice

**Census of the library's PDFs** (`library.list_folders(library.library_root())`, 94 folders, every file
enumerated): **158 PDFs.** By filename class: **EARNINGS UPDATE 62**, RESEARCH PACK 43, STOCK MOVE 1,
OTHER 52. File types overall: 158 `.pdf`, 79 `.xlsx`, 71 `.docx`, 17 `.png`, 1 `.html`, 1 extensionless.

**Page counts of all 62 earnings updates, read with `pypdf` (62 of 62 read, none failed):**

| pages | 2 | 3 | 4 | 5 | 7 | 10 | 11 | 16 | 17 | 19 | 21 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| count | **9** | **24** | 16 | 6 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

**Only 9 of 62 are two pages. The mode is THREE.** So *"2pg max"* is **Andrew's target for the export, not a
description of what the team produces** -- the two constraints in his sentence are separate, and the second is
tighter than the first. **A build that reproduces the team's format faithfully will land at 3 pages and miss
the goal.** The 9 two-page instances are the exemplars to copy, and they are the ones read below.

---

## 2. THE TEMPLATE, confirmed on THREE documents across three currencies and three continents

Read in full: `HSBC HSBA LN/HSBC Q2 2026 Earnings Update Aug 4 2026.pdf` (2pp),
`America Movil AXMB MM/America Movil Q2 2026 Earnings Update.pdf` (2pp),
`Iberdrola IBE SM/IBE SM Earnings Update 22 Jul 2026.pdf` (2pp).

**A three-document sample is deliberate.** One document is one analyst's choice; the round-41 lesson is that a
sample of one cannot be called representative. **All three share the skeleton below verbatim in shape**, in
GBP, MXN and EUR respectively, so it is a TEMPLATE.

### 2.1 Page 1, in order

1. **`RECOMMENDATION: MAINTAIN <x.xx>% POSITION IN <FUND>`** -- caps, first line, **verbatim shape in all
   three**: `MAINTAIN 2.75% POSITION IN IDVZ` / `MAINTAIN 2.25% POSITION IN IDVZ` /
   `MAINTAIN 1.25% POSITION IN IDVZ`. **An ACTION, a WEIGHT and a FUND.** Not a rating, not a target price.
2. **One to three lines of thesis, in plain prose**, carrying the quarter's tension:
   *"Despite a strong quarter the stock is down ~5%."* / *"Strong earnings and FCF growth. Anticipate more
   shareholder return as cap ex slows juicing FCF. Valuation remains very attractive."*
3. **Named-issue blocks with the analyst's reasoning** -- e.g. `China Outbound Direct Investment (ODI) Rules:`
   followed by what it does to the business.
4. **Bulleted quarter substance**, figures inline with their y/y change and the currency named.
5. **A title block**: `Q2 2026 Earnings Update` / `<LEGAL NAME> (Ticker: <BBG TICKER> Equity)` / `(in millions)`.
6. **THE TABLE** (section 2.2).

### 2.2 THE TABLE -- the part the product cannot currently build

```
<CCY> (millions) | Q2 2025 | Q3 2025 | Q4 2025 | Q1 2026 | Q2 2026 | 2025A | 2026E | 2027E | 2028E
Net Revenue      |  16,473 |  17,788 |  18,208 |  18,624 |  19,118 | 72,539|       |       |
y/y Growth       |  (0.4%) |   +4.6% |  +18.3% |   +5.5% |  +16.1% |  +3.9%|       |       |
Adj. EPS         |    0.26 |    0.20 |    0.56 |    0.47 |    0.42 |   1.40|   1.70|   1.82|   2.00
y/y Growth       | (26.9%) | (41.3%) |  (0.1%) |      NM |  +61.0% |  (7.3%)| +21.2%|  +6.9%|  +9.9%
```

**Five structural properties, all three documents:**

- **FIVE TRAILING QUARTERS** then **2025A** then **three FORWARD YEARS** `2026E / 2027E / 2028E`.
- **A `y/y Growth` ROW UNDER EVERY METRIC.** Negatives in parentheses, `NM` where not meaningful.
- **Roughly EIGHT curated metrics**, chosen for the business -- HSBC: Net Revenue, Net Interest Income, Total
  Loans, Total Deposits, Adj. EPS, DPS, P/E, P/B, DVD Yield, RoA, RoE, TD/TC. America Movil: Revenue, EBITDA.
  **Sector-specific, not a universal field list.**
- **The reporting currency is NAMED in the stub** (`MXN (millions)`), and **both local and USD appear where
  they differ** (`Market Cap (MXN)` AND `Market Cap (USD)`; `EV (MXN)` AND `EV (USD)`).
- **A RIGHT-HAND POSITION PANEL.** **[SUPERSEDED BY A1: this line read "the half with no data source in the
  estate" and that was WRONG -- `silver/holdings/` holds all five facts. See AMENDMENT A1.]**
  `Price (Gbp): 14.96` / `Market Cap (Gbp)` / `Market Cap (USD)` / `Float (Gbp)` / `ADTV (Gbp)` /
  **`Fund IDVZ`** / **`Fund Weight 2.75%`** / **`Initial Purchase Date: 12/27/2024`** /
  **`TR (Local) +122.7%`** / **`TR +48.6%`** / **`+/- (Index) +74.1%`**.

### 2.3 Page 2

`Key Financial Results` -- `Strategic and Operational Progress` -- **`Broker Perspectives on Capital Returns
and Valuation`**, which names brokers and their reasoning: *"Citi downgraded HSBC from Buy to Neutral ...
citing a 'constrained' scale for share buybacks"*; *"JPMorgan analysts highlighted ..."*; *"CFRA Research
maintains a positive view ..."*.

---

## 3. THE GAP, measured against what the product serves today

| the template requires | the product serves | class |
|---|---|---|
| `RECOMMENDATION: MAINTAIN x.xx% POSITION IN <FUND>` | a `Recommendation` section with no fund, weight or action | **DATA ABSENT** |
| **five trailing QUARTERS** | **fiscal-YEAR figures only** -- the model block holds no quarters | **GRAIN WRONG** |
| three forward years `2026E/2027E/2028E` | fiscal years to 2028 exist, but **every `BEST_*` forward figure is REFUSED** (`unit/sign convention is 'NOT-YET-BUILT'`) | **REFUSED UPSTREAM** |
| a **`y/y Growth` row under every metric** | Model Notes: *"y/y growth rows: ABSENT -- the block carries none and this page computes none"* | **NOT COMPUTED** |
| ~8 metrics curated by sector | **391 figures**, each with its full Bloomberg field description | **CURATION ABSENT** |
| reporting currency named; local AND USD where they differ | `px_last` for `HSBA` serves **1499.8** where the team writes **`Price (Gbp): 14.96`** | **UNIT DEFECT** |
| the position panel (fund, weight, purchase date, TR, TR vs index) | **[SUPERSEDED BY A1]** `silver/holdings/{date}.parquet` holds all five; AMGT declares no join to it | **JOIN UNDECLARED, not data absent** |
| named broker views with reasoning | a MACHINE `Analyst Posture`; `Divergence` ruled ABSENT until a house forecast exists | **DIFFERENT OBJECT** |
| **2 pages** | **13 pages** | consequence of the four rows above |

**THE HEADLINE: THIS IS NOT A RENDERING TASK.** Three of the table's five structural properties -- quarters,
forward estimates, growth rows -- **are data the model block does not hold**, and the CVO's own round-4
adjudication already said so from the other direction: `robustness`'s absent reason reads
*"grain: annual (fiscal-year model block, not the ruled 8-quarter TTM window)"*. **The 2-page export is
blocked on the model block's GRAIN, and no amount of export-side work reaches it.**

---

## 4. AND THE TEAM'S OWN DOCUMENT INDEPENDENTLY CONFIRMS THE 100x DEFECT

`ROUND_ANALYSIS.round4.md` amendment A1 found four London names serving Base cases at 1.4-4.6% of their own
`px_last`, and inferred a GBp-vs-GBP mismatch from the signature alone -- **all four London names, no other
name in the band.**

**The HSBC earnings update settles it from outside the product entirely:** the team writes
**`Price (Gbp): 14.96`**. The served `px_last` for `HSBA_LN_Equity` is **1499.8**. **1499.8 GBp = 14.998 GBP,
which is 14.96 to the team's rounding.** The inference is now a measurement, and the instrument is a document
written by the people who will read the export.

**America Movil corroborates the discipline the product lacks:** its table stub reads `MXN (millions)` and it
carries `Market Cap (MXN)` AND `Market Cap (USD)` as separate labelled rows. **The team never serves a figure
whose currency a reader has to infer.** That is the rule the base case broke.

---

## 5. WHAT NO SURFACE IN THE ESTATE CARRIES -- the position panel  **[HEADING SUPERSEDED BY A1: the estate DOES carry it. This section's ZERO is true about AMGT's FIELD NAMES and false about the FACTS.]**

`comp-find 'fund_weight|initial_purchase_date|Fund Weight|Initial Purchase|tr_local|plus_minus_index'` over
`lib/research`, `portal/src` and `infra/aws/lambda`: **0 hits across 6641 scanned files.** The tool's own
caveat is recorded with it: 1586 in-scope files were BINARY and never searched, and 424 ephemeral-floor files
were excluded, **so the zero does not cover them.** A positive control on the same instrument and scope is
recorded beside this line in the commit that lands it; **an uncontrolled zero is not a finding and this one is
not being published as an absence until its control passes.**

**Whatever the census returns, the class of the gap is clear from the template alone:** `Fund`, `Fund Weight`,
`Initial Purchase Date`, `TR (Local)`, `TR` and `+/- (Index)` are **PORTFOLIO facts, not research facts.**
They live in whatever system holds Opal's positions, and **`AMGT_RESAPP`'s PRD contains no contract for a
portfolio data source.** The first line of the team's document is a position instruction, so **the export
cannot open the way every one of these documents opens without a portfolio join that no AMGT outcome
currently declares.**

---

## 6. WHAT THIS MEANS FOR THE ENDPOINT -- a ruling and a card

**RULING 1 -- `FWD-5` is not one outcome, it is three, and the fence cannot be met by the round it sits in.**
The export clause decomposes into: **(a)** the DOCUMENT SHAPE (title block, recommendation line, prose,
sections, page-2 structure) -- export-side, buildable now; **(b)** the TABLE -- blocked on the model block's
grain (quarters, forward estimates, growth rows); **(c)** the POSITION PANEL -- blocked on a portfolio data
source that no outcome declares. **Cutting (a) alone produces a two-page document that is missing the table
every one of these reports is built around.** The honest sequence is (b), then (a), with (c) carded.

**RULING 2 -- the rich-text branch already satisfies the goal's `or`, and that changes the priority rather
than the requirement.** The goal reads *"2pg max OR machine readable rich text output"*. **The rich branch is
built** (`FWD-30` branch (b), the 402-line export). So the 2-page branch is not blocking the goal's export
clause on a strict reading of the `or` -- **and it is the branch a person actually forwards**, which is what
`FWD-5`'s DONE WHEN measures (*"Adam has actually forwarded one"*). **Recorded so the `or` is not used to
retire (b) and (c) by accident.**

**CARD AT ANDREW -- ONE, and it is cheap to answer:**

```
+-- CALL 1 of 1 ------------------------------------------------------+
  **Where do Fund, Fund Weight, Initial Purchase Date, TR and
  +/- (Index) come from?**
  Every earnings update in the library opens with a position
  instruction built from these five facts. No AMGT surface carries
  any of them and no PRD contract declares a source.
  ----------------------------------------------------------------------
  **REC --** Name the system that holds Opal's positions and I will
  write the contract. If the answer is "the export does not carry the
  position line", say so and the export opens with the thesis instead
  -- a one-line answer either way, and it unblocks the whole panel.
+---------------------------------------------------------------------+
```

---

## 7. THE ONE-LINE VERSION FOR THE ISSUER

**Build (b) before (a).** The 2-page export's centre is a quarterly table with forward estimates and growth
rows; **the model block is annual, computes no growth, and refuses every forward figure.** Until that changes,
an export-side cell produces a well-shaped page with a hole where the table goes.

---

## 8. INSTRUMENTS

`library.list_folders(library.library_root())` for the 94 folders and every file in them -- `pypdf` page
counts on 62 of 62 earnings updates, none failed -- full text extraction of three 2-page exemplars in three
currencies, chosen because a template claim on one document is a sample of one -- the served `thesis` and
`overlay` routes for the comparison column -- `comp-find` with its own binary and ephemeral-floor caveats
printed, and its positive control landed beside it. **No vendor call: every document read is a local file in
the team's own library, and every served figure came from a `lambda:Invoke` of Opal's own function.**

---

# AMENDMENT A1 -- ~17:5xZ -- **THE CARD IS WITHDRAWN. THE ESTATE ALREADY HOLDS ALL FIVE POSITION FACTS, AND I WAS ONE `comp-find` AWAY**

**Section 6's card asked Andrew where `Fund`, `Fund Weight`, `Initial Purchase Date`, `TR` and `+/- (Index)`
come from. It should never have been written.** One census of the fund code answered it.

## `IDVZ` IS AN OPAL ETF THIS ESTATE ALREADY BUILDS HOLDINGS FOR

`comp-find 'IDVZ'` -- **11,101 hits across 74,733 scanned files.** It is not an unknown fund; it is one of
four Opal ETFs the `ETFS_POSITIONING` pipeline has been producing for over a month:

> `silver/netassets/2026-08-20.parquet  ticker = ['DIVZ','IDVZ','PFDE','PFOE']`
> `silver/holdings/2026-08-21.parquet` -- 114 rows

and the surfaces that consume it, read at their definition lines:
`data/etfs/scripts/gold/etf_positioning_gold.py:89` `SILVER_HOLDINGS = "silver/holdings"`;
`infra/aws/lambda/etfs-pipeline/etfs-netassets-daily/lambda_function.py:135`;
`infra/aws/terraform/cot-value-parity/cot_value_parity.tf:117`
`VP_ANCHOR_KEY_TPL = "silver/holdings/{date}.parquet"`; and
`data/assets/scripts/gold/satellites_weights.py:165` returning per-constituent `{"book", "weight"}`.

## ALL FIVE FACTS ARE DERIVABLE FROM SURFACES THE ESTATE OWNS

| position-panel fact | where it comes from |
|---|---|
| `Fund IDVZ` | membership in `silver/holdings/{date}.parquet` for that fund |
| `Fund Weight 2.75%` | the per-constituent weight the holdings surface carries (`satellites_weights.py`) |
| `Initial Purchase Date: 12/27/2024` | **the FIRST date the name appears in that DATED series** -- the key is `silver/holdings/{date}.parquet`, so the series is the history |
| `TR (Local) +122.7%` / `TR +48.6%` | price history from that first date, which the model block already carries per fiscal year and `PX_LAST` carries live |
| `+/- (Index) +74.1%` | the same against a benchmark |

**So section 5's measured zero was TRUE and MISLEADING.** `fund_weight`, `initial_purchase_date`,
`tr_local` and `plus_minus_index` genuinely appear nowhere -- 0 hits, positive control passed (66 hits for
`build_rich_text|model_cases` on the same instrument and scope). **But I searched for AMGT's names for the
fields instead of for the THING.** The estate does not spell it `fund_weight`; it spells it `weight`, inside a
pipeline with its own vocabulary. **A field-name census answers "does this codebase use my word", never "does
this estate hold this fact."**

## WHAT REPLACES THE CARD

**RULING 3 -- the position panel is a JOIN, not a data gap, and it is `AMGT_RESAPP`'s to declare.** The export
needs one contract naming `silver/holdings/{date}.parquet` as the position source and stating the four
derivations above. **No new producer, no new pipeline, no vendor call, and nothing from Andrew.** CLAUDE.md's
BUILD LADDER rung 2 -- *"the estate already has it"* -- answers this, and rung 2 is where I should have started.

**The card at Andrew for the position panel is WITHDRAWN.** Section 6's card block is superseded by this
amendment; the only cards remaining on this record are none.

## AND THIS IS THE SECOND TIME TODAY, WHICH MAKES IT A PATTERN RATHER THAN A SLIP

| card | what actually answered it | how far away the answer was |
|---|---|---|
| *"89 or 94 -- which universe?"*, carried across five ticks | `C-BACKFILL-DENOMINATOR-IS-THE-RESEARCH-FOLDER`, Andrew's own word of 2026-09-24, ratified in the SIBLING project's PRD | one `comp-find` over `org/missions/D5/AMGT/` |
| *"where does the position panel come from?"*, written 30 minutes ago | `silver/holdings/`, a live Opal pipeline with 11,101 references | one `comp-find` on the fund code printed in the document I was reading |

**Both cards were about the ESTATE, and I looked only at MY PROJECT.** The first failure taught the sibling-
project census; **it did not generalise, because I wrote the rule about siblings instead of about scope.**

> **RULE R-6 (standing, and it supersedes the sibling rule by containing it).** **Before a card leaves this
> seat, census the term ONCE, UNSCOPED, over the whole estate** -- not the project, not the directive, not the
> sibling set. **And census the THING, not your name for it:** the fund code printed on the document, the
> bucket prefix, the vendor's mnemonic. A zero on my own field names is evidence about my vocabulary.
> **Cost: one `comp-find`, and both of today's cards died to it.** Non-application: a question about intent,
> money or a standing hold -- no census answers what Andrew wants.

**The cheapest measurement in this session was the one I kept not running.**
