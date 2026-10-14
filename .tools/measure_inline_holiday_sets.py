#!/usr/bin/env python3
"""Measure the hand-typed NYSE holiday sets held inside Lambda files against the library. READ-ONLY.

Discovery under infra/aws/lambda: every .py file that defines at top level either a holiday-set
assignment named NYSE_HOLIDAYS, or a top-level is_trading_day / _is_trading_day / _is_trading_day_iso
function. Vendored copies of lib/trading_calendar.py are excluded here: they are the job of
measure_calendar_copies.py, whose discover() is reused by path, so the two tools agree on the copies.

For each candidate the holiday set is the name its function tests with `not in` (NYSE_HOLIDAYS when the
function names none). The set is read through ast: ast.literal_eval of the assigned value, with one
frozenset(...) or set(...) call around a literal unwrapped. No Lambda module is imported (they import
boto3); no network, no AWS; files are read, never written.

The function body is checked statically: it may read only its parameters, the set, the names it stores
and the calendar/int helpers, call only weekday/isoformat/split/int, and must compare weekday() < 5 and
`not in` the set. Anything else is LOGIC-DIFFERS; a file with no such function is LOGIC-UNREAD.

The library side is measure_calendar_copies.probe(lib): the library's weekday closures for 2026 and
2027, answered by its fallback table (pandas_market_calendars masked).

A candidate is SAME only when its set equals the library's weekday closures AND its logic is LOGIC-OK;
a set that differs, or a logic that does not read as LOGIC-OK, is DIFFERS; a set that cannot be read
is UNREADABLE. Unreadable files and parse failures are candidates counted as unreadable, never as equal.

Last line: INLINE-HOLIDAY-SETS found=<n> same_2026_2027=<a> differs_2026_2027=<b> unreadable=<c> ok=<bool>
ok is True when n == a + b + c and n >= 1. Exit 0 when ok, else 1.
"""
from __future__ import annotations

import argparse
import ast
import datetime as dt
import importlib.util
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
_MCC_PATH = os.path.join(HERE, "measure_calendar_copies.py")
_spec = importlib.util.spec_from_file_location("measure_calendar_copies", _MCC_PATH)
MCC = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(MCC)

YEARS = MCC.YEARS
_PREFILTER = (b"NYSE_HOLIDAYS", b"is_trading_day")
_FN_NAME = re.compile(r"^_?is_trading_day(_iso)?$")
_ISO = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$")
_SET_DEFAULT = "NYSE_HOLIDAYS"
_LOGIC_ATTRS = frozenset({"weekday", "isoformat", "split"})
_LOGIC_NAMES = frozenset({"calendar", "int"})
_NODES = (
    ast.Return, ast.Assign, ast.Expr, ast.Import, ast.ImportFrom, ast.alias, ast.Tuple,
    ast.GeneratorExp, ast.comprehension, ast.Load, ast.Store, ast.Constant, ast.Name,
    ast.Attribute, ast.Call, ast.BoolOp, ast.And, ast.UnaryOp, ast.Not, ast.Compare,
    ast.Lt, ast.NotIn,
)


def _repo_root() -> str:
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _ascii(text: str) -> str:
    return text.encode("ascii", "replace").decode("ascii")


def _rel(path: str, root: str) -> str:
    return os.path.relpath(path, root).replace("\\", "/")


def _top_def(tree):
    """First top-level function named is_trading_day (or a private spelling of it), or None."""
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and _FN_NAME.match(node.name):
            return node
    return None


def _top_assigns(tree, name: str) -> list:
    out = []
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == name for t in node.targets):
            out.append(node)
        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name) and node.target.id == name:
            out.append(node)
    return out


def _set_name(fn) -> str:
    """The name the function tests with `not in`; NYSE_HOLIDAYS when it names none."""
    for node in ast.walk(fn):
        if isinstance(node, ast.Compare):
            for op, comp in zip(node.ops, node.comparators):
                if isinstance(op, ast.NotIn) and isinstance(comp, ast.Name):
                    return comp.id
    return _SET_DEFAULT


def _literal(node):
    """ast.literal_eval, with one frozenset(...)/set(...) call around a literal unwrapped. Returns (value, form)."""
    if (isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in ("frozenset", "set")
            and len(node.args) == 1 and not node.keywords):
        return ast.literal_eval(node.args[0]), "%s-wrapped-literal" % node.func.id
    return ast.literal_eval(node), "literal"


def read_set(tree, name: str):
    """Return (dates, form, None) for a literal set of ISO dates, or (None, None, reason)."""
    found = _top_assigns(tree, name)
    if not found:
        return None, None, "no top-level assignment to %s" % name
    if len(found) > 1:
        return None, None, "%s assigned %d times at top level" % (name, len(found))
    node = found[0]
    if node.value is None:
        return None, None, "%s has no value (line %d)" % (name, node.lineno)
    try:
        held, form = _literal(node.value)
    except (ValueError, TypeError, SyntaxError, MemoryError, RecursionError):
        return None, None, "%s is not a literal (%s at line %d)" % (name, type(node.value).__name__, node.lineno)
    if not isinstance(held, (set, frozenset)):
        return None, None, "%s is %s, not a set (line %d)" % (name, type(held).__name__, node.lineno)
    for item in held:
        if not (isinstance(item, str) and _ISO.match(item)):
            return None, None, "%s holds a non-ISO entry %s" % (name, _ascii(repr(item)))
        try:
            dt.date.fromisoformat(item)
        except ValueError:
            return None, None, "%s holds an invalid date %s" % (name, item)
    return set(held), form, None


def _allowed_call(node) -> bool:
    func = node.func
    if isinstance(func, ast.Name):
        return func.id == "int"
    if isinstance(func, ast.Attribute):
        return func.attr in _LOGIC_ATTRS
    return False


def _is_weekday_call(node) -> bool:
    return isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == "weekday"


def _is_int(node, value: int) -> bool:
    return isinstance(node, ast.Constant) and type(node.value) is int and node.value == value


def check_logic(fn, set_name: str):
    """Static read of the function body: (verdict, detail), verdict LOGIC-OK / LOGIC-DIFFERS."""
    body = [s for s in fn.body
            if not (isinstance(s, ast.Expr) and isinstance(s.value, ast.Constant) and isinstance(s.value.value, str))]
    if not body:
        return "LOGIC-UNREAD", "empty body"
    params = {a.arg for a in fn.args.posonlyargs + fn.args.args + fn.args.kwonlyargs}
    stored = set()
    for stmt in body:
        for node in ast.walk(stmt):
            if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
                stored.add(node.id)
            elif isinstance(node, ast.alias):
                stored.add((node.asname or node.name).split(".")[0])
    names_ok = params | stored | {set_name} | _LOGIC_NAMES
    problems = []
    saw_weekday = saw_membership = False
    for stmt in body:
        for node in ast.walk(stmt):
            where = "line %s" % getattr(node, "lineno", getattr(stmt, "lineno", "?"))
            if not isinstance(node, _NODES):
                problems.append("%s at %s" % (type(node).__name__, where))
            elif isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load) and node.id not in names_ok:
                problems.append("reads %s at %s" % (node.id, where))
            elif isinstance(node, ast.Attribute) and node.attr not in _LOGIC_ATTRS:
                problems.append("attribute .%s at %s" % (node.attr, where))
            elif isinstance(node, ast.Call) and not _allowed_call(node):
                problems.append("call at %s" % where)
            elif isinstance(node, ast.BoolOp) and not isinstance(node.op, ast.And):
                problems.append("or-condition at %s" % where)
            elif isinstance(node, ast.UnaryOp) and not isinstance(node.op, ast.Not):
                problems.append("unary operator at %s" % where)
            elif isinstance(node, ast.Compare):
                op = node.ops[0] if len(node.ops) == 1 else None
                comp = node.comparators[0] if len(node.comparators) == 1 else None
                if op is not None and isinstance(op, ast.Lt) and _is_weekday_call(node.left) and _is_int(comp, 5):
                    saw_weekday = True
                elif (op is not None and isinstance(op, ast.NotIn) and isinstance(comp, ast.Name)
                      and comp.id == set_name):
                    saw_membership = True
                else:
                    problems.append("comparison at %s" % where)
    if not saw_weekday:
        problems.append("does not test weekday() < 5")
    if not saw_membership:
        problems.append("does not test membership in %s" % set_name)
    if problems:
        return "LOGIC-DIFFERS", _ascii("; ".join(problems[:3]))
    return "LOGIC-OK", "reads weekday and %s only" % set_name


def _candidates(py_files, copies, root):
    """Return (candidates, hits). A candidate is (path, tree, reason-or-None)."""
    out = []
    hits = 0
    for path in py_files:
        if path in copies:
            continue
        try:
            with open(path, "rb") as fh:
                data = fh.read()
        except OSError as exc:
            out.append((path, None, "cannot read (%s)" % _ascii(exc.strerror or type(exc).__name__)))
            continue
        if not any(token in data for token in _PREFILTER):
            continue
        hits += 1
        try:
            tree = ast.parse(data, filename=path)
        except (SyntaxError, ValueError) as exc:
            out.append((path, None, "parse failed (%s)" % type(exc).__name__))
            continue
        if _top_def(tree) is None and not _top_assigns(tree, "NYSE_HOLIDAYS"):
            continue
        out.append((path, tree, None))
    return out, hits


def measure(lib_path: str, lambda_root: str, root: str):
    """Return (output_lines, ok). The last output line is the INLINE-HOLIDAY-SETS summary."""
    out = []
    lib_hol, lib_err = MCC.probe(lib_path)
    if lib_err is None:
        out.append("LIB path=%s weekday_closures_2026_2027=%d %s"
                   % (_rel(lib_path, root), len(lib_hol), MCC._fmt(lib_hol)))
    else:
        out.append("LIB path=%s IMPORT-FAILED %s" % (_rel(lib_path, root), lib_err))
    copies = set(MCC.discover(lambda_root))
    py_files = []
    if os.path.isdir(lambda_root):
        for dirpath, dirnames, filenames in os.walk(lambda_root):
            dirnames[:] = sorted(d for d in dirnames if d != "__pycache__")
            for name in sorted(filenames):
                if name.endswith(".py"):
                    py_files.append(os.path.join(dirpath, name))
    cands, hits = _candidates(py_files, copies, root)
    lib_copies = sum(1 for p in py_files if p in copies)
    for p in sorted(copies):
        if p in py_files:
            out.append("EXCLUDED-LIBRARY-COPY path=%s" % _rel(p, root))
    out.append("SEARCHED root=%s py_files=%d pattern=NYSE_HOLIDAYS|is_trading_day prefilter_hits=%d "
               "library_copies_excluded=%d candidates=%d"
               % (_rel(lambda_root, root), len(py_files), hits, lib_copies, len(cands)))
    same = differs = unreadable = 0
    for path, tree, reason in cands:
        rel = _rel(path, root)
        if reason is not None:
            unreadable += 1
            out.append("INLINE path=%s dates_2026_2027=unread UNREADABLE %s" % (rel, _ascii(reason)))
            out.append("VERDICT unreadable path=%s" % rel)
            continue
        fn = _top_def(tree)
        set_name = _set_name(fn) if fn is not None else _SET_DEFAULT
        held, form, serr = read_set(tree, set_name)
        if serr is None and lib_err is not None:
            serr = "library-not-importable"
            held = None
        if serr is not None:
            dates_txt = "unread"
            status = "UNREADABLE %s" % _ascii(serr)
            form_txt = "none"
        else:
            raw = sum(1 for d in held if int(d[:4]) in YEARS)
            weekday_held = sorted(d for d in held if int(d[:4]) in YEARS and dt.date.fromisoformat(d).weekday() < 5)
            dates_txt = str(raw)
            form_txt = form
            if weekday_held == lib_hol:
                status = "SAME-2026-2027"
            else:
                only_lam = sorted(set(weekday_held) - set(lib_hol))
                only_lib = sorted(set(lib_hol) - set(weekday_held))
                status = "DIFFERS-2026-2027 only_in_lambda=%s only_in_lib=%s" % (MCC._fmt(only_lam), MCC._fmt(only_lib))
        if fn is None:
            logic, detail = "LOGIC-UNREAD", "no is_trading_day definition in the file"
        else:
            logic, detail = check_logic(fn, set_name)
        out.append("INLINE path=%s set=%s form=%s dates_2026_2027=%s %s" % (rel, set_name, form_txt, dates_txt, status))
        out.append("LOGIC %s path=%s %s" % (logic, rel, _ascii(detail)))
        if serr is not None:
            unreadable += 1
            verdict = "unreadable"
        elif status == "SAME-2026-2027" and logic == "LOGIC-OK":
            same += 1
            verdict = "same"
        else:
            differs += 1
            verdict = "differs"
        out.append("VERDICT %s path=%s" % (verdict, rel))
    n = len(cands)
    ok = n >= 1 and n == same + differs + unreadable
    out.append("INLINE-HOLIDAY-SETS found=%d same_2026_2027=%d differs_2026_2027=%d unreadable=%d ok=%s"
               % (n, same, differs, unreadable, ok))
    return out, ok


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Measure inline NYSE holiday sets in Lambdas (read-only).")
    parser.add_argument("--root", default=_repo_root(), help="repository root")
    parser.add_argument("--lib", default=None, help="library path (default lib/trading_calendar.py)")
    parser.add_argument("--lambda-root", default=None, help="Lambda tree (default infra/aws/lambda)")
    args = parser.parse_args(argv)
    root = os.path.abspath(args.root)
    lib = os.path.abspath(args.lib or os.path.join(root, "lib", "trading_calendar.py"))
    lam = os.path.abspath(args.lambda_root or os.path.join(root, "infra", "aws", "lambda"))
    lines, ok = measure(lib, lam, root)
    for line in lines:
        print(line)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
