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
#   bash .tools/box-sync.sh grade P1 P2              ANY seat, read-only: merge P1 and P2 in the object store and grade the
#                                                    merge exactly as a pass would (row gate + scoped tree check); lands nothing,
#                                                    moves no ref, no fetch, no lock, no audit row. EXIT 0 pass, 1 refused, 4 conflict
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
case "$MODE" in box|integrate|status|grade) ;; *) echo "usage: box-sync.sh box|integrate [--dry-run] | status [--fetch] | grade P1 P2" >&2; exit 2 ;; esac

ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || { echo "box-sync: not in a git repo" >&2; exit 2; }
cd "$ROOT" || exit 2
. "$ROOT/.tools/merged-checker.sh" || { echo "box-sync: cannot source .tools/merged-checker.sh" >&2; exit 2; }

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
case "${AGENTBUS_DEVICE:-}" in ""|*[!a-z0-9-]*) GAO_REL="org/git-author-override-audit.log" ;; *) GAO_REL="org/git-author-override-audit.${AGENTBUS_DEVICE}.log" ;; esac  # one file per box (shape (a), MSTR consensus 2026-10-11); unset device -> legacy shared file
AUDIT="${COMMON}/../$GAO_REL"
GATE="$ROOT/.tools/surprise-row-gate.py"
SAFE_MERGE="$ROOT/.tools/safe-merge.sh"
T0="${EPOCHREALTIME:-0}"
NOW_TS() { date -u +%Y-%m-%dT%H:%M:%SZ; }
secs() { local a="${1/[.,]/}" b="${EPOCHREALTIME:-0}"; b="${b/[.,]/}"; local d=$(( (10#$b - 10#$a) / 10000 )); printf '%d.%02d' $((d / 100)) $((d % 100)); }
ROWNOTE=""
# PHASES (CTO ruling 3 @ba20ac668b): per-phase seconds on every BOX-SYNC row -- t_fetch, t_merge_<box> (integrate) or
# t_merge_cloud (box), t_land, t_push -- so a slow pass names its slow phase. A retried integrate tags its later attempts aN.
PHASES=""
row() {
  # the GITSTATE record (NFRA_MCPORTAL FWD-16, owner 4.0.0_SA_CRO): every non-dry pass, in the background so it costs the pass nothing
  [ "$DRY" -eq 0 ] && [ -f "$ROOT/.tools/fabric-gitstate.py" ] && \
    ( python "$ROOT/.tools/fabric-gitstate.py" --mode "$MODE" --rc "$1" --serial "${SERIAL:-unknown}" --note "${ROWNOTE}" >> "${GITDIR}/fabric-gitstate.log" 2>&1 & )
  [ -d "$(dirname "$AUDIT")" ] || return 0; echo "$(NOW_TS) BOX-SYNC  ${SERIAL:-unknown}  mode=${MODE}  rc=$1  secs=$(secs "$T0")  ${ROWNOTE}${PHASES:+  phases:${PHASES}}" >> "$AUDIT" 2>/dev/null || true; }

# --- who: an MSTR serial only (box and CLOUD are shared branches; GATE 5 of never-rules-gate.sh, LD-0367/0368)
SERIAL="${OPAL_AGENT_SERIAL:-}"
if [ -z "$SERIAL" ] && [ -n "${CLAUDE_CODE_SESSION_ID:-}" ] && [ -f "$ROOT/org/mcp/sessions/${CLAUDE_CODE_SESSION_ID}.serial" ]; then
  read -r SERIAL < "$ROOT/org/mcp/sessions/${CLAUDE_CODE_SESSION_ID}.serial" || true
fi
_mstr_re='^0\.0\.0_AB_MSTR(~[A-Za-z0-9]+)?$'
if ! [[ "$SERIAL" =~ $_mstr_re ]] && [ "$DRY" -eq 0 ] && [ "$MODE" != grade ]; then
  echo "box-sync: REFUSED -- only an MSTR serial runs a pass (got '${SERIAL:-unset}'). --dry-run is open to any seat." >&2
  ROWNOTE="refused=not-mstr"; row 1; exit 1
fi
export GIT_AUTHOR_NAME="${SERIAL:-box-sync}" GIT_AUTHOR_EMAIL="${SERIAL:-box-sync}@opal.agent"

# --- skip, never overlap
PASSLOCK="${COMMON}/box-sync-${MODE}.lock.d"
if [ "$MODE" = grade ]; then PASSLOCK=""   # grade is read-only and takes no lock: any number may run beside a pass
elif ! mkdir "$PASSLOCK" 2>/dev/null; then
  _hp=""; [ -f "$PASSLOCK/pid" ] && read -r _hp < "$PASSLOCK/pid"
  if [ -n "$_hp" ] && kill -0 "$_hp" 2>/dev/null; then
    echo "box-sync: SKIP -- a ${MODE} pass is still running (pid $_hp); this slot is skipped, never overlapped."
    ROWNOTE="skipped=overlap holder=$_hp"; row 3; exit 3
  fi
  rm -rf "$PASSLOCK"; mkdir "$PASSLOCK" 2>/dev/null || { ROWNOTE="skipped=passlock"; row 3; exit 3; }
fi
[ -n "$PASSLOCK" ] && echo "$$" > "$PASSLOCK/pid"
PRIV=""
cleanup() { [ -n "$PASSLOCK" ] && rm -rf "$PASSLOCK" 2>/dev/null; [ -n "$PRIV" ] && rm -rf "$PRIV" 2>/dev/null; return 0; }
trap cleanup EXIT

_tf="${EPOCHREALTIME:-0}"
[ "$MODE" = grade ] || git fetch -q origin 2>/dev/null || { echo "box-sync: git fetch origin failed -- nothing done" >&2; ROWNOTE="fetch=failed"; row 1; exit 1; }
[ "$MODE" = grade ] || PHASES=" t_fetch=$(secs "$_tf")s"

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
  local nst=0 so
  if [ "$n" -eq 0 ]; then
    echo "box-sync: grade SKIP -- the merge introduces nothing and no path changed on both sides"
    _standing_priv "$p1" "$p2" "$t" || return 1
    so="$(_standing_run tree; _standing_run corpus)"; _standing_cleanup
    [ -n "$so" ] && printf '%s
' "$so"
    nst="$(printf '%s
' "$so" | grep -c '^STANDING ')"
    echo "box-sync: ${nst} standing"; return 0
  fi
  [ -f "$GATE" ] || { echo "box-sync: REFUSED -- $n path(s) to grade but $GATE is missing" >&2; return 1; }
  _standing_priv "$p1" "$p2" "$t" || return 1
  local rc=0 gout tout cout="" chk
  # shellcheck disable=SC2086
  gout="$(STAGED="$paths" GIT_DIR="$PRIV" GIT_WORK_TREE="$ROOT" ROOT="$ROOT" python "$GATE" 2>&1)" || rc=$?
  [ -n "$gout" ] && printf '%s
' "$gout"
  if [ "$rc" -ne 0 ]; then
    _standing_cleanup
    echo "box-sync: REFUSED BY THE ROW GATE on the merge's own paths (rc=$rc)" >&2
    return "$rc"
  fi
  # the project-tree check (GS-t-3), on the same merged bytes in the same private git dir, scoped to the merge's graded
  # path set: it refuses only a violation in a project those paths touch and prints every other one as STANDING.
  chk="$(merged_checker_path "$PRIV" "$ROOT")" || { _standing_cleanup; echo "box-sync: REFUSED -- no merged checker for the tree check (see merged-checker above)" >&2; return 1; }
  tout="$(GRADE_ACT="$paths" GIT_DIR="$PRIV" GIT_WORK_TREE="$ROOT" python "$chk" check --staged --act-from-env GRADE_ACT 2>&1)" || rc=$?
  [ -n "$tout" ] && printf '%s
' "$tout"
  # the corpus pass runs inside the row gate only when a channel path is in the set; otherwise show its standing view.
  if [ "$rc" -eq 0 ] && ! printf '%s
' "$paths" | grep -q 'surprise-channel/'; then
    cout="$(_standing_run corpus)"
    [ -n "$cout" ] && printf '%s
' "$cout"
  fi
  _standing_cleanup
  [ "$rc" -eq 0 ] || { echo "box-sync: REFUSED BY THE TREE CHECK on the merge's own paths (rc=$rc)" >&2; return "$rc"; }
  nst="$(printf '%s
%s
%s
' "$gout" "$tout" "$cout" | grep -c '^STANDING ')"
  echo "box-sync: ${nst} standing"
  return 0
}

# private GIT_DIR pinned to the merge (PRIV), index read from T.
_standing_priv() {
  PRIV="${GITDIR}/box-sync-${EPOCHSECONDS:-0}-$$"
  mkdir -p "$PRIV" && printf '%s
' "$1" > "$PRIV/HEAD" && printf '%s
' "$2" > "$PRIV/MERGE_HEAD" && printf '%s
' "$COMMON" > "$PRIV/commondir" || return 1
  GIT_DIR="$PRIV" GIT_WORK_TREE="$ROOT" git read-tree "$3" || { rm -rf "$PRIV"; PRIV=""; return 1; }
}
_standing_cleanup() { [ -n "$PRIV" ] && rm -rf "$PRIV"; PRIV=""; return 0; }
# information pass: act = this script (belongs to no project, no channel); exit codes never refuse.
_standing_run() {
  local tool="$1" out rc=0 chk
  if [ "$tool" = tree ]; then
    chk="$(merged_checker_path "$PRIV" "$ROOT")" || { echo "box-sync: WARN standing pass could not run (tree: no merged checker)"; return 0; }
    out="$(GIT_DIR="$PRIV" GIT_WORK_TREE="$ROOT" python "$chk" check --staged --act .tools/box-sync.sh 2>&1)" || rc=$?
  else
    out="$(GIT_DIR="$PRIV" GIT_WORK_TREE="$ROOT" ROOT="$ROOT" python "$ROOT/.tools/surprise-corpus-validate.py" --act .tools/box-sync.sh 2>&1)" || rc=$?
  fi
  printf '%s
' "$out" | grep '^STANDING '
  if ! printf '%s
' "$out" | grep -q '^STANDING ' && [ "$rc" -ne 0 ]; then
    echo "box-sync: WARN standing pass could not run (${tool} rc=${rc})"
  fi
  return 0
}

# resolve_known P1 P2 T0 -> prints the resolved tree when EVERY conflicted path is a known multi-writer class (a surprise-
# channel section union, a regenerated generated index entry, or an append-only log: .tools/merge-resolve-known.py);
# returns 1 otherwise. CLOUD_SIDE (ours in integrate, theirs in box) tells an append-only log which tail is CLOUD's.
# The conflicted paths come from `git merge-tree --name-only`; T0 is the tree it wrote (markers and all).
resolve_known() {
  local p1="$1" p2="$2" t0="$3" mb res idx k path blob how mode tr
  local -a cps=()
  while IFS= read -r path; do [ -n "$path" ] && cps+=("$path"); done < <(git merge-tree --write-tree --name-only --no-messages "$p1" "$p2" 2>/dev/null | tail -n +2)
  [ "${#cps[@]}" -gt 0 ] || return 1
  mb="$(git merge-base "$p1" "$p2" 2>/dev/null)" || return 1
  res="$(python "$ROOT/.tools/merge-resolve-known.py" --base "$mb" --ours "$p1" --theirs "$p2" --tree "$t0" --cloud "$CLOUD_SIDE" "${cps[@]}" 2>&1)" \
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
MERGE_OUT=""; GRADED_NOTE=""; MERGED_TREE=""; CLOUD_SIDE="ours"
# merge_tree_of P1 P2 -> sets MERGED_TREE (the merge's tree); rc 4 on a conflict beyond the known classes, 1 on failure.
merge_tree_of() {
  local p1="$1" p2="$2" out t
  MERGED_TREE=""
  out="$(git merge-tree --write-tree --no-messages "$p1" "$p2" 2>/dev/null)"; local mrc=$?
  t="$(printf '%s\n' "$out" | head -1)"
  if [ "$mrc" -eq 1 ]; then
    # a conflict: resolve it here when it is only the known multi-writer classes (O6), else HOLD as before
    t="$(resolve_known "$p1" "$p2" "$t")" || return 4
    echo "box-sync: the conflict was only known multi-writer files -- resolved without a worktree" >&2
    mrc=0
  fi
  if [ "$mrc" -ne 0 ] || [ -z "$t" ]; then echo "box-sync: git merge-tree failed (rc=$mrc)" >&2; return 1; fi
  MERGED_TREE="$t"
}
make_merge() {
  local p1="$1" p2="$2" msg="$3" t m
  MERGE_OUT=""
  merge_tree_of "$p1" "$p2" || return $?
  t="$MERGED_TREE"
  grade_merge "$p1" "$p2" "$t" >&2 || return 1
  m="$(git commit-tree "$t" -p "$p1" -p "$p2" -m "$msg")" || return 1
  bash "$SAFE_MERGE" --verify-merge "$m" >&2 || { echo "box-sync: REFUSED -- the tree check failed on $m" >&2; return 1; }
  MERGE_OUT="$m"
}

# ============================================================== grade: read-only, any seat -- merge P1 and P2 and grade it
if [ "$MODE" = "grade" ]; then
  G1="$(git rev-parse --verify -q "${2:-}^{commit}")" && G2="$(git rev-parse --verify -q "${3:-}^{commit}")" \
    || { echo "usage: box-sync.sh grade P1 P2   (two commits)" >&2; exit 2; }
  _grc=0; merge_tree_of "$G1" "$G2" || _grc=$?
  [ "$_grc" -eq 4 ] && { echo "box-sync: grade -- HELD: the merge conflicts beyond the known multi-writer classes" >&2; exit 4; }
  [ "$_grc" -eq 0 ] || exit 1
  _grc=0; grade_merge "$G1" "$G2" "$MERGED_TREE" || _grc=$?
  echo "box-sync: grade ${G1:0:10} + ${G2:0:10} -> $([ "$_grc" -eq 0 ] && echo PASS || echo REFUSED) (${GRADED_NOTE:-graded=?}); nothing landed, no ref moved"
  exit "$_grc"
fi

# ============================================================== integrate: every box branch into CLOUD
if [ "$MODE" = "integrate" ]; then
  # A REFUSED PUSH IS RETRIED IN THE SAME PASS (CTO ruling 3 @ba20ac668b), as box mode already does: re-fetch, rebuild every
  # merge on the new origin/CLOUD, push again -- at most twice more. Before, one refusal cost the whole slot.
  for _att in 1 2 3; do
    _ap=""; [ "$_att" -gt 1 ] && _ap="a${_att}."
    C0="$(git rev-parse --verify -q refs/remotes/origin/CLOUD)" || { ROWNOTE="no-origin-CLOUD"; row 1; exit 1; }
    C="$C0"; DONE=""; HELD=""
    for r in $(git for-each-ref --format='%(refname:short)' refs/remotes/origin/box/); do
      tip="$(git rev-parse "$r")"
      git merge-base --is-ancestor "$tip" "$C" && continue
      GRADED_NOTE=""; _tm="${EPOCHREALTIME:-0}"
      if make_merge "$C" "$tip" "integrate(${SERIAL}): ${r#origin/} @${tip:0:10} into CLOUD (box-sync)"; then
        C="$MERGE_OUT"; DONE="${DONE}${DONE:+,}${r#origin/}(${GRADED_NOTE})"
      else
        _mrc=$?
        HELD="${HELD}${HELD:+,}${r#origin/}$([ "$_mrc" -eq 4 ] && echo ':conflict' || echo ':refused')"
        echo "box-sync: HELD ${r#origin/} -- $([ "$_mrc" -eq 4 ] && echo 'it conflicts with CLOUD; that box resolves it in its next box pass (one owner repairs: the seat owning the broken file lane, on its own box; an ANY path, the integrator box)' || echo 'refused, see above'). The other boxes go on."
      fi
      PHASES="${PHASES} ${_ap}t_merge_${r#origin/box/}=$(secs "$_tm")s"
    done
    ROWNOTE="merged=(${DONE:-none}) held=(${HELD:-none})$([ "$_att" -gt 1 ] && echo " attempt=${_att}")"
    if [ "$C" = "$C0" ]; then echo "box-sync: integrate -- nothing to merge"; row "$([ -n "$HELD" ] && echo 4 || echo 0)"; [ -n "$HELD" ] && exit 4; exit 0; fi
    if [ "$DRY" -eq 1 ]; then echo "box-sync: DRY RUN -- would push CLOUD ${C0:0:10} -> ${C:0:10}: $ROWNOTE"; ROWNOTE="dry-run $ROWNOTE"; row 0; exit 0; fi
    _tp="${EPOCHREALTIME:-0}"
    if git push -q origin "${C}:refs/heads/CLOUD"; then
      PHASES="${PHASES} ${_ap}t_push=$(secs "$_tp")s"
      echo "box-sync: integrate -- CLOUD ${C0:0:10} -> ${C:0:10} pushed; $ROWNOTE"
      ROWNOTE="pushed=${C:0:10} $ROWNOTE"; row "$([ -n "$HELD" ] && echo 4 || echo 0)"
      [ -n "$HELD" ] && exit 4; exit 0
    fi
    PHASES="${PHASES} ${_ap}t_push=$(secs "$_tp")s(refused)"
    if [ "$_att" -eq 3 ]; then
      echo "box-sync: push of CLOUD was refused on all 3 attempts (a writer outside the integrator keeps moving it?) -- nothing landed; the next pass retries" >&2
      ROWNOTE="push=refused-x3 $ROWNOTE"; row 3; exit 3
    fi
    echo "box-sync: push of CLOUD was refused (attempt ${_att}) -- re-fetching and rebuilding on the new CLOUD" >&2
    _tf="${EPOCHREALTIME:-0}"
    git fetch -q origin 2>/dev/null || { echo "box-sync: re-fetch failed -- nothing landed" >&2; ROWNOTE="push=refused refetch=failed $ROWNOTE"; row 3; exit 3; }
    PHASES="${PHASES} a$((_att + 1)).t_fetch=$(secs "$_tf")s"
  done
fi

# ============================================================== box: take CLOUD into box/<this box>, push it
BOX="${AGENTBUS_DEVICE:-}"
[ -n "$BOX" ] || BOX="$(bash "$ROOT/.tools/agentbus-sqs.sh" device 2>/dev/null | sed -n 's/^device: *//p' | head -1)"
[ -n "$BOX" ] && [ "$BOX" != "UNKNOWN" ] || { echo "box-sync: REFUSED -- this box's name is unknown (AGENTBUS_DEVICE)" >&2; ROWNOTE="box=unknown"; row 1; exit 1; }
B="box/$BOX"
CLOUD_SIDE="theirs"   # box mode merges (box tip, CLOUD): CLOUD is the second parent
CUR_BR="$(git symbolic-ref -q --short HEAD 2>/dev/null || echo '')"
[ "$CUR_BR" = "$B" ] || { echo "box-sync: REFUSED -- this shared tree is on '${CUR_BR:-detached}', not $B: the box has not switched" >&2; ROWNOTE="not-switched=${CUR_BR:-detached}"; row 1; exit 1; }
CLOUD_TIP="$(git rev-parse --verify -q refs/remotes/origin/CLOUD)" || { ROWNOTE="no-origin-CLOUD"; row 1; exit 1; }
LOCK_DIR="${GITDIR}/commit-queue.lock"   # the lock safe-commit lands under (legacy and two-phase)

# APPEND-ONLY LOGS, UNCOMMITTED (0.0.0_AB_MSTR msg 107817; dell1 06:5xZ, laptop 07:0xZ): every manager spawn, /govern reaper
# run and law edit appends a line to one of these files in the shared tree, so the land below (`read-tree -m -u`) HELD on
# them whenever CLOUD changed the same file. When the working copy extends the box tip's blob byte for byte, commit it
# first through safe-commit under this serial (LD-0639 grants the spawn audit to box managers); the merge then resolves the
# file as a LINE UNION, CLOUD's file then the box-only lines (merge-resolve-known.py, 0.0.0_AB_MSTR msg 107847). Anything else -- staged by a seat, an earlier line edited,
# a lane refusal -- is left alone, and the land HOLDS as before.
APPEND_PATHS="$(python -c 'import importlib.util as u,sys;s=u.spec_from_file_location("m",sys.argv[1]);m=u.module_from_spec(s);s.loader.exec_module(m);print(" ".join(m.APPEND_ONLY))' "$ROOT/.tools/merge-resolve-known.py")"
for _p in $APPEND_PATHS; do
  _mb="$(git merge-base "refs/heads/$B" "$CLOUD_TIP" 2>/dev/null)" || break
  git diff --quiet "$_mb" "$CLOUD_TIP" -- "$_p" && continue        # CLOUD did not change it: the land cannot overlap
  git diff --quiet -- "$_p" && continue                            # nothing uncommitted
  git diff --cached --quiet -- "$_p" || { echo "box-sync: $_p is staged by a seat -- left to that seat"; continue; }
  python "$ROOT/.tools/merge-resolve-known.py" --extends "refs/heads/$B" "$_p" \
    || { echo "box-sync: $_p is not a pure append of the box tip -- left; the land may HOLD on it"; continue; }
  if [ "$DRY" -eq 1 ]; then echo "box-sync: DRY RUN -- would commit the uncommitted appends of $_p"; continue; fi
  _msg="$(mktemp)"
  python -c 'import sys;open(sys.argv[1],"w",encoding="utf-8",newline="\n").write("chore(%s): commit the uncommitted appends of %s before taking CLOUD (box-sync, append-only log)\n\nThe working copy extends the box tip byte for byte; CLOUD changed the same file, so the land would HOLD on it\n(0.0.0_AB_MSTR msg 107817).\n" % (sys.argv[2], sys.argv[3]))' "$_msg" "$SERIAL" "$_p"
  if _out="$(bash "$ROOT/.tools/safe-commit.sh" --author "$SERIAL <$SERIAL@opal.agent>" -F "$_msg" -- "$_p" 2>&1)"; then
    echo "box-sync: committed the uncommitted appends of $_p ($(git rev-parse --short=10 "refs/heads/$B"))"
  else
    echo "box-sync: safe-commit refused the appends of $_p -- left; the land may HOLD on it. Its last lines:"
    printf '%s\n' "$_out" | tail -3 | sed 's/^/    /'
  fi
  rm -f "$_msg"
done
TOOK="none"
for attempt in 1 2 3; do
  P1="$(git rev-parse "refs/heads/$B")"
  if git merge-base --is-ancestor "$CLOUD_TIP" "$P1"; then TOOK="already-current"; break; fi
  GRADED_NOTE=""
  _tm="${EPOCHREALTIME:-0}"
  make_merge "$P1" "$CLOUD_TIP" "box-sync(${SERIAL}): take CLOUD @${CLOUD_TIP:0:10} into ${B}"; mrc=$?; M="$MERGE_OUT"
  PHASES="${PHASES} $([ "$attempt" -gt 1 ] && echo "a${attempt}.")t_merge_cloud=$(secs "$_tm")s"
  if [ "$mrc" -eq 4 ]; then
    echo "box-sync: HELD -- CLOUD @${CLOUD_TIP:0:10} conflicts with ${B}. Resolve with the /integrate BOX PASS (safe-merge in a drain worktree); one owner repairs a trunk break -- the seat owning the file lane, on its own box (owned-paths-validate.py --check-path names it; an ANY path: the integrator box); every other box just takes CLOUD next pass. Nothing landed."
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
  # APPEND-ONLY LOGS STILL DIRTY AT THE LAND (0.0.0_AB_MSTR msg 107952): org/git-author-override-audit.log is appended by
  # every safe-commit -- including the pre-land commit above -- and by this script, so it is dirty again within seconds and
  # `read-tree -m -u` HELD on it every run. For each APPEND_ONLY path the merge changes that is dirty and not staged: land a
  # tree that keeps the path at P1's blob (so the land does not touch the file), point the index at the merge's blob, then
  # APPEND to the working copy the merge's lines it lacks (merge-resolve-known.py --append-missing). Nothing is rewritten,
  # so a line another process appends meanwhile is never lost. A staged path is left alone and the land HOLDS as before.
  LAND_TREE="$M"; APP_FIX=""
  for _p in $APPEND_PATHS; do
    git diff --quiet "$P1" "$M" -- "$_p" && continue
    git diff --quiet -- "$_p" && continue
    git diff --cached --quiet -- "$_p" || continue
    git cat-file -e "$P1:$_p" 2>/dev/null || continue
    APP_FIX="$APP_FIX $_p"
  done
  if [ -n "$APP_FIX" ]; then
    _lidx="$GITDIR/box-sync-land-$$.index"; rm -f "$_lidx"
    if GIT_INDEX_FILE="$_lidx" git read-tree "$M"; then
      for _p in $APP_FIX; do
        GIT_INDEX_FILE="$_lidx" git update-index --cacheinfo "$(git ls-tree "$P1" -- "$_p" | awk '{print $1}'),$(git rev-parse "$P1:$_p"),$_p" || LAND_TREE=""
      done
      [ -n "$LAND_TREE" ] && LAND_TREE="$(GIT_INDEX_FILE="$_lidx" git write-tree)" || LAND_TREE="$M"
    fi
    rm -f "$_lidx"
    [ "$LAND_TREE" = "$M" ] && APP_FIX=""
  fi
  if ! git read-tree -m -u "$P1" "$LAND_TREE"; then
    rm -rf "$LOCK_DIR"
    echo "box-sync: HELD -- updating the shared tree would overwrite a seat's uncommitted edit of a path CLOUD changed. Nothing landed; the next slot retries after that seat commits."
    ROWNOTE="held=dirty-overlap ${GRADED_NOTE}"; row 4; exit 4
  fi
  if ! git update-ref -m "box-sync: take CLOUD @${CLOUD_TIP:0:10}" "refs/heads/$B" "$M" "$P1"; then
    git read-tree -m -u "$LAND_TREE" "$P1" 2>/dev/null; rm -rf "$LOCK_DIR"
    echo "box-sync: the branch moved under the lock -- the shared tree was put back; nothing landed" >&2; ROWNOTE="cas=failed"; row 3; exit 3
  fi
  for _p in $APP_FIX; do
    git update-index --cacheinfo "$(git ls-tree "$M" -- "$_p" | awk '{print $1}'),$(git rev-parse "$M:$_p"),$_p"
    echo "box-sync: $_p was dirty at the land -- $(python "$ROOT/.tools/merge-resolve-known.py" --append-missing "$(git rev-parse "$M:$_p")" "$_p" 2>&1)"
  done
  rm -rf "$LOCK_DIR"
  TOOK="${CLOUD_TIP:0:10} hold=$(secs "$_TL")s ${GRADED_NOTE}"; PHASES="${PHASES} t_land=$(secs "$_TL")s"
  break
done
[ "$TOOK" = "none" ] && { ROWNOTE="took=none (3 attempts lost the race)"; row 3; exit 3; }
if [ "$DRY" -eq 1 ]; then echo "box-sync: DRY RUN -- $B already holds CLOUD; would push $B"; ROWNOTE="dry-run took=$TOOK"; row 0; exit 0; fi
if [ "$(git rev-parse "refs/heads/$B")" != "$(git rev-parse -q --verify "refs/remotes/origin/$B" 2>/dev/null || echo none)" ]; then
  _tp="${EPOCHREALTIME:-0}"
  git push -q origin "$B" && PHASES="${PHASES} t_push=$(secs "$_tp")s" || { echo "box-sync: push of $B failed -- the branch is current locally; the next slot pushes" >&2; ROWNOTE="took=$TOOK push=failed"; row 3; exit 3; }
fi
echo "box-sync: box -- $B took CLOUD (${TOOK}) and is pushed"
ROWNOTE="took=$TOOK pushed=$(git rev-parse --short=10 "refs/heads/$B")"; row 0; exit 0
