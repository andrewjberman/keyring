# AMGT_RESAPP -- round 115 L8/L9 (dell1)

<sweep_watermark>2026-10-18T03:57:08Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-18T03:57:08Z, on 2.0.0_SA_COO~R1 msg 7884 (org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round115/DRAIN_END_PACKET.md @fe9455f675). Swept: 11 dell1 rows never named, all dismissed. FWD-5's printed-pack grade (the CTO's item 4(b)) is NOT MET. Clocks advanced in place: REMEDIATION_v54 W505-S1, W505-S2, W506-S4, W506-S5. The watermark moves to now.

```json
[
  {
    "id": "AMGT_RESAPP-D1-C-S184",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-18T03:57:08Z",
    "one_line": "ROUND 115 L9 (the CTO's item 4(b)): FWD-5 printed pack NOT MET. No raw code and no dashboard chrome, but not every figure is right to its source. ICT PM prints 'Market value, currency-adjusted: USD 1,735,465.1 million' (a PHP figure labelled USD, read as USD 1.7 trillion), and RIO LN prints 'Market cap: GBp 115,578.9 million' (a USD figure labelled GBp). As a document, each pack is about 830 lines of 'label: value - Bloomberg' with an empty Management section on RIO LN. Round 115 itself is MAY-CLOSE.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-W509-S1",
      "AMGT_RESAPP-D1-W509-S2",
      "AMGT_RESAPP-D1-W509-S3",
      "AMGT_RESAPP-D1-W508-S1",
      "AMGT_RESAPP-D1-W508-S2",
      "AMGT_RESAPP-D1-W508-S3",
      "AMGT_RESAPP-D1-W508-S4",
      "AMGT_RESAPP-D1-W508-S5",
      "AMGT_RESAPP-D1-W508-S6",
      "AMGT_RESAPP-D1-W508-S7",
      "AMGT_RESAPP-D1-W508-S8"
    ],
    "spec_asserts": "The CTO's round-114 analysis item 4(b), FWD-5: each live printed pack reads as a DOCUMENT: Opal form, every figure traceable, no raw code and no dashboard chrome.",
    "world_is": "READ BY THIS SEAT 2026-10-18 ~04:0xZ. The three live packs in org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round115/packs/ (RIO LN 24 pages, ICT PM 24, GOOGL US 25; renderer at CodeSha256 lp+7X1V...) were rendered to images with PyMuPDF (RIO LN pages 1, 2, 16 and 24; ICT PM 1 and 5; GOOGL US 1 and 7) and their text extracted. MET: no raw field code and no dashboard chrome (no tiles, buttons or navigation; a title, a 'Printed October 18th, 2026' line and section rules). The issuer's 0 ISO days and 0 UPPER_SNAKE tokens agree with this read. NOT MET, traceability. ICT PM page 1: 'Market cap: PHP 1,735,465.1 million' and 'Market value, currency-adjusted: USD 1,735,465.1 million'. The same number carries two currencies, and the page's own What Changed row for this field reads 'PHP 1.74T' (the field is in the requested currency, PHP), so the pack states a USD 1.7 trillion value that no source holds. RIO LN page 1: 'Market cap: GBp 115,578.9 million' and 'Market value, currency-adjusted: USD 115,578.9 million'. 1,255,183,664 shares at GBp 6,816 is about GBp 8.55 trillion, about USD 115.6 billion, so the GBp label is wrong on the market cap line. GOOGL US (all USD) does not show the defect. Every figure line ends '- Bloomberg', with 'Figures marked without a date: date not stored with this figure', so a figure is traceable to a source but not to a pull date. AS A DOCUMENT: 831, 811 and 854 lines of the 910, 891 and 931 extracted lines are 'label: value - Bloomberg', repeated per fiscal year from 2016, with one heading style. It reads as a figure listing, not a research note. RIO LN page 24, 'Management/Board', reads 'No chief executive or board biography has been written for this company yet', though the live page's Exec tab carries an AI-filled CEO passage for RIO LN (round 108 walk). The document-form judgment is this seat's reading for the CTO; the currency defect is a measured fact. DISMISSED (round-115 worker rows, all INERT): W509-S1 to S3 (bv-2's premise and control facts: the pack prints no evidence passage, the Q3 control, the accession-number day run held by the bounded pattern). W508-S1 to S8 (bv-1's census and order facts, routed by AMENDMENT 1 inside the cell; W508-S8 an unreachable branch, routed).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round115/packs/RIO_LN_Equity_pack.pdf, ICT_PM_Equity_pack.pdf, GOOGL_US_Equity_pack.pdf (rendered and text-extracted by this seat)",
        "C:/dev/ui-walk-evidence/bo-3/A/20261017T103803Z/shots/067-ICT-PM-Model.png (the page's What Changed row: PHP 1.74T)",
        "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round115/DRAIN_END_PACKET.md @fe9455f675"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record (FWD-5 printed pack NOT MET) and round-115 worker rows routed inside their cells."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S185",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-18T03:57:08Z",
    "one_line": "Graduated to REMEDIATION_v55 (1): this seat's finding, filed as row C-S186. The printed pack labels a market-value figure with the wrong currency (ICT PM 'USD 1,735,465.1 million' for a PHP value; RIO LN 'Market cap: GBp' for a USD value).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L10: an item that still bears on a later act graduates with an owner and a close condition.",
    "world_is": "See C-S184. The defect is in the pack renderer's unit for two header fields; whether other foreign-listed names carry it is not counted.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "adjudication row AMGT_RESAPP-D1-C-S184 (this file)"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Remediation row C-S186 in REMEDIATION_v55."
  }
]
```

-- 3.0.0_SA_CVO
