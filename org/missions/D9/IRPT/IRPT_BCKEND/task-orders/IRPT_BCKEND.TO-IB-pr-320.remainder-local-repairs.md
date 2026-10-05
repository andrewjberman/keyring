# TO IRPT_BCKEND.TO-IB-pr-320 -- the ONE repair cell over E1's LOCAL non-BLOCKING remainder: eight rows, each fixed with its own test

<to_id>IRPT_BCKEND.TO-IB-pr-320</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~123</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-05</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>51</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** decomposition section 42 ("the rest of E1's LIVE list is not BLOCKING, and it is
batched as ONE repair cell at the next issuance"). The source list is
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~116/E1_RECONCILE_ROUNDS_42_46.json`. | **Decomp cell:** `IB-pr-320`
(decomposition section 45) | **outcome_ref:** FWD-8 | **depends_on:** none. The risk is WORLD because the cell edits code under
infra/; the cell itself deploys nothing, and every served release is the issuer's.

---

## WORKER FACE

Eight open surprise rows each name a small defect in the investor-reporting Lambdas, their tests, or the CI build script. Fix each
one and add a test that names its row id (for example in the test name or docstring: `test_S297_landed_target_writes_nothing`).
Do not change behavior beyond what each row names. Your worktree is `C:/Users/AndrewBerman/Desktop/wk-irpt-bckend-123`; run
everything from its root. `IR` below means `infra/aws/lambda/investor-reporting`.

1. **S220. The census test is wrong; the code is not.** `IR/_authz/tests/test_unguarded_census.py` fails 6 at base. It resolves the
   module dispatcher instead of the marked `_http_handler` in `IR/export/entry.py`, and it pins counts as literals (`:99`
   `len(table) == 19`, and `:125`, `:151`, `:194`). Make the test resolve the marked handler, and derive each count from the route
   table it reads, never a typed number. Keep the test's mutant arm: an unguarded route must still fail it.
2. **S282.** `IR/reports/tests/test_generate_installed.py:71` hard-codes 24 packaged schemas, but 25 are present. Derive the expected
   count from the schemas directory the test already reads.
3. **W62-S1.** `IR/export/tests/test_export.py:30` uses `import handler as handler_mod`, which depends on import order, so
   `pytest tests/test_submit_async.py` run ALONE from `IR/export` fails. Load the module with `importlib.util.spec_from_file_location`,
   as `IR/export/tests/test_submit_async.py:25` does. Change whichever file the solo failure names.
4. **S241.** In `IR/_authz/served.py`, the lazy `from canonical_profile_reads import CanonicalProfileReaders` (`:950`) sits inside a
   try whose catch-all (`:967-968`) turns an ImportError into a silent `[]`. Move the import out of the catch-all, or narrow the
   handler so an ImportError propagates. Test: with the module absent, the call raises (or logs the module name), never a silent `[]`.
5. **S297.** In `IR/holdings-performance/handler.py`, `_days_to_compute` returns `[str(target)]` when the landed max is already at or
   after the target (`:121`), so a re-fire rewrites a landed day. CTO batch 207 says the catch-up writes new keys only. When
   `max(landed) >= target`, return `[]`. The listing-failure branch (`:116`) and the empty-landed branch stay as they are. Test in
   `IR/holdings-performance/tests/test_catch_up.py`.
6. **S298.** In `IR/performance/holdings_gold.py`, `node.value_facts["claim"]` is set only on the missing-day branch (`:288-292`).
   Set `claim` to the measured value (the module's own measured constant; read it, do not invent one) when nothing is missing. Make
   the absence text near `:318` agree. Test in `IR/performance/tests/test_holdings_gold.py`: no missing day gives claim measured;
   a missing day gives claim inferred.
7. **W101-S14.** `export_receipt` in `IR/export/entry.py` (`:222-245`) returns the stored receipt without rewriting `download_route`.
   Compare `:283`, which builds the live route. Make the read return the live route. Test in `IR/export/tests/`: a stored receipt
   with a stale route reads back with the live one.
8. **W101-S16.** In `infra/aws/lambda/ci/build-and-upload.sh`, `STAGED_ABS_SOURCE` and `STAGED_NAMES` are assigned AFTER the staging
   call (`:388-389`), so a failed staging leaves no cleanup record. Assign them before the staging call (above `:381`). Add
   `infra/aws/lambda/ci/tests/test_staged_cleanup_record.sh`, modeled on `test_sha_handoff.sh`. It shows the assignment precedes the
   staging call and prints `PASS` lines, exit 0. Name `W101-S16` in it.

<criterion id="IB51-1-AC1" cell_refs="IB-pr-320"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r51/p51_repair.py" . IB51-1-AC1</invocation><expect>IB51-1-AC1 PASS</expect></criterion>
`IB51-1-AC1` -- every named suite passes with 0 failed: the census, the installed-schema test, test_submit_async.py run alone, the
holdings-performance, performance, export and _authz suites, and every `ci/tests/test_*.sh`. Base: FAIL.

<criterion id="IB51-1-AC2" cell_refs="IB-pr-320"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r51/p51_repair.py" . IB51-1-AC2</invocation><expect>IB51-1-AC2 PASS</expect></criterion>
`IB51-1-AC2` -- each of the eight row ids is named in a test file you added or changed. Base: FAIL.

<criterion id="IB51-1-AC3" cell_refs="IB-pr-320"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r51/p51_repair.py" . IB51-1-AC3</invocation><expect>IB51-1-AC3 PASS</expect></criterion>
`IB51-1-AC3` -- a GUARD: your commits touch only the grant, and nothing under infra/aws/terraform/. Base: PASS.

<expected_criteria>IB51-1-AC1,IB51-1-AC2,IB51-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below.
- **AWS:** none. No deploy, no `lambda-source-map.json` edit, no terraform.
- **Refusal clause.** A fix that needs more than its row names (a contract change, a new reason code, a schema change) is out of
  scope: file a row and leave that row's fix out.

<paths>
infra/aws/lambda/investor-reporting/_authz/
infra/aws/lambda/investor-reporting/reports/tests/
infra/aws/lambda/investor-reporting/export/
infra/aws/lambda/investor-reporting/holdings-performance/
infra/aws/lambda/investor-reporting/performance/
infra/aws/lambda/ci/build-and-upload.sh
infra/aws/lambda/ci/tests/
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~123/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-320.remainder-local-repairs.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 45 (round 51, workstream ~P), cell `IB-pr-320`.
<owned_cells>IB-pr-320</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB51-1-AC1, IB51-1-AC2, IB51-1-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~123/IRPT_BCKEND.TO-IB-pr-320.remainder-local-repairs.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB51-1-AC1,IB51-1-AC2,IB51-1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message gives the commit hashes, each criterion's last line, one line per row on what changed, and any
surprise row ids.

## AMENDMENT 1 (2026-10-05 ~04:2xZ, issuer 2.0.0_SA_COO~P, on row IRPT_BCKEND-W123-S1)

With the S297 fix, `_days_to_compute` can return `[]`. In `IR/holdings-performance/handler.py`, `lambda_handler` (`results[-1]`,
:151) and `_target_day` (`[-1]`, :133) then raise `IndexError`, so a re-fire on a landed target errors where it should do nothing.
The guard is inside S297's own intent ("the catch-up writes new keys only"), so it is in this order:
- `lambda_handler`: on an empty plan, compute nothing and return the same keys with `{"date": None, "rc": 0, "ok": True,
  "days": [], "planned": [], "reason": "TARGET_ALREADY_LANDED"}`.
- `_target_day`: on an empty plan, return `None`. It never raises.

Test, in `IR/holdings-performance/tests/test_catch_up.py` and naming `W123-S1`: a handler fire on a landed target returns that
no-op and calls `hp.main` zero times.

The criteria are unchanged; AC1's holdings-performance suite carries the new test. No gate limb graded this modification: LIMB 6
does not fire on a modification, and GATE (viii) grades the declared `<placeholders>NONE</placeholders>`, which is unchanged.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- code in five investor-reporting Lambda dirs and the CI build script; 0 served bytes move in the cell. The served releases (S241 authz, S297 holdings-performance x2, S298 performance, W101-S14 export) are the issuer's, each under its own never-widen half.
comp-iam: DECLARED-NOT-APPLICABLE -- no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- no route changes; W101-S14 changes only the route string a receipt read returns.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- IB51-1-AC1 base FAIL (census 6 failed, installed-schema 1 failed, submit-async alone 1 failed), IB51-1-AC2 base FAIL (0 rows named), IB51-1-AC3 base PASS (guard), dry-run at base 0c3bc53717 2026-10-05 ~03:1xZ.
lane: the <paths> block IS the grant.
</preflight>
