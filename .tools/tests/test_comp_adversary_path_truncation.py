"""Acceptance: comp-adversary's path extractor does not TRUNCATE, censused over org/.

Andrew-PRIORITIZED 2026-08-20, VERBATIM: "truncated outputs is a very risky error type and one
we've seen crop up many times."

THE DEFECT: PATH_RE's trailing \\b was satisfied by the FIRST dot-segment that could pass as an
extension, so a bare serial-named directory truncated rather than not matching --
"org/tier2_senior/0.8.0_AE_CloudComp" extracted as "org/tier2_senior/0.8", which does not exist,
so source 2 emitted a confident GONE about a path nobody cited.

THE ACCEPTANCE MSTR/COO NAMED, implemented literally: a path census over org/ -- where EVERY
serial-named directory carries dots -- pinning 100% correctly, with the measured false-GONE cases
as regression fixtures.

Four legs, and two of them must behave in ways a naive "extract more" fix would break:
  1. CENSUS         every real file under org/ round-trips: cited -> extracted -> same path
  2. FIXTURES       the 4 measured false-GONE shapes no longer truncate
  3. DIRECTORY      a bare directory yields NO match (it is not a file citation) -- NOT a
                    truncated one. A fix that merely widened the regex would extract garbage here.
  4. MUTANT         the OLD pattern still truncates the fixtures, proving the census would have
                    FAILED before the fix. Without this, leg 1 could pass on a corpus that never
                    exercised the defect.

Usage: python .tools/tests/test_comp_adversary_path_truncation.py
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

OLD_RE = re.compile(
    r"\b((?:org|docs|infra|data|portal|rcg|workflows)/[A-Za-z0-9_\-./~]+\.[A-Za-z0-9]{1,6})\b")


def shipped_pattern() -> re.Pattern:
    """Read PATH_RE from the SHIPPED tool, never a copy. A test carrying its own copy of the
    pattern measures the copy -- the tool could regress and this would stay green."""
    src = (_ws() / ".tools" / "comp-adversary").read_text(encoding="utf-8")
    m = re.search(r"^PATH_RE = re\.compile\(r\"(.+)\"\)$", src, re.MULTILINE)
    if not m:
        raise SystemExit("could not read PATH_RE from the shipped comp-adversary")
    return re.compile(m.group(1))


RESULTS: list[tuple[str, str, str]] = []


def rec(tid, ok, detail):
    RESULTS.append((tid, "PASS" if ok else "FAIL", detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {tid}: {detail}")


_RAN = False


def _run_battery():
    """EVERY piece of work the battery does lives here, so IMPORT IS INERT (the T-16 pass-2 shape,
    03cf4d17ac; NFRA_COMPEFFICACY F6, 92794). Called once per process by test_all_arms_pass (pytest)
    or _report (direct). Before this, NEW_RE was read from the shipped tool at import (a SystemExit path) and the census walked org/ at import."""
    global _RAN
    if _RAN:
        return
    _RAN = True
    NEW_RE = shipped_pattern()

    # --- 1. THE CENSUS over org/ -------------------------------------------------
    files = []
    for root, dirs, names in os.walk(_ws() / "org"):
        dirs[:] = [d for d in dirs if d not in (".git", "__pycache__", "read")]
        for n in names:
            rel = os.path.relpath(os.path.join(root, n), _ws()).replace("\\", "/")
            if re.fullmatch(r"[A-Za-z0-9_\-./~]+\.[A-Za-z0-9]{1,6}", rel):
                files.append(rel)

    dotted = [f for f in files if re.search(r"/\d+\.\d+\.\d+", f)]   # serial-named dirs
    exact, truncated, missed = 0, [], []
    for f in files:
        hits = NEW_RE.findall(f"see {f} for detail")
        if hits == [f]:
            exact += 1
        elif hits and hits[0] != f:
            truncated.append((f, hits[0]))
        else:
            missed.append(f)

    rec("CENSUS-100PCT", not truncated and exact == len(files),
        f"{exact}/{len(files)} files under org/ pin EXACTLY "
        f"({len(dotted)} of them under serial-named dirs carrying dots); "
        f"{len(truncated)} truncated, {len(missed)} unmatched")
    if truncated[:3]:
        for f, h in truncated[:3]:
            print(f"        TRUNCATED {f} -> {h}")

    # --- 2. THE MEASURED FIXTURES ------------------------------------------------
    FIXTURES = [
        "the seat folder org/tier2_senior/0.8.0_AE_CloudComp holds the TOs",
        "see org/tier1_exec/1.0.0_SA_CTO for the deliverables",
        "under org/tier2_senior/0.8.0_AE_CloudComp/task_orders/ there are 17",
        "inbox at org/mcp/inbox/0.4.0_DS_ClientPlatform",
    ]
    bad = [(t, NEW_RE.findall(t)) for t in FIXTURES
           if any(not os.path.exists(_ws() / h) for h in NEW_RE.findall(t))]
    rec("FIXTURES-NO-FALSE-GONE", not bad,
        f"{len(FIXTURES)}/{len(FIXTURES)} measured false-GONE shapes now extract nothing that fails to "
        f"exist (was 4/4 FALSE GONE before the fix)")

    # --- 3. A BARE DIRECTORY IS NOT A FILE CITATION ------------------------------
    d = "the seat folder org/tier2_senior/0.8.0_AE_CloudComp holds the TOs"
    rec("DIRECTORY-NO-MATCH", NEW_RE.findall(d) == [],
        "a bare serial directory yields NO match -- correct, it is not a file citation. A fix that "
        "merely widened the pattern would extract a directory here and then report it GONE-or-worse")

    # --- 4. MUTANT: the OLD pattern still truncates -------------------------------
    old_bad = sum(1 for t in FIXTURES
                  if any(not os.path.exists(_ws() / h) for h in OLD_RE.findall(t)))
    rec("MUTANT-OLD-TRUNCATES", old_bad == len(FIXTURES),
        f"the PRE-FIX pattern still produces {old_bad}/{len(FIXTURES)} false GONEs on the same "
        f"fixtures -- so the census above is a real result, not a corpus that never exercised the defect")


def _report() -> int:
    _run_battery()
    n = sum(1 for _, v, _ in RESULTS if v == "PASS")
    print()
    print("=" * 80)
    print("PATH-TRUNCATION BATTERY: %d/%d PASS (denominator %d)" % (n, len(RESULTS), len(RESULTS)))
    print("=" * 80)
    return 0 if n == len(RESULTS) else 1


def test_all_arms_pass():
    _run_battery()
    failed = [(t, d) for t, v, d in RESULTS if v != "PASS"]
    assert not failed, "arms failed (%d of %d): %s" % (len(failed), len(RESULTS), failed)
    print("PATH-TRUNCATION BATTERY: %d/%d PASS (denominator %d)" % (len(RESULTS), len(RESULTS), len(RESULTS)))


if __name__ == "__main__":
    sys.exit(_report())
