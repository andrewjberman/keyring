#!/usr/bin/env python3
"""
comp-shell -- detect bare references to forbidden Git Bash 3.6.7 utilities
in local-runtime shell scripts before they cause silent guard fall-through.

Forbidden utilities (CLAUDE.md Rule 16):
    pgrep, pkill, flock, pidof, setsid, wget

Detection:
    UNGUARDED (ERROR) -- utility appears as a command with no guard in lookback window
    GUARDED   (WARN)  -- utility appears but 'command -v <util>' / 'which <util>' guard
                         found within GUARD_LOOKBACK_DEFAULT lines above

Output format (one finding per line):
    <file>:<line>:<severity>:<utility>:<guard-status>:<context-excerpt>

Exit codes:
    0 -- no ERROR-level findings (WARNs do not block)
    1 -- at least one ERROR finding
    2 -- usage / config error

Usage:
    comp-shell scan [path ...]      scan files/directories
    comp-shell scan --all           scan workspace (excluding EC2/data paths)
    comp-shell list-forbidden       print forbidden utilities + canonical fallbacks
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
_WORKSPACE = _THIS_DIR.parent.parent.parent

# Utilities forbidden on local-runtime paths (CLAUDE.md Rule 16)
FORBIDDEN = {"pgrep", "pkill", "flock", "pidof", "setsid", "wget"}

# Canonical fallback patterns (from ADHC_BASHFIX.002 / inbox-watch.sh)
FALLBACKS = {
    "pgrep": "command -v pgrep >/dev/null 2>&1 || ps -ef | awk ...",
    "pkill": "command -v pkill >/dev/null 2>&1 || kill $(ps -ef | awk ...)",
    "flock": "command -v flock >/dev/null 2>&1 (no universal fallback -- avoid flock)",
    "pidof": "command -v pidof >/dev/null 2>&1 || ps -ef | awk '{print $2}' | ...",
    "setsid": "command -v setsid >/dev/null 2>&1 (no universal fallback -- avoid setsid)",
    "wget": "curl -fsSL <url> -o <file>  (curl is present in Git Bash 3.6.7+)",
}

# How many lines above a usage to look for a guard
GUARD_LOOKBACK_DEFAULT = 30

# EC2-side + data-scripts paths are exempt (run on Amazon Linux where utils exist).
# Additional non-local-runtime paths are also exempt:
#   worktrees/   -- git worktrees, isolated from local runtime context
#   .tmp/        -- temp artifacts (e.g. deployed_gold_compare snapshots)
#   codex2/      -- third-party CLI tool directory
#   infra/ec2/   -- alternate EC2-side path (not infra/aws/ec2/ prefix)
EXEMPT_PREFIXES = (
    "infra/aws/ec2/",
    "infra/ec2/",
    "data/",
    "worktrees/",
    ".tmp/",
    "codex2/",
)

# In-scope paths per CLAUDE.md Rule 16 (for --all default)
IN_SCOPE_PREFIXES = (
    ".tools/",
    "org/mcp/",
    "org/threads/",
    "infra/aws/lambda/ci/",
    "infra/aws/terraform/",
)

# ---------------------------------------------------------------------------
# Detection helpers
# ---------------------------------------------------------------------------

# Regex: utility appears as a standalone command token.
# Matches: start-of-line or after whitespace/semicolons/pipes/&&/||/!
# followed by the utility name followed by a non-word char (space, flag, end).
_CMD_TOKEN = re.compile(
    r'(?:^|[\s;|&!`(])({util})(?:\s|;|$|`|\))',
)

# Guard patterns: command -v <util> or which <util>
_GUARD_CMD_V = re.compile(r'command\s+-v\s+(\w+)')
_GUARD_WHICH = re.compile(r'which\s+(\w+)')


def _build_util_re(util: str) -> re.Pattern[str]:
    return re.compile(
        r'(?:^|[\s;|&!`(])' + re.escape(util) + r'(?:\s|;|$|`|\)|-)',
    )


_UTIL_RES: dict[str, re.Pattern[str]] = {u: _build_util_re(u) for u in FORBIDDEN}


def _is_in_single_quote(line: str, pos: int) -> bool:
    """Return True if position pos in line is inside a single-quoted string."""
    in_sq = False
    for i, ch in enumerate(line):
        if i >= pos:
            break
        if ch == "'":
            in_sq = not in_sq
    return in_sq


def scan_file(
    filepath: Path,
    guard_lookback: int = GUARD_LOOKBACK_DEFAULT,
) -> list[dict]:
    """Scan a shell script for forbidden utility references.

    Returns list of finding dicts: {line_no, severity, utility, guard_status, excerpt}.
    """
    try:
        text = filepath.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return []

    lines = text.splitlines()
    findings = []

    # Pre-compute heredoc ranges to exclude from scanning
    heredoc_ranges: list[tuple[int, int]] = []
    i = 0
    while i < len(lines):
        m = re.search(r'<<\s*[\'"!-]?(\w+)', lines[i])
        if m:
            delimiter = m.group(1)
            start = i + 1
            for j in range(start, len(lines)):
                if lines[j].strip() == delimiter:
                    heredoc_ranges.append((start, j))
                    i = j + 1
                    break
            else:
                i += 1
        else:
            i += 1

    def _in_heredoc(line_no: int) -> bool:
        for start, end in heredoc_ranges:
            if start <= line_no <= end:
                return True
        return False

    for line_no, line in enumerate(lines, start=1):
        # Skip comment lines
        stripped = line.lstrip()
        if stripped.startswith("#"):
            continue

        # Skip heredoc body lines
        if _in_heredoc(line_no):
            continue

        # Strip inline comment portion (text after unquoted #)
        # Simple heuristic: find # not inside quotes
        scan_portion = line
        in_sq = False
        in_dq = False
        for ci, ch in enumerate(line):
            if ch == "'" and not in_dq:
                in_sq = not in_sq
            elif ch == '"' and not in_sq:
                in_dq = not in_dq
            elif ch == "#" and not in_sq and not in_dq:
                scan_portion = line[:ci]
                break

        for util, util_re in _UTIL_RES.items():
            m = util_re.search(scan_portion)
            if not m:
                continue

            # Check if the match position is inside single quotes
            if _is_in_single_quote(scan_portion, m.start()):
                continue

            # Determine guard status: look back GUARD_LOOKBACK lines
            look_start = max(0, line_no - guard_lookback - 1)
            context_lines = lines[look_start:line_no]
            guarded = False
            for ctx_line in context_lines:
                if _GUARD_CMD_V.search(ctx_line):
                    guards = _GUARD_CMD_V.findall(ctx_line)
                    if util in guards:
                        guarded = True
                        break
                if _GUARD_WHICH.search(ctx_line):
                    guards = _GUARD_WHICH.findall(ctx_line)
                    if util in guards:
                        guarded = True
                        break

            severity = "WARN" if guarded else "ERROR"
            guard_status = "guarded" if guarded else "unguarded"
            excerpt = line.strip()[:80]

            findings.append({
                "line_no": line_no,
                "severity": severity,
                "utility": util,
                "guard_status": guard_status,
                "excerpt": excerpt,
            })

    return findings


# ---------------------------------------------------------------------------
# Path helpers
# ---------------------------------------------------------------------------

def _is_exempt(path: Path) -> bool:
    """Return True if path is EC2-side or data-scripts (exempt per Rule 16)."""
    rel = ""
    try:
        rel = str(path.relative_to(_WORKSPACE)).replace("\\", "/")
    except ValueError:
        return False
    return any(rel.startswith(p) for p in EXEMPT_PREFIXES)


def _is_in_scope(path: Path) -> bool:
    """Return True if path is in a Rule-16-scoped directory."""
    rel = ""
    try:
        rel = str(path.relative_to(_WORKSPACE)).replace("\\", "/")
    except ValueError:
        return False
    return any(rel.startswith(p) for p in IN_SCOPE_PREFIXES)


def _collect_sh_files(paths: list[str], all_mode: bool) -> list[Path]:
    """Collect .sh files from the given path list (or workspace if --all)."""
    collected: list[Path] = []
    if all_mode:
        for sh in _WORKSPACE.rglob("*.sh"):
            if not _is_exempt(sh):
                collected.append(sh)
        return sorted(collected)

    for p in paths:
        target = Path(p)
        if not target.is_absolute():
            target = _WORKSPACE / p
        if target.is_file() and target.suffix == ".sh":
            collected.append(target)
        elif target.is_dir():
            collected.extend(sorted(target.rglob("*.sh")))
        else:
            print(f"comp-shell: path not found or not .sh: {p}", file=sys.stderr)
    return collected


# ---------------------------------------------------------------------------
# Subcommands
# ---------------------------------------------------------------------------

def cmd_scan(args) -> int:
    guard_lookback = getattr(args, "guard_lookback", GUARD_LOOKBACK_DEFAULT)
    all_mode = getattr(args, "all", False)

    files = _collect_sh_files(getattr(args, "paths", []), all_mode)
    if not files:
        print("comp-shell: no .sh files to scan.", file=sys.stderr)
        return 0

    total_errors = 0
    total_warns = 0
    file_count = 0

    for sh_file in files:
        findings = scan_file(sh_file, guard_lookback=guard_lookback)
        if not findings:
            continue

        file_count += 1
        try:
            rel = str(sh_file.relative_to(_WORKSPACE)).replace("\\", "/")
        except ValueError:
            rel = str(sh_file)

        for f in findings:
            line = (
                f"{rel}:{f['line_no']}:{f['severity']}:{f['utility']}:"
                f"{f['guard_status']}:{f['excerpt']}"
            )
            print(line)
            if f["severity"] == "ERROR":
                total_errors += 1
            else:
                total_warns += 1

    if total_errors == 0 and total_warns == 0:
        scanned = len(files)
        print(f"OK: comp-shell scan clean ({scanned} file(s) scanned, 0 findings)")
    else:
        print(
            f"SUMMARY: {total_errors} ERROR, {total_warns} WARN "
            f"across {file_count} file(s)"
        )

    return 1 if total_errors > 0 else 0


def cmd_list_forbidden(_args) -> int:
    print("Forbidden Git Bash 3.6.7 utilities (CLAUDE.md Rule 16):")
    print("")
    for util in sorted(FORBIDDEN):
        fallback = FALLBACKS.get(util, "(no documented fallback)")
        print(f"  {util}")
        print(f"    Fallback: {fallback}")
        print("")
    print("Guard pattern: command -v <util> >/dev/null 2>&1")
    print("Reference: org/mcp/inbox-watch.sh (commit 045296b18, ADHC_BASHFIX.002)")
    return 0


# ---------------------------------------------------------------------------
# .compshellrc loader (v1 stub — path-based exemption only)
# ---------------------------------------------------------------------------

def _load_compshellrc() -> dict:
    """Stub loader for .compshellrc. v1: path-based exemption is hardcoded.
    v2 can extend this to read YAML allowlist from workspace root .compshellrc."""
    return {}


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        prog="comp-shell",
        description="Detect forbidden Git Bash 3.6.7 utilities in local-runtime shell scripts.",
    )
    sub = parser.add_subparsers(dest="command")

    # scan
    p_scan = sub.add_parser("scan", help="Scan shell scripts for forbidden utilities")
    p_scan.add_argument("paths", nargs="*", help="Files or directories to scan")
    p_scan.add_argument("--all", action="store_true",
                        help="Scan entire workspace (excluding EC2/data paths)")
    p_scan.add_argument("--guard-lookback", type=int, default=GUARD_LOOKBACK_DEFAULT,
                        dest="guard_lookback",
                        help=f"Lines to look back for a guard (default {GUARD_LOOKBACK_DEFAULT})")

    # list-forbidden
    sub.add_parser("list-forbidden", help="Print forbidden utilities + canonical fallbacks")

    args = parser.parse_args()

    _load_compshellrc()

    if args.command == "scan":
        return cmd_scan(args)
    elif args.command == "list-forbidden":
        return cmd_list_forbidden(args)
    else:
        parser.print_help()
        return 2


if __name__ == "__main__":
    sys.exit(main())
