#!/usr/bin/env python3
"""script_io_ast.py -- DETERMINISTIC AST-derived script I/O for ANY first-party Python file.

WHY THIS EXISTS (Andrew-direct 2026-08-05, at the 3.0.0_SA_CVO~B terminal, VERBATIM):
    "The issue with pipescript is that it needs to be a script io generalist, not bound to a
     handful of gold pipelines."

MEASURED STATE THAT PROMPTED IT (P8 cold descent @a2be6600c, denominators re-derived live with
named exclusions): comp-pipescript's curated DAG universe is 262 scripts = 52.6% of all
data/*/scripts .py and 7.7% of first-party repo .py. Six script trees -- assets (77, the
OPAL_ASSETS monolith, DEPLOYABLE per CLAUDE.md Rule 13), smartx (31), seeking-alpha (14),
etfs (5), demo (4), yang_pkl (1) -- resolve to no graph at all.

THE DESIGN POSITION, and it is the load-bearing one:

    THIS IS A FACT ENGINE, NOT A RANKER.

`comp-pipescript io` answers a question whose correct output is COMPLETE-OR-HONESTLY-INCOMPLETE:
"what does this script read and write." A missing edge is a WRONG ANSWER, not a lower score. That
is why the anatomy-main `corp_write` stack (L0 reach -> L1 CatBoost -> L2 qwen3-coder:30b, which
ranks "files a human should EDIT for this issue") was surveyed and DELIBERATELY NOT RECYCLED here:
porting a ranker would seat a guess behind a fact's interface, inside a deploy-gate obligation,
where CLAUDE.md Rule 22 forbids grounding a source-confirmed claim on a rank. What IS recycled from
that survey is the ARCHITECTURE -- corpgraph_schema's File/Symbol + READS/WRITES dataflow edges,
derived once per repo, language-level and roster-free (see the design doc's section 2).

SILENCE IS THE DEFECT (CLAUDE.md Rule 22a, the comp-iam lesson, applied one tool over):
an under-reporting I/O instrument does not fail loudly -- it produces a clean zero that reads as
"this script has no I/O." So a call site whose target cannot be statically resolved is NEVER
dropped: it is emitted as UNRESOLVED with its evidence line. And EVERY result carries the
DENOMINATOR (call sites scanned), so a caller can always tell "nothing to report" from "I was
pointed at the wrong thing" -- the distinction the whole P8 finding turned on.

NOT A REPLACEMENT for the curated DAG. The curated graph knows chain membership, run order, column
gaps and portal consumers -- things AST cannot see. This is the FALLBACK that makes the tool answer
*something true* for the other 92.3%, instead of refusing or, worse, returning a clean zero.
"""
from __future__ import annotations

import ast
import os
import re

# --------------------------------------------------------------------------- recognizers
# (method name -> direction). Kept EXPLICIT and small: an unrecognized call becomes UNRESOLVED
# rather than being silently classified, because a wrong direction is worse than an unknown one.
_S3_READ = {"get_object", "download_file", "download_fileobj", "head_object"}
_S3_WRITE = {"put_object", "upload_file", "upload_fileobj", "copy_object"}
_PD_READ = {"read_parquet", "read_csv", "read_json", "read_excel", "read_feather", "read_sql"}
_PD_WRITE = {"to_parquet", "to_csv", "to_json", "to_excel", "to_feather", "to_sql"}
_PATH_READ = {"read_text", "read_bytes"}
_PATH_WRITE = {"write_text", "write_bytes"}
_DDB_READ = {"get_item", "query", "scan", "batch_get_item"}
_DDB_WRITE = {"put_item", "update_item", "delete_item", "batch_write_item"}

_S3_URI = re.compile(r"s3://([A-Za-z0-9._-]+)/(\S*)")


def _module_consts(tree):
    """Module-level NAME = "literal" bindings, for constant folding at call sites.

    WHY THIS IS WORTH THE CODE: without it the common real shape --
        BUCKET = "opal-data-assets"  ...  s3.get_object(Bucket=BUCKET, Key=key)
    yields UNRESOLVED, and a manifest that is all-UNRESOLVED is only marginally better than the
    clean zero it replaced. Folding module constants converts a large share of real call sites into
    named targets WITHOUT guessing: every value here is a literal that appears in the source.

    DELIBERATELY SHALLOW -- module scope only, single assignment, string literals only. A name
    rebound later, or built at runtime, stays UNRESOLVED rather than being resolved to a stale or
    invented value. Under-claiming here is correct: a WRONG target is worse than an honest unknown,
    because a wrong one is actionable and silently so.
    """
    consts, rebound = {}, set()
    for node in tree.body:
        if isinstance(node, ast.Assign):
            val = None
            if isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
                val = node.value.value
            for tgt in node.targets:
                if isinstance(tgt, ast.Name):
                    if tgt.id in consts or tgt.id in rebound:
                        rebound.add(tgt.id)      # ambiguous -> refuse to fold
                        consts.pop(tgt.id, None)
                    elif val is not None:
                        consts[tgt.id] = val
    return consts


def _lit(node, consts=None):
    """Return a literal string for `node`, or None. f-strings resolve to a shape with the
    dynamic parts marked -- an f-string key is still evidence of WHICH prefix is touched, and
    discarding it would be exactly the silent under-report this module exists to prevent."""
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if isinstance(node, ast.Name) and consts:
        return consts.get(node.id)
    if isinstance(node, ast.JoinedStr):
        out = []
        for v in node.values:
            if isinstance(v, ast.Constant) and isinstance(v.value, str):
                out.append(v.value)
            elif (isinstance(v, ast.FormattedValue) and isinstance(v.value, ast.Name)
                    and consts and v.value.id in consts):
                out.append(consts[v.value.id])
            else:
                out.append("{?}")
        return "".join(out)
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        left, right = _lit(node.left, consts), _lit(node.right, consts)
        if left is not None or right is not None:
            return (left or "{?}") + (right or "{?}")
    return None


def _kw(call, *names, consts=None):
    for k in call.keywords or []:
        if k.arg in names:
            return _lit(k.value, consts)
    return None


def _target_of(call, func_name, consts=None):
    """Best-effort literal target for a recognized call, else None (-> UNRESOLVED)."""
    if func_name in _S3_READ | _S3_WRITE:
        bucket = _kw(call, "Bucket", consts=consts)
        key = _kw(call, "Key", consts=consts)
        if bucket or key:
            return f"s3://{bucket or '{?}'}/{key or '{?}'}"
        for a in call.args:                      # download_file(bucket, key, path) positional
            lit = _lit(a, consts)
            if lit:
                return lit
        return None
    if func_name in _DDB_READ | _DDB_WRITE:
        t = _kw(call, "TableName", consts=consts)
        return f"dynamodb:{t}" if t else None
    for a in call.args:                          # pandas / Path / open: first positional
        lit = _lit(a, consts)
        if lit:
            return lit
    for kwname in ("path", "path_or_buf", "filepath_or_buffer", "fname", "name"):
        v = _kw(call, kwname, consts=consts)
        if v:
            return v
    return None


class _Visitor(ast.NodeVisitor):
    def __init__(self, consts=None):
        self.consts = consts or {}
        self.rows = []          # (direction, target|None, method, lineno)
        self.sites = 0          # DENOMINATOR: recognized I/O call sites seen
        self.uri_hits = []      # bare s3:// literals anywhere (constants, dict values, ...)

    def visit_Call(self, node):
        fn = None
        if isinstance(node.func, ast.Attribute):
            fn = node.func.attr
        elif isinstance(node.func, ast.Name):
            fn = node.func.id
        if fn:
            direction = None
            if fn in _S3_READ or fn in _PD_READ or fn in _PATH_READ or fn in _DDB_READ:
                direction = "READS"
            elif fn in _S3_WRITE or fn in _PD_WRITE or fn in _PATH_WRITE or fn in _DDB_WRITE:
                direction = "WRITES"
            elif fn == "open":
                mode = None
                if len(node.args) > 1:
                    mode = _lit(node.args[1], self.consts)
                mode = mode or _kw(node, "mode", consts=self.consts) or "r"
                direction = "WRITES" if any(c in mode for c in "wax+") else "READS"
            if direction:
                self.sites += 1
                self.rows.append((direction, _target_of(node, fn, self.consts), fn, node.lineno))
        self.generic_visit(node)

    def visit_Constant(self, node):
        if isinstance(node.value, str):
            for m in _S3_URI.finditer(node.value):
                self.uri_hits.append((f"s3://{m.group(1)}/{m.group(2)}", node.lineno))
        self.generic_visit(node)


def derive_script_io(path: str) -> dict:
    """Derive READS/WRITES for one Python file. Never raises on a bad file -- returns a row set
    with `error` set, because an exception here would surface to a caller as an empty I/O list,
    i.e. the clean-zero failure this module exists to prevent."""
    out = {
        "path": path, "reads": [], "writes": [], "unresolved": [], "s3_literals": [],
        "sites_scanned": 0, "error": None,
    }
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            src = fh.read()
        tree = ast.parse(src, filename=path)
    except (OSError, SyntaxError) as exc:
        out["error"] = f"{type(exc).__name__}: {exc}"
        return out
    v = _Visitor(_module_consts(tree))
    v.visit(tree)
    out["sites_scanned"] = v.sites
    for direction, target, method, lineno in v.rows:
        row = {"target": target, "method": method, "line": lineno}
        if target is None:
            row["target"] = "UNRESOLVED"
            out["unresolved"].append({**row, "direction": direction})
        elif direction == "READS":
            out["reads"].append(row)
        else:
            out["writes"].append(row)
    seen = set()
    for uri, lineno in v.uri_hits:
        if uri not in seen:
            seen.add(uri)
            out["s3_literals"].append({"uri": uri, "line": lineno})
    return out


def render(res: dict, rel: str | None = None) -> str:
    """Human-readable manifest. ASCII only (CLAUDE.md Code Quality: no non-ASCII on AWS/CI paths)."""
    name = rel or res["path"]
    L = [f"I/O MANIFEST (AST-DERIVED): {os.path.basename(name)}",
         f"  source: {name}"]
    if res["error"]:
        L.append(f"  ERROR: {res['error']}")
        L.append("  UNPARSEABLE -- this is NOT an empty I/O set. Nothing was measured.")
        return "\n".join(L)

    L.append(f"  DENOMINATOR: {res['sites_scanned']} recognized I/O call site(s) scanned")
    L.append("")

    def _blk(title, rows):
        L.append(f"  {title} ({len(rows)}):")
        if not rows:
            L.append("    (none found)")
            return
        for r in rows:
            L.append(f"    {r['target']}   <- {r['method']}() :{r['line']}")

    _blk("READS", res["reads"])
    L.append("")
    _blk("WRITES", res["writes"])
    if res["unresolved"]:
        L.append("")
        L.append(f"  UNRESOLVED ({len(res['unresolved'])}) -- a real I/O call whose TARGET is not")
        L.append("  statically knowable (dynamic key, variable, runtime join). These are NOT absent")
        L.append("  I/O and must never be read as such; the call happens, the target needs a human.")
        for r in res["unresolved"]:
            L.append(f"    {r['direction']:<6} {r['method']}() :{r['line']}")
    if res["s3_literals"]:
        L.append("")
        L.append(f"  S3 URI LITERALS ({len(res['s3_literals'])}) -- found anywhere in the source,")
        L.append("  including config dicts and constants the call-site scan does not reach:")
        for r in res["s3_literals"]:
            L.append(f"    {r['uri']}  :{r['line']}")
    if not res["reads"] and not res["writes"] and not res["unresolved"]:
        L.append("")
        L.append("  NOTE: 0 recognized I/O call sites. This is a MEASURED zero over the recognizer")
        L.append("  set (see _S3_READ/_PD_READ/... in this module) -- it is not a claim that the")
        L.append("  script is inert. A script doing I/O through an unrecognized helper reads as")
        L.append("  zero here, which is exactly why the denominator is printed above.")
    return "\n".join(L)


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("usage: script_io_ast.py <path-to-python-file>", file=sys.stderr)
        raise SystemExit(2)
    print(render(derive_script_io(sys.argv[1])))
