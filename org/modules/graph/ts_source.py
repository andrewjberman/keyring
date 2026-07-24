"""ts_source -- comment-aware JS/TS source handling for the graph extractors.

Bundle item 2 (CTO 20260722T210151Z item (2), DE finding @7a2805d4e): comp-routes +
comp-platinum resolved getAccountDistribution to the COMMENTED-OUT /api/private TODO
at portal aum.ts (:517 region) instead of the live /api/general call at :552 --
confidently, with wrong URL and auth columns, no warning. Mechanism: the endpoint
extractors regex-scan RAW source, and the dead call precedes the live one, so
first-match won. This is the FALSE-PRESENCE class (COO aiming note 220729Z: NOT the
silent-absence/count-vs-throw family -- the control is instrument selection, i.e.
never present dead code to the resolver at all, not resolution-time liveness).

`strip_comments` is a character state machine, not a regex: `//` inside a string
literal ("https://...") is NOT a comment, and a naive line-strip would truncate
every absolute URL in the tree. States: code, ' string, " string, ` template,
// line comment, /* block comment. Escapes honored inside strings. Comments are
replaced with equivalent WHITESPACE (newlines preserved) so downstream character
offsets/line numbers stay meaningful.

Also the seed for bundle item 7's polyglot lane (comp-constants JS/TS parsing):
one shared comment-model rather than a per-tool re-guess.
"""
from __future__ import annotations


def strip_comments(source: str) -> str:
    """Return source with // and /* */ comments blanked to whitespace.

    String and template literals are preserved verbatim (including any // or /*
    inside them). Unterminated constructs blank to end-of-input rather than
    raising -- extractors must degrade, never crash the graph build.
    """
    out = list(source)
    i = 0
    n = len(source)
    CODE, SQ, DQ, TPL, LINE, BLOCK = range(6)
    state = CODE
    while i < n:
        c = source[i]
        nxt = source[i + 1] if i + 1 < n else ""
        if state == CODE:
            if c == "'":
                state = SQ
            elif c == '"':
                state = DQ
            elif c == "`":
                state = TPL
            elif c == "/" and nxt == "/":
                state = LINE
                out[i] = " "
                if i + 1 < n:
                    out[i + 1] = " "
                i += 2
                continue
            elif c == "/" and nxt == "*":
                state = BLOCK
                out[i] = " "
                if i + 1 < n:
                    out[i + 1] = " "
                i += 2
                continue
        elif state in (SQ, DQ):
            quote = "'" if state == SQ else '"'
            if c == "\\":
                i += 2
                continue
            if c == quote or c == "\n":   # unterminated string: newline ends it
                state = CODE
        elif state == TPL:
            if c == "\\":
                i += 2
                continue
            if c == "`":
                state = CODE
        elif state == LINE:
            if c == "\n":
                state = CODE
            else:
                out[i] = " "
        elif state == BLOCK:
            if c == "*" and nxt == "/":
                out[i] = " "
                out[i + 1] = " "
                state = CODE
                i += 2
                continue
            if c != "\n":
                out[i] = " "
        i += 1
    return "".join(out)
