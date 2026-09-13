#!/usr/bin/env python3
"""LIMB 4 -- GATE (viii) grades a MODIFICATION of an order that ALREADY DECLARES <placeholders>.

Subject: `.tools/to-pipeline-gate.py` main() -> _staged_modified() / _head_blob() /
_placeholder_modify_violations(). Built 2026-09-13 by `0.9.0_WK_IRPT_FNTEND~4` on `IRPT_FNTEND.TO-FE-s-29`
(decomp cell FE-s-29; Andrew-direct card 6, ~18:4xZ 2026-09-13, "recs approved", record @e2210bf34c).

THE RULING. Gate (viii) used to grade only orders STAGED AS ADDED. It now also grades an order staged as
MODIFIED -- only if that order already declares <placeholders> at HEAD. Nothing is back-filled.

EVERY ARM RUNS IN A REAL GIT INDEX, THROUGH THE GATE'S OWN CLI, ON REAL ORDER BYTES (`git show HEAD:`):
  BROKEN DECLARATION REFUSED   a real declaring order (FE-s-28, FE-s-23) committed, then staged as MODIFIED
                               with its declaration broken two ways -- the element line deleted, and the
                               element re-pointed at a token its invocations do not carry -- each REFUSED
                               at rc=1, the refusal naming the file and saying it is a MODIFY.
  CONTROL                      the SAME order staged as MODIFIED with the declaration intact (an amendment
                               line appended) -- ADMITTED at rc=0. So the refusal is the broken declaration's.
  UNDECLARED NOT GRADED        a real order that does NOT declare (FE-s-27) committed, then staged as
                               MODIFIED -- amended, and amended so as to ADD a broken declaration -- never
                               named by this limb; and in the SAME gate run a twin of the same bytes staged
                               as ADDED IS refused by this limb, so the run could have fired.

Scratch repos live under <WS>/.scratch/ and are removed at the end.
Run: python .tools/tests/test_gate_viii_modify.py
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
TO_DIR = "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/"
SCRATCH = WORKSPACE / ".scratch" / "fe-s-29-gate8"
results: list = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    results.append((name, ok, detail))
    return ok


def _ws_git(*args: str) -> str:
    out = subprocess.run(["git", *args], cwd=str(WORKSPACE), capture_output=True, text=True,
                         encoding="utf-8", errors="replace", timeout=120)
    if out.returncode != 0:
        raise RuntimeError("git %s rc=%d" % (" ".join(args[:2]), out.returncode))
    return out.stdout


def _order(stem: str) -> str:
    return next(p for p in _ws_git("ls-files", "--", TO_DIR).splitlines()
                if p.rsplit("/", 1)[-1].startswith("IRPT_FNTEND.TO-%s." % stem))


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
    env["OPAL_AGENT_SERIAL"] = "2.0.0_SA_COO"
    env.pop("STAGED", None)
    out = subprocess.run([sys.executable, str(GATE), *rels], cwd=str(repo), capture_output=True, text=True,
                         encoding="utf-8", errors="replace", timeout=300, env=env)
    return out.returncode, (out.stdout or "") + (out.stderr or "")


def _ph_lines(output: str, rel: str) -> list:
    return [ln.strip() for ln in output.splitlines() if rel in ln and "<placeholders>" in ln]


def _status(repo: Path, rel: str) -> str:
    st = _git(repo, "diff", "--cached", "--name-status").stdout
    return next((ln.split("\t")[0] for ln in st.splitlines() if ln.split("\t")[-1] == rel), "?")


def _element_line(text: str) -> str:
    return next(ln for ln in text.split("\n")
                if ln.strip().startswith("<placeholders>") and ln.strip().endswith("</placeholders>"))


def _modify_run(name: str, rel: str, head_text: str, staged_text: str):
    repo = _repo(name)
    _place(repo, rel, head_text)
    _git(repo, "add", rel)
    _git(repo, "commit", "-q", "--no-verify", "-m", "the order as issued")
    _place(repo, rel, staged_text)
    _git(repo, "add", rel)
    st = _status(repo, rel)
    rc, out = _gate(repo, [rel])
    return st, rc, out


def main() -> int:
    SCRATCH.mkdir(parents=True, exist_ok=True)
    try:
        # ---- AC11: declaring orders, broken on a MODIFY -> REFUSED; intact on a MODIFY -> ADMITTED
        n_ref = n_arm = n_ctl = n_ctl_ok = 0
        for stem in ("FE-s-28", "FE-s-23"):
            rel = _order(stem)
            text = _ws_git("show", "HEAD:" + rel)
            el = _element_line(text)
            broken = {
                "element line deleted": text.replace(el + "\n", "", 1),
                "element re-pointed at a token its invocations do not carry": text.replace(
                    el, el.replace("WS", "PORT"), 1),
            }
            for how, staged in broken.items():
                n_arm += 1
                st, rc, out = _modify_run("%s-%d" % (stem, n_arm), rel, text, staged)
                lines = _ph_lines(out, rel)
                ok = st == "M" and rc == 1 and any("MODIFIED" in ln for ln in lines)
                n_ref += ok
                print("  %-4s %s staged %s, %s -> rc=%d; %s" % ("PASS" if ok else "FAIL", stem, st, how, rc,
                                                              (lines[0].split("]: ", 1)[-1][:120] if lines else "no refusal line")))
                check("BROKEN %s (%s) staged as MODIFIED -> REFUSED naming the modify" % (stem, how), ok)
            n_ctl += 1
            st, rc, out = _modify_run("%s-ctl" % stem, rel, text, text + "\n<!-- amended in place; declaration intact -->\n")
            ok = st == "M" and rc == 0 and not _ph_lines(out, rel) and "already declare" in out
            n_ctl_ok += ok
            print("  %-4s %s staged %s, amended with the declaration intact -> rc=%d (control)" % (
                "PASS" if ok else "FAIL", stem, st, rc))
            check("CONTROL %s amended, declaration intact -> ADMITTED, and the gate says it graded it" % stem, ok)
        if n_ref == n_arm and n_ctl_ok == n_ctl:
            print("MODIFIED DECLARING ORDER, BROKEN DECLARATION: REFUSED %d of %d (FE-s-28, FE-s-23; element deleted "
                  "and element under-declared), each at rc=1 naming the file and the modify; control: the same orders "
                  "amended with the declaration intact ADMITTED %d of %d at rc=0" % (n_ref, n_arm, n_ctl_ok, n_ctl))
        else:
            print("MODIFIED DECLARING ORDER, BROKEN DECLARATION: NOT AS SPECIFIED (%d of %d refused, %d of %d controls)"
                  % (n_ref, n_arm, n_ctl_ok, n_ctl))

        # ---- AC12: an undeclared order staged as MODIFIED is NOT graded; a same-run ADD twin IS
        rel = _order("FE-s-27")
        text = _ws_git("show", "HEAD:" + rel)
        declares = any(ln.strip().startswith("<placeholders>") for ln in text.split("\n"))
        check("FE-s-27 does not declare <placeholders> at HEAD (the premise of the arm)", not declares)
        ok_all = True
        for how, staged in (("amended in place", text + "\n<!-- amended in place; still no element -->\n"),
                            ("amended to ADD a broken declaration", "<placeholders>PORT</placeholders>\n" + text)):
            st, rc, out = _modify_run("FE-s-27-%s" % how.split()[-1], rel, text, staged)
            named = _ph_lines(out, rel)
            ok = st == "M" and rc == 0 and not named
            ok_all &= ok
            print("  %-4s FE-s-27 staged %s, %s -> rc=%d, lines naming it from this limb: %d" % (
                "PASS" if ok else "FAIL", st, how, rc, len(named)))
            check("UNDECLARED FE-s-27 %s, staged as MODIFIED -> NOT GRADED" % how, ok)
        # the same run, with a twin of the same bytes staged as ADDED: the limb must fire on the twin only
        repo = _repo("FE-s-27-twin")
        _place(repo, rel, text)
        _git(repo, "add", rel)
        _git(repo, "commit", "-q", "--no-verify", "-m", "the order as issued")
        _place(repo, rel, text + "\n<!-- amended in place; still no element -->\n")
        twin = rel.rsplit("/", 1)[0] + "/IRPT_FNTEND.TO-ZZ-TWIN-1.boundary.md"
        _place(repo, twin, text)
        _git(repo, "add", rel, twin)
        st_m, st_a = _status(repo, rel), _status(repo, twin)
        rc, out = _gate(repo, [rel, twin])
        twin_lines, mod_lines = _ph_lines(out, twin), _ph_lines(out, rel.rsplit("/", 1)[-1] + ":")
        twin_ok = st_m == "M" and st_a == "A" and any("NO <placeholders> element" in ln for ln in twin_lines) \
            and not [ln for ln in _ph_lines(out, rel) if twin not in ln]
        ok_all &= twin_ok
        print("  %-4s same run: FE-s-27 staged %s is not named; its ADDED twin (staged %s) IS refused by this limb "
              "(%d line(s)) -- the run could have fired" % ("PASS" if twin_ok else "FAIL", st_m, st_a, len(twin_lines)))
        check("POSITIVE CONTROL in the same gate run: the ADDED twin is refused, the MODIFIED original is not", twin_ok)
        del mod_lines
        if ok_all and not declares:
            print("MODIFIED ORDER WITHOUT THE ELEMENT: NOT GRADED (FE-s-27, amended and amended-to-add-a-broken-"
                  "declaration, rc=0 both; nothing is back-filled; a same-run ADDED twin of the same bytes IS refused)")
        else:
            print("MODIFIED ORDER WITHOUT THE ELEMENT: NOT AS SPECIFIED -- see the FAIL lines below")
    finally:
        shutil.rmtree(SCRATCH, ignore_errors=True)

    failed = [r for r in results if not r[1]]
    print()
    for nm, ok, detail in results:
        print("  %-4s %s%s" % ("PASS" if ok else "FAIL", nm, ("   <- " + detail[:200]) if (detail and not ok) else ""))
    print("gate-viii-modify battery: %d of %d arm(s) as expected" % (len(results) - len(failed), len(results)))
    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(main())
