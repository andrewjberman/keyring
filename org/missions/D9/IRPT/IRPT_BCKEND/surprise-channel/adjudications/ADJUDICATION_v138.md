# IRPT_BCKEND: CVO adjudication, round 6 (workstream ~PL, IB-pr-608)

<sweep_watermark>2026-10-16T03:50Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-16T03:50Z, on msg 8992 (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_PL3_TO_PL8_DRAIN_END_20261016.md` @5d90e76797, blob f0310e6f79, shared by ~PL rounds 3 to 8). Round 6 ~PL: one order, IB-pr-608 (49F candidate rebuilt, digest 75c6902d (VOID by design: no key on a successful read that does not show the account)), complete, merged @860e265792. No judgment criterion. Re-run here at HEAD 6729ef019e. IB239-1-AC1, AC3 PASS at HEAD; AC2 FAILS at HEAD. It fails at HEAD only on what a later ~PL round replaced by design, traced by content: the test name account_not_in_smartx_is_exempt_without_an_evidence_key is present in test_absent_at_source_smartx_evidence.py at f888350689, 56d4c0fea7, 53c238604b and 860e265792, and absent from 1ff5e87e40 on (IB-pr-609 makes that account write smartx_map_absent); holdings_snapshot.py's blob moves e01e8d0401 (r3/r4) -> c55f55f774 (r5/r6) -> 89a3b9eff5 (r7, r8, HEAD), so a candidate built on an earlier blob no longer equals HEAD's D spans. ROUND-CLOSE READS REFUSED: 'no proof instance named IRPT_BCKEND.TO-IB-pr-608.addendum-candidate-49f-v2.proof_of_spec.json'. The instance at deliverables/0.9.0_WK_IRPT_BCKEND~444/IRPT_BCKEND.TO-IB-pr-608.addendum-candidate-49f.proof_of_spec.json reads VALID (rc=0) under proof-of-spec-check, but this seat does not waive a gate: the round stays NOT MAY-CLOSE until the instance carries the order stem's name or the gate's owner rules. Gate: .tools/round-close-check.py (header: NFRA_CTLPLN workstream SEATS, cell CT-s-8, contract C-SEATS clause 7, FWD-23; its last commits are 1.0.0_SA_CTO's). ~P2 cannot rename it (owned-paths refuses a COO write into a worker folder). Nothing deployed (read-only, 03:4xZ): Lambda irpt-holdings LastModified 2026-10-13T12:47:20Z; the three firm bundles s3://opal-data-{49financial,cottonwood,inflection}/irpt/<firm>/code/gold/investor-reporting-holdings.tar.gz were last modified 2026-10-15T15:19-15:21Z, before these rounds. Verdict: **NOT MAY-CLOSE**. No remediation row.

```json
[
 {
  "id": "IRPT_BCKEND-D2-C-S46",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-16T03:50:00Z",
  "one_line": "Round 6 ~PL (IB-pr-608): NOT MAY-CLOSE. Rows: W444-S1 (ARMED: sparse pin worktree; carried into IB-pr-605/611 step 2, so the apply cannot meet it unwarned); W444-S2 (ARMED: the commit gate's client-data list is absent on dell2; WARN-only on dell2 by Andrew's record ANDREW_DIRECT_20261009_192xZ_CLIENT_DATA_IN_PRIVATE_GIT_NOT_WORTH_TIME, the same disposition as earlier rounds; the records are ID-free by their own criteria; restoring the list is MSTR's); W444-S3/S4 INERT record notes.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-W444-S1",
   "IRPT_BCKEND-D2-W444-S2",
   "IRPT_BCKEND-D2-W444-S3",
   "IRPT_BCKEND-D2-W444-S4"
  ],
  "spec_asserts": "Spine L9/L10: every terminal round is graded by the CVO before close; the round-close gate's verdict stands unless its owner rules; CTO msg 8627: the exemption pair is bound to the transplant bundles, Branch A diff exactly the two members, the S206 CUSIP STOP in every HEAD-based build.",
  "world_is": "Repo-only round; nothing deployed or minted. The round-close gate refuses on an instance name only; the instance itself is VALID.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-16T03:3xZ at HEAD 6729ef019e: IB239-1-AC1..AC3 as stated",
    "python .tools/round-close-check.py --project IRPT_BCKEND --round 6 --workstream ~PL: REFUSED",
    "aws lambda get-function-configuration irpt-holdings; s3api head-object on the three firm holdings bundles (read-only)",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_PL3_TO_PL8_DRAIN_END_20261016.md blob f0310e6f79 (msg 8992)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Worker and issuer rows of a repo-only round, each dispositioned on its evidence above; the ARMED ones are carried into the apply orders or ruled by a recorded Andrew-direct record."
 }
]
```
