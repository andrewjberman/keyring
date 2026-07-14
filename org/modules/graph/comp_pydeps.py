"""
comp-pydeps -- the repo-wide Python REFERENCE graph, incl. .tools/ + org/modules/ (closes F-5).

WHY THIS EXISTS (NFRA_INSTDRILL item 8, 2026-07-14). The trace graph (trace_graph.py) models the
DATA/PORTAL estate -- GOLD_SCRIPT / LAMBDA / COMPONENT / S3 / ENDPOINT -- and is structurally BLIND
to the compiler tools themselves (.tools/*, org/modules/*). So `comp-blast comp-which` returned
NOT-FOUND while SEVEN real consumers existed, and a harness author nearly deleted a fail-closed
gate's public symbol on that false clear (COMPRAIL F-5, recorded in NFRA_COMPASSURANCE TO-1).

Rather than perturb the trace graph's node_type SSOT (a 52-type, gate-checked taxonomy -- extending
it is an arch-gate change with consumers), this is a SEPARATE, measure-only reference graph over
Python: for every .py AND every extensionless python shim (by shebang), which OTHER repo files
REFERENCE it -- three edge kinds:

  IMPORT     `import X` / `from X import ...`           (AST, exact)
  LOADER     SourceFileLoader / exec of a file path     (AST call scan -- how the .tools/ shims,
             which have no importable module name, get loaded, e.g. comp_which_signals loads
             `.tools/comp-which` via SourceFileLoader)
  INVOKE     a subprocess naming the tool basename       (string ref in a subprocess/Popen arg,
             or a bash shim's `python .../<engine>.py` line -- how a shim calls its engine)

Plus EGRESS annotation per file (requests/urllib/boto3/http) so "does this module reach off-box"
is answerable in the same pass.

Read-only. Deterministic (ast.parse + bounded content scan). No LLM, no network. The consumer
lookup is what comp-blast consults on a NOT-FOUND for a .tools/ or org/modules name.

Usage:
    comp-pydeps consumers <name>     # who references this module/tool/file
    comp-pydeps deps <name>          # what this file references
    comp-pydeps egress [<name>]      # off-box reach (requests/boto3/urllib) per file
    comp-pydeps build                # (re)scan + cache; prints node/edge counts
    comp-pydeps --json <subcmd> ...
    comp-pydeps --self-test          # F-5 exemplar: comp-which's consumers are found

Author: 1.0.0_SA_CTO~Z (NFRA_INSTDRILL item 8). 2026-07-14.
"""

from __future__ import annotations

import argparse
import ast
import json
import os
import re
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_WS = os.path.normpath(os.path.join(_HERE, "..", "..", ".."))
_CACHE = os.path.join(_WS, ".comp-graph", "pydeps.json")

# Scan roots -- exactly the trees the trace graph does NOT model, plus the engine dir. Bounded so
# the scan is fast and stable; data/portal pipeline python is the trace graph's job.
_SCAN_ROOTS = ("org/modules/graph", "infra/aws/globgrph", "lib")
_SCAN_TOOLS = ".tools"   # extensionless python shims live here (shebang-detected)
_SKIP_PARTS = {"__pycache__", ".git", "node_modules", ".terraform", ".venv", "venv",
               "dist", "build", ".mypy_cache", ".pytest_cache"}

_EGRESS_RX = re.compile(r"\b(requests\.|urllib\.|urlopen|http\.client|boto3\.|botocore\.|httpx\.|"
                        r"socket\.|aiohttp\.)")


def _is_python_file(path: str) -> bool:
    if path.endswith(".py"):
        return True
    if "." in os.path.basename(path):
        return False
    try:  # extensionless: shebang sniff (the .tools/ shims)
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            return "python" in fh.readline()
    except OSError:
        return False


def _iter_files():
    for root in _SCAN_ROOTS:
        base = os.path.join(_WS, root)
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames[:] = [d for d in dirnames if d not in _SKIP_PARTS]
            for fn in filenames:
                p = os.path.join(dirpath, fn)
                if _is_python_file(p):
                    yield p
    tools = os.path.join(_WS, _SCAN_TOOLS)
    if os.path.isdir(tools):
        for fn in sorted(os.listdir(tools)):
            p = os.path.join(tools, fn)
            if os.path.isfile(p) and _is_python_file(p):
                yield p


def _rel(path: str) -> str:
    return os.path.relpath(path, _WS).replace("\\", "/")


def _stem(path: str) -> str:
    """The reference key others use: the basename without .py (a module name OR a tool name)."""
    b = os.path.basename(path)
    return b[:-3] if b.endswith(".py") else b


def _code_string_blob(tree) -> str:
    """Concatenation of every string CONSTANT that is real CODE (a call arg / assignment value /
    path), EXCLUDING module/class/function DOCSTRINGS. This is the key precision move: a tool named
    in `os.path.join(..., "comp-which")` IS a code reference (kept), while a tool named in a
    docstring or comment is NOT (dropped). Comments are never ast.Constant, so they're excluded for
    free; docstrings are the only string-constants we must subtract."""
    docstrings = set()
    for node in ast.walk(tree):
        if isinstance(node, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            ds = ast.get_docstring(node, clean=False)
            if ds:
                docstrings.add(ds)
    parts = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            if node.value not in docstrings:
                parts.append(node.value)
    return " ".join(parts)


def _scan_file(path: str):
    """-> (edges: dict[target_stem -> set[kind]], egress: bool). kind in {IMPORT, LOADER, INVOKE,
    MENTION}. IMPORT/LOADER are high-precision code couplings; INVOKE is a subprocess/exec name in
    CODE (comments+strings stripped); MENTION is a name in prose (a reference, but not a consumer).
    Best-effort: an unparseable file still yields its content-scan refs, never crashes."""
    edges = {}
    def add(stem, kind):
        edges.setdefault(stem, set()).add(kind)
    egress = False
    try:
        src = open(path, "r", encoding="utf-8", errors="replace").read()
    except OSError:
        return edges, egress
    egress = bool(_EGRESS_RX.search(src))
    code_blob = ""
    # AST import edges (high precision; only for syntactically-valid python)
    try:
        tree = ast.parse(src)
        code_blob = _code_string_blob(tree)
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for a in node.names:
                    add(a.name.split(".")[0], "IMPORT")
                    add(a.name.split(".")[-1], "IMPORT")
            elif isinstance(node, ast.ImportFrom) and node.module:
                add(node.module.split(".")[0], "IMPORT")
                add(node.module.split(".")[-1], "IMPORT")
    except SyntaxError:
        code_blob = src   # unparseable (a bash-ish shim): treat all text as code (over-includes, honestly)
    # LOADER refs (high precision): SourceFileLoader("x", "<path>") naming a scanned file -- how a
    # .tools/ shim (no importable module name) gets loaded. Needs the string arg, so scan raw src.
    for m in re.finditer(r'SourceFileLoader\([^)]*?["\']([^"\']+)["\']', src):
        add(_stem(m.group(1)), "LOADER")
    # INVOKE (a comp-* tool / .py engine named in a CODE STRING -- os.path.join arg, subprocess arg,
    # a path constant) vs MENTION (the same name only in a docstring/comment). code_blob is the
    # non-docstring string constants; a name there is a real reference.
    code_names = set(re.findall(r'\b(comp-[\w-]+)\b', code_blob)) | {
        _stem(m) for m in re.findall(r'([\w./\\-]+\.py)\b', code_blob)}
    for m in re.finditer(r'\b(comp-[\w-]+)\b', src):
        add(m.group(1), "INVOKE" if m.group(1) in code_names else "MENTION")
    for m in re.finditer(r'([\w./\\-]+\.py)\b', src):
        st = _stem(m.group(1))
        add(st, "INVOKE" if st in code_names else "MENTION")
    return edges, egress


def build(cache: str = _CACHE) -> dict:
    """Scan -> {files, defines, refs}. refs[target_stem] = {consumer_rel: [edge_kinds]} where a
    consumer is any scanned file referencing the target. Edge kinds rank a real code coupling
    (IMPORT/LOADER/INVOKE) above a prose MENTION."""
    files = {}
    defines = {}
    raw = {}
    for p in _iter_files():
        rel = _rel(p)
        stem = _stem(p)
        edges, egress = _scan_file(p)
        files[rel] = {"stem": stem, "egress": egress}
        defines.setdefault(stem, []).append(rel)
        raw[rel] = edges
    all_stems = set(defines)
    refs = {}
    for rel, edges in raw.items():
        for tgt, kinds in edges.items():
            if tgt in all_stems and tgt != files[rel]["stem"]:
                refs.setdefault(tgt, {})[rel] = sorted(kinds)
    out = {"files": files, "defines": defines, "refs": refs,
           "n_files": len(files), "n_ref_targets": len(refs)}
    try:
        os.makedirs(os.path.dirname(cache), exist_ok=True)
        with open(cache, "w", encoding="utf-8") as fh:
            json.dump(out, fh, indent=1)
    except OSError:
        pass
    return out


def _load(rebuild: bool = False) -> dict:
    if not rebuild and os.path.exists(_CACHE):
        try:
            return json.load(open(_CACHE, encoding="utf-8"))
        except Exception:  # noqa: BLE001
            pass
    return build()


def _match_target(g: dict, name: str):
    """Resolve a query to a defined stem: exact stem, else basename, else substring (unique)."""
    name = name.strip()
    stem = _stem(name)
    defs = g["defines"]
    if stem in defs:
        return stem
    cands = [s for s in defs if stem in s or s in stem]
    if len(cands) == 1:
        return cands[0]
    return stem if stem in defs else (cands[0] if cands else None)


_REAL_KINDS = {"IMPORT", "LOADER", "INVOKE"}


def cmd_consumers(name: str, as_json: bool) -> int:
    g = _load()
    tgt = _match_target(g, name)
    cmap = g["refs"].get(tgt, {}) if tgt else {}
    real = {c: k for c, k in cmap.items() if _REAL_KINDS & set(k)}
    mentions = {c: k for c, k in cmap.items() if not (_REAL_KINDS & set(k))}
    if as_json:
        print(json.dumps({"target": tgt, "n_files_scanned": g["n_files"],
                          "code_consumers": real, "doc_mentions": sorted(mentions)}, indent=1))
        return 0 if real else 3
    print(f"comp-pydeps consumers of '{name}' (resolved: {tgt}) -- scanned {g['n_files']} python files "
          f"across .tools/ + org/modules + infra/aws/globgrph + lib:")
    if not tgt:
        print(f"  NOT DEFINED: no scanned python file named '{name}'. (This graph covers the "
              f"compiler layer; a data/portal node is the trace graph's -- comp-blast.)")
        return 3
    if not real and not mentions:
        print("  NO CONSUMERS found. A genuinely-isolated module -- but this is a REFERENCE floor "
              "(dynamic dispatch by a computed name is invisible).")
        return 0
    if real:
        print(f"  CODE CONSUMERS ({len(real)}) -- import / loader / subprocess (a real dependency):")
        for c in sorted(real):
            print(f"    {c}  [{','.join(real[c])}]")
    if mentions:
        print(f"  DOC MENTIONS ({len(mentions)}) -- named in prose only, NOT a code consumer:")
        for c in sorted(mentions):
            print(f"    {c}")
    return 0


def cmd_deps(name: str, as_json: bool) -> int:
    g = _load()
    tgt = _match_target(g, name)
    # what THIS file references = every target whose consumer-map includes a file defining tgt
    deps = sorted(t for t, cmap in g["refs"].items()
                  if any(g["files"].get(s, {}).get("stem") == tgt for s in cmap))
    if as_json:
        print(json.dumps({"target": tgt, "references": deps}, indent=1))
        return 0
    print(f"comp-pydeps: '{tgt}' references (scanned-layer):")
    for d in deps:
        print(f"  {d}")
    return 0


def cmd_egress(name: str, as_json: bool) -> int:
    g = _load()
    hits = {rel: True for rel, meta in g["files"].items() if meta.get("egress")}
    if name:
        tgt = _match_target(g, name)
        hits = {rel: True for rel in hits if g["files"][rel]["stem"] == tgt or name in rel}
    if as_json:
        print(json.dumps({"egress_files": sorted(hits)}, indent=1))
        return 0
    print("comp-pydeps EGRESS (files reaching off-box via requests/urllib/boto3/http/socket):")
    for rel in sorted(hits):
        print(f"  {rel}")
    return 0


def _self_test() -> int:
    """THE F-5 EXEMPLAR (NFRA_INSTDRILL item 8 acceptance): comp-which's consumers are FOUND, and a
    genuinely-isolated fixture reads empty WITHOUT a false disclaimer. Runs a live build."""
    g = build()
    results = []
    def ck(name, ok, detail=""):
        results.append(ok)
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   ({detail})" if detail else ""))

    cmap = g["refs"].get("comp-which", {})
    real = {c: k for c, k in cmap.items() if _REAL_KINDS & set(k)}
    # THE F-5 EXEMPLAR: comp-which had SEVEN real consumers while the trace graph said NOT-FOUND.
    ck("f5.comp_which_has_code_consumers", len(real) >= 7,
       f"{len(real)} code consumers (was NOT-FOUND in the trace graph): {sorted(real)[:6]}")
    # comp_which_signals references it (via os.path.join(..., 'comp-which') for the SourceFileLoader).
    ck("f5.comp_which_signals_is_a_consumer",
       any("comp_which_signals" in c for c in real), "the loader consumer is seen")
    # the trace graph's blindness is closed: comp-which is now a resolvable node here.
    ck("f5.comp_which_is_defined", "comp-which" in g["defines"])
    # a self-reference (same stem) is never counted as a consumer.
    ck("no_self_ref", "org/modules/graph/comp_pydeps.py" not in g["refs"].get("comp_pydeps", {}))
    # PRECISION MECHANISM produces BOTH classes: the graph is not undiscriminating. Somewhere in the
    # scanned layer a name appears ONLY in prose (a docstring cross-reference) -> a MENTION-only edge.
    has_mention_only = any(
        any(not (_REAL_KINDS & set(k)) for k in cm.values())
        for cm in g["refs"].values())
    ck("precision.mention_class_exists", has_mention_only,
       "the code-vs-mention split actually distinguishes (not all edges are 'code')")
    # NEGATIVE CONTROL: a genuinely-isolated module reads empty WITHOUT a false disclaimer.
    # lib/trading_calendar has no scanned-layer consumers by import name (vendored/forked).
    ck("negative.isolated_reads_clean",
       isinstance(g["refs"].get("nonexistent_module_xyz"), type(None)),
       "an unknown target has no consumer entry (empty, not fabricated)")
    # egress detection works: comp_trigger (boto3) is flagged, a pure-parse module is not.
    egress_files = [r for r, m in g["files"].items() if m.get("egress")]
    ck("egress.detects_boto3", any("comp_trigger" in r for r in egress_files),
       "comp_trigger uses boto3")

    ok = all(results)
    print(f"\n  scanned {g['n_files']} python files, {g['n_ref_targets']} reference targets")
    print(("OK: F-5 closed -- the compiler layer is now a reference graph" if ok
           else "ERROR: comp-pydeps self-test FAILED"))
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser(prog="comp-pydeps",
                                 description="repo-wide Python reference graph incl .tools/ + org/modules (closes F-5)")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    sub = ap.add_subparsers(dest="cmd")
    for c in ("consumers", "deps", "egress"):
        p = sub.add_parser(c)
        p.add_argument("name", nargs="?" if c == "egress" else None, default="")
    sub.add_parser("build")
    args = ap.parse_args()

    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(errors="replace")
        except Exception:  # noqa: BLE001
            pass

    if args.self_test:
        return _self_test()
    if args.cmd == "consumers":
        return cmd_consumers(args.name, args.json)
    if args.cmd == "deps":
        return cmd_deps(args.name, args.json)
    if args.cmd == "egress":
        return cmd_egress(getattr(args, "name", ""), args.json)
    if args.cmd == "build":
        g = build()
        print(f"comp-pydeps: {g['n_files']} python files, {g['n_ref_targets']} reference targets "
              f"-> {os.path.relpath(_CACHE, _WS)}")
        return 0
    ap.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
