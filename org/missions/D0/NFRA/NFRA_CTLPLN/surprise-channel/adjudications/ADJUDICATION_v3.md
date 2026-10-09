# NFRA_CTLPLN: CVO adjudication -- the 35 BLOCKING/ARMED items of the other workstreams (dismissals)

L8 compile by `3.0.0_SA_CVO`, on 1.0.0_SA_CTO msg 107476 ("you compile the 35 undispositioned BLOCKING/ARMED NFRA_CTLPLN items now
... No audited override for the 10").

**Denominator.** The row gate's own resolver (`.tools/surprise-row-gate.py` `_latest_dispositions` and `_gating_item_ids`) was run
over the index at HEAD 6729c4b1bf. The channel holds 207 items, 186 of them undispositioned. 40 of those are BLOCKING or ARMED:
- 35 belong to workstreams other than INBOUND, and are compiled here;
- 5 are INBOUND rows whose graduation ADJUDICATION_v2.md held (S33, S34, W31-S4, W31-S5, W36-S2).

The other 146 undispositioned items are OBSERVATION/INERT. They gate no slug and are not dispositioned here.

**This version carries the 27 DISMISSED of the 35:**
- 10 because the hazard is gone in code at HEAD (C-S5);
- 11 because a later order, amendment or apply overtook them (C-S6);
- 6 because the CTO's and Andrew's rulings widening the Dell grants overtook them (C-S7).

**Not in this version.** The other 8 of the 35 are to GRADUATE (C-S8), and INBOUND's 10 held graduations land under C-S4. Both,
with their remediation rows, land in one later commit. The row gate refuses any new remediation row while an NFRA_CTLPLN task
order reads non-terminal (TO-APPLY-20 dell2 shell window, pending; TO-DELL-1, see row S37).

<sweep_watermark>2026-10-08T23:45Z</sweep_watermark>

```json
[
  {
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-08T23:45Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "id": "NFRA_CTLPLN-C-S5",
    "one_line": "Ten items whose hazard is gone in the code at HEAD, read by this seat: the Dell id grammar in every reader, the fabric enum, the halt gate's lane rule, the agentbus queue size, sender check and refused-mail path, and the fence census self-test.",
    "spec_asserts": "Each row names a defect in a file at its filing; the defect is gone when the file at HEAD no longer carries it.",
    "world_is": "W9-S1, W9-S2: both row schemas carry fabric ['laptop','site-z','dell1','dell2'] and an id, adjudicates and disarms pattern that admits a D1-/D2- infix. W9-S3: .tools/proof-of-spec-check.py:1206 SURPRISE_ID_RE and org/surprise_channel/surprise-watch.sh:85 ID_RE admit the Dell infix. W9-S4: infra/aws/lambda/investor-reporting/ycharts/research/file_stop_row.py:13 carries the schema's grammar. W5-S1: the gate no longer derives fabric from a Z- infix (no id_fabric assignment) and org/standards/PRD_HEADER.schema.json carries the four fabrics; the D2-S1 row itself was admitted. Z-S1: .tools/halt-gate-check.sh:219-222 names its refusal reason under CTO_RULING_HALT_GATE_MULTI_LETTER_LANE_20261007.md. W3-S1: the queue root moved to provider ~> 6.0 (221ee5b0b6), which takes max_message_size 1048576. W3-S2 and W3-S3: .tools/agentbus-consumer.py:73-82 checks the sender's tailnet name against the device register, records a refused message and deletes it so it cannot block the FIFO group. W6-S15: dell_fence_census.py --selftest prints 'FENCE-CENSUS-SELFTEST cases=7/7 ok=True' (248277c024).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "read by this seat at HEAD 6729c4b1bf: org/surprise_channel/schemas/investigation_item.schema.json and remediation_row.schema.json properties fabric, id, adjudicates, disarms",
        ".tools/proof-of-spec-check.py:1206; org/surprise_channel/surprise-watch.sh:85; infra/aws/lambda/investor-reporting/ycharts/research/file_stop_row.py:13",
        ".tools/halt-gate-check.sh:219-222; org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_HALT_GATE_MULTI_LETTER_LANE_20261007.md",
        "git log infra/aws/terraform/nfra-ctlpln-agentbus: 221ee5b0b6 'amendment 2 -- provider ~> 6.0 (6.67.0), refused mail recorded and deleted'; .tools/agentbus-consumer.py:73-82",
        "run by this seat: timeout 120 python infra/aws/terraform/shared-infra/tests/dell_fence_census.py --selftest -> 'FENCE-CENSUS-SELFTEST cases=7/7 ok=True'"
      ]
    },
    "adjudicates": [
      "NFRA_CTLPLN-W9-S1",
      "NFRA_CTLPLN-W9-S2",
      "NFRA_CTLPLN-W9-S3",
      "NFRA_CTLPLN-W9-S4",
      "NFRA_CTLPLN-W5-S1",
      "NFRA_CTLPLN-Z-S1",
      "NFRA_CTLPLN-W3-S1",
      "NFRA_CTLPLN-W3-S2",
      "NFRA_CTLPLN-W3-S3",
      "NFRA_CTLPLN-W6-S15"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The hazard each row names is gone in the file at HEAD, read or run by this seat. No remedy is owed."
  },
  {
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-08T23:45Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "id": "NFRA_CTLPLN-C-S6",
    "one_line": "Eleven items overtaken by a later order, amendment or apply: a stopped apply re-signed and applied, criteria the issuer amended, a decomp citation corrected, a grant cut by ruling, and orders now complete.",
    "spec_asserts": "Each row records a criterion, citation or plan shape that could not hold as written at its filing.",
    "world_is": "S25: TO-APPLY-11 stopped on a 7-resource plan; the resource-policy ALLOW it refused was later signed by both halves and applied as its own pair (TO-APPLY-13, complete). S30: TO-APPLY-12 and TO-APPLY-13 now cite NFRA_CTLPLN_DECOMP.access1.md. W14-S1: dell2_ssm_policy.json now grants ssm:SendCommand on the resident host and named documents (SendResidentDocumentsToResidentHost), applied by TO-APPLY-18 on a ruling. W14-S3: the routes Deny is rendered through modules/routes_policy and TO-CT-a-1 is complete. W14-S9, W14-S10, W14-S19: the issuer amended CTa1-AC2 and CTa1-AC5 (AMENDMENT 16 names W14-S19 as resolved, expect dell_write_refused=8/10) and TO-CT-a-1 is complete. W10-S1: TO-CT-d-7 complete. W4-S10: TO-CT-c-5 complete and protected_functions.json is committed. W6-S13: TO-CT-e-3 complete. S13: TO-CT-k-2 ran AMENDMENT 5 (the bun egress disarm measured against a loopback listener, the control CTO msg 106214 set) and is complete through AMENDMENT 8.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "status lines read by this seat at HEAD 6729c4b1bf: TO-CT-a-1, TO-CT-c-5, TO-CT-d-7, TO-CT-e-3, TO-CT-k-2 'complete'; org/tier2_senior/0.7.0_AE_CloudOps~E/task_orders/NFRA_CTLPLN.TO-APPLY-11/-12/-13 'complete'",
        "<decomp_doc> of TO-APPLY-12 and TO-APPLY-13: org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.access1.md",
        "infra/aws/terraform/nfra-ctlpln-identity/dell2_ssm_policy.json statement SendResidentDocumentsToResidentHost",
        "org/missions/D0/NFRA/NFRA_CTLPLN/task-orders/NFRA_CTLPLN.TO-CT-a-1.dell2-sendcommand-grant.md:956-968 (AMENDMENT 16, row W14-S19)",
        "org/missions/D0/NFRA/NFRA_CTLPLN/task-orders/NFRA_CTLPLN.TO-CT-k-2.dell-python-kit.md, AMENDMENT 5 heading and authority (msg 106214)"
      ]
    },
    "adjudicates": [
      "NFRA_CTLPLN-S25",
      "NFRA_CTLPLN-S30",
      "NFRA_CTLPLN-W14-S1",
      "NFRA_CTLPLN-W14-S3",
      "NFRA_CTLPLN-W14-S9",
      "NFRA_CTLPLN-W14-S10",
      "NFRA_CTLPLN-W14-S19",
      "NFRA_CTLPLN-W10-S1",
      "NFRA_CTLPLN-W4-S10",
      "NFRA_CTLPLN-W6-S13",
      "NFRA_CTLPLN-S13"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A later order, amendment or signed apply overtook each row; the orders are complete. No remedy is owed."
  },
  {
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-08T23:45Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "id": "NFRA_CTLPLN-C-S7",
    "one_line": "Six items overtaken by the rulings that widened the Dell grants: PassRole is now allowed, 72 resource-policy actions are allowed by the signed ALLOW, and Andrew named the protected functions and the audit trail with its bucket.",
    "spec_asserts": "Each row warns that a Dell can reach an access-granting act the order of its day meant to leave unallowed, or cannot pass a role.",
    "world_is": "W1-S1: dell_iam_roles_policy.json AllowPassAnyRole allows iam:PassRole on *; the simulation reads PassRole allowed for lambda and ec2. W4-S1, W4-S2, W8-S2: dell_respol_policy.json puts 72 of 75 resource-policy actions in the ALLOW, sqs/sns AddPermission, sqs:SetQueueAttributes, s3:PutBucketPolicy and kms:PutKeyPolicy among them, signed and applied (TO-APPLY-13), so access-granting by attribute, at create time or by an API Gateway resource policy is the same class the rulings allow. Treating the apigateway residual (UNSURE) as part of that class is this seat's reading. W14-S15, W14-S16: Andrew-direct 2026-10-08 ~13:2xZ 'WIDEN THE TWO GRANTS, YES' names 'the portal's protected functions' and 'the audit trail and its bucket'; this seat's simulation reads PROTECTED-ADDPERMISSION allowed 10 of 10 per user, as AMENDMENT 16 item 4 expects, and the audit bucket's policy and ACL actions UNDO-FREED.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "run by this seat at HEAD: timeout 300 python infra/aws/terraform/nfra-ctlpln-identity/tests/simulate_policy.py (rc 0; read-only IAM simulation): 'PASSROLE-ALLOWED-EXPECTED iam:PassRole ... -> allowed', 'CANUNDO-ii PROTECTED-ADDPERMISSION functions=10 allowed: dell1=10 dell2=10 (AMENDMENT 16 item 4 expects 10 of 10)', 'UNDO-FREED audit-trail bucket ... s3:PutBucketPolicy ... allowed', last line 'POLICY-SIM allowed_ok=22/22 denied_ok=15/15 passrole_ok=5/5 ... freed_allowed=72/72'",
        "infra/aws/terraform/nfra-ctlpln-identity/dell_iam_roles_policy.json statement AllowPassAnyRole; dell_respol_policy.json summary 'total 75, in_allow 72, excluded 3'",
        "org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_132xZ_TEN_ANSWERS_LIFT_ITEMS_5_AND_4_WIDEN_BOTH_GRANTS_DELL2_RETRIES_DELL1_INSTALLS.md row 3 (quoted in TO-CT-a-1 AMENDMENT 16, lines 889-895)"
      ]
    },
    "adjudicates": [
      "NFRA_CTLPLN-W1-S1",
      "NFRA_CTLPLN-W4-S1",
      "NFRA_CTLPLN-W4-S2",
      "NFRA_CTLPLN-W8-S2",
      "NFRA_CTLPLN-W14-S15",
      "NFRA_CTLPLN-W14-S16"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The access each row warns of is now granted by a ruling (PassRole, the signed resource-policy ALLOW, Andrew's widening of the two grants). The hazard is a decision taken, not an open defect. No remedy is owed."
  }
]
```
