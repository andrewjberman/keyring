#!/usr/bin/env python3
"""LIMB 1 -- the LINE-ANCHORED <placeholders> reader, in BOTH readers, in ONE change.

Subject: PLACEHOLDERS_TAG_RE in `.tools/to-pipeline-gate.py` (read by _placeholder_declaration_violations)
and in `.tools/proof-of-spec-check.py` (read by _declared_placeholders). Built 2026-09-13 by
`0.9.0_WK_IRPT_FNTEND~4` on `IRPT_FNTEND.TO-FE-s-29` (decomp cell FE-s-29; 1.0.0_SA_CTO RULING M(i)
@23af9479ab; rows IRPT_FNTEND-S53, IRPT_FNTEND-W4-S7).

S53's FIVE CASES, EVERY ONE BUILT FROM REAL BYTES (`git show HEAD:<order>`), through BOTH readers:
  A  FE-s-28 as issued                                                          admitted
  E  FE-s-23 as issued (the order that invented the element)                    admitted
  B  FE-s-27 as issued (no element)                                             refused
  C  FE-s-28 + a REAL criterion carrying <PORT>, spliced among its criteria -- BETWEEN its prose mention
     of the tag and its element, the layout S53 measured failing -- the element still declaring WS only
                                                                                refused
  D  FE-s-27 + a prose paragraph quoting the GATE'S OWN EMITTED refusal text for FE-s-27 (which quotes
     the element mid-sentence), still no element                                refused
The <PORT> criterion is not chosen here: it is the FIRST criterion in the committed IRPT_FNTEND corpus
(sorted) whose REAL committed row matches it exactly under full expansion of <WS> and <PORT>, found by the
checker's own _to_invocations / _invocation_pattern -- so the only thing that can make C's row diverge
is the reader failing to expand <PORT>.

WHAT ADMITTED / REFUSED MEANS FOR EACH READER
  GATE     _placeholder_declaration_violations(rel, text) == [] is ADMITTED; anything else is REFUSED.
  CHECKER  A, E: _declared_placeholders returns EXACTLY the names on the element's own line (read here
                 by plain string operations, a different instrument from the regex under test).
           B, D: it returns None -- no declaration is read, so prose arms nothing.
           C:    it returns the element's names WITHOUT PORT, and invocation_alignment_check REFUSES the
                 spliced criterion's real committed row (its real port value stays literal under ENFORCE).

DISCRIMINATION, IN THE SAME RUN: the five cases are first run with the OLD unanchored pattern swapped into
BOTH modules, and the gate must ADMIT C and D there (S53's measurement, reproduced). A case counts toward
the bar line only if the OLD reader gave its S53 verdict AND the new reader gives the ruled one -- so the
count cannot be satisfied by a case that never could have failed.

Run: python .tools/tests/test_placeholders_reader.py
Exit 0 = all five cases behave, the control reproduces S53, and the readers are byte-identical. Exit 1 otherwise.
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
TO_DIR = "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/"
DELIV_DIR = "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/"
OLD_PATTERN = r"<placeholders>(.*?)</placeholders>"
NEW_PATTERN = r"^[ \t]*<placeholders>(.*?)</placeholders>[ \t]*$"


def _load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, str(path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


gate = _load(TOOLS / "to-pipeline-gate.py", "to_pipeline_gate_l1")
checker = _load(TOOLS / "proof-of-spec-check.py", "pos_check_l1")


def _git(*args: str) -> str:
    out = subprocess.run(["git", *args], cwd=str(WORKSPACE), capture_output=True, text=True,
                         encoding="utf-8", errors="replace", timeout=120)
    if out.returncode != 0:
        raise RuntimeError("git %s failed rc=%d: %s" % (" ".join(args), out.returncode, out.stderr.strip()[:200]))
    return out.stdout


def _show(rel: str) -> str:
    return _git("show", "HEAD:" + rel)


def _tracked(prefix: str) -> list:
    return sorted(p for p in _git("ls-files", "--", prefix).splitlines() if p.strip())


def _order(stem: str) -> str:
    hits = [p for p in _tracked(TO_DIR) if p.rsplit("/", 1)[-1].startswith("IRPT_FNTEND.TO-%s." % stem)]
    if len(hits) != 1:
        raise RuntimeError("order %s: %d tracked matches" % (stem, len(hits)))
    return hits[0]


def _element_line_names(text: str):
    """The names on the element's OWN line, by string operations -- not the regex under test."""
    lines = [ln.strip() for ln in text.splitlines()
             if ln.strip().startswith("<placeholders>") and ln.strip().endswith("</placeholders>")]
    if not lines:
        return None
    body = lines[0][len("<placeholders>"):-len("</placeholders>")]
    names = {w.upper() for w in re.findall(r"[A-Za-z][A-Za-z0-9_]*", body)}
    names.discard("NONE")
    return names


def _instances_for(to_id: str) -> list:
    out = []
    for rel in _tracked(DELIV_DIR):
        if rel.endswith(".proof_of_spec.json"):
            try:
                j = json.loads(_show(rel))
            except Exception:  # noqa: BLE001
                continue
            if str(j.get("to_id", "")).split()[0:1] == [to_id]:
                out.append((rel, j))
    return out


def _port_specimen():
    """(order rel, criterion id, criterion element text, committed row) -- the first REAL <PORT> criterion
    whose committed row matches it exactly under full expansion {WS, PORT}."""
    for rel in _tracked(TO_DIR):
        text = _show(rel)
        invs = checker._to_invocations(text)
        ports = [c for c, i in invs.items() if i and "<PORT>" in i]
        if not ports:
            continue
        m = re.search(r"<to_id>([^<]+)</to_id>", text)
        if not m:
            continue
        for _irel, inst in _instances_for(m.group(1).strip()):
            rows = {r.get("criterion_id"): r for r in inst.get("acceptance", []) if isinstance(r, dict)}
            for cid in ports:
                row = rows.get(cid)
                rec = str((row or {}).get("invocation", "") or "").strip()
                if not rec:
                    continue
                if re.fullmatch(checker._invocation_pattern(invs[cid], {"WS", "PORT"}), rec, re.S):
                    for b in checker.CRITERION_BLOCK_RE.finditer(text):
                        if dict(checker.ATTR_RE.findall(b.group(1))).get("id", "").strip() == cid:
                            return rel, cid, b.group(0), row
    return None


def _build_cases():
    o28, o23, o27 = _order("FE-s-28"), _order("FE-s-23"), _order("FE-s-27")
    t28, t23, t27 = _show(o28), _show(o23), _show(o27)
    spec = _port_specimen()
    if spec is None:
        raise RuntimeError("no REAL <PORT> criterion with a faithfully recorded row exists -- case C cannot be built")
    s_rel, s_cid, s_block, s_row = spec
    # C: splice the real criterion AFTER the last criterion line that precedes FE-s-28's element line.
    lines = t28.split("\n")
    el = next(i for i, ln in enumerate(lines) if ln.strip().startswith("<placeholders>") and ln.strip().endswith("</placeholders>"))
    last_crit = max(i for i, ln in enumerate(lines[:el]) if "</criterion>" in ln or "<criterion " in ln)
    prose = next(i for i, ln in enumerate(lines) if "<placeholders>" in ln)
    t_c = "\n".join(lines[:last_crit + 1] + [s_block] + lines[last_crit + 1:])
    layout = (prose < last_crit + 1 < el + 1)
    # D: the gate's OWN emitted refusal for FE-s-27, quoted as a prose paragraph under the worker-face heading.
    refusal = gate._placeholder_declaration_violations(o27, t27)
    if not refusal:
        raise RuntimeError("the gate did not refuse FE-s-27 -- case D has no emitted text to quote")
    quoted = refusal[0]
    anchor = t27.find("## WORKER FACE")
    cut = t27.find("\n", anchor) + 1 if anchor != -1 else t27.find("<criterion")
    t_d = t27[:cut] + "\n" + quoted + "\n\n" + t27[cut:]
    return {
        "A": dict(label="FE-s-28 as issued", rel=o28, text=t28, want="admitted", old="admitted"),
        "E": dict(label="FE-s-23 as issued", rel=o23, text=t23, want="admitted", old="admitted"),
        "B": dict(label="FE-s-27 as issued (no element)", rel=o27, text=t27, want="refused", old="refused"),
        "C": dict(label="FE-s-28 + real %s (%s) spliced below its prose mention, above its element" % (
            s_cid, s_rel.rsplit("/", 1)[-1][:40]), rel=o28, text=t_c, want="refused", old="admitted",
            row=s_row, cid=s_cid, layout=layout, prose_line=prose + 1, element_line=el + 2),
        "D": dict(label="FE-s-27 + the gate's own emitted refusal text quoted as prose", rel=o27, text=t_d,
                  want="refused", old="admitted", quoted=quoted),
    }


def _gate_verdict(case) -> tuple:
    got = gate._placeholder_declaration_violations(case["rel"], case["text"])
    return ("admitted" if got == [] else "refused"), got


def _checker_verdict(key: str, case) -> tuple:
    """(verdict, detail) for the checker's reader, per the table in the module docstring."""
    names = checker._declared_placeholders(case["text"])
    if key in ("A", "E"):
        want = _element_line_names(case["text"])
        ok = names is not None and names == want
        return ("admitted" if ok else "refused"), "reads %s; the element's own line declares %s" % (
            sorted(names) if names is not None and len(names) < 12 else ("%d names" % len(names) if names else None),
            sorted(want) if want is not None else None)
    if key in ("B", "D"):
        return ("refused" if names is None else "admitted"), "reads %s" % (
            "None (no declaration)" if names is None else "%d names from prose" % len(names))
    inst = {"to_id": "IRPT_FNTEND.TO-FE-s-28",
            "acceptance": [{"criterion_id": case["cid"], "invocation": case["row"].get("invocation", "")}]}
    viol, _fr = checker.invocation_alignment_check(inst, to_text=case["text"], to_label="case C")
    port_read = names is not None and "PORT" in names
    verdict = "refused" if (viol and not port_read) else "admitted"
    return verdict, "reads %s; PORT read: %s; the real committed %s row -> %d alignment violation(s)" % (
        sorted(names) if names is not None and len(names) < 12 else ("%d names" % len(names) if names else None),
        "yes" if port_read else "no", case["cid"], len(viol))


def _run(cases, pattern: str, flags: int) -> dict:
    saved = (gate.PLACEHOLDERS_TAG_RE, checker.PLACEHOLDERS_TAG_RE)
    gate.PLACEHOLDERS_TAG_RE = checker.PLACEHOLDERS_TAG_RE = re.compile(pattern, flags)
    try:
        out = {}
        for k, c in cases.items():
            gv, gdetail = _gate_verdict(c)
            cv, cdetail = _checker_verdict(k, c)
            out[k] = (gv, cv, gdetail, cdetail)
        return out
    finally:
        gate.PLACEHOLDERS_TAG_RE, checker.PLACEHOLDERS_TAG_RE = saved


def main() -> int:
    ok_all = True
    try:
        cases = _build_cases()
    except Exception as exc:  # noqa: BLE001
        print("FAIL: could not build the five cases from real bytes -- %s" % exc)
        print("LINE-ANCHORED READER, BOTH READERS: 0 of 5 cases (not built)")
        return 1
    c = cases["C"]
    print("case C layout: prose mention of the tag at line %d, spliced real criterion %s after it, element at line %d "
          "-> %s" % (c["prose_line"], c["cid"], c["element_line"], "the S53 layout" if c["layout"] else "NOT the S53 layout"))
    print("case D quotes the gate's own emitted text, %d chars, opening: %r" % (len(cases["D"]["quoted"]),
                                                                              cases["D"]["quoted"][:90]))
    old = _run(cases, OLD_PATTERN, re.S)
    new = {k: (_gate_verdict(v)[0], _checker_verdict(k, v)[0], _gate_verdict(v)[1], _checker_verdict(k, v)[1])
           for k, v in cases.items()}
    print()
    print("OLD UNANCHORED READER (control, swapped into BOTH modules for this run only):")
    for k in "AEBCD":
        gv, cv, _gd, cd = old[k]
        print("  %s  gate %-8s (S53: %-8s)  checker: %s" % (k, gv.upper(), cases[k]["old"], cd))
    control = all(old[k][0] == cases[k]["old"] for k in "AEBCD") and c["layout"]
    print("  control: %s" % ("REPRODUCES S53 -- the gate admits C and D under the old reader, so the cases can fail"
                             if control else "DOES NOT reproduce S53 -- the cases cannot discriminate"))
    ok_all &= control
    print()
    print("LINE-ANCHORED READER (as shipped in both modules):")
    n_ok = 0
    for k in "AEBCD":
        gv, cv, gd, cd = new[k]
        want = cases[k]["want"]
        case_ok = gv == want and cv == want and old[k][0] == cases[k]["old"]
        n_ok += case_ok
        detail = ""
        if gv == "refused" and gd:
            detail = " | gate text: %s" % gd[0].split(": ", 1)[-1][:110]
        print("  %s  %-4s %s -- gate %s, checker %s (want %s): %s%s" % (
            k, "PASS" if case_ok else "FAIL", cases[k]["label"], gv.upper(), cv.upper(), want, cd, detail))
    ok_all &= n_ok == 5
    if new["C"][0] == "refused":
        c_text = new["C"][2][0] if new["C"][2] else ""
        names_port = "<PORT>" in c_text
        print("  C's gate refusal names <PORT>: %s" % ("yes" if names_port else "NO"))
        ok_all &= names_port
    print()
    print("LINE-ANCHORED READER, BOTH READERS: %d of 5 cases behave as S53 measured and the ruling requires "
          "(A, E admitted; B, C, D refused -- each case counted only where the old reader gave S53's verdict)" % n_ok)
    same = (gate.PLACEHOLDERS_TAG_RE.pattern == checker.PLACEHOLDERS_TAG_RE.pattern
            and gate.PLACEHOLDERS_TAG_RE.flags == checker.PLACEHOLDERS_TAG_RE.flags
            and gate.PLACEHOLDER_TOKEN_RE.pattern == checker.PLACEHOLDER_TOKEN_RE.pattern)
    anchored = gate.PLACEHOLDERS_TAG_RE.pattern == NEW_PATTERN and bool(gate.PLACEHOLDERS_TAG_RE.flags & re.M)
    print("READERS BYTE-IDENTICAL: %s (gate %r flags=%d; checker %r flags=%d; token readers %s; the shared pattern "
          "%s the line-anchored one)" % (
              "yes" if same else "no", gate.PLACEHOLDERS_TAG_RE.pattern, gate.PLACEHOLDERS_TAG_RE.flags,
              checker.PLACEHOLDERS_TAG_RE.pattern, checker.PLACEHOLDERS_TAG_RE.flags,
              "equal" if gate.PLACEHOLDER_TOKEN_RE.pattern == checker.PLACEHOLDER_TOKEN_RE.pattern else "DIFFER",
              "IS" if anchored else "is NOT"))
    ok_all &= same and anchored
    print("placeholders-reader battery: %s" % ("PASS" if ok_all else "FAILED"))
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
