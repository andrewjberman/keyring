#!/usr/bin/env bash
# Exercise of safe-merge.sh's one-merge lock and MERGE_HEAD re-read (NFRA_OPLGTW-Z-S66) in a scratch repo.
# usage: bash sm_lock_exercise.sh <abs path to safe-merge.sh>
set -u
SM="$1"
S="/c/tmp/mstrz-relay/sm-scratch-$$"
rm -rf "$S"; mkdir -p "$S"; cd "$S" || exit 2
git init -q -b main .
git config user.name t; git config user.email t@t; git config core.hooksPath /nonexistent-hooks
echo base > base.txt; git add .; git commit -q -m base
for b in A B C; do
  git checkout -q -b "$b" main; echo "$b" > "$b.txt"; git add .; git commit -q -m "add $b"
done
git checkout -q main
export OPAL_AGENT_SERIAL="0.0.0_TEST_X"
pass=0; n=0
ok() { n=$((n+1)); if [ "$2" = "$3" ]; then pass=$((pass+1)); echo "  PASS  $1"; else echo "  FAIL  $1 (got '$2', want '$3')"; fi; }

echo "T1 lock held by a live other run"
mkdir .git/safe-merge.lock.d; echo "0.0.0_TEST_OTHER" > .git/safe-merge.lock.d/serial; echo $$ > .git/safe-merge.lock.d/pid; echo B > .git/safe-merge.lock.d/what
bash "$SM" A -m t1 > t1.out 2>&1; ok "rc 2" "$?" "2"
ok "names the holder" "$(grep -c 'ANOTHER safe-merge RUN HOLDS' t1.out)" "1"
ok "the other run's lock is kept" "$([ -d .git/safe-merge.lock.d ] && echo yes || echo no)" "yes"
ok "nothing committed" "$(git log --oneline | wc -l | tr -d ' ')" "1"
rm -rf .git/safe-merge.lock.d

echo "T2 a merge this run did not open"
git merge -q --no-commit --no-ff B > /dev/null 2>&1
bash "$SM" A -m t2 > t2.out 2>&1; ok "rc 2" "$?" "2"
ok "says a merge is already open" "$(grep -c 'A MERGE IS ALREADY OPEN' t2.out)" "1"
ok "the foreign merge is NOT aborted" "$([ -f .git/MERGE_HEAD ] && echo open || echo gone)" "open"
git merge --abort

echo "T3 green merge"
bash "$SM" A -m "t3 merge A" > t3.out 2>&1; ok "rc 0" "$?" "0"
ok "two parents" "$(git log -1 --format=%p | wc -w | tr -d ' ')" "2"
ok "author is the draining seat" "$(git log -1 --format=%an)" "0.0.0_TEST_X"
ok "A.txt landed" "$([ -f A.txt ] && echo yes || echo no)" "yes"
ok "lock released" "$([ -d .git/safe-merge.lock.d ] && echo held || echo released)" "released"

echo "T4 stale lock (dead pid, no merge open)"
mkdir .git/safe-merge.lock.d; echo "0.0.0_TEST_DEAD" > .git/safe-merge.lock.d/serial; echo 999999 > .git/safe-merge.lock.d/pid
bash "$SM" B -m "t4 merge B" > t4.out 2>&1; ok "rc 0" "$?" "0"
ok "says it cleared a stale lock" "$(grep -c 'clearing a STALE one-merge lock' t4.out)" "1"
ok "B.txt landed" "$([ -f B.txt ] && echo yes || echo no)" "yes"
ok "lock released" "$([ -d .git/safe-merge.lock.d ] && echo held || echo released)" "released"

echo "T5 MERGE_HEAD replaced during the grade (a python shim swaps the open merge)"
git checkout -q -b D main; echo D > D.txt; git add D.txt; git commit -q -m "add D"; git checkout -q main
mkdir shim
cat > shim/python <<'EOF'
#!/usr/bin/env bash
git merge --abort > /dev/null 2>&1
git merge -q --no-commit --no-ff D > /dev/null 2>&1
exit 0
EOF
chmod +x shim/python
H0="$(git rev-parse HEAD)"
PATH="$S/shim:$PATH" bash "$SM" C -m "t5 merge C" > t5.out 2>&1; ok "rc 1" "$?" "1"
ok "says MERGE_HEAD changed" "$(grep -c 'MERGE_HEAD CHANGED UNDER THIS RUN' t5.out)" "1"
ok "HEAD unmoved" "$(git rev-parse HEAD)" "$H0"
ok "the other merge is still open, not aborted" "$([ -f .git/MERGE_HEAD ] && echo open || echo gone)" "open"
ok "lock released" "$([ -d .git/safe-merge.lock.d ] && echo held || echo released)" "released"
git merge --abort

echo "T6 conflict keeps the lock; another seat cannot --continue or --abort; the opener can"
git checkout -q -b E main; echo E > base.txt; git add .; git commit -q -m "E edits base"; git checkout -q main
echo M > base.txt; git add .; git commit -q -m "main edits base"
bash "$SM" E -m "t6 merge E" > t6.out 2>&1; ok "rc 4 on conflict" "$?" "4"
ok "lock kept across the open conflict" "$([ -d .git/safe-merge.lock.d ] && echo held || echo released)" "held"
OPAL_AGENT_SERIAL="0.0.0_TEST_OTHER" bash "$SM" --abort > t6b.out 2>&1; ok "another seat's --abort rc 2" "$?" "2"
ok "merge still open after the refused abort" "$([ -f .git/MERGE_HEAD ] && echo open || echo gone)" "open"
OPAL_AGENT_SERIAL="0.0.0_TEST_OTHER" bash "$SM" --continue > t6c.out 2>&1; ok "another seat's --continue rc 2" "$?" "2"
OPAL_AGENT_SERIAL="0.0.0_TEST_OTHER" bash "$SM" A > t6d.out 2>&1; ok "another seat's new merge rc 2" "$?" "2"
echo R > base.txt; git add base.txt
bash "$SM" --continue -m "t6 merge E" > t6e.out 2>&1; ok "the opener's --continue rc 0" "$?" "0"
ok "lock released after the commit" "$([ -d .git/safe-merge.lock.d ] && echo held || echo released)" "released"

echo "DENOMINATOR: $pass of $n arm(s) passed"
if [ "$pass" -ne "$n" ]; then echo "--- outputs kept at $S"; exit 1; fi
cd /c/tmp && rm -rf "$S"
echo PASS
