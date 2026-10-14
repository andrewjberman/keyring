#!/usr/bin/env python3
"""Arms for .tools/measure_inline_holiday_sets.py. Standard library; temporary directories only.

Each arm builds its own library and Lambda tree under a temporary directory, runs measure(), and
checks the output. Final line: MEASURE-INLINE-HOLIDAYS arms=<k>/<n> ok=<True|False>
"""
from __future__ import annotations

import importlib.util
import os
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
TOOL = os.path.join(os.path.dirname(HERE), "measure_inline_holiday_sets.py")
_spec = importlib.util.spec_from_file_location("measure_inline_holiday_sets", TOOL)
MIH = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(MIH)

HOLIDAYS = ["2026-01-01", "2026-07-03", "2027-12-24"]
LAMBDA_FILE = "fn-a/lambda_function.py"


def library_text(holidays) -> str:
    lines = ["import datetime as dt", "NYSE_HOLIDAYS_FALLBACK = frozenset({"]
    lines += ['    "%s",' % h for h in sorted(holidays)]
    lines.append("})")
    lines += [
        "def is_trading_day(date):",
        "    d = date if isinstance(date, dt.date) else dt.date.fromisoformat(str(date)[:10])",
        "    return d.weekday() < 5 and d.isoformat() not in NYSE_HOLIDAYS_FALLBACK",
        "",
    ]
    return "\n".join(lines)


def lambda_text(holidays, literal=True, extra="", set_name="NYSE_HOLIDAYS") -> str:
    lines = ["import datetime as dt"]
    if literal:
        lines.append("%s = {" % set_name)
        lines += ['    "%s",' % h for h in sorted(holidays)]
        lines.append("}")
    else:
        # a comprehension is not a literal: ast.literal_eval refuses it
        items = ", ".join('"%s"' % h for h in sorted(holidays))
        lines.append("%s = {d for d in [%s]}" % (set_name, items))
    lines += [
        "def is_trading_day(d: dt.date) -> bool:",
        "    return d.weekday() < 5 and d.isoformat() not in %s%s" % (set_name, extra),
        "",
    ]
    return "\n".join(lines)


def write(path: str, text: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="ascii", newline="\n") as fh:
        fh.write(text)


def run(root: str, lambdas: dict):
    """lambdas maps a path relative to root/infra/aws/lambda to text. Returns (lines, ok)."""
    lib = os.path.join(root, "lib", "trading_calendar.py")
    write(lib, library_text(HOLIDAYS))
    lam = os.path.join(root, "infra", "aws", "lambda")
    os.makedirs(lam, exist_ok=True)
    for rel, text in lambdas.items():
        write(os.path.join(lam, rel), text)
    return MIH.measure(lib, lam, root)


def last_line(lines) -> str:
    return lines[-1]


def arm_same_set_reads_same():
    with tempfile.TemporaryDirectory() as root:
        lines, ok = run(root, {LAMBDA_FILE: lambda_text(HOLIDAYS)})
        assert last_line(lines) == (
            "INLINE-HOLIDAY-SETS found=1 same_2026_2027=1 differs_2026_2027=0 unreadable=0 ok=True"), lines
        assert ok is True
        assert any(x.startswith("INLINE path=") and x.endswith("SAME-2026-2027") for x in lines), lines
        assert "VERDICT same path=infra/aws/lambda/%s" % LAMBDA_FILE in lines, lines


def arm_dropped_2026_date_differs_named():
    with tempfile.TemporaryDirectory() as root:
        dropped = [h for h in HOLIDAYS if h != "2026-07-03"]
        lines, ok = run(root, {LAMBDA_FILE: lambda_text(dropped)})
        inline = [x for x in lines if x.startswith("INLINE path=")][0]
        assert "DIFFERS-2026-2027" in inline, inline
        assert "only_in_lambda=none" in inline, inline
        assert "only_in_lib=2026-07-03" in inline, inline
        assert last_line(lines) == (
            "INLINE-HOLIDAY-SETS found=1 same_2026_2027=0 differs_2026_2027=1 unreadable=0 ok=True"), lines
        assert ok is True


def arm_non_literal_unreadable_arithmetic_closes():
    with tempfile.TemporaryDirectory() as root:
        lines, ok = run(root, {LAMBDA_FILE: lambda_text(HOLIDAYS, literal=False)})
        inline = [x for x in lines if x.startswith("INLINE path=")][0]
        assert "UNREADABLE" in inline and "not a literal" in inline, inline
        assert last_line(lines) == (
            "INLINE-HOLIDAY-SETS found=1 same_2026_2027=0 differs_2026_2027=0 unreadable=1 ok=True"), lines
        assert ok is True


def arm_extra_condition_logic_differs():
    with tempfile.TemporaryDirectory() as root:
        lines, ok = run(root, {LAMBDA_FILE: lambda_text(HOLIDAYS, extra=" and d.day != 13")})
        logic = [x for x in lines if x.startswith("LOGIC ")][0]
        assert logic.startswith("LOGIC LOGIC-DIFFERS path=infra/aws/lambda/%s" % LAMBDA_FILE), logic
        assert "attribute .day" in logic, logic
        assert "VERDICT differs path=infra/aws/lambda/%s" % LAMBDA_FILE in lines, lines
        assert last_line(lines) == (
            "INLINE-HOLIDAY-SETS found=1 same_2026_2027=0 differs_2026_2027=1 unreadable=0 ok=True"), lines


def arm_empty_file_set_found_0_not_ok():
    with tempfile.TemporaryDirectory() as root:
        lines, ok = run(root, {})
        assert last_line(lines) == (
            "INLINE-HOLIDAY-SETS found=0 same_2026_2027=0 differs_2026_2027=0 unreadable=0 ok=False"), lines
        assert ok is False


ARMS = [
    ("same-set-reads-same", arm_same_set_reads_same),
    ("dropped-2026-date-differs-named", arm_dropped_2026_date_differs_named),
    ("non-literal-unreadable-arithmetic-closes", arm_non_literal_unreadable_arithmetic_closes),
    ("extra-condition-logic-differs", arm_extra_condition_logic_differs),
    ("empty-file-set-found-0-not-ok", arm_empty_file_set_found_0_not_ok),
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
    print("MEASURE-INLINE-HOLIDAYS arms=%d/%d ok=%s" % (passed, total, ok))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
