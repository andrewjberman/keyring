# TO IRPT_DASHBD.TO-DB-b-152 -- the withdrawn figures in `UNEXPLAINED_244.json` marked withdrawn in the record that quotes them

<to_id>IRPT_DASHBD.TO-DB-b-152</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~104</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>79</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2's ROUND-78 ANALYSIS `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_78_20261011.md` @bf620b7e50, section 3 item 4, answering `org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/remediations/REMEDIATION_v33.md` @7c237a67ec | **Rows:** IRPT_DASHBD-D2-W118-S1 | **Decomp cell:** `DB-b-152` (decomposition section 81) | **outcome_ref:** FWD-12 (the tie-out) | **depends_on:** DB-b-145 (drained @f09dfcb6d9).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-104` (branch `wk-irpt-dashbd-79-104`); run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~104/`. Read first: section 2 of the analysis above, and each row named above in
`org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/remediations/REMEDIATION_v33.md` (the reviewer's statement of it) and in `org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md` (the original row).

**Why.** DB-b-145 listed 42 figures the tie-out records quote and found three with no producing script: they are WITHDRAWN (row
`IRPT_DASHBD-D2-W118-S1`; record `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~118/FIGURE_PRODUCERS.json`). The CTO: "the records that
quote them are amended this round. A withdrawn figure left in a record is still being quoted." This order is issued to the serial that
owns the record, so the lane admits the edit.

**The cell (`DB-b-152`).** You recompute NOTHING and change no other member of the record.
1. Read `FIGURE_PRODUCERS.json` (its `figures` entries with `state: "WITHDRAWN"`) and row `IRPT_DASHBD-D2-W118-S1`: the two in this record are the split of the 244 by DB-b-106 verdict (122, 113 and 9), and the statement that none of the 244 is among the 74 restated segments.
2. In `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~104/UNEXPLAINED_244.json` (your own folder):
   - add a top-level member `withdrawn_figures`: a list of 2 entries, each {figure (the sentence or member as it read, with
     where in the record it sat), why (no script computes it: say exactly what the tracked script does and does not do), withdrawn_by
     ("1.0.0_SA_CTO~DELL2 ROUND-78 ANALYSIS item 4; row IRPT_DASHBD-D2-W118-S1")};
   - where the figure sits in the record's own text, replace the number with the words `WITHDRAWN (see withdrawn_figures)` so a
     reader who meets the sentence does not meet the number; keep the rest of the sentence. If the figure is a structured member a
     check reads, do not remove a member the round's checks rely on: read the checks under
     `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/` that name your record first, and say which you read.
   - keep the file's indentation, key order and line endings; `git diff` shows only those lines.
3. Re-run the criterion that first graded your record, if its check still exists, and report that it still passes.

<criterion id="DB79-2-AC1" cell_refs="DB-b-152"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r79/p79_round79.py" . DB79-2-AC1</invocation><expect>DB79-2-AC1 PASS</expect></criterion>
`DB79-2-AC1` -- the record carries its withdrawn figures, each with why and by whom, and still states its own denominator. Base: FAIL.

<expected_criteria>DB79-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No served write.** No S3 put, copy or delete; no Lambda, Terraform or IAM act; no `upload=True` call; no deploy; no push. No AWS call at all.
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
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-152.withdrawn-figures-marked-in-the-244-record.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 81 (round 79), cell `DB-b-152`.
<owned_cells>DB-b-152</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB79-2-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~104/IRPT_DASHBD.TO-DB-b-152.withdrawn-figures-marked-in-the-244-record.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB79-2-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; each withdrawn figure as it read before and how the record reads now; that nothing else in the record changed (the diff's line count); and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; one record's own text; no figure is recomputed, nothing served.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the scheduled producer runs from its source-map pins, not from this branch.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record). The rows are the reviewer's and the CTO's statements; the issuer re-read none of their evidence for this issuance.
lane: the <paths> block IS the grant.
</preflight>
