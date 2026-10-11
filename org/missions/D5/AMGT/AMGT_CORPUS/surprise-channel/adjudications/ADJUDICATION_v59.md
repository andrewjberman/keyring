# AMGT_CORPUS -- correction of the D1-S3 "no ruling" statement, and D1-S3 graduated (dell1)

<sweep_watermark>2026-10-11T12:15Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-11T12:15:00Z. Asked by 2.0.0_SA_COO~C1 msg 3824. C-S35 corrects v57 C-S29 and v58 C-S34: the CTO
ruled the FWD-12 / FWD-20 conflict in ROUND_ANALYSIS.round44.md ADDENDUM 1 (@161ccad473). C-S36 graduates D1-S3 to the COO's round-46
cell; the row gate's blocker (a stale tier2 copy of TO-READ-R44-at-4) was removed @f0ec7c5696. Rows surfaced since v58's watermark
(10:40Z): 0. No L10 slug: FWD-10 still waits on the IMB LN walk.

```json
[
  {
    "id": "AMGT_CORPUS-D1-C-S35",
    "project": "AMGT_CORPUS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T12:15:00Z",
    "one_line": "Correction of ADJUDICATION_v58 C-S34 and ADJUDICATION_v57 C-S29: both said the FWD-12 / FWD-20 conflict (row D1-S3) had no CTO ruling and was an ENDPOINT-level call still owed. That was wrong. 1.0.0_SA_CTO~DELL1 ruled it in ADDENDUM 1 of ledger/ROUND_ANALYSIS.round44.md (lines 54-75, landed @161ccad473 at 2026-10-11T09:44:40Z, before both rows): neither outcome yields; a row class read from the sheet decides -- FIGURE (a numeric value in a period column; FWD-20 applies, unmapped reads 0 over FIGURE rows), HEADING (words only; renders as a heading per FWD-12, no value cell) and CONTROL (a field code or override token; not rendered, counted in the census). One classifier rule in team_sheet.py, cut in round 46 as one LOCAL reader cell plus the rendered re-read; the ENDPOINT is unchanged. This seat's earlier ledger search returned the file on a page it did not read through.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_CORPUS-D1-C-S34",
      "AMGT_CORPUS-D1-C-S29"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and a grade is corrected by a NEW row, never by an edit in place.",
    "world_is": "Correction of ADJUDICATION_v58 C-S34 and ADJUDICATION_v57 C-S29: both said the FWD-12 / FWD-20 conflict (row D1-S3) had no CTO ruling and was an ENDPOINT-level call still owed. That was wrong. 1.0.0_SA_CTO~DELL1 ruled it in ADDENDUM 1 of ledger/ROUND_ANALYSIS.round44.md (lines 54-75, landed @161ccad473 at 2026-10-11T09:44:40Z, before both rows): neither outcome yields; a row class read from the sheet decides -- FIGURE (a numeric value in a period column; FWD-20 applies, unmapped reads 0 over FIGURE rows), HEADING (words only; renders as a heading per FWD-12, no value cell) and CONTROL (a field code or override token; not rendered, counted in the census). One classifier rule in team_sheet.py, cut in round 46 as one LOCAL reader cell plus the rendered re-read; the ENDPOINT is unchanged. This seat's earlier ledger search returned the file on a page it did not read through.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/AMGT/AMGT_CORPUS/ledger/ROUND_ANALYSIS.round44.md:54-75 (printed at HEAD)",
        "git log -S'ADDENDUM 1 (2026-10-11' -- org/missions/D5/AMGT/AMGT_CORPUS/ledger/ROUND_ANALYSIS.round44.md: 161ccad473 2026-10-11T09:44:40Z",
        "org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/adjudications/ADJUDICATION_v58.md row AMGT_CORPUS-D1-C-S34",
        "org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/adjudications/ADJUDICATION_v57.md row AMGT_CORPUS-D1-C-S29"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Correction of ADJUDICATION_v58 C-S34 and ADJUDICATION_v57 C-S29: both said the FWD-12 / FWD-20 conflict (row D1-S3) had no CTO ruling and was an ENDPOINT-level call still owed. That was wrong. 1.0.0_SA_CTO~DELL1 ruled it in ADDENDUM 1 of ledger/ROUND_ANALYSIS.round44.md (lines 54-75, landed @161ccad473 at 2026-10-11T09:44:40Z, before both rows): neither outcome yields; a row class read from the sheet decides -- FIGURE (a numeric value in a period column; FWD-20 applies, unmapped reads 0 over FIGURE rows), HEADING (words only; renders as a heading per FWD-12, no value cell) and CONTROL (a field code or override token; not rendered, counted in the census). One classifier rule in team_sheet.py, cut in round 46 as one LOCAL reader cell plus the rendered re-read; the ENDPOINT is unchanged. This seat's earlier ledger search returned the file on a page it did not read through."
  },
  {
    "id": "AMGT_CORPUS-D1-C-S36",
    "project": "AMGT_CORPUS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T12:15:00Z",
    "one_line": "D1-S3 (OBSERVATION, INERT) graduated to REMEDIATION_v8, owner 2.0.0_SA_COO~C1 (the round-46 reader cell ADDENDUM 1 cuts), not to the CTO as the held file prepared. The gate's blocker is gone: the tier2 transport copy of TO-READ-R44-at-4 was removed @f0ec7c5696, and this seat's census reads 0 non-terminal of 121 AMGT_CORPUS orders (to-check --all --project AMGT_CORPUS: 0 active).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_CORPUS-D1-S3"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and a grade is corrected by a NEW row, never by an edit in place.",
    "world_is": "D1-S3 (OBSERVATION, INERT) graduated to REMEDIATION_v8, owner 2.0.0_SA_COO~C1 (the round-46 reader cell ADDENDUM 1 cuts), not to the CTO as the held file prepared. The gate's blocker is gone: the tier2 transport copy of TO-READ-R44-at-4 was removed @f0ec7c5696, and this seat's census reads 0 non-terminal of 121 AMGT_CORPUS orders (to-check --all --project AMGT_CORPUS: 0 active).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row AMGT_CORPUS-D1-S3",
        "org/missions/D5/AMGT/AMGT_CORPUS/ledger/ROUND_ANALYSIS.round44.md:62-73 (ADDENDUM 1 ruling)",
        "commit f0ec7c5696 (transport copy removed)",
        "3.0.0_SA_CVO python .tools/to-check.py --all --project AMGT_CORPUS 2026-10-11T12:11Z: 0 active TOs; status census 121 orders, 0 non-terminal"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Graduated to remediations/REMEDIATION_v8.md. Supersedes the held file org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_CORPUS_R45_D1_S3_REMEDIATION_v8_HELD_20261011.md (its owner is changed)."
  }
]
```
