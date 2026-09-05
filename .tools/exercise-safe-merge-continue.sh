#!/usr/bin/env bash
# EXERCISE the safe-merge --continue limb on REAL bytes, in an ISOLATED worktree.
# Never in the shared tree: manufacturing a conflict there is the hazard this fix is about.
set -uo pipefail
MAIN=/c/Users/AndrewBerman/Desktop/ajb_workspace
WT=/c/Users/ANDREW~1/AppData/Local/Temp/claude/sm-exercise
BR=sm-exercise-base
FEAT=sm-exercise-feat
export OPAL_AGENT_SERIAL=1.0.0_SA_CTO

cd "$MAIN" || exit 2
git worktree remove --force "$WT" 2>/dev/null || true
git branch -D "$BR" "$FEAT" 2>/dev/null || true
rm -rf "$WT" 2>/dev/null || true

echo "=== SETUP: isolated worktree off HEAD ==="
git worktree add -q -b "$BR" "$WT" HEAD || { echo "SETUP FAILED"; exit 2; }
cd "$WT" || exit 2

# an append-only file: both sides append at the same offset -- the S36 shape
printf 'row-1\nrow-2\nrow-3\n' > appendonly.txt
git add appendonly.txt >/dev/null
git -c user.name=x -c user.email=x@y commit -q --no-verify -m "base: the append-only file" || exit 2

git checkout -q -b "$FEAT"
printf 'row-1\nrow-2\nrow-3\nFEAT-row-A\n' > appendonly.txt
git add appendonly.txt >/dev/null
git -c user.name=x -c user.email=x@y commit -q --no-verify -m "feat: append FEAT-row-A" || exit 2

git checkout -q "$BR"
printf 'row-1\nrow-2\nrow-3\nBASE-row-B\n' > appendonly.txt
git add appendonly.txt >/dev/null
git -c user.name=x -c user.email=x@y commit -q --no-verify -m "base: append BASE-row-B" || exit 2

STATE="$(git rev-parse --git-path safe-merge-conflict)"
pass=0; fail=0
chk() { if eval "$2"; then echo "  PASS  $1"; pass=$((pass+1)); else echo "  FAIL  $1"; fail=$((fail+1)); fi; }

echo
echo "=== ARM 1 (RED, the bug that was live): a CONFLICT must leave the merge OPEN, not abort ==="
bash "$MAIN/.tools/safe-merge.sh" "$FEAT" -m "drain: exercise" > /tmp/sm1.out 2>&1
rc1=$?
echo "    rc=$rc1"
chk "rc is 4 (CONFLICT, merge open) and not 1 (aborted)"        "[ $rc1 -eq 4 ]"
chk "MERGE_HEAD EXISTS -- the merge was NOT aborted"            "[ -f \"\$(git rev-parse --git-path MERGE_HEAD)\" ]"
chk "the conflict state file was written"                       "[ -f '$STATE' ]"
chk "the output NAMES the conflicted path"                      "grep -q 'appendonly.txt' /tmp/sm1.out"
chk "the output forbids finishing with a bare git commit"       "grep -q 'Do NOT finish this with a bare' /tmp/sm1.out"

echo
echo "=== ARM 2 (RED): --continue with the conflict UNRESOLVED must refuse and keep it open ==="
bash "$MAIN/.tools/safe-merge.sh" --continue > /tmp/sm2.out 2>&1
rc2=$?
echo "    rc=$rc2"
chk "rc is 4 and it names the unresolved path"                  "[ $rc2 -eq 4 ] && grep -q 'unresolved conflict markers' /tmp/sm2.out"
chk "MERGE_HEAD still exists (nothing was aborted)"             "[ -f \"\$(git rev-parse --git-path MERGE_HEAD)\" ]"

echo
echo "=== ARM 3 (RED, THE POINT OF THE LIMB): a FOREIGN staged file must be refused ==="
printf 'row-1\nrow-2\nrow-3\nBASE-row-B\nFEAT-row-A\n' > appendonly.txt
git add appendonly.txt >/dev/null
echo "another seat's work" > foreign-seat-file.txt
git add foreign-seat-file.txt >/dev/null
bash "$MAIN/.tools/safe-merge.sh" --continue > /tmp/sm3.out 2>&1
rc3=$?
echo "    rc=$rc3"
chk "rc is 4 -- refused on the foreign path"                    "[ $rc3 -eq 4 ]"
chk "the FOREIGN file is NAMED in the refusal"                  "grep -q 'foreign-seat-file.txt' /tmp/sm3.out"
chk "the refusal explains the authorship consequence"           "grep -q \"draining seat's authorship\" /tmp/sm3.out"
chk "MERGE_HEAD still exists; nothing landed"                   "[ -f \"\$(git rev-parse --git-path MERGE_HEAD)\" ]"
chk "no merge commit was created"                               "[ \"\$(git rev-parse HEAD)\" = \"\$(git rev-parse $BR)\" ]"

echo
echo "=== ARM 4 (GREEN): unstage the foreign file, --continue must GRADE and COMMIT ==="
git rm -q --cached foreign-seat-file.txt >/dev/null 2>&1
rm -f foreign-seat-file.txt
before="$(git rev-parse HEAD)"
bash "$MAIN/.tools/safe-merge.sh" --continue -m "drain: exercise merge" > /tmp/sm4.out 2>&1
rc4=$?
echo "    rc=$rc4"
chk "rc is 0 -- the merge landed"                               "[ $rc4 -eq 0 ]"
chk "HEAD MOVED"                                                "[ \"\$(git rev-parse HEAD)\" != '$before' ]"
chk "the commit has TWO parents (a real merge)"                 "[ \"\$(git rev-list --parents -n1 HEAD | wc -w)\" -eq 3 ]"
chk "the commit is AUTHORED by the draining seat"               "git log -1 --format=%an | grep -q '1.0.0_SA_CTO'"
chk "the row gate ran on the merged index"                      "grep -q 'grading the MERGED index' /tmp/sm4.out"
chk "the conflict state file was CLEARED"                       "[ ! -f '$STATE' ]"
chk "both sides' rows survived the resolution"                  "grep -q 'FEAT-row-A' appendonly.txt && grep -q 'BASE-row-B' appendonly.txt"

echo
echo "=== ARM 5: --continue with NO merge open must refuse (not pretend) ==="
bash "$MAIN/.tools/safe-merge.sh" --continue > /tmp/sm5.out 2>&1
rc5=$?
chk "rc is 2 and it says nothing to continue"                   "[ $rc5 -eq 2 ] && grep -q 'NO merge in progress' /tmp/sm5.out"

echo
echo "=== ARM 6: --abort restores the tree and clears state ==="
git checkout -q "$BR" 2>/dev/null
git reset -q --hard "$before" 2>/dev/null
bash "$MAIN/.tools/safe-merge.sh" "$FEAT" -m x > /dev/null 2>&1
bash "$MAIN/.tools/safe-merge.sh" --abort > /tmp/sm6.out 2>&1
rc6=$?
chk "rc is 0 and the merge is gone"                             "[ $rc6 -eq 0 ] && [ ! -f \"\$(git rev-parse --git-path MERGE_HEAD)\" ]"
chk "state cleared"                                             "[ ! -f '$STATE' ]"

echo
echo "=== ARM 7 (RED, 2.0.0_SA_COO 94259): a merge that FAILS WITHOUT OPENING ONE must write NO state ==="
# an UNSTAGED local change the merge would overwrite: passes the index guard, then git refuses
git reset -q --hard "$BR" 2>/dev/null
rm -f "$STATE" "$STATE.branch" 2>/dev/null
printf 'row-1
row-2
row-3
BASE-row-B
LOCAL-UNCOMMITTED
' > appendonly.txt
bash "$MAIN/.tools/safe-merge.sh" "$FEAT" -m "should not open" > /tmp/sm7.out 2>&1
rc7=$?
echo "    rc=$rc7"
chk "rc is 1 (refused) -- NOT 4, because nothing is open"       "[ $rc7 -eq 1 ]"
chk "it says this is NOT a conflict"                            "grep -q 'is NOT a conflict' /tmp/sm7.out"
chk "NO conflict state file was written (the 94259 defect)"     "[ ! -f '$STATE' ]"
chk "no merge was left open"                                    "[ ! -f \"\$(git rev-parse --git-path MERGE_HEAD)\" ]"
chk "the banner does NOT claim a conflict with 0 paths"         "! grep -q 'CONFLICT -- THE MERGE IS OPEN' /tmp/sm7.out"

echo
echo "=== ARM 8 (94259 residue): --abort must clear a STALE state file with no merge open ==="
git checkout -q -- appendonly.txt 2>/dev/null
: > "$STATE"; echo "$FEAT" > "$STATE.branch"
bash "$MAIN/.tools/safe-merge.sh" --abort > /tmp/sm8.out 2>&1
rc8=$?
chk "rc is 0 and it reports clearing a STALE state file"        "[ $rc8 -eq 0 ] && grep -q 'STALE conflict state file' /tmp/sm8.out"
chk "the stale state file is GONE"                              "[ ! -f '$STATE' ]"

echo
echo "=== ARM 9: --continue over a stale state with no merge NAMES the stale file ==="
: > "$STATE"; echo "$FEAT" > "$STATE.branch"
bash "$MAIN/.tools/safe-merge.sh" --continue > /tmp/sm9.out 2>&1
rc9=$?
chk "rc is 2 and it tells the operator how to disarm"           "[ $rc9 -eq 2 ] && grep -q 'it is STALE' /tmp/sm9.out"
rm -f "$STATE" "$STATE.branch" 2>/dev/null

echo
echo "DENOMINATOR: $pass passed / $((pass+fail)) arm(s)"
[ "$fail" -eq 0 ] && echo "EXERCISE: ALL GREEN" || echo "EXERCISE: $fail FAILED"

echo
echo "=== TEARDOWN ==="
cd "$MAIN" || exit 0
git worktree remove --force "$WT" 2>/dev/null && echo "worktree removed" || echo "worktree NOT removed -- remove by hand: $WT"
git branch -D "$BR" "$FEAT" >/dev/null 2>&1 && echo "scratch branches deleted" || true
