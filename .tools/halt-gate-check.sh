#!/usr/bin/env bash
# =============================================================================
# halt-gate-check.sh -- HALTGT checkpoint core library (ADHC_HALTGT.001)
# =============================================================================
# Fires at deploy time, BEFORE a long irreversible operation. Reads the running
# agent's MCP inbox, classifies each pending (unread) message as STOP-class or
# routine per docs/architecture/HALTGT_SEVERITY_CONVENTION.md, and renders the
# ADHC_HALTGT PRD section 3.2 tiered verdict.
#
# Tiered verdict:
#   - Empty inbox                 -> PASS silently, exit 0.
#   - Routine message(s) pending  -> SURFACE (sender/subject/age), exit 1.
#                                    Re-invoke with HALT_ACK=1 to pass (exit 0).
#   - STOP-class message present  -> HARD-BLOCK, exit 2.
#                                    Bypass with HALT_OVERRIDE="<reason>" -- the
#                                    override is audited to
#                                    org/halt-gate-override-audit.log, exit 0.
#   - Serial cannot be resolved   -> FAIL LOUD, exit 3. NEVER a silent pass.
#   - Serial names NO known agent -> FAIL LOUD, exit 3 (Andrew-direct 2026-07-30;
#     a corrupted serial file must not make the gate scan a nonexistent inbox).
#
# Non-interactive by contract: every consumer is an agent Bash-tool call with no
# TTY. This library NEVER reads stdin -- both the routine ack and the STOP
# override are env-var gates (HALT_ACK / HALT_OVERRIDE), so a deploy can never
# hang on a prompt.
#
# Dual-mode: source it for the functions (halt_gate_check, halt_gate_main, ...)
# or run it directly. Stable sourceable surface for ADHC_HALTGT.002 / .003:
#   halt_gate_main [context-label]   -> runs the checkpoint, returns the exit code
#   halt_gate_check                  -> core logic, no printing of the banner
# Exit-code contract (stable): 0 pass | 1 routine-unacked | 2 stop-block | 3 no-serial.
#
# Git Bash 3.6.7-safe (CLAUDE.md Rule 16): uses only bash/grep/find/date/sed/
# awk/mktemp -- no pgrep/pkill/flock/pidof/setsid/wget. ASCII only -- no emoji.
# =============================================================================

# Repo root: this file lives in <repo>/.tools/ . Overridable for tests.
HALT_GATE_REPO_ROOT="${HALT_GATE_REPO_ROOT:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." 2>/dev/null && pwd)}"
# THE SHARED CHECKOUT (NFRA_OPLGTW-S19, S18 and W1-S6; LGIC_ENFORCE-W3-S6; 2026-09-15, 1.0.0_SA_CTO). A spine-v3
# worker runs this gate from its OWN linked worktree, where org/mcp/inbox and org/mcp/sessions (both gitignored) do not
# exist: they live only in the main checkout. Rooted at this script's checkout, the gate read an ABSENT inbox as "no
# messages" (halt_gate_unread_for) and passed rc=0, so a [STOP] to a worker's issuer never halted the worker's apply;
# and identity failed closed rc=3. Measured by 2.0.0_SA_COO~O as a discriminating pair in one worktree at one HEAD:
# default root rc=0 silent, HALT_GATE_INBOX_ROOT at the shared inbox rc=1 with 14 pending (97257).
# git's common dir is the main checkout's .git from EVERY worktree, so its parent is the one checkout that holds the
# live inbox and sessions. Outside a git checkout (a test's temp root) it falls back to the repo root, the prior
# behaviour. Overridable for tests.
if [ -z "${HALT_GATE_SHARED_ROOT:-}" ]; then
  _hg_common="$(cd "$HALT_GATE_REPO_ROOT" 2>/dev/null && git rev-parse --git-common-dir 2>/dev/null)"
  if [ -n "$_hg_common" ]; then
    HALT_GATE_SHARED_ROOT="$(cd "$HALT_GATE_REPO_ROOT" 2>/dev/null && cd "$_hg_common/.." 2>/dev/null && pwd)"
  fi
  HALT_GATE_SHARED_ROOT="${HALT_GATE_SHARED_ROOT:-$HALT_GATE_REPO_ROOT}"
fi
HALT_GATE_INBOX_ROOT="${HALT_GATE_INBOX_ROOT:-${HALT_GATE_SHARED_ROOT}/org/mcp/inbox}"
HALT_GATE_CONTEXT_FILE="${HALT_GATE_CONTEXT_FILE:-${HALT_GATE_REPO_ROOT}/.comp-graph/.agent_context}"
HALT_GATE_AUDIT_LOG="${HALT_GATE_AUDIT_LOG:-${HALT_GATE_REPO_ROOT}/org/halt-gate-override-audit.log}"

# --- serial resolution (PRD R4 + LD-0070 §7.2 session-id-keyed) -----------------
# Resolve the agent serial via the session-id-keyed pattern first (per LD-0070
# §7.2; matches TARGET A telemetry hook pattern at e410400f8). Falls back to the
# legacy .comp-graph/.agent_context if session-id path unavailable. Eliminates
# the cross-agent contamination class where one agent's serial in the shared
# .comp-graph/.agent_context file clobbers the halt-gate diagnostic for any
# other concurrent agent running halt-gate-check.sh. Empirical anchor:
# 2026-05-26 cycle #21 -- CL CTO clobbered ws CTO's .comp-graph state mid-session;
# halt-gate misroutd MSTR-FERRY-addressed-to-CL-CTO as ws CTO's pending message.
halt_gate_resolve_serial() {
  local repo_root="${HALT_GATE_REPO_ROOT}" ctx="${HALT_GATE_CONTEXT_FILE}" serial=""

  # Primary: session-id-keyed serial file (LD-0070 §7.2 canonical). Two directories, in order: this checkout's own
  # (an issuer may provision a worker's serial inside the worker's worktree, so parallel workers of one session each
  # resolve as themselves), then the SHARED checkout's, where a session's serial file actually lives. The second was
  # unreachable from a linked worktree before 2026-09-15 (see HALT_GATE_SHARED_ROOT above).
  if [ -n "${CLAUDE_CODE_SESSION_ID:-}" ]; then
    local sess_dir sess_file
    for sess_dir in "${repo_root}/org/mcp/sessions" "${HALT_GATE_SHARED_ROOT}/org/mcp/sessions"; do
      sess_file="${sess_dir}/${CLAUDE_CODE_SESSION_ID}.serial"
      if [ -f "$sess_file" ]; then
        serial="$(tr -d '\r\n[:space:]' < "$sess_file" 2>/dev/null)"
        if [ -n "$serial" ]; then
          printf '%s\n' "$serial"
          return 0
        fi
      fi
    done

    # Secondary (session-keyed, clobber-PROOF): the register_agent PostToolUse hook
    # (hook_register_orphan_cleanup.py) writes a per-(session,serial) marker
    # `${sid}.${serial}.orphan-cleaned` -- it encodes THIS agent's serial in the filename and is scoped
    # to THIS session, so it resolves the true invoker even when the .serial file above is absent, WITHOUT
    # falling to the shared .agent_context (which is last-writer-wins across concurrent agents and silently
    # mis-attributes -- the safe-ec2-deploy deployed_by mis-derivation, 5x on 2026-07-07 recorded another
    # agent's serial into the EC2 manifest ledger). If several markers exist (an agent re-registered under
    # >1 serial this session) the NEWEST wins = the current active serial. Real serials carry no '/', so
    # the hook's '/'->'_' safe_serial is byte-identical to the serial.
    local marker
    marker="$(ls -t "${repo_root}/org/mcp/sessions/${CLAUDE_CODE_SESSION_ID}."*.orphan-cleaned 2>/dev/null | head -1)"
    [ -n "$marker" ] || marker="$(ls -t "${HALT_GATE_SHARED_ROOT}/org/mcp/sessions/${CLAUDE_CODE_SESSION_ID}."*.orphan-cleaned 2>/dev/null | head -1)"
    if [ -n "$marker" ]; then
      serial="$(basename "$marker")"
      serial="${serial#"${CLAUDE_CODE_SESSION_ID}".}"
      serial="${serial%.orphan-cleaned}"
      if [ -n "$serial" ]; then
        printf '%s\n' "$serial"
        return 0
      fi
    fi
  fi

  # --- FAIL CLOSED (Andrew-direct 2026-07-13; CTO) --------------------------------
  # The legacy `.comp-graph/.agent_context` fallback is REMOVED. It is a SHARED,
  # LAST-WRITER-WINS file, and org/XXX.md:90 states the law outright:
  #     "`.comp-graph/.agent_context` is NOT an identity source."
  # `register_agent` carries a hard IDENTITY GUARD against exactly this. The halt
  # gate had none -- so it resolved whichever serial some *other* agent wrote last.
  #
  # MEASURED 2026-07-13 (1.0.0_SA_CTO, on the live primitive): with no session-keyed
  # serial file, this function returned `0.7.0_AE_CloudOps` -- A DEAD AGENT. At an
  # earlier push it had returned `2.0.0_SA_COO`. The gate scanned THEIR inboxes.
  #
  # BOTH failure directions, and the second is the dangerous one:
  #   FALSE POSITIVE  blocked on a STOP addressed to a stranger.  (loud; I noticed)
  #   FALSE NEGATIVE  *** MY OWN inbox was NEVER SCANNED. A genuine [STOP] addressed
  #                   to me would have been INVISIBLE to my own halt gate, and I would
  #                   have pushed straight through it with a clean exit 0. ***
  # Rule 18 already concedes "a HALTGT pass is not evidence you were not halted," but
  # it locates the defect in WHICH FILES are seen. The real defect is one level up:
  # <serial> may be THE WRONG AGENT ENTIRELY.
  #
  # >> A SAFETY GATE THAT CANNOT NAME ITS OWN PRINCIPAL MUST NOT GUESS. Guessing does
  #    not degrade a control -- it converts it into a random number generator that is
  #    wrong in BOTH directions while reporting success. <<
  #
  # Callers treat a non-zero return as exit 3 = NO-SERIAL = BLOCK (halt_gate_check:171
  # already says: "a checkpoint that cannot find its inbox must NOT green-light a
  # deploy"). That path existed and was simply never reachable, because the fallback
  # always "succeeded" -- with someone else's name.
  #
  # REMEDIATION IS ONE LINE (printed by the caller):
  #     printf '%s\n' "<your-serial>" > "org/mcp/sessions/${CLAUDE_CODE_SESSION_ID}.serial"
  return 1
}

# --- serial VALIDATION (Andrew-direct 2026-07-30) --------------------------------
# A RESOLVED serial is not necessarily a REAL one. Measured 2026-07-30 (0.0.0_AB_
# MSTR~Z, site Z): a printf escaping slip wrote "0.0.0_AB_MSTR~Zn" -- a serial that
# exists nowhere -- into the session serial file, and this gate ACCEPTED it,
# scanned a nonexistent nested inbox, and PASSED. Andrew-direct, verbatim:
# "halt-gate should not accept nonexistent serials that should fail loudly."
# Two checks, same resolver contract as inbox-watch.sh:82-89 / agent-poller.py
# _find_agent_folder:
#   (1) the BASE serial must match an agent home folder under the tier dirs;
#   (2) a ~lane suffix must be a single uppercase letter (every fabric lane is:
#       ~A..~E, ~Z; "Zn" is exactly the corruption shape that got through).
# Unknown -> caller renders the loud exit-3 fail-closed banner. NEVER silent.
# --- SPINE v3 WORKER (2026-09-04; 2.0.0_SA_COO~A 94157, gate 1 of v3's first worker drain) ---------
# 0.9.0_WK_<CODE>~<n> has no home folder and a DIGIT lane, so the two checks below refused every
# worker and no L7 worker could safe-apply or safe-ec2-deploy; the commit lane learned about workers
# at e08447ff7d and this gate did not. A worker is a REAL principal iff a NON-TERMINAL task order
# under <CODE> at HEAD is issued_to it -- the same grant rule the commit lane reads
# (ADHC_OWNPTH.005; the terminal words are the TO protocol's). Its STOPs are its ISSUER's: a worker
# has no inbox by design (spine v3 L7), so the gate scans the inbox of the issuer that order names
# and a [STOP] to the issuer halts its workers' deploys. Fail-closed: no such order, no admission.
halt_gate_worker_issuer() {
  # Prints the <issued_by> of a NON-TERMINAL task order under the worker's project that is
  # issued_to the worker, read at HEAD; rc 1 when none. A `git show` that fails is a `continue`
  # (toward refusal), never an absence verdict.
  local serial="$1" code p text issued_to status issued_by
  code="${serial#0.9.0_WK_}"; code="${code%%~*}"
  [ -n "$code" ] || return 1
  while IFS= read -r p; do
    [ -n "$p" ] || continue
    text="$(git -C "$HALT_GATE_REPO_ROOT" show "HEAD:$p")" || continue
    issued_to="$(printf '%s\n' "$text" | grep -m1 -oE '<issued_to>[^<]*</issued_to>' | sed -E 's/<[^>]+>//g' | tr -d ' \r')"
    [ "$issued_to" = "$serial" ] || continue
    status="$(printf '%s\n' "$text" | grep -m1 -oiE '<status>[[:space:]]*[A-Za-z_-]+' | sed -E 's/<status>[[:space:]]*//' | tr 'A-Z' 'a-z')"
    case "$status" in
      complete|completed|closed|done|superseded|cancelled|canceled|withdrawn) continue ;;
    esac
    issued_by="$(printf '%s\n' "$text" | grep -m1 -oE '<issued_by>[^<]*</issued_by>' | sed -E 's/<[^>]+>//g' | tr -d ' \r')"
    [ -n "$issued_by" ] || continue
    printf '%s\n' "$issued_by"
    return 0
  done < <(git -C "$HALT_GATE_REPO_ROOT" ls-files -- "org/missions/D*/*/${code}/task-orders/*.md")
  return 1
}

halt_gate_validate_serial() {
  local serial="$1" base lane tier d found=0
  base="${serial%%~*}"
  [ -n "$base" ] || return 1
  case "$serial" in
    0.9.0_WK_*~[0-9]*)
      HALT_GATE_WORKER_ISSUER="$(halt_gate_worker_issuer "$serial")" || return 1
      export HALT_GATE_WORKER_ISSUER
      return 0 ;;
  esac
  if [ "$serial" != "$base" ]; then
    lane="${serial#*~}"
    case "$lane" in
      [A-Z]) : ;;
      *) return 1 ;;
    esac
  fi
  for tier in tier0_exec tier0_utility tier1_exec tier2_senior tier3_junior; do
    for d in "${HALT_GATE_REPO_ROOT}/org/${tier}"/*/; do
      [ -d "$d" ] || continue
      case "$(basename "$d")" in
        *"$base"*) found=1; break 2 ;;
      esac
    done
  done
  [ "$found" -eq 1 ]
}

# --- STOP-class classifier (ADHC_HALTGT.000 canonical rule) ---------------------
# Return 0 if the message file is STOP-class, 1 if routine. Transcribes the
# HALTGT_SEVERITY_CONVENTION.md match rule verbatim: a [STOP] or [HALT] token at
# the start of the subject text, case-sensitive, brackets required.
halt_gate_is_stop_class() {
  local msg_file="$1"
  [ -f "$msg_file" ] || return 1
  grep -m1 '^\*\*Subject:\*\*' "$msg_file" 2>/dev/null \
    | grep -qE '^\*\*Subject:\*\* *\[(STOP|HALT)\]'
}

# --- field extraction -----------------------------------------------------------
halt_gate_subject() {
  grep -m1 '^\*\*Subject:\*\*' "$1" 2>/dev/null | sed 's/^\*\*Subject:\*\* *//' | tr -d '\r'
}

halt_gate_sender() {
  # Message files lead with "# Message from <serial>".
  grep -m1 '^# Message from ' "$1" 2>/dev/null | sed 's/^# Message from //' | tr -d '\r'
}

halt_gate_recipient() {
  # Message files carry the intended recipient on a "**To:** <serial>" line.
  # Empty string if absent (older files / non-broker writes) -- callers must
  # fail SAFE on empty (include the message; never drop a possible STOP we
  # cannot classify). Used by the LD-0131 recipient-scoping filter.
  grep -m1 '^\*\*To:\*\*' "$1" 2>/dev/null \
    | sed 's/^\*\*To:\*\* *//' | tr -d '\r' | sed 's/[[:space:]]*$//'
}

halt_gate_age_label() {
  # Human age from file mtime. Falls back to "unknown" if mtime is unreadable.
  local f="$1" now mtime delta
  now="$(date +%s 2>/dev/null)" || now=""
  mtime="$(date -r "$f" +%s 2>/dev/null)" || mtime=""
  if [ -z "$now" ] || [ -z "$mtime" ]; then
    printf 'age unknown'
    return 0
  fi
  delta=$(( now - mtime ))
  [ "$delta" -lt 0 ] && delta=0
  if [ "$delta" -lt 3600 ]; then
    printf '%dm ago' $(( delta / 60 ))
  elif [ "$delta" -lt 86400 ]; then
    printf '%dh ago' $(( delta / 3600 ))
  else
    printf '%dd ago' $(( delta / 86400 ))
  fi
}

# --- inbox enumeration ----------------------------------------------------------
# Echo (newline-separated) the unread message files for a serial. Unread = *.md
# directly under inbox/<serial>/ (NOT under inbox/<serial>/read/). -maxdepth 1
# excludes the read/ subdir. Missing inbox dir = no messages (not an error).
halt_gate_unread_for() {
  local serial="$1" dir="${HALT_GATE_INBOX_ROOT}/$1"
  [ -d "$dir" ] || return 0
  find "$dir" -maxdepth 1 -type f -name '*.md' 2>/dev/null | sort
}

# --- audited override (mirrors safe-commit.sh --force audit pattern) -------------
halt_gate_write_audit() {
  local serial="$1" sender="$2" subject="$3" context="$4" reason="$5" ts
  ts="$(date -u +%Y-%m-%dT%H:%M:%SZ 2>/dev/null)" || ts="unknown"
  mkdir -p "$(dirname "$HALT_GATE_AUDIT_LOG")" 2>/dev/null || true
  printf '%s  HALT-OVERRIDE  agent=%s  stop_from=%s  subject=%s  context=%s  reason=%s\n' \
    "$ts" "$serial" "${sender:-unknown}" "${subject:-unknown}" \
    "${context:-unspecified}" "${reason:-unspecified}" >> "$HALT_GATE_AUDIT_LOG"
}

# --- core checkpoint ------------------------------------------------------------
# Args: $1 = optional context label (the deploy operation being gated).
# Prints the verdict. Returns: 0 pass | 1 routine-unacked | 2 stop-block | 3 no-serial.
halt_gate_check() {
  local context="${1:-${HALT_GATE_CONTEXT:-unspecified}}"
  local serial base f s
  local -a scan_serials=() msg_files=() stop_files=()

  serial="$(halt_gate_resolve_serial)" || {
    printf '======================================================================\n' >&2
    printf 'HALT-GATE: IDENTITY UNRESOLVED -- BLOCKED (fail-closed)\n' >&2
    printf '======================================================================\n' >&2
    printf '  This gate could not determine WHICH AGENT it is running as from any\n' >&2
    printf '  session-keyed source. It will NOT guess.\n\n' >&2
    printf '  It used to guess -- from .comp-graph/.agent_context, a SHARED\n' >&2
    printf '  last-writer-wins file. That made it scan ANOTHER agent`s inbox:\n' >&2
    printf '    - it blocked you on STOPs addressed to strangers, AND\n' >&2
    printf '    - *** IT NEVER SCANNED YOUR OWN INBOX, so a real [STOP] to YOU\n' >&2
    printf '        was INVISIBLE and you pushed straight through it. ***\n\n' >&2
    printf '  A safety gate that cannot name its own principal must not guess.\n\n' >&2
    printf '  FIX (one line -- use YOUR serial, incl. any ~lane suffix):\n' >&2
    printf '    printf %%s\\\\n "1.2.3_XX_Yourserial" > "org/mcp/sessions/%s.serial"\n' \
      "${CLAUDE_CODE_SESSION_ID:-<CLAUDE_CODE_SESSION_ID-IS-UNSET>}" >&2
    printf '\n  Then re-run. Do NOT override this; overriding it means deploying\n' >&2
    printf '  while blind to your own STOP messages.\n' >&2
    printf '======================================================================\n' >&2
    return 3
  }

  # A serial that matches NO agent fails closed exactly like an absent one
  # (Andrew-direct 2026-07-30: "halt-gate should not accept nonexistent serials
  # that should fail loudly"). Without this, a corrupted serial file (measured:
  # "0.0.0_AB_MSTR~Zn", a printf slip on site Z) makes the gate scan a
  # nonexistent inbox and green-light the push -- blind to every real STOP.
  if ! halt_gate_validate_serial "$serial"; then
    printf '======================================================================\n' >&2
    printf 'HALT-GATE: SERIAL RESOLVES TO NO KNOWN AGENT -- BLOCKED (fail-closed)\n' >&2
    printf '======================================================================\n' >&2
    printf '  Resolved serial: %s\n' "$serial" >&2
    printf '  No agent home folder under org/tier*_*/ matches its base, or its\n' >&2
    printf '  ~lane suffix is not a single uppercase letter; a spine-v3 worker\n' >&2
    printf '  (0.9.0_WK_<CODE>~<n>) is admitted only while a NON-TERMINAL task\n' >&2
    printf '  order under <CODE> at HEAD is issued_to it. This is usually a\n' >&2
    printf '  CORRUPTED session serial file (escaping slip / stray character):\n' >&2
    printf '    org/mcp/sessions/%s.serial\n' "${CLAUDE_CODE_SESSION_ID:-<unset>}" >&2
    printf '  Scanning a nonexistent inbox would PASS while a real [STOP] to the\n' >&2
    printf '  real you sits unread. Fix the serial file and re-run:\n' >&2
    printf '    printf %%s\\\\n "<your-real-serial>" > "org/mcp/sessions/%s.serial"\n' \
      "${CLAUDE_CODE_SESSION_ID:-<CLAUDE_CODE_SESSION_ID-IS-UNSET>}" >&2
    printf '======================================================================\n' >&2
    return 3
  fi

  # A WORKER scans its ISSUER (the block above): a worker has no inbox, and a [STOP] addressed to
  # the seat that issued its order is the STOP that halts it. Printed so the scan's principal is
  # never silent.
  if [ -n "${HALT_GATE_WORKER_ISSUER:-}" ]; then
    printf 'HALT-GATE: worker %s has no inbox; scanning its issuer %s (a [STOP] to the issuer halts its workers)\n' \
      "$serial" "$HALT_GATE_WORKER_ISSUER" >&2
    serial="$HALT_GATE_WORKER_ISSUER"
  fi

  # Scan the serial's own inbox AND the base-serial inbox (strip ~X suffix) --
  # a tilde-lane agent's STOP can land in either. Dedupe when there is no suffix.
  base="${serial%%~*}"
  scan_serials=("$serial")
  # THE THIRD PATH (0.8.0_AE_CloudComp~C, 2026-07-25; ruled + re-derived by 1.0.0_SA_CTO 183004Z).
  # The comment below said "a tilde-lane agent's STOP can land in either." IT CANNOT. The two dirs
  # named there are FLAT inbox/<serial~lane>/ and inbox/<base>/. The broker writes NEITHER for a
  # lane message -- it writes NESTED inbox/<base>/~<lane>/ (LD-0105 suffix-strip + nest; its own
  # receipts read "delivered to X~D (inbox X/~D)"). Live counts, every tilde lane on the box:
  # FLAT = 0 *.md (only a read/ subdir); NESTED = 530 (CTO~Z) / 1076 (COO~B) / 495 (CTO~B) / 420 (AE~D).
  # So the own-serial limb was a STRUCTURAL NO-OP for every tilde lane, leaving base as the only
  # working scan -- and therefore:
  #
  #   >> ADDRESSING A [STOP] MORE PRECISELY MADE IT LESS BINDING. The precise form was
  #      delivered-but-not-enforcing; the base form enforcing-but-not-delivered. Neither was both. <<
  #
  # DISTINCT FROM THE DEFECT AT :98-101 -- and the distinction is the durable part. That one is the
  # IDENTITY axis (the gate resolving another agent's serial off the shared .agent_context), fixed
  # 07-13 by the session-keyed serial file. This is the PATH axis: the serial resolves CORRECTLY and
  # the gate then builds the wrong DIRECTORY. Same symptom, two mechanisms, and the fixed one sat in
  # front of the live one:
  #
  #   >> A REMEDIATED DEFECT STANDING IN FRONT OF AN UNREMEDIATED ONE IS BETTER COVER THAN NO
  #      COMMENT AT ALL -- the reader's own diligence (reading the comment) is what closes the
  #      case prematurely. <<
  #
  # The FLAT limb is RETAINED deliberately: it is inert today, but removing it is a second
  # behaviour change riding a fix, and the two would be indistinguishable in the blame if anything
  # regressed. Strip it later as its own change if wanted. halt_gate_unread_for concatenates
  # ${INBOX_ROOT}/$1, so "<base>/~<lane>" path-joins correctly and needs no change there; the
  # recipient-scoping filter below is unaffected (it keys on the To: base, not the directory).
  #
  # WARNING TO A FUTURE FIXER: do NOT "fix" this class by pointing a WATCHER at the flat path.
  # That path is dead -- it would look like a fix, change nothing, and retire the symptom.
  # Exercise: scratchpad haltgate-lane-exercise.sh (5/5 pre, 6/6 post; cell 4 is the mutant that
  # makes the negative cell falsifiable, cell 5 proves routine lane mail surfaces rc=1, NOT rc=2).
  if [ "$base" != "$serial" ]; then
    scan_serials+=("$base" "${base}/~${serial#*~}")
  fi

  # LD-0131 Layer 1 -- recipient-scoping. A HALTGT must only trip on messages
  # addressed to the RUNNING agent. LD-0099 filesystem-direct ferries to a
  # tilde-lane (broker strips the ~suffix per LD-0105) scatter EXTRA copies into
  # UNRELATED base inboxes; those land at top-level here and falsely trip the
  # wrong agent's gate (DS-MI/AE hit by RD~B ferries 2026-05-28; the
  # MSTR-FERRY-to-CL-CTO anchor at line ~49). Filter: skip a file whose intended
  # recipient (**To:**), base-stripped, differs from the running serial's base.
  # FAIL-SAFE: a file with no parseable To: is INCLUDED -- never drop a message
  # we cannot classify (guardrail (i): no regression on a genuine same-serial
  # STOP). Same-base messages (incl. sibling ~lanes + the base itself) are kept,
  # matching the scan-both-serial-and-base philosophy and MSTR's anti-over-scope
  # bound (do NOT suppress same-base pendings).
  local to_field to_base
  for s in "${scan_serials[@]}"; do
    while IFS= read -r f; do
      [ -n "$f" ] || continue
      # RACE GUARD (1.0.0_SA_CTO~Z, 2026-09-03; observed by 0.0.0_AB_MSTR~Z 08:12:32Z): a file the
      # listing named but which is gone by the time it is read was moved to read/ by the agent's own inbox
      # watcher between the find and this stat -- it is a DELIVERED message, not an unread one. Without this
      # line the vanished file falls through both fail-safes (empty To: -> included; not stop-class ->
      # routine) and blocks the push as "1 pending (age unknown)", inviting HALT_ACK=1 spent on a race.
      [ -f "$f" ] || continue  # HALT-GATE-RACE-GUARD (the battery's mutant deletes exactly this line)
      to_field="$(halt_gate_recipient "$f")"
      if [ -n "$to_field" ]; then
        to_base="${to_field%%~*}"
        [ "$to_base" != "$base" ] && continue
      fi
      msg_files+=("$f")
      if halt_gate_is_stop_class "$f"; then
        stop_files+=("$f")
      fi
    done < <(halt_gate_unread_for "$s")
  done

  # Verdict 1: empty inbox -> pass silently.
  if [ "${#msg_files[@]}" -eq 0 ]; then
    return 0
  fi

  # Verdict 3: STOP-class present -> hard-block (override-able, audited).
  if [ "${#stop_files[@]}" -gt 0 ]; then
    printf '======================================================================\n' >&2
    printf 'HALT-GATE: STOP-CLASS MESSAGE -- HARD BLOCK (%s)\n' "$context" >&2
    printf '======================================================================\n' >&2
    for f in "${stop_files[@]}"; do
      printf '  [STOP] from %s\n         %s\n         (%s)  %s\n' \
        "$(halt_gate_sender "$f")" "$(halt_gate_subject "$f")" \
        "$(halt_gate_age_label "$f")" "$f" >&2
    done
    if [ -n "${HALT_OVERRIDE:-}" ]; then
      for f in "${stop_files[@]}"; do
        halt_gate_write_audit "$serial" "$(halt_gate_sender "$f")" \
          "$(halt_gate_subject "$f")" "$context" "$HALT_OVERRIDE"
      done
      printf 'HALT-GATE: OVERRIDE accepted -- audited to %s. Proceeding.\n' \
        "$HALT_GATE_AUDIT_LOG" >&2
      return 0
    fi
    printf 'HALT-GATE: blocked. Resolve the STOP, or bypass with an audited override:\n' >&2
    printf '           HALT_OVERRIDE="<reason>" <re-run the deploy command>\n' >&2
    return 2
  fi

  # Verdict 2: routine message(s) pending -> surface + require ack.
  printf '======================================================================\n' >&2
  printf 'HALT-GATE: %d pending message(s) -- review before proceeding (%s)\n' \
    "${#msg_files[@]}" "$context" >&2
  printf '======================================================================\n' >&2
  for f in "${msg_files[@]}"; do
    printf '  from %s\n       %s\n       (%s)\n' \
      "$(halt_gate_sender "$f")" "$(halt_gate_subject "$f")" "$(halt_gate_age_label "$f")" >&2
  done
  if [ -n "${HALT_ACK:-}" ]; then
    printf 'HALT-GATE: HALT_ACK set -- messages acknowledged. Proceeding.\n' >&2
    return 0
  fi
  printf 'HALT-GATE: blocked. Review the message(s) above, then re-run with HALT_ACK=1.\n' >&2
  return 1
}

# --- direct-run entry point -----------------------------------------------------
halt_gate_main() {
  halt_gate_check "$@"
}

# Run only when executed directly; stay quiet when sourced as a library.
if [ "${BASH_SOURCE[0]}" = "${0}" ]; then
  halt_gate_main "$@"
  exit $?
fi
