# TO NFRA_CTLPLN.TO-CT-aj-1 -- workstream OUTCOME round 6 (cell CT-aj-1): step 1 of the package journey -- every fetch record names its device (W111-S1), and the laptop-side refusal that names the route is recorded (FWD-19, FWD-18)

<to_id>NFRA_CTLPLN.TO-CT-aj-1</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~112</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<status_reason>Closed by the issuer 2.0.0_SA_COO~C after its own re-run in wk-NFRA_CTLPLN-112 @941e0ed9aa (merged at the drain): FETCH-DEVICE arms=8/8 ok=True; WRAPPER-REFUSAL rc=3 names_route=True ok=True; INTAKE-REQUESTS arms=15/15 ok=True; INTAKE-FETCH-TEST cases=19/19 ok=True; proof VALID. W111-S1 is closed for fetch records written by intake_fetch.py; intake_check.py is a second writer with no device key (W112-S4), carried.</status_reason>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>6</round>
<workstream>OUTCOME</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-aj-1` (`decompositions/NFRA_CTLPLN_DECOMP.round20.md`) | **outcome_ref:** FWD-19, FWD-18 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

PRD outcomes FWD-19 (`prd/NFRA_CTLPLN_PRD.md` line 214: what did this box download today, answered from a record) and FWD-18 (line 199: a download tried on purpose is stopped and told the route that works). Round 19 built `org/devices/intake/intake_request.py` (read it and `.tools/tests/test_round19_intake_requests.py`). Its `downloads --device D --day YYYYMMDD` reader cannot attribute a record to a device, because the fetch record written by `org/devices/intake/intake_fetch.py` (schema `intake-fetch/1`) names the fetching seat in `fetched_by` and carries no device key (row `NFRA_CTLPLN-W111-S1`; Grep that id in `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` first). This cell is step 1 of one journey: a real package a Dell lane needs is fetched, checked, delivered and installed in the rounds after it. FWD-18's laptop-side arm is the refusal text of `org/devices/kit_pip_no_egress.py`.

YOUR WORKTREE WAS CUT BY `.tools/wk-provision.sh` AND IS A SPARSE CHECKOUT: it holds `.tools/`, `lib/`, the project folder `org/missions/D0/NFRA/NFRA_CTLPLN/`, `org/modules/graph/`, `org/devices/`, `infra/logic/registry/`, `org/standards/` and the paths of this order. If a command fails because a file or folder is missing, run `git sparse-checkout add <folder>`, retry, and name the folder, the command and the error in your final report.

### BUILD

1. **Device key.** In `org/devices/intake/intake_fetch.py`, write a `device` field into every new fetch record, derived (the box's device name from `lib/devices.py` / `AGENTBUS_DEVICE`, never typed), and bump the schema string only if the existing readers and `org/devices/intake/test_intake_fetch.py` allow it (they must still pass). Do not edit existing records.
2. **Reader.** In `org/devices/intake/intake_request.py` `downloads`, count a record for the device it names; a record with NO `device` key is counted under `UNATTRIBUTED` and printed as `unattributed=<n>`, never guessed to belong to the asking device. The line becomes `DOWNLOADS-TODAY device=<D> day=<day> requests=<n> files=<k> unattributed=<u>`. Keep every arm of `.tools/tests/test_round19_intake_requests.py` passing (edit its expectation for the added field only).
3. **FWD-18, laptop side.** Run `python org/devices/kit_pip_no_egress.py wrap -- download six` ONCE (read the kit first; it must refuse before any network request, and you must set `PIP_NO_INDEX=1` in the child environment as a second guard; if the kit could reach the network, STOP and file a BLOCKING row). Record its printed refusal and exit code verbatim in `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~112/FWD18_LAPTOP_REFUSAL.md`, and say whether the refusal names the route that works (`org/devices/intake/`).
4. A NEW test `.tools/tests/test_round20_fetch_device.py`: with flag `--device`, a temporary intake folder, one fetch produced through the real `intake_fetch.py` code path with its network call replaced by a local stub (no network; read the file to find the seam), asserts the record carries `device`, then the reader counts it for that device and counts an old-shape record (no `device`) as unattributed. Last line `FETCH-DEVICE arms=<k>/<n> ok=<True|False>`. With flag `--wrapper`, run the kit's `wrap -- download six` refusal in a child process and assert exit code non-zero, no network (the child's environment has `PIP_NO_INDEX=1`), and the refusal text contains `org/devices/intake`. Last line `WRAPPER-REFUSAL rc=<rc> names_route=<True|False> ok=<True|False>`.

### RULES FOR THIS CELL

Write surface = the `<paths>` plus your own folder `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~112/`. Every experiment runs in a temporary folder or repository unless the cell says otherwise. No push, no deploy, no AWS write. Use `.tools/safe-commit.sh` for every commit, with explicit file paths. Do NOT commit the `portal` gitlink or `org/git-author-override-audit.laptop.log`. ASCII only; Python 3.12; bash is Git Bash 3.6.7 (default utilities only). CLAUDE.md and org/XXX.md are LOCKED. COMMIT A WORK-IN-PROGRESS COMMIT AS SOON AS A FILE EXISTS, and again after each criterion passes. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~105/NFRA_CTLPLN.TO-CT-ah-1.sparse-safe-commit-abs-path-link-batch.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W112-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working. 

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTaj1-AC1" cell_refs="CT-aj-1"><invocation>python .tools/tests/test_round20_fetch_device.py --device</invocation><expect>ok=True</expect></criterion>
`CTaj1-AC1` -- a fetch record carries its device and the reader counts per device, with old records unattributed (base: the file does not exist); report the whole last line.

<criterion id="CTaj1-AC2" cell_refs="CT-aj-1"><invocation>python .tools/tests/test_round20_fetch_device.py --wrapper</invocation><expect>ok=True</expect></criterion>
`CTaj1-AC2` -- the kit's refusal for a download is non-zero, makes no network request and names the intake route (base: the file does not exist); report the whole last line.

<criterion id="CTaj1-AC3" cell_refs="CT-aj-1"><invocation>python .tools/tests/test_round19_intake_requests.py</invocation><expect>ok=True</expect></criterion>
`CTaj1-AC3` -- the round-19 request, decision and downloads suite still passes (base: `INTAKE-REQUESTS arms=15/15 ok=True`, a control); report the whole last line.
</proof_of_spec>

<expected_criteria>CTaj1-AC1,CTaj1-AC2,CTaj1-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 280`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~112/NFRA_CTLPLN.TO-CT-aj-1.fetch-record-device-key-and-wrapper-refusal.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTaj1-AC1,CTaj1-AC2,CTaj1-AC3` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round20.md</decomp_doc>
<owned_cells>CT-aj-1</owned_cells>
</decomp_ref>

<paths>
org/devices/intake/intake_fetch.py
org/devices/intake/intake_request.py
.tools/tests/test_round19_intake_requests.py
.tools/tests/test_round20_fetch_device.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call; the fetch's network call is stubbed in the test and the kit refusal runs with PIP_NO_INDEX=1.
comp-adversary: RUN -- a real network fetch started by the test (the stub seam is asserted and `PIP_NO_INDEX=1` is set in every child); the reader guessing a device for an old record (the unattributed arm); the schema bump breaking the other intake tools (`test_intake_fetch.py`, `test_intake_check.py`, `test_intake_seam.py` are run before the final commit); the wrapper reaching pip's index (read the kit; STOP if so); BLIND: the real fetch, check, taildrop and install of a package a Dell lane needs are the next rounds; the Dell's own download count needs that box's seat.
risk: LOCAL -- temporary folders, a stubbed fetch and one refusal run with the index disabled; no real package moves.
lane: the <paths> block IS the grant (worker RULING 1). `org/devices/intake/` is NFRA_CTLPLN's laptop-side intake folder (C-INTAKE); the CTO ordered the chain (round-19 analysis ruling 2).
</preflight>

Base checks, dry-run by the issuer before the cut: CTaj1-AC1 and CTaj1-AC2 FAIL as expected (the file does not exist); CTaj1-AC3 base `INTAKE-REQUESTS arms=15/15 ok=True` (a control).
Source: CTO round-19 analysis sections 2-3 (`ledger/ROUND_ANALYSIS.round19.md` @2009d89478), msg 109424; FWD-19, FWD-18.
