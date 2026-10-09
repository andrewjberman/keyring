# TO IRPT_DASHBD.TO-DB-b-97 -- E3: the backfill path also calls record_lots_status with each landed day removed, so the lots status record never states a day as skipped once it has data (W69-S2)

<to_id>IRPT_DASHBD.TO-DB-b-97</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~72</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>47</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's R44 CTO half @fa8d2c2961 and ADDENDUM 13.1 (msg 3413), enrichment item E3 | **Decomp cell:** `DB-b-97` (decomposition section 49) | **outcome_ref:** FWD-4 | **depends_on:** DB-b-91 (drained).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-72`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~72/`.

**The cell (`DB-b-97`).** DB-b-91 added `record_lots_status` to `catch_up_lots` (the scheduled path) in
`C:/dev/wk-irpt-dashbd-72/infra/aws/lambda/investor-reporting/reporting-gold/handler.py`. Row W69-S2 found that `run_backfill` does not call it, so a
day refused on a scheduled fire and later landed by a backfill stays stated as "lots not computed". The CTO placed this cell (R44 CTO half,
enrichment item).

1. Make the backfill path call `record_lots_status` with every day it lands removed, and every day it refuses added with its reason. Use the
   same object, rules and failure handling as the scheduled path: a dry run writes nothing, and a status failure is logged by name and never
   raised.
2. Tests: a day stated by a refused scheduled fire is removed when a backfill lands it; a backfill-refused day is stated; every existing
   reporting-gold test still passes.
3. Record `BACKFILL_CLEARS.json` {tests: {passed, failed, new_test}}.

No deploy: this ships in a later release under its own pair.

<criterion id="DB47-3-AC1" cell_refs="DB-b-97"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r47/p47_round47.py" . DB47-3-AC1</invocation><expect>DB47-3-AC1 PASS</expect></criterion>
`DB47-3-AC1` -- the backfill path clears a landed day from the status record, tested. Base: FAIL.

<expected_criteria>DB47-3-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`.
- **This order's exception:** you edit the reporting-gold handler and its tests folder. No deploy.
- **AWS:** S3 reads only unless this face says otherwise. NO Black Diamond or vendor call, no secret read, no S3 write, no deploy, no bun,
  no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~72/
infra/aws/lambda/investor-reporting/reporting-gold/handler.py
infra/aws/lambda/investor-reporting/reporting-gold/tests/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-97.backfill-clears-status.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 49 (round 47), cell `DB-b-97`.
<owned_cells>DB-b-97</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB47-3-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~72/IRPT_DASHBD.TO-DB-b-97.backfill-clears-status.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB47-3-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the call site, the tests, and any row, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the reporting-gold handler's backfill path; it reaches the Lambda only in a later release under its own pair.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call; the status key is already in the role's write set.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB47-3-AC1 FAIL at base (no record; one call site). Row W69-S2; R44 CTO half enrichment item.
lane: the <paths> block IS the grant.
</preflight>
