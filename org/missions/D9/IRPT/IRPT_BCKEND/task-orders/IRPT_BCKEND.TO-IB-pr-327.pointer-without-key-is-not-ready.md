# TO IRPT_BCKEND.TO-IB-pr-327 -- a directory latest.json pointer with no usable key raises FirmArtifactIncomplete (NOT_READY), never a bare KeyError (CTO batch 271 item 2; r58 CTO half condition 1)

<to_id>IRPT_BCKEND.TO-IB-pr-327</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~130</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-06</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>59</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** 1.0.0_SA_CTO RULINGS batch 271 item 2 and the r58 CTO half
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_IRPT_BCKEND_RELEASE_R58_20261006.md` @38fbca18a2, condition 1: "Cut IB-pr-327, then IB-pr-328")
| **Decomp cell:** `IB-pr-327` (decomposition section 52) | **outcome_ref:** FWD-1 (the served read path) | **depends_on:** none (IB-pr-326 drained
@abf14e56ba). The risk is WORLD because the cell edits code under infra/aws/lambda that a deploy would ship. It deploys nothing.

---

## WORKER FACE

**The defect.** `infra/aws/lambda/investor-reporting/_authz/loaders.py`, function `load_directory` (lines 195-204 at your base):

```
def load_directory(tenant, s3=None):
    bucket = bucket_for(tenant)
    client = s3 or _s3()
    pointer = _get_json(bucket, DIRECTORY_PREFIX + "/latest.json", client)
    return _fetch_directory(bucket, pointer["key"], client)
```

`pointer` is the firm's `latest.json`, a server-side pointer object. If it has no `key` the subscript raises a bare `KeyError`. Since IB-pr-326
(`served.py:1052` now answers `self.public_reason_for(exc)`), `errors.reason_for` (`_authz/errors.py:116`) maps the class name `KeyError` to
`NOT_FOUND`, so a BROKEN SERVER-SIDE POINTER would answer `NOT_FOUND` as if the caller asked for something that does not exist. Batch 271 item 2: a
server fault must not read as a client fault, and gets a declared class in the same release. The class this estate already uses for "a required server
source is absent or malformed" is `FirmArtifactIncomplete` (`loaders.py:49`, declares `public_reason_code = "NOT_READY"`, W124-S2); it is raised today
at `opaque_firm_for` (`loaders.py:218`) for a directory with no `firm_id_opaque`.

**What you build** (your worktree is `C:/Users/AndrewBerman/Desktop/wk-irpt-bckend-130`; run everything from its root):

1. **The edit, `_authz/loaders.py` only, inside `load_directory`.** After reading `pointer`, take its key as `pointer.get("key")` when `pointer` is a
   `dict`, else `None`. When that value is not a non-empty `str`, raise `FirmArtifactIncomplete` with a message in the style of line 218's: it must say
   the directory pointer `latest.json` declares no usable `key`, so the artifact cannot be read and nothing may be served. Otherwise call
   `_fetch_directory(bucket, key, client)` exactly as today. Touch no other line of `loaders.py`.
2. **`_authz/tests/test_pointer_guard.py`**, at least 4 offline tests, with the S3 transport stubbed (`_authz/tests/test_loader_freshness.py` already
   builds a fake client and calls `load_directory`; copy its harness, do not invent one):
   - a pointer `{}` raises `FirmArtifactIncomplete`;
   - a pointer that is a list (`[]`) raises `FirmArtifactIncomplete`;
   - a pointer `{"key": ""}` raises `FirmArtifactIncomplete`;
   - a good pointer `{"key": "<a key>"}` still returns the directory (the control: the guard does not refuse a valid pointer);
   - the refusal answers `NOT_READY` on the wire: drive the guarded path with `enforcer_for` NOT patched, `bucket_for` and `_get_json` stubbed to
     return a malformed pointer, and read the refusal's `public_reason_code` (copy the entry/boundary harness from
     `_authz/tests/test_wire_reason_codes.py`, which IB-pr-326 added).
   The words `FirmArtifactIncomplete`, `NOT_READY`, `latest.json` and `key` must appear in the file.
3. **Run the `_authz` suite once** (`python -m pytest -q -p no:cacheprovider` from `infra/aws/lambda/investor-reporting/_authz`) and report the last
   line verbatim. It must show 0 failed and 0 errors.
4. Commit `loaders.py` and the tests. Do not build, upload or deploy anything, and do not call AWS.

<criterion id="IB59-1-AC1" cell_refs="IB-pr-327"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r59/p59_pointer_guard.py" . IB59-1-AC1</invocation><expect>IB59-1-AC1 PASS</expect></criterion>
`IB59-1-AC1` -- the new tests (at least 4, naming `FirmArtifactIncomplete`, `NOT_READY`, `latest.json`, `key`) pass, and the whole `_authz` suite
passes with 0 failed. Base: FAIL (dry-run at base 38fbca18a2 2026-10-06: no test file).

<criterion id="IB59-1-AC2" cell_refs="IB-pr-327"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r59/p59_pointer_guard.py" . IB59-1-AC2</invocation><expect>IB59-1-AC2 PASS</expect></criterion>
`IB59-1-AC2` -- a GUARD: your commits touch only your grant. Base: PASS (dry-run at base 38fbca18a2: 0 changed paths).

<expected_criteria>IB59-1-AC1,IB59-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, and nothing else.
- **No AWS, no deploy, no build.** Local code and tests only.
- **Refusal clause.** A change to any line of `loaders.py` outside `load_directory`, any edit to `served.py`, `errors.py` or `enforce.py`, or a call to
  AWS is a defect: stop and file a row.
- **A test that fails for a reason you did not cause** is a surprise row and a stop on that criterion, never an edit to another test.

<paths>
infra/aws/lambda/investor-reporting/_authz/loaders.py
infra/aws/lambda/investor-reporting/_authz/tests/
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~130/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-327.pointer-without-key-is-not-ready.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 52 (round 59, workstream ~P), cell `IB-pr-327`.
<owned_cells>IB-pr-327</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB59-1-AC1, IB59-1-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~130/IRPT_BCKEND.TO-IB-pr-327.pointer-without-key-is-not-ready.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB59-1-AC1,IB59-1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message gives the commit hashes, each criterion's last line, the `_authz` suite's last line, the exact diff of `load_directory`,
and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- local code and tests; nothing is deployed by this order.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call is added.
comp-routes: DECLARED-NOT-APPLICABLE -- no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- IB59-1-AC1 base FAIL (no test file), IB59-1-AC2 base PASS (guard), dry-run at base 38fbca18a2 2026-10-06 ~01:0xZ.
lane: the <paths> block IS the grant.
</preflight>

**Release (not this order's):** IB-pr-328 re-pins the `served.py` and `loaders.py` `staged_from` members after this order drains, so the pinned
loaders blob carries this guard. The build, the changed-member census, the targeted applies and the invokes follow under the r58 CTO half.
