"""Battery for pipeline_cli.classify_digest -- the comp-pipescript deployed CRLF false-STALE fix.

WHY THIS EXISTS AS A UNIT BATTERY AND NOT A LIVE SWEEP: the comparison used to live inside a
closure, reachable only through a real S3 sweep. A live sweep can demonstrate the MATCH arm and
CANNOT PLANT A MUTANT -- so the arm that must fail was structurally unreachable, and a fix whose
failing arm cannot be exercised is not verified. classify_digest was lifted to module level so
BOTH arms are reachable from different truths.

Run: python org/modules/graph/tests/test_pipescript_digest.py
"""
from __future__ import annotations

import hashlib
import importlib.util
import pathlib
import sys

_WS = pathlib.Path(__file__).resolve().parents[4]
_spec = importlib.util.spec_from_file_location(
    "pipeline_cli", _WS / "org" / "modules" / "graph" / "pipeline_cli.py")
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
classify_digest = _mod.classify_digest

_results = []


def check(name, cond, detail=""):
    _results.append((name, bool(cond), detail))


def md5(b):
    return hashlib.md5(b).hexdigest()


# ---------------------------------------------------------------- fixtures
LF_BODY = b"import os\nx = 1\nprint(x)\n"
CRLF_BODY = LF_BODY.replace(b"\n", b"\r\n")
OTHER_LF = b"import os\nx = 2\nprint(x)\n"          # DIFFERENT CONTENT, same line endings
OTHER_CRLF = OTHER_LF.replace(b"\n", b"\r\n")

# ---------------------------------------------------------------- A. the fix
st, info = classify_digest(CRLF_BODY, md5(LF_BODY))
check("A1 CRLF local vs LF s3, identical content -> MATCH", st == "MATCH", st)
check("A2 ...and the verdict PRINTS its normalisation basis",
      any("LF-NORMALISED" in x for x in info), info)
check("A3 ...and shows BOTH digests so the reader can audit it",
      any(md5(LF_BODY) in x for x in info) and any(md5(CRLF_BODY) in x for x in info), info)

# ---------------------------------------------------------------- B. THE MUTANT
# The whole risk of this fix is that normalising manufactures a MATCH. Plant a real content
# difference ACROSS the same CRLF/LF boundary: if normalisation were doing too much, this
# would go green.
st, info = classify_digest(CRLF_BODY, md5(OTHER_LF))
check("B1 MUTANT: CRLF local vs LF s3, DIFFERENT content -> STALE (no false MATCH)",
      st == "STALE", st)
check("B2 ...and it reports that BOTH raw and LF digests differ",
      any("BOTH raw and LF-normalised" in x for x in info), info)

st, info = classify_digest(CRLF_BODY, md5(OTHER_CRLF))
check("B3 MUTANT: CRLF local vs CRLF s3 of different content -> STALE", st == "STALE", st)

# B4 IS THE ARM THAT ACTUALLY BOUNDS THE NORMALISATION, AND B1-B3 DO NOT.
# B1-B3 differ in CONTENT (x = 1 vs x = 2), so they stay STALE even under a normalisation that
# strips ALL whitespace -- they cannot tell "collapses line endings" from "collapses everything".
# Found by planting exactly that mutation against this battery: it went GREEN, i.e. BLIND.
# SPACED_LF differs from LF_BODY ONLY in non-newline whitespace, so it is STALE under the correct
# rule and MATCH under an over-eager one. This is the fixture that fails at the field under test.
SPACED_LF = b"import os\nx  =  1\nprint(x)\n"
st, info = classify_digest(CRLF_BODY, md5(SPACED_LF))
check("B4 MUTANT: differs ONLY in non-newline whitespace -> STALE "
      "(bounds normalisation to line endings)", st == "STALE", st)

# ---------------------------------------------------------------- C. unchanged behaviour
st, info = classify_digest(LF_BODY, md5(LF_BODY))
check("C1 byte-identical -> MATCH", st == "MATCH", st)
check("C2 ...basis says raw bytes", any("raw bytes" in x for x in info), info)

st, info = classify_digest(LF_BODY, md5(OTHER_LF))
check("C3 LF local, real difference -> STALE", st == "STALE", st)
check("C4 ...and states normalisation would not have changed it",
      any("no CRLF" in x for x in info), info)

# ---------------------------------------------------------------- D. Rule 28 Q7
st, info = classify_digest(LF_BODY, "d41d8cd98f00b204e9800998ecf8427e-3")
check("D1 multipart ETag -> ETAG_NOT_COMPARABLE, NOT STALE", st == "ETAG_NOT_COMPARABLE", st)
check("D2 ...and it says explicitly this is not a staleness verdict",
      any("NOT a staleness verdict" in x for x in info), info)
check("D3 ...and names its basis as NONE", any("basis:    NONE" in x for x in info), info)
# NEGATIVE CONTROL on the multipart guard: a normal single-part ETag must NOT be caught by it.
st, _ = classify_digest(LF_BODY, md5(LF_BODY))
check("D4 NEG CONTROL: single-part ETag is NOT classified uncomparable",
      st == "MATCH", st)

# ---------------------------------------------------------------- E. live positive control
# The exact specimen 2.0.0_SA_COO cited (build_cottonwood_mdpf_slice.py), digests as measured
# against s3://opal-data-mdpf on 2026-08-26. Pins the fix to a REAL object, not only fixtures.
_LIVE_S3 = "82d08cf27e1b3da2fecdb2a188765e0d"
_LIVE_RAW = "06c92e7a0ab940aaa2965d2f5622d4a9"
_live = _WS / "data" / "assets" / "scripts" / "gold" / "build_cottonwood_mdpf_slice.py"
if _live.exists():
    b = _live.read_bytes()
    check("E1 live specimen: raw digest still matches the recorded one",
          md5(b) == _LIVE_RAW, md5(b))
    check("E2 live specimen: LF digest equals the recorded S3 ETag",
          md5(b.replace(b"\r\n", b"\n")) == _LIVE_S3, md5(b.replace(b"\r\n", b"\n")))
    st, _ = classify_digest(b, _LIVE_S3)
    check("E3 live specimen classifies MATCH (was a PERMANENT false STALE)", st == "MATCH", st)
else:
    check("E0 live specimen present", False, "file absent -- control could not run")

# ---------------------------------------------------------------- report
# sys.exit() MUST NOT run at module scope: the comp-pipescript suite collects this file with
# pytest, and a module-level SystemExit crashes the COLLECTOR -- pytest reports INTERNALERROR
# and "no tests ran", so a GREEN battery takes the whole suite red. Caught by the F9 suite gate
# on the very commit that added this file, which is the gate working exactly as intended.


def _report():
    fails = [r for r in _results if not r[1]]
    for name, ok, detail in _results:
        print("  %s  %s%s" % ("PASS" if ok else "FAIL", name,
                              "" if ok else "   got=%r" % (detail,)))
    print()
    print("ARMS: %d passed / %d failed / %d total"
          % (len(_results) - len(fails), len(fails), len(_results)))
    return 1 if fails else 0


def test_all_arms_pass():
    """pytest entry point -- the arms above already ran at import."""
    fails = [(n, d) for n, ok, d in _results if not ok]
    assert not fails, "digest battery arms failed: %r" % (fails,)


if __name__ == "__main__":
    sys.exit(_report())
