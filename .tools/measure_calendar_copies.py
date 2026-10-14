#!/usr/bin/env python3
"""Measure the Lambda-vendored copies of lib/trading_calendar.py. READ-ONLY.

For the library and every copy it prints one line: path, line count, sha256 of the LF-normalised
bytes, and the NYSE full-day closures for 2026 and 2027 (weekdays on which the file's own
is_trading_day answers False). Each file's code is loaded by path into a fresh module object with
pandas_market_calendars masked, so the hardcoded fallback table answers -- the answer a Lambda
runtime gives, since the Lambda copies do not vendor pandas_market_calendars.

Copies are discovered under infra/aws/lambda: every file named trading_calendar.py, plus every
other .py file that defines the library's holiday-set name NYSE_HOLIDAYS_FALLBACK (a renamed
vendored copy). Standard library only; reads files only; no network; no AWS; writes nothing.

Last line: CALENDAR-COPIES found=<n> same_2026_2027=<a> differs_2026_2027=<b> import_failed=<c> ok=<bool>
ok is True when n == a + b + c and n >= 1 and the library itself imports. Exit 0 when ok, else 1.
"""
from __future__ import annotations

import argparse
import contextlib
import datetime as dt
import hashlib
import importlib.util
import io
import os
import re
import sys

YEARS = (2026, 2027)
_HOLIDAY_DEF = re.compile(rb"^NYSE_HOLIDAYS_FALLBACK\s*(?::[^=\n]*)?=", re.M)
_MASKED = "pandas_market_calendars"
_CALL = "is_trading_day"


def _repo_root() -> str:
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _ascii(text: str) -> str:
    return text.encode("ascii", "replace").decode("ascii")


def read_normalised(path: str):
    """Return (lines, sha256) of the LF-normalised bytes of path."""
    with open(path, "rb") as fh:
        raw = fh.read()
    data = raw.replace(b"\r\n", b"\n")
    lines = data.count(b"\n") + (1 if data and not data.endswith(b"\n") else 0)
    return lines, hashlib.sha256(data).hexdigest()


def discover(lambda_root: str) -> list:
    """Every trading_calendar.py, and every other .py defining NYSE_HOLIDAYS_FALLBACK, sorted."""
    found = []
    if not os.path.isdir(lambda_root):
        return found
    for dirpath, dirnames, filenames in os.walk(lambda_root):
        dirnames[:] = sorted(d for d in dirnames if d != "__pycache__")
        for name in sorted(filenames):
            if not name.endswith(".py"):
                continue
            path = os.path.join(dirpath, name)
            if name == "trading_calendar.py":
                found.append(path)
                continue
            with open(path, "rb") as fh:
                if _HOLIDAY_DEF.search(fh.read()):
                    found.append(path)
    return found


def load_by_path(path: str):
    """Load path's code into a fresh module object, with pandas_market_calendars masked."""
    name = "_cal_measure_" + hashlib.sha256(path.encode("utf-8")).hexdigest()[:16]
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError("no loader for this path")
    module = importlib.util.module_from_spec(spec)
    had = _MASKED in sys.modules
    saved = sys.modules.get(_MASKED)
    sys.modules[_MASKED] = None  # any import of the package now raises ImportError
    try:
        spec.loader.exec_module(module)
    finally:
        if had:
            sys.modules[_MASKED] = saved
        else:
            sys.modules.pop(_MASKED, None)
    return module


def yielded_holidays(module) -> list:
    """Weekdays in YEARS on which the module's is_trading_day answers False, sorted ISO dates."""
    fn = getattr(module, _CALL, None)
    if not callable(fn):
        raise AttributeError("no callable %s" % _CALL)
    out = []
    for year in YEARS:
        day = dt.date(year, 1, 1)
        while day.year == year:
            if day.weekday() < 5 and not fn(day):
                out.append(day.isoformat())
            day += dt.timedelta(days=1)
    return sorted(out)


def probe(path: str):
    """Return (holidays, None) or (None, reason). Any failure to import or answer is a reason."""
    err = io.StringIO()
    try:
        with contextlib.redirect_stderr(err):
            module = load_by_path(path)
            return yielded_holidays(module), None
    except Exception as exc:  # an unimportable or non-answering copy is IMPORT-FAILED, not a crash
        text = str(exc).strip().splitlines()
        detail = text[0] if text else ""
        return None, _ascii("%s: %s" % (type(exc).__name__, detail))


def _fmt(dates) -> str:
    return ",".join(dates) if dates else "none"


def _rel(path: str, root: str) -> str:
    return os.path.relpath(path, root).replace("\\", "/")


def measure(lib_path: str, lambda_root: str, root: str):
    """Return (output_lines, ok). The last output line is the CALENDAR-COPIES summary."""
    out = []
    lib_lines, lib_sha = read_normalised(lib_path)
    lib_hol, lib_err = probe(lib_path)
    if lib_err is None:
        out.append("LIB path=%s lines=%d sha256=%s holidays=%s"
                   % (_rel(lib_path, root), lib_lines, lib_sha, _fmt(lib_hol)))
    else:
        out.append("LIB path=%s lines=%d sha256=%s IMPORT-FAILED %s"
                   % (_rel(lib_path, root), lib_lines, lib_sha, lib_err))
    same = differs = failed = 0
    copies = discover(lambda_root)
    for path in copies:
        lines, sha = read_normalised(path)
        head = "COPY path=%s lines=%d sha256=%s" % (_rel(path, root), lines, sha)
        hol, err = probe(path)
        if err is not None:
            failed += 1
            out.append("%s IMPORT-FAILED %s" % (head, err))
        elif lib_err is not None:
            failed += 1
            out.append("%s holidays=%s IMPORT-FAILED library-not-importable" % (head, _fmt(hol)))
        elif hol == lib_hol:
            same += 1
            out.append("%s holidays=%s SAME-2026-2027" % (head, _fmt(hol)))
        else:
            differs += 1
            only_copy = sorted(set(hol) - set(lib_hol))
            only_lib = sorted(set(lib_hol) - set(hol))
            out.append("%s holidays=%s DIFFERS-2026-2027 only_in_copy=%s only_in_lib=%s"
                       % (head, _fmt(hol), _fmt(only_copy), _fmt(only_lib)))
    n = len(copies)
    ok = n >= 1 and n == same + differs + failed and lib_err is None
    out.append("CALENDAR-COPIES found=%d same_2026_2027=%d differs_2026_2027=%d import_failed=%d ok=%s"
               % (n, same, differs, failed, ok))
    return out, ok


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Measure Lambda-vendored trading_calendar copies (read-only).")
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
