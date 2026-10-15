# TO NFRA_CTLPLN.TO-CT-am-1 -- workstream OUTCOME round 15 (cell CT-am-1): the package journey repair -- `intake_receive.py` classes a COLOURED ModuleNotFoundError as a missing dependency, so a wheel whose optional module wants a package outside the pack is not refused

<to_id>NFRA_CTLPLN.TO-CT-am-1</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~123</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<status_reason>Closed by the issuer 2.0.0_SA_COO~C after its own re-run in worker tree wk-NFRA_CTLPLN-123 @5b9e08a865 (merged a9e9fa8b00): CTam1-AC1 RECEIVE-COLOR arms=15/15 ok=True; CTam1-AC2 INTAKE-RECEIVE-TEST cases=32/32 ok=True; diff paths inside the order; proof instance VALID in the main tree; row W123-S1 (client-data check NOT checked, hashed list absent on this box) OBSERVATION, INERT. LOCAL until MSTR pushes.</status_reason>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>15</round>
<workstream>OUTCOME</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-am-1` (`decompositions/NFRA_CTLPLN_DECOMP.round23.md`) | **outcome_ref:** FWD-15, FWD-16, FWD-18, FWD-19 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

PRD outcomes FWD-15, 16, 18, 19 (the duckdb journey, `ledger/ROUND_ANALYSIS.round22.md` ruling and enrichment item 1). dell1 received the pack (all 4 SHA-256 equal the laptop's record), `verify` read `wheels=1 verified=1 checked=1 stray=0 ok=True`, `prove` read `INTAKE-PROVE device=dell1 python=3.14.7 wheels=1 installed=1 imported=0 import_missing_dep=0 failed=0 refused=0 ok=True`, and then `install --dry-run` REFUSED: `receipt records an import failure that is not import_missing_dep` (carried by `0.0.0_AB_MSTR` from dell1's CTO, call `XB-20261015T204024Z-7bc4`). Cause as dell1 read it: the environment variable `FORCE_COLOR=3` makes Python 3.14 colour the traceback, so the ImportError for `adbc_driver_duckdb` (an optional module of the duckdb wheel) reads `ModuleNotFoundError` wrapped in ANSI escape codes, and `MISSING_RE` at `org/devices/intake/intake_receive.py` line 54 (`ModuleNotFoundError: No module named '([^']+)'`) misses the module name; the tool then grades the import `failed` instead of `import_missing_dep` (a FINDING, not a fault, per `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~8/INTAKE_RECEIVE_COMMANDS.md`). Read `org/devices/intake/intake_receive.py` whole first (the `prove` verb's child process and where `MISSING_RE` is applied) and `org/devices/intake/test_intake_receive.py` (30 of 30 at the cut).

YOUR WORKTREE WAS CUT BY `.tools/wk-provision.sh` AND IS A SPARSE CHECKOUT: it holds `.tools/`, `lib/`, the project folder `org/missions/D0/NFRA/NFRA_CTLPLN/`, `org/modules/graph/`, `org/devices/`, `infra/logic/registry/`, `org/standards/` and the paths of this order. If a command fails because a file or folder is missing, run `git sparse-checkout add <folder>`, retry, and name the folder, the command and the error in your final report.

### BUILD

1. **Strip colour before matching.** In `org/devices/intake/intake_receive.py`, remove ANSI escape sequences (CSI sequences `ESC[` ... final byte, and the OSC forms if any) from the child's captured error text BEFORE `MISSING_RE` is applied. Keep `MISSING_RE` itself and the grading rule unchanged: only a ModuleNotFoundError whose module is NOT in the pack is `import_missing_dep`; every other import failure stays `failed`.
2. **Run the child plain.** The import child process and the pip child get an environment with `PYTHON_COLORS=0` and `NO_COLOR=1` set and `FORCE_COLOR` removed, so a coloured traceback is not produced in the first place (belt and braces).
3. A NEW test `.tools/tests/test_round23_receive_color.py` (standard library; no network, no real install): arms over the pure classification function the tool uses (extract or call it; read the file): (a) the plain text `ModuleNotFoundError: No module named 'adbc_driver_duckdb'` -> `import_missing_dep` with the module name; (b) the SAME message wrapped in ANSI colour codes exactly as Python 3.14 prints it with `FORCE_COLOR=3` (for example `\x1b[1;35mModuleNotFoundError\x1b[0m: No module named '\x1b[35madbc_driver_duckdb\x1b[0m'`; build two or three real shapes) -> `import_missing_dep`; (c) a coloured `ImportError: cannot import name 'x'` and a coloured `SyntaxError` -> `failed` (a different failure stays a failure); (d) the module named in the message IS one of the pack's own modules -> `failed`; (e) the child environment built for the import has `PYTHON_COLORS=0`, `NO_COLOR=1` and no `FORCE_COLOR`. Last line `RECEIVE-COLOR arms=<k>/<n> ok=<True|False>`.
4. Add two cases (the coloured missing-dependency case and the coloured other-failure case) to `org/devices/intake/test_intake_receive.py` so its own count grows from 30. Do not change the schema, the receipts or any other verb.

### RULES FOR THIS CELL

Write surface = the `<paths>` plus your own folder `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~123/`. Every experiment runs in a temporary folder or repository unless the cell says otherwise. No push, no deploy, no AWS write. Use `.tools/safe-commit.sh` for every commit, with explicit file paths. Do NOT commit the `portal` gitlink or `org/git-author-override-audit.laptop.log`. ASCII only; Python 3.12; bash is Git Bash 3.6.7 (default utilities only). CLAUDE.md and org/XXX.md are LOCKED. COMMIT A WORK-IN-PROGRESS COMMIT AS SOON AS A FILE EXISTS, and again after each criterion passes. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~105/NFRA_CTLPLN.TO-CT-ah-1.sparse-safe-commit-abs-path-link-batch.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W123-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working. 

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTam1-AC1" cell_refs="CT-am-1"><invocation>python .tools/tests/test_round23_receive_color.py</invocation><expect>ok=True</expect></criterion>
`CTam1-AC1` -- a coloured missing-dependency import error is classed `import_missing_dep` and every other failure stays `failed` (base: the test does not exist); report the whole last line with its denominator.

<criterion id="CTam1-AC2" cell_refs="CT-am-1"><invocation>python org/devices/intake/test_intake_receive.py</invocation><expect>ok=True</expect></criterion>
`CTam1-AC2` -- the receiving tool's own suite passes with the two new cases (base: `INTAKE-RECEIVE-TEST cases=30/30 ok=True`; the count must grow); report the whole last line.
</proof_of_spec>

<expected_criteria>CTam1-AC1,CTam1-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 280`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~123/NFRA_CTLPLN.TO-CT-am-1.intake-receive-reads-a-coloured-import-error.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTam1-AC1,CTam1-AC2` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round23.md</decomp_doc>
<owned_cells>CT-am-1</owned_cells>
</decomp_ref>

<paths>
org/devices/intake/intake_receive.py
org/devices/intake/test_intake_receive.py
.tools/tests/test_round23_receive_color.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call, no network, no real install; the test builds strings and an environment mapping.
comp-adversary: RUN -- the strip swallowing real text (the other-failure arms and a module name containing digits, dots or underscores); a coloured ImportError for a module INSIDE the pack read as a missing dependency (arm d); the tool's receipts or `install` gate loosened (it must still refuse a receipt with a real failure: run the existing suite); the strip failing on the legacy console form (`ESC` sequences with `?` private modes); BLIND: the fix reaches dell1 only after dell1 pulls it (the journey's immediate repair on dell1 is to re-run prove and install with `PYTHON_COLORS=0`, asked of dell1's CTO in parallel); Python 3.12 on the laptop cannot prove the cp314 wheel, so no real prove of the duckdb wheel is run here.
risk: LOCAL -- one local receiving tool and its tests, with strings and an environment mapping as the only inputs; no wheel is installed.
lane: the <paths> block IS the grant (worker RULING 1). `org/devices/intake/` is NFRA_CTLPLN's intake route (C-INTAKE); the CTO ruled the journey (round-22 analysis enrichment item 1) and dell1's CTO asked for this repair.
</preflight>

Base checks, dry-run by the issuer before the cut: CTam1-AC1 FAIL as expected (the test does not exist); CTam1-AC2 base `INTAKE-RECEIVE-TEST cases=30/30 ok=True` (a control; the count must grow).
Source: CTO round-22 analysis sections 2-3 (`ledger/ROUND_ANALYSIS.round22.md` @1d8ee95b78); FWD-15, FWD-16, FWD-18, FWD-19.
