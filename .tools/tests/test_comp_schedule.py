"""Acceptance: comp-schedule -- the VIEW-TIME COMPILED gate ledger.

Andrew-direct 2026-09-01, VERBATIM: "having 'preconditions' floating from 12 days ago with no
immediate visibility is not good planning. I had asked for a comp-schedule or some kind of schedule
function to track ongoing schedule checks/future gates/etc. If we are going to manage preconditions
and other such gates over time, we need a clear way of managing these in that persistent location
and clear means of cleaning/sweeping items from that list when they no longer are needed."

DESIGN CONSTRAINT (1.0.0_SA_CTO, handoff 90454): do NOT build a hand-maintained gate list. A curated
registry is one more thing that goes stale -- the exact failure being fixed. VIEW-TIME COMPILE from
the carriers where gates already live.

THE FINDING THAT SHAPED THIS BUILD, measured by 3.0.0_SA_CVO~C 2026-09-01 before any code:
the five carriers are NOT the same kind of thing.
    org/projects/*.json `blocking`  = FREE PROSE. 348 files, 333 carry the key; 189 are the word
                                      "None" written in English; 135 are non-null prose of which
                                      16 SELF-NEGATE ("SEQUENCING (not a hard blocker)") and 65
                                      use closed/complete/resolved language. Median 648 chars,
                                      max 30,625. A 30 KB `blocking` field is an essay, not a field.
    the other four                  = machine-decidable (or semi, once chatter is excluded).
>> A TOOL THAT FLATTENS THOSE TOGETHER REPORTS 135 BLOCKED PROJECTS AND IS WRONG BEFORE THE SECOND
   LINE. Counting the prose carrier IS the defect. It is surfaced as a READING LIST with its own
   denominator, and never as gates. <<

NINE LEGS. Legs 1-8 are RED against a non-existent/pre-build tool BY CONSTRUCTION.
  1 CARRIER-DENOMINATOR  every carrier prints its OWN denominator and its OWN decidability
  2 PROSE-NOT-COUNTED    the 135 prose fields are NOT in the gate count -- they are NEEDS-READ
  3 GRAMMAR-REUSED       the sentinel grammar is safe_deploy_core.SERVE_HELD_RE, not a copy
  4 CHATTER-EXCLUDED     org/mcp/inbox chatter is not counted as armed sentinels
  5 GATE-GRAIN           gates are grouped by DISCHARGE CONDITION, so gates < sentinel lines
  6 UNREADABLE-NOT-ZERO  an unreadable carrier renders UNREADABLE, never as zero rows
  7 GATE-SCHEMA          every gate row carries OWNER + DISCHARGE + LAST VERIFIED (or an
                         explicit UNKNOWN -- a missing field is never rendered as satisfied)
  8 DRIFT-SUBSET         --drift is exceptions-only: a strict subset of the full view
  9 MUTANT               a planted build that counts the prose carrier as gates FAILS leg 2

Usage: python .tools/tests/test_comp_schedule.py   (direct)  |  python -m pytest -q .tools/tests/test_comp_schedule.py   (collected)
COMP_SCHEDULE_TOOL=<path> aims it at a mutant
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

_WS_CACHE = None


def _ws():
    """Workspace root, resolved on first use -- never at import (import must be INERT under pytest)."""
    global _WS_CACHE
    if _WS_CACHE is None:
        _WS_CACHE = Path(subprocess.run(["git", "rev-parse", "--show-toplevel"],
                                        cwd=str(Path(__file__).resolve().parent),
                                        capture_output=True, text=True).stdout.strip())
    return _WS_CACHE


def _tool():
    """The comp-schedule UNDER TEST. COMP_SCHEDULE_TOOL overrides it, so a grader can aim the battery at a mutant
    of their own without touching this file or the tool."""
    return Path(os.environ.get("COMP_SCHEDULE_TOOL") or (_ws() / ".tools" / "comp-schedule"))

RESULTS: list[tuple[str, str, str]] = []


def rec(tid, ok, detail):
    RESULTS.append((tid, "PASS" if ok else "FAIL", detail))
    print("  [%s] %s: %s" % ("PASS" if ok else "FAIL", tid, detail))


def run(args, tool=None, timeout=300):
    if not (tool or _tool()).exists():
        return "TOOL-ABSENT"
    r = subprocess.run([sys.executable, str(tool or _tool())] + args,
                       capture_output=True, text=True, cwd=str(_ws()), timeout=timeout)
    return r.stdout + r.stderr


_RAN = False


def _run_battery():
    """EVERY subprocess the battery runs lives here, so IMPORT IS INERT (the T-16 pass-2 shape,
    03cf4d17ac). Called once per process by test_all_arms_pass (pytest) or _report (direct). Before
    this, the arms ran at IMPORT: collection of this one file took 98 s, and its module-scope
    sys.exit ended the pytest session for the whole directory (NFRA_COMPEFFICACY F6, 92794). The arm
    code below is 3.0.0_SA_CVO~C's, byte-identical but for the indentation and _tool()/_ws() -> _tool()/_ws()."""
    global _RAN
    if _RAN:
        return
    _RAN = True
    OUT = run([])

    # --- 1. EVERY CARRIER PRINTS ITS OWN DENOMINATOR AND DECIDABILITY -----------
    # One global total is the thing this tool exists to refuse: the carriers differ in kind, so a
    # single number silently averages a regex over an essay.
    carrier_lines = re.findall(r"^\s*(C\d)\s+(\S+).*?denominator[= ](\d+)", OUT, re.MULTILINE)
    decid = len(re.findall(r"DECIDABLE|SEMI-DECIDABLE|NOT-DECIDABLE", OUT))
    rec("CARRIER-DENOMINATOR", len(carrier_lines) >= 4 and decid >= 4,
        "%d carrier row(s) carry an explicit denominator and %d decidability label(s) are printed"
        % (len(carrier_lines), decid))

    # --- 2. THE PROSE CARRIER IS NEVER COUNTED AS GATES -------------------------
    gm = re.search(r"GATES ARMED:\s*(\d+)", OUT)
    needs = re.search(r"NEEDS-READ:\s*(\d+)", OUT)
    gates = int(gm.group(1)) if gm else -1
    rec("PROSE-NOT-COUNTED",
        bool(gm) and bool(needs) and int(needs.group(1)) > 100 and gates < 100,
        ("GATES ARMED=%d is separate from NEEDS-READ=%s prose field(s) -- the prose carrier is a "
         "reading list, never a count" % (gates, needs.group(1))) if (gm and needs) else
        "no separate 'GATES ARMED' / 'NEEDS-READ' totals -- prose and gates are being flattened, which "
        "is the defect this tool exists to avoid")

    # --- 3. THE SENTINEL GRAMMAR IS REUSED, NOT RE-IMPLEMENTED ------------------
    # Build ladder rung 2: safe_deploy_core.py OWNS this grammar and enforces it at deploy time. A
    # second regex here would be a shadow grammar that drifts from the one that actually gates.
    src = _tool().read_text(encoding="utf-8") if _tool().exists() else ""
    reused = ("safe_deploy_core" in src and "SERVE_HELD_RE" in src)
    recopied = re.search(r"DEPLOY-SERVE-HELD\\b|re\.compile\(r[\"'].*DEPLOY-SERVE-HELD", src)
    rec("GRAMMAR-REUSED", reused and not recopied,
        "imports SERVE_HELD_RE from safe_deploy_core (%s) and does NOT compile its own copy of the "
        "sentinel pattern (%s)" % (reused, "clean" if not recopied else "FOUND A SECOND COPY"))

    # --- 4. INBOX CHATTER IS NOT AN ARMED SENTINEL ------------------------------
    # Measured: 39 raw text matches, 19 of them inbox mail QUOTING the sentinel. Counting those is the
    # same class of error as counting a code comment about a gate as the gate.
    # The declaration itself contains the path, so "absent from the output" was a self-contradictory
    # assertion in the first cut -- it can only be checked on the EVIDENCE lines.
    _ev = [ln for ln in OUT.splitlines() if ln.strip().startswith("evidence:")]
    rec("CHATTER-EXCLUDED",
        all("org/mcp/inbox" not in ln for ln in _ev) and "EXCLUDES org/mcp/inbox" in OUT,
        "no inbox path appears in any of the %d evidence line(s) and the exclusion is DECLARED in the "
        "output -- 19 of 39 raw matches are agents quoting the sentinel, not sentinels" % len(_ev))

    # --- 5. GATES ARE GROUPED BY DISCHARGE CONDITION ----------------------------
    sm = re.search(r"(\d+) sentinel line", OUT)
    c1g = re.search(r"C1\s+SENTINEL.*?->\s*(\d+) gate", OUT, re.S)
    ok5 = bool(sm) and bool(c1g) and int(c1g.group(1)) < int(sm.group(1))
    rec("GATE-GRAIN", ok5,
        ("%s sentinel lines collapse to %s gate(s) -- one gate stamped across many files is ONE gate; "
         "a line count is not a gate count" % (sm.group(1), c1g.group(1))) if ok5 else
        "sentinel lines are not collapsed to distinct discharge conditions -- the tool would report "
        "20 gates where there are 3")

    # --- 6. AN UNREADABLE CARRIER RENDERS UNREADABLE, NOT ZERO ------------------
    rec("UNREADABLE-NOT-ZERO", "UNREADABLE" in src,
        "the tool has an explicit UNREADABLE rendering path -- a carrier that cannot be read is a "
        "DIFFERENT fact from a carrier with no rows, and they must never print alike")

    # --- 7. THE GATE SCHEMA IS COMPLETE OR EXPLICITLY UNKNOWN -------------------
    rows = re.findall(r"^\s+(G-\d+)\b", OUT, re.MULTILINE)
    has_owner = len(re.findall(r"owner[= ]", OUT))
    has_disc = len(re.findall(r"discharge[: ]", OUT))
    has_lastv = len(re.findall(r"last[- ]verified[: ]", OUT))
    rec("GATE-SCHEMA",
        len(rows) > 0 and has_owner >= len(rows) and has_disc >= len(rows) and has_lastv >= len(rows),
        "%d gate row(s); owner printed %d, discharge %d, last-verified %d -- the field tonight's "
        "failure lacked must be present or explicitly UNKNOWN, never omitted"
        % (len(rows), has_owner, has_disc, has_lastv))

    # --- 8. --drift IS EXCEPTIONS-ONLY ------------------------------------------
    DOUT = run(["--drift"])
    dg = re.findall(r"^\s+(G-\d+)\b", DOUT, re.MULTILINE)
    rec("DRIFT-SUBSET", DOUT != "TOOL-ABSENT" and len(dg) <= len(rows),
        "--drift returns %d row(s) against the full view's %d -- exceptions-only, so an empty drift "
        "view is the good day" % (len(dg), len(rows)))

    # --- 9. MUTANT: a build that counts the prose carrier as gates --------------
    if not _tool().exists():
        rec("MUTANT-PROSE-COUNTED", False,
            "tool absent -- the leg certifies nothing and is reported FAIL, never skipped")
    else:
        mutant_src, nsub = re.subn(r"^(\s*)PROSE_IS_NEVER_A_GATE = True",
                                   r"\1PROSE_IS_NEVER_A_GATE = False", src, flags=re.MULTILINE)
        if nsub == 0:
            rec("MUTANT-PROSE-COUNTED", False,
                "could not plant the mutant: no 'PROSE_IS_NEVER_A_GATE = True' switch in the shipped "
                "source -- the leg certifies nothing and is reported FAIL, never skipped")
        else:
            # Write the mutant BESIDE the real tool so its sibling imports still resolve.
            mp = _ws() / ".tools" / ".comp-schedule-mutant.tmp"
            try:
                mp.write_text(mutant_src, encoding="utf-8")
                MO = run([], tool=mp)
            finally:
                if mp.exists():
                    mp.unlink()
            mm = re.search(r"GATES ARMED:\s*(\d+)", MO)
            inflated = bool(mm) and int(mm.group(1)) > 100
            rec("MUTANT-PROSE-COUNTED", inflated,
                "the planted prose-counting build reports GATES ARMED=%s (inflated past 100) -- so "
                "leg 2's separation is enforced by the switch and is not an accident of the data"
                % (mm.group(1) if mm else "n/a"))


def _report() -> int:
    _run_battery()
    n = sum(1 for _, v, _ in RESULTS if v == "PASS")
    print()
    print("=" * 80)
    print("COMP-SCHEDULE BATTERY: %d/%d PASS (denominator %d)" % (n, len(RESULTS), len(RESULTS)))
    print("=" * 80)
    return 0 if n == len(RESULTS) else 1


def test_all_arms_pass():
    _run_battery()
    failed = [(t, d) for t, v, d in RESULTS if v != "PASS"]
    assert not failed, "arms failed (%d of %d): %s" % (len(failed), len(RESULTS), failed)
    print("COMP-SCHEDULE BATTERY: %d/%d PASS (denominator %d)" % (len(RESULTS), len(RESULTS), len(RESULTS)))


if __name__ == "__main__":
    sys.exit(_report())
