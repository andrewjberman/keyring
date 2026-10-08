# TO IRPT_BCKEND.TO-IB-pr-370 -- E9's release packet: irpt-export-render packages the per-family policy revisions (repository.py, composition.py, the irpt-custody-x10-v1 registry row) with submit_installed.py; clean-tree BUILD_ONLY; never-widen packet

<to_id>IRPT_BCKEND.TO-IB-pr-370</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~178</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>83</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** CTO ADDENDUM 6 and ADDENDUM 9 (msg 1474: "~P2: E9 under its own pair") |
**Decomp cell:** `IB-pr-370` (decomposition section 76) | **outcome_ref:** FWD-8 / CUSTDY hop 5 | **depends_on:** IB-pr-369 (drained
@0c2bdf7634), E8 PENDING row (fdc0a92a21, at HEAD), IB-pr-368 (live).

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-irpt-bckend-178` (branch `wk-IRPT_BCKEND-178`). Work and commit only there. Paths below are relative to
it. Model this order on IB-pr-367 (`deliverables/0.9.0_WK_IRPT_BCKEND~175/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-367.md` and its census
file).

**What is live now.** `irpt-export-render` CodeSha256 `idanP8nX/mqaQ+FIGGY6AT4Xe/JxckOM3N0rWwivSh8=`, from IB-pr-368. The census at
HEAD shows `submit_installed.py` changed: it is packaged from the source dir (`files[]`), so any HEAD build already carries IB-pr-369's
copy. The staged rows still pin:
- `repository.py` at `b13bab7495` (no per-family revisions);
- `composition.py` at `83e8b9577a` (older than HEAD; row D2-S6);
- the policy registry `infra/logic/registry/reporting_policies.json` at `c4fedd31c5` (no `irpt-custody-x10-v1` row; E8 landed at
  `fdc0a92a21`).

**Your cell. Nothing is uploaded or applied.**
1. **Find the minimal repin set** that makes the packaged function retain and read a CUSTODY_REPORT under `irpt-custody-x10-v1`, with
   PERFORMANCE and ANALYSIS unchanged under `irpt-x10-v1`. Expected: `repository.py` and `composition.py` at the IB-pr-369 commit, and
   the registry row past `fdc0a92a21`. Prove every member by reading the code, including anything they import that changed. Leave
   every other row alone.
2. **Edit those staged rows in place:** full 40-char pin and the sha256 of the blob at the pin. Commit. That commit is the release
   pin P.
3. **Census at P:** `python infra/aws/lambda/ci/release-census.py irpt-export-render --pin P`. Every changed member must be
   intentional and owned: the repinned rows plus `submit_installed.py`, owned by IB-pr-369.
4. **BUILD_ONLY from a clean tree at P.** `git status --porcelain` must be empty first. Run
   `BUILD_ONLY=1 bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-export-render`, then record rc and the built
   sha256. Remove any residue afterwards. Never run without `BUILD_ONLY=1`.
5. **Census file:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~178/IB83-1_e9_repin_census.json`, with
   `{pin, changed_members:[{member, state, built, live, owner_commit, why}], build_only:{rc, tree_clean, built_sha256}}`.
6. **Packet:** `.../0.9.0_WK_IRPT_BCKEND~178/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-370.md`, containing:
   - P and the census table with owners;
   - Branch A (released) and Branch B (rollback: the artifact S3 version and live CodeSha256 `idanP8nX...`, read live, saying if it
     moved);
   - the writers of each changed property;
   - **the E8 status question, answered from the code.** Does the packaged code admit a `PENDING_ENFORCEMENT` policy row for
     retention, or only `ACTIVE`? How does `~M2`'s PENDING -> ACTIVE flip reach a function that packages the registry as a staged
     file: another repin and release, or something else? Use the word ACTIVE.
   - **a regression arm for the release order,** shaped like IB-pr-368's AMENDMENT 1: an offline differential replay of an
     `irpt-x10-v1` fixture through the live and built zips, plus a negative control.
   - the two after-reads for the LATER order, after `~K2`'s E2 retains a real report: an Opal `custody-report-read` of one real
     CUSTODY_REPORT by reference returns it; another firm gets `OBJECT_NOT_COVERED` with no body.

<criterion id="IB83-1-AC1" cell_refs="IB-pr-370"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r83/p83_cells.py" . IB83-1-AC1</invocation><expect>IB83-1-AC1 PASS</expect></criterion>
`IB83-1-AC1` -- the census re-run at P lists exactly your census file's members, each owned, with repository.py among them. Base: FAIL.

<criterion id="IB83-1-AC2" cell_refs="IB-pr-370"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r83/p83_cells.py" . IB83-1-AC2</invocation><expect>IB83-1-AC2 PASS</expect></criterion>
`IB83-1-AC2` -- at P the packaged repository.py has per-family revisions, the packaged registry carries irpt-custody-x10-v1, entry.py
routes custody-report-read, and a clean-tree BUILD_ONLY is recorded with rc 0. Base: FAIL.

<criterion id="IB83-1-AC3" cell_refs="IB-pr-370"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r83/p83_cells.py" . IB83-1-AC3</invocation><expect>IB83-1-AC3 PASS</expect></criterion>
`IB83-1-AC3` -- the packet names P, the rollback sha, both branches, both after-reads and the ACTIVE question. Base: FAIL.

<expected_criteria>IB83-1-AC1, IB83-1-AC2, IB83-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block and nothing else. No upload, apply or deploy: BUILD_ONLY only. AWS reads only.
- **The source map:** edit only the `irpt-export-render` `staged_from` rows the cell needs, in place.
- **Refusal clause.** If a criterion cannot be met as written, stop, file a row, and report. Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W178-S<k>`. `surfaced_at` is the real time you write the row. Re-read the channel right before you
  append. Gate: `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~178" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~178@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~178 <0.9.0_WK_IRPT_BCKEND~178@opal.agent>" -F <msgfile> -- <paths>`.
  Do NOT pre-`git add`. Write the message file with the Write tool.
- **Search:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools. **ASCII only.**

<paths>
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-370.e9-release-packet.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~178/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 76 (round 83, workstream ~P), cell `IB-pr-370`.
<owned_cells>IB-pr-370</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB83-1-AC1, IB83-1-AC2, IB83-1-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~178/IRPT_BCKEND.TO-IB-pr-370.e9-release-packet.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: P, the commit hashes, the repinned members and why, the built sha256, the answer to the ACTIVE
question, each criterion's last line, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- release-census irpt-export-render at HEAD 0c2bdf7634 (issuer): built 64 / live 64, changed submit_installed.py only (files[] from source_dir); staged repository.py b13bab7495, composition.py 83e8b9577a, registry c4fedd31c5 all predate E9/E8; one function.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission changes.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p83_cells.py dry-run at base 25076d5af5 on dell2 2026-10-08 ~19:5xZ: AC1, AC2, AC3 FAIL (no census file, no packet).
lane: the <paths> block IS the grant; irpt-export-render is ~P's function; the registry file itself is ~M2's and is NOT edited here (only its staged pin).
</preflight>
