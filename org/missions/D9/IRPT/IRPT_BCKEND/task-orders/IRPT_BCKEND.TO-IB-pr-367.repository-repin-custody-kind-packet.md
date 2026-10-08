# TO IRPT_BCKEND.TO-IB-pr-367 -- irpt-export-render packages a repository.py whose KINDS carries CUSTODY_REPORT: the repin, a clean-tree BUILD_ONLY, and the never-widen packet for its release

<to_id>IRPT_BCKEND.TO-IB-pr-367</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~175</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>80</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** CTO round analysis ADDENDUM 4 @eba8fde8bb (msg on sweep 18), E7, ruling row
D2-W172-S3 | **Decomp cell:** `IB-pr-367` (decomposition section 73) | **outcome_ref:** FWD-8 / CUSTDY hop 5 (IRPT_CUSTDY E2 waits on it) |
**depends_on:** IB-pr-364 (drained @fd99fb52e5).

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-irpt-bckend-175` (branch `wk-IRPT_BCKEND-175`). Work and commit only there. Paths below are relative
to it.

**The gap.** The custody-report route is live (IB-pr-364), but it cannot return a custody report to anyone.
- `irpt-export-render`'s source map row (`infra/aws/lambda/ci/lambda-source-map.json`, function `irpt-export-render`, `staged_from`)
  packages `reports/repository.py` at pin `83e8b9577a`. There, `KINDS = ("PERFORMANCE", "ANALYSIS")`.
- HEAD's `reports/repository.py` has carried `CUSTODY_REPORT` in KINDS since `b13bab7495` (IB-pr-336).
- So an owner read of a CUSTODY_REPORT fails closed with DEPENDENCY_UNAVAILABLE.

**Your cell. Nothing is uploaded or applied.**
1. **Find the minimal repin set.** Move the `repository.py` staged row past `b13bab7495`. Add any other staged row the custody READ path
   needs to serve a CUSTODY_REPORT: check the `infra/logic/registry/reporting_policies.json` row (pinned `c4fedd31c5`) and any member
   the read path imports. Prove each one by reading the code, never by guessing. Leave every other row alone.
2. **Edit those rows in place.** Each takes a full 40-char `pin` and the `sha256` of the blob at that pin, in the same format as the
   other rows. Change nothing else, and do not re-serialize the file. Commit it. That commit is the release pin P.
3. **Census at P:** `python infra/aws/lambda/ci/release-census.py irpt-export-render --pin P`. Every changed member must be one you
   repinned on purpose, with its owner commit.
4. **BUILD_ONLY from a clean tree at P.**
   - Print `git status --porcelain` first; it must be empty.
   - Then run `BUILD_ONLY=1 bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-export-render`. Never run it without
     `BUILD_ONLY=1`.
   - Record rc and the built sha256.
   - The build stages copies into the source dir (row D2-S3). Afterwards remove every untracked file it left and restore any modified
     tracked file, so your tree is clean again.
5. **Write the census file:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~175/IB80-1_repository_repin_census.json`.
   It holds `pin` (P, full sha), `changed_members` (a list of `{member, state, built, live, owner_commit, why}`), and `build_only`
   (`{rc, tree_clean, built_sha256}`).
6. **Write the packet:** `.../0.9.0_WK_IRPT_BCKEND~175/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-367.md`. Use
   `deliverables/0.9.0_WK_IRPT_BCKEND~171/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-363.md` as the model. It must contain:
   - P;
   - the census table with an owner per member;
   - which principal classes change (Branch A, released) and the rollback (Branch B): artifact S3 version and live CodeSha256
     `03p2eIEKU9iSIOe5GYDbkbisapqAjULUyAPA/Wcxrfc=` (read it live and say if it moved);
   - the writers of each changed property;
   - the two after-reads for the later release order: (1) an Opal `custody-report-read` of one REAL CUSTODY_REPORT by reference
     returns that report and revision; (2) another firm's read returns `OBJECT_NOT_COVERED` with no body.
   - Say which seat can produce the real CUSTODY_REPORT for after-read 1 (IRPT_CUSTDY, `2.0.0_SA_COO~K2`, E2) and in what order.

<criterion id="IB80-1-AC1" cell_refs="IB-pr-367"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r80/p80_cells.py" . IB80-1-AC1</invocation><expect>IB80-1-AC1 PASS</expect></criterion>
`IB80-1-AC1` -- the census re-run at P lists exactly the members in your census file, each with an owner commit, and repository.py
is among them. Base: FAIL.

<criterion id="IB80-1-AC2" cell_refs="IB-pr-367"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r80/p80_cells.py" . IB80-1-AC2</invocation><expect>IB80-1-AC2 PASS</expect></criterion>
`IB80-1-AC2` -- at P the packaged repository.py's KINDS names CUSTODY_REPORT and the packaged entry.py routes custody-report-read,
and the census file records a clean-tree BUILD_ONLY with rc 0. Base: FAIL.

<criterion id="IB80-1-AC3" cell_refs="IB-pr-367"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r80/p80_cells.py" . IB80-1-AC3</invocation><expect>IB80-1-AC3 PASS</expect></criterion>
`IB80-1-AC3` -- the packet names P, the rollback sha, Branch A and Branch B, and both after-reads. Base: FAIL.

<expected_criteria>IB80-1-AC1, IB80-1-AC2, IB80-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block and nothing else.
- **No upload, no apply, no deploy.** BUILD_ONLY only. AWS reads only (the live CodeSha256 and the artifact version).
- **The source map:** edit only the `irpt-export-render` `staged_from` rows the cell needs, in place.
- **Refusal clause.** If a criterion cannot be met as written, stop, file a row, and report. Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W175-S<k>`. Re-read the channel right before you append. Gate:
  `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~175" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~175@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~175 <0.9.0_WK_IRPT_BCKEND~175@opal.agent>" -F <msgfile> -- <paths>`.
  Do NOT pre-`git add`. Write the message file with the Write tool.
- **Search:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools. **ASCII only.**

<paths>
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-367.repository-repin-custody-kind-packet.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~175/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 73 (round 80, workstream ~P), cell `IB-pr-367`.
<owned_cells>IB-pr-367</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB80-1-AC1, IB80-1-AC2, IB80-1-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~175/IRPT_BCKEND.TO-IB-pr-367.repository-repin-custody-kind-packet.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: P, the commit hashes, the repinned members and why each was needed, the built sha256, each
criterion's last line, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- one function, irpt-export-render (the only function whose staged_from packages reports/repository.py as repository.py for the export dir; worker re-measures per row); release-census at the new pin is the blast measure; nothing is uploaded or applied in this order.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission changes.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change; custody-report-read is already live (IB-pr-364).
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p80_cells.py dry-run at base 2c287dec89 on dell2 2026-10-08 ~18:3xZ: AC1, AC2, AC3 FAIL (no census file, no packet); KINDS at HEAD ("PERFORMANCE", "ANALYSIS", "CUSTODY_REPORT") vs the pinned 83e8b9577a ("PERFORMANCE", "ANALYSIS"), read.
lane: the <paths> block IS the grant; irpt-export-render is ~P's function (ADDENDUM 4).
</preflight>
