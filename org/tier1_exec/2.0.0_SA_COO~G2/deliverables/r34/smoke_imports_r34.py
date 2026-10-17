"""Package-layout import smoke for a BUILT resident tree (issuer 2.0.0_SA_COO~G2; CTO msg 10172 ruling 2).

usage: python -I smoke_imports_r34.py <built tree root> <path to r32_reachability.py>

Sets sys.path the way the service does and imports EVERY module the static reachability walk marks LIVE, by its module name, in this one
interpreter (run it with -I so neither the cwd, PYTHONPATH nor a site .pth supplies a directory the service does not have). The service's path is:
the directory of ycharts/generate/resident_main.py (the script directory), then the entries of resident_main's own `for _relative in (...)` tuple read from the built tree
(each inserted at the front when it is a directory, as resident_main does), then ycharts/research appended (resident_worker.load_opal_producer appends it at run time). The walk's own
model of the path (r32_reachability.DIRS) is NOT used: it counts `lib` as on the path, which is exactly what r34j's V2 found false.

A LIVE module that raises ModuleNotFoundError for a name the package itself holds is a FAILURE (the package is not importable in the service); a name the package does not hold is a NOTE
(a third-party library absent on this box); any other exception on import is a FAILURE. Prints `SMOKE live=<n> imported=<n> fail=<n> note=<n>` and one line per failure or note; rc 1 on any failure.
ASCII only. Reads the tree; writes nothing.
"""
import ast
import importlib
import importlib.util
import os
import sys

sys.dont_write_bytecode = True  # the smoke reads the built tree and writes nothing into it (no __pycache__ members)


def path_tuple(text):
    for node in ast.walk(ast.parse(text)):
        if isinstance(node, ast.For) and getattr(node.target, "id", "") == "_relative" and isinstance(node.iter, (ast.Tuple, ast.List)):
            return [e.value for e in node.iter.elts]
    raise SystemExit("SMOKE-BAD no `for _relative in (...)` tuple in resident_main.py")


def main(argv):
    root, reach_path = os.path.abspath(argv[1]), argv[2]
    main_path = os.path.join(root, "ycharts", "generate", "resident_main.py")
    rels = path_tuple(open(main_path, encoding="utf-8").read())
    sys.path.insert(0, os.path.dirname(main_path))
    for rel in rels:
        directory = os.path.join(root, *rel.split("/"))
        if os.path.isdir(directory):
            sys.path.insert(0, directory)
    research = os.path.join(root, "ycharts", "research")
    if os.path.isdir(research):
        sys.path.append(research)
    spec = importlib.util.spec_from_file_location("r32_reachability", reach_path)
    reach = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(reach)
    live = sorted(reach.reachable(root))
    held = set()
    for directory in reach.DIRS:
        path = os.path.join(root, *directory.split("/"))
        if os.path.isdir(path):
            held.update(name[:-3] for name in os.listdir(path) if name.endswith(".py"))
    imported, fails, notes = 0, [], []
    for rel in live:
        name = os.path.basename(rel)[:-3]
        try:
            importlib.import_module(name)
            imported += 1
        except ModuleNotFoundError as exc:
            top = (exc.name or "").split(".")[0]
            if top in held:
                fails.append("%s: ModuleNotFoundError %s (the package holds it, the service path does not reach it)" % (rel, exc.name))
            else:
                notes.append("%s: %s is not a package module and is absent on this box" % (rel, top))
        except BaseException as exc:  # a smoke prints whatever an import raises
            fails.append("%s: %s.%s %s" % (rel, type(exc).__module__, type(exc).__name__, str(exc)[:100].replace("\n", " ")))
    print("SMOKE live=%d imported=%d fail=%d note=%d" % (len(live), imported, len(fails), len(notes)))
    for line in fails:
        print("SMOKE FAIL " + line)
    for line in notes:
        print("SMOKE NOTE " + line)
    return 1 if fails else 0


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("usage: python -I smoke_imports_r34.py <built tree root> <path to r32_reachability.py>")
    sys.exit(main(sys.argv))
