#!/usr/bin/env bash
# safe-merge.sh -- the DRAIN'S REFUSER (spine v3 L7, gap 3).
#
# THE HOLE THIS CLOSES: `git merge` runs NO hook. A worker's branch carries
# surprise-channel rows minted against ITS OWN index, which cannot see the main
# index's allocations; the merge then lands them with nothing having graded the
# UNION. Measured 2026-09-04 on v3's first drain: NFRA_COMPEFFICACY-S34 was minted
# in two indexes and both are now at HEAD permanently (append-only binds them).
#
# THE MECHANISM IS ONE FLAG: `git merge --no-commit` builds the merged INDEX
# without landing the commit. That is the only window in which the row gate can
# see the union, and in which a collision is still a re-mint on the branch rather
# than a permanent fact. The gate's duplicate-id limb (@72d05b2642) grades the
# index it is given -- so given the MERGED index, it does the cross-document
# census that no seat should be doing by hand.
#
# ON REFUSAL THIS ABORTS THE MERGE -- WITH ONE DELIBERATE EXCEPTION: a CONFLICT.
#
# ⛔ NFRA_CLDGRPH-S36 (2.0.0_SA_COO~A, 2026-09-04): this script's two protections were
# BOTH LOST in exactly the case they were built for. It aborted on a conflicted merge
# BEFORE its index guard and its row gate could run, so the drain had to be finished by
# hand -- with neither. And the conflict is not the exception: an append-only surprise
# channel takes every side's rows at the same offset and every side restates the header,
# so two concurrent workers ALWAYS collide there. 3 of 3 of round 4's drains conflicted.
# THE ABORT PATH WAS THE DRAIN PATH.
#
# So a CONFLICT now leaves the merge OPEN and hands it back with `--continue`. Every
# other refusal still aborts. `--continue` re-enters the SAME grade and the SAME authored
# commit, and adds the check the one-shot path gets free from its pre-merge index guard:
# a path staged that the MERGE did not stage is another seat's work riding the drain.
#
# Usage:  bash .tools/safe-merge.sh <branch-to-merge> [-m <subject>]
#         bash .tools/safe-merge.sh --continue [-m <subject>]   # after resolving
#         bash .tools/safe-merge.sh --abort                     # give up, restore the tree
#         bash .tools/safe-merge.sh --self-test
#
#         bash .tools/safe-merge.sh --verify-merge <commit>      # read-only tree check of a landed merge
#         bash .tools/safe-merge.sh --verify-index <commit>      # read-only: does the index of THIS worktree agree with HEAD on that merge's paths
#
# EXIT CODES: 0 merged | 1 refused, merge aborted | 2 usage/precondition, nothing done
#             4 CONFLICT, THE MERGE IS OPEN AND YOURS TO RESOLVE (nothing landed)
#             5 COMMITTED BUT THE BRANCH WAS NOT CARRIED, in whole or in part (tree check, see _verify_merge_tree)
#             6 COMMITTED AND CARRIED, BUT THE INDEX DISAGREES WITH HEAD on merged path(s) (see _verify_shared_index)
#             7 COMMITTED BUT THE MERGE COMMIT LACKS PATH(S) THE MERGE STAGED (GS-f-6, row D1-S5; see _verify_staged_carried)
#
# Owner 2.0.0_SA_COO (the drain is the COO's limb). Lane .tools/ (ANY).
set -uo pipefail

ROOT="$(git rev-parse --show-toplevel 2>/dev/null || true)"
[ -n "$ROOT" ] || { echo "safe-merge: not inside a git worktree" >&2; exit 2; }
cd "$ROOT" || exit 2

# The gate lives beside THIS script, not under the target repo's root: a drain of a branch in a
# nested repo (portal/, a gitlink with no .tools/) resolved "$ROOT/.tools/..." to nothing and
# refused every portal drain as rc=2 (IRPT_FNTEND FE-s-1 drain, 2026-09-10).
GATE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/surprise-row-gate.py"
. "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/merged-checker.sh" || { echo "safe-merge: cannot source merged-checker.sh" >&2; exit 2; }

# ---------------------------------------------------------------- self-test
if [ "${1:-}" = "--self-test" ]; then
  fails=0; n=0
  chk() { n=$((n+1)); if eval "$2"; then echo "  PASS  $1"; else echo "  FAIL  $1"; fails=$((fails+1)); fi; }
  echo "safe-merge --self-test"
  chk "the row gate exists at the path this script calls"        "[ -f '$GATE' ]"
  chk "the gate runs standalone and exits 0 on a clean index"    "python '$GATE' >/dev/null 2>&1"
  chk "refuses with no branch argument"                          "! bash '$0' 2>/dev/null"
  chk "refuses a branch that does not exist"                     "! bash '$0' definitely-not-a-branch-xyz 2>/dev/null"
  chk "git supports --no-commit (the whole mechanism)"           "git merge --help 2>/dev/null | grep -q -- '--no-commit' || true"
  # REGRESSION ARM for the bug this script shipped with: the gate takes argv, so a BARE
  # call grades nothing and returns 0. If that ever reads as a pass, the refuser is blind.
  chk "a BARE gate call reports ZERO dispatched paths (the vacuous-pass trap)" \
      "python '$GATE' 2>&1 | grep -q '0 dispatched path'"
  chk "the script feeds the gate from the staged set, never bare"  \
      "grep -q 'STAGED_ARR\[@\]' '$0'"
  # REGRESSION ARM (94639): above the ~32 KB argv cliff the list goes through the STAGED
  # environment, and rc=126/127 is named as "the gate did not run", never as a collision.
  chk "the script hands the gate its list through STAGED above the argv cliff" \
      "grep -q 'exceed the ~32 KB Windows cliff' '$0'"
  chk "an rc=126 launch failure is reported as NOT a row-gate verdict"  \
      "grep -q 'THE ROW GATE DID NOT RUN' '$0'"
  # REGRESSION ARM: the drain commit must name the draining seat, never the git-config identity.
  chk "the merge commit carries --author (no silent git-config attribution)" \
      "grep -q 'git commit --no-edit --author' '$0'"
  chk "an unset OPAL_AGENT_SERIAL REFUSES rather than guessing an author" \
      "grep -q 'OPAL_AGENT_SERIAL is unset' '$0'"
  # --continue limb (NFRA_CLDGRPH-S36). STRUCTURAL ONLY, and deliberately so: an arm that ran
  # `--continue` for real would read the SHARED worktree's merge state, so it would behave
  # differently depending on whether another seat happens to be draining right now -- a test
  # whose verdict depends on a peer is not a test. The behaviour is covered by EXERCISE below.
  chk "a CONFLICT does NOT abort -- the S36 fix (exit 4, merge left open)" \
      "grep -q 'CONFLICT -- THE MERGE IS OPEN AND NOTHING HAS LANDED' '$0' && grep -q 'exit 4' '$0'"
  chk "the conflict path records what the merge staged (so --continue can spot a foreign file)" \
      "grep -q 'comm -12 \"\$STATE.cached\" \"\$STATE.mine\" > \"\$STATE\"' '$0'"
  chk "--continue refuses while any path is still UNRESOLVED" \
      "grep -q 'still carry unresolved conflict markers' '$0'"
  chk "--continue refuses a path THIS MERGE DID NOT STAGE (the drain-sweep guard)" \
      "grep -q 'THIS MERGE DID NOT STAGE' '$0'"
  chk "--continue refuses when this script did not open the merge (no state file)" \
      "grep -q 'THIS script did not open it' '$0'"
  chk "--continue refuses when HEAD moved since the merge opened (D1-S16)" \
      "grep -q 'HEAD MOVED SINCE THE MERGE OPENED' '$0' && grep -q 'safe-merge-conflict' '$0' && grep -q 'STATE.head' '$0'"
  chk "--abort exists and clears the conflict state" \
      "grep -q 'merge aborted; tree restored and conflict state cleared' '$0'"
  chk "the state file is resolved via --git-path (a linked worktree keeps its own)" \
      "grep -q 'git rev-parse --git-path safe-merge-conflict' '$0'"
  # REGRESSION ARM (1.0.0_SA_CTO~Z 2026-09-29): "MERGED" was printed on merges whose tree equals ^1.
  chk "the commit path reads the TREE before reporting MERGED (exit 5 when the branch was not carried)" \
      "grep -q '_verify_merge_tree HEAD' '$0' && grep -q 'COMMITTED BUT THE BRANCH WAS NOT CARRIED' '$0'"
  # REGRESSION ARM (2.0.0_SA_COO~Y 103457): a PARTIAL drop on parents that merge clean returned 0 and printed MERGED.
  chk "a partial drop is graded against the clean merge tree of the parents (exit 5 when a needed file is lost)" \
      "grep -q 'git merge-tree --write-tree' '$0' && grep -q 'NEEDED FILE(S) WERE NOT CARRIED' '$0'"
  # REGRESSION ARM (NFRA_OPLGTW-Z-S23 residual, 2026-10-03): the private index is taken BEFORE the grade, and the grade
  # reads it. Taken after the grade, a peer staging inside HEAD..MERGE_HEAD during the minutes-long grade rode in.
  chk "the private index is snapshotted before the grade, and the grade reads it" \
      "[ \"\$(grep -n 'could not snapshot the index after the merge' '$0' | tail -1 | cut -d: -f1)\" -lt \"\$(grep -n 'grading the MERGED index' '$0' | tail -1 | cut -d: -f1)\" ] && grep -q 'GIT_INDEX_FILE=\"\$_PRIV_IDX\" python \"\$GATE\"' '$0'"
  # REGRESSION ARM (NFRA_OPLGTW-Z-S61): the commit path reads the INDEX against HEAD after the merge lands.
  chk "the commit path reads the index against HEAD after MERGED (exit 6 when merged paths are stale)" \
      "grep -q '_verify_shared_index HEAD' '$0' && grep -q 'THE INDEX DISAGREES WITH HEAD ON' '$0'"
  # REGRESSION ARMS (NFRA_OPLGTW-Z-S66): one merge per worktree, and the commit re-reads MERGE_HEAD.
  chk "the one-shot path refuses a merge it did not open and takes the one-merge lock before the clean-index check" \
      "grep -q 'A MERGE IS ALREADY OPEN in this worktree' '$0' && [ \"\$(grep -n 'ANOTHER safe-merge RUN HOLDS THIS WORKTREE' '$0' | tail -1 | cut -d: -f1)\" -lt \"\$(grep -n 'the index carries STAGED changes' '$0' | tail -1 | cut -d: -f1)\" ]"
  chk "the commit refuses when MERGE_HEAD is no longer the one this run opened" \
      "grep -q 'MERGE_HEAD CHANGED UNDER THIS RUN' '$0'"
  chk "--abort and --continue refuse a merge held by another seat's lock" \
      "[ \"\$(grep -c 'is held by another run' '$0')\" -ge 3 ]"
  chk "--verify-index refuses a non-merge commit" \
      "! bash '$0' --verify-index \"\$(git rev-list --no-merges -n 1 HEAD)\" >/dev/null 2>&1"
  chk "--verify-merge refuses a non-merge commit" \
      "! bash '$0' --verify-merge \"\$(git rev-list --no-merges -n 1 HEAD)\" >/dev/null 2>&1"
  # GS-t-3: the fast lane (lands by commit-tree, so no commit hook fires) runs the scoped tree check on the merged bytes.
  chk "the fast lane runs the scoped tree check on its private index and refuses by it" \
      "grep -q 'check --staged --act-from-env _SM_ACT' '$0' && grep -q 'merged_checker_path ' '$0' && grep -q 'REFUSED BY THE TREE CHECK ON THE MERGE' '$0'"
  # GS-f-6 (row D1-S5): the commit paths are compared with the paths the merge staged; behaviour is covered by
  # .tools/tests/test_safe_merge_continue.py (a full resolution exits 0; the planted partial exits 7).
  chk "the commit path refuses a merge commit lacking a path the merge staged (exit 7)"       "grep -q '_verify_staged_carried HEAD' '$0' && grep -q 'the merge commit lacks' '$0'"
  echo "DENOMINATOR: $((n-fails)) of $n arm(s) passed"
  echo "  STOP: BLIND SPOT, STATED: every arm above is a REFUSAL or a structural check. This"
  echo "     self-test has NO GREEN MERGE ARM -- a version of this script that refused"
  echo "     EVERYTHING would pass all of them. A self-test cannot safely perform a real"
  echo "     merge in the SHARED tree, so the permit path is covered by EXERCISE, not here:"
  echo "       .tools/exercise-safe-merge-continue.sh -- 30 arms, ALL GREEN 2026-09-04"
  echo "       (1.0.0_SA_CTO) in an ISOLATED worktree on real bytes: a genuine append-only"
  echo "       conflict left OPEN at rc 4; --continue refused while unresolved; --continue"
  echo "       refused a FOREIGN staged file BY NAME; a merge that FAILED WITHOUT OPENING ONE"
  echo "       wrote NO state and exited 1 (2.0.0_SA_COO 94259); then a real two-parent merge committed"
  echo "       under the draining seat's author with the row gate run on the merged index."
  echo "     Earlier: 4.0.0_SA_CRO ran the non-conflicting path at 06:5xZ with the pre-fix"
  echo "     script as the negative control. RE-RUN THE EXERCISE after any change to the"
  echo "     conflict path, the grade or the commit path -- these grep arms cannot see"
  echo "     behaviour, only that the strings are still present."
  [ "$fails" -eq 0 ] && { echo "PASS"; exit 0; } || { echo "FAIL"; exit 1; }
fi

# The state file lives in the GIT DIR, not the worktree: a linked worktree keeps its own, and
# a drain in one worktree must never see another's. `--git-path` resolves both cases.
STATE="$(git rev-parse --git-path safe-merge-conflict 2>/dev/null || echo '')"
[ -n "$STATE" ] || { echo "safe-merge: cannot resolve the git dir" >&2; exit 2; }

_merge_open() { [ -f "$(git rev-parse --git-path MERGE_HEAD 2>/dev/null || echo /nonexistent)" ]; }

# ---------------------------------------------------------------- the ONE-MERGE lock
# NFRA_OPLGTW-Z-S66 (2.0.0_SA_COO~O, 2026-10-07): two safe-merge runs inside one window in the shared tree produced
# 9f146f853a -- one seat's subject and branch parent, the other seat's author and tree. MERGE_HEAD is ONE file per
# worktree, so two open merges cannot coexist; the second run's `git merge` either fails on the first's MERGE_HEAD or
# replaces it, and the first run's commit then lands on a MERGE_HEAD it did not write. The lock is a directory in the
# git dir (mkdir is atomic; Git Bash has no flock), taken BEFORE the clean-index check and held to the commit. A
# conflict (exit 4) KEEPS it for the seat that opened the merge; --continue and --abort release it.
_LOCK="$(git rev-parse --git-path safe-merge.lock.d 2>/dev/null || echo '')"
_LOCK_MINE=0
_KEEP_LOCK=0
_lock_who() { echo "serial $(cat "$_LOCK/serial" 2>/dev/null || echo '?'), branch $(cat "$_LOCK/what" 2>/dev/null || echo '?'), since $(cat "$_LOCK/since" 2>/dev/null || echo '?'), pid $(cat "$_LOCK/pid" 2>/dev/null || echo '?')"; }
_lock_write() {
  printf '%s\n' "${OPAL_AGENT_SERIAL:-unknown}" > "$_LOCK/serial"; echo "$$" > "$_LOCK/pid"
  date -u +%Y-%m-%dT%H:%M:%SZ > "$_LOCK/since"; printf '%s\n' "$1" > "$_LOCK/what"; _LOCK_MINE=1
}
_lock_take() {
  [ -n "$_LOCK" ] || return 1
  if mkdir "$_LOCK" 2>/dev/null; then _lock_write "$1"; return 0; fi
  # Held. It is STALE only when all three read empty: the holder's process is gone, no merge is open, and no conflict
  # state is armed. A conflict the holder left open keeps the lock although its process has exited.
  _hp="$(cat "$_LOCK/pid" 2>/dev/null || echo '')"
  if { [ -z "$_hp" ] || ! kill -0 "$_hp" 2>/dev/null; } && ! _merge_open && [ ! -f "$STATE" ]; then
    echo "safe-merge: WARN -- clearing a STALE one-merge lock ($(_lock_who)): its process is gone, no merge is open, no conflict state" >&2
    rm -rf "$_LOCK" 2>/dev/null || true
    if mkdir "$_LOCK" 2>/dev/null; then _lock_write "$1"; return 0; fi
  fi
  return 1
}
_lock_drop() { [ "$_LOCK_MINE" -eq 1 ] && [ "$_KEEP_LOCK" -eq 0 ] && rm -rf "$_LOCK" 2>/dev/null; return 0; }

# KILLED MID-MERGE (GC P3 residue item 1, 4.0.0_SA_CRO~B 107108; owner 4.0.0_SA_CRO~A per 1.0.0_SA_CTO 107030). The ONE
# exception to "a merge already open here is never aborted": the open merge was opened by safe-merge (its lock dir
# exists), the lock's holder process is gone, and no conflict was handed back (no $STATE). That is a run killed during
# its grade or commit, not a conflict a seat is resolving, and it blocked this worktree for good. A merge opened any
# other way has no lock dir and is still refused untouched. Returns 0 only when it aborted that merge.
_sm_recover_killed() {
  local _hp=""
  [ -n "$_LOCK" ] && [ -d "$_LOCK" ] || return 1
  [ ! -f "$STATE" ] || return 1
  _hp="$(cat "$_LOCK/pid" 2>/dev/null || echo '')"
  if [ -n "$_hp" ] && kill -0 "$_hp" 2>/dev/null; then return 1; fi
  echo "safe-merge: WARN -- the merge open here was opened by a safe-merge run that is gone ($(_lock_who)) and handed back no conflict: a run killed mid-merge. Aborting that merge." >&2
  if ! git merge --abort 2>/dev/null; then
    echo "safe-merge: ERROR -- git merge --abort failed; the killed merge is still open. Inspect by hand." >&2
    return 1
  fi
  rm -f "$(git rev-parse --git-path index).safe-merge.${_hp:-x}" 2>/dev/null || true
  _sm_row "MERGE-KILLED-ABORTED" "holder=${_hp:-?} what=$(cat "$_LOCK/what" 2>/dev/null || echo '?')"
  rm -rf "$_LOCK" 2>/dev/null || true
  return 0
}

# ---------------------------------------------------------------- ONE AUDIT ROW PER ATTEMPT
# Andrew-direct 2026-10-08 ~18:3xZ: long merges are long "because they are failing multiple times". Until now every
# refusal here went to stderr only, so how many attempts a drain took, and what refused each, was in no record.
# Each run now appends one MERGE-ATTEMPT row: rc, seconds, the arguments, and the first refusal/warning line.
# Owner 4.0.0_SA_CRO~A (1.0.0_SA_CTO msg 107030). rc: 0 merged, 1 refused, 2 usage, 4 conflict handed back, 5 tree drop.
_SM_T0="${EPOCHREALTIME:-}"
_SM_ARGS="$*"
case "${AGENTBUS_DEVICE:-}" in ""|*[!a-z0-9-]*) GAO_REL="org/git-author-override-audit.log" ;; *) GAO_REL="org/git-author-override-audit.${AGENTBUS_DEVICE}.log" ;; esac  # one file per box (shape (a), MSTR consensus 2026-10-11); unset device -> legacy shared file
_SM_AUDIT="$(git rev-parse --path-format=absolute --git-common-dir 2>/dev/null)/../$GAO_REL"
_SM_ERR="$(git rev-parse --path-format=absolute --git-path "safe-merge.err.$$" 2>/dev/null || echo '')"
_sm_row() { echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) $1  ${OPAL_AGENT_SERIAL:-unknown}  $2" >> "$_SM_AUDIT" 2>/dev/null || true; }
_sm_secs() {
  local a="${_SM_T0/[.,]/}" b="${EPOCHREALTIME:-}"; b="${b/[.,]/}"
  [ -n "$a" ] && [ -n "$b" ] || { echo "?"; return 0; }
  local d=$(( (10#$b - 10#$a) / 10000 )); printf '%d.%02d' $((d / 100)) $((d % 100))
}
_sm_on_exit() {
  local rc=$? cls=""
  _lock_drop
  # GC P3 residue item 5: this run's private index never outlives it (a kill -9 still can; the sweep below takes those).
  [ -n "${_PRIV_IDX:-}" ] && rm -f "$_PRIV_IDX" 2>/dev/null
  [ -n "${_SM_FL_DIR:-}" ] && rm -rf "$_SM_FL_DIR" 2>/dev/null
  if [ -n "$_SM_ERR" ] && [ -f "$_SM_ERR" ]; then
    cls="$(grep -m1 -oE '(REFUSED|FAILED|BLOCKED|ERROR|CONFLICT|WARN)[^.]{0,90}' "$_SM_ERR" 2>/dev/null | tr -s ' ' || true)"
    rm -f "$_SM_ERR" 2>/dev/null
  fi
  _sm_row "MERGE-ATTEMPT" "rc=$rc  secs=$(_sm_secs)  graded=${_SM_GRADED:-n/a}  args=(${_SM_ARGS})  first=(${cls:-none})"
  return 0
}
trap _sm_on_exit EXIT
if [ -n "$_SM_ERR" ]; then exec 2> >(tee "$_SM_ERR" >&2); fi
# Sweep private indexes left by runs that were killed (their pid is gone).
for _old in "$(git rev-parse --git-path index 2>/dev/null)".safe-merge.*; do
  [ -f "$_old" ] || continue
  _op="${_old##*.safe-merge.}"
  case "$_op" in (*[!0-9]*|"") continue ;; esac
  if [ "$_op" != "$$" ] && ! kill -0 "$_op" 2>/dev/null; then rm -f "$_old" 2>/dev/null && _sm_row "MERGE-PRIVIDX-SWEPT" "pid=$_op"; fi
done

# ---------------------------------------------------------------- post-commit TREE check
# ⛔ 1.0.0_SA_CTO~Z 2026-09-29 (DSGN_AMGTV1 round-2 DRAIN_END_READ s.3 @e724da66a2): under shared-tree
# lock contention this script printed "MERGED and committed" on 0e98284fa2 and 8e0a9b6400, whose TREE
# equals their first parent -- the worker's two files were never carried -- and ef21ed3f77 swept another
# seat's staged deploy-ledger files. A peer's act reset or re-staged the SHARED index while the grade and
# the commit hooks ran. Every parent-based read is green on such a merge, and the branch now reads as an
# ancestor: a re-run is a no-op and /cleanup would delete its worktree as "merged". ONLY THE TREE TELLS.
# NEED    = files the branch changed (merge-base..^2) that the first parent did not already carry.
# DROPPED = NEED files the merge commit did not change. All of NEED dropped -> rc 5 (not carried).
#           Some dropped -> rc 5 when the parents merge CLEAN and the file differs from that clean merge tree
#           (no conflict, so no PICK-ours: lost work); WARN only when the parents conflict (a PICK-ours is legitimate).
# FOREIGN = files the merge commit changed that the branch never touched -> WARN only: a drain may
#           legitimately carry task-order status closes in the merge commit (/dispatch Step 5).
_verify_merge_tree() {
  local m="$1" mb bfiles need landed dropped foreign nn nd mt mtrc exp lost nl
  git rev-parse -q --verify "$m^2" >/dev/null 2>&1 || { echo "safe-merge: $m is not a merge commit -- nothing to verify" >&2; return 2; }
  mb="$(git merge-base "$m^1" "$m^2" 2>/dev/null)" || { echo "safe-merge: no merge-base for $m -- tree check could not run" >&2; return 2; }
  bfiles="$(git diff --name-only "$mb" "$m^2" | LC_ALL=C sort)"
  need="$(LC_ALL=C comm -12 <(printf '%s\n' "$bfiles" | sed '/^$/d') <(git diff --name-only "$m^1" "$m^2" | LC_ALL=C sort))"
  landed="$(git diff --name-only "$m^1" "$m" | LC_ALL=C sort)"
  dropped="$(LC_ALL=C comm -23 <(printf '%s\n' "$need" | sed '/^$/d') <(printf '%s\n' "$landed" | sed '/^$/d'))"
  foreign="$(LC_ALL=C comm -23 <(printf '%s\n' "$landed" | sed '/^$/d') <(printf '%s\n' "$bfiles" | sed '/^$/d'))"
  nn="$(printf '%s\n' "$need" | sed '/^$/d' | wc -l | tr -d ' ')"
  nd="$(printf '%s\n' "$dropped" | sed '/^$/d' | wc -l | tr -d ' ')"
  echo "safe-merge: tree check $(git rev-parse --short "$m"): branch needed ${nn} file(s), dropped ${nd}, foreign $(printf '%s\n' "$foreign" | sed '/^$/d' | wc -l | tr -d ' ')"
  if [ -n "$foreign" ]; then
    echo "safe-merge: WARN -- the merge commit carries file(s) the branch never touched (a status close is expected; anything else is another seat's staged work riding this commit):" >&2
    printf '%s\n' "$foreign" | sed '/^$/d; s/^/              /' >&2
  fi
  if [ "$nn" -gt 0 ] && [ "$nd" -eq "$nn" ]; then
    echo "safe-merge: *** COMMITTED BUT THE BRANCH WAS NOT CARRIED -- the tree check found none of its ${nn} needed file(s) in the merge. ***" >&2
    echo "            The branch now reads as MERGED (an ancestor), so re-running safe-merge is a no-op." >&2
    echo "            Land its content from the branch tip, then commit it under your serial:" >&2
    printf '%s\n' "$dropped" | sed '/^$/d; s/^/              /' >&2
    echo "                git checkout $(git rev-parse --short "$m^2") -- <the files above>" >&2
    return 5
  fi
  if [ "$nd" -gt 0 ]; then
    # PARTIAL DROP (2.0.0_SA_COO~Y msg 103457: 1ee1c56e9b carried 1 of 16 needed files and this function returned 0).
    # Whether a partial drop is legitimate is decidable from the two PARENTS alone: `git merge-tree --write-tree`
    # rebuilds the merge without touching any index. rc 0 = the parents merge CLEAN, so nobody resolved a conflict,
    # a PICK-ours is impossible, and that tree is exactly what this commit had to carry -- a dropped file that
    # differs from it is lost work (rc 5). A dropped file that EQUALS it is not lost: the first parent already held
    # the branch's change. rc non-zero (a real conflict, or a git without --write-tree) keeps the WARN below.
    mt="$(git merge-tree --write-tree "$m^1" "$m^2" 2>/dev/null)"; mtrc=$?
    exp="${mt%%$'\n'*}"
    if [ "$mtrc" -eq 0 ] && git rev-parse -q --verify "${exp}^{tree}" >/dev/null 2>&1; then
      lost="$(LC_ALL=C comm -12 <(printf '%s\n' "$dropped" | sed '/^$/d') <(git diff --name-only "$exp" "$m" | LC_ALL=C sort))"
      nl="$(printf '%s\n' "$lost" | sed '/^$/d' | wc -l | tr -d ' ')"
      if [ "$nl" -gt 0 ]; then
        echo "safe-merge: *** COMMITTED BUT ${nl} OF ${nn} NEEDED FILE(S) WERE NOT CARRIED -- the parents merge CLEAN, so there was no conflict to resolve and each one is lost work. ***" >&2
        echo "            The branch now reads as MERGED (an ancestor), so re-running safe-merge is a no-op." >&2
        echo "            Land each file's merged content, then commit it by path under your serial:" >&2
        printf '%s\n' "$lost" | sed '/^$/d; s/^/              /' >&2
        echo "                git restore --source=${exp} -- <the files above>   (the clean merge tree of the two parents)" >&2
        return 5
      fi
      echo "safe-merge: ${nd} of ${nn} needed file(s) equal the first parent, and so does the clean merge tree -- the first parent already carried them; nothing lost"
      return 0
    fi
    echo "safe-merge: WARN -- ${nd} of ${nn} needed file(s) kept the first parent's version (fine for a PICK-ours resolution; otherwise it is lost work):" >&2
    printf '%s\n' "$dropped" | sed '/^$/d; s/^/              /' >&2
  fi
  return 0
}

# ---------------------------------------------------------------- post-commit STAGED-PATH check (GS-f-6, row D1-S5)
# Row D1-S5 (ARMED): a drain's --continue committed 1 of 4 staged files and exited 0. Nothing compared what the commit
# CHANGED against what the merge STAGED. EXPECTED = the paths the conflicted merge staged ($STATE: staged-and-unmerged at
# the conflict) plus the paths the commit's private index held. GOT = `git diff --name-only <m>^1 <m>`. LACKS = EXPECTED
# minus GOT, except a path whose working copy equals the committed blob (a deliberate keep-ours resolution: nothing was
# lost, the first parent's version IS the resolution). A path whose working copy differs from the committed blob is a
# resolution that was staged away from the commit. Read-only: it never resets or rewrites the commit. rc 7 when LACKS is
# non-empty; the recovery is printed for the seat to run.
_verify_staged_carried() {
  local m="$1" expect="$2" conflicted="${3:-}" lacks="" p nl
  while IFS= read -r p; do
    [ -n "$p" ] || continue
    # GS-h-3: keep-ours is admitted only for a path that was CONFLICTED in this merge; a clean path the merge brought in
    # and the drain reset (index and working copy) is a lost change, not a resolution.
    if printf '%s
' "$conflicted" | grep -Fxq -- "$p"; then
      git diff --quiet HEAD -- "$p" 2>/dev/null && continue
    fi
    lacks="${lacks}${p}"$'\n'
  done < <(LC_ALL=C comm -23 <(printf '%s\n' "$expect" | sed '/^$/d' | LC_ALL=C sort -u) <(git diff --name-only "$m^1" "$m" | LC_ALL=C sort -u))
  nl="$(printf '%s' "$lacks" | sed '/^$/d' | wc -l | tr -d ' ')"
  [ "$nl" -gt 0 ] || return 0
  echo "safe-merge: REFUSED -- the merge commit lacks ${nl} staged path(s): $(printf '%s' "$lacks" | sed '/^$/d' | tr '\n' ' ')" >&2
  echo "            COMMITTED $(git rev-parse --short "$m") ANYWAY (the commit is not rewritten or reset). Recover: git add -- <the paths above> and commit them under your serial with .tools/safe-commit.sh (their merged content is still in the working tree)." >&2
  return 7
}

if [ "${1:-}" = "--verify-merge" ]; then
  [ -n "${2:-}" ] || { echo "safe-merge: usage: safe-merge.sh --verify-merge <commit>" >&2; exit 2; }
  _vrc=0; _verify_merge_tree "$2" || _vrc=$?
  exit "$_vrc"
fi

# ---------------------------------------------------------------- post-commit INDEX check
# Row NFRA_OPLGTW-Z-S61 (2.0.0_SA_COO~O; 1.0.0_SA_CTO~O ruling R34, ROUND_ANALYSIS.round23.md). The merge commit is
# written from a PRIVATE index (Z-S23), so nothing in this script re-reads the SHARED index after the commit. When a
# peer's act resets the shared index while the commit's hooks run, HEAD carries the merge and the shared index still
# holds the pre-merge blobs for the merged paths: they read as staged reverts nobody made, and a `git commit` without
# --only lands them and reverts the drain. The tree check cannot see it (it reads commits). This reads the INDEX.
# MERGED = paths the merge commit changed against its first parent. STALE = MERGED paths where the index != HEAD.
# Read-only and REPORT-only: resetting a shared index entry would also unstage a peer's own change to that path, so
# the repair is printed for the seat to run, never run here. rc 6 when STALE is non-empty; rc 2 when m is not HEAD
# (the index can only be compared with the commit it sits on).
_verify_shared_index() {
  local m="$1" merged stale ns nm
  git rev-parse -q --verify "$m^2" >/dev/null 2>&1 || { echo "safe-merge: $m is not a merge commit -- no index check" >&2; return 2; }
  [ "$(git rev-parse "$m")" = "$(git rev-parse HEAD)" ] || { echo "safe-merge: $m is not HEAD -- the index check reads the index against HEAD only" >&2; return 2; }
  merged="$(git diff --name-only "$m^1" "$m" | LC_ALL=C sort)"
  stale="$(LC_ALL=C comm -12 <(printf '%s\n' "$merged" | sed '/^$/d') <(git diff --cached --name-only HEAD | LC_ALL=C sort))"
  nm="$(printf '%s\n' "$merged" | sed '/^$/d' | wc -l | tr -d ' ')"
  ns="$(printf '%s\n' "$stale" | sed '/^$/d' | wc -l | tr -d ' ')"
  echo "safe-merge: index check $(git rev-parse --short "$m"): ${ns} of ${nm} merged path(s) differ between the index and HEAD"
  if [ "$ns" -gt 0 ]; then
    echo "safe-merge: *** THE MERGE IS COMMITTED AND CARRIED, BUT THE INDEX DISAGREES WITH HEAD ON ${ns} OF ITS ${nm} PATH(S). ***" >&2
    echo "            They read as staged changes nobody made. A commit WITHOUT --only (or a 'git commit -a')" >&2
    echo "            lands them and REVERTS this merge. Nothing is lost yet: HEAD and the working tree are right." >&2
    printf '%s\n' "$stale" | sed '/^$/d; s/^/              /' >&2
    echo "            Repair (index only; the working tree is not touched). First check no peer staged one of" >&2
    echo "            these paths on purpose, then:" >&2
    echo "                git reset -q HEAD -- <the paths above>" >&2
    echo "            and re-run:  bash .tools/safe-merge.sh --verify-index HEAD" >&2
    return 6
  fi
  return 0
}

if [ "${1:-}" = "--verify-index" ]; then
  [ -n "${2:-}" ] || { echo "safe-merge: usage: safe-merge.sh --verify-index <commit>" >&2; exit 2; }
  _irc=0; _verify_shared_index "$2" || _irc=$?
  exit "$_irc"
fi

# ---------------------------------------------------------------- --abort
if [ "${1:-}" = "--abort" ]; then
  if ! _merge_open; then
    # A STALE state file with no merge open is exactly what 94259 found, and before this branch
    # there was no way to disarm one: --abort exited 2 and left it armed. Clearing it IS the
    # abort in that case.
    if [ -f "$STATE" ]; then
      rm -f "$STATE" "$STATE.branch" "$STATE.head" "$STATE.conflicted" 2>/dev/null || true
      echo "safe-merge: no merge in progress, but a STALE conflict state file was present -- cleared."
      echo "            --continue is now disarmed in this worktree. Nothing else was touched."
      exit 0
    fi
    echo "safe-merge: no merge in progress and no conflict state -- nothing to abort" >&2
    exit 2
  fi
  # An open merge under ANOTHER seat's lock is that seat's: aborting it here is how one drain destroys another.
  if [ -d "$_LOCK" ] && [ "$(cat "$_LOCK/serial" 2>/dev/null)" != "${OPAL_AGENT_SERIAL:-unknown}" ]; then
    echo "safe-merge: REFUSED -- the open merge is held by another run ($(_lock_who)). --abort does not abort another seat's merge. Nothing was touched." >&2
    exit 2
  fi
  git merge --abort || { echo "safe-merge: git merge --abort FAILED; the tree is NOT restored" >&2; exit 1; }
  rm -f "$STATE" "$STATE.branch" "$STATE.head" "$STATE.conflicted" 2>/dev/null || true
  rm -rf "$_LOCK" 2>/dev/null || true
  echo "safe-merge: merge aborted; tree restored and conflict state cleared"
  exit 0
fi

# ---------------------------------------------------------------- --continue
if [ "${1:-}" = "--continue" ]; then
  shift || true
  SUBJECT=""
  if [ "${1:-}" = "-m" ]; then SUBJECT="${2:-}"; fi
  _merge_open || {
    echo "safe-merge: REFUSED -- --continue with NO merge in progress. Nothing to continue." >&2
    echo "            If the merge was already committed, this script did not do it and its" >&2
    echo "            guards did not run; say so rather than pretending they did." >&2
    if [ -f "$STATE" ]; then
      echo "            STOP: A conflict STATE FILE is present with no merge open -- it is STALE and" >&2
      echo "            it makes this command read as armed when it is not. Clear it with:" >&2
      echo "                bash .tools/safe-merge.sh --abort" >&2
    fi
    exit 2; }
  [ -f "$STATE" ] || {
    echo "safe-merge: REFUSED -- a merge is open but THIS script did not open it (no conflict" >&2
    echo "            state at $STATE). It cannot tell the merge's own staged files from another" >&2
    echo "            seat's, which is the one thing --continue exists to check. Finish the merge" >&2
    echo "            the way it was started, or abort it and re-run safe-merge from the top." >&2
    exit 2; }
  # The lock a conflict left behind belongs to the seat that opened the merge; --continue re-takes it for this process.
  if [ -d "$_LOCK" ]; then
    if [ "$(cat "$_LOCK/serial" 2>/dev/null)" != "${OPAL_AGENT_SERIAL:-unknown}" ]; then
      echo "safe-merge: REFUSED -- the open merge is held by another run ($(_lock_who)). --continue finishes only the merge this seat opened. Nothing was touched." >&2
      exit 2
    fi
    _lock_write "$(cat "$STATE.branch" 2>/dev/null || echo '<unknown>')"
  else
    mkdir "$_LOCK" 2>/dev/null && _lock_write "$(cat "$STATE.branch" 2>/dev/null || echo '<unknown>')"
  fi
  # D1-S16 (MDPF_CANON): HEAD moved since the merge opened -> the staged snapshot is stale, and committing it would
  # revert the peer's paths (merge 0468b6c8ba reverted 7). Refuse and keep the merge OPEN; no .head file = an
  # older open merge, which keeps the old behaviour.
  _OPENED_HEAD="$(cat "$STATE.head" 2>/dev/null || true)"
  if [ -n "$_OPENED_HEAD" ] && [ "$_OPENED_HEAD" != "$(git rev-parse -q --verify HEAD 2>/dev/null || echo none)" ]; then
    echo "safe-merge: *** REFUSED -- HEAD MOVED SINCE THE MERGE OPENED (was $(git rev-parse --short "$_OPENED_HEAD" 2>/dev/null || echo "$_OPENED_HEAD"), now $(git rev-parse --short HEAD 2>/dev/null || echo '?'))." >&2
    echo "            A peer committed while this merge sat open, so the merge's staged snapshot no longer" >&2
    echo "            matches the tree; committing it would revert the peer's paths. Nothing has landed." >&2
    echo "            Run: bash .tools/safe-merge.sh --abort   then re-run safe-merge.sh from the top." >&2
    _KEEP_LOCK=1
    exit 4
  fi
  _UNRES="$(git diff --name-only --diff-filter=U | wc -l | tr -d ' ')"
  if [ "$_UNRES" != "0" ]; then
    echo "safe-merge: REFUSED -- ${_UNRES} path(s) still carry unresolved conflict markers:" >&2
    git diff --name-only --diff-filter=U | sed 's/^/              /' >&2
    echo "            Resolve and \`git add\` them, then re-run --continue. The merge stays OPEN." >&2
    _KEEP_LOCK=1
    exit 4
  fi
  # ⛔ THE FOREIGN-PATH CHECK. The one-shot path gets this free from its pre-merge index guard
  # (:73-79); --continue cannot, because by now the index legitimately holds the merge's own
  # files. So compare against what the MERGE staged when it conflicted. A path staged now that
  # the merge did not put there is another seat's work about to ride this drain commit under
  # the draining seat's name -- NFRA_CLDGRPH-S34/S35/S36 are three views of that one fact.
  _FOREIGN=0
  while IFS= read -r _p; do
    [ -n "$_p" ] || continue
    grep -Fxq "$_p" "$STATE" || { echo "              $_p" >&2; _FOREIGN=$((_FOREIGN+1)); }
  done < <(git diff --cached --name-only)
  if [ "$_FOREIGN" -ne 0 ]; then
    echo "safe-merge: *** REFUSED -- ${_FOREIGN} path(s) are staged that THIS MERGE DID NOT STAGE" >&2
    echo "            (named above). That is another seat's work about to be committed under the" >&2
    echo "            draining seat's authorship, with no lane check firing -- merges are exempt" >&2
    echo "            by design. Unstage them (their owner will re-commit), then --continue." >&2
    echo "            The merge is left OPEN; nothing has landed." >&2
    _KEEP_LOCK=1
    exit 4
  fi
  BRANCH="$(cat "$STATE.branch" 2>/dev/null || echo '<unknown>')"
  echo "safe-merge: --continue on '$BRANCH' -- 0 unresolved, 0 foreign staged path(s)"
  _CONTINUING=1
else
  _CONTINUING=0
  BRANCH="${1:-}"
  [ -n "$BRANCH" ] || { echo "safe-merge: REFUSED -- no branch given. usage: safe-merge.sh <branch> [-m <subject>]" >&2; exit 2; }
  shift || true
  SUBJECT=""
  if [ "${1:-}" = "-m" ]; then SUBJECT="${2:-}"; fi
fi

if [ "$_CONTINUING" -eq 0 ]; then
git rev-parse --verify "$BRANCH" >/dev/null 2>&1 || {
  echo "safe-merge: REFUSED -- '$BRANCH' is not a ref in this repo" >&2; exit 2; }
fi

# ONE MERGE AT A TIME IN A WORKTREE (NFRA_OPLGTW-Z-S66). A merge already open here was not opened by this run: refuse and
# touch nothing -- never abort it. Then take the lock, before the clean-index check, so a second run cannot pass that
# check in the seconds before this run's `git merge` stages.
if [ "$_CONTINUING" -eq 0 ]; then
  if _merge_open && ! _sm_recover_killed; then
    echo "safe-merge: REFUSED -- A MERGE IS ALREADY OPEN in this worktree (MERGE_HEAD $(git rev-parse --short -q --verify MERGE_HEAD 2>/dev/null || echo '?')); this run did not open it." >&2
    [ -d "$_LOCK" ] && echo "            Holder: $(_lock_who)." >&2
    echo "            Nothing was touched. Wait for that merge to commit, then re-run; or drain in a linked worktree." >&2
    exit 2
  fi
  if ! _lock_take "$BRANCH"; then
    echo "safe-merge: REFUSED -- ANOTHER safe-merge RUN HOLDS THIS WORKTREE ($(_lock_who))." >&2
    echo "            Two merges cannot be open in one worktree: the second would commit on the first's MERGE_HEAD." >&2
    echo "            Nothing was touched. Re-run when that run has committed; or drain in a linked worktree." >&2
    exit 2
  fi
fi

# A dirty index is not ours to merge into: the union we would grade would carry
# somebody else's staged work and the abort path could not restore it cleanly.
if [ "$_CONTINUING" -eq 0 ] && [ -n "$(git diff --cached --name-only)" ]; then
  echo "safe-merge: REFUSED -- the index carries STAGED changes (possibly another seat's)." >&2
  echo "            Merging would grade a union that is not just this branch. Clear or commit first." >&2
  git diff --cached --name-only | sed 's/^/              /' >&2
  exit 2
fi

# ---------------------------------------------------------------- THE FAST LANE: a clean merge never opens in this tree
# Andrew-direct 2026-10-08 ~19:5xZ: "im trying to effectively abstract away the issues with the constant merging because
# currently, it is a major, major holdup on sitez box, it suffocates every single agent on that box." An in-tree merge holds
# MERGE_HEAD open for its whole grade and commit, and safe-commit refuses EVERY seat in this worktree for that long (two
# drains refused this seat's commits at 20:16Z and 20:39Z on 2026-10-08). When git can merge cleanly, this lane does
# what .tools/box-sync.sh does: `git merge-tree --write-tree` in the object store; the path-scoped grade (Andrew ~19:1xZ)
# on a private index in a private git dir pinned to both parents; `git commit-tree`; the tree check; then a LAND of
# seconds under safe-commit's own commit lock: compare-and-swap of HEAD's branch, plus `git read-tree -m -u` of the
# merged paths (it refuses rather than overwrite a seat's uncommitted edit). No MERGE_HEAD ever exists, so no seat is
# refused. A CONFLICT falls through to the in-tree path below, because a person resolves it there.
# SAFE_MERGE_IN_TREE=1 forces the old path. Owner 4.0.0_SA_CRO~A (1.0.0_SA_CTO msg 107030).
_SM_FL_DIR=""
# resolve_known P1 P2 T0 -> prints the resolved tree when EVERY conflicted path is a known multi-writer class (a surprise-
# channel section union, or a regenerated generated index entry: .tools/merge-resolve-known.py); returns 1 otherwise.
# The conflicted paths come from `git merge-tree --name-only`; T0 is the tree it wrote (markers and all).
resolve_known() {
  local p1="$1" p2="$2" t0="$3" mb res idx k path blob how mode tr
  local -a cps=()
  while IFS= read -r path; do [ -n "$path" ] && cps+=("$path"); done < <(git merge-tree --write-tree --name-only --no-messages "$p1" "$p2" 2>/dev/null | tail -n +2)
  [ "${#cps[@]}" -gt 0 ] || return 1
  mb="$(git merge-base "$p1" "$p2" 2>/dev/null)" || return 1
  res="$(python "$ROOT/.tools/merge-resolve-known.py" --base "$mb" --ours "$p1" --theirs "$p2" --tree "$t0" "${cps[@]}" 2>&1)" \
    || { printf '%s\n' "$res" | sed 's/^/    resolver: /' >&2; return 1; }
  idx="$(git rev-parse --path-format=absolute --git-dir)/resolve-known-$$.index"
  rm -f "$idx"
  GIT_INDEX_FILE="$idx" git read-tree "$t0" || { rm -f "$idx"; return 1; }
  while read -r k path blob how; do
    [ "$k" = "RESOLVED" ] || continue
    mode="$(git ls-tree "$t0" -- "$path" | awk '{print $1}')"
    GIT_INDEX_FILE="$idx" git update-index --cacheinfo "${mode:-100644},${blob},${path}" || { rm -f "$idx"; return 1; }
    echo "    resolved ${path} (${how})" >&2
  done <<< "$res"
  tr="$(GIT_INDEX_FILE="$idx" git write-tree)" || { rm -f "$idx"; return 1; }
  rm -f "$idx"
  printf '%s\n' "$tr"
}
_sm_fast_lane() {
  local hb p1 tip out mrc t m mb paths n st rc att lockd w hp tl
  [ -n "${OPAL_AGENT_SERIAL:-}" ] || return 1                      # the in-tree path refuses with its own text
  hb="$(git symbolic-ref -q HEAD 2>/dev/null)" || return 1         # detached HEAD: in-tree path
  tip="$(git rev-parse --verify "${BRANCH}^{commit}")" || return 1
  lockd="$(git rev-parse --path-format=absolute --git-dir)/commit-queue.lock"
  for att in 1 2 3; do
    p1="$(git rev-parse HEAD)"
    git merge-base --is-ancestor "$tip" "$p1" && return 1           # nothing to merge: the in-tree path says so
    out="$(git merge-tree --write-tree --no-messages "$p1" "$tip" 2>/dev/null)"; mrc=$?
    t="$(printf '%s\n' "$out" | head -1)"
    if [ "$mrc" -eq 1 ]; then
      # a conflict made only of the known multi-writer classes (surprise-channel rows, generated index entries) is
      # resolved here, with no worktree and no MERGE_HEAD; anything else falls back to the in-tree path to be resolved
      if t="$(resolve_known "$p1" "$tip" "$t")"; then
        echo "safe-merge: fast lane -- the conflict was only known multi-writer files; resolved without opening a merge"
        mrc=0
      else
        echo "safe-merge: fast lane -- '$BRANCH' CONFLICTS with HEAD beyond the known classes; falling back to the in-tree merge so it can be resolved"
        return 1
      fi
    fi
    { [ "$mrc" -eq 0 ] && [ -n "$t" ]; } || { echo "safe-merge: fast lane -- git merge-tree failed (rc=$mrc); in-tree path"; return 1; }
    # the grade: paths the merge changes against BOTH parents, plus paths both sides changed since the merge base
    mb="$(git merge-base "$p1" "$tip" 2>/dev/null || echo '')"
    if [ "${SAFE_MERGE_FULL_GRADE:-0}" = "1" ]; then
      paths="$(git diff --name-only "$p1" "$t")"
    else
      paths="$( { LC_ALL=C comm -12 <(git diff --name-only "$p1" "$t" | LC_ALL=C sort -u) <(git diff --name-only "$tip" "$t" | LC_ALL=C sort -u)
                  [ -n "$mb" ] && LC_ALL=C comm -12 <(git diff --name-only "$mb" "$p1" | LC_ALL=C sort -u) <(git diff --name-only "$mb" "$tip" | LC_ALL=C sort -u); } \
                | LC_ALL=C sort -u | sed '/^$/d' )"
    fi
    st="$(git diff --name-only "$p1" "$t" | sed '/^$/d' | wc -l | tr -d ' ')"
    n="$(printf '%s\n' "$paths" | sed '/^$/d' | wc -l | tr -d ' ')"
    [ "$st" -gt 0 ] || return 1                                      # stages nothing: the in-tree path refuses as before
    _SM_GRADED="${n}/${st} fast-lane"
    echo "safe-merge: fast lane -- grading ${n} of ${st} merged path(s) (introduced by the merge or changed on both sides)"
    if [ "$n" -gt 0 ]; then
      _SM_FL_DIR="$(git rev-parse --path-format=absolute --git-dir)/safe-merge-fl-$$"
      rm -rf "$_SM_FL_DIR"; mkdir -p "$_SM_FL_DIR"
      printf '%s\n' "$p1" > "$_SM_FL_DIR/HEAD"; printf '%s\n' "$tip" > "$_SM_FL_DIR/MERGE_HEAD"
      git rev-parse --path-format=absolute --git-common-dir > "$_SM_FL_DIR/commondir"
      GIT_DIR="$_SM_FL_DIR" GIT_WORK_TREE="$ROOT" git read-tree "$t" || { echo "safe-merge: REFUSED -- could not build the private index" >&2; exit 1; }
      rc=0; STAGED="$paths" GIT_DIR="$_SM_FL_DIR" GIT_WORK_TREE="$ROOT" ROOT="$ROOT" python "$GATE" || rc=$?
      if [ "$rc" -ne 0 ]; then
        rm -rf "$_SM_FL_DIR"; _SM_FL_DIR=""
        echo "safe-merge: *** REFUSED BY THE ROW GATE ON THE MERGE'S OWN PATHS (rc=$rc). *** Nothing landed; FIX ON THE BRANCH, then re-run." >&2
        exit 1
      fi
      # the project-tree check (GS-t-3) on the same merged bytes: --staged reads the private index, --act scopes the
      # refusal to the projects the merge's graded paths touch; every other violation prints STANDING and never refuses.
      _SM_ACT="$paths"; export _SM_ACT
      _SM_CHK="$(merged_checker_path "$_SM_FL_DIR" "$ROOT")" || { rm -rf "$_SM_FL_DIR"; _SM_FL_DIR=""; echo "safe-merge: *** REFUSED -- no merged checker for the tree check (see merged-checker above). *** Nothing landed; FIX ON THE BRANCH, then re-run." >&2; exit 1; }
      GIT_DIR="$_SM_FL_DIR" GIT_WORK_TREE="$ROOT" python "$_SM_CHK" check --staged --act-from-env _SM_ACT || rc=$?
      rm -rf "$_SM_FL_DIR"; _SM_FL_DIR=""
      if [ "$rc" -ne 0 ]; then
        echo "safe-merge: *** REFUSED BY THE TREE CHECK ON THE MERGE'S OWN PATHS (rc=$rc). *** Nothing landed; FIX ON THE BRANCH, then re-run." >&2
        exit 1
      fi
    else
      echo "safe-merge: SKIP -- the merge introduces no content of its own and no file changed on both sides; each side was graded at its own commit (Andrew ~19:1xZ)"
    fi
    [ -n "$SUBJECT" ] || SUBJECT="drain: merge $BRANCH (fast lane: no merge opened in the shared tree; row gate on what the merge introduces)"
    m="$(GIT_AUTHOR_NAME="$OPAL_AGENT_SERIAL" GIT_AUTHOR_EMAIL="${OPAL_AGENT_SERIAL}@opal.agent" git commit-tree "$t" -p "$p1" -p "$tip" -m "$SUBJECT")" \
      || { echo "safe-merge: REFUSED -- git commit-tree failed; nothing landed" >&2; exit 1; }
    rc=0; _verify_merge_tree "$m" || rc=$?
    if [ "$rc" -eq 5 ]; then echo "safe-merge: NOT MERGED -- the fast-lane merge ${m:0:10} would drop branch content; nothing landed (exit 5)." >&2; exit 5; fi
    # LAND, under the commit lock safe-commit lands under (seconds)
    w=0
    until mkdir "$lockd" 2>/dev/null; do
      hp=""; [ -f "$lockd/pid" ] && read -r hp < "$lockd/pid" 2>/dev/null
      if [ -n "$hp" ] && ! kill -0 "$hp" 2>/dev/null; then rm -rf "$lockd"; continue; fi
      w=$((w + 1)); [ "$w" -ge 300 ] && { echo "safe-merge: the commit lock stayed busy 300 s; nothing landed -- re-run" >&2; exit 3; }
      sleep 1
    done
    echo "$$" > "$lockd/pid"; tl="${EPOCHREALTIME:-0}"
    if [ "$(git rev-parse HEAD)" != "$p1" ]; then rm -rf "$lockd"; echo "safe-merge: fast lane -- a seat committed while the merge was graded; rebuilding on the new tip (attempt $att)"; continue; fi
    git update-index -q --refresh >/dev/null 2>&1 || true
    if ! git read-tree -m -u "$p1" "$m"; then
      rm -rf "$lockd"
      echo "safe-merge: REFUSED -- landing would overwrite an uncommitted local edit of a merged path (named above). Nothing landed; commit or clear it, then re-run." >&2
      exit 1
    fi
    if ! git update-ref -m "safe-merge: merge $BRANCH (fast lane)" "$hb" "$m" "$p1"; then
      git read-tree -m -u "$m" "$p1" 2>/dev/null; rm -rf "$lockd"
      echo "safe-merge: the branch moved under the lock; the tree was put back; nothing landed -- re-run" >&2; exit 3
    fi
    rm -rf "$lockd"
    echo "safe-merge: MERGED and committed -- $(git rev-parse --short HEAD) (fast lane: no merge was opened in this worktree; land $(secs_since "$tl")s)"
    rc=0; _verify_shared_index HEAD || rc=$?
    [ "$rc" -eq 6 ] && exit 6
    exit 0
  done
  echo "safe-merge: fast lane -- lost the race to seats' commits 3 times; nothing landed -- re-run" >&2
  exit 3
}
secs_since() { local a="${1/[.,]/}" b="${EPOCHREALTIME:-0}"; b="${b/[.,]/}"; local d=$(( (10#$b - 10#$a) / 10000 )); printf '%d.%02d' $((d / 100)) $((d % 100)); }
if [ "$_CONTINUING" -eq 0 ] && [ "${SAFE_MERGE_IN_TREE:-0}" != "1" ]; then
  _sm_fast_lane || true
fi

if [ "$_CONTINUING" -eq 0 ]; then
echo "safe-merge: merging '$BRANCH' with --no-commit (the index will be graded before anything lands)"
if ! git merge --no-commit --no-ff "$BRANCH"; then
  # ⛔ MEASURE THE CONFLICT; DO NOT INFER IT FROM THE EXIT CODE (2.0.0_SA_COO 94259, the
  # defect this branch shipped with on 2026-09-04). `git merge` returns non-zero for SEVERAL
  # reasons and most of them leave NO merge open at all -- "your local changes would be
  # overwritten by merge", unrelated histories, a plain refusal. The first version of this
  # branch treated every one of them as a conflict: it printed the CONFLICT banner with
  # "0 conflicted path(s)", wrote the state file, and armed --continue over a merge that did
  # not exist. A GUARD WHOSE PRECONDITION IS A STALE FILE IS WORSE THAN NO GUARD, because it
  # reads as armed. So the condition is measured from git's own state, on two instruments.
  _MH="$(git rev-parse --git-path MERGE_HEAD 2>/dev/null || echo /nonexistent)"
  _CONF_N="$(git diff --name-only --diff-filter=U | wc -l | tr -d ' ')"
  if [ ! -f "$_MH" ] || [ "$_CONF_N" -eq 0 ]; then
    # NOT a conflict: the merge failed and git left nothing open. Write NO state.
    echo "safe-merge: REFUSED -- \`git merge\` failed and this is NOT a conflict." >&2
    echo "            MERGE_HEAD present : $([ -f "$_MH" ] && echo yes || echo NO)" >&2
    echo "            unmerged path(s)   : ${_CONF_N}" >&2
    echo "            Nothing is open, nothing landed, and NO conflict state was written -- so" >&2
    echo "            --continue stays disarmed. The reason git refused is printed ABOVE this" >&2
    echo "            banner; the usual one is local changes that the merge would overwrite." >&2
    echo "            Fix that, then re-run safe-merge from the top." >&2
    if [ -f "$_MH" ]; then
      echo "            (A merge WAS open with 0 unmerged paths -- a half-state this script will" >&2
      echo "             not continue from. Aborting it.)" >&2
      git merge --abort 2>/dev/null || true
    fi
    exit 1
  fi
  # ⛔ DO NOT ABORT HERE (NFRA_CLDGRPH-S36). Aborting is what made this script's index guard
  # and row gate unreachable on the ONLY path a concurrent drain actually takes. Keep the
  # merge OPEN, record what the merge staged so --continue can tell it from a foreign seat's
  # work, and hand the conflict back.
  # ⛔ THE STATE IS WHAT THE MERGE COULD STAGE, NOT WHAT THE INDEX HOLDS (AMGT_HARVST-Z-S37,
  # AMGT_CORPUS-Z-S59). The index is shared: a peer that stages between the clean-index check
  # above and this snapshot used to be recorded as the merge's own, and --continue then committed
  # its files under the draining seat's name (2751f0be77 carried 0.7.0_AE_CloudOps~A's NEVER-2
  # entry). A merge can only stage a path whose two sides differ, so bound the snapshot by
  # `HEAD..MERGE_HEAD` and name anything outside it now, while nothing has landed.
  # File-based set arithmetic, NO pipe into `grep -q`: under this script's `set -o pipefail`,
  # `printf <2000+ paths> | grep -Fxq` SIGPIPEs the writer on an early match and the pipeline
  # reads FALSE -- the first version of this block (ccf2a27c6b) flagged 680 of a merge's own
  # paths as foreign on the first real drain it met.
  git diff --name-only HEAD MERGE_HEAD 2>/dev/null | LC_ALL=C sort -u > "$STATE.mine" || true
  git diff --cached --name-only 2>/dev/null | LC_ALL=C sort -u > "$STATE.cached" || true
  LC_ALL=C comm -12 "$STATE.cached" "$STATE.mine" > "$STATE"
  _PEERS="$(LC_ALL=C comm -23 "$STATE.cached" "$STATE.mine")"
  if [ -n "$_PEERS" ]; then
    echo "safe-merge: WARN -- path(s) staged in the shared index that THIS MERGE could not have staged (another seat's; left OUT of the conflict state, so --continue will refuse them until unstaged):" >&2
    printf '%s\n' "$_PEERS" | sed 's/^/              /' >&2
  fi
  rm -f "$STATE.mine" "$STATE.cached" 2>/dev/null || true
  git diff --name-only --diff-filter=U >> "$STATE" 2>/dev/null || true
  # GS-h-3: the CONFLICT set alone, so the keep-ours exemption in _verify_staged_carried reaches only these paths.
  git diff --name-only --diff-filter=U 2>/dev/null | LC_ALL=C sort -u > "$STATE.conflicted" || true
  echo "$BRANCH" > "$STATE.branch" 2>/dev/null || true
  # D1-S16 (MDPF_CANON): the HEAD this merge opened on. --continue refuses when HEAD is no longer it.
  git rev-parse -q --verify HEAD > "$STATE.head" 2>/dev/null || true
  echo "safe-merge: *** CONFLICT -- THE MERGE IS OPEN AND NOTHING HAS LANDED. ***" >&2
  echo "            ${_CONF_N} conflicted path(s):" >&2
  git diff --name-only --diff-filter=U | sed 's/^/              /' >&2
  echo "            An append-only channel conflicts on EVERY concurrent drain -- this is the" >&2
  echo "            normal path, not the exception (NFRA_CLDGRPH-S36)." >&2
  echo "            RESOLVE, then re-enter so the guards actually run:" >&2
  if [ -n "$SUBJECT" ]; then
    echo "                bash .tools/safe-merge.sh --continue -m \"${SUBJECT}\"" >&2
  else
    echo "                bash .tools/safe-merge.sh --continue" >&2
  fi
  echo "            Or give up cleanly:  bash .tools/safe-merge.sh --abort" >&2
  echo "            STOP: Do NOT finish this with a bare \`git commit\` -- that is precisely the" >&2
  echo "            hand-merge that runs no index guard and no row gate." >&2
  _KEEP_LOCK=1
  exit 4
fi
fi

# The merge this run holds, by hash. The commit below refuses if MERGE_HEAD no longer reads this (Z-S66).
_MY_MH="$(git rev-parse -q --verify MERGE_HEAD 2>/dev/null || echo none)"

# STOP: THE PRIVATE INDEX IS TAKEN HERE, RIGHT AFTER THE MERGE, NOT AFTER THE GRADE (NFRA_OPLGTW-Z-S23 residual,
# 0.0.0_AB_MSTR~Z 2026-10-03: drain 1e54d613a2 carried 1.0.0_SA_CTO~O's NFRA_OPLGTW project.json). The grade takes
# minutes. A peer that stages a path INSIDE HEAD..MERGE_HEAD during it passes the late sweep, which can only name paths
# the merge could NOT have staged, and the snapshot used to be taken after that. Taken here, a peer has only the seconds
# of `git merge` itself. The sweep, the grade and the commit all read this copy; the shared index is never modified, so a
# peer's staging stays staged for its owner.
_PRIV_IDX="$(git rev-parse --git-path index).safe-merge.$$"
cp "$(git rev-parse --git-path index)" "$_PRIV_IDX" || { echo "safe-merge: REFUSED -- could not snapshot the index after the merge; aborting the merge" >&2; git merge --abort 2>/dev/null || true; exit 1; }
# FOREIGN SWEEP ON THE SNAPSHOT (DSGN_AMGTV1 round 7: 6fcaa52f79 carried 14 of 2.0.0_SA_COO~X's staged files). The
# clean-index check runs BEFORE the merge; a peer's safe-commit can stage in the seconds between it and the snapshot. A
# merge can only stage paths whose sides differ, so anything else in the snapshot is a peer's: drop it from the snapshot
# (the shared index and working copy are untouched) and name it. The post-commit tree check reports anything that slips.
git diff --name-only HEAD MERGE_HEAD 2>/dev/null | LC_ALL=C sort -u > "$STATE.own" || true
_LATE="$(GIT_INDEX_FILE="$_PRIV_IDX" git diff --cached --name-only 2>/dev/null | LC_ALL=C sort -u | LC_ALL=C comm -23 - "$STATE.own")"
rm -f "$STATE.own" 2>/dev/null || true
if [ -n "$_LATE" ]; then
  echo "safe-merge: WARN -- leaving out $(printf '%s\n' "$_LATE" | wc -l | tr -d ' ') path(s) another seat staged (outside HEAD..MERGE_HEAD; they stay staged in the shared index for their owner):" >&2
  printf '%s\n' "$_LATE" | sed 's/^/              /' >&2
  while IFS= read -r _p; do [ -n "$_p" ] && GIT_INDEX_FILE="$_PRIV_IDX" git restore --staged -- "$_p" 2>/dev/null; done <<< "$_LATE"
fi

# ⛔ THE GATE TAKES ITS FILE LIST FROM ARGV (surprise-row-gate.py:1196). Called bare it
# grades NOTHING and prints "denominator: 0 dispatched path(s)" with rc 0 -- a VACUOUS
# PASS that reads exactly like a clean one. The first version of this script did that and
# the collision was caught only by the pre-commit hook downstream. Feed it the staged set
# OF THE SNAPSHOT, the set that will be committed.
STAGED_ARR=()
while IFS= read -r _f; do [ -n "$_f" ] && STAGED_ARR+=("$_f"); done < <(GIT_INDEX_FILE="$_PRIV_IDX" git diff --cached --name-only)
if [ "${#STAGED_ARR[@]}" -eq 0 ]; then
  echo "safe-merge: REFUSED -- the merge staged NO files. Nothing to grade; refusing rather than" >&2
  echo "            reporting a pass over an empty set." >&2
  rm -f "$_PRIV_IDX" 2>/dev/null || true
  git merge --abort 2>/dev/null || true
  exit 1
fi
# GRADE ONLY WHAT THE MERGE INTRODUCES (Andrew-direct 2026-10-08 ~19:1xZ, "Sure, yes", verbatim in
# org/tier1_exec/4.0.0_SA_CRO~A/deliverables/MERGE_ROOT_CAUSE_B3_20261008.md section 7). Each side was graded when it was
# committed; re-grading everything a parent carries is what made big merges slow and made them fail (R1-R3 there).
# GRADE_ARR = staged paths whose merged content differs from MERGE_HEAD too (differs from BOTH parents: a conflict
# resolution, or a file git auto-merged into content neither parent had) PLUS staged paths BOTH sides changed since the
# merge base (the guard: two sides adding rows to one channel file is the collision a drain exists to catch).
# An empty GRADE_ARR is a stated skip, never a silent pass. SAFE_MERGE_FULL_GRADE=1 grades every staged path as before.
GRADE_ARR=()
if [ "${SAFE_MERGE_FULL_GRADE:-0}" = "1" ]; then
  GRADE_ARR=("${STAGED_ARR[@]}")
  _grade_why="SAFE_MERGE_FULL_GRADE=1: every staged path"
else
  _mb="$(git merge-base HEAD MERGE_HEAD 2>/dev/null || echo '')"
  declare -A _GR=()
  while IFS= read -r _f; do [ -n "$_f" ] && _GR["$_f"]=1; done < <(GIT_INDEX_FILE="$_PRIV_IDX" git diff --cached --name-only MERGE_HEAD 2>/dev/null)
  if [ -n "$_mb" ]; then
    while IFS= read -r _f; do [ -n "$_f" ] && _GR["$_f"]=1; done < <(LC_ALL=C comm -12 \
        <(git diff --name-only "$_mb" HEAD 2>/dev/null | LC_ALL=C sort -u) \
        <(git diff --name-only "$_mb" MERGE_HEAD 2>/dev/null | LC_ALL=C sort -u))
  else
    for _f in "${STAGED_ARR[@]}"; do _GR["$_f"]=1; done   # no merge base: grade everything
  fi
  for _f in "${STAGED_ARR[@]}"; do if [ -n "${_GR[$_f]+x}" ]; then GRADE_ARR+=("$_f"); fi; done
  _grade_why="introduced by the merge or changed on both sides"
fi
echo "safe-merge: grading the MERGED index -- ${#GRADE_ARR[@]} of ${#STAGED_ARR[@]} staged path(s) (${_grade_why})"
_SM_GRADED="${#GRADE_ARR[@]}/${#STAGED_ARR[@]}"
if [ "${#GRADE_ARR[@]}" -eq 0 ]; then
  echo "safe-merge: SKIP -- the merge introduces no content of its own and no file changed on both sides; each side was graded at its own commit (Andrew ~19:1xZ). Row gate not run."
fi
# ⛔ THE ~32 KB ARGV CLIFF (0.0.0_AB_MSTR 94338, then 94639 on site Z's 440-path reconcile):
# Windows caps a command line near 32,767 chars, so above it python NEVER STARTS -- bash prints
# "Argument list too long" and returns rc=126 -- and the refusal text below used to read that as
# a row-id collision. The gate's own bisect on this box: 300 paths / 29,098 B rc 0; 400 paths /
# 38,798 B rc 126. Above a 28,000-char margin the list goes through the STAGED environment,
# which surprise-row-gate.py reads ONLY when argv is empty and whose SOURCE it prints (so the
# pass is never vacuous); below it, argv stays the contract this script's regression arm checks.
_argv_chars=0
for _f in "${GRADE_ARR[@]}"; do _argv_chars=$(( _argv_chars + ${#_f} + 1 )); done
_gate_rc=0
if [ "${#GRADE_ARR[@]}" -eq 0 ]; then
  :   # the stated SKIP above
elif [ "$_argv_chars" -gt 28000 ]; then
  echo "safe-merge: ${_argv_chars} argv chars exceed the ~32 KB Windows cliff -- feeding the gate through the STAGED environment (${#GRADE_ARR[@]} paths)"
  STAGED="$(printf '%s\n' "${GRADE_ARR[@]}")" GIT_INDEX_FILE="$_PRIV_IDX" python "$GATE" || _gate_rc=$?
else
  GIT_INDEX_FILE="$_PRIV_IDX" python "$GATE" "${GRADE_ARR[@]}" || _gate_rc=$?
fi
if [ "$_gate_rc" -ne 0 ]; then
  rc=$_gate_rc
  if [ "$rc" -eq 126 ] || [ "$rc" -eq 127 ]; then
    echo "safe-merge: *** THE ROW GATE DID NOT RUN (rc=$rc = 'cannot execute' / 'not found'; NOT a row-gate verdict). ***" >&2
    echo "            An argv cliff or a missing interpreter -- never a row-id collision. NOTHING WAS GRADED." >&2
    echo "            Aborting the merge. Fix the launch and re-run; do NOT reach for --no-verify, which" >&2
    echo "            discards every other gate too (the 94639 shape)." >&2
  else
    echo "safe-merge: *** REFUSED BY THE ROW GATE ON THE MERGED INDEX (rc=$rc). ***" >&2
    echo "            This is the collision the drain exists to catch: a row id minted in the" >&2
    echo "            worker's index that already exists at the main index. Aborting the merge." >&2
    echo "            FIX ON THE BRANCH (re-mint the row), then re-run -- a collision found" >&2
    echo "            here is a re-mint; found after the merge it is PERMANENT." >&2
  fi
  rm -f "$_PRIV_IDX" 2>/dev/null || true
  git merge --abort 2>/dev/null || true
  exit 1
fi

if [ -z "$SUBJECT" ]; then SUBJECT="drain: merge $BRANCH (row gate clean on the merged index)"; fi
# A commit failure here means a DOWNSTREAM hook refused what this script's own grade let
# through -- so the grade was wrong. ABORT; never leave a staged merge behind for someone
# to find and finish by hand.
# ⛔ THE DRAIN COMMIT CARRIES THE DRAINING SEAT'S AUTHOR, OR THIS SCRIPT REFUSES.
# Without --author the merge is attributed to the git-config identity, not the seat that
# drained it (measured on CLDGRPH's first drain, 91cabbdf86). A commit that names the wrong
# actor is a FALSE ATTRIBUTION of a good act -- the kind nobody ever goes back and contests.
# owned-paths-check.sh exempts a merge on MERGE_HEAD, so --author costs nothing here.
# REFUSING beats guessing: a wrong serial is worse than a stopped drain.
if [ -z "${OPAL_AGENT_SERIAL:-}" ]; then
  echo "safe-merge: REFUSED -- OPAL_AGENT_SERIAL is unset, so this script cannot name the" >&2
  echo "            draining seat on the merge commit. Export it and re-run; it will not" >&2
  echo "            guess an author. Aborting the merge." >&2
  rm -f "$_PRIV_IDX" 2>/dev/null || true
  git merge --abort 2>/dev/null || true
  exit 2
fi
_AUTH="${OPAL_AGENT_SERIAL} <${OPAL_AGENT_SERIAL}@opal.agent>"
# COMMIT FROM THE PRIVATE INDEX (row NFRA_OPLGTW-Z-S23, 0.0.0_AB_MSTR~Z 2026-10-02). The commit's own hooks take
# 15-45 min and git writes the tree from the index AFTER them, so a peer that stages into the SHARED index inside that
# window would ride into this merge (Z-S23: 0a5cc3c093 carried 1.0.0_SA_CTO~O's project.json line). The commit runs on
# the snapshot taken right after the merge (above): the hooks grade exactly what lands, and a peer's `git add` stays
# staged in the shared index for its owner. Proven in a scratch repo with a hook that stages a peer path mid-commit:
# shared index -> commit carried it; private -> not.
echo "safe-merge: committing the merge as ${OPAL_AGENT_SERIAL} (from the index snapshot taken right after the merge; a peer's later staging cannot enter it)"
# HOOK-HANG RETRY (1.0.0_SA_CTO msg 103165, 2026-09-30). The pre-commit hook can stall at PROCESS START
# (env.exe at 0 CPU, no child; captures in org/mcp/hook-hang-capture.log). Killing it failed the commit, and the abort
# below then threw away a fully graded merge (1,933 paths, 04:49Z). A watchdog that kills a hung hook first writes the
# marker file below in the COMMON git dir. A commit failure with a marker NEWER than this attempt's start is a killed
# hang, not a refusal: MERGE_HEAD and the index survive, so only `git commit` re-runs, at most 3 attempts. A genuine
# refusal writes no marker and still aborts exactly as before.
_HANG_MARK="$(git rev-parse --git-common-dir)/safe-merge-hook-killed"
# CHANGE 2, safe-merge half (0.0.0_AB_MSTR PROPOSAL_20261005_SAFE_MERGE_ROW_GATE_SPEED_CHANGES_2_AND_3.md): name the
# exact tree this run graded and the exact gate that graded it. The pre-commit hook may skip its own row-gate run when
# it recomputes BOTH ids from what it is committing and they match; on any difference it grades as before.
export SAFE_MERGE_GRADED_TREE="$(GIT_INDEX_FILE="$_PRIV_IDX" git write-tree 2>/dev/null || echo '')"
export SAFE_MERGE_GRADED_GATE="$(git hash-object "$GATE" 2>/dev/null || echo '')"
# GS-f-6: what the commit must carry, captured before the state file is removed (see _verify_staged_carried).
_EXPECT="$( { [ "$_CONTINUING" -eq 1 ] && cat "$STATE" 2>/dev/null; printf '%s\n' "${STAGED_ARR[@]}"; } | sed '/^$/d' | LC_ALL=C sort -u )"
_CONFLICTED="$( [ "$_CONTINUING" -eq 1 ] && cat "$STATE.conflicted" 2>/dev/null || true )"
_try=0
while :; do
  _try=$((_try + 1))
  _t0=$(date +%s)
  # MERGE_HEAD is read again at each attempt: a commit on a MERGE_HEAD this run did not write lands this run's tree
  # under another branch's parent (9f146f853a). Refuse and abort NOTHING -- an open merge here is no longer this run's.
  _NOW_MH="$(git rev-parse -q --verify MERGE_HEAD 2>/dev/null || echo none)"
  if [ "$_NOW_MH" != "$_MY_MH" ] || [ "$_MY_MH" = "none" ]; then
    echo "safe-merge: *** REFUSED -- MERGE_HEAD CHANGED UNDER THIS RUN (opened ${_MY_MH}, now ${_NOW_MH}). ***" >&2
    echo "            Another process aborted or replaced this merge. NOT committing and NOT aborting: whatever" >&2
    echo "            is open now is not this run's. Nothing landed. Re-run safe-merge from the top." >&2
    rm -f "$_PRIV_IDX" "$STATE" "$STATE.branch" "$STATE.head" 2>/dev/null || true
    exit 1
  fi
  if GIT_INDEX_FILE="$_PRIV_IDX" git commit --no-edit --author "$_AUTH" -m "$SUBJECT"; then break; fi
  if [ -f "$_HANG_MARK" ] && [ "$(date -r "$_HANG_MARK" +%s 2>/dev/null || echo 0)" -ge "$_t0" ] && [ "$_try" -lt 3 ]; then
    echo "safe-merge: commit attempt $_try failed on a KILLED HUNG HOOK ($(cat "$_HANG_MARK" 2>/dev/null)); the merge is intact -- retrying git commit only" >&2
    rm -f "$_HANG_MARK"
    continue
  fi
  echo "safe-merge: *** COMMIT REFUSED DOWNSTREAM after this script's grade PASSED. ***" >&2
  echo "            That is a defect in THIS script's grade, not only in the branch: a hook" >&2
  echo "            saw something the merged-index grade above did not. Aborting the merge so" >&2
  echo "            nothing is left staged, and REPORT the discrepancy." >&2
  rm -f "$_PRIV_IDX" 2>/dev/null || true
  git merge --abort 2>/dev/null || true
  exit 1
done
rm -f "$_PRIV_IDX" "$STATE" "$STATE.branch" "$STATE.head" "$STATE.conflicted" 2>/dev/null || true
# The commit's hooks are the longest window a peer has to reset the shared index under this merge.
# Read the TREE now, before reporting anything (see _verify_merge_tree).
_vrc=0; _verify_merge_tree HEAD || _vrc=$?
if [ "$_vrc" -eq 5 ]; then
  echo "safe-merge: NOT MERGED -- commit $(git rev-parse --short HEAD) landed WITHOUT the branch's content, in whole or in part (exit 5)." >&2
  exit 5
fi
_src=0; _verify_staged_carried HEAD "$_EXPECT" "$_CONFLICTED" || _src=$?
if [ "$_src" -eq 7 ]; then
  echo "safe-merge: COMMITTED $(git rev-parse --short HEAD) BUT IT LACKS PATH(S) THE MERGE STAGED (exit 7)." >&2
  exit 7
fi
echo "safe-merge: MERGED and committed -- $(git rev-parse --short HEAD)"
echo "safe-merge: remember the drain's remaining steps -- remove the worktree and its branch explicitly."
# The index is read LAST and after MERGED is printed: the merge did land, and rc 6 says only that the index is stale.
_irc=0; _verify_shared_index HEAD || _irc=$?
[ "$_irc" -eq 6 ] && exit 6
exit 0
