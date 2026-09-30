# TO-IB-yr-282 -- two served answers on this lane's surface tell the truth: correction words where the browser reads, and a named refusal for an absent bundle

<to_id>IRPT_BCKEND.TO-IB-yr-282</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~92</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<issued_date>2026-09-30</issued_date>
<status>dispatched</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>28</round>
<workstream>~Y</workstream>

**Directive:** D9 | **Fabric:** laptop | **Workstream:** ~Y | **Decomp cell:** `IB-yr-282` (`decompositions/IRPT_BCKEND_DECOMP_R28_Y.md`)

---

## WORKER FACE

### THE CELL -- two defects of one kind: a served answer that does not say the true thing

**This order is cut under a rule this lane learned the hard way: NAME THE PATH BEFORE THE PART.** Five defects in
three rounds came from verifying a function in isolation and calling it an outcome. Both halves below are stated as a
PATH, and both paths are measured, not assumed.

**(a) The correction words reach nothing a browser reads.** Round 24 put `RESOLVE_RETRY_EXHAUSTED` and a `CORRECT`
action into `ops/status.py::build_envelope`. **That function has exactly two callers and NEITHER can pass
`NEEDS_CORRECTION`:** `ops/status_loader.py:164` passes only `RUNNING` or `UNCERTAIN`, and `ops/owned_status.py:59`
takes `public_state` from `PHASES`, whose 11 durable phases map only to `QUEUED`/`RUNNING`/`FAILED`/`UNAVAILABLE`
plus a `READY` override. **The answer a browser actually receives for an upload needing correction is built at
`intake/uploads.py:313-320`** as its own dict: `upload_id`, `input_id`, `state`, `reason`, `findings`,
`findings_total`, plus `template` on the template lane. **Make the words reach THAT dict** -- the same vocabulary the
envelope declares -- so a user is told what to do next on the path that answers them.

**(b) A READY report with no rendered bundle answers `UNEXPECTED`.** Row `IRPT_BCKEND-S213`: window 24's K10 read
`GET .../analysis/RPT-2e21b52e.../sections` -> 200, `UNAVAILABLE`, `public_reason_code: UNEXPECTED`. The path:
`routes.json` sends that route to handler **`irpt-status`**, operation `analysis-report`; `ops/entry.py:61`
`OPERATION_REPORT = "analysis-report"`, served through `reports/status_installed.py`; the projection is
**`ops/owned_report.py`**, which already raises named refusals (`REPORT_RETENTION_REQUIRED`,
`READY_REPORT_RECEIPT_REQUIRED`, `ANALYSIS_REPORT_NOT_READY`). The absent-bundle case escapes all of them and lands on
the residual. **Name it.**

**THE TRAP THE ISSUER MEASURED SO YOU DO NOT LOSE A DAY TO IT.** `_authz/served.py:770` ends `public_reason_for` with
`return code if code in BOUNDARY_REASONS else "UNEXPECTED"`. **A new reason code that is not a member of the closed
enum is silently clamped straight back to `UNEXPECTED`** -- you would add a named refusal, watch the answer stay
`UNEXPECTED`, and have nothing to look at.

**ISSUER RULING, and it is not yours to revisit: USE AN EXISTING MEMBER. Do not extend `PUBLIC_REASONS`.** That enum
is CLOSED and its own comment records that it was *"derived by SUBTRACTION over the outcomes the six handler families
can actually reach ... rather than as a forward list of reasons that came to mind"*; adding a member is a taxonomy
proposal under CLAUDE.md rule 24 with a four-postulate record and a token census, and this cell does not need one.
**The member is `NOT_READY`**, under the enum's own heading *"the state of the thing being asked about"*: the report
JSON exists, the bundle the page asks for does not. `DEPENDENCY_UNAVAILABLE` is the wrong axis -- the renderer is this
system's, not a dependency it does not control. **So `_authz/errors.py` is NOT in your grant and must not change.**

**Out of scope, deliberately:** making the report never reach READY without a bundle. That is the deeper half of
S213 and it belongs with the certifier cell next round, because a report READY without its bundle and a Comparison
certified without its comparison are the same defect -- publication asserting more than it checked.

### ACCEPTANCE (run from your worktree root unless the invocation says otherwise)

<criterion id="Y28-2-AC1" cell_refs="IB-yr-282"><invocation>cd infra/aws/lambda/investor-reporting && python -m pytest -q -p no:cacheprovider intake/tests/ -k correction</invocation><expect>at least 1 test, 0 failed -- a test you add asserting the NEEDS_CORRECTION answer from `intake/uploads.py` carries the correction vocabulary</expect></criterion>

<criterion id="Y28-2-AC2" cell_refs="IB-yr-282"><invocation>cd infra/aws/lambda/investor-reporting && python -m pytest -q -p no:cacheprovider ops/tests/test_owned_report.py</invocation><expect>0 failed, including a test you add asserting the absent-bundle case answers NOT_READY and NOT UNEXPECTED</expect></criterion>

<criterion id="Y28-2-AC3" cell_refs="IB-yr-282"><invocation>cd infra/aws/lambda/investor-reporting && python -m pytest -q -p no:cacheprovider reports/tests/test_status_installed.py ops/tests/test_status.py</invocation><expect>0 failed (control: the status boundary and the envelope are unchanged)</expect></criterion>

<expected_criteria>Y28-2-AC1,Y28-2-AC2,Y28-2-AC3</expected_criteria>

**Issuer's base dry-run, measured at CLOUD HEAD:**

- **AC1 -- the served dict at `intake/uploads.py:313-320` carries NO `actions` and NO `public_reason_code` key**, read
  at source. The test does not exist yet, so `-k correction` currently selects nothing; **a criterion that selects
  nothing is not a pass**, and your added test is what makes the number real. Report the selected count.
- **AC2 -- the suite passes today and the absent-bundle assertion does not exist.** So AC2 is a **both-ends**
  criterion: the existing tests must stay green AND your new one must be among them. Report the count before and after.
- **AC3 -- green at base. THIS IS THE CONTROL.** `build_envelope` and the status boundary are NOT the path and must
  not move; a cell that "fixes" the envelope instead of the answering dict fails its own control, and that is exactly
  the mistake round 24 made.

## BOUNDS

- **Grant.** The `<paths>` block plus `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~92/` and
  this order's file. **`_authz/errors.py` and `_authz/served.py` are READ-ONLY and out of grant** -- if you believe
  the enum must grow, that is a REFUSAL AND A ROW, not an edit. `ops/status.py` is READ-ONLY: round 24 already put the
  vocabulary there and the defect is that nothing reaches it.
- **No AWS call, no deploy, no Terraform, no vendor/external network call.** Served code moves through
  `2.0.0_SA_COO~P`'s rebuild, never by you.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise
  row, and do not weaken a test to pass. **Three of the last four rounds were refused for an ISSUER defect and every
  refusal was right** -- a file you need that is not in `<paths>` is a refusal and a row naming the file, not your
  shortfall.
- **Row ids** are `IRPT_BCKEND-W92-S<k>`, appended with a `## <ID> -- <one line>` markdown heading; re-read the
  channel immediately before writing and re-check `<k>`; `hazard_standing` is `ARMED` or `INERT` only. Gate:
  `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `.tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~92 <0.9.0_WK_IRPT_BCKEND~92@opal.agent>" -F <msgfile> -- <paths>`; do NOT pre-`git add`; the message file is written by the Write tool or python, never a shell heredoc and never a `python -c "..."` containing double quotes.
- **Verify every commit with git, not the tool's stdout** (`git status --porcelain <path>` empty).
- **MSYS trap (row S215):** a unix path inside a `python -c` SOURCE BODY is not converted. Pass paths as argv.
- **Search discipline:** raw recursive `grep`/`find` in Bash is gated; use `comp-find` or native Grep/Glob/Read, and
  never pipe `comp-find` into `head`.

<paths>
infra/aws/lambda/investor-reporting/intake/uploads.py
infra/aws/lambda/investor-reporting/intake/tests/
infra/aws/lambda/investor-reporting/ops/owned_report.py
infra/aws/lambda/investor-reporting/ops/tests/test_owned_report.py
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R28_Y.md</decomp_doc> round 28, workstream ~Y, cell `IB-yr-282`.
<owned_cells>IB-yr-282</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: Y28-2-AC1, Y28-2-AC2, Y28-2-AC3. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~92/IRPT_BCKEND.TO-IB-yr-282.served-answers-tell-the-truth.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> Y28-2-AC1,Y28-2-AC2,Y28-2-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** each criterion's output line with counts before and after; the exact reason code the
absent-bundle case now serves; whether anything tempted you toward `_authz/`; the diff summary; and the commit hash.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule, trigger or scheduled producer is touched.
comp-blast: RUN -- WORLD: both halves change what a SERVED answer says, on two live routes (the upload answer and GET analysis/{jobId}/sections). Blast radius bounded by the ruling that no new reason code is minted: the answer moves from the residual UNEXPECTED to NOT_READY, both already members of the closed PUBLIC_REASONS enum, so no contract, schema or consumer enum changes and no published file moves. The upload half adds keys to a dict the browser already receives; it removes none. Nothing served moves until ~P rebuilds.
comp-iam: DECLARED-NOT-APPLICABLE -- no boto3 call, no role, no grant.
comp-adversary: RUN -- four risks. (1) The worker "fixes" ops/status.py's envelope, which is where the words already are and where round 24 went wrong: ops/status.py is READ-ONLY in the grant and AC3 is a green-at-base control over the envelope and status boundary, so moving them turns it red. (2) The worker adds a new PUBLIC_REASONS member and watches served.py:770 clamp it back to UNEXPECTED, losing a day: the issuer measured the clamp, the order quotes the line, rules an existing member (NOT_READY), and puts _authz/ out of grant entirely. (3) AC1 selects nothing and is read as a pass -- pytest -k with no match exits 0: the face states that a criterion selecting nothing is NOT a pass and requires the selected count in the report. (4) The worker also tries to stop reports reaching READY without a bundle, which is the deeper and more tempting fix: explicitly out of scope, named as next round's certifier cell, because publication asserting more than it checked is one defect and should be cut once.
lane: the <paths> block IS the grant. intake/ and ops/ carry no open ~M or ~P order. NOTE for the record: ops/** and intake/** sit inside lane IRPT_LIVE_SCOPE_P / IRPT_COMPLETION_P, where 2.0.0_SA_COO~Y is NOT a permitted agent -- the worker is admitted by .owned-paths.yaml's top-level worker_grant, which resolves a 0.9.0_WK_* serial to exactly its own order's <paths> and never through a lane. That is why this cell is a worker cell and not a direct act.
</preflight>
