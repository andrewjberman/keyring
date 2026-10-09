# NFRA_MCPMSP -- surprise channel, ADJUDICATION v2 (site Z) -- ROUND 2 L8 compile + L9

**Lane:** the CVO. **By:** `3.0.0_SA_CVO~Z`, standing in for `3.0.0_SA_CVO~O` (not registered), 2026-10-09 ~08:0xZ, on
`2.0.0_SA_COO~MS` msg 32440 (acked). **Input:** `deliverables/2.0.0_SA_COO~MS/round2/DRAIN_END_round2.md` @a92355352f.

**Denominator at this compile** (`comp-surprise --project NFRA_MCPMSP --json`, read 07:5xZ): 31 investigation items,
2 adjudication rows, 7 remediation rows; OPEN 13, ARMED 0. This document dispositions all 13 OPEN rows: 10 DISMISSED
(C-S3) and 3 GRADUATED (C-S4). It also grades the round's one judgment criterion, MS-dn-1 AC5 (C-S5). The watermark
moves from round 1 to round 2.

```json
[
  {
    "id": "NFRA_MCPMSP-Z-C-S3",
    "project": "NFRA_MCPMSP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-09T08:00Z",
    "one_line": "Round 2 L8: 10 rows DISMISSED -- each was resolved by an issuer amendment, handled in the act it describes, or records a fact with no live defect.",
    "class": "OBSERVATION",
    "spec_asserts": "The L8 compile dispositions every undispositioned row of the round.",
    "world_is": "W1-S9: MS-dn-1 parsed the one .env line, as the row asked (proof method line). W1-S10: the wider census is correct, and sprint_view reads daily-reports/, not firm keys. W3-S3: AC2's conflict was resolved by the issuer's AMENDMENT 1 (fakes carry member emails; W3-S5 records it), and MS-sg-1 is complete. W3-S4: the KNOWN_FIRMS positional mapping is guarded by the pinned test, which fails first on a reorder. W3-S5: the address-carrying refusal fields are covered by test_refusal_entry_has_sender_email_domain_no_text. W3-S6: the issuer flipped the status, as for MS-ig-1. W5-S1: the release-commit lane refusal is the class the estate now meets with an audited author override on the release commit (R13(a), used at r29 91811b648a). W5-S2: a reproduction note for the suite's env placeholders. W5-S3: three failures identical at base and release, not this release's. W5-S4: the saved-plan apply is stricter than apply-time -target, and AC2 read the Deny live.",
    "adjudicates": [
      "NFRA_MCPMSP-Z-W1-S9",
      "NFRA_MCPMSP-Z-W1-S10",
      "NFRA_MCPMSP-Z-W3-S3",
      "NFRA_MCPMSP-Z-W3-S4",
      "NFRA_MCPMSP-Z-W3-S5",
      "NFRA_MCPMSP-Z-W3-S6",
      "NFRA_MCPMSP-Z-W5-S1",
      "NFRA_MCPMSP-Z-W5-S2",
      "NFRA_MCPMSP-Z-W5-S3",
      "NFRA_MCPMSP-Z-W5-S4"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigations/INVESTIGATION_v1.Z.md (each row's own text, read via comp-surprise 07:5xZ)",
        "deliverables/0.9.0_WK_NFRA_MCPMSP~5/NFRA_MCPMSP.TO-MS-dn-1.gateway-firm-deny.proof_of_spec.json (method, session_log)",
        "deliverables/0.9.0_WK_NFRA_OPLGTW~43/ANNOUNCE_OG-rl-15.md @368e48e533 line 7 (R13(a) release-commit override, NFRA_OPLGTW)",
        "round-close-check.py --project NFRA_MCPMSP --round 2: 11 complete, proof_ok=11, 3 cancelled"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "No row leaves a live defect in this project: each is resolved by an amendment or act already landed, or is a recorded fact."
  },
  {
    "id": "NFRA_MCPMSP-Z-C-S4",
    "project": "NFRA_MCPMSP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-09T08:00Z",
    "one_line": "Round 2 L8: 3 rows GRADUATE to REMEDIATION_v2.Z -- each is a defect still live at HEAD.",
    "class": "OBSERVATION",
    "spec_asserts": "The L8 compile dispositions every undispositioned row of the round.",
    "world_is": "Live: W7-S1 (safe-apply's tag-authz and tombstone gates re-plan the whole tree for a targeted or planfile apply); W4-S3 (the asker refusal listing derives sender fields from the record's user field; correct only if user is the Teams sender, never measured); Z-S4 (round-close-check's id fallback disagrees with proof-of-spec-check, the same class as NFRA_REPORT-Z-S26).",
    "adjudicates": [
      "NFRA_MCPMSP-Z-W7-S1",
      "NFRA_MCPMSP-Z-W4-S3",
      "NFRA_MCPMSP-Z-S4"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "remediations/REMEDIATION_v2.Z.md",
        ".tools/round-close-check.py:159 (read 2026-10-09 07:1xZ)",
        "investigations/INVESTIGATION_v1.Z.md#NFRA_MCPMSP-Z-W7-S1",
        "investigations/INVESTIGATION_v1.Z.md#NFRA_MCPMSP-Z-W4-S3"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "NFRA_MCPMSP-Z-C-S5",
    "project": "NFRA_MCPMSP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-09T08:00Z",
    "one_line": "L9 grade, TO-MS-dn-1 AC5 (judgment): PASS -- the gateway firm Deny changed no served answer, and a served firm answer flows through the gateway today with the Deny live.",
    "class": "OBSERVATION",
    "spec_asserts": "MS-dn-1 AC5: the internal Analyst's and /query/v0's served figures, dates and coverage on a fixed set of firm questions are unchanged after vs before the Deny.",
    "world_is": "BEFORE (14:18:18Z) and AFTER (14:33:45Z) on 2026-10-01 read 10 keys (9 firm, 1 global) through app.query_v0._fetch_capped with INTERNAL_READER_ROLE_ARN set on the host: sha256, bytes and every as-of field equal on 10 of 10, with 0 errors either time. AFTER follows the apply, and AC2 read explicitDeny on the firm keys in between, so the AFTER read ran under the Deny. Live re-read by this seat 2026-10-09 ~07:5xZ: iam get-role-policy opal-gateway-role gateway-firm-deny-policy shows Deny s3:GetObject on exactly platinum/mdpf/{49financial,inflection,cottonwood}/*. mdpf_get_aum_metrics(scope=inflection) through the gateway returns status ok from platinum/mdpf/inflection/aum-metrics.json, as-of 2026-10-07, 548 accounts. The served path does not read firm data as the gateway identity. The Analyst path is covered at code level by AC1 (unrouted=0), not by its own before/after answer.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/0.9.0_WK_NFRA_MCPMSP~5/AC5_BEFORE_MS-dn-1.json",
        "deliverables/0.9.0_WK_NFRA_MCPMSP~5/AC5_AFTER_MS-dn-1.json",
        "aws iam get-role-policy --role-name opal-gateway-role --policy-name gateway-firm-deny-policy (live, 2026-10-09)",
        "opalgateway mdpf_get_aum_metrics(scope=inflection), live 2026-10-09: status ok, key platinum/mdpf/inflection/aum-metrics.json, as_of 2026-10-07"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade, not a defect: AC5 PASS. Bound stated: the Analyst arm rests on AC1's routing census, not its own before/after answer."
  }
]
```

-- 3.0.0_SA_CVO~Z
