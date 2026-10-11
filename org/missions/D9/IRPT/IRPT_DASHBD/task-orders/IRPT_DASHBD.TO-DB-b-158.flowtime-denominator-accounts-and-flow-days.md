# TO IRPT_DASHBD.TO-DB-b-158 -- the count ruling 24 requires, printed: the accounts and the flow-bearing days behind the 51 segments, with how many close under each timing

<to_id>IRPT_DASHBD.TO-DB-b-158</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~127</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>83</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2's ROUND-83 ANALYSIS `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_83_20261011.md` @3f7c91e682, section 3 item 1 | **Rows:** NONE | **Decomp cell:** `DB-b-158` (decomposition section 85) | **outcome_ref:** FWD-8 / C-FLOWTIME (the tie-out's flow-timing measurement) | **depends_on:** DB-b-157 (drained @6a82a2a5ba).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-127` (branch `wk-irpt-dashbd-83-127`); run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~127/`. Read first: the analysis above, whole (it is one page), and the records this order names.

**Why.** The PRD's C-FLOWTIME (`org/missions/D9/IRPT/IRPT_DASHBD/prd/IRPT_DASHBD_PRD.md`, near lines 224-225) says the tie-out scores start, end and midpoint and writes
the winner into the method contract. Ruling 24 (near lines 524-527) withheld a winner from round 1 because one flow-bearing day in one
account cannot rank three conventions, and set the bar: eligible flow-bearing days from more than one account, **with that count
printed beside the winner**. The measurement now exists (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~121/TIMING_CLASSES_PROPOSAL.json`); the count beside it does not.

**The cell (`DB-b-158`).** A count. You recompute no return.
1. From the private per-segment tables the proposal's script reads (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~121/y1_place.py` names
   them; they sit under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/`), take the 51 segments (the `RESTATED_CLOSES_UNDER_OTHER_TIMING` ones) and count:
   `accounts` (distinct accounts among them) and `flow_bearing_days` (distinct account-days carrying a flow inside those segments;
   say exactly what you counted as a flow-bearing day and from which column), plus `flow_bearing_days_per_account` as a small
   distribution (min, median, max) and `accounts_with_one_flow_day`.
2. `closes`: {end, start, mid, both, start_only, mid_only} over the 51, re-derived from the same tables. `agrees_with_record` (bool)
   against the proposal's placement (47 not determined, 3 START, 1 MID; END 0) with `agrees_basis`.
3. Say whether ruling 24's bar is met as written (more than one account; the count printed): `ruling_24_bar` {met (bool), why}.
4. **In every record of this round (item 5): `the_39`** {count: 39, accrual_class: 31, unclassed: 8, statement}. The statement says in a
   sentence that 39 of the 90 two-sided segments close under NO timing (31 of the accrual class, 8 unclassed), that nothing in this
   record changes them, and that a change of convention would not close the tie-out. A reader who quotes a number from your record
   must meet that sentence beside it.
5. No account id, client name or amount; counts only. Record `FLOWTIME_DENOMINATOR.json`; `segments: 51`.

<criterion id="DB83-1-AC1" cell_refs="DB-b-158"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r83/p83_round83.py" . DB83-1-AC1</invocation><expect>DB83-1-AC1 PASS</expect></criterion>
`DB83-1-AC1` -- the accounts and flow-bearing days behind the 51 are counted from the per-segment tables, the closes under each timing are restated from the same tables, and it is said whether they agree with the ruled record. Base: FAIL.

<expected_criteria>DB83-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No served write.** No S3 put, copy or delete; no Lambda, Terraform or IAM act; no `upload=True` call; no deploy; no push. No AWS call at all. Everything is taken from the private per-segment tables behind the class proposal.
- **No client data in what you write.** Counts and booleans only: no account id, no client name, no figure of any client. Anything you
  download goes OUTSIDE the repo, under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~127/`.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. A result you could not establish is NOT_ESTABLISHED with its reason, never guessed. An edit outside the grant is a
  defect: stop and file a row.
- **Every `.py` edit passes `bash .tools/commit-gate.sh <file>`.** ASCII only.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W127-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~127/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-158.flowtime-denominator-accounts-and-flow-days.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 85 (round 83), cell `DB-b-158`.
<owned_cells>DB-b-158</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB83-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~127/IRPT_DASHBD.TO-DB-b-158.flowtime-denominator-accounts-and-flow-days.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB83-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the accounts and the flow-bearing days behind the 51, and how each was counted; the closes under END, START, MID, both, START only and MID only; whether that agrees with the ruled record; the sentence on the 39; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; a count record; nothing served.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the scheduled producer runs from its source-map pins, not from this branch.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record). The rows are the reviewer's and the CTO's statements; the issuer re-read none of their evidence for this issuance.
lane: the <paths> block IS the grant.
</preflight>
