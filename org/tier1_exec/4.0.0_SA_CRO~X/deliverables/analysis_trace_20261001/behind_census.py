"""For each served member that differs from CLOUD HEAD: which commit of its source file do the served bytes equal,
and which newer commits of that file are NOT served. Also resolves the first census's NO-SOURCE members against the
whole HEAD tree by path suffix. Read-only.

    python behind_census.py <scratch dir>
"""
import hashlib
import json
import subprocess
import sys
import zipfile

S = sys.argv[1]


def norm(b):
    return hashlib.sha256(b.replace(b"\r\n", b"\n")).hexdigest()


def git(*a):
    return subprocess.run(["git", *a], capture_output=True).stdout


census = json.load(open(S + "/member_census.json"))
tree = [p for p in git("ls-tree", "-r", "--name-only", "HEAD").decode().split("\n") if p]
out = {}
for fn, rec in census["packages"].items():
    z = zipfile.ZipFile("%s/%s.zip" % (S, fn))
    print("\n== %s" % fn)
    rows = []
    for d in rec["differ"]:
        served = norm(z.read(d["member"]))
        log = git("log", "--format=%h|%cI|%s", "--", d["source"]).decode().strip().split("\n")
        found = None
        for i, line in enumerate(log):
            h = line.split("|", 1)[0]
            if norm(git("show", "%s:%s" % (h, d["source"]))) == served:
                found = i
                break
        if found is None:
            print("  %-30s served bytes equal NO commit of %s (%d commits walked)" % (d["member"], d["source"], len(log)))
            rows.append({"member": d["member"], "source": d["source"], "served_equals": None, "walked": len(log)})
            continue
        newer = log[:found]
        print("  %-30s = %s; %d newer commit(s) not served:" % (d["member"], log[found].split("|")[0] + " " + log[found].split("|")[1][:16], len(newer)))
        for line in newer:
            h, when, subj = line.split("|", 2)
            print("       %s %s %s" % (h, when[:16], subj[:150]))
        rows.append({"member": d["member"], "source": d["source"], "served_equals": log[found].split("|")[0],
                     "not_served": [line.split("|")[0] for line in newer]})
    res = []
    for n in rec["no_head_source"]:
        got = norm(z.read(n))
        cands = [p for p in tree if p.endswith("/" + n) or p == n or p.endswith("/" + n.split("/", 1)[-1])]
        cands = [p for p in cands if "/tests/" not in p and "/fixtures/" not in p]
        hit = [p for p in cands if norm(git("show", "HEAD:" + p)) == got]
        res.append({"member": n, "identical_to": hit[0] if hit else None, "candidates": len(cands)})
    same = sum(1 for r in res if r["identical_to"])
    print("  suffix-resolved: %d of %d earlier NO-SOURCE members are identical to a HEAD file; not identical:" % (same, len(res)))
    for r in res:
        if not r["identical_to"]:
            print("       %s (%d candidate paths)" % (r["member"], r["candidates"]))
    out[fn] = {"behind": rows, "suffix_resolved": res}
json.dump(out, open(S + "/behind_census.json", "w"), indent=1)
