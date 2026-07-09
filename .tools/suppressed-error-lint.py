#!/usr/bin/env python3
"""suppressed-error-lint -- find places where a failure is swallowed and a
zero-result is then treated as a fact about the world.

CTO 2026-07-09T195435Z:

    "A zero-result is a claim about the query, not about the world -- and here
     the swallowed error becomes a MISLEADING claim, which is worse than a
     silent one."

THE FIRST CASE, and the reason this lint exists (safe-commit.sh:271):

    git add -f -- "${PATHSPEC[@]}" 2>/dev/null || true

Under index-lock contention the staging silently fails. Line 421's
`git commit --only -- PATHSPEC` then aborts with

    pathspec 'X' did not match any file(s) known to git

which points the agent at their own path instead of at the lock. Hit three times
on 2026-07-09 while MSTR held the shared index. An agent who trusts that message
goes hunting a typo in a path that is perfectly correct. The suppression did not
merely hide an error -- it MANUFACTURED a false one, in the tool every lane calls
on every commit.

RULES -- severity is the whole design
------------------------------------
  S-HIGH  a suppressed MUTATION: `git add|commit|checkout|restore|reset`, `aws`,
          `terraform apply|import|state`, `cp`/`mv`/`ln`, or a redirect-into-file,
          with stderr discarded and/or exit ignored. A later step will ASSUME this
          succeeded. This is where a swallowed error becomes a misleading claim.
  S-LOW   suppressed but idempotent/scratch (`rm -f`, `mkdir -p`, `touch`, `chmod`).
          A failure here misleads nobody; reported, never enforced.
  S-INFO  suppressed, unclassified.
  S2      `except ...: pass` -- a Python swallow with no re-raise, log, or comment.

Only S-HIGH fails `--strict`. A first cut flagged every `2>/dev/null || true` and
produced 165 findings on `.tools/` alone, overwhelmingly `rm -f tmp || true`. **A
lint that cries wolf gets muted -- which is this lint's own failure mode, one level
up.** Tiering cut the actionable set to 22 and kept `safe-commit.sh:271` in it.

Not every suppression is wrong. Mark the deliberate ones inline and this lint
stays quiet:

    some_cmd 2>/dev/null || true   # lint-ok: probing for optional file, absence is the answer

The marker is the point: it forces the author to state WHY a zero-result is a
fact about the world here, rather than about the query. Same convention as
`# rail-checked:` (NFRA_COMPRAIL).

WARN-mode by default (announce-then-enforce). `--strict` exits 1.
Read-only. ASCII only.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

OK_MARKER = re.compile(r"#\s*lint-ok:")

# Suppression = stderr discarded AND/OR exit status ignored.
SUPPRESSED = re.compile(r"2>\s*/dev/null|\|\|\s*true|\|\|\s*:")

# SEVERITY IS THE WHOLE DESIGN.
#
# A first cut flagged every `2>/dev/null || true` and produced 165 findings on
# .tools/ alone -- overwhelmingly `rm -f tmp 2>/dev/null || true`, which is
# harmless and idempotent. A lint that cries wolf gets muted, which is the exact
# failure this lint exists to prevent, one level up.
#
# The harm is not suppression. The harm is a suppressed MUTATION whose success is
# ASSUMED DOWNSTREAM. `rm -f` cannot half-succeed in a way that misleads. A failed
# `git add` absolutely can -- and did: it produced `pathspec did not match`, a
# MISLEADING claim, in the tool every lane calls on every commit.
#
# HIGH: state-changing, non-idempotent, and a later step reads the state.
HIGH_CMDS = re.compile(
    r"\b(git\s+(add|commit|checkout|restore|mv|reset|stash|apply)"
    r"|aws\s+\w+"
    r"|terraform\s+(apply|import|state)"
    r"|\bcp\b|\bln\b|\bmv\b"
    r"|>\s*[\"']?\$?\w)"          # redirect-into-file: a write
)
# LOW: idempotent or purely-destructive-of-scratch; a failure changes nothing a
# later step depends on.
LOW_CMDS = re.compile(r"\b(rm\s+-f|rmdir|mkdir\s+-p|touch|chmod|kill|pkill|true)\b")

# S2: python swallow. `except X: pass` on one line, or `except X:` then a lone `pass`.
S2_INLINE = re.compile(r"^\s*except\b[^:]*:\s*pass\s*$")
S2_OPEN = re.compile(r"^\s*except\b[^:]*:\s*$")

DEFAULT_PATHS = [".tools", "org/mcp"]
SUFFIXES = {".sh", ".py", ".bash"}


def scan_file(p: Path) -> list:
    hits = []
    try:
        lines = p.read_text(encoding="utf-8", errors="replace").splitlines()
    except Exception as e:  # noqa: BLE001 -- surface, never drop (the lint's own rule)
        return [(0, "E0", f"unreadable: {type(e).__name__}: {e}")]

    for i, line in enumerate(lines, 1):
        if OK_MARKER.search(line):
            continue
        stripped = line.strip()
        if stripped.startswith("#") or not stripped:
            continue

        if p.suffix in (".sh", ".bash"):
            if SUPPRESSED.search(line):
                # LOW first: an idempotent command's failure misleads nobody.
                if LOW_CMDS.search(line) and not HIGH_CMDS.search(line):
                    hits.append((i, "S-LOW", "suppressed, but idempotent/scratch -- failure changes nothing downstream"))
                elif HIGH_CMDS.search(line):
                    hits.append((i, "S-HIGH", "suppressed MUTATION -- a later step will assume this succeeded"))
                else:
                    hits.append((i, "S-INFO", "suppressed command (unclassified)"))
        elif p.suffix == ".py":
            if S2_INLINE.match(line):
                hits.append((i, "S2", "except ...: pass -- swallowed with no re-raise, log, or comment"))
            elif S2_OPEN.match(line) and i < len(lines):
                nxt = lines[i].strip() if i < len(lines) else ""
                if nxt == "pass":
                    hits.append((i, "S2", "except ...: / pass -- swallowed with no re-raise, log, or comment"))
    return hits


def main() -> int:
    ap = argparse.ArgumentParser(description="Find swallowed-error sites")
    ap.add_argument("paths", nargs="*", default=None, help=f"paths to scan (default: {DEFAULT_PATHS})")
    ap.add_argument("--strict", action="store_true", help="exit 1 on any finding")
    ap.add_argument("--rule", help="only this rule (S-HIGH/S-LOW/S-INFO/S2)")
    args = ap.parse_args()

    roots = [Path(p) for p in (args.paths or DEFAULT_PATHS)]
    files: list[Path] = []
    for r in roots:
        if r.is_file():
            files.append(r)
        elif r.is_dir():
            files.extend(f for f in r.rglob("*") if f.is_file() and f.suffix in SUFFIXES)

    total = 0
    by_rule: dict = {}
    for f in sorted(files):
        for line_no, rule, msg in scan_file(f):
            if args.rule and rule != args.rule:
                continue
            total += 1
            by_rule.setdefault(rule, []).append((str(f).replace("\\", "/"), line_no, msg))

    print(f"suppressed-error-lint -- scanned {len(files)} file(s) under {[str(r) for r in roots]}")
    print()
    if not total:
        print("OK: no swallowed-error sites.")
        return 0

    for rule in sorted(by_rule):
        rows = by_rule[rule]
        print(f"{rule} ({len(rows)}):")
        for path, line_no, msg in rows:
            print(f"  {path}:{line_no}")
            print(f"      {msg}")
        print()

    print(f"{total} finding(s). Mark deliberate ones with an inline `# lint-ok: <why a zero-result")
    print("is a fact about the world here, not about the query>`.")
    if args.strict and any(r in by_rule for r in ("S-HIGH",)):
        return 1
    print("WARN: advisory mode -- rerun with --strict to enforce.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
