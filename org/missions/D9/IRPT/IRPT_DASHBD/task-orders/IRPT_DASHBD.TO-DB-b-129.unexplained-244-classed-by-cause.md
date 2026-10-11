# TO IRPT_DASHBD.TO-DB-b-129 -- the 244 UNEXPLAINED tie-out segments: classed by cause, the remainder printed -- a read of existing records, counts only

<to_id>IRPT_DASHBD.TO-DB-b-129</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~104</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>68</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2's ROUND-68 ANALYSIS `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_68_20261011.md` @0005d9fd9a, section 4 item 6, answering `org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/remediations/REMEDIATION_v27.md` @806d057711 | **Rows:** IRPT_DASHBD-D2-W86-S2 (and W86-S1 for the set's definition) | **Decomp cell:** `DB-b-129` (decomposition section 70) | **outcome_ref:** FWD-12 (the tie-out) | **depends_on:** DB-b-124 (its read of rows W86-S1 and W86-S2).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-104` (branch `wk-irpt-dashbd-68-104`); run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~104/`. Read first: section 3 (row W86-S2) and 4 (item 6) of the analysis above, and each row named above in
`org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/remediations/REMEDIATION_v27.md` (the reviewer's statement of it) and in `org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md` (the original row).

**What is asked.** The tie-out's 990 outside segments were split under the DATE TEST (ruled today: it stands, analysis section 3, row
W86-S1). CONVENTION is accepted as a FLOOR (74 segments carry a per-segment convention shift), and 244 segments remain UNEXPLAINED: "that
is the figure the tie-out is judged on. The next cell on the tie-out works the 244."

**The cell (`DB-b-129`).** Read-only; you change no code and no served thing.
1. **Find and reproduce the 244.** The split was produced by the cell behind rows W86-S1 and W86-S2: its record is in
   `deliverables/0.9.0_WK_IRPT_DASHBD~86/` (and the cells it cites: DB-b-106's flagged set, the restated tie-out). Reproduce the count of
   UNEXPLAINED segments from that record's own data, and state how (`method` {source, how}). If you reproduce a different number, STOP
   with a row: the criterion's denominator is 244 and a different count is a finding, not something to round.
2. **Class each by cause**, from what the records ALREADY hold per segment (dates, flow presence, the size of the difference relative to
   the tolerance, account type, whether a corporate action or a fee falls in the window, whether a neighbouring segment of the same account
   is explained): propose a small set of causes, each with a RULE a reader could re-apply (`classes`: [{cause, count, rule,
   example_segment_ref}], where `example_segment_ref` is a row index or segment key in the record, never an account id). A cause is a
   property of the segment's data, not a guess about the custodian. Hunt the uncovered member by subtraction: every one of the 244 lands in
   exactly one class or in the remainder.
3. **The remainder** (`remainder` {count, why}): what cannot be classed from the records, and what a next cell would need to class it.
4. `denominator: 244`, `client_figures: 0`. Counts only; no account id, no client figure, no dollar amount of any account.

<criterion id="DB68-6-AC1" cell_refs="DB-b-129"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r68/p68_round68.py" . DB68-6-AC1</invocation><expect>DB68-6-AC1 PASS</expect></criterion>
`DB68-6-AC1` -- the 244 UNEXPLAINED segments are classed by cause with a stated rule per class, and the classes and the remainder sum to 244. Base: FAIL.

<expected_criteria>DB68-6-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No served write.** No S3 put, copy or delete; no Lambda, Terraform or IAM act; no `upload=True` call; no deploy; no push. No AWS call at all. If the records in the tree cannot class a segment without a custodian re-read, that segment is in the REMAINDER with that reason; re-reading custodian rows is not ordered in this round.
- **No client data in what you write.** Counts and booleans only: no account id, no client name, no figure of any client. Anything you
  download goes OUTSIDE the repo, under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~104/`.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. A result you could not establish is NOT_ESTABLISHED with its reason, never guessed. An edit outside the grant is a
  defect: stop and file a row.
- **Every `.py` edit passes `bash .tools/commit-gate.sh <file>`.** ASCII only.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W104-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~104/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-129.unexplained-244-classed-by-cause.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 70 (round 68), cell `DB-b-129`.
<owned_cells>DB-b-129</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB68-6-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~104/IRPT_DASHBD.TO-DB-b-129.unexplained-244-classed-by-cause.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB68-6-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; where the 244 came from (file and how you reproduced the count); ONE table of classes: cause, count, the rule that puts a segment in it; the remainder and why it is not classed; what a next cell would need to class the remainder; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; a read of existing tie-out records; nothing served, nothing written but a record.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the scheduled producer runs from its source-map pins, not from this branch.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record). The rows are the reviewer's and the CTO's statements; the issuer re-read none of their evidence for this issuance.
lane: the <paths> block IS the grant.
</preflight>
