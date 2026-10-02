#!/usr/bin/env python3
"""Which package members the resident's runtime can load: a static import walk from its two entry modules.

    python resident_reachability.py <package-dir> [<member path> ...]

Starts at ycharts/generate/resident_main.py and reports/resident_installed.py and follows every `import`, `from ...
import`, `__import__("<name>")` and `import_module("<name>")` (function-level ones included) to a module the package
holds on the resident's sys.path. Prints the reachable module count and, per named member, REACHABLE or not. A dynamic
import whose name is not a literal is not followed. Read-only; ASCII only.
"""
import ast
import os
import sys

DIRS = ("ycharts/generate", "intake", "ops", "reports", "_keys", "_authz", "_gate", "ycharts/session",
        "ycharts/extract", "_scope", "_ids", "_contracts", "lib")
ENTRIES = ("ycharts/generate/resident_main.py", "reports/resident_installed.py")


def module_index(root):
    index = {}
    for directory in DIRS:
        path = os.path.join(root, directory)
        if os.path.isdir(path):
            for name in sorted(os.listdir(path)):
                if name.endswith(".py"):
                    index.setdefault(name[:-3], directory + "/" + name)
    return index


def imported_names(tree):
    found = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            found.extend(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module and not node.level:
            found.append(node.module.split(".")[0])
        elif isinstance(node, ast.Call) and (getattr(node.func, "id", None) == "__import__"
                                             or getattr(node.func, "attr", None) == "import_module"):
            if node.args and isinstance(node.args[0], ast.Constant) and isinstance(node.args[0].value, str):
                found.append(node.args[0].value.split(".")[0])
    return found


def reachable(root):
    index, seen, todo = module_index(root), set(), list(ENTRIES)
    while todo:
        rel = todo.pop()
        if rel in seen:
            continue
        seen.add(rel)
        with open(os.path.join(root, rel), encoding="utf-8") as handle:
            tree = ast.parse(handle.read())
        todo.extend(index[name] for name in imported_names(tree) if name in index)
    return seen


def main(argv):
    seen = reachable(argv[1])
    print("reachable modules:", len(seen))
    for member in argv[2:]:
        print(member, "REACHABLE" if member in seen else "not reachable")


if __name__ == "__main__":
    main(sys.argv)
