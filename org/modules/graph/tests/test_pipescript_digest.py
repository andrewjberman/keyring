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


def skip(name, why):
    """Record an arm as NOT EVALUATED. WARN: A harness whose vocabulary has only PASS and FAIL
    encodes non-evaluation AS a verdict -- an unreachable-S3 run would otherwise either score
    the live arm green (a pass nothing exercised) or red (a network outage reported as a code
    defect). Neither is true. SKIPPED is printed loudly and never counts toward PASS."""
    _results.append((name, None, why))


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
# WARN: REBUILT 2026-09-02 (CTO Q5 ruling, adopting 3.0.0_SA_CVO's remedy unchanged): ASSERT THE
# PROPERTY, NOT THE CONSTANT.
#
# WHAT WAS WRONG: these three arms pinned `_LIVE_S3` / `_LIVE_RAW` -- md5 constants measured
# against a LIVE, MUTABLE S3 object on 2026-08-26. The intent was right (a fixture-only battery
# cannot prove the fix works on production bytes) and the mechanism guaranteed decay:
#     A TEST THAT PINS A LIVE MUTABLE OBJECT'S DIGEST AS A CONSTANT IS SELF-EXPIRING. It does
#     not fail when the tool breaks; it fails when the WORLD MOVES, which the world may do.
# Both the local file and the S3 object moved (together, still in sync) later on 08-26, so E1/E2
# failed on the constants and E3 then read STALE -- the CORRECT answer to the question actually
# asked, against an EXPECTATION that had expired. Because this file is a WATCHED TRIGGER PATH,
# that aged constant refused unrelated commits at the F9 gate and forced two audited bypasses
# (1.0.0_SA_CTO~D @32d5967277; 3.0.0_SA_CVO~C's PIPESCRIPT_SUITE_SKIP on comp-read --enumerate).
#
# WHAT IT DOES NOW: fetches the CURRENT ETag at run time and asserts the CLASSIFIER agrees with
# an INDEPENDENTLY computed LF-normalised comparison. No pinned digest, nothing to expire. It is
# not a tautology: classify_digest could compare raw instead of normalised, or mis-band the
# basis, and this arm would catch it -- the expectation is derived from the bytes, not from the
# tool's own answer.
# CONFIRMED at the live plane before rewriting (comp-pipescript deployed --pipeline mdpf,
# 2026-09-02): verdict MATCH, basis LF-NORMALISED, raw ffc40e68... != s3 87a175e3..., LF
# 87a175e3... == s3. Tool sound, constants aged -- exactly 3.0.0_SA_CVO's diagnosis, reached on
# a DIFFERENT instrument (live deployed sweep vs their arm enumeration), so corroboration.
_LIVE_BUCKET = "opal-data-mdpf"
_LIVE_KEY = "code/scripts/assets_gold/build_cottonwood_mdpf_slice.py"
_live = _WS / "data" / "assets" / "scripts" / "gold" / "build_cottonwood_mdpf_slice.py"


def _live_etag():
    """Current single-part ETag for the specimen, or None if S3 cannot be reached.
    None is NOT a failure -- it is an unmeasured arm (see skip()).

    Uses the .tools/aws SHIM (never bare aws -- the shim is the MSYS leading-slash mangle
    guard) and --bucket/--key rather than an s3:// URI, so there is no path to mangle.
    WARN: THE SHIM MUST BE LAUNCHED THROUGH GIT BASH, NOT EXEC'D DIRECTLY. It is a `#!/usr/bin/env
    bash` script, and a bare subprocess of a shebang script on Windows raises
    `WinError 193: %1 is not a valid Win32 application` -- which this function would have
    swallowed into a permanent, silent SKIP, i.e. a live arm that never runs and looks fine.
    Measured here 2026-09-02. .tools/git_bash_resolver.bash_argv is the canonical resolver
    (CLAUDE.md: python shelling to bash goes through it; it never degrades to bare `bash`,
    which can resolve the System32 WSL stub)."""
    import subprocess
    sys.path.insert(0, str(_WS / ".tools"))
    try:
        from git_bash_resolver import bash_argv
    except ImportError:
        return None
    try:
        r = subprocess.run(
            bash_argv(str(_WS / ".tools" / "aws"),
                      "s3api", "head-object", "--bucket", _LIVE_BUCKET, "--key", _LIVE_KEY,
                      "--query", "ETag", "--output", "text"),
            capture_output=True, text=True, timeout=60, cwd=str(_WS))
    except (OSError, RuntimeError, subprocess.SubprocessError):
        return None
    if r.returncode != 0:
        return None
    tag = (r.stdout or "").strip().strip('"')
    # A multipart ETag ("<md5>-<n>") is NOT an md5 and must never be compared as one -- the D
    # arms cover that classification separately. Treat it as unmeasurable here.
    return tag if tag and "-" not in tag else None


if not _live.exists():
    check("E0 live specimen present", False, "file absent -- control could not run")
else:
    _etag = _live_etag()
    if _etag is None:
        skip("E1-E3 live specimen property",
             "S3 unreachable / multipart ETag -- NOT EVALUATED. The 15 offline fixture arms "
             "above still bound the classifier; this arm alone is unmeasured, not passed.")
    else:
        b = _live.read_bytes()
        _raw, _lf = md5(b), md5(b.replace(b"\r\n", b"\n"))
        # The expectation is computed from the BYTES, independently of classify_digest.
        _expected = "MATCH" if _lf == _etag else "STALE"
        st, info = classify_digest(b, _etag)
        check("E1 live specimen: classifier agrees with an independent LF-normalised compare",
              st == _expected, "got=%s expected=%s lf=%s etag=%s" % (st, _expected, _lf, _etag))
        # E2 is the REGRESSION ITSELF: a CRLF working tree against an LF S3 object of identical
        # content must be MATCH. Only assertable when that is genuinely the live situation.
        if b"\r\n" in b and _lf == _etag and _raw != _etag:
            check("E2 live CRLF-vs-LF, identical content -> MATCH (the false-STALE regression)",
                  st == "MATCH", st)
            check("E2b ...and the basis names the normalisation rather than asserting equality",
                  any("LF-NORMALISED" in x for x in info), info)
        else:
            skip("E2/E2b live CRLF-vs-LF regression",
                 "the live pair is not currently CRLF-local/LF-s3 with identical content "
                 "(raw=%s lf=%s etag=%s) -- the regression shape is absent, not passing"
                 % (_raw, _lf, _etag))
        check("E3 live specimen: raw digest alone does NOT decide the verdict",
              (_raw == _etag) or st == _expected, "raw=%s etag=%s st=%s" % (_raw, _etag, st))

# ---------------------------------------------------------------- report
# sys.exit() MUST NOT run at module scope: the comp-pipescript suite collects this file with
# pytest, and a module-level SystemExit crashes the COLLECTOR -- pytest reports INTERNALERROR
# and "no tests ran", so a GREEN battery takes the whole suite red. Caught by the F9 suite gate
# on the very commit that added this file, which is the gate working exactly as intended.


def _report():
    fails = [r for r in _results if r[1] is False]
    skips = [r for r in _results if r[1] is None]
    for name, ok, detail in _results:
        verdict = "SKIP" if ok is None else ("PASS" if ok else "FAIL")
        print("  %s  %s%s" % (verdict, name,
                              "" if ok else "   %s%r" % ("why=" if ok is None else "got=", detail)))
    print()
    # PRINT THE DENOMINATOR AND KEEP SKIPPED OUT OF 'passed' -- a skipped arm is unmeasured, and
    # rolling it into the pass count is how an unexercised control reads as an exercised one.
    print("ARMS: %d passed / %d failed / %d SKIPPED (unmeasured) / %d total"
          % (len(_results) - len(fails) - len(skips), len(fails), len(skips), len(_results)))
    if skips:
        print("  ^ SKIPPED is NOT a pass. Those arms did not run; nothing was proven about them.")
    return 1 if fails else 0


def test_all_arms_pass():
    """pytest entry point -- the arms above already ran at import.
    Fails on FALSE only. A SKIPPED arm (None) is unmeasured, not failed: the live-specimen arm
    needs S3, and a network outage is not a defect in classify_digest. The 15 offline fixture
    arms carry the gate when the live arm cannot run."""
    fails = [(n, d) for n, ok, d in _results if ok is False]
    assert not fails, "digest battery arms failed: %r" % (fails,)


if __name__ == "__main__":
    sys.exit(_report())
