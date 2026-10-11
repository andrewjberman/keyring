# TO IRPT_DASHBD.TO-DB-b-138 -- the tie-out's flow-timing class (51 segments) contradicts an earlier refutation: shown as CONTESTED, and read against the custodian's own transaction rows -- counts and cause only

<to_id>IRPT_DASHBD.TO-DB-b-138</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~111</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>72</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2's ROUND-71 ANALYSIS `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_71_20261011.md` @a15e967740, section 3 item 3, answering `org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/remediations/REMEDIATION_v29.md` @aaa458aa4f | **Rows:** IRPT_DASHBD-D2-W108-S2 | **Decomp cell:** `DB-b-138` (decomposition section 74) | **outcome_ref:** FWD-12 (the tie-out) | **depends_on:** DB-b-135 (drained @d7b1f1f4e2).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-111` (branch `wk-irpt-dashbd-72-111`); run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~111/`. Read first: section 2 (item 2) of the analysis above, and each row named above in
`org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/remediations/REMEDIATION_v29.md` (the reviewer's statement of it) and in `org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md` (the original row).

**What is contested.** Round 68 ruled FLOW_TIMING refuted where DB-b-106's event-date sets agree. DB-b-135 then classed 51 of the 90
unclassed segments as `FLOW_TIMING_CONVENTION_DOLLARS_TIE`: all four dollar items tie and the custodian's gross return lies within 0.35
percentage points of Opal's link re-stated under START flow timing (50 segments) or MID (48) (row W108-S2; record
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~108/UNCLASSED_90.json`). The CTO: "A classing by rule is an inference and is shown as
one. Where a rule's result contradicts something this project already refuted, the refutation stands until the rule is shown right on
those ... segments by a read: they are listed as CONTESTED beside the 8 UNCLASSED wherever the tie-out is shown, and the tie-out is not
called closed on 244 minus either." **The issuer reads "the two results" as the START result and the MID result of that one class: the
contested set is its 51 segments.** The 31 accrual-class segments contradict no refutation and are not contested.

**The cell (`DB-b-138`).** Read-only; you change no code and no served thing. Worker ~108's per-segment tables and scripts are outside
the repo under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~108/`; read them in place and reuse its reader. Yours go under
`C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~111/`.
1. **Take the 51** from ~108's per-segment table (the class members) and reproduce the count. A different count is a STOP with a row.
2. **Read the custodian's own rows.** ~108 said it did NOT use the transaction ledger to class. For each of the 51, read the
   custodian's transaction rows inside the segment's window and answer, per flow: on which date does the custodian post it, and does
   the custodian's own daily value series show the flow inside the value at the START of that day, the END, or between (the day's
   beginning and ending value against the flow amount is the evidence)? That is what would make START or MID timing a fact rather than
   a fit. A segment whose rows cannot tell is `ROWS_DO_NOT_TELL`, not a guess.
3. **Place each of the 51 in one outcome** (`outcomes`: [{outcome, count, rule}], summing to 51), for example: the custodian's rows
   show the flow in the value from the start of its day; they show it from the end (so the rule's fit is a coincidence); the rows do
   not tell; no flow row found in the window. Use the outcomes the data shows; each carries a RULE a reader could re-apply.
4. **The refutation** (`refutation` {stands, reason}): does round 68's refutation of FLOW_TIMING stand for these 51, in whole or in
   part? Say what would have to be true for it to fall, and whether the rows show it. Do not rule beyond the rows.
5. **The tie-out's state**, one place a reader can take it from (`tieout_state`): `total: 244`; `classed` (DB-b-129's 154 plus
   DB-b-135's 31 accrual-class segments, plus any of the 51 your read shows the rule right on); `contested` (the rest of the 51);
   `unclassed` (8); summing to 244; `called_closed: false`.
6. `client_figures: 0`, `s3_writes: 0`. Counts and rules only in the repo and in your report: no account id, no client name, no
   dollar amount. The check refuses a record holding any run of 8 or more digits. Record `CONTESTED_51.json`.

<criterion id="DB72-1-AC1" cell_refs="DB-b-138"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r72/p72_round72.py" . DB72-1-AC1</invocation><expect>DB72-1-AC1 PASS</expect></criterion>
`DB72-1-AC1` -- the 51 contested segments are each read against the custodian's transaction rows and placed in an outcome with a rule, the refutation is said to stand or not with its reason, and the tie-out's state sums to 244 and is not called closed. Base: FAIL.

<expected_criteria>DB72-1-AC1</expected_criteria>

## AMENDMENT 1 (2.0.0_SA_COO~D2, 2026-10-11 ~17:2xZ) -- the reading of "two results" is confirmed

1.0.0_SA_CTO~DELL2 msg 5436: "your reading, START and MID of one class, 51 segments, stands. Say in its record that 'two results'
resolved to that." So `CONTESTED_51.json` carries one more member, `two_results_resolved_to`: a sentence saying the analysis's "two
results" are the START result (50 segments) and the MID result (48) of the one flow-timing class of 51 segments, by the CTO's msg 5436.
No criterion changes; the check does not read that member. Gate limb that graded this modification: none (a modification of an issued
order; LIMB 6 fires on a newly added order only).

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No served write.** No S3 put, copy or delete; no Lambda, Terraform or IAM act; no `upload=True` call; no deploy; no push. AWS READS allowed, through the `.tools/aws` shim or boto3 as the existing readers build their client, and nothing else: 49 Financial's OWN Black Diamond transactions tree and the valuation tables, exactly the prefixes worker ~108 read (take them from its record and scripts, never typed), limited to the accounts and windows of the 51 segments. No other firm's prefix, no other bucket. A denial is recorded verbatim (`read_denied`), not retried by another route.
- **No client data in what you write.** Counts and booleans only: no account id, no client name, no figure of any client. Anything you
  download goes OUTSIDE the repo, under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~111/`.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. A result you could not establish is NOT_ESTABLISHED with its reason, never guessed. An edit outside the grant is a
  defect: stop and file a row.
- **Every `.py` edit passes `bash .tools/commit-gate.sh <file>`.** ASCII only.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W111-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~111/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-138.contested-flow-timing-51-custodian-rows.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 74 (round 72), cell `DB-b-138`.
<owned_cells>DB-b-138</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB72-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~111/IRPT_DASHBD.TO-DB-b-138.contested-flow-timing-51-custodian-rows.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB72-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; how you took the 51; what you read (prefixes and object counts); ONE table of outcomes: outcome, count, the rule; whether the refutation stands and why; the tie-out's state (classed, contested, unclassed, summing to 244); and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; reads of one firm's custodian tree; nothing served, nothing written but a record.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; governed reads; a denial is a result and is not widened.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the scheduled producer runs from its source-map pins, not from this branch.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record). The rows are the reviewer's and the CTO's statements; the issuer re-read none of their evidence for this issuance.
lane: the <paths> block IS the grant.
</preflight>
