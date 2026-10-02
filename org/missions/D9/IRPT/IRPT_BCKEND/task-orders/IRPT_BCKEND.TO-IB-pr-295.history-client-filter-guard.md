# TO IRPT_BCKEND.TO-IB-pr-295 -- The owner-read guard admits client_id on the history operation only, by an allowlist keyed by operation

<to_id>IRPT_BCKEND.TO-IB-pr-295</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~101</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-02</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>32</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** CTO RULINGS batch 154 item ITEM22-CLIENT-FILTER-IS-ADMITTED-BY-THE-GUARD
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/RULINGS.md`, @4b3e51674c, msg 104203: the guard's owner,
2.0.0_SA_COO~P, amends it) | **Decomp cell:** `IB-pr-295` (decomposition section 27 addendum note: round 32, one cell; row
IRPT_BCKEND-S267) | **outcome_ref:** FWD-9 (item 22, the request history filtered by client) | **depends_on:** IB-pr-293 (merged
@88480ab9d8; it last held `_authz/served.py`); queued on slot 101 after TO-IB-pr-294

---

## WORKER FACE

**The cell.** `infra/aws/lambda/investor-reporting/_authz/served.py` `_owner_read_request` (`:803-828`) refuses any issued owner
read whose query names `client_id` (`:815-818`, the list `input_id, account_ids, client_id, snapshot_id, account_set_id, owner,
principal_id, firm_id`). The history reader already applies `client_id` as a narrowing filter over the owner's own records
(`ops/owned_requests.py:219-252`), and the history route already passes it (`ops/entry.py:168-176`), but the guard refuses it first.
Admit `client_id` on the HISTORY operation only.

**What exists (read first).** `_authz/served.py` (`Entry.__init__` `:575-610`: `owner_read_modes`; `_owner_read_request`;
`_handle_owner_read`); `ops/entry.py:210-226` (the one production composition: `analysis-request-history` is
`CURRENT_OWNER_HISTORY`; `analysis-request-read`, `analysis-report`, `status-job` are `OWNED_RECORD`); `ops/owned_requests.py`
`history()`; existing tests for fixtures: `_authz/tests/test_owner_read_entry.py`, `ops/tests/test_history_client_scope.py`,
`ops/tests/test_owned_entry.py`.

**What you build.**
- In `served.py` only: an allowlist KEYED BY OPERATION that admits `client_id` on `analysis-request-history` and nothing else. Every
  other name in the refused list stays refused on every operation, and `client_id` stays refused on every other owner read. Never a
  renamed parameter (a filter that names a client is a client claim, whatever it is called).
- `_authz/tests/test_owner_history_client_filter.py`, through `served.Entry` (never the reader alone): for each client id read, an
  UNKNOWN one included, history(client_id) is a subset of history() by item id; an unknown client answers `items: []`. At least 3
  tests; name `client_id`, `Entry`, "subset" and "unknown".
- `_authz/tests/test_owner_read_client_refused.py`, through `served.Entry`: `client_id` refused on `analysis-request-read`,
  `analysis-report` and `status-job`, one negative arm each (name each operation).

<criterion id="IB32-1-AC1" cell_refs="IB-pr-295"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r32/p32_1_ac1_history_client_subset.py" .</invocation><expect>IB32-1-AC1 PASS</expect></criterion>
`IB32-1-AC1` -- the subset and unknown-client tests pass through `served.Entry` (at least 3, none failing). Base: FAIL (no file).

<criterion id="IB32-1-AC2" cell_refs="IB-pr-295"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r32/p32_1_ac2_client_refused_elsewhere.py" .</invocation><expect>IB32-1-AC2 PASS</expect></criterion>
`IB32-1-AC2` -- `client_id` refused on each of the three other owner reads (at least 3 tests, none failing). Base: FAIL (no file).

<criterion id="IB32-1-AC3" cell_refs="IB-pr-295"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r32/p32_1_ac3_suites_unchanged.py" .</invocation><expect>IB32-1-AC3 PASS</expect></criterion>
`IB32-1-AC3` -- `ops` and `directory` suites fail 0; `_authz` fails only the six baseline `test_unguarded_census` tests (each
suite in its own process). Base: PASS (a regression guard: served.py is shared, the change must be inert elsewhere).

<expected_criteria>IB32-1-AC1,IB32-1-AC2,IB32-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. `ops/entry.py` and
  `ops/owned_requests.py` are read only: a reader change the guard needs is a row, never an edit.
- **AWS:** none. Offline, fixtures only. No deploy: the served move rides irpt-status's next packet (2.0.0_SA_COO~Y).
- **Refusal clause.** An existing test that moves is a defect: stop and file a row, never edit the test.

<paths>
infra/aws/lambda/investor-reporting/_authz/served.py
infra/aws/lambda/investor-reporting/_authz/tests/test_owner_history_client_filter.py
infra/aws/lambda/investor-reporting/_authz/tests/test_owner_read_client_refused.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r32/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read without a grant (never written): `infra/aws/lambda/investor-reporting/` (all of it), `docs/contracts/investor-reporting/v1/`, `lib/`.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 27 addendum note (round 32, workstream ~P), cell `IB-pr-295`.
<owned_cells>IB-pr-295</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB32-1-AC1, IB32-1-AC2, IB32-1-AC3. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~101/IRPT_BCKEND.TO-IB-pr-295.history-client-filter-guard.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IB32-1-AC1,IB32-1-AC2,IB32-1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message: the commit hashes, each criterion's last line, the allowlist (file:line), and any surprise row id.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the shared served layer `_authz/served.py`; the one production composition with owner reads is irpt-status (`ops/entry.py:216`); AC3 holds the _authz, ops and directory suites; 0 served bytes move in the cell (the served move is irpt-status's next packet, 2.0.0_SA_COO~Y).
comp-iam: DECLARED-NOT-APPLICABLE -- no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- the history route is unchanged; it admits one more query name.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: a request-driven guard; no schedule, trigger or cron is created or moved.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- IB32-1-AC1 base FAIL (no file), IB32-1-AC2 base FAIL (no file), IB32-1-AC3 base PASS (regression guard: ops 208, directory 171, _authz 177 passed + the 6 baseline failures), dry-run at the base 2026-10-02 ~11:3xZ.
lane: the <paths> block IS the grant.
</preflight>
