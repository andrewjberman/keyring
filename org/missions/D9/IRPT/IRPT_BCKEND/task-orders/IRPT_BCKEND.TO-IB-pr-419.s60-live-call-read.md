# TO IRPT_BCKEND.TO-IB-pr-419 -- live-call read of row D2-S60: one real GET through each route that reaches a call-signature split, and each function's 24h CloudWatch error count

<to_id>IRPT_BCKEND.TO-IB-pr-419</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~281</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>117</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** CTO msg 3732 (row D2-S60: "within the hour, drive ONE real GET through each route that reaches profile_reader, with the CloudWatch error count for the last 24h printed") | **Decomp cell:** `IB-pr-419` (decomposition section 110) | **outcome_ref:** FWD-2

---

## WORKER FACE

**Client data rule (CTO ruling @0e8209c33c item 6).** No account id, balance, fee or flow goes in any tracked file. The repo carries counts,
sha256, status codes and reason codes only. Response bodies stay OUTSIDE the worktree and are deleted file by file at the end.

**The question.** Row D2-S60: three LIVE functions ship `served.py` calls whose keywords the packaged callee does not accept.
- irpt-status (rev 3) and irpt-performance-adapter: `InteractiveAccess(profile_reader=)` at `served.py:1011`, on the CREATE_INPUT path
  for a verified internal subject.
- irpt-narrative: `guard_prospect(authorize_owner=, resolve_owner=)` at `served.py:1021`.
- irpt-performance-adapter: `Enforcer(load_report_owner=)`, 2 events in 24h.
Is any live caller failing NOW (FAILING), or is the split reachable but unused (LATENT)? This is a READ. Root: `C:/dev/wk-irpt-bckend-281/`.
Time box: 45 minutes.

**Do:**
1. **CloudWatch, per function, last 24h.** Run `aws logs filter-log-events` over `/aws/lambda/<function>` and count:
   - `"unexpected keyword argument"`;
   - all ERROR lines (`?ERROR ?Traceback ?"Task timed out"`).
   Auto-paginate and count client-side; print the window.
2. **One real GET per route** that reaches each split. Go through the function's real entry: `aws lambda invoke` with an API Gateway
   GET event shaped like the live route's.
   - Use a verified internal subject's headers where the split needs one.
   - Use a synthetic or Opal-internal principal, never a client login.
   - GET only: no POST, no CREATE that writes.
   - If the split is reachable only by a write (CREATE_INPUT), drive the nearest read on the same `served.py` path, and say which split
     the GET does and does not reach.
   - Record the route, status_code and error class (from the response and the request's own log lines).
3. Write `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~281/IB117-4_live_call_read.json` as
   `{window, functions:[{function, cloudwatch_24h:{unexpected_keyword, errors_total}, gets:[{route, status_code, error_class,
   reaches_split}], verdict: "FAILING"|"LATENT", reason}]}`. FAILING means a live caller in the 24h window hit the split, or your
   GET did.

<criterion id="IB117-4-AC1" cell_refs="IB-pr-419"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r117/p117_cells.py" . IB117-4-AC1</invocation><expect>IB117-4-AC1 PASS</expect></criterion>

<expected_criteria>IB117-4-AC1</expected_criteria>

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. AWS reads and GET invokes only; no write, upload, apply or deploy.
- **Refusal clause:** if a criterion cannot be met as written, stop, file a row, and report. Never weaken a check or a test.
- **Row ids** are `IRPT_BCKEND-D2-W281-S<k>`; `surfaced_at` is the real time; check the id is still free just before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~281" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~281@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~281 <0.9.0_WK_IRPT_BCKEND~281@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only.
- **Search:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~281/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-419.s60-live-call-read.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 110 (round 117, workstream ~P), cell `IB-pr-419`.
<owned_cells>IB-pr-419</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB117-4-AC1. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~281/IRPT_BCKEND.TO-IB-pr-419.s60-live-call-read.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message, give each function's counts, each GET's route and status, each verdict, the criterion's last line and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- CloudWatch reads and GET invokes on three live functions; nothing written, nothing deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change; GETs only.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p117_cells.py dry-run at base box/dell2 on dell2 2026-10-09 ~16:5xZ: AC1 FAIL (no read); ruff clean.
lane: the <paths> block IS the grant; ~P's (CTO msg 3732).
</preflight>
