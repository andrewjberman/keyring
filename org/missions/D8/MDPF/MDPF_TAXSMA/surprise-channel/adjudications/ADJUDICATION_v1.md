# MDPF_TAXSMA -- L8/L9 adjudication of the channel to date (ordered by the CTO's closure plan)

<sweep_watermark>2026-10-01T02:00Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-10-01 ~08:5xZ. Trigger: 1.0.0_SA_CTO 103630 (RULINGS batch 71 @e70dab03fe, the compile order: MDPF_TAXSMA first after the IRPT grades). Review: org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_TAXSMA_CHANNEL_COMPILE_20261001.md (co-committed). 24 undispositioned rows: 11 dismissed by the five rows below. The other 13 have dispositions written and NOT landed: the row gate refuses a new remediation row while 15 of this project's 27 task orders read non-terminal at HEAD, so their rows wait, prepared, in org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_TAXSMA_REMEDIATION_v1_PREPARED_20261001.md (co-committed) and those 13 items stay undispositioned on this channel. The project is FAST (lease MDPF_TAXSMA, seat 4.0.0_SA_CRO); no JUDGMENT criterion is graded here.

```json
[
  {
    "id": "MDPF_TAXSMA-C-S1",
    "project": "MDPF_TAXSMA",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T08:50:00Z",
    "one_line": "S2, S3 and W1-S1 record that moto is absent on this box, so four Gateway test modules cannot collect here; the orders named them NOT-EVALUATED and forbade a new dependency.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_TAXSMA-S2",
      "MDPF_TAXSMA-S3",
      "MDPF_TAXSMA-W1-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "TO-TX-g-1 and TO-TX-g-2 read complete at HEAD and the Gateway route module is on CLOUD (infra/aws/ec2/opal-gateway/app/taxsma_workbook.py tracked). The four moto modules stay unrun on the laptop; the Gateway's releases are site Z's by Andrew's 2026-10-01 word (STATUS.md), where that suite belongs.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git show HEAD:<order> for TO-TX-g-1 and TO-TX-g-2 (this seat, 08:4xZ): <status>complete on both",
        "git ls-files infra/aws/ec2/opal-gateway/app/taxsma_workbook.py: 1",
        "investigation rows MDPF_TAXSMA-S2, -S3 (2.0.0_SA_COO~T) and -W1-S1 (0.9.0_WK_MDPF_TAXSMA~1)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_TAXSMA_CHANNEL_COMPILE_20261001.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An environment limit the orders stated in their own criteria; the unrun modules are named in the review as a coverage limit for the Gateway release, not as a row."
  },
  {
    "id": "MDPF_TAXSMA-C-S2",
    "project": "MDPF_TAXSMA",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T08:50:00Z",
    "one_line": "W6-S1 and W6-S4 (TX-p-1's read-only census needs a Send verb, and its one redirect is to the null device) were resolved by the issuer's amendment of AC10; the order is complete.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_TAXSMA-W6-S1",
      "MDPF_TAXSMA-W6-S4"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "TO-TX-p-1 reads complete at HEAD. Row W6-S4 itself quotes the amended criterion (condition 2: no redirect or write to a path outside the agent's working directory); the census ran one read-only command and created no file.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git show HEAD:org/missions/D8/MDPF/MDPF_TAXSMA/task-orders/MDPF_TAXSMA.TO-TX-p-1.baseline.md (this seat): <status>complete",
        "investigation rows MDPF_TAXSMA-W6-S1 and -W6-S4 (0.9.0_WK_MDPF_TAXSMA~6): the amended TXP1-AC10 text and the probe's reading of /dev/null",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_TAXSMA_CHANNEL_COMPILE_20261001.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The two criteria that could not both pass were amended by their issuer and the order drained. Reading /dev/null as the null device is accepted: it discards bytes and creates nothing."
  },
  {
    "id": "MDPF_TAXSMA-C-S3",
    "project": "MDPF_TAXSMA",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T08:50:00Z",
    "one_line": "S4 (TX-g-1's commits lived only in a worktree) and S7 (the gateway root planned four destroys from a stale tree) describe states that no longer hold: the commits are on CLOUD, and S7 is superseded by S10.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_TAXSMA-S4",
      "MDPF_TAXSMA-S7"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "f2cac74c60 is an ancestor of CLOUD HEAD and TO-TX-g-1 reads complete. Row S10 (0.0.0_AB_MSTR, 2026-10-01T01:55Z) states S7's disarm ran (the integrate at 68e15a70df, pushed), its four destroys are gone, and the hazard class is carried by S10, whose remediation row is prepared and waits on the order files (see the header).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git merge-base --is-ancestor f2cac74c60 HEAD (this seat, 08:4xZ): yes",
        "investigation row MDPF_TAXSMA-S10: 'S7 is superseded by this row, not closed'",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_TAXSMA_REMEDIATION_v1_PREPARED_20261001.md row MDPF_TAXSMA-S10 (co-committed, not yet on the channel)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_TAXSMA_CHANNEL_COMPILE_20261001.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "S4's state is corrected in git. S7 was BLOCKING and ARMED on a stale tree that has since been integrated; what remains of it is S10's and is carried there."
  },
  {
    "id": "MDPF_TAXSMA-C-S4",
    "project": "MDPF_TAXSMA",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T08:50:00Z",
    "one_line": "W6-S3 (the publisher's commit stamp named a build it was not) and S8 (the Tax control write could never have landed) are repaired in the world, read today.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_TAXSMA-W6-S3",
      "MDPF_TAXSMA-S8"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The live publisher's MDPF_PUBLISHER_COMMIT reads e8994f23af282296037bd28bb539ac55cc9465dd, the pin both deployed packages were built from. The control write is covered by tests that read which bucket receives it, that a changed body overwrites, and that a disabled prelude runs no stage; the suite reads 227 passed at CLOUD HEAD and the test file is present at the deployed pin.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "lambda get-function-configuration opal-assets-mdpf-portal-publisher (this seat, 08:4xZ): MDPF_PUBLISHER_COMMIT e8994f23af...; CodeSha256 pj+Jat96..., LastModified 2026-10-01T02:21:34Z",
        "data/mdpf/tests/taxsma/test_taxsma_scoped_access.py:36,48 (test_control_goes_to_its_builder_address_and_overwrites, test_control_is_not_in_a_firm_bucket) and test_taxsma_consolidator.py:388 (test_none_gateway_call_returns_disabled_with_no_stage_run) at HEAD; git cat-file -e e8994f23af:<the first file>: present",
        "py -3.12 -m pytest data/mdpf/tests/taxsma (this seat, 06:3xZ): 227 passed",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_TAXSMA_FAST_PIN_GRADES_20261001.md @bc8413dbd8"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Both defects were found and repaired inside the lane before anything served Tax; the stamp was re-read live and the control write is under three tests. The control write has never run for real (Tax is DISABLED); that exercise is TX-r-3's."
  },
  {
    "id": "MDPF_TAXSMA-C-S5",
    "project": "MDPF_TAXSMA",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T08:50:00Z",
    "one_line": "W1-S3 (one Gateway lag-bar test fails intermittently before the edit) and W2-S1 (four rollup levels read as one arithmetic identity, with a fifth field added to make it checkable) are records of how two criteria were read; neither names a hazard.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_TAXSMA-W1-S3",
      "MDPF_TAXSMA-W2-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The lag-bar test was counted as failing before the edit and left ungraded, which is the conservative reading. The identity W2-S1 describes has since been exercised on real served spines by the lane: STATUS.md records 49 Financial at 1,761,000,294.98 on the timeseries, the category tree and aum-metrics alike (held, not re-run by this seat).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows MDPF_TAXSMA-W1-S3 (0.9.0_WK_MDPF_TAXSMA~1) and -W2-S1 (0.9.0_WK_MDPF_TAXSMA~2)",
        "org/missions/D8/MDPF/MDPF_TAXSMA/STATUS.md acceptance row E2b (held)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_TAXSMA_CHANNEL_COMPILE_20261001.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Interpretation records with a conservative reading taken in each; no artifact is at risk."
  }
]
```
