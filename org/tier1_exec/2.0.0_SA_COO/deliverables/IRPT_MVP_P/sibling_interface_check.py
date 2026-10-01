#!/usr/bin/env python3
"""Do the bundled modules accept the calls their bundled siblings make? (the IB-pr-275 defect, as a gate)

    python sibling_interface_check.py <built zip | extracted bundle dir> [--root served.py]

A flat Lambda zip can carry modules of different vintages. `served.py` at one commit called
`enforce.Request(..., path_ids=...)` and `errors.public_line(..., admitted=...)`; three bundles carried an
`enforce.py` and an `errors.py` from before those keywords existed, and every request past the firm checks would
have raised TypeError. A member list cannot show that, and neither can a cold import.

For every bundled top-level module reachable from --root through imports (any depth, function-level included),
each call written `alias.name(...)` or `name(...)` where the target is a function or class DEFINED in another
bundled module is checked against that definition as bundled:
  - the name exists at module level in the bundled sibling;
  - every keyword the call passes is a parameter of the function (or of the class's `__init__`), unless the
    definition takes **kwargs;
  - the call does not pass more positional arguments than the definition admits, unless it takes *args.
Calls on objects (`enforcer.guard(...)`) are not resolved: this is a floor, and it says so in its last line.
rc 1 on any finding, rc 0 on none. Read-only.
"""
from __future__ import annotations

import ast
import os
import sys
import zipfile


class Bundle:
    def __init__(self, path):
        self.zip = zipfile.ZipFile(path) if os.path.isfile(path) else None
        self.dir = None if self.zip else path
        if self.zip:
            self.names = {n for n in self.zip.namelist() if "/" not in n}
        else:
            self.names = {n for n in os.listdir(path) if os.path.isfile(os.path.join(path, n))}

    def read(self, name):
        if self.zip:
            return self.zip.read(name)
        with open(os.path.join(self.dir, name), "rb") as fh:
            return fh.read()


def _defs(tree):
    """module-level name -> (params, has_varargs, has_kwargs, max_positional) for functions and classes."""
    out = {}
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            out[node.name] = _sig(node, drop_self=False)
        elif isinstance(node, ast.ClassDef):
            init = next((n for n in node.body if isinstance(n, ast.FunctionDef) and n.name == "__init__"), None)
            # A class with its OWN __init__ is checked against it, whatever its bases. A class with no own
            # __init__ inherits one this check cannot see: accept anything.
            out[node.name] = _sig(init, drop_self=True) if init is not None else None
        elif isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    out.setdefault(target.id, None)
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            for alias in node.names:
                out.setdefault((alias.asname or alias.name).split(".")[0], None)
    return out


def _sig(fn, drop_self):
    a = fn.args
    positional = [x.arg for x in a.posonlyargs + a.args]
    if drop_self and positional:
        positional = positional[1:]
    return (set(positional) | {x.arg for x in a.kwonlyargs}, a.vararg is not None, a.kwarg is not None, len(positional))


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if not argv:
        print(__doc__)
        return 2
    root = "served.py"
    if "--root" in argv:
        root = argv[argv.index("--root") + 1]
    bundle = Bundle(argv[0])
    if root not in bundle.names:
        print("ERROR: %s is not a top-level member of %s" % (root, argv[0]))
        return 2

    trees, queue, order = {}, [root], []
    while queue:
        name = queue.pop(0)
        if name in trees:
            continue
        try:
            trees[name] = ast.parse(bundle.read(name).decode("utf-8"))
        except (SyntaxError, UnicodeDecodeError) as exc:
            print("ERROR: %s does not parse: %s" % (name, exc))
            return 1
        order.append(name)
        for node in ast.walk(trees[name]):
            mods = []
            if isinstance(node, ast.Import):
                mods = [a.name.split(".")[0] for a in node.names]
            elif isinstance(node, ast.ImportFrom) and node.module and node.level == 0:
                mods = [node.module.split(".")[0]]
            for mod in mods:
                if mod + ".py" in bundle.names:
                    queue.append(mod + ".py")
    defs = {name: _defs(tree) for name, tree in trees.items()}

    findings, checked = [], 0
    for name in order:
        tree = trees[name]
        alias_mod, from_names = {}, {}
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for a in node.names:
                    mod = a.name.split(".")[0]
                    if mod + ".py" in trees:
                        alias_mod[a.asname or mod] = mod + ".py"
            elif isinstance(node, ast.ImportFrom) and node.module and node.level == 0:
                mod = node.module.split(".")[0] + ".py"
                if mod in trees:
                    for a in node.names:
                        from_names[a.asname or a.name] = (mod, a.name)
                        if a.name != "*" and a.name not in defs[mod]:
                            findings.append("%s: from %s import %s -- no such module-level name in the bundled %s"
                                            % (name, mod[:-3], a.name, mod))
        for node in ast.walk(tree):
            target = None
            if isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name) and node.value.id in alias_mod:
                mod = alias_mod[node.value.id]
                if node.attr not in defs[mod]:
                    findings.append("%s:%d: %s.%s -- no such module-level name in the bundled %s"
                                    % (name, node.lineno, node.value.id, node.attr, mod))
            if not isinstance(node, ast.Call):
                continue
            if isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Name) and node.func.value.id in alias_mod:
                target = (alias_mod[node.func.value.id], node.func.attr)
            elif isinstance(node.func, ast.Name) and node.func.id in from_names:
                target = from_names[node.func.id]
            if target is None:
                continue
            mod, attr = target
            sig = defs[mod].get(attr)
            checked += 1
            if sig is None:
                continue
            params, has_varargs, has_kwargs, max_pos = sig
            passed_kw = [k.arg for k in node.keywords if k.arg]
            unknown = [k for k in passed_kw if k not in params and not has_kwargs]
            if unknown:
                findings.append("%s:%d: %s.%s(...) passes keyword(s) %s the bundled %s does not accept (it takes %s)"
                                % (name, node.lineno, mod[:-3], attr, unknown, mod, sorted(params)))
            n_pos = len([x for x in node.args if not isinstance(x, ast.Starred)])
            if not has_varargs and n_pos > max_pos:
                findings.append("%s:%d: %s.%s(...) passes %d positional argument(s); the bundled %s admits %d"
                                % (name, node.lineno, mod[:-3], attr, n_pos, mod, max_pos))

    print("%s: %d bundled module(s) reachable from %s; %d cross-module call(s) checked" % (argv[0], len(order), root, checked))
    for f in findings:
        print("  FINDING %s" % f)
    print("findings: %d (a floor: calls on objects and inherited constructors are not resolved)" % len(findings))
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
