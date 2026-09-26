#!/usr/bin/env python3
"""Every import a Lambda package makes, resolved against what the RUNTIME will actually have: the zip itself, its
attached layers (`python/` of each layer zip), the python3.12 standard library, and boto3/botocore (shipped in the
Lambda python runtime). Third-party included -- the gap K5 hit (row: the offline closure walk saw first-party
modules only, and `composition_admission.py:11 import jsonschema` passed it).

    python package_import_check.py <function.zip> [--layer <layer.zip>]... [--layer-arn <arn>]...
        [--path <dir inside the zip the code puts on sys.path>]... [--allow <module>=<reason>]...

Exit 0 when every absolute import in every packaged .py resolves; exit 1 naming each unresolved top-level module and
the files (and whether at module level) that import it. `--layer-arn` downloads that layer version's content.
AST only: nothing is imported or executed.
"""
from __future__ import annotations

import argparse
import ast
import io
import sys
import urllib.request
import zipfile

RUNTIME_EXTRA = {"boto3", "botocore", "s3transfer", "jmespath", "dateutil", "urllib3", "six", "awslambdaric"}


def top_names(zf, prefix=""):
    names = set()
    for n in zf.namelist():
        if not n.startswith(prefix):
            continue
        rel = n[len(prefix):]
        if not rel or rel.startswith("__pycache__"):
            continue
        head = rel.split("/", 1)[0]
        if "/" in rel:
            names.add(head)
        elif head.endswith(".py"):
            names.add(head[:-3])
        elif head.endswith((".so", ".pyd")):
            names.add(head.split(".", 1)[0])
    return names


def layer_zip(args):
    zips = [zipfile.ZipFile(p) for p in args.layer]
    if args.layer_arn:
        import boto3
        lam = boto3.client("lambda")
        for arn in args.layer_arn:
            loc = lam.get_layer_version_by_arn(Arn=arn)["Content"]["Location"]
            zips.append(zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(loc).read())))
    return zips


def imports_of(source):
    tree = ast.parse(source)
    module_level = {id(n) for n in tree.body}
    found = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for a in node.names:
                found.append((a.name.split(".")[0], id(node) in module_level))
        elif isinstance(node, ast.ImportFrom) and node.level == 0 and node.module:
            found.append((node.module.split(".")[0], id(node) in module_level))
    return found


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("zip")
    ap.add_argument("--layer", action="append", default=[])
    ap.add_argument("--layer-arn", action="append", default=[])
    ap.add_argument("--path", action="append", default=[],
                    help="a zip subdirectory the package itself inserts on sys.path (e.g. lib)")
    ap.add_argument("--allow", action="append", default=[],
                    help="module=reason: a NESTED import known absent by design; a module-level one is never allowed")
    args = ap.parse_args(argv)
    fn = zipfile.ZipFile(args.zip)
    available = top_names(fn) | set(sys.stdlib_module_names) | RUNTIME_EXTRA
    for sub in args.path:
        available |= top_names(fn, sub.rstrip("/") + "/")
    allowed = dict(a.split("=", 1) for a in args.allow)
    for lz in layer_zip(args):
        available |= top_names(lz, "python/")
    unresolved = {}
    files = 0
    for name in sorted(n for n in fn.namelist() if n.endswith(".py") and "__pycache__" not in n):
        files += 1
        try:
            found = imports_of(fn.read(name).decode("utf-8"))
        except SyntaxError as exc:
            unresolved.setdefault("<syntax>", []).append("%s (%s)" % (name, exc))
            continue
        for mod, at_module_level in found:
            if mod not in available:
                unresolved.setdefault(mod, []).append("%s%s" % (name, " [module level]" if at_module_level else ""))
    print("checked %d .py files; available top-level names %d (zip + %d layer(s) + stdlib + runtime)"
          % (files, len(available), len(args.layer) + len(args.layer_arn)))
    failing = 0
    for mod in sorted(unresolved):
        sites = sorted(set(unresolved[mod]))
        module_level = any(s.endswith("[module level]") for s in sites)
        if mod in allowed and not module_level:
            print("ALLOWED %s (%s) <- %s" % (mod, allowed[mod], ", ".join(sites)))
        else:
            failing += 1
            print("UNRESOLVED %s <- %s" % (mod, ", ".join(sites)))
    if failing:
        return 1
    print("OK: every absolute import resolves (%d allowed nested import(s) named above)" % (len(unresolved)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
