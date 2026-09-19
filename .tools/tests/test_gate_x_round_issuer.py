#!/usr/bin/env python3
"""GATE (x) -- ONE ISSUER PER ROUND, keyed to the ROUND, never the serial.

Subject: `.tools/to-pipeline-gate.py` main() -> _round_issuer_violations() / _head_rounds_for_project()
/ _head_rounds_census(). Built on `AMGT_RESAPP.TO-AMGT-rk-55` (decomp cell AMGT-rk-55; row
AMGT_RESAPP-Z-S154; CLAUDE.md Rule 27, "ONE ISSUER PER ROUND -- and a WORKSTREAM IS A SCOPE, NOT A
ROUND"). Round 13 of AMGT_RESAPP was issued TWICE by two continuations of ONE COO seat serial
(2.0.0_SA_COO~Z) on 2026-09-17; GATE (iv) grades WHO commits and passed both times, because it is
keyed to the SERIAL, not the ROUND. This battery proves the limb that IS keyed to the round.

EVERY ARM RUNS IN A REAL GIT INDEX, THROUGH THE GATE'S OWN CLI, ON REAL ORDER BYTES:
  RED  COLLISION       an order with <round>13</round> COMMITTED under $OPAL_AGENT_SERIAL =
                       2.0.0_SA_COO~Z, then a SECOND file with <round>13</round> staged under the
                       SAME author -- REFUSED at rc=1, naming "round 13" and "S154" (the
                       serial-blind case S154 measured).
  GREEN NEXT ROUND      a <round>14</round> file, no round-14 order at HEAD -- ADMITTED by this
                       limb (other limbs' output on the same run is tolerated and named, not
                       counted).
  GREEN MODIFY NOT GRADED  the committed round-13 order staged as MODIFIED (a status flip) --
                       this limb does not grade it (main() feeds it only the newly-added set).
  RED  MISSING KEY      a new order with NO <round> element -- REFUSED naming the missing key.

Scratch repos live under <WS>/.scratch/ and are removed at the end.
Run: python .tools/tests/test_gate_x_round_issuer.py
Exit 0 = every arm as expected. Exit 1 otherwise.
"""
from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
WORKSPACE = TOOLS.parent
GATE = TOOLS / "to-pipeline-gate.py"
TO_DIR = "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/"
SCRATCH = WORKSPACE / ".scratch" / "rk-55-gate-x-round-issuer"
AUTHOR = "2.0.0_SA_COO~Z"
results: list = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    results.append((name, ok, detail))
    return ok


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


def _order_text(round_line, status="issued") -> str:
    lines = [
        "<decomp_ref>",
        "<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>",
        "<owned_cells>AMGT-rk-99</owned_cells>",
        "</decomp_ref>",
        "<issued_to>0.9.0_WK_AMGT_RESAPP~99</issued_to>",
        "<issued_by>%s</issued_by>" % AUTHOR,
        "<placeholders>NONE</placeholders>",
    ]
    if round_line is not None:
        lines.append(round_line)
    lines += [
        "<preflight>",
        "comp-schedule: DECLARED-NOT-APPLICABLE -- fixture, no cadence",
        "comp-iam: DECLARED-NOT-APPLICABLE -- fixture, no AWS resource",
        "comp-adversary: DECLARED-NOT-APPLICABLE -- fixture, not a produced artifact",
        "</preflight>",
        "<paths>",
        "org/ok.py",
        "</paths>",
        "<status>%s</status>" % status,
        "<proof_of_spec>",
        '  <criterion id="AC1" cell_refs="AMGT-rk-99"><invocation>echo 1</invocation><expect>1</expect></criterion>',
        "</proof_of_spec>",
    ]
    return "\n".join(lines) + "\n"


def _round_lines(output: str, rel: str) -> list:
    return [ln.strip() for ln in output.splitlines() if rel in ln and "ONE ISSUER PER ROUND" in ln]


def main() -> int:
    SCRATCH.mkdir(parents=True, exist_ok=True)
    try:
        rel13 = TO_DIR + "AMGT_RESAPP.TO-AMGT-rk-98.first-into-13.md"
        rel13b = TO_DIR + "AMGT_RESAPP.TO-AMGT-rk-99.second-into-13.md"
        rel14 = TO_DIR + "AMGT_RESAPP.TO-AMGT-rk-100.round-14.md"
        rel_noround = TO_DIR + "AMGT_RESAPP.TO-AMGT-rk-101.no-round.md"

        # ---- RED: a second file with <round>13</round> staged under the SAME author is refused
        repo = _repo("red-collision")
        _place(repo, rel13, _order_text("<round>13</round>"))
        _git(repo, "add", rel13)
        _git(repo, "commit", "-q", "--no-verify", "-m", "round 13 as issued")
        _place(repo, rel13b, _order_text("<round>13</round>"))
        _git(repo, "add", rel13b)
        st = _status(repo, rel13b)
        rc, out = _gate(repo, [rel13b])
        lines = _round_lines(out, rel13b)
        ok = st == "A" and rc == 1 and any("round 13" in ln and "S154" in ln for ln in lines)
        print("  %-4s second round-13 order staged %s -> rc=%d; %s" % (
            "PASS" if ok else "FAIL", st, rc, (lines[0][:160] if lines else "no round-issuer refusal")))
        check("RED: a second round-13 order staged under the same author -> REFUSED naming round 13 and S154", ok)

        # ---- GREEN: a round-14 file is ADMITTED by this limb (other limbs' output tolerated)
        repo2 = _repo("green-next-round")
        _place(repo2, rel13, _order_text("<round>13</round>"))
        _git(repo2, "add", rel13)
        _git(repo2, "commit", "-q", "--no-verify", "-m", "round 13 as issued")
        _place(repo2, rel14, _order_text("<round>14</round>"))
        _git(repo2, "add", rel14)
        st2 = _status(repo2, rel14)
        rc2, out2 = _gate(repo2, [rel14])
        lines2 = _round_lines(out2, rel14)
        ok2 = st2 == "A" and not lines2
        print("  %-4s round-14 order staged %s -> rc=%d (other limbs tolerated); round-issuer lines: %d"
              % ("PASS" if ok2 else "FAIL", st2, rc2, len(lines2)))
        check("GREEN: a round-14 order (none at HEAD) -> ADMITTED by this limb", ok2)

        # ---- GREEN: the committed round-13 order staged as MODIFIED (status flip) is NOT graded
        repo3 = _repo("green-modify-not-graded")
        _place(repo3, rel13, _order_text("<round>13</round>", status="issued"))
        _git(repo3, "add", rel13)
        _git(repo3, "commit", "-q", "--no-verify", "-m", "round 13 as issued")
        _place(repo3, rel13, _order_text("<round>13</round>", status="complete"))
        _git(repo3, "add", rel13)
        st3 = _status(repo3, rel13)
        rc3, out3 = _gate(repo3, [rel13])
        lines3 = _round_lines(out3, rel13)
        ok3 = st3 == "M" and not lines3
        print("  %-4s round-13 order staged %s (status flip) -> round-issuer lines: %d (not graded on a modify, rc=%d tolerated)"
              % ("PASS" if ok3 else "FAIL", st3, len(lines3), rc3))
        check("GREEN: the committed round-13 order staged as MODIFIED (status flip) -> NOT graded by this limb", ok3)

        # ---- RED: a new order with no <round> element is refused naming the missing key
        repo4 = _repo("red-missing-key")
        _place(repo4, rel_noround, _order_text(None))
        _git(repo4, "add", rel_noround)
        st4 = _status(repo4, rel_noround)
        rc4, out4 = _gate(repo4, [rel_noround])
        lines4 = _round_lines(out4, rel_noround)
        ok4 = st4 == "A" and rc4 == 1 and any("line-anchored" in ln for ln in lines4)
        print("  %-4s order with no <round> element staged %s -> rc=%d; %s" % (
            "PASS" if ok4 else "FAIL", st4, rc4, (lines4[0][:160] if lines4 else "no round-issuer refusal")))
        check("RED: a new order with NO <round> element -> REFUSED naming the missing key", ok4)
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
