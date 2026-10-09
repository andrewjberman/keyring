# TO IRPT_BCKEND.TO-IB-pr-416 -- three live irpt functions rebuilt from one tree so every served.py call fits its packaged callee; attribute-call limb; never-widen packet

<to_id>IRPT_BCKEND.TO-IB-pr-416</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~278</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>117</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** row IRPT_BCKEND-D2-S60 (2.0.0_SA_COO~Y2, msg 3722), ruled by this issuance's row | **Decomp cell:** `IB-pr-416` (decomposition section 110) | **outcome_ref:** FWD-2

---

## WORKER FACE

**Client data rule (CTO ruling @0e8209c33c item 6).** No account id, balance, fee or flow goes in any tracked file. The repo carries counts,
sha256 and reason codes only. Extracted zips and any client data stay OUTSIDE the worktree and are deleted file by file at the end.

**The defect (row D2-S60).** Three live functions ship `served.py` with calls whose keywords the PACKAGED callee does not accept. The
source tree at HEAD agrees with itself; the zips were built from mixed members.
- `served.py:1011` passes `InteractiveAccess(profile_reader=)` in irpt-status and irpt-performance-adapter. The packaged
  `interactive_access.py` takes `(read_headers, data_firm, *, ordinary_authorizer)`.
- `served.py:1021` passes `guard_prospect(authorize_owner=, resolve_owner=)` in irpt-narrative.
- irpt-performance-adapter logs `Enforcer.__init__() unexpected keyword load_report_owner` (2 events in 24h). That is an attribute call,
  which `signature_closure.py` cannot see.
- Instrument: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r2/signature_closure.py <zip>`.
Root: `C:/dev/wk-irpt-bckend-278/`.

**Build:**
1. **Attribute-call limb.** Copy the instrument to `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~278/signature_closure_attr.py`
   and extend it so `module.Cls(...)` and `module.f(...)` calls, where `module` is a packaged module, are checked the same way. Its last
   line adds `attr_checked=<k> attr_mismatched=<m>`. Leave ~Y2's original file untouched.
2. **Negative control.** Fetch each LIVE zip (`aws lambda get-function`, Code.Location) to scratch outside the worktree. Run both
   limbs. Each must report at least one mismatch; the performance-adapter must show the Enforcer split on the attribute limb.
3. **Rebuild** irpt-narrative, irpt-performance-adapter and irpt-status the way IB-pr-409 built irpt-narrative (read
   `deliverables/0.9.0_WK_IRPT_BCKEND~272/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-409.md` and its build scripts first). Use one pinned tree, with
   every member that `served.py` calls taken from that same pin. Pack twice to byte-identical output and upload nothing. Both limbs must
   read 0 mismatches on each built zip. If a member must stay at an older pin for a reason in a packet, stop and file a row.
4. **Census** `deliverables/0.9.0_WK_IRPT_BCKEND~278/IB117-1_signature_census.json`:
   `{functions:[{function, pin, built_sha256, built_twice_identical, live_sha256, live_signature_mismatched,
   live_attribute_mismatched, built_signature_mismatched, built_attribute_mismatched, changed_members}]}`.
5. **Packet** `deliverables/0.9.0_WK_IRPT_BCKEND~278/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-416.md`, in IB-pr-409's packet form:
   - per function: live and built sha256, the changed members, Branch A (land it) and Branch B (restore the live version, named and
     re-read at apply);
   - the ADDENDUM 18 red list, showing your members touch none of its targets;
   - replay arms in 409's form, at least the no-row-internal and prospect arms, live zip against built zip, every verdict `identical`
     or `expected-diff`.
   - per CTO msg 3732, the packet carries both `signature_closure.py` (with your attribute limb) and the live-call arm of IRPT_ANLREQ's
     release 1 half AMENDMENT 5 beside the zip census.
   The pair is ~P2's COO half and the CTO half. **irpt-status's apply waits on IRPT_ANLREQ release 1 (2.0.0_SA_COO~Y2 is rolling it
   back); say so in the packet.** Applying is NOT in this order; it comes by amendment once the pair is signed.

<criterion id="IB117-1-AC1" cell_refs="IB-pr-416"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r117/p117_cells.py" . IB117-1-AC1</invocation><expect>IB117-1-AC1 PASS</expect></criterion>
<criterion id="IB117-1-AC2" cell_refs="IB-pr-416"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r117/p117_cells.py" . IB117-1-AC2</invocation><expect>IB117-1-AC2 PASS</expect></criterion>

<expected_criteria>IB117-1-AC1, IB117-1-AC2</expected_criteria>

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. BUILD_ONLY plus AWS reads; no upload, apply or deploy.
- **Do not edit product source.** The tree is self-consistent at HEAD. If it is not, stop, file a row and report.
- **Every `.py` edit passes `.tools/commit-gate.sh`**; safe-commit runs it.
- **Refusal clause:** if a criterion cannot be met as written, stop, file a row, and report. Never weaken a check or a test.
- **Row ids** are `IRPT_BCKEND-D2-W278-S<k>`; `surfaced_at` is the real time; check the id is still free just before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~278" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~278@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~278 <0.9.0_WK_IRPT_BCKEND~278@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only.
- **Search:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~278/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-416.signature-closure-rebuild.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 110 (round 117, workstream ~P), cell `IB-pr-416`.
<owned_cells>IB-pr-416</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB117-1-AC1, IB117-1-AC2. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~278/IRPT_BCKEND.TO-IB-pr-416.signature-closure-rebuild.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message, give each function's live and built mismatch counts, the built sha256, each criterion's last line and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- three function zips built, nothing uploaded; the apply is a later amendment under a never-widen pair.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p117_cells.py dry-run at base box/dell2 on dell2 2026-10-09 ~16:5xZ: AC1 FAIL, AC2 FAIL (no census, no packet); ruff clean.
lane: the <paths> block IS the grant; ~P's (row D2-S60 names 2.0.0_SA_COO~P2 its disarm owner).
</preflight>
