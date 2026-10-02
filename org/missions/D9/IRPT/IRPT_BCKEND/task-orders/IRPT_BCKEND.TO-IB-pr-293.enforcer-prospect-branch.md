# TO IRPT_BCKEND.TO-IB-pr-293 -- The Enforcer's prospect branch: a stored prospect grant admits exactly its four artifact keys, owner re-resolved at read time, no accounts

<to_id>IRPT_BCKEND.TO-IB-pr-293</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~101</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-02</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>30</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** CTO round-28 ~P analysis ADDENDUM 1, cell E5
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_ROUND_28_P_20261002.md`, batch 143 @11340658da, msg 104177);
row IRPT_BCKEND-W101-S4 | **Decomp cell:** `IB-pr-293` (decomposition section 27 addendum note: round 30, one cell; row IRPT_BCKEND-S267) | **outcome_ref:** FWD-9 (hop 12) |
**depends_on:** IB-pr-291 (merged @dff84e882f)

---

## WORKER FACE

**The cell.** IB-pr-291 builds and stores a PROSPECT render grant (`account_ids == []`, a `prospect_scope` record). The Enforcer's
RENDER_DELEGATE read (`infra/aws/lambda/investor-reporting/_authz/enforce.py` `_resolve_render_delegate`, `:408-576`) intersects the
delegator's permitted accounts with the grant's `account_ids` and refuses `EMPTY_GRANT` on the empty list (`:550-556`), so no prospect
render can run. Give the Enforcer a prospect branch.

**What exists (read first).**
- `_authz/enforce.py`: `_resolve_render_delegate` (the bundle load `:464-466`, the path-id pin `:487-496`, the intersection and the
  fingerprint `:548-576`); `covers` (`:578-670`; note `:658-670`: an artifact whose `account_ids` is empty passes for any viewer in
  the firm -- the prospect branch must not lean on that); `OBJECT_KINDS` (`:207`).
- `_render_identity/grant.py`: `PROSPECT_ROLES` (report, sections, composition, vendor_pdf), `_PROSPECT_SCOPE_FIELDS`, `read()`
  (`:245-275`, re-checks a stored prospect scope), `render_ports()` (`:277-300`: `load_render_bundle` today returns only
  `account_ids`, `bundle_id`, `pinned_ids` -- the prospect scope never reaches the Enforcer).
- `_authz/served.py:745` (unpacks `render_ports(tenant)` as a 2-tuple); `_scope/prospect.py:22` `resolve_prospect_owner`;
  `export/retained_export.py:38` `authorizer` (the exact-owner rule: same principal, firm, advisor and home firm).
- Existing tests to keep green and read for fixtures: `_authz/tests/test_render_delegate_pins.py`, `_authz/tests/test_enforce.py`,
  `_render_identity/tests/test_grant.py`, `_render_identity/tests/test_grant_prospect.py`.

**What you build (each line binds; it is the CTO's contract).**
1. TYPED, NEVER INFERRED. The Enforcer takes the prospect branch only when the loaded grant carries the stored prospect scope,
   re-checked as `grant.read()` re-checks it (pass the scope through `render_ports`). A grant with no prospect scope and an empty
   `account_ids` still refuses `EMPTY_GRANT`, exactly as today.
2. EXACT OWNER, AT READ TIME. The delegator resolved NOW must be the report's owner; a changed, revoked or other-firm owner is
   refused by name. The grant's stamp alone is not enough. An owner source the Enforcer cannot read refuses (fail closed).
3. NO ACCOUNTS. The rendered scope's `permitted_account_set` stays `[]`. `covers` admits exactly the four artifact keys the grant
   pins for that report id and revision; every account, account set, advisor, other report's key or prefix is refused.
4. ITS OWN CACHE KEY. The fingerprint folds in a PROSPECT class marker and the report revision (the `:570` pattern), never colliding
   with a RENDER_DELEGATE account fingerprint. `_scope/resolve.py` is NOT touched.
- Tests: `_authz/tests/test_enforce_prospect_admit.py` -- at least 7 tests: an admit for each of the four roles (name each role:
  report, sections, composition, vendor_pdf), and refusals of a foreign artifact (say "foreign"), another report's key and an account
  object. `_authz/tests/test_enforce_prospect_refuse.py` -- at least 2 tests: no prospect scope + empty `account_ids` reads
  `EMPTY_GRANT`; a prospect grant whose owner no longer resolves is refused (say "owner").

<criterion id="IB29-3-AC1" cell_refs="IB-pr-293"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r29/p29_3_ac1_prospect_admits.py" .</invocation><expect>IB29-3-AC1 PASS</expect></criterion>
`IB29-3-AC1` -- the admit file names the four roles and "foreign"; at least 7 tests pass, none failing. Base: FAIL (no file).

<criterion id="IB29-3-AC2" cell_refs="IB-pr-293"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r29/p29_3_ac2_prospect_refusals.py" .</invocation><expect>IB29-3-AC2 PASS</expect></criterion>
`IB29-3-AC2` -- the refusal file names `EMPTY_GRANT` and "owner"; at least 2 tests pass, none failing. Base: FAIL (no file).

<criterion id="IB29-3-AC3" cell_refs="IB-pr-293"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r29/p29_3_ac3_suites_unchanged.py" .</invocation><expect>IB29-3-AC3 PASS</expect></criterion>
`IB29-3-AC3` -- `export`, `holdings` and `_render_identity` suites fail 0; `_authz` fails only the six `test_unguarded_census` tests
that already fail at the base (each suite in its own process). Base: PASS (a regression guard; it grades that nothing moved).

<expected_criteria>IB29-3-AC1,IB29-3-AC2,IB29-3-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. In `grant.py`, only `render_ports`
  (passing the prospect scope through); in `served.py`, only the port wiring at `:745` if the port shape changes.
- **AWS:** none. Offline, fixtures only. No write, no deploy, no invoke.
- **Refusal clause.** An existing test that moves is a defect: stop and file a row, never edit the test. A prospect render that
  needs anything beyond the four pinned keys is a row, never a wider scope.

<paths>
infra/aws/lambda/investor-reporting/_authz/enforce.py
infra/aws/lambda/investor-reporting/_authz/served.py
infra/aws/lambda/investor-reporting/_render_identity/grant.py
infra/aws/lambda/investor-reporting/_authz/tests/test_enforce_prospect_admit.py
infra/aws/lambda/investor-reporting/_authz/tests/test_enforce_prospect_refuse.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r29/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read without a grant (never written): `infra/aws/lambda/investor-reporting/` (all of it), `docs/contracts/investor-reporting/v1/`, `lib/`.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 27 addendum note (round 30, workstream ~P), cell `IB-pr-293`.
<owned_cells>IB-pr-293</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB29-3-AC1, IB29-3-AC2, IB29-3-AC3. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~101/IRPT_BCKEND.TO-IB-pr-293.enforcer-prospect-branch.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IB29-3-AC1,IB29-3-AC2,IB29-3-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message: the commit hashes, each criterion's last line, how the owner is re-resolved at read time (file:line),
and any surprise row id (`IRPT_BCKEND-W101-S<k>`, k >= 7).

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the shared Enforcer (`_authz/enforce.py`) guards every served read; the new branch is reached only by a grant carrying a stored prospect scope; AC3 holds the four suites; 0 served bytes move in the cell.
comp-iam: DECLARED-NOT-APPLICABLE -- no role changes; the served move's packet reads what a prospect render may read.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: a request-driven authorization module; no schedule, trigger or cron is created or moved.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface; the Enforcer's own fingerprint is graded by the tests.
comp-adversary: RUN -- IB29-3-AC1 base FAIL (no file), IB29-3-AC2 base FAIL (no file), IB29-3-AC3 base PASS (regression guard: export 139, holdings 165, _render_identity 45 passed; _authz 146 passed + the 6 baseline failures), dry-run at the base 2026-10-02 ~10:5xZ.
lane: the <paths> block IS the grant.
</preflight>
