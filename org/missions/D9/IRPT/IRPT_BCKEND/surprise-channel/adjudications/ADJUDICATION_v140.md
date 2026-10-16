# IRPT_BCKEND: CVO adjudication, round 8 (workstream ~PL, IB-pr-610)

<sweep_watermark>2026-10-16T03:50Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-16T03:50Z, on msg 8992 (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_PL3_TO_PL8_DRAIN_END_20261016.md` @5d90e76797, blob f0310e6f79, shared by ~PL rounds 3 to 8). Round 8 ~PL: one order, IB-pr-610 (49F candidate rebuilt, digest 61537d6d (the current one)), complete, merged @65650cbbbd. No judgment criterion. Re-run here at HEAD 6729ef019e. IB241-1-AC1, AC2, AC3 PASS at HEAD. BUNDLE CHECK (CTO msg 8627), re-derived here by content: the current candidate's publication.py is byte-identical to the signed IB-pr-595 transplant (deliverables/0.9.0_WK_IRPT_BCKEND~434/transplant/49financial/publication.py); its holdings_snapshot.py with the three ABSENT-AT-SOURCE-D spans stripped is byte-identical to the signed transplant's holdings_snapshot.py, and its spans equal HEAD's three spans exactly; the two artifacts hash to the record's 028cebb8 and cfe39832; allow_older_date is absent (no one-date bypass); the 12 CUSIP lines are present in both the candidate and the signed transplant. So Branch A's diff against live is the two exemption members only. The S206 CUSIP STOP is written into both apply orders (IB-pr-605 and IB-pr-611 step (iv): count the built file's CUSIP lines, STOP if reversed). The bundle digest 61537d6d itself is the worker's build, not rebuilt here; the apply's digest gate rebuilds it before any upload. ROUND-CLOSE READS REFUSED: 'no proof instance named IRPT_BCKEND.TO-IB-pr-610.addendum-candidate-49f-v3.proof_of_spec.json'. The instance at deliverables/0.9.0_WK_IRPT_BCKEND~446/IRPT_BCKEND.TO-IB-pr-610.addendum-candidate-49f.proof_of_spec.json reads VALID (rc=0) under proof-of-spec-check, but this seat does not waive a gate: the round stays NOT MAY-CLOSE until the instance carries the order stem's name or the gate's owner rules. Gate: .tools/round-close-check.py (header: NFRA_CTLPLN workstream SEATS, cell CT-s-8, contract C-SEATS clause 7, FWD-23; its last commits are 1.0.0_SA_CTO's). ~P2 cannot rename it (owned-paths refuses a COO write into a worker folder). Nothing deployed (read-only, 03:4xZ): Lambda irpt-holdings LastModified 2026-10-13T12:47:20Z; the three firm bundles s3://opal-data-{49financial,cottonwood,inflection}/irpt/<firm>/code/gold/investor-reporting-holdings.tar.gz were last modified 2026-10-15T15:19-15:21Z, before these rounds. Verdict: **NOT MAY-CLOSE**. No remediation row.

```json
[
 {
  "id": "IRPT_BCKEND-D2-C-S48",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-16T03:50:00Z",
  "one_line": "Round 8 ~PL (IB-pr-610): NOT MAY-CLOSE. Rows: W446-S1 (sparse pin worktree, as W444-S1), W446-S2 (36 CRLF-only M entries checked by raw equality), W446-S3 (read_date as the UTC date), INERT; S213 (the issuer's dispositions of rows W440..W446) checked against each row and accepted.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-W446-S1",
   "IRPT_BCKEND-D2-W446-S2",
   "IRPT_BCKEND-D2-W446-S3",
   "IRPT_BCKEND-D2-S213"
  ],
  "spec_asserts": "Spine L9/L10: every terminal round is graded by the CVO before close; the round-close gate's verdict stands unless its owner rules; CTO msg 8627: the exemption pair is bound to the transplant bundles, Branch A diff exactly the two members, the S206 CUSIP STOP in every HEAD-based build.",
  "world_is": "Repo-only round; nothing deployed or minted. The round-close gate refuses on an instance name only; the instance itself is VALID.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-16T03:3xZ at HEAD 6729ef019e: IB241-1-AC1..AC3 as stated",
    "python .tools/round-close-check.py --project IRPT_BCKEND --round 8 --workstream ~PL: REFUSED",
    "aws lambda get-function-configuration irpt-holdings; s3api head-object on the three firm holdings bundles (read-only)",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_PL3_TO_PL8_DRAIN_END_20261016.md blob f0310e6f79 (msg 8992)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Worker and issuer rows of a repo-only round, each dispositioned on its evidence above; the ARMED ones are carried into the apply orders or ruled by a recorded Andrew-direct record."
 }
]
```
