#!/usr/bin/env bash
# box-sync.sh -- the per-box branch passes as a PROGRAM, with no worktree and no open merge in any shared tree.
#
# Andrew-direct 2026-10-08 ~19:5xZ, verbatim in
# org/tier1_exec/4.0.0_SA_CRO~A/deliverables/ANDREW_DIRECT_20261008_195xZ_LAPTOP_TO_BOX_BRANCH_PROGRAMMATIC_PULLS.md:
# "we need to figure out how we manage pulls to the respective box branches from the main CLOUD branch. I think this
# should be programmatic. ... having Laptop MSTR running the merges all the time is ok ... as long as it doesnt cause any
# delay on the laptop ops. im trying to effectively abstract away the issues with the constant merging".
# Design: org/tier1_exec/4.0.0_SA_CRO~A/deliverables/PER_BOX_BRANCH_DESIGN_20261008.md; merge grading per
# MERGE_ROOT_CAUSE_B3_20261008.md (Andrew ~19:1xZ: grade only what a merge introduces). Owner: 4.0.0_SA_CRO~A.
#
# USAGE (an MSTR serial only -- OPAL_AGENT_SERIAL, else the session serial file):
#   bash .tools/box-sync.sh box        [--dry-run]   take origin/CLOUD into box/<this box>, then push box/<this box>
#   bash .tools/box-sync.sh integrate  [--dry-run]   merge every origin/box/* that is ahead into CLOUD, then push CLOUD
#   bash .tools/box-sync.sh status     [--fetch]     ANY seat, read-only: each box branch behind/ahead of CLOUD
#
# HOW IT AVOIDS SUFFOCATING THE BOX: each merge is computed in the object store (`git merge-tree --write-tree`), graded on
# a PRIVATE index in a private git dir (HEAD and MERGE_HEAD pinned to the two parents, over the shared files), and written
# with `git commit-tree`. Nothing opens a merge in the shared tree, and nothing checks out a worktree. The only act that
# touches the shared tree is `box` mode's land: under the SAME lock safe-commit lands under, it moves the box branch
# from P1 to the merge (compare-and-swap) and updates the files that the trunk changed (`git read-tree -m -u`, the
# fast-forward rule: it refuses rather than overwrite a seat's uncommitted edit). `integrate` mode never touches a
# working tree at all.
#
# EXIT: 0 done (or nothing to do); 1 refused or failed (nothing landed); 3 contention (skipped, the next slot retries);
#       4 HELD: a conflict needs a person or seat (logged; the other boxes proceed in integrate mode).
# Every run appends one BOX-SYNC row to org/git-author-override-audit.log.

set -uo pipefail
MODE="${1:-}"; DRY=0
[ "${2:-}" = "--dry-run" ] && DRY=1
case "$MODE" in box|integrate|status) ;; *) echo "usage: box-sync.sh box|integrate [--dry-run] | status [--fetch]" >&2; exit 2 ;; esac

ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || { echo "box-sync: not in a git repo" >&2; exit 2; }
cd "$ROOT" || exit 2

# STATUS (read-only, any seat): where every box branch stands against CLOUD, read from git, because each box's BOX-SYNC
# rows live in that box's own untracked audit log and no other box can read them. A box still BEHIND CLOUD after its slot
# is a held or skipped pass. Reads the remote-tracking refs as last fetched; --fetch fetches origin first.
if [ "$MODE" = status ]; then
  [ "${2:-}" = "--fetch" ] && { git fetch -q origin || { echo "box-sync status: fetch failed" >&2; exit 1; }; }
  cl="$(git rev-parse -q --verify refs/remotes/origin/CLOUD)" || { echo "box-sync status: origin/CLOUD unreadable" >&2; exit 1; }
  echo "origin/CLOUD $(git log -1 --format='%h %cI' "$cl")"
  n=0
  for r in $(git for-each-ref --format='%(refname)' refs/remotes/origin/box/); do
    took="$(git log -1 --first-parent --format='%cI %h' --grep='^box-sync(.*take CLOUD' "$r")"
    printf '%-12s tip %s  behind CLOUD %s  ahead of CLOUD %s  last take of CLOUD: %s
' "${r#refs/remotes/origin/}"       "$(git log -1 --format='%h %cI' "$r")" "$(git rev-list --count "$r..$cl")" "$(git rev-list --count "$cl..$r")" "${took:-none}"
    n=$((n + 1))
  done
  echo "box branches read: $n"
  exit 0
fi
GITDIR="$(git rev-parse --path-format=absolute --git-dir)"
COMMON="$(git rev-parse --path-format=absolute --git-common-dir)"
AUDIT="${COMMON}/../org/git-author-override-audit.log"
GATE="$ROOT/.tools/surprise-row-gate.py"
SAFE_MERGE="$ROOT/.tools/safe-merge.sh"
T0="${EPOCHREALTIME:-0}"
NOW_TS() { date -u +%Y-%m-%dT%H:%M:%SZ; }
secs() { local a="${1/[.,]/}" b="${EPOCHREALTIME:-0}"; b="${b/[.,]/}"; local d=$(( (10#$b - 10#$a) / 10000 )); printf '%d.%02d' $((d / 100)) $((d % 100)); }
ROWNOTE=""
row() {
  # the GITSTATE record (NFRA_MCPORTAL FWD-16, owner 4.0.0_SA_CRO): every non-dry pass, in the background so it costs the pass nothing
  [ "$DRY" -eq 0 ] && [ -f "$ROOT/.tools/fabric-gitstate.py" ] && \
    ( python "$ROOT/.tools/fabric-gitstate.py" --mode "$MODE" --rc "$1" --serial "${SERIAL:-unknown}" --note "${ROWNOTE}" >> "${GITDIR}/fabric-gitstate.log" 2>&1 & )
  [ -d "$(dirname "$AUDIT")" ] || return 0; echo "$(NOW_TS) BOX-SYNC  ${SERIAL:-unknown}  mode=${MODE}  rc=$1  secs=$(secs "$T0")  ${ROWNOTE}" >> "$AUDIT" 2>/dev/null || true; }

# --- who: an MSTR serial only (box and CLOUD are shared branches; GATE 5 of never-rules-gate.sh, LD-0367/0368)
SERIAL="${OPAL_AGENT_SERIAL:-}"
if [ -z "$SERIAL" ] && [ -n "${CLAUDE_CODE_SESSION_ID:-}" ] && [ -f "$ROOT/org/mcp/sessions/${CLAUDE_CODE_SESSION_ID}.serial" ]; then
  read -r SERIAL < "$ROOT/org/mcp/sessions/${CLAUDE_CODE_SESSION_ID}.serial" || true
fi
_mstr_re='^0\.0\.0_AB_MSTR(~[A-Za-z0-9]+)?$'
if ! [[ "$SERIAL" =~ $_mstr_re ]] && [ "$DRY" -eq 0 ]; then
  echo "box-sync: REFUSED -- only an MSTR serial runs a pass (got '${SERIAL:-unset}'). --dry-run is open to any seat." >&2
  ROWNOTE="refused=not-mstr"; row 1; exit 1
fi
export GIT_AUTHOR_NAME="${SERIAL:-box-sync}" GIT_AUTHOR_EMAIL="${SERIAL:-box-sync}@opal.agent"

# --- skip, never overlap
PASSLOCK="${COMMON}/box-sync-${MODE}.lock.d"
if ! mkdir "$PASSLOCK" 2>/dev/null; then
  _hp=""; [ -f "$PASSLOCK/pid" ] && read -r _hp < "$PASSLOCK/pid"
  if [ -n "$_hp" ] && kill -0 "$_hp" 2>/dev/null; then
    echo "box-sync: SKIP -- a ${MODE} pass is still running (pid $_hp); this slot is skipped, never overlapped."
    ROWNOTE="skipped=overlap holder=$_hp"; row 3; exit 3
  fi
  rm -rf "$PASSLOCK"; mkdir "$PASSLOCK" 2>/dev/null || { ROWNOTE="skipped=passlock"; row 3; exit 3; }
fi
echo "$$" > "$PASSLOCK/pid"
PRIV=""
cleanup() { rm -rf "$PASSLOCK" 2>/dev/null; [ -n "$PRIV" ] && rm -rf "$PRIV" 2>/dev/null; return 0; }
trap cleanup EXIT

git fetch -q origin 2>/dev/null || { echo "box-sync: git fetch origin failed -- nothing done" >&2; ROWNOTE="fetch=failed"; row 1; exit 1; }

# grade_merge P1 P2 T -> 0 pass, 1 refused. Path-scoped: paths T changes against BOTH parents, plus paths both sides
# changed since the merge base; the row gate reads them from a private index in a private git dir pinned to the merge.
grade_merge() {
  local p1="$1" p2="$2" t="$3" mb paths n
  mb="$(git merge-base "$p1" "$p2" 2>/dev/null || echo '')"
  paths="$( { LC_ALL=C comm -12 <(git diff --name-only "$p1" "$t" | LC_ALL=C sort -u) <(git diff --name-only "$p2" "$t" | LC_ALL=C sort -u)
              [ -n "$mb" ] && LC_ALL=C comm -12 <(git diff --name-only "$mb" "$p1" | LC_ALL=C sort -u) <(git diff --name-only "$mb" "$p2" | LC_ALL=C sort -u); } \
            | LC_ALL=C sort -u | sed '/^$/d' )"
  n="$(printf '%s\n' "$paths" | sed '/^$/d' | wc -l | tr -d ' ')"
  GRADED_NOTE="graded=${n}/$(git diff --name-only "$p1" "$t" | wc -l | tr -d ' ')"
  [ "$n" -eq 0 ] && { echo "box-sync: grade SKIP -- the merge introduces nothing and no path changed on both sides"; return 0; }
  [ -f "$GATE" ] || { echo "box-sync: REFUSED -- $n path(s) to grade but $GATE is missing" >&2; return 1; }
  PRIV="${GITDIR}/box-sync-${EPOCHSECONDS:-0}-$$"
  mkdir -p "$PRIV" && printf '%s\n' "$p1" > "$PRIV/HEAD" && printf '%s\n' "$p2" > "$PRIV/MERGE_HEAD" && printf '%s\n' "$COMMON" > "$PRIV/commondir" || return 1
  GIT_DIR="$PRIV" GIT_WORK_TREE="$ROOT" git read-tree "$t" || { rm -rf "$PRIV"; PRIV=""; return 1; }
  local rc=0
  # shellcheck disable=SC2086
  STAGED="$paths" GIT_DIR="$PRIV" GIT_WORK_TREE="$ROOT" ROOT="$ROOT" python "$GATE" || rc=$?
  rm -rf "$PRIV"; PRIV=""
  [ "$rc" -eq 0 ] || echo "box-sync: REFUSED BY THE ROW GATE on the merge's own paths (rc=$rc)" >&2
  return "$rc"
}

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

# make_merge P1 P2 MESSAGE -> sets MERGE_OUT (the merge commit) and GRADED_NOTE; rc 4 on conflict, 1 on refusal.
# Called directly, never inside $( ): a subshell would lose GRADED_NOTE and the private dir path the EXIT trap cleans.
MERGE_OUT=""; GRADED_NOTE=""
make_merge() {
  local p1="$1" p2="$2" msg="$3" out t m
  MERGE_OUT=""
  out="$(git merge-tree --write-tree --no-messages "$p1" "$p2" 2>/dev/null)"; local mrc=$?
  t="$(printf '%s\n' "$out" | head -1)"
  if [ "$mrc" -eq 1 ]; then
    # a conflict: resolve it here when it is only the known multi-writer classes (O6), else HOLD as before
    t="$(resolve_known "$p1" "$p2" "$t")" || return 4
    echo "box-sync: the conflict was only known multi-writer files -- resolved without a worktree" >&2
    mrc=0
  fi
  if [ "$mrc" -ne 0 ] || [ -z "$t" ]; then echo "box-sync: git merge-tree failed (rc=$mrc)" >&2; return 1; fi
  grade_merge "$p1" "$p2" "$t" >&2 || return 1
  m="$(git commit-tree "$t" -p "$p1" -p "$p2" -m "$msg")" || return 1
  bash "$SAFE_MERGE" --verify-merge "$m" >&2 || { echo "box-sync: REFUSED -- the tree check failed on $m" >&2; return 1; }
  MERGE_OUT="$m"
}

# ============================================================== integrate: every box branch into CLOUD
if [ "$MODE" = "integrate" ]; then
  C0="$(git rev-parse --verify -q refs/remotes/origin/CLOUD)" || { ROWNOTE="no-origin-CLOUD"; row 1; exit 1; }
  C="$C0"; DONE=""; HELD=""
  for r in $(git for-each-ref --format='%(refname:short)' refs/remotes/origin/box/); do
    tip="$(git rev-parse "$r")"
    git merge-base --is-ancestor "$tip" "$C" && continue
    GRADED_NOTE=""
    if make_merge "$C" "$tip" "integrate(${SERIAL}): ${r#origin/} @${tip:0:10} into CLOUD (box-sync)"; then
      C="$MERGE_OUT"; DONE="${DONE}${DONE:+,}${r#origin/}(${GRADED_NOTE})"
    else
      _mrc=$?
      HELD="${HELD}${HELD:+,}${r#origin/}$([ "$_mrc" -eq 4 ] && echo ':conflict' || echo ':refused')"
      echo "box-sync: HELD ${r#origin/} -- $([ "$_mrc" -eq 4 ] && echo 'it conflicts with CLOUD; that box resolves it in its next box pass' || echo 'refused, see above'). The other boxes go on."
    fi
  done
  ROWNOTE="merged=(${DONE:-none}) held=(${HELD:-none})"
  if [ "$C" = "$C0" ]; then echo "box-sync: integrate -- nothing to merge"; row "$([ -n "$HELD" ] && echo 4 || echo 0)"; [ -n "$HELD" ] && exit 4; exit 0; fi
  if [ "$DRY" -eq 1 ]; then echo "box-sync: DRY RUN -- would push CLOUD ${C0:0:10} -> ${C:0:10}: $ROWNOTE"; ROWNOTE="dry-run $ROWNOTE"; row 0; exit 0; fi
  if ! git push -q origin "${C}:refs/heads/CLOUD"; then
    echo "box-sync: push of CLOUD was refused (a writer outside the integrator moved it?) -- nothing landed; the next pass retries" >&2
    ROWNOTE="push=refused $ROWNOTE"; row 3; exit 3
  fi
  echo "box-sync: integrate -- CLOUD ${C0:0:10} -> ${C:0:10} pushed; $ROWNOTE"
  ROWNOTE="pushed=${C:0:10} $ROWNOTE"; row "$([ -n "$HELD" ] && echo 4 || echo 0)"
  [ -n "$HELD" ] && exit 4; exit 0
fi

# ============================================================== box: take CLOUD into box/<this box>, push it
BOX="${AGENTBUS_DEVICE:-}"
[ -n "$BOX" ] || BOX="$(bash "$ROOT/.tools/agentbus-sqs.sh" device 2>/dev/null | sed -n 's/^device: *//p' | head -1)"
[ -n "$BOX" ] && [ "$BOX" != "UNKNOWN" ] || { echo "box-sync: REFUSED -- this box's name is unknown (AGENTBUS_DEVICE)" >&2; ROWNOTE="box=unknown"; row 1; exit 1; }
B="box/$BOX"
CUR_BR="$(git symbolic-ref -q --short HEAD 2>/dev/null || echo '')"
[ "$CUR_BR" = "$B" ] || { echo "box-sync: REFUSED -- this shared tree is on '${CUR_BR:-detached}', not $B: the box has not switched" >&2; ROWNOTE="not-switched=${CUR_BR:-detached}"; row 1; exit 1; }
CLOUD_TIP="$(git rev-parse --verify -q refs/remotes/origin/CLOUD)" || { ROWNOTE="no-origin-CLOUD"; row 1; exit 1; }
LOCK_DIR="${GITDIR}/commit-queue.lock"   # the lock safe-commit lands under (legacy and two-phase)
TOOK="none"
for attempt in 1 2 3; do
  P1="$(git rev-parse "refs/heads/$B")"
  if git merge-base --is-ancestor "$CLOUD_TIP" "$P1"; then TOOK="already-current"; break; fi
  GRADED_NOTE=""
  make_merge "$P1" "$CLOUD_TIP" "box-sync(${SERIAL}): take CLOUD @${CLOUD_TIP:0:10} into ${B}"; mrc=$?; M="$MERGE_OUT"
  if [ "$mrc" -eq 4 ]; then
    echo "box-sync: HELD -- CLOUD @${CLOUD_TIP:0:10} conflicts with ${B}. Resolve with the /integrate BOX PASS (safe-merge in a drain worktree); nothing landed."
    ROWNOTE="held=conflict cloud=${CLOUD_TIP:0:10}"; row 4; exit 4
  fi
  [ "$mrc" -eq 0 ] || { ROWNOTE="refused ${GRADED_NOTE}"; row 1; exit 1; }
  if [ "$DRY" -eq 1 ]; then echo "box-sync: DRY RUN -- would move $B ${P1:0:10} -> ${M:0:10} (${GRADED_NOTE}) and push"; ROWNOTE="dry-run ${GRADED_NOTE}"; row 0; exit 0; fi
  # LAND under the commit lock: seconds, the only shared-tree act.
  _w=0
  until mkdir "$LOCK_DIR" 2>/dev/null; do
    _hp=""; [ -f "$LOCK_DIR/pid" ] && read -r _hp < "$LOCK_DIR/pid" 2>/dev/null
    if [ -n "$_hp" ] && ! kill -0 "$_hp" 2>/dev/null; then rm -rf "$LOCK_DIR"; continue; fi
    _w=$((_w + 1)); [ "$_w" -ge 120 ] && { echo "box-sync: the commit lock stayed busy 120 s -- skipped; the next slot retries"; ROWNOTE="skipped=lock-busy"; row 3; exit 3; }
    sleep 1
  done
  echo "$$" > "$LOCK_DIR/pid"; _TL="${EPOCHREALTIME:-0}"
  if [ "$(git rev-parse "refs/heads/$B")" != "$P1" ]; then
    rm -rf "$LOCK_DIR"; echo "box-sync: a seat committed to $B while the merge was graded -- rebuilding on the new tip (attempt $attempt)"; continue
  fi
  git update-index -q --refresh >/dev/null 2>&1 || true   # stale stat data must not read as a seat's edit
  if ! git read-tree -m -u "$P1" "$M"; then
    rm -rf "$LOCK_DIR"
    echo "box-sync: HELD -- updating the shared tree would overwrite a seat's uncommitted edit of a path CLOUD changed. Nothing landed; the next slot retries after that seat commits."
    ROWNOTE="held=dirty-overlap ${GRADED_NOTE}"; row 4; exit 4
  fi
  if ! git update-ref -m "box-sync: take CLOUD @${CLOUD_TIP:0:10}" "refs/heads/$B" "$M" "$P1"; then
    git read-tree -m -u "$M" "$P1" 2>/dev/null; rm -rf "$LOCK_DIR"
    echo "box-sync: the branch moved under the lock -- the shared tree was put back; nothing landed" >&2; ROWNOTE="cas=failed"; row 3; exit 3
  fi
  rm -rf "$LOCK_DIR"
  TOOK="${CLOUD_TIP:0:10} hold=$(secs "$_TL")s ${GRADED_NOTE}"
  break
done
[ "$TOOK" = "none" ] && { ROWNOTE="took=none (3 attempts lost the race)"; row 3; exit 3; }
if [ "$DRY" -eq 1 ]; then echo "box-sync: DRY RUN -- $B already holds CLOUD; would push $B"; ROWNOTE="dry-run took=$TOOK"; row 0; exit 0; fi
if [ "$(git rev-parse "refs/heads/$B")" != "$(git rev-parse -q --verify "refs/remotes/origin/$B" 2>/dev/null || echo none)" ]; then
  git push -q origin "$B" || { echo "box-sync: push of $B failed -- the branch is current locally; the next slot pushes" >&2; ROWNOTE="took=$TOOK push=failed"; row 3; exit 3; }
fi
echo "box-sync: box -- $B took CLOUD (${TOOK}) and is pushed"
ROWNOTE="took=$TOOK pushed=$(git rev-parse --short=10 "refs/heads/$B")"; row 0; exit 0
