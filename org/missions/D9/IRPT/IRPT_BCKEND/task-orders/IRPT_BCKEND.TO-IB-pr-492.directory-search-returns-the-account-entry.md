# TO IRPT_BCKEND.TO-IB-pr-492 -- the directory search producer returns the ACCOUNT entry when the query matches an account's tail (row DSGN_IRPTV1-D2-S28)

<to_id>IRPT_BCKEND.TO-IB-pr-492</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~343</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>170</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's routing of row `DSGN_IRPTV1-D2-S28` (CTO msg 6665; DSGN_IRPTV1 ROUND-31 ANALYSIS section 2a) and the CTO ROUND-170 ANALYSIS section 4 (msg 6739) | **Decomp cell:** `IB-pr-492` (decomposition section 162) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Cell `IB-pr-492` (inlined):** a client search whose query matches the LAST FOUR digits of an account today returns a relationship-kind entry (the entry-level `masked_discriminator` is the HEAD account's mask), so a pick starts Performance on the relationship's largest account, not the one typed; a tail of a non-head account matches nothing. The producer, which knows which account matched, must return that ACCOUNT's entry. **BUILD ONLY: no deploy, no AWS call.** Edit ONLY `infra/aws/lambda/investor-reporting/directory/handler.py` (module `irpt-directory-search`; pure functions, no I/O) and add ONE new test file `infra/aws/lambda/investor-reporting/directory/tests/test_tail_account_entry.py`. Read first: `handler.py` `project` (:121), `_score` (:153), `search` (:171), `resolve` (:236), `_entry_key` (:99); `_contracts/DirectoryEntry.schema.json` (`account_masks`: one `{account_id, masked_discriminator}` per account, optional; `permitted_scope.scope_kind` already admits `ACCOUNT`); the existing tests `directory/tests/test_handler.py` and `fixtures.py`.

**Behaviour to build (all of it, as written):**
1. A pure helper that, for a PROJECTED entry carrying `account_masks`, yields one synthesized ACCOUNT-kind entry per permitted account in its masks: `ids` = the entry's ids without `relationship_id` and with `account_ids` = that one account; `masked_discriminator` = that account's own mask; `permitted_scope` = `{scope_kind: "ACCOUNT", scope_ids: [that account]}`; `permitted_account_ids` = [that account]; `scope_completeness` `WHOLE`; `withheld_account_count` 0; `entry_id` = `_entry_key` of the synthesized entry; `display_name` unchanged.
2. `search`: when a query token matches an account's mask (the same token / substring rule `_score` uses for the discriminator), that ACCOUNT entry is a result (one per matching permitted account; two accounts sharing a tail give TWO results, each with its own `entry_id`; the existing `ambiguous` rule then reads honestly). A relationship entry that carries `account_masks` is returned only when the query matches its NAME (the discriminator no longer matches at the entry level for such an entry; the ACCOUNT entries carry that match). An entry with NO `account_masks` behaves exactly as today.
3. `resolve`: `selection.entry_id` of a synthesized ACCOUNT entry resolves to exactly that one account (`ok` true, `account_ids` = [that account]); every other selection form and the relationship entry's own `entry_id` are unchanged (a relationship still reaches all its accounts).
4. No schema change, no change to `entry.py`, no other module. The result shape of `search` is unchanged (`scope_kind` reads `ACCOUNT` for these results).

**Your new test file** carries at least SIX arms: tail of a non-head account; two accounts sharing a tail; the head tail; a name query returning the relationship entry only; an entry without masks unchanged; resolve of a synthesized entry id and the relationship's own resolve. Use synthetic opaque ids only.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB170-1-AC1" cell_refs="IB-pr-492"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r170/p170_cells.py" . IB170-1-AC1</invocation><expect>IB170-1-AC1 PASS</expect></criterion>
<criterion id="IB170-1-AC2" cell_refs="IB-pr-492"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r170/p170_cells.py" . IB170-1-AC2</invocation><expect>IB170-1-AC2 PASS</expect></criterion>
<criterion id="IB170-1-AC3" cell_refs="IB-pr-492"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r170/p170_cells.py" . IB170-1-AC3</invocation><expect>IB170-1-AC3 PASS</expect></criterion>

<expected_criteria>IB170-1-AC1, IB170-1-AC2, IB170-1-AC3</expected_criteria>

What the checks grade: AC1 your new test file passes (6 or more, none failed); AC2 the issuer's seam probe on a synthetic directory (a tail of a non-head account shared by two entries gives two ACCOUNT results and no relationship result and each resolves to its own account; the head tail gives its ACCOUNT result; a name query gives the relationship entry only; an entry with no masks is found as before; the relationship's own resolve still reaches all its accounts); AC3 no EXISTING directory test file changed, and the existing suite is no worse than base (173 passed, 10 failed, 28 errors there: pre-existing, not yours). Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block and nothing else. No deploy, no AWS call, no source-map edit, no schema edit, no edit of an existing test.
- **Refusal clause:** STOP, file a row, change nothing more, if the behaviour cannot be built without changing `entry.py`, a schema or an existing test, or if `account_masks` is not present on the projected entries the handler receives (say what shape it receives).
- **Row ids** are `IRPT_BCKEND-D2-W343-S<k>` (the next free `k`).
- **Commit** on your worktree branch per your definition; ASCII only. Report once, under 150 words.

<paths>
infra/aws/lambda/investor-reporting/directory/handler.py
infra/aws/lambda/investor-reporting/directory/tests/test_tail_account_entry.py
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~343/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-492.directory-search-returns-the-account-entry.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 162 (round 170, workstream ~P), cell `IB-pr-492`.
<owned_cells>IB-pr-492</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB170-1-AC1, IB170-1-AC2, IB170-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~343/IRPT_BCKEND.TO-IB-pr-492.directory-search-returns-the-account-entry.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- one pure module of `irpt-directory-search` and one new test file; BUILD ONLY, no deploy: no resource, role, route or served artifact is touched by this order. The module's APPLY is a later order under its own never-widen pair (a served behaviour change).
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched (`directory/search` and `directory/resolve` keep their shapes).
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p170_cells.py dry-run at base on dell2 2026-10-13 ~02:2xZ: IB170-1 AC1 FAIL (no test file), AC2 FAIL (a tail query returns nothing), AC3 PASS (a bound: the existing directory suite reads 173 passed, 10 failed, 28 errors). AC2 also run against a throwaway reference implementation: PASS.
lane: the paths block IS the grant; worker slot ~343 of IRPT_BCKEND. Class WORLD (the `infra/` floor).
</preflight>
