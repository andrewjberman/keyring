# TO IRPT_DASHBD.TO-DB-b-23 -- the published route inventory declares both live reporting routes (row S23; round-15 E3)

<to_id>IRPT_DASHBD.TO-DB-b-23</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~9</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-05</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>15</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** 1.0.0_SA_CTO round-15 analysis, item E3
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_IRPT_DASHBD_ROUNDS_12_14_B_20261005.md` @b09cafb7a4, msg 105203) |
**Decomp cell:** `DB-b-23` (decomposition section 15) | **outcome_ref:** FWD-9 | **depends_on:** none.

---

## WORKER FACE

**Row S23.** `docs/contracts/investor-reporting/v1/routes.json` declares 19 routes. Its own note says every route the product needs
is covered, yet it omits both live reporting routes:
- `GET .../reporting/{account_id}/{which}`;
- `GET .../reporting/client/{client_id}/summary`.

Both are declared in `infra/aws/lambda/investor-reporting/reporting/entry.py` (`:92`, `:373`), live behind
`irpt-49f-reporting-read-lambda`, and called by PROD portal v2.1.197. The `_authz` unguarded census reads this file, so it cannot see
them.

Your worktree is `C:/Users/AndrewBerman/Desktop/wk-irpt-dashbd-9`; run everything from its root.

1. Read `reporting/entry.py` around `:92` and `:373` for the exact path templates and the guard each route runs. Then add two route
   objects to `routes` in the same shape as the existing rows: `route_key` with the full path as the gateway names it, `handler`
   `irpt-49f-reporting-read-lambda`, `status`, `note`, `operation` and the schema fields where the entry declares them. The note
   names the guard.
2. Update `_denominator` to the new count (21), and any other count the file states.
3. Run `infra/aws/lambda/investor-reporting/_authz/tests/test_unguarded_census.py`. If the census now reads a route without a
   guard, that is a real finding: file a row. Do not weaken the census.

<criterion id="DB15-1-AC1" cell_refs="DB-b-23"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r15/p15_cells.py" . DB15-1-AC1</invocation><expect>DB15-1-AC1 PASS</expect></criterion>
`DB15-1-AC1` -- both reporting routes are declared on irpt-49f-reporting-read-lambda, and `_denominator` names the new count. Base: FAIL.

<criterion id="DB15-1-AC2" cell_refs="DB-b-23"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r15/p15_cells.py" . DB15-1-AC2</invocation><expect>DB15-1-AC2 PASS</expect></criterion>
`DB15-1-AC2` -- the census that reads the file passes with 0 failed. Base: PASS.

<expected_criteria>DB15-1-AC1,DB15-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below.
- **AWS:** none. Docs and contract inventory only.
- **Refusal clause.** A change to `reporting/entry.py`, to the census or to any guard is out of scope: file a row.

<paths>
docs/contracts/investor-reporting/v1/routes.json
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~9/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-23.routes-json-reporting-routes.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 15 (round 15, workstream B), cell `DB-b-23`.
<owned_cells>DB-b-23</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB15-1-AC1, DB15-1-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~9/IRPT_DASHBD.TO-DB-b-23.routes-json-reporting-routes.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB15-1-AC1,DB15-1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message gives the commit hashes, the two route_keys and guards you declared, each criterion's last line, and
any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a contract inventory file; 0 served bytes move.
comp-iam: DECLARED-NOT-APPLICABLE -- no role changes.
comp-routes: RUN -- the two routes are READ from reporting/entry.py and declared; no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB15-1-AC1 base FAIL (routes absent), DB15-1-AC2 base PASS (regression), dry-run at base 53acc6abb8 2026-10-05 ~07:3xZ.
lane: the <paths> block IS the grant.
</preflight>
