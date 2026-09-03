"""Independent battery for comp-similar -- NFRA_COMPEFFICACY.TO-CE-T-12.

The fixtures are offline: they use comp-similar's synthetic corpus and never query Kuzu or AWS.
Every answer-state arm has its own source mutant, Rule T has a cursor mutant, and the historical
D1-D3 vintage capture control has a no-capture runtime mutant.

Run either grain:
  python .tools/tests/test_comp_similar_battery.py
  pytest -q .tools/tests/test_comp_similar_battery.py
"""
from __future__ import annotations

import importlib.util
import os
import subprocess
import sys
from pathlib import Path


RESULTS: list[tuple[str, bool, str]] = []
_WS_CACHE = None
_MOD = None


def _ws() -> Path:
    global _WS_CACHE
    if _WS_CACHE is None:
        proc = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                              cwd=str(Path(__file__).resolve().parent),
                              capture_output=True, text=True, check=True)
        _WS_CACHE = Path(proc.stdout.strip())
    return _WS_CACHE


def _tool() -> Path:
    return _ws() / "org" / "modules" / "graph" / "debtscan" / "comp_similar.py"


def _mod():
    global _MOD
    if _MOD is None:
        spec = importlib.util.spec_from_file_location("comp_similar_battery_import", str(_tool()))
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        _MOD = module
    return _MOD


def rec(tid: str, ok: bool, detail: str = "") -> None:
    RESULTS.append((tid, bool(ok), detail))


def run(args: list[str], tool: Path | None = None, timeout: int = 30) -> tuple[int, str]:
    proc = subprocess.run([sys.executable, str(tool or _tool())] + args,
                          cwd=str(_ws()), capture_output=True, text=True, timeout=timeout)
    return proc.returncode, (proc.stdout or "") + (proc.stderr or "")


def _write_mutant(kind: str, needle: str, replacement: str, expected_count: int = 1) -> Path:
    source = _tool().read_text(encoding="utf-8")
    count = source.count(needle)
    assert count == expected_count, "mutant %s expected %d target(s), found %d" % (
        kind, expected_count, count)
    path = _tool().parent / ("_tmp_comp_similar_mutant_%s_%d.py" % (kind, os.getpid()))
    path.write_text(source.replace(needle, replacement, 1), encoding="utf-8")
    return path


def _heat():
    return {
        "opal-data-legacyfeed": {"data": "COLD", "invoke": "COLD"},
        "opal-data-assets": {"data": "HOT", "invoke": "HOT"},
        "inf-gold-legacyfeed": {"data": "COLD", "invoke": "COLD"},
        "inf-report-sync": {"data": "COLD", "invoke": "COLD"},
        "cot-report-sync": {"data": "HOT", "invoke": "HOT"},
    }


def _run_battery() -> None:
    RESULTS.clear()
    module = _mod()

    # One real engine invocation must plant all four exact enum tokens, and the stale-corpus
    # specimen must carry a concrete vintage rather than merely saying "partial".
    rc, self_out = run(["--self-test"])
    expected = [
        "SUBJECT_ABSENT_FROM_CORPUS",
        "PRESENT_WITH_ZERO_RESULTS",
        "PARTIAL_OR_BLIND",
        "NOT_APPLICABLE",
    ]
    planted = [line for line in self_out.splitlines() if "PLANTED " in line]
    rec("CS-T12-ANSWER-STATES-ONE-INVOCATION",
        rc == 0 and len(planted) == 4 and all("ANSWER-STATE: " + token in self_out
                                             for token in expected),
        "rc=%s planted=%s" % (rc, len(planted)))
    stale = next((line for line in planted if "PLANTED stale-corpus:" in line), "")
    rec("CS-T12-PARTIAL-CARRIES-VINTAGE",
        "corpus built:" in stale and "age: STALE" in stale, stale)

    # Red mutant per answer-state arm. Each mutant changes exactly one literal; the battery's
    # external enum oracle must reject it even though a self-referential internal set could agree.
    for token in expected:
        kind = token.lower()
        mutant = None
        try:
            needle = '= "%s"' % token
            mutant = _write_mutant(kind, needle, '= "MUTATED_%s"' % token)
            mrc, mout = run(["--self-test"], mutant)
            detected = "ANSWER-STATE: " + token not in mout
            rec("CS-T12-MUTANT-%s-DETECTED" % token, detected,
                "mutant rc=%s expected token present=%s" %
                (mrc, "ANSWER-STATE: " + token in mout))
        finally:
            if mutant is not None and mutant.exists():
                mutant.unlink()

    # Help is the public carrier: precedence, default, unbounded value, cursor and engine path.
    hrc, help_out = run(["--help"])
    help_ok = (hrc == 0 and "Rule T: --budget SECONDS >" in help_out
               and "COMP_BUDGET_S > 90s default" in help_out
               and "0 is unbounded" in help_out and "--cursor LAST_ARN" in help_out
               and "org/modules/graph/debtscan/comp_similar.py" in help_out)
    rec("CS-T12-RULE-T-HELP-CARRIER", help_ok, help_out[-500:])

    # Direct functional Rule T arm: an already-spent clock still completes exactly one stable
    # unit, marks the answer partial, and produces a cursor naming that fully processed ARN.
    class _SpentClock:
        @staticmethod
        def remaining():
            return 0.0

    corpus = module._mkcorpus()
    index = module.SimilarityIndex(corpus)
    progress = {}
    module.supersede_scan(corpus, index, _heat(), clock=_SpentClock(), progress=progress)
    cursor_ok = (progress == {"completed": 1, "total": len(corpus),
                              "cursor": sorted(corpus)[0], "partial": True})
    rec("CS-T12-RULE-T-TINY-BUDGET-CURSOR", cursor_ok, repr(progress))

    # Red Rule T mutant: deleting the expiry predicate makes the self-test fail its exact 1/N
    # cursor claim. There are two production predicates; mutate only the supersede one.
    mutant = None
    try:
        mutant = _write_mutant("budget_expiry",
                               "if completed and _budget_expired(clock):",
                               "if False and _budget_expired(clock):", expected_count=2)
        mrc, mout = run(["--self-test"], mutant)
        rec("CS-T12-MUTANT-RULE-T-EXPIRY-DETECTED",
            mrc != 0 and "Rule T tiny-budget + genuine cursor: FAIL" in mout,
            "mutant rc=%s" % mrc)
    finally:
        if mutant is not None and mutant.exists():
            mutant.unlink()

    # Completion control and unchanged similarity semantics over the established synthetic
    # controls. No heat means no supersession; the hot/cold pair remains the same ranked result.
    full_progress = {}
    candidates = module.supersede_scan(corpus, index, _heat(), progress=full_progress)
    no_heat = module.supersede_scan(corpus, index, {})
    semantics_ok = (index.score("arn:x1", "arn:x2") == 0.0
                    and index.score("arn:old", "arn:new") == 1.0
                    and candidates[0]["candidate"] == "opal-data-legacyfeed"
                    and candidates[0]["replaced_by"] == "opal-data-assets"
                    and no_heat == [] and full_progress["completed"] == full_progress["total"]
                    and full_progress["partial"] is False)
    rec("CS-T12-SIMILARITY-SEMANTICS-AND-CLEAN-COMPLETION", semantics_ok,
        "scores=%s/%s progress=%r" %
        (index.score("arn:x1", "arn:x2"), index.score("arn:old", "arn:new"), full_progress))

    # D1-D3 vintage regression: production self-test covers UNKNOWN disclosure, real stderr
    # header capture, and a headerless negative control. Then a no-capture runtime mutant must
    # remain ABSENT, proving the arm would catch the 2026-09-02 stdout/stderr regression.
    vintage_ok = ("C3b disclosure" in self_out and "C3c vintage-CAPTURE" in self_out
                  and "compute=2/2 json=4/4 human=4/4 PASS" in self_out
                  and "parse=ok neg-control=ok PASS" in self_out)
    rec("CS-T12-D1-D3-VINTAGE-REGRESSION", vintage_ok, "C3b/C3c rc=%s" % rc)

    import summary_corpus as sc
    saved_vintage = dict(sc._CORPUS_VINTAGE)
    saved_capture = sc._capture_kuzu_vintage
    try:
        sc._CORPUS_VINTAGE.clear()
        sc._capture_kuzu_vintage = lambda _stderr: None
        sc._capture_kuzu_vintage(
            "DB: kuzu_nessie_db\nbuilt: 2026-09-02T14:20:11.113748+00:00 (age: 0.2h)\n")
        mutant_cov = module.coverage(corpus)
        detected = (mutant_cov["corpus_vintage_claim"] == "absent"
                    and "UNKNOWN" in mutant_cov["vintage_note"])
        rec("CS-T12-MUTANT-VINTAGE-CAPTURE-DROPPED-DETECTED", detected,
            mutant_cov["vintage_note"])
    finally:
        sc._capture_kuzu_vintage = saved_capture
        sc._CORPUS_VINTAGE.clear()
        sc._CORPUS_VINTAGE.update(saved_vintage)


def test_comp_similar_battery() -> None:
    _run_battery()
    failures = [(tid, detail) for tid, ok, detail in RESULTS if not ok]
    assert not failures, "\n".join("%s: %s" % item for item in failures)


if __name__ == "__main__":
    _run_battery()
    for tid, ok, detail in RESULTS:
        print("%-58s %s%s" % (tid, "PASS" if ok else "FAIL",
                              (" -- " + detail) if detail else ""))
    failed = [tid for tid, ok, _ in RESULTS if not ok]
    print("=== comp-similar battery: %s (%d/%d) ===" %
          ("PASS" if not failed else "FAIL", len(RESULTS) - len(failed), len(RESULTS)))
    raise SystemExit(1 if failed else 0)
