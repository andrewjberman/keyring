#!/usr/bin/env python3
"""Arms for .tools/measure_calendar_copies.py. Standard library; temporary directories only.

Each arm builds its own library and Lambda tree under a temporary directory, runs measure(), and
checks the output. Final line: MEASURE-CALENDAR-COPIES arms=<k>/<n> ok=<True|False>
"""
from __future__ import annotations

import importlib.util
import os
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
TOOL = os.path.join(os.path.dirname(HERE), "measure_calendar_copies.py")
_spec = importlib.util.spec_from_file_location("measure_calendar_copies", TOOL)
MCC = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(MCC)

HOLIDAYS = ["2026-01-01", "2026-07-03", "2027-12-24"]


def module_text(holidays, raises=False) -> str:
    lines = ["import datetime as dt", "NYSE_HOLIDAYS_FALLBACK = frozenset({"]
    lines += ['    "%s",' % h for h in sorted(holidays)]
    lines.append("})")
    if raises:
        lines.append('raise RuntimeError("boom at import")')
    lines += [
        "def is_trading_day(date):",
        "    d = date if isinstance(date, dt.date) else dt.date.fromisoformat(str(date)[:10])",
        "    return d.weekday() < 5 and d.isoformat() not in NYSE_HOLIDAYS_FALLBACK",
        "",
    ]
    return "\n".join(lines)


def write(path: str, text: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="ascii", newline="\n") as fh:
        fh.write(text)


def run(root: str, copies: dict):
    """copies maps a path relative to root/lambda to text. Returns (lines, ok)."""
    lib = os.path.join(root, "lib", "trading_calendar.py")
    write(lib, module_text(HOLIDAYS))
    lam = os.path.join(root, "infra", "aws", "lambda")
    os.makedirs(lam, exist_ok=True)
    for rel, text in copies.items():
        write(os.path.join(lam, rel), text)
    return MCC.measure(lib, lam, root)


def last_line(lines) -> str:
    return lines[-1]


def arm_identical_two_read_same():
    with tempfile.TemporaryDirectory() as root:
        lines, ok = run(root, {
            "fn-a/trading_calendar.py": module_text(HOLIDAYS),
            "fn-b/vendored_calendar.py": module_text(HOLIDAYS),  # renamed vendored copy
        })
        assert last_line(lines) == (
            "CALENDAR-COPIES found=2 same_2026_2027=2 differs_2026_2027=0 import_failed=0 ok=True"), lines
        assert ok is True
        assert sum("SAME-2026-2027" in x for x in lines) == 2, lines


def arm_dropped_2026_holiday_differs():
    with tempfile.TemporaryDirectory() as root:
        dropped = [h for h in HOLIDAYS if h != "2026-07-03"]
        lines, ok = run(root, {"fn-a/trading_calendar.py": module_text(dropped)})
        copy_line = [x for x in lines if x.startswith("COPY ")][0]
        assert "DIFFERS-2026-2027" in copy_line, copy_line
        assert "only_in_lib=2026-07-03" in copy_line, copy_line
        assert "only_in_copy=none" in copy_line, copy_line
        assert last_line(lines) == (
            "CALENDAR-COPIES found=1 same_2026_2027=0 differs_2026_2027=1 import_failed=0 ok=True"), lines
        assert ok is True


def arm_import_failure_closes_arithmetic():
    with tempfile.TemporaryDirectory() as root:
        lines, ok = run(root, {"fn-a/trading_calendar.py": module_text(HOLIDAYS, raises=True)})
        copy_line = [x for x in lines if x.startswith("COPY ")][0]
        assert "IMPORT-FAILED" in copy_line and "boom at import" in copy_line, copy_line
        assert last_line(lines) == (
            "CALENDAR-COPIES found=1 same_2026_2027=0 differs_2026_2027=0 import_failed=1 ok=True"), lines
        assert ok is True


def arm_empty_folder_set_not_ok():
    with tempfile.TemporaryDirectory() as root:
        lines, ok = run(root, {})
        assert last_line(lines) == (
            "CALENDAR-COPIES found=0 same_2026_2027=0 differs_2026_2027=0 import_failed=0 ok=False"), lines
        assert ok is False


ARMS = [
    ("identical-copies-read-same", arm_identical_two_read_same),
    ("dropped-2026-holiday-differs", arm_dropped_2026_holiday_differs),
    ("import-failure-counted-arithmetic-closes", arm_import_failure_closes_arithmetic),
    ("empty-folder-set-found-0-not-ok", arm_empty_folder_set_not_ok),
]


def main() -> int:
    passed = 0
    for name, fn in ARMS:
        try:
            fn()
            passed += 1
            print("ARM PASS %s" % name)
        except AssertionError as exc:
            print("ARM FAIL %s: %s" % (name, str(exc).encode("ascii", "replace").decode("ascii")))
    total = len(ARMS)
    ok = passed == total
    print("MEASURE-CALENDAR-COPIES arms=%d/%d ok=%s" % (passed, total, ok))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
