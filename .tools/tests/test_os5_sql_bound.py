#!/usr/bin/env python3
"""NFRA_OUTSET.TO-OS-s-5 battery: `comp-heat federated --sql` is BOUNDED like every other
subcommand, or refused with its reason. An unbounded remote query is not a mode.

Run at both required file grains:
  python .tools/tests/test_os5_sql_bound.py
  python -m pytest -q .tools/tests/test_os5_sql_bound.py

WARN: THIS FILE DISPATCHES NOTHING TO THE LIVE TRINO PLANE, AND THAT IS A CHECKED PROPERTY.
Two mechanisms, and neither is "we were careful":
  1. Every arm that exercises the REFUSAL path uses the real tool with a --budget BELOW comp-heat's
     own FEDERATED_LIVE_FLOOR_S (200 s), so refuse-before-dispatch fires.
  2. Every arm that must get PAST that floor -- the whole point of this cell -- runs a TEMPORARY
     COPY of comp-heat in a tempfile directory beside a STUB `_trino_fed.py`. comp-heat resolves
     its transport with `sys.path.insert(0, _HERE)` where _HERE is its own directory, so the copy
     imports the STUB and the real transport is never reachable from those arms by construction.
  3. A final arm (Z) greps EVERY captured stdout+stderr in this run for the real transport's own
     dispatch banner ("launching in-VPC Trino query task") and fails if it ever appears. That is
     the falsifier for 1 and 2 rather than a restatement of them.

WHAT THE CELL FIXED. `_trino_fed.run_federated_query(sqls, *, delay=15, max_attempts=40)` bounds the
ECS tasks_stopped waiter at delay*max_attempts seconds. The wrapper called it with NEITHER, so every
dispatched query waited on a fixed 600 s ceiling that no --budget could shorten -- an arbitrary
remote query with the caller's ceiling not reaching the transport at all. The wrapper now derives
both from clock.remaining(). The RED mutant (arm G) puts the old call back and the battery catches
it by reading what the transport actually received.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TOOL = ROOT / ".tools" / "comp-heat"
HEATMAP = ROOT / "org" / "modules" / "heatmap"
LIVE_BANNER = "launching in-VPC Trino query task"
SQL = "SELECT 1"

# The mutation anchor: the line OS-s-5 added, whose removal restores the unbounded pre-cell call.
BOUND_ANCHOR = "        results = run_federated_query(qs, delay=delay, max_attempts=attempts)"
UNBOUND_MUTANT = "        results = run_federated_query(qs)  # RED MUTANT: pre-OS-s-5, unbounded"

RESULTS: list[tuple[str, bool, str]] = []
CAPTURED: list[str] = []          # every byte of every child process this battery ran


def _record(name: str, ok: bool, detail) -> None:
    RESULTS.append((name, ok, str(detail).replace("\n", " ")[:300]))


def _run_real(*args: str, timeout: int = 60):
    r = subprocess.run([sys.executable, str(TOOL), *args], cwd=str(ROOT), text=True,
                       capture_output=True, timeout=timeout)
    CAPTURED.append((r.stdout or "") + (r.stderr or ""))
    return r


STUB = '''"""STUB _trino_fed for the OS-s-5 battery. Dispatches NOTHING. Records the kwargs the
wrapper passed -- which is the only way to see whether the caller's budget reached the transport."""
import json, os, time

Q_CODE_BANDS = "SELECT 1 FROM iceberg.globgrph.graph_nodes g JOIN code_heat.globgrph.code_heat ch ON 1=1"
Q_CODE_COLDEST = "SELECT {top} FROM iceberg.globgrph.graph_nodes"


def run_federated_query(sqls, *, delay=15, max_attempts=40):
    with open(os.environ["OS5_STUB_LOG"], "w", encoding="utf-8") as fh:
        json.dump({"delay": delay, "max_attempts": max_attempts,
                   "ceiling_s": delay * max_attempts, "n_sqls": len(sqls)}, fh)
    mode = os.environ.get("OS5_STUB_MODE", "ok")
    if mode == "waiter":
        from botocore.exceptions import WaiterError
        raise WaiterError(name="TasksStopped", reason="Max attempts exceeded", last_response={})
    if mode == "slow":
        time.sleep(float(os.environ.get("OS5_STUB_SLEEP", "2")))
    return [{"sql": s, "columns": ["c"], "rows": [["1"]], "error": None} for s in sqls]


def render_table(res):
    return "c\\n-\\n1"
'''


def _stub_run(*args: str, mode: str = "ok", mutate: bool = False, timeout: int = 60):
    """Run a TEMPORARY COPY of comp-heat beside the STUB transport. Returns (proc, stub_record)."""
    src = TOOL.read_text(encoding="utf-8")
    if src.count(BOUND_ANCHOR) != 1:
        raise AssertionError("mutation anchor count != 1: %d" % src.count(BOUND_ANCHOR))
    if mutate:
        src = src.replace(BOUND_ANCHOR, UNBOUND_MUTANT, 1)
    tmp = tempfile.mkdtemp(prefix="os5-stub-")
    try:
        (Path(tmp) / "comp-heat").write_text(src, encoding="utf-8")
        (Path(tmp) / "_trino_fed.py").write_text(STUB, encoding="utf-8")
        shutil.copyfile(ROOT / ".tools" / "_compbudget.py", Path(tmp) / "_compbudget.py")
        # NAMED `rec_path`, not `log`: this is a SINGLE-WRITER record file written by the
        # stub in this same process tree, not a multi-writer append log. The commit gate
        # blocked the earlier `log = ...` name and it was RIGHT to -- the name was the
        # misleading part, so the name is what changed, not the strictness of the read.
        rec_path = str(Path(tmp) / "stub.json")
        env = dict(os.environ)
        env.update({"OS5_STUB_LOG": rec_path, "OS5_STUB_MODE": mode,
                    "COMP_HEATMAP_DIR": str(HEATMAP)})
        r = subprocess.run([sys.executable, str(Path(tmp) / "comp-heat"), *args], cwd=str(ROOT),
                           text=True, capture_output=True, timeout=timeout, env=env)
        CAPTURED.append((r.stdout or "") + (r.stderr or ""))
        rec = None
        if os.path.exists(rec_path):
            with open(rec_path, encoding="utf-8") as fh:
                rec = json.load(fh)
        return r, rec
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def _run_battery() -> None:                                                # noqa: C901
    if RESULTS:
        return

    # ---- ARM A: the order's own invocation -- refuses, and dispatches NOTHING ----
    a = _run_real("federated", "--sql", SQL, "--budget", "30", timeout=60)
    _record("A-AC1-INVOCATION-REFUSES-AND-DISPATCHES-NOTHING",
            a.returncode == 0 and "budget: 30 s (flag)" in a.stdout
            and "BUDGET REACHED:" in a.stdout
            and "refusing to dispatch to the LIVE Trino plane" in a.stdout
            and LIVE_BANNER not in (a.stdout + a.stderr),
            "rc=%d | %s | live-banner-absent=%s"
            % (a.returncode,
               next((ln for ln in a.stdout.splitlines() if ln.startswith("budget:")), ""),
               LIVE_BANNER not in (a.stdout + a.stderr)))

    # ---- ARM B: the --sql path specifically, at a near-zero budget (row W1-S2's race) ----
    b = _run_real("federated", "--sql", SQL, "--budget", "0.0001", timeout=60)
    _record("B-SQL-PATH-TINY-BUDGET-STILL-REFUSES",
            b.returncode == 0 and "refusing to dispatch to the LIVE Trino plane" in b.stdout
            and LIVE_BANNER not in (b.stdout + b.stderr),
            b.stdout.splitlines()[-1][:200] if b.stdout else b.stderr[:200])

    # ---- ARM C: the guard is NOMINAL, not elapsed-time -- W1-S2's actual claim, tested ----
    # 199.9 and 200.1 differ by 0.2 s of DECLARED budget and by nothing at all in wall-clock, so
    # only a nominal comparison can separate them. An elapsed-time check would treat them alike.
    c_lo = _run_real("federated", "--sql", SQL, "--budget", "199.9", timeout=60)
    c_hi, c_hi_rec = _stub_run("federated", "--sql", SQL, "--budget", "200.1", timeout=60)
    _record("C-FLOOR-IS-NOMINAL-NOT-ELAPSED-TIME",
            "refusing to dispatch" in c_lo.stdout
            and c_hi_rec is not None and "refusing to dispatch" not in c_hi.stdout,
            "--budget 199.9 -> refused (rc=%d) ; --budget 200.1 -> dispatched to the STUB "
            "(transport received %r). 0.2 s of nominal budget separates them; wall-clock does not"
            % (c_lo.returncode, c_hi_rec))

    # ---- ARM D: the waiter ceiling MOVES with the caller's budget ----
    # ASSERTED AS A PROPERTY, NOT AS A CONSTANT, and deliberately so. An earlier draft of this arm
    # hardcoded max_attempts==45 for --budget 250 and FAILED at 44: the ceiling derives from
    # clock.remaining() at the moment of dispatch, which is already a second or two below the
    # nominal budget because the disclosure and the vintage block ran first. The code was right and
    # the expectation was wrong. A constant here would also have had to be re-tuned by anyone who
    # added a line above the dispatch -- a brittle red that teaches re-tuning instead of reading.
    d1, d1_rec = _stub_run("federated", "--sql", SQL, "--budget", "250", timeout=60)
    d2, d2_rec = _stub_run("federated", "--sql", SQL, "--budget", "400", timeout=60)

    def _within(rec, budget, reserve=25.0, slack=15.0):
        """the ceiling never exceeds what the caller has left, and is not trivially small"""
        return rec is not None and 0 < rec["ceiling_s"] <= budget - reserve \
            and rec["ceiling_s"] >= budget - reserve - slack

    ok_d = (d1_rec is not None and d2_rec is not None
            and d1_rec["delay"] == 5 and d2_rec["delay"] == 5
            and _within(d1_rec, 250.0) and _within(d2_rec, 400.0)
            and d2_rec["ceiling_s"] > d1_rec["ceiling_s"]      # MONOTONE in the budget
            and d1_rec["ceiling_s"] < 600 and d2_rec["ceiling_s"] < 600
            and d1.returncode == 0 and d2.returncode == 0)
    _record("D-WAITER-CEILING-DERIVES-FROM-AND-MOVES-WITH-THE-BUDGET", ok_d,
            "--budget 250 -> transport received %r ; --budget 400 -> %r ; monotone=%s ; both under "
            "the pre-cell fixed 600 s (which the caller's budget could not shorten at all)"
            % (d1_rec, d2_rec,
               (d2_rec or {}).get("ceiling_s", 0) > (d1_rec or {}).get("ceiling_s", 0)))

    # ---- ARM E: --budget 0 means UNBOUNDED and the tool must not invent a ceiling ----
    e, e_rec = _stub_run("federated", "--sql", SQL, "--budget", "0", timeout=60)
    _record("E-UNBOUNDED-IS-HONOURED-AND-DISCLOSED",
            e_rec is not None and e_rec["delay"] == 15 and e_rec["max_attempts"] == 40
            and "caller asked for unbounded (--budget 0)" in e.stdout,
            "transport received %r ; disclosure line present=%s"
            % (e_rec, "caller asked for unbounded (--budget 0)" in e.stdout))

    # ---- ARM F: a waiter timeout is a BUDGET EVENT with a non-clean rc, not a traceback ----
    f, f_rec = _stub_run("federated", "--sql", SQL, "--budget", "250", mode="waiter", timeout=60)
    _record("F-WAITER-TIMEOUT-IS-A-BUDGET-EVENT-NOT-A-TRACEBACK",
            f.returncode == 3 and "BUDGET REACHED:" in f.stdout
            and "ANSWER-STATE: PARTIAL_OR_BLIND" in f.stdout
            and "results are NOT claimed" in f.stdout
            and "was NOT cancelled" in f.stdout
            and "Traceback" not in (f.stdout + f.stderr),
            "rc=%d (3 = PARTIAL_OR_BLIND; refuse-before-dispatch stays rc 0) | traceback-absent=%s"
            % (f.returncode, "Traceback" not in (f.stdout + f.stderr)))

    # ---- ARM G: RED MUTANT -- --sql dispatched UNBOUNDED, exactly as before this cell ----
    g, g_rec = _stub_run("federated", "--sql", SQL, "--budget", "250", mutate=True, timeout=60)
    _record("G-RED-MUTANT-SQL-RUNS-UNBOUNDED-AND-IS-CAUGHT",
            g_rec is not None and g_rec["delay"] == 15 and g_rec["max_attempts"] == 40
            and g_rec["ceiling_s"] == 600
            and d1_rec is not None and d1_rec["ceiling_s"] < 600,
            "mutant at --budget 250 -> transport received %r (the transport's OWN defaults, a "
            "fixed 600 s wait no --budget can shorten) vs production at the SAME budget -> %r"
            % (g_rec, d1_rec))

    _record("H-MUTATION-ANCHOR-UNIQUE",
            TOOL.read_text(encoding="utf-8").count(BOUND_ANCHOR) == 1,
            "exactly one occurrence of the bounded-dispatch call expected in .tools/comp-heat")

    # ---- ARM I: --help discloses the bound on the arbitrary-query path ----
    i = _run_real("federated", "--help", timeout=60)
    _record("I-HELP-DISCLOSES-THE-SQL-BOUND",
            i.returncode == 0 and "--sql" in i.stdout and "REFUSED before dispatch" in i.stdout,
            i.stdout[i.stdout.find("--sql"):][:200] if "--sql" in i.stdout else i.stdout[:200])

    # ---- ARM Z: the falsifier for this battery's own safety claim ----
    hits = [c for c in CAPTURED if LIVE_BANNER in c]
    _record("Z-NO-LIVE-TRINO-DISPATCH-BY-THIS-BATTERY",
            not hits and len(CAPTURED) >= 9,
            "swept %d captured child-process outputs for the real transport's own dispatch banner "
            "%r -- %d hit(s)" % (len(CAPTURED), LIVE_BANNER, len(hits)))


def _report() -> int:
    _run_battery()
    failed = [(n, d) for n, ok, d in RESULTS if not ok]
    for name, ok, detail in RESULTS:
        print("[%s] %s -- %s" % ("PASS" if ok else "FAIL", name, detail))
    print("OS5-SQL-BOUND BATTERY: %d/%d PASS (denominator %d; %d child runs, 0 live Trino "
          "dispatches -- arm Z is the check, not the claim)"
          % (len(RESULTS) - len(failed), len(RESULTS), len(RESULTS), len(CAPTURED)))
    return 1 if failed else 0


def test_all_arms_pass():
    _run_battery()
    failed = [(n, d) for n, ok, d in RESULTS if not ok]
    assert not failed, "comp-heat OS5 sql-bound battery failures: %r" % failed


if __name__ == "__main__":
    raise SystemExit(_report())
