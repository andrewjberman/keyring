#!/usr/bin/env bash
# NFRA_CMTQUE TO-5 -- commit_gate_lib.sh
# SHARED sensitive-leak gate: the SINGLE SOURCE of the leak-pattern lists + the
# hit-detector, sourced by BOTH the commit-worker (commit-worker.sh) AND
# safe-commit.sh's D6 fallback path (when TO-2 rewrites it). Extracted so a future
# pattern update to the _LEAK_*_RE lists can NEVER drift between the two consumers.
# (CTO arch-gate 2026-07-06: "copy-drift on a SECURITY gate is the failure mode.")
# Logic ported VERBATIM from the proven safe-commit.sh:236-261 fail-closed gate.
#
# RULE 16 (Git Bash 3.6.7): default utilities only -- grep, printf, git check-ignore.
#
# USAGE: source this file, then call cg_sensitive_hits. Run directly for a self-test:
#   bash .tools/commit_gate_lib.sh selftest

# --------------------------------------------------------------------------
# The three pattern classes -- SINGLE SOURCE OF TRUTH. Do not redefine elsewhere;
# both the worker and safe-commit's fallback reference THESE.
# --------------------------------------------------------------------------
# (a) Unambiguous secret file TYPES -- always block, regardless of gitignore.
CG_LEAK_ALWAYS_RE='\.(har|pem|p12|pfx|jks|keystore|ppk)$|(^|/)id_(rsa|dsa|ecdsa|ed25519)([./]|$)|(^|/)\.(netrc|pgpass)$'
# (b) Contextual patterns -- block ONLY when the file is also gitignored (keeps
#     false-positives near zero: a TRACKED cookie_utils.py is not ignored -> never fires).
CG_LEAK_IF_IGNORED_RE='\.(env|key|crt|cer)$|(cookie|secret|credential|password|apikey|api_key|private_key|access_token|auth_token)|(^|/)(\.aws|\.ssh|\.gnupg|sources)/'
# (c) Explicit exemptions (safe sample/template files).
CG_LEAK_EXCLUDE_RE='\.env\.(template|example|sample|dist)$'

# cg_sensitive_hits <in_scope_newline_list>
# Pure detector (no side effects). Echoes the offending files (one per line). A
# file is a hit if it (a) matches an unambiguous secret type, or (b) matches a
# contextual pattern AND is gitignored (git check-ignore --no-index). EXCLUDE
# patterns are exempt. The CALLER decides what to do with the hits (unstage,
# audit, reject) so the security-critical DETECTION lives in exactly one place.
cg_sensitive_hits() {
  local in_scope="$1" f
  [ -n "$in_scope" ] || return 0
  while IFS= read -r f; do
    [ -z "$f" ] && continue
    printf '%s\n' "$f" | grep -qiE "$CG_LEAK_EXCLUDE_RE" && continue
    if printf '%s\n' "$f" | grep -qiE "$CG_LEAK_ALWAYS_RE"; then
      printf '%s\n' "$f"
    elif [ "$f" = ".tools/comp-secrets" ]; then
      # Exact-path allowlist (CTO-gated 2026-07-10): comp-secrets is a Secrets Manager
      # LENS tool -- its NAME matches the (b) 'secret' filename-trigger but it carries NO
      # secret VALUES. The .tools/ dir is broadly gitignored (.gitignore:183), so the (b)
      # branch false-positives on it every edit. This skips the (b) filename-trigger for
      # this EXACT path ONLY; the (a) unambiguous-secret-TYPE detection above still applies
      # to it (defense-in-depth). NOT a glob/substring -- a 2nd lens tool tripping this is
      # the signal to make the trigger content-based, not to grow this allowlist.
      :
    elif printf '%s\n' "$f" | grep -qiE "$CG_LEAK_IF_IGNORED_RE" \
         && git check-ignore --no-index -q -- "$f" 2>/dev/null; then
      printf '%s\n' "$f"
    fi
  done <<< "$in_scope"
}

# --------------------------------------------------------------------------
# MEASURED-STATE STAGING (safe-commit-pure-deletion-staging TO, CTO fix shape
# 081918Z + COO AMENDMENT-1 pycache exclusion). Shared by BOTH staging sites
# (safe-commit.sh retry loop + commit-worker.sh step D) so the branch can never
# copy-drift. Callers keep their own error semantics (retry vs swallow).
# --------------------------------------------------------------------------
# The measured git-2.55 failure matrix this branch encodes (sandbox, 2026-07-14):
#   unstaged deletion (rm; tracked in HEAD+index, absent worktree)
#       -> `git add -f` ALREADY works (rc=0, stages the removal). Kept on -A for
#          uniformity of the deletion branch; behavior identical.
#   staged deletion (git rm / git mv old-side; in HEAD, absent worktree+index)
#       -> BOTH `add -f` and `add -A` fatal rc=128 "pathspec did not match" --
#          the pathspec matches nothing in worktree/index. The index is ALREADY
#          correct; the fix is a recognized NO-OP, not a different add.
#   untracked + missing (in neither HEAD nor worktree)
#       -> rc=128 stays a LOUD FAILURE (caller typo, not a deletion).
# Predicates are CWD-safe (ls-tree/ls-files pathspecs resolve from subdirs --
# commit-worker cd's to the requester's cwd).
CG_PYCACHE_RE='(^|/)__pycache__(/|$)|\.pyc$'

# cg_stage_pathspec <path>...
# ONE measured branch per path (no mode flag, no caller-visible convention change):
#   pycache artifact (__pycache__/ dir or *.pyc)      -> excluded, `SKIP: pycache-artifact` per path
#   tracked-in-HEAD + absent-worktree + in-index      -> `git add -A` (stages the deletion)
#   tracked-in-HEAD + absent-worktree + absent-index  -> no-op (deletion already staged; re-adding fatals)
#   everything else                                   -> `git add -f` (existing behavior; untracked+missing still fails loud)
# Two batched git calls max; if the -f batch fails after deletions were staged,
# the staged deletions are rolled back so a failed call stages NOTHING (matches
# the old single-call atomicity). Post-add, any pycache artifact a DIRECTORY
# pathspec swept in is unstaged, one `SKIP: pycache-artifact` line each (the
# AMENDMENT-1 defect: the gate's own py_compile creates them mid-commit).
cg_stage_pathspec() {
  local p del=() rest=()
  for p in "$@"; do
    if printf '%s\n' "$p" | grep -qE "$CG_PYCACHE_RE"; then
      echo "SKIP: pycache-artifact (never committed): $p" >&2
      continue
    fi
    if [ ! -e "$p" ] && git ls-tree --name-only HEAD -- "$p" 2>/dev/null | grep -q .; then
      if git ls-files --error-unmatch -- "$p" >/dev/null 2>&1; then
        del+=("$p")
      else
        echo "OK: pure deletion already staged (index correct, nothing to re-add): $p" >&2
      fi
    else
      rest+=("$p")
    fi
  done
  local rc=0
  if [ "${#del[@]}" -gt 0 ]; then
    git add -A -- "${del[@]}" || rc=$?
  fi
  if [ "$rc" -eq 0 ] && [ "${#rest[@]}" -gt 0 ]; then
    if ! git add -f -- "${rest[@]}"; then
      rc=$?
      # atomicity rollback: do not leave the deletion half staged for the NEXT
      # invocation to (mis-)inherit -- mirrors the sensitive/contamination resets.
      if [ "${#del[@]}" -gt 0 ]; then
        git reset -q HEAD -- "${del[@]}" 2>/dev/null || true
      fi
    fi
  fi
  [ "$rc" -ne 0 ] && return "$rc"
  # AMENDMENT-1: unstage pycache artifacts a directory pathspec swept in --
  # measured from the index (what was ACTUALLY staged), never pattern-guessed.
  local swept
  swept="$(git diff --cached --name-only -- "$@" 2>/dev/null | grep -E "$CG_PYCACHE_RE" || true)"
  if [ -n "$swept" ]; then
    while IFS= read -r p; do
      [ -z "$p" ] && continue
      git reset -q HEAD -- "$p" 2>/dev/null || true
      echo "SKIP: pycache-artifact (never committed): $p" >&2
    done <<< "$swept"
  fi
  return 0
}

# cg_commit_exclude_pathspec -- the pathspec-magic excludes appended to the
# `git commit --only -- ...` invocation by BOTH commit sites. Belt to the
# staging filter above: `commit --only` re-takes the WORKTREE state of the
# pathspec at commit time, so a .pyc created by the gate's own py_compile
# AFTER staging (the c36710809 / fbdb335b4 mechanism) would still be swept
# without this. Emitted one per line for array-safe consumption.
cg_commit_exclude_pathspec() {
  printf '%s\n' ':(exclude,glob)**/__pycache__/**' ':(exclude,glob)**/*.pyc'
}

# --------------------------------------------------------------------------
# LOG-COMMIT SOURCE-SWEEP GUARD (safe-commit-pure-deletion-staging AMENDMENT-2,
# CTO ratified 190021Z). THE DEFECT: commit 64b6b9d65 (subject
# "log(COMP_LEARNS.session13)...") DELETED all 15 exec-summary-generator source
# files and SAT UNNOTICED 11 WEEKS (ES-1, Rule-10-class). The surviving sibling
# of AMENDMENT-1's pycache class: a source-tree sweep riding an unrelated
# session-log commit. This guard makes a log(-class commit that DELETES paths
# OUTSIDE the session-log/org-record surface refuse loud, per-path.
# Shared by BOTH commit sites (safe-commit.sh + commit-worker.sh) -- no drift.
# --------------------------------------------------------------------------
# The log-commit subject class. Session-log commits are `log(scope): ...` or
# `log: ...` (the /log skill convention). Conservative: a false MATCH only makes
# a non-log commit's out-of-surface deletion loud (recoverable via override); a
# false MISS re-enables the ES-1 class (silent). So err toward matching.
CG_LOG_SUBJECT_RE='^[[:space:]]*log[(:]'

# cg_path_is_log_surface <path> -- true if a deletion of this path is a
# legitimate session-close/record operation (session logs OR org-record tree).
# Per the AMENDMENT-2 ruling's "session-log/org-record surface". Deliberately
# does NOT include source/infra/tooling -- deleting those in a log commit is the
# ES-1 defect. (org/ breadth is the ruling's "org-record surface"; tightenable.)
cg_path_is_log_surface() {
  case "$1" in
    logs/*|*/logs/*) return 0 ;;   # session logs (any depth)
    org/*) return 0 ;;             # org records: ledgers, TOs, projects, memory, compiler-tools-log
    *) return 1 ;;
  esac
}

# cg_extract_subject <COMMIT_ARGS...> -- echo the commit subject (first line)
# from a -m argument or the first line of a -F file. Empty if neither present.
# Parse-free: reads the -F FILE, never evaluates it (the -F safety property).
cg_extract_subject() {
  local prev="" a
  for a in "$@"; do
    if [ "$prev" = "-m" ]; then printf '%s' "${a%%$'\n'*}"; return 0; fi
    if [ "$prev" = "-F" ]; then [ -f "$a" ] && head -n 1 "$a" 2>/dev/null; return 0; fi
    prev="$a"
  done
}

# cg_log_sweep_offenders <subject> <staged_deletions_newline_list>
# Pure detector (no side effects). Echoes the OFFENDING deletions (one per line)
# -- deleted paths OUTSIDE the log/org-record surface -- ONLY when <subject> is a
# log-commit-class subject. Empty otherwise (non-log commit, or all deletions
# are log-surface). The CALLER decides refuse/scream/override (mirrors
# cg_sensitive_hits: detection lives in exactly one place).
cg_log_sweep_offenders() {
  local subject="$1" dels="$2" f
  printf '%s' "$subject" | grep -qE "$CG_LOG_SUBJECT_RE" || return 0
  [ -n "$dels" ] || return 0
  while IFS= read -r f; do
    [ -z "$f" ] && continue
    cg_path_is_log_surface "$f" || printf '%s\n' "$f"
  done <<< "$dels"
}

# cg_selftest -- verify the detector fires on unambiguous secrets, spares
# exemptions, and spares ordinary files. (The gitignored-contextual case is
# exercised end-to-end in commit-worker.sh --selftest, which has a real repo.)
cg_selftest() {
  local hits
  hits="$(cg_sensitive_hits "workflows/session.har")"
  [ "$hits" = "workflows/session.har" ] || { echo "FAIL: .har (ALWAYS) not caught: [$hits]"; return 1; }
  hits="$(cg_sensitive_hits "$(printf 'a/id_rsa\nb/keep.txt')")"
  [ "$hits" = "a/id_rsa" ] || { echo "FAIL: id_rsa not caught / keep.txt flagged: [$hits]"; return 1; }
  hits="$(cg_sensitive_hits ".env.template")"
  [ -z "$hits" ] || { echo "FAIL: .env.template should be EXEMPT: [$hits]"; return 1; }
  hits="$(cg_sensitive_hits ".tools/commit-worker.sh")"
  [ -z "$hits" ] || { echo "FAIL: ordinary .sh flagged: [$hits]"; return 1; }
  # Exact-path allowlist: the comp-secrets LENS tool (name-trigger, no values) is spared.
  # Repo-independent (the branch is checked before the gitignored-(b) grep). An unambiguous
  # secret TYPE at that path would still be caught by the (a) ALWAYS branch above.
  hits="$(cg_sensitive_hits ".tools/comp-secrets")"
  [ -z "$hits" ] || { echo "FAIL: .tools/comp-secrets should be exact-path allowlisted: [$hits]"; return 1; }
  hits="$(cg_sensitive_hits ".tools/comp-secrets.pem")"
  [ "$hits" = ".tools/comp-secrets.pem" ] || { echo "FAIL: allowlist must be EXACT-PATH -- a .pem at a comp-secrets-like path must still be caught (a): [$hits]"; return 1; }
  # AMENDMENT-2 log-commit source-sweep detector (unit).
  local off
  off="$(cg_log_sweep_offenders 'log(COMP_LEARNS.session13): x' "$(printf 'infra/aws/lambda/exec-summary-generator/lambda_function.py\norg/tier2_senior/x/logs/2026/s.md')")"
  [ "$off" = "infra/aws/lambda/exec-summary-generator/lambda_function.py" ] || { echo "FAIL: ES-1 shape -- source deletion in a log( commit not flagged / log deletion flagged: [$off]"; return 1; }
  off="$(cg_log_sweep_offenders 'log: session wind-down' "$(printf 'org/critical_paths/change_management/old.json\norg/tier2_senior/x/logs/2026/s.md')")"
  [ -z "$off" ] || { echo "FAIL: a log commit deleting only org/+logs paths must have ZERO offenders: [$off]"; return 1; }
  off="$(cg_log_sweep_offenders 'feat(x): refactor' "$(printf 'infra/aws/lambda/exec-summary-generator/lambda_function.py')")"
  [ -z "$off" ] || { echo "FAIL: a NON-log commit must never flag (guard is log-subject-scoped): [$off]"; return 1; }
  off="$(cg_extract_subject --author 'a <b>' -m 'log(x): hi
body')"
  [ "$off" = "log(x): hi" ] || { echo "FAIL: cg_extract_subject -m first-line: [$off]"; return 1; }
  echo "PASS: commit_gate_lib selftest (sensitive gate + log-sweep detector + subject extract)"
  return 0
}

if [ "${1:-}" = "selftest" ]; then cg_selftest; exit $?; fi
