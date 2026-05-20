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
HALT_GATE_INBOX_ROOT="${HALT_GATE_INBOX_ROOT:-${HALT_GATE_REPO_ROOT}/org/mcp/inbox}"
HALT_GATE_CONTEXT_FILE="${HALT_GATE_CONTEXT_FILE:-${HALT_GATE_REPO_ROOT}/.comp-graph/.agent_context}"
HALT_GATE_AUDIT_LOG="${HALT_GATE_AUDIT_LOG:-${HALT_GATE_REPO_ROOT}/org/halt-gate-override-audit.log}"

# --- serial resolution (PRD R4) -------------------------------------------------
# Echo the agent serial from .comp-graph/.agent_context (the SERIAL= line).
# Return 1 if the file is absent, unreadable, or the SERIAL value is empty.
halt_gate_resolve_serial() {
  local ctx="${HALT_GATE_CONTEXT_FILE}" serial=""
  [ -f "$ctx" ] || return 1
  serial="$(grep -m1 '^SERIAL=' "$ctx" 2>/dev/null | sed 's/^SERIAL=//' | tr -d '\r' | sed 's/[[:space:]]*$//')"
  [ -n "$serial" ] || return 1
  printf '%s\n' "$serial"
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
    printf 'HALT-GATE: ERROR -- agent serial unresolved (%s missing or SERIAL= empty).\n' \
      "$HALT_GATE_CONTEXT_FILE" >&2
    printf 'HALT-GATE: failing loud -- a checkpoint that cannot find its inbox must NOT green-light a deploy.\n' >&2
    return 3
  }

  # Scan the serial's own inbox AND the base-serial inbox (strip ~X suffix) --
  # a tilde-lane agent's STOP can land in either. Dedupe when there is no suffix.
  base="${serial%%~*}"
  scan_serials=("$serial")
  [ "$base" != "$serial" ] && scan_serials+=("$base")

  for s in "${scan_serials[@]}"; do
    while IFS= read -r f; do
      [ -n "$f" ] || continue
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
