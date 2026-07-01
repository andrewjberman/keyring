"""
comp-symbols -- the intra-file SYMBOL-INVENTORY tool (NFRA_COMPROUTE Stage-1 #3).

Fronts the file symbol-table -- "what functions / classes / constants are defined in file X, and
WHERE". No comp-tool answered it: agents raw-grep large HOT files for their OWN symbols
(derive_runner.py, 90KB/heat 0.94, grepped for `def ingest_|def commit_to_iceberg|_PRODUCERS|
NODE_TYPE_LAYER`). comp-symbols is the INVENTORY (forward enumeration, needs a FILE) sibling to
comp-blast's DEPENDENCY view (reverse blast-radius, needs a NAME) -- distinct one-home node (CTO
ruling 013811Z: opposite directions + opposite inputs + distinct concern -> sibling, not a
`comp-blast symbols` subcommand). They COMPOSE: comp-symbols --grep ingest_ -> pick a fn -> comp-blast it.

Deterministic ast.parse -> FunctionDef/AsyncFunctionDef/ClassDef/module-Assign/Import + line numbers.
Read-only, no LLM, no execution. Language-agnostic SURFACE, parser-PLUGGABLE underneath (CTO note,
mirrors the COMPROUTE provider pattern): v1 ships the Python (ast) parser; .ts/.sh add a parser per
language behind the same surface + --json.

Usage:
    comp-symbols <file>                          # the symbol index (functions/classes/constants/imports + lines)
    comp-symbols <file> --grep <pattern>         # filter symbol names (regex, case-insensitive)
    comp-symbols <file> --kind func|class|const|import
    comp-symbols <file> --json

Author: 0.8.0_AE_CloudComp~E (NFRA_COMPROUTE Stage-1). 2026-07-01. Spec:
org/projects/NFRA_COMPLEARN/comp_symbols_spec_v1.md. CTO-ratified 013811Z (sibling, read-side).
"""

from __future__ import annotations

import argparse
import ast
import json
import os
import re
import sys

_WS = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))


def _resolve(path: str) -> str | None:
    for cand in (path, os.path.join(_WS, path)):
        if os.path.isfile(cand):
            return cand
    return None


def _sig(node) -> str:
    """A compact arg signature for a function node (ast.unparse on 3.9+; degrade gracefully)."""
    try:
        return ast.unparse(node.args)
    except Exception:  # noqa: BLE001 -- signature is cosmetic; never fail the index over it
        return ", ".join(a.arg for a in getattr(node.args, "args", []))


# --------------------------------------------------------------------------------------------
def parse_python(text: str) -> dict:
    """ast.parse a Python source -> {functions, classes, constants, imports}. Each symbol carries
    its 1-based line number (the deterministic-parse proof)."""
    tree = ast.parse(text)
    functions: list[dict] = []
    classes: list[dict] = []
    constants: list[dict] = []
    imports: list[dict] = []
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            functions.append({"name": node.name, "line": node.lineno,
                              "sig": _sig(node), "async": isinstance(node, ast.AsyncFunctionDef)})
        elif isinstance(node, ast.ClassDef):
            methods = [{"name": b.name, "line": b.lineno, "sig": _sig(b),
                        "async": isinstance(b, ast.AsyncFunctionDef)}
                       for b in node.body if isinstance(b, (ast.FunctionDef, ast.AsyncFunctionDef))]
            classes.append({"name": node.name, "line": node.lineno, "methods": methods})
        elif isinstance(node, ast.Assign):
            for tgt in node.targets:
                if isinstance(tgt, ast.Name):
                    constants.append({"name": tgt.id, "line": node.lineno,
                                      "upper": tgt.id.isupper() or tgt.id.lstrip("_").isupper()})
        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            constants.append({"name": node.target.id, "line": node.lineno,
                              "upper": node.target.id.isupper()})
        elif isinstance(node, ast.Import):
            for a in node.names:
                imports.append({"name": a.name, "line": node.lineno})
        elif isinstance(node, ast.ImportFrom):
            mod = node.module or ""
            for a in node.names:
                imports.append({"name": f"{mod}.{a.name}" if mod else a.name, "line": node.lineno})
    return {"functions": functions, "classes": classes, "constants": constants, "imports": imports}


# parser registry (language-agnostic surface; parser-pluggable -- CTO note). v1 = python only.
_PARSERS = {".py": parse_python}


def analyze(path: str) -> dict:
    resolved = _resolve(path)
    if not resolved:
        return {"error": f"file not found: {path}"}
    ext = os.path.splitext(resolved)[1].lower()
    parser = _PARSERS.get(ext)
    if not parser:
        return {"error": f"no parser for '{ext}' (v1 = Python only; .ts/.sh are a future parser add). "
                         f"file: {os.path.relpath(resolved, _WS)}"}
    with open(resolved, encoding="utf-8", errors="replace") as fh:
        text = fh.read()
    try:
        syms = parser(text)
    except SyntaxError as e:
        return {"error": f"parse failed ({type(e).__name__}: line {e.lineno}): {e.msg}",
                "path": os.path.relpath(resolved, _WS).replace(os.sep, "/")}
    syms["path"] = os.path.relpath(resolved, _WS).replace(os.sep, "/")
    syms["lang"] = ext.lstrip(".")
    return syms


# --------------------------------------------------------------------------------------------
def _filter(a: dict, grep: str | None) -> dict:
    if not grep:
        return a
    rx = re.compile(grep, re.IGNORECASE)
    out = dict(a)
    out["functions"] = [f for f in a.get("functions", []) if rx.search(f["name"])]
    out["constants"] = [c for c in a.get("constants", []) if rx.search(c["name"])]
    out["imports"] = [i for i in a.get("imports", []) if rx.search(i["name"])]
    kept_classes = []
    for c in a.get("classes", []):
        meth = [m for m in c["methods"] if rx.search(m["name"])]
        if rx.search(c["name"]) or meth:
            kept_classes.append({**c, "methods": meth if not rx.search(c["name"]) else c["methods"]})
    out["classes"] = kept_classes
    return out


def render(a: dict, kind: str | None, grep: str | None) -> str:
    if a.get("error"):
        return f"comp-symbols: {a['error']}"
    a = _filter(a, grep)
    L = [f"=== comp-symbols: {a['path']}  ({a.get('lang','?')}) ==="]

    def show(k):
        return kind is None or kind == k

    if show("func"):
        fns = a["functions"]
        L.append(f"\nFUNCTIONS ({len(fns)}) [module-level]:")
        for f in fns:
            L.append(f"  {f['line']:5d}  {'async ' if f['async'] else ''}{f['name']}({f['sig']})")
    if show("class"):
        cls = a["classes"]
        L.append(f"\nCLASSES ({len(cls)}):")
        for c in cls:
            L.append(f"  {c['line']:5d}  class {c['name']}  ({len(c['methods'])} methods)")
            for m in c["methods"]:
                L.append(f"    {m['line']:5d}    .{m['name']}({m['sig']})")
    if show("const"):
        cs = a["constants"]
        L.append(f"\nCONSTANTS / module-level bindings ({len(cs)}):")
        for c in cs:
            L.append(f"  {c['line']:5d}  {c['name']}" + ("   [UPPER]" if c.get("upper") else ""))
    if show("import"):
        ims = a["imports"]
        L.append(f"\nIMPORTS ({len(ims)}):")
        for i in ims:
            L.append(f"  {i['line']:5d}  {i['name']}")
    return "\n".join(L)


def main() -> int:
    ap = argparse.ArgumentParser(description="comp-symbols -- intra-file symbol-inventory tool")
    ap.add_argument("file", nargs="?", help="path to a source file (v1: Python)")
    ap.add_argument("--grep", help="filter symbol names (regex, case-insensitive)")
    ap.add_argument("--kind", choices=["func", "class", "const", "import"], help="one symbol class")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args()

    if not args.file:
        ap.print_help()
        return 2
    a = analyze(args.file)
    if args.json:
        print(json.dumps(_filter(a, args.grep) if not a.get("error") else a, indent=2))
        return 1 if a.get("error") else 0
    print(render(a, args.kind, args.grep))
    return 1 if a.get("error") else 0


if __name__ == "__main__":
    sys.exit(main())
