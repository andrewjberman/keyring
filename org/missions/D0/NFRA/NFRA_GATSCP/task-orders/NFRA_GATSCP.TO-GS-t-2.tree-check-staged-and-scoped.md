# TO NFRA_GATSCP.TO-GS-t-2 -- round 1 GS-t-2: the project-tree check reads the staged bytes and refuses only a violation in a project the act touches

<to_id>NFRA_GATSCP.TO-GS-t-2</to_id>
<project>NFRA_GATSCP</project>
<issued_to>0.9.0_WK_NFRA_GATSCP~2</issued_to>
<issued_by>2.0.0_SA_COO~N1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>~N1</workstream>

**Directive:** D0 | **Fabric:** dell1 | **Decomp cell:** `GS-t-2` (`decompositions/NFRA_GATSCP_DECOMP.md`) | **outcome_ref:** FWD-1 |
**depends_on:** none

---

## WORKER FACE

### CONTEXT

Every commit that stages a path under `org/missions/D<n>/` or `org/projects/<CODE>.json` runs the hook
`.tools/git-hooks/missions-tree-check.sh`, which runs `python .tools/missions-tree-index.py check` over EVERY project (350+
rows) and refuses on any violation anywhere. Two defects: (a) one project's drift refuses every seat's tree commit on the box;
(b) `check` reads the WORKING TREE, so a file staged differently from its working copy is graded as the working copy has it, and
another seat's unsaved edit is graded inside your commit. This cell makes the check read the staged bytes and refuse only a
violation in a project the act touches, printing every other violation as STANDING with its project. It does not change any
rule (R1-R6, ROW-*, INDEX-*).

Facts at the base (read them before you build):
- `missions-tree-index.py`: CLI (:813-828) `mode` = `check` (default) | `derive`; flags `--write`, `--json`, `--self-test`, and
  path overrides `--contract --root --projects --directives --macros` (defaults from `__file__`, :46-53). Reads the filesystem
  (flat index :143, tree rows :184, the YAML files, close artifacts) except `_index_only_projects` (:194-237), which reads index
  blobs only for rows absent on disk. A violation is a 3-tuple `(rule_id, path, detail)` (:263, :270; `--json` gives
  `{"id","path","detail"}`, :420); `path` is the tree home `org/missions/<D>/<M>/<CODE>` (`home_of`, :245) or the flat file path
  for INDEX-DRIFT, INDEX-ORPHAN and flat parse errors (:256, :340-345). The project is the home's last segment or the flat
  file's stem. `--self-test` (:592-810) builds scratch estates in a temp dir (~36 checks). Base `check`: 0 violations.
- `missions-tree-check.sh`: `ROOT="${PRECOMP_REPO_ROOT:-$(git rev-parse --show-toplevel)}"`; the staged list is
  `OWNED_PATHS_STAGED_FILES`, else `git diff --cached --name-only --diff-filter=d` (:39-42); trigger regex at :45; the run at :63
  (`python "$TOOL" check`); rc 0 runs `close_gate` then OK, rc 1 BLOCKED, other rc fail-closed (:127-141). Its header (:24-27)
  names the working-tree read as a known hole: update that header to the new truth.
- One approach (yours to choose): with `--staged`, materialise the inputs the check reads from the index into a temporary
  directory (`git ls-files` + `git cat-file --batch`, honouring `GIT_INDEX_FILE` and `GIT_DIR`) and run the existing reader
  there through the existing path overrides. Whatever you build, the working tree must not be read under `--staged`.

### THE CELL

`GS-t-2`. The tree check reads every input from the git index (`check --staged`, honouring `GIT_INDEX_FILE` and `GIT_DIR`) and
takes the act's paths (`--act PATH`, repeatable; `--act-from-env VAR`); a violation in a project the act does not touch prints
`STANDING <CODE>` and does not refuse; `missions-tree-check.sh` passes the staged list and `--staged`.

**Build:**
1. `missions-tree-index.py check --staged`: the contract, the tree rows, the flat index, `org/missions/DIRECTIVES.yaml`,
   `org/missions/MACROS.yaml` and the close artifacts are read from the index git resolves, never the working tree.
2. `--act PATH` (repeatable) and `--act-from-env VAR` (newline-separated paths in that variable). The act's projects are the
   `<CODE>`s of act paths under `org/missions/D<n>/<MACRO>/<CODE>/` and of `org/projects/<CODE>.json`. If an act path is
   `org/missions/DIRECTIVES.yaml`, `org/missions/MACROS.yaml` or `org/standards/PROJECT_TREE.contract.json`, every project is
   in-act. A violation whose project is not in-act prints exactly `STANDING <CODE> <rule_id> <path> <detail>` (one line, column 0)
   and does not count toward the exit code; in-act violations print and refuse exactly as today. Print a denominator line with
   the in-act and STANDING counts. rc 0 when no in-act violation remains, 1 otherwise. Without `--act`: unchanged.
3. `missions-tree-check.sh`: run `check --staged --act-from-env <the variable holding the staged list>`; keep the trigger, the
   close gate and the fail-closed branches as they are.
4. Keep `--self-test` green and add to it arms for `--staged` and `--act` (bystander lands, own refused), each arm's PASS line
   naming the flag it exercises. Keep `.tools/tests/test_missions_tree_index_selftest.py` passing. `derive` is unchanged.

### ACCEPTANCE

<criterion id="GS2-AC1" cell_refs="GS-t-2"><invocation>python "org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/round1_prep/checks/r1_tree_scope.py"</invocation><expect>GS-T2-SCOPE ok=True</expect></criterion>
`GS2-AC1` -- with `LGIC_BLANKFIX`'s row drifted in the index only, `check --staged --act <NFRA_GATSCP's row>` passes and prints
`STANDING LGIC_BLANKFIX`; `--act <LGIC_BLANKFIX's row>` is refused (the difference control).

<criterion id="GS2-AC2" cell_refs="GS-t-2"><invocation>python "org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/round1_prep/checks/r1_treehook_seam.py"</invocation><expect>GS-T2-HOOK ok=True</expect></criterion>
`GS2-AC2` -- the seam: the real hook, given the staged list, lands beside the drift and refuses on it. A working-tree read fails
the second arm.

<criterion id="GS2-AC3" cell_refs="GS-t-2"><invocation>python "org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/round1_prep/checks/r1_tree_selftest.py"</invocation><expect>GS-T2-SELFTEST ok=True</expect></criterion>
`GS2-AC3` -- the tool's own `--self-test` stays green (every arm PASS, rc 0) and carries at least one PASS arm line naming
`--staged` and one naming `--act` or `STANDING`.

<expected_criteria>GS2-AC1,GS2-AC2,GS2-AC3</expected_criteria>

Each check plants its defect in a private copy of the git index; it changes no working-tree file and no ref. Read each check
before you build. Each prints its arms and ONE last line. AC1 and AC2 FAIL at the base. You do not edit the checks.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- No edit outside the grant. No change to any rule, the contract, the register files, or any project row. No override at any
  commit. Do not run `derive --write`.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `NFRA_GATSCP-D1-W2-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the check or
  the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not
  block.
- After this order, the same worker receives `GS-t-3` (box-sync and safe-merge call your `check --staged --act`), so keep the
  CLI exactly as written above.

<paths>
.tools/missions-tree-index.py
.tools/git-hooks/missions-tree-check.sh
.tools/tests/test_missions_tree_index_selftest.py
org/missions/D0/NFRA/NFRA_GATSCP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside it, in particular the check files under
`org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/round1_prep/checks/`.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_GATSCP/decompositions/NFRA_GATSCP_DECOMP.md</decomp_doc> (round 1), cell `GS-t-2`.
<owned_cells>GS-t-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: GS2-AC1, GS2-AC2, GS2-AC3. Instance at
`org/missions/D0/NFRA/NFRA_GATSCP/deliverables/0.9.0_WK_NFRA_GATSCP~2/NFRA_GATSCP.TO-GS-t-2.tree-check-staged-and-scoped.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> GS2-AC1,GS2-AC2,GS2-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the three last lines whole; the STANDING line as printed; how `--staged` reads each input; commits.

### AMENDMENT 1 (2.0.0_SA_COO~N1, 2026-10-09) -- the row id carries the dell1 coordinate

A row filed on dell1 is `NFRA_GATSCP-D1-W2-S<k>` (the row gate refuses a dell1 row without `-D1-`; measured on the issuer's own
row `NFRA_GATSCP-D1-S1` @6911a2f5d7). The refusal clause above now reads that form. Graded by: the surprise-row gate's fabric
coordinate limb; no TO-gate limb grades this modification beyond GATE (viii).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE thread round; no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the thread touches no IAM.
comp-adversary: DECLARED-NOT-APPLICABLE thread round; the cut's own arms: AC1 and AC2 carry the difference control (the same drift in the act's own project is refused), and AC2's own arm fails a working-tree read. BLIND: a violation present only in a working tree (by design, C-BYTES).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD v0.2 @7cb6183997 (FWD-1; C-SCOPE, C-BYTES); decomposition round 1. Base dry-run at the cut (box/dell1 95669cba44):
GS2-AC1 FAIL as expected (usage rc 2); GS2-AC2 FAIL as expected (own arm rc 0); GS2-AC3 FAIL as expected (green half PASS
38/38, arm half FAIL).
