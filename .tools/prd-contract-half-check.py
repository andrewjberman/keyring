#!/usr/bin/env python3
"""prd-contract-half-check -- REFUSE a step-4 PRD whose C- CONTRACT DEFINITIONS hash into the BRIEF half.

WHY THIS EXISTS. The L4-R sign-off has two halves and `prd_signoff_lib.half_of_section()` decides
which one a section belongs to by the heading's FIRST WORD against
RATIFIED_SECTIONS = ("ENDPOINT", "CONTRACTS") (`prd_signoff_lib.py:34`, `:88-98`, backtick-insensitive).
A section headed `## A.4 -- ...` or `## B.4 -- NEW CONTRACTS` therefore classifies **brief** even when its
body MINTS contracts -- so those contracts sit OUTSIDE the bytes the CVO signature binds, on a half the
spine assigns elsewhere while assigning CONTRACTS to the CVO "always".

MEASURED 2026-09-24 on AMGT_CORPUS v0.5 and AMGT_RESAPP v0.25: ONE amendment to a HARD vendor-egress
contract (C-NO-VENDOR-CALL) and EIGHT newly minted C- contracts classified brief across three sections
(A.4, A.5, B.4). Found by 3.0.0_SA_CVO~Z (row AMGT_CORPUS-Z-S11) and INDEPENDENTLY by 4.0.0_SA_CRO~Z,
whose first verdict was REFUSE on the same ground. EXPOSURE only -- both read the nine and they were
sound -- and the remedy both named was to BUILD THE GUARD rather than re-open the addendum.

SO: this is the guard. It is the durable form of that correction, and it is a SEPARATE checker on
purpose -- it imports half_of_section rather than editing the signing path other seats are using.

WHAT IT REFUSES. Any top-level `## ` section whose body DEFINES a contract (a bolded `C-<NAME>` at the
start of a line) while `half_of_section(title)` reads "brief".

WHAT IT DOES NOT DO. It does not grade contract TEXT, does not touch signatures, and does not read the
signoff store. A section that merely MENTIONS a C- id is counted and reported but never refused -- the
definition/mention split is the whole reason a naive grep would be useless here.

USAGE
  prd-contract-half-check.py <PRD.md> [<PRD.md> ...]     -> rc 0 clean, rc 1 refused
  prd-contract-half-check.py --self-test                 -> proves the check CAN FAIL (rc 0 on success)

THE SELF-TEST IS NOT OPTIONAL CEREMONY. A checker whose failing arm was never exercised is the
instrument-that-cannot-fail class: it reads identical to a real pass. --self-test builds a fixture that
MUST be refused and a fixture that MUST pass, in memory, and fails loudly if either arm disagrees.
"""

import argparse
import importlib.util
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent

# A CONTRACT DEFINITION, not a mention: a line that OPENS with a bolded C- id.
#   **`C-NAME`.** ...      **C-NAME.** ...      **`C-NAME` (v0.5).** ...
DEFINE = re.compile(r"^\*\*`?(C-[A-Z][A-Z0-9_-]*)`?", re.M)
# Any occurrence at all, for the reported denominator.
MENTION = re.compile(r"`?(C-[A-Z][A-Z0-9_-]*)`?")


def _load_half_of_section():
    """Import the ONE authority on half classification. Never re-implement it here --
    a second copy of that rule is exactly the two-carrier defect this file guards against."""
    lib = HERE / "prd_signoff_lib.py"
    spec = importlib.util.spec_from_file_location("prd_signoff_lib", lib)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.half_of_section


def sections(text):
    """[(title, body)] over top-level '## ' headings. The pre-heading preamble is title None,
    which half_of_section() maps to neither half (it carries prd_version)."""
    out, title, buf = [], None, []
    for line in text.split("\n"):
        if line.startswith("## "):
            out.append((title, "\n".join(buf)))
            title, buf = line[3:].strip(), []
        else:
            buf.append(line)
    out.append((title, "\n".join(buf)))
    return out


def check(path, half_of_section):
    text = pathlib.Path(path).read_text(encoding="utf-8", errors="replace")
    secs = sections(text)
    violations, defining, mentions = [], 0, 0
    for title, body in secs:
        defs = DEFINE.findall(body)
        mentions += len(MENTION.findall(body))
        if not defs:
            continue
        defining += 1
        half = half_of_section(title)
        if half != "ratified-text":
            violations.append((title, half, defs))
    return secs, defining, mentions, violations


def report(path, secs, defining, mentions, violations):
    print("prd-contract-half-check: %s" % path)
    print("  DENOMINATOR: %d top-level section(s); %d DEFINE a contract; %d C- mention(s) total"
          % (len(secs), defining, mentions))
    if not violations:
        print("  OK: every contract-DEFINING section classifies ratified-text (the CVO's half)")
        return 0
    for title, half, defs in violations:
        print("  REFUSED: section classifies %s but DEFINES %d contract(s)" % (half.upper(), len(defs)))
        print("    heading: %s" % (title[:96] if title else "<preamble>"))
        print("    defines: %s" % ", ".join(defs))
    print("  ERROR: %d section(s) put contract definitions OUTSIDE the bytes the CVO signature binds."
          % len(violations))
    print("  FIX: make the heading's FIRST WORD 'CONTRACTS' (e.g. '## CONTRACTS -- B.4 -- ...').")
    print("       half_of_section() matches the first word only; renaming moves the bytes into the")
    print("       ratified half and RE-OPENS it deliberately, which is the point.")
    return 1


SELF_TEST_BAD = """# X

```json
{"project":"X"}
```

## B.4 -- NEW CONTRACTS

**`C-SELFTEST-ONE`.** A contract minted under a heading whose first word is not CONTRACTS.
"""

SELF_TEST_GOOD = """# X

```json
{"project":"X"}
```

## CONTRACTS -- B.4 -- NEW CONTRACTS

**`C-SELFTEST-ONE`.** The same contract under a heading that classifies ratified-text.

## B.5 -- PROSE THAT ONLY MENTIONS `C-SELFTEST-ONE`

A mention is not a definition and must NOT be refused.
"""


def self_test(half_of_section):
    import tempfile
    rc = 0
    with tempfile.TemporaryDirectory() as td:
        bad = pathlib.Path(td) / "bad.md"
        good = pathlib.Path(td) / "good.md"
        bad.write_text(SELF_TEST_BAD, encoding="utf-8")
        good.write_text(SELF_TEST_GOOD, encoding="utf-8")

        print("SELF-TEST arm 1 -- a contract under '## B.4' MUST be REFUSED:")
        s, d, m, v = check(bad, half_of_section)
        got = report(bad, s, d, m, v)
        if got != 1:
            print("  FAIL: the failing arm did NOT fire. This checker cannot fail and proves nothing.")
            rc = 1
        else:
            print("  arm 1 OK (refused as designed)")

        print()
        print("SELF-TEST arm 2 -- the same contract under '## CONTRACTS -- B.4' MUST PASS,")
        print("                   and a section that only MENTIONS it must not be refused:")
        s, d, m, v = check(good, half_of_section)
        got = report(good, s, d, m, v)
        if got != 0:
            print("  FAIL: the passing arm was refused. The check is over-broad.")
            rc = 1
        else:
            print("  arm 2 OK (passed, and the mention-only section was not refused)")

    print()
    print("SELF-TEST: %s -- both arms exercised, so a clean run on a real PRD means something."
          % ("PASS" if rc == 0 else "FAIL"))
    return rc


def main():
    ap = argparse.ArgumentParser(description="Refuse a PRD whose C- contract definitions hash into the brief half.")
    ap.add_argument("paths", nargs="*", help="step-4 PRD markdown file(s)")
    ap.add_argument("--self-test", action="store_true", help="prove the check can fail, then exit")
    args = ap.parse_args()

    half_of_section = _load_half_of_section()

    if args.self_test:
        return self_test(half_of_section)

    if not args.paths:
        ap.print_usage()
        print("ERROR: no PRD given. Pass a path, or --self-test.")
        return 2

    rc = 0
    for p in args.paths:
        if not pathlib.Path(p).exists():
            print("prd-contract-half-check: %s" % p)
            print("  ERROR: no such file -- an absent PRD is not a clean pass")
            rc = 2
            continue
        s, d, m, v = check(p, half_of_section)
        rc = max(rc, report(p, s, d, m, v))
        print()
    return rc


if __name__ == "__main__":
    sys.exit(main())
