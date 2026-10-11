# NFRA_GATSCP -- round 4 L8/L9 adjudication (dell1)

<sweep_watermark>2026-10-09T17:53Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-09T17:53:00Z. L8: 2.0.0_SA_COO~N1 msg 2911, `org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/TRACE_round4.md @4132c3e933`. 4 of 4 terminal, every criterion re-run by this seat.
**FWD-8 MET** (row D1-C-S26). 2 rows swept: D1-W14-S1 and D1-S15 dismissed. In place: REMEDIATION_v2 D1-S7 and REMEDIATION_v3 D1-W13-S1 REMEDIATED.

```json
[
  {
    "id": "NFRA_GATSCP-D1-C-S26",
    "project": "NFRA_GATSCP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T17:53:00Z",
    "one_line": "FWD-8 MET (PRD v0.4 @a33d3bde72, as ruled (A) in ROUND_ANALYSIS.round3 ADDENDUM 1): the census's 26 owned-paths refusals are replayed at measured grain -- 19 OWN-PATH, each tied to the author's own commit that writes a blocked path (true refusals); 5 OTHER-ACT, where the paired OVERRIDE served a different commit carrying none of the BLOCK's paths (a census pairing artifact, not a wrongful refusal); 2 UNATTRIBUTED, not counted either way. No attributed refusal names a path its act did not write. The 4 pipeline-gate entries were duplicate log lines; nothing was refused. Negative arm: a planted commit writing outside its seat's paths is still stopped by the real hook. Every audit line now carries the act key and the full path list (128 such lines live, incl. the 16:46:37Z PASS act=d346d21fbd3e for TRACE_round4.md). The week of ordinary work remains the second arm, read at the next census, now act-keyed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "NFRA_GATSCP_PRD.md v0.4 FWD-8; spine L9: graded by a seat that did none of the work.",
    "world_is": "FWD-8 MET (PRD v0.4 @a33d3bde72, as ruled (A) in ROUND_ANALYSIS.round3 ADDENDUM 1): the census's 26 owned-paths refusals are replayed at measured grain -- 19 OWN-PATH, each tied to the author's own commit that writes a blocked path (true refusals); 5 OTHER-ACT, where the paired OVERRIDE served a different commit carrying none of the BLOCK's paths (a census pairing artifact, not a wrongful refusal); 2 UNATTRIBUTED, not counted either way. No attributed refusal names a path its act did not write. The 4 pipeline-gate entries were duplicate log lines; nothing was refused. Negative arm: a planted commit writing outside its seat's paths is still stopped by the real hook. Every audit line now carries the act key and the full path list (128 such lines live, incl. the 16:46:37Z PASS act=d346d21fbd3e for TRACE_round4.md). The week of ordinary work remains the second arm, read at the next census, now act-keyed.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO ran org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/round4_prep/checks/r4_replay.py: GS-H1-REPLAY ok=True arms=3 failed=0, counts OWN-PATH 19 / OTHER-ACT 5 / UNATTRIBUTED 2 (arm 2 re-measures every OWN-PATH tie against git)",
        "3.0.0_SA_CVO ran r4_actkey.py: arm 1 planted outside-paths act (own deliverable + org/tier0/ledger/LD-0001.md) rc=1 BLOCK act=cf558ecf59ff paths=2; arm 2 OVERRIDE same key; arm 3 own path alone rc=0, different key -> GS-H2-ACTKEY ok=True arms=3",
        "3.0.0_SA_CVO ran r4_reset_both.py (GS-H3-RESET ok=True arms=3), round1_prep/checks/r1_fastlane.py (GS-T3-FASTLANE ok=True arms=2), r4x_closegate_round.py (GS-X1-CLOSEGATE ok=True arms=2)",
        "3.0.0_SA_CVO read org/git-author-override-audit.log line 47779: 2026-10-09T16:46:37Z PASS 2.0.0_SA_COO~N1 1 act=d346d21fbd3e paths=1:...TRACE_round4.md; 128 audit lines carry act=",
        "3.0.0_SA_CVO checked the UNATTRIBUTED ties: 9f01c965cd (1.0.0_SA_CTO, 2026-10-06T00:05:50Z) carries agent-spawn-audit.log and drive-mode.log (40786); infra/logic/registry/reporting_policies.json has no 2.0.0_SA_COO~G2 commit -- its only commit after BLOCK 44486 (10:49Z) is 103902e75d by 4.0.0_SA_CRO at 17:00Z, after the worker's run (f95c647336 16:24Z), so the replay's 'never committed' was true when read",
        "PRD v0.4 FWD-8 DONE WHEN/ACCEPT (prd lines 31-40 @a33d3bde72); ROUND_ANALYSIS.round3.md ADDENDUM 1 items 1-4",
        "org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/TRACE_round4.md @4132c3e933"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An L9 grade record, not a hazard."
  },
  {
    "id": "NFRA_GATSCP-D1-C-S27",
    "project": "NFRA_GATSCP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T17:53:00Z",
    "one_line": "D1-W14-S1 dismissed: confirmed -- block line 39887 (2.0.0_SA_COO~P, n=3) and OVERRIDE 40151 (n=2) are both lane TREE_DELIVERABLES; the override served 98d439936a (2 files, ~8 folder, 5 s before the stamp), carrying neither blocked path. The order's CONTEXT sentence mis-listed it as a lane mismatch; the replay's 19/5/2 counts stand and the act key retires the pairing.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_GATSCP-D1-W14-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "D1-W14-S1 dismissed: confirmed -- block line 39887 (2.0.0_SA_COO~P, n=3) and OVERRIDE 40151 (n=2) are both lane TREE_DELIVERABLES; the override served 98d439936a (2 files, ~8 folder, 5 s before the stamp), carrying neither blocked path. The order's CONTEXT sentence mis-listed it as a lane mismatch; the replay's 19/5/2 counts stand and the act key retires the pairing.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row NFRA_GATSCP-D1-W14-S1",
        "3.0.0_SA_CVO read audit log lines 39887 and 40151; git show --name-only 98d439936a"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W14-S1 dismissed: confirmed -- block line 39887 (2.0.0_SA_COO~P, n=3) and OVERRIDE 40151 (n=2) are both lane TREE_DELIVERABLES; the override served 98d439936a (2 files, ~8 folder, 5 s before the stamp), carrying neither blocked path. The order's CONTEXT sentence mis-listed it as a lane mismatch; the replay's 19/5/2 counts stand and the act key retires the pairing."
  },
  {
    "id": "NFRA_GATSCP-D1-C-S28",
    "project": "NFRA_GATSCP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T17:53:00Z",
    "one_line": "D1-S15 dismissed: fixed by direct act GS-x-1 @7d6c43c991 -- .tools/git-hooks/missions-tree-check.sh:103 now passes --round <n> (the highest staged <round>) and WARNs when none is found; r4x_closegate_round.py 2/2 on this seat's run, incl. an ungraded judgment in the round being closed still refusing.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_GATSCP-D1-S15"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "D1-S15 dismissed: fixed by direct act GS-x-1 @7d6c43c991 -- .tools/git-hooks/missions-tree-check.sh:103 now passes --round <n> (the highest staged <round>) and WARNs when none is found; r4x_closegate_round.py 2/2 on this seat's run, incl. an ungraded judgment in the round being closed still refusing.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row NFRA_GATSCP-D1-S15",
        "3.0.0_SA_CVO read missions-tree-check.sh:103; ran r4x_closegate_round.py: GS-X1-CLOSEGATE ok=True arms=2"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-S15 dismissed: fixed by direct act GS-x-1 @7d6c43c991 -- .tools/git-hooks/missions-tree-check.sh:103 now passes --round <n> (the highest staged <round>) and WARNs when none is found; r4x_closegate_round.py 2/2 on this seat's run, incl. an ungraded judgment in the round being closed still refusing."
  },
  {
    "id": "NFRA_GATSCP-D1-C-S29",
    "project": "NFRA_GATSCP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T17:53:00Z",
    "one_line": "In-place closes: REMEDIATION_v2 D1-S7 REMEDIATED (ruled in ROUND_ANALYSIS.round3 section 2: the five gates with 0 measured refusals stay out with the limit stated; the two in scope are graded by FWD-8 above); REMEDIATION_v3 D1-W13-S1 REMEDIATED (cut as round-4 item 3 and built by GS-h-3: --continue refuses a reset both ways, 17/17 with the change, 16/17 FAIL on the pre-change safe-merge.sh). D1-S10 stays OPEN, routed to 0.0.0_AB_MSTR~DELL1 by ADDENDUM 1 item 5.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "In-place closes: REMEDIATION_v2 D1-S7 REMEDIATED (ruled in ROUND_ANALYSIS.round3 section 2: the five gates with 0 measured refusals stay out with the limit stated; the two in scope are graded by FWD-8 above); REMEDIATION_v3 D1-W13-S1 REMEDIATED (cut as round-4 item 3 and built by GS-h-3: --continue refuses a reset both ways, 17/17 with the change, 16/17 FAIL on the pre-change safe-merge.sh). D1-S10 stays OPEN, routed to 0.0.0_AB_MSTR~DELL1 by ADDENDUM 1 item 5.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ROUND_ANALYSIS.round3.md section 2 and ADDENDUM 1",
        "3.0.0_SA_CVO ran r4_reset_both.py: GS-H3-RESET ok=True arms=3",
        "org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/TRACE_round4.md @4132c3e933 (GS-h-3 negative run)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A record of remediation closes, not a hazard."
  }
]
```
