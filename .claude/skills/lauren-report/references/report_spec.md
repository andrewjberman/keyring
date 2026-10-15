# Report spec -- the JSON that `scripts/build_report.py` renders

`{"meta": {...}, "blocks": [...]}`. `references/example_asml_2q26.json` is Lauren's ASML 2Q26 update transcribed
(text, header block, Financial Summary, all 16 figure titles; four figures carry their printed data, the rest are
placeholders). **Copy its block order.** The file name is `<TICKER> earnings update <period>.docx`.

## meta
`ticker_short` (`ASML`), `period` (`3Q26`), `author` (`Lauren Harmon`), `fiscal_quarter_end` (`2026-09-30`).

## blocks, in the house order

| # | block | content |
|---|---|---|
| 1 | `title` | `company_line`: `ASML Holding NV (ASML-US)`; `period_line`: `3Q26 earnings update` (fiscal labels as the company uses them, e.g. `Fiscal 4Q26`) |
| 2 | `summary` | header block + Financial Summary (below) |
| 3 | `heading` "Recommendation: Maintain positions in PFOE and IDVZ" + `para` | the one-paragraph verdict on the quarter |
| 4 | `heading` "Headline results", `subhead` "Positives", `dash` [1 item], `subhead` "Negatives", `dash` [1 item] | one dense paragraph each |
| 5 | `heading` "Geographic highlights" + `dash` | |
| 6 | `heading` "Segment highlights" + `dash` | |
| 7 | `heading` "Headwinds and risks" + `dash` of `{"topic", "text"}` | renders "Topic – text", 3-5 items |
| 8 | `heading` "Guidance" + `dash` | updated vs prior guidance, next-quarter guide |
| 9 | `heading` "Rating actions and target price changes" + `para` and/or `table` | broker table: `[["Broker","Rating","Price Target","2026E EPS","2027E EPS","Source"], ...]` |
| 10 | `heading` "Appendix" + `figures` | the company's chart set, two per row |
| 11 | `heading` "Why we own" + `para` | carried from the prior report; edit only when the thesis changed |

Other blocks: `para` (prose; `**bold**`, `_italic_`), `pagebreak`.

## summary

```json
{"type": "summary",
 "header": {"left":   [["Ticker","ASML-NL"],["Name",...],["Sector",...],["Location",...],["Currency",...],
                       ["Fiscal Yr","12"],["PE NTM","30.0x"],["Fund","PFOE","IDVZ"],["Weight","6.1%","2.4%"]],
            "middle": [["Date of Pricing","9/2/26","ADTV","$ 0.2"],["Share Price","$ 1,435.40","Short Interest / Total",""],
                       ["Market Cap (bn)","$ 557","Oustanding Shares","385.4"],["Net Debt","$ (8.7)","Float","99.3%"],
                       ["Other","$ (1.6)","Beta","2.3x"],["Enterprise Value","$ 546.9","Div Yield","0.5%"]],
            "right":  [["Cash & Equiv","$13.3","26.3%","Curr Liab","$24.3","48.0%"], ... ["Total Assets","$50.6","","TL & SE","$50.6",""]]},
 "summary": {"quarters": ["4Q24", ... 10 quarters ending with the reported one],
             "annual": ["2025", "2026E", "2027E", "2028E", "2029E"],
             "rows": [{"label": "Revenue", "q": [...10], "a": [...5]},
                      {"label": "y/y Growth", "kind": "growth", "q": [...], "a": [...]}, ...]}}
```

Row order (keep it): Revenue, y/y Growth, Operating Income, Operating Margin, EBITDA, EBITDA Margin, EPS, y/y
Growth, Avg Diluted Shares, y/y Growth, Cap Ex, FCF, DPS, y/y Growth, Dividend Yield (`kind: rule`), FCF Yield,
P/E, FCF Margin (`kind: rule`), ROA, ROE. Quarters roll forward one column each report (the oldest drops off).
Quarter labels follow the company (`1Q24` for ASML, `Mar-24` for UNH). Money in millions of the reporting
currency. `kind`: `growth` = italic indented; `rule` = a thin rule above the row.

## figures

```json
{"type": "figures", "height_in": 2.65, "items": [
  {"title": "Figure 1: local currency sales growth (% year-over-year)", "type": "bar", "format": "0",
   "categories": ["Jun-22", ...], "series": [{"name": "sales growth", "values": [35, 10, ...]}]},
  {"title": "Figure 13: net bookings (bn)", "type": "combo", "categories": [...],
   "series": [{"name": "net bookings", "values": [...]},
              {"name": "growth (% year-over-year)", "as": "line", "format": "0.0", "labels": "last", "values": [...]}]},
  {"title": "Figure 14: net bookings by application (bn)", "pending": true, "pending_note": "AlphaSense: ..."},
  {"note": "Net bookings are a demand signal ..."}]}
```

- `type`: `bar` (one series, clustered), `clustered` (several series side by side), `stacked100` (100% stacked,
  her "sales by X (bn)" mix charts, labelled with the bn values), `stacked`, `line`, `combo` (bars + a line on a
  secondary axis, the "level + growth" charts).
- `labels`: `all` (default; every point labelled, as hers are), `last` (only the latest point, her growth lines and
  margin lines), `none`. Per series overrides allowed. `format`: an Excel number format (`0`, `0.0`).
- Levels run 21 quarters (Jun-21 .. Jun-26 in the example); growth charts start a year later (17 quarters).
- `values` may contain `null` for a quarter with no data (a gap; never a guessed value).
- `pending: true` (or no `series`) renders a bordered placeholder of the same size with `pending_note`. Use it for
  any figure whose data is not in hand (AlphaSense-only series), naming exactly what is needed.
- `{"note": "..."}` places a definition paragraph between figure rows (MCR definition, net bookings definition).
- Numbering is the report's: renumber when a figure is retired (ASML dropped its bookings charts in 3Q26 once the
  company stopped quarterly bookings disclosure).
