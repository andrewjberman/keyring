# IRPT_BCKEND: CVO adjudication, round 2 (workstream ~PS, the filled-report serve path build slices)

<sweep_watermark>2026-10-15T04:46Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T04:46Z, on msg 8051 (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_2_PS_DRAIN_END_20261015.md` @aefc53ef3a). Three orders, IB-pr-553 (hop 2 publisher plumbing), IB-pr-554 (hop 3 route), IB-pr-555 (hop 4 export source kind), all complete, issued @8cdd704be7 on the CTO's msg 7995 after the CTO half signed @82183fcfaf. No judgment criterion; nothing deployed, applied, invoked or written to AWS. Re-run here at HEAD: IB200-1, IB200-2 and IB200-3 AC1..AC3, 9 of 9 PASS (exit 0 each). `round-close-check --round 2 --workstream "~PS"`: orders=3, proofs 3 of 3 ok, verdict=MAY-CLOSE.

**The audited override at 409a7f7ef2.** It is a LANE override (`GIT_COMMIT_AUTHOR_OVERRIDE`, audit line `org/git-author-override-audit.dell2.log` 2026-10-15T04:42:13Z `OVERRIDE 2.0.0_SA_COO~P2 ... --author-override TREE_DELIVERABLES applied`, landed 04:42:21Z): it let the issuer write worker 398's proof instance in the worker's deliverables folder, replacing that instance's IB200-2-AC3 row (worker's FAIL exit 1, "paths outside the grant: test_reporting_entry.py") with the issuer's re-run PASS. It bypassed WHO MAY WRITE the file, not the criterion. AC3 passes on this seat's own re-run at HEAD with no override in the path. Negative control: the check as it stood before the amendment (`c13575e177^`) reads IB200-2-AC3 FAIL on the same tree, on exactly that one path; the amended check reads PASS; the only difference between the two is one line adding `test_reporting_entry.py` to the allowed set. The amendment followed worker 398's refusal-clause stop (D2-W398-S1) and is stated in c13575e177 (AMENDMENT 1, gate limb GATE (viii)). The worker's change to that file is the one ROUTES pin line, as the amendment allows. Standing note: the AC3 row in the worker's proof instance is the issuer's grade, not the worker's; this seat's independent re-run is what carries the PASS.

10 rows dismissed below. Carried into round 3, not hazards today: the packaged ExportBundle contract refuses a filled_report item (D2-W399-S1), so hop 4 cannot freeze a bundle end to end yet; and the export freeze gates on `household.accounts` only while the signed packet's scope rule names every by_row account key (D2-W399-S2), so the route and the export check scope on different sets until round 3 reconciles them. HELD, carried and owned: D2-W392-S2, D2-W394-S2, W349-S1, W361-S1, W348-S2, W368-S2 (owner `~P2`), D2-S158 (owner the CTO).

```json
[
 {
  "id": "IRPT_BCKEND-D2-C-S10",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T04:46:00Z",
  "one_line": "Round 2 ~PS. The three LOCAL build slices of the signed serve-path pair are built and tested with stubs, nothing deployed: hop 2 publisher plumbing (default OFF unless FILLED_REPORT_PASS is exactly 1), hop 3 route with a new named-account reader and all-accounts refusal, hop 4 filled_report export source pinned by VersionId and sha256. 9 of 9 criteria PASS re-run here. IB200-2-AC3 passes on this seat's re-run with no override; the 409a7f7ef2 override was a lane override (TREE_DELIVERABLES) letting the issuer rewrite the worker's proof-instance AC3 row, not a criterion bypass; negative control: the pre-amendment check fails only on the amended path. Dismissed (10): D2-W397-S1, -S2, D2-W398-S1..S4 (two issuer defects repaired in-round: the entry-test pin outside the grant and the check not amended on the branch; the rest readings), D2-W399-S1 (BLOCKING, INERT: the packaged ExportBundle contract refuses a filled_report item; a round-3 cell, nothing exercised), D2-W399-S2 (route vs export scope sets; round 3), D2-W399-S3 (the freeze has no caller; round 3), D2-S183 (the issuer's dispositions).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-W397-S1",
   "IRPT_BCKEND-D2-W397-S2",
   "IRPT_BCKEND-D2-W398-S1",
   "IRPT_BCKEND-D2-W398-S2",
   "IRPT_BCKEND-D2-W398-S3",
   "IRPT_BCKEND-D2-W398-S4",
   "IRPT_BCKEND-D2-W399-S1",
   "IRPT_BCKEND-D2-W399-S2",
   "IRPT_BCKEND-D2-W399-S3",
   "IRPT_BCKEND-D2-S183"
  ],
  "spec_asserts": "Spine L7/L9 (CLAUDE.md rule 27): a criterion is graded by its named invocation, never self-graded; an issuer amends its own criteria stating the gate limb; every BLOCKING or ARMED row is dispositioned before the slug.",
  "world_is": "Code for hops 2-4 is on box/dell2, LOCAL, tested with stubs; no route exists in AWS. The first exercise still waits on 49F gold for one date (CTO msg 7995), on the round-3 contract cell (the packaged ExportBundle contract must admit filled_report), on a caller and production reader for the freeze, and on reconciling the export freeze's account set with the signed scope rule. The worker's proof instance carries an issuer-written AC3 row under an audited lane override; the PASS stands on this seat's independent re-run.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T04:4xZ of org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r200/p200_cells.py at HEAD: IB200-1-AC1..3, IB200-2-AC1..3, IB200-3-AC1..3 PASS, exit 0 each",
    "negative control: git show c13575e177^:.../checks/r200/p200_cells.py run on the same tree: IB200-2-AC3 FAIL, paths outside the grant: test_reporting_entry.py; git diff c13575e177^ HEAD on the check: 1 file, 2 insertions, 1 deletion (the allowed set)",
    "org/git-author-override-audit.dell2.log: 2026-10-15T04:42:13Z OVERRIDE 2.0.0_SA_COO~P2 --author-override TREE_DELIVERABLES on the worker 398 proof_of_spec.json; 04:42:21Z LANDED-2P 409a7f7ef2",
    "git diff 8cdd704be7 HEAD -- infra/aws/lambda/investor-reporting/reporting/tests/test_reporting_entry.py: one assertion, ROUTES pin gains FILLED_ROUTE_KEY",
    "python .tools/round-close-check.py --project IRPT_BCKEND --round 2 --workstream ~PS: orders=3 proof_ok=3 judgment=0 verdict=MAY-CLOSE",
    "investigation rows D2-W397-S1..S2, D2-W398-S1..S4, D2-W399-S1..S3, D2-S183",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_2_PS_DRAIN_END_20261015.md @aefc53ef3a (msg 8051)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Two issuer defects repaired in-round and verified here by re-run and negative control, readings, and three round-3 cells on code nothing exercises yet. The override is a lane override on the proof file, not a criterion bypass."
 }
]
```
