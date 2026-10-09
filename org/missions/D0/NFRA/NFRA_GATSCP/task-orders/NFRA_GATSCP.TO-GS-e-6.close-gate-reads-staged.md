# TO NFRA_GATSCP.TO-GS-e-6 -- round 2 GS-e-6: the round-close gate grades what the commit carries, not the shared working tree

<to_id>NFRA_GATSCP.TO-GS-e-6</to_id>
<project>NFRA_GATSCP</project>
<issued_to>0.9.0_WK_NFRA_GATSCP~7</issued_to>
<issued_by>2.0.0_SA_COO~N1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>~N1</workstream>

**Directive:** D0 | **Fabric:** dell1 | **Decomp cell:** `GS-e-6` (`decompositions/NFRA_GATSCP_DECOMP.round2.md`) | **outcome_ref:** FWD-6 |
**depends_on:** none

---

## WORKER FACE

### CONTEXT

The tree hook `.tools/git-hooks/missions-tree-check.sh` grades a commit that stages tree paths. Round 1 made its main check read the
staged bytes (`check --staged --act-from-env MTC_ACT_PATHS`). Its `close_gate()` still reads the working tree in two places:
- For each staged `org/missions/D<n>/<M>/<CODE>/project.json`, it reads `dep_stage` from the index (`git show ":$p"`) but FALLS
  BACK to the working-tree file (`tr -d '\r' < "$ROOT/$p" | sed ...`) when that read is empty.
- When `dep_stage` moves to ROUND_CLOSE or CLOSED, it runs `python .tools/round-close-check.py --project "$code"`. That tool
  (500 lines; CLI at :469-478: `--project --round --workstream --device --deep --max-age-minutes --reviewer-only --selftest`) opens
  the project's task orders, proof-of-spec instances and channel rows from the WORKING TREE. It prints
  `PROOFS mode=... complete=N proof_ok=N proof_bad=N` and a last line `ROUND-CLOSE project=... verdict=MAY-CLOSE|REFUSED`.
So another seat's unsaved edit in the shared folder (an order, a proof, a row) is graded inside someone else's close commit, and a
file the commit stages differently is graded as the working tree has it. FWD-6 asks that the checks read what the commit carries.

### THE CELL

`GS-e-6`. `round-close-check.py --staged` reads the project's orders, proofs and rows from the index; the tree hook's close gate
passes it and drops its working-tree fallback.

**Build:**
1. `round-close-check.py --staged`: every file it reads for the project (task orders, proof instances, channel documents, the
   project row, the decomposition) comes from the index git resolves (`GIT_INDEX_FILE`, `GIT_DIR`): enumerate with `git ls-files`
   and read with `git cat-file --batch` or `git show :<path>`. A file absent from the index is absent, even if the working tree
   has it. The liveness/reviewer read (runtime state, not repository content) is unchanged. Without `--staged`: unchanged. Same
   output lines.
2. `missions-tree-check.sh` `close_gate()`: call `round-close-check.py --project "$code" --staged`, and delete the working-tree
   fallback for `dep_stage` (an unreadable staged row is not a ROUND_CLOSE move; print one `WARN:` line naming the path).
   Everything else in the hook stays as it is.
3. `round-close-check.py --selftest` stays green; add one arm for `--staged`.

### ACCEPTANCE

<criterion id="GE6-AC1" cell_refs="GS-e-6"><invocation>python "org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/round2_prep/checks/r2_close_staged.py"</invocation><expect>GS-E6-CLOSE ok=True</expect></criterion>
`GE6-AC1` -- `--staged` over a private index that lacks one of round 1's proof instances reads fewer than 3 proofs ok, while the
same plant read from the working tree (no `--staged`) still reads 3 (the difference control).

<criterion id="GE6-AC2" cell_refs="GS-e-6"><invocation>python "org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/round2_prep/checks/r2_closegate_staged.py"</invocation><expect>GS-E6-HOOK ok=True</expect></criterion>
`GE6-AC2` -- the close gate passes `--staged` and has no working-tree fallback (structural; the issuer's real ROUND_CLOSE commit of
this round exercises the hook).

<expected_criteria>GE6-AC1,GE6-AC2</expected_criteria>

Read both checks before you build. Each prints its arms and ONE last line. Both FAIL at the base. You do not edit the checks. Report
`python .tools/round-close-check.py --selftest`'s last line after your change.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- No edit outside the grant. Do not create or remove any enforce switch file under `org/mcp/`.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `NFRA_GATSCP-D1-W7-S<k>`, `surfaced_at` = `date -u +%FT%H:%MZ` at filing) in the investigation file, and do not weaken the check
  or the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not
  block.

<paths>
.tools/round-close-check.py
.tools/git-hooks/missions-tree-check.sh
org/missions/D0/NFRA/NFRA_GATSCP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside it, in particular the check files under
`org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/`.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_GATSCP/decompositions/NFRA_GATSCP_DECOMP.round2.md</decomp_doc> (round 2), cell `GS-e-6`.
<owned_cells>GS-e-6</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: GE6-AC1, GE6-AC2. Instance at
`org/missions/D0/NFRA/NFRA_GATSCP/deliverables/0.9.0_WK_NFRA_GATSCP~7/NFRA_GATSCP.TO-GS-e-6.proof_of_spec.json` with `to_id`
`NFRA_GATSCP.TO-GS-e-6`, validated with `python .tools/proof-of-spec-check.py <instance> GE6-AC1,GE6-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** both last lines whole; the selftest's last line; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule.
comp-iam: DECLARED-NOT-APPLICABLE no IAM is read, granted or changed by this cell.
comp-adversary: RUN -- AC1 arm 3 is the difference control (the working-tree read still sees the file the index lacks). BLIND: AC2 is structural; the seam is the issuer's real ROUND_CLOSE commit; the reviewer-liveness read stays runtime state by design.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round1.md @5c65160327 item 6; PRD C-BYTES; decomposition round 2. Base dry-run (box/dell1 7611122124): GE6-AC1
FAIL as expected (no --staged; the worktree control arm PASS); GE6-AC2 FAIL as expected.
