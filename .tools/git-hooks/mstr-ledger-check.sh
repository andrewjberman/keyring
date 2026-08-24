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

# precomp_v1 (RV0017-F002): orchestrator may pre-resolve REPO_ROOT via
# PRECOMP_REPO_ROOT to skip the redundant git rev-parse subprocess.
REPO_ROOT="${PRECOMP_REPO_ROOT:-$(git rev-parse --show-toplevel 2>/dev/null || pwd)}"
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

# MERGE EXEMPTION (merge-exemption class, 2026-07-31) -- a merge integrates
# already-committed, already-validated work; the integrator is NOT its author, so it
# needs no Decision Ledger entry, and any merged records were schema-checked at their
# own authorship. Same class as the owned-paths merge exemption (CTO, c0241a1eaa).
# A merge is a merge regardless of how the staged list was sourced -- do NOT guard this
# on MSTR_LEDGER_STAGED_FILES (that inversion was the owned-paths production bug).
# Applied by 0.0.0_AB_MSTR (integrator) under Andrew-authorized emergency to clear a
# fabric-wide merge deadlock (mstr-ledger blocked every window merge); CTO to review +
# re-home the wording per SoD.
if git rev-parse -q --verify MERGE_HEAD >/dev/null 2>&1; then
    audit "PASS  ${AGENT:-UNKNOWN}  (MERGE COMMIT -- ledger requirement exempt; merged records validated at their own authorship)"
    exit 0
fi

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
# precomp_v1: bash parameter expansion `${path##*/}` replaces `basename` subprocess
# spawn (was ~200-300ms x N_files on Windows). Loop short-circuits paths outside
# org/tier0/{ledger,ratifications,cycles}/ entirely before any per-file work.
while IFS= read -r path; do
  [ -z "$path" ] && continue
  case "$path" in
    org/tier0/ledger/LD-*.md|org/tier0/ratifications/RT-*.md|org/tier0/cycles/CY-*.md) : ;;
    *) continue ;;
  esac
  bn="${path##*/}"
  case "$bn" in _TEMPLATE.md|README.md) continue ;; esac
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
    org/tier0/ledger/*|org/tier0/cycles/*|org/tier0/reviews/*|org/tier0/ratifications/*|org/tier0/sessions/*) : ;;
    org/tier0_exec/*/logs/*) : ;;
    org/tier0_exec/*/deliverables/ANDREW_DIRECT_*) : ;;  # ANDREW-DIRECT VERBATIM RECORDS (CTO gate-shape ruling 2026-08-24, on MSTR 66791; instance resolved as LD-0447). The org/XXX.md record+broadcast law obliges EVERY seat receiving an Andrew-direct instruction to record it durably SAME TURN -- and this gate classed that act as a strategic commitment requiring an LD minted FOR THE ACT OF WRITING HIS WORDS DOWN, taxing exactly the act we least want taxed (recording fast). By this allowlist's own stated reasoning (logs/* line, LD-0258: a record of decisions is not itself a decision), a verbatim record of HIS decision is the purest record there is; any strategic CONSEQUENCE is ledgered separately. NARROW BY CONSTRUCTION: the ANDREW_DIRECT_ filename prefix is the record-file convention (every seat's deliverables carry it); all OTHER tier0_exec deliverables remain STRATEGIC -- an MSTR deliverable that commits the fabric to something still needs its LD. Gate edited by CTO, not MSTR (the header's SoD line: the enums live in .tools, not MSTR-writable).  # MSTR's own session logs (org/tier0_exec/0.0.0_AB_MSTR/logs/**) are RECORDS, not strategic commitments -- the /log skill writes them here per org/XXX.md; the actual decisions are ledgered separately as LD-*. Closes the allowlist gap that misclassified every MSTR session-close /log as strategic (Andrew sovereign-authorized 2026-07-07; LD-0258).
    org/compiler-tools-log.md|org/git-author-override-audit.log|org/mcp/comp_ferry_queue.json) : ;;  # record-append / MSTR-owned execution-tracking (every-agent /log + author-override audit + the comp-ferry queue, LD-0119) -- tracking under an existing LD, not a new strategic commitment (MSTR gate-hygiene fix 2026-06-29)
    org/audit/archive/*) : ;;  # AUDIT-ARCHIVER TAMPER-EVIDENCE SNAPSHOTS (LD-0380, 2026-08-06). The audit-archive-invoker (CTO-ruled Option B 2026-07-19) commits its automated snapshots + FINDINGS.md as the RUNNING session's serial -- in an MSTR session that reads as an MSTR author, and this gate REFUSED the 2026-08-04T213358Z checkpoint as "strategic", punching a hole in the very integrity chain it protects (gate-vs-gate, CTO-surfaced 0055Z). An automated tamper-evidence snapshot is a RECORD, not a decision (same reasoning + authority chain as the logs/* line above); the invoker's own append-only clause polices content. NARROW BY CONSTRUCTION: this pattern is the archiver's entire write surface and nothing else writes here.
    # --- MISSION REGISTER (Andrew sovereign-authorized 2026-07-29, LD-0345) ---------------
    # ORDER IS LOAD-BEARING: `case` takes the FIRST match, so GOALS.yaml must be listed
    # BEFORE the general org/missions/* line or it would be swallowed as a record.
    org/missions/GOALS.yaml) STRATEGIC=1 ;;  # THE GOALS ARE THE STRATEGIC PART -- Andrew-approved
                                             # mission goals. Changing one IS a new commitment and
                                             # still requires an LD. This is the half of the register
                                             # the gate must keep holding.
    org/missions/*) : ;;                     # The rest of the register is a RECORD, not a commitment:
                                             # commits.jsonl is machine-written by comp-missions scan;
                                             # MISSIONS.md is COMPILED (never hand-authored);
                                             # state.yaml/execsum.yaml carry stance + prose ABOUT work
                                             # whose decisions are ledgered separately (LD-0341 and its
                                             # amendments). Same reasoning and same authority as the
                                             # org/tier0_exec/*/logs/* line above (LD-0258): a record of
                                             # decisions is not itself a decision. Without this, every
                                             # register correction -- including fixing a STALE line --
                                             # required its own ledger amendment, which made the register
                                             # expensive to keep TRUE and left a post-commit-hook-refreshed
                                             # file permanently dirty in a SHARED worktree, blocking peers'
                                             # pushes. Four blocks in one session, and a live DT push
                                             # blocked at 020142Z, is what earned this.
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
