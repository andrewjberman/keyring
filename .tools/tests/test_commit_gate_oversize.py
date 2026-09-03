#!/usr/bin/env python3
"""The OVERSIZE REFUSAL in commit-gate: does it actually block?

WHY THIS EXISTS
---------------
2026-07-14: a 685MB terraform provider .exe was swept into a commit from an
un-ignored .terraform/ cache. It froze CLOUD for EVERY agent and cost an
Andrew-authorized history rewrite of a shared branch.

It passed commit-gate and comp-surface-check IN SILENCE. Not because the gate
was bypassed -- the gate RECEIVED the path and ran ZERO checks on it, because the
per-suffix dispatch has no branch for `.exe`. It printed "clean for 0 file(s)"
and exited 0.

    THE ONLY THING THAT STOPPED IT WAS GITHUB'S 100MB PRE-RECEIVE LIMIT.
    We were saved by someone else's control.

This suite exists so the replacement control is EXERCISED, not assumed -- because
the whole lesson of that night (twice over, on me) is that an unexercised guard
and an absent guard are the same guard.

    A PASSING ASSERTION NEVER MADE TO FAIL HAS NEVER BEEN TESTED.

Run:  python .tools/tests/test_commit_gate_oversize.py
"""
from __future__ import annotations

import importlib.util
import os
import pathlib
import sys
import tempfile

TOOLS = pathlib.Path(__file__).resolve().parents[1]
RUNNER = TOOLS / "commit_gate_runner.py"

spec = importlib.util.spec_from_file_location("cgr", RUNNER)
cgr = importlib.util.module_from_spec(spec)
# F6-adjacent (2026-09-02, TOOL_BATTERIES lane maintenance): commit_gate_runner.py :101 imports its
# sibling git_bash_resolver bare; loaded by spec from here, .tools/ is not on sys.path and the
# import raised ModuleNotFoundError at collection -- this battery had been dead since that import landed.
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))
spec.loader.exec_module(cgr)

LIMIT = cgr.MAX_FILE_BYTES


def _sparse(path: pathlib.Path, size: int) -> pathlib.Path:
    """A file of exactly `size` bytes, without writing `size` bytes to disk."""
    with open(path, "wb") as fh:
        if size:
            fh.seek(size - 1)
            fh.write(b"\0")
    return path


def main() -> int:
    failures = []
    results = {}

    print("THE OVERSIZE REFUSAL (limit = "
          f"{LIMIT} bytes = {LIMIT / 1024 / 1024:.0f}MB, GitHub's exactly)")
    print("=" * 72)

    with tempfile.TemporaryDirectory() as td:
        td = pathlib.Path(td)
        audit = td / "audit.log"
        os.environ["COMMIT_GATE_AUDIT"] = str(audit)
        os.environ.pop("COMMIT_GATE_ALLOW_LARGE", None)

        # The 685MB .exe, reconstructed. THE CASE THAT ACTUALLY HAPPENED.
        exe = _sparse(td / "terraform-provider-aws_v5.100.0_x5.exe", 718820352)
        # A .py of the same size -- proves the check is not suffix-scoped.
        big_py = _sparse(td / "huge.py", LIMIT + 1)
        # Boundary cases.
        at_limit = _sparse(td / "at_limit.bin", LIMIT)          # >= limit -> BLOCK
        under = _sparse(td / "under.bin", LIMIT - 1)            # < limit  -> pass
        tiny = _sparse(td / "tiny.bin", 10)
        empty = _sparse(td / "empty.bin", 0)

        CASES = [
            (exe, 1, "THE REAL ONE: 685MB .exe -- a suffix the dispatch has no branch for"),
            (big_py, 1, "oversize .py -- the check is NOT suffix-scoped"),
            (at_limit, 1, "EXACTLY 100MB -- GitHub rejects >100MB; at the limit we refuse too"),
            (under, 0, "one byte under -- must PASS (no false alarm on a pushable file)"),
            (tiny, 0, "a normal small file -- must PASS"),
            (empty, 0, "an empty file -- must PASS"),
        ]

        for path, expect, why in CASES:
            got = cgr._check_file_size(str(path))
            ok = got == expect
            results[path.name] = got
            print(f"  {'BLOCK' if expect else 'pass ':<6} got "
                  f"{'BLOCK' if got else 'pass '}  {'OK  ' if ok else 'FAIL'}  {why}")
            if not ok:
                failures.append((path.name, expect, got, why))

        # ---- the AUDITED OVERRIDE ----
        print()
        print("THE AUDITED OVERRIDE")
        print("-" * 72)
        os.environ["COMMIT_GATE_ALLOW_LARGE"] = "deliberate: signed installer for RD"
        got = cgr._check_file_size(str(exe))
        if got != 0:
            failures.append(("override", 0, got, "override did not suppress the block"))
        print(f"  override set -> {'pass' if got == 0 else 'BLOCK'}  "
              f"{'OK  ' if got == 0 else 'FAIL'}  a deliberate large artifact is allowed")

        wrote = audit.exists() and "OVERSIZE-OVERRIDE" in audit.read_text()
        print(f"  audited        -> {'yes' if wrote else 'NO'}   "
              f"{'OK  ' if wrote else 'FAIL'}  the bypass is on the record")
        if not wrote:
            failures.append(("override-audit", 1, 0, "override was NOT audited"))

        # F-020: the log must record an override ONLY when it SUPPRESSED A REAL BLOCK.
        # An override that "allows" a 10-byte file suppressed nothing -- logging it
        # would be theater in an audit trail's clothes.
        before = audit.read_text()
        cgr._check_file_size(str(tiny))
        if audit.read_text() != before:
            failures.append(("F-020", 0, 1,
                             "audited a no-op override -- log is theater"))
            print("  F-020          -> FAIL  logged an override that suppressed nothing")
        else:
            print("  F-020          -> OK    a no-op override is NOT logged "
                  "(no theater in the audit trail)")
        os.environ.pop("COMMIT_GATE_ALLOW_LARGE", None)

        # ---- THE OVERRIDE FAILS CLOSED WHEN IT CANNOT BE AUDITED ----
        # COO review 2026-07-14. The override is legal ONLY when recorded. If the
        # audit log cannot be written, the condition is unmet and the override must
        # be REFUSED -- never a silent pass. This is the failure path nobody tests,
        # and it is exactly where an unaudited suppression of a real block hides.
        print()
        print("FAIL-CLOSED: override + unwritable audit -> REFUSE, never silent-pass")
        print("-" * 72)
        # point the audit at a path that cannot be created: a file used as a dir.
        blocker = td / "not_a_dir"
        blocker.write_text("x")
        os.environ["COMMIT_GATE_AUDIT"] = str(blocker / "audit.log")  # parent is a file
        os.environ["COMMIT_GATE_ALLOW_LARGE"] = "deliberate, but audit is broken"
        got = cgr._check_file_size(str(exe))
        os.environ["COMMIT_GATE_AUDIT"] = str(audit)  # restore
        os.environ.pop("COMMIT_GATE_ALLOW_LARGE", None)
        if got == 1:
            print("  OK: override REFUSED (exit 1) when the audit is unwritable -- "
                  "no unaudited suppression.")
        else:
            print(f"  FAIL: override PASSED ({got}) with a broken audit -- "
                  "an unaudited override slipped through.")
            failures.append(("fail-closed", 1, got,
                             "override failed OPEN on unwritable audit"))
        # the helper's return value is the signal the caller fails-closed on, so
        # pin BOTH sides of it: True on a writable path, False on an unwritable one.
        wrote_ok = cgr._audit_oversize(str(exe), 999, "probe") is True   # audit restored -> writable
        os.environ["COMMIT_GATE_AUDIT"] = str(blocker / "audit.log")
        wrote_fail = cgr._audit_oversize(str(exe), 999, "probe") is False  # unwritable -> False
        os.environ["COMMIT_GATE_AUDIT"] = str(audit)
        ok = wrote_ok and wrote_fail
        print(f"  {'OK  ' if ok else 'FAIL'}  _audit_oversize returns True on a "
              "writable log and False on an unwritable one (the fail-closed signal)")
        if not ok:
            failures.append(("audit-return", "(True,False)",
                             (wrote_ok, wrote_fail), "helper signal wrong"))

        # ---- THE REMEDIATION MUST NOT BE DANGEROUS ----
        # The first version of _ignore_suggestion returned f"*{suffix}" for ANY
        # suffix -- so an oversize .py told the agent to run
        #     echo '*.py' >> .gitignore
        # which would untrack EVERY PYTHON FILE IN THE REPO. The gate blocks (good),
        # earns your trust (good), and then hands you a repo-destroying command as
        # its help. That is worse than saying nothing.
        # A gate is not only its verdict. It is also what it tells you to do next.
        print()
        print("THE REMEDIATION ITSELF (a gate's advice is part of the gate)")
        print("-" * 72)
        SUGGEST = [
            ("infra/aws/terraform/x/.terraform/providers/aws.exe", "**/.terraform/",
             "a cache dir in the path -> ignore the DIR (the real fix)"),
            ("some/where/model.pkl", "*.pkl", "a build artifact -> ignore the suffix"),
            ("data/scripts/gold/huge.py", "", "SOURCE -> suggest NOTHING, never '*.py'"),
            ("infra/main.tf", "", "SOURCE -> suggest NOTHING, never '*.tf'"),
            ("org/notes.md", "", "SOURCE -> suggest NOTHING, never '*.md'"),
        ]
        for path, want, why in SUGGEST:
            got = cgr._ignore_suggestion(path)
            ok = got == want
            shown = repr(got) if got else "(none -- go look at it)"
            print(f"  {shown:<22} {'OK  ' if ok else 'FAIL'}  {why}")
            if not ok:
                failures.append((path, want, got, why))
        # the invariant that actually protects the repo
        for src in ("a/b/c.py", "a/b/c.tf", "a/b/c.sh", "a/b/c.md", "a/b/c.json"):
            s = cgr._ignore_suggestion(src)
            if s.startswith("*."):
                failures.append((src, "", s, "SUGGESTED A SOURCE-SUFFIX GLOB"))
                print(f"  FAIL: would have suggested {s!r} for {src}")

        # ---- THE MUTANT ----
        # Guardrail (CTO, verbatim): "gate disabled -> exactly the size tests go
        # red, nothing else." Disable the refusal and prove THIS SUITE CATCHES IT.
        # Without this, everything above is just lines that happen to print OK.
        print()
        print("MUTANT -- disable the gate; this suite MUST go red")
        print("-" * 72)
        real = cgr._check_file_size
        cgr._check_file_size = lambda f: 0  # the gate, dead
        caught = [name for path, expect, _ in
                  [(p, e, w) for p, e, w in CASES] if expect == 1
                  for name in [path.name]
                  if cgr._check_file_size(str(path)) != expect]
        cgr._check_file_size = real
        if len(caught) == 3:
            print(f"  OK: a dead gate is caught by exactly the {len(caught)} "
                  f"blocking cases ({', '.join(caught)}) -- and by nothing else.")
        else:
            print(f"  FAIL: mutant caught by {len(caught)} cases, expected 3. "
                  "The suite does not pin the gate.")
            failures.append(("MUTANT", 3, len(caught), "mutant not caught correctly"))

    print()
    if failures:
        print(f"FAILED -- {len(failures)} problem(s):")
        for f in failures:
            print(f"   {f}")
        return 1
    print("ALL OVERSIZE TESTS PASS -- the gate blocks, and this proves it.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
