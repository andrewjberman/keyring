# Change 2, hook half -- the pre-commit row-gate step skips a tree safe-merge already graded

**For:** each box's MSTR (`0.0.0_AB_MSTR`, `~Z`, `~DELL1`, `~DELL2`): the live `.git/hooks/pre-commit` is per clone and
untracked. `.tools/git-hooks/install-surprise-row-gate.sh` appends its block only when its marker is absent, so an edit
to the installer never reaches an existing hook. Replace the block in place on each box, then make the same edit in the
installer's heredoc so a fresh clone gets it.
**Why:** Andrew-direct ~19:1xZ, "Sure, yes" (record: `MERGE_ROOT_CAUSE_B3_20261008.md` section 7). `safe-merge.sh`
@ this commit exports `SAFE_MERGE_GRADED_TREE` (the tree it graded) and `SAFE_MERGE_GRADED_GATE` (the gate's blob id)
for its merge commit. Proposal: `0.0.0_AB_MSTR` `PROPOSAL_20261005_SAFE_MERGE_ROW_GATE_SPEED_CHANGES_2_AND_3.md`,
section 2.

## Replace this line in the row-gate step

```bash
    ROOT="$ROOT" STAGED="$STAGED" python "$ROOT/.tools/surprise-row-gate.py" || exit 1
```

## with

```bash
    if [ -n "${SAFE_MERGE_GRADED_TREE:-}" ] && [ -n "${SAFE_MERGE_GRADED_GATE:-}" ] \
       && [ "$(git write-tree 2>/dev/null)" = "$SAFE_MERGE_GRADED_TREE" ] \
       && [ "$(git hash-object "$ROOT/.tools/surprise-row-gate.py" 2>/dev/null)" = "$SAFE_MERGE_GRADED_GATE" ]; then
        echo "SKIP: row gate -- safe-merge already graded this exact tree ($SAFE_MERGE_GRADED_TREE) with this exact gate (change 2)"
    else
        ROOT="$ROOT" STAGED="$STAGED" python "$ROOT/.tools/surprise-row-gate.py" || exit 1
    fi
```

**Safety:** the skip is keyed on the content being committed, never on a claim. A different index, a peer's staged path
or an edited gate changes one of the two ids, and the gate runs as before. An ordinary commit never has the variables.
**Exercised** (scratch repo, 19:20Z): a fixture hook recomputing both ids printed "graded ids MATCH what is being
committed" on a clean merge and on a conflict finished with `--continue`.
