# TO NFRA_TRNSPT.TO-TR-tt23 -- read_refused in the pull's totals and dry line; test_eod_voice.py collects

<to_id>NFRA_TRNSPT.TO-TR-tt23</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~1</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>23</round>
<workstream>totals</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `TR-tt-23` (`decompositions/NFRA_TRNSPT_DECOMP_R23.md`) | **outcome_ref:** FWD-2 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`TR-tt-23` (CTO round-23 analysis, item 4). Two small repairs in the transcripts scripts.

**A. The pull's totals do not show refused reads.** `data/transcripts/scripts/teams/pull.py` counts a refused content read per series as
`read_refused`, but `totals(rec)` (about line 240) returns only `listed`, `new`, `held`, `expired`, `refused`, and the CLI's `PULL-DRY`
line (about line 331) prints only those. The Lambda handler returns `pull.totals(rec)` as `totals`, so a run with refused reads looks
the same as a run with none.

1. `totals(rec)` returns a sixth key, `read_refused`, the sum of each series' `read_refused`. Key order: `listed`, `new`, `held`,
   `expired`, `read_refused`, `refused`. No other key changes meaning.
2. The `PULL-DRY` line prints `read_refused=<n>` between `expired=` and `refused=`. Nothing else on the line changes.
3. The tests that pin the totals are edited in this same cell: `data/transcripts/scripts/tests/test_teams_pull.py` (the two full-dict
   equalities, about lines 55 and 92) and `data/transcripts/scripts/tests/test_pull_handler.py` (about line 39) gain
   `"read_refused": 0` in the expected dict. If a test pins the `PULL-DRY` line's text, update it the same way.
4. In `data/transcripts/scripts/tests/test_pull_read_refused.py` add two tests:
   - `test_totals_carry_read_refused`: a run whose first series has two refused reads gives `pull.totals(rec)["read_refused"] == 2`.
   - `test_dry_line_prints_read_refused`: the CLI's dry line for a fixture run contains `read_refused=`.

**B. One test file does not collect.** `data/transcripts/scripts/tests/test_eod_voice.py` line 12 reads
`from test_teams_chat_tenant import a, t`: a bare import of a sibling test module, which fails when pytest runs from the repo root
(`ModuleNotFoundError`). Make the import resolve from the repo root the way the other test files in that folder import their siblings
(a package-qualified import, `data.transcripts.scripts.tests.test_teams_chat_tenant`). Change only the import. The file must collect and
its tests pass.

### ACCEPTANCE

<criterion id="TR23-tt23-AC1" cell_refs="TR-tt-23"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R23_CHECKS/r23_checks.py tt23</invocation><expect>R23-TT23-OK</expect></criterion>
`TR23-tt23-AC1` -- the two named tests exist and the five test files (the four pull files and `test_eod_voice.py`) pass together.

<expected_criteria>TR23-tt23-AC1</expected_criteria>

Dry-run at the base: `R23-TT23-FAIL missing test_totals_carry_read_refused, test_dry_line_prints_read_refused` -- FAIL as expected.

## BOUNDS

- **Grant.** The paths below, this order's file, your deliverables folder.
- **LOCAL.** No AWS or HTTP call, no deploy, no Terraform, no other module. The Lambda handler file is NOT edited (it already returns
  `pull.totals(rec)`). ASCII only. No transcript text.
- Run ONLY the acceptance check and the five named test files. Do NOT run the whole tests directory: another test there rewrites a
  tracked fixture. If `git status` shows a path outside your grant modified, restore it with `git checkout -- <path>` before committing.
- If part B cannot be done by changing the import alone, file a surprise row (`NFRA_TRNSPT-D2-W1-S<k>`, next unused across every document
  under `surprise-channel/`) naming why, finish part A, and say so in the report.

<paths>
data/transcripts/scripts/teams/pull.py
data/transcripts/scripts/tests/test_teams_pull.py
data/transcripts/scripts/tests/test_pull_handler.py
data/transcripts/scripts/tests/test_pull_read_refused.py
data/transcripts/scripts/tests/test_eod_voice.py
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP_R23.md</decomp_doc> (round 23), cell `TR-tt-23`.
<owned_cells>TR-tt-23</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR23-tt23-AC1. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~1/NFRA_TRNSPT.TO-TR-tt23.totals-carry-read-refused.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR23-tt23-AC1` BEFORE the flip. Commit first, then pin.
</proof_of_spec>

**REPORT:** the lines changed in `pull.py`, each test file touched and why, the two new test names with pass or fail, how the
`test_eod_voice.py` import was fixed, the check line, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a repo build; the deploy of this change rides a later apply of the pull under its own pair.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call.
comp-adversary: RUN -- sources: the CTO round-23 analysis @b8a07a7e17 item 4, round 22's worker report (the totals were left unchanged because the pinning tests were outside that order's grant). Traps: a consumer that reads the totals dict by exact equality (the two pinning tests are in the grant; the handler passes the dict through); the dry line parsed by a regex elsewhere (the worker reports any test that pins its text). BLIND: readers of the function's returned totals outside this repo.
lane: the paths block.
</preflight>

Source: CTO_ROUND_ANALYSIS_NFRA_TRNSPT_ROUND_23_20261011.md section 4 item 4; decomposition round 23, cell TR-tt-23.
