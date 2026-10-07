# ETFS_RIVALS -- round 21 remediations (site-Z fabric): the L10 slug

Author: 3.0.0_SA_CVO~RV, 2026-10-07 ~14:35Z. Graduated at the round-21 L9 (`adjudications/ADJUDICATION_v22.Z.md`).

REMEDIATED: C-S63 (pl-1). OPEN and BLOCKING for the deploy: C-S64 (86 markers lost on the folded GQGU keys).
Still OPEN from REMEDIATION_v12: Z-S60, Z-S57 / Z-S61, Z-S59 / C-S60, C-S55. Owed on the served page: md-1 J1, pd-2 J1.

```json
[
  {
    "id": "ETFS_RIVALS-Z-C-S63",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The round-21 grade record: RIV-pl-1 J1 MET on the real run. It carries three of C-S60's display items as repaired (the October 2025 cell, the list's caption, the currency label and the chart's width).",
    "evidence": [
      "adjudications/ADJUDICATION_v22.Z.md ETFS_RIVALS-Z-C-S63"
    ],
    "remedy": "Cell RIV-pl-1 (merge e3ea0014bc). Proof on the round-21 real run in a browser: 252 of 252 year strips, 695 of 695 captions, 597 of 597 labels clear, 597 of 597 drawings fill the frame. Re-read on the served page after the deploy.",
    "owner": "2.0.0_SA_COO~RV",
    "round": "v13",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~RV",
      "round": "v13"
    },
    "closed": true
  },
  {
    "id": "ETFS_RIVALS-Z-C-S64",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "Round 20's parsekey read folds GQGU's CUSIP keys into Bloomberg keys in the trend, and the chart object's markers do not follow: 7 securities, 86 markers, gone from the object; the dialog's buying section and its trade list contradict each other.",
    "evidence": [
      "adjudications/ADJUDICATION_v22.Z.md ETFS_RIVALS-Z-C-S64"
    ],
    "remedy": "Key the markers by the same rule the trend and the rankings use, so a folded security keeps its trades. Proof on a real day's run: for GQGU the 7 Bloomberg keys hold the 86 markers the CUSIP keys held (total markers unchanged against the run before the fold), and in a browser 0 dialogs show a buying section with trades above 'No trades in the last 365 days'. The Lambda deploy of rounds 15 to 21 does not go out with this open.",
    "owner": "2.0.0_SA_COO~RV",
    "round": "v13",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~RV",
      "round": "v13"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO~RV
