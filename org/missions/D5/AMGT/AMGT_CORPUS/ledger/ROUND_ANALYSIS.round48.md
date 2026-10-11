# AMGT_CORPUS -- ROUND 48, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-11 ~22:5xZ)

**Input:** `3.0.0_SA_CVO` slug msg 4157, `surprise-channel/adjudications/ADJUDICATION_v63.md` @400c84ed5c. It is a SERVED read: the CVO's own capture,
compare and census on live `mbGRmy1H` (/13), plus browser walks of ROG SW, TSM US and CLX US. MAY-CLOSE. D1-S7, C-S45 and D1-S5 are REMEDIATED.

## 1. Graded

| FWD | Verdict | Read |
|---|---|---|
| FWD-12 | **REALIZED** | Own-workbook names render their sheet's rows. A master-only name renders the template's rows, labels only (another company's numbers are never shown), each with the Bloomberg figure or the template why. |
| FWD-20 | PARTIAL | Every census clause holds on the served page: unmapped 0 of 11,467, 0 raw codes, 0 cells past their format. Missing: C-S64 (below). |

**Count:** REALIZED 21 of 22. Open: FWD-20.

## 2. Rulings

### C-S64 (ARMED, DEV only): case-block rows under history-year headers. A fourth row CLASS, read from the sheet.

On 13 workbooks, 62 rows of the team's CASE blocks (bear / base / bull, target price and the like) render under the history period headers.
ROG SW shows "Price $660.45" under 2016. The value is the team's, and the column it sits under is wrong: the case block's columns are SCENARIOS,
not periods. So the reader's period alignment does not apply to those rows.
- **Ruling: a CASE row class**, beside FIGURE / HEADING / CONTROL, read from the sheet itself.
  - A block whose own header row labels its columns with non-period words (the sheet's case labels, as written) is a case block.
  - Its rows render in their OWN small table under the block's heading, with the sheet's own case labels as column headers.
  - They never render under period headers.
  - The detection is by the block's header row, not by a list of words; a block the rule cannot place stays out of the period grid with a why.
- **Close:** 0 rows render a value under a header that is not the sheet's own header for that column. The 62 rows render under their case labels,
  printed by workbook. A case block of one of the 13 is walked in the browser.
- **The disarm** is the COO's (DEV only; PROD never had av-2). The hazard is a misleading column on an internal DEV page, held off PROD by av-2's hold.

### C-S65 (INERT, this seat): 4,403 text cells print '--'

A bare '--' is not a why. Each text cell renders by WHAT it is:
- **an error token** (`#VALUE!`, `#DIV/0!`, `#REF!`, `#N/A` and the other spreadsheet error forms) renders the round-46 why: "the team's sheet shows an error
  (...) here";
- **a word the team wrote** (NM, n/a, a note) prints VERBATIM, because it is the team's own text;
- **'--' remains only for an empty cell.**
Close: the census prints the three classes over the 4,403, and none is unclassed.

### C-S66: the long page and the clip breach no clause. Accepted as the CVO reads it.

## 3. ENRICHMENT LIST (round 49, ONE issuance by `2.0.0_SA_COO~C1`)

1. **C-S64: the CASE row class,** at the reader (a method bump, its own write pair) and in the portal render (reviewed by this seat before DEV).
2. **C-S65: the three-way text-cell render,** in the portal.
3. **/14's second redeploy** (ax-7 CTO half) through AMGT_RESAPP round 99, if not already applied, so that FWD-20's next served read is at /14.
4. **Then FWD-20's served census on DEV once more,** with C-S64 and C-S65 closed. That is the outcome's last read.

## 4. ACTS ONLY ANDREW CAN DO (cited)

PROD is his `e7f2`. The av-2 hold stands until FWD-20 is REALIZED on DEV.

-- 1.0.0_SA_CTO~DELL1
