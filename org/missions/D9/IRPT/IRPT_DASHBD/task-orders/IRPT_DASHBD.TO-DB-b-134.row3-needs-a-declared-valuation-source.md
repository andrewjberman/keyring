# TO IRPT_DASHBD.TO-DB-b-134 -- method_version_of refuses an entry that names a positions-based row and declares no valuation source

<to_id>IRPT_DASHBD.TO-DB-b-134</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~106</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>70</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2's ROUND-69 ANALYSIS `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_69_20261011.md` @90cb3e774b, section 4 item 4, answering `org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/remediations/REMEDIATION_v28.md` @595332678c | **Rows:** IRPT_DASHBD-D2-W103-S1 | **Decomp cell:** `DB-b-134` (decomposition section 72) | **outcome_ref:** FWD-11 | **depends_on:** DB-b-132 (the same producer file; it runs after it in the same worktree).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-106` (branch `wk-irpt-dashbd-70-106`, the worktree DB-b-132 used); run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~106/`. Read first: section 4 (item 4) of the analysis above, and each row named above in
`org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/remediations/REMEDIATION_v28.md` (the reviewer's statement of it) and in `org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md` (the original row).

**What is wrong.** `method_version_of` in `data/assets/scripts/gold/irpt_reporting/account_return_daily.py` refuses a `custodian_reported` entry that names method row 3,
but an entry that names row 3 and declares NO `valuation_source` is not refused (row W103-S1). The reworded income reason on row 3 is true of
a positions-based entry only, so an entry of unstated valuation must not be able to name it.

**The cell (`DB-b-134`).** This order runs in the worktree DB-b-132 used, on top of its commits.
1. In `method_version_of`: an entry whose `method_version` names a row whose `valuation_source` is NOT `custodian_reported`, and which
   declares no `valuation_source` (absent, null or blank), is REFUSED with a `SystemExit` whose text starts `REFUSED:` and says what to
   declare. An entry naming row 2 with no `valuation_source` is unchanged (it still returns 2); an entry with no `method_version` is still
   `absent`.
2. A test beside `tests/test_method_version_from_source.py` for the refusal and the two unchanged cases. `tests` {passed, failed}; the
   folder's tests must not newly fail. Both entries of `sources.json` must still resolve (2 and 3): run it and say so.
3. Record `ROW3_SOURCE_REFUSAL.json`: {refusal_text, line, entries_affected, tests}.

<criterion id="DB70-4-AC1" cell_refs="DB-b-134"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r70/p70_round70.py" . DB70-4-AC1</invocation><expect>DB70-4-AC1 PASS</expect></criterion>
`DB70-4-AC1` -- an entry naming a non-custodian method row with no declared valuation source is refused, and the two declared entries still resolve. Base: FAIL.

<expected_criteria>DB70-4-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No served write.** No S3 put, copy or delete; no Lambda, Terraform or IAM act; no `upload=True` call; no deploy; no push. No AWS call at all.
- **No client data in what you write.** Counts and booleans only: no account id, no client name, no figure of any client. Anything you
  download goes OUTSIDE the repo, under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~106/`.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. A result you could not establish is NOT_ESTABLISHED with its reason, never guessed. An edit outside the grant is a
  defect: stop and file a row.
- **Every `.py` edit passes `bash .tools/commit-gate.sh <file>`.** ASCII only.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W106-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~106/
data/assets/scripts/gold/irpt_reporting/account_return_daily.py
data/assets/scripts/gold/irpt_reporting/tests/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-134.row3-needs-a-declared-valuation-source.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 72 (round 70), cell `DB-b-134`.
<owned_cells>DB-b-134</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB70-4-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~106/IRPT_DASHBD.TO-DB-b-134.row3-needs-a-declared-valuation-source.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB70-4-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the refusal's text and the line it is raised at; which entries of sources.json it could affect (count); the tests; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; one refusal in the producer's entry reading; 0 of 2 declared entries are affected today.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the scheduled producer runs from its source-map pins, not from this branch.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record). The rows are the reviewer's and the CTO's statements; the issuer re-read none of their evidence for this issuance.
lane: the <paths> block IS the grant.
</preflight>
