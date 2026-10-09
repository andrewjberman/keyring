# TO IRPT_DASHBD.TO-DB-b-90 -- E1: the realized-lot uniqueness check moved to the FINAL rows, after every rewrite (the in-kind / wash-sale re-measure rewrites realized_gain), with one test where a rewrite creates a repeat the check catches (W62-S1)

<to_id>IRPT_DASHBD.TO-DB-b-90</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~65</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>44</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's ADDENDUM 11 (msg 3288; CVO ADJUDICATION_v25 @5f365678bf), enrichment item E1 | **Decomp cell:** `DB-b-90` (decomposition section 46) | **outcome_ref:** FWD-4 | **depends_on:** DB-b-87 (drained).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-65`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~65/`.

**The cell (`DB-b-90`).** DB-b-87 added `realized_gain` to the realized key. Its row W62-S1 found that `realized_rows()` checks the key BEFORE
the in-kind / wash-sale re-measure rewrites `realized_gain`, so uniqueness rests on `emit_day()`'s later duplicate check. The CTO ruled (ADDENDUM 11,
item 2) that the check runs on the FINAL rows.

1. In `C:/dev/wk-irpt-dashbd-65/data/assets/scripts/gold/irpt_reporting/account_activity_lots.py`, make the realized-key uniqueness check run on
   the final realized rows, after every rewrite. It refuses by name, as now ("identical in every column" and "key is not unique"). Record the
   function it lives in as `check_site`.
2. Add one test where a rewrite creates a repeat of the final key, and the check refuses it by name. Keep every existing lots test passing.
3. Record `FINAL_ROWS_UNIQ.json` {tests: {passed, failed, new_test}, check_site}.

No deploy: the change reaches the Lambda in a later release.

<criterion id="DB44-1-AC1" cell_refs="DB-b-90"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r44/p44_round44.py" . DB44-1-AC1</invocation><expect>DB44-1-AC1 PASS</expect></criterion>
`DB44-1-AC1` -- the uniqueness check runs on the final rows, and a test proves a rewrite-made repeat is refused. Base: FAIL.

<expected_criteria>DB44-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`.
- **This order's exception:** you edit the lots producer and its tests folder. No deploy.
- **AWS:** S3 reads only unless this face says otherwise. NO Black Diamond or vendor call, no secret read, no S3 write, no deploy, no bun,
  no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~65/
data/assets/scripts/gold/irpt_reporting/account_activity_lots.py
data/assets/scripts/gold/irpt_reporting/tests/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-90.final-rows-uniqueness.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 46 (round 44), cell `DB-b-90`.
<owned_cells>DB-b-90</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB44-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~65/IRPT_DASHBD.TO-DB-b-90.final-rows-uniqueness.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB44-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the check site, the new test, the test result, and any row, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- a producer/handler code change and tests; it reaches served output only through a later release under the R37 half; nothing deploys in this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call; no role change.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB44-1-AC1 FAIL at base (no record). Row W62-S1; CTO ADDENDUM 11 item 2.
lane: the <paths> block IS the grant.
</preflight>
