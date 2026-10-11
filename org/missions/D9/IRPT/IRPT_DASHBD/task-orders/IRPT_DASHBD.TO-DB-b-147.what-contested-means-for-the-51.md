# TO IRPT_DASHBD.TO-DB-b-147 -- what CONTESTED still means for the 51 now that their day-by-day flows reproduce, and what would close each -- a statement from the records, no new read

<to_id>IRPT_DASHBD.TO-DB-b-147</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~120</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>77</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2's ROUND-76 ANALYSIS `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_76_20261011.md` @d70feb6d15, item 4, answering `org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/remediations/REMEDIATION_v32.md` @305103f259 | **Rows:** IRPT_DASHBD-D2-W108-S2, IRPT_DASHBD-D2-W111-S1 | **Decomp cell:** `DB-b-147` (decomposition section 79) | **outcome_ref:** FWD-12 (the tie-out) | **depends_on:** DB-b-142 and DB-b-144 (drained).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-120` (branch `wk-irpt-dashbd-77-120`); run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~120/`. Read first: the analysis above, and each row named above in
`org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/remediations/REMEDIATION_v32.md` (the reviewer's statement of it) and in `org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md` (the original row).

**Why.** The tie-out reads 185 classed, 51 contested, 8 unclassed, not closed. The 51 were classed by DB-b-135 under a flow-timing rule
that contradicted round 68's refutation of FLOW_TIMING, and so were ruled CONTESTED. Since then: DB-b-138 found the custodian's rows
fix the DAY of a flow and not its time of day; DB-b-140, the issuer's re-run and DB-b-142 found that with each transaction id counted
once the ledger reproduces the served flow to the cent on 234 of 235 flow days, the last being an expense the method does not count as
a flow; DB-b-144 found 89 of 90 tie on net additions. The CTO: "one cell says what CONTESTED still means for the 51 now that their
day-by-day flows reproduce, and what would close each: a segment that reproduces to the cent with ids counted once is no longer
contested on its flow."

**The cell (`DB-b-147`).** No AWS call, no code. Read the records (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~108/UNCLASSED_90.json`,
`~111/CONTESTED_51.json`, `~113/UNREPRODUCED_18.json`, `~115/CENT_REREAD.json`, `~117/TIE_59_OF_90_REDERIVED.json`,
`2.0.0_SA_COO~D2/RERUN_FIVE_DAYS_ROW_W111_S1.md`) and their private per-segment tables under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/` (read in
place; counts only leave them).
1. **Per segment, what is settled and what is not.** For each of the 51: does its flow reproduce to the cent on every flow day with
   ids counted once (`flow_reproduces` {segments_all_days_to_the_cent, segments_not}); do its four dollar items tie (DB-b-135); under
   which timing does its return close within 0.35 percentage points (START, MID, both); which DB-b-138 outcome it had (the rows fix
   the day; the ledger did not reproduce, now explained; no determinable flow).
2. **Groups by what is STILL contested** (`groups`: [{meaning, segments, what_would_close_it}], summing to 51), in plain words. For
   example: the amount and the day of every flow are settled and only the time of day the custodian credits a flow is not, which no
   record this project can read shows; or the segment has no flow large enough to tell. For each group, the ONE thing that would close
   it, named concretely: a custodian statement of its convention, a custodian intraday series, a ruling that a fit within tolerance
   under one stated timing is accepted as the classing, or nothing obtainable.
3. **A proposal, marked as one** (`proposal`, `proposal_is_a_ruling: false`): what the tie-out should say about the 51 where it is
   shown. You rule nothing and move no segment: `tieout_state` {total: 244, classed: 185, contested: 51, unclassed: 8,
   called_closed: false}. The CTO rules.
4. Counts and plain statements only: no account id, no client name, no amount. Record `CONTESTED_51_MEANING.json`.

<criterion id="DB77-3-AC1" cell_refs="DB-b-147"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r77/p77_round77.py" . DB77-3-AC1</invocation><expect>DB77-3-AC1 PASS</expect></criterion>
`DB77-3-AC1` -- the 51 contested segments are grouped by what is still contested about each, with what would close each group, and the tie-out's state is restated and not called closed. Base: FAIL.

<expected_criteria>DB77-3-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No served write.** No S3 put, copy or delete; no Lambda, Terraform or IAM act; no `upload=True` call; no deploy; no push. No AWS call at all. Everything is taken from the records and private tables rounds 70 to 76 already made.
- **No client data in what you write.** Counts and booleans only: no account id, no client name, no figure of any client. Anything you
  download goes OUTSIDE the repo, under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~120/`.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. A result you could not establish is NOT_ESTABLISHED with its reason, never guessed. An edit outside the grant is a
  defect: stop and file a row.
- **Every `.py` edit passes `bash .tools/commit-gate.sh <file>`.** ASCII only.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W120-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~120/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-147.what-contested-means-for-the-51.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 79 (round 77), cell `DB-b-147`.
<owned_cells>DB-b-147</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB77-3-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~120/IRPT_DASHBD.TO-DB-b-147.what-contested-means-for-the-51.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB77-3-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; ONE table of groups: what is still contested, segments, what would close it; how many of the 51 reproduce their flow to the cent on every day; your proposal in one sentence, marked as a proposal; the tie-out's state; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; a statement assembled from existing records; no read, no code, nothing served.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the scheduled producer runs from its source-map pins, not from this branch.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record). The rows are the reviewer's and the CTO's statements; the issuer re-read none of their evidence for this issuance.
lane: the <paths> block IS the grant.
</preflight>
