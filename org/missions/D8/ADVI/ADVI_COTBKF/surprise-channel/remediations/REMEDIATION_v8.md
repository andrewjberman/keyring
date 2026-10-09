# ADVI_COTBKF -- round 14 remediations

<sweep_watermark>2026-10-07T16:2xZ</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2), 2026-10-07 ~16:2xZ. Graduated at this compile (ADJUDICATION_v12.md): 1 row, OPEN, round label v15.

```json
[
 {
  "id": "ADVI_COTBKF-D2-S25",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "After the re-apply on the one signing table, the crosswalk's near-match list (AWAITING_PERSON) grew from 21 to 22; the near-match page round 4 graded (deliverables/0.9.0_WK_ADVI_COTBKF~14/near_matches.md) lists 21.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-S25",
   "s3 opal-data-assets commonwealth/cottonwood/silver/crosswalk/date=2026-06-23/crosswalk.parquet: 1,533 rows, 471 MATCHED, 1,062 NOT_MATCHED, 22 AWAITING_PERSON; account_links/date=2026-06-23/account_links.parquet: 1,450 rows, 212 LINKED; acct#e1e2dacb -> acct#f6464238 LINKED; acct#d6187d4b NOT_LINKED LEFT_COMMONWEALTH (this compile's read, dell2, 2026-10-07 ~16:2xZ)"
  ],
  "remedy": "Regenerate the near-match page from the applied crosswalk before it reaches Andrew or Cottonwood; the new entry is read like the 21 (both sides, by CUSIP and quantity).",
  "owner": "2.0.0_SA_COO~C2",
  "round": "v15",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~C2",
   "round": "v15"
  },
  "closed": true
 }
]
```

Clock advanced in place at the round-15 compile (3.0.0_SA_CVO, 2026-10-07 ~16:4xZ; state fields only): D2-S25 REMEDIATED and closed. CB-o-1 (@cb6c7d6cd5) regenerated the near-match page from the served crosswalk (VersionId wv5z6zeR..): 22 entries, all 21 of round 4's kept, 1 entered (acct#8179a706, 0.75, unscored under the old rules). This seat read the served crosswalk: 22 AWAITING_PERSON rows, the page's 22 accounts the same set; acct#8179a706 NOT_MATCHED, 0.75, AWAITING_PERSON. Round 15 filed no rows, so no adjudication file is written for it.
