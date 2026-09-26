"""Import-closure check of a built irpt-ycharts-generate zip against the source tree.

Walks every import (module-level and lazy, via the AST) reachable from the package's entry module and reports:
- each FIRST-PARTY module (a .py basename under infra/aws/lambda/investor-reporting, tests excluded) that the zip does
  not carry;
- each THIRD-PARTY top-level package imported by a module in the closure that is neither in the zip (as a flat module
  or a top-level directory), nor in the standard library, nor in RUNTIME_PROVIDED. Each carries its level: MODULE
  (runs at import), LAZY (runs when the function is called), or GUARDED (inside a try that catches ImportError; a WARN,
  not a failure).
Exit 0 = nothing missing; exit 1 = a first-party module, or a MODULE/LAZY third-party import, is missing. Read-only; no
AWS call.

Limit: a third-party package is checked for presence only. Its own dependencies (for jsonschema: attrs, referencing,
rpds, jsonschema_specifications) and its compiled wheels' platform are not walked. The check for those is an import of
every module on the deployed function (CTO 101230 condition 3).

    python generate_package_closure.py <zip> [--tree <investor-reporting dir>] [--entry generate_installed]

Found necessary on 2026-09-26:
- the deployed zip LdjdnnLh lacked interactive_access, template_reader and security_resolution, and the first live
  upload failed on the first of them (corr-32b49d41af2a);
- the next zip IJD6bd1I passed the first-party check but lacked jsonschema, which composition_admission imports at
  module level, and the first live /analysis POST failed on it (corr-8c5e097ea21e).
"""
import argparse
import ast
import os
import sys
import zipfile

# Held, not measured: the AWS Lambda python3.12 managed runtime ships the AWS SDK and its dependencies.
RUNTIME_PROVIDED = frozenset({"boto3", "botocore", "s3transfer", "jmespath", "dateutil", "urllib3", "six",
                              "awslambdaric"})
IMPORT_ERRORS = frozenset({"ImportError", "ModuleNotFoundError", "Exception", "BaseException"})


def _guarded(handlers):
    for handler in handlers:
        kinds = handler.type.elts if isinstance(handler.type, ast.Tuple) else [handler.type]
        if handler.type is None or any(isinstance(k, ast.Name) and k.id in IMPORT_ERRORS for k in kinds):
            return True
    return False


def leveled_imports(source):
    """{top-level name: level}, the strictest level wins (MODULE > LAZY > GUARDED)."""
    found = {}
    rank = {"GUARDED": 0, "LAZY": 1, "MODULE": 2}
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return found

    def note(name, level):
        if rank[level] > rank.get(found.get(name), -1):
            found[name] = level

    def visit(node, in_function, guarded):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda)):
            in_function = True
        if isinstance(node, ast.Try):
            for child in node.body:
                visit(child, in_function, guarded or _guarded(node.handlers))
            for child in node.handlers + node.orelse + node.finalbody:
                visit(child, in_function, guarded)
            return
        names = []
        if isinstance(node, ast.Import):
            names = [alias.name.split(".")[0] for alias in node.names]
        elif isinstance(node, ast.ImportFrom) and node.module and node.level == 0:
            names = [node.module.split(".")[0]]
        for name in names:
            note(name, "GUARDED" if guarded else ("LAZY" if in_function else "MODULE"))
        for child in ast.iter_child_nodes(node):
            visit(child, in_function, guarded)

    visit(tree, False, False)
    return found


def imports(source):
    return set(leveled_imports(source))


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
    top_dirs = {n.split("/", 1)[0] for n in archive.namelist() if "/" in n}
    tree = first_party(tree_dir)
    if entry not in packaged:
        raise SystemExit("ERROR: entry module %r is not in the zip" % entry)
    seen, stack, missing, third = set(), [entry], {}, {}
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
        for name, level in leveled_imports(source).items():
            if name in tree or name in packaged:
                if name not in packaged:
                    missing.setdefault(name, set()).add(module)
                stack.append(name)
            elif (name not in top_dirs and name not in sys.stdlib_module_names
                  and name not in RUNTIME_PROVIDED and name != "__future__"):
                third.setdefault(name, {}).setdefault(level, set()).add(module)
    return seen, packaged, tree, missing, third


def main(argv=None):
    here = os.path.dirname(os.path.abspath(__file__))
    default_tree = os.path.normpath(os.path.join(here, "..", "..", "..", "..", "..",
                                                 "infra", "aws", "lambda", "investor-reporting"))
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("zip")
    parser.add_argument("--tree", default=default_tree)
    parser.add_argument("--entry", default="generate_installed")
    args = parser.parse_args(argv)
    seen, packaged, tree, missing, third = missing_modules(args.zip, args.tree, args.entry)
    print("closure %d modules | packaged .py %d | first-party in tree %d | third-party names absent %d | tree %s"
          % (len(seen), len(packaged), len(tree), len(third), args.tree))
    for name, importers in sorted(missing.items()):
        print("MISSING %s <- imported by %s | source %s" % (name, ", ".join(sorted(importers)), tree.get(name)))
    failing = False
    for name, levels in sorted(third.items()):
        for level in ("MODULE", "LAZY", "GUARDED"):
            if level in levels:
                tag = "WARN" if level == "GUARDED" else "MISSING-THIRD-PARTY"
                failing = failing or level != "GUARDED"
                print("%s %s [%s] <- imported by %s" % (tag, name, level, ", ".join(sorted(levels[level]))))
    if not missing and not failing:
        print("OK: no first-party module and no unguarded third-party import in the closure is missing from the zip")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
