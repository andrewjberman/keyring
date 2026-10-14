# TO NFRA_CTLPLN.TO-CT-ad-2 -- workstream COMMITPATH round 1 (cell CT-ad-2): `safe-commit.sh` hands the naming gate the FULL staged path set for committing-project DERIVATION only, grading stays on the same eight extensions (row NFRA_MCPINDEX-Z-W34-S8, CTO ruling 1)

<to_id>NFRA_CTLPLN.TO-CT-ad-2</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~93</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>COMMITPATH</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-ad-2` (`decompositions/NFRA_CTLPLN_DECOMP.round14.md`) | **outcome_ref:** FWD-2 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`.tools/safe-commit.sh` sits on EVERY seat's commit path. Its naming-gate stage (about :1052-1110, "THE NAMING LIMB") collects only the staged files with extension `.py .js .mjs .ts .tf .json .yaml .yml` into `NGATE_FILES` (about :1088-1092) and hands the diff of exactly those to `.tools/naming-gate.py --diff ... --post-from-index`. `naming-gate.py` derives the COMMITTING PROJECT from the staged paths (`committing_project(files)` about :1992, home pattern `PROJECT_HOME_RE = org/missions/D*/<MACRO>/<CODE>/`, one code or None), and the project's legacy-address rows apply only when one is derived. A commit whose graded files sit outside a project home, with the project's `.md`, `.txt` or `.sh` deliverable staged beside them, therefore derives NO project and is graded without the project's rows. Read the row `NFRA_MCPINDEX-Z-W34-S8` first (Grep `"id": "NFRA_MCPINDEX-Z-W34-S8"` in `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`), then the CTO ruling it received: pass the FULL staged path set to the gate for DERIVATION only, and grade the same eight extensions as today.

### BUILD

1. In `.tools/safe-commit.sh`, write the full staged path list (every path in `IN_SCOPE`, with its old name for a rename if the script already carries one, whatever the extension) to a temporary file and pass it to `naming-gate.py` as a new option (name it `--staged-paths <file>`). The diff handed to the gate stays the diff of the eight extensions only. The temporary file is removed on every exit path the script already cleans (follow how `NGATE_DIFF` is removed).
2. In `.tools/naming-gate.py`, accept `--staged-paths <file>` and use its paths, plus the diff's own paths, as the input of `committing_project(...)` and for NOTHING else. Grading, the files graded, the verdicts and the exit codes are unchanged. Without the option the behaviour is byte-identical to today. An unreadable or empty `--staged-paths` file falls back to today's derivation with one `NOTE:` line on stderr; it never refuses a commit by itself.
3. A NEW test `.tools/tests/test_safe_commit_derivation.py` (standard library; temporary git repositories and temporary directories only; no network; it must NOT commit in the real repository) with these NEGATIVE CONTROLS as well as the positive one: (a) POSITIVE: a graded `.json` file outside any project home plus a `.md` under `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/` staged together derive `NFRA_MCPINDEX`; (b) a `.md` or `.txt` under a project home is still NEVER graded (it is not in the graded set, and a naming literal planted in it produces no verdict); (c) staged paths under TWO project homes still derive None; (d) a path under a FOREIGN project home that is not staged derives nothing (the derivation reads staged paths only); (e) with no `--staged-paths` the gate's output on an identical diff is byte-identical to the base copy (`git show HEAD:.tools/naming-gate.py`, run from a temporary directory); (f) an empty and an unreadable `--staged-paths` file fall back to today's result and exit code. Final line `SAFE-COMMIT-DERIVATION cases=<k>/<n> ok=<True|False>`.

### RULES FOR THIS CELL

Write surface = the `<paths>`. This is the commit path every seat uses: change nothing outside the two tools and the test, keep the stage fail-open exactly as it is today in WARN mode (the stage never changes the script's exit code in WARN mode, and in ENFORCE mode stays fail-closed). Test the shell change by running the script's stage against a TEMPORARY repository only, never the real index. No aws, no network, no push. Commit your own work with `.tools/safe-commit.sh` and explicit file paths (the unchanged real script commits your change; if it is the changed script that you doubt, commit with the base copy of the script from your worktree's `git show HEAD:.tools/safe-commit.sh` in a temporary file). Do NOT commit the `portal` gitlink. ASCII only; Python 3.11; Git Bash 3.6.7 default utilities only. CLAUDE.md and org/XXX.md are LOCKED. The `<status>` flip is the issuer's: do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W93-S<k>`, `surfaced_at` = `date -u +%FT%TZ`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTad2-AC1" cell_refs="CT-ad-2"><invocation>python .tools/tests/test_safe_commit_derivation.py</invocation><expect>ok=True</expect></criterion>
`CTad2-AC1` -- the positive case and all five negative controls pass (base: the file does not exist); report the whole last line with its denominator.

<criterion id="CTad2-AC2" cell_refs="CT-ad-2"><invocation>python .tools/naming-gate.py --self-test</invocation><expect>NAMING-GATE-SELF-TEST: PASS</expect></criterion>
`CTad2-AC2` -- the gate's own self-test still passes (base: `NAMING-GATE-SELF-TEST: PASS`, a control); report the whole last line.
</proof_of_spec>

<expected_criteria>CTad2-AC1,CTad2-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 300`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~93/NFRA_CTLPLN.TO-CT-ad-2.safe-commit-derives-the-project-from-every-staged-path.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTad2-AC1,CTad2-AC2` on the COMMITTED state. Also run once and report the last line of: `bash .tools/safe-commit.sh --help` (it must still print usage and exit as it did at the base) and `python .tools/tests/test_apply_who_and_crossbox.py`.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round14.md</decomp_doc>
<owned_cells>CT-ad-2</owned_cells>
</decomp_ref>

<paths>
.tools/safe-commit.sh
.tools/naming-gate.py
.tools/tests/test_safe_commit_derivation.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- a `.md` deliverable graded because it now reaches the gate (case b); a foreign project's home deriving a project it did not stage (case d); two projects staged and one wrongly derived (case c); the no-option path drifting from today (case e); a commit refused by the new option's own failure (case f); BLIND: a seat whose staged set holds a path with a space or a non-ASCII byte that the path file mangles (the worker adds a space-in-path arm if the script's own list already handles one, and says so if it does not).
lane: the <paths> block IS the grant (worker RULING 1). `.tools/safe-commit.sh` is on every seat's commit path; the CTO ruled the shape (round-13 analysis section 3 ruling 1) and asked for negative controls, which are criteria CTad2-AC1's cases b-f.
</preflight>

Base checks, dry-run by the issuer before the cut: CTad2-AC1 base: FAIL as expected (the file does not exist); CTad2-AC2 base: PASS as expected (`NAMING-GATE-SELF-TEST: PASS`).
Source: row NFRA_MCPINDEX-Z-W34-S8 (routed by 1.0.0_SA_CTO~Z via 0.0.0_AB_MSTR msg 109072); CTO ruling `ledger/ROUND_ANALYSIS.round13.md` @7d271cb57b section 3 ruling 1, YES to the stated shape.
