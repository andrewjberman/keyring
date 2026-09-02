"""Acceptance: comp-adversary STAGE 4 (PACKET) emits comp-read DIGESTS, not pointers.

Brief: org/tier1_exec/3.0.0_SA_CVO/deliverables/SPAWN_BRIEF_CVO_C_COMP_ADVERSARY_STAGE4_PACKET_20260831.md
Spec:  org/tier1_exec/1.0.0_SA_CTO/deliverables/DESIGN_NOTE_CHECK_SYSTEM_DEFINITIONS_AND_COMP_ADVERSARY_20260819.md
       s.3.1 stage 4, VERBATIM: "PACKET: comp-read digests of the complement set, sized for a
       validator context."

THE GAP THIS CLOSES: v1 implemented 2 of 5 spec'd stages. Stage 4 was DECLARED EXCLUDED
(":155 -- v1: the packet lists POINTERS, not digests"). A validator was handed 542 file paths
and no way to read them.

THE DESIGN CONSTRAINT THAT MAKES THIS NON-TRIVIAL, MEASURED 2026-08-31 by 3.0.0_SA_CVO~C:
  542 uncited siblings on the D2 proof-of-spec.
  A comp-read digest measures 2382-10395 bytes and 313-562 ms (n=4, this box).
  So "digest everything" = ~3 MB and ~240 s -- a context bomb AND a breach of the design
  note's own measured 71.5 s freshness constraint. THE DELIVERABLE IS A SELECTION RULE
  PLUS DIGESTS, never digest-everything.

SEVEN LEGS. Legs 1-3 are RED against the pre-build binary BY CONSTRUCTION (the feature is
absent); leg 5 is the planted mutant that keeps them honest afterwards.
  1. DIGEST-CONTENT   the packet carries comp-read's OWN output (its shape panel), not paths
  2. DENOMINATOR      the selection rule prints "selected N of M" on its own line
  3. EXCLUSIONS-5     the DECLARED EXCLUSIONS block drops 6 rows -> 5 (:155 retired, 5 intact)
  4. OPEN-MODE        --open still emits the empty-context declaration and runs NO sources
  5. MUTANT           a planted build with the digest emitter neutered FAILS leg 1 -- so leg 1
                      is a real result and not a string that would appear anyway
  6. NEGATIVE-CONTROL a zero-cited-path artifact fires ZERO-PIN and claims NO packet coverage
  7. MECE             every sibling lands in exactly ONE salience class (Rule 24 postulate i)

Usage: python .tools/tests/test_comp_adversary_stage4_packet.py
"""
from __future__ import annotations

import re
import subprocess
import sys
import tempfile
from pathlib import Path

WS = Path(subprocess.run(["git", "rev-parse", "--show-toplevel"],
                         cwd=str(Path(__file__).resolve().parent),
                         capture_output=True, text=True).stdout.strip())

TOOL = WS / ".tools" / "comp-adversary"

# The two artifacts the brief names as acceptance subjects (s.5 rows 2 and 7).
RICH = "org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/ADVI_PERFRP.TO-R1-DS_PROOF_OF_SPEC.json"
ZERO = "org/tier2_senior/0.6.2_AE_PartnerETL/deliverables/AUTH_SELFHEAL_PRD_v0.1.md"

RESULTS: list[tuple[str, str, str]] = []


def rec(tid, ok, detail):
    RESULTS.append((tid, "PASS" if ok else "FAIL", detail))
    print("  [%s] %s: %s" % ("PASS" if ok else "FAIL", tid, detail))


def run(args, tool=None):
    """Run the tool and return combined output. Never raises on rc -- the legs assert on
    CONTENT, because an rc alone does not discriminate this feature's presence."""
    r = subprocess.run([sys.executable, str(tool or TOOL)] + args,
                       capture_output=True, text=True, cwd=str(WS), timeout=600)
    return r.stdout + r.stderr


# --- the run under test (one compose, reused by legs 1,2,3,7) ----------------
OUT = run(["compose", RICH, "--digest-budget", "6"])

# --- 1. DIGEST CONTENT, not pointers ----------------------------------------
# comp-read's own output signature. A packet that merely LISTS paths cannot contain these:
# they are printed by comp-read itself, one panel header per digested file.
digest_sig = len(re.findall(r"comp-read: \S+", OUT))
shape_sig = len(re.findall(r"SHAPE \(all \d+, never truncated\)", OUT))
rec("DIGEST-CONTENT", digest_sig >= 2 and shape_sig >= 2,
    "packet carries comp-read's own panels: %d 'comp-read: <file>' banners, %d SHAPE panels "
    "(a pointer list would carry 0 of each)" % (digest_sig, shape_sig))

# --- 2. THE SELECTION RULE PRINTS ITS DENOMINATOR ---------------------------
m = re.search(r"selected:\s*(\d+)\s+of\s+(\d+)\s+uncited siblings", OUT)
rec("DENOMINATOR", bool(m) and int(m.group(2)) > int(m.group(1)) > 0,
    ("selection prints 'selected %s of %s uncited siblings' -- partial coverage stated, "
     "never silent" % (m.group(1), m.group(2))) if m else
    "NO 'selected N of M uncited siblings' line -- the packet does not declare its denominator")

# --- 3. DECLARED EXCLUSIONS: 6 rows -> 5 ------------------------------------
blk = OUT.split("## DECLARED EXCLUSIONS", 1)[-1].split("## DENOMINATORS", 1)[0]
rows = [ln for ln in blk.splitlines() if ln.strip().startswith("- ")]
retired = "the packet lists POINTERS, not digests" not in OUT
rec("EXCLUSIONS-5", len(rows) == 5 and retired,
    "DECLARED EXCLUSIONS carries %d row(s) and the ':155 pointers-not-digests' row is %s"
    % (len(rows), "RETIRED" if retired else "STILL PRESENT"))

# --- 4. --open UNCHANGED: empty-context declaration, zero sources -----------
OO = run(["--open"])
rec("OPEN-MODE", ("mode: OPEN" in OO and "ZERO estate context" in OO
                  and "source 1" not in OO and "source 5" not in OO),
    "--open still declares empty context and runs NO complement sources (the packet must not "
    "leak into the mode whose whole point is having no estate context)")

# --- 5. MUTANT: neuter the digest emitter in the SHIPPED bytes --------------
# Built from the shipped source, never a decaying commit pin: a pinned baseline goes stale the
# moment the file moves, and then this leg would measure a ghost.
src = TOOL.read_text(encoding="utf-8")
mutant_src, nsub = re.subn(r"^(\s*)(\w+), err = _comp_read_digest\(",
                           r"\1\2, err = (None, 'MUTANT: digest emitter neutered'); _unused = (",
                           src, flags=re.MULTILINE)
if nsub == 0:
    rec("MUTANT-NO-DIGEST", False,
        "could not plant the mutant: the digest call site '_comp_read_digest(' was not found in "
        "the shipped source -- the leg cannot certify anything and is reported as FAIL, never skipped")
else:
    with tempfile.TemporaryDirectory() as td:
        mp = Path(td) / "comp-adversary-mutant"
        mp.write_text(mutant_src, encoding="utf-8")
        MOUT = run(["compose", RICH, "--digest-budget", "6"], tool=mp)
    mut_sig = len(re.findall(r"comp-read: \S+", MOUT))
    rec("MUTANT-NO-DIGEST", mut_sig == 0,
        "the planted no-digest build emits %d comp-read panel(s) (expected 0) -- so leg 1's %d "
        "is caused by the feature, not by text that would print regardless"
        % (mut_sig, digest_sig))

# --- 6. NEGATIVE CONTROL: zero cited paths claims no coverage ---------------
NOUT = run(["compose", ZERO, "--digest-budget", "6"])
banner = "ZERO MACHINE-EXTRACTABLE PINS" in NOUT
no_false_pkt = ("comp-read: " not in NOUT) and re.search(r"selected:\s*0 of 0", NOUT) is not None
rec("NEGATIVE-CONTROL", banner and no_false_pkt,
    "zero-pin artifact: ZERO-PIN banner %s, packet declares 'selected: 0 of 0' and digests "
    "nothing %s -- an empty complement must never render as covered"
    % ("FIRED" if banner else "ABSENT", "OK" if no_false_pkt else "VIOLATED"))

# --- 7. MECE over the declared domain (Rule 24 postulate i) ----------------
cm = re.search(r"class census:\s*(.+)", OUT)
mece = False
detail = "no 'class census:' line -- the taxonomy does not state its own partition"
if cm and m:
    pairs = re.findall(r"S\d\s+(\d+)/(\d+)", cm.group(1))
    if pairs:
        sel = sum(int(a) for a, _ in pairs)
        tot = sum(int(b) for _, b in pairs)
        mece = (tot == int(m.group(2)) and sel == int(m.group(1)))
        detail = ("classes partition the domain exactly: sum(class totals)=%d == %s uncited "
                  "siblings, sum(selected)=%d == %s selected -- no member uncovered, none "
                  "double-counted" % (tot, m.group(2), sel, m.group(1)))
rec("MECE-PARTITION", mece, detail)

# ---------------------------------------------------------------- report
# sys.exit() MUST NOT run at module scope: the standard runner (pytest) collects this file, and a
# module-level SystemExit crashes the COLLECTOR -- pytest reports INTERNALERROR / "no tests
# collected" (measured 2026-09-02: SystemExit: 0, i.e. the battery PASSED and then killed the
# collector). A GREEN battery read as a RED suite, and it could not have contributed a test
# denominator to any gate that runs pytest. Same defect test_pipescript_digest.py documents in
# its own header; same repair. Release condition 5 (CVO~A @0d272d257c): "collected by the
# standard runner with a real test denominator." Lane-owner maintenance, no TO (1.0.0_SA_CTO 92659).


def _report() -> int:
    n = sum(1 for _, v, _ in RESULTS if v == "PASS")
    print()
    print("=" * 80)
    print("STAGE-4 PACKET BATTERY: %d/%d PASS (denominator %d)" % (n, len(RESULTS), len(RESULTS)))
    print("=" * 80)
    return 0 if n == len(RESULTS) else 1


def test_all_arms_pass():
    """pytest entry point -- the arms above already ran at import (the same shape the pipescript
    battery uses). Fails on any FAIL row; the denominator is len(RESULTS)."""
    fails = [(tid, d) for tid, v, d in RESULTS if v != "PASS"]
    assert not fails, "stage-4 packet battery arms failed (%d of %d): %r" % (
        len(fails), len(RESULTS), fails)


if __name__ == "__main__":
    sys.exit(_report())
