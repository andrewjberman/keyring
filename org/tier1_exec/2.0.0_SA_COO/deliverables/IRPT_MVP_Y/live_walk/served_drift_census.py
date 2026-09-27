"""Served-vs-source census for Y-owned modules.

    python served_drift_census.py <dir holding the unpacked packages named in PACKAGES>

Every .py in each deployed IRPT package whose basename is a Y-owned
source file (intake/, ycharts/, ops/ at P's HEAD, tests excluded) is compared, CRLF-normalized. Read-only.
A flat package's same-named module may be a DIFFERENT module (holdings' own entry.py): read the docstring before
calling a difference drift."""
import collections
import hashlib
import os
import subprocess
import sys

P = r"C:\Users\AndrewBerman\Desktop\irpt-smoke-p-backend-20260923"
ROOT = "infra/aws/lambda/investor-reporting/"
OWNED = ("intake/", "ycharts/", "ops/")
S = sys.argv[1]
PACKAGES = {"irpt-ycharts-generate": "genzip", "irpt-status": "statuszip", "resident lt": "respkg",
            "irpt-export-render": "pkg_irpt-export-render", "irpt-holdings": "pkg_irpt-holdings",
            "irpt-intake-poller": "pkg_irpt-intake-poller", "irpt-performance-adapter": "pkg_irpt-performance-adapter",
            "irpt-narrative": "pkg_irpt-narrative"}


def norm(b):
    return hashlib.sha256(b.replace(b"\r\n", b"\n")).hexdigest()[:12]


head = subprocess.run(["git", "-C", P, "rev-parse", "--short=10", "HEAD"], capture_output=True, text=True).stdout.strip()
files = subprocess.run(["git", "-C", P, "ls-tree", "-r", "--name-only", "HEAD", ROOT], capture_output=True,
                       text=True).stdout.split()
owned = [f for f in files if f.endswith(".py") and f[len(ROOT):].startswith(OWNED) and "/tests/" not in f]
source = collections.defaultdict(dict)
for f in owned:
    data = subprocess.run(["git", "-C", P, "show", "HEAD:" + f], capture_output=True).stdout
    source[os.path.basename(f)][f[len(ROOT):]] = norm(data)
print("P HEAD %s: %d Y-owned source modules (%d basenames)" % (head, len(owned), len(source)))
stale = []
for name, sub in PACKAGES.items():
    base = os.path.join(S, sub)
    compared = same = 0
    for dp, _, fn in os.walk(base):
        if {"tests", "fixtures", "__pycache__"} & set(dp.replace(base, "").split(os.sep)):
            continue
        for f in fn:
            if not f.endswith(".py") or f not in source:
                continue
            got = norm(open(os.path.join(dp, f), "rb").read())
            rel = os.path.relpath(os.path.join(dp, f), base).replace(os.sep, "/")
            cands = source[f]
            # a structured package names its own source path; a flat one is matched on any same-named Y source
            exact = {k: v for k, v in cands.items() if rel.endswith(k)} or cands
            compared += 1
            if got in exact.values():
                same += 1
            else:
                stale.append((name, rel, got, exact))
    print("%-26s compared %3d Y-owned modules, %3d identical to P HEAD, %d differ" % (name, compared, same, compared - same))
print("\nDIFFERING (package, served file, served sha -> P HEAD candidates):")
for name, rel, got, cands in stale:
    print("  %-24s %-40s %s -> %s" % (name, rel, got, cands))
