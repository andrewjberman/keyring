# TO-IB-yr-661 -- irpt-ycharts-generate's staged served.py carries E5 (the on-behalf guard)

<to_id>IRPT_BCKEND.TO-IB-yr-661</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~157</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>66</round>
<workstream>~Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~Y | **Decomp cell:** `IB-yr-661` (`decompositions/IRPT_BCKEND_DECOMP_R66_Y.md`)

---

## WORKER FACE

### THE CELL

`infra/aws/lambda/ci/lambda-source-map.json` describes how each Lambda is packaged. In the row `"irpt-ycharts-generate"`, the
`staged_from` list names files copied in from other repo paths, each at a fixed git `pin` with its `sha256`. The row with
`packaged_as` = `served.py` (`repo_path` = `infra/aws/lambda/investor-reporting/_authz/served.py`) is pinned at `db8161f46e`, older
than the E5 fix the next release must carry.

**Your cell: move exactly that one row to pin `038b35d676`.**
- Set its `pin` to the FULL 40-character sha `038b35d676eada6a67b91bffbe64fc21d8c598e8`. Match the form the other rows use.
- Set its `sha256` to the hex sha256 of the blob at that pin (`git show 038b35d676:infra/aws/lambda/investor-reporting/_authz/served.py`,
  hashed as bytes), in the same format the other rows use.
- Change nothing else: no other row, no other field. Edit the values in place; do not re-serialize the JSON; it must still parse.
  Preserve the file's existing line endings byte for byte.

**Why:** E5 (IB-pr-366, fix fff1b0395a, drained @038b35d676) makes the served CREATE guard resolve an on-behalf owner, so the X-1
upload door can actually be reached. Nothing deploys here.

### ACCEPTANCE (run from your worktree root, after your commit)

<criterion id="Y66-1-AC1" cell_refs="IB-yr-661"><invocation>python infra/aws/lambda/ci/release-census.py irpt-ycharts-generate --pin HEAD</invocation><expect>changed_members=4</expect></criterion>

<criterion id="Y66-1-AC2" cell_refs="IB-yr-661"><invocation>BUILD_ONLY=1 bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-ycharts-generate</invocation><expect>OK: import-closure</expect></criterion>

<expected_criteria>Y66-1-AC1,Y66-1-AC2</expected_criteria>

AC1 must name exactly `generate_installed.py`, `interactive_access.py`, `uploads.py` and `served.py` as the changed members. Any other
changed member is a ROW, not a pass. AC1 reads the map at your COMMITTED HEAD and the live function zip (an AWS read, allowed).

**Issuer's base run at dell2 CLOUD HEAD (2f7fa13324):** AC1 `changed_members=3` (the first three, release 1 live). AC2 is the control
(`OK: import-closure -- 63 packaged .py file(s)` at f7a9d0b34f) and must stay OK.

## BOUNDS

- **Grant.** The `<paths>` block and this order's file.
- **No deploy, no upload: `BUILD_ONLY=1` only.** AWS reads only.
- **No downloads or installs. No `bun`.**
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row, and do not
  weaken the check.
- **Row ids** are `IRPT_BCKEND-D2-W157-S<k>`. Append ONLY your own block with a `## <ID> -- <one line>` heading, re-reading the channel
  immediately before writing. Gate: `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~157" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~157@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~157 <0.9.0_WK_IRPT_BCKEND~157@opal.agent>" -F <msgfile> -- <paths>`.
  Do NOT pre-`git add`. Write the message file with the Write tool. On `rc=128` with `index.lock`, wait and retry; never delete the lock.
- **Search:** native Grep/Glob/Read tools. **ASCII only.**

<paths>
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~157/IRPT_BCKEND.TO-IB-yr-661.repin-served-e5.proof_of_spec.json
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-yr-661.repin-served-e5.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R66_Y.md</decomp_doc> round 66, workstream ~Y, cell `IB-yr-661`.
<owned_cells>IB-yr-661</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: Y66-1-AC1, Y66-1-AC2. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~157/IRPT_BCKEND.TO-IB-yr-661.repin-served-e5.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> Y66-1-AC1,Y66-1-AC2` BEFORE the flip to complete. Copy the shape from
`deliverables/0.9.0_WK_IRPT_BCKEND~155/IRPT_BCKEND.TO-IB-yr-641.repin-x1-staged-rows.proof_of_spec.json`.
</proof_of_spec>

**REPORT (your final message):** each criterion's output lines (including the four `changed` lines); the row's new pin and sha256;
the diff summary; the commit hashes.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule, trigger or scheduled producer is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no boto3 call, role or grant changes; the census and BUILD_ONLY only read AWS and build locally.
comp-adversary: DECLARED-NOT-APPLICABLE -- AC1 names its exact member set and any extra member is a row; AC2 is the import-closure control.
comp-blast: RUN (by reading) -- one staged row of one function's package list; git log db8161f46e..038b35d676 on served.py is exactly fff1b0395a; no deployed byte moves.
lane: the <paths> block IS the grant (worker_grant); lambda-source-map.json is also in IRPT_COMPLETION_SOURCE_MAP, which permits 2.0.0_SA_COO~Y2, the drain's merge author.
</preflight>
