# AMGT_RESAPP -- SUBSTRATE MEASUREMENTS FOR THE ROUND-10 L10 ADDENDUM (Rule 28 cards)

**Seat:** `1.0.0_SA_CTO~W` · **Date:** 2026-09-15 05:3x-05:5xZ · **Egress authority:** Andrew-direct ~05:2xZ
(record `ANDREW_DIRECT_20260915_052xZ_EGRESS_GRANTED_TO_CTO_W_FOR_THE_SESSION.md` @473526f738).
**Purpose:** each card measures a resource the addendum's new outcomes would BUILD ON, before any cell does
(CLAUDE.md Rule 28: process, artifact, trust; every row carries its owner). Raw outputs sit beside this file.
Nothing here is a cell, a production run, or a claim that a feature exists.

---

## CARD 1 -- THE FILINGS ANALYZER SUBSTRATE: the Claude API over one filing, with citations and a schema

**Resource:** Anthropic Messages API, model `claude-opus-5`, document input with `citations: {enabled: true}`,
a JSON schema asked for in the prompt. Script `measure_filings_analyzer.py`; record `BA_10K_2026-01-30_measurement.json`.
**Stand-in input:** Boeing's 10-K filed 2026-01-30 from SEC EDGAR (primary `ba-20251231.htm`, 3,439,474 bytes).
Production input will be the filing Bloomberg pulls; a public filing stands in for the measurement and is
disclosed as such. Bloomberg-derived content was NOT sent.

| # | question | measured |
|---|---|---|
| 1 | methodology | HTML -> text (494,404 chars); Item 1A (260,784) + Item 7 (89,966) sent = 350,787 chars, 71.0% of the full text, a NAMED subset, never a silent truncation; `count_tokens` 148,601 input tokens |
| 2 | cadence / trigger | one call, streamed, adaptive thinking, effort high; 114.5 s wall clock; DESIRED production shape = a nightly Batch API run per new filing (50% price), never a per-page call |
| 3 | persistence / authority | the model's output is machine prose under FWD-9's marking rule; the FILING is the authority and the output points at it |
| 4 | exact location | output would land in the pool: `s3://opal-data-harvest/filings/v1/{security_key}/{accession}.analysis.json` (proposed; nothing written) |
| 5 | coverage + denominator | 76 items extracted (15 guidance, 5 segments, 17 risks, 15 commentary, 9 bets, 15 challenges); **71 of 76 carry an inline citation** to the document; the 5 without are the segment-revenue rows, which carried figures (BCA 41,494 / BDS 27,234 / BGS 20,923 / total 89,463 USD m) without a cite |
| 6 | key / identity space | `security_key` + EDGAR accession (or Bloomberg's filing id) |
| 7 | failure mode distinguishable? | `stop_reason` was `end_turn`; a refusal or `max_tokens` is a distinct stop reason; a JSON parse failure is loud. ⚠ ONE FINDING: with a JSON answer requested, the API returned the citations INLINE as `<cite index="1-11,1-12">...</cite>` tags inside the JSON strings and NO `citations` field on the text block (blocks carrying citations = 0). So structured extraction and citation blocks are two passes or a tag parser, and `output_config.format` cannot be combined with citations (400, per the platform reference). The addendum's outcome must name which shape the cell uses. |

**Cost of the measurement:** 149,211 input + 12,518 output tokens ≈ USD 1.06 at list. **Owner of the
substrate:** Andrew (vendor account, the `anthropic-api-key` secret, last accessed 2026-09-13). **Licence
question, open:** sending a Bloomberg-pulled filing to a third-party API is a Bloomberg-terms question, not an
egress one; carded, not answered.

---

## CARD 2 -- THE EXEC-MANAGEMENT SUBSTRATE: Lusha v3 prospecting, one company, C-suite seniority

**Resource:** Lusha API v3 through the estate's own client (`data/find/imo/scripts/_util/lusha_client.py`),
`POST /v3/contacts/prospecting`, company domain `boeing.com`, seniority `c-suite` (id 9, discovered from
`GET /v3/contacts/prospecting/filters/seniority`: founder, partner, c-suite, vice president, director, manager,
senior, entry, intern, other). Script `measure_lusha_csuite.py`; record `boeing_csuite_prospecting.json`
(scrubbed to id, name, title, social links; no contact data points were requested or stored).

| # | question | measured |
|---|---|---|
| 1 | methodology | one prospecting page, page_size 50, NO contact reveal (the estate's interim policy keeps `contacts/enrich` off; `LUSHA_CONTACT_REVEAL_ENABLED` unset) |
| 2 | cadence / trigger | 1.6 s; 2 credits per page; rate limits read from headers (daily 2,000 / hourly 400 / minute 200 requests) |
| 3 | persistence / authority | Lusha is a PROFILE source (title, department, social link), not the authority on who the executive officers ARE; that authority is the filing (the 10-K's executive-officer section and the proxy statement), which also carries the "since" years tenure needs |
| 4 | exact location | proposed pool key `s3://opal-data-harvest/people/v1/{security_key}/{person_id}.json` (nothing written) |
| 5 | coverage + denominator | 50 of 50 results returned on page 0 for `c-suite`; the field set is 9 fields (`id, firstName, lastName, jobTitle{title, department}, socialLinks, company, location, has, canReveal`); ⚠ the `c-suite` filter is LOOSE: the 12 sampled rows include an IT operations manager, a program manager and an executive director of HR beside a chief scientist, a CTO and a "President and Chief Executive..." row, so the roster is a CANDIDATE list that the filing's officer list must confirm |
| 6 | key / identity space | Lusha `id` + LinkedIn URL; joins to the filing by name only (no shared key) |
| 7 | failure mode distinguishable? | HTTP status + `billing.creditsCharged` per call; a zero-result page is distinct from an error; **NO tenure or role-start field exists anywhere in the response or the reference** (`tenure-like fields: []`), so the sixth word's average-tenure measure CANNOT come from Lusha alone |

**Credits consumed:** 2 (1,029 -> 1,027 remaining of 1,200). **Owner of the substrate:** Andrew (the
`find-insure/lusha-ai/api-key` account, shared with FIND_INSURE; whether AMGT gets its own key is his call).
**Design consequence:** the C-suite roster and tenure come from the FILING (officer list with ages and
"since" years, public, already inside the filings-analyzer lane); Lusha enriches each confirmed officer with a
profile link and title; the pool-average tenure is computed over the union universe from the same filing
field. The "targeted web search" half stays unmeasured tonight and is the same shape as a Claude
`web_search` server-tool call scoped to the company's IR domain.

---

## CARD 3 -- THE PEERS / MODEL STRUCTURE SOURCES: Adam's pack workbook and the Security Scanner registry

**Resource A:** Adam's one-pager workbook, measured on `Boeing BA/BOEING ONE PAGER 2026 01 27_v1.xlsx` in the
synced SharePoint library `Shared - Documents/Asset Management/Research/` (90 name folders; the F1 corpus).
Read with openpyxl, values only. Sheets: `_CIQHiddenCacheSheet`, `Model`, `Sheet1`, `CSC`.
- `Model` = THE MODEL TAB'S SHAPE, Bloomberg-keyed (`BA US EQUITY`): a Financial Summary 2016-2028 of
  Revenue/Sh, EPS, BVPS, diluted shares, DPS, dividend yield, FCF yield, P/E, P/B, FCF margin, ROA, ROE, RoTA
  with y/y growth rows; Upside / Base / Downside cases (EPS x multiple -> price -> return); "Opal Case
  Assumptions" (revenue growth, earnings margin -> revenue, EPS); EBITDA and earnings-margin history.
- `CSC` = THE PEERS TAB'S SHAPE, a comparable-multiples table on Bloomberg fields (`px_last`,
  `EQY_SH_OUT_REAL`, `CUR_MKT_CAP`, debt, preferred, minority, cash): per peer Price, Shares, Debt, Preferred,
  Minority, Cash, Mkt Cap, EV, P/E 2025/2026/2027, Debt/Equity, Net Debt/Equity, Net Debt/Capital, 5-yr annual
  growth of Revenue / EBIT / FCF, with Average / Median / Min / Max rows. ⚠ On BOEING the 12 peers are
  KPN, Vodafone, BT, Orange, Telenor, Telekom Austria, Rogers, Telus, Swisscom, AT&T, Verizon, Telefonica:
  **the stale telecom set F6 measured (48 of 54 packs)**, seen here in the workbook itself. The STRUCTURE is
  right; the SET is the defect.
- `Sheet1` = revenue, net income and FCF history 2015-2028E (the chart data).
**Resource B:** the Security Scanner: `factor_metadata_registry.json` = **289 factors across 18 categories**
(size 11, efficiency 22, growth 25, management 11, profitability 21, quality 15, solvency 28, value 26,
analyst 12, governance 11, crowding 25, insider 10, short 10, liquidity 6, beta 7, momentum 15, technical 22,
volatility 12), each with `code, name, category, relationship, ic, coveragePct, autocorrelationPct, assetClass,
systematic`; the portal's presets are PER OPAL ETF: DIVZ = the default preset (13 factors, dividend-tilted:
dy_ntm 20, dps_gr_1yr 10, shldr_yield 10, six momentum at 5, ey_ntm / fcfy / accruals_bs / leverage at 7.5),
PFOE = 16 factors (growth 42 / quality 30 / sentiment 10 / valuation 8 / momentum 10). Served by
`/api/scoped/security-scanner/{factors, universe/{id}/data, universe/{id}/scanner}` on the same portal API.
**Consequence for the design:** the Peers tab = the `CSC` table computed for a CORRECT peer set, with the
scanner's factor quintiles as the ranking half; the Model tab = the `Model` sheet served from the model
block plus the cases; and **the per-ETF presets are the scoring key Posture needs** -- a name's factor
profile scored under DIVZ's or PFOE's preset says which book it would fit, before any judgment is written.
**Owners:** the corpus is Adam's team's (read-only to us); the scanner's registry and presets are the
ETFS / security-scanner producers' (the `~Z` fabric's domain); AMGT reads both.

---

## WHAT THESE CARDS DO NOT CLAIM

No feature works; no cell is cut; no production key is written; no vendor cadence is chosen. Each card is a
measured input to the addendum's outcome text, and each open question above stays open until its owner
answers it.
