#!/usr/bin/env bash
# detached-job.sh -- DECLARE a deliberate long-running detached job so the box's reaper (.tools/kill-maint.ps1, run
# unattended by its scheduled task) never stops it as ORPHAN / NATIVE.
#
# 0.0.0_AB_MSTR msgs 107412 + 107416 (2026-10-08): deliberate detached jobs (site Z's AMGT_HARVST backfill, dell2's
# worker gold-run loops) outlive the 31-minute Monitor cap and sit outside every claude tree, so the age predicate
# could not tell them from a leaked watcher. A marker names the job; kill-maint exempts the marked process, its Windows
# subtree and its MSYS descendants until the declared max runtime passes. An expired marker exempts nothing.
#
#   bash .tools/detached-job.sh run --owner <serial> --purpose "<text>" --max-hours <h> -- <command> [args...]
#        runs <command> as a child of a marked shell; the marker is removed when it exits. Detach the whole call
#        yourself, e.g.  nohup bash .tools/detached-job.sh run ... -- python -m pkg.job > job.log 2>&1 &
#   bash .tools/detached-job.sh declare --owner <serial> --purpose "<text>" --max-hours <h> --winpid <pid>
#        marks an ALREADY-running process by its Windows PID (Get-Process / `cat /proc/<msys pid>/winpid`)
#   bash .tools/detached-job.sh list          every marker with LIVE / GONE / EXPIRED
#   bash .tools/detached-job.sh clear <id>|--dead
#
# Markers: <git common dir>/detached-jobs/<id>.json (never tracked; shared by every worktree of the repo).
# max-hours is capped at 48. Git Bash default utilities only. ASCII only.
set -u
MAX_HOURS_CAP=48

die() { echo "ERROR: $*" >&2; exit 2; }
common=$(git rev-parse --path-format=absolute --git-common-dir 2>/dev/null) || die "not inside a git repository"
DIR="$common/detached-jobs"

jesc() { printf '%s' "$1" | sed -e 's/\\/\\\\/g' -e 's/"/\\"/g' | tr -d '\000-\037'; }
utc() { date -u +%Y-%m-%dT%H:%M:%SZ; }
alive() { tasklist //FI "PID eq $1" //NH 2>/dev/null | grep -q " $1 "; }   # pipe receiver: a predicate, not a census

write_marker() {   # id winpid owner purpose max_seconds cmd
  mkdir -p "$DIR" || die "cannot create $DIR"
  local f="$DIR/$1.json"
  printf '{"id": "%s", "winpid": %s, "owner": "%s", "purpose": "%s", "declared_at": "%s", "max_seconds": %s, "cwd": "%s", "cmd": "%s"}\n' \
    "$1" "$2" "$(jesc "$3")" "$(jesc "$4")" "$(utc)" "$5" "$(jesc "$PWD")" "$(jesc "$6")" > "$f.tmp" && mv "$f.tmp" "$f" \
    || die "cannot write $f"
  echo "DECLARED $1 winpid=$2 owner=$3 max_seconds=$5 marker=$f"
}

parse_common() {
  OWNER=""; PURPOSE=""; HOURS=""; WINPID=""
  while [ $# -gt 0 ]; do
    case "$1" in
      --owner) OWNER="${2:-}"; shift 2 ;;
      --purpose) PURPOSE="${2:-}"; shift 2 ;;
      --max-hours) HOURS="${2:-}"; shift 2 ;;
      --winpid) WINPID="${2:-}"; shift 2 ;;
      --) shift; break ;;
      *) die "unknown argument: $1" ;;
    esac
  done
  REST=("$@")
  [ -n "$OWNER" ] || die "--owner <serial> is required"
  [ -n "$PURPOSE" ] || die "--purpose is required"
  case "$HOURS" in ''|*[!0-9]*) die "--max-hours must be a whole number of hours" ;; esac
  [ "$HOURS" -ge 1 ] && [ "$HOURS" -le "$MAX_HOURS_CAP" ] || die "--max-hours must be 1..$MAX_HOURS_CAP"
}

new_id() { echo "dj-$(date -u +%Y%m%dT%H%M%SZ)-$$"; }

cmd=${1:-}; [ $# -gt 0 ] && shift
case "$cmd" in
  run)
    parse_common "$@"
    [ ${#REST[@]} -gt 0 ] || die "run needs -- <command> [args...]"
    winpid=$(cat "/proc/$$/winpid" 2>/dev/null) || die "cannot read this shell's Windows PID"
    id=$(new_id)
    write_marker "$id" "$winpid" "$OWNER" "$PURPOSE" $((HOURS * 3600)) "${REST[*]}"
    trap 'rm -f "$DIR/$id.json"; echo "CLEARED $id"' EXIT
    "${REST[@]}"
    rc=$?
    echo "JOB-EXIT $id rc=$rc"
    exit $rc
    ;;
  declare)
    parse_common "$@"
    case "$WINPID" in ''|*[!0-9]*) die "--winpid <Windows PID> is required" ;; esac
    alive "$WINPID" || die "no running process with Windows PID $WINPID"
    write_marker "$(new_id)" "$WINPID" "$OWNER" "$PURPOSE" $((HOURS * 3600)) "(declared running process)"
    ;;
  list)
    n=0
    for f in "$DIR"/*.json; do
      [ -e "$f" ] || continue
      n=$((n + 1))
      wp=$(sed -n 's/.*"winpid": \([0-9]*\).*/\1/p' "$f")
      if alive "$wp"; then st=LIVE; else st=GONE; fi
      echo "$st $(cat "$f")"
    done
    echo "DETACHED-JOBS markers=$n dir=$DIR (EXPIRED is judged by kill-maint against declared_at + max_seconds)"
    ;;
  clear)
    [ $# -ge 1 ] || die "clear <id>|--dead"
    if [ "$1" = "--dead" ]; then
      for f in "$DIR"/*.json; do
        [ -e "$f" ] || continue
        wp=$(sed -n 's/.*"winpid": \([0-9]*\).*/\1/p' "$f")
        alive "$wp" || { rm -f "$f"; echo "CLEARED $(basename "$f" .json) (pid $wp gone)"; }
      done
    else
      [ -e "$DIR/$1.json" ] || die "no marker $1"
      rm -f "$DIR/$1.json" && echo "CLEARED $1"
    fi
    ;;
  *) sed -n '2,20p' "$0"; exit 2 ;;
esac
