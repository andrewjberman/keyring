"""Battery for .tools/comp-find -- NFRA_COMPEFFICACY unit 3b (3.0.0_SA_CVO 92758; lane TOOL_BATTERIES).

WHY THIS EXISTS: comp-find is the estate's primary search instrument (3,722 rail rows / 30d) and
had NO battery. Its contract is asserted here from a MEASURED run, not from its docstring:

    comp-find [content] '<pattern>'
      DENOMINATOR: N hit(s) across M file(s) scanned in scope [corpus=all] | ...
      BANDS (true totals, not this page): DEF=4      (or: none)
      PAGE i of j  (showing a of b)

IMPORT IS INERT (the T-16 lesson): every subprocess lives in _run_battery(), called once per
process by test_all_arms_pass (pytest) or _report (direct). `pytest --collect-only` runs no search.

THE TOOL UNDER TEST is chosen by path, never edited: COMP_FIND_TOOL overrides the binary so a
PRODUCTION MUTANT can be planted in a temp copy. TWO FIXTURE DEFECTS FOUND ON THE FIRST RUN AND
FIXED HERE, recorded because both are the "a fixture that cannot represent the failure cannot
score it" class:
  1. The ABSENT token was a string literal in THIS file, and this file lives inside the search
     scope -- so comp-find found it (1 hit across 357 files) and the false-zero arm could never
     pass. The token is now BUILT AT RUNTIME; no literal search can find it.
  2. A mutant copy in the system temp dir cannot `import _comprail` (a sibling module resolved
     relative to the tool's own directory), so it CRASHED -- and the mutant arm read the crash as
     PASS because "no denominator line" is true of a crash too. A DEAD ARM. The copy now lives
     BESIDE the real tool (sibling imports resolve) and the arm asserts the mutant RAN (rc 0, the
     tool's own header printed) AND lacks the denominator. A crash now reads FAIL, never PASS.

ARM F/G (added NFRA_COMPEFFICACY CE-t-1, Rule T -- PRD v0.3 s.4.4): before this cell, the
`--corpus aws` pull hard-coded timeout=600 against a 120s outer harness ceiling (5x over, nothing
at expiry said so). It is now `--budget-s` (caller-settable, default 100s). F exercises the
REAL ceiling on the PRODUCTION binary directly (no mutant needed to force it -- a tiny --budget-s
against a real pull is a genuine timeout, not a simulation) and asserts the DEFERRED disclosure is
printed and is TEXTUALLY DISTINCT from a clean "NO HITS" zero. G is the red-first control: a
mutant with the DEFERRED marker text neutered must still RUN (not crash) and FAIL F's own
predicate -- proving F is a live arm, not a dead one. BOTH SKIP (recorded, not silently omitted)
if this box has no local Kuzu DB/CLI to exercise (a fixture that cannot represent the failure
cannot score it -- stated, not silent).

Run: python .tools/tests/test_comp_find_battery.py    |    pytest -q .tools/tests/test_comp_find_battery.py
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

RESULTS: list[tuple[str, bool | None, str]] = []
_WS_CACHE = None
_RAN = False

SCOPE = ".tools"                      # small (~360 files), fast (~1 s), contains the tool itself
PRESENT = "def _self_report"          # defined in comp-find, comp-read, comp-adversary (DEF band)
AWS_PATTERN = "opal-gateway"          # a real, present AWS-corpus term (34 hits / 2100 nodes measured)
DENOM_RE = re.compile(r"DENOMINATOR: (\d+) hit\(s\) across (\d+) file\(s\) scanned")
PAGE_RE = re.compile(r"PAGE (\d+) of (\d+)\s+\(showing (\d+) of (\d+)\)")
HEADER_RE = re.compile(r"^comp-find \[(content|name)\]", re.M)
AWS_HEADER_RE = re.compile(r"^comp-find \[aws", re.M)
DEFERRED_MARKER = "DEFERRED: comp-kuzu pull did not return within the budget"


def _aws_exercisable() -> bool:
    """MOVE-2-style precondition, not an assumption: the CLI file and the default Kuzu DB path
    must both exist on THIS box, or --corpus aws cannot be exercised for real here."""
    cli = _ws() / "infra" / "aws" / "globgrph" / "kuzu_cli.py"
    if not cli.is_file():
        return False
    try:
        sys.path.insert(0, str(cli.parent))
        import kuzu_cli  # noqa: PLC0415
        return os.path.exists(kuzu_cli.DEFAULT_DB_PATH)
    except Exception:
        return False


def _absent_token() -> str:
    """Built at runtime from parts, so the token never exists as a literal anywhere in the corpus --
    including in this file, which is inside SCOPE. Fixture defect 1."""
    return "ZZZ" + "_NOSUCH_" + "%d" % os.getpid() + "_" + "0902"


def _ws() -> Path:
    global _WS_CACHE
    if _WS_CACHE is None:
        _WS_CACHE = Path(subprocess.run(["git", "rev-parse", "--show-toplevel"],
                                        cwd=str(Path(__file__).resolve().parent),
                                        capture_output=True, text=True).stdout.strip())
    return _WS_CACHE


def _tool() -> Path:
    """COMP_FIND_TOOL overrides the binary under test; unset = the real .tools/comp-find.
    The override MUST live inside .tools/ (comp-find imports its sibling _comprail by its own
    directory) -- a copy elsewhere crashes on import and proves nothing. Fixture defect 2."""
    return Path(os.environ.get("COMP_FIND_TOOL") or (_ws() / ".tools" / "comp-find"))


def rec(tid: str, ok: bool, detail: str = "") -> None:
    RESULTS.append((tid, bool(ok), detail))


def run(args: list[str], tool: Path | None = None) -> tuple[int, str]:
    r = subprocess.run([sys.executable, str(tool or _tool())] + args,
                       capture_output=True, text=True, timeout=120, cwd=str(_ws()))
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def _denom(out: str):
    m = DENOM_RE.search(out)
    return (int(m.group(1)), int(m.group(2))) if m else None


def _run_battery() -> None:
    global _RAN
    if _RAN:
        return
    _RAN = True

    # A1 -- a KNOWN-PRESENT token is found and the DENOMINATOR is printed with both numbers.
    rc, out = run([PRESENT, SCOPE, "--limit", "5"])
    d = _denom(out)
    rec("A1-PRESENT-FOUND", rc == 0 and d is not None and d[0] >= 1 and d[1] > 0, "rc=%s denom=%s" % (rc, d))
    # A2 -- the hit lands in the DEF band and the BANDS line is printed.
    rec("A2-DEF-BAND", "BANDS (true totals, not this page):" in out and "DEF=" in out and "[DEF]" in out, out[:300])
    # A3 -- THE FALSE-ZERO DISCRIMINATOR: an ABSENT token reports 0 hits across N>0 files SCANNED.
    #       A bare grep hands you '0' with no denominator; this line is what the tool exists to print.
    rc, out = run([_absent_token(), SCOPE])
    d = _denom(out)
    rec("A3-ABSENT-IS-MEASURED-ZERO", rc == 0 and d is not None and d[0] == 0 and d[1] > 0, "rc=%s denom=%s" % (rc, d))
    # A4 -- --name mode finds a file by BASENAME (content mode structurally cannot return the file
    #       whose name you typed unless that file also mentions its own name -- 2026-09-01 finding).
    rc, out = run(["--name", "comp-find", SCOPE])
    rec("A4-NAME-MODE-BASENAME", rc == 0 and ".tools/comp-find" in out and "[HEAD]" in out, out[:300])
    # A5 -- the PAGE line is printed and 'showing a of b' is consistent (a <= b, i <= j).
    rc, out = run([PRESENT, SCOPE, "--limit", "2"])
    m = PAGE_RE.search(out)
    rec("A5-PAGE-CONTRACT", m is not None and int(m.group(3)) <= int(m.group(4)) and int(m.group(1)) <= int(m.group(2)), out[:300])

    # E -- MUTANT: a copy of the tool BESIDE the real one, with the DENOMINATOR print neutered, must
    #      RUN (rc 0, its own header printed -- a crash is a DEAD arm, not a pass) and FAIL A1's predicate.
    src = _tool().read_text(encoding="utf-8", errors="replace")
    needle = "DENOMINATOR:"
    mp = _ws() / ".tools" / (".mutant-comp-find-%d" % os.getpid())
    if src.count(needle) == 0:
        rec("E-MUTANT-NO-DENOMINATOR", False, "mutation anchor absent from the tool under test")
    else:
        try:
            mp.write_text(src.replace(needle, "DENOMINATOR-MUTATED:"), encoding="utf-8")
            rc, out = run([PRESENT, SCOPE, "--limit", "5"], tool=mp)
            ran = rc == 0 and HEADER_RE.search(out) is not None
            rec("E-MUTANT-NO-DENOMINATOR", ran and _denom(out) is None,
                ("mutant did not RUN (rc=%s, header=%s) -> DEAD arm, not a pass" % (rc, bool(HEADER_RE.search(out))))
                if not ran else ("mutant still printed a denominator -> arm A1 is DEAD" if _denom(out) else "mutant ran and fails A1: OK"))
        finally:
            try:
                mp.unlink()
            except OSError:
                pass

    # F/G -- RULE T (CE-t-1): the --corpus aws budget ceiling and its expiry disclosure.
    if not _aws_exercisable():
        skip = "SKIP: no local Kuzu CLI/DB on this box -- --corpus aws not exercisable here"
        rec("F-CEILING-DEFERRED", None, skip)
        rec("G-MUTANT-NO-DEFERRED", None, skip)
        return

    # F -- driven past its ceiling on the REAL PRODUCTION BINARY (no mutant needed: the ceiling
    # is now a caller-supplied flag, not a hard-coded constant, so exercising it touches no bytes
    # and production sha is trivially unchanged -- itself evidence Rule T is doing its job).
    rc, out = run(["--corpus", "aws", AWS_PATTERN, "--budget-s", "0.001"])
    deferred_ok = (rc == 0 and DEFERRED_MARKER in out and "DENOMINATOR:" not in out
                   and "NO HITS" not in out)
    rec("F-CEILING-DEFERRED", deferred_ok, "rc=%s deferred_marker=%s" % (rc, DEFERRED_MARKER in out))

    # SIDE-BY-SIDE CONTROL: a clean empty must NOT be able to produce the same line (T1-AC3).
    rc0, out0 = run(["--corpus", "aws", "ZZZ_NOSUCH_AWS_TERM_%d" % os.getpid()])
    rec("F2-CLEAN-EMPTY-DIFFERS", rc0 == 0 and DEFERRED_MARKER not in out0 and "NO HITS" in out0,
        "rc=%s" % rc0)

    # G -- MUTANT, red-first: neuter the DEFERRED marker text in a copy beside the real tool.
    # Must RUN (rc 0, its own aws header printed -- a crash is a DEAD arm, not a pass) and FAIL
    # F's own predicate (the marker must be ABSENT).
    src = _tool().read_text(encoding="utf-8", errors="replace")
    mp2 = _ws() / ".tools" / (".mutant-comp-find-ceiling-%d" % os.getpid())
    if src.count(DEFERRED_MARKER) == 0:
        rec("G-MUTANT-NO-DEFERRED", False, "mutation anchor absent from the tool under test")
    else:
        try:
            mp2.write_text(src.replace(DEFERRED_MARKER, "MUTATED: no longer says DEFERRED"),
                           encoding="utf-8")
            rc, out = run(["--corpus", "aws", AWS_PATTERN, "--budget-s", "0.001"], tool=mp2)
            ran = rc == 0 and AWS_HEADER_RE.search(out) is not None
            rec("G-MUTANT-NO-DEFERRED", ran and DEFERRED_MARKER not in out,
                ("mutant did not RUN (rc=%s, header=%s) -> DEAD arm, not a pass"
                 % (rc, bool(AWS_HEADER_RE.search(out)))) if not ran
                else ("mutant still printed the DEFERRED marker -> arm F is DEAD" if DEFERRED_MARKER in out
                      else "mutant ran and lacks the marker: OK"))
        finally:
            try:
                mp2.unlink()
            except OSError:
                pass


def _report() -> int:
    """PRE-EXISTING GAP FIXED HERE: the RESULTS type was declared `bool | None` (None = SKIP,
    neither pass nor fail) since this file's first version, but this printer had no branch for
    it -- `"PASS" if ok else "FAIL"` renders a None row as FAIL even though the fails-count below
    correctly excludes it. Never fired before F/G (the first arms to use None); fixed on first use
    rather than left to misrender silently."""
    _run_battery()
    fails = [r for r in RESULTS if r[1] is False]
    for tid, ok, detail in RESULTS:
        label = "SKIP" if ok is None else ("PASS" if ok else "FAIL")
        print("  [%s] %s%s" % (label, tid, "" if ok or ok is None else "  -- " + detail[:160]))
    print("COMP-FIND BATTERY: %d/%d PASS (denominator %d)" % (len(RESULTS) - len(fails), len(RESULTS), len(RESULTS)))
    return 1 if fails else 0


def test_all_arms_pass():
    """pytest entry. Fails on any FAIL row; the denominator is len(RESULTS)."""
    _run_battery()
    fails = [(t, d) for t, ok, d in RESULTS if ok is False]
    assert not fails, "comp-find battery arms failed (%d of %d): %r" % (len(fails), len(RESULTS), fails)


if __name__ == "__main__":
    sys.exit(_report())
