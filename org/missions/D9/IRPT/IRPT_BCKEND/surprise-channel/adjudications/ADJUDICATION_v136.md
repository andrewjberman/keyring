# IRPT_BCKEND: CVO adjudication, round 4 (workstream ~PL, IB-pr-606)

<sweep_watermark>2026-10-16T03:50Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-16T03:50Z, on msg 8992 (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_PL3_TO_PL8_DRAIN_END_20261016.md` @5d90e76797, blob f0310e6f79, shared by ~PL rounds 3 to 8). Round 4 ~PL: one order, IB-pr-606 (49F addendum candidate, digest 32d6dfcb (VOID by design: it omitted the key on a failed read)), complete, merged @56d4c0fea7. No judgment criterion. Re-run here at HEAD 6729ef019e. IB237-1-AC1, AC3 PASS at HEAD; AC2 FAILS at HEAD. It fails at HEAD only on what a later ~PL round replaced by design, traced by content: the test name account_not_in_smartx_is_exempt_without_an_evidence_key is present in test_absent_at_source_smartx_evidence.py at f888350689, 56d4c0fea7, 53c238604b and 860e265792, and absent from 1ff5e87e40 on (IB-pr-609 makes that account write smartx_map_absent); holdings_snapshot.py's blob moves e01e8d0401 (r3/r4) -> c55f55f774 (r5/r6) -> 89a3b9eff5 (r7, r8, HEAD), so a candidate built on an earlier blob no longer equals HEAD's D spans. Nothing deployed (read-only, 03:4xZ): Lambda irpt-holdings LastModified 2026-10-13T12:47:20Z; the three firm bundles s3://opal-data-{49financial,cottonwood,inflection}/irpt/<firm>/code/gold/investor-reporting-holdings.tar.gz were last modified 2026-10-15T15:19-15:21Z, before these rounds. Verdict: **MAY-CLOSE**. No remediation row.

```json
[
 {
  "id": "IRPT_BCKEND-D2-C-S44",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-16T03:50:00Z",
  "one_line": "Round 4 ~PL (IB-pr-606): MAY-CLOSE. Rows: W442-S1 (a git worktree add from this box comes up sparse; carried into IB-pr-605/611 step 2) and W442-S2, INERT.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-W442-S1",
   "IRPT_BCKEND-D2-W442-S2"
  ],
  "spec_asserts": "Spine L9/L10: every terminal round is graded by the CVO before close; the round-close gate's verdict stands unless its owner rules; CTO msg 8627: the exemption pair is bound to the transplant bundles, Branch A diff exactly the two members, the S206 CUSIP STOP in every HEAD-based build.",
  "world_is": "Repo-only round; nothing deployed or minted. The round may close.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-16T03:3xZ at HEAD 6729ef019e: IB237-1-AC1..AC3 as stated",
    "python .tools/round-close-check.py --project IRPT_BCKEND --round 4 --workstream ~PL: MAY-CLOSE",
    "aws lambda get-function-configuration irpt-holdings; s3api head-object on the three firm holdings bundles (read-only)",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_PL3_TO_PL8_DRAIN_END_20261016.md blob f0310e6f79 (msg 8992)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Worker and issuer rows of a repo-only round, each dispositioned on its evidence above; the ARMED ones are carried into the apply orders or ruled by a recorded Andrew-direct record."
 }
]
```
