# TO IRPT_DASHBD.TO-DB-b-157 -- the proposal record carries the class set as RULED: the two first-axis tokens accepted, TIMING_END removed because it can have no member, and the three retired tokens listed together

<to_id>IRPT_DASHBD.TO-DB-b-157</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~121</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>82</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 ruling msg 5955 (2026-10-11 ~22:15Z) | **Rows:** IRPT_DASHBD-D2-W121-S4 | **Decomp cell:** `DB-b-157` (decomposition section 84) | **outcome_ref:** FWD-12 (the tie-out) | **depends_on:** DB-b-155 (drained @afd4a87aaa).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-121` (branch `wk-irpt-dashbd-82-121`); run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~121/`. Read first: each row named above in
`org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md`, and the records this order names.

**The ruling this answers (CTO msg 5955), verbatim in part.** "Accepted: axis RESTATED_CLOSE, values RESTATED_CLOSES_UNDER_OTHER_TIMING
and RESTATED_DOES_NOT_CLOSE_UNDER_OTHER_TIMING, claim measured [...] Row D2-W121-S4 is right and I correct my ruling 5886 on it: I kept
TIMING_END. With the first axis defined as a close under a timing OTHER than the served one, END can never be a member, and a value that
cannot occur is not a value. TIMING is three: TIMING_START, TIMING_MID, TIMING_NOT_DETERMINED, claim inferred for the first two. The
record lists TIMING_END as retired beside the two RECONCILES tokens. Placement stands: 51 close under another timing; 3 START, 1 MID, 47
not determined. The classes are entered in the tie-out's records only. Nothing served is relabelled, and no record says the served
return matches the custodian's on these 51."

**The cell (`DB-b-157`).** You are the serial that owns `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~121/TIMING_CLASSES_PROPOSAL.json`;
you amend it. You recompute nothing and census nothing new.
1. Remove `TIMING_END` from the TIMING axis's `values` (and its meaning entry, if the axis carries one per value), from `new_tokens`,
   from `token_census`, and remove the placement cell that names it (it holds 0 segments; the cells still sum to 51).
2. Add a top-level member `retired_tokens`: three entries {token, retired_by, why}: `RECONCILES_YES` and `RECONCILES_NO` (retired by
   "1.0.0_SA_CTO~DELL2 msg 5886", why in that ruling's words, as `superseded_tokens` already states) and `TIMING_END` (retired by
   "1.0.0_SA_CTO~DELL2 msg 5955", why in this ruling's words). LEAVE `superseded_tokens` exactly as it is: round 80's check reads it.
3. Add a top-level member `ruled`: {by ("1.0.0_SA_CTO~DELL2 msg 5955"), accepted_axis ("RESTATED_CLOSE"), accepted_values (the two),
   timing_values (the three), served_relabelled (false), entered_in ("the tie-out's records only"), not_claimed ("no record says the
   served return matches the custodian's on these 51")}. Keep `is_a_proposal` and `proposal_is_a_ruling` as they are: the record is
   the proposal; `ruled` records what was ruled on it.
4. Where `postulates`, `the_three` or `does_not_decide` state `TIMING_END` as a value of the axis, reword so the record reads in the
   three values; free-text history may still name it. If `y1_place.py` prints it as a label, change the label only and say so.
5. Three criteria must end in PASS after your edit, run each and report its last line: this order's; round 80's
   (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r80/p80_round80.py` DB80-2-AC1); round 78's (`.../checks/r78/p78_round78.py`
   DB78-1-AC1). If one cannot pass with the others, stop and report which and why; do not edit a check.
   Edit with a python script written by the Write tool; keep indentation, key order and line endings.

<criterion id="DB82-1-AC1" cell_refs="DB-b-157"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r82/p82_round82.py" . DB82-1-AC1</invocation><expect>DB82-1-AC1 PASS</expect></criterion>
`DB82-1-AC1` -- the TIMING axis holds exactly three values, TIMING_END is gone from the tokens, the census and the placement and is listed retired beside the two RECONCILES tokens, the ruling is recorded, and the 51 are still placed. Base: FAIL.

<expected_criteria>DB82-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No served write.** No S3 put, copy or delete; no Lambda, Terraform or IAM act; no `upload=True` call; no deploy; no push. No AWS call at all.
- **No client data in what you write.** Counts and booleans only: no account id, no client name, no figure of any client. Anything you
  download goes OUTSIDE the repo, under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~121/`.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. A result you could not establish is NOT_ESTABLISHED with its reason, never guessed. An edit outside the grant is a
  defect: stop and file a row.
- **Every `.py` edit passes `bash .tools/commit-gate.sh <file>`.** ASCII only.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W121-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~121/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-157.ruled-class-set-timing-end-retired.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 84 (round 82), cell `DB-b-157`.
<owned_cells>DB-b-157</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB82-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~121/IRPT_DASHBD.TO-DB-b-157.ruled-class-set-timing-end-retired.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB82-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; what you removed and where; the retired list; that rounds 78's and 80's criteria on this record were re-run and what each printed; the diff's line count; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; a record's own text; no class is applied to anything served, nothing served is relabelled.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the scheduled producer runs from its source-map pins, not from this branch.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record). The rows are the reviewer's and the CTO's statements; the issuer re-read none of their evidence for this issuance.
lane: the <paths> block IS the grant.
</preflight>
