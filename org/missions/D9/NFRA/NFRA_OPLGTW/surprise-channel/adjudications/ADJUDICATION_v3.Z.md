# NFRA_OPLGTW -- adjudication v3 (site Z): L8 COMPILE + L9 (rounds 3-12)

Author: `3.0.0_SA_CVO~O`. Written 2026-10-02T00:44:59Z. Trigger: 2.0.0_SA_COO~O msg 28092 (slug-ready per 1.0.0_SA_CTO~O msg 28091). **Terminality:** every order is terminal except OG-g-1 (pending, round 6, held on gate G-C) and OG-v-7 / OG-v-8 (staged, round 3, held on their gates), carried by that ruling; OG-tx-2 is terminal as failed.

Input: `investigations/INVESTIGATION_v1.md`, 37 UNDER_INVESTIGATION by the channel gate's own census before this file. After it: 0.

```json
[
  {
    "id": "NFRA_OPLGTW-Z-C-S12",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-10-02T00:44:59Z",
    "one_line": "OPLGTW L8 (rounds 3-12): 26 rows DISMISSED_WITH_REASON -- causes closed by completed orders (OG-x-3, OG-t-1, OG-m-3), issuer dispositions, records, and 3 companions carried by their lead slug row.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "The L8 compile dispositions every undispositioned row of the round.",
    "world_is": "Rows whose cause is resolved by a completed order or ruling, re-read where it binds: Z-W11-S6 (OG-x-3 held for a peer ledger; OG-x-3 is complete), Z-S8 (Schwab CSV export; the streaming export OG-x-3 is complete), Z-W12-S1 (tk.AC2 stray argument; OG-t-1 complete, the 8 named tests passed by name), Z-W13-S1 (dispatcher SSM-output cap; OG-m-3's chain-log classifier is complete, 9bafcb01fa), Z-W15-S1/S2/S3 (advi floor marker and chain-log literals: infra/aws/terraform/opal-assets/advi_49f_floor.tf at HEAD carries s3:GetObjectVersion at :172 and the chain-log prefix at :56, landed by OG-m-3 @4e14699746, read by this seat). Issuer dispositions recorded and carried: Z-S20 (Part D off-repo record), Z-S21 (ancestry is not shipped: content grading, CLAUDE.md 22a). Records and instrument limits that changed no result: Z-W10-S4, Z-W11-S3, Z-W11-S5, Z-W12-S3, S6, S9, S11, Z-W13-S3, S4, Z-W14-S1 (same class as NFRA_MCPINDEX OPEN Z-W21-S19), Z-W15-S4, S5, S14, S15. Companions carried by their lead: Z-S42 -> Z-S43; Z-W10-S2 -> Z-W10-S1; Z-W12-S10 -> Z-W15-S23.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigations/INVESTIGATION_v1.md (each id adjudicated)",
        "task-orders/*.md last <status> tags, read by this seat: every order complete except OG-g-1 (pending), OG-v-7/OG-v-8 (staged), OG-tx-2 (failed) and 4 superseded",
        "infra/aws/terraform/opal-assets/advi_49f_floor.tf:56,:172 at HEAD"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "adjudicates": [
      "NFRA_OPLGTW-Z-S20",
      "NFRA_OPLGTW-Z-S21",
      "NFRA_OPLGTW-Z-S42",
      "NFRA_OPLGTW-Z-S8",
      "NFRA_OPLGTW-Z-W10-S2",
      "NFRA_OPLGTW-Z-W10-S4",
      "NFRA_OPLGTW-Z-W11-S3",
      "NFRA_OPLGTW-Z-W11-S5",
      "NFRA_OPLGTW-Z-W11-S6",
      "NFRA_OPLGTW-Z-W12-S1",
      "NFRA_OPLGTW-Z-W12-S10",
      "NFRA_OPLGTW-Z-W12-S11",
      "NFRA_OPLGTW-Z-W12-S3",
      "NFRA_OPLGTW-Z-W12-S6",
      "NFRA_OPLGTW-Z-W12-S9",
      "NFRA_OPLGTW-Z-W13-S1",
      "NFRA_OPLGTW-Z-W13-S3",
      "NFRA_OPLGTW-Z-W13-S4",
      "NFRA_OPLGTW-Z-W14-S1",
      "NFRA_OPLGTW-Z-W15-S1",
      "NFRA_OPLGTW-Z-W15-S14",
      "NFRA_OPLGTW-Z-W15-S15",
      "NFRA_OPLGTW-Z-W15-S2",
      "NFRA_OPLGTW-Z-W15-S3",
      "NFRA_OPLGTW-Z-W15-S4",
      "NFRA_OPLGTW-Z-W15-S5"
    ],
    "dismissal_reason": "Each row's cause is closed by a completed order or a recorded ruling, is a record or instrument limit that changed no result, or is a companion whose hazard its lead row in REMEDIATION_v2 carries."
  },
  {
    "id": "NFRA_OPLGTW-Z-C-S13",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-10-02T00:44:59Z",
    "one_line": "OPLGTW L8: 11 rows GRADUATED as 11 OPEN slug rows (REMEDIATION_v2), led by the Research Meeting reach (invitation), the Tax bearer tuple, and DATA_CATALOG.yaml still stored CRLF on 1,614 of 1,614 lines.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "The L8 compile dispositions every undispositioned row of the round.",
    "world_is": "See remediations/REMEDIATION_v2.md. Z-W13-S5 measured here: git ls-files --eol infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml reads i/crlf w/crlf attr/-text; 1,614 of 1,614 index-blob lines carry CR.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigations/INVESTIGATION_v1.md (each id adjudicated)",
        "remediations/REMEDIATION_v2.md"
      ]
    },
    "disposition": "GRADUATED",
    "adjudicates": [
      "NFRA_OPLGTW-S63",
      "NFRA_OPLGTW-Z-S23",
      "NFRA_OPLGTW-Z-S34",
      "NFRA_OPLGTW-Z-S41",
      "NFRA_OPLGTW-Z-S43",
      "NFRA_OPLGTW-Z-W10-S1",
      "NFRA_OPLGTW-Z-W12-S7",
      "NFRA_OPLGTW-Z-W12-S8",
      "NFRA_OPLGTW-Z-W13-S2",
      "NFRA_OPLGTW-Z-W13-S5",
      "NFRA_OPLGTW-Z-W15-S23"
    ]
  },
  {
    "id": "NFRA_OPLGTW-Z-C-S14",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-10-02T00:44:59Z",
    "one_line": "L9 grade: OGTX2-J1 PASS -- the four meetings are the spec's four by name, and REACH covers three meetings where Andrew is an invitee and not the organizer, so the spec's section-2 hypothesis holds.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Judgment criteria are graded at L9 by the CVO, never self-graded.",
    "world_is": "Graded against OG-tx-2 section 4's J1 text.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/TRANSCRIPT_REACH_RUN.json",
        "org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~15/TRANSCRIPT_REACH.json",
        "docs/briefs/opal-gateway-meeting-transcript-tools-spec-20260929.md:11-17"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Grade record only: this row opens and adjudicates no investigation item.",
    "grades": [
      {
        "criterion": "OGTX2-J1",
        "instance": "org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~15/NFRA_OPLGTW.TO-OG-tx-2.transcript-reach-live.proof_of_spec.json@3403243217",
        "verdict": "PASS",
        "reason": "spec_name on the 4 meeting objects equals the spec's list (spec :11-12): 9a ET Monday Meeting (Teams 'Morning Meeting'), OCIO investment committee ('OCIO IC'), Asset Management investment committee ('Asset Management IC'), Research Meeting ('Research Team Meeting'). The three read meetings each carry organizer_is_andrew false and andrew_is_invitee true, with rows 19/7/8 and body bytes 59,266/66,701/63,093 equal to total bytes, so REACH covers invitee-not-organizer three times (the hypothesis at spec :16). Limits: the organizer and invitee flags are the issuer's run record, not re-read by this seat; the fourth meeting doubles as the negative arm, so the negative arm is not independent of the AC1 failure. AC1's own FAIL (3 of 4) stands and is the slug's row Z-S43."
      }
    ]
  }
]
```
