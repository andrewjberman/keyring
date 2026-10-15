# TO NFRA_CTLPLN.TO-CT-ai-2 -- workstream OUTCOME round 2 (cell CT-ai-2): one box's seat list refreshed, read, and every seat named from the list alone (FWD-23)

<to_id>NFRA_CTLPLN.TO-CT-ai-2</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~107</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>OUTCOME</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-ai-2` (`decompositions/NFRA_CTLPLN_DECOMP.round19.md`) | **outcome_ref:** FWD-23 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

PRD outcome FWD-23 (`prd/NFRA_CTLPLN_PRD.md` line 262): anyone can tell what each operations seat on a box is doing, and no driven work finishes without a reviewer on that box grading it. DONE WHEN: one box's seat list read by someone who then names each seat's work without opening a log, and one finished piece of work shown with its grade. The laptop's list `org/devices/state/laptop/seats.json` is 10449 minutes old (written 2026-10-08), so `python .tools/seat-list.py show` reads `stale=laptop`. The tool is `.tools/seat-list.py` (`write`, `show`).

YOUR WORKTREE WAS CUT BY `.tools/wk-provision.sh` AND IS A SPARSE CHECKOUT: it holds `.tools/`, `lib/`, the project folder `org/missions/D0/NFRA/NFRA_CTLPLN/`, `org/modules/graph/`, `org/devices/`, `infra/logic/registry/`, `org/standards/` and the paths of this order. If a command fails because a file or folder is missing, run `git sparse-checkout add <folder>`, retry, and name the folder, the command and the error in your final report.

### BUILD

1. Refresh the laptop's list: `python .tools/seat-list.py write` (it writes `org/devices/state/laptop/seats.json`), then commit that file.
2. A NEW test `.tools/tests/test_round19_seat_record.py` (standard library). It generates, from the list's own fields only (serial, kind, live, doing, project, drive, orders, commit age, summary; no log is opened), the record `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~107/SEAT_LIST_READ.md`: one row per seat with what it is doing, and a separate line naming each seat whose `DOING` reads IDLE or whose commit age is over 120 minutes (the 'one that is doing nothing'). The same record carries the one finished piece of work with its grade: run `python .tools/round-close-check.py --project NFRA_CTLPLN --round 18` and copy its `ROUND-CLOSE ... reviewer=present` line and two `GRADED (adjudication row ...)` lines verbatim. The test then re-reads the record against the list and prints `SEAT-RECORD seats=<n> named=<k> idle_flagged=<m> round_close_reviewer=<present|absent> ok=<True|False>` (ok = every seat named, reviewer present). Run it in a temporary copy of the list as well, with one seat removed, to show the test fails when a seat is missing (the mutant).

### RULES FOR THIS CELL

Write surface = the `<paths>` plus your own folder `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~107/`. Every experiment runs in a temporary folder or repository unless the cell says otherwise. No push, no deploy, no AWS write. Use `.tools/safe-commit.sh` for every commit, with explicit file paths. Do NOT commit the `portal` gitlink or `org/git-author-override-audit.laptop.log`. ASCII only; Python 3.12; bash is Git Bash 3.6.7 (default utilities only). CLAUDE.md and org/XXX.md are LOCKED. COMMIT A WORK-IN-PROGRESS COMMIT AS SOON AS A FILE EXISTS, and again after each criterion passes. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~105/NFRA_CTLPLN.TO-CT-ah-1.sparse-safe-commit-abs-path-link-batch.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W107-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working. 

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTai2-AC1" cell_refs="CT-ai-2"><invocation>python .tools/seat-list.py show</invocation><expect>stale=none</expect></criterion>
`CTai2-AC1` -- the laptop's seat list is fresh (base: `stale=laptop`); report the whole `SEAT-LIST-SHOW` line.

<criterion id="CTai2-AC2" cell_refs="CT-ai-2"><invocation>python .tools/tests/test_round19_seat_record.py</invocation><expect>ok=True</expect></criterion>
`CTai2-AC2` -- every seat in the list is named in the record from the list alone, and the reviewer line is present (base: the file does not exist); report the whole last line.
</proof_of_spec>

<expected_criteria>CTai2-AC1,CTai2-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 280`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~107/NFRA_CTLPLN.TO-CT-ai-2.seat-list-read-and-recorded.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTai2-AC1,CTai2-AC2` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round19.md</decomp_doc>
<owned_cells>CT-ai-2</owned_cells>
</decomp_ref>

<paths>
org/devices/state/laptop/seats.json
.tools/tests/test_round19_seat_record.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- the seat list refreshed from a stale cache and still reading fresh (check the `written_at` the tool prints); a record typed by hand that drifts from the list (the test derives it); a seat whose summary hides that it is idle; BLIND: the list is the laptop's only; the other boxes' lists are their own managers' writes and this cell does not read them.
risk: LOCAL -- one box-local state file and a test.
lane: the <paths> block IS the grant (worker RULING 1). `org/devices/state/laptop/seats.json` is this box's own state file, written by `.tools/seat-list.py`.
</preflight>

Base checks, dry-run by the issuer before the cut: CTai2-AC1 FAIL as expected (`stale=laptop` at the cut); CTai2-AC2 FAIL as expected (the file does not exist).
Source: CTO round-18 analysis section 3 (`ledger/ROUND_ANALYSIS.round18.md` @721e05298f), msg 109398; FWD-23.
