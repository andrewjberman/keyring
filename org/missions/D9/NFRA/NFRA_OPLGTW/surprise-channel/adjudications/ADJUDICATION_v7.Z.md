# NFRA_OPLGTW -- adjudication v7 (site Z): L9 re-grade of OGO2-J1 on OG-o-5 A1

Author: `3.0.0_SA_CVO~O`. Written 2026-10-04T00:05:00Z. Trigger: 2.0.0_SA_COO~O msg 29073 (OG-o-5 A1 drained @2a3c9151b2). A grade
record only.

```json
[
  {
    "id": "NFRA_OPLGTW-Z-C-S21",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-10-04T00:05:00Z",
    "one_line": "L9 re-grade: OGO2-J1 PASS on OG-o-5 A1. 7.1-7.2 carry the flag truth and the schwab_status read; 7.3 names the four read-only bucket reads, which this seat ran: all resolve and match the baseline.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Judgment criteria are graded at L9 by the CVO, never self-graded.",
    "world_is": "Graded on infra/aws/ec2/opal-gateway/runbooks/SCHWAB_PILOT_RUNBOOK.md at 2a3c9151b2, on OG-o-5's J1.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/opal-gateway/runbooks/SCHWAB_PILOT_RUNBOOK.md@2a3c9151b2 sections 7.1-7.3",
        "aws s3api get-bucket-versioning / get-bucket-encryption / get-public-access-block / get-bucket-policy-status --bucket opal-data-assets, run read-only by this seat ~00:0xZ: Enabled / AES256 / True x4 / IsPublic False"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Grade record only: this row opens and adjudicates no investigation item.",
    "grades": [
      {
        "criterion": "OGO2-J1",
        "instance": "org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~21/NFRA_OPLGTW.TO-OG-o-5.runbook-section7-remedy.proof_of_spec.json@bfe0028826",
        "verdict": "PASS",
        "reason": "Graded on SCHWAB_PILOT_RUNBOOK.md at 2a3c9151b2 (OG-o-5 A1, equal to HEAD). PASS. Sections 0-6 and 8 are unchanged from their PASS. 7.1: the disable, the template re-render at every deploy (:250-252), and step 3's Read command (ops/schwab_status.py, which prints HEALTH.checks.integration_enabled). 7.2 step 2: re-apply 7.1 after any restore and confirm integration_enabled=false, pointing to 7.1 step 3. 7.3: one 'Bucket reads' line names the four read-only reads on opal-data-assets, and the contradicting 'does not run the AWS read' sentence is gone. This seat ran all four at ~00:0xZ, and each resolved and matched the stated baseline: versioning Enabled; encryption AES256; public-access blocks True/True/True/True; policy IsPublic False. An operator can execute each section at its named moment without other context."
      }
    ]
  }
]
```

-- 3.0.0_SA_CVO~O
