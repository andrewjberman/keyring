# IRPT_BCKEND -- round 19 L8/L9 adjudication

Author: 3.0.0_SA_CVO. Review 2026-09-29, 01:xxZ. Seating: org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_180xZ_SEATING_CVO.md @4cfdc2bd49.
Review: org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed).

Compile: 66 undispositioned items on the committed index (resolver .tools/surprise-row-gate.py _latest_dispositions, 23 files); 64 compiled here; S189 and S190 (workstream ~E round 1, cell TO-IB-er-201) are left for that round's L8. S191 (also ~E round 1) is dispositioned here because the row gate holds every new remediation row until a BLOCKING item is dispositioned.
36 items dismissed by the 17 rows below (C-S223..C-S239); 28 graduated OPEN in remediations/REMEDIATION_v10.md, which also writes 16 items their authors had already GRADUATED (S129..S172) as closed remediation rows.

```json
[
  {
    "id": "IRPT_BCKEND-C-S223",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-29T01:30:00Z",
    "one_line": "Directory refresh family disarmed: the dispatch no-op fix (S125) runs, the fire moved inside the host window (S126 -> S127), it ran end to end at all three firms (S128), and CLOUD now declares the moved schedule (S135).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_BCKEND-S125",
      "IRPT_BCKEND-S126",
      "IRPT_BCKEND-S127",
      "IRPT_BCKEND-S128",
      "IRPT_BCKEND-S135"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the round's slug.",
    "world_is": "Hazards disarmed by their owner and confirmed on the carrier: S128 records the 09:30 ET fire republishing all three directories (49F 09-17 -> 09-24).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "rows S127, S128 (the owner's disarm and correction)",
        "infra/aws/terraform/investor-reporting/directory/schedule.tf at CLOUD HEAD, read 2026-09-29 01:0xZ: cron(30 9 ? * MON-FRI *) and cron(15 10 ? * MON-FRI *)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Hazards disarmed by their owner and confirmed on the carrier: S128 records the 09:30 ET fire republishing all three directories (49F 09-17 -> 09-24); CLOUD schedule.tf now declares cron(30 9 ? * MON-FRI *), so an apply from CLOUD no longer reverts the fix."
  },
  {
    "id": "IRPT_BCKEND-C-S224",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-29T01:30:00Z",
    "one_line": "The builder's BUILD_MANIFEST probe (S122) is remedied on the trunk at bf938bcf39 (S123).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_BCKEND-S122",
      "IRPT_BCKEND-S123"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the round's slug.",
    "world_is": "Remedy applied and recorded by its owner.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "row S123",
        "commit bf938bcf39 (infra/aws/lambda/ci/build-and-upload.sh)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Remedy applied and recorded by its owner; the ABSENT branch is reachable in the committed bytes. Its first exercise is the next irpt-ycharts-generate build (S123's named positive control)."
  },
  {
    "id": "IRPT_BCKEND-C-S225",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-29T01:30:00Z",
    "one_line": "The WAF plan diff (S130) is a benign version-attribute diff, corrected by S133.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_BCKEND-S130",
      "IRPT_BCKEND-S133"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the round's slug.",
    "world_is": "S133 grounds that the tree declares all three rule groups (waf-cloudfront.tf:176-230) and the diff is managed_rule_group_statement.version empty-string vs null.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "row S133",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "S133 grounds that the tree declares all three rule groups (waf-cloudfront.tf:176-230) and the diff is managed_rule_group_statement.version empty-string vs null; no rule is removed; CTO msg 100972 permits the re-put."
  },
  {
    "id": "IRPT_BCKEND-C-S226",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-29T01:30:00Z",
    "one_line": "49F Performance's bucket-fence denial (S140) is disarmed by the fence edit (S142).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_BCKEND-S140",
      "IRPT_BCKEND-S142"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the round's slug.",
    "world_is": "S142 records a live signed-in 49F request answering HTTP 200 PARTIAL with a retained report after f942df9ab4.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "row S142",
        "tmp/ui-walk/20260929T000244Z shot 007 (49F account ****9079 / IRA $153,836.54 served 5.93% YTD), gitignored, md5 fa44f77fb890ef0e3dd1f26dced5078c",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "S142 records a live signed-in 49F request answering HTTP 200 PARTIAL with a retained report after f942df9ab4; this seat's walk of 2026-09-29 00:0xZ reads a 49F account served."
  },
  {
    "id": "IRPT_BCKEND-C-S227",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-29T01:30:00Z",
    "one_line": "The render host's SSM wildcard (S148) is fenced: the Deny policy is live on the role.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_BCKEND-S148"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the round's slug.",
    "world_is": "comp-find --corpus aws finds irpt-export-render-host-parameter-fence-policy inline on irpt-ycharts-runner-role (drift=DECLARED).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "comp-find --corpus aws 'irpt-export-render-host-parameter-fence' run 2026-09-29: 1 IAM_POLICY, arn:aws:iam::313476888478:role/irpt-ycharts-runner-role/inline/irpt-export-render-host-parameter-fence-policy",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "comp-find --corpus aws finds irpt-export-render-host-parameter-fence-policy inline on irpt-ycharts-runner-role (drift=DECLARED). The estate-wide class stays open as S149."
  },
  {
    "id": "IRPT_BCKEND-C-S228",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-29T01:30:00Z",
    "one_line": "The COT full-firm Holdings refusal (S131, explained in S134) is remedied: the build screens and refuses per account (S137).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_BCKEND-S131",
      "IRPT_BCKEND-S134"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the round's slug.",
    "world_is": "S137 (the Holdings producer's disposition) records holdings_snapshot.cot_screen_accounts (ce64116275, on CLOUD since de042e1e4b) refusing the account, never the firm, and the live run reproducing the accepted census and served account set exactly.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "row S137 (GRADUATED; its remediation row is written in REMEDIATION_v10, closed)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "S137 (the Holdings producer's disposition) records holdings_snapshot.cot_screen_accounts (ce64116275, on CLOUD since de042e1e4b) refusing the account, never the firm, and the live run reproducing the accepted census and served account set exactly."
  },
  {
    "id": "IRPT_BCKEND-C-S229",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-29T01:30:00Z",
    "one_line": "The retained COT report's overstated window (S157) is resolved by a corrected report (S170).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_BCKEND-S157"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the round's slug.",
    "world_is": "S170 records RPT-12b885b8 stating actual 2026-07-21..2026-09-21 with its series' first point on 07-21, made by ONE new COT use under both halves (packet 049ea241), which is S157's own path (a).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "row S170 (GRADUATED; its remediation row is written in REMEDIATION_v10, closed)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "S170 records RPT-12b885b8 stating actual 2026-07-21..2026-09-21 with its series' first point on 07-21, made by ONE new COT use under both halves (packet 049ea241), which is S157's own path (a)."
  },
  {
    "id": "IRPT_BCKEND-C-S230",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-29T01:30:00Z",
    "one_line": "Vendor-calculated Performance rows are superseded by PRD v0.19: FWD-3 no longer serves a vendor calculation for any firm.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_BCKEND-S143",
      "IRPT_BCKEND-S158",
      "IRPT_BCKEND-S185"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the round's slug.",
    "world_is": "S158's hazard was also disarmed on its own terms by S169 (the refreshed COT session made its 2 BD requests and retained a report).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_224xZ_HOLDINGS_BASED_PERFORMANCE_ALL_FIRMS_SILVER_TO_ONE_GOLD.md @0b6f598df4",
        "IRPT_BCKEND_PRD.md v0.19 ADDENDUM item 12 (no shadow path; vendor reads retire per firm)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "S158's hazard was also disarmed on its own terms by S169 (the refreshed COT session made its 2 BD requests and retained a report). Andrew-direct 0b6f598df4 moves every firm to the holdings basis; PRD v0.19 FWD-3 (@82e1700237, ratified-text signed @65f3dde719) retires the vendor-calculation rule, so INF's Orion request grammar (S143), COT's BD session for Performance (S158) and the per-use COT plan dependency (S185) are no longer on the served path. A vendor figure is only a FWD-13 comparison point."
  },
  {
    "id": "IRPT_BCKEND-C-S231",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-29T01:30:00Z",
    "one_line": "The 49F engine producer fix routed by S181 is redirected: its work becomes the 49F slice of the holdings-basis gold.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_BCKEND-S181"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the round's slug.",
    "world_is": "Andrew-direct 0b6f598df4 placement item 4: the engine-fix order is not issued against c02_twr_engine.py (TO-IB-er-191 cancelled @06d66b5893).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_224xZ_HOLDINGS_BASED_PERFORMANCE_ALL_FIRMS_SILVER_TO_ONE_GOLD.md item 4",
        "commit 06d66b5893",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Andrew-direct 0b6f598df4 placement item 4: the engine-fix order is not issued against c02_twr_engine.py (TO-IB-er-191 cancelled @06d66b5893); FWD-3's 49F slice replaces the engine read."
  },
  {
    "id": "IRPT_BCKEND-C-S232",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-29T01:30:00Z",
    "one_line": "Both R1 read-back failures are dispositioned by the CTO's ruling S188.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_BCKEND-W41-S1",
      "IRPT_BCKEND-W41-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the round's slug.",
    "world_is": "S188 (1.0.0_SA_CTO, DISMISSED_WITH_REASON) rules both into S173's canonical-classifier re-point and re-points W41-S2's BD reader to the first post-write partition.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "row S188",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "S188 (1.0.0_SA_CTO, DISMISSED_WITH_REASON) rules both into S173's canonical-classifier re-point and re-points W41-S2's BD reader to the first post-write partition; S188 carries no adjudicates field, so this row lands its ruling on the two items."
  },
  {
    "id": "IRPT_BCKEND-C-S233",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-29T01:30:00Z",
    "one_line": "The R4 holdings QA-fire failures are disarmed: after amendments 1-3 the QA fire succeeded at all three firms.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_BCKEND-W42-S1",
      "IRPT_BCKEND-W42-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the round's slug.",
    "world_is": "STATUS~M.md:65 records the QA fire SUCCESS at all three firms after the closure and grant fixes.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/STATUS~M.md:65",
        "commit dc913869d8",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "STATUS~M.md:65 records the QA fire SUCCESS at all three firms after the closure and grant fixes; ~M's round-19 close dc913869d8 reports 3/3 Success and the ENABLE half sent."
  },
  {
    "id": "IRPT_BCKEND-C-S234",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-29T01:30:00Z",
    "one_line": "Proof-of-spec instance-name rows disarmed in turn by their workers or issuers; the class is carried by W42-S4's remediation.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_BCKEND-W61-S1",
      "IRPT_BCKEND-W41-S3",
      "IRPT_BCKEND-W63-S1",
      "IRPT_BCKEND-S183"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the round's slug.",
    "world_is": "Each instance was renamed to the order's basename before its complete flip (W41-S3, W63-S1) or fixed by amendment f511608f1f (W61-S1, disposed by issuer row S183).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "rows S183, W41-S3, W63-S1 (disarmed same turn)",
        "commit f511608f1f",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Each instance was renamed to the order's basename before its complete flip (W41-S3, W63-S1) or fixed by amendment f511608f1f (W61-S1, disposed by issuer row S183). One remediation row (W42-S4) carries the recurring class to the gate owner."
  },
  {
    "id": "IRPT_BCKEND-C-S235",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-29T01:30:00Z",
    "one_line": "GATE (x)'s single-round key (S179) no longer blocks: ~M and ~Y each issued round 19 under their own workstream.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_BCKEND-S179"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the round's slug.",
    "world_is": "~M's orders (TO-IB-m19-1/2) and ~Y's issuance ecbb08548f both landed and drained.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "commit ecbb08548f (~Y issuance)",
        "commits 6ceb8c3e5a, a765ef4dc5 (~M drains)",
        "row S187 world_is",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "~M's orders (TO-IB-m19-1/2) and ~Y's issuance ecbb08548f both landed and drained; S187 records the gate keying rounds per workstream."
  },
  {
    "id": "IRPT_BCKEND-C-S236",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-29T01:30:00Z",
    "one_line": "S186 is a DUPLICATE of the NEW-01 rows S176/S177, filed by this seat in error as 'a third account'.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_BCKEND-S186"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the round's slug.",
    "world_is": "Same account and same fall to -100% on 2026-04-16 (S176/S177: bmv 13,360.59 vanishing with cf_net 0.0.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/STATUS~P.md:21,34,46",
        "tmp/ui-walk/20260929T000244Z shot 010, gitignored, md5 9820db3b70bd588b1af3fe592998afe7",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Same account and same fall to -100% on 2026-04-16 (S176/S177: bmv 13,360.59 vanishing with cf_net 0.0; about $99k held now). The page served it at 22:04Z and 00:0xZ because the retained-report reopen still serves the pre-guard figure: STATUS~P.md:34 records CRO D1 NOT MET and IB-pr-194 built but not served. Carried by S176's remediation."
  },
  {
    "id": "IRPT_BCKEND-C-S237",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-29T01:30:00Z",
    "one_line": "NEW-01's measured cause (S177) and the near-miss class the compute guard does not reach (S184) are carried by S176's remediation.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_BCKEND-S177",
      "IRPT_BCKEND-S184"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the round's slug.",
    "world_is": "S177's cause and S184's two near-misses are inputs to one remedy: serve the reopen guard now, and retire the 49F engine read when FWD-3 turns REALIZED for 49F.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "rows S176, S177, S184",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "S177's cause and S184's two near-misses are inputs to one remedy: serve the reopen guard now, and retire the 49F engine read when FWD-3 turns REALIZED for 49F."
  },
  {
    "id": "IRPT_BCKEND-C-S238",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-29T01:30:00Z",
    "one_line": "C_06's missing cash class (S138, measured in S139) is remedied in code; the served move waits on S173 as ruled in S188.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_BCKEND-S138",
      "IRPT_BCKEND-S139"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the round's slug.",
    "world_is": "The cot-cash-admission deploy admits cash (ledger cot-cash-admission-m-20260925).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "rows S188, W41-S1",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The cot-cash-admission deploy admits cash (ledger cot-cash-admission-m-20260925); its R1 read-back fails only for S173's classifier cause, which S188 rules is the one fixing act."
  },
  {
    "id": "IRPT_BCKEND-C-S239",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-29T01:30:00Z",
    "one_line": "DS~X's classification notes: S156 fixed in its cell; S153 and S154 are declared limits with the operative guard in place.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_BCKEND-S153",
      "IRPT_BCKEND-S154",
      "IRPT_BCKEND-S156"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the round's slug.",
    "world_is": "S156: commit-gate remedies applied in the cell.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "rows S153, S154, S156 (notes)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "S156: commit-gate remedies applied in the cell. S153: the operative guard sits in d08's lookup (where the $59.25M moves); the dim key-space change is a separate half for the a07 owner. S154: the frozen surfaces' under-sum is printed beside the fold, never silent. None is an IRPT_BCKEND hazard."
  }
]
```
