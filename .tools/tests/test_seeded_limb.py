#!/usr/bin/env python3
"""LIMB 3 -- the DRIVES (seeded-criterion) limb of `.tools/proof-of-spec-check.py` (drives_check).

Built 2026-09-13 by `0.9.0_WK_IRPT_FNTEND~4` on `IRPT_FNTEND.TO-FE-s-29` (decomp cell FE-s-29;
1.0.0_SA_CTO RULING Q and its condition @4f6c7abc7b; rows IRPT_FNTEND-S42 substrate half, IRPT_FNTEND-C-S67).

THE CLASS. This portal has no DOM test environment, so under renderToStaticMarkup a body that MOUNTED from
the network and a body SEEDED through `initialEnvelope` / `initialHoldingsEnvelope` / `initialReport` render
identically. Both kinds of criterion invoke `bun test <file>`; only the invoked TEST FILE tells them apart.

THE RULING'S OWN OUTCOME, stated so the cell cannot grade its own key: the limb REFUSES the seeded
criteria S42 names and PASSES the fe-s-19 browser-driven criteria. A limb that cannot tell those two
sets apart is not the limb. So the two sets below are graded by ONE call, the checker's drives_check():

  SEEDED (positive)   every criterion in the committed IRPT_FNTEND orders whose <invocation> runs one of
                      the six suites the cell measured as seeding (fe-s-5/{states,fields,controls},
                      fe-s-10/{tabs-mounted,parity}, fe-s-26/renders-differently). The population is found
                      by a plain substring census of the invocations -- a different instrument from the
                      limb -- and each criterion is evaluated AS IF declared drives="network", against its
                      REAL committed instance row.
  BROWSER (negative)  F19-AC4 and F19-AC5 (fe-s-19/mounted-from-wire.test.ts, which drives a real browser
                      under node), AS IF declared drives="network", against FE-s-19's committed instance.
  NEW, UNDECLARED     the first committed round-5 order (derived: cut after the ruling pin AND carrying a
                      drives="network" criterion) as issued -> admitted; the same bytes with ONE criterion's
                      drives= removed -> REFUSED; with EVERY drives= removed -> still REFUSED, because the
                      boundary is the order's add commit, never its declaration (an issuer cannot reach the
                      legacy side by omitting it).
  LEGACY              every round-4 instance (FE-s-25, 26, 27, 28 and FE-s-18), through the checker's OWN CLI,
                      ANNOUNCES with 0 violations from this limb and stays VALID.

WHERE THE TEST FILES ARE READ: the limb resolves them itself (the recorded cd, else this tree's portal,
else the main worktree's) and prints the directory and the checkout hash it read -- quoted per row below.
Every committed order and instance is read ONCE by `git show HEAD:` and cached.

Run: python .tools/tests/test_seeded_limb.py
Exit 0 = every arm as expected. Exit 1 otherwise.
"""
from __future__ import annotations

import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
WORKSPACE = TOOLS.parent
CHECKER = TOOLS / "proof-of-spec-check.py"
TO_DIR = "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/"
DELIV = "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/"
SEEDED_SUITES = ("fe-s-5/states", "fe-s-5/fields", "fe-s-5/controls",
                 "fe-s-10/tabs-mounted", "fe-s-10/parity", "fe-s-26/renders-differently")
BROWSER_IDS = ("F19-AC4", "F19-AC5")
ROUND4 = ("FE-s-25", "FE-s-26", "FE-s-27", "FE-s-28", "FE-s-18")


def _load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, str(path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


checker = _load(CHECKER, "pos_check_l3")
results: list = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    results.append((name, ok, detail))
    return ok


def _safe(s: str, n: int = 170) -> str:
    return (s or "").replace("\n", " | ").encode("ascii", "replace").decode("ascii")[:n]


def _git(*args: str) -> str:
    out = subprocess.run(["git", *args], cwd=str(WORKSPACE), capture_output=True, text=True,
                         encoding="utf-8", errors="replace", timeout=120)
    if out.returncode != 0:
        raise RuntimeError("git %s rc=%d" % (" ".join(args[:2]), out.returncode))
    return out.stdout


def _to_id(text: str) -> str:
    m = re.search(r"<to_id>([^<]+)</to_id>", text)
    return m.group(1).strip() if m else ""


ORDER_TEXT = {p: _git("show", "HEAD:" + p) for p in sorted(_git("ls-files", "--", TO_DIR).splitlines())
              if p.endswith(".md")}
ORDERS = sorted(ORDER_TEXT)
INST_BY_TO: dict = {}
for _rel in sorted(p for p in _git("ls-files", "--", DELIV).splitlines() if p.endswith(".proof_of_spec.json")):
    _j = json.loads(_git("show", "HEAD:" + _rel))
    INST_BY_TO.setdefault((str(_j.get("to_id", "")).split() or [""])[0], (_rel, _j))


def _with_drives(text: str, cid: str, value: str) -> str:
    """The order's bytes with drives="<value>" added to ONE criterion's opening tag, nothing else."""
    pat = re.compile(r'(<criterion\b(?:(?!/>)[^>])*?\bid="%s"(?:(?!/>)[^>])*?)(/?>)' % re.escape(cid))
    out, n = pat.subn(lambda m: m.group(1) + ' drives="%s"' % value + m.group(2), text, count=1)
    if n != 1:
        raise RuntimeError("criterion %s not found to declare" % cid)
    return out


def _as_if_network(order_rel: str, cid: str):
    """(violations naming cid, frames naming cid) -- cid evaluated AS IF declared drives="network"."""
    text = ORDER_TEXT[order_rel]
    irel, inst = INST_BY_TO.get(_to_id(text), (None, None))
    if inst is None:
        return None, ["no committed instance for %s" % _to_id(text)]
    row = next((r for r in inst.get("acceptance", []) if r.get("criterion_id") == cid), None)
    if row is None or row.get("status") != "PASS":
        return None, ["the committed row for %s is %s, not PASS" % (cid, row and row.get("status"))]
    v, fr = checker.drives_check(inst, to_text=_with_drives(text, cid, "network"), to_label=order_rel,
                                 to_rel=order_rel, enforce=True)
    key = "drives[%s]" % cid
    return [x for x in v if x.startswith(key)], [f for f in fr if f.startswith(key)]


def main() -> int:
    try:
        sys.stdout.reconfigure(line_buffering=True)
    except Exception:  # noqa: BLE001
        pass
    # ---- the boundary pin carries the CTO's condition, and is the commit that introduced it
    doc = checker.RULING_DOC
    pin = checker.DRIVES_RULING["IRPT_FNTEND"]
    needle = "declaration is MANDATORY, never opt-in"
    check("boundary: the ruling pin %s carries the CTO's condition and its parent does not (the pin INTRODUCED it)" % pin,
          needle in _git("show", "%s:%s" % (pin, doc)) and needle not in _git("show", "%s~1:%s" % (pin, doc)))

    # ---- POSITIVE: the seeded population, by a substring census of the invocations
    population = []
    for rel in ORDERS:
        for cid, inv in checker._to_invocations(ORDER_TEXT[rel]).items():
            if inv and any("__tests__/%s.test" % s in inv for s in SEEDED_SUITES):
                population.append((rel, cid, next(s for s in SEEDED_SUITES if "__tests__/%s.test" % s in inv)))
    print("SEEDED POPULATION (substring census of %d committed IRPT_FNTEND orders for the six suites): %d criteria"
          % (len(ORDERS), len(population)))
    n_ref = 0
    for rel, cid, suite in population:
        viol, fr = _as_if_network(rel, cid)
        seeded = [x for x in (viol or []) if "SEEDED" in x]
        ok = bool(seeded)
        n_ref += ok
        detail = seeded[0].split("SEEDED -- the invoked test passes ", 1)[-1] if seeded else (fr[0] if fr else "")
        print("  %-4s %-9s %-28s %s" % ("PASS" if ok else "FAIL", cid, suite, _safe(detail, 230)))
        check("SEEDED %s (%s) evaluated as drives=network -> REFUSED as SEEDED" % (cid, suite), ok, detail)
    suites_seen = sorted({s for _r, _c, s in population})
    check("the population covers all six measured suites", suites_seen == sorted(SEEDED_SUITES), str(suites_seen))
    print("SEEDED CRITERIA REFUSED: %d of %d (%s)" % (n_ref, len(population), ", ".join(c for _r, c, _s in population)))

    # ---- NEGATIVE: the fe-s-19 browser criteria, same call
    f19 = next(p for p in ORDERS if "TO-FE-s-19." in p)
    n_adm = 0
    for cid in BROWSER_IDS:
        viol, fr = _as_if_network(f19, cid)
        clean = viol == [] and any("seeding props named in code: none" in f and "read " in f for f in fr)
        n_adm += clean
        print("  %-4s %-9s %s" % ("PASS" if clean else "FAIL", cid, _safe(fr[0] if fr else (viol or ["?"])[0], 240)))
        check("BROWSER %s evaluated as drives=network -> read, and ADMITTED" % cid, clean)
    print("BROWSER CRITERIA ADMITTED: %d of %d (%s; the same drives_check call that refused the seeded set)"
          % (n_adm, len(BROWSER_IDS), ", ".join(BROWSER_IDS)))

    # ---- UNSCOPED READ (information, not an arm): every single-FILE bun-test criterion, as if network
    n_bun = n_file = 0
    extra, unread = [], []
    for rel in ORDERS:
        for cid, inv in checker._to_invocations(ORDER_TEXT[rel]).items():
            call = checker._bun_test_call(inv) if inv else None
            if call is None:
                continue
            n_bun += 1
            if not call[1] or not all(re.search(r"\.test\.[cm]?[jt]sx?$", t) for t in call[1]):
                continue                       # directory / filter / no-target runs: counted, not read here
            n_file += 1
            if any("__tests__/%s.test" % s in inv for s in SEEDED_SUITES):
                continue
            viol, fr = _as_if_network(rel, cid)
            if viol is None:
                continue
            if any("SEEDED" in x for x in viol):
                extra.append(cid)
            elif any("CANNOT BE READ" in x for x in viol):
                unread.append(cid)
    print("UNSCOPED (information, not an arm): %d bun-test criteria in the committed IRPT_FNTEND orders, %d naming "
          "test FILES; beyond the six-suite population, %d more would be refused as SEEDED if declared network (%s); "
          "%d unreadable here (%s)" % (n_bun, n_file, len(extra), ", ".join(extra) or "none", len(unread),
                                       ", ".join(unread) or "none"))

    # ---- NEW: a real round-5 order, as issued / one drives= removed / every drives= removed
    news = [rel for rel in ORDERS if checker._cut_after(rel, pin)[0] is True]
    print("NEW orders (added in a commit descending from @%s, derived per order): %d -- %s"
          % (pin, len(news), ", ".join(r.rsplit("/", 1)[-1].split(".")[1] for r in news)))
    target = next(rel for rel in news if 'drives="network"' in ORDER_TEXT[rel])
    t_text = ORDER_TEXT[target]
    crit = checker._criteria_attrs(t_text)
    inst = {"to_id": _to_id(t_text), "decomp_ref": {"to_ref": target},
            "acceptance": [{"criterion_id": c, "status": "UNVERIFIABLE-BY-INSTRUMENT",
                            "status_reason": "battery: the seeding half is graded by the SEEDED/BROWSER arms"}
                           for c in crit]}
    v0, f0 = checker.drives_check(inst, to_text=t_text, to_label=target, to_rel=target)
    first = next(iter(crit))
    one = re.sub(r'(<criterion\b[^>]*?\bid="%s"[^>]*?)\s+drives="[^"]*"' % re.escape(first), r"\1", t_text, count=1)
    v1, f1 = checker.drives_check(inst, to_text=one, to_label=target, to_rel=target)
    every = re.sub(r'(<criterion\b[^>]*?)\s+drives="[^"]*"', r"\1", t_text)
    v2, f2 = checker.drives_check(inst, to_text=every, to_label=target, to_rel=target)
    name = target.rsplit("/", 1)[-1]
    print("new order %s as issued: %s" % (name, _safe(f0[0], 240)))
    ok0 = check("NEW order as issued (every criterion declares) -> ADMITTED under a DERIVED ENFORCE",
                v0 == [] and "mode ENFORCE" in f0[0])
    ok1 = check("NEW order with ONE criterion's drives= removed (%s) -> REFUSED naming it" % first,
                len(v1) == 1 and "NEITHER" in v1[0] and first in v1[0] and "mode ENFORCE" in f1[0])
    ok2 = check("NEW order with EVERY drives= removed -> still ENFORCE, REFUSED naming all %d" % len(crit),
                len(v2) == 1 and ("%d of %d" % (len(crit), len(crit))) in v2[0] and "mode ENFORCE" in f2[0])
    print("  one removed   -> %s" % _safe(v1[0] if v1 else "ADMITTED", 200))
    print("  every removed -> %s" % _safe(v2[0] if v2 else "ADMITTED", 200))
    if ok0 and ok1 and ok2:
        print("NEW INSTANCE, CRITERION DECLARING NEITHER: REFUSED (%s, criterion %s; the boundary is the order's add "
              "commit, so omitting every declaration is refused too)" % (name, first))
    else:
        print("NEW INSTANCE, CRITERION DECLARING NEITHER: NOT AS SPECIFIED -- see the FAIL lines below")

    # ---- LEGACY: the round-4 instances through the checker's OWN CLI
    n_leg = 0
    for stem in ROUND4:
        orel = next(p for p in ORDERS if "TO-%s." % stem in p)
        irel, _inst = INST_BY_TO[_to_id(ORDER_TEXT[orel])]
        cli = subprocess.run([sys.executable, str(CHECKER), str(WORKSPACE / irel)], cwd=str(WORKSPACE),
                             capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=300)
        out = cli.stdout or ""
        frame = next((ln.strip() for ln in out.splitlines() if ln.strip().startswith("drives-frame:")), "")
        dv = [ln for ln in out.splitlines() if "VIOLATION: drives" in ln]
        ok = "mode ANNOUNCE" in frame and not dv and cli.returncode == 0
        n_leg += ok
        print("  %-4s %s -> rc=%d, drives violations=%d; %s" % ("PASS" if ok else "FAIL", irel.rsplit("/", 1)[-1],
                                                                 cli.returncode, len(dv), _safe(frame, 200)))
        check("LEGACY %s -> ANNOUNCE, no drives violation, instance VALID" % stem, ok)
    print("LEGACY ROUND-4 INSTANCES: %d of %d ANNOUNCED with 0 violations from this limb (%s)"
          % (n_leg, len(ROUND4), ", ".join(ROUND4)))

    failed = [r for r in results if not r[1]]
    print()
    for nm, ok, detail in results:
        print("  %-4s %s%s" % ("PASS" if ok else "FAIL", nm, ("   <- " + _safe(detail, 200)) if (detail and not ok) else ""))
    print("seeded-limb battery: %d of %d arm(s) as expected" % (len(results) - len(failed), len(results)))
    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(main())
