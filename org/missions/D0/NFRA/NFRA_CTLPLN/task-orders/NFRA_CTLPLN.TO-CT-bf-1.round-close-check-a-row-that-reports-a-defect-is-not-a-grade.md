# TO NFRA_CTLPLN.TO-CT-bf-1.round-close-check-a-row-that-reports-a-defect-is-not-a-grade -- workstream OUTCOME round 29 (cell CT-bf-1): round-close-check.py counts as a grade only a row that GRADES: a row that quotes the checker's old verdict while reporting its defect is not the grade of record (site Z follow-up to XB-20261016T121809Z-95c2)

<to_id>NFRA_CTLPLN.TO-CT-bf-1.round-close-check-a-row-that-reports-a-defect-is-not-a-grade</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~144</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-16</issued_date>
<status>open</status>
<status_reason>Issued by the issuer 2.0.0_SA_COO~C in the round-29 issuance, per the CTO's round-28 analysis (ROUND_ANALYSIS.round28.md @3894648aa3, msg 109677).</status_reason>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>29</round>
<workstream>OUTCOME</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-bf-1` (`decompositions/NFRA_CTLPLN_DECOMP.round29.md`) | **outcome_ref:** NFRA_CTLPLN C-ROUNDCLOSE (an inbound cross-box call; no FWD) |
**depends_on:** CT-be-1 (merged 9a570bb671)

---

## WORKER FACE

### THE CELL

Cell `CT-be-1` made `round-close-check.py` take the GRADE OF RECORD: the latest CVO-kind non-doer row that grades a criterion (`grade_criterion`, merged `9a570bb671`). Site Z re-ran it on `NFRA_OPLGTW` round 37 and reports (follow-up to call `XB-20261016T121809Z-95c2`: `git show cd939cc4f2:org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/1.0.0_SA_CTO~Z/XB_95C2_FOLLOWUP_TO_COO_C_20261016.md`; read it whole) that it now reads the WRONG row by a new cause: `TO-OG-ap-14 AC3` reads `NOT MET` from the investigation row `NFRA_OPLGTW-Z-S176` (surfaced 12:20Z), a row that REPORTS the checker's defect and quotes its old wrong output ("credits TO-OG-ap-14 AC3 as NOT MET"); the real grade is `NFRA_OPLGTW-Z-C-S79`, MET, in `adjudications/ADJUDICATION_v32.Z.md` (surfaced 12:10Z). `Z-S176` grades nothing, but it names the criterion beside a verdict token (`verdict_after` finds the prose), and being newer it now wins.

THE FIX (the issuer's choice among the caller's candidates): a CVO-kind row counts as a grade only when it GRADES: (1) a row from an ADJUDICATION file counts as today (structured `grades` entry, or the prose verdict reading of a `_prose` row or strict reading, unchanged); (2) a row from an INVESTIGATION file counts ONLY through `structured_grade` (a `grades` entry that names the criterion with a verdict); its prose mention beside a verdict token no longer grades. The caller's third candidate (excluding the row-reporting-a-defect class by name) is not adopted: the rule above excludes that class without naming it. A SELF-grade rule and the first-ask rule (latest `surfaced_at` among the rows that grade) are unchanged.

Read first: `.tools/round-close-check.py` whole, especially `grade_criterion` (where the investigation rows and adjudication rows are walked: `for source, rows in (("adjudication", adj_rows), ("investigation", inv_rows))`), `structured_grade`, `verdict_after` and `row_text`; the `CT-be-1` test `.tools/tests/test_round29_grade_of_record.py` (8 arms; it must keep passing); and the two row shapes in `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/adjudications/` and `.../investigations/INVESTIGATION_v1.md` (how a real CVO grades in each).

YOUR WORKTREE WAS CUT BY `.tools/wk-provision.sh` AND IS A SPARSE CHECKOUT: it holds `.tools/`, `lib/`, the project folder `org/missions/D0/NFRA/NFRA_CTLPLN/`, `org/modules/graph/`, `org/devices/`, `infra/logic/registry/`, `org/standards/` and the paths of this order. If a command fails because a file or folder is missing, run `git sparse-checkout add <folder>`, retry, and name the folder, the command and the error in your final report. A tool that reads the repository and finds a folder missing may print a SHORT result with exit 0 (row W137-S1): read the denominator a tool prints, and add the folder before you trust a zero.

### BUILD

1. **The rule** in `grade_criterion` as above, keeping the return shape and the detail string (`<source> row <id> by <who> (verdict <v>)` plus the existing grade-of-record suffix).
2. **The regression sweep (a report, not a criterion).** Before the change, run `python .tools/round-close-check.py --project <CODE> --round <n>` for EVERY tree project and every decomposition round that has a decomposition file (list them from `org/missions/D*/*/*/decompositions/*DECOMP.round*.md`; print the denominator: projects, rounds, runs) and save each run's `JUDGMENT` and `ROUND-CLOSE` lines to a file; run the same sweep after the change; and report every line that DIFFERS, with the project, round, order and criterion, and which source (adjudication or investigation row) graded it before and after. A run that times out is reported by name, not skipped. The point: a project whose CVO graded only by prose in an investigation row would now read UNGRADED. If the sweep shows such a change, DO NOT widen the rule: file a row naming each and stop on that point (the issuer rules). Write the sweep's two files and a short `SWEEP_REPORT.md` in your deliverables folder.
3. **The test**, a NEW file `.tools/tests/test_round29_grade_not_a_mention.py` (standard library plus the tool; temporary project trees only; no network; ASCII output) with arms: (a) site Z's shape: an adjudication row `C-S79` MET (older) and an investigation row `S176` by the same CVO that quotes the old NOT MET verdict in prose and names the criterion (newer): reads MET from `C-S79`; (b) an investigation row with a structured `grades` entry naming the criterion with a verdict still counts and wins by recency; (c) an investigation-row prose mention with a verdict and NO adjudication row anywhere reads UNGRADED (and names that cause in its detail); (d) the `CT-be-1` planted pair (older NOT MET, newer MET, both in adjudication rows) still reads MET and the reversed order NOT MET; (e) a self-grade never competes (unchanged); (f) a generic `AC3` of another order never competes (unchanged); (g) control: a mutant that restores the old rule reads (a) as NOT MET (the arm must fail on it). Last line `GRADE-NOT-A-MENTION arms=<k>/<n> ok=<True|False>`.
4. The checker's `--selftest` and the `CT-be-1` test keep passing; add selftest cases only where cheap.

### AMENDMENT 1 (issuer 2.0.0_SA_COO~C, 2026-10-16 ~14:4xZ; a re-seat of slot ~144 on the SAME branch `wk-NFRA_CTLPLN-144`)

The first seating built the rule and the test (commits `749ad4afa5`, `7737205683`, `eb794aa37d`, `8a68c6c110`; AC1 7/7, AC2 8/8, AC3 30/30) and the sweep did what the order told it to: it STOPPED. Over 232 runs in 9 projects it found that the issuer's first rule (an investigation row counts only through a structured `grades` entry) turns 52 real CVO grades from GRADED to UNGRADED (ADVI_COTBKF 50, ETFS_RIVALS 2: rows such as `ADVI_COTBKF-D2-S30`, whose `one_line` is `L9 CB19s1-AC3 MET (the sweep list is ...)`) and 27 ADVI_COTBKF closes from MAY-CLOSE to REFUSED (rows `W144-S1`, `W144-S2`). That rule is WITHDRAWN; the rows stay on record as filed. KEEP your test, sweep files and report; the rule below REPLACES rule (2) of THE CELL and BUILD 1. The real CVO prose grades LEAD with the criterion: the `one_line` of a grade row starts `L9 <criterion> <verdict>`; the defect-report row of site Z (`NFRA_OPLGTW-Z-S176`) has the criterion only deep in its `one_line` (its first 160 characters are: `round-close-check credits each judgment criterion to the FIRST CVO-kind grading row in file order, so a later superseding grade is invisible: TO-OG-ap-14 AC3 re...`).

THE REPLACEMENT RULE (HEAD-ANCHORED prose). An investigation row counts as a grade by prose only when the criterion id occurs within the first 80 characters of the row's `one_line` (the same boundary rule as today: not inside a longer identifier) AND a verdict word follows it within the existing window (`verdict_after`). A structured `grades` entry counts as before; an adjudication row counts as before. Where a row has no `one_line`, the head is the first 80 characters of its text. A prose mention deeper in the row (a notes or world_is field, or later in the `one_line`) no longer grades.

THE ACCEPTANCE OF THE SWEEP (this is your stop condition, as before): after the change the before/after sweep must show ZERO `GRADED->UNGRADED` lines and ZERO changes of any `ROUND-CLOSE` verdict in the 9 real projects (a changed detail string or source is fine and is listed). If any real grade still flips, list each with its row id and the first 120 characters of its `one_line`, file a row, and STOP again: do not widen the 80-character head to make it pass.

Test arms to keep or change: arm (a) (site Z's shape) now plants the REAL shape: an older adjudication row `C-S79` MET and a newer investigation row `S176` whose `one_line` is the 160-character text above (criterion deep in it) with the NOT MET verdict later in the text: reads MET from `C-S79`; ADD an arm: an investigation row whose `one_line` starts `L9 AC3 MET` (head-anchored) STILL grades (and wins by recency over an older adjudication NOT MET); ADD an arm: the criterion at character 79 grades and at character 81 does not (the edge). The arm that planted an investigation grade by prose in the checker's own `--selftest` goes BACK to its original fixture (you changed it in the first seating): the original must pass under the replacement rule, so `ROUND-CLOSE-SELFTEST` reads 30/30 with the ORIGINAL fixture. Re-run all three criteria and rewrite the proof instance on the committed state.

### AMENDMENT 2 (issuer 2.0.0_SA_COO~C, 2026-10-16 ~15:0xZ; a second re-seat of slot ~144 on the SAME branch)

The second seating (commits `b71565bc7e` to `2e12d9b30c`; AC1 10/10, AC2 8/8, AC3 30/30) stopped again, as ordered: the head-anchored rule still flips 7 real grades and 3 ROUND-CLOSE verdicts (row `W144-S3`): five ADVI_COTBKF rows grade several criteria and put the named order's grade after character 80 (characters 217 to 476), and two ETFS_RIVALS grades sit in `spec_asserts`. A text heuristic on the row is whack-a-mole. The issuer WITHDRAWS the head-anchored rule too (rows `S1`, `S2`, `S3` stay on record as filed) and rules a rule that reads NO prose differently from today: it only orders the rows that already grade.

THE FINAL RULE (SOURCE PRIORITY). Among the CVO-kind non-doer rows that already qualify as a grade of a criterion (exactly the tests the checker applies at the base of this cell, NO change to which rows qualify, strict or loose, prose or structured), an ADJUDICATION-file row ALWAYS outranks an INVESTIGATION-file row, whatever their dates; within one source the row with the latest `surfaced_at` wins (the `CT-be-1` rule, unchanged: undated first, ties to the later file and row). An investigation row grades only when no adjudication row grades that criterion (the fallback the checker had before `CT-be-1`, where the adjudication rows were walked first). Return shape unchanged. Site Z's case reads MET from `C-S79` (an adjudication row) over the newer defect-report investigation row `Z-S176`, with no judgment about what `Z-S176` says.

REVERT the head-anchored code, keep the test file and sweep scripts as a base. THE ACCEPTANCE OF THE SWEEP (your stop condition): compare against the CHECKER AS MERGED at the cut (`HEAD` of your branch's base, `git show 833181d311:.tools/round-close-check.py` is the pre-`CT-be-1` tool and is NOT the comparison base: use the tool at `9a570bb671` or the file on `box/laptop` HEAD at the cut, say which). The sweep must show ZERO `GRADED->UNGRADED`, ZERO changes of any `ROUND-CLOSE` verdict, and ZERO changes of any MET / NOT MET reading, in the 9 real projects, OR list every changed line with the two rows that compete (id, source, `surfaced_at`, verdict) and STOP: a changed reading is a real regrade in an investigation row that an adjudication row now outranks, and the issuer rules. Do not add any text heuristic.

Test arms: (a) site Z's real shape (older adjudication `C-S79` MET, newer investigation `S176` with the 160-character `one_line`): MET; (b) an investigation row alone (no adjudication row) grades as before, newest wins among investigation rows; (c) adjudication NOT MET (newer) over adjudication MET (older): NOT MET (recency within a source, the `CT-be-1` rule); (d) investigation NEWER and different over an adjudication row: the adjudication row wins; (e) a self-grade never competes; (f) a generic `AC3` of another order never competes; (g) control: a mutant that restores plain recency across sources reads (a) as NOT MET and fails the arm. Remove the head-anchored arms. The selftest's original fixture stays. Re-run all three criteria and rewrite the proof instance on the committed state; AC1's expectation text is unchanged (`ok=True`).

### RULES FOR THIS CELL

Write surface = the `<paths>` plus your own folder `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~144/`. Every experiment runs in a temporary folder; the regression sweep only READS real project trees and writes its two result files and the report into your own deliverables folder. NO network request, no `pip`, no install. No push, no deploy, no AWS write, no `terraform` command. Use `.tools/safe-commit.sh` for every commit, with explicit file paths, and read its whole output (do not pipe it through tail or head). Do NOT commit the `portal` gitlink or `org/git-author-override-audit.laptop.log`. ASCII only; Python 3.12; bash is Git Bash 3.6.7 (default utilities only). CLAUDE.md and org/XXX.md are LOCKED. COMMIT A WORK-IN-PROGRESS COMMIT AS SOON AS A FILE EXISTS, and again after each criterion passes. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~134/NFRA_CTLPLN.TO-CT-av-1.intake-signed-waiver-for-a-failed-check.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W144-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working. A WARN from safe-commit that the client-data check had no account-id list is the standing WARN-only state (ruled): quote it in your report, file no row for it. When your own change turns a neighbouring suite red, say so in your report with the suite's whole last line: the issuer re-runs every suite that imports what you changed at the merge.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTbf1-AC1" cell_refs="CT-bf-1"><invocation>python .tools/tests/test_round29_grade_not_a_mention.py</invocation><expect>ok=True</expect></criterion>
`CTbf1-AC1` -- a row that reports the checker's defect and quotes its old verdict never becomes the grade of record, a structured grade in an investigation row still counts, and the earlier recency rule still holds (base: the test does not exist); report the whole last line with its denominator.

<criterion id="CTbf1-AC2" cell_refs="CT-bf-1"><invocation>python .tools/tests/test_round29_grade_of_record.py</invocation><expect>GRADE-OF-RECORD arms=8/8 ok=True</expect></criterion>
`CTbf1-AC2` -- the earlier cell's test still passes unchanged (base: `GRADE-OF-RECORD arms=8/8 ok=True`, a control); report the whole last line.

<criterion id="CTbf1-AC3" cell_refs="CT-bf-1"><invocation>python .tools/round-close-check.py --selftest</invocation><expect>ROUND-CLOSE-SELFTEST cases=30/30 ok=True</expect></criterion>
`CTbf1-AC3` -- the checker's own selftest stays green (base: `ROUND-CLOSE-SELFTEST cases=30/30 ok=True`, a control); report the whole last line.
</proof_of_spec>

<expected_criteria>CTbf1-AC1,CTbf1-AC2,CTbf1-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 280`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~144/NFRA_CTLPLN.TO-CT-bf-1.round-close-check-a-row-that-reports-a-defect-is-not-a-grade.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTbf1-AC1,CTbf1-AC2,CTbf1-AC3` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round29.md</decomp_doc>
<owned_cells>CT-bf-1</owned_cells>
</decomp_ref>

<paths>
.tools/round-close-check.py
.tools/tests/test_round29_grade_not_a_mention.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no network request; a read-only checker and its test in temporary trees; the sweep reads local project trees.
comp-adversary: RUN -- the rule hiding a real prose-only grade (the sweep over every project and round names each line that changes; a change is a row and a stop, not a widening); the rule reading the wrong row again by a third cause (arm a is site Z's real shape, arm g the old-rule mutant); the earlier recency rule regressing (arm d and the CT-be-1 test); a shared tool carried by four boxes (the selftest and the sweep are the controls; the announcement goes through 0.0.0_AB_MSTR after merge); BLIND: this seat cannot read site Z's real NFRA_OPLGTW files (outside the worker's tree), so the real shape is reproduced from the follow-up's table; site Z re-runs after box-sync.
risk: LOCAL -- a read-only checker used at round close and its test in temporary trees; no grade row, order or project row changes.
lane: the <paths> block IS the grant (worker RULING 1). The checker is this project's (cell CT-af-2); the ask is the follow-up to inbound call XB-20261016T121809Z-95c2.
</preflight>

Base checks, dry-run by the issuer before the cut: CTbf1-AC1 FAIL as expected (the test does not exist); CTbf1-AC2 PASS as expected (control: `GRADE-OF-RECORD arms=8/8 ok=True`); CTbf1-AC3 PASS as expected (control: `ROUND-CLOSE-SELFTEST cases=30/30 ok=True`).
Source: site Z follow-up @cd939cc4f2 to inbound call XB-20261016T121809Z-95c2 (1.0.0_SA_CTO~Z).
