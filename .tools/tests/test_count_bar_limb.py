#!/usr/bin/env python3
"""LIMB 2 -- the COUNT-BAR limb of `.tools/proof-of-spec-check.py` (count_bar_check).

Built 2026-09-13 by `0.9.0_WK_IRPT_FNTEND~4` on `IRPT_FNTEND.TO-FE-s-29` (decomp cell FE-s-29;
1.0.0_SA_CTO RULING M(ii) @23af9479ab; row IRPT_FNTEND-S56).

THE CLASS. The checker decides a mechanical criterion with an UNANCHORED re.search of the bar over the
evidence and raises nothing when it matches. So a `0 fail` bar passes ` 10 fail` (shape a -- the `0 fail`
inside `10 fail`), and passes evidence that ALSO carries a contradicting count (shape b -- F17-AC8's
committed evidence holds its deciding ` 0 fail` AND a BEFORE note's ` 1 fail`). The limb refuses a PASS
whose evidence carries a NONZERO count for the noun a zero-count bar asserts: REFUSE new, ANNOUNCE legacy.

EVERY INPUT IS A REAL SHAPE, NEVER A STRING CHOSEN SO THAT IT PASSES:
  shape (a)       a REAL `bun test` summary -- bun is run here on a scratch suite of TEN failing tests under
                  <WS>/.scratch/, and its own summary block is the evidence (` 10 fail`, ANSI and all)
  shape (b)       F17-AC8's COMMITTED row, read by `git show HEAD:`, carried by a NEW instance
  plain zero      a COMMITTED plain ` 0 fail` evidence (F10-AC10's row, read by `git show HEAD:`)
  ANSI zero       a REAL coloured `bun test` summary of a scratch suite whose tests all pass
  F18-AC17        its committed pass-2 evidence (` 486 pass |  1 skip |  0 fail`)
  legacy          F17-AC8's committed INSTANCE, unmodified, through the checker's own CLI
The bar in shape (a) and the zero arms is `0 fail`, the most common bar in the estate, read from the real
order F10-AC10 carries it on.

THE BOUNDARY IS DERIVED, NOT INJECTED. A NEW instance is one whose governing order was first added in a
commit that descends from the ruling pin; the NEW arms carry the first tracked IRPT_FNTEND order (sorted)
that the checker's own _cut_after() calls NEW, and the legacy arm carries F17's own order. The pin is
content-checked: the ruling document AT THE PIN carries RULING M's own words.

A CONTROL REFUSED FOR THE WRONG REASON PROVES NOTHING (row S52). So every refused case first prints that
the bar's own regex DOES match its evidence and that conditional_checks() -- the existing grader -- raises
nothing on it: the refusal is the limb's, not the existing search's.

Run: python .tools/tests/test_count_bar_limb.py
Exit 0 = every arm as expected. Exit 1 otherwise.
"""
from __future__ import annotations

import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
WORKSPACE = TOOLS.parent
CHECKER = TOOLS / "proof-of-spec-check.py"
TO_DIR = "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/"
DELIV = "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/"
F17_INST = DELIV + "0.9.0_WK_IRPT_FNTEND~2/IRPT_FNTEND.TO-FE-s-17.lato-packaging.proof_of_spec.json"
F18_INST = DELIV + "0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-18.evidence-mobile-captures.proof_of_spec.json"
F10_INST = DELIV + "0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-10.global-view.proof_of_spec.json"
SCRATCH = WORKSPACE / ".scratch" / "fe-s-29-countbar"


def _load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, str(path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


checker = _load(CHECKER, "pos_check_l2")
results: list = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    results.append((name, ok, detail))
    return ok


def _safe(s: str, n: int = 160) -> str:
    """ASCII-only rendering of real output: ESC shown as \\x1b, anything else non-ASCII as '?'."""
    s = (s or "").replace("\x1b", "\\x1b").replace("\n", " | ")
    return s.encode("ascii", "replace").decode("ascii")[:n]


def _git(*args: str) -> str:
    out = subprocess.run(["git", *args], cwd=str(WORKSPACE), capture_output=True, text=True,
                         encoding="utf-8", errors="replace", timeout=120)
    if out.returncode != 0:
        raise RuntimeError("git %s rc=%d: %s" % (" ".join(args[:2]), out.returncode, out.stderr.strip()[:160]))
    return out.stdout


def _row(inst_rel: str, cid: str) -> dict:
    inst = json.loads(_git("show", "HEAD:" + inst_rel))
    return next(r for r in inst["acceptance"] if r.get("criterion_id") == cid)


def _bar_from_order(stem: str, cid: str) -> str:
    rel = next(p for p in _git("ls-files", "--", TO_DIR).splitlines()
               if p.rsplit("/", 1)[-1].startswith("IRPT_FNTEND.TO-%s." % stem))
    text = _git("show", "HEAD:" + rel)
    for m in checker.CRITERION_BLOCK_RE.finditer(text):
        if dict(checker.ATTR_RE.findall(m.group(1))).get("id", "").strip() == cid:
            e = re.search(r"<expect>(.*?)</expect>", m.group(2), re.S)
            if e:
                return e.group(1)
    raise RuntimeError("no <expect> for %s in %s" % (cid, rel))


def _first_new_order():
    """(rel, to_id, reason) of the first tracked IRPT_FNTEND order (sorted) the checker calls NEW."""
    for rel in sorted(_git("ls-files", "--", TO_DIR).splitlines()):
        new, why = checker._cut_after(rel, checker.COUNT_BAR_RULING)
        if new is True:
            to_id = re.search(r"<to_id>([^<]+)</to_id>", _git("show", "HEAD:" + rel)).group(1).strip()
            return rel, to_id, why
    raise RuntimeError("no tracked IRPT_FNTEND order is cut after the ruling -- the NEW side cannot be exercised")


def _bun() -> str | None:
    found = shutil.which("bun")
    if found:
        return found
    for name in ("bun.exe", "bun"):
        p = Path.home() / ".bun" / "bin" / name
        if p.is_file():
            return str(p)
    return None


def _bun_summary(suite: str, body: str, env_extra: dict) -> str:
    """Run bun on a scratch suite and return ITS OWN final summary block, unmodified (ANSI included)."""
    bun = _bun()
    if bun is None:
        raise RuntimeError("bun not found on PATH or under ~/.bun/bin -- a REAL bun summary cannot be produced")
    SCRATCH.mkdir(parents=True, exist_ok=True)
    with open(SCRATCH / suite, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(body)
    env = dict(os.environ)
    env.update(env_extra)
    out = subprocess.run([bun, "test", "./" + suite], cwd=str(SCRATCH), capture_output=True, text=True,
                         encoding="utf-8", errors="replace", timeout=180, env=env)
    lines = ((out.stdout or "") + (out.stderr or "")).splitlines()
    plain = [checker._ANSI_RE.sub("", ln) for ln in lines]
    i = max(k for k, ln in enumerate(plain) if re.search(r"^\s*\d+ pass\b", ln))
    j = next(k for k in range(i, len(plain)) if plain[k].lstrip().startswith("Ran "))
    return "\n".join(lines[i:j + 1])


TEN_FAIL = ("import { expect, test } from 'bun:test'\n"
            "for (let i = 1; i <= 10; i++) {\n"
            "  test('fe-s-29 scratch failing arm ' + i, () => { expect(i).toBe(0) })\n"
            "}\n")
ALL_PASS = ("import { expect, test } from 'bun:test'\n"
            "for (let i = 1; i <= 5; i++) {\n"
            "  test('fe-s-29 scratch passing arm ' + i, () => { expect(i).toBe(i) })\n"
            "}\n")


def _new_instance(to_id: str, to_rel: str, row: dict) -> dict:
    return {"to_id": to_id, "decomp_ref": {"to_ref": to_rel}, "acceptance": [row]}


def _grader_admits(row: dict) -> tuple:
    """(bar matches its evidence by the grader's own call, conditional_checks raises nothing on the row)."""
    matched = re.search(row["expect"], row.get("output_evidence", ""), re.S | re.M) is not None
    existing = [x for x in checker.conditional_checks({"acceptance": [row]}) if x.startswith("acceptance[")]
    return matched, existing


def main() -> int:
    # ---- the boundary, derived and content-checked
    doc_at_pin = _git("show", "%s:%s" % (checker.COUNT_BAR_RULING, checker.RULING_DOC))
    pin_ok = "RULING M -- BOTH CHECKER LIMBS ADOPTED" in doc_at_pin and "REFUSE for new instances" in doc_at_pin
    check("boundary: the ruling pin %s carries RULING M(ii)'s own words in %s" % (
        checker.COUNT_BAR_RULING, checker.RULING_DOC.rsplit("/", 1)[-1]), pin_ok)
    new_rel, new_to, new_why = _first_new_order()
    print("NEW governing order (derived): %s" % new_why)
    f17_rel = next(p for p in _git("ls-files", "--", TO_DIR).splitlines() if "TO-FE-s-17." in p)
    old_new, old_why = checker._cut_after(f17_rel, checker.COUNT_BAR_RULING)
    print("LEGACY governing order (derived): %s" % old_why)
    check("boundary: F17's order is LEGACY and the chosen order is NEW, both by the checker's own derivation",
          old_new is False)
    bar = _bar_from_order("FE-s-10", "F10-AC10")
    print("bar under test (read from the real F10-AC10 criterion): %r" % bar)

    # ---- POSITIVE ARMS: a contradicting count carried by a NEW instance is REFUSED
    refused, positives = 0, []
    try:
        ev_a = _bun_summary("tenfail.test.ts", TEN_FAIL, {})
        positives.append(("shape (a): a REAL bun summary of ten failing scratch tests",
                          {"criterion_id": "F10-AC10", "criterion_verbatim": "the suite is green",
                           "method": "test_suite", "invocation": "bun test ./tenfail.test.ts",
                           "output_evidence": ev_a, "denominator": "10 tests", "status": "PASS", "expect": bar}))
    except Exception as exc:  # noqa: BLE001
        check("shape (a): a REAL bun summary could be produced", False, str(exc))
    positives.append(("shape (b): F17-AC8's COMMITTED row (git show HEAD:), carried by a NEW instance",
                      dict(_row(F17_INST, "F17-AC8"))))
    for label, row in positives:
        matched, existing = _grader_admits(row)
        v, fr = checker.count_bar_check(_new_instance(new_to, new_rel, row))
        mode_new = any("mode ENFORCE" in f for f in fr)
        ok = matched and not existing and mode_new and len(v) >= 1
        refused += ok
        print("%s" % label)
        print("    evidence: %s" % _safe(row["output_evidence"], 150))
        print("    the bar's own re.search MATCHES the evidence: %s; conditional_checks raises on it: %s"
              % ("yes" if matched else "NO", "nothing" if not existing else _safe(existing[0], 80)))
        print("    limb: mode %s, %s" % ("ENFORCE" if mode_new else "NOT ENFORCE",
                                          ("REFUSED -- " + _safe(v[0].split(" -- but ", 1)[-1], 150)) if v else "ADMITTED"))
        check("POSITIVE %s -> REFUSED by the limb, not by the existing search" % label.split(":")[0], ok)
    print("CONTRADICTING COUNT, NEW INSTANCE: REFUSED %d of %d" % (refused, len(positives)))

    # ---- the limb is WIRED into main(): the real CLI over shape (b) as a full instance file
    SCRATCH.mkdir(parents=True, exist_ok=True)
    full = json.loads(_git("show", "HEAD:" + F17_INST))
    full["to_id"] = new_to
    full.setdefault("decomp_ref", {})["to_ref"] = new_rel
    cli_file = SCRATCH / "shape_b_new_instance.proof_of_spec.json"
    with open(cli_file, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(full, fh, indent=1)
    cli = subprocess.run([sys.executable, str(CHECKER), str(cli_file)], cwd=str(WORKSPACE), capture_output=True,
                         text=True, encoding="utf-8", errors="replace", timeout=300)
    wired = [ln.strip() for ln in (cli.stdout or "").splitlines() if "VIOLATION: count-bar[F17-AC8]" in ln]
    print("CLI (the checker's own main) over shape (b) as a NEW instance file: rc=%d; %s"
          % (cli.returncode, _safe(wired[0], 120) if wired else "no count-bar VIOLATION line"))
    check("CLI: main() raises the count-bar VIOLATION for F17-AC8 on a NEW instance", bool(wired) and cli.returncode == 1)

    # ---- NEGATIVE ARMS: a genuine zero carried by a NEW instance is ADMITTED
    admitted, negatives = 0, []
    plain = dict(_row(F10_INST, "F10-AC10"))
    negatives.append(("plain zero: F10-AC10's COMMITTED evidence (no ANSI)", plain))
    try:
        ev_c = _bun_summary("allpass.test.ts", ALL_PASS, {"FORCE_COLOR": "1"})
        negatives.append(("ANSI zero: a REAL coloured bun summary of five passing scratch tests",
                          {"criterion_id": "F10-AC10", "status": "PASS", "expect": bar, "output_evidence": ev_c}))
    except Exception as exc:  # noqa: BLE001
        check("ANSI zero: a REAL coloured bun summary could be produced", False, str(exc))
    negatives.append(("F18-AC17: its COMMITTED pass-2 evidence", dict(_row(F18_INST, "F18-AC17"))))
    for label, row in negatives:
        row = dict(row, expect=row.get("expect") or bar)
        matched, existing = _grader_admits(row)
        v, fr = checker.count_bar_check(_new_instance(new_to, new_rel, row))
        mode_new = any("mode ENFORCE" in f for f in fr)
        ansi = "\x1b" in row["output_evidence"]
        ok = matched and not existing and mode_new and not v
        if label.startswith("plain"):
            ok = ok and not ansi
        if label.startswith("ANSI"):
            ok = ok and ansi
        admitted += ok
        print("%s" % label)
        print("    evidence: %s" % _safe(row["output_evidence"], 150))
        print("    bar matches: %s; ANSI present: %s; limb mode %s -> %s"
              % ("yes" if matched else "NO", "yes" if ansi else "no", "ENFORCE" if mode_new else "NOT ENFORCE",
                 "ADMITTED" if not v else "REFUSED -- " + _safe(v[0], 100)))
        check("NEGATIVE %s -> ADMITTED under ENFORCE" % label.split(":")[0], ok)
    print("GENUINE ZERO ADMITTED: %d of %d" % (admitted, len(negatives)))

    # ---- LEGACY: F17-AC8's committed instance, unmodified -> ANNOUNCED, never a violation
    legacy = json.loads(_git("show", "HEAD:" + F17_INST))
    lv, lfr = checker.count_bar_check(legacy)
    announced = [f for f in lfr if f.startswith("count-bar-announce") and "count-bar[F17-AC8]" in f]
    mode_legacy = any("mode ANNOUNCE" in f for f in lfr)
    inst_path = WORKSPACE / F17_INST
    cli_l = subprocess.run([sys.executable, str(CHECKER), str(inst_path)], cwd=str(WORKSPACE), capture_output=True,
                           text=True, encoding="utf-8", errors="replace", timeout=300)
    cli_announce = any("count-bar-announce" in ln and "F17-AC8" in ln for ln in (cli_l.stdout or "").splitlines())
    cli_valid = cli_l.returncode == 0 and "VALID (rc=0)" in (cli_l.stdout or "")
    print("legacy: F17-AC8's committed instance -> limb mode %s, raised=%d, announce lines naming F17-AC8=%d; the CLI "
          "over the committed file reads %s and prints the announce line: %s"
          % ("ANNOUNCE" if mode_legacy else "NOT ANNOUNCE", len(lv), len(announced),
             "VALID (rc=0)" if cli_valid else "rc=%d" % cli_l.returncode, "yes" if cli_announce else "NO"))
    leg_ok = check("LEGACY F17-AC8 -> ANNOUNCED, raises nothing, instance stays VALID",
                   mode_legacy and not lv and bool(announced) and cli_valid and cli_announce)
    if leg_ok:
        print("CONTRADICTING COUNT, LEGACY INSTANCE: ANNOUNCED, %d violations (F17-AC8, governing order cut before "
              "RULING M(ii) @%s; the would-refuse text is printed as an announce frame)" % (len(lv), checker.COUNT_BAR_RULING))
    else:
        print("CONTRADICTING COUNT, LEGACY INSTANCE: NOT AS SPECIFIED -- see the FAIL line below")

    failed = [r for r in results if not r[1]]
    print()
    for name, ok, detail in results:
        print("  %-4s %s%s" % ("PASS" if ok else "FAIL", name, ("   <- " + _safe(detail, 200)) if (detail and not ok) else ""))
    print("count-bar battery: %d of %d arm(s) as expected" % (len(results) - len(failed), len(results)))
    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(main())
