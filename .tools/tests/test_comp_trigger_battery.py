"""Battery for org/modules/graph/comp_trigger.py (comp-trigger) -- NFRA_COMPEFFICACY TO-CE-T-9.

NEW FILE (0 files existed in .tools/tests/ for this tool at cut, per the TO's own measurement).

WHY EVERY ARM HERE IS FIXTURE-DRIVEN, NOT A LIVE AWS CALL: comp-trigger's public functions
(`live_rules`, `rule_targets`, `rule_fired`, `_enrich_matches`) all take a plain client-shaped
object as their first argument -- they never call `_clients()`/`boto3` themselves. This lets every
arm below inject a FAKE client (a small class with the one or two methods the function under test
actually calls) instead of racing live AWS latency or requiring live credentials in CI. The one
exception, ARM CT-AC4-HELP-DISCLOSES-BUDGET, spawns the real CLI as a subprocess -- `--help` is
pure argparse, zero AWS, zero live-latency risk.

ARM CT-AC5-LIVE-RULES-NO-CRASH is a REGRESSION arm for a REAL bug this cell found BY EXERCISE, not
by reading: before this fix, `live_rules()` had no try/except at all, so a tiny `--budget` (Rule
T's own new flag) produced a raw `ConnectTimeoutError` traceback and crashed the whole tool -- the
worst possible shape of the KILLED-OUTSIDE hazard Rule T exists to bound, and self-inflicted by
this very cell's own budget carrier rather than the harness's ceiling. `live_schedules()` already
had this exact try/except shape; `live_rules()` did not. Fixed to match.

Run: python .tools/tests/test_comp_trigger_battery.py    |    pytest -q .tools/tests/test_comp_trigger_battery.py
"""
from __future__ import annotations

import importlib.util
import os
import subprocess
import sys
import time
from pathlib import Path

RESULTS: list[tuple[str, bool | None, str]] = []
_WS_CACHE = None
_MOD = None


def _ws() -> Path:
    global _WS_CACHE
    if _WS_CACHE is None:
        _WS_CACHE = Path(subprocess.run(["git", "rev-parse", "--show-toplevel"],
                                        cwd=str(Path(__file__).resolve().parent),
                                        capture_output=True, text=True).stdout.strip())
    return _WS_CACHE


def _tool() -> Path:
    return _ws() / "org" / "modules" / "graph" / "comp_trigger.py"


def _mod():
    """Direct in-process import by path -- comp_trigger.py has no sibling-module imports of its
    own (only _compbudget via an explicit sys.path insert it does itself), so unlike comp-iam this
    needs no extra sys.path massaging to import cleanly."""
    global _MOD
    if _MOD is None:
        spec = importlib.util.spec_from_file_location("comp_trigger_battery_import", str(_tool()))
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        _MOD = m
    return _MOD


def rec(tid: str, ok: bool | None, detail: str = "") -> None:
    RESULTS.append((tid, ok, detail))


def run(args: list[str], tool: Path | None = None, timeout: int = 30) -> tuple[int, str]:
    r = subprocess.run([sys.executable, str(tool or _tool())] + args,
                       capture_output=True, text=True, timeout=timeout, cwd=str(_ws()))
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def _mutant_path(kind: str) -> Path:
    return _tool().parent / ("_tmp_trigger_mutant_%s_%d.py" % (kind, os.getpid()))


def _write_mutant(kind: str, needle: str, replacement: str) -> Path:
    src = _tool().read_text(encoding="utf-8")
    n = src.count(needle)
    assert n == 1, ("fixture assumption broken for mutant %r -- comp_trigger.py's source no "
                     "longer contains the targeted block exactly once (found %d)" % (kind, n))
    p = _mutant_path(kind)
    p.write_text(src.replace(needle, replacement, 1), encoding="utf-8")
    return p


class _FakeEvents:
    """Stands in for the boto3 'events' client. list_targets_by_rule is the only method
    rule_targets()/live_rules() (via a raising variant) needs."""
    def __init__(self, targets=None, delay=0.0):
        self.targets = targets or {}
        self.delay = delay
        self.calls = 0

    def list_targets_by_rule(self, Rule):
        self.calls += 1
        if self.delay:
            time.sleep(self.delay)
        return {"Targets": [{"Arn": a} for a in self.targets.get(Rule, [])]}


class _RaisingEvents:
    """list_rules always raises -- the exact live shape this cell's fix now catches."""
    def list_rules(self, **kw):
        raise TimeoutError("fake ConnectTimeoutError (battery specimen, no real network touched)")


class _FakeCW:
    def __init__(self, delay=0.0):
        self.delay = delay
        self.calls = 0

    def get_metric_statistics(self, **kw):
        self.calls += 1
        if self.delay:
            time.sleep(self.delay)
        return {"Datapoints": []}


def _fixture_matches(n=3):
    return [{"kind": "events-rule", "name": "fixture-rule-%d" % i, "state": "ENABLED",
             "schedule": "cron(0 0 * * ? *)", "pattern": "", "arn": "arn:aws:events:::rule/f%d" % i,
             "match": "name", "targets": None, "census_error": False}
            for i in range(n)]


def _run_battery() -> None:
    m = _mod()

    # ---------------- ARM 1: T9-AC3 scope line on both hit and miss ----------------
    hit = [{**_fixture_matches(1)[0], "fired": {"claim": "x"}, "tf_desired": []}]
    out_hit = m.render(hit, "fixture-rule-0", {"rules": 1, "schedules": 0, "region": "fixture"},
                       show_fired=True, show_tf=True)
    out_miss = m.render([], "zzz", {"rules": 1, "schedules": 0, "region": "fixture"})
    ok1 = ("S3 bucket notifications NOT scanned" in out_hit and "event_notifications" in out_hit
           and "S3 bucket notifications NOT scanned" in out_miss)
    rec("CT-AC3-SCOPE-LINE-ON-HIT-AND-MISS", ok1, "hit has scope=%s miss has scope=%s" %
        ("S3 bucket notifications NOT scanned" in out_hit, "S3 bucket notifications NOT scanned" in out_miss))

    # ---------------- ARM 2 (red-first): mutant drops the scope line from render() ----------------
    needle1 = (
        "         % denom,\n"
        "         SCOPE_LINE]\n"
    )
    replacement1 = (
        "         % denom]\n"  # MUTANT: SCOPE_LINE silently dropped from every answer
    )
    mutant1 = None
    try:
        mutant1 = _write_mutant("scope_dropped", needle1, replacement1)
        spec = importlib.util.spec_from_file_location("comp_trigger_mutant1", str(mutant1))
        mm = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mm)
        mout_hit = mm.render(hit, "fixture-rule-0", {"rules": 1, "schedules": 0, "region": "fixture"},
                             show_fired=True, show_tf=True)
        mout_miss = mm.render([], "zzz", {"rules": 1, "schedules": 0, "region": "fixture"})
        mutant_ok = ("S3 bucket notifications NOT scanned" in mout_hit
                    or "S3 bucket notifications NOT scanned" in mout_miss)
        rec("CT-AC3-MUTANT-SCOPE-LINE-DROPPED-DETECTED", not mutant_ok,
            "mutant output carries the scope line: %s (arm correctly detects its absence)" % mutant_ok)
    finally:
        if mutant1 is not None and mutant1.exists():
            mutant1.unlink()

    # ---------------- ARM 3: T9-AC4 --help discloses the Rule T carrier ----------------
    rc, out = run(["--help"])
    ok3 = rc == 0 and "_compbudget" not in out and "Rule T" in out and "COMP_BUDGET_S" in out
    rec("CT-AC4-HELP-DISCLOSES-BUDGET", ok3, out[-400:])

    # ---------------- ARM 4: T9-AC5 live_rules never crashes on a raising client ----------------
    ok4 = True
    detail4 = ""
    try:
        result = m.live_rules(_RaisingEvents())
        ok4 = (isinstance(result, list) and len(result) == 1
              and result[0].get("census_error") is True
              and "UNAVAILABLE" in result[0]["name"])
        detail4 = "returned %r" % result
    except Exception as exc:
        ok4 = False
        detail4 = "RAISED instead of returning a census_error sentinel: %r" % exc
    rec("CT-AC5-LIVE-RULES-NO-CRASH", ok4, detail4)

    # ---------------- ARM 5 (red-first): mutant removes live_rules' try/except (pre-fix shape) ----------------
    needle2 = (
        "    out, token = [], None\n"
        "    try:\n"
        "        while True:\n"
        "            kw = {\"NextToken\": token} if token else {}\n"
        "            resp = events.list_rules(**kw)\n"
        "            for r in resp.get(\"Rules\", []):\n"
        "                out.append({\n"
        "                    \"kind\": \"events-rule\",\n"
        "                    \"name\": r.get(\"Name\", \"\"),\n"
        "                    \"state\": r.get(\"State\", \"?\"),\n"
        "                    \"schedule\": r.get(\"ScheduleExpression\", \"\") or \"(event-pattern)\",\n"
        "                    \"pattern\": r.get(\"EventPattern\", \"\"),\n"
        "                    \"arn\": r.get(\"Arn\", \"\"),\n"
        "                })\n"
        "            token = resp.get(\"NextToken\")\n"
        "            if not token:\n"
        "                return out\n"
        "    except Exception as e:  # AWS-plane call under Rule T's ceiling -- reported, never a crash\n"
        "        return [{\"kind\": \"events-rule\", \"name\": \"(events census UNAVAILABLE: %s)\" % e,\n"
        "                 \"state\": \"UNKNOWN\", \"schedule\": \"\", \"pattern\": \"\", \"arn\": \"\", \"census_error\": True}]\n"
    )
    replacement2 = (
        "    out, token = [], None\n"
        "    while True:  # MUTANT: the try/except is gone -- the pre-fix, crash-prone shape\n"
        "        kw = {\"NextToken\": token} if token else {}\n"
        "        resp = events.list_rules(**kw)\n"
        "        for r in resp.get(\"Rules\", []):\n"
        "            out.append({\n"
        "                \"kind\": \"events-rule\",\n"
        "                \"name\": r.get(\"Name\", \"\"),\n"
        "                \"state\": r.get(\"State\", \"?\"),\n"
        "                \"schedule\": r.get(\"ScheduleExpression\", \"\") or \"(event-pattern)\",\n"
        "                \"pattern\": r.get(\"EventPattern\", \"\"),\n"
        "                \"arn\": r.get(\"Arn\", \"\"),\n"
        "            })\n"
        "        token = resp.get(\"NextToken\")\n"
        "        if not token:\n"
        "            return out\n"
    )
    mutant2 = None
    try:
        mutant2 = _write_mutant("crash_reintroduced", needle2, replacement2)
        spec = importlib.util.spec_from_file_location("comp_trigger_mutant2", str(mutant2))
        mm2 = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mm2)
        mutant_raised = False
        try:
            mm2.live_rules(_RaisingEvents())
        except Exception:
            mutant_raised = True
        rec("CT-AC5-MUTANT-CRASH-REINTRODUCED-DETECTED", mutant_raised,
            "mutant (try/except removed) raised=%s against the identical raising fake client "
            "production correctly swallows" % mutant_raised)
    finally:
        if mutant2 is not None and mutant2.exists():
            mutant2.unlink()

    # ---------------- ARM 6: T9-AC4/AC5 _enrich_matches WITHIN BUDGET on a generous budget ----------------
    matches6 = _fixture_matches(3)
    fake_events6, fake_cw6 = _FakeEvents(), _FakeCW()
    line6 = m._enrich_matches(matches6, fake_events6, fake_cw6, 7, 0, "test", query="x")["line"]
    ok6 = ("WITHIN BUDGET: scanned 3 of 3 match" in line6
          and all(mm6.get("fired") not in (None, "DEFERRED") for mm6 in matches6)
          and all(mm6.get("tf_desired") != "DEFERRED" for mm6 in matches6))
    rec("CT-AC5-ENRICH-WITHIN-BUDGET", ok6, line6)

    # ---------------- ARM 7: T9-AC4/AC5 _enrich_matches DEFERRED mid-sweep on a tiny budget ----------------
    matches7 = _fixture_matches(3)
    fake_events7, fake_cw7 = _FakeEvents(delay=0.12), _FakeCW(delay=0.12)
    line7 = m._enrich_matches(matches7, fake_events7, fake_cw7, 7, 0.05, "flag", query="x")["line"]
    n_deferred = sum(1 for mm7 in matches7 if mm7.get("fired") == "DEFERRED")
    ok7 = "BUDGET REACHED" in line7 and n_deferred >= 1
    rec("CT-AC5-ENRICH-DEFERRED-MID-SWEEP", ok7, "%s | %d of %d deferred" % (line7, n_deferred, len(matches7)))

    # ---------------- ARM 8 (red-first): mutant neuters _enrich_matches' remaining<=0 check ----------------
    needle3 = "        if remaining is not None and remaining <= 0:\n            exhausted_at = idx\n"
    replacement3 = "        if False and remaining is not None and remaining <= 0:  # MUTANT: budget check disabled\n            exhausted_at = idx\n"
    mutant3 = None
    try:
        mutant3 = _write_mutant("enrich_budget_ignored", needle3, replacement3)
        spec = importlib.util.spec_from_file_location("comp_trigger_mutant3", str(mutant3))
        mm3 = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mm3)
        matches8 = _fixture_matches(3)
        fake_events8, fake_cw8 = _FakeEvents(delay=0.12), _FakeCW(delay=0.12)
        line8 = mm3._enrich_matches(matches8, fake_events8, fake_cw8, 7, 0.05, "flag", query="x")["line"]
        n_deferred8 = sum(1 for mm8 in matches8 if mm8.get("fired") == "DEFERRED")
        mutant_ignored_budget = ("BUDGET REACHED" not in line8) and (n_deferred8 == 0)
        rec("CT-AC5-MUTANT-ENRICH-BUDGET-IGNORED-DETECTED", mutant_ignored_budget,
            "mutant line=%r n_deferred=%d (budget silently ignored, as expected of this mutant)" %
            (line8, n_deferred8))
    finally:
        if mutant3 is not None and mutant3.exists():
            mutant3.unlink()


def _report() -> int:
    _run_battery()
    fails = [r for r in RESULTS if r[1] is False]
    for tid, ok, detail in RESULTS:
        label = "SKIP" if ok is None else ("PASS" if ok else "FAIL")
        print("  [%s] %s%s" % (label, tid, "" if ok or ok is None else "  -- " + detail[:200]))
    n_scored = len([r for r in RESULTS if r[1] is not None])
    n_pass = n_scored - len(fails)
    print("COMP-TRIGGER BATTERY: %d/%d PASS (denominator %d, %d SKIP)"
          % (n_pass, n_scored, len(RESULTS), len(RESULTS) - n_scored))
    return 1 if fails else 0


def test_all_arms_pass():
    """pytest entry. Fails on any FAIL row; the denominator is len(RESULTS)."""
    _run_battery()
    fails = [(t, d) for t, ok, d in RESULTS if ok is False]
    assert not fails, "comp-trigger battery arms failed (%d of %d): %r" % (len(fails), len(RESULTS), fails)


if __name__ == "__main__":
    sys.exit(_report())
