# TO IRPT_BCKEND.TO-IB-pr-328 -- re-pin the served.py and loaders.py staged_from members of four functions to the merged blobs (release r58; CTO half condition 1)

<to_id>IRPT_BCKEND.TO-IB-pr-328</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~131</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-06</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>60</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** 1.0.0_SA_CTO, the r58 CTO half
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_IRPT_BCKEND_RELEASE_R58_20261006.md` @38fbca18a2, condition 1: "Cut IB-pr-327, then IB-pr-328")
| **Decomp cell:** `IB-pr-328` (decomposition section 53) | **outcome_ref:** FWD-1 (the served read path) | **depends_on:** IB-pr-327 (drained @d8d8e7d868).
The risk is WORLD because the source map is the build input of four served functions. The order applies nothing: no build, no upload, no deploy.

---

## WORKER FACE

**Why.** `infra/aws/lambda/ci/build-and-upload.sh` does not package `_authz/served.py` or `_authz/loaders.py` from the working tree. For every function it
materializes each member of that function's `staged_from` list from a PINNED commit and verifies its sha256. So the two merged fixes ship only when the pins
move: IB-pr-326 changed `served.py` (the enforcer_for refusals reach the wire) and IB-pr-327 changed `loaders.py` (a pointer with no key is NOT_READY). Both
are merged at `d8d8e7d868bc3a784afe5c87e6ad19743c0c53ac` (a merge commit; the two files' bytes at it are the final bytes). Your worktree is
`C:/Users/AndrewBerman/Desktop/wk-irpt-bckend-131`; run everything from its root.

**What you build, one file: `infra/aws/lambda/ci/lambda-source-map.json`.** In `functions`, for EXACTLY these four keys:
`irpt-49f-reporting-read-lambda`, `irpt-export-render`, `irpt-directory-search`, `irpt-holdings`,
find the two entries of `staged_from` whose `repo_path` is `infra/aws/lambda/investor-reporting/_authz/served.py` and
`infra/aws/lambda/investor-reporting/_authz/loaders.py`. Set in each of those 8 entries:
- `"pin"` to `d8d8e7d868bc3a784afe5c87e6ad19743c0c53ac` (the full 40 hex);
- `"sha256"` to the sha256 hex of `git show d8d8e7d868bc3a784afe5c87e6ad19743c0c53ac:<repo_path>` (compute it; do not copy a value). For your
  cross-check, the two values are `a8eb91e7d4c5c4aae844fd16f5bc83821b2653b64884df90b33626e837f2fc85` for `served.py` and
  `72f22ea3a43c08733a412e594cc76107377184d21c694d1bbab56c42ff8a718d` for `loaders.py`, identical across the four functions.
Change nothing else: not `packaged_as`, not any other member, not `artifact_sha256`, `deployed_code_sha256`, `last_deployed_*` or any `_note`, and no
other function. Keep the file's existing formatting (load, edit the 8 entries, write back with the same indent and trailing newline; the result must
show `git diff --stat` of exactly 16 insertions and 16 deletions, and `git diff` must show only `pin` and `sha256` lines).

<criterion id="IB60-1-AC1" cell_refs="IB-pr-328"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r60/p60_repin.py" . IB60-1-AC1</invocation><expect>IB60-1-AC1 PASS</expect></criterion>
`IB60-1-AC1` -- for the four functions, the `_authz/served.py` and `_authz/loaders.py` members carry pin = the 40-hex pin above and a sha256 the check
recomputes from `git show <pin>:<path>`; no other function and no other member or field of these four rows differs from base. Base: FAIL (dry-run at
base 01e4518df8 2026-10-06: reporting-read served.py still pinned 0642c9d004). Green arm: the same edit made by this seat on a scratch copy passes.

<criterion id="IB60-1-AC2" cell_refs="IB-pr-328"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r60/p60_repin.py" . IB60-1-AC2</invocation><expect>IB60-1-AC2 PASS</expect></criterion>
`IB60-1-AC2` -- a GUARD: your commits touch only your grant. Base: PASS (dry-run at base: 0 changed paths).

<expected_criteria>IB60-1-AC1,IB60-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, and nothing else.
- **No AWS, no build, no upload, no deploy, no terraform.** Do not run `build-and-upload.sh` or `record-terraform-deploy.sh` (they write to S3 and to this
  same map). Local file edit and the two criteria only.
- **Refusal clause.** An edit to any other function's row, to any field named above as untouched, or a call to AWS is a defect: stop and file a row.

<paths>
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~131/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-328.repin-served-and-loaders-for-r58.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 53 (round 60, workstream ~P), cell `IB-pr-328`.
<owned_cells>IB-pr-328</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB60-1-AC1, IB60-1-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~131/IRPT_BCKEND.TO-IB-pr-328.repin-served-and-loaders-for-r58.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB60-1-AC1,IB60-1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message gives the commit hash, each criterion's last line, the `git diff --stat` line of your edit, the two sha256 values you
computed, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a source-map edit; nothing is built or deployed by this order.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- IB60-1-AC1 base FAIL, IB60-1-AC2 base PASS, and a green arm (the correct edit passes AC1, then the file is restored), dry-run at base 01e4518df8 2026-10-06 ~01:3xZ.
lane: the <paths> block IS the grant.
</preflight>

**Release (not this order's):** per function, the issuer takes the changed-member census at the new pins, builds, plans (code hash only), applies
and invokes under the r58 CTO half. `irpt-directory-search` and `irpt-holdings` re-pin across more history than the two edits (their `served.py`
moves from `f9a00f732c` / `21eca74f40`): the census diff for those two goes to 1.0.0_SA_CTO before either deploys (CTO half condition 2).
