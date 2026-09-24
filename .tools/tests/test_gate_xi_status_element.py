#!/usr/bin/env python3
"""GATE (xi) -- THE STATUS-ELEMENT LIMB, ON NEWLY-ADDED TREE ORDERS ONLY.

Subject: `.tools/to-pipeline-gate.py` check_file() -> _status_element_violations() /
STATUS_ELEMENT_RE / GATE_XI_TERMINAL_WORDS. Built on `AMGT_RESAPP.TO-AMGT-rk-56` (decomp cell
AMGT-rk-56; row AMGT_RESAPP-Z-S153, surfaced by `4.0.0_SA_CRO~Z` 2026-09-17). All 15 round-13 task
orders (AMGT-rk-19..rk-30) were born with NO <status> element at all, while each worker face's
closing step tells the worker to flip <status> to complete and to-check.py lists all 15 as '??'.
No limb of check_file() read the record face's status -- this is that limb.

EVERY ARM RUNS IN A REAL GIT INDEX, THROUGH THE GATE'S OWN CLI, ON A REAL ORDER'S OWN BYTES
(`git show HEAD:` of `AMGT_RESAPP.TO-AMGT-rk-19.adapter-second-join.md`, which the estate has
already flipped to `<status>complete</status>` and which also carries the natural backticked prose
mention "flip `<status>` to `complete`" a few lines above it -- the exact Z-S15 / to-check FIX C
shape, not a synthetic fixture):
  RED  MISSING ELEMENT     the real order's bytes with the <status>complete</status> line REMOVED,
                           staged as ADDED -- REFUSED at rc=1, naming "S153" and "NO <status>
                           element" (the prose mention two lines above stays inert).
  RED  PROSE-ONLY MENTION  the same bytes with the element REPLACED by a second, different
                           backticked prose mention (not a real element) -- REFUSED identically.
  GREEN PENDING             the same bytes with the element set to <status>pending</status> on its
                           own line -- ADMITTED by this limb (other limbs' output on a scratch repo
                           lacking project.json is tolerated and named, not counted).
  GREEN MODIFY NOT GRADED  the missing-element bytes COMMITTED, then staged as MODIFIED with the
                           <status>pending</status> element added back -- this limb does not grade
                           it (main() feeds it only the newly-added set, exactly as GATE (viii)'s
                           newly-added half does).
  RED  BORN TERMINAL       the real order's UNMODIFIED bytes (already <status>complete</status> at
                           HEAD) staged as ADDED -- REFUSED as "born terminal": an order is issued
                           OPEN, and a terminal word belongs to the worker's close.

Scratch repos live under <WS>/.scratch/ and are removed at the end.
Run: python .tools/tests/test_gate_xi_status_element.py
Exit 0 = every arm as expected. Exit 1 otherwise.
"""
from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
WORKSPACE = TOOLS.parent
GATE = TOOLS / "to-pipeline-gate.py"
REL = "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-19.adapter-second-join.md"
SCRATCH = WORKSPACE / ".scratch" / "rk-56-gate-xi-status-element"
AUTHOR = "2.0.0_SA_COO~Z"
STATUS_LINE_RE = re.compile(r"^[ \t]*<status>\s*[A-Za-z_-]+\s*</status>[ \t]*$\n?", re.M)
results: list = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    results.append((name, ok, detail))
    return ok


def _ws_git(*args: str) -> str:
    out = subprocess.run(["git", *args], cwd=str(WORKSPACE), capture_output=True, text=True,
                         encoding="utf-8", errors="replace", timeout=120)
    if out.returncode != 0:
        raise RuntimeError("git %s rc=%d: %s" % (" ".join(args[:2]), out.returncode, out.stderr))
    return out.stdout


def _git(repo: Path, *args: str):
    cmd = ["git", "-c", "core.hooksPath=" + str(repo / ".nohooks"), "-c", "core.autocrlf=false",
           "-c", "user.name=battery", "-c", "user.email=battery@opal.agent", *args]
    return subprocess.run(cmd, cwd=str(repo), capture_output=True, text=True, encoding="utf-8",
                          errors="replace", timeout=180)


def _repo(name: str) -> Path:
    repo = SCRATCH / name
    (repo / ".nohooks").mkdir(parents=True)
    _git(repo, "init", "-q")
    (repo / "README.md").write_text("battery fixture repo\n", encoding="utf-8")
    _git(repo, "add", "README.md")
    _git(repo, "commit", "-q", "--no-verify", "-m", "base")
    return repo


def _place(repo: Path, rel: str, text: str) -> None:
    dst = repo / rel
    dst.parent.mkdir(parents=True, exist_ok=True)
    with open(dst, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def _gate(repo: Path, rels: list):
    env = dict(os.environ)
    env["OPAL_AGENT_SERIAL"] = AUTHOR
    env.pop("STAGED", None)
    out = subprocess.run([sys.executable, str(GATE), *rels], cwd=str(repo), capture_output=True, text=True,
                         encoding="utf-8", errors="replace", timeout=300, env=env)
    return out.returncode, (out.stdout or "") + (out.stderr or "")


def _status(repo: Path, rel: str) -> str:
    st = _git(repo, "diff", "--cached", "--name-status").stdout
    return next((ln.split("\t")[0] for ln in st.splitlines() if ln.split("\t")[-1] == rel), "?")


def _xi_lines(output: str, rel: str) -> list:
    """GATE (xi)'s OWN violation lines for `rel` -- distinguished from the OTHER limbs' noise a
    real order triggers in a bare scratch repo (no project.json, no decomp doc: those fire too and
    are tolerated, exactly as the GATE (x) and GATE (viii)-modify batteries tolerate their noise)."""
    return [ln.strip() for ln in output.splitlines()
            if rel in ln and ("NO <status> element" in ln or "born terminal" in ln)]


def main() -> int:
    SCRATCH.mkdir(parents=True, exist_ok=True)
    try:
        base_text = _ws_git("show", "HEAD:" + REL)
        m = STATUS_LINE_RE.search(base_text)
        if not m:
            print("FATAL: %s at HEAD does not carry a line-anchored <status> element to build the "
                  "battery on -- the fixture order this battery depends on has moved." % REL)
            return 1
        status_line = m.group(0)
        missing_text = STATUS_LINE_RE.sub("", base_text, count=1)
        prose_text = STATUS_LINE_RE.sub(
            "the order's status is recorded as `<status>complete</status>` above\n", base_text, count=1)
        pending_text = STATUS_LINE_RE.sub("<status>pending</status>\n", base_text, count=1)
        terminal_text = base_text  # real bytes already carry <status>complete</status>

        print("  fixture: %s\n  real status line removed: %r" % (REL, status_line.strip()))

        # ---- RED: the <status> line REMOVED -> refused naming S153 / NO <status> element
        repo1 = _repo("red-missing")
        _place(repo1, REL, missing_text)
        _git(repo1, "add", REL)
        st1 = _status(repo1, REL)
        rc1, out1 = _gate(repo1, [REL])
        lines1 = _xi_lines(out1, REL)
        ok1 = (st1 == "A" and rc1 == 1
               and any("S153" in ln and "NO <status> element" in ln for ln in lines1))
        print("  %-4s status line removed, staged %s -> rc=%d; %s" % (
            "PASS" if ok1 else "FAIL", st1, rc1, (lines1[0][:160] if lines1 else "no status-element refusal")))
        check("RED: a real order's <status> line REMOVED, staged as ADDED -> REFUSED naming S153", ok1)

        # ---- RED: the element REPLACED by a backticked prose mention only -> refused identically
        repo2 = _repo("red-prose-only")
        _place(repo2, REL, prose_text)
        _git(repo2, "add", REL)
        st2 = _status(repo2, REL)
        rc2, out2 = _gate(repo2, [REL])
        lines2 = _xi_lines(out2, REL)
        ok2 = (st2 == "A" and rc2 == 1
               and any("S153" in ln and "NO <status> element" in ln for ln in lines2))
        print("  %-4s element replaced by a backticked prose mention only, staged %s -> rc=%d; %s" % (
            "PASS" if ok2 else "FAIL", st2, rc2, (lines2[0][:160] if lines2 else "no status-element refusal")))
        check("RED: the element REPLACED by a backticked prose mention only -> REFUSED identically to no element", ok2)

        # ---- GREEN: <status>pending</status> on its own line -> ADMITTED by this limb
        repo3 = _repo("green-pending")
        _place(repo3, REL, pending_text)
        _git(repo3, "add", REL)
        st3 = _status(repo3, REL)
        rc3, out3 = _gate(repo3, [REL])
        lines3 = _xi_lines(out3, REL)
        ok3 = st3 == "A" and not lines3
        print("  %-4s <status>pending</status>, staged %s -> rc=%d (other limbs' noise tolerated); "
              "status-element lines: %d" % ("PASS" if ok3 else "FAIL", st3, rc3, len(lines3)))
        check("GREEN: <status>pending</status> on its own line -> ADMITTED by this limb", ok3)

        # ---- GREEN: an untagged order COMMITTED, then staged as MODIFIED with the element added
        # back -> NOT graded by this limb (main() feeds check_file only the newly-added set)
        repo4 = _repo("green-modify-not-graded")
        _place(repo4, REL, missing_text)
        _git(repo4, "add", REL)
        _git(repo4, "commit", "-q", "--no-verify", "-m", "the order as issued, untagged")
        _place(repo4, REL, pending_text)
        _git(repo4, "add", REL)
        st4 = _status(repo4, REL)
        rc4, out4 = _gate(repo4, [REL])
        lines4 = _xi_lines(out4, REL)
        ok4 = st4 == "M" and not lines4
        print("  %-4s untagged order COMMITTED then staged %s with the element added -> "
              "status-element lines: %d (not graded on a modify, rc=%d tolerated)" % (
                  "PASS" if ok4 else "FAIL", st4, len(lines4), rc4))
        check("GREEN: an untagged order COMMITTED then staged as MODIFIED with the element added -> NOT graded", ok4)

        # ---- RED: the real order's UNMODIFIED bytes (already <status>complete</status>) staged as
        # ADDED -> refused as born terminal
        repo5 = _repo("red-born-terminal")
        _place(repo5, REL, terminal_text)
        _git(repo5, "add", REL)
        st5 = _status(repo5, REL)
        rc5, out5 = _gate(repo5, [REL])
        lines5 = _xi_lines(out5, REL)
        ok5 = (st5 == "A" and rc5 == 1 and any("born terminal" in ln for ln in lines5))
        print("  %-4s real UNMODIFIED bytes (<status>complete</status>), staged %s -> rc=%d; %s" % (
            "PASS" if ok5 else "FAIL", st5, rc5, (lines5[0][:160] if lines5 else "no status-element refusal")))
        check("RED: bytes born <status>complete</status> -> REFUSED as born terminal", ok5)
    finally:
        shutil.rmtree(SCRATCH, ignore_errors=True)

    failed = [r for r in results if not r[1]]
    print()
    for nm, ok, detail in results:
        print("  %-4s %s%s" % ("PASS" if ok else "FAIL", nm, ("   <- " + detail[:200]) if (detail and not ok) else ""))
    print("RESULT: %d arm(s) failed of %d" % (len(failed), len(results)))
    print("BATTERY PASS" if not failed else "BATTERY FAILED")
    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(main())
