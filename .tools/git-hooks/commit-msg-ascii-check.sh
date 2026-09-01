#!/usr/bin/env bash
# =============================================================================
# commit-msg-ascii-check.sh -- REFUSE a commit message containing non-ASCII.
#
# AUTHORITY: Andrew-direct 2026-09-01, VERBATIM: "i never want emojis, made it
# very specific in many docs not to use them" -> then, asked whether to enforce
# mechanically: "yes enforce it at commit time". Implemented by 0.0.0_AB_MSTR~Z.
#
# WHY IT EXISTS -- a MEASURED cost, not a style preference:
#   CLAUDE.md already says "No non-ASCII in production code/logs/AWS -- use
#   OK:/WARN:/ERROR:/SKIP:/BLOCKED:". It was stated, loaded by every seat at
#   startup, and enforced by nobody. MEASURED on origin/SITEZ 2026-09-01:
#   83 of 426 commits in 24h (19%) carried non-ASCII, 197 characters, 12
#   distinct authors. Top offenders U+26D4 x85, U+2B50 x43, U+26A0 x25.
#   On 2026-09-01 ~07:1xZ a single U+2B50 in a commit message CRASHED
#   safe_deploy_core.py: it read `git log` with subprocess text=True and no
#   explicit encoding, Windows decoded as cp1252, cp1252 cannot map 0x90 (the
#   third byte of E2 AD 90), stdout came back None and the regex died on it.
#   THE DEPLOY GATE DID NOT FAIL OPEN OR CLOSED -- IT CRASHED, and it blocked
#   every deploy-scope push on the device until repaired (24da55157d). The
#   laptop fabric hit the identical failure on its own copy.
#
# SCOPE -- DELIBERATELY NARROW. This gate reads the COMMIT MESSAGE ONLY.
#   It does NOT inspect file contents. Widening it to code/doc content is a
#   SEPARATE decision with real false-positive risk (existing docs, data files,
#   vendor fixtures) and Andrew authorized "at commit time" in a conversation
#   measuring commit MESSAGES. A gate that blocks legitimate content is a gate
#   that gets bypassed wholesale.
#
# COST: one grep over the message file per commit. NON-APPLICATION: merges are
#   NOT exempt -- `git commit -F` on a merge reaches commit-msg like any other
#   commit, and merge messages were part of the measured 19%.
#
# BYPASS (audited, edge cases only -- a genuine need for a non-ASCII literal):
#   ASCII_OVERRIDE="<reason>" git commit ...
#   Appends to org/commit-msg-ascii-override-audit.log. A bare/empty value is
#   NOT accepted -- the reason is the point of the audit row.
#
# Rule 16: Git Bash 3.6.7 default utilities only. This file is ASCII-only, and
# it checks itself in --self-test.
# =============================================================================
set -e

MSG_FILE="$1"
ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"

# --- self-test ---------------------------------------------------------------
if [ "$1" = "--self-test" ]; then
  TMP="$(mktemp)"; FAIL=0
  # ARM 1: a clean ASCII message must PASS.
  printf 'fix(thing): a clean ascii subject\n\nBody with OK: and WARN: markers.\n' > "$TMP"
  if bash "$0" "$TMP" >/dev/null 2>&1; then echo "  ARM1 PASS -- clean message accepted"
  else echo "  ARM1 FAIL -- clean message was REFUSED"; FAIL=1; fi
  # ARM 2: a message carrying the exact character that crashed the deploy gate
  #        must be REFUSED. Built with printf \x so this file stays ASCII.
  printf 'fix(thing): subject with a star \xe2\xad\x90 in it\n' > "$TMP"
  if bash "$0" "$TMP" >/dev/null 2>&1; then echo "  ARM2 FAIL -- U+2B50 was ACCEPTED"; FAIL=1
  else echo "  ARM2 PASS -- U+2B50 refused"; fi
  # ARM 3: the override must let ARM 2 through, and must be audited.
  if ASCII_OVERRIDE="self-test" bash "$0" "$TMP" >/dev/null 2>&1; then
    echo "  ARM3 PASS -- audited override accepted"
  else echo "  ARM3 FAIL -- override did not work"; FAIL=1; fi
  # ARM 4: an EMPTY override must NOT bypass -- the reason is the point.
  if ASCII_OVERRIDE="" bash "$0" "$TMP" >/dev/null 2>&1; then
    echo "  ARM4 FAIL -- empty override bypassed the gate"; FAIL=1
  else echo "  ARM4 PASS -- empty override refused"; fi
  # ARM 5: this script must itself be ASCII -- a gate that violates its own rule.
  if LC_ALL=C grep -qP '[^\x00-\x7F]' "$0" 2>/dev/null; then
    echo "  ARM5 FAIL -- this gate file contains non-ASCII"; FAIL=1
  else echo "  ARM5 PASS -- the gate file is itself ASCII"; fi
  rm -f "$TMP"
  [ "$FAIL" -eq 0 ] && echo "  SELF-TEST: 5/5 PASS" || echo "  SELF-TEST: FAILURES ABOVE"
  exit "$FAIL"
fi

[ -n "$MSG_FILE" ] && [ -f "$MSG_FILE" ] || exit 0

# Strip comment lines git adds to the template -- they are not the author's text.
BODY="$(grep -v '^#' "$MSG_FILE" 2>/dev/null || true)"

# LC_ALL=C so the byte class is byte-exact regardless of the caller's locale.
if ! printf '%s' "$BODY" | LC_ALL=C grep -qP '[^\x00-\x7F]' 2>/dev/null; then
  exit 0
fi

if [ -n "${ASCII_OVERRIDE:-}" ]; then
  printf '%s | %s | ASCII_OVERRIDE: %s\n' \
    "$(date -u +%Y-%m-%dT%H%M%SZ)" \
    "$(git var GIT_AUTHOR_IDENT 2>/dev/null | sed 's/ <.*//')" \
    "$ASCII_OVERRIDE" >> "$ROOT/org/commit-msg-ascii-override-audit.log" 2>/dev/null || true
  echo "WARN: ASCII_OVERRIDE -- commit message carries non-ASCII (audited: $ASCII_OVERRIDE)" >&2
  exit 0
fi

echo "BLOCKED: the commit message contains non-ASCII characters." >&2
echo "" >&2
echo "  Andrew-direct 2026-09-01: 'i never want emojis, made it very specific in" >&2
echo "  many docs not to use them' -> 'yes enforce it at commit time'." >&2
echo "  CLAUDE.md: No non-ASCII in production code/logs/AWS." >&2
echo "" >&2
echo "  OFFENDING LINES:" >&2
printf '%s' "$BODY" | LC_ALL=C grep -nP '[^\x00-\x7F]' 2>/dev/null \
  | LC_ALL=C sed 's/[^\x00-\x7F]/<NON-ASCII>/g' | head -12 | sed 's/^/    /' >&2
echo "" >&2
echo "  USE INSTEAD: OK:  WARN:  ERROR:  SKIP:  BLOCKED:  NOTE:  >>  <<  --" >&2
echo "  A U+2B50 in a commit message CRASHED the deploy gate on 2026-09-01" >&2
echo "  (cp1252 cannot decode it) and blocked every deploy-scope push until repaired." >&2
echo "" >&2
echo "  Audited bypass, genuine need only:  ASCII_OVERRIDE=\"<reason>\" git commit ..." >&2
exit 1
