# TO IRPT_BCKEND.TO-IB-mr-1 -- Grade the R1 read-back of three HELD ledgers on the 2026-09-28 COT gold run

<to_id>IRPT_BCKEND.TO-IB-mr-1</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~41</issued_to>
<issued_by>2.0.0_SA_COO~M</issued_by>
<issued_date>2026-09-28</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>19</round>
<workstream>~M</workstream>

**Directive:** D9 | **Fabric:** laptop | **Workstream:** ~M | **Decomp cell:** `IB-mr-1` (`decompositions/IRPT_BCKEND_DECOMP_R19_M.md`) | **outcome_ref:** FWD-5 backend half, goal criterion 3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`IB-mr-1` -- three deploy-ledger entries authored by 2.0.0_SA_COO~M are HELD: their apply legs are proven and only
the verify leg `R1` is open. Each R1 reads the first scheduled COT gold run after its write. That run landed on
2026-09-28 (`s3://opal-data-cot/platinum/firm/mix_summary.json` LastModified 2026-09-28 11:36:20Z). Grade each R1 on
the SERVED output of that run, record the grade, and move each ledger to the state the grade implies.

The three entries (read each whole; its R1 row names what to read and what it expects):
1. `cot-other-admission-m-20260925` --
   `C:/Users/AndrewBerman/Desktop/ajb_workspace/org/critical_paths/change_management/20260925T2031Z_cot-other-admission-m-20260925_deploy_completion.md`.
   R1 expects: C_06's mix carries an `other` key (value 0 is correct, since batch B is not written), and D_03 compositions
   show `unclassified` in place of `other` for unknown rows.
2. `cot-cash-admission-m-20260925` --
   `C:/Users/AndrewBerman/Desktop/ajb_workspace/org/critical_paths/change_management/20260925T2343Z_cot-cash-admission-m-20260925_deploy_completion.md`.
   R1 expects: relationship z09308463 (0.37 cash at 09-22) shows a cash slice at its measured amount with shares summing
   to 1; all-cash z09326138 or z09308511 shows 100% cash.
3. `bd-securities-cot-new-p1-m-20260926` --
   `C:/Users/AndrewBerman/Desktop/ajb_workspace/org/critical_paths/change_management/20260926T0321Z_bd-securities-cot-new-p1-m-20260926_deploy_completion.md`.
   R1 expects: COT's mix moves equity -> fixed_income/alternatives per the signed half (+NEOS $149,663 to fixed_income),
   and BD's next C_06 run moves 652 accounts per the half. The half and its measured deltas:
   `.../IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_COT_NEW_WRITE_20260926.md`, `.../IRPT_MVP_M/A07_DELTA_COT_NEW_20260926.json`,
   receipt `.../IRPT_MVP_M/BD_SECURITIES_COT_NEW_P1_RECEIPT_20260926.json`.

Where the served output lives (COT, bucket `opal-data-cot`): firm composition `gold/views/firm_composition.json`;
relationship compositions `gold/entities/clients/<zid>_composition.json`; firm mix `platinum/firm/mix_summary.json`.
`C:/Users/AndrewBerman/Desktop/ajb_workspace/org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/cot_served_composition_check.py --out <json>`
reads every served composition (runbook A.2); write its output to
`.../IRPT_MVP_M/COT_SERVED_COMPOSITION_POSTRUN_20260928.json`. For BD, find the served C_06 output of BD's most recent
trading-day run in `opal-data-bd` from `C:/Users/AndrewBerman/Desktop/ajb_workspace/data/black_diamond/scripts/gold/`'s
C_06 script (read its write key); if BD has not run since 2026-09-26T03:21Z, that leg's BD half is FAIL with the
run time you measured.

### KNOWN HAZARD (read before grading)

Surprise row `IRPT_BCKEND-S173` (ARMED, in the investigation file below) says the COT gold host role
`cot-exporter-ec2-role` cannot read DynamoDB `bd-securities`, so COT gold classifies with empty maps. Legs that depend on
the table (item 3, and any classification in item 1) may FAIL for that reason. Grade what the served bytes show and
name S173 as the cause only if the run's own evidence shows it (a gold log line, or the classification the output
carries). Never fix the grant, re-run gold, or write any served object: this cell READS and GRADES.

### BUILD

1. For each entry, read the served objects its R1 names (record `s3://` uri + VersionId + LastModified of each), compare
   to the expectation, and set `verdict` PASS or FAIL.
2. Write `R19_R1_READBACK_20260928.json` with `{"legs": [{"slug", "verdict", "expected", "measured", "served_objects":
   [{"uri", "version_id", "last_modified"}], "run_evidence", "surprise_row"}]}` -- `run_evidence` names what proves the
   object came from the 09-28 run; `surprise_row` is required on a FAIL.
3. PASS: `python .tools/deploy_ledger.py close-leg --slug <slug> --leg-id R1 --proof "<one line: measured vs expected,
   uri@version>"`, then `python .tools/deploy_ledger.py close --slug <slug>`.
   FAIL: leave the ledger as it is (HELD, R1 unproven) and append ONE surprise row per failed leg to the investigation
   file (`spec_asserts` = the R1 expectation, `world_is` = the measured value), id `IRPT_BCKEND-W41-S<k>`.
4. Commit through `.tools/safe-commit.sh` with the files in `<paths>` (the sentinels that close are deletions).

### ACCEPTANCE

<criterion id="IBM19-1-AC1" cell_refs="IB-mr-1"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R19_CHECKS/r19_m1_r1_verdicts.py</invocation><expect>R1-GRADED followed by each of the three slugs with PASS or FAIL</expect></criterion>
`IBM19-1-AC1` -- each R1 is graded on served objects of the 09-28 run, with uri + VersionId per object.

<criterion id="IBM19-1-AC2" cell_refs="IB-mr-1"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R19_CHECKS/r19_m1_ledger_agrees.py</invocation><expect>AGREES followed by the same three slug=verdict pairs as IBM19-1-AC1</expect></criterion>
`IBM19-1-AC2` -- each ledger's state agrees with its grade (PASS closed, FAIL held with a surprise row).

<expected_criteria>IBM19-1-AC1,IBM19-1-AC2</expected_criteria>

Both checks run from your worktree root and exit 1 at the base (dry-run 2026-09-28 18:1xZ: MISSING / DISAGREES).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Read-only everywhere
  else, including all of AWS: no S3 write, no DynamoDB write, no gold run, no IAM change.
- **No merge, no deploy.** The COT cash-line, S155, B1 and B_01b branches are not yours to touch.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise
  row, and do not weaken the test to pass.

<paths>
org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R19_R1_READBACK_20260928.json
org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/COT_SERVED_COMPOSITION_POSTRUN_20260928.json
org/critical_paths/change_management/20260925T2031Z_cot-other-admission-m-20260925_deploy_completion.md
org/critical_paths/change_management/20260925T2343Z_cot-cash-admission-m-20260925_deploy_completion.md
org/critical_paths/change_management/20260926T0321Z_bd-securities-cot-new-p1-m-20260926_deploy_completion.md
org/critical_paths/.open_deploys/cot-other-admission-m-20260925.json
org/critical_paths/.open_deploys/cot-cash-admission-m-20260925.json
org/critical_paths/.open_deploys/bd-securities-cot-new-p1-m-20260926.json
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named on this face (the half, the receipts, the composition check,
the checks in `R19_CHECKS/`, the gold scripts) you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R19_M.md</decomp_doc> (round 19, workstream ~M), cell `IB-mr-1`.
<owned_cells>IB-mr-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IBM19-1-AC1, IBM19-1-AC2. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~41/IRPT_BCKEND.TO-IB-mr-1.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IBM19-1-AC1,IBM19-1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** per slug the verdict, the measured value beside the expected one, and the surprise
row id of each FAIL; the commit hash.

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- the COT gold run of 2026-09-28 landed: platinum/firm/mix_summary.json LastModified 11:36:20Z (head-object 17:5xZ).
comp-iam: DECLARED-NOT-APPLICABLE -- read-only on AWS; no policy changes.
comp-adversary: RUN -- S173 (ARMED) predicts the table-dependent legs FAIL; the face tells the worker to grade the bytes and cite the run's own evidence, never the prediction.
lane: the <paths> block IS the grant; no open order holds these files.
</preflight>


Source: `STATUS~M.md` @e589729e6a next-list item 1; runbook `IRPT_MVP_M/MONDAY_20260928_RUNBOOK.md` A.1-A.2.
