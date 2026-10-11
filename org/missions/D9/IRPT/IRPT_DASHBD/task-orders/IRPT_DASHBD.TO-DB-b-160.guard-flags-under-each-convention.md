# TO IRPT_DASHBD.TO-DB-b-160 -- the guard's interplay: how many days now marked FLOW_UNRECONCILED or LARGE_FLOW under END would not be under START or MID, and the reverse

<to_id>IRPT_DASHBD.TO-DB-b-160</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~129</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>83</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2's ROUND-83 ANALYSIS `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_83_20261011.md` @3f7c91e682, section 3 item 3 | **Rows:** NONE | **Decomp cell:** `DB-b-160` (decomposition section 85) | **outcome_ref:** FWD-8 / C-FLOWTIME and C-GUARD | **depends_on:** DB-b-159 (its private per-account-day table).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-129` (branch `wk-irpt-dashbd-83-129`); run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~129/`. Read first: the analysis above, whole (it is one page), and the records this order names.

**Why.** C-GUARD marks a day `FLOW_UNRECONCILED` or `LARGE_FLOW` and such a day falls back to the price return. The CTO: "how many
days now marked FLOW_UNRECONCILED or LARGE_FLOW under END would not be under START, and the reverse. A convention that moves which days
fall back to the price return changes more than the flow days."

**The cell (`DB-b-160`).** A read and a private recomputation; it starts after DB-b-159 has drained.
1. **The guard's rule.** Read C-GUARD in `org/missions/D9/IRPT/IRPT_DASHBD/prd/IRPT_DASHBD_PRD.md` and the producer code that sets the two flags (under
   `infra/aws/lambda/investor-reporting/`; cite `guard_rule` {file, line} and say what each flag compares: a flow against what,
   at what threshold). Decide from the code whether each flag's test uses a quantity that depends on the flow convention (the day's
   return, or a base value that includes or excludes the flow): `flag_depends_on_convention` (bool) with `depends_basis` per flag.
2. **The counts.** On DB-b-159's private per-account-day table (`C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~128/`, its README names
   the columns; read, never edit), evaluate each flag under END, START and MID by the code's own rule. Control first: your END flags
   must reproduce the SERVED flags (`end_reproduces` {flagged_served, flagged_restated, differ}); if they do not, stop and report.
   `flags`: {FLOW_UNRECONCILED, LARGE_FLOW}, each {under_end, under_start, under_mid, end_not_start, start_not_end, end_not_mid,
   mid_not_end}. If a flag does not depend on the convention, its moves are 0 and the three counts are equal: say so.
3. **What a moved flag changes.** Cite where a flagged day falls back to the price return, and count `fallback_days_moved` for START
   and for MID (days whose served return would switch between the flow-adjusted and the price return). No return is written.
4. `s3_writes: 0`, `limits`. Counts only: no account id, client name, amount or return value. Private files under
   `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~129/`. Record `GUARD_INTERPLAY.json`.
5. **In every record of this round (item 5): `the_39`** {count: 39, accrual_class: 31, unclassed: 8, statement}. The statement says in a
   sentence that 39 of the 90 two-sided segments close under NO timing (31 of the accrual class, 8 unclassed), that nothing in this
   record changes them, and that a change of convention would not close the tie-out. A reader who quotes a number from your record
   must meet that sentence beside it.

<criterion id="DB83-3-AC1" cell_refs="DB-b-160"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r83/p83_round83.py" . DB83-3-AC1</invocation><expect>DB83-3-AC1 PASS</expect></criterion>
`DB83-3-AC1` -- the guard's rule is cited, and for each of the two flags the days flagged under END, START and MID and the days that move each way are counted so the moves carry one count to the other. Base: FAIL.

<expected_criteria>DB83-3-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No served write.** No S3 put, copy or delete; no Lambda, Terraform or IAM act; no `upload=True` call; no deploy; no push. AWS READS allowed, through the `.tools/aws` shim or boto3 as the existing readers build their client, and nothing else: the served gold objects the Investor Reporting dashboard's producer writes for the ONE firm the tie-out reads (the daily account return, its flow and its guard flags), read into a private copy outside the repo. No write, no producer run against a served prefix, no other firm's prefix. A denial is recorded verbatim, not retried by another route. Only if DB-b-159's private copy lacks a column the guard reads.
- **No client data in what you write.** Counts and booleans only: no account id, no client name, no figure of any client. Anything you
  download goes OUTSIDE the repo, under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~129/`.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. A result you could not establish is NOT_ESTABLISHED with its reason, never guessed. An edit outside the grant is a
  defect: stop and file a row.
- **Every `.py` edit passes `bash .tools/commit-gate.sh <file>`.** ASCII only.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W129-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~129/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-160.guard-flags-under-each-convention.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 85 (round 83), cell `DB-b-160`.
<owned_cells>DB-b-160</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB83-3-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~129/IRPT_DASHBD.TO-DB-b-160.guard-flags-under-each-convention.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB83-3-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; where the guard's rule is and what it compares; whether each flag depends on the convention at all, and why; for each flag the days under END, START and MID and the days that move each way; what a moved flag changes downstream (the fallback to the price return), cited; the sentence on the 39; what you could not establish; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; a private recomputation and a count record; nothing served.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; governed reads; a denial is a result.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the scheduled producer runs from its source-map pins, not from this branch.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record). The rows are the reviewer's and the CTO's statements; the issuer re-read none of their evidence for this issuance.
lane: the <paths> block IS the grant.
</preflight>
