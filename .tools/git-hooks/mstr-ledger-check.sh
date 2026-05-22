#!/usr/bin/env bash
# mstr-ledger-check.sh -- Tier-0 Decision Ledger enforcement (Constitution Art. V).
#
# Pre-commit hook. Two checks:
#   CHECK 1  record integrity (UNIVERSAL): every changed Tier-0 record file
#            (ledger/LD-*, cycles/CY-*, ratifications/RT-*) is schema-validated.
#   CHECK 2  strategic-action ledger requirement (MSTR-SCOPED): a 0.0.0_AB_MSTR
#            commit touching any non-record path must include a valid Decision
#            Ledger entry; an unratified S3/S4 entry cannot be executed.
#
# SCOPE, STATED PLAINLY: this hook governs git COMMITS. It is not the entire
# enforcement regime -- non-git side effects are governed by the /govern skill
# discipline (Phase 3). See org/tier0/README.md.
#
# Override: MSTR_LEDGER_OVERRIDE="<reason>" -- audited; STRUCTURALLY IGNORED when
#           the committer is 0.0.0_AB_MSTR (MSTR cannot override its own gate).
#
# Rule 16 (CLAUDE.md): Git Bash 3.6.7 default utilities only -- git, grep, sed,
# awk, date, printf, basename, tr, mkdir. No pgrep/pkill/flock.
#
# Test seam: MSTR_LEDGER_STAGED_FILES (newline-separated) bypasses git diff.

set -uo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
AUDIT_LOG="$REPO_ROOT/org/tier0/audit/ledger-hook-audit.log"
TS="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
MSTR="0.0.0_AB_MSTR"

RAW_AUTHOR="${GIT_AUTHOR_NAME:-}"
AGENT="${RAW_AUTHOR%% <*}"
OVERRIDE="${MSTR_LEDGER_OVERRIDE:-}"

# Closed enums -- encoded HERE (in .tools/, not MSTR-writable). Mirror
# Constitution Art. II (decision_type) and the Stakes Matrix (stakes_class).
DECISION_TYPES="directive_execution directive_decomposition directive_conflict_resolution directive_risk_reduction clarification_request escalation halt amendment_proposal bypass_exception"
STAKES_CLASSES="S0 S1 S2 S3 S4"

audit() { mkdir -p "$(dirname "$AUDIT_LOG")" 2>/dev/null || true
          printf '%s %s\n' "$TS" "$*" >> "$AUDIT_LOG" 2>/dev/null || true; }
block() { echo "BLOCKED (mstr-ledger-check): $1" >&2; audit "BLOCK  ${AGENT:-UNKNOWN}  -- $1"; exit 1; }

# Staged files (test seam or real git).
STAGED="${MSTR_LEDGER_STAGED_FILES:-$(git diff --cached --name-only 2>/dev/null || true)}"
if [ -z "$STAGED" ]; then audit "PASS  ${AGENT:-UNKNOWN}  (no staged files)"; exit 0; fi

# --- frontmatter field reader: fm <file> <field> -> value (first --- ... --- block)
fm() {
  awk -v f="$2" '
    /^---[[:space:]]*$/ { d++; next }
    d==1 && index($0, f":")==1 { sub("^"f":[[:space:]]*",""); gsub(/\r/,""); print; exit }
  ' "$1" 2>/dev/null
}
in_set() { case " $2 " in *" $1 "*) return 0 ;; *) return 1 ;; esac; }

# --- validate a ledger (LD) entry ---
validate_ld() {
  local f="$1" fld dt sc st dr s4 rb
  [ -f "$f" ] || { echo "$f: file not found"; return 1; }
  grep -q '^---[[:space:]]*$' "$f" || { echo "$f: no YAML frontmatter"; return 1; }
  for fld in decision_id timestamp agent created_by decision_type stakes_class status directive_refs; do
    [ -n "$(fm "$f" "$fld")" ] || { echo "$f: missing required field '$fld'"; return 1; }
  done
  dt="$(fm "$f" decision_type)"; sc="$(fm "$f" stakes_class)"; st="$(fm "$f" status)"
  dr="$(fm "$f" directive_refs)"; s4="$(fm "$f" s4_type)"; rb="$(fm "$f" rollback_plan)"
  in_set "$dt" "$DECISION_TYPES" || { echo "$f: decision_type '$dt' not in the closed enum (Constitution Art. II)"; return 1; }
  in_set "$sc" "$STAKES_CLASSES" || { echo "$f: stakes_class '$sc' invalid"; return 1; }
  # Empty directive_refs => new goal => must be S4 + proposed (closes the no-mandate hatch).
  case "$dr" in
    "[]"|"[ ]"|"null"|"")
      [ "$sc" = "S4" ]       || { echo "$f: empty directive_refs is a new goal -- stakes_class must be S4"; return 1; }
      [ "$st" = "proposed" ] || { echo "$f: empty directive_refs (new goal) -- status must be proposed"; return 1; }
      ;;
  esac
  # S2+ requires a rollback_plan value.
  case "$sc" in S2|S3|S4) [ -n "$rb" ] || { echo "$f: stakes_class $sc requires rollback_plan"; return 1; } ;; esac
  # S4 requires s4_type.
  if [ "$sc" = "S4" ]; then
    case "$s4" in operational|constitutional) : ;;
      *) echo "$f: stakes_class S4 requires s4_type (operational|constitutional)"; return 1 ;;
    esac
  fi
  return 0
}

# --- validate a ratification (RT) record + independence ---
validate_rt() {
  local f="$1" fld lref ratifier verdict ldfile ldauthor lds4
  [ -f "$f" ] || { echo "$f: file not found"; return 1; }
  grep -q '^---[[:space:]]*$' "$f" || { echo "$f: no YAML frontmatter"; return 1; }
  for fld in ratification_id timestamp ledger_ref ratifier_agent verdict; do
    [ -n "$(fm "$f" "$fld")" ] || { echo "$f: missing required field '$fld'"; return 1; }
  done
  lref="$(fm "$f" ledger_ref)"; ratifier="$(fm "$f" ratifier_agent)"; verdict="$(fm "$f" verdict)"
  case "$verdict" in ratified|rejected|changes_requested) : ;;
    *) echo "$f: verdict '$verdict' invalid"; return 1 ;;
  esac
  case "$lref" in *,*|*" "*|"") echo "$f: ledger_ref must name exactly one LD"; return 1 ;; esac
  ldfile="$REPO_ROOT/org/tier0/ledger/${lref}.md"
  if [ -f "$ldfile" ]; then
    ldauthor="$(fm "$ldfile" created_by)"
    if [ -n "$ldauthor" ] && [ "$ldauthor" = "$ratifier" ]; then
      echo "$f: ratifier_agent ($ratifier) authored $lref -- author-independence violated (Art. XIV)"; return 1
    fi
    lds4="$(fm "$ldfile" s4_type)"
    if [ "$lds4" = "constitutional" ]; then
      echo "$f: $lref is constitutional S4 -- never CVO-ratifiable; Andrew renders (Art. XIV)"; return 1
    fi
  fi
  return 0
}

# --- validate a cycle (CY) record (lighter: frontmatter + attestation fields) ---
validate_cy() {
  local f="$1" fld
  [ -f "$f" ] || { echo "$f: file not found"; return 1; }
  grep -q '^---[[:space:]]*$' "$f" || { echo "$f: no YAML frontmatter"; return 1; }
  for fld in cycle_id started constitution_read stakes_matrix_read directives_read; do
    [ -n "$(fm "$f" "$fld")" ] || { echo "$f: missing required field '$fld'"; return 1; }
  done
  return 0
}

# ===== Override -- audited; structurally unavailable to MSTR =====
if [ -n "$OVERRIDE" ]; then
  if [ "$AGENT" = "$MSTR" ]; then
    echo "mstr-ledger-check: MSTR_LEDGER_OVERRIDE ignored -- MSTR cannot override its own ledger gate." >&2
    audit "OVERRIDE-REFUSED  $MSTR  -- MSTR self-override denied; reason=\"$OVERRIDE\""
    # fall through to the real checks
  else
    audit "OVERRIDE  ${AGENT:-UNKNOWN}  reason=\"$OVERRIDE\"  files=[$(printf '%s' "$STAGED" | tr '\n' ',')]"
    echo "mstr-ledger-check: OVERRIDE applied by ${AGENT:-UNKNOWN} -- logged; raises OVERRIDE_REVIEW in /mstr_review." >&2
    exit 0
  fi
fi

# ===== CHECK 1 -- record integrity (universal) =====
PROBLEMS=""
while IFS= read -r path; do
  [ -z "$path" ] && continue
  case "$(basename "$path")" in _TEMPLATE.md|README.md) continue ;; esac
  case "$path" in
    org/tier0/ledger/LD-*.md)        p="$(validate_ld "$REPO_ROOT/$path")" || PROBLEMS="$PROBLEMS
  $p" ;;
    org/tier0/ratifications/RT-*.md) p="$(validate_rt "$REPO_ROOT/$path")" || PROBLEMS="$PROBLEMS
  $p" ;;
    org/tier0/cycles/CY-*.md)        p="$(validate_cy "$REPO_ROOT/$path")" || PROBLEMS="$PROBLEMS
  $p" ;;
  esac
done <<EOF
$STAGED
EOF
if [ -n "$(printf '%s' "$PROBLEMS" | tr -d '[:space:]')" ]; then
  echo "BLOCKED (mstr-ledger-check): Tier-0 record integrity:" >&2
  printf '%s\n' "$PROBLEMS" | grep -v '^[[:space:]]*$' >&2
  audit "BLOCK  ${AGENT:-UNKNOWN}  -- record-integrity failure"
  exit 1
fi

# ===== CHECK 2 -- strategic-action ledger requirement (MSTR-scoped) =====
if [ "$AGENT" != "$MSTR" ]; then
  audit "PASS  ${AGENT:-UNKNOWN}  (non-MSTR -- record-integrity only)"
  exit 0
fi

STRATEGIC=0
while IFS= read -r path; do
  [ -z "$path" ] && continue
  case "$path" in
    org/tier0/ledger/*|org/tier0/cycles/*|org/tier0/reviews/*|org/tier0/ratifications/*) : ;;
    *) STRATEGIC=1 ;;
  esac
done <<EOF
$STAGED
EOF
if [ "$STRATEGIC" -eq 0 ]; then
  audit "PASS  $MSTR  (record-only commit)"
  exit 0
fi

# Strategic MSTR commit -- require >=1 Decision Ledger entry in the commit.
LD_FILES="$(printf '%s\n' "$STAGED" | grep -E '^org/tier0/ledger/LD-[0-9][0-9]*\.md$' || true)"
if [ -z "$LD_FILES" ]; then
  block "strategic MSTR commit touches non-record paths but includes no Decision Ledger entry (org/tier0/ledger/LD-*.md). Constitution Art. V: every commitment is ledgered before it propagates."
fi
while IFS= read -r ldf; do
  [ -z "$ldf" ] && continue
  prob="$(validate_ld "$REPO_ROOT/$ldf")" || block "ledger entry invalid -- $prob"
  sc="$(fm "$REPO_ROOT/$ldf" stakes_class)"
  case "$sc" in
    S3|S4)
      st="$(fm "$REPO_ROOT/$ldf" status)"
      rby="$(fm "$REPO_ROOT/$ldf" ratified_by)"
      if [ "$st" != "ratified" ] || [ -z "$rby" ] || [ "$rby" = "null" ]; then
        block "$ldf is $sc but status='$st' ratified_by='$rby' -- an unratified S3/S4 decision cannot be executed (Stakes Matrix gate, Art. XIV)."
      fi
      ;;
  esac
done <<EOF
$LD_FILES
EOF

audit "PASS  $MSTR  (strategic commit -- ledgered, schema valid, gate clear)"
exit 0
