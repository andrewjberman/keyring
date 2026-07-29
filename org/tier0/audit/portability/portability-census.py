#!/usr/bin/env python3
"""Site-Z portability census.

Two detectors, because the class I named needs both and a path-flavor audit finds
only three of the four known instances:

  A. PATH LITERAL  -- a user-rooted absolute path baked into a file.
  B. WRITE-TIME STAND-IN -- a textual property used as a proxy for a run-time fact.
     .tools/aws's `*.exe` test contained NO path literal, so detector A is blind to it.

Prints DENOMINATORS for every stage (Rule 22: put the control on the retrieval).
Read-only. Emits JSON to stdout.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(subprocess.run(["git", "rev-parse", "--show-toplevel"],
                           capture_output=True, text=True).stdout.strip())

USER_ROOT = re.compile(r'(?:[A-Za-z]:[\\/]+|/)?Users[\\/]+([A-Za-z][A-Za-z0-9 _.-]{1,40})[\\/]', re.I)

# B: write-time stand-ins for run-time facts.
STANDIN = [
    (r'\*\.exe\)|\.exe"?\s*\)\s*;;|%\.exe|\$\{[A-Za-z_]+%\.exe\}',
     'suffix-test standing in for "is this a native binary"'),
    (r'==\s*["\']?/c/|==\s*["\']?/cygdrive/|-d\s+/cygdrive|test\s+-d\s+/c\b',
     'hardcoded MSYS path FLAVOR rather than resolving it'),
    (r'\bwhich\s+-a\b.*\|\s*head\s+-1|\bwhich\s+\w+\s*\)\s*$',
     'first-PATH-hit assumed correct without checking what it is'),
]

# Files that are RECORDS of incidents, not operative code -- a path literal in a
# ledger entry describing a bug is evidence, not a defect.
RECORD_DIRS = ('docs/', 'org/tier0/ledger/', 'org/tier0/reviews/', 'org/missions/',
               'org/mcp/agentbus-trunk/', 'memory/')
EXEC_SUFFIX = ('.sh', '.ps1', '.py', '.cmd', '.bat')
CONFIG_SUFFIX = ('.json', '.yaml', '.yml', '.toml', '.cfg', '.ini')


def tracked_files() -> list[str]:
    out = subprocess.run(["git", "ls-files"], capture_output=True, text=True, cwd=ROOT).stdout
    return [line for line in out.splitlines() if line.strip()]


def classify(rel: str, text: str = "") -> str:
    """Classify by what the file IS, not only what it is NAMED.

    BUG CAUGHT BY MY OWN POSITIVE CONTROL, 2026-07-29: this keyed on extension
    alone. Every .tools/ shim is EXTENSIONLESS (`aws`, `operator`, all ~93
    `comp-*`), so they classified as "other" and the stand-in detector never ran
    on them -- the exact surface where the defect class lives. The census
    reported "0 stand-ins", and that zero was manufactured by this function.

    That is the same failure I am auditing FOR: an extension is a WRITE-TIME
    textual property standing in for "is this an executable", which is a
    RUN-TIME fact. I wrote the bug into the detector built to find the bug.
    Fix: read the shebang -- the file's own declaration of what it is.
    """
    if rel.startswith(RECORD_DIRS):
        return "record"
    if rel.endswith(EXEC_SUFFIX) or text.startswith("#!"):
        return "operative-executable"
    if rel.endswith(CONFIG_SUFFIX):
        return "operative-config"
    return "other"


def main() -> int:
    files = tracked_files()
    stats = {"tracked_total": len(files), "read_ok": 0, "unreadable": 0}
    path_hits, standin_hits = [], []

    for rel in files:
        p = ROOT / rel
        try:
            text = p.read_text(encoding="utf-8", errors="strict")
        except (OSError, UnicodeDecodeError):
            stats["unreadable"] += 1
            continue
        stats["read_ok"] += 1
        kind = classify(rel, text)

        users = {m.group(1) for m in USER_ROOT.finditer(text)}
        # a generic placeholder is not a device hardcode
        users = {u for u in users if u.lower() not in
                 ("user", "username", "youruser", "opalbl~1", "runner", "root")}
        if users:
            n = sum(1 for _ in USER_ROOT.finditer(text))
            path_hits.append({"file": rel, "kind": kind,
                              "users": sorted(users), "occurrences": n})

        if kind in ("operative-executable", "operative-config"):
            has_runtime_check = ("MZ" in text and "head -c 2" in text)
            for pat, why in STANDIN:
                if re.search(pat, text) and not (has_runtime_check and ".exe" in pat):
                    standin_hits.append({"file": rel, "kind": kind, "signal": why})
                    break

    by_kind: dict[str, int] = {}
    for h in path_hits:
        by_kind[h["kind"]] = by_kind.get(h["kind"], 0) + 1

    operative = [h for h in path_hits if h["kind"].startswith("operative")]
    operative.sort(key=lambda h: -h["occurrences"])

    result = {
        "denominators": stats,
        "path_literal_files": len(path_hits),
        "path_literal_by_kind": by_kind,
        "operative_path_literal_files": len(operative),
        "standin_files": len(standin_hits),
        "top_operative": operative[:25],
        "standins": standin_hits,
    }
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
