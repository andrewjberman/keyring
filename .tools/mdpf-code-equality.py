#!/usr/bin/env python3
"""MDPF runner code equality -- read-only comparison of the runner's code prefixes with the repo.

WHAT IT COMPARES. The MDPF daily runner pulls its code from the code prefixes of the opal-data-mdpf bucket with two
aws s3 sync --delete lines in infra/aws/ec2/mdpf-daily-runner/mdpf-daily-dispatch.sh. This tool compares, file by file,
every runner code tree with its repo home: the script trees declared in CODE_TREES for the runner's product key (the layers that are not
shared repo homes), and the config tree (repo home data/mdpf/config; its S3 prefix is read from the dispatch script's
config sync line, never typed here). Four script trees and one config tree: five trees.

HOW EQUALITY IS DECIDED. A local file is EQUAL when the S3 object of the same relative name has an ETag equal to the
md5 of the bytes git holds for that file: its index blob (git show :PATH), which is the byte content the deploy uploads.
The working tree is read only for a path with no index entry. A multipart ETag (it contains a dash) is UNDETERMINED and
is never EQUAL. A local file with no S3 object is MISSING_ON_S3; an S3 object with no local file is EXTRA_ON_S3; any
other pair is DIFFER. The basis of each EQUAL decision (blob or worktree) is printed, and an EQUAL blob-basis file whose
working copy holds CR bytes is printed with its CR count (worktree_cr).

WHAT IT NEVER DOES. It never repairs, copies, uploads, deletes or moves anything. Its only AWS calls are list reads
(boto3, default credential chain, region us-east-1). A DIFFER, MISSING_ON_S3 or EXTRA_ON_S3 name is a fact about the
tree, not an instruction. A repo file that is not a runner member (a test, a QA tool, a file a bundle ships) is
expected to read that way. Equality of the whole tree is not a goal; named files EQUAL is the goal of a deploy act.

MODES. No arguments: one TREE table per tree (with its names), then one summary line. --files REPO_PATH ...: grades
only the named files; the trees that hold them are printed, then one NAMED line per name, then the summary line.
Summary denominators: files = distinct relative names across the local and S3 sides of the trees shown, so
equal + not_equal = files; under --files, named = the names given and named_not_equal = those not EQUAL.

EXIT CODES. 0 = the run completed (whole-tree mode, or under --files every named file EQUAL). 1 = under --files at
least one named file is not EQUAL. 2 = REFUSED: a named file is under no runner code tree, the dispatch script's prefix
lines are unreadable or ambiguous, or the S3 read failed; in each case nothing is compared and nothing is written.
"""
from __future__ import annotations

import argparse
import hashlib
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REGION = "us-east-1"
# The runner's dispatch script. Its CODE_PREFIX assignment and its config sync line are the only sources of the config
# tree's S3 prefix (see runner_config_prefix). The config sync is the line whose destination ends in the dot-dot path
# to config; the repo home below is the tree that line delivers.
DISPATCH_REL = "infra/aws/ec2/mdpf-daily-runner/mdpf-daily-dispatch.sh"
CONFIG_HOME = "data/mdpf/config"
CODE_PREFIX_RE = re.compile(r'^CODE_PREFIX="([^"\n]+)"', re.M)
CONFIG_SYNC_RE = re.compile(r's3 sync "s3://\$\{MDPF_BUCKET\}/\$\{CODE_PREFIX\}/([^"/\n]+)/" "[^"\n]*/\.\./config/"')
CLASSES = (("differ", "DIFFER"), ("missing_on_s3", "MISSING_ON_S3"), ("extra_on_s3", "EXTRA_ON_S3"),
           ("undetermined", "UNDETERMINED"))


def _ascii(text):
    return str(text).encode("ascii", "backslashreplace").decode("ascii")


def _repo_root():
    try:
        got = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True)
    except OSError:
        got = None
    if got is not None and got.returncode == 0 and got.stdout.strip():
        return os.path.normpath(got.stdout.strip())
    return os.path.dirname(HERE)


ROOT = _repo_root()


def load_core():
    tools = os.path.join(ROOT, ".tools")
    if tools not in sys.path:
        sys.path.insert(0, tools)
    import safe_deploy_core
    return safe_deploy_core


def runner_config_prefix(dispatch_path):
    """Return the S3 prefix the runner syncs its config from, read from the dispatch script.

    Raises ValueError with the reason when a line is unreadable or ambiguous. No default is used."""
    try:
        with open(dispatch_path, encoding="utf-8") as fh:
            text = fh.read()
    except OSError:
        raise ValueError("dispatch script unreadable (%s)" % DISPATCH_REL)
    code = CODE_PREFIX_RE.findall(text)
    sub = CONFIG_SYNC_RE.findall(text)
    if len(code) != 1:
        raise ValueError("expected one CODE_PREFIX assignment in %s, found %d" % (DISPATCH_REL, len(code)))
    if len(sub) != 1:
        raise ValueError("expected one config sync line in %s, found %d" % (DISPATCH_REL, len(sub)))
    return "%s/%s/" % (code[0].strip("/"), sub[0])


def _product_key():
    """The runner's CODE_TREES key, read through the estate's scope registry (lib/opal_naming.py lookup)."""
    lib = os.path.join(ROOT, "lib")
    if lib not in sys.path:
        sys.path.insert(0, lib)
    import opal_naming
    return opal_naming.lookup("mdpf")["key"]


def runner_trees(core):
    """The runner's code trees: the script layers of the runner's CODE_TREES row minus its shared repo homes, plus config."""
    mdpf = core.CODE_TREES[_product_key()]
    bucket = mdpf["bucket"]
    shared = frozenset(mdpf.get("shared_repo_homes", ()))
    trees = []
    for layer, (home, prefix) in mdpf["layers"].items():
        if layer in shared:
            continue
        trees.append({"home": home, "bucket": bucket, "prefix": prefix})
    trees.append({"home": CONFIG_HOME, "bucket": bucket,
                  "prefix": runner_config_prefix(os.path.join(ROOT, *DISPATCH_REL.split("/")))})
    return trees


def _md5_file(path):
    h = hashlib.md5()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def _blob_md5(full):
    """md5 of the bytes git holds in its index for the local file `full`, or None.

    ROOT is read at call time. None when git exits non-zero (no index entry) or when the path lies outside ROOT.
    No fallback to the working tree happens here; the caller decides that."""
    try:
        rel = os.path.relpath(full, ROOT).replace(os.sep, "/")
    except ValueError:  # a path on another drive lies outside ROOT
        return None
    if rel.startswith("../"):
        return None
    got = subprocess.run(["git", "-C", ROOT, "show", ":" + rel], capture_output=True)
    if got.returncode != 0:
        return None
    return hashlib.md5(got.stdout).hexdigest()


def _cr_count(path):
    n = 0
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            n += chunk.count(b"\r")
    return n


def _local_files(local_dir):
    out = {}
    for dirpath, dirnames, filenames in os.walk(local_dir):
        dirnames[:] = [d for d in dirnames if d != "__pycache__"]
        for fn in filenames:
            if fn.endswith(".pyc"):
                continue
            full = os.path.join(dirpath, fn)
            out[os.path.relpath(full, local_dir).replace(os.sep, "/")] = full
    return out


def compare_tree(local_dir, bucket, prefix, s3):
    """Classify every name on the local side and the S3 side of one tree. Read-only: list calls only."""
    local = _local_files(local_dir)
    remote = {}
    for page in s3.get_paginator("list_objects_v2").paginate(Bucket=bucket, Prefix=prefix):
        for obj in page.get("Contents", []):
            remote[obj["Key"][len(prefix):]] = obj["ETag"].strip('"')
    res = {"local": len(local), "equal": [], "differ": [], "missing_on_s3": [], "extra_on_s3": [], "undetermined": [],
           "basis": {}, "worktree_cr": {}}
    for name in sorted(local):
        if name not in remote:
            res["missing_on_s3"].append(name)
        elif "-" in remote[name]:
            res["undetermined"].append(name)
        else:
            digest = _blob_md5(local[name])
            basis = "blob" if digest is not None else "worktree"
            if digest is None:
                digest = _md5_file(local[name])
            res["basis"][name] = basis
            if remote[name] == digest:
                res["equal"].append(name)
                if basis == "blob":
                    n = _cr_count(local[name])
                    if n > 0:
                        res["worktree_cr"][name] = n
            else:
                res["differ"].append(name)
    for name in sorted(remote):
        if name not in local:
            res["extra_on_s3"].append(name)
    for key in ("equal", "differ", "missing_on_s3", "extra_on_s3", "undetermined"):
        res[key].sort()
    return res


def _names(res):
    return res["equal"] + res["differ"] + res["missing_on_s3"] + res["extra_on_s3"] + res["undetermined"]


def _repo_dir(tree):
    return os.path.join(ROOT, *tree["home"].split("/"))


def _print_tree(tree, res):
    print("TREE %s -> s3://%s/%s | local %d | EQUAL %d | DIFFER %d | MISSING_ON_S3 %d | EXTRA_ON_S3 %d | UNDETERMINED %d"
          % (tree["home"], tree["bucket"], tree["prefix"], res["local"], len(res["equal"]), len(res["differ"]),
             len(res["missing_on_s3"]), len(res["extra_on_s3"]), len(res["undetermined"])))
    for key, label in CLASSES:
        for name in res[key]:
            print("  %s %s" % (label, _ascii(name)))


def _s3_client():
    import boto3
    return boto3.client("s3", region_name=REGION)


def _norm(path):
    rel = path.replace("\\", "/")
    while rel.startswith("./"):
        rel = rel[2:]
    return rel


def _owning_tree(trees, rel):
    best = None
    for t in trees:
        home = t["home"]
        if rel.startswith(home + "/") and (best is None or len(home) > len(best["home"])):
            best = t
    return best


def whole_tree(trees):
    try:
        s3 = _s3_client()
        results = [(t, compare_tree(_repo_dir(t), t["bucket"], t["prefix"], s3)) for t in trees]
    except Exception as exc:  # noqa: BLE001 -- a failed read must never read as equal
        print("REFUSED: S3 read failed (nothing compared): %s: %s" % (type(exc).__name__, _ascii(exc)))
        return 2
    files = equal = 0
    for t, res in results:
        _print_tree(t, res)
        files += len(_names(res))
        equal += len(res["equal"])
    print("MDPF-CODE-EQUALITY: trees %d | files %d | equal %d | not_equal %d"
          % (len(results), files, equal, files - equal))
    return 0


def named(trees, paths):
    rels = [_norm(p) for p in paths]
    owner = {rel: _owning_tree(trees, rel) for rel in rels}
    unmapped = [rel for rel in rels if owner[rel] is None]
    if unmapped:
        print("REFUSED: not under any runner code tree (nothing read): %s" % [_ascii(u) for u in unmapped])
        return 2
    shown = [t for t in trees if any(owner[rel] is t for rel in rels)]
    try:
        s3 = _s3_client()
        results = {id(t): compare_tree(_repo_dir(t), t["bucket"], t["prefix"], s3) for t in shown}
    except Exception as exc:  # noqa: BLE001 -- a failed read must never read as equal
        print("REFUSED: S3 read failed (nothing compared): %s: %s" % (type(exc).__name__, _ascii(exc)))
        return 2
    files = equal = 0
    for t in shown:
        _print_tree(t, results[id(t)])
        files += len(_names(results[id(t)]))
        equal += len(results[id(t)]["equal"])
    not_equal_named = 0
    for rel in rels:
        t = owner[rel]
        res = results[id(t)]
        inner = rel[len(t["home"]) + 1:]
        label = "ABSENT_BOTH"
        for key, cls in CLASSES:
            if inner in res[key]:
                label = cls
        if inner in res["equal"]:
            line = "NAMED EQUAL (%s) %s" % (res["basis"][inner], _ascii(rel))
            if inner in res["worktree_cr"]:
                line += " worktree_cr=%d" % res["worktree_cr"][inner]
            print(line)
        else:
            not_equal_named += 1
            print("NAMED NOT_EQUAL %s %s" % (label, _ascii(rel)))
    print("MDPF-CODE-EQUALITY: trees %d | files %d | equal %d | not_equal %d | named %d | named_not_equal %d"
          % (len(shown), files, equal, files - equal, len(rels), not_equal_named))
    return 0 if not_equal_named == 0 else 1


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--files", nargs="+", metavar="REPO_PATH",
                    help="Named files only: grade these repo-relative paths (exit 1 if any is not EQUAL).")
    a = ap.parse_args(argv)
    try:
        trees = runner_trees(load_core())
    except (ImportError, KeyError, ValueError) as exc:
        print("REFUSED: runner code trees unreadable (nothing compared): %s" % _ascii(exc))
        return 2
    if a.files is None:
        return whole_tree(trees)
    return named(trees, a.files)


if __name__ == "__main__":
    sys.exit(main())
