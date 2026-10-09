# TO NFRA_GATSCP.TO-GS-e-5 -- round 2 GS-e-5: the commit that changes a project's tree row regenerates its index entry in the same commit

<to_id>NFRA_GATSCP.TO-GS-e-5</to_id>
<project>NFRA_GATSCP</project>
<issued_to>0.9.0_WK_NFRA_GATSCP~6</issued_to>
<issued_by>2.0.0_SA_COO~N1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>~N1</workstream>

**Directive:** D0 | **Fabric:** dell1 | **Decomp cell:** `GS-e-5` (`decompositions/NFRA_GATSCP_DECOMP.round2.md`) | **outcome_ref:** FWD-4 |
**depends_on:** none

---

## WORKER FACE

### CONTEXT

Every tree project has a row `org/missions/D<n>/<MACRO>/<CODE>/project.json` and a GENERATED index entry `org/projects/<CODE>.json`.
Today a seat that changes the row (e.g. its `dep_stage`) must remember to run `python .tools/missions-tree-index.py derive --write`
and stage the entry too; otherwise the tree check refuses the commit (INDEX-DRIFT). The rule this project serves (P2): the commit
that changes a generated file's source regenerates it in the same commit, so nobody has to remember. If the entry cannot be
made, the commit is refused with the reason.

Facts at the base:
- `missions-tree-index.py`: `Estate.compose_index(self, t) -> dict` (:383) composes one project's entry. `t` needs `D`, `M`,
  `code` and `row`, and the method uses only contract fields. The `Estate` constructor (:93-125) reads the contract and resolves
  the value enums. `derive --write` (:399-431) is whole-estate: a `check()` and `scan_tree()` first, then a write when the
  existing entry differs on `compared + [idx_marker, "generated_from"]`. `derive` reads the working tree only; `--staged`
  applies to `check` only (:1145-1147). `materialise_index(repo, dest, env=None)` (:483) is round 1's staged reader for `check`.
- `.tools/safe-commit.sh` stages the act into a PRIVATE index (two-phase: `export GIT_DIR="$_SC2P_DIR"` at :448, so a plain
  `git add` stages there; legacy path: `git commit --only -- PATHSPEC` re-reads the working tree). `cg_stage_pathspec` (:705)
  stages; the merge re-check ends at :754; `IN_SCOPE="$(git diff --cached --name-only -- "${PATHSPEC[@]}")"` is :757, and the
  later gates read IN_SCOPE / IN_SCOPE_SET / PATHSPEC. The land step (:488) carries only PATHSPEC. Precedent for a path the
  act adds to itself: the naming-log block (:1109-1118), `git add -f -- "$NP_LOG"` then `PATHSPEC+=("$NP_LOG")`.

### THE CELL

`GS-e-5`. `derive --staged --only CODE --stdout` composes one entry from the staged row; safe-commit regenerates and stages it inside
the act, or refuses with the reason.

**Build:**
1. `missions-tree-index.py derive --staged --only CODE --stdout`: reads that project's `project.json`, the contract and the value
   enums from the index git resolves (`GIT_INDEX_FILE`, `GIT_DIR`), composes the entry with `compose_index` exactly as
   `derive --write` would write it, and prints that JSON (the file's exact content) to stdout. rc 1 with a one-line reason on
   stderr when the row cannot be composed (absent, unparsable, a field off its enum, R1/R4 identity). It writes no file. A
   one-project read only: do not materialise the whole estate for it. Plain `derive` and `derive --write` are unchanged.
2. `safe-commit.sh`, after the merge re-check (:754) and before `IN_SCOPE` (:757): for each staged path matching
   `org/missions/D<n>/<MACRO>/<CODE>/project.json`, run (1), write its stdout to `org/projects/<CODE>.json` in the working tree,
   `git add` it, and append it to PATHSPEC unless already there. On rc 1: print
   `safe-commit: REFUSED -- org/projects/<CODE>.json could not be regenerated from the staged row: <reason>` and exit 1 having
   committed nothing. When nothing in the act is a tree row, do nothing.

### ACCEPTANCE

<criterion id="GE5-AC1" cell_refs="GS-e-5"><invocation>python "org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/round2_prep/checks/r2_derive_one.py"</invocation><expect>GS-E5-DERIVE ok=True</expect></criterion>
`GE5-AC1` -- the unchanged staged row composes exactly the committed entry; a staged dep_stage change is carried (the difference);
a row off its enum is refused with rc 1; the working-tree entry is untouched.

<criterion id="GE5-AC2" cell_refs="GS-e-5"><invocation>python "org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/round2_prep/checks/r2_safecommit_regen.py"</invocation><expect>GS-E5-SAFECOMMIT ok=True</expect></criterion>
`GE5-AC2` -- safe-commit calls it before IN_SCOPE, appends the entry to PATHSPEC and carries the refusal message. (Structural: the
issuer's real ROUND_CLOSE commit of this round is the seam's exercise.)

<expected_criteria>GE5-AC1,GE5-AC2</expected_criteria>

Read both checks before you build. Each prints its arms and ONE last line. Both FAIL at the base. You do not edit the checks. Run
`python .tools/missions-tree-index.py --self-test` once after your change and report its last line (every arm must still pass).

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- No edit outside the grant. Do not run `derive --write`. Do not commit any project.json or org/projects entry: your lane cannot,
  and the regeneration is proven by the issuer's real commit.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `NFRA_GATSCP-D1-W6-S<k>`, `surfaced_at` = `date -u +%FT%H:%MZ` at filing) in the investigation file, and do not weaken the check
  or the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not
  block.

<paths>
.tools/missions-tree-index.py
.tools/safe-commit.sh
org/missions/D0/NFRA/NFRA_GATSCP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside it, in particular the check files under
`org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/`.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_GATSCP/decompositions/NFRA_GATSCP_DECOMP.round2.md</decomp_doc> (round 2), cell `GS-e-5`.
<owned_cells>GS-e-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: GE5-AC1, GE5-AC2. Instance at
`org/missions/D0/NFRA/NFRA_GATSCP/deliverables/0.9.0_WK_NFRA_GATSCP~6/NFRA_GATSCP.TO-GS-e-5.proof_of_spec.json` with `to_id`
`NFRA_GATSCP.TO-GS-e-5`, validated with `python .tools/proof-of-spec-check.py <instance> GE5-AC1,GE5-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** both last lines whole; the self-test's last line; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule.
comp-iam: DECLARED-NOT-APPLICABLE no IAM is read, granted or changed by this cell.
comp-adversary: RUN -- AC1 carries the difference (a staged change is carried) and the refusal (an unmakeable entry refuses); the worktree arm guards a derive that writes the shared tree. BLIND: AC2 is structural; the seam is the issuer's real ROUND_CLOSE commit.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round1.md @5c65160327 item 5; PRD C-REGEN; decomposition round 2. Base dry-run (box/dell1 7611122124): GE5-AC1
FAIL as expected (unrecognized arguments); GE5-AC2 FAIL as expected (no call).
