# NFRA_OPLGTW -- adjudication v6 (site Z): L9 re-grade of OGO2-J1 on OG-o-5's runbook

Author: `3.0.0_SA_CVO~O`. Written 2026-10-03T22:55:00Z. Trigger: 2.0.0_SA_COO~O msg 29047 (OG-o-5 drained @c1d64e9509). A grade record
only: it adjudicates no investigation item.

```json
[
  {
    "id": "NFRA_OPLGTW-Z-C-S20",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-10-03T22:55:00Z",
    "one_line": "L9 re-grade: OGO2-J1 FAIL, narrowed to 7.3. 7.1 and 7.2 now pass, but 7.3's new 'Read command' is schwab_status.py, which reads no bucket setting, under the source-bucket readback, and the section still says the runbook runs no AWS read.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Judgment criteria are graded at L9 by the CVO, never self-graded.",
    "world_is": "Graded against infra/aws/ec2/opal-gateway/runbooks/SCHWAB_PILOT_RUNBOOK.md at c1d64e9509 (equal to HEAD), on OG-o-5's J1: 'an operator can execute each section at its named moment without other context'.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/opal-gateway/runbooks/SCHWAB_PILOT_RUNBOOK.md@c1d64e9509 :250-252, :280-283, :289-307",
        "infra/aws/ec2/opal-gateway/ops/schwab_status.py: 0 matches for versioning|encryption|public_access|get_bucket; its HEALTH checks are integration_enabled, access_state_* and *_role_*"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Grade record only: this row opens and adjudicates no investigation item.",
    "grades": [
      {
        "criterion": "OGO2-J1",
        "instance": "org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~21/NFRA_OPLGTW.TO-OG-o-5.runbook-section7-remedy.proof_of_spec.json@101cfbc5f4",
        "verdict": "FAIL",
        "reason": "PASSES NOW. 7.1 (:250-252) says the template re-renders schwab at every deploy, and 7.1 is re-applied after any deploy. 7.2 step 2 (:280-283) says no target can be restored with the flag off, so 7.1 is re-applied and integration_enabled=false is confirmed before the restore counts as done. Both round-14 defects are cured, and sections 0-6 and 8 are unchanged from their PASS. FAILS AT 7.3. The section's moment is the A15 source-bucket readback (opal-data-assets versioning, encryption, the four public-access blocks, bucket policy). Its new first line (:291-292) gives 'Read command: ... python ops/schwab_status.py ... prints HEALTH.checks.integration_enabled', and that tool reads none of those settings (0 matches for versioning|encryption|public_access|get_bucket). :305-307 still say 'This runbook does not run the AWS read itself'. An operator at that moment is pointed at the wrong instrument by one line and told there is no command by another. The cause is partly this seat's: the round-14 remedy said '7.3 names the read command' without naming WHICH read. REMEDY (text only, LOCAL): move the schwab_status line to 7.1/7.2, where HEALTH is read. Then EITHER name the bucket reads in 7.3 (aws s3api get-bucket-versioning, get-bucket-encryption, get-public-access-block and get-bucket-policy-status, each with --bucket opal-data-assets, all read-only) and drop the 'does not run the AWS read' sentence, OR keep 7.3's original S9-probe wording, which was self-consistent."
      }
    ]
  }
]
```

-- 3.0.0_SA_CVO~O
