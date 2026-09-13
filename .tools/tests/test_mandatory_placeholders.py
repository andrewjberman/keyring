#!/usr/bin/env python3
"""GATE (viii) -- the MANDATORY <placeholders> declaration on a newly-added tree task order.

Subject: `.tools/to-pipeline-gate.py` `_placeholder_declaration_violations()` and the L6 gate that
calls it, built 2026-09-12 by `0.9.0_WK_IRPT_FNTEND~4` on `IRPT_FNTEND.TO-FE-s-28` (decomp cell
FE-s-28; rows S31, S38, S43).

WHAT IS BEING ARMED, AND WHY IT COULD NOT ARM ITSELF. `.tools/proof-of-spec-check.py` compares each
acceptance row's RECORDED invocation against the same-id <invocation> in the governing task order.
It ENFORCES that comparison only when the order DECLARES its substitution set -- `<placeholders>WS,
PORT</placeholders>` -- because an undeclared set is a guess and a guess must not refuse. That made
the enforcement OPT-IN, and the party who opts in is the ISSUER: the exact party whose prompt-only
correction the limb exists to catch (round 2, row S31: two criteria corrected in a SPAWN PROMPT and
never in the file; the checker read VALID over 20 rows and 0 violations). 1.0.0_SA_CTO ruling D
closes that: the declaration is MANDATORY at the L6 gate. NON-APPLICATION: none.

    A LIMB THAT REFUSES EVERYTHING IS AS USELESS AS ONE THAT REFUSES NOTHING,
    AND A CONTROL BUILT FROM A STRING ITS AUTHOR INVENTED CERTIFIES NOTHING AT ALL.

So every arm below is built from REAL corpus bytes -- three task orders this estate actually cut --
and the two directions differ by EXACTLY the inserted element:

  UNDECLARED NEW TO REFUSED   3 real tree orders, unmodified bytes, staged as ADDED in a real git
                              index and run through the gate's own CLI: each REFUSED, each refusal
                              naming the element and the file.
  DECLARED NEW TO ADMITTED    the SAME 3 files with one line inserted (declaring exactly the tokens
                              their own invocations carry): this limb silent on all 3, and the
                              gate's OTHER refusals byte-identical between the two runs -- so the
                              delta is attributable to the element and to nothing else.
  EXISTING CORPUS COMMITTABLE the boundary, measured end-to-end rather than asserted: ONE real order,
                              ONE gate run, TWO git states -- refused as an ADD, admitted as a
                              MODIFY -- plus the census of what the corpus carries today.
  REFUSAL TEXT                the refusal names the element, the rule, the boundary (what it binds
                              and what it does not) and how to satisfy it. A fail-closed gate's
                              error text is its AUTHOR'S CLAIM, so this arm asserts what the text
                              SAYS; the arms above are what prove it keys on the right thing.
  CROSS-TOOL AGREEMENT        the gate's reader and proof-of-spec-check's `_declared_placeholders`
                              return the same verdict on the same bytes, including the UPPERCASE
                              <PLACEHOLDERS> near-miss. A gate that admitted an element the checker
                              cannot see would certify an order that arms nothing.

Run: python .tools/tests/test_mandatory_placeholders.py
Exit 0 = every arm as expected. Exit 1 = at least one arm did not.
"""
from __future__ import annotations

import importlib.util
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
WORKSPACE = TOOLS.parent
GATE = TOOLS / "to-pipeline-gate.py"
CHECKER = TOOLS / "proof-of-spec-check.py"

PASS, FAIL = "PASS", "FAIL"
results: list = []


def check(name: str, ok: bool, detail: str = "") -> None:
    results.append((name, PASS if ok else FAIL, detail))


def _load(path: Path, name: str):
    """The module names carry hyphens, so a plain import cannot reach them."""
    spec = importlib.util.spec_from_file_location(name, str(path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


gate = _load(GATE, "to_pipeline_gate_ph")
_raw_limb = gate._placeholder_declaration_violations


def limb(rel: str, text: str) -> list:
    """The limb under test, with an exception converted into a SCOREABLE result rather than a
    crash: a battery that dies on the defect it exists to catch cannot score it. The returned
    marker matches no arm's expectation, so a raise FAILS every arm and passes none."""
    try:
        return _raw_limb(rel, text)
    except Exception as exc:  # noqa: BLE001
        return ["BATTERY: the limb RAISED %s: %s" % (type(exc).__name__, exc)]


# --------------------------------------------------------------------------- the real corpus
def _tracked() -> list:
    out = subprocess.run(["git", "ls-files", "-z"], cwd=str(WORKSPACE), capture_output=True,
                         text=True, encoding="utf-8", errors="replace", timeout=120)
    if out.returncode != 0:
        return []
    return [p for p in out.stdout.split("\0") if p]


def _read(rel: str) -> str:
    return (WORKSPACE / rel).read_text(encoding="utf-8", errors="replace")


TRACKED = _tracked()
ALL_TOS = [p for p in TRACKED if gate.TO_PATH_RE.search(p)]
TREE_TOS = [p for p in ALL_TOS if gate.TREE_TO_RE.search(p)]
FLAT_TOS = [p for p in ALL_TOS if not gate.TREE_TO_RE.search(p)]
DECLARING = [p for p in ALL_TOS if "<placeholders>" in _read(p)]
UNDECLARED_TREE = [p for p in TREE_TOS if "<placeholders>" not in _read(p)]


def _specimens(n: int = 3) -> list:
    """n REAL tree task orders that lack the element and carry at least one <invocation>, taken
    from DISTINCT projects where the corpus allows it. Deterministic (sorted), so the battery
    grades the same bytes on every run and a specimen can be cited."""
    by_project: dict = {}
    for rel in sorted(UNDECLARED_TREE):
        if "<invocation>" not in _read(rel):
            continue
        key = rel.rsplit("/task-orders/", 1)[0]
        by_project.setdefault(key, []).append(rel)
    picked: list = []
    for key in sorted(by_project):
        picked.append(by_project[key][0])
        if len(picked) == n:
            return picked
    for key in sorted(by_project):          # fall back to same-project specimens
        for rel in by_project[key]:
            if rel not in picked:
                picked.append(rel)
            if len(picked) == n:
                return picked
    return picked


SPECIMENS = _specimens(3)


def _declaration_for(text: str) -> str:
    """The element the order's OWN invocations require -- never a token invented here."""
    used = set()
    for m in gate.INVOCATION_TAG_RE.finditer(text):
        used |= set(gate.PLACEHOLDER_TOKEN_RE.findall(m.group(1)))
    body = ", ".join(sorted(used)) if used else "NONE"
    return "<placeholders>%s</placeholders>" % body


def _declare(text: str) -> str:
    """Insert the declaration, changing nothing else. Before the <paths> block when there is one
    (where FE-s-28's own face carries it), else before <preflight>, else appended."""
    line = _declaration_for(text) + "\n\n"
    for anchor in ("<paths>", "<preflight>"):
        i = text.find(anchor)
        if i != -1:
            return text[:i] + line + text[i:]
    return text + "\n" + line


# --------------------------------------------------------------------------- a real git index
def _git(repo: Path, *args: str, quiet: bool = True):
    cmd = ["git", "-c", "core.hooksPath=" + str(repo / ".nohooks"),
           "-c", "user.name=battery", "-c", "user.email=battery@opal.agent", *args]
    return subprocess.run(cmd, cwd=str(repo), capture_output=True, text=True,
                          encoding="utf-8", errors="replace", timeout=180)


def _new_repo(tmp: Path, name: str) -> Path:
    repo = tmp / name
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


def _run_gate(repo: Path, rels: list):
    env = dict(os.environ)
    env["OPAL_AGENT_SERIAL"] = "2.0.0_SA_COO"   # the issuer seat, so GATE (iv) is not the story
    env.pop("STAGED", None)
    out = subprocess.run([sys.executable, str(GATE), *rels], cwd=str(repo), capture_output=True,
                         text=True, encoding="utf-8", errors="replace", timeout=300, env=env)
    return out.returncode, (out.stdout or "") + (out.stderr or "")


def _ph_lines(output: str, rel: str) -> list:
    """The lines of a gate run that are THIS limb's refusal of THIS file."""
    return [ln.strip() for ln in output.splitlines()
            if rel in ln and "<placeholders>" in ln]


def _other_lines(output: str) -> list:
    """Every refusal line of a gate run that is NOT this limb's -- the invariant half."""
    return sorted(ln.strip() for ln in output.splitlines()
                  if ln.startswith("    ") and "<placeholders>" not in ln)


# --------------------------------------------------------------------------- arms
def main() -> int:
    if len(SPECIMENS) != 3:
        check("specimens: three REAL undeclared tree task orders available to test against",
              False, "found %d; the battery refuses to score itself on fixtures it invented"
              % len(SPECIMENS))
        _report()
        return 1
    check("specimens: three REAL undeclared tree task orders, from the committed corpus",
          True, "; ".join(SPECIMENS))

    tmp = Path(tempfile.mkdtemp(prefix="ph-gate-battery-"))
    try:
        # ---- ARM 1 (F28-AC2): three REAL undeclared orders, staged as ADDED, through the CLI.
        repo_a = _new_repo(tmp, "undeclared")
        for rel in SPECIMENS:
            _place(repo_a, rel, _read(rel))
        _git(repo_a, "add", *SPECIMENS)
        rc_a, out_a = _run_gate(repo_a, SPECIMENS)
        refused = []
        for rel in SPECIMENS:
            lines = _ph_lines(out_a, rel)
            named = bool(lines) and any("NO <placeholders> element" in ln for ln in lines)
            check("UNDECLARED (real bytes, staged ADDED): %s -> refused, refusal names the element and the file"
                  % rel.rsplit("/", 1)[-1], named, (lines[0][:200] if lines else "no refusal line"))
            if named:
                refused.append(rel)
        check("UNDECLARED: the gate's exit code is a REFUSAL (rc=1), not merely a printed complaint",
              rc_a == 1, "rc=%d" % rc_a)

        # ---- ARM 2 (F28-AC3): the SAME three files + one inserted line.
        repo_b = _new_repo(tmp, "declared")
        for rel in SPECIMENS:
            _place(repo_b, rel, _declare(_read(rel)))
        _git(repo_b, "add", *SPECIMENS)
        rc_b, out_b = _run_gate(repo_b, SPECIMENS)
        admitted = []
        for rel in SPECIMENS:
            lines = _ph_lines(out_b, rel)
            check("DECLARED (same bytes + one line): %s -> this limb is silent"
                  % rel.rsplit("/", 1)[-1], not lines, (lines[0][:200] if lines else ""))
            if not lines:
                admitted.append(rel)
        check("DELTA ATTRIBUTION: every OTHER refusal is byte-identical across the two runs, so the "
              "difference is the element and nothing else",
              _other_lines(out_a) == _other_lines(out_b),
              "undeclared=%d other line(s), declared=%d" % (len(_other_lines(out_a)), len(_other_lines(out_b))))

        # ---- ARM 3 (F28-AC4): the boundary, ONE run, TWO git states, IDENTICAL bytes.
        spec = SPECIMENS[0]
        repo_c = _new_repo(tmp, "boundary")
        _place(repo_c, spec, _read(spec))
        _git(repo_c, "add", spec)
        _git(repo_c, "commit", "-q", "--no-verify", "-m", "an order that already exists")
        with open(repo_c / spec, "a", encoding="utf-8", newline="\n") as fh:
            fh.write("\n<!-- amended in place; still no <placeholders> element -->\n")
        twin = spec.rsplit("/", 1)[0] + "/ZZZ_TWIN.TO-BOUNDARY-1.md"
        _place(repo_c, twin, _read(spec))
        _git(repo_c, "add", spec, twin)
        rc_c, out_c = _run_gate(repo_c, [spec, twin])
        mod_lines, add_lines = _ph_lines(out_c, spec), _ph_lines(out_c, twin)
        check("BOUNDARY: the same bytes staged as an ADD are REFUSED (positive control on the one run)",
              bool(add_lines), (add_lines[0][:160] if add_lines else "no refusal -- the run proves nothing"))
        check("BOUNDARY: an existing order MODIFIED in place is NOT graded by this limb",
              not mod_lines, (mod_lines[0][:160] if mod_lines else ""))
        check("BOUNDARY: the flat-root legacy population is out of scope by path",
              limb("org/tier2_senior/A/task_orders/X.TO-1.md", _read(spec)) == [])
        boundary_ok = bool(add_lines) and not mod_lines and not limb(
            "org/tier2_senior/A/task_orders/X.TO-1.md", _read(spec))

        # ---- ARM 4 (F28-AC5): what the refusal TEXT says.
        text_only = limb("org/missions/D9/IRPT/IRPT_FNTEND/task-orders/X.TO-1.md", "<invocation>cd <WS> && x</invocation>")
        need = {"the element": "<placeholders>",
                "the rule": "MANDATORY at L6",
                "the boundary keyword": "BOUNDARY",
                "what it binds": "STAGED AS ADDED",
                "what it does NOT bind (a modification)": "MODIFICATION",
                "what it does NOT bind (the legacy root)": "org/**/task_orders/",
                "how to satisfy it": "<placeholders>NONE</placeholders>"}
        missing = [k for k, v in need.items() if not text_only or v not in text_only[0]]
        check("REFUSAL TEXT: names the element, the rule, both sides of the boundary and how to satisfy it",
              not missing, "missing: " + ", ".join(missing) if missing else "")

        # ---- ARM 5: cross-tool agreement -- the gate arms the element the CHECKER reads.
        checker = _load(CHECKER, "pos_check_ph")
        und, dec = _read(spec), _declare(_read(spec))
        upper = dec.replace("<placeholders>", "<PLACEHOLDERS>").replace("</placeholders>", "</PLACEHOLDERS>")
        check("CROSS-TOOL: undeclared -> checker reads None (ANNOUNCE) and the gate REFUSES",
              checker._declared_placeholders(und) is None and bool(limb(spec, und)))
        check("CROSS-TOOL: declared -> checker reads a SET (ENFORCE) and the gate ADMITS",
              isinstance(checker._declared_placeholders(dec), set) and limb(spec, dec) == [])
        check("CROSS-TOOL: an UPPERCASE <PLACEHOLDERS> is invisible to the checker, and the gate refuses it too",
              checker._declared_placeholders(upper) is None and bool(limb(spec, upper)))

        # ---- ARM 6: the two orders that ALREADY carry the element are admitted (real positive control).
        for rel in DECLARING:
            check("REAL DECLARING ORDER ADMITTED: %s" % rel.rsplit("/", 1)[-1],
                  limb(rel, _read(rel)) == [], "; ".join(limb(rel, _read(rel)))[:200])

        # ---- the four bar lines, each printed from the arms' own counts.
        print()
        print("UNDECLARED NEW TO REFUSED: %d of %d   (real corpus bytes, staged as ADDED in a real git "
              "index, refused by the gate's own CLI at rc=%d; each refusal names <placeholders> and the file)"
              % (len(refused), len(SPECIMENS), rc_a))
        print("DECLARED NEW TO ADMITTED: %d of %d   (the SAME bytes plus one declaration line; this limb "
              "silent, and every other refusal byte-identical to the run above)"
              % (len(admitted), len(SPECIMENS)))
        if boundary_ok:
            print("EXISTING CORPUS STILL COMMITTABLE: %d task-order files tracked (%d tree, %d flat-root "
                  "legacy), %d carry <placeholders>, %d tree orders lack it and 0 of them are graded -- "
                  "BOUNDARY: the limb binds ONLY a file STAGED AS ADDED (git A/R) under "
                  "org/missions/D*/*/*/task-orders/*.md; a MODIFICATION of an existing order and the whole "
                  "org/**/task_orders/ population are never graded (measured end-to-end: identical bytes, "
                  "REFUSED as an add and ADMITTED as a modify, in one gate run)."
                  % (len(ALL_TOS), len(TREE_TOS), len(FLAT_TOS), len(DECLARING), len(UNDECLARED_TREE)))
        else:
            print("EXISTING CORPUS: BOUNDARY ARM DID NOT HOLD -- see the FAIL line(s) above.")
        if not missing:
            print("REFUSAL TEXT NAMES THE RULE AND ITS BOUNDARY: the missing element, the ruling that "
                  "makes it MANDATORY at L6, what the rule binds (a task order STAGED AS ADDED under "
                  "org/missions/D<n>/<MACRO>/<CODE>/task-orders/), what it does NOT bind (a MODIFICATION "
                  "of an existing order; the flat-root org/**/task_orders/ population) and how to satisfy "
                  "it (<placeholders>WS, PORT</placeholders>, or <placeholders>NONE</placeholders>).")
        else:
            print("REFUSAL TEXT INCOMPLETE: missing " + ", ".join(missing))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    return _report()


def _report() -> int:
    width = max(len(n) for n, _, _ in results)
    for name, verdict, detail in results:
        line = "  %-4s %s" % (verdict, name.ljust(width))
        if verdict == FAIL and detail:
            line += "   <- " + detail[:300]
        print(line)
    failed = [r for r in results if r[1] == FAIL]
    print("\nmandatory-placeholders battery: %d/%d arms as expected" % (len(results) - len(failed), len(results)))
    if failed:
        print("BATTERY FAILED -- the gate does not behave as specified.")
        return 1
    print("BATTERY PASS -- an undeclared NEW order is refused, a declared one is admitted, the existing "
          "corpus is untouched, and the refusal teaches the rule.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
