# BRIEF (midstream) -- IRPT_ANLREQ: the report's data layer -- recreate the YCharts packet from real data, yfinance first, Bloomberg without limit

Author: `4.0.0_SA_CRO~TCKT` (dell2), 2026-10-20. Mode: `--midstream`.
Consumer: `1.0.0_SA_CTO~DELL2`, `/endpoint --forward`, as a PRD addendum to IRPT_ANLREQ (v0.28). It sits beside
FWD-9 to FWD-12 (the engine brief @e197f63e58) and widens their data source.

Authority (verbatim, one record):
`org/tier1_exec/4.0.0_SA_CRO~TCKT/deliverables/ANDREW_DIRECT_20261020_22xxZ_REPORT_FROM_DATA_WE_HAVE_BLOOMBERG_DRAW.md`
@c464f10d32. Seven messages after he read run 7d's Opal Overview sample:
- the report must come "from data that we actually have/forseeably could get";
- "There are no data restraints ... if we have to run it on bloomberg to get beta, duration, etc characteristics ...
  to be able to generate a bunch of pie charts on concentrations ... then so be it";
- the YCharts packet's purpose is "to assess what data we would need to be able to generate a packet";
- "if we cannot get that from yfinance, then we need to get it from bloomberg";
- "I do not give a shit what this packet looks like as long as it has a bunch of charts and concentrations";
- "the premise is simply to recreate the y chart format, hwoever we have to do it";
- "there are no limits on bloomberg when it comes to this, it has to get done".

Evidence: `org/tier1_exec/4.0.0_SA_CRO~TCKT/deliverables/RESEARCH_OPAL_REPORT_DATA_GAP_MAP_BLOOMBERG_20261020.md`, the
gap map (cited below as GM and its section numbers).

---

## PART 0 -- How the blind constraint was honoured, and where it bent

- Not read: the IRPT_ANLREQ task-order files or decompositions.
- Read:
  - run 7d's run.json element set;
  - the three YCDGEN maps;
  - the 2026-09-16 YCharts sample (a client document, read locally; field names only reach this file);
  - the Bloomberg playbook (`integrations/bloomberg/READ_HERE.md`);
  - read-only yfinance calls on AAPL, SPY and AGG.
- **Bent:**
  - the commit stream told this seat that release r34o (FWD-10 Core comparison, the audit wiring, Overview price
    pages) is signed and staged;
  - this brief assumes r34o lands and does not restate it.

## PART I -- THE OUTCOME TERRITORY

**Candidate thread:**
- An Opal staff user files an Overview for a real client holdings file that holds non-Opal funds and stocks.
- Every concentration page of the packet is filled:
  - region and country;
  - sector;
  - asset class;
  - credit quality;
  - maturity;
  - market cap.
- Each value comes from yfinance, or from Bloomberg where yfinance has nothing.

### D1 -- Every concentration chart in the YCharts packet is drawn from real data, for every holding the client owns
- The packet carries every chart and breakdown the YCharts packet carries, in GM section 2's 12 groups:
  - region and country;
  - sector;
  - asset class;
  - credit quality;
  - maturity buckets;
  - bond sector;
  - market cap;
  - style box;
  - fundamentals;
  - top holdings;
  - return and risk series;
  - text.
- They are computed for the client's actual holdings, not only for Opal's own ETFs.
- **Today (M, GM s.1):** the generator's Bloomberg characteristics file covers only the Opal ETFs and their
  constituents (173 securities). Any other holding reads "not covered". That is why run 7d showed 13 values out of 257
  elements.

### D2 -- A characteristic is looked up once per security, yfinance first, then Bloomberg, and the report names its source
- Per security, for each field:
  1. yfinance (the GM s.2 key: `info` keys, `funds_data` methods);
  2. otherwise Bloomberg reference data (GM s.2 mnemonic) through the existing Bloomberg request queue;
  3. otherwise the report says in words what is missing for that holding (FWD-12).
- Each value carries its source as a claim field (yfinance / bloomberg), as prices already do (C-PRICES).

### D3 -- The style box and the full look-through are not left out for want of a Bloomberg entitlement
- The 3x3 stock style box for funds (9 elements) has no yfinance source (M). The plain Bloomberg reference fields do
  not clearly serve it (I).
- The full constituent look-through behind the top-25 table needs BQL.
- BQL is "User not authorized" on this terminal (M, READ_HERE s.4).
- Andrew said "no limits on bloomberg ... it has to get done". The BQL entitlement is the clean way to meet D3.
- **Buying it is his act, named as an act** (Part V).

### D4 -- Andrew judges the filled packet against the YCharts sample
- The FWD-9 judgement is repeated on a packet built under D1 to D3.
- The bar is his words: charts and concentrations, recreating the YCharts format. Pixel likeness is not the bar.

## PART II -- WHERE THE BOUNDARY SITS

- **IRPT_ANLREQ owns:**
  - the producer reading per-security characteristics;
  - the per-request draw;
  - the claim field.
- **The Bloomberg queue and terminal belong to their owners** (`integrations/bloomberg/`, the `0.0.3_BG_BBGTerminal`
  seat):
  - this project REQUESTS through the queue, never around it (CLAUDE.md: "Bloomberg pulls go only through their
    queue");
  - a new request type, if the queue needs one, is that owner's change.
- **Prices are not in scope.** C-PRICES keeps Bloomberg out of the PRICE chain, and that stands (GM s.6). D2 adds
  CHARACTERISTICS only.
- **FWD-10/11 (the engine brief):** this brief supplies their data; it does not change their outcomes.

## PART III -- THE QUALITATIVE BAR

- Andrew opens the packet for a real client and sees full concentration pies, with nothing reading "not covered", for
  a holding that yfinance or Bloomberg knows.
- A holding neither source knows is named in words, and is rare.

## PART IV -- THE SUBSTRATE (measured unless marked)

| Finding | Status | Source |
|---|---|---|
| yfinance serves stock `info.country`, `sector`, `marketCap`, `trailingPE`, `priceToBook`, `dividendYield`, `beta` | M | AAPL |
| yfinance serves fund `sector_weightings`, `asset_classes`, `bond_ratings`, `top_holdings`, `equity_holdings`, `bond_holdings` | M | SPY, AGG |
| yfinance has NO fund country/region method and NO bond-sector method | M | |
| Bloomberg serves `HB_GEO_CNTRY_ALLOC`, `HB_INDUSTRY_SECTOR_ALLOCATION`, `TOTAL_NUMBER_OF_HOLDINGS_IN_PORT`, `HB_OAS_EFF_DURTN` | M | READ_HERE s.4 and the parquet |
| Further Bloomberg mnemonics (maturity, bond sector, market cap, rating allocations; YTM; coupon) | I | names to confirm on the terminal |
| Bloomberg derived fields are CURRENT-DAY ONLY | M | READ_HERE s.4 |

On the current-day limit: a per-request draw at filing needs no history, because the packet is as-of the filing.

Fill counts (GM s.3, of 244 not-available elements):

| Source | Elements |
|---|---|
| yfinance | 41 |
| Bloomberg | 104 |
| Price math, code only | 25 |
| Text | 65 |
| At risk (D3) | 9 |

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

- **The Bloomberg queue accepts a per-security reference request for an arbitrary security list at filing time.** If
  it only serves a fixed daily universe, the draw needs a new request type from its owner (GM s.5).
- **The terminal is signed in when a request files.** The sign-in is two-phase, with a 2-attempt budget
  (READ_HERE s.2).
- **Every new S3 address is builder output** (C-NAMES). The characteristics cache needs a registry row (GM s.5).
- **ACT FOR ANDREW:** the BQL entitlement is a purchase (READ_HERE s.4: "a purchase, not a build"). His "no limits"
  is read as permission to propose it. This seat asks him for the act explicitly; it is not assumed.

## PART VI -- STATUS (NOT OUTCOME-BEARING), measured 2026-10-20 ~22:xxZ

- Run 7d PASS (both PDFs open).
- r34o (Core comparison) is staged behind run 7d.
- The Opal Overview sample is at `C:/dev/andrew_samples/Opal_Overview_sample_E2E7D.pdf` (synthetic).

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- Most Bloomberg mnemonics beyond the four measured are unconfirmed.
- yfinance was read on three tickers only; coverage on a real client file is not measured.
- The fundamentals split between yfinance and Bloomberg is estimated.
- Nothing about the queue's ability to take an ad-hoc list was tested.
- No Bloomberg call was made.

## REFS

```
  BRIEF PATH        docs/briefs/irpt-anlreq-report-data-layer-yfinance-bloomberg-brief-20261020.md
  PROJECT           IRPT_ANLREQ (D9/IRPT, dell2), PRD v0.28
  EXISTING PRD      org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md
  SIBLINGS          integrations/bloomberg (queue + terminal, 0.0.3_BG_BBGTerminal); IRPT_DASHBD (TWR engine)
  PRIOR ART         RESEARCH_OPAL_REPORT_DATA_GAP_MAP_BLOOMBERG_20261020.md; engine brief @e197f63e58; YCDGEN maps
  MEASURED AT       2026-10-20 ~22:xxZ
```
