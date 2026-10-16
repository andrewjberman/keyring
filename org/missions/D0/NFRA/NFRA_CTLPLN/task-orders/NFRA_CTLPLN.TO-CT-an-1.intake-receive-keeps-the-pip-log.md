# TO NFRA_CTLPLN.TO-CT-an-1 -- workstream OUTCOME round 16 (cell CT-an-1): the install leaves a log -- `intake_receive.py` `prove` and `install` write the child pip's full output, command line and pinned environment to a log beside the receipt, and the receipt names the log and its SHA-256

<to_id>NFRA_CTLPLN.TO-CT-an-1</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~126</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<status_reason>Closed by the issuer 2.0.0_SA_COO~C after its own re-run in the main tree after merge 79ee07a0b7 (worker branch wk-NFRA_CTLPLN-126 @74aeadbbab): CTan1-AC1 PIP-LOG arms=7/7 ok=True; CTan1-AC2 INTAKE-RECEIVE-TEST cases=34/34 ok=True (base 32/32); diff paths inside the order; proof instance VALID. Row W126-S1 OBSERVATION, ARMED, adjudicated by MSTR msg 109561 as the ruled WARN-only state (not a defect). LOCAL until MSTR pushes.</status_reason>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>16</round>
<workstream>OUTCOME</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-an-1` (`decompositions/NFRA_CTLPLN_DECOMP.round24.md`) | **outcome_ref:** FWD-15 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

PRD outcome FWD-15 (a delivered file is checked from the file alone). The CTO's round-23 analysis (`ledger/ROUND_ANALYSIS.round23.md` ruling 2) found that dell1's install receipt reached the laptop only as a relayed summary and asks that the receipt come from dell1 itself: `verify` and `prove` output with the SHA-256, and the install run with `--no-index` plus ITS LOG. Today `org/devices/intake/intake_receive.py` runs pip through `run_pip` (about line 353), which captures pip's stdout and stderr and returns only the LAST non-empty line, so no log of the run exists. The tool already builds ONE pip command (`build_pip_command`: `pip install --no-index --no-deps`, a local wheel path, `--target` or `--user`) and a child environment that removes every inherited `PIP_*` variable and pins `PIP_NO_INDEX=1`, `PIP_DISABLE_PIP_VERSION_CHECK=1` and `PIP_CONFIG_FILE=` the null device (`build_child_env`). Each receipt records the command, the return code and `received_sha256` (`write_receipt`, about line 416). Read `org/devices/intake/intake_receive.py` whole first (782 lines: `prove_pack`, the install verb and its install receipt `receipts/<wheel>.install.<device>.json`, `receipt_gate`) and `org/devices/intake/test_intake_receive.py` (32 of 32 at the cut; it builds synthetic wheels with `ir.build_synthetic_wheel` and installs them into temporary folders with the real pip, no network). HONEST LIMIT to keep in the code comments and the report: the log records the command, the pinned environment and what pip itself printed. It is NOT a network trace and does not prove that no packet left the box; it shows that the tool asked pip for no index and that no inherited index setting reached pip.

YOUR WORKTREE WAS CUT BY `.tools/wk-provision.sh` AND IS A SPARSE CHECKOUT: it holds `.tools/`, `lib/`, the project folder `org/missions/D0/NFRA/NFRA_CTLPLN/`, `org/modules/graph/`, `org/devices/`, `infra/logic/registry/`, `org/standards/` and the paths of this order. If a command fails because a file or folder is missing, run `git sparse-checkout add <folder>`, retry, and name the folder, the command and the error in your final report.

### BUILD

1. **Capture the whole run.** `run_pip` keeps its `(rc, last_line)` return for its callers and ALSO makes the full captured text available (for example a third return value or a module-level record of the last run; choose the smaller change and keep the existing callers and tests working).
2. **Write the log.** A new function writes `<pack>/receipts/<wheel>.prove-pip.<device>.log` after a `prove` pip run and `<pack>/receipts/<wheel>.install-pip.<device>.log` after an `install` pip run (ASCII, LF line ends, UTF-8-safe: non-ASCII bytes replaced with `?`). Content, in this order: a first line `INTAKE-PIP-LOG schema=1`; `device=`; `utc=`; `kind=prove` or `kind=install`; `python=` (the version); `command=` the command list as a JSON line; `env_pins=` the pinned names with their values (`PIP_NO_INDEX=1`, `PIP_DISABLE_PIP_VERSION_CHECK=1`, `PIP_CONFIG_FILE=` the null device); `inherited_pip_vars_removed=` the NAMES ONLY of the `PIP_*` variables that were in the parent environment and were removed (never a value: a value may hold a URL or a credential); `rc=`; then a line `--- pip stdout+stderr ---` and pip's full captured text. Cap the pip text at 200000 bytes and, if it is cut, end the file with a line `TRUNCATED at 200000 bytes`.
3. **Name the log in the receipt.** The prove receipt and the install receipt gain a key `pip_log` = `{"file": <log file name>, "sha256": <hex of the log file bytes>, "bytes": <size>}`. When pip did NOT run (a refused prove, a refused install, a dry run) there is NO log and NO `pip_log` key. `receipt_gate` and every other reader keep working on a receipt WITHOUT the key (an older receipt must still clear the gate: add no requirement for the key).
4. Do NOT change `build_pip_command`, the command a receipt records, `MISSING_RE`, the grading, the schema string, or any verb's last line. No new dependency.
5. A NEW test `.tools/tests/test_round24_pip_log.py` (standard library plus `intake_receive`; temporary folders; synthetic wheels as `test_intake_receive.py` builds them; every pip run goes to a local wheel with `--no-index`). Arms: (a) `prove` on a good synthetic pack writes the prove log; it is ASCII only, its `command=` line carries `--no-index` and `--no-deps`, `rc=0`, `device=` and `kind=prove`; (b) the prove receipt's `pip_log.sha256` equals the SHA-256 of the log file bytes you compute in the test, `pip_log.bytes` equals the file size, and `received_sha256` equals the wheel's SHA-256 computed in the test; (c) `install --target <new temp folder>` writes the install log and the install receipt names it with a matching SHA-256; (d) with `PIP_INDEX_URL=http://127.0.0.1:9/simple` and `PIP_FIND_LINKS=<a temp folder>` set in the PARENT environment, the log's `inherited_pip_vars_removed=` line lists both NAMES and the log holds neither the URL, nor `127.0.0.1`, nor the temp folder value, and has no line that starts with `Looking in indexes`; (e) CONTROL of the instrument: the same assertion function applied to a hand-made log text that contains `Looking in indexes: http://127.0.0.1:9/simple` returns FAIL (the check can see an index line); (f) a refused `prove` (a pack whose wheel has no good check record) writes NO log file and its receipt has NO `pip_log` key; (g) a receipt whose `pip_log` key is deleted by the test still clears `install --dry-run` (an older receipt is accepted). Last line `PIP-LOG arms=<k>/<n> ok=<True|False>`.
6. Add two cases to `org/devices/intake/test_intake_receive.py` (its own count grows from 32): `prove` writes a log the receipt names, and a parent `PIP_INDEX_URL` value never appears in the log. Change nothing else in that file.

### RULES FOR THIS CELL

Write surface = the `<paths>` plus your own folder `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~126/`. Every experiment runs in a temporary folder or repository unless the cell says otherwise. No push, no deploy, no AWS write. Use `.tools/safe-commit.sh` for every commit, with explicit file paths. Do NOT commit the `portal` gitlink or `org/git-author-override-audit.laptop.log`. ASCII only; Python 3.12; bash is Git Bash 3.6.7 (default utilities only). CLAUDE.md and org/XXX.md are LOCKED. COMMIT A WORK-IN-PROGRESS COMMIT AS SOON AS A FILE EXISTS, and again after each criterion passes. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~105/NFRA_CTLPLN.TO-CT-ah-1.sparse-safe-commit-abs-path-link-batch.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W126-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working. 

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTan1-AC1" cell_refs="CT-an-1"><invocation>python .tools/tests/test_round24_pip_log.py</invocation><expect>ok=True</expect></criterion>
`CTan1-AC1` -- `prove` and `install` write a pip log beside the receipt, the receipt names it with a matching SHA-256, no inherited index value reaches the log, and a refused run writes none (base: the test does not exist); report the whole last line with its denominator.

<criterion id="CTan1-AC2" cell_refs="CT-an-1"><invocation>python org/devices/intake/test_intake_receive.py</invocation><expect>ok=True</expect></criterion>
`CTan1-AC2` -- the receiving tool's own suite passes with the two new cases (base: `INTAKE-RECEIVE-TEST cases=32/32 ok=True`; the count must grow); report the whole last line.
</proof_of_spec>

<expected_criteria>CTan1-AC1,CTan1-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 280`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~126/NFRA_CTLPLN.TO-CT-an-1.intake-receive-keeps-the-pip-log.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTan1-AC1,CTan1-AC2` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round24.md</decomp_doc>
<owned_cells>CT-an-1</owned_cells>
</decomp_ref>

<paths>
org/devices/intake/intake_receive.py
org/devices/intake/test_intake_receive.py
.tools/tests/test_round24_pip_log.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call, no network; the test installs synthetic local wheels into temporary folders with pip and --no-index.
comp-adversary: RUN -- a parent PIP_* VALUE (a URL, a credential) leaking into the log (arm d, names only); the log read as proof of no network traffic (it is not: the cell text and the code comment say so); a receipt that is rejected because it lacks `pip_log` (arm g keeps older receipts valid); an unbounded log (cap and TRUNCATED line); the `receipts/` folder gaining a stray file that makes `verify` report STRAY (run the existing suite; the logs live under `receipts/`, which the tool creates and owns); a log file name colliding with a receipt name (`<wheel>.receipt.<device>.json` and `<wheel>.install.<device>.json` differ from the `.prove-pip.` and `.install-pip.` names); BLIND: Python 3.12 pip on the laptop prints differently from Python 3.14 pip on dell1, so the test pins the structure, not pip's wording.
risk: LOCAL -- one local receiving tool and its tests; synthetic wheels installed into temporary folders with --no-index; no network and no real package.
lane: the <paths> block IS the grant (worker RULING 1). `org/devices/intake/` is NFRA_CTLPLN's intake route (C-INTAKE); the CTO ruled the receipt (round-23 analysis ruling 2).
</preflight>

Base checks, dry-run by the issuer before the cut: CTan1-AC1 FAIL as expected (the test does not exist); CTan1-AC2 base `INTAKE-RECEIVE-TEST cases=32/32 ok=True` (a control; the count must grow).
Source: CTO round-23 analysis sections 2-4 (`ledger/ROUND_ANALYSIS.round23.md` @32c2378d19); FWD-15.
