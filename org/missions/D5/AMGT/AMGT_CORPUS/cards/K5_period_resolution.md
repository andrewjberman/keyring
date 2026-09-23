# K5 -- period resolution (CRPS-c-3)

**Seat:** `0.9.0_WK_AMGT_CORPUS~1`. **Cell:** `CRPS-c-3` (manifest row R3, FWD-2). **Built:**
`lib/research/corpus/typed.py`. **Measured against:** the 123 bronze `research-report` objects
landed by `CRPS-c-1` (the 33 RESOLVED-folder subset of the library, NOT the full 351-file /
93-folder scan denominator -- see "scope" below, same boundary as the K3/K4 card).

## K5, verbatim

*"period resolution -- how a report's PERIOD is determined (filename, header, or content) and
how many of the 351 carry one -- FWD-2's ordering depends on it."*

## Scope of this measurement

`CRPS-c-3` types one silver row per bronze `research-report` object -- 123 objects, not the
CRO scan's full 351-file corpus. The 228 files under UNRESOLVED/AMBIGUOUS folders were never
landed to bronze (`CRPS-c-1`'s own rule) and so carry no extraction and no period resolution
attempt here; they are counted, by folder and by reason, in the FWD-2 denominator line below
(read verbatim from `CRPS-c-4`'s stored backlog document, never re-worded), but this card's
period counts are over the 123 that WERE resolved and typed.

## How the period is determined

Three-stage order, exactly as ruled: **filename first, then the document's own header
excerpt (its heading list plus its first few paragraphs / first page), then the full body.**
All three stages share ONE token-finder (`typed._find_period_token`), tried in the same
specificity ladder at each stage -- a full calendar date (several filename spellings), then
a month-name date, then a quarter label, then a half-year label, then a fiscal-year-only
label -- so a filename or passage carrying BOTH a calendar date and a quarter/FY label (for
example `ICICI Bank Q1 2027 Earnings Update 2026 07 18.pdf`) resolves to the more precise
calendar date.

**Filename date forms measured and coded** (regex constants in `typed.py`, named for what
they parse):
- `YYMMDD` prefix (`260804-hsbc-holdings-plc-interim-results-2026-media-release.pdf` ->
  2026-08-04)
- `YYYY MM DD` / `YYYY-MM-DD` / `YYYY_MM_DD` / `YYYY.MM.DD` (any single-char separator --
  `KDDI Research Pack Template 2026 03 16_v1.docx` -> 2026-03-16)
- `YYYYMMDD` compact (8 digits run together)
- `YYYY MMDD` -- year separated from an UNseparated month+day pair, measured once
  (`VLO Valero ONE PAGER 2026 0120_v1.xlsx` -> 2026-01-20)
- Month-name `D, YYYY` / `D YYYY` (`HSBC Q2 2026 Earnings Update Aug 4 2026.docx` -> the
  literal "Aug 4 2026" -> 2026-08-04, agreeing with the YYMMDD-prefix HSBC media-release
  object above on the SAME calendar date by two independent forms)
- `M_D_YYYY` / `M-D-YYYY` / `M_D_YY` (`ASML research pack 5_5_2026.pdf` -> 2026-05-05;
  `INTU stock price move update 8_26_26.pdf` -> 2026-08-26)
- `Qn YYYY` / `nQyy(yy)` (`BP Q2 2026 Earnings Update.docx` -> 2026-Q2;
  `Walmex 2Q26 Earnings Release.pdf` -> 2026-Q2; `INTU earnings update fiscal 4Q26.pdf` ->
  2026-Q4)
- `Hn YYYY` / `nHyy(yy)` -- a half-year label, MEASURED in this corpus and not in the ruled
  list, coded as an additional filename form (`Enel sPa Earnings Update H1 2026.docx` ->
  2026-H1; `RMS earnings update 1H26.pdf` -> 2026-H1)
- `FYyy(yy)` (`IMB-FY25-RNS.pdf.downloadasset.pdf` -> FY2025, no calendar date present in
  that filename)

The `YYMMDD`/`YYYYMMDD` compact (no-separator) forms are tried ONLY against a filename, never
against header/content prose -- a bare 6- or 8-digit run inside a body of text is far more
likely to be an unrelated figure than a date.

## Commands and their printed output (this run)

```
$ python -m lib.research.corpus.typed --write
...
silver_rows 123 of 123 bronze
class A 16 B 31 C 3 D 1 OTHER 72
fund IDVZ 37 PFOE 7 DIVZ 0 absent 79
k5 period carried 103 of 123 by filename 95 header 7 content 1 absent 20
backlog files 351 = resolved_files 123 + unresolved_files 228
unresolved Adobe ADBE US | bloomberg_ticker status 'UNRESOLVED', evidence '...'
... (60 unresolved-folder lines, one per UNRESOLVED/AMBIGUOUS backlog record)
written_rows 123 skipped_unchanged 0 parts 1

$ python -m lib.research.corpus.typed --census
silver_rows 123 of 123 bronze
k5 period carried 103 of 123 by filename 95 header 7 content 1 absent 20
```

## How many carry a period

**103 of 123** (84%) typed reports carry a resolved period: **95 by filename** (the large
majority -- this team's own filenames are the most reliable period signal in the corpus), **7
by header** (mostly one-pager/workbook label cells such as "H1 2026" or "Q2 2026" sitting near
the top of a sheet, and one PDF's opening lines), and **1 by content** (a date recovered only
from deep in the body text). **20 of 123 carry no period** -- every one of the 20 was checked
by hand and is a genuinely dateless document: the three `... Company Overview, Investment
Thesis, Risks, and Mgmt Board.docx` static templates (class C), five `International Dividend
One Pagers.xlsx` / similar undated workbook templates, three PNG chart snapshots, a
production-history workbook named by a YEAR RANGE rather than a period
(`petrobras_production_2006_2025.xlsx` -- "2006_2025" is a span, not a single period, and is
correctly not matched), a bare-hash-named vendor PDF (`6a7e127270465485.pdf`), and a handful
of results pages whose filename and header carry no date at all.

## FWD-2's own denominator (this cell's second required print)

`backlog files 351 = resolved_files 123 + unresolved_files 228` -- 123 is this cell's own
bronze-object count (matching K3/K4's population exactly); 228 is the sum of the `files`
field on every UNRESOLVED/AMBIGUOUS record in `CRPS-c-4`'s stored backlog document (60
folders, 0 ambiguous), and 123 + 228 = 351 reproduces the CRO scan's own file denominator
exactly. Each of the 60 `unresolved <folder> | <reason>` lines quotes that record's own
`reason` field verbatim, unmodified.

**What this could NOT measure:** a period for the 20 genuinely dateless objects above (there
is nothing in the object to resolve -- these are template/reference documents, not dated
reports); whether the single "content" hit and few "header" hits generalise to a larger
population (this corpus is 123 objects, and the three-stage order was designed to prefer the
more reliable earlier stages, so a corpus with fewer well-named files would lean harder on
header/content).
