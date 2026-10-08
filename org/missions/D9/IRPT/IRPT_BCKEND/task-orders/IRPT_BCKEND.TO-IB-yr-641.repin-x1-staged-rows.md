# TO-IB-yr-641 -- irpt-ycharts-generate's staged rows carry both X-1 halves (release 2 repin)

<to_id>IRPT_BCKEND.TO-IB-yr-641</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~155</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>64</round>
<workstream>~Y</workstream>

**Directive:** D9 | **Fabric:** laptop | **Workstream:** ~Y | **Decomp cell:** `IB-yr-641` (`decompositions/IRPT_BCKEND_DECOMP_R64_Y.md`)

---

## WORKER FACE

### THE CELL

`infra/aws/lambda/ci/lambda-source-map.json` describes how each Lambda is packaged. In the row `"irpt-ycharts-generate"`,
the `staged_from` list names files copied in from other repo paths, each at a fixed git `pin` with its `sha256`. Three of
those rows are pinned at `3f29017cfc`, a commit older than the changes the next release must carry:

| packaged_as | repo_path |
|---|---|
| `uploads.py` | `infra/aws/lambda/investor-reporting/intake/uploads.py` |
| `interactive_access.py` | `infra/aws/lambda/investor-reporting/_scope/interactive_access.py` |
| `generate_installed.py` | `infra/aws/lambda/investor-reporting/reports/generate_installed.py` |

**Your cell: move exactly those three rows to pin `f09b802cdc`.**
- Set each row's `pin` to the FULL 40-character sha of `f09b802cdc` (`git rev-parse f09b802cdc`). Match the form the other
  rows use; check what they store.
- Set each row's `sha256` to the hex sha256 of the blob at that pin (`git show f09b802cdc:<repo_path>`, hashed as bytes),
  in the same format the other rows use.
- Change nothing else: no other row, no other field.
- Edit those values in place. Do not re-serialize the whole JSON; the file must still parse.

**Why:** X-1 (the upload door admits an internal filer for an allowed firm) is merged, but the build still packages the old
copies. CTO~DELL2 msg 1089 ruled that release 2 is this repin plus the smoke test. Nothing deploys here.

### ACCEPTANCE (run from your worktree root)

<criterion id="Y64-1-AC1" cell_refs="IB-yr-641"><invocation>python infra/aws/lambda/ci/release-census.py irpt-ycharts-generate --pin HEAD</invocation><expect>changed_members=3</expect></criterion>

<criterion id="Y64-1-AC2" cell_refs="IB-yr-641"><invocation>BUILD_ONLY=1 bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-ycharts-generate</invocation><expect>OK: import-closure</expect></criterion>

<expected_criteria>Y64-1-AC1,Y64-1-AC2</expected_criteria>

AC1 must name exactly `uploads.py`, `interactive_access.py` and `generate_installed.py` as the changed members. Any other
changed member is a ROW, not a pass. AC1 reads the map at your COMMITTED HEAD, so run it after your commit. AC1 also reads
the live function zip, which is an AWS read, allowed.

**Issuer's base run at dell2 CLOUD f09b802cdc:**
- AC1: `changed_members=0` (live `ZspX0qD2..` equals a HEAD build).
- AC2: `OK: import-closure -- 63 packaged .py file(s)`, from the release-1 build at `1b5afe6a49`. The map has changed only in
  deployed-hash fields since. AC2 is the control and must stay OK.

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule, trigger or scheduled producer is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no boto3 call, no role or grant changes; the census and BUILD_ONLY only read AWS and build locally.
comp-adversary: DECLARED-NOT-APPLICABLE -- AC1 names its exact member set, and any extra member is a row; AC2 is the import-closure control.
comp-blast: RUN (by reading) -- three staged rows of one function's package list; no deployed byte moves; the release is a later act under its own pair.
lane: the <paths> block IS the grant (worker_grant); lambda-source-map.json is also in IRPT_COMPLETION_SOURCE_MAP, which permits 2.0.0_SA_COO~Y2, the drain's merge author.
</preflight>

## BOUNDS

- **Grant.** The `<paths>` block and this order's file.
- **No deploy, no upload: `BUILD_ONLY=1` only.** Never run build-and-upload.sh without `BUILD_ONLY=1`. AWS reads only.
- **Per Andrew-direct 2026-10-07:** research browsing only when necessary, and NO downloads of any kind (no package or
  install). No `bun`.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row, and do
  not weaken the check.
- **Row ids** are `IRPT_BCKEND-W155-S<k>`. Append ONLY your own block, with a `## <ID> -- <one line>` heading, and re-read
  the channel immediately before writing. The disposition is one of UNDER_INVESTIGATION, GRADUATED, DISMISSED_WITH_REASON or
  DECOMP_INVALIDATING. Gate: `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~155" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~155@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~155 <0.9.0_WK_IRPT_BCKEND~155@opal.agent>" -F <msgfile> -- <paths>`.
  Do NOT pre-`git add`. Write the message file with the Write tool. If you get `rc=128` with `index.lock`, wait a few
  seconds and retry; never delete the lock. Verify with `git status --porcelain <path>` (empty).
- **Search discipline:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools.
- **ASCII only.**

<paths>
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~155/IRPT_BCKEND.TO-IB-yr-641.repin-x1-staged-rows.proof_of_spec.json
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-yr-641.repin-x1-staged-rows.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R64_Y.md</decomp_doc> round 64, workstream ~Y, cell `IB-yr-641`.
<owned_cells>IB-yr-641</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: Y64-1-AC1, Y64-1-AC2. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~155/IRPT_BCKEND.TO-IB-yr-641.repin-x1-staged-rows.proof_of_spec.json`,
validated with your worktree's own `python .tools/proof-of-spec-check.py <instance> Y64-1-AC1,Y64-1-AC2` BEFORE the flip to
complete. Copy the shape from
`deliverables/0.9.0_WK_IRPT_BCKEND~151/IRPT_BCKEND.TO-IB-yr-624.drop-fixtures-har-from-package.proof_of_spec.json`.
</proof_of_spec>

**REPORT (your final message):**
- each criterion's output line, including the three `changed` lines;
- the three rows' new pin and sha256;
- the diff summary and the commit hash.
