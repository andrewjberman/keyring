# TO IRPT_BCKEND.TO-IB-pr-373 -- E10 recut: the custody writer persists with a SERVER-DERIVED owner and account set, reached only through the guarded Entry or an in-function scheduled run; release packet carries the ACTIVE registry row

<to_id>IRPT_BCKEND.TO-IB-pr-373</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~181</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>86</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** CTO ruling msg 1651 (RECUT; replaces IB-pr-372), on CTO ADDENDUM 10 (E10) | **Decomp
cell:** `IB-pr-373` (decomposition section 79) | **outcome_ref:** FWD-8 / IRPT_CUSTDY hop S07 | **depends_on:** IB-pr-371 (E9 live,
PbyqmHBQ), E8 ACTIVE (b4d98a4fe3).

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-irpt-bckend-181` (branch `wk-IRPT_BCKEND-181`, cut from `box/dell2`). Work, build and commit only there.
`L` = `infra/aws/lambda/investor-reporting`. Paths below are relative to the worktree. Keep scratch outside the worktree.

**Why this is a recut.** IB-pr-372 (branch `wk-IRPT_BCKEND-180` @3528d24f92, NOT drained, read it for reference only) reached the custody
writer through a marked direct-invoke event in which the CALLER asserted the principal and the account set (row D2-W180-S2). Any
identity able to invoke the function, admin principals included, could then have persisted a custody report under any principal.
**The CTO ruled (msg 1651): a write takes no principal from its caller.** You may reuse 372's sound parts: the composition through
`submit_installed`'s registry-gated probe, its tests of the composed path, and its packaging and ACTIVE-row repin. Rebuild the entry
and the identity model.

**Your cell. Nothing is uploaded or applied.**
1. **The trigger.** The persist is reachable ONLY:
   - (a) through the guarded Entry: a route plus operation behind the existing CUSTOM portal authorizer, with an Opal principal
     verified by the authorizer, as `custody-report-read` is; or
   - (b) as an in-function run on a schedule that reads its own work from server-side state.
   - Choose by reading IRPT_CUSTDY's PRD (`org/missions/D9/IRPT/IRPT_CUSTDY/prd/IRPT_CUSTDY_PRD.md`, hops S06/S07) and the code, and
     say why.
   - For (a), add the route row to `docs/contracts/investor-reporting/v1/routes.json` (status DECLARED) and the operation to
     `L/export/entry.py`; nothing is applied here.
   - For (b), STOP and file a row naming the schedule resource you would need: a Terraform schedule is outside this grant.
2. **Derive the owner server-side.** The owner and the account set come from server-held state: the producer's own retained request
   (an IRPT_CUSTDY custody submission retained through `submit_installed`), or the registry and advisor-ownership map. NEVER from a
   field the caller sends.
   - The request names WHICH retained request to persist, by reference. The server loads it, checks the caller's authority over it
     (the same `retained_export.resolve` rule the read uses), and takes owner and accounts from it.
3. **Remove the direct-invoke path.** `L/export/entry.py` must carry NO `irpt_custody_persist` branch.
4. **Accepted source evidence (row D2-W180-S1).** The ACTIVE custody family is accepted-only, so `persist_custody_report` alone is
   refused ("published reports require accepted source evidence"). Pass the producer's accepted source refs taken from the retained
   request.
   - If `L/reports/custody_write.py` needs a `retention_dependencies` parameter, it is granted here. Change only that.
5. **Tests:** `L/export/tests/test_custody_writer_composed.py`, with test names containing:
   - `custody_writer_composed`: a CUSTODY_REPORT is retained under `irpt-custody-x10-v1` (ACTIVE fixture) and read back; an unregistered
     kind refuses.
   - `derived_owner`: a caller-supplied principal, owner or account field in the request cannot change what is stored; the stored
     owner equals the retained request's.
   - `guarded_or_scheduled`: an unauthenticated, a non-Opal, and an other-firm caller each refuse with existing codes; a marked
     direct-invoke event is not handled.
   - Show one negative control per group.
6. **Package, pin, census, BUILD_ONLY, packet,** as IB-pr-372 did:
   - `custody_write.py` (and any new module) packaged by `irpt-export-render`;
   - the registry row repinned to `b4d98a4fe3` or later;
   - commit = pin P;
   - census at P, every member owned;
   - BUILD_ONLY from a clean tree;
   - census file `deliverables/0.9.0_WK_IRPT_BCKEND~181/IB86-1_e10_census.json`, holding `{pin, entry_point, trigger, changed_members,
     build_only}`;
   - packet `deliverables/0.9.0_WK_IRPT_BCKEND~181/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-373.md`.
   - **The packet must also contain:**
     - the trigger and its authentication;
     - the server-side source of the owner and accounts;
     - for (a), the route to apply AFTER the function (as IB-pr-363/364 ordered);
     - Branch A and Branch B: rollback to live `PbyqmHBQpr4DC76qt0noBfoqKVleydNaJ7s2qsx5mT0=`, read live;
     - a replay regression arm;
     - the two after-reads once IRPT_CUSTDY E2a retains a real report: an Opal `custody-report-read` by reference returns it, and
       another firm gets `OBJECT_NOT_COVERED` with no body.

<criterion id="IB86-1-AC1" cell_refs="IB-pr-373"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r86/p86_cells.py" . IB86-1-AC1</invocation><expect>IB86-1-AC1 PASS</expect></criterion>
`IB86-1-AC1` -- the census re-run at P equals the census file's members, each owned; the writer and the registry row are among them;
the packaged irpt-custody-x10-v1 is ACTIVE. Base: FAIL.

<criterion id="IB86-1-AC2" cell_refs="IB-pr-373"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r86/p86_cells.py" . IB86-1-AC2</invocation><expect>IB86-1-AC2 PASS</expect></criterion>
`IB86-1-AC2` -- the three test groups pass (composed, derived owner, guarded or scheduled), and entry.py carries no irpt_custody_persist
direct-invoke path. Base: FAIL.

<criterion id="IB86-1-AC3" cell_refs="IB-pr-373"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r86/p86_cells.py" . IB86-1-AC3</invocation><expect>IB86-1-AC3 PASS</expect></criterion>
`IB86-1-AC3` -- the packet names P, the rollback sha, the host function, both branches and both after-reads, and the census file records
a clean-tree BUILD_ONLY with rc 0. Base: FAIL.

<expected_criteria>IB86-1-AC1, IB86-1-AC2, IB86-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block and nothing else. No upload, apply or deploy: BUILD_ONLY only. AWS reads only.
- **No IAM, bucket, table, principal or Terraform change.** A route is a DECLARED contract row only; it is applied by the later release
  order. A schedule resource STOPS the cell (row).
- **Every `.py` edit passes `.tools/commit-gate.sh`**; safe-commit runs it.
- **Refusal clause.** If a criterion cannot be met as written, stop, file a row, and report. Never weaken a check or a test.
- **Row ids** are `IRPT_BCKEND-D2-W181-S<k>`; `surfaced_at` is the real time. Gate: `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~181" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~181@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~181 <0.9.0_WK_IRPT_BCKEND~181@opal.agent>" -F <msgfile> -- <paths>`.
  Do NOT pre-`git add`. Write the message file with the Write tool.
- **Search:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools. **ASCII only** (no control bytes either).

<paths>
infra/aws/lambda/investor-reporting/export/entry.py
infra/aws/lambda/investor-reporting/export/submit_installed.py
infra/aws/lambda/investor-reporting/export/custody_persist.py
infra/aws/lambda/investor-reporting/export/tests/test_custody_writer_composed.py
infra/aws/lambda/investor-reporting/reports/custody_write.py
infra/aws/lambda/ci/lambda-source-map.json
docs/contracts/investor-reporting/v1/routes.json
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-373.custody-writer-server-derived-owner.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~181/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 79 (round 86, workstream ~P), cell `IB-pr-373`.
<owned_cells>IB-pr-373</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB86-1-AC1, IB86-1-AC2, IB86-1-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~181/IRPT_BCKEND.TO-IB-pr-373.custody-writer-server-derived-owner.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: P, the trigger chosen and why, how the owner and accounts are derived server-side, the commit hashes,
the census members, the built sha256, each criterion's last line, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- irpt-export-render (live PbyqmHBQ) is the S07 host; persist_custody_report has 0 production callers at HEAD; IB-pr-372's caller-asserted entry is NOT drained (CTO msg 1651), so HEAD carries no persist path.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission changes; the trigger rides the existing CUSTOM portal authorizer or STOPS for a schedule.
comp-routes: RUN -- api 7k3ed8px20 carries custody-report-read behind the CUSTOM portal authorizer (IB-pr-364); a new persist route, if chosen, is a DECLARED contract row applied only by a later release order after the function.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: a schedule resource STOPS the cell; none is added.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p86_cells.py dry-run at base b012511132 on dell2 2026-10-08 ~21:2xZ: AC1, AC2, AC3 FAIL (no census file, no test, no packet); 0 control bytes in the check.
lane: the <paths> block IS the grant; irpt-export-render, export/ and reports/custody_write.py are ~P's (IB-pr-351); routes.json rows are added by the cell that owns the route (IB-pr-355 precedent); the registry content is ~M2's (staged pin only).
</preflight>
