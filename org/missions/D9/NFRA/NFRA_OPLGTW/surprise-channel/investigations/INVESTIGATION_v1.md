# NFRA_OPLGTW -- surprise channel, INVESTIGATION v1

**Opened by:** `2.0.0_SA_COO~O` at L6, 2026-09-15. **Home:** the project tree's channel. Lane `ANY`; the gate
`.tools/surprise-row-gate.py` validates every NEW row (schema, identity, coordinate, folder == project). **Append-only.**
Worker rows carry their slot's coordinate, `NFRA_OPLGTW-W<n>-S<k>`; a seat's row carries none.

**Why this file is opened at the issuance.** The first row was found while grounding the task orders' test criteria: the
Gateway's existing test suite does not pass at the cut base, so every "whole suite passes" criterion of this round has to
name the one known failure instead of silently inheriting it.

**Denominator at this write: 1 row** -- `NFRA_OPLGTW-S1`, 2.0.0_SA_COO~O at L6.

```json
[
  {
    "id": "NFRA_OPLGTW-S1",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-15T09:10Z",
    "one_line": "The Gateway's own suite fails one test at the cut base: test_scoped_deny_by_default still lists opal_data_refresh_upload as denied to the Bloomberg service identity, while the tracked allowlist overlay grants that identity that tool.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "TEST: infra/aws/ec2/opal-gateway/tests/test_identity_scope.py:32-51 @7921d898c0 -- _FRAME_III_DENIED includes 'opal_data_refresh_upload', and test_scoped_deny_by_default asserts identity_scope.check('opalbloomberg@opalinvest.com', tool) is not None for every member.",
        "OVERLAY: infra/aws/ec2/opal-gateway/identity_tool_allowlist.txt:13 @7921d898c0 reads 'opalbloomberg@opalinvest.com opal_data_refresh_upload'; the test module's own AC-D says the overlay widens the named identity, and infra/aws/ec2/opal-gateway/deploy-to-ec2.sh:134 carries the grant's rationale, so the grant reads as deliberate.",
        "RUN: Python 3.12.10, pytest 9.0.2, 'python -m pytest tests -q -p no:cacheprovider' from infra/aws/ec2/opal-gateway at 2026-09-15 09:03Z: '1 failed, 76 passed, 34 subtests passed'; FAILED tests/test_identity_scope.py::test_scoped_deny_by_default -- AssertionError: opal_data_refresh_upload."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The round's cut would have said 'the whole infra/aws/ec2/opal-gateway/tests suite passes' as a criterion on every Gateway code cell, which assumes the suite is green at the base the workers branch from.",
    "world_is": "The suite is red at the base on one test that predates this project and belongs to the opal_portal integration's grant, not to any NFRA_OPLGTW cell. Every suite criterion in this issuance therefore deselects exactly that test by name (-k 'not test_scoped_deny_by_default') and cites this row; no worker edits the test or the overlay.",
    "notes": "INERT: the failure does not change the Gateway's runtime behaviour, which follows the overlay. OBSERVATION: it blocks nothing in this round, because the criteria name it. Whether the test or the overlay is the one to change is the owner of the opal_portal integration's grant to decide; it is outside this project's write surface."
  },
  {
    "id": "NFRA_OPLGTW-W1-S1",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~1",
    "surfaced_at": "2026-09-15T10:44Z",
    "one_line": "OG-i-1's plan of the opal-gateway root reads 4 to add, 2 to change, 0 to destroy: the two change rows are in-place '+ description' backfills on the existing aws_wafv2_ip_set.opal_blocked_ips_regional_v4 and _v6, so the order's own blast-radius bound refuses the apply.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "PLAN: .tools/terraform.exe v1.9.8 'plan -input=false -out' on infra/aws/terraform/opal-gateway at worktree base 417631ae6f, 2026-09-15T10:42:25Z..10:42:38Z, rc 0: 'Plan: 4 to add, 2 to change, 0 to destroy.' -- 71 resource_changes = 65 no-op + 4 create (this cell's four) + 2 update; redacted plan JSON at org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/og_i1.plan.json.",
        "DIFF: each update changes exactly one attribute, description, absent live and declared in waf.tf ('+ description = NFRA_OPSEC202609 C-2: addresses blocked at the ALB. Written ONLY by the OP-s-15 reconciler ...'); addresses is not in the diff because of lifecycle ignore_changes = [addresses] at infra/aws/terraform/opal-gateway/waf.tf:294-296 and :335-337 @417631ae6f.",
        "PRIOR RECORD: commit 3758b14afc (2026-09-04, 0.7.0_AE_CloudOps~T) says in its message 'THE ONLY REMAINING DIFF ON ALL FOUR SETS IS + description, a backfill of a field absent on the live resource -- benign'; the declared strings date from 37c4bde812 (waf.tf:261 and :271), so this diff has stood on the root since then.",
        "BOUND: org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-i-1.access-state-table.md @417631ae6f BOUNDS 'Blast radius': 'A plan that shows any change or destroy is refused: a BLOCKING row, no apply.', and 'Terraform': 'never -target'. CLOUD @496a89e4b5 carries no change under infra/aws/terraform/opal-gateway/ against the base (git diff --stat empty)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The order and the decomposition (OG-i-1 acceptance, first bullet, decomposition @8768f46770 line 178) assume a plan of the opal-gateway root that creates only this cell's four resources and changes nothing that exists.",
    "world_is": "Every plan of this root also carries two in-place description backfills on the Gateway's regional blocked-IP sets, which NFRA_OPSEC202609 owns. With -target forbidden and the bound literal, no apply of this cell is admissible: no ledger entry was opened, nothing was applied, and OGI1-AC2..AC9 have no applied object to read. The branch wk-nfra_oplgtw-1-1 carries infra/aws/terraform/opal-gateway/schwab_access_state.tf DECLARED and NOT APPLIED, so any later apply of this root from a tree that holds it (a drain to CLOUD included) would create the table and both grants outside this order's ledger.",
    "notes": "INERT: nothing moved in AWS. Form only, not significance: the diff leaves this cell's plan by one of two acts, neither this worker's -- the order's author names the two description backfills as admitted changes in the bound, or the IP sets' owner applies the backfill under its own ledger so the root plans with no change to existing resources. The probe's OGI1-AC1 arm reads the saved plan and prints both NOT-CREATE rows."
  },
  {
    "id": "NFRA_OPLGTW-W1-S2",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~1",
    "surfaced_at": "2026-09-15T10:55Z",
    "one_line": "The order runs OGI1-AC8, the operator revision race, 'through SSM on i-07dccb1615503ac99 with the instance's own role', but that role is the RUNTIME principal, which by the same order cannot write POLICY# keys; the race can run only under the separate operator role.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ORDER: NFRA_OPLGTW.TO-OG-i-1 @417631ae6f lines 48-49: 'The on-host arms (AC7, AC8) run through SSM on i-07dccb1615503ac99 with the instance's own role'; OGI1-AC6 and OGI1-AC8 name the operator principal and two concurrent operator revisions of one POLICY# record.",
        "PRD: org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md:193 @f0aa50dbc0: 'The operator role alone may conditionally update POLICY records' and runtime writes are 'conditioned through dynamodb:LeadingKeys to the RUNTIME prefix only'.",
        "LIVE: ec2 describe-instances i-07dccb1615503ac99 at 2026-09-15 ~10:36Z: running, IamInstanceProfile arn:aws:iam::313476888478:instance-profile/opal-gateway-profile, whose role is opal-gateway-role (infra/aws/terraform/opal-gateway/main.tf:160-163 @417631ae6f)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "OGI1-AC7 and OGI1-AC8 are both on-host arms run with the Gateway instance's own role.",
    "world_is": "Only OGI1-AC7 can be. The probe's AC8 arm assumes opal-gateway-access-admin from the checkout's operator identity (arn:aws:iam::313476888478:user/Andrew_Berman) and races two conditional UpdateItem calls (ConditionExpression revision = 1) released by one barrier. Running it on the host would require the operator role to trust opal-gateway-role, which schwab_access_state.tf refuses by aws:PrincipalArn and OGI1-AC6 grades as separation.",
    "notes": "INERT: the arm was not exercised in this run, because W1-S1 blocks the apply. The race uses single-item conditional UpdateItem rather than TransactWriteItems because two concurrent transactions on one item can be cancelled with TransactionConflict rather than ConditionalCheckFailed; the operator's one-transaction update-plus-audit is exercised separately in the AC6 arm."
  },
  {
    "id": "NFRA_OPLGTW-W1-S3",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~1",
    "surfaced_at": "2026-09-15T10:52Z",
    "one_line": "The PRD and OGI1-AC5 grant and grade 'TransactWrite' as a runtime action, but dynamodb:TransactWriteItems is not an IAM action: AWS Access Analyzer returns INVALID_ACTION for it, and a transaction is authorized per item against PutItem and UpdateItem.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "LIVE: aws accessanalyzer validate-policy --policy-type IDENTITY_POLICY, us-east-1, account 313476888478, one Allow on the table ARN: dynamodb:TransactWriteItems at 2026-09-15T10:52:10Z -> 'ERROR INVALID_ACTION The action dynamodb:TransactWriteItems does not exist.'; positive control dynamodb:PutItem at 10:52:13Z -> no finding; dynamodb:TransactGetItems at 10:52:16Z -> 'ERROR INVALID_ACTION The action dynamodb:TransactGetItems does not exist.'",
        "SPEC: org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md:189 @f0aa50dbc0 'limited to needed Get/Put/Update/TransactWrite operations' and :193 'all transaction items must satisfy the restriction'; OGI1-AC5 in NFRA_OPLGTW.TO-OG-i-1 @417631ae6f."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The runtime grant allows Get, Put, Update and TransactWrite on the table, as four grantable operations.",
    "world_is": "A policy naming dynamodb:TransactWriteItems would carry an action that grants nothing. schwab_access_state.tf grants GetItem, and PutItem and UpdateItem under ForAllValues:StringLike dynamodb:LeadingKeys RUNTIME#* with Null dynamodb:LeadingKeys false -- the same condition that binds every item of a TransactWriteItems call. The probe's AC5 arm grades TransactWrite on those constituents, and its AC7 arm exercises a mixed RUNTIME# plus POLICY# transaction as a supplementary line.",
    "notes": "INERT: no grant was applied (W1-S1). The same holds for a later cell that wants transactional reads: TransactGetItems is authorized against GetItem."
  }
]
```
