#!/usr/bin/env python3
"""client-data-check.py -- refuse a commit whose staged files carry a served client account id.

Rule (dell2 1.0.0_SA_CTO~DELL2 ruling CTO_RULING_CLIENT_ACCOUNT_DATA_IN_REPO_CONTAINMENT_20261009.md item 6; owner of the gate edit
1.0.0_SA_CTO, item 8): no account id, balance, fee or flow in any tracked file; the repo carries counts, sha256 and reason codes only.
Built after 1ba8eafcda (2026-10-09) put 121 accounts on CLOUD: the sensitive-leak gate (.tools/commit_gate_lib.sh cg_sensitive_hits)
matches FILE NAMES only, so no gate read a file's content for account ids.

HOW: every staged text file is read from the INDEX (the bytes being committed, never the working tree). Each id-shaped token (letters,
digits and '-', 5-24 long, at least 5 digits) is upper-cased and sha256-hashed, and the hash is looked up in the hashed id list. The list
lives OUTSIDE the repo -- $OPAL_ACCOUNT_ID_HASHES, else ~/.opal/account_id_hashes.txt -- one lowercase sha256 hex per line of the
upper-cased served account id, so no id ever enters the repo or this gate. A hit prints path, line number and hit count, never the token.

ABSENT IS NOT EMPTY: with no hash list the gate cannot see account ids, so it prints a loud WARN naming the missing file and passes
(exit 0) -- a missing list never reads as "no client data". Exit 1 on any hit. Override (audited by safe-commit): CLIENT_DATA_ALLOW=<reason>.
COST: one hash per candidate token of staged text files, milliseconds for ordinary commits. NON-APPLICATION: binary files, files over 8 MB
(WARN printed), deletions.
"""
from __future__ import annotations

import hashlib
import os
import re
import subprocess
import sys
from pathlib import Path

TOKEN_RE = re.compile(rb"(?<![A-Za-z0-9-])[A-Za-z0-9][A-Za-z0-9-]{4,23}(?![A-Za-z0-9-])")
MAX_BYTES = 8 * 1024 * 1024


def _hash_list_path() -> Path:
    env = os.environ.get("OPAL_ACCOUNT_ID_HASHES", "").strip()
    return Path(env) if env else Path.home() / ".opal" / "account_id_hashes.txt"


def _load_hashes(p: Path) -> set[str]:
    out = set()
    for line in p.read_text(encoding="utf-8").splitlines():
        h = line.strip().lower()
        if len(h) == 64 and all(c in "0123456789abcdef" for c in h):
            out.add(h)
    return out


def _staged_paths() -> list[str]:
    staged = os.environ.get("STAGED")
    if staged is None:
        staged = subprocess.run(["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR"],
                                capture_output=True, text=True, encoding="utf-8").stdout
    return [s for s in staged.splitlines() if s.strip()]


def _index_bytes(path: str) -> bytes | None:
    r = subprocess.run(["git", "cat-file", "-p", f":{path}"], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def hits_in(data: bytes, hashes: set[str]) -> list[tuple[int, int]]:
    """(line number, hit count) for every line carrying a token whose hash is in the list."""
    found = []
    for n, line in enumerate(data.splitlines(), 1):
        k = 0
        for m in TOKEN_RE.finditer(line):
            tok = m.group(0)
            if sum(1 for b in tok if 48 <= b <= 57) < 5:
                continue
            if hashlib.sha256(tok.upper()).hexdigest() in hashes:
                k += 1
        if k:
            found.append((n, k))
    return found


def main() -> int:
    lp = _hash_list_path()
    if not lp.is_file():
        print(f"WARN: client-data-check: hashed account-id list ABSENT at {lp} -- this commit was NOT checked for client account ids "
              "(absent is not empty; set OPAL_ACCOUNT_ID_HASHES or place the list there).", file=sys.stderr)
        return 0
    hashes = _load_hashes(lp)
    if not hashes:
        print(f"WARN: client-data-check: hashed account-id list at {lp} holds 0 valid hashes -- NOT checked.", file=sys.stderr)
        return 0
    bad = []
    for path in _staged_paths():
        data = _index_bytes(path)
        if data is None:
            continue
        if len(data) > MAX_BYTES:
            print(f"WARN: client-data-check: {path} is {len(data)} bytes (> {MAX_BYTES}); not scanned.", file=sys.stderr)
            continue
        if b"\x00" in data[:8192]:
            continue
        h = hits_in(data, hashes)
        if h:
            bad.append((path, h))
    if not bad:
        return 0
    allow = os.environ.get("CLIENT_DATA_ALLOW", "").strip()
    total = sum(k for _, h in bad for _, k in h)
    print(f"BLOCKED: client-data-check: {total} served client account id(s) in {len(bad)} staged file(s) "
          f"(list {lp}, {len(hashes)} hashes). Tokens are not printed.", file=sys.stderr)
    for path, h in bad:
        lines = ", ".join(f"{n}(x{k})" if k > 1 else str(n) for n, k in h[:12])
        more = f" +{len(h) - 12} more lines" if len(h) > 12 else ""
        print(f"  {path}: lines {lines}{more}", file=sys.stderr)
    print("  The repo carries counts, sha256 and reason codes only: move the file outside the repo or redact each id to a token.",
          file=sys.stderr)
    if allow:
        print(f"  OVERRIDE CLIENT_DATA_ALLOW='{allow}' -- passing.", file=sys.stderr)
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
