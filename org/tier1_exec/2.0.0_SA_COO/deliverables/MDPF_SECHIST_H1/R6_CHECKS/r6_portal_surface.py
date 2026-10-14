"""MDPF_SECHIST round 6, SH-t-25: the portal candidate's surface, exactly. Read only (git diff in the nested portal repo).

  python r6_portal_surface.py <portal repo path> <base ref> <head ref>

The candidate may change EXACTLY these portal-root-relative paths and no others; every other path in the diff is a defect, and the four files
a feature must never carry (package.json, bun.lock, src/lib/firmAccess.ts, src/App.tsx) must show a zero-line diff.
Last line: PORTAL-SURFACE-OK files=<n> ... or PORTAL-SURFACE-BAD <reason>.
"""
from __future__ import annotations

import subprocess
import sys

ALLOWED = {
    "src/api/portal-proxy.ts",
    "src/pages/Positioning/shared/etfAdapter.ts",
    "src/pages/Positioning/tabs/HoldingsTab.tsx",
    "src/pages/Positioning/tabs/ReturnsFrontier.tsx",
    "src/pages/Positioning/__harness__/frontierLabel.harness.cjs",
    "src/pages/Positioning/__harness__/frontierFixture.json",
    "src/pages/Positioning/__harness__/frontierNoCarry.golden.json",
}
NEVER = ("package.json", "bun.lock", "src/lib/firmAccess.ts", "src/App.tsx")


def git(repo, *args):
    return subprocess.check_output(["git", "-C", repo, *args], text=True).strip()


def main(repo, base, head):
    changed = set(x for x in git(repo, "diff", "--name-only", base, head).split("\n") if x)
    extra, missing = sorted(changed - ALLOWED), sorted(ALLOWED - changed)
    if extra or missing:
        print("PORTAL-SURFACE-BAD unexpected=" + str(extra) + " missing=" + str(missing) + " changed=" + str(len(changed)))
        return 1
    for p in NEVER:
        n = len([x for x in git(repo, "diff", base, head, "--", p).split("\n") if x])
        if n:
            print("PORTAL-SURFACE-BAD forbidden file changed: " + p + " (" + str(n) + " diff lines)")
            return 1
    print("PORTAL-SURFACE-OK files=" + str(len(changed)) + " forbidden=0 base=" + base + " head=" + head)
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("PORTAL-SURFACE-BAD usage: r6_portal_surface.py <portal repo> <base> <head>")
        sys.exit(2)
    sys.exit(main(*sys.argv[1:]))
