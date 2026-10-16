# IRPT_DASHBD: CVO adjudication, round 118 (workstream F-SHIP, ~F2): one test for a household scalar under an avs member

<sweep_watermark>2026-10-16T00:58Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-16T00:58Z, on msg 8821 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/L8_PACKET_R118_F.md` @dbf56b0a3d, blob 8eb06bafa1), a packet written after the issuer's close at the CTO's round-119 ruling 5; graded by this lane under rule 5 of `CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md` (CTO msg 8009). Not B-49F's or B-IN's round 118. One order, TO-DB-f-507 (LOCAL, direct act; worker ~507; issuance 4e10f83b5d, drained @209c3ff2a3). No judgment criterion. Re-run: DBF118-1-AC1 and AC2 FAIL on the landed tree and PASS on the candidate head 65f2e5430b (scratch root, removed after). 2 of 2 PASS on the target tree; proof VALID; round-close MAY-CLOSE. No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S57",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-16T00:58:00Z",
  "one_line": "Round 118 F-SHIP (~F2): one test pins that a household scalar under an avs benchmark member prints the same figure in every account table (the producer's guard D2-S67 forbids that input). No source change. 2 of 2 PASS on the candidate tree. NOTHING PROMOTED WHILE UNSEEN: the candidate heads of rounds 116-118 (portal e23ddb8e34, 0d58fe2c43, 65f2e5430b) are each NOT an ancestor of origin/DEV (d6fd0684) or origin/PROD (e0e69da7), and no remote ref contains them (git -C portal merge-base --is-ancestor; branch -r --contains; fetched 2026-10-16T00:5xZ). No client-facing page change reached DEV or PROD, so Andrew's word was never needed. No worker row from this round. THE CTO'S TWO ARMED ROWS (msg 8820), checked here. D2-S102 (FWD-3 hops 2-6) is ARMED with disarm_owner 2.0.0_SA_COO~F2, and names the hop owners per the CTO's round-119 ruling (producer ~F2, series contract and publish ~D2, OBJECTS member ~S2, portal ~F2). D2-S103 (FWD-5: no contract, no producer) is ARMED with disarm_owner 2.0.0_SA_COO~F2, the sole writer of the new IRPT_DASHBD_ACCOUNT_TRANSACTION_CONTRACT.json. Both have an OWNER. NEITHER STATES A DISARM CONDITION: no field or sentence says what act disarms it. S103's notes list next acts (a code census, a vocabulary with its rule-24 record, then the contract), and S102 raises a premise conflict instead (the table the ruling calls NEW already has a contract 0.1.0, a producer and an applied release). Each row needs a one-line 'disarms when' (for example, S103: when the contract and its per-firm producer land, with their L9; S102: when a served series object carries class keys and the route serves it), or it can never be graded disarmed. Both are HELD.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-S102",
   "IRPT_DASHBD-D2-S103"
  ],
  "spec_asserts": "Spine L9/L10: every terminal round is graded by the CVO before close; a criterion is re-run on the tree it targets; a client-facing page reaches PROD only on Andrew's word.",
  "world_is": "The scalar case is pinned by a test in an unpushed candidate. The two ARMED FWD-3 and FWD-5 carriers exist with owners but without disarm conditions, and S102 carries an open premise question for the CTO.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-16T00:5xZ: DBF118-1-AC1, AC2 FAIL on the landed tree; PASS at 65f2e5430b; proof VALID (~507); round-close --round 118 --workstream ~F2 MAY-CLOSE",
    "git -C portal: 65f2e5430b not in origin/DEV nor origin/PROD; no remote ref contains it",
    "investigation rows D2-S102, D2-S103 (fields: disarm_owner 2.0.0_SA_COO~F2 each; no disarm-condition field or sentence)",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/L8_PACKET_R118_F.md blob 8eb06bafa1 (msg 8821)"
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "D2-S102 and D2-S103 are named to HOLD them (ARMED, owner ~F2), not to dismiss them, so this row carries UNDER_INVESTIGATION. Round 118's own cell is graded above (2 of 2 PASS on its target tree)."
 }
]
```
