# TO IRPT_BCKEND.TO-IB-pr-326 -- the refusal classes at the guarded path's enforcer_for call site reach the wire (CTO batch 265 item 2; batch 253 class rule)

<to_id>IRPT_BCKEND.TO-IB-pr-326</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~129</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-05</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>58</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** 1.0.0_SA_CTO RULINGS batch 265 item 2 (msg 105349 thread): "The wire fix
(`served.py:1052` classifying through `reason_for`) is `~P`'s cell to cut. It changes a served `public_reason_code`, so its release is its
own never-widen half; batch 253 remains the target." | **Decomp cell:** `IB-pr-326` (decomposition section 51) | **outcome_ref:** FWD-1
(the served read path) | **depends_on:** none. The risk is WORLD because the cell edits code under infra/aws/lambda that a deploy would
ship. It deploys nothing: the build, the CTO's never-widen half and the apply are the issuer's, after this order drains.

---

## WORKER FACE

**The defect.** `infra/aws/lambda/investor-reporting/_authz/served.py` lines 1043-1054 (the guarded path) read:

```
        try:
            ...
            enforcer, ctx = self.enforcer_for(verified, principals)
        except Exception as exc:                       # noqa: BLE001 -- classified, never echoed
            cid = _errors.new_correlation_id()
            code = "FIRM_BINDING" if isinstance(exc, _enforce.AuthzError) else "UNEXPECTED"
            _record(cid, operation, exc, code)
            return refuse(operation, None, code, cid)
```

The response code never passes through the estate's classifier. `BucketUnmapped` (`_authz/loaders.py:43`, a `ValueError` declaring
`public_reason_code = "FIRM_BINDING"`) and `FirmArtifactIncomplete` (`:49`, a `ValueError` declaring `"NOT_READY"`) are raised inside
`enforcer_for`, so they answer `UNEXPECTED` on the wire while the function's own log record already carries their class. The classifier is
`Entry.public_reason_for(self, exc)` at `served.py:773` (it calls `_errors.reason_for(exc)` first, then this function's own `self.reasons`
by MRO, and returns `UNEXPECTED` for anything not in `BOUNDARY_REASONS`). `_errors.reason_for` is `_authz/errors.py:116`: it reads a
declared `public_reason_code` first, then a by-type table that maps `AuthzError` to `NOT_AUTHORIZED` and a bare `ValueError` to `INVALID_INPUT`.

**What you build** (your worktree is `C:/Users/AndrewBerman/Desktop/wk-irpt-bckend-129`; run everything from its root):

1. **The edit, `served.py` only, the `except` block above.** Precedence, in this order:
   - an `AuthzError` keeps `FIRM_BINDING` exactly as today (do NOT let it fall to the classifier, which would answer `NOT_AUTHORIZED` and
     change a code that is served today);
   - every other exception answers `self.public_reason_for(exc)`.
   - `_record(cid, operation, exc, code)` and `refuse(...)` keep their arguments and order, with the new `code`.
   Touch no other line of `served.py`.
2. **`_authz/tests/test_wire_reason_codes.py`**, at least 4 tests (the 5th below makes it 5), each driving the guarded path to the `except`
   block with an `enforcer_for` that raises the named exception and reading the WIRE answer (`public_reason_code` in the refusal), not the
   log. Use the fixtures and the entry construction the sibling tests use (`_authz/tests/test_reason_codes_W124.py`,
   `test_reason_codes_S260_S175.py` and `fixtures.py` already build an `Entry` and call the boundary; copy their harness, do not invent one):
   - an `AuthzError` answers `FIRM_BINDING`;
   - a `BucketUnmapped` answers `FIRM_BINDING`;
   - a `MaintainedSourceUnready` (`_scope/maintained_sources.py:41`) answers `NOT_READY`;
   - an unclassified exception (a bare `RuntimeError`) answers `UNEXPECTED`;
   - a plain `ValueError` answers what `public_reason_for` returns for it today (`INVALID_INPUT`). This test RECORDS a served consequence of the
     edit, so the CTO's never-widen half can name it; say so in the test's docstring.
   The words `FIRM_BINDING`, `NOT_READY`, `UNEXPECTED` and `AuthzError` must appear in the file.
3. **Run the `_authz` suite once** (`python -m pytest -q -p no:cacheprovider` from `infra/aws/lambda/investor-reporting/_authz`) and report the
   last line verbatim. It must show 0 failed and 0 errors.
4. Commit `served.py` and the tests. Do not build, upload or deploy anything, and do not call AWS.

<criterion id="IB58-1-AC1" cell_refs="IB-pr-326"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r58/p58_wire_codes.py" . IB58-1-AC1</invocation><expect>IB58-1-AC1 PASS</expect></criterion>
`IB58-1-AC1` -- the new tests (at least 4, naming `FIRM_BINDING`, `NOT_READY`, `UNEXPECTED`, `AuthzError`) pass, and the whole `_authz` suite
passes with 0 failed. Base: FAIL (dry-run at base aee5b1d269 2026-10-05: no test file).

<criterion id="IB58-1-AC2" cell_refs="IB-pr-326"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r58/p58_wire_codes.py" . IB58-1-AC2</invocation><expect>IB58-1-AC2 PASS</expect></criterion>
`IB58-1-AC2` -- a GUARD: your commits touch only your grant. Base: PASS (dry-run at base aee5b1d269: 0 changed paths).

<expected_criteria>IB58-1-AC1,IB58-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, and nothing else.
- **No AWS, no deploy, no build.** Local code and tests only.
- **Refusal clause.** A change to any line of `served.py` outside the `except` block, any edit to `loaders.py`, `errors.py` or `enforce.py`, or
  a call to AWS is a defect: stop and file a row.
- **A test that fails for a reason you did not cause** is a surprise row and a stop on that criterion, never an edit to another test.

<paths>
infra/aws/lambda/investor-reporting/_authz/served.py
infra/aws/lambda/investor-reporting/_authz/tests/
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~129/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-326.enforcer-for-refusals-reach-the-wire.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 51 (round 58, workstream ~P), cell `IB-pr-326`.
<owned_cells>IB-pr-326</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB58-1-AC1, IB58-1-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~129/IRPT_BCKEND.TO-IB-pr-326.enforcer-for-refusals-reach-the-wire.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB58-1-AC1,IB58-1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message gives the commit hashes, each criterion's last line, the `_authz` suite's last line, the exact diff of the
`except` block, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- local code and tests; nothing is deployed by this order.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call is added.
comp-routes: DECLARED-NOT-APPLICABLE -- no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- IB58-1-AC1 base FAIL (no test file), IB58-1-AC2 base PASS (guard), dry-run at base aee5b1d269 2026-10-05 ~21:5xZ.
lane: the <paths> block IS the grant.
</preflight>

**Release (not this order's):** the build of the four re-pinned functions that carry `_authz/served.py`, the CTO's never-widen half naming the
served delta (a refusal at this call site answers its declared class where it answered UNEXPECTED; a plain ValueError answers INVALID_INPUT), and
the targeted applies are the issuer's after the drain. batch 253 is the target; batch 265 item 2 assigned the cell.
