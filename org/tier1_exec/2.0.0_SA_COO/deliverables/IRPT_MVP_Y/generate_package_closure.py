"""Import-closure check of a built irpt-ycharts-generate zip against the source tree.

Walks every import (module-level and lazy, via the AST) reachable from the package's entry module and reports each
FIRST-PARTY module (a .py basename under infra/aws/lambda/investor-reporting, tests excluded) that the zip does not
carry. Exit 0 = nothing missing; exit 1 = missing modules printed. Read-only; no AWS call.

    python generate_package_closure.py <zip> [--tree <investor-reporting dir>] [--entry generate_installed]

Found necessary on 2026-09-26: the deployed zip LdjdnnLh lacked interactive_access, template_reader and
security_resolution, and the first live upload failed on the first of them (corr-32b49d41af2a).
"""
import argparse
import ast
import os
import sys
import zipfile


def imports(source):
    names = set()
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return names
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module and node.level == 0:
            names.add(node.module.split(".")[0])
    return names


def first_party(tree_dir):
    found = {}
    for dirpath, dirnames, filenames in os.walk(tree_dir):
        parts = set(os.path.normpath(dirpath).split(os.sep))
        if "tests" in parts or "__pycache__" in parts:
            continue
        for name in filenames:
            if name.endswith(".py"):
                found.setdefault(name[:-3], os.path.join(dirpath, name))
    return found


def missing_modules(zip_path, tree_dir, entry):
    archive = zipfile.ZipFile(zip_path)
    packaged = {n.rsplit("/", 1)[-1][:-3]: n for n in archive.namelist() if n.endswith(".py")}
    tree = first_party(tree_dir)
    if entry not in packaged:
        raise SystemExit("ERROR: entry module %r is not in the zip" % entry)
    seen, stack, missing = set(), [entry], {}
    while stack:
        module = stack.pop()
        if module in seen:
            continue
        seen.add(module)
        if module in packaged:
            source = archive.read(packaged[module]).decode("utf-8", "replace")
        elif module in tree:
            source = open(tree[module], encoding="utf-8").read()  # follow a missing module's own imports too
        else:
            continue
        for name in imports(source):
            if name in tree or name in packaged:
                if name not in packaged:
                    missing.setdefault(name, set()).add(module)
                stack.append(name)
    return seen, packaged, tree, missing


def main(argv=None):
    here = os.path.dirname(os.path.abspath(__file__))
    default_tree = os.path.normpath(os.path.join(here, "..", "..", "..", "..", "..",
                                                 "infra", "aws", "lambda", "investor-reporting"))
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("zip")
    parser.add_argument("--tree", default=default_tree)
    parser.add_argument("--entry", default="generate_installed")
    args = parser.parse_args(argv)
    seen, packaged, tree, missing = missing_modules(args.zip, args.tree, args.entry)
    print("closure %d modules | packaged .py %d | first-party in tree %d | tree %s"
          % (len(seen), len(packaged), len(tree), args.tree))
    if not missing:
        print("OK: no first-party module in the closure is missing from the zip")
        return 0
    for name, importers in sorted(missing.items()):
        print("MISSING %s <- imported by %s | source %s" % (name, ", ".join(sorted(importers)), tree.get(name)))
    return 1


if __name__ == "__main__":
    sys.exit(main())
