# TO NFRA_CTLPLN.TO-CT-ak-2 -- workstream BATCH round 8 (cell CT-ak-2): ONE hygiene batch -- rebuild the stale comp-pulse danger map and make its test SKIP on a stale map (S9127), then classify the four census values (W114-S1)

<to_id>NFRA_CTLPLN.TO-CT-ak-2</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~117</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>8</round>
<workstream>BATCH</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-ak-2` (`decompositions/NFRA_CTLPLN_DECOMP.round21.md`) | **outcome_ref:** hygiene |
**depends_on:** none

---

## WORKER FACE

### THE CELL

Two items, ONE cell. Read rows `NFRA_CTLPLN-S9127` and `NFRA_CTLPLN-W114-S1` first (Grep each id in `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md`), and the remediation row S9127 in `surprise-channel/remediations/REMEDIATION_v10.md`. At the cut: `bash .tools/comp-pulse diff .tools/wk-provision.sh` prints `NOT-DECIDABLE: danger map STALE -- the reflex CANNOT clear this diff`; the map `org/modules/graph/nerves-risk-edges.json` was written 2026-10-07 05:36Z by the `nerves_lexical` build (`org/modules/graph/nerves_lexical.py`), past comp-pulse's staleness limit, so the commit-time risk reflex is blind on every laptop commit; `python .tools/tests/test_round20_hygiene.py --map` reads `HYGIENE-MAP tsx_classed=0 py_classed=0 ok=False`; `python .tools/tests/fabric_value_census.py` reads `unclassified=4 ok=False`.

YOUR WORKTREE WAS CUT BY `.tools/wk-provision.sh` AND IS A SPARSE CHECKOUT: it holds `.tools/`, `lib/`, the project folder `org/missions/D0/NFRA/NFRA_CTLPLN/`, `org/modules/graph/`, `org/devices/`, `infra/logic/registry/`, `org/standards/` and the paths of this order. If a command fails because a file or folder is missing, run `git sparse-checkout add <folder>`, retry, and name the folder, the command and the error in your final report.

### BUILD

1. **Rebuild the map.** Find how `nerves-risk-edges.json` is produced (read `org/modules/graph/nerves_lexical.py` and `comp_pulse.py` for the build command and the staleness limit; Grep for the command in `.tools/` and the scheduled-task registry files, read only), run the build ONCE in your worktree so the regenerated `org/modules/graph/nerves-risk-edges.json` is committed, and report the command, its runtime and the map's new written-at time. If the build needs a network call, AWS or more than 10 minutes, STOP and file a BLOCKING row. Say in a row why the producer stopped running if the files show it (a schedule that no longer exists, a path that moved); do not install a schedule (standing moratorium on monitors).
2. **Make the test state the precondition.** In `.tools/tests/test_round20_hygiene.py` (round-20 file, edit it), when `comp-pulse diff` reports `danger map STALE`, the `--map` arm prints `HYGIENE-MAP SKIP map STALE age=<h>h` and exits 0 (a stale map is a precondition not met, not a defect of the map edit); with a fresh map it classes a mapped portal `.tsx` and a `.py` as before (`ok=True`). Add an arm `--stale` that points the test at a copy of the map with an old written-at to prove the SKIP prints.
3. **`W114-S1`.** `.tools/tests/fabric_value_census.py` cannot classify 4 values (3 of them in files outside your paths). Add entries for them to the census's own classification table (read it; classify each by what the site is: enum source, comparison, display, fixture, with a reason in the table), without editing the files they sit in, so the census reads `unclassified=0 ok=True`. If a value is truly a box-list literal that FWD-2 forbids, do NOT hide it in the table: STOP on that one and file a BLOCKING row naming the file and line.

### RULES FOR THIS CELL

Write surface = the `<paths>` plus your own folder `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~117/`. Every experiment runs in a temporary folder or repository unless the cell says otherwise. No push, no deploy, no AWS write. Use `.tools/safe-commit.sh` for every commit, with explicit file paths. Do NOT commit the `portal` gitlink or `org/git-author-override-audit.laptop.log`. ASCII only; Python 3.12; bash is Git Bash 3.6.7 (default utilities only). CLAUDE.md and org/XXX.md are LOCKED. COMMIT A WORK-IN-PROGRESS COMMIT AS SOON AS A FILE EXISTS, and again after each criterion passes. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~105/NFRA_CTLPLN.TO-CT-ah-1.sparse-safe-commit-abs-path-link-batch.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W117-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working. 

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTak2-AC1" cell_refs="CT-ak-2"><invocation>python .tools/tests/test_round20_hygiene.py --map</invocation><expect>ok=True</expect></criterion>
`CTak2-AC1` -- with the rebuilt map a staged portal `.tsx` and a `.py` are classed (base: `HYGIENE-MAP tsx_classed=0 py_classed=0 ok=False`); report the whole last line.

<criterion id="CTak2-AC2" cell_refs="CT-ak-2"><invocation>python .tools/tests/test_round20_hygiene.py --stale</invocation><expect>SKIP</expect></criterion>
`CTak2-AC2` -- the test prints a SKIP naming the map's age when the map is stale, and does not fail (base: the arm does not exist); report the whole last line.

<criterion id="CTak2-AC3" cell_refs="CT-ak-2"><invocation>python .tools/tests/fabric_value_census.py</invocation><expect>unclassified=0</expect></criterion>
`CTak2-AC3` -- the census classifies every value it finds (base: `unclassified=4 ok=False`); report the whole last line.
</proof_of_spec>

<expected_criteria>CTak2-AC1,CTak2-AC2,CTak2-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 280`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~117/NFRA_CTLPLN.TO-CT-ak-2.hygiene-danger-map-rebuild-and-census-classes.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTak2-AC1,CTak2-AC2,CTak2-AC3` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round21.md</decomp_doc>
<owned_cells>CT-ak-2</owned_cells>
</decomp_ref>

<paths>
org/modules/graph/nerves-risk-edges.json
.tools/tests/test_round20_hygiene.py
.tools/tests/fabric_value_census.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call; the map build is a local read of the repository.
comp-adversary: RUN -- the rebuilt map classing more than the build's own rule (do not hand-edit it; commit the generator's output as it came); a map build that takes the wrong repository root (run it from the worktree root and check the written-at and the file count); the SKIP arm hiding a map that is stale for good (the test prints the age so a reader sees it); the census table hiding a real hard-coded box list (the BLOCKING instruction); the map is generated data shared with the risk reflex on every commit, so a bad map blinds or blocks every commit: run `bash .tools/comp-pulse diff` on two real staged files (one `.py`, one `.tsx`) after the rebuild and report both outputs; BLIND: the map's owner is `1.0.0_SA_CTO` (git history) and the CTO ruled the cell rebuilds it.
risk: LOCAL -- a generated data file and two test files; no infra path.
lane: the <paths> block IS the grant (worker RULING 1). `org/modules/graph/nerves-risk-edges.json` is a generated file of the graph module; the CTO ruled the rebuild into this cell (round-20 analysis ruling 5). The census file is a test helper.
</preflight>

Base checks, dry-run by the issuer before the cut: CTak2-AC1 FAIL as expected (`ok=False`); CTak2-AC2 FAIL as expected (the arm does not exist); CTak2-AC3 FAIL as expected (`unclassified=4`).
Source: CTO round-20 analysis sections 2-3 (`ledger/ROUND_ANALYSIS.round20.md` @5df0b0af31), msg 109441; hygiene.
