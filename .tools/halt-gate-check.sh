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

  # Primary: session-id-keyed serial file (LD-0070 §7.2 canonical)
  if [ -n "${CLAUDE_CODE_SESSION_ID:-}" ]; then
    local sess_file="${repo_root}/org/mcp/sessions/${CLAUDE_CODE_SESSION_ID}.serial"
    if [ -f "$sess_file" ]; then
      serial="$(tr -d '\r\n[:space:]' < "$sess_file" 2>/dev/null)"
      if [ -n "$serial" ]; then
        printf '%s\n' "$serial"
        return 0
      fi
    fi
  fi

  # Fallback: legacy .comp-graph/.agent_context (per-workspace-shared; clobber-prone)
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
