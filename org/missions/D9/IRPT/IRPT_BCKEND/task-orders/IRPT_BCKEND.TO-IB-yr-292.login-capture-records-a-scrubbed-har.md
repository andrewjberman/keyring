# TO-IB-yr-292 -- the login/session capture records a Playwright HAR behind YC_RECORD_HAR=1, and a scrub proven by a planted value strips every credential and cookie value

<to_id>IRPT_BCKEND.TO-IB-yr-292</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~95</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<issued_date>2026-09-30</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>29</round>
<workstream>~Y</workstream>

**Directive:** D9 | **Fabric:** laptop | **Workstream:** ~Y | **Decomp cell:** `IB-yr-292` (`decompositions/IRPT_BCKEND_DECOMP_R29_Y.md`)

---

## WORKER FACE

### THE CELL

`infra/aws/ec2/investor-reporting-ycharts/ycharts_session.js` is the YCharts session library (Playwright/chromium).
It creates a browser context in TWO places, both as `browser.newContext({ userAgent: UA, viewport: { width: 1280,
height: 900 } })`: inside `acquireSession` (around line 972) and inside `withAuthenticatedPage`'s `openContext`
(around line 1381). It records no HAR today. The resident's per-job ledger (cell IB-yr-291) cannot see the LOGIN and
WAF legs; only the browser can.

**Your cell, part 1 -- the recording, opt-in only.** Add ONE exported function `contextOptions()` that returns the
context options object. With `process.env.YC_RECORD_HAR` unset it returns exactly what the two sites pass today
(`userAgent`, `viewport`) and NO `recordHar` key. With `YC_RECORD_HAR === '1'` it adds
`recordHar: { path: process.env.YC_RECORD_HAR_PATH, content: 'omit' }` -- bodies omitted, headers kept for the
scrub. With `YC_RECORD_HAR === '1'` and no `YC_RECORD_HAR_PATH` it THROWS (a recording with nowhere to go is a
refusal, never a default path). Both `newContext` sites call `contextOptions()`. Playwright writes the HAR when the
CONTEXT closes: on the acquire path's non-`keepContext` branch and in `withAuthenticatedPage`'s own teardown, close
the context (`await ctx.close()`, best-effort try/catch) BEFORE `browser.close()` so the file is flushed even if a
future Playwright stops flushing on browser close. Export `contextOptions` from `module.exports`.

**Your cell, part 2 -- the scrub, as a check, not a promise.** Add `har_scrub.py` (Python 3, stdlib only, ASCII
only) in the same directory with `scrub(src_path, dst_path) -> dict`. It reads the HAR JSON, and for every entry's
request and response: every header whose name is `cookie`, `set-cookie` or `authorization` (case-insensitive) has
its `value` replaced by `<redacted:len=N>` (N = the original length); every `cookies[].value` is replaced the same
way; every other header and field is left byte-for-byte. It writes `dst_path`, then RE-READS the output bytes and
counts occurrences of every ORIGINAL value it replaced -- that count is `residual_hits`. It returns
`{"headers_scrubbed": <int>, "cookies_scrubbed": <int>, "residual_hits": <int>, "entries": <int>}` and, run as a CLI
(`python har_scrub.py <src> <dst>`), prints that dict as JSON on one line. A HAR with none of those headers scrubs to
IDENTICAL bytes (the negative control). Never print, log or keep an original value.

**Part 3 -- the test and the README row.** `tests/test_har_scrub.py` (pytest) with a PLANTED value in a synthetic
HAR on all four paths (request Cookie, response Set-Cookie, Authorization, cookies[].value) asserting 0 occurrences
in the output bytes and the census counts, plus the negative control. One row in `README.md`'s file table for
`har_scrub.py`, and one line under the environment pointers naming `YC_RECORD_HAR` / `YC_RECORD_HAR_PATH` as
opt-in, off by default.

**Why:** Andrew-direct 2026-09-30 ~06:5xZ *"record HAR and identify the endpoints that appear in that recording"*;
CTO half condition 8 and CRO half condition 4 (W27): the HAR is scanned for credential and cookie values with a
planted-value control, counts printed, before it leaves the host. The raw HAR never enters the repo.

### ACCEPTANCE (run from your worktree root unless the invocation says otherwise)

<criterion id="Y29-2-AC1" cell_refs="IB-yr-292"><invocation>node org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y/R29_checks/check_292_context_options.js</invocation><expect>PASS: contextOptions -- off: no recordHar; on: path honoured, content omit; no path: refused</expect></criterion>

<criterion id="Y29-2-AC2" cell_refs="IB-yr-292"><invocation>python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y/R29_checks/check_292_har_scrub.py</invocation><expect>PASS: planted value absent from the scrubbed output on every path; harmless header kept; negative control byte-identical</expect></criterion>

<criterion id="Y29-2-AC3" cell_refs="IB-yr-292"><invocation>node org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y/R29_checks/check_292_suite_control.js</invocation><expect>PASS: offline suite all_pass with the netguard preload</expect></criterion>

<expected_criteria>Y29-2-AC1,Y29-2-AC2,Y29-2-AC3</expected_criteria>

**Issuer's base run at CLOUD HEAD a7a6d286f2 (CTO 103159: the base reading beside every criterion):**

- **AC1 -- FAIL as expected:** `FAIL: contextOptions is not exported (typeof undefined)`.
- **AC2 -- FAIL as expected:** `FAIL: har_scrub not importable from .../infra/aws/ec2/investor-reporting-ycharts`.
- **AC3 -- PASS as expected (control):** arms `a_five_surfaces, b_no_otp_branch, c_bounded_eviction,
  d_lease_and_fencing, e_offline`, `summary.all_pass true`. **It is green at base and must stay green.** The suite
  refuses to start without `node --require ./tests/netguard.js` (row S121); the check script passes that preload.
  Your own pytest for part 3 is graded through AC2's planted value; run it and report its count, but it is not a
  fourth criterion.

## BOUNDS

- **Grant.** The `<paths>` block plus `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~95/` and
  this order's file. `tests/run_offline_suite.js`, `tests/replay_browser.js`, `tests/fakes.js`, `tests/netguard.js`
  and the check scripts are READ-ONLY.
- **NO browser launch against anything but the loopback replay, NO vendor call, NO AWS call, no deploy, no SSM.** The
  host picks the file up under `~P`'s next host act; nothing here runs on the runner.
- **Never write a real HAR into the repo.** The synthetic HARs in the test live in temp dirs or in memory.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise
  row, and do not weaken the test to pass. If a file you need is not in `<paths>`, that is a REFUSAL AND A ROW.
- **Row ids** are `IRPT_BCKEND-W95-S<k>`, appended to the project surprise channel with a
  `## <ID> -- <one line>` markdown heading. Other seats append concurrently: re-read immediately before writing and
  re-check your `<k>`. `hazard_standing` is `ARMED` or `INERT`, nothing else. Gate:
  `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `.tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~95 <0.9.0_WK_IRPT_BCKEND~95@opal.agent>" -F <msgfile> -- <paths>`; do NOT pre-`git add`; the message file is written by the Write tool or python, never a shell heredoc and never a `python -c "..."` containing double quotes.
- **Verify every commit with git, not the tool's stdout** (`git status --porcelain <path>` empty).
- **MSYS trap (row S215):** a unix path inside a `python -c` SOURCE BODY is not converted. Pass paths as argv.
- **Search discipline:** raw recursive `grep`/`find` in Bash is gated; use `comp-find` or the native Grep/Glob/Read
  tools, and never pipe `comp-find` into `head`.
- **ASCII only** in every file you write.

<paths>
infra/aws/ec2/investor-reporting-ycharts/ycharts_session.js
infra/aws/ec2/investor-reporting-ycharts/har_scrub.py
infra/aws/ec2/investor-reporting-ycharts/tests/test_har_scrub.py
infra/aws/ec2/investor-reporting-ycharts/README.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y/R29_checks/check_292_context_options.js
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y/R29_checks/check_292_har_scrub.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y/R29_checks/check_292_suite_control.js
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R29_Y.md</decomp_doc> round 29, workstream ~Y, cell `IB-yr-292`.
<owned_cells>IB-yr-292</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: Y29-2-AC1, Y29-2-AC2, Y29-2-AC3. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~95/IRPT_BCKEND.TO-IB-yr-292.login-capture-records-a-scrubbed-har.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> Y29-2-AC1,Y29-2-AC2,Y29-2-AC3` BEFORE the flip. Copy
the shape from `deliverables/0.9.0_WK_IRPT_BCKEND~92/IRPT_BCKEND.TO-IB-yr-282.served-answers-tell-the-truth.proof_of_spec.json`.
</proof_of_spec>

**REPORT (your final message):** each criterion's output line; the two `newContext` sites now calling
`contextOptions()` (line numbers); where the context is closed on each path; your pytest's passed count; the diff
summary; and the commit hash.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule, trigger or scheduled producer is touched.
comp-blast: RUN -- WORLD by the gate's floor (a host script under infra/). Off by default: with YC_RECORD_HAR unset the library's context options are byte-equal to today's, and the offline suite (AC3) is the control that the five surfaces behave as before. On the host nothing changes until ~P's next host act copies the file. Blast radius when armed: one HAR file at a path the operator names, never a default.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, no grant; the secret-id pointers are untouched.
comp-adversary: RUN -- three risks. (1) A HAR with cookie or credential VALUES leaves the host: the scrub is graded on the OUTPUT BYTES with a planted value (AC2) and residual_hits is computed by re-reading the file, not by trusting the replacement loop. (2) The recording turns on by default or invents a path: AC1's arms (unset -> no recordHar; set without a path -> throws). (3) The context is never closed so the HAR is empty: the face requires ctx.close() before browser.close() on both paths; a live recording is read at the window, which is the only place an empty HAR could show, and the window act reads the file size. Blind to Playwright's own HAR content under 'omit' beyond what the scrub covers -- stated, and the CRO's condition 4 scan runs on the real file at the window regardless.
lane: the <paths> block IS the grant. Measured: no non-terminal ~P or ~M order names infra/aws/ec2/investor-reporting-ycharts/ (11 non-terminal orders of 155 scanned, 0 hits). CONTRACT row 24 places recipe/session/broker with Y.
</preflight>
