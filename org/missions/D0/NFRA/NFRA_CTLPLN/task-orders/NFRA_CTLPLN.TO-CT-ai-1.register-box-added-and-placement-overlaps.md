# TO NFRA_CTLPLN.TO-CT-ai-1 -- workstream OUTCOME round 1 (cell CT-ai-1): two read-backs of the device register -- a box added once is known to every tool (FWD-2), and every placement overlap classed (FWD-7)

<to_id>NFRA_CTLPLN.TO-CT-ai-1</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~106</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>OUTCOME</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-ai-1` (`decompositions/NFRA_CTLPLN_DECOMP.round19.md`) | **outcome_ref:** FWD-2, FWD-7 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

Two exercises of the box register `org/devices/DEVICES.json`, ONE cell. PRD outcomes: FWD-2 (`prd/NFRA_CTLPLN_PRD.md` line 41: a box added once, in one place, every tool knows its name and role; DONE WHEN a box added that way and a seat started on it) and FWD-7 (line 87: anyone can see which box runs each project; none split across boxes; two on different boxes change different files). What exists: `FABRIC_ENUM` in `.tools/to-pipeline-gate.py` is ALREADY derived from the register (`.tools/tests/test_box_lists_from_register.py` reads `ok=True`), and `.tools/placement-check.py` already prints the placement of every live project, 4 boxes, 29 projects, and 57 `OVERLAP` lines at the cut. What is missing is (a) a box ADDED through the register and read by every box-listing tool, and (b) a class for each of the 57 overlaps.

YOUR WORKTREE WAS CUT BY `.tools/wk-provision.sh` AND IS A SPARSE CHECKOUT: it holds `.tools/`, `lib/`, the project folder `org/missions/D0/NFRA/NFRA_CTLPLN/`, `org/modules/graph/`, `org/devices/`, `infra/logic/registry/`, `org/standards/` and the paths of this order. If a command fails because a file or folder is missing, run `git sparse-checkout add <folder>`, retry, and name the folder, the command and the error in your final report.

### BUILD

1. **FWD-2.** A NEW test `.tools/tests/test_round19_register.py` (standard library; no AWS, no network) with the flag `--fwd2`. Copy the register to a temporary folder and add ONE fixture box named `fixbox` (copy a Dell entry's shape: role, lane cap, tailnet fields). For each tool that reads the box list -- `lib/devices.py` (`names()`), the gate's `FABRIC_ENUM`, `.tools/placement-check.py`, `.tools/crossbox-matrix.py`, `.tools/seat-list.py`, and any tool `.tools/tests/test_box_lists_from_register.py` or `.tools/tests/fabric_value_census.py` names -- point it at the temporary register (read each tool to find how: a `--root`, an environment variable, a function argument) and require its output or value to name `fixbox`. A tool that cannot be pointed at a register copy is LISTED by name with the reason, counted as not-reached (not failed), and gets a row. The real register is never written. Last line: `FWD2-BOX-ADDED tools=<reached>/<listed> not_reached=<n> named=<k> ok=<True|False>` (ok = every reached tool names `fixbox`).
2. **FWD-7.** The same test with the flag `--fwd7`: run `python .tools/placement-check.py`, parse every `OVERLAP` line, and class each as SHARED (the overlapping path is one with a declared single writer or merge rule: under `org/critical_paths/.open_deploys`, under `infra/aws/lambda/ci/`, or another path for which you cite the file that states the rule), SPLIT (two projects on different boxes both write a project-owned file, for example the `portal/src/api/endpoints/investor-reporting.ts` pair of DSGN_IRPTV1 and AMGT_RESAPP) or UNCLASSIFIED. Write one table to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~106/FWD7_OVERLAP_CLASSES.md` (every overlap, its class, the rule that classes it, and the denominator). Do not change `placement-check.py`. Last line: `FWD7-OVERLAPS total=<n> shared=<a> split=<b> unclassified=<u> ok=<True|False>` (ok = unclassified 0).

### RULES FOR THIS CELL

Write surface = the `<paths>` plus your own folder `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~106/`. Every experiment runs in a temporary folder or repository unless the cell says otherwise. No push, no deploy, no AWS write. Use `.tools/safe-commit.sh` for every commit, with explicit file paths. Do NOT commit the `portal` gitlink or `org/git-author-override-audit.laptop.log`. ASCII only; Python 3.12; bash is Git Bash 3.6.7 (default utilities only). CLAUDE.md and org/XXX.md are LOCKED. COMMIT A WORK-IN-PROGRESS COMMIT AS SOON AS A FILE EXISTS, and again after each criterion passes. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~105/NFRA_CTLPLN.TO-CT-ah-1.sparse-safe-commit-abs-path-link-batch.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W106-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working. 

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTai1-AC1" cell_refs="CT-ai-1"><invocation>python .tools/tests/test_round19_register.py --fwd2</invocation><expect>ok=True</expect></criterion>
`CTai1-AC1` -- a fixture box added to a copy of the register is named by every reached tool (base: the file does not exist); report the whole last line with its denominator and the not-reached tools.

<criterion id="CTai1-AC2" cell_refs="CT-ai-1"><invocation>python .tools/tests/test_round19_register.py --fwd7</invocation><expect>unclassified=0</expect></criterion>
`CTai1-AC2` -- every overlap of the placement read is classed (base: the file does not exist); report the whole last line.

<criterion id="CTai1-AC3" cell_refs="CT-ai-1"><invocation>python .tools/tests/test_box_lists_from_register.py</invocation><expect>ok=True</expect></criterion>
`CTai1-AC3` -- the register-derived box lists still read ok after your work (base: `BOX-LISTS-FROM-REGISTER gate=derived status_report=derived ok=True`, a control); report the whole last line.
</proof_of_spec>

<expected_criteria>CTai1-AC1,CTai1-AC2,CTai1-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 280`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~106/NFRA_CTLPLN.TO-CT-ai-1.register-box-added-and-placement-overlaps.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTai1-AC1,CTai1-AC2,CTai1-AC3` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round19.md</decomp_doc>
<owned_cells>CT-ai-1</owned_cells>
</decomp_ref>

<paths>
.tools/tests/test_round19_register.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- the real register written by the test (a temporary copy only, asserted); a tool pointed at the real register by mistake and reading `fixbox` as absent; an overlap classed SHARED because its path merely looks shared (cite the rule file); BLIND: a tool that lists boxes in a form this cell does not look for (a regex over scripts), which `fabric_value_census.py` covers; the worker reports which tools it could not reach.
risk: LOCAL -- temporary files and read-only tools.
lane: the <paths> block IS the grant (worker RULING 1). Only a new test file is written, so no lane is touched.
</preflight>

Base checks, dry-run by the issuer before the cut: CTai1-AC1 and CTai1-AC2 FAIL as expected (the test file does not exist); CTai1-AC3 base `BOX-LISTS-FROM-REGISTER gate=derived status_report=derived ok=True` (a control).
Source: CTO round-18 analysis section 3 (`ledger/ROUND_ANALYSIS.round18.md` @721e05298f), msg 109398; FWD-2, FWD-7.
