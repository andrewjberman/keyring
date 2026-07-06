"""
log-open-lint -- a hygiene lint born from the NFRA_TOOLHEALTH corpus-brick incident (2026-07-06).

THE BUG CLASS IT CATCHES: a text-READ `open()` with an explicit `encoding=` but NO `errors=`, pointed at
a KNOWN-MULTI-WRITER LOG path. Such a read crashes with UnicodeDecodeError the instant ANY writer appends
a single non-UTF-8 byte -- and multi-writer append logs (rail logs, the compiler-tools-log, telemetry
jsonl, routing logs) accumulate bytes from dozens of agents, so a mangled smart-quote is a matter of time.
On 2026-07-06 a truncated em-dash (bare 0xe2) in comp-which-rail.log line 3445 crashed
tool_activity_emit.parse_rail -> load_corpus -> COMPLEARN corpus load was BRICKED FABRIC-WIDE for every
consumer since ~07-02, silently. The fix was `errors="replace"` on the read.

This lint flags that shape so it cannot recur silently. It ties to the CLAUDE.md "no non-ASCII in logs"
Code-Quality discipline from the OTHER side: producers should not WRITE non-ASCII into logs, and consumers
must not READ them strictly -- belt AND suspenders.

WHY it requires `encoding=` present: an explicit encoding is the author declaring "this is a text op where
charset matters" -- exactly the read that will decode-crash. It also keeps false-positives low (we do not
flag every open() in the tree, only text reads of log-shaped paths that forgot errors=).

Scope decision (RAVC'd COO+CTO 2026-07-06): STANDALONE checker first. Wiring it into the shared
ds-commit-gate / a ruff-tier is a CTO-ruled follow-on (a shared gate that false-positive-blocks would
stall the whole fabric) -- this ships the detector + its honesty (the self-test), integration is separate.

Invoke:
  python org/modules/graph/compproof/log_open_lint.py <file.py> [<file.py> ...]   # exit 1 if any violation
  python org/modules/graph/compproof/log_open_lint.py --self-test                 # AST cases + the em-dash runtime demo

Author: 0.8.0_AE_CloudComp (NFRA_TOOLHEALTH durable-hygiene, COO GO 2026-07-06).
"""

from __future__ import annotations

import ast
import os
import re
import sys
import tempfile

# Explicit multi-writer log paths named in the incident + the COO GO. Substring match (case-insensitive).
# Specific tokens only (NOT a bare "telemetry" -- that matched a HAR-capture docstring in the 07-06 sweep;
# specific filenames keep the enclosing-function/docstring heuristic precise).
KNOWN_MULTIWRITER_SUBSTR = (
    "comp-which-rail", "compiler-tools-log", "agent_telemetry", "-routing.jsonl",
    "rail.log", "routing.log",
)
# Generic log-file shapes: a path literal that ENDSWITH one of these is a log/stream file.
LOG_FILE_SUFFIXES = (".log", ".jsonl")
# Variable/constant NAMES that conventionally hold a log path (RAIL_LOG, ROUTING_LOG, log_path, ...).
LOG_NAME_RE = re.compile(r"(?i)(^|_)(rail|routing|telemetry)(_|$)|_log$|log_?path$|(^|_)log$")
# A FUNCTION that parses a multi-writer log: the real 07-06 crash sites (parse_rail / parse_rolling_log /
# parse_telemetry) receive the log path via a bare PARAM, so the open()-site path is generic -- the log-ness
# lives in the function's name/docstring. Distinctive tokens on an underscore boundary (so 'catalog' does
# NOT match on a bare 'log'). NOTE 'routing' is deliberately NOT here (it matched a config-manifest loader
# 'load_routing' in the 07-06 sweep); a genuine routing-LOG read is still caught by the '-routing.jsonl'
# path-literal, so dropping the name token loses no real coverage.
LOG_PARSER_NAME_RE = re.compile(r"(?i)(^|_)(rail|rolling|telemetry|log)(_|$)")


def _str_looks_like_log(s: str) -> str | None:
    low = s.lower()
    for sub in KNOWN_MULTIWRITER_SUBSTR:
        if sub in low:
            return "path contains %r (known multi-writer log)" % sub
    for suf in LOG_FILE_SUFFIXES:
        if low.endswith(suf):
            return "path ends with %r (log/stream file)" % suf
    return None


def _name_looks_like_log(name: str) -> str | None:
    # ALL_CAPS constant ending LOG (RAIL_LOG) or a *_log / log_path convention.
    if name.isupper() and name.endswith("LOG"):
        return "identifier %r (ALL_CAPS log constant)" % name
    if LOG_NAME_RE.search(name):
        return "identifier %r (log-path naming convention)" % name
    return None


def _path_looks_like_log(node: ast.AST) -> str | None:
    """Does the path EXPRESSION resolve to a known-multi-writer log? Recurses through the common shapes:
    a str literal, a Name/Attribute (RAIL_LOG / tae.RAIL_LOG), os.path.join(..., RAIL_LOG), and string
    concatenation. Returns a human reason (for the report) or None."""
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return _str_looks_like_log(node.value)
    if isinstance(node, ast.Name):
        return _name_looks_like_log(node.id)
    if isinstance(node, ast.Attribute):
        return _name_looks_like_log(node.attr) or _path_looks_like_log(node.value)
    if isinstance(node, ast.Call):  # os.path.join(_WS, RAIL_LOG) / Path(...) -- any arg log-shaped => yes
        for a in node.args:
            r = _path_looks_like_log(a)
            if r:
                return r
        return _path_looks_like_log(node.func)
    if isinstance(node, ast.BinOp):  # "dir/" + RAIL_LOG  or  base % name
        return _path_looks_like_log(node.left) or _path_looks_like_log(node.right)
    if isinstance(node, ast.JoinedStr):  # f"{base}/comp-which-rail.log"
        for v in node.values:
            if isinstance(v, ast.Constant) and isinstance(v.value, str):
                r = _str_looks_like_log(v.value)
                if r:
                    return r
    return None


def _kw(call: ast.Call, name: str) -> ast.AST | None:
    for k in call.keywords:
        if k.arg == name:
            return k.value
    return None


def _mode_node(call: ast.Call, is_attr_open: bool) -> ast.AST | None:
    """The mode argument, positional or keyword. builtin open(path, mode, ...) -> args[1];
    obj.open(mode, ...) (Path.open) -> args[0]; else a mode= kwarg."""
    mkw = _kw(call, "mode")
    if mkw is not None:
        return mkw
    idx = 0 if is_attr_open else 1
    return call.args[idx] if len(call.args) > idx else None


def _is_text_read(call: ast.Call, is_attr_open: bool) -> bool:
    """A read that decodes text: mode absent (default 'r') or a literal containing r/+ and NOT b. A literal
    write/append-only mode (w/a/x, no r, no +) does not decode-on-read -> not this bug. A non-literal mode
    is treated as possibly-reading (conservative) since encoding= already marks it a text op."""
    m = _mode_node(call, is_attr_open)
    if m is None:
        return True
    if isinstance(m, ast.Constant) and isinstance(m.value, str):
        mode = m.value.lower()
        if "b" in mode:
            return False
        if ("r" in mode) or ("+" in mode):
            return True
        return False  # w / a / x only -> write, no decode-on-read
    return True  # unknown mode expression -> conservative


def _path_node(call: ast.Call, is_attr_open: bool) -> ast.AST | None:
    if is_attr_open:
        return call.func.value if isinstance(call.func, ast.Attribute) else None
    if call.args:
        return call.args[0]
    return _kw(call, "file")


def _func_is_log_parser(fn: ast.AST) -> str | None:
    """A function that READS a multi-writer log -- caught by name (parse_rail / parse_rolling_log /
    parse_telemetry) or by a docstring that names a known log file. This is the signal that catches the
    real 2026-07-06 crash sites, where the open()-site path is a bare param and the log-ness lives here."""
    name = getattr(fn, "name", "")
    if LOG_PARSER_NAME_RE.search(name):
        return "enclosing function %r reads a multi-writer log (by name)" % name
    hit = _str_looks_like_log((ast.get_docstring(fn) or "").lower())
    if hit:
        return "enclosing function %r reads a multi-writer log (docstring: %s)" % (name, hit)
    return None


def _parser_open_reasons(tree: ast.AST) -> dict:
    """id(open-Call) -> reason, for every open() lexically inside a log-parser function."""
    out: dict = {}
    for fn in ast.walk(tree):
        if not isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        reason = _func_is_log_parser(fn)
        if not reason:
            continue
        for n in ast.walk(fn):
            if isinstance(n, ast.Call) and (
                    (isinstance(n.func, ast.Name) and n.func.id == "open") or
                    (isinstance(n.func, ast.Attribute) and n.func.attr == "open")):
                out.setdefault(id(n), reason)
    return out


def check_source(src: str, filename: str = "<src>") -> list[dict]:
    """Return one violation dict per offending open(): a text read that declares an encoding but no errors=
    AND is either on a log-shaped path OR inside a log-parser function. {file, line, col, path_reason, snippet}."""
    try:
        tree = ast.parse(src, filename=filename)
    except SyntaxError as e:
        return [{"file": filename, "line": e.lineno or 0, "col": e.offset or 0,
                 "path_reason": "SYNTAX ERROR (cannot lint): %s" % e.msg, "snippet": ""}]
    lines = src.splitlines()
    parser_reasons = _parser_open_reasons(tree)
    out: list[dict] = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        is_builtin = isinstance(node.func, ast.Name) and node.func.id == "open"
        is_attr_open = isinstance(node.func, ast.Attribute) and node.func.attr == "open"
        if not (is_builtin or is_attr_open):
            continue
        if _kw(node, "encoding") is None:      # require an explicit encoding (the text-op signal)
            continue
        if _kw(node, "errors") is not None:    # already hardened
            continue
        if not _is_text_read(node, is_attr_open):
            continue
        pnode = _path_node(node, is_attr_open)
        reason = (_path_looks_like_log(pnode) if pnode is not None else None) or parser_reasons.get(id(node))
        if not reason:
            continue
        ln = getattr(node, "lineno", 0)
        out.append({"file": filename, "line": ln, "col": getattr(node, "col_offset", 0),
                    "path_reason": reason,
                    "snippet": lines[ln - 1].strip() if 0 < ln <= len(lines) else ""})
    return out


def check_file(path: str) -> list[dict]:
    with open(path, encoding="utf-8", errors="replace") as fh:   # this lint eats its own dogfood
        return check_source(fh.read(), filename=path)


def _selftest() -> int:
    # --- AST cases: the exact shapes the lint must (not) flag ---
    flag = "with open(RAIL_LOG, encoding='utf-8') as fh:\n    for ln in fh: pass\n"
    assert check_source(flag), "strict-utf8 read of RAIL_LOG must FLAG"
    lit = "open('org/mcp/comp-which-rail.log', encoding='utf-8').read()\n"
    assert check_source(lit), "literal known-multi-writer log path must FLAG"
    joined = "import os\nwith open(os.path.join(_WS, RAIL_LOG), encoding='utf-8') as fh: fh.read()\n"
    assert check_source(joined), "os.path.join(..., RAIL_LOG) must FLAG (recurses args)"
    hardened = "with open(RAIL_LOG, encoding='utf-8', errors='replace') as fh: fh.read()\n"
    assert not check_source(hardened), "errors= present must NOT flag"
    writemode = "with open(RAIL_LOG, 'w', encoding='utf-8') as fh: fh.write('x')\n"
    assert not check_source(writemode), "write-only mode does not decode-on-read -> must NOT flag"
    binary = "with open(RAIL_LOG, 'rb') as fh: fh.read()\n"
    assert not check_source(binary), "binary read has no encoding= -> must NOT flag"
    cleanpath = "with open('config.json', encoding='utf-8') as fh: fh.read()\n"
    assert not check_source(cleanpath), "a non-log path must NOT flag (keeps false-positives down)"
    jsonl = "with open(routing_path, encoding='utf-8') as fh: fh.read()\n"  # name convention
    # routing_path -> LOG_NAME_RE (routing) -> flag
    assert check_source("routing_path='x'\n" + jsonl), "a *routing* named path must FLAG"

    # --- the REAL 2026-07-06 case: the log path arrives via a bare PARAM; log-ness is in the FUNCTION ---
    real = ("def parse_rail(path):\n"
            "    'comp-which-rail.log -> rows'\n"
            "    with open(path, encoding='utf-8') as fh:\n"
            "        for ln in fh: pass\n")
    assert check_source(real), "text-read in a log-parser function (param path) must FLAG (the 07-06 crash)"
    realtel = ("import glob\n"
               "def parse_telemetry(glob_pat):\n"
               "    'agent_telemetry/*.jsonl -> rows'\n"
               "    for f in glob.glob(glob_pat):\n"
               "        with open(f, encoding='utf-8') as fh: fh.read()\n")
    assert check_source(realtel), "text-read in parse_telemetry (glob var) must FLAG"
    nonparser = ("def load_config(path):\n"
                 "    'read the app config'\n"
                 "    with open(path, encoding='utf-8') as fh: return fh.read()\n")
    assert not check_source(nonparser), "generic param read in a NON-log-parser function must NOT flag"
    catalog = ("def load_catalog(path):\n"
               "    'the product catalog'\n"
               "    with open(path, encoding='utf-8') as fh: return fh.read()\n")
    assert not check_source(catalog), "'catalog' must NOT trip the log-parser name heuristic (word-boundary)"

    # --- the em-dash RUNTIME demo: prove WHY the lint matters (the exact crash it prevents) ---
    fd, tmp = tempfile.mkstemp(suffix=".log")
    try:
        with os.fdopen(fd, "wb") as fh:
            fh.write(b"clean line\n\xe2 truncated em-dash line\n")  # a bare 0xe2 = invalid utf-8
        crashed = False
        try:
            with open(tmp, encoding="utf-8") as fh:      # the UNHARDENED read (what the lint flags)
                for _ln in fh:
                    pass
        except UnicodeDecodeError:
            crashed = True
        assert crashed, "the unhardened strict-utf8 read MUST crash on the 0xe2 byte (the real bug)"
        with open(tmp, encoding="utf-8", errors="replace") as fh:   # the HARDENED read (the fix)
            got = sum(1 for _ in fh)
        assert got == 2, "errors=replace reads all lines without crashing (the fix the lint enforces)"
    finally:
        os.unlink(tmp)

    print("SELF-TEST PASS: AST 12/12 (flag: RAIL_LOG read / literal log / join(RAIL_LOG) / *routing* name /"
          " parse_rail param-path / parse_telemetry glob-var; clean: errors= / write-mode / binary /"
          " non-log path / load_config param / load_catalog word-boundary) | em-dash runtime demo"
          " (unhardened read CRASHES on 0xe2, errors=replace reads clean) -- the exact fabric-brick prevented")
    return 0


def main(argv: list | None = None) -> int:
    import argparse
    ap = argparse.ArgumentParser(prog="log-open-lint",
                                 description="flag a text-read open() with encoding= but no errors= on a "
                                             "known-multi-writer log path (the COMPLEARN corpus-brick class)")
    ap.add_argument("files", nargs="*", help="python files to lint")
    ap.add_argument("--self-test", action="store_true", help="AST cases + the em-dash runtime demo")
    ap.add_argument("--advisory", action="store_true",
                    help="announce-then-enforce mode: print findings as ADVISORY + ALWAYS exit 0 (never "
                         "block). For a shared gate before block-mode promotion; silent when clean.")
    a = ap.parse_args(argv)
    if a.self_test:
        return _selftest()
    if not a.files:
        ap.print_help()
        return 0
    total = 0
    for f in a.files:
        if not os.path.exists(f):
            print("SKIP: %s (not found)" % f)
            continue
        for v in check_file(f):
            total += 1
            print("%s:%d:%d  strict-utf8 log read, no errors= -- %s\n    %s"
                  % (v["file"], v["line"], v["col"], v["path_reason"], v["snippet"]))
    if total:
        tag = "ADVISORY" if a.advisory else "BLOCKED"
        print("\n%s: %d strict-utf8 log-read(s) without errors= -- add errors=\"replace\" "
              "(a multi-writer log will eventually carry a non-UTF-8 byte and crash the read)." % (tag, total))
        return 0 if a.advisory else 1     # advisory NEVER blocks (announce-then-enforce)
    if not a.advisory:                    # advisory is silent-when-clean (0 noise on unrelated commits)
        print("OK: no unguarded strict-utf8 log reads.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
