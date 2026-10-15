# Memo spec -- the JSON that `scripts/build_memo.py` renders

One JSON object: `meta` + an ordered list of `blocks`. `references/example_tmus.json` is a complete, real example
(Adam Muller's T-Mobile US memo of 2026-10-13, converted 1:1; rebuilding it reproduces the original's text, every
table cell's fill/style/alignment and every paragraph's styling). **Copy its block order and table shapes.**

## meta

| field | example | notes |
|---|---|---|
| `company` | `T-Mobile US, Inc.` | legal name |
| `exchange`, `ticker` | `Nasdaq`, `TMUS` | banner reads `Company (Exchange: TICKER)` |
| `industry` | `Wireless Telecommunications` | |
| `hq` | `Bellevue, Washington, USA` | |
| `author` | `Adam Muller` | the person the memo is prepared for/by |
| `date` | `October 13, 2026` | long form |
| `short_name` | `T-Mobile US` | footer title and file name |
| `file_date` | `2026_10_13` | file name: `<short_name>_Investment_Memo_<file_date>.docx` |

## blocks

| type | fields | renders as |
|---|---|---|
| `section` | `text` | navy bold caps with a teal rule under it (COMPANY FINANCIAL INFO, ...) |
| `subhead` | `text` | navy bold line ("What the balance sheet shows", "Debt maturities (principal, $bn)") |
| `label` | `text` | grey bold line ("Sources", "Notes", "Sources and notes") |
| `notes` | `items: [str]` | grey bullet lines, one per source or note |
| `para` | `text` | body paragraph |
| `findings` | `items: [{lead, text}]` | "**Lead:** finding" paragraphs under a "What the ... shows" subhead |
| `bullets` | `items: [{lead, text}]` | teal square + bold navy lead sentence + body (thesis, risks, management, questions) |
| `table` | see below | |
| `pagebreak` | -- | hard page break. The house memo has two: after the 10-year table (page 1 = snapshot + 10-year table) and before BALANCE SHEET SUMMARY |

Inline markup in any prose string: `**text**` = bold navy, `_text_` = teal italic (an Opal-derived figure in prose).

## table

```json
{"type": "table", "widths": [2950, 706, ...], "header_rows": 1, "size": 15,
 "align": ["left", "right", ...], "col_fills": {"11": "highlight"}, "col_styles": {"14": "bold"},
 "gap_cols": [4], "header_style": "light",
 "rows": [ {"cells": [...], "kind": "sub", "derived": true}, ... ]}
```

- `widths` in twips; they should sum to 14256 (the text width). `size` in half-points: `15` (7.5pt) for the 10-year
  financial table, `null` (10pt body) for every other table.
- `header_rows`: navy header rows (white bold); `header_style: "light"` gives the grey-on-light header of the
  snapshot table. A header cell can span columns: `{"t": "P/E", "span": 2}`.
- `col_fills`: shade whole columns: `highlight` (pale blue) for estimate years, `light` (pale grey) for a side panel.
- `col_styles`: style a whole column on main rows (e.g. the CAGR columns `bold`).
- `gap_cols`: an empty spacer column (no fill, even in the header): the balance-sheet table's column 4.
- Row `kind`:

| kind | label | values | use |
|---|---|---|---|
| (none) | plain | plain | ordinary line |
| `bold` | bold | plain | |
| `strong` | bold | bold | a key line (principal due) |
| `sub` | grey italic | teal italic | growth / margin / ratio lines under a line item (indent the label with 3 spaces) |
| `total` | bold | bold, grey band | totals (total assets, net debt, total revenue) |
| `highlight` | navy bold | bold, pale-blue band | the subject company's row in the comps table |
| `median` | teal bold italic | teal italic | peer median |
| `key` | navy bold | navy bold | the snapshot table's data row |

- Row `"derived": true` makes every value teal italic (an all-Opal-derived row such as P/E, EV/EBITDA, yields).
- Cell overrides: `{"t": "13.9x", "d": true}` teal (Opal-derived) one cell; `"s"` one of `plain bold navy teal tealb
  grey greyp`; `"fill"`: `light | highlight | navy | none`; `"align"`: `left | center | right`; `"span"`.
- Name cells in the comps table carry extra lines: `"T-Mobile US\nTMUS US\n$151.87 · FY Dec-26"` (lines 2+ render
  grey 8pt).

## The nine sections (fixed order, as in the example)

1. **COMPANY FINANCIAL INFO**
   - Snapshot table (8 cols, light header, one `key` row): Company | Ticker / listing | Share price (date) with 52-wk
     range | Shares outstanding | Market cap | Net debt / (cash) with date | Enterprise value | YTD / 1-yr.
   - 10-year table (17 cols, `size` 15, first col 2950, rest 706): 10 fiscal years, 3 estimate years (`col_fills`
     highlight), 3 CAGR columns (9y historical, 5y historical, 3y forward; `col_styles` bold). Rows in this order:
     Revenue, growth (sub); the company's key revenue KPI line if it has one (e.g. service revenue), growth (sub);
     Operating income (GAAP EBIT), Operating margin (sub); Adjusted EBITDA (company definition), growth, margin
     (sub); Diluted EPS, growth (sub); Adjusted/free cash flow; Capex, Capex / revenue (sub); DPS, DPS growth, Payout
     ratio (sub); Diluted shares; Net debt, Net debt / EBITDA (sub); then `derived` valuation rows on the estimate
     years only: P/E (at price), EV / EBITDA, FCF yield, Dividend yield (gross), Net yield after WHT.
   - `label` Sources + `notes`; `label` Notes + `notes` (definitions, splices, restatements, footnote markers ¹ ² ³
     † ‡, consensus basis, and always the line "Teal italics = Opal-derived (...)").
2. **BALANCE SHEET SUMMARY** -- table (8 cols): `$bn | <last FY end> | <latest quarter> | Change | (gap) | Key
   balance sheet indicators | <FY> | <LTM>`; assets, total assets (`total`), debt lines, total debt and net debt
   (`total`), leases, liabilities, equity on the left; leverage, coverage, interest rate, fixed-rate share,
   liquidity, gearing, target/covenant, ratings and outlooks in the panel. Then `subhead` "Debt maturities
   (principal, $bn)" + maturity-ladder table (buckets, % of total, cumulative %, multiple of FCF, prior-year memo
   row). Then `subhead` "What the balance sheet shows" + 4-5 `findings`; `label` "Sources and notes" + `notes`.
3. **COMPANY DESCRIPTION** -- one dense paragraph (history, segments, mix, scale, ownership) + a revenue-line table
   (Revenue line | FY | % | latest interim | % | YoY | What it is), last row `total`.
4. **INVESTMENT THESIS** -- 4-6 `bullets`, each a bold claim then the numbers that support it.
5. **INVESTMENT RISKS** -- 5-7 `bullets`.
6. **KEY MANAGEMENT INFO** -- 4-6 `bullets`: CEO, chair/predecessor, CFO, other key officers, "Governance and
   history" (board, control, activism, scandals).
7. **SALES BY REGION** -- a `para` on what the company discloses geographically; a `subhead` naming the cut;
   a two-header-row table (3 fiscal years + latest interim, each `$bn | % total | y/y`); "What the data shows"
   `findings`; Sources and notes. If there is no geographic split, use the best disclosed cut and say so (the
   example does).
8. **OTHER QUESTIONS WORTH ASKING** -- 4-6 `bullets`, each a bold topic then the open questions.
9. **COMPARABLE COMPANY VALUATION** -- a `para` naming and justifying the peer set; a comps table (two header rows:
   Size ($bn) [Mkt cap, EV] | P/E [FY1, FY2] | EV/EBITDA [FY1, FY2] | EV/Sales [FY1] | Yield [FCF FY1, Div. FY1,
   Treaty WHT, Div. net of WHT] | Margin FY1 [EBITDA, EBIT] | Growth [Rev. FY1, EPS FY2] | Debt [ND/EBITDA]); the
   subject company row `highlight`, peers plain, `median` last (median excludes the subject). Then "What the
   comparison shows" `findings` and Sources and notes (prices and FX date, consensus source per company, EV
   definition, footnotes, withholding-tax basis for a US investor).
