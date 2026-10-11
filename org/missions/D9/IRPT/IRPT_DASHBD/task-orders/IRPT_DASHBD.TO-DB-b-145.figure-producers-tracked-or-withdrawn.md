# TO IRPT_DASHBD.TO-DB-b-145 -- a number whose producer is not in the tree is not shown: the scripts behind the tie-out records' figures are tracked in the project's folder, or the figure is listed as withdrawn

<to_id>IRPT_DASHBD.TO-DB-b-145</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~118</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>77</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2's ROUND-76 ANALYSIS `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_76_20261011.md` @d70feb6d15, item 1 (second half), answering `org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/remediations/REMEDIATION_v32.md` @305103f259 | **Rows:** IRPT_DASHBD-D2-W114-S1 | **Decomp cell:** `DB-b-145` (decomposition section 79) | **outcome_ref:** FWD-12 (the tie-out) | **depends_on:** DB-b-144 (drained @76ceae2cc7).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-118` (branch `wk-irpt-dashbd-77-118`); run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~118/`. Read first: the analysis above, and each row named above in
`org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/remediations/REMEDIATION_v32.md` (the reviewer's statement of it) and in `org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md` (the original row).

**Why.** The tie-out's records quote figures (59 of 90, 82 classed, 51 contested, 18 unreproduced, 50 of 50, 89 of 90, and others)
that were computed by scripts living OUTSIDE the repo, under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/<worker>/`. DB-b-141 found it, and DB-b-144 showed
one such figure was wrong for a reason only the script could show (row W114-S1). The CTO: "The two untracked scripts that produced
figures the records quote are tracked in the project's folder, or their figures are withdrawn with them. A number whose producer is not
in the tree is not shown."

**The cell (`DB-b-145`).** You recompute NOTHING and edit no other worker's record.
1. **The figures.** Read the tie-out records of rounds 68 to 76 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~104`, `~108`, `~111`,
   `~113`, `~115`, `~117`, and `2.0.0_SA_COO~D2/RERUN_FIVE_DAYS_ROW_W111_S1.md`): each figure a record states that came from a script
   in the private folder. `figures`: [{record, figure (the sentence or member), producer_origin (the private script path and the lines
   that make the number), state, tracked_as, why}].
2. **Track the producers.** For each, copy the SCRIPT files (code only: `.py`; never a pickle, parquet, JSON table or log) into your
   folder under `producers/<origin worker folder name>/`, unchanged except as item 3 requires, and record each copy's sha256
   (`tracked_as`: [{file (relative to your folder), sha256, origin_sha256, changed (bool)}]). A script you cannot find, or that cannot
   be made clean under item 3, leaves its figure `WITHDRAWN` with why, and you file ONE row listing the withdrawn figures (the records
   themselves are their owners' to amend).
3. **No client data enters the tree.** Before copying, scan every script for a run of 8 or more digits and for anything that reads as
   an account id, a client name or an amount written as a literal. If a script holds one (a hard-coded account, a literal used to pick
   a row), replace that literal in YOUR COPY with a named placeholder (for example `ACCOUNT_REDACTED`) and set `changed: true` with a
   one-line note; the check refuses a tracked file holding a run of 8 or more digits (the private evidence folder's own name, which carries a date, is
   excepted and stays). Bucket names, prefixes, column names and
   tolerances are not client data and stay. `scanned` {files, long_digit_runs: 0}.
4. Record `FIGURE_PRODUCERS.json`. The issuer tracks its own re-run script; do not copy from `2.0.0_SA_COO~D2/`'s private folder.

<criterion id="DB77-1-AC1" cell_refs="DB-b-145"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r77/p77_round77.py" . DB77-1-AC1</invocation><expect>DB77-1-AC1 PASS</expect></criterion>
`DB77-1-AC1` -- every figure the tie-out records quote from a script outside the tree is listed, and its producing script is tracked in the worker's folder with its hash, or the figure is listed as withdrawn with why. Base: FAIL.

<expected_criteria>DB77-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No served write.** No S3 put, copy or delete; no Lambda, Terraform or IAM act; no `upload=True` call; no deploy; no push. No AWS call at all.
- **No client data in what you write.** Counts and booleans only: no account id, no client name, no figure of any client. Anything you
  download goes OUTSIDE the repo, under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~118/`.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. A result you could not establish is NOT_ESTABLISHED with its reason, never guessed. An edit outside the grant is a
  defect: stop and file a row.
- **Every `.py` edit passes `bash .tools/commit-gate.sh <file>`.** ASCII only.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W118-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~118/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-145.figure-producers-tracked-or-withdrawn.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 79 (round 77), cell `DB-b-145`.
<owned_cells>DB-b-145</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB77-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~118/IRPT_DASHBD.TO-DB-b-145.figure-producers-tracked-or-withdrawn.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB77-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; ONE table: record, figure, where its producer was, TRACKED (as which files) or WITHDRAWN (why); how many script files you copied and that none holds a long digit run; any script you did NOT copy and why; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; copies of read-only scripts and one record; no figure is recomputed, no served thing is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the scheduled producer runs from its source-map pins, not from this branch.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record). The rows are the reviewer's and the CTO's statements; the issuer re-read none of their evidence for this issuance.
lane: the <paths> block IS the grant.
</preflight>
