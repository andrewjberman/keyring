# NFRA_MCPINDEX ROUND 6 -- L8 COMPILE + L9 ADJUDICATION

**Seat:** `3.0.0_SA_CVO~O`. **Written:** 2026-10-01T14:50:00Z. **Terminality:** 5 of 6 orders terminal; MX-s-16 closes on its scheduled run 2026-10-02 ~00:1xZ, so the L10 slug waits for it. MX-t-12 CANCELLED.

Input: `investigations/INVESTIGATION_v1.md`, 27 UNDER_INVESTIGATION by the channel gate's own census before this file. After it: 0. Packet `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round6/L8_PACKET_ROUND6.md@235653342a`.

```json
[
  {
    "id": "NFRA_MCPINDEX-Z-C-S36",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-10-01T14:50:00Z",
    "one_line": "Round 6 L8: 20 rows DISMISSED_WITH_REASON -- disarms re-read (OTP rotation, sender table), instrument records, and 2 companions carried by their lead slug row.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "The L8 compile dispositions every undispositioned row of the round.",
    "world_is": "Re-read by this seat: Z-S73 (OTP bearer echoed): the OG-rl-1 ledger 20261001T1038Z_nfra-oplgtw-trnspt-deps-release is CLOSED with cot otp-gateway-token rotated (AWSPREVIOUS holds the old), /otp/health old=401 new=200, and K1 MATCH on both principal keys before the put. Z-W22-S4 disarmed by Z-W22-S9 (MAIL_SENDER_TABLE read SET items=3 len=67 before and after; shape, not identity, as the row says). Z-S75 (r8.AC2 empty SSM read): check hardened @273e5832cb; MX-r-8 live e3567ce5f7 was read by this seat through discover and the BD tool (Z-C-S35). Records and limits that changed no result: Z-W22-S2 (routing-recall enrichment, carried by OPEN v3 Z-W10-S1), S3 (internal_role Config; 8 s wall-clock bound), S5 (audited override on scratch branches), S6 (AccessDenied for an absent key; every catalogued key exists), S7, S8 (wrapper manifest fields: same class as OPEN v4 Z-W21-S23), S10, S11 (per-date total compared; it covers every matched row), S12 (wrapper path exercised by the principal-session call); Z-W23-S1, S3; Z-W24-S1, S6, S7. Companions carried by their lead: Z-W24-S2 -> Z-W24-S4; Z-W24-S5 -> Z-W24-S4.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigations/INVESTIGATION_v1.md (each id adjudicated)",
        "org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round6/L8_PACKET_ROUND6.md@235653342a",
        "org/critical_paths/change_management/20261001T1038Z_nfra-oplgtw-trnspt-deps-release_deploy_completion.md, read by this seat"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "adjudicates": [
      "NFRA_MCPINDEX-Z-S73",
      "NFRA_MCPINDEX-Z-S75",
      "NFRA_MCPINDEX-Z-W22-S10",
      "NFRA_MCPINDEX-Z-W22-S11",
      "NFRA_MCPINDEX-Z-W22-S12",
      "NFRA_MCPINDEX-Z-W22-S2",
      "NFRA_MCPINDEX-Z-W22-S3",
      "NFRA_MCPINDEX-Z-W22-S4",
      "NFRA_MCPINDEX-Z-W22-S5",
      "NFRA_MCPINDEX-Z-W22-S6",
      "NFRA_MCPINDEX-Z-W22-S7",
      "NFRA_MCPINDEX-Z-W22-S8",
      "NFRA_MCPINDEX-Z-W22-S9",
      "NFRA_MCPINDEX-Z-W23-S1",
      "NFRA_MCPINDEX-Z-W23-S3",
      "NFRA_MCPINDEX-Z-W24-S1",
      "NFRA_MCPINDEX-Z-W24-S2",
      "NFRA_MCPINDEX-Z-W24-S5",
      "NFRA_MCPINDEX-Z-W24-S6",
      "NFRA_MCPINDEX-Z-W24-S7"
    ],
    "dismissal_reason": "Each row is a disarm whose effect was read, a record or instrument limit that changed no result, or a companion whose hazard its lead row in REMEDIATION_v5 carries."
  },
  {
    "id": "NFRA_MCPINDEX-Z-C-S37",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-10-01T14:50:00Z",
    "one_line": "Round 6 L8: 7 rows GRADUATED as 7 OPEN slug rows (REMEDIATION_v5); one corrects the issuer's disarm note -- the stale merge script still runs for realized and transactions (Z-W24-S3).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "The L8 compile dispositions every undispositioned row of the round.",
    "world_is": "See remediations/REMEDIATION_v5.md. Z-W24-S3 measured here: aws ssm get-document opal-bd-realized-download and opal-bd-transaction-download (Default = Latest = v3) each name s3://opal-data-bd/scripts/merge-daily-incremental.py; unrealized (v4) and allocation (v6) name no merge script.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigations/INVESTIGATION_v1.md (each id adjudicated)",
        "remediations/REMEDIATION_v5.md",
        "org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round6/L8_PACKET_ROUND6.md@235653342a",
        "aws ssm describe-document / get-document on the four opal-bd-*-download documents, read by this seat 2026-10-01 ~14:4xZ"
      ]
    },
    "disposition": "GRADUATED",
    "adjudicates": [
      "NFRA_MCPINDEX-Z-S72",
      "NFRA_MCPINDEX-Z-S74",
      "NFRA_MCPINDEX-Z-W22-S1",
      "NFRA_MCPINDEX-Z-W23-S2",
      "NFRA_MCPINDEX-Z-W24-S3",
      "NFRA_MCPINDEX-Z-W24-S4",
      "NFRA_MCPINDEX-Z-W24-S8"
    ]
  },
  {
    "id": "NFRA_MCPINDEX-Z-C-S38",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-10-01T14:50:00Z",
    "one_line": "L9 grades, round 6: MXV7-J1 PASS (the route and the figure, measured independently by this seat and by the cell); MXV7-J2 NOT_EVALUATED (Alyssa's cold run has not run; now unblocked).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Judgment criteria are graded at L9 by the CVO, never self-graded.",
    "world_is": "Graded against MX-v-7's J1 and J2 text.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "adjudications/ADJUDICATION_v5.md#NFRA_MCPINDEX-Z-C-S35",
        "org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round6/L8_PACKET_ROUND6.md@235653342a",
        "org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~22/THREAD_RERUN_round6.json"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Grade record only: this row opens and adjudicates no investigation item.",
    "grades": [
      {
        "criterion": "MXV7-J1",
        "instance": "org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~22/NFRA_MCPINDEX.TO-MX-v-7.thread-rerun-round6.proof_of_spec.json@e9b50ae78c",
        "verdict": "PASS",
        "reason": "Two independent measurements agree. This seat (Z-C-S35): a principal session whose tool list postdates MX-r-8, discover names blackdiamond_list_fees for the BD fees ask, and the tool's 2026-09-29 answer equals silver/fees/2026-09-29.parquet VersionId Qp7FdHII2X4JQYzDSOAB9wGi1UcNJfpt on 22,853 rows, 22,221 de-duplicated, 632 duplicate rows, transaction_fee 63.43, account_fee 0.00, as_of 2026-09-29. The cell's THREAD_RERUN_round6.json reads the same figures on the answer() path. Limit: per-date totals, not a row-level compare (Z-W22-S11); totals cover every matched row."
      },
      {
        "criterion": "MXV7-J2",
        "instance": "org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~22/NFRA_MCPINDEX.TO-MX-v-7.thread-rerun-round6.proof_of_spec.json@e9b50ae78c",
        "verdict": "NOT_EVALUATED",
        "reason": "No material: Alyssa's cold run has not run. Its prerequisite is served (this seat read 'Schwab positions' -> schwab_query live). For the grader: discover's freshness for silver rows names the field only (latest_value and served_written_at both claim 'absent', deferring the date to the tool's as_of), and the A1 firm gate shows silver rows only to OPAL_INTERNAL, so the asker must resolve OPAL_INTERNAL for discover to name any Schwab row (Z-W22-S1)."
      }
    ]
  }
]
```
