# TO IRPT_DASHBD.TO-DB-b-93 -- E1: the statement runner accepts the seat-authored selection FILE -- account_set_id is derived the API's own way if the API derives it deterministically, otherwise the statement path takes the file without an id and records selection_source: file with its sha256 (S43)

<to_id>IRPT_DASHBD.TO-DB-b-93</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~68</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>45</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's ADDENDUM 11.1 (msg 3362, @43bbe32935), enrichment item E1 | **Decomp cell:** `DB-b-93` (decomposition section 47) | **outcome_ref:** FWD-12 | **depends_on:** none.

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-68`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~68/`.

**The cell (`DB-b-93`).** The runner `C:/dev/wk-irpt-dashbd-68/data/assets/scripts/gold/irpt_custody/e2a_real_statement.py` requires the
selection's `account_set_id` as `sel_<64 hex>` (`load_selection`). It sends that id as the `account_set_id` query parameter of
`POST /api/scoped/investor-reporting/analysis` (around line 314).

Only an Opal operator's selection-create answer produces that id, and the CTO refused an operator seat minting it (ADDENDUM 11.1 item 1;
ADDENDUM 9.2). The selection stays a seat-authored FILE: client_id, account_ids and snapshot_id, from two served reads (row S43).

1. **Find out whether `sel_<64 hex>` is deterministic.** Read the backend code that creates a selection and the code that validates
   `account_set_id` on POST /analysis, under `C:/dev/wk-irpt-dashbd-68/infra/aws/lambda/investor-reporting/`. Decide whether the id is a
   deterministic hash of the selection's own fields, or random or stored.
   - **If deterministic:** make the runner compute it the same way from the file. Record the API function as `derivation_site`
     ("<file>::<function>"). Have the runner print both inputs and the derived id to its output for the ledger.
   - **If not deterministic:** make the statement path take the file without an id, and record `selection_source: file` and the selection
     file's sha256 in the refs. If the route refuses a submission without a valid stored id, file a row naming the route and the check, and
     keep the runner change.
2. **Tests** for the branch you took: a file without `account_set_id` is accepted, and a malformed file is still refused by name. Keep every
   existing runner test passing.
3. Record `SELECTION_FILE.json` {deterministic, derivation_site (when deterministic), evidence (the file:line you read), tests: {passed,
   failed, new_test}}.

**No live call, no AWS write, no backend edit.** DB-b-86 runs the real statement later, after the Cottonwood returns gold lands (ADDENDUM
11.1 item 2).

<criterion id="DB45-1-AC1" cell_refs="DB-b-93"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r45/p45_round45.py" . DB45-1-AC1</invocation><expect>DB45-1-AC1 PASS</expect></criterion>
`DB45-1-AC1` -- the runner accepts the seat-authored selection file, by derivation or by recorded file source, with tests. Base: FAIL.

<expected_criteria>DB45-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`.
- **This order's exception:** you edit the runner and its tests folder. You READ backend code under infra/ and edit none of it. No live call.
- **AWS:** S3 reads only unless this face says otherwise. NO Black Diamond or vendor call, no secret read, no S3 write, no deploy, no bun,
  no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~68/
data/assets/scripts/gold/irpt_custody/e2a_real_statement.py
data/assets/scripts/gold/irpt_custody/tests/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-93.runner-selection-file.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 47 (round 45), cell `DB-b-93`.
<owned_cells>DB-b-93</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB45-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~68/IRPT_DASHBD.TO-DB-b-93.runner-selection-file.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB45-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the deterministic finding with its file:line, the branch taken, the tests, and any row, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: an offline runner change and tests; nothing runs live in this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call; no role change.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: the backend routes are read, not changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB45-1-AC1 FAIL at base (no record). Row S43; CTO ADDENDUM 11.1 item 1.
lane: the <paths> block IS the grant.
</preflight>
