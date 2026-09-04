#!/usr/bin/env bash
# EXERCISE the to-pipeline-gate MERGE EXEMPTION (0.0.0_AB_MSTR 94264) on real bytes, ISOLATED.
#
# The RED case is a merge that carries a task order authored by someone who is not the COO -- the
# exact shape that refused 27 of site Z's already-committed orders as "a NEW tree task order
# committed under 0.0.0_AB_MSTR". The GREEN control is the same file, same author, NO merge: it
# must still be refused, or the exemption is a hole rather than a narrow carve-out.
set -uo pipefail
MAIN=/c/Users/AndrewBerman/Desktop/ajb_workspace
WT=/c/Users/ANDREW~1/AppData/Local/Temp/claude/tpg-exercise
BR=tpg-ex-base
FEAT=tpg-ex-feat
TO=org/missions/D0/NFRA/NFRA_CLDGRPH/task-orders/NFRA_CLDGRPH.TO-EX-s-1.exercise-order.md

cd "$MAIN" || exit 2
git worktree remove --force "$WT" 2>/dev/null || true
git branch -D "$BR" "$FEAT" 2>/dev/null || true
rm -rf "$WT" 2>/dev/null || true

echo "=== SETUP ==="
git worktree add -q -b "$BR" "$WT" HEAD || { echo "SETUP FAILED"; exit 2; }
cd "$WT" || exit 2
mkdir -p "$(dirname "$TO")"
pass=0; fail=0
chk() { if eval "$2"; then echo "  PASS  $1"; pass=$((pass+1)); else echo "  FAIL  $1"; fail=$((fail+1)); fi; }

# a v2-grammar task order -- site Z's shape, which our v3 gate refuses on grammar too
mk_to() {
  printf '# TO-EX-s-1\n\n<issued_to>0.0.0_AB_MSTR</issued_to>\n<decomp_ref>d.md</decomp_ref>\n' > "$TO"
  printf '<owned_cells>EX-s-1</owned_cells>\n<criterion id="EX-s-1-c1" judgment="false"/>\n' >> "$TO"
}

echo
echo "=== GREEN CONTROL FIRST: the same order, NO merge, must still be REFUSED ==="
mk_to
git add "$TO" >/dev/null 2>&1
python "$MAIN/.tools/to-pipeline-gate.py" "$TO" > /tmp/tpg_green.out 2>&1
rcg=$?
echo "    rc=$rcg"
chk "a NEW tree task order outside a merge is still REFUSED (rc!=0)"  "[ $rcg -ne 0 ]"
chk "and the refusal is the authorship one"                           "grep -qi 'task order' /tmp/tpg_green.out"
chk "the exemption line is ABSENT outside a merge"                    "! grep -q 'MERGE COMMIT' /tmp/tpg_green.out"

git reset -q --hard "$BR" >/dev/null 2>&1
rm -f "$TO"

echo
echo "=== RED (the 94264 case): the SAME order arriving on a MERGE must be EXEMPT ==="
# base and feature both touch one file so the merge is a real merge; the feature also adds the TO
printf 'base\n' > ex-marker.txt; git add ex-marker.txt >/dev/null
git -c user.name=x -c user.email=x@y commit -q --no-verify -m "base marker" || exit 2
git checkout -q -b "$FEAT"
mk_to
printf 'feat\n' > ex-marker.txt
git add "$TO" ex-marker.txt >/dev/null
git -c user.name=x -c user.email=x@y commit -q --no-verify -m "feat: an already-committed task order" || exit 2
git checkout -q "$BR"
printf 'base2\n' > ex-marker.txt; git add ex-marker.txt >/dev/null
git -c user.name=x -c user.email=x@y commit -q --no-verify -m "base marker 2" || exit 2

git merge --no-commit --no-ff "$FEAT" > /tmp/tpg_merge.out 2>&1
MH="$(git rev-parse --git-path MERGE_HEAD)"
chk "a merge is genuinely in progress (precondition of the RED arm)"  "[ -f \"\$MH\" ]"
chk "the merge really carries the task order"                         "git diff --cached --name-only | grep -q 'TO-EX-s-1'"
python "$MAIN/.tools/to-pipeline-gate.py" $(git diff --cached --name-only) > /tmp/tpg_red.out 2>&1
rcr=$?
echo "    rc=$rcr"
chk "THE FIX: the gate EXITS 0 on a merge carrying a task order"      "[ $rcr -eq 0 ]"
chk "and it SAYS it exempted a merge (not a silent pass)"             "grep -q 'MERGE COMMIT -- task-order checks exempt' /tmp/tpg_red.out"
chk "no authorship refusal was emitted"                               "! grep -q 'is the only agent that does task orders' /tmp/tpg_red.out"

git merge --abort 2>/dev/null || true

echo
echo "=== NARROWNESS: after the merge is aborted, the same file is refused again ==="
git reset -q --hard "$BR" >/dev/null 2>&1
mk_to
git add "$TO" >/dev/null 2>&1
python "$MAIN/.tools/to-pipeline-gate.py" "$TO" > /tmp/tpg_after.out 2>&1
rca=$?
chk "rc!=0 once MERGE_HEAD is gone -- the exemption did not stick"    "[ $rca -ne 0 ]"

echo
echo "DENOMINATOR: $pass passed / $((pass+fail)) arm(s)"
[ "$fail" -eq 0 ] && echo "EXERCISE: ALL GREEN" || echo "EXERCISE: $fail FAILED"

echo
echo "=== TEARDOWN ==="
cd "$MAIN" || exit 0
git worktree remove --force "$WT" 2>/dev/null && echo "worktree removed" || echo "worktree NOT removed: $WT"
git branch -D "$BR" "$FEAT" >/dev/null 2>&1 && echo "scratch branches deleted" || true
