# TO NFRA_FIDUPL.TO-FX-s-1 -- the two walks: readable sign-in failures, a bounded retry on a 5xx list read, final lines on stderr

<to_id>NFRA_FIDUPL.TO-FX-s-1</to_id>
<project>NFRA_FIDUPL</project>
<issued_to>0.9.0_WK_NFRA_FIDUPL~8</issued_to>
<issued_by>2.0.0_SA_COO~P1</issued_by>
<issued_date>2026-10-21</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>fidelity-r3-walkrobust</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `FX-s-1` (`decompositions/NFRA_FIDUPL_DECOMP_R3.md` section 17) | **outcome_ref:** FWD-9 (C-BACKFILL) |
**depends_on:** FV-s-2 and FW-s-1 (merged)

---

## WORKER FACE

### THE CELL

**FX-s-1** -- Three gaps seen in the live runs of `hist_walk.py` and `api_walk.py`. Fix them in those two files; nothing else.

**Read first:** `hist_walk.py` (`_Run._ensure_session`, `_rows`, `_post`, `execute`, `_say`), `api_walk.py` (`_Run._ensure_session`, `execute`, `_say`), `backfill_main.py` (`_say`), `signin.py` (`SigninError` and its attribute `failure_class`, `FAILURE_CLASSES`), `tests/test_hist_walk.py` and `tests/test_api_walk.py` (the fake session and deps style).

### WHAT TO BUILD

1. **Sign-in failure class.** In both modules, when `deps["open_session"](...)` raises, print one flushed line `SIGNIN failed class=<c>` where `<c>` is `exc.failure_class` when the exception has that attribute and a string from `signin.FAILURE_CLASSES` is held, else the exception's class name; then re-raise unchanged. The run's stop evidence (the `stop` record and the `STOP` line) for a run that ends on an exception during sign-in is `<ExceptionClassName>:<c>` instead of the bare class name (for example `SigninError:code never arrived`). Characters outside `A-Za-z0-9 _.:-` in the class are replaced by `?` and the text is cut to 60 characters. Nothing else about the failure path changes (still one sign-in, exit 1, record written).
2. **Bounded retry of a 5xx status-list read** (`hist_walk.py` only). `_rows` (the Export Status list read) retries a status in `(500, 502, 503, 504)` up to THREE times in all, sleeping 10 seconds (the injectable `sleep`) between tries, and prints `RETRY status=<n> try=<k>`; after the third try it raises `WalkError` as today. Any other non-200 status (a 4xx, and 401 or 403 which halt as `auth`) is NOT retried and behaves exactly as today. The create call (`historicalExport.json`) and downloads are NOT retried.
3. **Final lines on stderr.** In both modules the `STOP ...` line, the `CLOSE ...` line and the final `OK:` or `ERROR:` line are written to stdout exactly as today AND ALSO to stderr (flushed), because SSM cuts a long command's stdout at 24 KB and keeps stderr separately. No other line goes to stderr.
4. Tests in the NEW `tests/test_walk_robust.py` (fakes only, `sleep` injected so none waits): `test_a_failed_sign_in_prints_its_failure_class_and_the_stop_evidence_carries_it` (both modules, a fake `open_session` raising an object with `failure_class`), `test_hist_walk_retries_a_5xx_status_list_read_up_to_three_times` (504, 504, 200 succeeds on the third try; 504 three times raises `WalkError`), `test_hist_walk_does_not_retry_a_4xx_or_an_auth_status` (a 404 and a 403 are each read once; the 403 halts `auth`), `test_the_final_stop_and_ok_lines_also_go_to_stderr_in_both_modules` (captured stderr holds the `STOP`, `CLOSE` and `OK:` lines and no other line).

### ACCEPTANCE

<criterion id="FX-s-1-AC1" cell_refs="FX-s-1"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py fx1</invocation><expect>R1-FX1-OK passed=\d+</expect></criterion>
`FX-s-1-AC1` -- the four named robustness tests exist and pass.

<criterion id="FX-s-1-AC2" cell_refs="FX-s-1"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py fv2</invocation><expect>R1-FV2-OK passed=\d+</expect></criterion>
`FX-s-1-AC2` -- the Historical walk's thirteen tests still pass.

<criterion id="FX-s-1-AC3" cell_refs="FX-s-1"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py fw1</invocation><expect>R1-FW1-OK passed=\d+</expect></criterion>
`FX-s-1-AC3` -- the API walk's seventeen tests still pass.

<expected_criteria>FX-s-1-AC1,FX-s-1-AC2,FX-s-1-AC3</expected_criteria>

Dry-run at the base: `FX-s-1-AC1` base: FAIL as expected; `FX-s-1-AC2` base: PASS as expected; `FX-s-1-AC3` base: PASS as expected.

## BOUNDS

- **Grant.** The `<paths>` block below, this order's file and your deliverables folder.
- **Fakes only.** No network, no AWS, no sign-in from any test. Do not edit `backfill_main.py`, `signin.py`, `land.py` or `fetch.py`: import from them. Existing test files `tests/test_hist_walk.py` and `tests/test_api_walk.py` may be edited ONLY if a change here forces an assertion about stderr or the evidence text to change; say so in your report.
- **Refusal clause.** A premise that fails is a surprise row (`NFRA_FIDUPL-D1-W8-S<k>`, next unused), never a guess.
- **ASCII and Python 3.9 syntax.** The whole module suite must have no failure: its last line goes in your report.

<paths>
infra/aws/ec2/canonical-fidelity/hist_walk.py
infra/aws/ec2/canonical-fidelity/api_walk.py
infra/aws/ec2/canonical-fidelity/tests/test_walk_robust.py
infra/aws/ec2/canonical-fidelity/tests/test_hist_walk.py
infra/aws/ec2/canonical-fidelity/tests/test_api_walk.py
org/missions/D8/NFRA/NFRA_FIDUPL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_DECOMP_R3.md</decomp_doc> (round 3, section 17 addendum), cell `FX-s-1`.
<owned_cells>FX-s-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: FX-s-1-AC1, FX-s-1-AC2, FX-s-1-AC3. Instance at `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.9.0_WK_NFRA_FIDUPL~8/NFRA_FIDUPL.TO-FX-s-1.walk-robust.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> FX-s-1-AC1,FX-s-1-AC2,FX-s-1-AC3` BEFORE the flip. Commit code first, then pin.
</proof_of_spec>

**REPORT:** what was built and where, the test names, each check line verbatim, the module suite's last line, every surprise row id, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched; denominator 0 schedules changed.
comp-iam: DECLARED-NOT-APPLICABLE -- fakes only; denominator 0 IAM statements changed.
comp-adversary: DECLARED-NOT-APPLICABLE -- build on fakes; delivery to the box is by the issuer's message to CloudOps between runs.
lane: the paths block.
</preflight>

Source: CloudOps run reports 9163, 9190, 9192, 9194 (2026-10-21).
