"""Fixture battery for comp-cache's NFRA_COMPEFFICACY T-23 result contract.

Run both grains:
  python .tools/tests/test_comp_cache_battery.py
  pytest -q .tools/tests/test_comp_cache_battery.py

The fixture is a disposable portal/src tree; it never reads or writes the live portal submodule.
Each answer-state arm has a red mutant made from the production engine source.  A mutant must run
and make that arm fail, otherwise the arm is dead rather than evidence.
"""
from __future__ import annotations

import argparse
import contextlib
import io
import sys
import tempfile
import types
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ENGINE = ROOT / "org" / "modules" / "graph" / "cache_cli.py"
RESULTS: list[tuple[str, bool, str]] = []


def _load_engine(source: str | None = None):
    """Load production bytes, or a source-mutant, with its real __file__ sibling context."""
    name = "comp_cache_battery_%d" % (len(RESULTS) + len(sys.modules))
    module = types.ModuleType(name)
    module.__file__ = str(ENGINE)
    sys.modules[name] = module
    exec(compile(source or ENGINE.read_text(encoding="utf-8"), str(ENGINE), "exec"), module.__dict__)
    return module


def _write(root: Path, rel: str, text: str) -> None:
    path = root / "portal" / "src" / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _query(key: str = "'present-key'") -> str:
    return ("export const C = () => useQuery({\n"
            f"  queryKey: [{key}],\n"
            "  queryFn: () => fetch('/ok'),\n"
            "})\n")


def _run(module, command: str, source: Path, *, query: str | None = None,
         budget: float | None = None, expired: bool = False) -> str:
    ns = argparse.Namespace(command=command, portal_src=str(source), cursor=None, budget=budget)
    if query is not None:
        ns.query = query
    if budget is not None:
        ns._budget_s = budget
        ns._budget_source = "flag"
        ns._clock = module._compbudget.Clock(budget)
        if expired:
            ns._clock.start -= budget + 1.0
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        {"map": module.cmd_map, "collisions": module.cmd_collisions, "key": module.cmd_key}[command](ns)
    return buf.getvalue()


def _mutant(state: str):
    source = ENGINE.read_text(encoding="utf-8")
    if state not in source:
        raise AssertionError("mutation anchor absent: %s" % state)
    return _load_engine(source.replace(state, "MUTANT_" + state))


def _record(name: str, ok: bool, detail: str) -> None:
    RESULTS.append((name, ok, detail))


def _exercise_state(name: str, expected: str, command: str, source: Path, **kwargs) -> None:
    production = _load_engine()
    output = _run(production, command, source, **kwargs)
    passed = expected in output
    _record(name, passed, output[:220])

    mutant = _mutant(expected.removeprefix("ANSWER_STATE: "))
    mutant_output = _run(mutant, command, source, **kwargs)
    ran = ("CACHE" in mutant_output or "REACT QUERY" in mutant_output)
    _record(name + "-RED-MUTANT", ran and expected not in mutant_output,
            mutant_output[:220] if ran else "mutant did not run")


def _run_battery() -> None:
    if RESULTS:
        return
    with tempfile.TemporaryDirectory() as temp:
        root = Path(temp)

        # SUBJECT_ABSENT_FROM_CORPUS: the portal source subject itself does not exist.
        _exercise_state("A-SUBJECT-ABSENT", "ANSWER_STATE: SUBJECT_ABSENT_FROM_CORPUS", "map",
                        root / "missing" / "portal" / "src")

        # PRESENT_WITH_ZERO_RESULTS: the corpus exists and has a real query, but this key has no reader.
        complete = root / "complete" / "portal" / "src"
        _write(root / "complete", "components/Present.tsx", _query())
        _exercise_state("B-PRESENT-ZERO", "ANSWER_STATE: PRESENT_WITH_ZERO_RESULTS", "key", complete,
                        query="missing-key")

        # PARTIAL_OR_BLIND: an explicitly generated TSX file is declared skipped; collisions must not read CLEAN.
        partial = root / "partial" / "portal" / "src"
        _write(root / "partial", "components/Present.tsx", _query())
        _write(root / "partial", "generated/Blind.generated.tsx", "// @generated\n" + _query("'blind-key'"))
        _exercise_state("C-PARTIAL-BLIND", "ANSWER_STATE: PARTIAL_OR_BLIND", "collisions", partial)
        partial_output = _run(_load_engine(), "collisions", partial)
        _record("C-NO-SILENT-CLEAN", "COLLISION VERDICT: INCOMPLETE" in partial_output
                and "No cross-file cache-key collisions" not in partial_output, partial_output[:220])

        # NOT_APPLICABLE: portal source exists but the chosen cache-key modes have no useQuery population.
        not_applicable = root / "not_applicable" / "portal" / "src"
        _write(root / "not_applicable", "components/Plain.tsx", "export const Plain = () => null\n")
        _exercise_state("D-NOT-APPLICABLE", "ANSWER_STATE: NOT_APPLICABLE", "collisions", not_applicable)

        # Rule T: a caller-controlled tiny budget yields a partial prefix and explicit resume cursor.
        bounded_output = _run(_load_engine(), "map", complete, budget=0.001, expired=True)
        _record("E-RULE-T-BUDGET", "BUDGET REACHED:" in bounded_output
                and "ANSWER_STATE: PARTIAL_OR_BLIND" in bounded_output
                and "--cursor START" in bounded_output, bounded_output[:260])


def _report() -> int:
    _run_battery()
    failures = [item for item in RESULTS if not item[1]]
    for name, ok, detail in RESULTS:
        print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                               "" if ok else " -- " + detail.replace("\n", " ")[:160]))
    print("COMP-CACHE BATTERY: %d/%d PASS (denominator %d)" %
          (len(RESULTS) - len(failures), len(RESULTS), len(RESULTS)))
    return 1 if failures else 0


def test_all_arms_pass():
    _run_battery()
    failures = [(name, detail) for name, ok, detail in RESULTS if not ok]
    assert not failures, "comp-cache battery failures: %r" % failures


if __name__ == "__main__":
    raise SystemExit(_report())
