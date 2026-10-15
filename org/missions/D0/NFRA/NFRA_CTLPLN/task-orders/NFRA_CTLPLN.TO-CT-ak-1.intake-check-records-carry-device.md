# TO NFRA_CTLPLN.TO-CT-ak-1 -- workstream OUTCOME round 9 (cell CT-ak-1): step 2 of the package journey -- the records `intake_check.py` writes carry their device, like the fetch record (W112-S4)

<to_id>NFRA_CTLPLN.TO-CT-ak-1</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~116</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>OUTCOME</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-ak-1` (`decompositions/NFRA_CTLPLN_DECOMP.round21.md`) | **outcome_ref:** FWD-19, FWD-15 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

PRD outcomes FWD-19 (`prd/NFRA_CTLPLN_PRD.md` line 214) and FWD-15 (line 162). Round 20 put a `device` key into every fetch record written by `org/devices/intake/intake_fetch.py` (read its `this_device()` and `.tools/tests/test_round20_fetch_device.py`). Row `NFRA_CTLPLN-W112-S4` (Grep that id in `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md`): `org/devices/intake/intake_check.py` is a second writer of `intake-fetch/1`-shaped records (its selftest and its check step) and writes no `device` key, so the downloads reader counts them as unattributed. The package journey's check step runs next, on a real package; it must write attributed records first.

YOUR WORKTREE WAS CUT BY `.tools/wk-provision.sh` AND IS A SPARSE CHECKOUT: it holds `.tools/`, `lib/`, the project folder `org/missions/D0/NFRA/NFRA_CTLPLN/`, `org/modules/graph/`, `org/devices/`, `infra/logic/registry/`, `org/standards/` and the paths of this order. If a command fails because a file or folder is missing, run `git sparse-checkout add <folder>`, retry, and name the folder, the command and the error in your final report.

### BUILD

1. In `org/devices/intake/intake_check.py`, write the same derived `device` field wherever it writes a record of the fetch shape (read the file to find each place; reuse the SAME derivation as `intake_fetch.py this_device()` by importing it, or copy its 12 lines if an import creates a cycle, saying so). A box that cannot be named writes `null`, as the fetch does. The schema string stays `intake-fetch/1` (`org/devices/intake/test_intake_check.py` asserts it).
2. A NEW test `.tools/tests/test_round21_check_device.py` (standard library; temporary intake folder; no network): flag `--device` runs the check step on a tiny local fixture wheel (build it in the test; read `org/devices/intake/test_intake_check.py` for how it builds one), asserts the record it writes carries `device` equal to the derived device name, then that `intake_request.py downloads` counts it for that device and not as unattributed. Last line `CHECK-DEVICE arms=<k>/<n> ok=<True|False>`.
3. Do not change `intake_fetch.py` or `intake_request.py`. Keep `org/devices/intake/test_intake_check.py`, `org/devices/intake/test_intake_fetch.py` and `.tools/tests/test_round20_fetch_device.py --device` passing.

### RULES FOR THIS CELL

Write surface = the `<paths>` plus your own folder `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~116/`. Every experiment runs in a temporary folder or repository unless the cell says otherwise. No push, no deploy, no AWS write. Use `.tools/safe-commit.sh` for every commit, with explicit file paths. Do NOT commit the `portal` gitlink or `org/git-author-override-audit.laptop.log`. ASCII only; Python 3.12; bash is Git Bash 3.6.7 (default utilities only). CLAUDE.md and org/XXX.md are LOCKED. COMMIT A WORK-IN-PROGRESS COMMIT AS SOON AS A FILE EXISTS, and again after each criterion passes. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~105/NFRA_CTLPLN.TO-CT-ah-1.sparse-safe-commit-abs-path-link-batch.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W116-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working. 

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTak1-AC1" cell_refs="CT-ak-1"><invocation>python .tools/tests/test_round21_check_device.py --device</invocation><expect>ok=True</expect></criterion>
`CTak1-AC1` -- a record written by the check step carries the device and the reader counts it for that device (base: the file does not exist); report the whole last line.

<criterion id="CTak1-AC2" cell_refs="CT-ak-1"><invocation>python org/devices/intake/test_intake_check.py</invocation><expect>ok=True</expect></criterion>
`CTak1-AC2` -- the check suite still passes (base: `INTAKE-CHECK-TEST cases=57/57 skipped=0 ok=True`, a control; the count may grow); report the whole last line.

<criterion id="CTak1-AC3" cell_refs="CT-ak-1"><invocation>python .tools/tests/test_round20_fetch_device.py --device</invocation><expect>ok=True</expect></criterion>
`CTak1-AC3` -- the round-20 fetch-device suite still passes (base: `FETCH-DEVICE arms=8/8 ok=True`, a control); report the whole last line.
</proof_of_spec>

<expected_criteria>CTak1-AC1,CTak1-AC2,CTak1-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 280`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~116/NFRA_CTLPLN.TO-CT-ak-1.intake-check-records-carry-device.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTak1-AC1,CTak1-AC2,CTak1-AC3` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round21.md</decomp_doc>
<owned_cells>CT-ak-1</owned_cells>
</decomp_ref>

<paths>
org/devices/intake/intake_check.py
.tools/tests/test_round21_check_device.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call, no network.
comp-adversary: RUN -- the device derivation differing between the fetch and the check writers (the test compares to the derived name); a schema bump breaking the other intake tools (the three controls); a check step that runs a network call in the test (the fixture wheel is local); BLIND: the check of the real duckdb wheel is the next step of the journey, after the CTO's approval file.
risk: LOCAL -- a local tool and a test in a temporary folder.
lane: the <paths> block IS the grant (worker RULING 1). `org/devices/intake/` is NFRA_CTLPLN's laptop-side intake folder (C-INTAKE); the CTO ordered this fix (round-20 analysis ruling 3).
</preflight>

Base checks, dry-run by the issuer before the cut: CTak1-AC1 FAIL as expected (the file does not exist); CTak1-AC2 base `INTAKE-CHECK-TEST cases=57/57 skipped=0 ok=True` (a control); CTak1-AC3 base `FETCH-DEVICE arms=8/8 ok=True` (a control).
Source: CTO round-20 analysis sections 2-3 (`ledger/ROUND_ANALYSIS.round20.md` @5df0b0af31), msg 109441; FWD-19, FWD-15.
