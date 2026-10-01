#!/usr/bin/env python3
"""A function's WHOLE BUNDLE at one commit, member by member, against the zip that is live right now.

    python bundle_vs_live_census.py <repo-root> <function> <commit> <out.json> [--zip <built.zip>]

CTO rulings batch 61 item 3 (a function whose siblings are of mixed vintage moves as a whole bundle at one commit,
with the member census against the live zip) and batch 62 item 6 (the packet prints, for every bundled module
`served.py` imports directly or through a sibling, the member's hash beside CLOUD's at the pin).

Read-only. The live zip is downloaded from Lambda and its sha256 checked against the live CodeSha256. The bundle
"at the commit" is derived from the function's source-map row AT THAT COMMIT: each name in `files` comes from its
`staged_from` entry's repo path when it has one, else from `source_dir/<name>`, read with `git show <commit>:<path>`.
With --zip, the BUILT artifact's members are compared too, so the census grades the bytes that will be served.

Prints: members live / at the commit; identical, changed, added, removed; for each changed member the commit the live
bytes equal and how many commits the pin adds; the import closure of served.py with each member's state.
ASCII only.
"""
import ast
import base64
import hashlib
import io
import json
import subprocess
import sys
import urllib.request
import zipfile

import boto3

MAP = "infra/aws/lambda/ci/lambda-source-map.json"


def git(root, *args):
    return subprocess.run(["git", "-C", root] + list(args), capture_output=True)


TEXT = (".py", ".json", ".md", ".sh", ".js", ".txt", ".tf")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def norm(name, data):
    """Line endings folded to LF for text members: a Windows worktree builds CRLF where the commit holds LF, and
    that difference is not a change of content. The raw CR count is reported separately."""
    return data.replace(b"\r\n", b"\n") if name.endswith(TEXT) else data


def closure(members, start):
    """Bundle members reachable from `start` by import, through flat sibling module names."""
    modules = {name[:-3]: name for name in members if name.endswith(".py") and "/" not in name}
    seen, queue = [], [start]
    while queue:
        name = queue.pop(0)
        if name in seen or name not in members:
            continue
        seen.append(name)
        try:
            tree = ast.parse(members[name].decode("utf-8"))
        except (SyntaxError, UnicodeDecodeError):
            continue
        for node in ast.walk(tree):
            names = []
            if isinstance(node, ast.Import):
                names = [a.name.split(".")[0] for a in node.names]
            elif isinstance(node, ast.ImportFrom) and node.module and node.level == 0:
                names = [node.module.split(".")[0]]
            for mod in names:
                if mod in modules and modules[mod] not in seen:
                    queue.append(modules[mod])
    return seen


def main(argv):
    built = None
    if "--zip" in argv:
        i = argv.index("--zip")
        built = argv[i + 1]
        argv = argv[:i] + argv[i + 2:]
    root, fn, commit, out = argv[1:5]
    commit = git(root, "rev-parse", commit).stdout.decode().strip()
    lam = boto3.client("lambda", region_name="us-east-1")
    got = lam.get_function(FunctionName=fn)
    data = urllib.request.urlopen(got["Code"]["Location"], timeout=120).read()
    live_ok = base64.b64encode(hashlib.sha256(data).digest()).decode() == got["Configuration"]["CodeSha256"]
    live = {i.filename: zipfile.ZipFile(io.BytesIO(data)).read(i.filename)
            for i in zipfile.ZipFile(io.BytesIO(data)).infolist() if not i.is_dir()}
    smap = json.loads(git(root, "show", "%s:%s" % (commit, MAP)).stdout.decode("utf-8"))
    row = smap.get("functions", smap)[fn]
    staged = {e["packaged_as"]: e["repo_path"] for e in row.get("staged_from", [])}
    want, source_of = {}, {}
    for name in row["files"]:
        path = staged.get(name) or (row["source_dir"] + "/" + name)
        blob = git(root, "show", "%s:%s" % (commit, path))
        if blob.returncode != 0:
            raise SystemExit("ERROR: %s (for member %s) does not exist at %s" % (path, name, commit[:10]))
        want[name], source_of[name] = blob.stdout, path
    identical = sorted(n for n in want if n in live and sha(norm(n, live[n])) == sha(norm(n, want[n])))
    changed = sorted(n for n in want if n in live and sha(norm(n, live[n])) != sha(norm(n, want[n])))
    eol_only = sorted(n for n in identical if sha(live[n]) != sha(want[n]))
    added = sorted(set(want) - set(live))
    removed = sorted(set(live) - set(want))
    print("%s | live CodeSha256 %s (zip hashes to it: %s), LastModified %s | pin %s"
          % (fn, got["Configuration"]["CodeSha256"][:12], live_ok, got["Configuration"]["LastModified"][:19], commit[:10]))
    print("members: live %d, at the pin %d | identical %d (of them %d differ in line endings only), changed %d, "
          "added %d, removed %d" % (len(live), len(want), len(identical), len(eol_only), len(changed), len(added),
                                    len(removed)))
    history = []
    for name in changed:
        path = source_of[name]
        base, ahead = None, []
        for line in git(root, "log", "--format=%H\t%s", commit, "--", path).stdout.decode("utf-8", "replace").splitlines():
            h, s = line.split("\t", 1)
            if sha(norm(name, git(root, "show", "%s:%s" % (h, path)).stdout)) == sha(norm(name, live[name])):
                base = h
                break
            ahead.append([h[:10], s[:100]])
        history.append({"member": name, "source": path, "live_equals": base[:10] if base else None, "ahead": ahead})
        print("  ~ %-34s live = %-10s +%d commit(s)  %s" % (name, base[:10] if base else "NOT IN HISTORY", len(ahead),
                                                            "; ".join(h for h, _ in ahead[:5])))
    for name in added:
        print("  + %-34s %s" % (name, source_of[name]))
    for name in removed:
        print("  - %s" % name)
    reach = closure(want, "served.py") if "served.py" in want else []
    print("import closure of served.py at the pin: %d member(s)" % len(reach))
    closure_rows = []
    for name in reach:
        state = "ADDED" if name in added else ("CHANGED vs live" if name in changed else "identical to live")
        closure_rows.append({"member": name, "pin_sha256": sha(want[name])[:16],
                             "live_sha256": sha(live[name])[:16] if name in live else None, "state": state})
        print("    %-30s pin %s | live %s | %s" % (name, sha(want[name])[:12],
                                                    sha(live[name])[:12] if name in live else "-", state))
    result = {"function": fn, "pin": commit, "live_code_sha256": got["Configuration"]["CodeSha256"],
              "live_zip_hashes_to_it": live_ok, "live_members": len(live), "pin_members": len(want),
              "identical": len(identical), "eol_only": eol_only, "changed": changed, "added": added, "removed": removed,
              "history": history, "served_closure": closure_rows}
    if built:
        z = zipfile.ZipFile(built)
        zb = {i.filename: z.read(i.filename) for i in z.infolist() if not i.is_dir()}
        differ = sorted(n for n in set(zb) | set(want) if n not in zb or n not in want
                        or sha(norm(n, zb[n])) != sha(norm(n, want[n])))
        crlf = sorted(n for n in zb if n.endswith(TEXT) and b"\r\n" in zb[n])
        stale = [r["member"] for r in closure_rows
                 if r["member"] in zb and sha(norm(r["member"], zb[r["member"]])) != sha(norm(r["member"], want[r["member"]]))]
        print("BUILT zip %s: %d members; %d differ in content from the pin's bundle %s; text members carrying CRLF: %d; "
              "closure members that are not the pin's: %d %s"
              % (built.replace("\\", "/").split("/")[-1], len(zb), len(differ), differ[:8], len(crlf), len(stale), stale))
        result["built"] = {"members": len(zb), "differ_from_pin": differ, "closure_stale": stale, "crlf_members": crlf,
                           "zip_sha256_b64": base64.b64encode(hashlib.sha256(open(built, "rb").read()).digest()).decode()}
    json.dump(result, open(out, "w", encoding="utf-8", newline="\n"), indent=1)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
