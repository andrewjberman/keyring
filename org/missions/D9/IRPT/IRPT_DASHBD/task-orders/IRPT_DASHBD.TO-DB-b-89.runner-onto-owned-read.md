# TO IRPT_DASHBD.TO-DB-b-89 -- E1: re-cut the Performance client statement runner onto IRPT_BCKEND's owned read IB-pr-405 (persist_inputs) -- run, verify-submission and verify-persisted read through the route, never irpt-requests; a fixture run with table access removed; 0 direct table clients

<to_id>IRPT_DASHBD.TO-DB-b-89</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~64</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's ADDENDUM 10.1 (msg 3257), enrichment item E1 | **Decomp cell:** `DB-b-89` (decomposition section 45) | **outcome_ref:** FWD-12 | **depends_on:** IB-pr-405 drained @2f6fe31ad8.

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-64`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~64/`.

**The cell (`DB-b-89`).** DB-b-85's runner
`C:/dev/wk-irpt-dashbd-64/data/assets/scripts/gold/irpt_custody/e2a_real_statement.py` reads `artifact_id`, the composition hash, the retention
policy and the report index straight from the DynamoDB table `irpt-requests`. The issuer measured 7 direct table references at base.

The CTO ruled (ADDENDUM 9.2) that no executor gets a direct table grant. IRPT_BCKEND built the owned read **IB-pr-405 `persist_inputs`**,
which returns `artifact_id`, `composition_sha256`, the retention policy and the persisted report index, re-authorized per request. It is
drained @2f6fe31ad8; read its code and contract in that commit, and in `~P2`'s drain-end packet for rounds 106 and 108.

1. **Re-cut the runner** so `run`, `verify-submission` and `verify-persisted` take those values from the owned route. Call it as
   `svc-custody-statement`, with the same token handling as now. Remove every `irpt-requests` / `dynamodb` / `get_item` / `query` / `Table(`
   use.
   - `verify-submission` still prints `SUBMISSION RETAINED policy=<policy> ref=<ref>`, with the policy read from the route.
   - `verify-persisted` still prints `PERSISTED kind=CUSTODY_REPORT revision=<n> ref=<ref>`.
2. **Fixture test.**
   - Record the route's response shape as a fixture file. Take it from IB-pr-405's contract and tests; do not invent fields.
   - Add a test that runs `run`, then both verifies, against that fixture, with the environment's DynamoDB access removed (for example
     boto3's dynamodb client patched to raise). It must pass.
   - Keep the existing no-identity / no-figure tests passing.
3. Record `RUNNER_RECUT.json` {tests: {passed, failed, fixture_test}, fixture (path), table_access_removed: true}.

**No live call and no AWS write.** DB-b-86 runs the live statement only after the issuer reads IB-pr-405 LIVE and the mint's leg R closed.

<criterion id="DB43-1-AC1" cell_refs="DB-b-89"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r43/p43_round43.py" . DB43-1-AC1</invocation><expect>DB43-1-AC1 PASS</expect></criterion>
`DB43-1-AC1` -- the built runner holds 0 direct table clients. Base: FAIL.

<criterion id="DB43-1-AC2" cell_refs="DB-b-89"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r43/p43_round43.py" . DB43-1-AC2</invocation><expect>DB43-1-AC2 PASS</expect></criterion>
`DB43-1-AC2` -- a fixture run of run and both verifies passes with irpt-requests access removed. Base: FAIL.

<expected_criteria>DB43-1-AC1,DB43-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`.
- **This order's exception:** you edit the runner and its tests folder named in `<paths>`. No IRPT_BCKEND code, no live call, no AWS write.
- **AWS:** S3 reads only unless this face says otherwise. NO Black Diamond or vendor call, no secret read, no S3 write, no deploy, no bun,
  no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~64/
data/assets/scripts/gold/irpt_custody/e2a_real_statement.py
data/assets/scripts/gold/irpt_custody/tests/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-89.runner-onto-owned-read.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 45 (round 43), cell `DB-b-89`.
<owned_cells>DB-b-89</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB43-1-AC1, DB43-1-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~64/IRPT_DASHBD.TO-DB-b-89.runner-onto-owned-read.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB43-1-AC1,DB43-1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the route calls the runner now makes, the fixture, the test result, the table-reference count, and any row, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: an offline runner re-cut and its fixture test; nothing runs live in this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call; the cell removes the runner's need for a table grant.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: the runner calls IB-pr-405's existing owned route; no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB43-1-AC1 FAIL at base (7 direct table references); DB43-1-AC2 FAIL (no record). CTO ADDENDUM 10.1.
lane: the <paths> block IS the grant.
</preflight>
