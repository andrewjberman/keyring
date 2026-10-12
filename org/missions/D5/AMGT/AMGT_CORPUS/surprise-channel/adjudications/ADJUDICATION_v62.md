# AMGT_CORPUS -- round 47 L9 on FWD-12 and FWD-20 (stage BUILT, not served), the C-S43 correction and the round-47 sweep (dell1)

<sweep_watermark>2026-10-11T21:20Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-11T21:20:00Z. Asked by 2.0.0_SA_COO~C1 msg 4105 (packet `deliverables/2.0.0_SA_COO~C1/ROUND47_GRADED_READS_PACKET.md`
@2afe9f11af, blob 5dc46c4584 verified). The bar is the served page (C-S51). FWD-20 and FWD-12 PARTIAL, stage BUILT (C-S52, C-S53), on this seat's own
stored diff and builder prediction (0 per-name differences). C-S54 withdraws round 46's FWD-20 MET (C-S43). 13 of 207 investigation rows surfaced since
v61's watermark (15:50Z), all INERT: 11 dismissed, D1-S7 and D1-S6 graduated to REMEDIATION_v10. round-close-check --round 47: MAY-CLOSE.

```json
[
  {
    "id": "AMGT_CORPUS-D1-C-S51",
    "project": "AMGT_CORPUS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T21:20:00Z",
    "one_line": "The bar is the SERVED page. FWD-20's DONE WHEN (PRD:596-606) is 'a census of the RENDERED rows' on the Model tab 'a viewer opens' (PRD:593), and ADDENDUM E's DEC (PRD:1107-1116) says how each class RENDERS (a heading renders as a heading; a field-code FIGURE row is labelled by the vendor's description; a team value renders by its cell's format). FWD-12's DONE WHEN (PRD:409-412, ADDENDA B and D) names the rows the Model tab shows. A stored write plus a builder run over the stored field is the stage BUILT, not SERVED; it is graded PARTIAL, never MET on a prediction. The served read is the issuer's after AMGT_RESAPP round 98's redeploy.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): every judgment is graded by a seat that did none of the work, on grounded evidence; a prediction is never graded MET.",
    "world_is": "The bar is the SERVED page. FWD-20's DONE WHEN (PRD:596-606) is 'a census of the RENDERED rows' on the Model tab 'a viewer opens' (PRD:593), and ADDENDUM E's DEC (PRD:1107-1116) says how each class RENDERS (a heading renders as a heading; a field-code FIGURE row is labelled by the vendor's description; a team value renders by its cell's format). FWD-12's DONE WHEN (PRD:409-412, ADDENDA B and D) names the rows the Model tab shows. A stored write plus a builder run over the stored field is the stage BUILT, not SERVED; it is graded PARTIAL, never MET on a prediction. The served read is the issuer's after AMGT_RESAPP round 98's redeploy.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/AMGT/AMGT_CORPUS/prd/AMGT_CORPUS_PRD.md:593-606, :409-456 and :1099-1119 (printed at HEAD v0.10 @9794728d6e)",
        "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/ROUND47_GRADED_READS_PACKET.md @2afe9f11af (blob 5dc46c4584, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The bar is the SERVED page. FWD-20's DONE WHEN (PRD:596-606) is 'a census of the RENDERED rows' on the Model tab 'a viewer opens' (PRD:593), and ADDENDUM E's DEC (PRD:1107-1116) says how each class RENDERS (a heading renders as a heading; a field-code FIGURE row is labelled by the vendor's description; a team value renders by its cell's format). FWD-12's DONE WHEN (PRD:409-412, ADDENDA B and D) names the rows the Model tab shows. A stored write plus a builder run over the stored field is the stage BUILT, not SERVED; it is graded PARTIAL, never MET on a prediction. The served read is the issuer's after AMGT_RESAPP round 98's redeploy."
  },
  {
    "id": "AMGT_CORPUS-D1-C-S52",
    "project": "AMGT_CORPUS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T21:20:00Z",
    "one_line": "FWD-20 PARTIAL -- stage reached: BUILT, not served. This seat's prediction (the real DEV modelSheet.ts over live payloads with each team_sheet replaced by the stored /13 field) reads unmapped 0 of 11,467 FIGURE rows (Bloomberg 1,644, team 2,999, a why 6,823, refused 1), 0 raw field codes visible as a label, 0 of 27,666 team cells past 4 decimals, 7,898 of 7,898 percent cells as percents, 0 CONTROL rows rendered, 0 why-rows with a barred word. The served page (live opal-amgt-scoped-api TmeKvn83XnePF4RrJUQKIpbzYdH4VnCmvyXePbs3KB8= (LastModified 2026-10-11T18:03:44Z), serving the /12 objects) carries none of it. The own-workbook FIGURE denominator moved 3,381 -> 3,529 for a stated reason: the stored diff reads 177 rows HEADING->FIGURE (the D1-S7 header correction on CLX, ML FP, BABA) and 29 FIGURE->CONTROL (BEST_FPERIOD_OVERRIDE): 3,381 + 177 - 29 = 3,529; HEADING 316 - 177 - 32 = 107; CONTROL 62 + 32 + 29 = 123. 1,343 rendered rows read 'FactSet line' with the code in the title (row D1-S6).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): every judgment is graded by a seat that did none of the work, on grounded evidence; a prediction is never graded MET.",
    "world_is": "FWD-20 PARTIAL -- stage reached: BUILT, not served. This seat's prediction (the real DEV modelSheet.ts over live payloads with each team_sheet replaced by the stored /13 field) reads unmapped 0 of 11,467 FIGURE rows (Bloomberg 1,644, team 2,999, a why 6,823, refused 1), 0 raw field codes visible as a label, 0 of 27,666 team cells past 4 decimals, 7,898 of 7,898 percent cells as percents, 0 CONTROL rows rendered, 0 why-rows with a barred word. The served page (live opal-amgt-scoped-api TmeKvn83XnePF4RrJUQKIpbzYdH4VnCmvyXePbs3KB8= (LastModified 2026-10-11T18:03:44Z), serving the /12 objects) carries none of it. The own-workbook FIGURE denominator moved 3,381 -> 3,529 for a stated reason: the stored diff reads 177 rows HEADING->FIGURE (the D1-S7 header correction on CLX, ML FP, BABA) and 29 FIGURE->CONTROL (BEST_FPERIOD_OVERRIDE): 3,381 + 177 - 29 = 3,529; HEADING 316 - 177 - 32 = 107; CONTROL 62 + 32 + 29 = 123. 1,343 rendered rows read 'FactSet line' with the code in the title (row D1-S6).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO ran org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round47/aw3_diff.py --post 2026-10-11T21:0xZ: own 32 names FIGURE 3529 HEADING 107 CONTROL 123; master 63 names FIGURE 7938 HEADING 252 CONTROL 315; own transitions /12->/13 HEADING>FIGURE 177, HEADING>CONTROL 32, FIGURE>CONTROL 29; master team values 0; own_old_keys_equal 32/32, master_as_predicted 63/63, reader_equal 95/95, build 1/1",
        "3.0.0_SA_CVO ran org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round47/aw4_capture.py over live opal-amgt-scoped-api TmeKvn83XnePF4RrJUQKIpbzYdH4VnCmvyXePbs3KB8= (LastModified 2026-10-11T18:03:44Z), serving the /12 objects (95 of 95), org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round47/aw6_preread_inject.py (95 injected with the stored /13 team_sheet) and node org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round47/aw6_rendered_census.cjs with portal origin/DEV 44ec7e70: FIGURE 11467 HEADING 359 CONTROL 438 = 12264; bloomberg 1644, team 2999, why 6823, refused 1, unmapped 0; raw field codes visible 0; team cells 27666 past 4 decimals 0; percent cells 7898 of 7898; master 63 names 8190 rendered rows (Bloomberg 1115, template why 6823, team value 0); 0 per-name lines differing from the issuer's evidence/r47_aw6_rendered_census_PREREAD_20261011.txt",
        "org/missions/D5/AMGT/AMGT_CORPUS/prd/AMGT_CORPUS_PRD.md:593-606, :1107-1116"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "FWD-20 PARTIAL -- stage reached: BUILT, not served. This seat's prediction (the real DEV modelSheet.ts over live payloads with each team_sheet replaced by the stored /13 field) reads unmapped 0 of 11,467 FIGURE rows (Bloomberg 1,644, team 2,999, a why 6,823, refused 1), 0 raw field codes visible as a label, 0 of 27,666 team cells past 4 decimals, 7,898 of 7,898 percent cells as percents, 0 CONTROL rows rendered, 0 why-rows with a barred word. The served page (live opal-amgt-scoped-api TmeKvn83XnePF4RrJUQKIpbzYdH4VnCmvyXePbs3KB8= (LastModified 2026-10-11T18:03:44Z), serving the /12 objects) carries none of it. The own-workbook FIGURE denominator moved 3,381 -> 3,529 for a stated reason: the stored diff reads 177 rows HEADING->FIGURE (the D1-S7 header correction on CLX, ML FP, BABA) and 29 FIGURE->CONTROL (BEST_FPERIOD_OVERRIDE): 3,381 + 177 - 29 = 3,529; HEADING 316 - 177 - 32 = 107; CONTROL 62 + 32 + 29 = 123. 1,343 rendered rows read 'FactSet line' with the code in the title (row D1-S6)."
  },
  {
    "id": "AMGT_CORPUS-D1-C-S53",
    "project": "AMGT_CORPUS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T21:20:00Z",
    "one_line": "FWD-12 PARTIAL -- stage reached: BUILT, not served. The master arm is now stored: 63 names in class master (master_absent 0), each citing FactSet Based ONE PAGER TEMPLATE 2026 03 09_v2.xlsx, sheet Model NEW VERSION, 135 rows (FIGURE 126, HEADING 4, CONTROL 5), with no value, format or period (the template's sample company, CTO msg 4086); the template stored write-once (ledger amgt-corpus-r47-aw10 CLOSED). Prediction: each master name renders 130 rows, Bloomberg where its own block carries the field (1,115 over the 63), else the template why (6,823), team value 0. The own-workbook arm stays 32 of 32. Not served: the live function still serves /12.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): every judgment is graded by a seat that did none of the work, on grounded evidence; a prediction is never graded MET.",
    "world_is": "FWD-12 PARTIAL -- stage reached: BUILT, not served. The master arm is now stored: 63 names in class master (master_absent 0), each citing FactSet Based ONE PAGER TEMPLATE 2026 03 09_v2.xlsx, sheet Model NEW VERSION, 135 rows (FIGURE 126, HEADING 4, CONTROL 5), with no value, format or period (the template's sample company, CTO msg 4086); the template stored write-once (ledger amgt-corpus-r47-aw10 CLOSED). Prediction: each master name renders 130 rows, Bloomberg where its own block carries the field (1,115 over the 63), else the template why (6,823), team value 0. The own-workbook arm stays 32 of 32. Not served: the live function still serves /12.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO ran org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round47/aw3_diff.py --post 2026-10-11T21:0xZ: own 32 names FIGURE 3529 HEADING 107 CONTROL 123; master 63 names FIGURE 7938 HEADING 252 CONTROL 315; own transitions /12->/13 HEADING>FIGURE 177, HEADING>CONTROL 32, FIGURE>CONTROL 29; master team values 0; own_old_keys_equal 32/32, master_as_predicted 63/63, reader_equal 95/95, build 1/1",
        "3.0.0_SA_CVO ran org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round47/aw4_capture.py over live opal-amgt-scoped-api TmeKvn83XnePF4RrJUQKIpbzYdH4VnCmvyXePbs3KB8= (LastModified 2026-10-11T18:03:44Z), serving the /12 objects (95 of 95), org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round47/aw6_preread_inject.py (95 injected with the stored /13 team_sheet) and node org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round47/aw6_rendered_census.cjs with portal origin/DEV 44ec7e70: FIGURE 11467 HEADING 359 CONTROL 438 = 12264; bloomberg 1644, team 2999, why 6823, refused 1, unmapped 0; raw field codes visible 0; team cells 27666 past 4 decimals 0; percent cells 7898 of 7898; master 63 names 8190 rendered rows (Bloomberg 1115, template why 6823, team value 0); 0 per-name lines differing from the issuer's evidence/r47_aw6_rendered_census_PREREAD_20261011.txt",
        "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/ROUND47_GRADED_READS_PACKET.md FWD-12 table",
        "org/missions/D5/AMGT/AMGT_CORPUS/prd/AMGT_CORPUS_PRD.md:409-456"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "FWD-12 PARTIAL -- stage reached: BUILT, not served. The master arm is now stored: 63 names in class master (master_absent 0), each citing FactSet Based ONE PAGER TEMPLATE 2026 03 09_v2.xlsx, sheet Model NEW VERSION, 135 rows (FIGURE 126, HEADING 4, CONTROL 5), with no value, format or period (the template's sample company, CTO msg 4086); the template stored write-once (ledger amgt-corpus-r47-aw10 CLOSED). Prediction: each master name renders 130 rows, Bloomberg where its own block carries the field (1,115 over the 63), else the template why (6,823), team value 0. The own-workbook arm stays 32 of 32. Not served: the live function still serves /12."
  },
  {
    "id": "AMGT_CORPUS-D1-C-S54",
    "project": "AMGT_CORPUS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T21:20:00Z",
    "one_line": "Correction of ADJUDICATION_v61 C-S43 (FWD-20 MET on DEV at round 46): that MET is WITHDRAWN. It rested on the round-46 classes (FIGURE 3,381 / HEADING 316), which the issuer's own correction (row D1-S7) shows were wrong on three names: the all-numeric header test took the EQY_FUND_YEAR row as the period header on CLX, ML FP and BABA, so 177 rows that carry figures rendered on DEV as headings with no value. 'Every row the team's sheet carries shows a figure' was therefore not met at round 46, although 'unmapped 0 of 3,381' was true of the wrong classification. This seat's round-46 re-run reproduced the same wrong classes and its C-S45 found the EQY_FUND_YEAR heading but not the header misread. C-S40's '316 headings rendered' rests on the same reading.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_CORPUS-D1-C-S43",
      "AMGT_CORPUS-D1-C-S40"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): a grade is corrected by a NEW row citing the old one, never by an edit in place.",
    "world_is": "Correction of ADJUDICATION_v61 C-S43 (FWD-20 MET on DEV at round 46): that MET is WITHDRAWN. It rested on the round-46 classes (FIGURE 3,381 / HEADING 316), which the issuer's own correction (row D1-S7) shows were wrong on three names: the all-numeric header test took the EQY_FUND_YEAR row as the period header on CLX, ML FP and BABA, so 177 rows that carry figures rendered on DEV as headings with no value. 'Every row the team's sheet carries shows a figure' was therefore not met at round 46, although 'unmapped 0 of 3,381' was true of the wrong classification. This seat's round-46 re-run reproduced the same wrong classes and its C-S45 found the EQY_FUND_YEAR heading but not the header misread. C-S40's '316 headings rendered' rests on the same reading.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "adjudication rows AMGT_CORPUS-D1-C-S43, D1-C-S40, D1-C-S45 (ADJUDICATION_v61)",
        "investigation row AMGT_CORPUS-D1-S7",
        "3.0.0_SA_CVO ran org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round47/aw3_diff.py --post 2026-10-11T21:0xZ: own 32 names FIGURE 3529 HEADING 107 CONTROL 123; master 63 names FIGURE 7938 HEADING 252 CONTROL 315; own transitions /12->/13 HEADING>FIGURE 177, HEADING>CONTROL 32, FIGURE>CONTROL 29; master team values 0; own_old_keys_equal 32/32, master_as_predicted 63/63, reader_equal 95/95, build 1/1 (HEADING>FIGURE 177)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Correction of ADJUDICATION_v61 C-S43 (FWD-20 MET on DEV at round 46): that MET is WITHDRAWN. It rested on the round-46 classes (FIGURE 3,381 / HEADING 316), which the issuer's own correction (row D1-S7) shows were wrong on three names: the all-numeric header test took the EQY_FUND_YEAR row as the period header on CLX, ML FP and BABA, so 177 rows that carry figures rendered on DEV as headings with no value. 'Every row the team's sheet carries shows a figure' was therefore not met at round 46, although 'unmapped 0 of 3,381' was true of the wrong classification. This seat's round-46 re-run reproduced the same wrong classes and its C-S45 found the EQY_FUND_YEAR heading but not the header misread. C-S40's '316 headings rendered' rests on the same reading."
  },
  {
    "id": "AMGT_CORPUS-D1-C-S55",
    "project": "AMGT_CORPUS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T21:20:00Z",
    "one_line": "D1-S7 (the round-46 header test served ~190 model rows of CLX, ML FP and BABA as value-less headings on DEV) graduated INERT to REMEDIATION_v10, owner 2.0.0_SA_COO~C1: the correction is STORED (/13: 177 HEADING->FIGURE, 32 EQY_FUND_YEAR HEADING->CONTROL on this seat's diff) but not SERVED; the close is the live census after the redeploy.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_CORPUS-D1-S7"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence.",
    "world_is": "D1-S7 (the round-46 header test served ~190 model rows of CLX, ML FP and BABA as value-less headings on DEV) graduated INERT to REMEDIATION_v10, owner 2.0.0_SA_COO~C1: the correction is STORED (/13: 177 HEADING->FIGURE, 32 EQY_FUND_YEAR HEADING->CONTROL on this seat's diff) but not SERVED; the close is the live census after the redeploy.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row AMGT_CORPUS-D1-S7",
        "3.0.0_SA_CVO ran org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round47/aw3_diff.py --post 2026-10-11T21:0xZ: own 32 names FIGURE 3529 HEADING 107 CONTROL 123; master 63 names FIGURE 7938 HEADING 252 CONTROL 315; own transitions /12->/13 HEADING>FIGURE 177, HEADING>CONTROL 32, FIGURE>CONTROL 29; master team values 0; own_old_keys_equal 32/32, master_as_predicted 63/63, reader_equal 95/95, build 1/1"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Graduated to remediations/REMEDIATION_v10.md."
  },
  {
    "id": "AMGT_CORPUS-D1-C-S56",
    "project": "AMGT_CORPUS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T21:20:00Z",
    "one_line": "D1-S6 (50 of 106 field-code labels are FactSet data-item codes no estate source describes; 702 of 1,348 code-labelled FIGURE rows) graduated INERT to REMEDIATION_v10, owner 1.0.0_SA_CTO~DELL1: ADDENDUM E's DEC names a Bloomberg field code's label; it is silent on a FactSet code, which renders 'FactSet line' with the code and why in the title (1,343 rendered rows on this seat's prediction). The mechanism takes a cited entry (factset_descriptions.json, empty).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_CORPUS-D1-S6"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence.",
    "world_is": "D1-S6 (50 of 106 field-code labels are FactSet data-item codes no estate source describes; 702 of 1,348 code-labelled FIGURE rows) graduated INERT to REMEDIATION_v10, owner 1.0.0_SA_CTO~DELL1: ADDENDUM E's DEC names a Bloomberg field code's label; it is silent on a FactSet code, which renders 'FactSet line' with the code and why in the title (1,343 rendered rows on this seat's prediction). The mechanism takes a cited entry (factset_descriptions.json, empty).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row AMGT_CORPUS-D1-S6",
        "3.0.0_SA_CVO ran org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round47/aw4_capture.py over live opal-amgt-scoped-api TmeKvn83XnePF4RrJUQKIpbzYdH4VnCmvyXePbs3KB8= (LastModified 2026-10-11T18:03:44Z), serving the /12 objects (95 of 95), org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round47/aw6_preread_inject.py (95 injected with the stored /13 team_sheet) and node org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round47/aw6_rendered_census.cjs with portal origin/DEV 44ec7e70: FIGURE 11467 HEADING 359 CONTROL 438 = 12264; bloomberg 1644, team 2999, why 6823, refused 1, unmapped 0; raw field codes visible 0; team cells 27666 past 4 decimals 0; percent cells 7898 of 7898; master 63 names 8190 rendered rows (Bloomberg 1115, template why 6823, team value 0); 0 per-name lines differing from the issuer's evidence/r47_aw6_rendered_census_PREREAD_20261011.txt (labels by claim: factset_line 1343)",
        "org/missions/D5/AMGT/AMGT_CORPUS/prd/AMGT_CORPUS_PRD.md:1114-1115"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Graduated to remediations/REMEDIATION_v10.md."
  },
  {
    "id": "AMGT_CORPUS-D1-C-S57",
    "project": "AMGT_CORPUS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T21:20:00Z",
    "one_line": "Progress, not closure, on REMEDIATION_v9 C-S45 (CONTROL-form rows): the stored /13 classes EQY_FUND_YEAR CONTROL on 32 of 32 and moves 29 BEST_FPERIOD_OVERRIDE rows FIGURE->CONTROL (by-name CONTROL in aw-1 @7a58fb83fc), and the prediction renders 0 CONTROL rows. Its close condition names the rendered page, which still serves /12, so the remediation stays OPEN. REMEDIATION_v9 D1-S5 (raw codes): the prediction reads 0 raw codes visible; also OPEN until served.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_CORPUS-D1-C-S45",
      "AMGT_CORPUS-D1-S5"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence.",
    "world_is": "Progress, not closure, on REMEDIATION_v9 C-S45 (CONTROL-form rows): the stored /13 classes EQY_FUND_YEAR CONTROL on 32 of 32 and moves 29 BEST_FPERIOD_OVERRIDE rows FIGURE->CONTROL (by-name CONTROL in aw-1 @7a58fb83fc), and the prediction renders 0 CONTROL rows. Its close condition names the rendered page, which still serves /12, so the remediation stays OPEN. REMEDIATION_v9 D1-S5 (raw codes): the prediction reads 0 raw codes visible; also OPEN until served.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO ran org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round47/aw3_diff.py --post 2026-10-11T21:0xZ: own 32 names FIGURE 3529 HEADING 107 CONTROL 123; master 63 names FIGURE 7938 HEADING 252 CONTROL 315; own transitions /12->/13 HEADING>FIGURE 177, HEADING>CONTROL 32, FIGURE>CONTROL 29; master team values 0; own_old_keys_equal 32/32, master_as_predicted 63/63, reader_equal 95/95, build 1/1",
        "3.0.0_SA_CVO ran org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round47/aw4_capture.py over live opal-amgt-scoped-api TmeKvn83XnePF4RrJUQKIpbzYdH4VnCmvyXePbs3KB8= (LastModified 2026-10-11T18:03:44Z), serving the /12 objects (95 of 95), org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round47/aw6_preread_inject.py (95 injected with the stored /13 team_sheet) and node org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round47/aw6_rendered_census.cjs with portal origin/DEV 44ec7e70: FIGURE 11467 HEADING 359 CONTROL 438 = 12264; bloomberg 1644, team 2999, why 6823, refused 1, unmapped 0; raw field codes visible 0; team cells 27666 past 4 decimals 0; percent cells 7898 of 7898; master 63 names 8190 rendered rows (Bloomberg 1115, template why 6823, team value 0); 0 per-name lines differing from the issuer's evidence/r47_aw6_rendered_census_PREREAD_20261011.txt",
        "org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/remediations/REMEDIATION_v9.md rows AMGT_CORPUS-D1-C-S45, AMGT_CORPUS-D1-S5"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Progress, not closure, on REMEDIATION_v9 C-S45 (CONTROL-form rows): the stored /13 classes EQY_FUND_YEAR CONTROL on 32 of 32 and moves 29 BEST_FPERIOD_OVERRIDE rows FIGURE->CONTROL (by-name CONTROL in aw-1 @7a58fb83fc), and the prediction renders 0 CONTROL rows. Its close condition names the rendered page, which still serves /12, so the remediation stays OPEN. REMEDIATION_v9 D1-S5 (raw codes): the prediction reads 0 raw codes visible; also OPEN until served."
  },
  {
    "id": "AMGT_CORPUS-D1-C-S58",
    "project": "AMGT_CORPUS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T21:20:00Z",
    "one_line": "D1-W1-S10 and D1-W1-S12 dismissed: the 3,549 vs 3,381 drift was the first build's no-header state on three names (S12's own measurement: the round-46 base module on the same store reads 3,381 / 316 / 62), not store drift; the final /13 classes reconcile exactly to round 46 on this seat's diff (C-S52).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_CORPUS-D1-W1-S10",
      "AMGT_CORPUS-D1-W1-S12"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence.",
    "world_is": "D1-W1-S10 and D1-W1-S12 dismissed: the 3,549 vs 3,381 drift was the first build's no-header state on three names (S12's own measurement: the round-46 base module on the same store reads 3,381 / 316 / 62), not store drift; the final /13 classes reconcile exactly to round 46 on this seat's diff (C-S52).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows AMGT_CORPUS-D1-W1-S10, D1-W1-S12",
        "3.0.0_SA_CVO ran org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round47/aw3_diff.py --post 2026-10-11T21:0xZ: own 32 names FIGURE 3529 HEADING 107 CONTROL 123; master 63 names FIGURE 7938 HEADING 252 CONTROL 315; own transitions /12->/13 HEADING>FIGURE 177, HEADING>CONTROL 32, FIGURE>CONTROL 29; master team values 0; own_old_keys_equal 32/32, master_as_predicted 63/63, reader_equal 95/95, build 1/1"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W1-S10 and D1-W1-S12 dismissed: the 3,549 vs 3,381 drift was the first build's no-header state on three names (S12's own measurement: the round-46 base module on the same store reads 3,381 / 316 / 62), not store drift; the final /13 classes reconcile exactly to round 46 on this seat's diff (C-S52)."
  },
  {
    "id": "AMGT_CORPUS-D1-C-S59",
    "project": "AMGT_CORPUS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T21:20:00Z",
    "one_line": "D1-W1-S15 dismissed: a master answer keeps the template's FIGURE classes with row_values None, and the reader the page calls does not show those rows as figures with no numbers: this seat's prediction renders the 63 master names' FIGURE rows as Bloomberg (1,115) or the template why (6,823), team value 0.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_CORPUS-D1-W1-S15"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence.",
    "world_is": "D1-W1-S15 dismissed: a master answer keeps the template's FIGURE classes with row_values None, and the reader the page calls does not show those rows as figures with no numbers: this seat's prediction renders the 63 master names' FIGURE rows as Bloomberg (1,115) or the template why (6,823), team value 0.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row AMGT_CORPUS-D1-W1-S15",
        "3.0.0_SA_CVO ran org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round47/aw4_capture.py over live opal-amgt-scoped-api TmeKvn83XnePF4RrJUQKIpbzYdH4VnCmvyXePbs3KB8= (LastModified 2026-10-11T18:03:44Z), serving the /12 objects (95 of 95), org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round47/aw6_preread_inject.py (95 injected with the stored /13 team_sheet) and node org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round47/aw6_rendered_census.cjs with portal origin/DEV 44ec7e70: FIGURE 11467 HEADING 359 CONTROL 438 = 12264; bloomberg 1644, team 2999, why 6823, refused 1, unmapped 0; raw field codes visible 0; team cells 27666 past 4 decimals 0; percent cells 7898 of 7898; master 63 names 8190 rendered rows (Bloomberg 1115, template why 6823, team value 0); 0 per-name lines differing from the issuer's evidence/r47_aw6_rendered_census_PREREAD_20261011.txt"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W1-S15 dismissed: a master answer keeps the template's FIGURE classes with row_values None, and the reader the page calls does not show those rows as figures with no numbers: this seat's prediction renders the 63 master names' FIGURE rows as Bloomberg (1,115) or the template why (6,823), team value 0."
  },
  {
    "id": "AMGT_CORPUS-D1-C-S60",
    "project": "AMGT_CORPUS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T21:20:00Z",
    "one_line": "D1-W2-S3, D1-W2-S4, D1-W1-S9, D1-W1-S11, D1-W1-S13 and D1-W1-S14 dismissed: each records how the worker met an order clause the order left open (a null why titled by its code alone; sourceLabel only on team-valued rows; the labels line placed after the row-classes line a round-46 test pins; the reader raising on a missing FactSet descriptions file and leaving row_formats None without a header; the template-line identity's t and f; distinct codes vs rows). None changes a served or stored figure; the stored diff and the prediction read as expected.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_CORPUS-D1-W2-S3",
      "AMGT_CORPUS-D1-W2-S4",
      "AMGT_CORPUS-D1-W1-S9",
      "AMGT_CORPUS-D1-W1-S11",
      "AMGT_CORPUS-D1-W1-S13",
      "AMGT_CORPUS-D1-W1-S14"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence.",
    "world_is": "D1-W2-S3, D1-W2-S4, D1-W1-S9, D1-W1-S11, D1-W1-S13 and D1-W1-S14 dismissed: each records how the worker met an order clause the order left open (a null why titled by its code alone; sourceLabel only on team-valued rows; the labels line placed after the row-classes line a round-46 test pins; the reader raising on a missing FactSet descriptions file and leaving row_formats None without a header; the template-line identity's t and f; distinct codes vs rows). None changes a served or stored figure; the stored diff and the prediction read as expected.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows AMGT_CORPUS-D1-W2-S3, D1-W2-S4, D1-W1-S9, D1-W1-S11, D1-W1-S13, D1-W1-S14",
        "3.0.0_SA_CVO ran org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round47/aw3_diff.py --post 2026-10-11T21:0xZ: own 32 names FIGURE 3529 HEADING 107 CONTROL 123; master 63 names FIGURE 7938 HEADING 252 CONTROL 315; own transitions /12->/13 HEADING>FIGURE 177, HEADING>CONTROL 32, FIGURE>CONTROL 29; master team values 0; own_old_keys_equal 32/32, master_as_predicted 63/63, reader_equal 95/95, build 1/1",
        "3.0.0_SA_CVO ran org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round47/aw4_capture.py over live opal-amgt-scoped-api TmeKvn83XnePF4RrJUQKIpbzYdH4VnCmvyXePbs3KB8= (LastModified 2026-10-11T18:03:44Z), serving the /12 objects (95 of 95), org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round47/aw6_preread_inject.py (95 injected with the stored /13 team_sheet) and node org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round47/aw6_rendered_census.cjs with portal origin/DEV 44ec7e70: FIGURE 11467 HEADING 359 CONTROL 438 = 12264; bloomberg 1644, team 2999, why 6823, refused 1, unmapped 0; raw field codes visible 0; team cells 27666 past 4 decimals 0; percent cells 7898 of 7898; master 63 names 8190 rendered rows (Bloomberg 1115, template why 6823, team value 0); 0 per-name lines differing from the issuer's evidence/r47_aw6_rendered_census_PREREAD_20261011.txt"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W2-S3, D1-W2-S4, D1-W1-S9, D1-W1-S11, D1-W1-S13 and D1-W1-S14 dismissed: each records how the worker met an order clause the order left open (a null why titled by its code alone; sourceLabel only on team-valued rows; the labels line placed after the row-classes line a round-46 test pins; the reader raising on a missing FactSet descriptions file and leaving row_formats None without a header; the template-line identity's t and f; distinct codes vs rows). None changes a served or stored figure; the stored diff and the prediction read as expected."
  },
  {
    "id": "AMGT_CORPUS-D1-C-S61",
    "project": "AMGT_CORPUS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T21:20:00Z",
    "one_line": "D1-W2-S5 (the amendment's AC4 cites a decomposition cell not in the worker's branch, so its proof first refused) and Z-S92 (the aw10 step's bare 'python <path>' cannot import lib) dismissed: both orders are terminal with VALID proofs (round-close-check --round 47: 3 of 3 complete, proof_ok 3), and the aw10 ledger is CLOSED; aw10_locate.py's own usage line carries the PYTHONPATH=. form. The order-text defects are the cut's to carry.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_CORPUS-D1-W2-S5",
      "AMGT_CORPUS-Z-S92"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence.",
    "world_is": "D1-W2-S5 (the amendment's AC4 cites a decomposition cell not in the worker's branch, so its proof first refused) and Z-S92 (the aw10 step's bare 'python <path>' cannot import lib) dismissed: both orders are terminal with VALID proofs (round-close-check --round 47: 3 of 3 complete, proof_ok 3), and the aw10 ledger is CLOSED; aw10_locate.py's own usage line carries the PYTHONPATH=. form. The order-text defects are the cut's to carry.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows AMGT_CORPUS-D1-W2-S5, AMGT_CORPUS-Z-S92",
        "3.0.0_SA_CVO python .tools/round-close-check.py --project AMGT_CORPUS --round 47: orders 3 complete 3 proof_ok 3 MAY-CLOSE"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W2-S5 (the amendment's AC4 cites a decomposition cell not in the worker's branch, so its proof first refused) and Z-S92 (the aw10 step's bare 'python <path>' cannot import lib) dismissed: both orders are terminal with VALID proofs (round-close-check --round 47: 3 of 3 complete, proof_ok 3), and the aw10 ledger is CLOSED; aw10_locate.py's own usage line carries the PYTHONPATH=. form. The order-text defects are the cut's to carry."
  }
]
```
