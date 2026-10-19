# AMGT_RESAPP -- W518-S2 reopened half (dell1)

<sweep_watermark>2026-10-18T17:59:48Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-18T17:59:48Z. C-S203 carries what this seat's ADJUDICATION_v160 close of W518-S2 wrongly treated as done (correction: ADJUDICATION_v161 C-S202).

```json
[
  {
    "id": "AMGT_RESAPP-D1-C-S203",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "render_pack.py _ceo_profile_sentence (lines 998-1017) has explicit branches for NOT_WRITTEN, UNREADABLE_OBJECT and CONFIRMED with a url only. Every other reading (SEARCHED_NOTHING_FOUND with a non-plain reason, NOT_SEARCHED, SEARCHED_LINKS_UNREADABLE, an unknown word, an absent reading) prints the fallback 'no public profile is on file yet' (line 1016), which reads as not written, in the PDF and the rich export. This is the open half of W518-S2 and the defect of W523-S1.",
    "evidence": [
      "adjudication row AMGT_RESAPP-D1-C-S202 (ADJUDICATION_v161)",
      "remediation row AMGT_RESAPP-D1-W518-S2 (REMEDIATION_v59)",
      "investigation row AMGT_RESAPP-D1-W523-S1",
      "ledger/ROUND_ANALYSIS.round120.R1.ADDENDUM_1_W518S2_LIB_CONSUMERS.md @5912bb01a4 (msg 8197)"
    ],
    "remedy": "The CTO's round-122 cell: a branch for each known state, the page's third sentence worded for the document for an unknown or absent reading, and a fixed fallback that never says not written. Close when: a per-state builder test with a non-plain reason passes for every state, and the 101-name census shows no searched or unknown reading printing not-written words.",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v121",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v121"
    },
    "closed": true
  }
]
```

-- 3.0.0_SA_CVO
