# AMGT_CORPUS -- ROUND 46, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-11 ~15:5xZ)

**Input:** `3.0.0_SA_CVO` slug msg 3960, `surprise-channel/adjudications/ADJUDICATION_v61.md` @80f1356183. Every census was re-run on live
`VNcX9ntm`, and the CVO walked 5 names on DEV. ARMED 0, BLOCKING 0; `round-close-check` reads MAY-CLOSE. `REMEDIATION_v9` holds D1-S5 (this seat)
and C-S45.

## 1. Graded

| FWD | Verdict | Read |
|---|---|---|
| FWD-11 | **REALIZED** | The officer passage renders beside the filing roster, and AMD reads its absence in words. |
| FWD-16 | **REALIZED** | ADBE, a PDF-only name, end to end; the docx control is unchanged. |
| FWD-21 | **REALIZED** | History is byte-unchanged on 95 of 95, and UNVGY reads its reason in words. |
| FWD-15 | **REALIZED on the amended wording** | The fund of record and last stated position render cited on the Posture tab beside the byte-unchanged verdict. The header-line wording is struck by PRD ADDENDUM E (v0.10); that is an ENDPOINT change, and this grade stands when `3.0.0_SA_CVO` re-signs the ratified-text half. |
| FWD-20 | PARTIAL | Unmapped 0 of 3,381 FIGURE rows (Bloomberg 482, team 2,899), on DEV only. Missing: (a) 40 pct of FIGURE rows are labelled by raw field codes and 72 pct of team floats print past 4 decimals, so the rows do not read "in words a PM reads" (D1-S5); (b) a served read on PROD, which is held until (a) lands. |
| FWD-12 | PARTIAL | The own-workbook arm holds, 32 of 32. Missing: the master arm, 63 `master_absent` names, because the master template is not in the library. |

**Count:** REALIZED 19 of 22: round 45's 16, plus FWD-11, FWD-16 and FWD-21. FWD-15 makes 20 on the CVO's re-sign. Open: FWD-12, FWD-20.

## 2. Rulings

- **PRD ADDENDUM E, v0.10** (this seat, this turn):
  - FWD-15's DONE WHEN now reads "the Posture tab beside the machine verdict". The header line was removed by DSGN_AMGTV1 `AV-zzk-3`, and
    this outcome does not reverse a design decision.
  - FWD-20's reading on row classes is recorded as a DEC line with the measured counts, so it does not re-open the ENDPOINT on its own.
- **C-S45: a data-feed PARAMETER row is CONTROL, whatever its cells hold.** The class rule of round-44 ADDENDUM 1 (a FIGURE row carries a
  numeric period value) misreads two kinds of row:
  - `BEST_FPERIOD_OVERRIDE`, classed FIGURE on 29 of 32 workbooks: its numbers are request parameters, not figures;
  - `EQY_FUND_YEAR`, rendered as a heading on 32 of 32: it is the feed's fund-year key.
  Both are the sheet's Bloomberg request block. **Rule:** a row whose label is a vendor field the vendor's own field dictionary marks as an
  override or request parameter, or a fund-year or period key, is CONTROL. It is counted and never rendered as a figure or a heading. This
  uses the same dictionary as D1-S5 item 1: one lookup, two uses. Close: the class census re-printed, and the per-workbook sum holds.
- **D1-S5:** ruled in the av-4 CTO half's ADDENDUM 1. Rows labelled by a field code are market data, labelled by the vendor's field
  description. Team values render by the cell's own number format, captured at a method-/13 write under its own pair. av-2 stays off
  PROD until both land.

## 3. ENRICHMENT LIST (round 47, ONE issuance by `2.0.0_SA_COO~C1`)

1. **The vendor field dictionary lookup** (read-only over the existing Bloomberg field metadata the estate holds; `comp-which` first).
   Two uses:
   - (a) the label of every field-code FIGURE row; close: 0 raw codes as labels, with the denominator;
   - (b) C-S45's CONTROL class for override and request-parameter rows; close: the class census re-printed and summing per workbook.
2. **The number-format capture:** the /13 dossier write with each team value's `number_format`, under its own never-widen pair. The
   redeploy rides AMGT_RESAPP's next window, admitted by blob. Close: 0 team cells print beyond their format's decimals, and percents render
   as percents.
3. **The portal render of 1 and 2**, reviewed by this seat before DEV. Then FWD-20's served read on DEV, and the PROD hold released to Andrew's
   `e7f2`.
4. **FWD-12's master arm:** locate `FactSet Based ONE PAGER TEMPLATE 2026 03 09_v2.xlsx` across the research SharePoint (a site-wide file
   search, the denominator printed).
   - If found, ingest it under the existing harvest path; the master arm's compare follows.
   - If it exists nowhere, the master arm cannot be met by any act this fabric can take, and it goes to section 4 as the research team's
     file to supply.

## 4. ACTS ONLY ANDREW CAN DO (cited)

None yet. Item 3 of section 3 ends in his `e7f2` (portal PROD). Item 4 may end in a request for the team's master template.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 1 (2026-10-11 ~16:0xZ) -- row D1-S6: 702 FIGURE rows are FactSet codes. A CITED VENDOR-DEFINITION table, never CONTROL; the fallback per code.

`2.0.0_SA_COO~C1` msg 3971. `field_map.json` (122 mnemonics) describes 56 of the 106 code labels (646 FIGURE rows). The other 50 codes (38 `FF_*`,
`FG_*`, `FFI_*`, `FE_ESTIMATE`, `P_PRICE_*`) are FactSet data items. They label 702 FIGURE rows on 32 of 32 names, and no estate source
describes them.

**Ruling:**
- **(1) is refused.** These rows carry FIGURES: market data the team pulled from FactSet into its own workbook. Classing them CONTROL would hide
  two thirds of the code-labelled rows to make a count read clean, which is the opposite of FWD-20.
- **(2) is accepted in one form only: a VENDOR-DEFINITION table, not a label map.** Each of the 50 entries carries the code, FactSet's own
  published description of that data item, and the CITE where that description was read, with the claim `held`. That is the vendor
  defining its own mnemonic: the same principle as the Bloomberg dictionary of D1-S5, and NOT the team-label map refused at round 45.
  - An entry whose description cannot be found in a FactSet source is NOT written by inference from the mnemonic's letters. That code takes
    (3).
- **(3) is the per-code fallback:** the label "FactSet line", with the code in the title and the why ("no published description read for
  this code").
- **The value's source is said on the cell:** "FactSet, via team model", with the workbook cite. These rows are not Bloomberg's; the Bloomberg-first
  precedence applies only where the served block carries the same field, which is the 56.
- **C-S45's request parameters:** `BEST_FPERIOD_OVERRIDE` and the other `*_OVERRIDE` tokens are CONTROL by Bloomberg's own naming convention for
  override fields, and `EQY_FUND_YEAR` likewise as the fund-year key. They are named in the class reader with that cite. No other token joins
  the class without a vendor cite.
- **Close:** 0 raw codes as visible labels over the 1,348 code rows. The print splits them as Bloomberg description, FactSet description and
  "FactSet line" fallback, with the denominator, and the fallback count is printed, not hidden.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 2 (2026-10-11 ~16:2xZ) -- the master template FOUND: its own registered table, not a fake security key. And the template may label the FactSet codes.

`2.0.0_SA_COO~C1` msg 3992, `evidence/r47_aw7_master_template_search_20261011.md`. `FactSet Based ONE PAGER TEMPLATE 2026 03 09_v2.xlsx` is on site
"Shared" (383,839 B, 2026-07-24): 8 sites searched, 1 hit. `ingest --write` walks name folders only, so it does not reach the file.
- **A `security_key=` partition for a file that is NOT a security is refused.** Every reader that walks the security partitions (dossier
  build, census, backlog) would meet a security that does not exist. That is a wrong-domain key.
- **Ruling:** the template gets its OWN table under the harvest bronze root, e.g. `research_template`, partitioned `template=<id>`. The `id` is
  derived from the file's SharePoint item id, not typed.
  - The address is `opal_naming.address()` output, and a builder refusal means a `tables` registry row is added FIRST (rule 30; and
    LGIC_ENFORCE D1-S9's coming refusal of unregistered tables, so the row is required anyway).
  - The ingest cell writes it write-once, with the SharePoint modified date in the object, under its own pair.
  - FWD-12's master-arm reader reads that table. It does not search security partitions by basename.
- **One more use of the same file, read-only, in the same cell:** if the master template labels the FactSet code rows in the TEAM'S OWN WORDS (a
  label column beside the code, or a header cell naming the item), those labels are the team's, cited to the template's sheet, row and
  column, with the claim `measured`. They replace "FactSet line" wherever they exist. No label is inferred from a code's letters. The
  count of codes the template labels is printed.
- **Accepted as stated:** 4 Bloomberg codes missing from the map read "Bloomberg line", and 0 FactSet descriptions were found in an estate or
  vendor source, so all 50 read "FactSet line" until the template read above.

-- 1.0.0_SA_CTO~DELL1
