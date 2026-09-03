"""Battery for comp-estate -- NFRA_COMPEFFICACY TO-CE-T-17 (T17-AC2/AC4/AC5).

Seven independently falsifiable arms cover the four ratified answer states, the C(N)
RELIES-ON/no-guess boundary, Rule T expiry, resume-cursor union, and help disclosure.  Every arm
runs a disposable mutant beside the real engine and proves the same predicate goes RED; a green
production assertion without its red mutant is a dead arm, not a pass.

The NOT_APPLICABLE case is intentionally a planted empty-mode population passed to the public
engine helper.  Production's current snapshot has 29 verticals, so an external ``--list`` cannot
honestly produce that state today.  The fixture changes the population, never the ontology.

Run both grains:
  python .tools/tests/test_comp_estate_battery.py
  pytest -q .tools/tests/test_comp_estate_battery.py
"""
from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import os
import re
import subprocess
import sys
from pathlib import Path

RESULTS: list[tuple[str, bool, str]] = []
_RAN = False
_WS_CACHE: Path | None = None

STATE_TOKENS = (
    "SUBJECT_ABSENT_FROM_CORPUS",
    "PRESENT_WITH_ZERO_RESULTS",
    "PARTIAL_OR_BLIND",
    "NOT_APPLICABLE",
)


def _ws() -> Path:
    global _WS_CACHE
    if _WS_CACHE is None:
        proc = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            cwd=str(Path(__file__).resolve().parent),
            capture_output=True,
            text=True,
            check=True,
        )
        _WS_CACHE = Path(proc.stdout.strip())
    return _WS_CACHE


def _engine() -> Path:
    return _ws() / "org" / "modules" / "graph" / "opal_estate_infrastructure.py"


def _snapshot() -> Path:
    return _engine().with_name("estate-coverage-resolver.json")


def rec(arm: str, ok: bool, detail: str) -> None:
    RESULTS.append((arm, ok, detail))


def run(args: list[str], engine: Path | None = None, timeout: int = 30) -> tuple[int, str]:
    proc = subprocess.run(
        [sys.executable, str(engine or _engine()), *args],
        cwd=str(_ws()),
        capture_output=True,
        text=True,
        timeout=timeout,
    )
    return proc.returncode, (proc.stdout or "") + (proc.stderr or "")


def _mutant_path(kind: str) -> Path:
    return _engine().with_name(f"_tmp_estate_mutant_{kind}_{os.getpid()}.py")


def _write_mutant(kind: str, needle: str, replacement: str) -> Path:
    source = _engine().read_text(encoding="utf-8")
    count = source.count(needle)
    assert count == 1, (
        f"fixture assumption broken for {kind!r}: expected one target in engine, found {count}"
    )
    path = _mutant_path(kind)
    path.write_text(source.replace(needle, replacement, 1), encoding="utf-8")
    return path


def _import_engine(path: Path, name: str):
    sys.path.insert(0, str(path.parent))
    spec = importlib.util.spec_from_file_location(name, str(path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _one_state(out: str, expected: str) -> bool:
    found = re.findall(r"^ANSWER-STATE: (\S+)$", out, flags=re.MULTILINE)
    return found == [expected]


def _list_empty_output(module) -> tuple[int, str]:
    class NoCallLegacy:
        @staticmethod
        def cmd_list(_data):  # pragma: no cover - a call is the failure being guarded
            raise AssertionError("empty --list population must not delegate to the renderer")

    data = {"last_review": "2099-01-01", "named_threads": [], "threads": []}
    stream = io.StringIO()
    with contextlib.redirect_stdout(stream):
        rc = module._list_run(NoCallLegacy(), data, 0.0, "flag")
    return rc, stream.getvalue()


def _mutant_probe(
    kind: str,
    needle: str,
    replacement: str,
    args: list[str],
    predicate,
) -> tuple[bool, str]:
    mutant = None
    try:
        mutant = _write_mutant(kind, needle, replacement)
        rc, out = run(args, mutant)
        went_red = not predicate(rc, out)
        return went_red, f"mutant_rc={rc}; predicate_red={went_red}; tail={out[-180:]!r}"
    finally:
        if mutant is not None and mutant.exists():
            mutant.unlink()


def _run_battery() -> None:
    global _RAN
    if _RAN:
        return
    _RAN = True

    # ARM 1 -- absent subject is a corpus fact, not an ontology guess.
    absent_args = ["ZZZ_CE_T17_NO_SUCH_VERTICAL", "--budget", "0"]

    def absent_pred(rc, out):
        return rc == 2 and _one_state(out, STATE_TOKENS[0])

    rc, out = run(absent_args)
    red, detail = _mutant_probe(
        "absent_token",
        'STATE_SUBJECT_ABSENT = "SUBJECT_ABSENT_FROM_CORPUS"',
        'STATE_SUBJECT_ABSENT = "BROKEN_ABSENT_TOKEN"',
        absent_args,
        absent_pred,
    )
    rec("ESTATE-STATE-SUBJECT-ABSENT", absent_pred(rc, out) and red, detail)

    # ARM 2 -- a declared vertical with zero chains is zero, not absent.
    zero_args = ["ceo-digest", "--budget", "0"]

    def zero_pred(rc, out):
        return rc == 0 and _one_state(out, STATE_TOKENS[1]) and "0 chain(s)" in out

    rc, out = run(zero_args)
    red, detail = _mutant_probe(
        "zero_token",
        'STATE_PRESENT_ZERO = "PRESENT_WITH_ZERO_RESULTS"',
        'STATE_PRESENT_ZERO = "BROKEN_ZERO_TOKEN"',
        zero_args,
        zero_pred,
    )
    rec("ESTATE-STATE-PRESENT-ZERO", zero_pred(rc, out) and red, detail)

    # ARM 3 -- the explicit C(N) name is carried to its owner; guessing is forbidden.
    carried_args = ["C(N)", "--budget", "0"]

    def carried_pred(rc, out):
        return (
            rc == 0
            and _one_state(out, STATE_TOKENS[2])
            and "TOOL-VOICE: NOT-DECIDABLE" in out
            and "RELIES-ON NFRA_C3MATERIALIZE" in out
            and "GUESSED-ONTOLOGY" not in out
        )

    rc, out = run(carried_args)
    red, detail = _mutant_probe(
        "ontology_guess",
        '"membership, or answer was guessed."',
        '"membership, or answer was guessed. GUESSED-ONTOLOGY: advi-bd"',
        carried_args,
        carried_pred,
    )
    rec("ESTATE-STATE-CN-CARRIED-NOT-GUESSED", carried_pred(rc, out) and red, detail)

    # ARM 4 -- a mode with an empty population is NOT_APPLICABLE.  Fixture changes only data.
    real_module = _import_engine(_engine(), "comp_estate_battery_real")
    rc, out = _list_empty_output(real_module)

    def na_pred(got_rc, got_out):
        return got_rc == 0 and _one_state(got_out, STATE_TOKENS[3])

    mutant = None
    try:
        mutant = _write_mutant(
            "not_applicable_token",
            'STATE_NOT_APPLICABLE = "NOT_APPLICABLE"',
            'STATE_NOT_APPLICABLE = "BROKEN_NOT_APPLICABLE"',
        )
        mutant_module = _import_engine(mutant, "comp_estate_battery_na_mutant")
        mrc, mout = _list_empty_output(mutant_module)
        red = not na_pred(mrc, mout)
        detail = f"mutant_rc={mrc}; predicate_red={red}; output={mout!r}"
    finally:
        if mutant is not None and mutant.exists():
            mutant.unlink()
    rec("ESTATE-STATE-NOT-APPLICABLE", na_pred(rc, out) and red, detail)

    # ARM 5 -- tiny caller budget expires in tool voice, rc remains execution-only clean.
    budget_args = ["advi-bd", "--budget", "0.00001", "--head", "0"]

    def budget_pred(rc, out):
        return (
            rc == 0
            and "BUDGET REACHED:" in out
            and "scanned 0 of 19 chain(s)" in out
            and "WITHIN BUDGET:" not in out
            and _one_state(out, STATE_TOKENS[2])
        )

    rc, out = run(budget_args)
    deadline_block = (
        "    return (\n"
        "        (deadline_ns is not None and time.perf_counter_ns() >= deadline_ns)\n"
        "        or (remaining is not None and remaining <= 0)\n"
        "    )\n"
    )
    red, detail = _mutant_probe(
        "budget_ignored",
        deadline_block,
        "    return False  # MUTANT: caller budget silently ignored\n",
        budget_args,
        budget_pred,
    )
    rec("ESTATE-RULE-T-BUDGET-REACHED-RC-CLEAN", budget_pred(rc, out) and red, detail)

    # ARM 6 -- a real chain cursor removes exactly one deterministic unit from the resumed run.
    snapshot = json.loads(_snapshot().read_text(encoding="utf-8"))
    units = sorted(
        row["thread_id"]
        for row in snapshot["threads"]
        if row.get("named_thread") == "advi-bd"
    )
    first = units[0]
    expected = len(units) - 1
    cursor_args = ["advi-bd", "--cursor", first, "--budget", "0", "--head", "0"]
    cursor_re = re.compile(rf"WITHIN BUDGET: scanned {expected} of {expected} chain\b")

    def cursor_pred(rc, out):
        return rc == 0 and bool(cursor_re.search(out))

    rc, out = run(cursor_args)
    red, detail = _mutant_probe(
        "cursor_replays_unit",
        "            return ordered[idx + 1:], None",
        "            return ordered[idx:], None  # MUTANT: replays the cursor unit",
        cursor_args,
        cursor_pred,
    )
    rec("ESTATE-RULE-T-CURSOR-UNION", cursor_pred(rc, out) and red, detail)

    # ARM 7 -- carrier precedence and cursor are visible before anyone runs the tool.
    help_args = ["--help"]

    def help_pred(rc, out):
        return rc == 0 and "--budget" in out and "COMP_BUDGET_S" in out and "--cursor" in out

    rc, out = run(help_args)
    red, detail = _mutant_probe(
        "help_hides_carrier",
        '"chain traversal; carrier --budget > env COMP_BUDGET_S > default %ss. "',
        '"chain traversal; carrier removed. Default %ss. "',
        help_args,
        help_pred,
    )
    rec("ESTATE-RULE-T-HELP-DISCLOSES-CARRIER", help_pred(rc, out) and red, detail)


def _report() -> int:
    _run_battery()
    failures = [(arm, detail) for arm, ok, detail in RESULTS if not ok]
    for arm, ok, detail in RESULTS:
        print(f"  [{'PASS' if ok else 'FAIL'}] {arm}" + ("" if ok else f" -- {detail[:240]}"))
    print(f"COMP-ESTATE BATTERY: {len(RESULTS) - len(failures)}/{len(RESULTS)} PASS")
    return 1 if failures else 0


def test_all_arms_pass():
    """Pytest file-grain entry; importing this module performs no battery work."""
    _run_battery()
    failures = [(arm, detail) for arm, ok, detail in RESULTS if not ok]
    assert not failures, f"comp-estate battery failures: {failures!r}"


if __name__ == "__main__":
    sys.exit(_report())
