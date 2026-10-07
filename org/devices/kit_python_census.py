"""kit_python_census.py -- the Python kit's census (NFRA_CTLPLN PRD v0.14 C-KIT-PYTHON, cell CT-k-2).

What the shared tool directories import, what a box has installed, and the gap between the two. Pure stdlib: it runs on a Dell that has
nothing but its interpreter. No network, no package index, no install.

    python org/devices/kit_python_census.py required [--out <json>]      # the laptop's read: walk tracked .py under .tools/ and lib/
    AGENTBUS_DEVICE=<d> python org/devices/kit_python_census.py installed [--out <json>] [--required <json>]   # what a box runs
    python org/devices/kit_python_census.py compare <installed.json> [--required <json>]

`required` parses every tracked .py under .tools/ and lib/ with ast (a file that does not parse is UNPARSED, counted, and fails ok),
classifies each top-level imported module STDLIB / LOCAL / THIRD-PARTY, and for each third-party module records the distribution that
provides it HERE (importlib.metadata.packages_distributions), its version here, and whether the import is HARD (module level, not
inside a try that handles ImportError) or OPTIONAL (inside such a try, or inside a function). It is a STATIC read: an
importlib.import_module("x") call or a string-built import is not seen. `ruff` is a command-line tool the commit gate runs, not an
import: it is added as a required distribution with kind=tool.

Distribution names are PEP 503 normalised (lowercase, runs of - _ . collapsed to -). The committed result is
org/devices/kit_python_required.json (names and versions only).
"""
from __future__ import annotations

import argparse
import ast
import collections
import importlib.metadata as md
import json
import os
import pathlib
import platform
import re
import subprocess
import sys
import sysconfig

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
REQUIRED_PATH = HERE / "kit_python_required.json"
SCAN_PATHSPECS = (".tools/*.py", "lib/*.py")
TOOLS = ("ruff",)  # command-line tools the commit gate runs; not imports
IMPORT_ERRORS = {"ImportError", "ModuleNotFoundError", "Exception", "BaseException"}


def norm(name):
    return re.sub(r"[-_.]+", "-", name).lower()


# ---------------------------------------------------------------- the box's own facts


def wheel_platform():
    return sysconfig.get_platform().replace("-", "_").replace(".", "_")


def box_facts():
    v = sys.version_info
    return {
        "python_version": "%d.%d.%d" % (v[0], v[1], v[2]),
        "python_minor": "%d.%d" % (v[0], v[1]),
        "implementation": sys.implementation.name,
        "platform_tag": wheel_platform(),
        "sys_platform": sys.platform,
        "machine": platform.machine(),
    }


def installed_map():
    """{normalised distribution name: version} for EVERY distribution this interpreter can see."""
    out = {}
    for d in md.distributions():
        name = d.metadata["Name"]
        if name:
            out.setdefault(norm(name), d.version)
    return out


# ---------------------------------------------------------------- the import walk


def _handles_import_error(node):
    for h in node.handlers:
        if h.type is None:
            return True
        elts = h.type.elts if isinstance(h.type, ast.Tuple) else [h.type]
        for e in elts:
            n = e.attr if isinstance(e, ast.Attribute) else getattr(e, "id", "")
            if n in IMPORT_ERRORS:
                return True
    return False


def _walk(node, optional, found):
    """Collect (top-level module or None for relative, is_optional) from `node`, tracking try/function context."""
    for child in ast.iter_child_nodes(node):
        if isinstance(child, ast.Import):
            for a in child.names:
                found.append((a.name.split(".")[0], optional))
        elif isinstance(child, ast.ImportFrom):
            if child.level:
                found.append((None, optional))
            elif child.module:
                found.append((child.module.split(".")[0], optional))
        elif isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda)):
            _walk(child, True, found)
        elif isinstance(child, ast.Try) or child.__class__.__name__ == "TryStar":
            body_opt = optional or _handles_import_error(child)
            for stmt in child.body:
                _walk_stmt(stmt, body_opt, found)
            for part in (child.handlers, child.orelse, child.finalbody):
                for stmt in part:
                    _walk_stmt(stmt, optional, found)
        else:
            _walk(child, optional, found)


def _walk_stmt(stmt, optional, found):
    holder = ast.Module(body=[stmt], type_ignores=[])
    _walk(holder, optional, found)


def tracked_files(root):
    r = subprocess.run(["git", "-C", str(root), "ls-files", "--"] + list(SCAN_PATHSPECS),
                       capture_output=True, text=True, check=False)
    if r.returncode != 0:
        raise SystemExit("ERROR: git ls-files rc=%d: %s" % (r.returncode, r.stderr.strip()))
    return sorted(set(x for x in r.stdout.splitlines() if x.endswith(".py")))


def repo_local_roots(root):
    """Top-level names importable from inside the repo: root dirs and root .py stems, plus the stems/dirs of .tools/ and lib/."""
    names = set()
    r = subprocess.run(["git", "-C", str(root), "ls-files"], capture_output=True, text=True, check=False)
    for line in r.stdout.splitlines():
        parts = line.split("/")
        if len(parts) == 1:
            if parts[0].endswith(".py"):
                names.add(parts[0][:-3])
        else:
            names.add(parts[0])
    for sub in (".tools", "lib"):
        d = root / sub
        if d.is_dir():
            for p in d.iterdir():
                if p.suffix == ".py":
                    names.add(p.stem)
                elif p.is_dir():
                    names.add(p.name)
    return names


def repo_wide_names(root):
    """Every module/package name a tracked .py file or a directory holding one could answer to, anywhere in the repo."""
    names = set()
    r = subprocess.run(["git", "-C", str(root), "ls-files"], capture_output=True, text=True, check=False)
    for line in r.stdout.splitlines():
        if not line.endswith(".py"):
            continue
        parts = line.split("/")
        names.add(parts[-1][:-3])
        names.update(parts[:-1])
    return names


def beside_names(path, cache):
    d = path.parent
    if d not in cache:
        s = set()
        if d.is_dir():
            for p in d.iterdir():
                if p.suffix == ".py":
                    s.add(p.stem)
                elif p.is_dir():
                    s.add(p.name)
        cache[d] = s
    return cache[d]


def census_required(root=ROOT):
    files = tracked_files(root)
    local_roots = repo_local_roots(root)
    wide = repo_wide_names(root)
    cache = {}
    stdlib = set(sys.stdlib_module_names)
    unparsed = []
    relative = 0
    # module -> {"hard": set(files), "optional": set(files)}
    seen = collections.defaultdict(lambda: {"hard": set(), "optional": set()})
    for rel in files:
        p = root / rel
        try:
            tree = ast.parse(p.read_bytes(), filename=rel)
        except (SyntaxError, ValueError, OSError, RecursionError, MemoryError) as e:
            unparsed.append("%s: %s" % (rel, type(e).__name__))
            continue
        found = []
        _walk(tree, False, found)
        for mod, opt in found:
            if mod is None:
                relative += 1
                continue
            seen[mod]["optional" if opt else "hard"].add(rel)
    pd = md.packages_distributions()
    inst = installed_map()
    modules = []
    cls = collections.Counter()
    for mod in sorted(seen):
        info = seen[mod]
        importers = sorted(info["hard"] | info["optional"])
        local_via = None
        if mod in stdlib:
            klass = "STDLIB"
        elif mod in local_roots or any(mod in beside_names(root / f, cache) for f in importers):
            klass = "LOCAL"
            local_via = "path-root-or-beside"
        elif mod not in pd and mod in wide:
            klass = "LOCAL"
            local_via = "repo-wide-name"
        else:
            klass = "THIRD-PARTY"
        cls[klass] += 1
        row = {"module": mod, "class": klass, "importers": len(importers),
               "hard_importers": len(info["hard"]), "optional_importers": len(info["optional"])}
        if klass == "THIRD-PARTY":
            dists = sorted(set(norm(x) for x in pd.get(mod, [])))
            row["usage"] = "HARD" if info["hard"] else "OPTIONAL"
            row["distribution"] = dists[0] if dists else None
            row["other_distributions"] = dists[1:]
            row["version_here"] = inst.get(dists[0]) if dists else None
            row["status_here"] = "INSTALLED" if dists else "NOT-INSTALLED-HERE"
        if local_via:
            row["local_via"] = local_via
            row["shadows_installed_distribution"] = mod in pd
        modules.append(row)
    return {"files": len(files), "unparsed": unparsed, "relative_imports": relative, "modules": modules, "classes": dict(cls)}


def build_required(root=ROOT):
    c = census_required(root)
    third = [m for m in c["modules"] if m["class"] == "THIRD-PARTY"]
    inst = installed_map()
    dists = {}
    for m in third:
        if m["distribution"] is None:
            continue
        d = dists.setdefault(m["distribution"], {"distribution": m["distribution"], "version_here": m["version_here"],
                                                 "kind": "import", "usage": "OPTIONAL", "modules": []})
        d["modules"].append(m["module"])
        if m["usage"] == "HARD":
            d["usage"] = "HARD"
    for t in TOOLS:
        dists[t] = {"distribution": t, "version_here": inst.get(t), "kind": "tool", "usage": "TOOL", "modules": []}
    not_installed = [{"module": m["module"], "usage": m["usage"], "importers": m["importers"]}
                     for m in third if m["distribution"] is None]
    doc = {
        "schema": "kit_python_required/1",
        "claim": "measured: static ast read of tracked .py under .tools/ and lib/; versions are those installed on the box that ran it",
        "scan": {"pathspecs": list(SCAN_PATHSPECS), "files": c["files"], "unparsed": c["unparsed"],
                 "relative_imports": c["relative_imports"]},
        "read_on": {"python_version": box_facts()["python_version"], "platform_tag": wheel_platform()},
        "counts": {"modules": len(c["modules"]), "stdlib": c["classes"].get("STDLIB", 0), "local": c["classes"].get("LOCAL", 0),
                   "third_party": len(third), "distributions": len(dists), "not_installed_here": len(not_installed)},
        "modules": third,
        "distributions": [dists[k] for k in sorted(dists)],
        "not_installed_modules": not_installed,
    }
    return doc


def last_line_required(doc):
    n = doc["counts"]
    u = len(doc["scan"]["unparsed"])
    return ("KIT-REQUIRED files=%d unparsed=%d modules=%d stdlib=%d local=%d third_party=%d distributions=%d "
            "not_installed_here=%d ok=%s" % (doc["scan"]["files"], u, n["modules"], n["stdlib"], n["local"], n["third_party"],
                                             n["distributions"], n["not_installed_here"], u == 0))


def cmd_required(args):
    doc = build_required()
    out = pathlib.Path(args.out) if args.out else REQUIRED_PATH
    out.write_text(json.dumps(doc, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print("files scanned: %d  unparsed: %d  relative imports (LOCAL, no name): %d"
          % (doc["scan"]["files"], len(doc["scan"]["unparsed"]), doc["scan"]["relative_imports"]))
    for u in doc["scan"]["unparsed"]:
        print("UNPARSED %s" % u)
    print("classes: STDLIB=%d LOCAL=%d THIRD-PARTY=%d" % (doc["counts"]["stdlib"], doc["counts"]["local"], doc["counts"]["third_party"]))
    for m in sorted(doc["modules"], key=lambda r: (-r["importers"], r["module"])):
        print("THIRD-PARTY %-28s dist=%-28s ver=%-12s %-8s importers=%d (hard=%d optional=%d)%s"
              % (m["module"], m["distribution"] or "-", m["version_here"] or "-", m["usage"], m["importers"], m["hard_importers"],
                 m["optional_importers"], "" if m["distribution"] else "  NOT-INSTALLED-HERE"))
    for d in doc["distributions"]:
        if d["kind"] == "tool":
            print("TOOL        %-28s ver=%s" % (d["distribution"], d["version_here"] or "NOT-INSTALLED-HERE"))
    print("wrote %s" % out)
    line = last_line_required(doc)
    print(line)
    return 0 if line.endswith("ok=True") else 1


# ---------------------------------------------------------------- installed / compare


def load_required(path=None):
    p = pathlib.Path(path) if path else REQUIRED_PATH
    return json.loads(p.read_text(encoding="utf-8"))


def cmd_installed(args):
    device = os.environ.get("AGENTBUS_DEVICE", "").strip()
    if not device:
        print("REFUSED: AGENTBUS_DEVICE is unset; this box's name is never derived. Set it and re-run.")
        return 2
    req = load_required(args.required)
    inst = installed_map()
    facts = box_facts()
    dists = {}
    for d in req["distributions"]:
        dists[d["distribution"]] = inst.get(d["distribution"])
    import importlib.util
    modules = {}
    for m in req.get("not_installed_modules", []):
        try:
            modules[m["module"]] = importlib.util.find_spec(m["module"]) is not None
        except (ImportError, ValueError):
            modules[m["module"]] = False
    doc = {"schema": "kit_python_installed/1", "device": device, **facts, "distributions": dists,
           "modules_importable": modules, "all_installed": inst}
    text = json.dumps(doc, indent=2, sort_keys=True) + "\n"
    if args.out:
        pathlib.Path(args.out).write_text(text, encoding="utf-8", newline="\n")
        print("wrote %s" % args.out)
    present = sum(1 for v in dists.values() if v)
    print("INSTALLED device=%s python=%s platform=%s required=%d present=%d absent=%d total_distributions_seen=%d"
          % (device, facts["python_version"], facts["platform_tag"], len(dists), present, len(dists) - present, len(inst)))
    if not args.out:
        print(json.dumps({k: v for k, v in doc.items() if k != "all_installed"}, indent=2, sort_keys=True))
    return 0


def compare(installed, req):
    rows = []
    for d in req["distributions"]:
        have = installed["distributions"].get(d["distribution"])
        hard = d["usage"] in ("HARD", "TOOL")
        if not have:
            st = "MISSING"
        elif d.get("version_here") and have != d["version_here"]:
            st = "VERSION-DIFFERS"
        else:
            st = "PRESENT"
        rows.append({"distribution": d["distribution"], "kind": d["kind"], "usage": d["usage"], "hard": hard, "status": st,
                     "required_version": d.get("version_here"), "installed_version": have})
    for m in req.get("not_installed_modules", []):
        ok = installed.get("modules_importable", {}).get(m["module"])
        rows.append({"distribution": "module:" + m["module"], "kind": "import", "usage": m["usage"], "hard": m["usage"] == "HARD",
                     "status": "PRESENT" if ok else "MISSING", "required_version": None, "installed_version": None})
    return rows


def cmd_compare(args):
    installed = json.loads(pathlib.Path(args.installed).read_text(encoding="utf-8"))
    req = load_required(args.required)
    rows = compare(installed, req)
    for r in rows:
        extra = ""
        if r["status"] == "VERSION-DIFFERS":
            extra = "  laptop=%s here=%s (reported, not failed)" % (r["required_version"], r["installed_version"])
        print("%-16s %-30s %-8s%s" % (r["status"], r["distribution"], r["usage"], extra))
    cnt = collections.Counter(r["status"] for r in rows)
    hard_missing = sum(1 for r in rows if r["status"] == "MISSING" and r["hard"])
    line = ("KIT-COMPARE device=%s python=%s required=%d present=%d missing=%d version_differs=%d hard_missing=%d ok=%s"
            % (installed.get("device"), installed.get("python_version"), len(rows),
               cnt["PRESENT"] + cnt["VERSION-DIFFERS"], cnt["MISSING"], cnt["VERSION-DIFFERS"], hard_missing, cnt["MISSING"] == 0))
    print(line)
    return 0 if line.endswith("ok=True") else 1


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("required")
    a.add_argument("--out")
    a.set_defaults(fn=cmd_required)
    b = sub.add_parser("installed")
    b.add_argument("--out")
    b.add_argument("--required")
    b.set_defaults(fn=cmd_installed)
    c = sub.add_parser("compare")
    c.add_argument("installed")
    c.add_argument("--required")
    c.set_defaults(fn=cmd_compare)
    args = ap.parse_args(argv)
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
