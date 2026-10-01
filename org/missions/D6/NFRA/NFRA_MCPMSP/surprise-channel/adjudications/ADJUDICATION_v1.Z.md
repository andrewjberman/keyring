# NFRA_MCPMSP -- round 1 L8 COMPILE + L9 (site Z)

Author: 3.0.0_SA_CVO~O. Round: v1. Fabric: site-z. Written: 2026-09-30T21:35Z.

Round 1 is 10 of 10 orders complete, drained @1fe1ef07b3 (1.0.0_SA_CTO~O msg 27219 / 27372). The input is 18
investigation items, 18 undispositioned, 0 armed, 0 malformed (comp-surprise --project NFRA_MCPMSP). C-S1 dismisses 11,
C-S2 graduates 7 into REMEDIATION_v1.Z (7 entries), and C-S1 also records L9 as vacuous with its cause named.
Every dismissal was re-read at HEAD, not taken from the row.

```json
[
  {
    "id": "NFRA_MCPMSP-Z-C-S1",
    "project": "NFRA_MCPMSP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-30T21:35Z",
    "one_line": "Round 1 L8: 11 of 18 rows are DISMISSED_WITH_REASON -- each was resolved inside the round, and the resolution is re-read at HEAD here, not taken from the row.",
    "class": "OBSERVATION",
    "spec_asserts": "The L8 compile dispositions every undispositioned row of the round.",
    "world_is": "comp-surprise --project NFRA_MCPMSP read 18 investigation items, 18 open, 0 armed, 0 adjudication rows, 0 malformed (watermark 0 at the drain @1fe1ef07b3). Resolved in-round, by kind: Z-S1 -- PRD v0.2 C5 option (a) @82fddba4ff (the firm role reads its own opal-data-portal-v2 prefixes). Z-W2-S1 -- a check-script literal; the trust (aws_iam_role.gw.arn) was correct before the comment, no behaviour change. Z-W2-S2 -- MS-t-2 AMENDMENT 1 names through module opal_name (@289bde0b4a); the order's status records naming gate PASS. Z-W3-S1 + Z-W1-S1 -- access_state.py:64 POLICY_RECORD_TYPES now carries tenant_firm and :70 admits tenant_firm + operator_audit in the POLICY#TENANT# partition; live since 288fa78c93. Z-W1-S2 -- the writer writes attribute 'firm' (mcportal-grant-writer-lambda/lambda_function.py:286), the one the reader reads first. Z-W1-S3 -- tests/test_access_state.py:294 now asserts POLICY 5. Z-W1-S4 -- the release carried the 12 files (the MX-r-6 v2 base diff 093fc247c6..288fa78c93 lists access_state.py and its test). Z-W1-S5 -- a test reading the repo contract at a base revision; the issuer resolved it at the release, tests are not shipped. Z-W1-S6 -- textual adjacency to another project's config block, not a dependency; the live config carries only FIRM_ROLE_ARNS from this project (measured in the MX-r-6 v2/v3 .env reads). Z-S3 -- a loud, one-command failure (terraform get), repaired on the site-Z main tree and carried to the other seats at the drain. L9 of the round is VACUOUS, with its cause named: 0 of the 10 orders carries a judgment criterion (a census of task-orders/*.md), and the thread's live hop (A1, FWD-1's conversation) is PARKED by Andrew (PRD v0.4 @7ecc812be5), so nothing this round tests whether an advisor's answer is right.",
    "adjudicates": [
      "NFRA_MCPMSP-Z-S1",
      "NFRA_MCPMSP-Z-W2-S1",
      "NFRA_MCPMSP-Z-W2-S2",
      "NFRA_MCPMSP-Z-W3-S1",
      "NFRA_MCPMSP-Z-W1-S1",
      "NFRA_MCPMSP-Z-W1-S2",
      "NFRA_MCPMSP-Z-W1-S3",
      "NFRA_MCPMSP-Z-W1-S4",
      "NFRA_MCPMSP-Z-W1-S5",
      "NFRA_MCPMSP-Z-W1-S6",
      "NFRA_MCPMSP-Z-S3"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/opal-gateway/app/access_state.py:64, :70 (HEAD)",
        "infra/aws/ec2/opal-gateway/tests/test_access_state.py:294 (HEAD)",
        "infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/lambda_function.py:262-286 (HEAD)",
        "org/missions/D6/NFRA/NFRA_MCPMSP/prd/NFRA_MCPMSP_PRD.md C5 v0.2 @82fddba4ff",
        "task-orders/*.md: 10 of 10 <status>complete, each drained with its instance VALID",
        "investigations/INVESTIGATION_v1.Z.md#NFRA_MCPMSP-Z-S1",
        "investigations/INVESTIGATION_v1.Z.md#NFRA_MCPMSP-Z-W2-S1",
        "investigations/INVESTIGATION_v1.Z.md#NFRA_MCPMSP-Z-W2-S2",
        "investigations/INVESTIGATION_v1.Z.md#NFRA_MCPMSP-Z-W3-S1",
        "investigations/INVESTIGATION_v1.Z.md#NFRA_MCPMSP-Z-W1-S1",
        "investigations/INVESTIGATION_v1.Z.md#NFRA_MCPMSP-Z-W1-S2",
        "investigations/INVESTIGATION_v1.Z.md#NFRA_MCPMSP-Z-W1-S3",
        "investigations/INVESTIGATION_v1.Z.md#NFRA_MCPMSP-Z-W1-S4",
        "investigations/INVESTIGATION_v1.Z.md#NFRA_MCPMSP-Z-W1-S5",
        "investigations/INVESTIGATION_v1.Z.md#NFRA_MCPMSP-Z-W1-S6",
        "investigations/INVESTIGATION_v1.Z.md#NFRA_MCPMSP-Z-S3"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Each row's hazard is closed by an act re-read at HEAD; none leaves a live defect."
  },
  {
    "id": "NFRA_MCPMSP-Z-C-S2",
    "project": "NFRA_MCPMSP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-30T21:35Z",
    "one_line": "Round 1 L8: 7 rows GRADUATE to REMEDIATION_v1.Z (7 remediation entries) -- each is a defect still live at HEAD or an act still owed, and five of them recur on the next release or apply.",
    "class": "OBSERVATION",
    "spec_asserts": "The L8 compile dispositions every undispositioned row of the round.",
    "world_is": "Live at HEAD or owed: the firm-bucket carrier (Z-S2); safe-apply's full-tree naming limb, unchanged since 0af3c52597 (Z-W2-S3); the grant writer's CRLF staging (Z-W3-S2); the mcportal gitlink/build pin (Z-W1-S7); the test-dirtied audit.jsonl (Z-W1-S8); the unpublished opal_ai commits and Andrew's AC2 run (Z-W4-S1/S2).",
    "adjudicates": [
      "NFRA_MCPMSP-Z-S2",
      "NFRA_MCPMSP-Z-W2-S3",
      "NFRA_MCPMSP-Z-W3-S2",
      "NFRA_MCPMSP-Z-W1-S7",
      "NFRA_MCPMSP-Z-W1-S8",
      "NFRA_MCPMSP-Z-W4-S1",
      "NFRA_MCPMSP-Z-W4-S2"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "remediations/REMEDIATION_v1.Z.md",
        "investigations/INVESTIGATION_v1.Z.md#NFRA_MCPMSP-Z-S2",
        "investigations/INVESTIGATION_v1.Z.md#NFRA_MCPMSP-Z-W2-S3",
        "investigations/INVESTIGATION_v1.Z.md#NFRA_MCPMSP-Z-W3-S2",
        "investigations/INVESTIGATION_v1.Z.md#NFRA_MCPMSP-Z-W1-S7",
        "investigations/INVESTIGATION_v1.Z.md#NFRA_MCPMSP-Z-W1-S8",
        "investigations/INVESTIGATION_v1.Z.md#NFRA_MCPMSP-Z-W4-S1",
        "investigations/INVESTIGATION_v1.Z.md#NFRA_MCPMSP-Z-W4-S2"
      ]
    },
    "disposition": "GRADUATED"
  }
]
```

-- 3.0.0_SA_CVO~O
