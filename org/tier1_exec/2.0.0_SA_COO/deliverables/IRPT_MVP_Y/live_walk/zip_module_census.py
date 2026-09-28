"""Flat-zip module-name collision census (CTO 102269 item 2): every top-level module in a BUILT Lambda zip, each named
with the source file its bytes came from.

    python zip_module_census.py <zip> --tree <git worktree> [--ref HEAD] [--root infra/aws/lambda/investor-reporting]

A flat zip flattens every source directory into one namespace. Two sources with one basename (holdings/errors.py and
_authz/errors.py) become ONE module, and the importer silently gets whichever the build copied. irpt-status 5fSyChId
(2026-09-28) shipped holdings/errors.py where served.py needed _authz/errors.py, and every owner-read refusal became a
500.

For each top-level .py in the zip, the source files with that basename under --root at --ref (tests excluded):
- UNIQUE: one source, and the zip's bytes are it;
- COLLISION: several sources; the WINNER is the one whose bytes the zip carries. The build must intend it;
- STALE: the zip's bytes match NO source at --ref (an old vintage);
- ZIP-ONLY: no source has that basename.
Exit 1 on any STALE, or on a COLLISION whose winner is not named in --expect (repeatable: name=relative/source/path).
Bytes are compared CRLF-normalized. Read-only.
"""
import argparse
import collections
import hashlib
import os
import subprocess
import sys
import zipfile


def digest(data):
    return hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest()[:8]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("zip")
    ap.add_argument("--tree", required=True)
    ap.add_argument("--ref", default="HEAD")
    ap.add_argument("--root", default="infra/aws/lambda/investor-reporting")
    ap.add_argument("--expect", action="append", default=[], help="name=relative/source/path the build intends")
    a = ap.parse_args(argv)
    root = a.root.rstrip("/") + "/"
    expect = dict(e.split("=", 1) for e in a.expect)
    listed = subprocess.run(["git", "-C", a.tree, "ls-tree", "-r", "--name-only", a.ref, root],
                            capture_output=True, text=True, check=True).stdout.split()
    sources = collections.defaultdict(dict)
    for path in listed:
        if path.endswith(".py") and "/tests/" not in path:
            data = subprocess.run(["git", "-C", a.tree, "show", "%s:%s" % (a.ref, path)], capture_output=True,
                                  check=True).stdout
            sources[os.path.basename(path)][path[len(root):]] = digest(data)
    z = zipfile.ZipFile(a.zip)
    members = sorted(n for n in z.namelist() if n.endswith(".py") and "/" not in n)
    counts, failures = collections.Counter(), []
    for name in members:
        got = digest(z.read(name))
        cands = sources.get(name, {})
        winners = [p for p, d in cands.items() if d == got]
        if not cands:
            verdict, detail = "ZIP-ONLY", ""
        elif not winners:
            verdict, detail = "STALE", "zip %s; sources %s" % (got, cands)
            failures.append(name)
        elif len(cands) == 1:
            verdict, detail = "UNIQUE", winners[0]
        else:
            verdict = "COLLISION"
            detail = "winner %s of %s" % (winners, sorted(cands))
            if expect.get(name) not in winners:
                failures.append(name)
                detail += " -- NOT the intended %s" % (expect.get(name) or "(unnamed: pass --expect %s=<path>)" % name)
        counts[verdict] += 1
        if verdict != "UNIQUE":
            print("%-10s %-24s %s" % (verdict, name, detail))
    print("\n%d top-level modules: %s | FAIL %s" % (len(members), dict(counts), failures or "none"))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
