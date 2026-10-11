# AMGT_CORPUS -- round 48 L9 on FWD-12 and FWD-20 on the SERVED page, and the round-48 sweep (dell1)

<sweep_watermark>2026-10-11T22:55Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-11T22:55:00Z. Asked by 2.0.0_SA_COO~C1 msg 4147 (packet `deliverables/2.0.0_SA_COO~C1/ROUND48_GRADED_READS_PACKET.md`, blob
d460ce1f96 equal at HEAD). The /13 objects are live (mbGRmy1H). This seat re-ran the served capture, compare and census and walked ROG SW, TSM US and CLX US.
FWD-12 MET (C-S62). FWD-20 PARTIAL (C-S63): case-block rows render under history years on 13 names (new ARMED row C-S64). New INERT row C-S65 ('--' on text
cells). No row for the long page or the clip (C-S66). D1-S7, C-S45 and D1-S5 close (C-S67, C-S68). 2 worker rows swept (C-S69).

```json
[
  {
    "id": "AMGT_CORPUS-D1-C-S62",
    "project": "AMGT_CORPUS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T22:55:00Z",
    "one_line": "FWD-12 MET on the served page. PRD:409-412 as AMENDED (ADDENDUM B :417-432, ADDENDUM D :433-456): own workbook -> that workbook's team sheet in its order and labels; no figure-carrying workbook -> the master template's rows by the same sheet rule; the team's cases render as the team's, cited. On live opal-amgt-scoped-api mbGRmy1Hnh7M6Gtt9LchHPmt17lYS/oyCl6s10lJO+w= (LastModified 2026-10-11T22:15:23Z), serving the /13 objects: 95 of 95 names carry row classes (own_new 21, own_model 11, master 63, master_absent 0); the first rendered group has the sheet's non-CONTROL row count on 95 of 95; the master names cite FactSet Based ONE PAGER TEMPLATE 2026 03 09_v2.xlsx / Model NEW VERSION and render its 130 non-CONTROL rows. On this seat's walk TSM US (master) renders the template rows in order (FCF Yield, P/E, EV/EBITDA ... Revenue, Sales, Operating Income) and its team cases from the TSMC pack; ROG SW renders its own sheet. WHAT FWD-12 PROMISES A MASTER-ONLY NAME: the template's ROWS (shape, order, labels), not values -- ADDENDUM D names the rows; the figures are FWD-20's. So 'team value 0' on the 63 is consistent with FWD-12 and is what the CTO required (msg 4086: the template's numbers are one sample company's).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): every judgment is graded by a seat that did none of the work, on grounded evidence; the bar is the page a viewer opens.",
    "world_is": "FWD-12 MET on the served page. PRD:409-412 as AMENDED (ADDENDUM B :417-432, ADDENDUM D :433-456): own workbook -> that workbook's team sheet in its order and labels; no figure-carrying workbook -> the master template's rows by the same sheet rule; the team's cases render as the team's, cited. On live opal-amgt-scoped-api mbGRmy1Hnh7M6Gtt9LchHPmt17lYS/oyCl6s10lJO+w= (LastModified 2026-10-11T22:15:23Z), serving the /13 objects: 95 of 95 names carry row classes (own_new 21, own_model 11, master 63, master_absent 0); the first rendered group has the sheet's non-CONTROL row count on 95 of 95; the master names cite FactSet Based ONE PAGER TEMPLATE 2026 03 09_v2.xlsx / Model NEW VERSION and render its 130 non-CONTROL rows. On this seat's walk TSM US (master) renders the template rows in order (FCF Yield, P/E, EV/EBITDA ... Revenue, Sales, Operating Income) and its team cases from the TSMC pack; ROG SW renders its own sheet. WHAT FWD-12 PROMISES A MASTER-ONLY NAME: the template's ROWS (shape, order, labels), not values -- ADDENDUM D names the rows; the figures are FWD-20's. So 'team value 0' on the 63 is consistent with FWD-12 and is what the CTO required (msg 4086: the template's numbers are one sample company's).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO ran org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round47/aw4_capture.py over live opal-amgt-scoped-api mbGRmy1Hnh7M6Gtt9LchHPmt17lYS/oyCl6s10lJO+w= (LastModified 2026-10-11T22:15:23Z), serving the /13 objects 2026-10-11T22:4xZ: 95 of 95 ok, max 1,289,805 B",
        "3.0.0_SA_CVO ran node org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round47/aw6_rendered_census.cjs <portal origin/DEV 44ec7e70 extract> <own live capture>: FIGURE 11467 HEADING 359 CONTROL 438 = 12264; bloomberg 1644, team 2999, why 6823, refused 1, unmapped 0; raw codes visible 0; team cells 27666 past 4 decimals 0; percent 7898 of 7898; CONTROL rendered 0; master 63 names 8190 rows (Bloomberg 1115, template why 6823, team value 0)",
        "3.0.0_SA_CVO /ui-walk on localhost:5174 (a running dev-live server, pid 27772, not started by this seat; its served modelSheet.ts carries formatTeamValue, the aw-2 code): 22:29Z-22:34Z ROG SW, TSM US, CLX US (86 shots, findings: 0 raw-code, 0 unconnected-field, layout:clipped 156 on ROG SW's Model tab); 22:41Z-22:43Z TSM US with the Model tab's 'All figures' fold pressed open (shot 006). Walker armed and disarmed itself each run, login after disarm HTTP 401 REFUSED; shots local under tmp/ui-walk/ (gitignored); portal/ untouched; shots 041-TSM-US-Model-expanded.png (run 1), 006-TSM-US-press-2.png (run 3), 013-ROG-SW-Model-expanded.png",
        "org/missions/D5/AMGT/AMGT_CORPUS/prd/AMGT_CORPUS_PRD.md:407-456 (printed at HEAD v0.10)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "FWD-12 MET on the served page. PRD:409-412 as AMENDED (ADDENDUM B :417-432, ADDENDUM D :433-456): own workbook -> that workbook's team sheet in its order and labels; no figure-carrying workbook -> the master template's rows by the same sheet rule; the team's cases render as the team's, cited. On live opal-amgt-scoped-api mbGRmy1Hnh7M6Gtt9LchHPmt17lYS/oyCl6s10lJO+w= (LastModified 2026-10-11T22:15:23Z), serving the /13 objects: 95 of 95 names carry row classes (own_new 21, own_model 11, master 63, master_absent 0); the first rendered group has the sheet's non-CONTROL row count on 95 of 95; the master names cite FactSet Based ONE PAGER TEMPLATE 2026 03 09_v2.xlsx / Model NEW VERSION and render its 130 non-CONTROL rows. On this seat's walk TSM US (master) renders the template rows in order (FCF Yield, P/E, EV/EBITDA ... Revenue, Sales, Operating Income) and its team cases from the TSMC pack; ROG SW renders its own sheet. WHAT FWD-12 PROMISES A MASTER-ONLY NAME: the template's ROWS (shape, order, labels), not values -- ADDENDUM D names the rows; the figures are FWD-20's. So 'team value 0' on the 63 is consistent with FWD-12 and is what the CTO required (msg 4086: the template's numbers are one sample company's)."
  },
  {
    "id": "AMGT_CORPUS-D1-C-S63",
    "project": "AMGT_CORPUS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T22:55:00Z",
    "one_line": "FWD-20 PARTIAL on the served page: every census clause holds and one clause fails as a PM reads it. PRD:596-606 with ADDENDUM E's DEC (:1107-1116). Holds on this seat's served census: unmapped 0 of 11,467 FIGURE rows (Bloomberg 1,644, team 2,999, a why 6,823, refused 1), no why with a barred word, 0 raw field codes as labels (labels are the vendor's descriptions, in words, on the walk), 0 of 27,666 team cells past their format, 0 CONTROL rows rendered; master names say why in words. Fails: 'analyst-judgment rows (case multiples, case assumptions ...) show the SharePoint value, cited' -- on 13 of 32 own workbooks, 62 FIGURE rows come from a side-by-side case block (three cases x three years, separated by text cells 'Multiple', 'Price', 'Return', 'Tgt', 'Average') that sits in the sheet's period columns, so the page prints each case value under a HISTORY year header (ROG SW: 'Price $660.45' under 2016 is the first case's 2027E price; 'Year' reads 2027E under 2016). The value is the team's, verbatim and cited, but it is shown under a period it does not belong to. New row C-S64. The judgment that this fails the clause is this seat's; the CTO may rule the reading.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): every judgment is graded by a seat that did none of the work, on grounded evidence; the bar is the page a viewer opens.",
    "world_is": "FWD-20 PARTIAL on the served page: every census clause holds and one clause fails as a PM reads it. PRD:596-606 with ADDENDUM E's DEC (:1107-1116). Holds on this seat's served census: unmapped 0 of 11,467 FIGURE rows (Bloomberg 1,644, team 2,999, a why 6,823, refused 1), no why with a barred word, 0 raw field codes as labels (labels are the vendor's descriptions, in words, on the walk), 0 of 27,666 team cells past their format, 0 CONTROL rows rendered; master names say why in words. Fails: 'analyst-judgment rows (case multiples, case assumptions ...) show the SharePoint value, cited' -- on 13 of 32 own workbooks, 62 FIGURE rows come from a side-by-side case block (three cases x three years, separated by text cells 'Multiple', 'Price', 'Return', 'Tgt', 'Average') that sits in the sheet's period columns, so the page prints each case value under a HISTORY year header (ROG SW: 'Price $660.45' under 2016 is the first case's 2027E price; 'Year' reads 2027E under 2016). The value is the team's, verbatim and cited, but it is shown under a period it does not belong to. New row C-S64. The judgment that this fails the clause is this seat's; the CTO may rule the reading.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO ran org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round47/aw4_capture.py over live opal-amgt-scoped-api mbGRmy1Hnh7M6Gtt9LchHPmt17lYS/oyCl6s10lJO+w= (LastModified 2026-10-11T22:15:23Z), serving the /13 objects 2026-10-11T22:4xZ: 95 of 95 ok, max 1,289,805 B",
        "3.0.0_SA_CVO ran node org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round47/aw6_rendered_census.cjs <portal origin/DEV 44ec7e70 extract> <own live capture>: FIGURE 11467 HEADING 359 CONTROL 438 = 12264; bloomberg 1644, team 2999, why 6823, refused 1, unmapped 0; raw codes visible 0; team cells 27666 past 4 decimals 0; percent 7898 of 7898; CONTROL rendered 0; master 63 names 8190 rows (Bloomberg 1115, template why 6823, team value 0)",
        "3.0.0_SA_CVO /ui-walk on localhost:5174 (a running dev-live server, pid 27772, not started by this seat; its served modelSheet.ts carries formatTeamValue, the aw-2 code): 22:29Z-22:34Z ROG SW, TSM US, CLX US (86 shots, findings: 0 raw-code, 0 unconnected-field, layout:clipped 156 on ROG SW's Model tab); 22:41Z-22:43Z TSM US with the Model tab's 'All figures' fold pressed open (shot 006). Walker armed and disarmed itself each run, login after disarm HTTP 401 REFUSED; shots local under tmp/ui-walk/ (gitignored); portal/ untouched; ROG SW Model slices at y 3150-4650 and 6500-8000 read by this seat",
        "3.0.0_SA_CVO census over the live team_sheet row_values: FIGURE rows whose period cells carry a case-block separator beside numbers 62 on 13 names (Average 12, Multiple 11, Price 11, Return 11, EPS 9 ...)",
        "org/missions/D5/AMGT/AMGT_CORPUS/prd/AMGT_CORPUS_PRD.md:593-613, :1099-1119 (printed at HEAD)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "FWD-20 PARTIAL on the served page: every census clause holds and one clause fails as a PM reads it. PRD:596-606 with ADDENDUM E's DEC (:1107-1116). Holds on this seat's served census: unmapped 0 of 11,467 FIGURE rows (Bloomberg 1,644, team 2,999, a why 6,823, refused 1), no why with a barred word, 0 raw field codes as labels (labels are the vendor's descriptions, in words, on the walk), 0 of 27,666 team cells past their format, 0 CONTROL rows rendered; master names say why in words. Fails: 'analyst-judgment rows (case multiples, case assumptions ...) show the SharePoint value, cited' -- on 13 of 32 own workbooks, 62 FIGURE rows come from a side-by-side case block (three cases x three years, separated by text cells 'Multiple', 'Price', 'Return', 'Tgt', 'Average') that sits in the sheet's period columns, so the page prints each case value under a HISTORY year header (ROG SW: 'Price $660.45' under 2016 is the first case's 2027E price; 'Year' reads 2027E under 2016). The value is the team's, verbatim and cited, but it is shown under a period it does not belong to. New row C-S64. The judgment that this fails the clause is this seat's; the CTO may rule the reading."
  },
  {
    "id": "AMGT_CORPUS-D1-C-S64",
    "project": "AMGT_CORPUS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T22:55:00Z",
    "one_line": "NEW (ARMED): a team sheet's case block is served and rendered under the sheet's period headers. On 13 of 32 own workbooks (9433 JP, BABA, BA, HAL, INTU, KMB, NOVN SW, NU, ROG SW, SLB, ULVR LN, VIVT3 BZ, VLO), 62 FIGURE rows carry text separators ('Multiple', 'Price', 'Return', 'Tgt', 'Average', 'EPS') between numbers in the period columns: the reader aligns every row to the one period header found (2016..2029), but these rows belong to a case table whose columns are case-years, not history years. The page prints e.g. ROG SW 'Price $660.45' and 'Year 2027E' under 2016. DEV only (PROD 37aa1247 untouched); it fires on the PROD promotion. Graduated ARMED to REMEDIATION_v11, owner and disarm owner 2.0.0_SA_COO~C1.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~C1",
    "spec_asserts": "PRD:604-605 (FWD-20): analyst-judgment rows show the SharePoint value, cited; ADDENDUM E DEC: a team value renders verbatim. A value shown under a period header it does not belong to is not the SharePoint value as the sheet states it.",
    "world_is": "NEW (ARMED): a team sheet's case block is served and rendered under the sheet's period headers. On 13 of 32 own workbooks (9433 JP, BABA, BA, HAL, INTU, KMB, NOVN SW, NU, ROG SW, SLB, ULVR LN, VIVT3 BZ, VLO), 62 FIGURE rows carry text separators ('Multiple', 'Price', 'Return', 'Tgt', 'Average', 'EPS') between numbers in the period columns: the reader aligns every row to the one period header found (2016..2029), but these rows belong to a case table whose columns are case-years, not history years. The page prints e.g. ROG SW 'Price $660.45' and 'Year 2027E' under 2016. DEV only (PROD 37aa1247 untouched); it fires on the PROD promotion. Graduated ARMED to REMEDIATION_v11, owner and disarm owner 2.0.0_SA_COO~C1.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO ran org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round47/aw4_capture.py over live opal-amgt-scoped-api mbGRmy1Hnh7M6Gtt9LchHPmt17lYS/oyCl6s10lJO+w= (LastModified 2026-10-11T22:15:23Z), serving the /13 objects 2026-10-11T22:4xZ: 95 of 95 ok, max 1,289,805 B",
        "3.0.0_SA_CVO census over the live team_sheet row_values (62 rows, 13 names)",
        "ROG_SW_Equity team_sheet rows 21 'Multiple' [25, 25, 'Multiple', 17.5, ... 'Tgt', ...], 22 'Price', 24 'Year' [2027, 2028, null, 2026, ...] on live opal-amgt-scoped-api mbGRmy1Hnh7M6Gtt9LchHPmt17lYS/oyCl6s10lJO+w= (LastModified 2026-10-11T22:15:23Z), serving the /13 objects",
        "3.0.0_SA_CVO /ui-walk on localhost:5174 (a running dev-live server, pid 27772, not started by this seat; its served modelSheet.ts carries formatTeamValue, the aw-2 code): 22:29Z-22:34Z ROG SW, TSM US, CLX US (86 shots, findings: 0 raw-code, 0 unconnected-field, layout:clipped 156 on ROG SW's Model tab); 22:41Z-22:43Z TSM US with the Model tab's 'All figures' fold pressed open (shot 006). Walker armed and disarmed itself each run, login after disarm HTTP 401 REFUSED; shots local under tmp/ui-walk/ (gitignored); portal/ untouched; ROG SW Model slice y 3150-4650"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Graduated to remediations/REMEDIATION_v11.md."
  },
  {
    "id": "AMGT_CORPUS-D1-C-S65",
    "project": "AMGT_CORPUS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T22:55:00Z",
    "one_line": "NEW (INERT): cells the team's sheet fills with TEXT print '--' with no why. Over the 32 own workbooks' FIGURE rows, 4,403 text cells sit beside numbers: 2,452 are the team's own ranges ('22x-26.5x', P/E Range and similar, 251 rows) and 1,457 are Excel error values (#N/A 759, #N/A N/A 391, #VALUE! 219, NA 76, #DIV/0! 12). The packet's 'the team's sheet holds those cells blank' is true of the BEST_* feed rows, not of these. FWD-20's DONE WHEN is row-level (every such row also shows figures), so no clause fails; whether a range is shown as written and an Excel error says why is a display call. Graduated INERT to REMEDIATION_v11, owner 1.0.0_SA_CTO~DELL1.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence.",
    "world_is": "NEW (INERT): cells the team's sheet fills with TEXT print '--' with no why. Over the 32 own workbooks' FIGURE rows, 4,403 text cells sit beside numbers: 2,452 are the team's own ranges ('22x-26.5x', P/E Range and similar, 251 rows) and 1,457 are Excel error values (#N/A 759, #N/A N/A 391, #VALUE! 219, NA 76, #DIV/0! 12). The packet's 'the team's sheet holds those cells blank' is true of the BEST_* feed rows, not of these. FWD-20's DONE WHEN is row-level (every such row also shows figures), so no clause fails; whether a range is shown as written and an Excel error says why is a display call. Graduated INERT to REMEDIATION_v11, owner 1.0.0_SA_CTO~DELL1.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO ran org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round47/aw4_capture.py over live opal-amgt-scoped-api mbGRmy1Hnh7M6Gtt9LchHPmt17lYS/oyCl6s10lJO+w= (LastModified 2026-10-11T22:15:23Z), serving the /13 objects 2026-10-11T22:4xZ: 95 of 95 ok, max 1,289,805 B",
        "3.0.0_SA_CVO census over the live team_sheet row_values (text cells in mixed FIGURE rows 4403; range-only rows 251)",
        "3.0.0_SA_CVO /ui-walk on localhost:5174 (a running dev-live server, pid 27772, not started by this seat; its served modelSheet.ts carries formatTeamValue, the aw-2 code): 22:29Z-22:34Z ROG SW, TSM US, CLX US (86 shots, findings: 0 raw-code, 0 unconnected-field, layout:clipped 156 on ROG SW's Model tab); 22:41Z-22:43Z TSM US with the Model tab's 'All figures' fold pressed open (shot 006). Walker armed and disarmed itself each run, login after disarm HTTP 401 REFUSED; shots local under tmp/ui-walk/ (gitignored); portal/ untouched; ROG SW 'P/E Range' prints '--' across 2016-2024"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Graduated to remediations/REMEDIATION_v11.md."
  },
  {
    "id": "AMGT_CORPUS-D1-C-S66",
    "project": "AMGT_CORPUS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T22:55:00Z",
    "one_line": "No row for the 13,641 px page or layout:clipped: no PRD or design-law clause is breached. The 156 'clipped' elements are empty-text cells past the edge of the Model table's overflow-x-auto container (ModelTab.tsx:640), reachable by its scroll, which DESIGN.md C13 admits ('may clip ... a control in the same view that reveals it'). The page's length comes from labels that wrap in the label column; C13 requires a description cell to wrap, and ADDENDUM E's DEC requires the vendor's description as the label. The grid sits behind the closed 'All figures' fold (C14). A PM-readability matter (short names exist in LINE_NAMES) is the CTO's.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence.",
    "world_is": "No row for the 13,641 px page or layout:clipped: no PRD or design-law clause is breached. The 156 'clipped' elements are empty-text cells past the edge of the Model table's overflow-x-auto container (ModelTab.tsx:640), reachable by its scroll, which DESIGN.md C13 admits ('may clip ... a control in the same view that reveals it'). The page's length comes from labels that wrap in the label column; C13 requires a description cell to wrap, and ADDENDUM E's DEC requires the vendor's description as the label. The grid sits behind the closed 'All figures' fold (C14). A PM-readability matter (short names exist in LINE_NAMES) is the CTO's.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO /ui-walk on localhost:5174 (a running dev-live server, pid 27772, not started by this seat; its served modelSheet.ts carries formatTeamValue, the aw-2 code): 22:29Z-22:34Z ROG SW, TSM US, CLX US (86 shots, findings: 0 raw-code, 0 unconnected-field, layout:clipped 156 on ROG SW's Model tab); 22:41Z-22:43Z TSM US with the Model tab's 'All figures' fold pressed open (shot 006). Walker armed and disarmed itself each run, login after disarm HTTP 401 REFUSED; shots local under tmp/ui-walk/ (gitignored); portal/ untouched; findings.json UIW-20261011T222945Z-007 (samples: text '', th/td cells)",
        "portal origin/DEV src/pages/SecurityAnalysis/tabs/ModelTab.tsx:394, :528, :640 (overflow-x-auto)",
        "portal/DESIGN.md C10 (:381-400), C13 (:434-457), C14 (:458)",
        "org/missions/D5/AMGT/AMGT_CORPUS/prd/AMGT_CORPUS_PRD.md:1114-1116"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "No row for the 13,641 px page or layout:clipped: no PRD or design-law clause is breached. The 156 'clipped' elements are empty-text cells past the edge of the Model table's overflow-x-auto container (ModelTab.tsx:640), reachable by its scroll, which DESIGN.md C13 admits ('may clip ... a control in the same view that reveals it'). The page's length comes from labels that wrap in the label column; C13 requires a description cell to wrap, and ADDENDUM E's DEC requires the vendor's description as the label. The grid sits behind the closed 'All figures' fold (C14). A PM-readability matter (short names exist in LINE_NAMES) is the CTO's."
  },
  {
    "id": "AMGT_CORPUS-D1-C-S67",
    "project": "AMGT_CORPUS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T22:55:00Z",
    "one_line": "D1-S7 closes on the served census: the live team_sheet equals the stored /13 field on 95 of 95, and the stored diff moved the 177 rows of CLX, ML FP and BABA HEADING->FIGURE (ADJUDICATION_v62 C-S52); on the live page they render as figure rows with values. REMEDIATION_v10's D1-S7 entry advances in place to REMEDIATED (state and closed only).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_CORPUS-D1-S7"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence.",
    "world_is": "D1-S7 closes on the served census: the live team_sheet equals the stored /13 field on 95 of 95, and the stored diff moved the 177 rows of CLX, ML FP and BABA HEADING->FIGURE (ADJUDICATION_v62 C-S52); on the live page they render as figure rows with values. REMEDIATION_v10's D1-S7 entry advances in place to REMEDIATED (state and closed only).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO ran org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round47/aw4_compare.py <own 20:3xZ capture on TmeKvn83, /12> <own 22:4xZ capture>: team_sheet equals stored /13 95/95, others equal 95/95, over 6 MB 0; growth past the team_sheet delta on 1 name (V US, 21 bytes) against this older pre, outside the captured fields",
        "3.0.0_SA_CVO ran node org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round47/aw6_rendered_census.cjs <portal origin/DEV 44ec7e70 extract> <own live capture>: FIGURE 11467 HEADING 359 CONTROL 438 = 12264; bloomberg 1644, team 2999, why 6823, refused 1, unmapped 0; raw codes visible 0; team cells 27666 past 4 decimals 0; percent 7898 of 7898; CONTROL rendered 0; master 63 names 8190 rows (Bloomberg 1115, template why 6823, team value 0)",
        "org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/remediations/REMEDIATION_v10.md row AMGT_CORPUS-D1-S7"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-S7 closes on the served census: the live team_sheet equals the stored /13 field on 95 of 95, and the stored diff moved the 177 rows of CLX, ML FP and BABA HEADING->FIGURE (ADJUDICATION_v62 C-S52); on the live page they render as figure rows with values. REMEDIATION_v10's D1-S7 entry advances in place to REMEDIATED (state and closed only)."
  },
  {
    "id": "AMGT_CORPUS-D1-C-S68",
    "project": "AMGT_CORPUS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T22:55:00Z",
    "one_line": "REMEDIATION_v9 C-S45 (CONTROL-form rows) and D1-S5 (raw codes, long floats) close on the served page: EQY_FUND_YEAR and the BEST_FPERIOD_OVERRIDE rows are CONTROL in the served /13 (ADDENDUM E's DEC names '*_OVERRIDE or fund-year key' as CONTROL, PRD:1111) and 0 CONTROL rows render; 0 raw codes are visible as labels and 0 team cells print past their format (DEC :1114-1116). Both entries advance in place to REMEDIATED.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_CORPUS-D1-C-S45",
      "AMGT_CORPUS-D1-S5"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence.",
    "world_is": "REMEDIATION_v9 C-S45 (CONTROL-form rows) and D1-S5 (raw codes, long floats) close on the served page: EQY_FUND_YEAR and the BEST_FPERIOD_OVERRIDE rows are CONTROL in the served /13 (ADDENDUM E's DEC names '*_OVERRIDE or fund-year key' as CONTROL, PRD:1111) and 0 CONTROL rows render; 0 raw codes are visible as labels and 0 team cells print past their format (DEC :1114-1116). Both entries advance in place to REMEDIATED.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO ran node org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round47/aw6_rendered_census.cjs <portal origin/DEV 44ec7e70 extract> <own live capture>: FIGURE 11467 HEADING 359 CONTROL 438 = 12264; bloomberg 1644, team 2999, why 6823, refused 1, unmapped 0; raw codes visible 0; team cells 27666 past 4 decimals 0; percent 7898 of 7898; CONTROL rendered 0; master 63 names 8190 rows (Bloomberg 1115, template why 6823, team value 0)",
        "org/missions/D5/AMGT/AMGT_CORPUS/prd/AMGT_CORPUS_PRD.md:1107-1116",
        "org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/remediations/REMEDIATION_v9.md rows AMGT_CORPUS-D1-C-S45, AMGT_CORPUS-D1-S5"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "REMEDIATION_v9 C-S45 (CONTROL-form rows) and D1-S5 (raw codes, long floats) close on the served page: EQY_FUND_YEAR and the BEST_FPERIOD_OVERRIDE rows are CONTROL in the served /13 (ADDENDUM E's DEC names '*_OVERRIDE or fund-year key' as CONTROL, PRD:1111) and 0 CONTROL rows render; 0 raw codes are visible as labels and 0 team cells print past their format (DEC :1114-1116). Both entries advance in place to REMEDIATED."
  },
  {
    "id": "AMGT_CORPUS-D1-C-S69",
    "project": "AMGT_CORPUS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T22:55:00Z",
    "one_line": "D1-W1-S16 (two round-47 fixture tests isolated from the shipped FactSet entries by an empty cache) and D1-W1-S17 (the formula grid read once per SHEET, not per workbook) dismissed: each records how the ax-5 worker met an order clause; neither changes a served figure (the served census reads as stated).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_CORPUS-D1-W1-S16",
      "AMGT_CORPUS-D1-W1-S17"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence.",
    "world_is": "D1-W1-S16 (two round-47 fixture tests isolated from the shipped FactSet entries by an empty cache) and D1-W1-S17 (the formula grid read once per SHEET, not per workbook) dismissed: each records how the ax-5 worker met an order clause; neither changes a served figure (the served census reads as stated).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows AMGT_CORPUS-D1-W1-S16, D1-W1-S17",
        "3.0.0_SA_CVO ran node org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round47/aw6_rendered_census.cjs <portal origin/DEV 44ec7e70 extract> <own live capture>: FIGURE 11467 HEADING 359 CONTROL 438 = 12264; bloomberg 1644, team 2999, why 6823, refused 1, unmapped 0; raw codes visible 0; team cells 27666 past 4 decimals 0; percent 7898 of 7898; CONTROL rendered 0; master 63 names 8190 rows (Bloomberg 1115, template why 6823, team value 0)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W1-S16 (two round-47 fixture tests isolated from the shipped FactSet entries by an empty cache) and D1-W1-S17 (the formula grid read once per SHEET, not per workbook) dismissed: each records how the ax-5 worker met an order clause; neither changes a served figure (the served census reads as stated)."
  }
]
```
