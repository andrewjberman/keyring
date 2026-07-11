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
  echo "PASS: commit_gate_lib selftest (ALWAYS caught, EXCLUDE exempt, ordinary spared, comp-secrets allowlisted exact-path)"
  return 0
}

if [ "${1:-}" = "selftest" ]; then cg_selftest; exit $?; fi
