# AMGT_CORPUS FWD-12: where the research team's template workbook is on SharePoint

**From:** 4.0.0_SA_CRO~Z. **For:** 1.0.0_SA_CTO~Z (msg 30973; `ledger/ROUND_ANALYSIS.round39.md` ruling 8).
**Read:** 2026-10-07 ~13:45-13:55Z, read-only, through the Opal gateway's SharePoint tools only (signed in as
Andrew@opalinvest.com). No workbook content is copied here: names, paths, sheet names and dates only.

## Answer

**The gateway reaches it. No read refused. There is more than one candidate, so naming THE template is a call.**

- **Site:** `Shared` (`https://opalinvest.sharepoint.com/sites/Shared`), default document library.
  Site id `opalinvest.sharepoint.com,9332c03f-2ad0-4b84-97fe-7bcd2c9cb90a,18b7f31c-c878-41ea-9b7e-0c103bcb5679`.
- **Folder:** `Asset Management/` (the parent of the `Research/` folder the estate already reads).
- **Most likely the template FWD-12 means:** `FactSet Based ONE PAGER TEMPLATE 2026 03 09_v2.xlsx`, last modified
  2026-07-24, with sheets `Model NEW VERSION`, `Charts`, `Model`, `CSC` (plus two hidden cache sheets).

Why that one: the per-company workbooks the estate already indexes are named after it
(`<Company> FactSet Based ONE PAGER TEMPLATE <date>_vN.xlsx`, in `lib/research/identity/data/universe.json`), and it
is the newest of the two versions of that name.

## The candidates in `Asset Management/`

| # | File | Last modified (UTC) | Size | Sheets | Item id |
|---|---|---|---|---|---|
| 1 | `FactSet Based ONE PAGER TEMPLATE 2026 03 09_v2.xlsx` | 2026-07-24 | 383,839 | `__FDSCACHE__`, `_CIQHiddenCacheSheet`, `Model NEW VERSION`, `Charts`, `Model`, `CSC` | `01L6LHKFRTYYYRWCI37VGLHJQPCL3KMJXN` |
| 2 | `FactSet Based ONE PAGER TEMPLATE 2026 03 09_v1.xlsx` | 2026-05-04 | 383,776 | same six, same order | `01L6LHKFTKDOGLDD2WSFH3EVZD3UPEBR67` |
| 3 | `ONE PAGE TEMPLATE - FactSet_QA_QTR.xlsx` | 2026-09-02 | 323,664 | `FactSet Cover Sheet`, `Model NEW VERSION`, `Model NEW VERSION (update)` | `01L6LHKFT7L2L4J7ARC5HJUIGTQ25XKSO5` |
| 4 | `FactSet Conversion ONE PAGER TEMPLATE 2026 03 09_v1.xlsx` | 2026-03-10 | 382,431 | `__FDSCACHE__`, `_CIQHiddenCacheSheet`, `Model NEW VERSION`, `Model`, `Charts`, `CSC` | `01L6LHKFQW2JLHNZAIOZEJG7TBZITPPD4E` |
| 5 | `ONE PAGER TEMPLATE 2025 12 19_v1.xlsx` | 2026-03-02 | 301,358 | `_CIQHiddenCacheSheet`, `Model`, `Sheet1`, `CSC` | `01L6LHKFWMLUSXE6S7PNFYPIS5VSTOAVLR` |
| 6 | `Orange FactSet Based ONE PAGER TEMPLATE 2026 03 09_v1.xlsx` | 2026-05-04 | 386,206 | not read | `01L6LHKFQE3W5QMGJFENE3CU6C3BKK7DXD` |

Three things in that table decide the call:

1. **Candidate 3 is the newest file and is a different shape.** It was modified 2026-09-02, after candidate 1, and
   carries a sheet named `Model NEW VERSION (update)`. Its name says quarterly and QA. Whether the team now works
   from it is not something a file listing can say.
2. **Two model sheets sit in the same workbook.** Candidates 1, 2 and 4 each hold both `Model` and
   `Model NEW VERSION`. FWD-12's row set has to name one sheet, not just one file.
3. **Candidate 5 is the pre-FactSet template** (one `Model` sheet, no `Model NEW VERSION`). A byte-identical backup
   of it sits in `Asset Management/BACKUP Research Templates DO NOT USE/` (same quickXorHash), beside a backup of
   the FactSet v1 template. That folder's name is the team's own instruction.

## Other places a "template" lives, and why I rank them lower

| Place | What is there | Why lower |
|---|---|---|
| `Research/Model Templates/` (site root, not under `Asset Management/`) | 9 `DIVZ ...` model workbooks (one of them `DIVZ Bank Model Template BB v.01.xlsx`), plus `Pharma Model v.01.xlsx` | An older generation: most last modified 2021 to 2023; two touched 2026-01-20. `DIVZ Company Model Template BB v.03.xlsx` has sheets `_CIQHiddenCacheSheet`, `Overview`, `CSC`, with no `Model` sheet. The sector-specific names (Bank, Pharma) are the only per-sector templates I found |
| `Asset Management/Research Folder Copy for Claude Use/` | a copy of the research tree, 102 children, modified 2026-09-28 | Not opened. Its name says it was made for this purpose; whether it or `Research/` is the intended read surface is Andrew's to say |
| `Asset Management/Vident Actively Managed Model Template-*.xlsx` (3 files) | fund model-portfolio templates | Not company research |

## What bounds this

- **Search coverage.** The site search for "template" returned 200 hits with a next page I did not follow. I read
  the first page's names, then listed three folders in full: `Asset Management/` (20 children),
  `Research/Model Templates/` (13) and the backup folder (2). A template elsewhere on the site, or in another
  library or site, is not excluded. `list_site_files` reads the default library only.
- **Sheet names were read for 6 workbooks** (candidates 1 to 5 and one `Model Templates` file). Each read asked for
  one row; two answers came back oversized because the first sheet is a wide hidden cache, and I took the sheet
  list from them and nothing else.
- **I did not read any model sheet's rows**, so I have not checked which sheet matches the page's rows. That is
  the comparison cell's job.
- **The per-sector point matters for FWD-12 as written.** The PRD says rows come from "the template for that
  business type". Under `Asset Management/` I found one generic template family and no per-business-type set. If
  FWD-12 needs a template per business type, the only candidates by name are the old Bank and Pharma workbooks.

## Calls that are not this seat's

1. Which file is the team's current template: candidate 1 (matches the per-company file names) or candidate 3
   (newest). One question to the research team settles it.
2. Which sheet is the row set: `Model` or `Model NEW VERSION`.
3. Whether the comparison reads the master template or each company's own copy of it in `Research/<folder>/`.
