# TO NFRA_CTLPLN.TO-CT-cb-1.round-close-not-met-count-and-two-small-repairs -- workstream OUTCOME round 30 (cell CT-cb-1): the small batch: not_met=<n> beside graded= on the ROUND-CLOSE line, the crossbox split test's arm (f) compares crossbox/1 files only, and the sweep-before-merge clause in the order protocol (FWD-8; round-close checker)

<to_id>NFRA_CTLPLN.TO-CT-cb-1.round-close-not-met-count-and-two-small-repairs</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~146</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-16</issued_date>
<status>open</status>
<status_reason>Issued by the issuer 2.0.0_SA_COO~C in the round-29 issuance, per the CTO's round-28 analysis (ROUND_ANALYSIS.round28.md @3894648aa3, msg 109677).</status_reason>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>30</round>
<workstream>OUTCOME</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-cb-1` (`decompositions/NFRA_CTLPLN_DECOMP.round29.md`) | **outcome_ref:** FWD-8 (the test), the round-close checker (C-ROUNDCLOSE), the L6 order template |
**depends_on:** none

---

## WORKER FACE

### THE CELL

Three small repairs the CTO ruled in `org/missions/D0/NFRA/NFRA_CTLPLN/ledger/ROUND_ANALYSIS.round29.md` (rulings 4, 5 and 7; read them), batched as one cell (disjoint files):

1. **`not_met=<n>` on the ROUND-CLOSE line** (ruling 5; the CVO's ruling C-S103 stands: a NOT MET grade does not refuse a round close, it feeds the analysis). `python .tools/round-close-check.py --project <CODE> --round <n>` prints a last line `ROUND-CLOSE project=... judgment=<j> graded=<g> ungraded=<u> self_graded=<s> verdict=<v>`. Add `not_met=<n>` immediately after `graded=<g>`: the count, among the criteria that read GRADED, whose grade of record reads NOT MET (the checker already reads the verdict word of the grade of record; use the SAME reading, add no new reading of prose). It changes no verdict. THE LINE HAS CONSUMERS: `.tools/box-sync.sh`, `.tools/safe-merge.sh`, `.tools/seat-gates-dry-pass.py` and the tests `.tools/tests/test_apply_who_and_crossbox.py`, `test_round29_grade_of_record.py`, `test_round19_seat_record.py`, `test_round_close_and_research.py` name `ROUND-CLOSE project=` or `graded=`. READ each: if a consumer matches the line by a regular expression that the new field breaks, make the smallest change to that consumer in your paths; if a consumer is outside your paths and would break, file a BLOCKING row naming it and STOP on that point. Print, in your report, the whole last line of the real run for this project before and after.
2. **Arm (f) of `.tools/tests/test_round29_crossbox_split.py`** (C-S104; ruling 7): the arm compares the base tool (`git show 7d4aef5b93:.tools/crossbox-call.py`) with the new tool over a copy of the real `org/devices/crossbox/` directory, and now reads `files=237 ... differing=3` (`CROSSBOX-SPLIT arms=12/13 ok=False` at the base of this cell) because the real directory holds layout-2 files (`schema crossbox/2`, and answer files `XB-<id>.<box>.json`) that the BASE tool correctly refuses. Make the arm copy ONLY the files whose JSON `schema` is `crossbox/1` (skip every `crossbox/2` file and every `crossbox-answer/1` file), print how many it compared and how many it left out, and change nothing else in the test.
3. **The sweep-before-merge clause** (ruling 4) in `org/ref/TASK_ORDER_PROTOCOL.md` (412 lines; its `## XML Template` section holds the order template): add ONE short clause, placed where the template's rules for the verification criteria are stated (read the file whole to find the right place), headed `SWEEP BEFORE MERGE`: any order that changes a SHARED CHECKER or GATE (a tool whose output other projects' records feed: for example `round-close-check.py`, `placement-check.py`, `naming-gate.py`, `parity-gates.sh`) carries in its worker face the instruction to run the changed tool over EVERY real project's records before and after the change and print the counts, and the issuer re-reads the counts at the merge. Two lines inside the clause, exactly: `COST: one run per such cell.` and `NON-APPLICATION: a checker that no other project's records feed.` Nothing else in the file changes.

YOUR WORKTREE WAS CUT BY `.tools/wk-provision.sh` AND IS A SPARSE CHECKOUT: it holds `.tools/`, `lib/`, the project folder `org/missions/D0/NFRA/NFRA_CTLPLN/`, `org/modules/graph/`, `org/devices/`, `infra/logic/registry/`, `org/standards/` and the paths of this order. If a command fails because a file or folder is missing, run `git sparse-checkout add <folder>`, retry, and name the folder, the command and the error in your final report. A tool that reads the repository and finds a folder missing may print a SHORT result with exit 0 (row W137-S1): read the denominator a tool prints, and add the folder before you trust a zero.

### BUILD

Do the three repairs above. Then:

4. **The test** for repair 1, a NEW file `.tools/tests/test_round30_not_met.py` (standard library plus the tool; temporary project trees only; ASCII output): a planted tree with two judgment criteria, one graded MET and one graded NOT MET by adjudication rows: the line reads `graded=2 not_met=1` and the verdict is unchanged by the NOT MET grade; a tree with none NOT MET reads `not_met=0`; an ungraded criterion counts in neither; the line's field ORDER is `... graded=<g> not_met=<n> ungraded=<u> ...`. Last line `NOT-MET-COUNT arms=<k>/<n> ok=<True|False>`.
5. The neighbouring suites that name the line (the six listed in repair 1, plus `python .tools/round-close-check.py --selftest` and `python .tools/tests/test_round_close_decomp_round.py`) stay green: run each at the base first and report the base and after last lines.

### RULES FOR THIS CELL

Write surface = the `<paths>` plus your own folder `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~146/`. Every experiment runs in a temporary folder; do not write under real adjudication or investigation files. NO network request, no `pip`, no install. No push, no deploy, no AWS write, no `terraform` command. Use `.tools/safe-commit.sh` for every commit, with explicit file paths, and read its whole output (do not pipe it through tail or head). Do NOT commit the `portal` gitlink or `org/git-author-override-audit.laptop.log`. ASCII only; Python 3.12; bash is Git Bash 3.6.7 (default utilities only). CLAUDE.md and org/XXX.md are LOCKED. COMMIT A WORK-IN-PROGRESS COMMIT AS SOON AS A FILE EXISTS, and again after each criterion passes. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~134/NFRA_CTLPLN.TO-CT-av-1.intake-signed-waiver-for-a-failed-check.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W146-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working. A WARN from safe-commit that the client-data check had no account-id list is the standing WARN-only state (ruled): quote it in your report, file no row for it. When your own change turns a neighbouring suite red, say so in your report with the suite's whole last line: the issuer re-runs every suite that imports what you changed at the merge.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTcb1-AC1" cell_refs="CT-cb-1"><invocation>python .tools/tests/test_round30_not_met.py</invocation><expect>ok=True</expect></criterion>
`CTcb1-AC1` -- the ROUND-CLOSE line carries `not_met=<n>` beside `graded=`, counts NOT MET grades of record, changes no verdict and breaks no consumer (base: the test does not exist); report the whole last line with its denominator.

<criterion id="CTcb1-AC2" cell_refs="CT-cb-1"><invocation>python .tools/tests/test_round29_crossbox_split.py</invocation><expect>CROSSBOX-SPLIT arms=13/13 ok=True</expect></criterion>
`CTcb1-AC2` -- arm (f) compares only `crossbox/1` files and the whole test is green again (base: `CROSSBOX-SPLIT arms=12/13 ok=False`); report the whole last line and the arm's compared and left-out counts.

<criterion id="CTcb1-AC3" cell_refs="CT-cb-1"><invocation>grep -c "SWEEP BEFORE MERGE" org/ref/TASK_ORDER_PROTOCOL.md</invocation><expect>1</expect></criterion>
`CTcb1-AC3` -- the order protocol carries the clause exactly once (base: 0).
</proof_of_spec>

<expected_criteria>CTcb1-AC1,CTcb1-AC2,CTcb1-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 280` (AC2 builds temporary repositories and can take about two minutes). Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~146/NFRA_CTLPLN.TO-CT-cb-1.round-close-not-met-count-and-two-small-repairs.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTcb1-AC1,CTcb1-AC2,CTcb1-AC3` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round30.md</decomp_doc>
<owned_cells>CT-cb-1</owned_cells>
</decomp_ref>

<paths>
.tools/round-close-check.py
.tools/tests/test_round30_not_met.py
.tools/tests/test_round29_crossbox_split.py
.tools/tests/test_apply_who_and_crossbox.py
.tools/tests/test_round29_grade_of_record.py
.tools/tests/test_round19_seat_record.py
.tools/tests/test_round_close_and_research.py
.tools/box-sync.sh
.tools/safe-merge.sh
.tools/seat-gates-dry-pass.py
org/ref/TASK_ORDER_PROTOCOL.md
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no network request; a read-only checker, a test, a doc clause.
comp-adversary: RUN -- the new field breaking a consumer of the line (box-sync.sh, safe-merge.sh and seat-gates-dry-pass.py are read and each regex is checked; a consumer outside the grant that would break is a BLOCKING stop); a NOT MET count changing a verdict (arm: the verdict is unchanged); the count reading prose differently (it uses the checker's existing reading of the grade of record); arm (f) now hiding a real divergence (it still compares every crossbox/1 file and prints how many it left out); the clause editing the protocol beyond one clause (the diff is read); BLIND: a consumer of the line outside `.tools/` (a skill or a seat habit) reading `graded=` by hand: the field is appended after `graded=`, not substituted.
risk: LOCAL -- a read-only checker, tests, and one doc clause; no grade row, order or project row changes. `.tools/box-sync.sh` and `.tools/safe-merge.sh` are read; they are edited only if the new field breaks them (a shared script carried by four boxes: say so in the report).
lane: the <paths> block IS the grant (worker RULING 1). The CTO ruled the three repairs (round-29 analysis rulings 4, 5, 7, msg 109721).
</preflight>

Base checks, dry-run by the issuer before the cut: CTcb1-AC1 FAIL as expected (the test does not exist); CTcb1-AC2 FAIL as expected (`CROSSBOX-SPLIT arms=12/13 ok=False` at HEAD); CTcb1-AC3 FAIL as expected (`grep -c` reads 0).
Source: CTO round-29 analysis rulings 4, 5 and 7; the CVO's rulings C-S103 and C-S104.
