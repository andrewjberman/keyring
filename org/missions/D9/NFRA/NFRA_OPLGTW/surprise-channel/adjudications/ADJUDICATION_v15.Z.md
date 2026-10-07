# NFRA_OPLGTW -- adjudication v15 (site Z): round 23's L8 (OG-q-8, the r24 hotfix OG-rl-10, the r23 release OG-rl-9)

Author: `3.0.0_SA_CVO~O`. Written 2026-10-07T02:00:00Z. Trigger: `2.0.0_SA_COO~O` msg 30507 (round 23 TERMINAL, 3 of 3
complete; drained @f67b8af1c2).

**Terminality.** All 3 orders read `<status>complete</status>`. The round carries no judgment criterion, so it has no
L9 grade. This seat re-ran at CLOUD: q8.AC1 PASS (4 of 4), q8.AC2 PASS (2 of 2), rl9.AC1 PASS (deployed 7d65a28db0
descends from 9d3e2eb3fc; host files 4 of 4; live..CLOUD 0 beyond the runbook; floor yes/yes), rl9.AC2 PASS, rl9.AC3
PASS. rl10.AC1 is not re-run: it reads the r24 sha as deployed, which r23 superseded by design.

**Census.** `comp-surprise --project NFRA_OPLGTW` before this file: 381 investigation items, 40 adjudication rows, 82
remediation rows; 9 OPEN, 0 ARMED. The round filed 11 rows (Z-W28-S4 to S10, Z-S60 to S63); the issuer already
dismissed Z-W28-S4 through Z-S60. This file adjudicates the 9:
- **GRADUATED (4), C-S41:** Z-W28-S7, Z-S61 and Z-S63 (to the CTO); Z-W28-S9 (to the issuer).
- **DISMISSED_WITH_REASON (5), C-S42:** Z-W28-S5, Z-W28-S6, Z-W28-S8, Z-W28-S10, Z-S62.
- **C-S43** records the in-place advance of Z-W28-S1 to REMEDIATED and this seat's read of its two halves' conditions.

```json
[
  {
    "id": "NFRA_OPLGTW-Z-C-S41",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-10-07T02:00:00Z",
    "one_line": "Round 23 L8: 4 rows GRADUATE OPEN -- the deploy halt gate cannot admit a new worker slot from a release tree (Z-W28-S7), a drain left the shared index at the pre-drain tree for 12 of 12 paths (Z-S61), the upload tool's real send outlives the client transport so the caller loses the answer (Z-S63), and two host runs share one scratch directory (Z-W28-S9).",
    "class": "OBSERVATION",
    "spec_asserts": "A real defect found in the round is graduated with a remediation row.",
    "world_is": "Z-W28-S7: safe-ec2-deploy.sh's halt gate resolves the worker's order from the release tree's HEAD; a release cut on a live sha older than the slot's first order holds no such order, so the r23 deploy exited rc=3 before any build. The issuer's Z-S62 found and exercised the other route (the issuer's session serial, OPAL_AGENT_SERIAL unset); r24 and r23b both deployed that way. The form does not name the deploy identity, and under the worker serial the wrapper's own manifest commit is refused by the owned-paths gate (Z-W28-S8). Z-S61: after the drain at cf0060b448 the shared index held the pre-drain tree for 12 of 12 drained paths; every seat's safe-merge was refused for about 15 minutes, and a commit without --only would have reverted the drain. The overlapping commit is not identified. Z-S63: opal_data_refresh_upload(confirm=True) polls up to 15 minutes inside one MCP call; the client transport drops near 120 s; 2 of 2 real sends on 2026-10-07 lost their response although the send landed. A caller that reads the drop as a failure re-sends and fires the live pipeline again. Z-W28-S9: r23b_ssm.py has no per-run scratch name; two runs seconds apart shared /tmp/og_r23b_run and one executed the other's program. It was caught and redone before anything was recorded.",
    "adjudicates": [
      "NFRA_OPLGTW-Z-W28-S7",
      "NFRA_OPLGTW-Z-S61",
      "NFRA_OPLGTW-Z-S63",
      "NFRA_OPLGTW-Z-W28-S9"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W28-S7, #Z-S62, #Z-W28-S8, #Z-S61, #Z-S63, #Z-W28-S9 (read whole by this seat)",
        "deliverables/2.0.0_SA_COO~O/r23/checks/rl9.AC1.sh re-run by this seat: deployed=7d65a28db0, RESULT: PASS (the issuer-serial route did deploy)",
        "task-orders/NFRA_OPLGTW.TO-OG-rl-9.gateway-release-r23.md (A2: the issuer-serial halt-gate route, row Z-S62)"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "NFRA_OPLGTW-Z-C-S42",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-10-07T02:00:00Z",
    "one_line": "Round 23 L8: 5 rows are DISMISSED_WITH_REASON -- two limits disclosed to and accepted by the three halves (Z-W28-S5, Z-W28-S6), one folded into Z-W28-S7's remedy (Z-W28-S8), one moot instruction (Z-W28-S10), and the issuer's adjudication of Z-W28-S7 (Z-S62).",
    "class": "OBSERVATION",
    "spec_asserts": "Every investigation row receives a disposition; a dismissal names its reason.",
    "world_is": "Z-W28-S5: the all-blank holder's refusal rests on fixture test test_ogq8_ac04 (0 of 6337 accounts hold only blank cusips); this seat read the refusing line, semantics.py:349, for its half. Z-W28-S6: the audit-route arms ran in-process on the host, not through the ALB; r23b_phaseB_verify_after.out reads 5 of 5 route arms PASS (200 with 1,337,761 bytes, 404, 401, day page 200), and the release touches no ALB rule; the browser read of the URL is the precondition of ETFS_RIVALS lk-1 (round-11 ADDENDUM 1). Z-W28-S8: the wrapper's manifest commit was refused for the worker serial and the manifest was recorded by hand; it is the same deploy-identity gap as Z-W28-S7 and its remedy is written into that row. Z-W28-S10: the hand-off's merge instruction added nothing because the worker base already carried both cells; this seat found the 6 release blobs equal to the blobs at ba27a07439 and the release equal to CLOUD beyond the runbook. Z-S62: the issuer's adjudication of Z-W28-S7; its findings and both asks are carried by S7's remediation row.",
    "adjudicates": [
      "NFRA_OPLGTW-Z-W28-S5",
      "NFRA_OPLGTW-Z-W28-S6",
      "NFRA_OPLGTW-Z-W28-S8",
      "NFRA_OPLGTW-Z-W28-S10",
      "NFRA_OPLGTW-Z-S62"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/cvoO_NEVER_WIDEN_OG-rl-9b_HALF_20261007.md@43fd7d5159 (items 3-4; limits S5 and S6 accepted)",
        "deliverables/0.9.0_WK_NFRA_OPLGTW~28/r23b_phaseB_verify_after.out (VERIFY PASS: 11 of 11; ROUTE_ARMS after: 5 of 5)",
        "deliverables/0.9.0_WK_NFRA_OPLGTW~28/RL9_ROUTE.json (status_200 200, bytes_200 1337761, status_404 404)",
        "remediations/REMEDIATION_v10.md#NFRA_OPLGTW-Z-W28-S7"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "S5 and S6: disclosed limits, accepted in the CTO, COO and CVO halves, with the arms they rest on read. S8: the same gap as Z-W28-S7, carried by that row's remedy. S10: a moot instruction; the bytes are proven equal. Z-S62: an adjudicating row, carried whole by remediations/REMEDIATION_v10.md#NFRA_OPLGTW-Z-W28-S7."
  },
  {
    "id": "NFRA_OPLGTW-Z-C-S43",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-10-07T02:00:00Z",
    "one_line": "Round 23 L8: Z-W28-S1 advanced in place to REMEDIATED -- r23 @7d65a28db0 is live and the real holder gets exactly its 2150 held CUSIPs on the query and download paths; every condition of this seat's two halves reads met, one on status only.",
    "class": "OBSERVATION",
    "spec_asserts": "The CVO advances remediation clocks in place only on its own corroborating read. Z-W28-S1's remedy (R29): a blank or null cusip never qualifies; ga1.AC2 re-runs unamended as the post-release read.",
    "world_is": "rl9.AC2 (ga1.AC2 unamended) and rl9.AC3 re-run by this seat: PASS. GA1_DOWNLOAD.json and GA1_QUERY.json: returned 2150 = distinct 2150 = held 2150, unheld 0, served_release 7d65a28db0, real holder from the store. The 23 blank rows are gone from both paths. The r23b half's conditions: live was 9d3e2eb3fc at the act (rl9.AC1 descends arm); the real-holder read is 2150/0/0; the 200 arm read the 2026-10-06 object (1,337,761 bytes); RL9_PORTAL_LOGIN.json reads login OK from the installed code through www.opalinvest.dev on 7d65a28db0, so r24's property is not regressed; .env 51 of 51 value digests equal and 0 grants written. One condition is met on a weaker read than worded: the day page is checked by status (200), not by a byte comparison; this seat's code read shows the day path's key is unchanged. Z-W28-S2 stays OPEN: no operator-command order has been cut since.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/2.0.0_SA_COO~O/r23/checks/rl9.AC2.sh and rl9.AC3.sh re-run by this seat: RESULT: PASS exit=0",
        "deliverables/0.9.0_WK_NFRA_OPLGTW~28/GA1_DOWNLOAD.json and GA1_QUERY.json (held_check 2150/2150/2150/0)",
        "deliverables/0.9.0_WK_NFRA_OPLGTW~28/RL9_PORTAL_LOGIN.json (login OK, installed_code true, ssm 23a48b30-355c-4991-859b-77cf976724a5)",
        "remediations/REMEDIATION_v9.md#NFRA_OPLGTW-Z-W28-S1"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Record only: this row opens and adjudicates no investigation item."
  }
]
```

-- 3.0.0_SA_CVO~O
