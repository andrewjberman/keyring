"""Deployed-package member census against CLOUD HEAD. Read-only.

    python member_census.py <scratch dir holding <fn>.zip> <fn> [<fn> ...]

Each .py/.json member of a deployed zip is hashed (CRLF-normalized) and compared to the HEAD blob of its source
path. Source path: the source map's staged_from[packaged_as], else source_dir/<member>, else any same-basename
file under infra/aws/lambda/investor-reporting (tests excluded). Prints the denominator per package.
"""
import collections
import hashlib
import json
import subprocess
import sys
import zipfile

ROOT = "infra/aws/lambda/investor-reporting/"
S = sys.argv[1]


def norm(b):
    return hashlib.sha256(b.replace(b"\r\n", b"\n")).hexdigest()


def git(*a):
    return subprocess.run(["git", *a], capture_output=True).stdout


head = git("rev-parse", "--short=10", "HEAD").decode().strip()
tree = [p for p in git("ls-tree", "-r", "--name-only", "HEAD", ROOT).decode().split("\n") if p]
by_base = collections.defaultdict(list)
for p in tree:
    if "/tests/" in p or "/fixtures/" in p:
        continue
    by_base[p.rsplit("/", 1)[-1]].append(p)
smap = json.load(open("infra/aws/lambda/ci/lambda-source-map.json"))["functions"]
blob = {}


def head_sha(p):
    if p not in blob:
        blob[p] = norm(git("show", "HEAD:" + p))
    return blob[p]


out = {"head": head, "packages": {}}
print("CLOUD HEAD %s; %d tracked files under %s" % (head, len(tree), ROOT))
for fn in sys.argv[2:]:
    v = smap[fn]
    staged = {e["packaged_as"]: e["repo_path"] for e in v.get("staged_from", [])}
    z = zipfile.ZipFile("%s/%s.zip" % (S, fn))
    members = [n for n in z.namelist() if n.endswith((".py", ".json")) and "/tests/" not in n and "fixtures/" not in n]
    same, differ, nosrc = [], [], []
    for n in members:
        got = norm(z.read(n))
        cands = []
        if n in staged:
            cands.append(staged[n])
        cands.append(v["source_dir"].rstrip("/") + "/" + n)
        cands += by_base.get(n.rsplit("/", 1)[-1], [])
        cands = [c for i, c in enumerate(cands) if c in tree and c not in cands[:i]]
        if not cands:
            nosrc.append(n)
            continue
        hit = [c for c in cands if head_sha(c) == got]
        if hit:
            same.append((n, hit[0]))
        else:
            differ.append((n, cands[0], got[:12], head_sha(cands[0])[:12]))
    print("\n%s: %d members total, %d .py/.json compared; identical to HEAD %d, differ %d, no HEAD source %d"
          % (fn, len(z.namelist()), len(members), len(same), len(differ), len(nosrc)))
    for n, c, g, h in differ:
        print("  DIFFER %-34s vs %s  served %s head %s" % (n, c[len(ROOT):], g, h))
    for n in nosrc:
        print("  NO-SOURCE %s" % n)
    out["packages"][fn] = {"members_total": len(z.namelist()), "compared": len(members), "identical": len(same),
                           "differ": [{"member": n, "source": c, "served": g, "head": h} for n, c, g, h in differ],
                           "no_head_source": nosrc}
json.dump(out, open("%s/member_census.json" % S, "w"), indent=1)
