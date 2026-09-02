#!/bin/bash
# surprise-watch.sh -- the STEP-8 INVESTIGATIONS NOTIFIER (Andrew-direct 2026-09-01).
#
# AUTHORIZATION. The standing moratorium (CLAUDE.md HARD STOPS) bans building any
# alert/alarm/SNS/SES-send/notification/freshness-checker/monitor unless Andrew explicitly asks.
# He asked, twice and in his own words:
#   transcript 9-1 flow_6519.txt: "as these investigations pop in as that file is edited, there
#   should be a monitor function for CVO where CVO essentially gets pinged. Just like how we have
#   slash watcher skill, there should be a monitor to that investigations file"
#   /open-calls 2026-09-01 card 5 of 9, REC "YES, but scoped: a LOCAL notifier only" -> "All recs
#   approved".
# The approved scope is EXACTLY: a local notifier. NO SNS, NO SES, NO email, NO alarm, NO
# freshness-checker. It NOTIFIES; it never gates, never blocks, and never closes anything.
#
# ============================================================================================
# WHY THIS IS NOT A COPY OF inbox-watch.sh, AND THE DIFFERENCE IS THE WHOLE SAFETY ARGUMENT
# ============================================================================================
# inbox-watch.sh gets exactly-once delivery by MOVING the message (`mv` to read/) before echoing.
# That mv is precisely what makes ITS orphan a THIEF: a watcher whose session died still drains
# the mailbox into read/ and echoes into a dead pipe, so mail is consumed by nobody while every
# reachability probe reads REACHABLE (see .claude/skills/watcher/SKILL.md, ORPHAN HAZARD).
#
# THIS WATCHER NEVER MUTATES WHAT IT WATCHES. It is a read-only WATERMARK watcher: it counts rows
# and compares against its own state file. Consequences, and they are the reason for the design:
#   - AN ORPHAN OF THIS WATCHER CANNOT STEAL. The worst an orphan does is advance a state file
#     nobody reads. The investigation rows are still there, in full, for the next reader.
#   - CONCURRENT WORKERS ARE APPENDING TO THESE FILES. A watcher that moved or rewrote them would
#     race every worker in the fabric. Read-only is not politeness here, it is correctness.
#   - Delivery is therefore AT-LEAST-ONCE, never exactly-once. That is the correct trade for a
#     NOTIFIER: a duplicate ping costs a glance, a stolen row costs the finding.
#
# ⛔ THE STATE FILE IS NOT AN ORACLE FOR "CVO READ IT". It records what this PROCESS emitted.
# Same law as the inbox: SENT != EMITTED != READ, and only an agent-side ack is sound.
#
# Usage:
#   surprise-watch.sh <serial> stream     persistent poll; one stdout line per new row batch.
#                                         Run under the Monitor tool (persistent: true).
#   surprise-watch.sh <serial> once       one pass, emit and update, then exit (testing/cron-free).
#   surprise-watch.sh <serial> status     print the watermark table and exit. Never emits.
#   surprise-watch.sh <serial> reset      delete this serial's watermark (next run re-baselines).
#
# Rule 16 clean: bash 3.6.7 builtins + grep/sed/date/mkdir/mv only. No pgrep/pkill/flock/setsid.
# No non-ASCII in output (OK:/WARN:/ERROR:).

set -u

SERIAL="${1:-}"
MODE="${2:-stream}"

if [ -z "$SERIAL" ]; then
    echo "ERROR: usage: surprise-watch.sh <serial> [stream|once|status|reset]" >&2
    exit 2
fi

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
CHANNEL_DIR="$SCRIPT_DIR"
STATE_DIR="$CHANNEL_DIR/.watch-state"
STATE_FILE="$STATE_DIR/${SERIAL}.tsv"

mkdir -p "$STATE_DIR" 2>/dev/null || true

# The id pattern is the SCHEMA's own (investigation_item.schema.json "id"):
#   ^[A-Z0-9_]+-(Z-)?S[0-9]+$   -- {PROJECT}-S{n} laptop, {PROJECT}-Z-S{n} site Z.
# Anchoring the count to it is what makes this a ROW count and not a `"id"` substring count --
# evidence strings in these files routinely contain quoted fragments, and a naive grep for '"id"'
# scores them. Counting is a MEASUREMENT (Rule 21 non-application limb i), not a search.
ID_RE='^[[:space:]]*"id":[[:space:]]*"[A-Z0-9_]+-(Z-)?S[0-9]+"'

# ---------------------------------------------------------------------------------------------
# ID/HASH WATERMARK -- RC2, the watcher half (CVO~A re-grade @0dbf12ebb3).
# A row COUNT cannot see a same-id rewrite (count unchanged) or a delete-and-add (count unchanged).
# Each poll pulls `path<TAB>id<TAB>hash` for every row from the corpus validator's --index mode and
# diffs it against the stored index. Emits WARN on a known id whose hash changed (MUTATION) or that
# vanished (DELETION). Still READ-ONLY over the channel: the only write is this watcher's own state.
# If the index cannot be produced, say so LOUDLY every poll -- a notifier that degrades to
# count-only in silence is the P0 wearing a green light.
# ---------------------------------------------------------------------------------------------
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
IDX_FILE="$STATE_DIR/${SERIAL}.idx.tsv"
IDX_TOOL="$REPO_ROOT/.tools/surprise-corpus-validate.py"

_index_now() {
    # Echoes the current index, or nothing (with a WARN on stderr) if it cannot be produced.
    if [ ! -f "$IDX_TOOL" ]; then
        echo "WARN: [SURPRISE] id/hash index tool missing at $IDX_TOOL -- watcher is COUNT-ONLY this poll" >&2
        return 1
    fi
    python "$IDX_TOOL" --index 2>/dev/null
    rc=$?
    if [ "$rc" -ne 0 ]; then
        echo "WARN: [SURPRISE] id/hash index FAILED (rc=$rc) -- watcher is COUNT-ONLY this poll" >&2
        return 1
    fi
    return 0
}

_index_diff() {
    # Compares the live index to the stored one; emits MUTATION / DELETION lines. Writes the
    # new index afterwards. Returns the number of lines emitted.
    # CRLF TRAP, MEASURED 2026-09-02 on first smoke: Windows Python writes \r\n to a pipe, so the
    # stored hash read back as "hash\r" while awk's $(...) output had the \r stripped -- every row
    # compared unequal and a no-change poll emitted 191 MUTATION warnings. Strip \r on BOTH sides:
    # the live index before it is stored or compared, and each stored field on read.
    live="$(_index_now | tr -d '\r')" || return 0
    emitted=0
    if [ -s "$IDX_FILE" ]; then
        # For every stored (path,id,hash): missing id -> DELETION; same id, other hash -> MUTATION.
        while IFS="$(printf '\t')" read -r p i h; do
            p="${p%$'\r'}"; i="${i%$'\r'}"; h="${h%$'\r'}"
            [ -n "$i" ] || continue
            cur="$(printf '%s\n' "$live" | awk -F'\t' -v P="$p" -v I="$i" '$1==P && $2==I {print $3; exit}')"
            if [ -z "$cur" ]; then
                [ "$quiet" -eq 1 ] || echo "WARN: [SURPRISE] $(_project_of "$p")  ROW $i DISAPPEARED -> $p  (append-only channel; a vanished id is a deletion or a merge that dropped it)"
                emitted=$((emitted + 1))
            elif [ "$cur" != "$h" ]; then
                [ "$quiet" -eq 1 ] || echo "WARN: [SURPRISE] $(_project_of "$p")  ROW $i MUTATED in place (${h} -> ${cur}) -> $p  (corrections are NEW rows citing the old id)"
                emitted=$((emitted + 1))
            fi
        done < "$IDX_FILE"
    fi
    printf '%s\n' "$live" > "$IDX_FILE.tmp" && mv -f "$IDX_FILE.tmp" "$IDX_FILE"
    return "$emitted"
}

_count_rows() {
    # $1 = file. Echoes the row count, or 0 for an unreadable/empty file.
    #
    # THE TRAP, caught by control W7 on first exercise 2026-09-01: `grep -c` PRINTS "0" AND
    # RETURNS rc=1 when there are no matches. The obvious `grep -c ... || echo 0` therefore emits
    # BOTH -- the count becomes the two-line string "0\n0", every downstream $(( )) throws
    # "arithmetic syntax error", and the zero-row case (a freshly opened channel, or a file being
    # rewritten) breaks. `|| true` swallows the status; the case guard makes anything non-numeric
    # fail to 0 rather than propagate.
    n="$(grep -cE "$ID_RE" "$1" 2>/dev/null || true)"
    case "$n" in
        ''|*[!0-9]*) n=0 ;;
    esac
    printf '%s' "$n"
}

_watched_files() {
    # Every project's investigation doc, whatever the container. The protocol's container is
    # markdown-with-a-fenced-block today and a pure .json swap is proposed but NOT censused
    # against existing readers -- so BOTH suffixes are watched and the swap needs no change here.
    for f in "$CHANNEL_DIR"/*/INVESTIGATION_v*.md "$CHANNEL_DIR"/*/INVESTIGATION_v*.json; do
        [ -f "$f" ] || continue
        printf '%s\n' "$f"
    done
}

_project_of() {
    # .../org/surprise_channel/ADVI_PERFRP/INVESTIGATION_v1.md -> ADVI_PERFRP
    basename "$(dirname "$1")"
}

_prior_count() {
    # $1 = path. Echoes the recorded count, or the empty string if never seen.
    [ -f "$STATE_FILE" ] || { echo ""; return; }
    sed -n "s|^$(printf '%s' "$1" | sed 's/[][\\.*^$/]/\\&/g')	\\(.*\\)$|\\1|p" "$STATE_FILE" | head -1
}

_write_state() {
    # stdin: lines of "path<TAB>count". Atomic replace so a reader never sees a half-written table.
    tmp="$STATE_FILE.$$"
    cat > "$tmp" 2>/dev/null || return 1
    mv "$tmp" "$STATE_FILE" 2>/dev/null || { rm -f "$tmp" 2>/dev/null; return 1; }
    return 0
}

# ---------------------------------------------------------------------------- one pass
# Emits to stdout; returns the number of files that grew. Writes the new watermark table.
_pass() {
    quiet="${1:-0}"          # 1 = seed the baseline silently (first run)
    grew=0
    total_rows=0
    files=0
    new_state=""
    while IFS= read -r f; do
        [ -n "$f" ] || continue
        files=$((files + 1))
        n="$(_count_rows "$f")"
        total_rows=$((total_rows + n))
        prior="$(_prior_count "$f")"
        new_state="$new_state$f	$n
"
        [ "$quiet" -eq 1 ] && continue
        if [ -z "$prior" ]; then
            # A project dir that did not exist at baseline. Its rows are all new to this watcher.
            if [ "$n" -gt 0 ]; then
                echo "[SURPRISE] $(_project_of "$f")  NEW CHANNEL  ${n} row(s) -> $f"
                grew=$((grew + 1))
            fi
        elif [ "$n" -gt "$prior" ]; then
            echo "[SURPRISE] $(_project_of "$f")  +$((n - prior)) new row(s) (now ${n}) -> $f"
            grew=$((grew + 1))
        elif [ "$n" -lt "$prior" ]; then
            # Rows going DOWN is not routine. Do not silently re-baseline it -- a shrink is either
            # a rewrite, a truncation, or a merge that lost content, and all three want a human.
            echo "WARN: [SURPRISE] $(_project_of "$f")  ROW COUNT FELL ${prior} -> ${n} -> $f  (rewrite, truncation, or a merge that dropped rows -- not routine)"
            grew=$((grew + 1))
        fi
    done <<EOF
$(_watched_files)
EOF
    printf '%s' "$new_state" | _write_state
    LAST_FILES="$files"
    # RC2: the id/hash pass runs AFTER the count pass every poll, so a same-count rewrite that the
    # count above could not see is reported here. Its return value is the number of WARN lines.
    _index_diff
    grew=$((grew + $?))
    LAST_ROWS="$total_rows"
    return 0
}

case "$MODE" in
status)
    if [ ! -f "$STATE_FILE" ]; then
        echo "surprise-watch: NO WATERMARK for $SERIAL (never run). Next run seeds a baseline."
        exit 0
    fi
    echo "surprise-watch: watermark for $SERIAL  ($STATE_FILE)"
    tot=0; n=0
    while IFS='	' read -r p c; do
        [ -n "$p" ] || continue
        n=$((n + 1)); tot=$((tot + c))
        printf '  %-24s %5s  %s\n' "$(_project_of "$p")" "$c" "$p"
    done < "$STATE_FILE"
    echo "  DENOMINATOR: $n watched file(s), $tot row(s) at last pass"
    echo "  NOTE: this records what THIS PROCESS emitted. It is NOT evidence any agent READ a row."
    exit 0
    ;;
reset)
    rm -f "$STATE_FILE" 2>/dev/null || true
    echo "OK: watermark cleared for $SERIAL. The next run re-baselines WITHOUT emitting."
    exit 0
    ;;
once)
    if [ -f "$STATE_FILE" ]; then
        _pass 0
    else
        _pass 1
        echo "OK: baseline seeded -- ${LAST_FILES} file(s), ${LAST_ROWS} row(s). Pre-existing rows are NOT notified (that would be a flood, not a signal)."
    fi
    exit 0
    ;;
stream)
    : ;;
*)
    echo "ERROR: unknown mode '$MODE' (stream|once|status|reset)" >&2
    exit 2
    ;;
esac

# ---------------------------------------------------------------------------- stream mode
# PARENT-LIVENESS SELF-EXIT -- carried over from inbox-watch.sh:112-165 (0.0.0_AB_MSTR's
# orphan-thief root fix), INCLUDING its fail-open cell. MSYS renders a live non-MSYS parent as
# ppid 1, and a naive check would make healthy watchers suicide (the documented 7-false-positive
# trap), so PPID<=1 disables the check rather than killing on a probe that cannot see its subject.
# Read the arm banner below: "parent-tied: pid N" = armed, "parent-tied: OFF" = orphan-capable.
WATCH_PARENT="$PPID"
PARENT_CHECK=1
if [ -n "${SURPRISE_WATCH_NO_PARENT_CHECK:-}" ] || [ "$WATCH_PARENT" -le 1 ]; then
    PARENT_CHECK=0
fi

# NO-SPAWN WAIT -- `sleep` is an EXTERNAL binary in Git Bash, so a naive loop spawns one process
# per cycle per watcher. `read -t` against a held-open FIFO waits in-process. mkfifo failure falls
# back to sleep: correctness identical, only the spawn cost differs (Rule 16 guarded pattern).
_WAIT_FIFO="$(mktemp -u 2>/dev/null || echo "/tmp/surprise-watch-wait-$$")"
_NOSPAWN=0
if mkfifo "$_WAIT_FIFO" 2>/dev/null; then
    exec 9<>"$_WAIT_FIFO"
    rm -f "$_WAIT_FIFO"
    _NOSPAWN=1
fi
_wait_interval() {
    if [ "$_NOSPAWN" -eq 1 ]; then read -rt 15 -u 9 _ 2>/dev/null || true; else sleep 15; fi
}

if [ ! -f "$STATE_FILE" ]; then
    _pass 1
    echo "surprise-watch: baseline seeded -- ${LAST_FILES} file(s), ${LAST_ROWS} row(s); pre-existing rows NOT notified" >&2
fi

echo "surprise-watch: STREAM mode for $SERIAL watching $CHANNEL_DIR/*/INVESTIGATION_v* (persistent; READ-ONLY on the watched files; parent-tied: $([ "$PARENT_CHECK" -eq 1 ] && echo "pid $WATCH_PARENT" || echo "OFF"); wait=$([ "$_NOSPAWN" -eq 1 ] && echo no-spawn || echo sleep)/15s)" >&2

while true; do
    if [ "$PARENT_CHECK" -eq 1 ] && ! kill -0 "$WATCH_PARENT" 2>/dev/null; then
        ts="$(date -u +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || echo unknown-ts)"
        echo "$ts  SURPRISE-WATCH-SELF-EXIT  serial=$SERIAL  parent=$WATCH_PARENT gone -- exiting instead of orphaning" >> "$STATE_DIR/orphan-audit.log" 2>/dev/null || true
        exit 0
    fi
    _pass 0
    _wait_interval
done
