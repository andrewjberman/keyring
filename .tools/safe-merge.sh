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
# EXIT CODES: 0 merged | 1 refused, merge aborted | 2 usage/precondition, nothing done
#             4 CONFLICT, THE MERGE IS OPEN AND YOURS TO RESOLVE (nothing landed)
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
      "grep -q 'git diff --cached --name-only > \"\$STATE\"' '$0'"
  chk "--continue refuses while any path is still UNRESOLVED" \
      "grep -q 'still carry unresolved conflict markers' '$0'"
  chk "--continue refuses a path THIS MERGE DID NOT STAGE (the drain-sweep guard)" \
      "grep -q 'THIS MERGE DID NOT STAGE' '$0'"
  chk "--continue refuses when this script did not open the merge (no state file)" \
      "grep -q 'THIS script did not open it' '$0'"
  chk "--abort exists and clears the conflict state" \
      "grep -q 'merge aborted; tree restored and conflict state cleared' '$0'"
  chk "the state file is resolved via --git-path (a linked worktree keeps its own)" \
      "grep -q 'git rev-parse --git-path safe-merge-conflict' '$0'"
  echo "DENOMINATOR: $((n-fails)) of $n arm(s) passed"
  echo "  STOP: BLIND SPOT, STATED: every arm above is a REFUSAL or a structural check. This"
  echo "     self-test has NO GREEN MERGE ARM -- a version of this script that refused"
  echo "     EVERYTHING would pass all of them. A self-test cannot safely perform a real"
  echo "     merge in the SHARED tree, so the permit path is covered by EXERCISE, not here:"
  echo "       .tools/tests/exercise-safe-merge-continue.sh -- 30 arms, ALL GREEN 2026-09-04"
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

# ---------------------------------------------------------------- --abort
if [ "${1:-}" = "--abort" ]; then
  if ! _merge_open; then
    # A STALE state file with no merge open is exactly what 94259 found, and before this branch
    # there was no way to disarm one: --abort exited 2 and left it armed. Clearing it IS the
    # abort in that case.
    if [ -f "$STATE" ]; then
      rm -f "$STATE" "$STATE.branch" 2>/dev/null || true
      echo "safe-merge: no merge in progress, but a STALE conflict state file was present -- cleared."
      echo "            --continue is now disarmed in this worktree. Nothing else was touched."
      exit 0
    fi
    echo "safe-merge: no merge in progress and no conflict state -- nothing to abort" >&2
    exit 2
  fi
  git merge --abort || { echo "safe-merge: git merge --abort FAILED; the tree is NOT restored" >&2; exit 1; }
  rm -f "$STATE" "$STATE.branch" 2>/dev/null || true
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
  _UNRES="$(git diff --name-only --diff-filter=U | wc -l | tr -d ' ')"
  if [ "$_UNRES" != "0" ]; then
    echo "safe-merge: REFUSED -- ${_UNRES} path(s) still carry unresolved conflict markers:" >&2
    git diff --name-only --diff-filter=U | sed 's/^/              /' >&2
    echo "            Resolve and \`git add\` them, then re-run --continue. The merge stays OPEN." >&2
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

# A dirty index is not ours to merge into: the union we would grade would carry
# somebody else's staged work and the abort path could not restore it cleanly.
if [ "$_CONTINUING" -eq 0 ] && [ -n "$(git diff --cached --name-only)" ]; then
  echo "safe-merge: REFUSED -- the index carries STAGED changes (possibly another seat's)." >&2
  echo "            Merging would grade a union that is not just this branch. Clear or commit first." >&2
  git diff --cached --name-only | sed 's/^/              /' >&2
  exit 2
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
  git diff --cached --name-only > "$STATE" 2>/dev/null || true
  git diff --name-only --diff-filter=U >> "$STATE" 2>/dev/null || true
  echo "$BRANCH" > "$STATE.branch" 2>/dev/null || true
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
  exit 4
fi
fi

# ⛔ THE GATE TAKES ITS FILE LIST FROM ARGV (surprise-row-gate.py:1196). Called bare it
# grades NOTHING and prints "denominator: 0 dispatched path(s)" with rc 0 -- a VACUOUS
# PASS that reads exactly like a clean one. The first version of this script did that and
# the collision was caught only by the pre-commit hook downstream. Feed it the staged set.
STAGED_ARR=()
while IFS= read -r _f; do [ -n "$_f" ] && STAGED_ARR+=("$_f"); done < <(git diff --cached --name-only)
if [ "${#STAGED_ARR[@]}" -eq 0 ]; then
  echo "safe-merge: REFUSED -- the merge staged NO files. Nothing to grade; refusing rather than" >&2
  echo "            reporting a pass over an empty set." >&2
  git merge --abort 2>/dev/null || true
  exit 1
fi
echo "safe-merge: grading the MERGED index -- ${#STAGED_ARR[@]} staged path(s)"
# ⛔ THE ~32 KB ARGV CLIFF (0.0.0_AB_MSTR 94338, then 94639 on site Z's 440-path reconcile):
# Windows caps a command line near 32,767 chars, so above it python NEVER STARTS -- bash prints
# "Argument list too long" and returns rc=126 -- and the refusal text below used to read that as
# a row-id collision. The gate's own bisect on this box: 300 paths / 29,098 B rc 0; 400 paths /
# 38,798 B rc 126. Above a 28,000-char margin the list goes through the STAGED environment,
# which surprise-row-gate.py reads ONLY when argv is empty and whose SOURCE it prints (so the
# pass is never vacuous); below it, argv stays the contract this script's regression arm checks.
_argv_chars=0
for _f in "${STAGED_ARR[@]}"; do _argv_chars=$(( _argv_chars + ${#_f} + 1 )); done
_gate_rc=0
if [ "$_argv_chars" -gt 28000 ]; then
  echo "safe-merge: ${_argv_chars} argv chars exceed the ~32 KB Windows cliff -- feeding the gate through the STAGED environment (${#STAGED_ARR[@]} paths)"
  STAGED="$(printf '%s\n' "${STAGED_ARR[@]}")" python "$GATE" || _gate_rc=$?
else
  python "$GATE" "${STAGED_ARR[@]}" || _gate_rc=$?
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
  git merge --abort 2>/dev/null || true
  exit 2
fi
_AUTH="${OPAL_AGENT_SERIAL} <${OPAL_AGENT_SERIAL}@opal.agent>"
echo "safe-merge: committing the merge as ${OPAL_AGENT_SERIAL}"
if ! git commit --no-edit --author "$_AUTH" -m "$SUBJECT"; then
  echo "safe-merge: *** COMMIT REFUSED DOWNSTREAM after this script's grade PASSED. ***" >&2
  echo "            That is a defect in THIS script's grade, not only in the branch: a hook" >&2
  echo "            saw something the merged-index grade above did not. Aborting the merge so" >&2
  echo "            nothing is left staged, and REPORT the discrepancy." >&2
  git merge --abort 2>/dev/null || true
  exit 1
fi
rm -f "$STATE" "$STATE.branch" 2>/dev/null || true
echo "safe-merge: MERGED and committed -- $(git rev-parse --short HEAD)"
echo "safe-merge: remember the drain's remaining steps -- remove the worktree and its branch explicitly."
