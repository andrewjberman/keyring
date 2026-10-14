#!/usr/bin/env bash
# portal-merge-forward.sh -- the one approved route onto portal DEV (NFRA_DEVPLN cell DP-b-2).
#
# Usage:
#   bash .tools/portal-merge-forward.sh <branch> [--repo <portal repo path, default portal>] [--push] [--no-fetch]
#   bash .tools/portal-merge-forward.sh --selftest
#
# Before it decides, origin is fetched for DEV, and for the branch when origin has it (a failed fetch or
# ls-remote refuses fetch-failed). A branch absent on origin is read as the local branch (NOTE on stderr);
# absent both on origin and locally refuses branch-not-found. --no-fetch reads the local refs as they are
# (the self-test's fixed state uses it).
# The approval row is read through ${OPAL_APPROVAL_STATUS_CMD:-python .tools/open-calls.py approval-status}
# and must print one APPROVAL line. Any doubt refuses (fail closed). A feature lands as a MERGE commit
# on DEV, with the trailers Feature: and Approved-By:, in an ephemeral worktree. The result line prints last,
# and carries merge=<sha> (merge=- on a refusal).
set -u
set -f

PMF_TEST_ONLY_RE='(^|/)(__tests__|__harness__|__fixtures__|__mocks__)/|\.(test|spec)\.[cm]?[jt]sx?$|(^|/)(tests?|e2e|fixtures?)/'

PMF_SELF_DIR="$(cd "$(dirname "$0")" && pwd)"
PMF_SELF="$PMF_SELF_DIR/$(basename "$0")"

BRANCH="-"
ROOT=""
REPO=""
REPO_ARG="portal"
BREF=""
MFBR=""
DEVREF="refs/remotes/origin/DEV"
TIP="-"
DEV_BEFORE="-"
DEV_AFTER=""
PUSHED="no"
MERGE_OUT="-"
RUNTMP=""
WT=""
MSGF=""
PMF_TMP=""

pmf_cleanup() {
  if [ -n "$WT" ] && [ -e "$WT" ]; then
    if ! git -C "$REPO" worktree remove "$WT" 1>&2; then
      echo "WARN: merge worktree not removed, inspect and remove by hand: $WT" 1>&2
    fi
  fi
  WT=""
  if [ -n "$MSGF" ]; then rm -f "$MSGF"; fi
  MSGF=""
  return 0
}

pmf_finish() {
  local result="$1" reason="$2" rc=1
  pmf_cleanup
  if [ -z "$DEV_AFTER" ]; then DEV_AFTER="$DEV_BEFORE"; fi
  printf 'MERGE-FORWARD branch=%s result=%s reason=%s dev_before=%s dev_after=%s pushed=%s merge=%s\n' \
    "$BRANCH" "$result" "$reason" "$DEV_BEFORE" "$DEV_AFTER" "$PUSHED" "$MERGE_OUT"
  if [ "$result" = MERGED ]; then rc=0; fi
  exit "$rc"
}

pmf_refuse() { pmf_finish REFUSED "$1"; }

pmf_run() {
  local arg_branch="" do_push=0 tok out="" rc=0 nline=0 line="" F_BRANCH=""
  local STATE="" VALID="" ROW="" BY="" HEAD_SHA="" paths="" npath=0 nonfirst=0 p bases="" mb="" one=""
  local stamp slug APPR="" MERGESHA="" P1="" P2="" P3="" MSGTXT="" pout="" prc=0 _m=""
  local do_fetch=1 local_only=0 lsr_rc=0
  while [ $# -gt 0 ]; do
    case "$1" in
      --repo)
        if [ $# -lt 2 ]; then echo "ERROR: --repo needs a path" 1>&2; pmf_refuse usage; fi
        REPO_ARG="$2"; shift 2 ;;
      --push) do_push=1; shift ;;
      --no-fetch) do_fetch=0; shift ;;
      --*) echo "ERROR: unknown option $1" 1>&2; pmf_refuse usage ;;
      *)
        if [ -n "$arg_branch" ]; then echo "ERROR: one branch only" 1>&2; pmf_refuse usage; fi
        arg_branch="$1"; shift ;;
    esac
  done
  if [ -z "$arg_branch" ]; then
    echo "ERROR: usage: portal-merge-forward.sh <branch> [--repo <path>] [--push] [--no-fetch]" 1>&2
    pmf_refuse usage
  fi
  BRANCH="$arg_branch"
  trap pmf_cleanup EXIT

  ROOT="$(git rev-parse --show-toplevel)" || { echo "ERROR: not inside a git worktree" 1>&2; pmf_refuse repo-not-found; }
  case "$REPO_ARG" in
    /*|[A-Za-z]:*) REPO="$REPO_ARG" ;;
    *) REPO="$ROOT/$REPO_ARG" ;;
  esac
  git -C "$REPO" rev-parse --git-dir >/dev/null 2>&1 || pmf_refuse repo-not-found

  # Step 1: the branch name is valid; origin is fetched for DEV and for the branch unless --no-fetch (a failed fetch refuses).
  git check-ref-format "refs/heads/$BRANCH" || pmf_refuse branch-not-found
  if [ "$do_fetch" -eq 1 ]; then
    git -C "$REPO" fetch --quiet origin "+refs/heads/DEV:$DEVREF" 1>&2 || pmf_refuse fetch-failed
    # ls-remote exit 2 = the ref is absent on origin (not a network failure); any other failure refuses.
    git -C "$REPO" ls-remote --exit-code origin "refs/heads/$BRANCH" >/dev/null || lsr_rc=$?
    case "$lsr_rc" in
      0) git -C "$REPO" fetch --quiet origin "+refs/heads/$BRANCH:refs/remotes/origin/$BRANCH" 1>&2 || pmf_refuse fetch-failed ;;
      2)
        if ! git -C "$REPO" rev-parse --verify -q "refs/heads/$BRANCH" >/dev/null; then pmf_refuse branch-not-found; fi
        echo "NOTE: $BRANCH is not on origin; using the local branch" 1>&2
        local_only=1 ;;
      *) pmf_refuse fetch-failed ;;
    esac
  fi
  # Step 1 (cont.): the branch is read as origin/<branch>, else the local branch; a local-only branch skips origin/<branch>.
  if [ "$local_only" -eq 0 ] && git -C "$REPO" rev-parse --verify -q "refs/remotes/origin/$BRANCH" >/dev/null; then
    BREF="refs/remotes/origin/$BRANCH"
  elif git -C "$REPO" rev-parse --verify -q "refs/heads/$BRANCH" >/dev/null; then
    BREF="refs/heads/$BRANCH"
  else
    pmf_refuse branch-not-found
  fi
  TIP="$(git -C "$REPO" rev-parse --verify "$BREF^{commit}")" || pmf_refuse branch-not-found
  DEV_BEFORE="$(git -C "$REPO" rev-parse --verify -q "$DEVREF")" || { DEV_BEFORE="-"; pmf_refuse dev-not-found; }

  # Step 2: the approval row, read as ONE line.
  if [ -n "${OPAL_APPROVAL_STATUS_CMD:-}" ]; then
    # shellcheck disable=SC2086
    out="$(cd "$ROOT" && $OPAL_APPROVAL_STATUS_CMD --branch "$BRANCH" 2>&1)"; rc=$?
  else
    out="$(cd "$ROOT" && python .tools/open-calls.py approval-status --branch "$BRANCH" 2>&1)"; rc=$?
  fi
  nline="$(printf '%s\n' "$out" | grep -c '^APPROVAL ')"
  if [ "$rc" -ne 0 ] || [ "$nline" != 1 ]; then pmf_refuse status-unreadable; fi
  line="$(printf '%s\n' "$out" | grep '^APPROVAL ')"
  for tok in $line; do
    case "$tok" in
      branch=*) F_BRANCH="${tok#branch=}" ;;
      state=*) STATE="${tok#state=}" ;;
      valid=*) VALID="${tok#valid=}" ;;
      row=*) ROW="${tok#row=}" ;;
      by=*) BY="${tok#by=}" ;;
      head_sha=*) HEAD_SHA="${tok#head_sha=}" ;;
      *) : ;;
    esac
  done
  if [ "$F_BRANCH" != "$BRANCH" ]; then pmf_refuse status-unreadable; fi
  case "$STATE" in
    ABSENT|OPEN|APPROVED|DECLINED) ;;
    *) pmf_refuse status-unreadable ;;
  esac

  # Step 2 (decision): fail closed, in the order the TO fixes.
  case "$STATE" in
    ABSENT)
      # The changed paths are the union over EVERY merge base of DEV and the branch, so the set does not depend on
      # which base git would pick. A three-dot diff makes git choose one base and print "multiple merge bases" when
      # the history has several (a criss-cross); a product file changed relative to any base must still be seen.
      # With exactly one base the union is the three-dot diff.
      bases="$(git -C "$REPO" merge-base --all "$DEVREF" "$BREF")" || pmf_refuse no-approval-row
      [ -n "$bases" ] || pmf_refuse no-approval-row
      paths=""
      while IFS= read -r mb; do
        [ -n "$mb" ] || continue
        one="$(git -C "$REPO" diff --name-only "$mb" "$BREF")" || pmf_refuse no-approval-row
        paths="$paths$one"$'\n'
      done <<< "$bases"
      while IFS= read -r p; do
        [ -n "$p" ] || continue
        npath=$((npath + 1))
        if ! printf '%s\n' "$p" | grep -E -q "$PMF_TEST_ONLY_RE"; then nonfirst=$((nonfirst + 1)); fi
      done <<< "$paths"
      if [ "$npath" -lt 1 ] || [ "$nonfirst" -ne 0 ]; then pmf_refuse no-approval-row; fi
      BY="test-only"
      ROW="-"
      ;;
    OPEN) pmf_refuse not-approved ;;
    DECLINED) pmf_refuse declined ;;
    APPROVED)
      if [ "$VALID" != yes ]; then pmf_refuse approver-not-valid; fi
      if [ -z "$BY" ] || [ -z "$ROW" ] || [ "$BY" = - ] || [ "$ROW" = - ]; then pmf_refuse approver-not-valid; fi
      if [ "${#HEAD_SHA}" -lt 7 ]; then pmf_refuse stale-head; fi
      case "$TIP" in
        "$HEAD_SHA"*) ;;
        *) pmf_refuse stale-head ;;
      esac
      ;;
  esac
  if git -C "$REPO" merge-base --is-ancestor "$TIP" "$DEVREF"; then pmf_refuse already-on-dev; fi

  # Step 3: merge in an ephemeral detached worktree off origin/DEV.
  stamp="$(date -u +%Y%m%dT%H%M%SZ)-$$"
  slug="$(printf '%s' "$BRANCH" | tr '/' '-')"
  RUNTMP="${PMF_RUNTMP:-$ROOT/.runtmp}"
  mkdir -p "$RUNTMP" || pmf_refuse worktree-failed
  WT="$RUNTMP/portal-mf-$stamp"
  MSGF="$RUNTMP/portal-mf-$stamp.msg"
  MFBR="mf/$slug-$stamp"
  if [ "$BY" = test-only ]; then APPR="Approved-By: test-only @-"; else APPR="Approved-By: $BY @$ROW"; fi
  printf 'Merge %s into DEV (approved feature)\n\nFeature: %s\n%s\n' "$BRANCH" "$BRANCH" "$APPR" > "$MSGF" \
    || pmf_refuse worktree-failed
  git -C "$REPO" worktree add --detach "$WT" "$DEVREF" 1>&2 || pmf_refuse worktree-failed
  if ! git -C "$WT" merge --no-ff --no-edit -F "$MSGF" "$TIP" 1>&2; then
    git -C "$WT" merge --abort 1>&2
    pmf_refuse conflict
  fi
  MERGESHA="$(git -C "$WT" rev-parse --verify HEAD)" || pmf_refuse merge-verify-failed
  read -r _m P1 P2 P3 <<< "$(git -C "$REPO" rev-list --parents -n 1 "$MERGESHA")"
  if [ -z "$P2" ] || [ -n "$P3" ] || [ "$P1" != "$DEV_BEFORE" ] || [ "$P2" != "$TIP" ]; then
    pmf_refuse merge-verify-failed
  fi
  MSGTXT="$(git -C "$REPO" log -1 --format=%B "$MERGESHA")"
  if ! printf '%s\n' "$MSGTXT" | grep -qxF "Feature: $BRANCH"; then pmf_refuse merge-verify-failed; fi
  if ! printf '%s\n' "$MSGTXT" | grep -qxF "$APPR"; then pmf_refuse merge-verify-failed; fi
  git -C "$REPO" branch "$MFBR" "$MERGESHA" 1>&2 || pmf_refuse merge-verify-failed

  # Step 4: nothing leaves the machine unless --push is given; push is plain, never forced.
  if [ "$do_push" -eq 1 ]; then
    pout="$(git -C "$REPO" push origin "$MERGESHA:refs/heads/DEV" 2>&1)"; prc=$?
    printf '%s\n' "$pout" 1>&2
    DEV_AFTER="$(git -C "$REPO" rev-parse --verify -q "$DEVREF")"
    if [ "$prc" -ne 0 ]; then
      if printf '%s\n' "$pout" | grep -q -i -E 'rejected|non-fast-forward|fetch first'; then
        pmf_refuse push-rejected
      fi
      pmf_refuse push-failed
    fi
    PUSHED="yes"
  fi
  # Step 5: the one result line, last, carrying the merge commit.
  MERGE_OUT="$MERGESHA"
  pmf_finish MERGED -
}

# fx <command...>: runs one self-test fixture step (a fixture write, mkdir, git init/add/commit/checkout/branch/push/clone/
# merge/fetch). Stdin and stdout are inherited, so a heredoc or a redirect after fx reaches the step. A non-zero exit
# prints the step and exits the self-test before any case is graded. A step EXPECTED to fail is a plain command, not fx.
fx() {
  if ! "$@"; then
    echo "SELFTEST ERROR: fixture step failed: $*" 1>&2
    exit 1
  fi
}
# pmf_put <path> <text>: a fixture file holding <text> and a newline (runs inside fx, so a failed write is seen).
pmf_put() { printf '%s\n' "$2" > "$1"; }
# pmf_cat <path>: a fixture file from stdin, a heredoc (runs inside fx, so a failed write is seen).
pmf_cat() { cat > "$1"; }

pmf_selftest_cleanup() {
  if [ -n "$PMF_TMP" ] && [ -d "$PMF_TMP" ]; then
    chmod -R u+w "$PMF_TMP"
    rm -rf "$PMF_TMP"
  fi
}

pmf_selftest() {
  local ORIG SEED CLONE OTHER FIX N=0 K=0 RC=0 LAST="" dev0="" dev1="" devnew="" devnew2=""
  local CRISS="" devcriss="" CX=""
  local T_OK="" T_INV="" T_STALE="" T_UNR="" T_ABSP="" T_ABST="" T_CONF="" T_FF2="" SHA_OLD="" wtb="" wta=""
  local MF="" MS="" MFT="" tok

  PMF_TMP="$(mktemp -d)" || { echo "ERROR: mktemp failed" 1>&2; exit 1; }
  trap pmf_selftest_cleanup EXIT
  export GIT_AUTHOR_NAME=selftest GIT_AUTHOR_EMAIL=selftest@opal.agent
  export GIT_COMMITTER_NAME=selftest GIT_COMMITTER_EMAIL=selftest@opal.agent
  ORIG="$PMF_TMP/origin.git"; SEED="$PMF_TMP/seed"; CLONE="$PMF_TMP/clone"; OTHER="$PMF_TMP/other"
  FIX="$PMF_TMP/fixture-status.sh"

  # Fixture: the approval reader stand-in. FIX_LINE is printed, FIX_RC is the exit code.
  fx pmf_cat "$FIX" <<'FIXEOF'
#!/usr/bin/env bash
# selftest fixture for the approval reader
if [ "${FIX_RC:-0}" != 0 ]; then exit "$FIX_RC"; fi
if [ -n "${FIX_LINE:-}" ]; then printf '%s\n' "$FIX_LINE"; fi
exit 0
FIXEOF

  # Repositories: a bare origin with PROD and DEV (DEV one commit ahead), and feature branches cut from PROD.
  fx git init -q --bare "$ORIG"
  fx git -C "$ORIG" symbolic-ref HEAD refs/heads/PROD
  fx git init -q "$SEED"
  fx git -C "$SEED" symbolic-ref HEAD refs/heads/PROD
  fx pmf_put "$SEED/base.txt" base
  fx pmf_put "$SEED/shared.txt" 'prod line'
  fx git -C "$SEED" add -A
  fx git -C "$SEED" commit -q -m "prod seed"
  fx git -C "$SEED" branch DEV
  fx git -C "$SEED" checkout -q DEV
  fx pmf_put "$SEED/shared.txt" 'dev line'
  fx git -C "$SEED" commit -q -am "dev change"
  fx git -C "$SEED" checkout -q PROD

  pmf_mkfeat() { # pmf_mkfeat <branch> <file> <content>
    fx git -C "$SEED" checkout -q -b "$1" PROD
    fx mkdir -p "$(dirname "$SEED/$2")"
    fx pmf_put "$SEED/$2" "$3"
    fx git -C "$SEED" add -A
    fx git -C "$SEED" commit -q -m "feature $1"
    fx git -C "$SEED" checkout -q PROD
  }
  pmf_mkfeat feat-ok product/ok.txt ok
  pmf_mkfeat feat-open product/open.txt open
  pmf_mkfeat feat-declined product/declined.txt declined
  pmf_mkfeat feat-invalid product/invalid.txt invalid
  pmf_mkfeat feat-unread product/unread.txt unread
  pmf_mkfeat feat-abs-prod product/abs.txt abs
  pmf_mkfeat feat-conf shared.txt "feature line"
  pmf_mkfeat feat-ff2 product/ff2.txt ff2
  pmf_mkfeat feat-stale product/stale-a.txt stale-a
  fx git -C "$SEED" rev-parse --verify feat-stale >/dev/null
  SHA_OLD="$(git -C "$SEED" rev-parse --verify feat-stale)"
  fx git -C "$SEED" checkout -q feat-stale
  fx pmf_put "$SEED/product/stale-b.txt" stale-b
  fx git -C "$SEED" add -A
  fx git -C "$SEED" commit -q -m "feature feat-stale second commit"
  fx git -C "$SEED" checkout -q PROD
  fx git -C "$SEED" checkout -q -b feat-abs-test PROD
  fx mkdir -p "$SEED/src/__tests__" "$SEED/e2e"
  fx pmf_put "$SEED/src/__tests__/ok.test.ts" test
  fx pmf_put "$SEED/e2e/flow.spec.ts" flow
  fx git -C "$SEED" add -A
  fx git -C "$SEED" commit -q -m "feature feat-abs-test (tests only)"
  fx git -C "$SEED" checkout -q PROD
  fx git -C "$SEED" push -q "$ORIG" --all
  fx git clone -q "$ORIG" "$CLONE"

  T_OK="$(git -C "$CLONE" rev-parse --verify refs/remotes/origin/feat-ok)"
  T_INV="$(git -C "$CLONE" rev-parse --verify refs/remotes/origin/feat-invalid)"
  T_STALE="$(git -C "$CLONE" rev-parse --verify refs/remotes/origin/feat-stale)"
  T_UNR="$(git -C "$CLONE" rev-parse --verify refs/remotes/origin/feat-unread)"
  T_ABSP="$(git -C "$CLONE" rev-parse --verify refs/remotes/origin/feat-abs-prod)"
  T_ABST="$(git -C "$CLONE" rev-parse --verify refs/remotes/origin/feat-abs-test)"
  T_CONF="$(git -C "$CLONE" rev-parse --verify refs/remotes/origin/feat-conf)"
  T_FF2="$(git -C "$CLONE" rev-parse --verify refs/remotes/origin/feat-ff2)"
  dev0="$(git -C "$CLONE" rev-parse --verify refs/remotes/origin/DEV)"

  pmf_apv() { # pmf_apv <branch> <state> <valid> <row> <by> <head_sha> <commits> <class>
    printf 'APPROVAL branch=%s state=%s valid=%s row=%s by=%s head_sha=%s commits=%s class=%s box=laptop pages=-\n' \
      "$1" "$2" "$3" "$4" "$5" "$6" "$7" "$8"
  }
  pmf_setfix() { export FIX_LINE="$1" FIX_RC="${2:-0}"; }
  pmf_runmf() { # pmf_runmf <branch> [extra args]: sets RC and LAST; the fixed state is read with --no-fetch
    local br="$1" ob="$PMF_TMP/out-$N.txt"
    shift
    fx mkdir -p "$PMF_TMP/runtmp"
    PMF_RUNTMP="$PMF_TMP/runtmp" OPAL_APPROVAL_STATUS_CMD="bash $FIX" \
      bash "$PMF_SELF" "$br" --repo "$CLONE" --no-fetch "$@" >"$ob"
    RC=$?
    LAST="$(tail -n 1 "$ob")"
  }
  pmf_check() { # pmf_check <label> <command...>
    N=$((N+1))
    if "${@:2}"; then K=$((K+1)); echo "SELFTEST PASS $1"; else echo "SELFTEST FAIL $1"; fi
  }
  pmf_refused_ok() { # pmf_refused_ok <reason>: RC 1, REFUSED with that reason, DEV unchanged, merge=-
    [ "$RC" -eq 1 ] || return 1
    case "$LAST" in
      *" result=REFUSED reason=$1 dev_before=$dev0 dev_after=$dev0 pushed=no merge=-") return 0 ;;
    esac
    return 1
  }
  pmf_merged_ok() { # RC 0, MERGED, DEV unchanged (no push), merge= names a commit
    [ "$RC" -eq 0 ] || return 1
    case "$LAST" in
      *" result=MERGED reason=- dev_before=$dev0 dev_after=$dev0 pushed=no merge="?*) return 0 ;;
    esac
    return 1
  }
  pmf_merge_field() { # pmf_merge_field <sha>: the result line's merge= is exactly this commit
    case "$LAST" in
      *" pushed=no merge=$1") return 0 ;;
    esac
    return 1
  }
  pmf_parents_ok() { # pmf_parents_ok <merge sha> <first parent> <second parent>
    local a="" b="" c="" _x=""
    read -r _x a b c <<< "$(git -C "$CLONE" rev-list --parents -n 1 "$1")"
    [ -n "$b" ] && [ -z "$c" ] && [ "$a" = "$2" ] && [ "$b" = "$3" ]
  }
  pmf_msg_has() { # pmf_msg_has <sha> <exact line>
    git -C "$CLONE" log -1 --format=%B "$1" | grep -qxF "$2"
  }
  pmf_dev_now() { git -C "$CLONE" rev-parse --verify -q refs/remotes/origin/DEV; }
  pmf_mf_of() { git -C "$CLONE" for-each-ref --format='%(refname)' "refs/heads/mf/$1-*"; }
  pmf_trailers_1c() { pmf_msg_has "$1" "Feature: feat-ok" && pmf_msg_has "$1" "Approved-By: fixture-approver @ROW-OK-1"; }
  pmf_trailers_8b() { pmf_msg_has "$1" "Approved-By: test-only @-" && pmf_parents_ok "$1" "$dev0" "$T_ABST"; }
  pmf_leftover_9b() { [ "$wtb" = "$wta" ] && [ -z "$(ls -A "$PMF_TMP/runtmp")" ] && [ -z "$(pmf_mf_of feat-conf)" ]; }
  pmf_push_10a() {
    [ "$RC" -eq 0 ] || return 1
    case "$LAST" in
      *" dev_before=$dev0 dev_after=$devnew pushed=yes merge=$devnew") return 0 ;;
    esac
    return 1
  }
  pmf_origin_10b() { [ "$1" != "$dev0" ] && pmf_parents_ok "$1" "$dev0" "$T_OK"; }
  pmf_push_11a() {
    [ "$RC" -eq 1 ] || return 1
    case "$LAST" in
      *" result=REFUSED reason=push-rejected dev_before=$dev1 dev_after=$dev1 pushed=no merge=-") return 0 ;;
    esac
    return 1
  }
  pmf_fetch_12a() { # the default fetch: the branch was not known to the clone before the run, and the run merged it
    [ "$RC" -eq 0 ] || return 1
    case "$LAST" in
      *" result=MERGED reason=- dev_before=$devnew2 dev_after=$devnew2 pushed=no merge="?*) return 0 ;;
    esac
    return 1
  }
  pmf_origin_11b() { [ "$(git -C "$ORIG" rev-parse --verify refs/heads/DEV)" = "$1" ]; }

  # 1. APPROVED valid=yes merges: two parents, both trailers, dev_before is the first parent.
  pmf_setfix "$(pmf_apv feat-ok APPROVED yes ROW-OK-1 fixture-approver "$T_OK" 2 opal-internal)"
  pmf_runmf feat-ok
  pmf_check "1a APPROVED valid=yes merges (MERGED line, DEV unchanged)" pmf_merged_ok
  MF="$(pmf_mf_of feat-ok)"; MS="$(git -C "$CLONE" rev-parse --verify -q "$MF" || echo none)"
  pmf_check "1b merge commit has two parents, first is dev_before, second is the branch tip" pmf_parents_ok "$MS" "$dev0" "$T_OK"
  pmf_check "1c merge commit carries both trailers" pmf_trailers_1c "$MS"
  pmf_check "1d the MERGED line names that merge commit in merge=" pmf_merge_field "$MS"

  # 2-3. OPEN and DECLINED refuse.
  pmf_setfix "$(pmf_apv feat-open OPEN - - - - - opal-internal)"
  pmf_runmf feat-open
  pmf_check "2 OPEN refuses not-approved, DEV unchanged" pmf_refused_ok not-approved
  pmf_setfix "$(pmf_apv feat-declined DECLINED - - - - - opal-internal)"
  pmf_runmf feat-declined
  pmf_check "3 DECLINED refuses declined, DEV unchanged" pmf_refused_ok declined

  # 4. APPROVED valid=no refuses.
  pmf_setfix "$(pmf_apv feat-invalid APPROVED no ROW-INV-1 fixture-approver "$T_INV" 1 opal-internal)"
  pmf_runmf feat-invalid
  pmf_check "4 valid=no refuses approver-not-valid, DEV unchanged" pmf_refused_ok approver-not-valid

  # 5. stale head: the approval names an older head than the branch tip.
  pmf_setfix "$(pmf_apv feat-stale APPROVED yes ROW-STALE-1 fixture-approver "$SHA_OLD" 1 opal-internal)"
  pmf_runmf feat-stale
  pmf_check "5 stale head refuses stale-head, DEV unchanged" pmf_refused_ok stale-head

  # 6. unreadable status: a non-zero exit, and an UNREADABLE state line.
  pmf_setfix "$(pmf_apv feat-unread APPROVED yes ROW-UNR-1 fixture-approver "$T_UNR" 1 opal-internal)" 3
  pmf_runmf feat-unread
  pmf_check "6a non-zero status exit refuses status-unreadable, DEV unchanged" pmf_refused_ok status-unreadable
  pmf_setfix "$(pmf_apv feat-unread UNREADABLE - - - - - opal-internal)"
  pmf_runmf feat-unread
  pmf_check "6b state=UNREADABLE refuses status-unreadable, DEV unchanged" pmf_refused_ok status-unreadable

  # 7. ABSENT with a product file refuses.
  pmf_setfix "$(pmf_apv feat-abs-prod ABSENT - - - - - -)"
  pmf_runmf feat-abs-prod
  pmf_check "7 ABSENT with a product file refuses no-approval-row, DEV unchanged" pmf_refused_ok no-approval-row

  # 8. ABSENT with only test files merges with the test-only trailer.
  pmf_setfix "$(pmf_apv feat-abs-test ABSENT - - - - - -)"
  pmf_runmf feat-abs-test
  pmf_check "8a ABSENT with only test files merges (MERGED line, DEV unchanged)" pmf_merged_ok
  MF="$(pmf_mf_of feat-abs-test)"; MS="$(git -C "$CLONE" rev-parse --verify -q "$MF" || echo none)"
  pmf_check "8b merge carries Approved-By: test-only @- and parents are dev_before and the tip" pmf_trailers_8b "$MS"

  # 9. a conflicting branch refuses and leaves no worktree behind.
  pmf_setfix "$(pmf_apv feat-conf APPROVED yes ROW-CONF-1 fixture-approver "$T_CONF" 1 opal-internal)"
  wtb="$(git -C "$CLONE" worktree list --porcelain | grep -c '^worktree ')"
  pmf_runmf feat-conf
  wta="$(git -C "$CLONE" worktree list --porcelain | grep -c '^worktree ')"
  pmf_check "9a conflicting branch refuses conflict, DEV unchanged" pmf_refused_ok conflict
  pmf_check "9b no worktree and no runtmp entry left behind" pmf_leftover_9b

  # 10. --push moves the temporary origin's DEV onto the merge commit.
  pmf_setfix "$(pmf_apv feat-ok APPROVED yes ROW-OK-1 fixture-approver "$T_OK" 2 opal-internal)"
  pmf_runmf feat-ok --push
  devnew="$(git -C "$ORIG" rev-parse --verify refs/heads/DEV)"
  pmf_check "10a --push result MERGED pushed=yes with dev_before the old DEV" pmf_push_10a
  pmf_check "10b origin DEV is now a merge of old DEV and the tip" pmf_origin_10b "$devnew"
  dev1="$(pmf_dev_now)"

  # 11. a second branch whose push would not fast-forward: origin's DEV moved under the local tracking ref.
  # The rejected push is the call under test (pmf_runmf --push below): a plain command, expected to fail, not an fx step.
  fx git clone -q "$ORIG" "$OTHER"
  fx git -C "$OTHER" checkout -q DEV
  fx pmf_put "$OTHER/later.txt" later
  fx git -C "$OTHER" add -A
  fx git -C "$OTHER" commit -q -m "dev later change"
  fx git -C "$OTHER" push -q origin DEV
  devnew2="$(git -C "$ORIG" rev-parse --verify refs/heads/DEV)"
  pmf_setfix "$(pmf_apv feat-ff2 APPROVED yes ROW-FF2-1 fixture-approver "$T_FF2" 1 opal-internal)"
  pmf_runmf feat-ff2 --push
  pmf_check "11a non-fast-forward push reports REFUSED push-rejected pushed=no" pmf_push_11a
  pmf_check "11b origin DEV untouched by the rejected push" pmf_origin_11b "$devnew2"

  # 12. the DEFAULT fetch (no --no-fetch) picks up a branch pushed to origin after the clone, and DEV as origin now has it.
  fx git -C "$OTHER" checkout -q -b feat-late origin/PROD
  fx mkdir -p "$OTHER/product"
  fx pmf_put "$OTHER/product/late.txt" late
  fx git -C "$OTHER" add -A
  fx git -C "$OTHER" commit -q -m "feature feat-late"
  fx git -C "$OTHER" push -q origin feat-late
  T_LATE="$(git -C "$OTHER" rev-parse --verify feat-late)"
  pmf_check "12a precondition: the clone does not know feat-late before the run" test -z "$(git -C "$CLONE" rev-parse --verify -q refs/remotes/origin/feat-late)"
  pmf_setfix "$(pmf_apv feat-late APPROVED yes ROW-LATE-1 fixture-approver "$T_LATE" 1 opal-internal)"
  PMF_RUNTMP="$PMF_TMP/runtmp" OPAL_APPROVAL_STATUS_CMD="bash $FIX" \
    bash "$PMF_SELF" feat-late --repo "$CLONE" >"$PMF_TMP/out-12.txt"
  RC=$?
  LAST="$(tail -n 1 "$PMF_TMP/out-12.txt")"
  MS="${LAST##* merge=}"
  pmf_check "12b default fetch picks up the pushed branch: MERGED, DEV read as origin now has it" pmf_fetch_12a
  pmf_check "12c the fetched merge commit has origin DEV as first parent and the pushed tip as second" pmf_parents_ok "$MS" "$devnew2" "$T_LATE"

  # 13. a local-only branch (never pushed) with an approved row: the default fetch finds it absent on origin,
  # reads the local branch with a NOTE on stderr, and merges it.
  pmf_mkfeat feat-local product/local.txt local
  fx git -C "$CLONE" fetch -q "$SEED" refs/heads/feat-local:refs/heads/feat-local
  T_LOC="$(git -C "$SEED" rev-parse --verify feat-local)"
  pmf_setfix "$(pmf_apv feat-local APPROVED yes ROW-LOC-1 fixture-approver "$T_LOC" 1 opal-internal)"
  PMF_RUNTMP="$PMF_TMP/runtmp" OPAL_APPROVAL_STATUS_CMD="bash $FIX" \
    bash "$PMF_SELF" feat-local --repo "$CLONE" >"$PMF_TMP/out-13.txt" 2>"$PMF_TMP/err-13.txt"
  RC=$?
  LAST="$(tail -n 1 "$PMF_TMP/out-13.txt")"
  MS="${LAST##* merge=}"
  pmf_localonly_13() {
    [ "$RC" -eq 0 ] || return 1
    case "$LAST" in
      *" result=MERGED reason=- dev_before=$devnew2 dev_after=$devnew2 pushed=no merge="?*) ;;
      *) return 1 ;;
    esac
    grep -qxF "NOTE: feat-local is not on origin; using the local branch" "$PMF_TMP/err-13.txt"
  }
  pmf_check "13a local-only branch under the default fetch: MERGED, NOTE on stderr" pmf_localonly_13
  pmf_check "13b the local-only merge has origin DEV as first parent and the local tip as second" pmf_parents_ok "$MS" "$devnew2" "$T_LOC"

  # 14. a branch absent on origin and locally refuses branch-not-found (not fetch-failed).
  PMF_RUNTMP="$PMF_TMP/runtmp" OPAL_APPROVAL_STATUS_CMD="bash $FIX" \
    bash "$PMF_SELF" feat-nowhere --repo "$CLONE" >"$PMF_TMP/out-14.txt" 2>"$PMF_TMP/err-14.txt"
  RC=$?
  LAST="$(tail -n 1 "$PMF_TMP/out-14.txt")"
  pmf_nowhere_14() {
    [ "$RC" -eq 1 ] || return 1
    case "$LAST" in
      *" result=REFUSED reason=branch-not-found dev_before=- dev_after=- pushed=no merge=-") return 0 ;;
    esac
    return 1
  }
  pmf_check "14 a branch absent on origin and locally refuses branch-not-found" pmf_nowhere_14

  # 15. a deliberately broken remote: the DEV fetch refuses fetch-failed.
  BROKEN="$PMF_TMP/broken"
  fx git clone -q "$ORIG" "$BROKEN"
  fx git -C "$BROKEN" remote set-url origin "$PMF_TMP/no-such-origin.git"
  PMF_RUNTMP="$PMF_TMP/runtmp" OPAL_APPROVAL_STATUS_CMD="bash $FIX" \
    bash "$PMF_SELF" feat-ok --repo "$BROKEN" >"$PMF_TMP/out-15.txt" 2>"$PMF_TMP/err-15.txt"
  RC=$?
  LAST="$(tail -n 1 "$PMF_TMP/out-15.txt")"
  pmf_broken_15() {
    [ "$RC" -eq 1 ] || return 1
    case "$LAST" in
      *" result=REFUSED reason=fetch-failed dev_before=- dev_after=- pushed=no merge=-") return 0 ;;
    esac
    return 1
  }
  pmf_check "15 a broken remote makes the DEV fetch refuse fetch-failed" pmf_broken_15

  # 16. a criss-cross history: DEV and the branch have TWO merge bases (two branches that merge each other, then a
  # branch off one of the merges). The changed-file read unions the diff over both bases: no multiple-merge-bases
  # warning, and a product file changed after the bases is seen, so the ABSENT row is refused no-approval-row.
  CRISS="$PMF_TMP/criss"
  fx git init -q "$CRISS"
  fx git -C "$CRISS" symbolic-ref HEAD refs/heads/cc-root
  fx pmf_put "$CRISS/root.txt" root
  fx git -C "$CRISS" add -A
  fx git -C "$CRISS" commit -q -m "criss root"
  fx git -C "$CRISS" checkout -q -b cc-x
  fx mkdir -p "$CRISS/src/__tests__"
  fx pmf_put "$CRISS/src/__tests__/x.test.ts" x
  fx git -C "$CRISS" add -A
  fx git -C "$CRISS" commit -q -m "criss x side"
  fx git -C "$CRISS" checkout -q cc-root
  fx git -C "$CRISS" checkout -q -b cc-y
  fx mkdir -p "$CRISS/src/__tests__"
  fx pmf_put "$CRISS/src/__tests__/y.test.ts" y
  fx git -C "$CRISS" add -A
  fx git -C "$CRISS" commit -q -m "criss y side"
  CX="$(git -C "$CRISS" rev-parse --verify cc-x)"
  fx git -C "$CRISS" checkout -q cc-x
  fx git -C "$CRISS" merge -q --no-edit cc-y
  fx git -C "$CRISS" checkout -q cc-y
  fx git -C "$CRISS" merge -q --no-edit "$CX"
  fx git -C "$CRISS" checkout -q cc-x
  fx git -C "$CRISS" checkout -q -b cc-branch
  fx mkdir -p "$CRISS/product"
  fx pmf_put "$CRISS/product/p.txt" product
  fx git -C "$CRISS" add -A
  fx git -C "$CRISS" commit -q -m "criss branch product change"
  fx git -C "$CRISS" update-ref refs/remotes/origin/DEV "$(git -C "$CRISS" rev-parse --verify cc-y)"
  devcriss="$(git -C "$CRISS" rev-parse --verify refs/remotes/origin/DEV)"
  pmf_criss_16a() { # precondition: DEV and the branch have exactly two merge bases
    [ "$(git -C "$CRISS" merge-base --all refs/remotes/origin/DEV refs/heads/cc-branch | grep -c '^[0-9a-f]')" -eq 2 ]
  }
  pmf_setfix "$(pmf_apv cc-branch ABSENT - - - - - -)"
  PMF_RUNTMP="$PMF_TMP/runtmp" OPAL_APPROVAL_STATUS_CMD="bash $FIX" \
    bash "$PMF_SELF" cc-branch --repo "$CRISS" --no-fetch >"$PMF_TMP/out-16.txt" 2>"$PMF_TMP/err-16.txt"
  RC=$?
  LAST="$(tail -n 1 "$PMF_TMP/out-16.txt")"
  pmf_criss_16b() { # no multiple-merge-bases text on stderr
    ! grep -q "multiple merge bases" "$PMF_TMP/err-16.txt"
  }
  pmf_criss_16c() { # the product file after the bases is seen: refused no-approval-row, DEV unchanged
    [ "$RC" -eq 1 ] || return 1
    case "$LAST" in
      *" result=REFUSED reason=no-approval-row dev_before=$devcriss dev_after=$devcriss pushed=no merge=-") return 0 ;;
    esac
    return 1
  }
  pmf_check "16a precondition: the criss-cross branch has exactly two merge bases" pmf_criss_16a
  pmf_check "16b the criss-cross run prints no multiple-merge-bases warning" pmf_criss_16b
  pmf_check "16c a product file after the bases is seen: ABSENT refuses no-approval-row, DEV unchanged" pmf_criss_16c

  local okflag=False
  if [ "$K" -eq "$N" ]; then okflag=True; fi
  echo "MERGE-FORWARD-SELFTEST cases=$K/$N ok=$okflag"
  if [ "$okflag" = True ]; then exit 0; fi
  exit 1
}

PMF_TMP=""
if [ "${1:-}" = "--selftest" ]; then
  pmf_selftest
fi
pmf_run "$@"
