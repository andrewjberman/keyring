# TO IRPT_BCKEND.TO-IB-pr-298 -- Two repairs: the holdings-gold figure is labelled GROSS (P-4), and the build never deletes a tracked source file

<to_id>IRPT_BCKEND.TO-IB-pr-298</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~101</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-02</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>35</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** CTO RULINGS batch 178 (@2a537cbad4, msg 104324; Andrew's IR fold-in, P-4: "a
DEFECT serving today: file the row and fix the label now") and row IRPT_BCKEND-S276 (this seat is its disarm owner); repairs batched
into ONE cell | **Decomp cell:** `IB-pr-298` (decomposition section 27 addendum note: round 35, one cell; row IRPT_BCKEND-S267) |
**outcome_ref:** FWD-9 (the served Performance figure) | **depends_on:** none

---

## WORKER FACE

**Repair 1 -- P-4 (row IRPT_BCKEND-S275).** `infra/aws/lambda/investor-reporting/performance/holdings_gold.py:270` assigns
`result.method, result.fee_basis, result.annualization = "TIME_WEIGHTED", "NET", "NONE"`. The figure is a holdings-value price
return with no fee deducted, so it is GROSS of fees (the contract's `fee_basis` enum is `GROSS | NET | UNKNOWN`,
`_contracts/PerformanceReport.schema.json`).
- Make it `"GROSS"`. Nothing else in the result moves.
- Add `performance/tests/test_holdings_gold_fee_basis.py`, at least 2 tests: a holdings-gold result carries `fee_basis` GROSS,
  and its method and annualization are unchanged.
- `test_f49_engine.py:99` asserts NET for the separate 49 Financial engine. That is not this path; leave it.

**Repair 2 -- row IRPT_BCKEND-S276 (ARMED).** `infra/aws/lambda/ci/build-and-upload.sh` materializes each `staged_from` member at
`<source_dir>/<packaged_as>` (the staging script, IB-rte-4). `cleanup_staged` (`:232-235`) then runs `rm -f` on every staged name.
For a function whose member's repo path IS that file (the performance adapter's flat layout), the build overwrites the tracked
working copy with the pinned blob and then deletes it. Measured today: 19 tracked files of `performance/` deleted by one build and
restored from HEAD.
- `cleanup_staged` asks git whether each staged path is tracked (`git ls-files`). It restores a tracked path from HEAD and deletes
  only an untracked one.
- Staging refuses, by name, a tracked destination that carries uncommitted edits (never overwrite a seat's work).
- Add `infra/aws/lambda/ci/test_build_staging_keeps_tracked.py`, at least 2 tests, run in a temporary git repo: a tracked member
  survives staging and cleanup with its HEAD bytes, and an untracked staged member is removed. Name `tracked` and
  `cleanup_staged`.

<criterion id="IB35-1-AC1" cell_refs="IB-pr-298"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r35/p35_1_ac1_fee_basis_gross.py" .</invocation><expect>IB35-1-AC1 PASS</expect></criterion>
`IB35-1-AC1` -- `holdings_gold.py` assigns GROSS and no fee_basis assignment carries NET; the new tests pass (at least 2). Base:
FAIL (NET).

<criterion id="IB35-1-AC2" cell_refs="IB-pr-298"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r35/p35_1_ac2_build_keeps_tracked.py" .</invocation><expect>IB35-1-AC2 PASS</expect></criterion>
`IB35-1-AC2` -- `cleanup_staged` consults `git ls-files`; the staging tests pass (at least 2). Base: FAIL.

<criterion id="IB35-1-AC3" cell_refs="IB-pr-298"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r35/p35_1_ac3_suites_unchanged.py" .</invocation><expect>IB35-1-AC3 PASS</expect></criterion>
`IB35-1-AC3` -- `performance` (237), `export` (168) and the packaging test (3) pass, 0 failed. Base: PASS (a regression guard).

<expected_criteria>IB35-1-AC1,IB35-1-AC2,IB35-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file.
- **Do NOT run build-and-upload.sh** against a real function: no build, no upload, no AWS. Prove the cleanup in a temporary repo.
- **Refusal clause.** An existing test that moves is a defect: stop and file a row, never edit the test.

<paths>
infra/aws/lambda/investor-reporting/performance/holdings_gold.py
infra/aws/lambda/investor-reporting/performance/tests/test_holdings_gold_fee_basis.py
infra/aws/lambda/ci/build-and-upload.sh
infra/aws/lambda/ci/test_build_staging_keeps_tracked.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r35/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read without a grant (never written): `infra/aws/lambda/` (all of it), `docs/contracts/investor-reporting/v1/`, `lib/`.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 27 addendum note (round 35, workstream ~P), cell `IB-pr-298`.
<owned_cells>IB-pr-298</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB35-1-AC1, IB35-1-AC2, IB35-1-AC3. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~101/IRPT_BCKEND.TO-IB-pr-298.fee-basis-gross-and-build-keeps-tracked.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IB35-1-AC1,IB35-1-AC2,IB35-1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message must give the commit hashes, each criterion's last line, and any surprise row id
(`IRPT_BCKEND-W101-S<k>`, k >= 16).

---

## RECORD FACE

<preflight>
comp-blast: RUN -- holdings_gold.py is a member of the performance adapter (the served label moves at the next adapter deploy, the Inflection serving packet's F1); build-and-upload.sh is the shared build tool for every zip function (its cleanup only); AC3 holds three suites; 0 served bytes move in the cell.
comp-iam: DECLARED-NOT-APPLICABLE -- no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: a label in request-driven code and a build-time cleanup; no schedule, trigger or cron is created or moved.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- IB35-1-AC1 base FAIL (NET), IB35-1-AC2 base FAIL (cleanup does not consult git), IB35-1-AC3 base PASS (regression guard: performance 237, export 168, packaging 3), dry-run at the base 2026-10-02 ~17:4xZ.
lane: the <paths> block IS the grant.
</preflight>
