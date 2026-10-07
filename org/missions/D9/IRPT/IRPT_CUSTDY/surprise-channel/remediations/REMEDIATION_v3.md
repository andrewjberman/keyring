# IRPT_CUSTDY -- round 3 remediations

<sweep_watermark>2026-10-07T10:5xZ</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2), 2026-10-07 ~10:5xZ. Graduated at this compile (ADJUDICATION_v3.md): 2 rows, both OPEN, round label
v4. S7 is a red test on CLOUD; S8 carries E2's real-run grade and its two gaps to the analysis.

```json
[
 {
  "id": "IRPT_CUSTDY-S7",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The CLOUD test suite for irpt_custody is red: test_none_source_names_the_seam_line fabricates the round-2 'None' refusal, which IRPT_BCKEND's seam fix (IB-pr-339) removed, so the tracer test now fails on correct code.",
  "evidence": [
   "investigation row IRPT_CUSTDY-S7",
   "pytest -q data/assets/scripts/gold/irpt_custody/tests: 73 passed, 1 xfailed, 1 failed (test_advisor_projection_refused.py::test_none_source_names_the_seam_line) (this compile's read, dell2 CLOUD, 2026-10-07 ~10:5xZ)",
   "custodian_key_seam.json: 0 of 5,393 leaf values are the string 'None'; ids.py:388 now treats '', 'None' and 'nan' as unmapped (this compile's read, dell2 CLOUD, 2026-10-07 ~10:5xZ)"
  ],
  "remedy": "Retire the tracer test or re-point it to the guard that now handles a null-like key; the suite reads 0 failed.",
  "owner": "2.0.0_SA_COO~K2",
  "round": "v4",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~K2",
   "round": "v4"
  },
  "closed": true
 },
 {
  "id": "IRPT_CUSTDY-S8",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "E2's real run on dell2 (advisor matthew_gooch, as of 2026-09-30) grades QTD, YTD and 1Y on 14 of 14 accounts and QTD and YTD on 10 of 10 households (1Y: 7 OK, 3 NO_DATA shown in place), every figure naming its source rows (124 of 124). SI is NO_DATA on every account and household because no inception anchor resolves, and 4 granted accounts are NOT_IN_DIRECTORY; after the seam fix 1,961 of 7,022 granted accounts are NOT_IN_DIRECTORY.",
  "evidence": [
   "investigation row IRPT_CUSTDY-S8",
   "org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/2.0.0_SA_COO~K2/IRPT_CUSTDY_ROUND_3_DRAIN_END_20261007.md @8911b19a90: HOP3-REAL-RUN households=10 accounts=14 uncovered=4 held_si=0 error=none; PICK-REREAD before_refused=482 after_refused=0 of=7022 uncovered=2189 (NOT_IN_DIRECTORY 1961, NO_SILVER_AT_AS_OF 228)",
   "the real-run file holds a real advisor's client figures and is not committed; this seat graded from the row's measured summary"
  ],
  "remedy": "For the round-3 analysis: an SI inception anchor (the accounts-file inception, or the gold manifest's first_data_date) that resolves on real data, with the SI hold floor moved to 2010; and the 1,961 NOT_IN_DIRECTORY accounts read as an IRPT_BCKEND directory-coverage question.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v4",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v4"
  },
  "closed": true
 }
]
```
