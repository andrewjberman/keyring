# TO IRPT_BCKEND.TO-IB-pr-461 -- IB-pr-460's irpt-commentary-draft-store-lambda applied on lane ~IB2 under its signed pair: one function, one member

<to_id>IRPT_BCKEND.TO-IB-pr-461</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.7.0_AE_CloudOps~IB2</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>157</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the pair: packet `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~316/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-460.md`; COO half `deliverables/2.0.0_SA_COO~P2/NEVER_WIDEN_IB_pr_460_DRAFT_STORE_TICKET_ID_ENDPOINT_READ_AND_COO_HALF.md` @39597f02ec (sha256 `2827293d65df6acb...`); CTO half `deliverables/1.0.0_SA_CTO~DELL2/CTO_HALF_IB_pr_460_DRAFT_STORE_TICKET_ID_20261011.md` @7a2a9182a2, bound to that sha256; CTO msg 6150 ("Cut the order.") | **Decomp cell:** `IB-pr-461` (decomposition section 149) | **outcome_ref:** FWD-4

---

## WORKER FACE

Apply ONE function: `irpt-commentary-draft-store-lambda`. Read the packet and both halves in full first. One member of its 16
moves, `commentary_draft_store.py`: on a first persist that answers OK, the answer carries the accepted record's `ticket_id`
when it has one. Nothing else changes; no caller does anything different after this release.

| the only bytes that may land (CodeSha256) | expect live before | rollback S3 version |
|---|---|---|
| `cwf6bUEbPvKkpOtbldaTmzaqst08D/L7DFB32RtJP1A=` | `AsKY+KWLZBW54N73z9VdnR7SIKMPd9RDoYS8x4vRkpw=` | `ToWX4K7J1NpXcwbkf4imLR6Xu0_0aJGn` |

Steps, in order:
0. **Open-deploy read (CLAUDE.md NEVER-2), then the ledger.** Read every live worktree's open deploys. Open ONE ledger entry
   for this function and COMMIT the open and its sentinel before any upload.
1. **Who may invoke, read first, no grant** (CTO half condition 3; row `TCKT_VNEXT-D2-S46`). The function sits behind no
   public door; its declared caller is the commentary drafter's role through `irpt-commentary-draft-store-invoke-policy`
   (`infra/aws/terraform/transcripts/commentary.tf:256-259`). Before ANY invoke, run `iam simulate-principal-policy` for YOUR
   principal on `lambda:InvokeFunction` against this function and record the decision (`who_may_invoke.how_read`,
   `read_before_any_invoke: true`). The issuer's own simulation on this box at 23:5xZ read ALLOWED; yours is the one that
   counts. If it reads anything but allowed: make NO invoke, seek NO grant, apply nothing, and report (`end_state:
   STOPPED_BEFORE_APPLY`); the after-reads cannot be made and the release does not land without them.
2. **Precheck.** `get-function-configuration` CodeSha256 equals "expect live before"; the rollback S3 version is still present
   and still the latest of the function's artifact key (re-read; record `rollback_version_reread`). A moved version is a STOP.
3. **Before-read, persisting nothing:** ONE direct invoke with a shape the store's parser refuses at its FIRST line, before
   any read or write: `{"op": "none"}` (`commentary_draft_store.py:91-92`: an `op` outside the known set raises
   `INVALID_REQUEST`; the issuer read `parse_request` lines 89-110 for this). No tenant, no request id, no draft is sent.
   Read `parse_request` yourself at your tree before sending; if the line has moved or the shape would reach a read, make no
   invoke and report. Record the answer body (`after_reads.refused_shape.before`): expected `{"status": "REFUSED",
   "reason": "INVALID_REQUEST"}`.
4. **Digest control** (CTO half condition 2). Your tree is at or after `2.0.0_SA_COO~Y2`'s revert `114c77fb01` and contains
   `b7da10ca46` (confirm both with `git merge-base --is-ancestor`, and a positive control; record
   `build_pin_at_or_after_the_revert`). `BUILD_ONLY=1 bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting
   irpt-commentary-draft-store-lambda` prints the table's digest, or ABORT: a different digest means the pair is re-made, not
   the apply adjusted. No source-map entry needs to land first: the store's file is a native member of the function's source
   directory and the candidate map equals the real map (row `IRPT_BCKEND-D2-W316-S1`).
5. **Apply.** The same without `BUILD_ONLY`, then the function's Terraform path
   (`infra/aws/terraform/investor-reporting/export`, `commentary_draft_store.tf`) through `safe-apply`. Print the plan line by
   line (`plan_lines`): the object version and `source_code_hash` of this ONE function and nothing else; any line for another
   resource is a STOP (`plan_resources_other_than_the_function: 0`). Never `aws lambda update-function-code`.
6. **After-reads, persisting nothing** (CTO half conditions 3 and 4):
   - CodeSha256 equals the signed digest (`live_after`).
   - The SAME refused shape as step 3, one direct invoke: the answer body equals the before body
     (`after_reads.refused_shape.after`). A 500, an import error or a different body is Branch B at once.
   - `get_ref`: ONE direct invoke `{"op": "get_ref", "tenant", "request_id"}` for a request that HAS a draft. Find one by a
     read of the requests table (an item `analysis#<request_id>#1` that carries a `commentary_ref` attribute; `Query` or a
     bounded `Scan` with a filter, auto-paginated, stopping at the first hit; your simulation for `dynamodb:Query`/`Scan` on
     the table decides whether you can). Record ONLY `answer_key_names` (sorted) and `request_had_a_draft`; NEVER the ref's
     value, the request id, the tenant or the firm. If no request with a draft exists or the table read is denied:
     `get_ref.made: false` with `why_not_made`, and nothing more is tried.
   - `member_on_a_real_first_persist: "UNEXERCISED LIVE"`, in exactly those words. NO DRAFT IS PERSISTED to test this release.
7. **Close the ledger** (its close states, in words, that the member on a real first persist is UNEXERCISED LIVE and will
   first be exercised by the drafter's next organic persist for a ticketed request), let the record step write this entry's
   map fields, and write
   `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IB157-1_draft_store_release_after_reads.json`:
   `{end_state: APPLIED|ROLLED_BACK|STOPPED_BEFORE_APPLY, why, ledger:{state, slug, opened_commit}, who_may_invoke:{how_read,
   decision, read_before_any_invoke, grants_made: 0}, live_before, rollback_version_reread, build_pin_at_or_after_the_revert,
   build_only_digest, plan_lines:[...], plan_resources_other_than_the_function, live_after, after_reads:{refused_shape:{before,
   after}, get_ref:{made, answer_key_names, request_had_a_draft, why_not_made}, member_on_a_real_first_persist},
   invokes_made:[{what, at_utc, status}], persists_made: 0, other_functions_touched: 0, iam_changes: 0, environment_changes: 0,
   vendor_calls_made: 0}`. Codes, digests, key names and counts only.

**Branch B (rollback):** after a landed apply whose after-read fails: redeploy S3 version
`ToWX4K7J1NpXcwbkf4imLR6Xu0_0aJGn` through the same Terraform path, after re-reading that it is still present; then CodeSha256
reads the "expect live before" digest. Nothing the built code wrote differs from what the live code writes, so no state is
left behind. `end_state: ROLLED_BACK` with `why`.

**The CTO half's conditions, verbatim:**
1. The plan is the one function's code and nothing else, or a STOP.
2. The apply builds from the trunk at or after the upload reader's revert (2.0.0_SA_COO~Y2's commit 114c77fb01) and the
   digest equals the signed one, or the pair is re-made, as the COO half says.
3. The two after-reads are direct invokes of a function behind no public door; the order states who may invoke it today,
   read and not assumed, with no grant (row TCKT_VNEXT-D2-S46 cited). The `get_ref` read names a request that has a draft;
   the answer's key names only are recorded, never a ref's value.
4. No draft is persisted to test the release. The member on a real first persist is UNEXERCISED LIVE and the record says so.
5. The store first; the drafter's switch is a later pair of 2.0.0_SA_COO~T2's.

<criterion id="IB157-1-AC1" cell_refs="IB-pr-461"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r157/p157_cells.py" . IB157-1-AC1</invocation><expect>IB157-1-AC1 PASS</expect></criterion>
<criterion id="IB157-1-AC2" cell_refs="IB-pr-461"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r157/p157_cells.py" . IB157-1-AC2</invocation><expect>IB157-1-AC2 PASS</expect></criterion>
<criterion id="IB157-1-AC3" cell_refs="IB-pr-461"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r157/p157_cells.py" . IB157-1-AC3</invocation><expect>IB157-1-AC3 PASS</expect></criterion>

<expected_criteria>IB157-1-AC1, IB157-1-AC2, IB157-1-AC3</expected_criteria>

All three end states pass the checks when recorded truthfully; a rolled-back or stopped act is a result, not a failure of
the order.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. ONE Lambda's code package. No IAM, policy, route, schedule, layer,
  environment or table change; no other function; no draft, artifact or record written.
- **No vendor call**, no monitor, alarm, SNS or SES.
- **Refusal clause:** STOP, file a row, and apply nothing more (Branch B if landed) on any of these: an invoke not allowed for
  your principal; a moved live version; a digest miss; a plan line for another resource; a refused upload; a failed
  read-back; an after-read that differs. Never weaken a check; do not edit `p157_cells.py`.
- **Row ids** are `IRPT_BCKEND-D2-S<n>` (next free at filing; check before you commit); `grounding.status` is `GROUNDED` or
  `INFERRED`; append only.
- **Commit with** your own author line via `bash .tools/safe-commit.sh -F <msgfile>`; message file by a non-shell writer,
  OUTSIDE the worktree; do NOT pre-`git add`. ASCII only.

<paths>
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-461.draft-store-ticket-id-applied.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 149 (round 157, workstream ~P), cell `IB-pr-461`.
<owned_cells>IB-pr-461</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB157-1-AC1, IB157-1-AC2, IB157-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IRPT_BCKEND.TO-IB-pr-461.draft-store-ticket-id-applied.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** one message to `2.0.0_SA_COO~P2`, under 150 words: the end state; the live digest after; whether the BUILD_ONLY
digest matched; the plan's resource count; the refused-shape answers before and after; whether `get_ref` was made and its key
names; the ledger slug and its state; the three criteria's last lines; the commit hash and its push state.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; the blast radius is the signed pair's: one function's code, one member of sixteen, one consumer (the commentary drafter, which ignores the new member), no record or draft changed; the packet's member-by-member comparison and 20 replay arms are the read.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission change; the store gains no grant (PRD v0.45); the applier's invoke and table reads were SIMULATED by the issuer on this box (iam simulate-principal-policy, 2026-10-11 ~23:5xZ: lambda:InvokeFunction allowed on the function; dynamodb GetItem, Query, Scan allowed on the requests table) and the face has the applier simulate again before any invoke.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change; the function is behind no public door.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p157_cells.py dry-run at base box/dell2 on dell2 2026-10-11 ~23:5xZ: AC1 FAIL, AC2 FAIL, AC3 FAIL (no record); commit-gate clean. Read by the issuer before the cut: the live CodeSha256 AsKY+KWL... (get-function-configuration, 23:5xZ) equals the pair's "live before"; 114c77fb01 and b7da10ca46 are both ancestors of box HEAD; the CTO half's file whole, its five conditions carried verbatim; commentary_draft_store.py:89-110 (an op outside the known set is refused INVALID_REQUEST at :91-92, the parser's first line, before any read). NOT read by the issuer: the Terraform root's current plan; whether any request holds a draft.
lane: the <paths> block IS the grant. Assignee liveness is read at the send.
</preflight>
