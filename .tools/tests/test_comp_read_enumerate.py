"""Acceptance: comp-read --enumerate -- comp-find's efficacy properties at FILE-CONTENT grain.

Brief: org/tier1_exec/3.0.0_SA_CVO/deliverables/SPAWN_BRIEF_CVO_C_COMP_READ_ENUMERATE_20260901.md
Andrew-direct 2026-09-01 ~00:4xZ, VERBATIM: "It should enumerate, how can we make it do that? It
should have the same efficacy as comp-find just at the file-content level."

WHY IT EXISTS, MEASURED: org/mcp/comp-which-rail.log carries 1,021 `ALLOW-SEARCH shape=single-file`
rows over ~3 days (~340/day) -- file-internal reading done through raw grep, with no denominator, no
bands and no false-zero protection. The carve-out existed because no comp-tool covered file
internals.

TEN LEGS. Legs 1-6 are RED against the pre-build binary BY CONSTRUCTION (the mode is absent).
  1 DENOMINATOR      every run prints hits across LINES / SECTIONS scanned
  2 BAND-CONSERVATION per-band counts SUM to the total, over 3 DIFFERENT backends (Rule 24 (i))
  3 ANCHOR-ARM       the real 14.9 MB specimen: whole-value 0 / substring >0, never a bare 0
  4 ZERO-DENOMINATOR an absent pattern prints 0 WITH its denominator, never silence
  5 HONEST-DEGRADE   a no-structure backend says banding UNAVAILABLE and emits ONE band --
                     never a row of 0s implying the distinction was tested
  6 PAGINATION       over-page hit sets show page, total, and how to get the rest
  7 MUTANT           a planted build with the band classifier neutered FAILS leg 2
  8 CONSUMER         comp-adversary (a live consumer of the DEFAULT digest) is untouched
  9 BUDGET-CARRIER    (NFRA_COMPEFFICACY CE-t-2, Rule T / PRD s.4.4) a real production run: default
                     budget prints WITHIN BUDGET; a planted --budget 0.001 on the REAL binary (no
                     mutant needed -- the ceiling is a caller flag now, not a constant) prints
                     BUDGET REACHED, distinguishable from the clean line by token alone
 10 MUTANT-BUDGET     a planted build whose budget resolution ignores --budget FAILS leg 9's own
                     BUDGET REACHED predicate at --budget 0.001 (ONE new arm was owed; this is the
                     second, exceeding it -- the comp-find T-1 F/G precedent)

Usage: python .tools/tests/test_comp_read_enumerate.py   (direct)  |  python -m pytest -q .tools/tests/test_comp_read_enumerate.py   (collected)
COMP_READ_TOOL=<path> aims it at a mutant
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
import tempfile
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
    """The comp-read UNDER TEST. COMP_READ_TOOL overrides it, so a grader can aim the battery at a mutant
    of their own without touching this file or the tool."""
    return Path(os.environ.get("COMP_READ_TOOL") or (_ws() / ".tools" / "comp-read"))

# The brief's s.5 criterion-3 specimen: the artifact whose anchor-sensitivity halted the fabric.
SPECIMEN = ("org/tier2_senior/0.4.0_DS_ClientPlatform~V/deliverables/emissions/"
            "perfrp_book_advisor.json")

RESULTS: list[tuple[str, str, str]] = []


def rec(tid, ok, detail):
    RESULTS.append((tid, "PASS" if ok else "FAIL", detail))
    print("  [%s] %s: %s" % ("PASS" if ok else "FAIL", tid, detail))


def run(args, tool=None, timeout=300):
    r = subprocess.run([sys.executable, str(tool or _tool())] + args,
                       capture_output=True, text=True, cwd=str(_ws()), timeout=timeout)
    return r.stdout + r.stderr


DEN_RE = re.compile(r"ENUMERATE:\s+(\d+) hit\(s\) across (\d+) lines / (\d+) section\(s\) scanned")
WV_RE = re.compile(r"whole-value matches:\s*(\d+)\s*\|\s*substring matches:\s*(\d+)")
BANDSUM_RE = re.compile(r"BANDS \(sum to (\d+)\):")
BANDROW_RE = re.compile(r"^\s{4,}([A-Z][A-Z0-9-]*)\s+(\d+)\s*$", re.MULTILINE)


def bands(out):
    """Rows only from inside the BANDS block, so a stray uppercase line cannot inflate the sum."""
    if "BANDS" not in out:
        return []
    blk = out.split("BANDS", 1)[1]
    for stop in ("\n\n", "HITS", "PAGE"):
        if stop in blk:
            blk = blk.split(stop, 1)[0]
    return [(m.group(1), int(m.group(2))) for m in BANDROW_RE.finditer(blk)]


_RAN = False


def _run_battery():
    """EVERY subprocess the battery runs lives here, so IMPORT IS INERT (the T-16 pass-2 shape,
    03cf4d17ac). Called once per process by test_all_arms_pass (pytest) or _report (direct). Before
    this, the arms ran at IMPORT: collection of this one file took 36 s, and its module-scope
    sys.exit ended the pytest session for the whole directory (NFRA_COMPEFFICACY F6, 92794). The arm
    code below is 3.0.0_SA_CVO~C's, byte-identical but for the indentation and _tool()/_ws() -> _tool()/_ws()."""
    global _RAN
    if _RAN:
        return
    _RAN = True
    # --- 1. DENOMINATOR ---------------------------------------------------------
    OUT_PY = run([".tools/comp-adversary", "--enumerate", "salience"])
    m = DEN_RE.search(OUT_PY)
    rec("DENOMINATOR", bool(m) and int(m.group(2)) > 0,
        ("prints '%s hit(s) across %s lines / %s section(s) scanned' -- a zero would still carry its "
         "denominator" % m.groups()) if m else
        "NO 'ENUMERATE: N hit(s) across L lines / S section(s) scanned' line -- a bare count is the "
        "grep failure this build exists to retire")

    # --- 2. BAND CONSERVATION over THREE backends -------------------------------
    # .py -> python-ast | .md -> markdown-headings | extensionless tool -> top-level-keys
    CASES = [
        (".tools/tests/test_comp_adversary_stage4_packet.py", "digest", "python-ast"),
        ("org/XXX.md", "inbox", "markdown"),
        (".tools/comp-adversary", "salience", "top-level-keys/other"),
    ]
    rows, bad = [], []
    for path, pat, backend in CASES:
        o = run([path, "--enumerate", pat])
        mm, bs = DEN_RE.search(o), bands(o)
        if not mm or not bs:
            bad.append("%s (%s): no denominator or no band rows" % (path, backend))
            continue
        tot, s = int(mm.group(1)), sum(c for _, c in bs)
        rows.append("%s=%d/%d" % (backend, s, tot))
        if s != tot:
            bad.append("%s (%s): bands sum %d != total %d" % (path, backend, s, tot))
    rec("BAND-CONSERVATION", not bad and len(rows) == 3,
        ("bands sum to the total on all 3 backends: %s -- no hit uncovered, none double-counted"
         % ", ".join(rows)) if not bad else "; ".join(bad))

    # --- 3. THE ANCHOR ARM, on the real specimen --------------------------------
    # Pre-verified against the bytes (2026-09-01): 396 substring occurrences, 0 whole-value. The
    # enclosing tokens are UNLABELLED-RELATIONSHIP:UNMAPPED-RELATIONSHIP:0017633210 and
    # UNMAPPED-RELATIONSHIP:0032215441 -- so a startswith() probe sees SOME and misses others, which
    # is exactly how the 132 rows went unreported.
    OUT_SPEC = run([SPECIMEN, "--enumerate", "UNMAPPED-RELATIONSHIP"], timeout=600)
    w = WV_RE.search(OUT_SPEC)
    ms = DEN_RE.search(OUT_SPEC)
    ok3 = bool(w) and int(w.group(1)) == 0 and int(w.group(2)) > 0 and bool(ms) and int(ms.group(1)) > 0
    rec("ANCHOR-ARM", ok3,
        ("real specimen reports whole-value %s | substring %s -- the line that would have caught the "
         "132 unreported rows in ONE read" % w.groups()) if w else
        "NO 'whole-value | substring' line on the specimen -- the anchor-sensitivity discriminator is "
        "absent, and a bare hit count reads as a verdict")

    # --- 4. ZERO CARRIES ITS DENOMINATOR ---------------------------------------
    OUT_Z = run([".tools/comp-adversary", "--enumerate", "zzz_no_such_token_zzz"])
    mz = DEN_RE.search(OUT_Z)
    rec("ZERO-DENOMINATOR", bool(mz) and int(mz.group(1)) == 0 and int(mz.group(2)) > 0,
        ("absent pattern prints '0 hit(s) across %s lines / %s section(s) scanned' -- a zero that "
         "carries its denominator is safe; grep's silence is not" % (mz.group(2), mz.group(3)))
        if mz else "an absent pattern produced no denominator line -- indistinguishable from silence")

    # --- 5. HONEST DEGRADE ------------------------------------------------------
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "nostructure.log"
        p.write_text("alpha beta\nbeta gamma\nbeta\n", encoding="utf-8")
        OUT_D = run([str(p), "--enumerate", "beta"])
    bd = bands(OUT_D)
    zero_rows = [b for b in bd if b[1] == 0]
    rec("HONEST-DEGRADE",
        ("UNAVAILABLE" in OUT_D) and len(bd) <= 1 and not zero_rows,
        "no-structure backend states banding UNAVAILABLE and emits %d band row(s), %d of them zero -- "
        "four zero rows would imply the distinction was tested and found absent, which is a different "
        "and false claim" % (len(bd), len(zero_rows)))

    # --- 6. PAGINATION ----------------------------------------------------------
    OUT_P = run([SPECIMEN, "--enumerate", "UNMAPPED-RELATIONSHIP", "--limit", "10"], timeout=600)
    rec("PAGINATION", ("PAGE" in OUT_P and "--page" in OUT_P and DEN_RE.search(OUT_P) is not None),
        "an over-page hit set shows the page, the full total, and how to reach the rest -- never a "
        "silent truncation (CLAUDE.md Rule 21: a page is not an answer)")

    # --- 7. MUTANT: neuter the band classifier in the SHIPPED bytes -------------
    src = _tool().read_text(encoding="utf-8")
    mutant_src, nsub = re.subn(r"^(\s*)band = _band_of\(", r"\1band = 'CODE'; _dead = _band_of(",
                               src, flags=re.MULTILINE)
    if nsub == 0:
        rec("MUTANT-BAND", False,
            "could not plant the mutant: no 'band = _band_of(' call site in the shipped source -- the "
            "leg certifies nothing and is reported FAIL, never skipped (a skip would read as green)")
    else:
        with tempfile.TemporaryDirectory() as td:
            mp = Path(td) / "comp-read-mutant"
            mp.write_text(mutant_src, encoding="utf-8")
            MO = run([".tools/tests/test_comp_adversary_stage4_packet.py", "--enumerate", "digest"],
                     tool=mp)
        mb = bands(MO)
        collapsed = len([b for b in mb if b[1] > 0]) <= 1
        rec("MUTANT-BAND", collapsed,
            "the planted all-one-band build collapses to %d non-zero band(s) -- so leg 2's conservation "
            "is produced by real classification, not by an identity that would sum correctly regardless"
            % len([b for b in mb if b[1] > 0]))

    # --- 8. CONSUMER UNTOUCHED --------------------------------------------------
    CA = run(["--self-test"], tool=_ws() / ".tools" / "comp-adversary", timeout=600)
    rec("CONSUMER-INTACT", "PASS 5/5" in CA,
        "comp-adversary --self-test still %s -- it shells out to comp-read for its stage-4 packet, so a "
        "changed DEFAULT digest would silently alter every validation_context_declaration in the estate"
        % ("PASS 5/5" if "PASS 5/5" in CA else "DID NOT return PASS 5/5"))

    # --- 9. BUDGET-CARRIER: the REAL production binary, no mutant needed -------
    # (NFRA_COMPEFFICACY CE-t-2, Rule T / PRD s.4.4) comp-read's ceiling is now a caller flag, not
    # a constant -- exercising it touches zero bytes, exactly the comp-find T-1 precedent.
    OUT_WITHIN = run([SPECIMEN, "--enumerate", "class"], timeout=600)
    OUT_REACHED = run([SPECIMEN, "--enumerate", "class", "--budget", "0.001"], timeout=600)
    ok9 = ("WITHIN BUDGET" in OUT_WITHIN and "BUDGET REACHED" not in OUT_WITHIN
           and "BUDGET REACHED" in OUT_REACHED and "WITHIN BUDGET" not in OUT_REACHED)
    rec("BUDGET-CARRIER", ok9,
        "default budget -> WITHIN BUDGET (no BUDGET REACHED token); --budget 0.001 on the same real "
        "binary -> BUDGET REACHED (no WITHIN BUDGET token) -- the two are distinguishable by token "
        "alone, no shared shape" if ok9 else
        "the real binary did not produce two distinguishable Rule T lines: within=%r reached=%r"
        % ("WITHIN BUDGET" in OUT_WITHIN, "BUDGET REACHED" in OUT_REACHED))

    # --- 10. MUTANT-BUDGET: neuter the carrier in the SHIPPED bytes, RED-first --
    src2 = _tool().read_text(encoding="utf-8")
    mutant_src2, nsub2 = re.subn(
        r"_compbudget\.resolve_budget\(budget_flag\)", "_compbudget.resolve_budget(None)", src2)
    if nsub2 == 0:
        rec("MUTANT-BUDGET", False,
            "could not plant the mutant: no '_compbudget.resolve_budget(budget_flag)' call site in "
            "the shipped source -- the leg certifies nothing and is reported FAIL, never skipped")
    else:
        with tempfile.TemporaryDirectory() as td:
            mp = Path(td) / "comp-read-mutant"
            mp.write_text(mutant_src2, encoding="utf-8")
            MO2 = run([SPECIMEN, "--enumerate", "class", "--budget", "0.001"], tool=mp, timeout=600)
        ignored = "BUDGET REACHED" not in MO2
        rec("MUTANT-BUDGET", ignored,
            "the planted build that ignores --budget (always resolves flag=None) %s at --budget "
            "0.001 -- so leg 9's BUDGET REACHED is produced by real carrier resolution, not by an "
            "identity that would print it regardless"
            % ("still reports WITHIN BUDGET, never BUDGET REACHED" if ignored else
               "STILL reached BUDGET REACHED -- the mutant did not neuter the carrier, so this arm "
               "certifies nothing"))


def _report() -> int:
    _run_battery()
    n = sum(1 for _, v, _ in RESULTS if v == "PASS")
    print()
    print("=" * 80)
    print("COMP-READ ENUMERATE BATTERY: %d/%d PASS (denominator %d)" % (n, len(RESULTS), len(RESULTS)))
    print("=" * 80)
    return 0 if n == len(RESULTS) else 1


def test_all_arms_pass():
    _run_battery()
    failed = [(t, d) for t, v, d in RESULTS if v != "PASS"]
    assert not failed, "arms failed (%d of %d): %s" % (len(failed), len(RESULTS), failed)
    print("COMP-READ ENUMERATE BATTERY: %d/%d PASS (denominator %d)" % (len(RESULTS), len(RESULTS), len(RESULTS)))


if __name__ == "__main__":
    sys.exit(_report())
