#!/usr/bin/env python3
"""loop-resolve.py -- Resolve /loop input to active project codes.

Accepts any combination of:
  - macro_project code: ADVI_ROLLUP (4 + _ + 6 chars)
  - macro code:         ADVI        (4 chars) -> expand to every active ADVI_*
  - project suffix:     ROLLUP      (6 chars) -> resolve to exactly one active project

Tokens may be space- or comma-separated. Duplicates are deduped (first occurrence wins).
Only active projects (org/projects/{CODE}.json with status="active") are considered.

Exit codes:
  0  all tokens resolved to >=1 active project (codes printed on stdout)
  1  empty-match -- token had valid shape but no active project matched
  2  fork -- unparseable token OR ambiguous 6-char suffix (multiple active matches)

Output: one project code per line on stdout in the order tokens appeared.
Errors: one line per problem token on stderr.
"""

from __future__ import annotations

import argparse
import io
import json
import re
import sys
from pathlib import Path

if isinstance(sys.stdout, io.TextIOBase):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, OSError):
        pass

REPO_ROOT = Path(__file__).resolve().parents[1]
PROJECTS_DIR = REPO_ROOT / "org" / "projects"

MACRO_PROJECT_RE = re.compile(r"^[A-Z]{4}_[A-Z0-9]{6}$")
MACRO_RE = re.compile(r"^[A-Z]{4}$")
SUFFIX_RE = re.compile(r"^[A-Z0-9]{6}$")


def load_active_projects():
    out = []
    for jf in sorted(PROJECTS_DIR.glob("*.json")):
        try:
            data = json.loads(jf.read_text(encoding="utf-8"))
        except Exception:
            continue
        if data.get("status") != "active":
            continue
        code = data.get("project_code", "")
        if not MACRO_PROJECT_RE.match(code):
            continue
        out.append({"code": code, "macro": code[:4], "suffix": code[5:]})
    return out


def resolve_token(token, active):
    t = token.strip().upper()
    if MACRO_PROJECT_RE.match(t):
        if any(p["code"] == t for p in active):
            return True, [t]
        return False, {"kind": "NO_ACTIVE_MATCH", "token": token,
                       "reason": f"'{t}' is not an active project"}
    if MACRO_RE.match(t):
        matches = [p["code"] for p in active if p["macro"] == t]
        if matches:
            return True, matches
        return False, {"kind": "MACRO_EMPTY", "token": token,
                       "reason": f"macro '{t}' has no active projects"}
    if SUFFIX_RE.match(t):
        matches = [p["code"] for p in active if p["suffix"] == t]
        if len(matches) == 1:
            return True, matches
        if len(matches) == 0:
            return False, {"kind": "NO_ACTIVE_MATCH", "token": token,
                           "reason": f"suffix '{t}' matches no active project"}
        return False, {"kind": "AMBIGUOUS", "token": token,
                       "reason": f"suffix '{t}' matches {len(matches)} active: "
                                 f"{', '.join(matches)} -- use full macro_project code"}
    return False, {"kind": "UNPARSEABLE", "token": token,
                   "reason": f"'{token}' is not a valid macro (4ch), "
                             f"project suffix (6ch), or macro_project (ADVI_ROLLUP)"}


def main():
    ap = argparse.ArgumentParser(
        description="Resolve /loop input to active project codes (one per line on stdout).")
    ap.add_argument("tokens", nargs="+",
                    help="Macro codes, project suffixes, or macro_project codes; space/comma separated.")
    ap.add_argument("--json", action="store_true", help="Emit JSON array instead of newline list.")
    args = ap.parse_args()

    flat = []
    for t in args.tokens:
        for p in t.replace(",", " ").split():
            if p:
                flat.append(p)

    active = load_active_projects()

    resolved = []
    seen = set()
    errors = []
    exit_code = 0

    for token in flat:
        ok, result = resolve_token(token, active)
        if not ok:
            errors.append(result)
            if result["kind"] in ("UNPARSEABLE", "AMBIGUOUS"):
                exit_code = max(exit_code, 2)
            else:
                exit_code = max(exit_code, 1)
            continue
        for code in result:
            if code not in seen:
                seen.add(code)
                resolved.append(code)

    for e in errors:
        print(f"[LOOP-RESOLVE] {e['kind']}: {e['reason']}", file=sys.stderr)

    if exit_code != 0:
        sys.exit(exit_code)

    if not resolved:
        print("[LOOP-RESOLVE] no active projects resolved from input", file=sys.stderr)
        sys.exit(1)

    if args.json:
        print(json.dumps(resolved))
    else:
        for code in resolved:
            print(code)
    sys.exit(0)


if __name__ == "__main__":
    main()
