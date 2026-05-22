#!/usr/bin/env bash
# test-mstr-ledger-check.sh -- smoke-test matrix for mstr-ledger-check.sh.
#
# Run before declaring Phase-3 activation complete, and after any hook change.
# Creates temporary fixture records (LD-999xx), exercises the hook across the
# 10-case matrix via its test seam (MSTR_LEDGER_STAGED_FILES), and cleans up.
# READ-ONLY w.r.t. git -- never commits; fixtures are created + deleted on disk.
#
# Rule 16: Git Bash 3.6.7 default utilities only.

set -uo pipefail
REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
HOOK="$REPO_ROOT/.tools/git-hooks/mstr-ledger-check.sh"
LEDGER="$REPO_ROOT/org/tier0/ledger"
MSTR="0.0.0_AB_MSTR <0.0.0_AB_MSTR@opal.agent>"
CTO="1.0.0_SA_CTO <x>"
COO="2.0.0_SA_COO <x>"
CVO="3.0.0_SA_CVO <x>"
PASS=0; FAIL=0

cleanup() { rm -f "$LEDGER"/LD-9900*.md 2>/dev/null || true; }
trap cleanup EXIT

# --- fixture: write a ledger entry with given class/status/refs/ratified_by ---
mkld() {  # mkld <path> <stakes_class> <status> <directive_refs> <ratified_by> [omit_field]
  local omit="${6:-}"
  {
    echo "---"
    [ "$omit" != decision_id ]  && echo "decision_id: $(basename "$1" .md)"
    echo "timestamp: 2026-05-22T00:00:00Z"
    echo "agent: 0.0.0_AB_MSTR"
    echo "created_by: 0.0.0_AB_MSTR"
    echo "last_modified_by: 0.0.0_AB_MSTR"
    echo "cycle_id: CY-0001"
    echo "directive_refs: $4"
    echo "mandate_distance: 0"
    echo "authority_source: directive"
    [ "$omit" != decision_type ] && echo "decision_type: directive_execution"
    echo "stakes_class: $2"
    echo "s4_type: null"
    echo "rollback_plan: present"
    echo "requires_andrew_ratification: false"
    echo "ratified_by: $5"
    echo "status: $3"
    echo "---"
    echo "# fixture"
  } > "$1"
}

# --- run one case: expect <exit> from the hook under the given env ---
chk() {  # chk "<desc>" <expected_exit> <author> <staged> [override]
  local desc="$1" exp="$2" author="$3" staged="$4" ovr="${5:-}"
  local rc
  GIT_AUTHOR_NAME="$author" MSTR_LEDGER_OVERRIDE="$ovr" \
    MSTR_LEDGER_STAGED_FILES="$staged" bash "$HOOK" >/dev/null 2>&1
  rc=$?
  if [ "$rc" -eq "$exp" ]; then
    echo "  PASS  $desc  (exit $rc)"; PASS=$((PASS+1))
  else
    echo "  FAIL  $desc  (exit $rc, expected $exp)"; FAIL=$((FAIL+1))
  fi
}

echo "mstr-ledger-check.sh -- smoke-test matrix"
echo

cleanup
mkld "$LEDGER/LD-99001.md" S1 active "[D-001]" null            # valid S1
mkld "$LEDGER/LD-99002.md" S3 proposed "[D-001]" null          # S3 unratified
mkld "$LEDGER/LD-99003.md" S3 ratified "[D-001]" cvo           # S3 ratified
mkld "$LEDGER/LD-99004.md" S1 active "[D-001]" null decision_type   # malformed (missing field)

chk "1.  Andrew (human) commits a law doc"            0 ""     "org/tier0/CONSTITUTION.md"
chk "2.  MSTR record-only commit (valid LD)"          0 "$MSTR" "org/tier0/ledger/LD-99001.md"
chk "3.  MSTR strategic S1 commit WITH ledger entry"  0 "$MSTR" "org/tier0/ledger/LD-99001.md
docs/architecture/FOO.md"
chk "4.  MSTR strategic commit WITHOUT ledger entry"  1 "$MSTR" "docs/architecture/FOO.md"
chk "5.  MSTR S3 strategic commit, NOT ratified"      1 "$MSTR" "org/tier0/ledger/LD-99002.md
docs/architecture/FOO.md"
chk "6.  MSTR S3 strategic commit, ratified"          0 "$MSTR" "org/tier0/ledger/LD-99003.md
docs/architecture/FOO.md"
chk "7.  CTO normal commit"                           0 "$CTO"  "data/foo.py"
chk "8.  COO REGISTRY commit"                         0 "$COO"  "org/projects/REGISTRY.md"
chk "9.  non-MSTR commit touching a malformed record" 1 "$CVO"  "org/tier0/ledger/LD-99004.md"
chk "10a. non-MSTR override -> bypass + logged"       0 "$CTO"  "docs/architecture/FOO.md" "emergency fix"
chk "10b. MSTR self-override -> refused, falls to block" 1 "$MSTR" "docs/architecture/FOO.md" "trying to skip"

echo
echo "RESULT: $PASS passed, $FAIL failed."
[ "$FAIL" -eq 0 ] && echo "ALL PASS -- hook behaves to spec." || echo "FAILURES -- do not activate."
exit "$FAIL"
