# TO-YCD-d-8 -- read six armed generator, test and builder rows again at the tree as it stands; each gets one row that RESOLVES or RE-CUTS it

<to_id>IRPT_YCDGEN.TO-YCD-d-8</to_id>
<project>IRPT_YCDGEN</project>
<issued_to>0.9.0_WK_IRPT_YCDGEN~10</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>8</round>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `YCD-d-8` (`decompositions/IRPT_YCDGEN_DECOMP_R8.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none.

---

## WORKER FACE

### Read first

`org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R8.md`, the Finding and the row for `YCD-d-8`. Then, in
`org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md`, the six rows named below. Find each by its `"id"` value with the native Grep tool.

### THE CELL

Six rows in the project's surprise channel are ARMED or INERT against code that later cells rewrote. A row like that is neither
true nor false until it is read again. Read each one again against the tree in YOUR worktree, and say what the tree does today.

The six rows: `IRPT_YCDGEN-W6-S1`, `IRPT_YCDGEN-W6-S2`, `IRPT_YCDGEN-D2-W6-S3`, `IRPT_YCDGEN-D2-W7-S1`, `IRPT_YCDGEN-D2-W6-S1`,
`IRPT_YCDGEN-D2-W6-S2`.

For EACH row, in this order:

1. Read its `spec_asserts`, `world_is` and `notes`. They name the files, tests or commands the row was measured with.
2. Re-measure THAT claim today: run the test or command it names, or read the lines it names. A claim about a generator is
   re-measured by running the generator into a TEMPORARY directory, never into the tracked tree. If a named file or test no
   longer exists, that absence is your measurement; say which path you looked at.
3. Append ONE new row to the END of the channel file. Its `## ` heading is exactly one of:
   - `## <new id> -- RESOLVES <old id> (<what the tree does today, in a few words>)` when the claim is no longer true. The row
     is `disposition` `DISMISSED_WITH_REASON`, `hazard_standing` `INERT`, with the measurement as its evidence;
   - `## <new id> -- RE-CUTS <old id> (<what is still true, in a few words>)` when the claim still holds. Restate it against
     TODAY's code with file and line, keep the old row's `class`, and set `hazard_standing` to what you measured.
4. Do not change, move or delete the old row. Do not fix anything the row describes: this cell measures, it does not repair.

New row ids are `IRPT_YCDGEN-D2-W10-S1` to `-S6`, one per old row, in the order listed above. Each row's `surfaced_at` is the
output of `date -u +%Y-%m-%dT%H:%M:%SZ` run at the moment you write it; never type a time. Copy the field set of row
`IRPT_YCDGEN-D2-S23` (search for its heading in the same file) and add `"notes"`.

If one row's claim cannot be measured from this box at all, still append its row as `RE-CUTS`, say exactly what could not be
run and why, and report it. Do not guess a result.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="D8-AC1" cell_refs="YCD-d-8"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r8/r8_checks.py d8</invocation><expect>^R8-D8-OK</expect></criterion>

<criterion id="D8-AC2" cell_refs="YCD-d-8"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r8/r8_checks.py gate</invocation><expect>^R8-GATE-OK</expect></criterion>

<expected_criteria>D8-AC1,D8-AC2</expected_criteria>

- AC1: each of the six old ids has exactly one `IRPT_YCDGEN-D2-W10-S<k>` heading that says RESOLVES or RE-CUTS it. At base it FAILs
  (0 of 6).
- AC2: `python .tools/surprise-row-gate.py --check` on the channel file returns 0.

## BOUNDS

- **Grant.** The `<paths>` block only. No deploy, no AWS calls, no HTTP, no installs. You change NO product code and NO test.
- **Refusal clause.** If a criterion cannot be met as written: stop, report, and do not weaken a check.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_YCDGEN~10" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_YCDGEN~10@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_YCDGEN~10 <0.9.0_WK_IRPT_YCDGEN~10@opal.agent>" -F <msgfile> -- <paths>`.
  - Write the message file with the Write tool. Do not pre-`git add`.
  - ASCII only. Use the native Grep/Glob/Read tools; a recursive shell grep over the repo is denied by a hook.

<paths>
org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~10/
org/missions/D9/IRPT/IRPT_YCDGEN/task-orders/IRPT_YCDGEN.TO-YCD-d-8.remeasure-six-generator-and-builder-rows.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R8.md</decomp_doc> round 8, cell `YCD-d-8`.
<owned_cells>YCD-d-8</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: D8-AC1, D8-AC2. Instance at
`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~10/IRPT_YCDGEN.TO-YCD-d-8.remeasure-six-generator-and-builder-rows.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_YCDGEN.TO-YCD-d-8`.
- Validate with `python .tools/proof-of-spec-check.py <instance> D8-AC1,D8-AC2` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~65/IRPT_ANLREQ.TO-AR-g-22.packager-speaks-i7-and-custody-i5prime.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- a six-line table: old id, RESOLVES or RE-CUTS, the one command or file read that decided it, the new row id;
- anything you could not run, and why;
- commits.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- the cell writes six rows to an append-only channel and changes no product file.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission, no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- no route.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- read the six rows' one_line and notes and the round-8 analysis section 2. Traps: a row dismissed because its file moved and nobody looked for the successor; a generator run into the tracked tree; a typed timestamp (this issuer's own defect on D2-S26..S37); repairing what the row describes.
lane: ANY (the surprise channel).
</preflight>

Source: CTO round-8 analysis @fe73849335 section 3 item 4 and section 2 (rows W6-S1, W6-S2, D2-W6-S3, D2-W7-S1, D2-W6-S1, D2-W6-S2).
