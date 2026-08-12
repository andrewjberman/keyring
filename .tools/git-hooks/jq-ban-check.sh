#!/usr/bin/env bash
# jq-ban-check.sh -- deny `jq` INVOCATIONS in .claude/skills/** and .tools/** shell contexts.
#
# ANDREW GATE GO 2026-08-11 ~1905Z (verbatim "2a yes" against the CTO gate-candidate card set;
# record: ANDREW_DIRECT_20260811_GATE_REGISTER_RULINGS_FOUR_CARDS.md). Why: jq is NOT installed
# in the Git Bash runtime (CLAUDE.md Rule 16), and its prescribed call sites were written
# `jq ... 2>/dev/null`, so the missing binary returns CLEAN EMPTY -- a status/liveness read
# renders a false quiet fabric (COO-measured 2026-08-11, near-filed fabric-wide outage).
# The companion "deny 2>/dev/null on verdict reads" was DECLINED as a gate ("2b no") -- it
# stays Rule-16 prose; do NOT widen this lint to it.
#
# MATCHER DISCIPLINE (LD-0274 -- a mention is not an invocation): this lint matches jq as a
# COMMAND TOKEN in CODE contexts only:
#   - .md files: only lines INSIDE ``` fences are checked (prose mentions never match);
#   - comment lines (first non-space char '#') are excluded everywhere -- the ban is itself
#     documented in comments/prose in the fixed skills, and those must keep passing;
#   - backtick-quoted mentions (`jq`) do not match (the token must be followed by whitespace/EOL).
# Scope: staged Added/Copied/Modified files under .claude/skills/ or .tools/ with extension
# .sh/.bash/.md, plus extensionless files whose staged first line is a bash shebang.
# The check reads STAGED content (git show :path), never the worktree.
# Audited override: JQ_BAN_OVERRIDE="<reason>" -- appends to org/jq-ban-override-audit.log.
# Env from the orchestrator: ROOT, STAGED (precomp_v1 contract).

set -u

root="${ROOT:-$(git rev-parse --show-toplevel 2>/dev/null)}"
staged="${STAGED:-$(git diff --cached --name-only 2>/dev/null || true)}"
[ -z "$staged" ] && exit 0

candidates="$(git diff --cached --name-only --diff-filter=ACM 2>/dev/null \
    | grep -E '^(\.claude/skills/|\.tools/)' || true)"
[ -z "$candidates" ] && exit 0

blocked=0
while IFS= read -r f; do
    [ -z "$f" ] && continue
    mode=""
    case "$f" in
        *.sh|*.bash) mode="code" ;;
        *.md)        mode="md" ;;
        *.*)         continue ;;   # other extensions (py/json/yaml/...) out of scope
        *)  # extensionless: only if the staged content is a bash script
            head1="$(git show ":$f" 2>/dev/null | head -1)"
            case "$head1" in \#!*bash*|\#!*sh*) mode="code" ;; *) continue ;; esac ;;
    esac
    hits="$(git show ":$f" 2>/dev/null | awk -v mode="$mode" -v fn="$f" '
        BEGIN { infence = (mode == "code") ? 1 : 0 }
        mode == "md" && /^[ \t]*```/ { infence = !infence; next }
        !infence { next }
        # A COMMENT IS NOT CODE -- strip from the first hash before ANY matching, the same way
        # never-rules-gate.sh scan() does. Fired three times on prose during authoring (this
        # files own echo strings, the gates guarded check, then this very comment), which is the
        # mention-is-not-an-invocation class (LD-0274) that the ban itself exists to respect.
        # RESIDUAL, stated: a real jq after a hash on one line (only reachable inside a quoted
        # string) is now invisible. That is an UNDER-match in a heuristic lint, accepted
        # deliberately -- the structural alternative is a shell parser, which is disproportionate.
        # STRIP COMMENTS *AND* QUOTED STRINGS before matching. That is the real discriminator:
        # all three authoring-time false fires had jq inside a STRING (this files own echo text,
        # the gates error message, a trailing comment) -- a mention, never an invocation. A bare
        # `jq -r ".x"` still fires because the jq TOKEN sits outside the quotes.
        { code = $0; sub(/#.*$/, "", code); gsub(/"[^"]*"/, " ", code); gsub(/\047[^\047]*\047/, " ", code)
          s = code; sub(/^[ \t]+/, "", s) }
        s ~ /^[ \t]*$/ { next }
        # --- EXCLUSIONS: the ban targets a BARE, UNGUARDED jq at COMMAND POSITION (the measured
        # harm was `jq ... 2>/dev/null` rendering a false quiet fabric). It must NOT fire on the
        # patterns the estate is REQUIRED to use. ---
        code ~ /command[ \t]+-v[ \t]+jq|type[ \t]+jq|hash[ \t]+jq/ { next }   # Rule-16 GUARDED presence check
        code ~ /jq\.exe|JQ=|\$\{?JQ\}?/                            { next }   # the VENDORED .tools/jq.exe resolution + its resolved var
        code ~ /(^|[ \t|&;(`]|\$\()jq([ \t]|$)/ { printf "    %s:%d: %s\n", fn, NR, $0 }
    ')"
    [ -z "$hits" ] && continue
    if [ -n "${JQ_BAN_OVERRIDE:-}" ]; then
        printf '%s | %s | %s | %s\n' "$(date -u +%Y-%m-%dT%H%M%SZ)" \
            "$(git var GIT_AUTHOR_IDENT 2>/dev/null | sed 's/ <.*//')" "$f" "$JQ_BAN_OVERRIDE" \
            >> "$root/org/jq-ban-override-audit.log"
        echo "WARN: JQ_BAN_OVERRIDE -- 'jq' call in $f permitted (audited: $JQ_BAN_OVERRIDE)" >&2
        continue
    fi
    echo "BLOCKED: 'jq' INVOCATION staged in '$f' -- 'jq' is NOT INSTALLED (CLAUDE.md Rule 16)." >&2
    echo "$hits" >&2
    echo "  Under 2>/dev/null a missing 'jq' returns CLEAN EMPTY -- a liveness read renders a false" >&2
    echo "  quiet fabric (measured 2026-08-11). Parse JSON with python (pattern: /drive Step 2b.1)." >&2
    echo "  Audited override (edge cases only): JQ_BAN_OVERRIDE=\"<reason>\" git commit ..." >&2
    blocked=1
done <<EOF_LIST
$candidates
EOF_LIST

exit $blocked
