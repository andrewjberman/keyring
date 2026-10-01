#!/usr/bin/env python3
"""The import closure of `served.py` inside one function's flat zip, each member beside CLOUD's bytes
(1.0.0_SA_CTO rulings batch 62 item 6; batch 61 item 3).

    python served_import_closure.py <git worktree> <function> [--zip <built zip>] [--ref HEAD] [--root served.py] [--json <out>]

WHY: a served move of `served.py` was signed on the PRESENCE of the modules it imports. Two functions bundled a
`canonical_profile_reads.py` of an older vintage, three bundled an `enforce.py` and `errors.py` that did not accept
the keywords `served.py` passes, and neither showed in a member list. This prints, for every bundled top-level
module `served.py` imports directly or through a sibling, the bundled member's sha256 beside the sha256 of the same
source file at --ref, and says which differ.

HOW the closure is found: the BUNDLED bytes are parsed (the built zip's when --zip is given, else the source-map
row's `git show <pin>:<repo_path>` or the source_dir file at --ref); every `import x`, `from x import ...` and
`importlib.import_module("x")` at ANY depth is followed when `x.py` is a top-level member of the same bundle.
Modules outside the bundle (stdlib, boto3, a layer) are counted and not followed.

WHAT the verdict means:
  EQUAL    the bundled bytes are the --ref bytes (CRLF-normalized).
  OLDER    they differ and the row's pin is an ancestor of --ref: an older vintage. A STOP for a served.py move.
  DIFFERS  they differ and the pin is not an ancestor (or the member has no pin): named, with the reason to give.
  NO-SOURCE the member has no source-map row that names where its bytes came from.
rc 1 when any closure member is OLDER, DIFFERS or NO-SOURCE; rc 0 when every member is EQUAL. Read-only.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import os
import subprocess
import sys
import zipfile


def _norm_sha(data):
    return hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest()


def _git(tree, *args):
    out = subprocess.run(["git", "-C", tree, *args], capture_output=True)
    return out.returncode, out.stdout


def _imports(source):
    names = set()
    try:
        tree = ast.parse(source.decode("utf-8"))
    except (SyntaxError, UnicodeDecodeError):
        return names
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                names.add(alias.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            if node.module and node.level == 0:
                names.add(node.module.split(".")[0])
        elif (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == "import_module"
              and node.args and isinstance(node.args[0], ast.Constant) and isinstance(node.args[0].value, str)):
            names.add(node.args[0].value.split(".")[0])
    return names


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("tree")
    ap.add_argument("function")
    ap.add_argument("--zip", dest="zip_path")
    ap.add_argument("--ref", default="HEAD")
    ap.add_argument("--root", default="served.py",
                    help="the member whose import closure is printed (served.py by default; retained.py for the adapter's retained reader)")
    ap.add_argument("--json", dest="json_out")
    a = ap.parse_args(argv)

    with open(os.path.join(a.tree, "infra/aws/lambda/ci/lambda-source-map.json"), encoding="utf-8") as fh:
        row = json.load(fh)["functions"][a.function]
    staged = {s["packaged_as"]: s for s in row.get("staged_from", []) or []}
    origin = {}
    for name in row.get("files", []):
        if name in staged:
            origin[name] = (staged[name]["repo_path"], staged[name]["pin"])
        else:
            origin[name] = (row["source_dir"].rstrip("/") + "/" + name, None)
    for name, s in staged.items():
        origin.setdefault(name, (s["repo_path"], s["pin"]))

    zf = zipfile.ZipFile(a.zip_path) if a.zip_path else None
    members = set(zf.namelist()) if zf else set(origin)

    def bundled(name):
        if zf is not None:
            return zf.read(name)
        repo_path, pin = origin[name]
        rc, data = _git(a.tree, "show", "%s:%s" % (pin or a.ref, repo_path))
        if rc != 0:
            raise SystemExit("ERROR: cannot read %s at %s" % (repo_path, pin or a.ref))
        return data

    if a.root not in members:
        raise SystemExit("ERROR: %s bundles no %s" % (a.function, a.root))

    closure, outside, queue = [], set(), [a.root]
    seen = set()
    while queue:
        name = queue.pop(0)
        if name in seen:
            continue
        seen.add(name)
        closure.append(name)
        for mod in sorted(_imports(bundled(name))):
            if mod + ".py" in members:
                queue.append(mod + ".py")
            else:
                outside.add(mod)

    rows, bad = [], 0
    for name in closure:
        data = bundled(name)
        got = _norm_sha(data)
        src = origin.get(name)
        if src is None:
            rows.append({"member": name, "verdict": "NO-SOURCE", "bundled": got})
            bad += 1
            continue
        repo_path, pin = src
        rc, ref_bytes = _git(a.tree, "show", "%s:%s" % (a.ref, repo_path))
        if rc != 0:
            rows.append({"member": name, "verdict": "NO-SOURCE", "bundled": got, "repo_path": repo_path})
            bad += 1
            continue
        want = _norm_sha(ref_bytes)
        if got == want:
            verdict = "EQUAL"
        else:
            older = False
            if pin:
                older = _git(a.tree, "merge-base", "--is-ancestor", pin, a.ref)[0] == 0
            verdict = "OLDER" if older else "DIFFERS"
            bad += 1
        rows.append({"member": name, "verdict": verdict, "bundled": got, "at_ref": want, "repo_path": repo_path,
                     "pin": (pin or "")[:10]})

    rc_ref, ref_hash = _git(a.tree, "rev-parse", "--short=10", a.ref)
    print("%s: import closure of %s -- %d bundled member(s), %d module name(s) outside the bundle; ref %s; bytes from %s"
          % (a.function, a.root, len(closure), len(outside), ref_hash.decode().strip() if rc_ref == 0 else a.ref,
             "the built zip" if zf else "the source-map row"))
    for r in rows:
        print("  %-9s %-28s bundled %s  ref %s  pin %-10s %s" % (
            r["verdict"], r["member"], r["bundled"][:12], r.get("at_ref", "-" * 12)[:12], r.get("pin", ""), r.get("repo_path", "")))
    print("closure members not EQUAL to the ref: %d of %d" % (bad, len(closure)))
    # A name the closure imports that is neither bundled nor standard library must come from a layer or the
    # runtime (boto3). It is printed so a sibling the new bytes need and the bundle lacks is not read as "outside".
    stdlib = getattr(sys, "stdlib_module_names", frozenset())
    non_std = sorted(n for n in outside if n not in stdlib)
    print("imported names outside the bundle and outside the standard library: %d %s" % (len(non_std), non_std))
    if a.json_out:
        with open(a.json_out, "w", encoding="utf-8") as fh:
            json.dump({"function": a.function, "root": a.root, "ref": a.ref, "closure": rows, "outside_bundle": sorted(outside)}, fh, indent=1)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
