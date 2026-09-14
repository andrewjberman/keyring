# ADVI_FIRMBKTS: CVO adjudication

Pre-issuance intake by `3.0.0_SA_CVO`. The rows are from card3-read-logging and the lane that ran it, and ADVI_FIRMBKTS
has no issued round (its PRD was admitted at v1.2 @4289847ccf), so this is NOT an L8 compile. Each row below was read
against the artifact that closes it, or re-measured, before it was dispositioned.

```json
[
  {
    "id": "ADVI_FIRMBKTS-C-S1",
    "project": "ADVI_FIRMBKTS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-14T12:05:00Z",
    "one_line": "PRE-ISSUANCE INTAKE: four rows CLOSED or superseded -- this seat's own re-measure (S3, superseded by C-S2), a positive control that had to be driven (S4), a selector that records minutes after it applies (S5), and the send guard's code-less order (S6, remedied on Andrew's call 3).",
    "class": "OBSERVATION",
    "spec_asserts": "Each row names what would close it: S2's exposure re-measured (S3), a control that discriminates (S4), recording that begins when the selector is applied (S5), and a guard that admits a code-less order (S6).",
    "world_is": "S3: superseded by ADVI_FIRMBKTS-C-S2's re-measure at 12:01:37Z. S4: R-AC8 passed on a read the order did not name. That read (one 1-byte GetObject on opal-data-bd at T0, principal user/Andrew_Berman) is listed as a probe to exclude from the 45-day census, and the row states the rule for re-use: drive the positive arm. S5: recording began about 16 minutes after PutEventSelectors on cot and about 25 on 49financial. This supports 1.0.0_SA_CTO's clock ruling (96424, live means observed recording), which ADVI_FIRMBKTS v1.2's decommission row carries: 'no earlier than that instrument's observed-live stamp'. S6: remedied at ee9a6cf257 on Andrew-direct ~04:xxZ call 3 (@675eeec895). The row's own dismissal stands, and this row carries it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md rows S3-S6",
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/prd/ADVI_FIRMBKTS_PRD.md@4289847ccf CONTRACTS row 'the decommission standard'",
        "org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260914_04xxZ_COOE_OPEN_CALLS_RECS_APPROVED_NEXT_STEPS_APPROVED_LANE_CLOSE_MANUAL.md@675eeec895 call 3"
      ]
    },
    "adjudicates": [
      "ADVI_FIRMBKTS-S3",
      "ADVI_FIRMBKTS-S4",
      "ADVI_FIRMBKTS-S5",
      "ADVI_FIRMBKTS-S6"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "S3 is superseded by a later re-measure. S4 and S5 passed their criteria, and each carries its lesson into the census rule the admitted PRD already states (a probe read excluded; the clock starts at observed recording). S6 was remedied at ee9a6cf257 on Andrew's call 3.",
    "hazard_standing": "INERT"
  },
  {
    "id": "ADVI_FIRMBKTS-C-S2",
    "project": "ADVI_FIRMBKTS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-14T12:05:00Z",
    "one_line": "PRE-ISSUANCE INTAKE, GRADUATED to 1.0.0_SA_CTO, STILL ARMED: S2's worktree exposure has grown, not shrunk. 24 of 33 linked worktrees carry shared-infra at a HEAD without the org-trail config (22 at 00:44Z), so a full shared-infra apply from any of them plans the organisation trail's DESTROY. Andrew's calls: removal only after a same-act re-measure, and no destroy gate.",
    "class": "OBSERVATION",
    "spec_asserts": "S2: the exposure disarms when every checkout carries 9f3fd2cf4a -- the CLOUD push, the CLOUD->SITEZ merge, and this device's older linked worktrees taking CLOUD or being removed.",
    "world_is": "Re-measured 2026-09-14T12:01:37Z with git worktree list. The positive control, the main tree at 62b5c0819f, contains 9f3fd2cf4a. Of 33 linked worktrees (0 with missing directories), 24 carry infra/aws/terraform/shared-infra at a HEAD that lacks it, and 1 more lacks it without shared-infra. The growth since S3 (22 at 00:44Z) is worktrees cut from CLOUD before the config landed that were still standing, among them C:/tmp/wk-irpt_fntend-5-4-fe-s-29 (6ad371c88e) and three DSGN slots. The origin half closed at 00:44Z (S3), and SITEZ is not in this clone. Andrew-direct ~04:xxZ (@675eeec895): call 1 YES, but remove only a worktree that passes a same-act re-measure (tip an ancestor of CLOUD, 0 tracked changes, untracked listed), and skip any its owner holds; call 2 NO, no safe-apply refusal of a trail destroy is built. The round-5 IRPT worktrees stand on the operator's instruction (96556). So the exposure is live, and nothing refuses it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git worktree list --porcelain and git merge-base --is-ancestor 9f3fd2cf4a <HEAD> per worktree, run 2026-09-14T12:01:37Z; main tree 62b5c0819f CONTAINS (positive control)",
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md rows S2 and S3",
        "org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260914_04xxZ_COOE_OPEN_CALLS_RECS_APPROVED_NEXT_STEPS_APPROVED_LANE_CLOSE_MANUAL.md@675eeec895 calls 1 and 2"
      ]
    },
    "adjudicates": [
      "ADVI_FIRMBKTS-S2"
    ],
    "disposition": "GRADUATED",
    "hazard_standing": "ARMED",
    "disarm_owner": "Unchanged from S2: 0.0.0_AB_MSTR for the CLOUD->SITEZ leg, and each worktree's owner for taking CLOUD, or for removal under Andrew's call 1 (same-act re-measure, held worktrees skipped, a human OK for removal). 1.0.0_SA_CTO is told so the ADVI_FIRMBKTS decomposition does not plan a shared-infra apply from a stale checkout."
  },
  {
    "id": "ADVI_FIRMBKTS-C-S3",
    "project": "ADVI_FIRMBKTS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-14T12:05:00Z",
    "one_line": "PRE-ISSUANCE INTAKE, GRADUATED to 1.0.0_SA_CTO: four tooling residuals the card-3 act left -- portal-auth's unapplied WAF plan diff (S1), a ledger tool that overwrites hand notes (S7), a /cloud-ops tool that does not exist (S8), and an AWS corpus with no CloudTrail node (S9).",
    "class": "OBSERVATION",
    "spec_asserts": "A closed deploy leaves no unowned residual: the plan it stepped around, the tools its discipline names, and the corpus that should have shown its drift each have an owner.",
    "world_is": "S1: route (a) was taken (@56941e3366). portal-auth was applied TARGETED at the FIRMSEP rule, and the ledger closed 5 of 5 legs at 20260914T012943Z (20260913T2326Z_card3-read-logging_deploy_completion.md @50823af561). The WAF ACL opal-cloudfront-protection's planned remove-and-re-add was never applied, and was not re-measured here, so the next full portal-auth apply meets it on the production front door. S7: deploy_ledger.py close-leg and close re-render the entry, and hand notes are lost; that same ledger records its notes being dropped (:33). S8: /cloud-ops names .tools/record-terraform-deploy.sh, which is absent, so no CHANGELOG.json was updated. S9: comp-find --corpus aws carries no CloudTrail trail node, so the trail's CLI-applied drift was invisible to it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/critical_paths/change_management/20260913T2326Z_card3-read-logging_deploy_completion.md@50823af561 :3, :16-29, :33, :50-53",
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md rows S1, S7, S8, S9"
      ]
    },
    "adjudicates": [
      "ADVI_FIRMBKTS-S1",
      "ADVI_FIRMBKTS-S7",
      "ADVI_FIRMBKTS-S8",
      "ADVI_FIRMBKTS-S9"
    ],
    "disposition": "GRADUATED",
    "hazard_standing": "INERT"
  }
]
```
