#!/usr/bin/env python3
"""SEATING LINT battery -- one project per tier-2 seat instance.

Subject: `.tools/to-decomp-ref-lint.py` `seating_check()`. Authorized Andrew-direct
2026-08-25 ~00:2xZ ("Yeah thats fine you can build it"); rule from his 2026-08-24 ~19:29Z
word. Built by `0.8.0_AE_CloudComp~F`.

    THE ARM THAT MATTERS MOST HERE IS ARM 4, AND IT EXISTS BECAUSE I SHIPPED THE BUG.

My first cut harvested every serial in `<issued_to>` and treated each as the assignee. On the
live ADVI_STITCH TO that pulled `0.7.0_AE_CloudOps~G` out of the sentence "AND EXPLICITLY NOT
THE PERFRP LANE'S: `0.7.0_AE_CloudOps~G` holds ADVI_PERFRP" -- an EXCLUSION -- and accused ~G
of being multi-project. That is the SAME INVERSION CLASS I had fixed in gate 1 four hours
earlier, reintroduced in the next gate I built. It was caught only because to-check.py
disagreed and I checked the disagreement instead of trusting my own tool's first output.
ARM 4 is that exact sentence, frozen, so the class cannot come back silently.

Run: python .tools/tests/test_seating_lint.py
Exit 0 = all arms as expected. Exit 1 = at least one arm did not.
"""
from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
LINT = TOOLS / "to-decomp-ref-lint.py"

PASS, FAIL = "PASS", "FAIL"
results: list[tuple[str, str, str]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    results.append((name, PASS if ok else FAIL, detail))


def _load():
    spec = importlib.util.spec_from_file_location("lint_mod", LINT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


TO = """# TO {code}.{tid}
<task_order id="{code}.{tid}" project="{code}">
<issued_to>{issued}</issued_to>
<status>{status}</status>
</task_order>
"""


def _ws(tmp: Path, tos: list) -> Path:
    """tos = [(code, tid, issued_to_text, status, registered)]"""
    (tmp / "org" / "projects").mkdir(parents=True, exist_ok=True)
    d = tmp / "org" / "tier2_senior" / "seat" / "task_orders"
    d.mkdir(parents=True, exist_ok=True)
    for code, tid, issued, status, reg in tos:
        body = {"code": code, "status": "active"}
        if reg:
            body["dep_stage"] = "EXECUTING"
        (tmp / "org" / "projects" / f"{code}.json").write_text(
            json.dumps(body), encoding="utf-8")
        (d / f"{code}.{tid}.fixture.md").write_text(
            TO.format(code=code, tid=tid, issued=issued, status=status), encoding="utf-8")
    _commit_fixtures(tmp)
    return d


def _git(ws: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", "-c", "user.name=battery", "-c", "user.email=battery@opal.agent", *args],
        cwd=ws, capture_output=True, text=True)


def _commit_fixtures(ws: Path) -> None:
    """The prior TOs must be TRACKED, because the gate now reads committed state only.

    Fixing the FIXTURE rather than the check: pointing the tracked-state read at the live
    repo would test a path production never takes AND destroy the sealed property. Same
    call as the vintage repair, and the reason the batteries stay independently re-runnable.
    """
    _git(ws, "init", "-q")
    _git(ws, "add", "-A")
    _git(ws, "commit", "-q", "-m", "fixture corpus")


def _subject(tmp: Path, code: str, tid: str, issued: str):
    rel = f"org/tier2_senior/seat/task_orders/{code}.{tid}.fixture.md"
    text = TO.format(code=code, tid=tid, issued=issued, status="ACTIVE")
    (tmp / rel).write_text(text, encoding="utf-8")
    return [(rel, code, text)]


def main() -> int:
    mod = _load()
    if mod._to_check_resolver() is None:
        print("  FAIL  to-check.py resolver did not load -- battery cannot run")
        return 1

    # ---- ARM 1: multi-project instance -> REFUSED ----
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        mod.WORKSPACE = tmp
        mod.PROJECTS = tmp / "org" / "projects"
        _ws(tmp, [("PROJA", "TO-1", "0.9.9_XX_Fixture~A", "ACTIVE", True)])
        subj = _subject(tmp, "PROJB", "TO-1", "0.9.9_XX_Fixture~A")
        v, f = mod.seating_check(subj)
        check("multi-project instance -> REFUSED",
              any("SEATING:" in x and "PROJA" in x for x in v), str(v)[:160])
        check("refusal names the FIX (fresh lane)",
              any("FRESH LANE" in x for x in v), str(v)[:160])

    # ---- ARM 2: SAME project -> legal (the rule is one PROJECT, not one TO) ----
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        mod.WORKSPACE = tmp
        mod.PROJECTS = tmp / "org" / "projects"
        _ws(tmp, [("PROJA", "TO-1", "0.9.9_XX_Fixture~A", "ACTIVE", True)])
        v, f = mod.seating_check(_subject(tmp, "PROJA", "TO-2", "0.9.9_XX_Fixture~A"))
        check("second TO on the SAME project -> legal", not v, str(v)[:160])

    # ---- ARM 3: FRESH LANE passes BY CONSTRUCTION ----
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        mod.WORKSPACE = tmp
        mod.PROJECTS = tmp / "org" / "projects"
        _ws(tmp, [("PROJA", "TO-1", "0.9.9_XX_Fixture~A", "ACTIVE", True)])
        v, f = mod.seating_check(_subject(tmp, "PROJB", "TO-1", "0.9.9_XX_Fixture~B"))
        check("fresh lane ~B -> legal by construction", not v, str(v)[:160])

    # ---- ARM 4: THE REGRESSION ARM -- an EXCLUSION sentence must never accuse ----
    # Verbatim shape from the live ADVI_STITCH TO that my first cut mis-read.
    exclusion = ("AE-class (cloud/IAM). Seated: a FRESH `0.9.9_XX_Fixture~<letter>` for PROJB "
                 "ONLY. AND EXPLICITLY NOT THE PROJA LANE'S: `0.9.9_XX_Fixture~A` holds PROJA "
                 "and one project per instance binds.")
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        mod.WORKSPACE = tmp
        mod.PROJECTS = tmp / "org" / "projects"
        _ws(tmp, [("PROJA", "TO-1", "0.9.9_XX_Fixture~A", "ACTIVE", True)])
        v, f = mod.seating_check(_subject(tmp, "PROJB", "TO-1", exclusion))
        check("EXCLUSION prose does NOT produce an accusation", not v, str(v)[:200])
        check("EXCLUSION prose reports NOT EVALUATED with its reason",
              any("NOT EVALUATED" in x for x in f), str(f)[:200])
        # the mutation control: the same field WITHOUT the exclusion sentence, bare serial,
        # MUST refuse -- otherwise ARM 4 passes merely because the check is inert.
        v2, _ = mod.seating_check(_subject(tmp, "PROJB", "TO-2", "0.9.9_XX_Fixture~A"))
        check("...and the bare-serial control on the same fixture DOES refuse",
              bool(v2), "check may be inert: " + str(v2)[:120])

    # ---- ARM 5: a TERMINAL-status holding does not occupy the seat ----
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        mod.WORKSPACE = tmp
        mod.PROJECTS = tmp / "org" / "projects"
        _ws(tmp, [("PROJA", "TO-1", "0.9.9_XX_Fixture~A",
                   "COMPLETE -- CLOSED 2026-08-24", True)])
        v, f = mod.seating_check(_subject(tmp, "PROJB", "TO-1", "0.9.9_XX_Fixture~A"))
        check("COMPLETE holding does not occupy -> legal", not v, str(v)[:160])

    # ---- ARM 6: a NON-pipeline holding does not occupy (the legacy-heap scope) ----
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        mod.WORKSPACE = tmp
        mod.PROJECTS = tmp / "org" / "projects"
        _ws(tmp, [("PROJA", "TO-1", "0.9.9_XX_Fixture~A", "ACTIVE", False)])
        v, f = mod.seating_check(_subject(tmp, "PROJB", "TO-1", "0.9.9_XX_Fixture~A"))
        check("non-pipeline holding does not occupy -> legal", not v, str(v)[:160])

    # ---- ARM 7: unknown status counts as OPEN (fail-closed) ----
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        mod.WORKSPACE = tmp
        mod.PROJECTS = tmp / "org" / "projects"
        _ws(tmp, [("PROJA", "TO-1", "0.9.9_XX_Fixture~A", "WAITING-ON-SOMETHING", True)])
        v, f = mod.seating_check(_subject(tmp, "PROJB", "TO-1", "0.9.9_XX_Fixture~A"))
        check("unknown status treated as OPEN (fail-closed) -> REFUSED", bool(v), str(v)[:160])

    # ---- ARM 8: COMMITTED-STATE FILTER (COO 67721/67951) -- the PAIRED control ----
    # The SAME holding file, tracked vs untracked, must give DIFFERENT verdicts. Without the
    # pair this arm could pass merely because the corpus is empty for some other reason --
    # which is exactly how the seating check was inert for its first hour.
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        mod.WORKSPACE = tmp
        mod.PROJECTS = tmp / "org" / "projects"
        mod._TRACKED_TOS = None
        _ws(tmp, [("PROJA", "TO-1", "0.9.9_XX_Fixture~A", "ACTIVE", True)])   # commits it
        v_tracked, _ = mod.seating_check(_subject(tmp, "PROJB", "TO-1", "0.9.9_XX_Fixture~A"))
        # now add an UNTRACKED second holding on a THIRD project -- a peer's in-flight draft
        extra = tmp / "org" / "tier2_senior" / "seat" / "task_orders" / "PROJC.TO-1.fixture.md"
        (tmp / "org" / "projects" / "PROJC.json").write_text(
            json.dumps({"code": "PROJC", "status": "active", "dep_stage": "EXECUTING"}),
            encoding="utf-8")
        extra.write_text(TO.format(code="PROJC", tid="TO-1",
                                   issued="0.9.9_XX_Fixture~A", status="ACTIVE"),
                         encoding="utf-8")
        mod._TRACKED_TOS = None
        v_untracked, f_u = mod.seating_check(
            _subject(tmp, "PROJB", "TO-2", "0.9.9_XX_Fixture~A"))
        check("committed holding still counts (filter is not inert)", bool(v_tracked),
              str(v_tracked)[:120])
        check("UNTRACKED peer draft does NOT become a holding",
              not any("PROJC" in x for x in v_untracked), str(v_untracked)[:160])
        check("the skip is COUNTED in the frame, not silent",
              any("untracked in-flight file(s) SKIPPED" in x for x in f_u), str(f_u)[:200])

    width = max(len(n) for n, _, _ in results)
    for name, verdict, detail in results:
        line = f"  {verdict:4s} {name.ljust(width)}"
        if verdict == FAIL and detail:
            line += f"   <- {detail}"
        print(line)
    failed = [r for r in results if r[1] == FAIL]
    print(f"\nseating lint battery: {len(results) - len(failed)}/{len(results)} arms as expected")
    if failed:
        print("BATTERY FAILED -- the gate does not behave as specified.")
        return 1
    print("BATTERY PASS -- refuses a real multi-project seating, passes four legal shapes, "
          "and ARM 4 holds the inversion class shut with its own non-inertness control.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
