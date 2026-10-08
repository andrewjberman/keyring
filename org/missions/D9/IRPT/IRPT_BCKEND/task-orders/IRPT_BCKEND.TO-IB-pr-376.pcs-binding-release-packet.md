# TO IRPT_BCKEND.TO-IB-pr-376 -- release packet for IB-pr-375: irpt-export-render packages persisted_by and the composition-hash binding of the Performance client statement; clean-tree BUILD_ONLY; never-widen packet

<to_id>IRPT_BCKEND.TO-IB-pr-376</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~184</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>88</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** CTO half of IB-pr-373 condition 1 (msg 1719: persisted_by and the binding live
before any firm reads a Performance client statement) | **Decomp cell:** `IB-pr-376` (decomposition section 81) | **outcome_ref:** FWD-8 /
IRPT_CUSTDY hop S08 | **depends_on:** IB-pr-375 (drained @ed1303986b), IB-pr-374 (live, rNjtTwcm).

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-irpt-bckend-184` (branch `wk-IRPT_BCKEND-184`, from `box/dell2`). Work, build and commit only there. Keep
scratch outside the worktree. Model your work on IB-pr-370's packet and census
(`deliverables/0.9.0_WK_IRPT_BCKEND~178/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-370.md` and `IB83-1_repository_repin_census.json`).

**What is live and what is not.** `irpt-export-render` CodeSha256 is `rNjtTwcmhpNdHUV7VcO1cRPcC1wHaANm1oIP+Xvf6Ek=` (IB-pr-374).
IB-pr-375 changed two files. They ship differently:
- `export/custody_persist.py` ships from the function's source dir (`files[]`). A HEAD build already carries it, and the census at HEAD
  shows it changed.
- `reports/custody_write.py` ships from a `staged_from` row pinned at `d34a46f37d` (IB-pr-373), so a HEAD build does NOT carry IB-pr-375's
  change. Repin that row in place to the IB-pr-375 commit that changed it (full 40-char pin plus the sha256 of the blob at it). Leave
  every other row alone, unless reading the code proves another row is needed.

**Your cell. Nothing is uploaded or applied.**
1. Repin as above and commit. That commit is pin P.
2. Census at P: `python infra/aws/lambda/ci/release-census.py irpt-export-render --pin P`. Every member must be owned (IB-pr-375's
   commits).
3. **BUILD_ONLY from a clean tree at P.** Porcelain must be empty first. Run with `BUILD_ONLY=1` only, and clean the residue after.
4. **Census file:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~184/IB88-1_census.json`, holding
   `{pin, changed_members:[{member, state, built, live, owner_commit, why}], build_only:{rc, tree_clean, built_sha256}}`.
5. **Packet:** `.../0.9.0_WK_IRPT_BCKEND~184/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-376.md`, containing:
   - P and the census with owners;
   - Branch A (released): the record carries `persisted_by`; a document without the matching `composition_sha256` is refused and writes
     0 blobs;
   - Branch B: rollback to live `rNjtTwcm...`, with its S3 version read live;
   - the writers of each changed property;
   - the replay regression arm for the release order (an irpt-x10-v1 ANALYSIS and PERFORMANCE fixture through the live and built zips,
     plus a negative control), as IB-pr-374 ran it;
   - **the release goes to `0.7.0_AE_CloudOps~DELL2`** (Andrew-direct, msg 1756), FUNCTION ONLY. The route waits for the IAM leg
     (separate pair, @77440a907b).

<criterion id="IB88-1-AC1" cell_refs="IB-pr-376"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r88/p88_cells.py" . IB88-1-AC1</invocation><expect>IB88-1-AC1 PASS</expect></criterion>
`IB88-1-AC1` -- the census re-run at P equals your census file's members, each owned, with custody_persist.py among them. Base: FAIL.

<criterion id="IB88-1-AC2" cell_refs="IB-pr-376"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r88/p88_cells.py" . IB88-1-AC2</invocation><expect>IB88-1-AC2 PASS</expect></criterion>
`IB88-1-AC2` -- a clean-tree BUILD_ONLY is recorded with rc 0, and the packet names P, the rollback sha, both branches, persisted_by and
composition_sha256. Base: FAIL.

<expected_criteria>IB88-1-AC1, IB88-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block and nothing else. No upload, apply or deploy: BUILD_ONLY only. AWS reads only.
- **The source map:** edit only `irpt-export-render`'s staged rows the cell needs, in place.
- **Refusal clause.** If a criterion cannot be met as written, stop, file a row, and report. Never weaken a check.
- **Naming.** In prose, call the report the "Performance client statement"; code ids are unchanged.
- **Row ids** are `IRPT_BCKEND-D2-W184-S<k>`; `surfaced_at` is the real time. Gate: `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~184" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~184@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~184 <0.9.0_WK_IRPT_BCKEND~184@opal.agent>" -F <msgfile> -- <paths>`.
  Do NOT pre-`git add`. Write the message file with the Write tool. **ASCII only**, no control bytes.
- **Search:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools.

<paths>
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-376.pcs-binding-release-packet.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~184/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 81 (round 88, workstream ~P), cell `IB-pr-376`.
<owned_cells>IB-pr-376</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB88-1-AC1, IB88-1-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~184/IRPT_BCKEND.TO-IB-pr-376.pcs-binding-release-packet.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: P, the repinned rows and why, the commit hashes, the built sha256, each criterion's last line, and any
row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- release-census irpt-export-render at HEAD 6061d0e274 (issuer): built 66 / live 66, changed custody_persist.py only; custody_write.py is a staged row pinned d34a46f37d (source map read), so IB-pr-375's change to it needs the repin; one function.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission changes; the IAM leg is its own pair (@77440a907b, CTO half @5f65b4f40e).
comp-routes: DECLARED-NOT-APPLICABLE -- no route change; the custody-report-persist route is DECLARED and unapplied.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p88_cells.py dry-run at base 7c08fe294e on dell2 2026-10-08 ~22:4xZ: IB88-1-AC1 FAIL, IB88-1-AC2 FAIL (no census file); 0 control bytes in the check.
lane: the <paths> block IS the grant; irpt-export-render is ~P's function.
</preflight>
