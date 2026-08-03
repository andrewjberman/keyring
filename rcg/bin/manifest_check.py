"""rcg/ folder-cleanliness gate: the tree must be a subset of MANIFEST.yaml allowed_paths.

The folder contract's enforcement (NFRA_REPOCOHERENCEGRAPH PRD s.12): INTENT = the manifest
allowlist; DENOMINATOR = tracked + staged files under rcg/, enumerated from git at run time;
the GAP is printed and any gap is a DENY (rc=2). append_only files additionally require the
HEAD version to be a byte-prefix of the working version -- history is never edited.

Standalone by design (runnable today, solo posture R-0001); commit-chain wiring is the
D-0001 CTO ferry item. rc: 0 clean / 2 deny / 3 cannot-evaluate (never a silent pass).
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import yaml

WS = Path(__file__).resolve().parents[2]
MANIFEST = WS / "rcg" / "MANIFEST.yaml"


def git(*args: str) -> str:
    out = subprocess.run(["git", *args], cwd=WS, capture_output=True, text=True)
    if out.returncode != 0:
        print(f"BLOCKED: git {' '.join(args)} rc={out.returncode}: {out.stderr.strip()}")
        sys.exit(3)
    return out.stdout


def main() -> int:
    spec = yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))
    allowed = set(spec["allowed_paths"])
    append_only = set(spec.get("append_only", []))

    tracked = {p for p in git("ls-files", "--", "rcg/").splitlines() if p}
    staged = {p for p in git("diff", "--cached", "--name-only", "--", "rcg/").splitlines() if p}
    population = tracked | staged
    extras = sorted(population - allowed)

    tampered: list[str] = []
    for path in sorted(append_only & population):
        head = subprocess.run(["git", "show", f"HEAD:{path}"], cwd=WS,
                              capture_output=True)
        if head.returncode != 0:
            continue  # not yet in HEAD -- first commit of the file, nothing to protect
        current = (WS / path).read_bytes()
        if not current.startswith(head.stdout):
            tampered.append(path)

    print(f"rcg-manifest-check: DENOMINATOR {len(population)} tracked+staged file(s) under "
          f"rcg/ vs {len(allowed)} allowed; append-only checked: {len(append_only & population)}")
    if extras or tampered:
        for p in extras:
            print(f"  DENY [not-in-manifest] {p}  -> amend rcg/MANIFEST.yaml in the SAME commit or remove")
        for p in tampered:
            print(f"  DENY [append-only-edited] {p}  -> prior lines are immutable; append, never edit")
        return 2
    print("  CLEAN -- tree is a subset of the manifest; append-only intact.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
