# TO-IB-yr-631 -- the Analysis upload door admits an internal filer on behalf of an allowed firm (TCKT_VNEXT X-1)

<to_id>IRPT_BCKEND.TO-IB-yr-631</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~152</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>63</round>
<workstream>~Y</workstream>

**Directive:** D9 | **Fabric:** laptop | **Workstream:** ~Y | **Decomp cell:** `IB-yr-631` (`decompositions/IRPT_BCKEND_DECOMP_R63_Y.md`)

---

## WORKER FACE

### THE CELL

`infra/aws/lambda/investor-reporting/intake/uploads.py` is the door for uploading a client's holdings file to the Analysis
tab. Today an internal Opal user cannot upload on behalf of a partner firm, even one they are allowed to act for:
- `create` (around :219-234) refuses `UPLOAD_CREATOR_MUST_BE_CURRENT_ACTOR` when the acting principal is not the owner;
- it refuses `UPLOAD_ACTOR_ATTRIBUTION` when the principal's `home_firm_id` differs from the owner's.

**Your cell: admit exactly one more case and keep every other refusal.**
- **ADMIT:** an INTERNAL principal (Opal's own, home firm `opal-capital`) whose `allowedFirmIds` contains the owner's
  `firm_id`. Read how the estate marks a principal internal and where `allowedFirmIds` lives: `current_authority.decide`
  and `_scope/maintained_sources.py` (around :304), named in the comment at `create`. Use the existing field, and do not
  invent a new one.
- **RECORD:** on an admitted upload, the stored record carries BOTH the acting principal (its `principal_id`) and the owner
  firm. Today `original["owner"]` carries the owner. Add the actor in a field that a test can read back.
- **REFUSE, unchanged:**
  - (a) an internal principal whose `allowedFirmIds` lacks the owner firm;
  - (b) a non-internal principal filing for another firm;
  - (c) an owner whose `firm_id` is `opal-capital` (or `global`), which `_allow` keeps refusing.

  Each refusal keeps its existing refusal code.
- `_allow`'s `authorize_current` callback stays the gate it is. Do not bypass it; the admit must also pass it.

Write the tests in a NEW file, `intake/tests/test_uploads_on_behalf.py`, built from the fixtures that
`intake/tests/test_uploads.py` uses. Node names:
- one name containing `admit`: the admit, plus the read-back of actor and owner firm;
- three names containing `refuse`: arms (a), (b) and (c).

**Why:** TCKT_VNEXT PRD v0.2 C-ONE-DOOR, ruled into Y by `1.0.0_SA_CTO~DELL2` msg 925. TCKT_VNEXT's round-1 live run waits
on it.

### ACCEPTANCE (run from `infra/aws/lambda/investor-reporting` inside your worktree)

<criterion id="Y63-1-AC1" cell_refs="IB-yr-631"><invocation>python -m pytest -q -p no:cacheprovider intake/tests/test_uploads_on_behalf.py -k admit</invocation><expect>0 failed, at least 1 passed: an internal principal whose allowedFirmIds names the owner firm creates an upload, and the stored record reads back both the acting principal_id and the owner firm_id</expect></criterion>

<criterion id="Y63-1-AC2" cell_refs="IB-yr-631"><invocation>python -m pytest -q -p no:cacheprovider intake/tests/test_uploads_on_behalf.py -k refuse</invocation><expect>0 failed, 3 passed: (a) internal without the owner firm, (b) non-internal for another firm, (c) opal-capital owner -- each still refused with its existing code</expect></criterion>

<criterion id="Y63-1-AC3" cell_refs="IB-yr-631"><invocation>python -m pytest -q -p no:cacheprovider intake/tests/test_uploads.py intake/tests/test_uploads_refusal_class.py intake/tests/test_retained_uploads.py intake/tests/test_template_uploads.py</invocation><expect>0 failed, 50 passed (the base count; no existing test changed)</expect></criterion>

<expected_criteria>Y63-1-AC1,Y63-1-AC2,Y63-1-AC3</expected_criteria>

**Issuer's base run at dell2 CLOUD 4efdd8c961:**
- AC1 and AC2 FAIL as expected: the test file is absent ("no tests ran").
- AC3 PASSES: 50 passed, 11 subtests passed. It is the control and must stay green with the same count.

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule, trigger or scheduled producer is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no boto3 call, no role, no grant. The admit is a code-level rule over existing principal fields.
comp-adversary: DECLARED-NOT-APPLICABLE -- the three refusal arms are the adversarial control the CTO named (msg 925); AC3 holds every existing refusal test.
comp-blast: RUN (by reading) -- uploads.py's create path for the Analysis tab only. It changes behaviour for one principal class (internal with the owner firm allowed) and nothing else. Nothing deploys here; the release is a later act under a never-widen pair.
lane: the <paths> block IS the grant (worker_grant). uploads.py is in IRPT_Y_ACCESS_INTEGRATION_P and the tests in IRPT_COMPLETION_Y, both permitting 2.0.0_SA_COO~Y2, the drain's merge author.
</preflight>

## BOUNDS

- **Grant.** The `<paths>` block and this order's file. No other product file.
- **No AWS call, no deploy, no network call.** Per Andrew-direct 2026-10-07: research browsing only when necessary, and NO
  downloads of any kind (no package, install or fetched file). No `bun`.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row, and do
  not weaken a test. If admitting the case needs a file outside `<paths>` (for example `current_authority.py`), that is a
  REFUSAL AND A ROW naming the file, not your shortfall.
- **Row ids** are `IRPT_BCKEND-W152-S<k>`. Append only your own block, with a `## <ID> -- <one line>` heading. Re-read the
  channel immediately before writing. Gate: `python .tools/surprise-row-gate.py --check <path>`. The disposition is one of
  UNDER_INVESTIGATION, GRADUATED, DISMISSED_WITH_REASON or DECOMP_INVALIDATING.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~152" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~152@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~152 <0.9.0_WK_IRPT_BCKEND~152@opal.agent>" -F <msgfile> -- <paths>`.
  Do NOT pre-`git add`. Write the message file with the Write tool. Every `.py` passes `.tools/commit-gate.sh` (it runs
  inside safe-commit). Verify with `git status --porcelain <path>` (empty).
- **Search discipline:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools.
- **ASCII only** in `uploads.py` and the test.

<paths>
infra/aws/lambda/investor-reporting/intake/uploads.py
infra/aws/lambda/investor-reporting/intake/tests/test_uploads_on_behalf.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~152/IRPT_BCKEND.TO-IB-yr-631.upload-door-admits-internal-filer-for-allowed-firm.proof_of_spec.json
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-yr-631.upload-door-admits-internal-filer-for-allowed-firm.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R63_Y.md</decomp_doc> round 63, workstream ~Y, cell `IB-yr-631`.
<owned_cells>IB-yr-631</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: Y63-1-AC1, Y63-1-AC2, Y63-1-AC3. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~152/IRPT_BCKEND.TO-IB-yr-631.upload-door-admits-internal-filer-for-allowed-firm.proof_of_spec.json`,
validated with your worktree's own `python .tools/proof-of-spec-check.py <instance> Y63-1-AC1,Y63-1-AC2,Y63-1-AC3` BEFORE the
flip to complete. Copy the shape from
`deliverables/0.9.0_WK_IRPT_BCKEND~151/IRPT_BCKEND.TO-IB-yr-624.drop-fixtures-har-from-package.proof_of_spec.json`.
</proof_of_spec>

**REPORT (your final message):**
- each criterion's output line;
- the field that marks a principal internal, and where `allowedFirmIds` is read;
- the name of the new actor field on the upload record;
- the diff summary and the commit hash.
