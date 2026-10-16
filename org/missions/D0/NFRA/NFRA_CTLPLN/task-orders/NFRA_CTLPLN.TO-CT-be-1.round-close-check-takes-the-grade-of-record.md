# TO NFRA_CTLPLN.TO-CT-be-1.round-close-check-takes-the-grade-of-record -- workstream OUTCOME round 28 (cell CT-be-1): round-close-check.py grades a criterion from the grade of record (the last CVO row), not the first CVO row that names it (site Z call XB-20261016T121809Z-95c2)

<to_id>NFRA_CTLPLN.TO-CT-be-1.round-close-check-takes-the-grade-of-record</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~143</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<status_reason>Closed by the issuer 2.0.0_SA_COO~C after its own re-run in the worker tree (wk-NFRA_CTLPLN-143 @c1000e1948) and again in the main tree after merge 9a570bb671: CTbe1-AC1 GRADE-OF-RECORD arms=8/8 ok=True (the test was red at the base, 4/8); CTbe1-AC2 ROUND-CLOSE-SELFTEST cases=30/30 ok=True (the base printed the same); proof VALID; neighbouring suites green in the main tree: ROUND-CLOSE-DECOMP-ROUND 6/6, CLOSE-GATES-TEST 24/24, SEAT-RECORD 6 of 6. The change: grade_criterion collects every CVO-kind non-doer row that grades the criterion and returns the one with the latest surfaced_at (undated rows sort first, ties go to the later file and row, self-grades never compete); the real project's close line reads the same before and after. Real row shape the worker found: surfaced_at is minute-precision with a Z, adjudicates names surprise ids (never a grade row id), and no adjudication file carries a supersedes key, so that branch is inert on today's rows. W143-S1 (OBSERVATION, INERT): a grade of record of NOT MET reads GRADED and counts in graded=; whether a NOT MET grade should refuse the close is the CVO's rule, unchanged here. W143-S2: the sparse list lacked org/tier0. Not run: the site Z case itself (NFRA_OPLGTW round 37; its files are outside the worker's sparse tree): the planted pair reproduces its shape. The announcement to the four boxes goes through 0.0.0_AB_MSTR. LOCAL until MSTR pushes.</status_reason>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>28</round>
<workstream>OUTCOME</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-be-1` (`decompositions/NFRA_CTLPLN_DECOMP.round29.md`) | **outcome_ref:** NFRA_CTLPLN C-ROUNDCLOSE (an inbound cross-box call; no FWD) |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`.tools/round-close-check.py` (892 lines; this project's cell CT-af-2 built it) decides whether a round may close by reading each task order's JUDGMENT criteria and the CVO's grade rows. A cross-box call from site Z (`XB-20261016T121809Z-95c2`; body `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/1.0.0_SA_CTO~Z/XB_CALL_ROUND_CLOSE_CHECK_FIRST_ROW_TO_COO_C_20261016.md`, readable with `git show origin/box/sitez:<that path>`; read it whole) reports: `grade_criterion` (about lines 520-560) RETURNS on the FIRST CVO-kind row that grades a criterion, so a later regrade is never read: for `NFRA_OPLGTW` round 37, `TO-OG-ap-14 AC3` reads as the v29 row `Z-C-S76` (NOT MET) while the grade of record is v32's `Z-C-S79` (MET), which supersedes it. The CVO never edits old rows (the history is kept), so any regrade reads wrong.

THE FIX the caller asks for, which is yours to implement: `grade_criterion` takes the GRADE OF RECORD: among the CVO-kind rows that grade the criterion (after the same strict/verdict tests as today), the row with the LATEST `surfaced_at` (a row without a parseable `surfaced_at` sorts before every row that has one; ties keep file order and the later file/row wins), or, where a row carries an `adjudicates` or `supersedes` key naming another row id, the row no later row names. If the schema carries no such key, `surfaced_at` order alone is the rule. A row by the order's own doer (a self-grade) never becomes the grade of record: only CVO-kind non-doers compete, and a self-grade still reads SELF only when NO CVO-kind non-doer row exists, exactly as at the base.

Read first: `.tools/round-close-check.py` whole (especially `grade_criterion`, `structured_grade`, `verdict_after`, `author_of`, `kind_of`, the callers that turn GRADED rows into a MET / NOT MET reading, and the `--selftest`), and the two row shapes in `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/adjudications/` (look at two adjudication files for the `surfaced_at` and any `adjudicates` or `supersedes` keys the real rows carry; quote what the real rows carry in your report).

YOUR WORKTREE WAS CUT BY `.tools/wk-provision.sh` AND IS A SPARSE CHECKOUT: it holds `.tools/`, `lib/`, the project folder `org/missions/D0/NFRA/NFRA_CTLPLN/`, `org/modules/graph/`, `org/devices/`, `infra/logic/registry/`, `org/standards/` and the paths of this order. If a command fails because a file or folder is missing, run `git sparse-checkout add <folder>`, retry, and name the folder, the command and the error in your final report. A tool that reads the repository and finds a folder missing may print a SHORT result with exit 0 (row W137-S1): read the denominator a tool prints, and add the folder before you trust a zero.

### BUILD

1. **The rule, in `grade_criterion`** as above: collect every qualifying CVO-kind non-doer row across both sources (adjudication rows and investigation rows) with its `surfaced_at`, and return the grade of record; keep the return shape `("GRADED", "<source> row <id> by <who>[ (verdict <v>)]")` unchanged so every caller keeps working. The detail string names the row of record.
2. **Where the verdict is read.** The call says the check "credits NOT MET": find where a GRADED row's verdict becomes MET or NOT MET (`verdict_after` / `structured_grade`), and make sure that reading is of the row of record, not of the first row. If the caller reads the verdict from a different place than `grade_criterion`, fix that place too and say so.
3. **The test**, a NEW file `.tools/tests/test_round29_grade_of_record.py` (standard library plus the tool; temporary project trees only; no network; ASCII output): arms (a) a planted pair on one criterion, an older NOT MET CVO row then a newer MET CVO row: reads MET; (b) the reversed order (older MET, newer NOT MET): reads NOT MET; (c) three rows, the middle one newest: the newest wins regardless of file order; (d) a newer row by a doer (self-grade) does NOT supersede an older CVO row; (e) a CVO row for a different order's `AC3` never competes (the existing generic-id rule holds); (f) no CVO row at all: UNGRADED as before; (g) a row without `surfaced_at` loses to one with it; (h) the real project: `python .tools/round-close-check.py --project NFRA_CTLPLN --round 29` still reads its present `verdict=MAY-CLOSE` line (the five orders of this round are all open at the cut, so read the line as it is and report it unchanged from the base, whatever it is). Last line `GRADE-OF-RECORD arms=<k>/<n> ok=<True|False>`.
4. The tool's own `--selftest` keeps passing; add cases for the new rule only where cheap.

### RULES FOR THIS CELL

Write surface = the `<paths>` plus your own folder `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~143/`. Every experiment runs in a temporary folder; do not write under the real adjudications folder. NO network request, no `pip`, no install. No push, no deploy, no AWS write, no `terraform` command. Use `.tools/safe-commit.sh` for every commit, with explicit file paths, and read its whole output (do not pipe it through tail or head). Do NOT commit the `portal` gitlink or `org/git-author-override-audit.laptop.log`. ASCII only; Python 3.12; bash is Git Bash 3.6.7 (default utilities only). CLAUDE.md and org/XXX.md are LOCKED. COMMIT A WORK-IN-PROGRESS COMMIT AS SOON AS A FILE EXISTS, and again after each criterion passes. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~134/NFRA_CTLPLN.TO-CT-av-1.intake-signed-waiver-for-a-failed-check.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W143-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working. A WARN from safe-commit that the client-data check had no account-id list is the standing WARN-only state (ruled): quote it in your report, file no row for it. When your own change turns a neighbouring suite red, say so in your report with the suite's whole last line: the issuer re-runs every suite that imports what you changed at the merge.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTbe1-AC1" cell_refs="CT-be-1"><invocation>python .tools/tests/test_round29_grade_of_record.py</invocation><expect>ok=True</expect></criterion>
`CTbe1-AC1` -- a newer CVO row supersedes an older one for the same criterion in both directions, a self-grade never supersedes, and a row without a date loses (base: the test does not exist); report the whole last line with its denominator.

<criterion id="CTbe1-AC2" cell_refs="CT-be-1"><invocation>python .tools/round-close-check.py --selftest</invocation><expect>ok=True</expect></criterion>
`CTbe1-AC2` -- the checker's own selftest stays green (run it at the base in your worktree first and report the base's whole last line; the expectation is a green last line ending `ok=True` before and after).
</proof_of_spec>

<expected_criteria>CTbe1-AC1,CTbe1-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 280`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~143/NFRA_CTLPLN.TO-CT-be-1.round-close-check-takes-the-grade-of-record.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTbe1-AC1,CTbe1-AC2` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round29.md</decomp_doc>
<owned_cells>CT-be-1</owned_cells>
</decomp_ref>

<paths>
.tools/round-close-check.py
.tools/tests/test_round29_grade_of_record.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no network request; a read-only checker and its test in temporary trees.
comp-adversary: RUN -- a later self-grade or a doer row superseding a CVO grade (arm d); a generic id AC3 crediting another order's grade (arm e); a newer NOT MET hidden by an older MET (arm b); a row with no date winning by file order (arm g); a regression in the shared tool that four boxes carry (the tool's selftest and the project's own read are the controls; the announcement of the merge to the four boxes goes through 0.0.0_AB_MSTR); BLIND: a regrade the CVO files with no `surfaced_at` and no `supersedes` key is ordered by file order only; the cell reports the real rows' shape.
risk: LOCAL -- a read-only checker used at round close and its test in temporary trees; no grade row, order or project row changes.
lane: the <paths> block IS the grant (worker RULING 1). The checker is this project's (cell CT-af-2); the ask is the inbound call XB-20261016T121809Z-95c2 from site Z.
</preflight>

Base checks, dry-run by the issuer before the cut: CTbe1-AC1 FAIL as expected (the test does not exist); CTbe1-AC2 PASS as expected (control: `ROUND-CLOSE-SELFTEST cases=30/30 ok=True`).
Source: inbound cross-box call XB-20261016T121809Z-95c2 (1.0.0_SA_CTO~Z, row NFRA_OPLGTW-Z-S176).
