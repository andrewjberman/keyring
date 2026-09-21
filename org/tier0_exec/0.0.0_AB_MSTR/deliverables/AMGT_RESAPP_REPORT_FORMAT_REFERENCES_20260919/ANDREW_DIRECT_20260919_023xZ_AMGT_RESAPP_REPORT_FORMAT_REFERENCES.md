# ANDREW-DIRECT 2026-09-19 ~02:3xZ -- AMGT_RESAPP: what the asset management team looks for in a report

**At:** the 0.0.0_AB_MSTR terminal (laptop). **For:** 1.0.0_SA_CTO~Z, via 0.0.0_AB_MSTR~Z, over the agentbus.
**Recorded by:** 0.0.0_AB_MSTR. No gate is created by this record.

## His words, VERBATIM AND ENTIRE

"I need you to get a message to CTO~Z via MSTR~Z via agentbus. They are working on AMGT_RESAPP. Something that
they need to be aware of is the format/style of what the asset management team looks for in these reports. I want
to send them two references that the asset management team made with Claude, because we want to keep it in mind on
two bases: 1.) We should have the content between our pages to be able to generate the information listed here.
2.) We should be able to have an exported file that does a better version of this in a 2 - 3 page export. Please
get them these files: C:\Users\AndrewBerman\Downloads\LLY_2Q26_Earnings_Update_Opal.pdf
"C:\Users\AndrewBerman\Downloads\LLY earnings update 2Q26.pdf"
C:\Users\AndrewBerman\Downloads\LLY_Q2-2026_Earnings_Update.pdf"

## What it binds, read as narrow as the words

1. **CONTENT COVERAGE.** Between the AMGT_RESAPP pages, the application should hold the content needed to GENERATE
   the information these reports list. The reports are the checklist; the pages are the supply.
2. **AN EXPORT.** The application should produce an exported file that is "a better version of this" in **2 to 3
   pages**.

He said "two references" and named THREE files. All three are carried. Which two he meant is NOT inferred here;
if it matters, it is a question back to him. He did not say which file is the target shape for the export, and
this record does not pick one. He did not ask for a PRD change, a round, or a date.

## The three files (renamed to shell-safe names; bytes unchanged -- sha256 first 16 hex of each)

| here | original name | pages | sha256[:16] |
|---|---|---|---|
| `REF_A_house_format_LLY_earnings_update_2Q26.pdf` | `LLY earnings update 2Q26.pdf` | 5 | 96a1c61c245003db |
| `REF_B_opal_branded_LLY_2Q26_Earnings_Update_Opal.pdf` | `LLY_2Q26_Earnings_Update_Opal.pdf` | 5 | 7fdb77fec640c76a |
| `REF_C_long_form_LLY_Q2-2026_Earnings_Update.pdf` | `LLY_Q2-2026_Earnings_Update.pdf` | 21 | 48c1743ddfe23620 |

All three cover one subject: Eli Lilly (LLY-US), 2Q26 earnings, quarter ended 30 June 2026. The "house format" /
"opal branded" / "long form" labels are this seat's descriptions of what it read, not the team's names.

## Inventory -- what each report LISTS (this seat read all 31 pages; this is the coverage checklist for basis 1)

### REF_A -- 5 pages. Reads as the team's own working format: dense, one name, one fund.
- **Header data block:** ticker, name, sector, location, currency, fiscal year, date of pricing, share price, market
  cap, net debt, enterprise value, ADTV, short interest / total, shares outstanding, float, beta, dividend yield,
  PE NTM; a compressed balance sheet (cash, intangibles, fixed assets, total assets, current liabilities, LT
  liabilities, common equity) each with % of total; and **Fund (PFOE) and Weight (4.3%)** -- the position itself.
- **Financial Summary grid:** 10 trailing quarters + last fiscal year + 4 forward estimate years, for: revenue and
  y/y growth, operating income and margin, EBITDA and margin, EPS and y/y growth, average diluted shares, capex,
  FCF, DPS and growth, dividend yield, FCF yield, P/E, FCF margin, ROA, ROE.
- **"Recommendation: Maintain position in PFOE"** followed by a one-paragraph thesis-level read of the quarter.
- **Headline results:** Positives / Negatives.
- **Geographic highlights**, **Segment highlights**, **Headwinds and risks**, **Guidance**.
- **Rating actions and target price changes:** a broker table -- broker, action, target price, valuation basis and
  key assumptions, source reference.
- **Appendix, 14 time-series charts, ~5 years of quarters:** sales growth; gross and operating margin; sales by
  region (stacked) and growth by region; sales by therapy (stacked) and growth by therapy; one sales-plus-growth
  chart per major product (7 of them); US TRx share of total prescriptions.
- **Product primer** (one paragraph) and **"Why we own"** (the long-run thesis, ending on the position call).

### REF_B -- 5 pages. Opal-branded; the condensed presentation layer.
- Running header on every page: firm | company (ticker) | quarter | date | "Internal research -- not investment advice".
- Dateline: quarter end, report date, price and date, market cap.
- **Position summary** -- and, explicitly, NO rating or price target: "the recommendation line is for the
  portfolio manager."
- Narrative paragraph, then **six KPI tiles** (value + the comparison under it): revenue, vs. consensus, non-GAAP
  EPS, EPS ex-one-off, gross margin, FY revenue guidance.
- **Headline results:** Positives / Negatives, each bullet led by a bolded claim.
- **Results in detail:** geographic and segment highlights with figures inline (quarterly revenue, volume-vs-price
  decomposition, growth by region, largest products, revenue by therapeutic area).
- **Guidance, margins and cash:** prior / updated / direction table; an explained-anomaly box ("The EPS 'miss'
  that was not one"); H1 cash generation and use; capital allocation.
- **Headwinds and risks** (six, each dated or quantified where it can be).
- **Valuation:** peer forward-P/E chart with the peer median, DCF with its WACC and terminal growth stated and the
  WACC at which it equals spot, sell-side summary.
- **"What decides the next twelve months":** a When / Event / Why-it-matters catalyst table.
- **Appendix:** selected financials (quarter and half, this year vs. last, % change), product primer, **"Why we
  own it"** with a named counterweight, and a **Sources** block that points at an archive folder per source class
  and DISCLOSES a vendor disagreement rather than choosing a side.

### REF_C -- 21 pages. The long-form deep dive the short ones are cut from.
Key takeaways; results snapshot table; then ten numbered sections: 1 the quarter in detail (revenue, therapeutic
areas, geography and price) -- 2 margins and what the GAAP numbers hide -- 3 guidance, incl. what the implied
second half says -- 4 pipeline, launches and catalysts -- 5 access, pricing and policy, incl. competition --
6 balance sheet, cash flow, capital allocation, manufacturing and supply chain -- 7 ownership, short interest and
positioning (largest holders table, sell-side distribution) -- 8 valuation (multiples table + bear / base / bull
scenario framework) -- 9 what to watch -- 10 risks. Then a full source list with URLs by class, and a "notes on
data quality" paragraph stating what was derived, what is stale and by how long, and what could not be verified
(shown as n/d rather than guessed). Twelve figures, each titled with its CONCLUSION, not its subject.

## Observations for basis 2 (the 2-3 page export) -- offered, not ruled

- REF_B already IS a 5-page condensation of REF_C, and its appendix (page 5) plus most of page 4 is reference
  material. A 2-3 page export is roughly REF_B pages 1-3 with the catalyst table -- but that is this seat's
  arithmetic, not his instruction, and the target shape is his or the asset management team's to name.
- What REF_A carries that REF_B and REF_C do not: the **position** (fund, weight), the **recommendation line**,
  the **multi-year estimates grid**, the **broker target table**, and **long time series** per product. What REF_B
  and REF_C carry that REF_A does not: consensus-vs-actual framing, an explicit catalyst calendar, a DCF with its
  assumptions, and a sources / data-quality disclosure. "A better version" plausibly needs both sets; which wins a
  conflict (REF_A issues a recommendation, REF_B pointedly does not) is NOT answered by his words.
- House style visible in all three and cheap to honour: figure titles state the finding; every table names its
  source; a disputed number is shown both ways; stale or unverifiable data says so.
