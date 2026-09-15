#!/usr/bin/env bash
# Re-grade a FINISHED worker's proof instance against the task order as committed at a given SITEZ commit,
# inside the worker's own worktree (the checker grades the tree the script lives in), then restore the
# worktree's order bytes and PROVE the restore byte-identical by sha256. Never run against a live worker.
#
# usage: regrade_with_order_at.sh <worktree> <order-relpath> <instance-relpath> <criteria-csv> <sitez-commit>
# prints: the stale-copy verdict, the amended-bytes verdict, sha before/after, and RESTORED or RESTORE MISMATCH.
# exit:   0 when the amended-bytes checker is VALID and the restore is byte-identical; 1 otherwise.
W="$1"; O="$2"; I="$3"; C="$4"; AT="$5"
MAIN="C:/Users/Opal Bloomberg/Desktop/ajb_workspace"
S="C:/Users/OPALBL~1/AppData/Local/Temp/claude/C--Users-Opal-Bloomberg-Desktop-ajb-workspace/f44df7ef-924a-4d22-a758-c0e892a892d4/scratchpad"
tag="$(basename "$O" .md)"
cd "$W" || { echo "STOP: no worktree $W"; exit 1; }
dirty="$(git status --porcelain -- "$O" | cat)"
if [ -n "$dirty" ]; then echo "STOP: the order is dirty in the worktree [$dirty] -- not touching it"; exit 1; fi
before="$(sha256sum "$O" | cut -c1-64)"
echo "sha before: $before"
python .tools/proof-of-spec-check.py "$I" "$C" > "$S/regrade_${tag}_stale.txt" 2>&1
echo "stale-copy checker rc=$? -- $(tail -1 "$S/regrade_${tag}_stale.txt")"
git -C "$MAIN" show "$AT:$O" > "$S/regrade_${tag}_order_at.md" || { echo "STOP: cannot read $O at $AT"; exit 1; }
cp "$S/regrade_${tag}_order_at.md" "$O"
python .tools/proof-of-spec-check.py "$I" "$C" > "$S/regrade_${tag}_amended.txt" 2>&1
arc=$?
echo "amended-bytes checker rc=$arc -- $(tail -1 "$S/regrade_${tag}_amended.txt")"
git show HEAD:"$O" > "$O"
after="$(sha256sum "$O" | cut -c1-64)"
echo "sha after restore: $after"
if [ "$before" = "$after" ] && [ -z "$(git status --porcelain -- "$O" | cat)" ]; then
  echo "RESTORED byte-identical"
else
  echo "RESTORE MISMATCH -- STOP"; exit 1
fi
[ "$arc" = 0 ] && grep -q '^VALID' "$S/regrade_${tag}_amended.txt" && exit 0
exit 1
