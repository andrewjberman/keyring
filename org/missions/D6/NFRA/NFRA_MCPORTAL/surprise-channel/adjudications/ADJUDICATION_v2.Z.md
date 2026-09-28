# NFRA_MCPORTAL -- round 2 L8 compile + L9 (site Z)

Author: 3.0.0_SA_CVO~O. Round: v2. Fabric: site-z. Recorded: 2026-09-28T13:47:55Z.

Terminality: round 2's 6 orders are terminal: 5 complete, and MP-a-1 superseded @4ce47993e4 by 2.0.0_SA_COO~O on
Andrew-direct ('close out each project's round so the CVO can slug'). Input: the fold read 11 undispositioned of 25
items. This file dispositions all 11: 3 GRADUATED and 8 DISMISSED_WITH_REASON. L9 is vacuous: 0 judgment criteria.

```json
[
  {
    "id": "NFRA_MCPORTAL-Z-C-S12",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-28T13:47:55Z",
    "one_line": "Round 2 L8: 3 rows GRADUATED (Z-W2-S3 ARMED, Z-W1-S5, Z-W2-S6), each still measured present at 13:4xZ; remediation OPEN, owner the issuer.",
    "class": "OBSERVATION",
    "spec_asserts": "The L8 compile dispositions every undispositioned row of the round.",
    "world_is": "Z-W2-S3: infra/aws/ec2/opal-gateway/app/config.py:307 still defaults AUDIT_PATH to ./audit.jsonl, so the suite still writes the tracked audit file. Z-W1-S5: infra/aws/lambda/ci/lambda-source-map.json still names MCPORTAL_OWNER_OID (1 occurrence), and the MP-a-1 apply, re-cut next round, must pass the two new owner-key variables. Z-W2-S6: EC2_MANIFEST.json services.opal-gateway.file_checksums app/server.py still reads a101f27e..., the value the row found not to describe f1f0fc6780; deployed_commit has since moved to 6a98a0553a. Not re-hashed here.",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-W2-S3",
      "NFRA_MCPORTAL-Z-W1-S5",
      "NFRA_MCPORTAL-Z-W2-S6"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "INVESTIGATION_v1.Z.md#NFRA_MCPORTAL-Z-W2-S3, #NFRA_MCPORTAL-Z-W1-S5, #NFRA_MCPORTAL-Z-W2-S6",
        "infra/aws/ec2/opal-gateway/app/config.py:307",
        "infra/aws/lambda/ci/lambda-source-map.json (MCPORTAL_OWNER_OID count 1)",
        "infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S13",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-28T13:47:55Z",
    "one_line": "Round 2 L8: NFRA_MCPORTAL-Z-S4 dismissed with reason.",
    "class": "OBSERVATION",
    "spec_asserts": "The L8 compile dispositions every undispositioned row of the round.",
    "world_is": "A disarm record by the disarm owner (1.0.0_SA_CTO~O): owned-paths-validate now consults a worker's order grant on an unmapped path. Commit 6bc980ad5d exists and touches .tools/owned-paths-validate.py only (read here). The record opens no new hazard. W1-S1's REMEDIATION_v1.Z row still reads OPEN; the flip is carried in the slug.",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-S4"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "INVESTIGATION_v1.Z.md#NFRA_MCPORTAL-Z-S4"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A disarm record by the disarm owner (1.0.0_SA_CTO~O): owned-paths-validate now consults a worker's order grant on an unmapped path. Commit 6bc980ad5d exists and touches .tools/owned-paths-validate.py only (read here). The record opens no new hazard. W1-S1's REMEDIATION_v1.Z row still reads OPEN; the flip is carried in the slug."
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S14",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-28T13:47:55Z",
    "one_line": "Round 2 L8: NFRA_MCPORTAL-Z-S5 dismissed with reason.",
    "class": "OBSERVATION",
    "spec_asserts": "The L8 compile dispositions every undispositioned row of the round.",
    "world_is": "A containment record by the issuer for Z-W2-S3. Its own world_is says the hazard stands for any seat that commits the gateway tree after running the suite. The hazard is carried on Z-W2-S3, which C-S12 graduates.",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-S5"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "INVESTIGATION_v1.Z.md#NFRA_MCPORTAL-Z-S5"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A containment record by the issuer for Z-W2-S3. Its own world_is says the hazard stands for any seat that commits the gateway tree after running the suite. The hazard is carried on Z-W2-S3, which C-S12 graduates."
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S15",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-28T13:47:55Z",
    "one_line": "Round 2 L8: NFRA_MCPORTAL-Z-W2-S2 dismissed with reason.",
    "class": "OBSERVATION",
    "spec_asserts": "The L8 compile dispositions every undispositioned row of the round.",
    "world_is": "Resolved inside MP-g-1: the three whoami fields are added only when the ALB header carries claims, so the read-only exact-equality test holds and a real ALB-OIDC request carries the fields. No residual hazard.",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-W2-S2"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "INVESTIGATION_v1.Z.md#NFRA_MCPORTAL-Z-W2-S2"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Resolved inside MP-g-1: the three whoami fields are added only when the ALB header carries claims, so the read-only exact-equality test holds and a real ALB-OIDC request carries the fields. No residual hazard."
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S16",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-28T13:47:55Z",
    "one_line": "Round 2 L8: NFRA_MCPORTAL-Z-S6 dismissed with reason.",
    "class": "OBSERVATION",
    "spec_asserts": "The L8 compile dispositions every undispositioned row of the round.",
    "world_is": "A disarm record by the issuer for Z-W1-S3 and Z-W1-S4: the face and checks were amended @051240c792 and the rebuild passes 3 of 3 (db3bae76ba). It opens no new hazard.",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-S6"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "INVESTIGATION_v1.Z.md#NFRA_MCPORTAL-Z-S6"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A disarm record by the issuer for Z-W1-S3 and Z-W1-S4: the face and checks were amended @051240c792 and the rebuild passes 3 of 3 (db3bae76ba). It opens no new hazard."
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S17",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-28T13:47:55Z",
    "one_line": "Round 2 L8: NFRA_MCPORTAL-Z-S7 dismissed with reason.",
    "class": "OBSERVATION",
    "spec_asserts": "The L8 compile dispositions every undispositioned row of the round.",
    "world_is": "A disarm record by the issuer for Z-W2-S7 (the MP-d-1 outage, ~17:14-17:31:22Z, rolled back). The issuer verified /health 200 live. The retry shipped behind a render gate, and MP-d-1 is complete. It opens no new hazard.",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-S7"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "INVESTIGATION_v1.Z.md#NFRA_MCPORTAL-Z-S7"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A disarm record by the issuer for Z-W2-S7 (the MP-d-1 outage, ~17:14-17:31:22Z, rolled back). The issuer verified /health 200 live. The retry shipped behind a render gate, and MP-d-1 is complete. It opens no new hazard."
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S18",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-28T13:47:55Z",
    "one_line": "Round 2 L8: NFRA_MCPORTAL-Z-W2-S4 dismissed with reason.",
    "class": "OBSERVATION",
    "spec_asserts": "The L8 compile dispositions every undispositioned row of the round.",
    "world_is": "Resolved inside MP-d-1: the channel file was dropped from the release branch and never committed to CLOUD. The gateway census is unaffected (9 files). No residual hazard.",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-W2-S4"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "INVESTIGATION_v1.Z.md#NFRA_MCPORTAL-Z-W2-S4"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Resolved inside MP-d-1: the channel file was dropped from the release branch and never committed to CLOUD. The gateway census is unaffected (9 files). No residual hazard."
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S19",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-28T13:47:55Z",
    "one_line": "Round 2 L8: NFRA_MCPORTAL-Z-W2-S5 dismissed with reason.",
    "class": "OBSERVATION",
    "spec_asserts": "The L8 compile dispositions every undispositioned row of the round.",
    "world_is": "Resolved inside MP-d-1: the gate's documented routine acknowledgement (HALT_ACK=1) was added after the list was reviewed. The issuer's standing rule in Z-S8 makes later gateway faces carry the pre-acked line.",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-W2-S5"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "INVESTIGATION_v1.Z.md#NFRA_MCPORTAL-Z-W2-S5"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Resolved inside MP-d-1: the gate's documented routine acknowledgement (HALT_ACK=1) was added after the list was reviewed. The issuer's standing rule in Z-S8 makes later gateway faces carry the pre-acked line."
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S20",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-28T13:47:55Z",
    "one_line": "Round 2 L8: NFRA_MCPORTAL-Z-S8 dismissed with reason.",
    "class": "OBSERVATION",
    "spec_asserts": "The L8 compile dispositions every undispositioned row of the round.",
    "world_is": "A disarm record by the issuer for Z-W2-S8 (a 12-minute halt-gate delay on rollback). Later gateway faces arm the rollback pre-acked when the STOP count is 0. The MP-d-1 release did not need it. It opens no new hazard.",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-S8"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "INVESTIGATION_v1.Z.md#NFRA_MCPORTAL-Z-S8"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A disarm record by the issuer for Z-W2-S8 (a 12-minute halt-gate delay on rollback). Later gateway faces arm the rollback pre-acked when the STOP count is 0. The MP-d-1 release did not need it. It opens no new hazard."
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S21",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-28T13:47:55Z",
    "one_line": "Round 2 L9 is VACUOUS with its cause named: none of the round's 6 orders carries a judgment criterion.",
    "class": "OBSERVATION",
    "spec_asserts": "Judgment criteria are graded at L9, never self-graded.",
    "world_is": "The round-2 orders are MP-b-1, MP-b-2, MP-d-1, MP-g-1, MP-p-1 (complete) and MP-a-1 (superseded @4ce47993e4, held on Andrew's G-HDR, re-cut in round 3). A count of judgment=\"true\" over all 13 order files reads 0. The mechanical columns are the round's only oracle; SERVED/WORLD cells shipped without a plausibility criterion.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "task-orders/*.md (judgment=\"true\" count 0 of 13 files)",
        "commit 4ce47993e4"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Grade record only: this row opens and adjudicates no investigation item."
  }
]
```

-- 3.0.0_SA_CVO~O
