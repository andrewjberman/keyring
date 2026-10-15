---
name: adam-report
description: Generate an Opal Capital INVESTMENT MEMO in Adam Muller's house format (the 2026-10-13 T-Mobile US memo) as a Word .docx, for any listed company -- `/adam-report {ticker | company name | ISIN}`. Pulls the figures from the Opal data harvest through the opalgateway MCP first, falls back to web search (SEC EDGAR and primary filings first) for anything the harvest does not hold or when the gateway is unavailable, computes the Opal-derived ratios, and renders the nine-section landscape memo with a bundled stdlib-only builder. Use on "/adam-report", "investment memo for X", "write up X in Adam's format".
---

# /adam-report -- Opal Capital investment memo (Adam Muller's format)

**Input:** a ticker, company name, CIK or ISIN, plus optional overrides ("as of 10/12", "peers: VZ, T, CMCSA",
"prepared by ..."). **Output:** `<ShortName>_Investment_Memo_<YYYY_MM_DD>.docx`, saved to the user's linked folder.

Layout and wording standard: `references/example_tmus.json` (a real memo, rebuilt 1:1) and
`references/memo_spec.md`. Where the figures come from: `references/data_sources.md`. Read all three before the
first memo of a session; they are short.

## Steps

### 1. Resolve the company and pick the path (one round of parallel calls)
- `harvest_resolve_security(query)`. `status: exact` -> **harvest path**. Anything else (`none`, `not_held`,
  `candidates` that are not this company), or the opalgateway connector missing or erroring -> **web path**.
  Tell the user which in one line (e.g. "TMUS is not in the Opal harvest; building from SEC EDGAR and company IR").
- Harvest path, in the same round: `harvest_security_coverage`, `harvest_get_fundamentals` for `model` (always
  with the `mnemonics` list in data_sources.md), `consensus`, `segments`, `price`; `harvest_get_research`;
  `harvest_get_filing_analysis`; `harvest_get_peers_and_scores`; `harvest_search_articles(limit=25)`.
- A dataset that is absent or more than 5 trading days behind T-1 falls back to the web **for that item only**.

### 2. Fill what the harvest does not hold (web search)
Always from the web, even on the harvest path: the latest 10-Q / interim figures and balance sheet, LTM sums,
company-defined adjusted metrics and KPI lines, the latest guidance, the debt maturity ladder, credit ratings and
outlooks, the 52-week range and YTD return, broker actions and recent events, withholding-tax rates. Source
ranking in data_sources.md section 2: **SEC EDGAR (or the home regulator) first**, then company IR, ratings
agencies, consensus sites, reputable press. Never use an unsourced blog, forum or content farm.

### 3. Build the peer set
Start from `harvest_get_peers_and_scores` only if those peers are the same business; otherwise choose by business
(direct competitors, the parent or listed proxy, the sector names in the fund's benchmark) and justify it in the
section's opening paragraph. 5-7 peers. For each peer: harvest `consensus` + `model` if it resolves `exact`,
otherwise web. One price date and one FX date for the whole table.

### 4. Compute, then tie out
Compute every Opal-derived figure (growth, margins, CAGRs, payout, multiples, yields, LTM, change columns, medians)
from the table's own inputs and mark it teal (`"d": true`, a `sub`/`derived` row, or `_x_` in prose). Run the
checks in data_sources.md section 3. A figure you could not source is `—` (not available) or `n.m.` (not
meaningful), never an estimate presented as fact; say why in Notes.

### 5. Write the memo JSON
Follow example_tmus.json block by block: same nine sections, same table shapes and row order, same voice. Voice
rules, from the example:
- Every thesis / risk / management bullet opens with a bold one-sentence claim, then the numbers.
- Findings paragraphs open with a bold lead ending in a colon.
- Plain, specific, numeric. Dates as `12-Oct-26` in tables and notes; money as `$84.1bn`, `$151.87`; multiples `13.9x`.
- Sources notes name the document (form, period, filing date); Notes explain definitions, splices, restatements,
  footnote markers and the consensus basis. Keep the line "Teal italics = Opal-derived (...)".
- Add one Notes line on provenance: which sections came from the Opal harvest (with its as-of) and which from the web.

Save the JSON beside the output (`<ShortName>_Investment_Memo_<date>.json`) so the memo can be re-rendered after edits.

### 6. Render and deliver
```
python scripts/build_memo.py <memo.json> "<output folder>"
```
(Python 3.8+, standard library only; the path is relative to this skill's folder.) It prints `OK: <path>` or
`ERROR: <block> ...`; fix the JSON and re-run on an error.

**Where it goes:** the folder the user has linked for memos. If a folder is connected (a local folder or the
Microsoft / OneDrive connector), save there; if none is known, ask once which folder, and otherwise hand back the
file. Reply with the file path or link and a 3-line summary: the path used (harvest or web), any section that is
thin or unsourced, and the as-of date.

## Rules
- Never invent a figure, a quote or a source. Every number traces to a Sources note.
- The harvest is preferred but not trusted blindly: Bloomberg-standardised lines can differ from company-reported
  ones. For the lines the memo labels with a company definition (adjusted EBITDA, adjusted FCF, KPIs) use the
  company's figure and say so; a gap of more than 2% against the harvest gets a note.
- Prices are the last close before the memo date (T-1); say the date wherever a price is used.
- Fund mandate context (dividend yield, withholding tax for a US holder) stays in the memo, as in the example.
- If the user asks for a section to be skipped or added, edit the JSON; do not change the builder.
