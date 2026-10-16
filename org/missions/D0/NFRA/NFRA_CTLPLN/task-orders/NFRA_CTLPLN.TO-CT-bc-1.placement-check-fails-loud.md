# TO NFRA_CTLPLN.TO-CT-bc-1.placement-check-fails-loud -- workstream OUTCOME round 27 (cell CT-bc-1): placement-check.py stops saying nothing when it cannot read: a missing org/missions or a short project count exits non-zero with ERROR (FWD-7)

<to_id>NFRA_CTLPLN.TO-CT-bc-1.placement-check-fails-loud</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~141</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<status_reason>Closed by the issuer 2.0.0_SA_COO~C after its own re-run in the worker tree (wk-NFRA_CTLPLN-141 @eaf87f8810) and again in the main tree after merge 430e2d1615: CTbc1-AC1 PLACEMENT-LOUD arms=7/7 ok=True; CTbc1-AC2 placement-check --self-test: 7/7 PASS; proof VALID; the real tool on the healthy main tree reads rc=0 with `register rows with a tree home: 30 | live projects read: 30 | match=True` and `FINDINGS: 0 unplaced/unreadable, 64 cross-box write overlap(s)` (the same as the base); test_open_calls 19/19 (it imports read_projects, unchanged). A mutant with the short-count check disabled reads 6/7 (arm b fails). One deviation from the order's wording, accepted: the expected set is the register rows' own `home` field under org/missions united with any tree home under ROOT (30 of 73 non-terminal rows), because an in-ROOT-only definition shrinks in a sparse tree and would have read 1 of 1 in the very case the row W137-S1 reported; recorded as W141-S1. W141-S2 (the worker cut lacked org/projects and infra/aws/lambda/ci: sparse-set note for later cuts of this class), W141-S3 (test_round19_register.py --fwd7 rewrites a tracked CT-ai-1 deliverable on each run; the worker restored it): OBSERVATION, INERT. LOCAL until MSTR pushes.</status_reason>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>27</round>
<workstream>OUTCOME</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-bc-1` (`decompositions/NFRA_CTLPLN_DECOMP.round29.md`) | **outcome_ref:** FWD-7 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`python .tools/placement-check.py` is the FWD-7 placement read. In a sparse worktree that lacked `org/missions` it printed `placement-check | live projects: 1 ...` and `FINDINGS: ... 0 cross-box write overlap(s)` with exit 0 (row `NFRA_CTLPLN-W137-S1`): a zero without its denominator read as an answer. The CTO ruled (`org/missions/D0/NFRA/NFRA_CTLPLN/ledger/ROUND_ANALYSIS.round28.md`, ruling 3; read it): the tool exits non-zero and prints `ERROR:` when `org/missions` is absent, or when it reads fewer live projects than the register lists; a zero without its denominator is never an rc-0 answer again.

Read first: `.tools/placement-check.py` (177 lines; `read_projects` line ~70, `main` line ~125, `self_test` line ~151). Its header says findings never change the exit code (the monitor moratorium): that stays true of FINDINGS (an overlap, an UNPLACED project). Only an INPUT the tool cannot read, or reads short, is an error here, and it is not a finding.

YOUR WORKTREE WAS CUT BY `.tools/wk-provision.sh` AND IS A SPARSE CHECKOUT: it holds `.tools/`, `lib/`, the project folder `org/missions/D0/NFRA/NFRA_CTLPLN/`, `org/modules/graph/`, `org/devices/`, `infra/logic/registry/`, `org/standards/` and the paths of this order. If a command fails because a file or folder is missing, run `git sparse-checkout add <folder>`, retry, and name the folder, the command and the error in your final report. A tool that reads the repository and finds a folder missing may print a SHORT result with exit 0 (row W137-S1): read the denominator a tool prints, and add the folder before you trust a zero.

### BUILD

1. **Missing tree.** Before reading projects, if `org/missions` does not exist under ROOT, print `ERROR: placement-check cannot read org/missions (not found under <ROOT>); the read has no projects to place` to standard output (and to standard error), print nothing that looks like a result, and return exit code 3. Do the same for `--json` (one JSON document `{"error": "<same text>", "live_projects": null}`, exit 3).
2. **Short count.** The register of projects is `org/projects/*.json` (one row per project; read a row's `status`, `project_code`, and whether the project has a tree home `org/missions/D*/<MACRO>/<CODE>/project.json` in ROOT). Measure at the base what the healthy main tree reads: the number of non-terminal register rows that carry a tree home, against the number of live projects `read_projects` returns (the base reads `live projects: 30`). DEFINE the expectation so that the healthy main tree passes with rc 0 AND an `org/missions` holding fewer live project.json files than the register's non-terminal rows-with-a-tree-home exit 3 with `ERROR: placement-check read <n> live project(s) but the register lists <m> with a tree home` naming both numbers and the first three codes it did not read. If `org/projects` itself is absent, that is also exit 3 (`ERROR: ... cannot read org/projects`): the tool cannot prove it read everything. State your definition and the two measured numbers on the main tree in your report.
3. **The denominator line stays** as `placement-check | live projects: <n> | ...` (unchanged text), and a new line `placement-check | register rows with a tree home: <m> | live projects read: <n> | match=True` is printed before the boxes (so a reader sees the comparison on every successful run).
4. **Findings keep exit 0.** An overlap, an UNPLACED project and an UNREADABLE project.json (one file) stay findings with exit 0, exactly as at the base.
5. **The test**, a NEW file `.tools/tests/test_round29_placement_loud.py` (standard library plus the tool; synthetic trees in temporary folders: copy `.tools/placement-check.py` and `lib/devices.py` into `<tmp>/.tools/` and `<tmp>/lib/`, plus the smallest `org/devices/DEVICES.json`, `org/projects/*.json` and `org/missions/D0/X/<CODE>/project.json` files the tool needs, so ROOT resolves to the temporary tree; read `lib/devices.py` and `self_test` for what the register needs; no network; ASCII output) with arms: (a) no `org/missions` -> exit 3 and a line starting `ERROR:`; (b) `org/missions` holds one project.json but the register lists two with a tree home -> exit 3 and the message names `1` and `2`; (c) a healthy synthetic tree -> exit 0, no `ERROR:`, the `match=True` line; (d) a healthy tree with a planted cross-box overlap -> exit 0 and the overlap printed (findings never change the exit); (e) `--json` with no `org/missions` -> exit 3 and a JSON document with an `error` key; (f) no `org/projects` -> exit 3; (g) one unreadable project.json (invalid JSON) -> exit 0 and an UNREADABLE finding (not an ERROR). Last line `PLACEMENT-LOUD arms=<k>/<n> ok=<True|False>`.
6. The tool's own `--self-test` (7 cases at the base) keeps passing; add its cases for the new rules only if cheap, else leave it unchanged.

### RULES FOR THIS CELL

Write surface = the `<paths>` plus your own folder `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~141/`. NO network request, no `pip`, no install. No push, no deploy, no AWS write, no `terraform` command. Use `.tools/safe-commit.sh` for every commit, with explicit file paths, and read its whole output (do not pipe it through tail or head). Do NOT commit the `portal` gitlink or `org/git-author-override-audit.laptop.log`. ASCII only; Python 3.12; bash is Git Bash 3.6.7 (default utilities only). CLAUDE.md and org/XXX.md are LOCKED. COMMIT A WORK-IN-PROGRESS COMMIT AS SOON AS A FILE EXISTS, and again after each criterion passes. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~134/NFRA_CTLPLN.TO-CT-av-1.intake-signed-waiver-for-a-failed-check.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W141-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working. A WARN from safe-commit that the client-data check had no account-id list is the standing WARN-only state (ruled): quote it in your report, file no row for it. When your own change turns a neighbouring suite red, say so in your report with the suite's whole last line: the issuer re-runs every suite that imports what you changed at the merge.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTbc1-AC1" cell_refs="CT-bc-1"><invocation>python .tools/tests/test_round29_placement_loud.py</invocation><expect>ok=True</expect></criterion>
`CTbc1-AC1` -- a missing `org/missions` or `org/projects` and a short project count each exit 3 with an ERROR line, while findings keep exit 0 (base: the test does not exist); report the whole last line with its denominator.

<criterion id="CTbc1-AC2" cell_refs="CT-bc-1"><invocation>python .tools/placement-check.py --self-test</invocation><expect>placement-check --self-test: 7/7 PASS</expect></criterion>
`CTbc1-AC2` -- the tool's own planted cases still pass (base: `placement-check --self-test: 7/7 PASS`, a control); report the whole last line.
</proof_of_spec>

<expected_criteria>CTbc1-AC1,CTbc1-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 280`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~141/NFRA_CTLPLN.TO-CT-bc-1.placement-check-fails-loud.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTbc1-AC1,CTbc1-AC2` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round29.md</decomp_doc>
<owned_cells>CT-bc-1</owned_cells>
</decomp_ref>

<paths>
.tools/placement-check.py
.tools/tests/test_round29_placement_loud.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no network request; a read-only tool and synthetic trees in temporary folders.
comp-adversary: RUN -- the new error firing on the healthy main tree (arm c and the real-tree read in the report: rc 0 with `match=True`); an overlap or an unplaced project becoming an error (arm d keeps exit 0; the moratorium on monitors is untouched: this is an input-integrity exit code of a viewer, not a monitor or an alert); the count definition drifting (the report states the definition and both measured numbers); BLIND: a project that has a register row but no tree home is not counted by design, so a project whose tree was deleted is read as absent from both sides.
risk: LOCAL -- one read-only tool and its test against synthetic trees; no register, project row or lease changes.
lane: the <paths> block IS the grant (worker RULING 1); the CTO ruled the behaviour (round-28 analysis ruling 3, msg 109677).
</preflight>

Base checks, dry-run by the issuer before the cut: CTbc1-AC1 FAIL as expected (the test file does not exist); CTbc1-AC2 PASS as expected (control: `placement-check --self-test: 7/7 PASS`).
Source: CTO round-28 analysis ruling 3 and enrichment item 3; row `NFRA_CTLPLN-W137-S1`; FWD-7.
