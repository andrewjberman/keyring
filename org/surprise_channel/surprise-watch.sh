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
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
# STATE lives under .tools/state/ (project-tree spec s.7: "the watermark file moves to .tools/state/";
# CTO repoint 2026-09-02 under the COO/CTO prerequisite split @a8d63f097c). The old location was
# INSIDE the watched channel; the tree adds a second root, and a watcher's state belongs to neither.
STATE_DIR="$REPO_ROOT/.tools/state/surprise-watch"
_OLD_STATE_DIR="$CHANNEL_DIR/.watch-state"
STATE_FILE="$STATE_DIR/${SERIAL}.tsv"

mkdir -p "$STATE_DIR" 2>/dev/null || true
# ONE-TIME MIGRATION: a live watcher's watermark + id/hash index carry over, so the move never makes
# a seat re-seed (a re-seed is silent by design -- and silence is exactly what a moved state file
# would otherwise buy). Copies only the files this serial owns and only when the new home lacks them.
for _old in "$_OLD_STATE_DIR/${SERIAL}".*; do
    [ -f "$_old" ] || continue
    _new="$STATE_DIR/$(basename "$_old")"
    [ -e "$_new" ] || cp -p "$_old" "$_new" 2>/dev/null || true
done

# The id pattern is the SCHEMA's own (investigation_item.schema.json "id"):
#   ^[A-Z0-9_]+-(Z-)?(W[0-9]+-|C-)?S[0-9]+$   -- {PROJECT}-S{n} laptop, {PROJECT}-Z-S{n} site Z,
#                                                 {PROJECT}-W{n}-S{k} a worker worktree's row, {PROJECT}-C-S{k} a CVO row
#                                                 in adjudications/ (the allocator coordinates).
# Anchoring the count to it is what makes this a ROW count and not a `"id"` substring count --
# evidence strings in these files routinely contain quoted fragments, and a naive grep for '"id"'
# scores them. Counting is a MEASUREMENT (Rule 21 non-application limb i), not a search.
ID_RE='^[[:space:]]*"id":[[:space:]]*"[A-Z0-9_]+-(Z-)?(W[0-9]+-|C-)?S[0-9]+"'

# ---------------------------------------------------------------------------------------------
# ID/HASH WATERMARK -- RC2, the watcher half (CVO~A re-grade @0dbf12ebb3).
# A row COUNT cannot see a same-id rewrite (count unchanged) or a delete-and-add (count unchanged).
# Each poll pulls `path<TAB>id<TAB>hash` for every row from the corpus validator's --index mode and
# diffs it against the stored index. Emits WARN on a known id whose hash changed (MUTATION) or that
# vanished (DELETION). Still READ-ONLY over the channel: the only write is this watcher's own state.
# If the index cannot be produced, say so LOUDLY every poll -- a notifier that degrades to
# count-only in silence is the P0 wearing a green light.
# ---------------------------------------------------------------------------------------------
IDX_FILE="$STATE_DIR/${SERIAL}.idx.tsv"
PROV_FILE="$STATE_DIR/${SERIAL}.prov.tsv"   # cross-poll PROVISIONAL set (pass 2); the selftest overrides it
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
    # FAILURE MUST NOT REACH THE DIFF, AND MUST NOT REACH THE WRITE. First cut piped _index_now
    # through tr, so a tool failure exited 0 through the pipe (no pipefail in this bash), `live`
    # went EMPTY, every stored row read DISAPPEARED, and the index file was overwritten with
    # nothing (CVO~A re-grade, 2026-09-02). The exit status is captured on its own line, BEFORE any
    # pipe; an empty index is treated as failure too (the channel is never empty); and on failure
    # this function returns BEFORE the write so the prior index survives intact.
    live="$(_index_now)"
    rc=$?
    if [ "$rc" -ne 0 ] || [ -z "$live" ]; then
        [ "$rc" -eq 0 ] && echo "WARN: [SURPRISE] id/hash index came back EMPTY -- watcher is COUNT-ONLY this poll; prior index preserved" >&2
        return 0
    fi
    live="$(printf '%s\n' "$live" | tr -d '\r')"
    # SHORT-LIVE GUARD (3.0.0_SA_CVO 2026-09-02; confirmed independently by CVO~A @217ffafada).
    # A SUCCESSFUL emit (rc 0) with FEWER rows than the stored index is PROVISIONAL, never a verdict.
    # Measured 19:0xZ: one short read fired "ADVI_PERFRP-S1 DISAPPEARED" while S1 sat in the file, git
    # clean; the short emit then REPLACED the index, so the row's return would have fired NEW -- two
    # false events from one read, the second erasing the evidence of the first. The rc/empty guard
    # above cannot see this case: the producer SUCCEEDED, it just came back short.
    # Repair bar (CVO~A): re-sample once; if still short, confirm each missing id against the RAW
    # corpus; if any missing id is still IN its file, this poll is COUNT-ONLY and the prior index
    # is preserved. A row whose id is genuinely gone from its file still fires DISAPPEARED below.
    # PASS 2 (Andrew "All approved go" ~20:4xZ; CTO 92746 race note taken): the pass-1 form re-sampled
    # and grepped the RAW file in the SAME poll, and both reads can land inside the very write that
    # shortened the index. A write does not straddle two POLLS. So a short result is PROVISIONAL:
    # the missing ids are recorded in PROV_FILE, nothing is emitted, the prior index is preserved.
    # On the NEXT poll: a whole sample clears the provisional set silently (recovery); a sample still
    # missing the SAME id CONFIRMS the deletion -- DISAPPEARED fires then, and only that row leaves
    # the stored index. Mutations among present rows are deferred one poll while short (stated).
    quiet="${quiet:-0}"   # CTO grade (a): a caller global read under set -u; default so a bare call cannot die on it
    # PASS 3 (CTO grade of 1a4ce78782: F2 DEFECT + E2 bound; bar (i)-(iv) taken whole):
    #   (i)  the trigger is the SET, not the count. `missing` = stored pairs absent from live, computed
    #        UNCONDITIONALLY. Pass 2 keyed on live_n < stored_n, so a real row dropped AND a row appended in
    #        the same sample (count equal) took the old path, fired on poll 1, and FORGOT the row -- pass 1's
    #        defect through a different door (CTO's F2, measured on WSE_COTMDL-S1).
    #   (ii) the write while anything is provisional is a MERGE, not a copy: stored minus CONFIRMED; present
    #        rows take live's hash (a changed hash still warns MUTATED); missing-but-unconfirmed rows keep
    #        their stored hash; rows NEW in live are appended. So an append is recorded the poll it happens,
    #        a transient miss is never adopted, and the "mutations deferred while short" bound is retired.
    #   (E2) a provisional row is CONFIRMED only if, on the confirming poll, its id is ALSO absent from its
    #        raw file (RAW_ROOT is the selftest's hook; production reads REPO_ROOT). A row still in its file
    #        while the index omits it twice is an index-tool omission, not a deletion -- it stays provisional
    #        and says so. The residual is two INDEPENDENT races, not one.
    emitted=0
    if [ -s "$IDX_FILE" ]; then
        stored="$(tr -d '\r' < "$IDX_FILE")"
        missing="$(printf '%s\n' "$stored" | awk -F'\t' -v L="$live" 'BEGIN{n=split(L,a,"\n"); for(k=1;k<=n;k++){split(a[k],f,"\t"); if(f[2]!="") seen[f[1] "\t" f[2]]=1}} NF>=2 && !(($1 "\t" $2) in seen) {print $1 "\t" $2 "\t" $3}')"
        if [ -n "$missing" ]; then
            prev=""; [ -f "$PROV_FILE" ] && prev="$(tr -d '\r' < "$PROV_FILE")"
            raw_root="${RAW_ROOT:-$REPO_ROOT}"
            confirmed=""; newprov=""; nconf=0; nprov=0; nheld=0
            while IFS="$(printf '\t')" read -r p i h; do
                [ -n "$i" ] || continue
                row="${p}$(printf '\t')${i}$(printf '\t')${h}$(printf '\n')"
                if [ -n "$prev" ] && printf '%s\n' "$prev" | awk -F'\t' -v P="$p" -v I="$i" '$1==P && $2==I {f=1} END {exit !f}'; then
                    if grep -qF "\"id\": \"$i\"" "$raw_root/$p" 2>/dev/null; then
                        newprov="${newprov}${row}"; nprov=$((nprov+1)); nheld=$((nheld+1))   # E2: still in its file -- not a deletion
                    else
                        confirmed="${confirmed}${row}"; nconf=$((nconf+1))
                    fi
                else
                    newprov="${newprov}${row}"; nprov=$((nprov+1))
                fi
            done <<< "$missing"
            if [ "$nconf" -gt 0 ]; then
                while IFS="$(printf '\t')" read -r p i h; do
                    [ -n "$i" ] || continue
                    [ "$quiet" -eq 1 ] || echo "WARN: [SURPRISE] $(_project_of "$p")  ROW $i DISAPPEARED (absent from the index on two consecutive polls AND from its file) -> $p  (append-only channel; a vanished id is a deletion or a merge that dropped it)"
                    emitted=$((emitted + 1))
                done <<< "$confirmed"
            fi
            # mutations among PRESENT rows still warn (the merge takes live's hash; the change is not silent)
            while IFS="$(printf '\t')" read -r p i oh nh; do
                [ -n "$i" ] || continue
                [ "$quiet" -eq 1 ] || echo "WARN: [SURPRISE] $(_project_of "$p")  ROW $i MUTATED in place (${oh} -> ${nh}) -> $p  (corrections are NEW rows; an edited row is a rewrite of the record)"
                emitted=$((emitted + 1))
            done <<< "$(printf '%s\n' "$stored" | awk -F'\t' -v L="$live" 'BEGIN{n=split(L,a,"\n"); for(k=1;k<=n;k++){split(a[k],f,"\t"); if(f[2]!="") lh[f[1] "\t" f[2]]=f[3]}} NF>=2 && (($1 "\t" $2) in lh) && lh[$1 "\t" $2]!=$3 {print $1 "\t" $2 "\t" $3 "\t" lh[$1 "\t" $2]}')"
            # (ii) THE MERGE WRITE
            printf '%s\n' "$stored" | awk -F'\t' -v L="$live" -v C="$confirmed" 'BEGIN{n=split(L,a,"\n"); for(k=1;k<=n;k++){split(a[k],f,"\t"); if(f[2]!=""){lh[f[1] "\t" f[2]]=f[3]; ord[++ln]=f[1] "\t" f[2]}} m=split(C,c,"\n"); for(k=1;k<=m;k++){split(c[k],g,"\t"); if(g[2]!="") gone[g[1] "\t" g[2]]=1}} NF>=2 { key=$1 "\t" $2; if (key in gone) next; if (key in lh) { print $1 "\t" $2 "\t" lh[key]; seen[key]=1 } else print $0 } END{ for(k=1;k<=ln;k++){ key=ord[k]; if (!(key in seen) && !(key in gone)) print key "\t" lh[key] } }' > "$IDX_FILE.tmp" && mv -f "$IDX_FILE.tmp" "$IDX_FILE"
            if [ "$nprov" -gt 0 ]; then
                printf '%s' "$newprov" > "$PROV_FILE.tmp" && mv -f "$PROV_FILE.tmp" "$PROV_FILE"
                echo "WARN: [SURPRISE] id/hash index is MISSING $nprov stored row(s) this poll ($nheld of them still present in their files): PROVISIONAL, confirmed next poll only if absent from index AND file -- watcher is COUNT-ONLY on those rows this poll; index merged, not replaced" >&2
            else
                rm -f "$PROV_FILE"
            fi
            return "$emitted"
        fi
        rm -f "$PROV_FILE"    # nothing missing: any provisional set clears silently (recovery)
    fi
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
        # R4-c (1.0.0_SA_CTO, design @3814be3317; the fields R4-a/b put on every new row): the NEW arm.
        # The count pass says "+N new row(s)"; this names each one -- project, fabric, id, class,
        # hazard_standing -- so the L8 reader groups without opening a file. One --index-rows call,
        # only when the diff has found new ids (never on the seeding pass, never when nothing is new).
        # A 7-column sibling of --index, because the loop above reads exactly three columns.
        newpairs="$(printf '%s\n' "$live" | awk -F'\t' -v S="$(tr -d '\r' < "$IDX_FILE")" 'BEGIN{n=split(S,a,"\n"); for(k=1;k<=n;k++){split(a[k],f,"\t"); if(f[2]!="") seen[f[1] "\t" f[2]]=1}} NF>=2 && !(($1 "\t" $2) in seen) {print $1 "\t" $2}')"
        if [ -n "$newpairs" ] && [ "$quiet" -ne 1 ]; then
            rows7="$(python "$IDX_TOOL" --index-rows 2>/dev/null | tr -d '\r')"
            while IFS="$(printf '\t')" read -r p i; do
                [ -n "$i" ] || continue
                fields="$(printf '%s\n' "$rows7" | awk -F'\t' -v P="$p" -v I="$i" '$1==P && $2==I {printf "project=%s fabric=%s class=%s hazard=%s", $4, $5, $6, $7; exit}')"
                echo "[SURPRISE] $(_project_of "$p")  NEW ROW $i  ${fields:-fields=UNREAD (index-rows did not return this id)} -> $p"
            done <<< "$newpairs"
        fi
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
    # TWO ROOTS (project-tree spec s.7; grammar = org/standards/PROJECT_TREE.contract.json
    # surprise_channel_glob): the flat channel <CHANNEL_DIR>/<PROJECT>/ stays; the tree adds
    # org/missions/D*/<MACRO>/<PROJECT>/surprise-channel/investigations/. A watcher on one root is
    # deaf to the other for the whole dual-register period. The --index this watcher diffs
    # (surprise-corpus-validate.py) enumerates the same two roots.
    for f in "$CHANNEL_DIR"/*/INVESTIGATION_v*.md "$CHANNEL_DIR"/*/INVESTIGATION_v*.json \
             "$REPO_ROOT"/org/missions/D*/*/*/surprise-channel/investigations/INVESTIGATION_v*.md \
             "$REPO_ROOT"/org/missions/D*/*/*/surprise-channel/investigations/INVESTIGATION_v*.json; do
        [ -f "$f" ] || continue
        printf '%s\n' "$f"
    done
}

_project_of() {
    # flat: .../org/surprise_channel/ADVI_PERFRP/INVESTIGATION_v1.md            -> ADVI_PERFRP
    # tree: .../org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md
    #                                                                            -> ETFS_GUARDRAIL
    # (the tree's project folder is three levels up; basename(dirname) would say "investigations")
    case "$1" in
        */surprise-channel/investigations/*|*/surprise-channel/remediations/*)
            basename "$(dirname "$(dirname "$(dirname "$1")")")" ;;
        *)
            basename "$(dirname "$1")" ;;
    esac
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

# ---------------------------------------------------------------------------------------------
# selftest -- REAL bash integration controls for _index_diff (CVO~A re-grade 2026-09-02: the
# Python-side "watcher controls" were a dictionary emulation that never executed this script and
# could not see the pipeline-masked failure). Each case swaps IDX_TOOL/IDX_FILE for temp copies and
# runs the real function. Prints its own N/N line. Exit 1 on any failure.
# ---------------------------------------------------------------------------------------------
_selftest() {
    quiet=0
    T="$(mktemp -d 2>/dev/null || echo "${TMPDIR:-/tmp}/sw-selftest.$$")"; mkdir -p "$T"
    IDX_FILE="$T/idx.tsv"
    seed="$(printf 'org/surprise_channel/P/INVESTIGATION_v1.md\tP-S1\taaaaaaaaaaaa\norg/surprise_channel/P/INVESTIGATION_v1.md\tP-S2\tbbbbbbbbbbbb\n')"
    printf '%s\n' "$seed" > "$IDX_FILE"
    seed_sum="$(cksum < "$IDX_FILE")"
    pass=0; fail=0
    _case() {  # $1 name  $2 expected stdout WARN count  $3 expected stderr COUNT-ONLY count  $4 expect idx unchanged (1/0)
        out="$(_index_diff 2>"$T/err")"; rc=$?
        warns="$(printf '%s\n' "$out" | grep -c 'WARN: \[SURPRISE\]')"
        conly="$(grep -c 'COUNT-ONLY' "$T/err")"
        now_sum="$(cksum < "$IDX_FILE")"
        unchanged=0; [ "$now_sum" = "$seed_sum" ] && unchanged=1
        if [ "$warns" -eq "$2" ] && [ "$conly" -eq "$3" ] && [ "$unchanged" -eq "$4" ]; then
            pass=$((pass+1)); echo "  OK      $1"
        else
            fail=$((fail+1)); echo "  FAIL    $1  (row-warns=$warns want $2; count-only=$conly want $3; idx-unchanged=$unchanged want $4; rc=$rc)"
        fi
        printf '%s\n' "$seed" > "$IDX_FILE"   # re-seed for the next case
    }
    # A. tool missing -> one COUNT-ONLY, zero row warnings, index untouched
    IDX_TOOL="$T/does-not-exist.py";                                           _case "tool MISSING" 0 1 1
    # B. tool exits 1 -> same
    printf 'import sys\nsys.exit(1)\n' > "$T/fail.py"; IDX_TOOL="$T/fail.py";   _case "tool exits 1" 0 1 1
    # C. tool exits 0 with EMPTY output -> same (empty is failure; the channel is never empty)
    printf 'pass\n' > "$T/empty.py"; IDX_TOOL="$T/empty.py";                    _case "tool empty output" 0 1 1
    # D. CRLF output, same content -> zero warnings, index rewritten (LF) so 'unchanged' is 0 but no CR
    printf 'import sys\nsys.stdout.write("org/surprise_channel/P/INVESTIGATION_v1.md\\tP-S1\\taaaaaaaaaaaa\\r\\norg/surprise_channel/P/INVESTIGATION_v1.md\\tP-S2\\tbbbbbbbbbbbb\\r\\n")\n' > "$T/crlf.py"
    # After CR-stripping the live index is byte-identical to the LF seed, so the rewrite yields the
    # SAME file: unchanged=1 is the correct expectation (first cut of this case asserted 0 and was
    # wrong about the test, not the code). The LF-clean check below is the CRLF assertion proper.
    IDX_TOOL="$T/crlf.py";                                                     _case "CRLF output, same rows" 0 0 1
    [ "$(tr -cd '\r' < "$IDX_FILE" | wc -c)" -eq 0 ] && { pass=$((pass+1)); echo "  OK      stored index is LF-clean after CRLF input"; } || { fail=$((fail+1)); echo "  FAIL    stored index still carries CR"; }
    printf '%s\n' "$seed" > "$IDX_FILE"
    # E. same-count MUTATION of S2 -> exactly 1 row warning
    printf 'print("org/surprise_channel/P/INVESTIGATION_v1.md\\tP-S1\\taaaaaaaaaaaa")\nprint("org/surprise_channel/P/INVESTIGATION_v1.md\\tP-S2\\tCHANGEDHASH1")\n' > "$T/mut.py"
    IDX_TOOL="$T/mut.py";                                                      _case "same-count MUTATION" 1 0 0
    # F. same-count DELETE S2 + ADD S3 -> exactly 1 row warning (DISAPPEARED)
    printf 'print("org/surprise_channel/P/INVESTIGATION_v1.md\\tP-S1\\taaaaaaaaaaaa")\nprint("org/surprise_channel/P/INVESTIGATION_v1.md\\tP-S3\\tcccccccccccc")\n' > "$T/del.py"
    # PASS 3 (CTO grade 92 / 2026-09-02, bar (iii)+(iv)): same-count DELETE+ADD is CTO's F2 -- a real row dropped
    # AND a row appended in ONE sample hides a transient short exactly. It is TWO-POLL now: poll 1 provisional
    # (no DISAPPEARED, COUNT-ONLY, the dropped row KEPT, the appended row RECORDED -- the write is a MERGE);
    # poll 2 still missing -> CONFIRMED. The old single-poll "1 warning" expectation encoded the defect.
    rm -f "$PROV_FILE"; IDX_TOOL="$T/del.py";                                  _case "F2 DELETE+ADD same count, poll 1: provisional, merge write" 0 1 0
    rm -f "$PROV_FILE"; printf '%s\n' "$seed" > "$IDX_FILE"; IDX_TOOL="$T/del.py"; _index_diff >/dev/null 2>&1
    if [ "$(tr -d '\r' < "$IDX_FILE" | grep -c 'P-S2')" -eq 1 ] && [ "$(tr -d '\r' < "$IDX_FILE" | grep -c 'P-S3')" -eq 1 ]; then pass=$((pass+1)); echo "  OK      F2 poll 1: dropped row KEPT and appended row RECORDED (merge, not copy)"; else fail=$((fail+1)); echo "  FAIL    F2 poll 1 index: $(tr -d '\r' < "$IDX_FILE" | cut -f2 | tr '\n' ' ')"; fi
    IDX_TOOL="$T/del.py";                                                      _case "F2 DELETE+ADD same count, poll 2: CONFIRMED" 1 0 0
    rm -f "$PROV_FILE"
    # SHORT live (successful tool, FEWER rows than stored) -- the case 3.0.0_SA_CVO saw fire falsely at
    # 19:0xZ 2026-09-02 (ADVI_PERFRP-S1 "DISAPPEARED" while present in the file) and CVO~A confirmed
    # independently @217ffafada. Repair bar (CVO~A): a first short result is PROVISIONAL -- no warn, no
    # replace -- and absence is confirmed against the RAW corpus before any DISAPPEARED is emitted.
    # RAW_ROOT lets this suite point the corpus check at a temp tree instead of the live channel.
    # PASS 2 (3.0.0_SA_CVO, Andrew "All approved go" ~20:4xZ; CTO 92746 race note taken): a short
    # result is PROVISIONAL across POLLS, not confirmed by re-reading the raw file in the SAME poll --
    # a write does not straddle two polls, a same-poll grep can land inside it. So absence is
    # CONFIRMED only when the NEXT poll's sample still lacks the id. Four cases, each two polls where
    # it matters; PROV_FILE is the cross-poll carrier and the selftest points it at the temp tree.
    PROV_FILE="$T/prov.tsv"; rm -f "$PROV_FILE"
    printf 'print("org/surprise_channel/P/INVESTIGATION_v1.md\\tP-S1\\taaaaaaaaaaaa")\n' > "$T/short.py"
    printf 'print("org/surprise_channel/P/INVESTIGATION_v1.md\\tP-S1\\taaaaaaaaaaaa")\nprint("org/surprise_channel/P/INVESTIGATION_v1.md\\tP-S2\\tbbbbbbbbbbbb")\n' > "$T/whole.py"
    # (a) TRANSIENT SHORT, poll 1: no row-warn, COUNT-ONLY on stderr, index UNCHANGED, id marked provisional.
    rm -f "$PROV_FILE"; IDX_TOOL="$T/short.py";                                _case "SHORT poll 1: provisional, no warn, index kept" 0 1 1
    # (b) RECOVERY, poll 2 whole after a provisional short: no warnings at all, provisional cleared, index replaced (same rows).
    rm -f "$PROV_FILE"; IDX_TOOL="$T/short.py"; _index_diff >/dev/null 2>&1; IDX_TOOL="$T/whole.py"; _case "SHORT then WHOLE: recovery, silent, provisional cleared" 0 0 1
    [ -s "$PROV_FILE" ] && { fail=$((fail+1)); echo "  FAIL    provisional file not cleared after recovery"; } || { pass=$((pass+1)); echo "  OK      provisional file cleared after recovery"; }
    # (c) CONFIRMED DELETION, poll 2 still short with the SAME id missing: DISAPPEARED fires NOW, index = stored minus that row.
    IDX_TOOL="$T/short.py"; _index_diff >/dev/null 2>&1;                       _case "SHORT twice, same id: CONFIRMED DISAPPEARED on poll 2" 1 0 0
    # The index assertion must read the file RIGHT AFTER the confirming poll -- _case re-seeds at its
    # end, so a check placed after _case sees the seed, never the drop (first cut of this suite did).
    rm -f "$PROV_FILE"; printf '%s\n' "$seed" > "$IDX_FILE"; IDX_TOOL="$T/short.py"
    _index_diff >/dev/null 2>&1; _index_diff >/dev/null 2>&1
    if [ "$(tr -d '\r' < "$IDX_FILE" | grep -c 'P-S2')" -eq 0 ] && [ "$(tr -d '\r' < "$IDX_FILE" | grep -c 'P-S1')" -eq 1 ]; then pass=$((pass+1)); echo "  OK      confirmed row dropped from stored index; the present row kept"; else fail=$((fail+1)); echo "  FAIL    stored index after confirmation: $(tr -d '\r' < "$IDX_FILE" | cut -f2 | tr '\n' ' ')"; fi
    printf '%s\n' "$seed" > "$IDX_FILE"; rm -f "$PROV_FILE"
    # (d) CONCURRENT-APPEND BOUNDARY: live LONGER than stored, every stored row present: no warnings, replace.
    printf 'print("org/surprise_channel/P/INVESTIGATION_v1.md\\tP-S1\\taaaaaaaaaaaa")\nprint("org/surprise_channel/P/INVESTIGATION_v1.md\\tP-S2\\tbbbbbbbbbbbb")\nprint("org/surprise_channel/P/INVESTIGATION_v1.md\\tP-S3\\tcccccccccccc")\n' > "$T/longer.py"
    IDX_TOOL="$T/longer.py";                                                   _case "live LONGER than stored, all present: append boundary, silent, replace" 0 0 0
    # (e) E2 SECOND LIMB (CTO's stated bound, narrowed): a row short on TWO consecutive polls but STILL PRESENT
    # in its raw file must NOT be confirmed -- the index tool is omitting a present row. RAW_ROOT aims the
    # confirm-time file check at the temp tree; production reads REPO_ROOT. The residual is now two
    # INDEPENDENT races (index short on poll N AND the raw read racing a write on poll N+1), not one.
    mkdir -p "$T/org/surprise_channel/P"; printf '  "id": "P-S1",\n  "id": "P-S2",\n' > "$T/org/surprise_channel/P/INVESTIGATION_v1.md"
    RAW_ROOT="$T"; rm -f "$PROV_FILE"; IDX_TOOL="$T/short.py"; _index_diff >/dev/null 2>&1
    IDX_TOOL="$T/short.py";                                                    _case "E2: short twice but id STILL IN raw file -> NOT confirmed" 0 1 1
    unset RAW_ROOT; rm -f "$PROV_FILE"
    # TWO ROOTS (CTO repoint 2026-09-02): _watched_files sees a tree investigation doc beside a flat
    # one, and _project_of names the PROJECT for both shapes (a tree path's basename(dirname) is
    # "investigations", which is what the pre-repoint function would have reported).
    mkdir -p "$T/org/surprise_channel/P" "$T/org/missions/D8/ETFS/ETFS_TREEPRJ/surprise-channel/investigations"
    printf '  "id": "P-S1",\n' > "$T/org/surprise_channel/P/INVESTIGATION_v1.md"
    printf '  "id": "ETFS_TREEPRJ-S1",\n' > "$T/org/missions/D8/ETFS/ETFS_TREEPRJ/surprise-channel/investigations/INVESTIGATION_v1.md"
    _saved_channel="$CHANNEL_DIR"; _saved_root="$REPO_ROOT"
    CHANNEL_DIR="$T/org/surprise_channel"; REPO_ROOT="$T"
    _n="$(_watched_files | grep -c .)"
    if [ "$_n" -eq 2 ] && _watched_files | grep -q 'org/missions/D8/ETFS/ETFS_TREEPRJ/surprise-channel/investigations/INVESTIGATION_v1.md'; then pass=$((pass+1)); echo "  OK      two roots: _watched_files sees the flat AND the tree doc (2 of 2)"; else fail=$((fail+1)); echo "  FAIL    two roots: _watched_files saw $_n doc(s), want 2 incl. the tree path"; fi
    _p="$(_project_of "$T/org/missions/D8/ETFS/ETFS_TREEPRJ/surprise-channel/investigations/INVESTIGATION_v1.md")"
    if [ "$_p" = "ETFS_TREEPRJ" ]; then pass=$((pass+1)); echo "  OK      _project_of on a tree path -> ETFS_TREEPRJ"; else fail=$((fail+1)); echo "  FAIL    _project_of on a tree path -> '$_p' (want ETFS_TREEPRJ)"; fi
    _p="$(_project_of "$T/org/surprise_channel/P/INVESTIGATION_v1.md")"
    if [ "$_p" = "P" ]; then pass=$((pass+1)); echo "  OK      _project_of on a flat path -> P"; else fail=$((fail+1)); echo "  FAIL    _project_of on a flat path -> '$_p' (want P)"; fi
    CHANNEL_DIR="$_saved_channel"; REPO_ROOT="$_saved_root"
    # R4-c NEW-row arm: stored has S1 only, live (whole.py) has S1+S2 -> exactly one "NEW ROW P-S2"
    # line on STDOUT naming the row; a second poll (S2 now stored) names nothing. The synthetic tool
    # answers --index-rows with three columns, so the line reads fields=UNREAD -- the fields half is
    # exercised against the REAL validator below.
    rm -f "$PROV_FILE"; printf 'org/surprise_channel/P/INVESTIGATION_v1.md\tP-S1\taaaaaaaaaaaa\n' > "$IDX_FILE"
    IDX_TOOL="$T/whole.py"; quiet=0
    _out="$(_index_diff 2>/dev/null)"
    if [ "$(printf '%s\n' "$_out" | grep -c 'NEW ROW P-S2')" -eq 1 ] && [ "$(printf '%s\n' "$_out" | grep -c 'NEW ROW P-S1')" -eq 0 ]; then pass=$((pass+1)); echo "  OK      NEW-row arm: one line names P-S2 (S1, already stored, not named)"; else fail=$((fail+1)); echo "  FAIL    NEW-row arm: $(printf '%s\n' "$_out" | grep -c 'NEW ROW') NEW line(s): $(printf '%s' "$_out" | tr '\n' '|' | cut -c1-160)"; fi
    _out="$(_index_diff 2>/dev/null)"
    if [ "$(printf '%s\n' "$_out" | grep -c 'NEW ROW')" -eq 0 ]; then pass=$((pass+1)); echo "  OK      NEW-row arm: second poll, nothing new, names nothing"; else fail=$((fail+1)); echo "  FAIL    NEW-row arm: second poll named $(printf '%s\n' "$_out" | grep -c 'NEW ROW') row(s)"; fi
    _n7="$(python "$REPO_ROOT/.tools/surprise-corpus-validate.py" --index-rows 2>/dev/null | awk -F'\t' 'NF==7' | grep -c .)"
    _n3="$(python "$REPO_ROOT/.tools/surprise-corpus-validate.py" --index 2>/dev/null | grep -c .)"
    if [ "$_n7" -gt 0 ] && [ "$_n7" -eq "$_n3" ]; then pass=$((pass+1)); echo "  OK      real validator: --index-rows emits 7 columns for every --index row ($_n7 of $_n3)"; else fail=$((fail+1)); echo "  FAIL    real validator: --index-rows 7-col rows=$_n7 vs --index rows=$_n3"; fi
    rm -rf "$T"
    echo "selftest: $pass/$((pass+fail)) PASS"
    [ "$fail" -eq 0 ]
}

case "$MODE" in
selftest)
    _selftest; exit $?
    ;;
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

echo "surprise-watch: STREAM mode for $SERIAL watching $CHANNEL_DIR/*/INVESTIGATION_v* + org/missions/D*/*/*/surprise-channel/investigations/ (two roots; state $STATE_DIR) (persistent; READ-ONLY on the watched files; parent-tied: $([ "$PARENT_CHECK" -eq 1 ] && echo "pid $WATCH_PARENT" || echo "OFF"); wait=$([ "$_NOSPAWN" -eq 1 ] && echo no-spawn || echo sleep)/15s)" >&2

while true; do
    if [ "$PARENT_CHECK" -eq 1 ] && ! kill -0 "$WATCH_PARENT" 2>/dev/null; then
        ts="$(date -u +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || echo unknown-ts)"
        echo "$ts  SURPRISE-WATCH-SELF-EXIT  serial=$SERIAL  parent=$WATCH_PARENT gone -- exiting instead of orphaning" >> "$STATE_DIR/orphan-audit.log" 2>/dev/null || true
        exit 0
    fi
    _pass 0
    _wait_interval
done
