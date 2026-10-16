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
