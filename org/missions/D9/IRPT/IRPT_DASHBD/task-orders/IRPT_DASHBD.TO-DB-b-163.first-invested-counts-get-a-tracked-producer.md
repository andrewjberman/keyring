# TO IRPT_DASHBD.TO-DB-b-163 -- round 84's counts get a tracked producer: the scripts that made FLOW_DAYS_FIRST_INVESTED.json are tracked, lint-clean and free of client literals, and a re-run of the tracked copies reproduces the counts

<to_id>IRPT_DASHBD.TO-DB-b-163</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~131</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>85</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the issuer, 2.0.0_SA_COO~D2, inside its own decomposition, applying 1.0.0_SA_CTO~DELL2's round-77 rule (a figure with no tracked producing script is withdrawn; row IRPT_DASHBD-D2-W118-S1) | **Rows:** IRPT_DASHBD-D2-W118-S1 | **Decomp cell:** `DB-b-163` (decomposition section 87) | **outcome_ref:** FWD-8 / C-FLOWTIME | **depends_on:** DB-b-162 (drained @b096352faa).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-131` (branch `wk-irpt-dashbd-85-131`); run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~131/`. Read first: the records this order names.

**Why.** DB-b-162 counted when deposited cash was first invested on 88 deposit days (record
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~131/FLOW_DAYS_FIRST_INVESTED.json`). Its scripts stayed private because the tracked copies
failed the lint gate. By the CTO's standing rule on this tie-out a figure with no tracked producing script is not quotable. This cell
closes that, by the serial that owns the folder.

**The cell (`DB-b-163`).** You change NO count, NOT the rule and NOT the record.
1. Copy the counting scripts from `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~131/` into
   `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~131/producers/`. Make them pass `bash .tools/commit-gate.sh <file>` (py_compile, the
   pre-commit check, ruff for Python 3.9) by FORMAL edits only (imports, line length, unused names, naming): no change to a filter, a
   threshold, a join or a date rule. Private inputs are read by PATH (a constant naming the private folder is fine); no account id,
   amount, security name or any run of 8 or more digits may appear in a tracked script (a dated folder name is such a run: build the
   path from parts, or take it from an argument or an environment variable, and say which).
2. RE-RUN the TRACKED copies on the private copy of the data and compare with the record: `rerun` {from_tracked_copies: true,
   counts_equal_record (bool), classes (the five counts as re-run), splits (deposit, withdrawal, other as re-run)}. If the re-run does
   NOT reproduce the record, do not touch the record: report both sets of counts, file a row, and leave the order `issued`.
3. Confirm `RULE.md` is byte-identical to what the record names: `rule_sha256`.
4. Record `PRODUCERS.json`: {scripts: [{file (the name under producers/), sha256, does}], rerun, rule_sha256, client_literals: 0,
   formal_edits (a list, one line each)}.

<criterion id="DB85-1-AC1" cell_refs="DB-b-163"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r85/p85_round85.py" . DB85-1-AC1</invocation><expect>DB85-1-AC1 PASS</expect></criterion>
`DB85-1-AC1` -- the producing scripts are tracked at recorded bytes, compile, hold no long digit run, and a re-run of the tracked copies reproduces the record's classes with the rule's bytes unchanged. Base: FAIL.

<expected_criteria>DB85-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No served write.** No S3 put, copy or delete; no Lambda, Terraform or IAM act; no `upload=True` call; no deploy; no push. No AWS call is needed: re-run on the private copy the first run saved. If the private copy is incomplete, the reads DB-b-162 allowed are allowed again, the same way, and you say so.
- **No client data in what you write.** Counts and booleans only: no account id, no client name, no figure of any client. Anything you
  download goes OUTSIDE the repo, under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~131/`.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. A result you could not establish is NOT_ESTABLISHED with its reason, never guessed. An edit outside the grant is a
  defect: stop and file a row.
- **Every `.py` edit passes `bash .tools/commit-gate.sh <file>`.** ASCII only.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W131-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~131/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-163.first-invested-counts-get-a-tracked-producer.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 87 (round 85), cell `DB-b-163`.
<owned_cells>DB-b-163</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB85-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~131/IRPT_DASHBD.TO-DB-b-163.first-invested-counts-get-a-tracked-producer.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB85-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the scripts tracked, with what each does in a line; what you changed to make them pass the gate and that the logic is unchanged; the re-run's classes beside the record's; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; scripts added beside a record; no count changes, nothing served.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; none, or the governed reads of DB-b-162.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the scheduled producer runs from its source-map pins, not from this branch.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record). The rows are the reviewer's and the CTO's statements; the issuer re-read none of their evidence for this issuance.
lane: the <paths> block IS the grant.
</preflight>
