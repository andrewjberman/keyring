#!/usr/bin/env python3
"""INVOCATION ALIGNMENT LIMB -- the seeded battery + the real-corpus regression arm.

Subject: `.tools/proof-of-spec-check.py` `invocation_alignment_check()`, built 2026-09-12 by
`0.9.0_WK_IRPT_FNTEND~3` on `IRPT_FNTEND.TO-FE-s-23` (decomp cell FE-s-23, channel row
IRPT_FNTEND-S31).

THE CLASS IT CLOSES. The spine has the ISSUER substitute <WS>/<PORT> into the worker face at
spawn, so an issuer is ALWAYS editing the criterion string on the way out -- and nothing stopped
a SUBSTANTIVE correction going only there. Measured on IRPT_FNTEND round 2: an issuer corrected
two print-route URLs in the SPAWN PROMPT and never in the task-order FILE; the worker ran the
corrected URLs and recorded them faithfully; proof-of-spec-check returned VALID (rc=0) over 20
rows with 0 violations. The prompt is gone the moment the worker ends; the RECORD is what the
CVO grades and every successor reads.

    A LIMB THAT REFUSES EVERYTHING IS AS USELESS AS ONE THAT REFUSES NOTHING.

So both directions are proved here, and neither is proved by the other's fixtures:

  DIVERGENCE CAUGHT            4 seeded pairs -- a changed FLAG, a changed PATH, an added QUERY
                               PARAMETER, a changed QUOTED ARGUMENT -- each REFUSED, each naming
                               both strings and the criterion id.
  PLACEHOLDER EXPANSION        3 pairs differing ONLY by substitution (<WS> -> an absolute path,
  TOLERATED                    <PORT> -> a number, both at once) -- each ACCEPTED.
  ANTI-BRICK                   the SAME 3 tolerated pairs, with the placeholders NOT declared to
                               the limb, must all 3 diverge: the tolerance comes from the
                               DECLARATION, not from a limb that accepts whatever it is handed.
  ROUND-2 CORPUS STILL VALID   the 7 committed round-2 IRPT_FNTEND instances, through the
                               checker's OWN CLI on the real bytes, must still read VALID. A
                               fixture that cannot represent the real corpus cannot certify it.

BLOCKED: AND THE CORPUS ARM PRINTS ITS OWN DISCLOSURE. 2 of those 7 instances carry a row that DOES
diverge from its task order under the strict rule (FE-s-12 F12-AC5, FE-s-18 F18-AC17). They stay
VALID because no IRPT_FNTEND task order declares <placeholders>, so the limb ANNOUNCES on them --
and the census below prints both strings for both rows. The number "7 of 7" must never be read as
"7 of 7 are aligned"; it means "7 of 7 still validate". Filed as a surprise row, not normalised away.

Run: python .tools/tests/test_invocation_limb.py
Exit 0 = every arm as expected. Exit 1 = at least one arm did not.
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
PROJECT = WORKSPACE / "org" / "missions" / "D9" / "IRPT" / "IRPT_FNTEND"
ROUND2_CELLS = ["FE-s-12", "FE-s-13", "FE-s-14", "FE-s-15", "FE-s-16", "FE-s-17", "FE-s-18"]

PASS, FAIL = "PASS", "FAIL"
results: list[tuple[str, str, str]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    results.append((name, PASS if ok else FAIL, detail))


def _load_checker():
    """The module name carries hyphens, so a plain import cannot reach it."""
    spec = importlib.util.spec_from_file_location("pos_check_inv", CHECKER)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# --------------------------------------------------------------------------- fixtures
# Every seeded pair is shaped like a REAL round-2 invocation (a portal ui-smoke capture or a bun
# test), because a fixture that cannot represent the failure cannot score it.
SPEC_SMOKE = ('cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs "investor-reporting?firm=global" '
              '<WS>/org/x/fe-s-9_export_modal_390.png --port <PORT> --width 390 '
              '--fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-9.json --click "Analysis"')
WS_VAL = "/c/tmp/wk-irpt_fntend-2-5-fe-s-15"
PORT_VAL = "5181"


def _expand(spec: str, ws: str = WS_VAL, port: str = PORT_VAL) -> str:
    return spec.replace("<WS>", ws).replace("<PORT>", port)


# The four divergences, each applied to the faithfully-expanded record: what a worker would have
# recorded had the issuer corrected the PROMPT and not the FILE.
HONEST = _expand(SPEC_SMOKE)
SEEDED = [
    ("a changed FLAG (--width 390 -> --width 1440)",
     HONEST.replace("--width 390", "--width 1440")),
    ("a changed PATH (fe-s-9.json -> fe-s-16.json)",
     HONEST.replace("smoke/fe-s-9.json", "smoke/fe-s-16.json")),
    ("an ADDED QUERY PARAMETER (?firm=global -> ?firm=global&print=1) -- S31's own shape",
     HONEST.replace("?firm=global", "?firm=global&print=1")),
    ("a changed QUOTED ARGUMENT (--click \"Analysis\" -> --click \"Holdings\")",
     HONEST.replace('--click "Analysis"', '--click "Holdings"')),
]

TOLERATED = [
    ("<WS> -> an absolute path",
     "cd <WS>/portal && timeout 120 bun test src/pages/InvestorReporting",
     "cd %s/portal && timeout 120 bun test src/pages/InvestorReporting" % WS_VAL),
    ("<PORT> -> a number",
     "cd portal && node scripts/ui-smoke.mjs investor-reporting out.png --port <PORT> --width 390",
     "cd portal && node scripts/ui-smoke.mjs investor-reporting out.png --port %s --width 390" % PORT_VAL),
    ("<WS> and <PORT> at once, <WS> twice with one value",
     SPEC_SMOKE, HONEST),
]


def _to_text(spec: str, placeholders: str | None = "WS, PORT", cid: str = "F23-FIX1") -> str:
    """A minimal governing-TO text carrying ONE criterion. `placeholders=None` omits the
    declaration entirely, which is the ANNOUNCE branch."""
    decl = "" if placeholders is None else "<placeholders>%s</placeholders>\n" % placeholders
    return ("# FIXTURE TO\n<to_id>NFRA_TESTPROJ.TO-FIX-1</to_id>\n" + decl
            + '<criterion id="%s" cell_refs="FIX-a-1"><invocation>%s</invocation>'
              "<expect>x</expect></criterion>\n" % (cid, spec))


def _instance(recorded: str, cid: str = "F23-FIX1") -> dict:
    return {"to_id": "NFRA_TESTPROJ.TO-FIX-1",
            "acceptance": [{"criterion_id": cid, "invocation": recorded}]}


def _run(mod, spec: str, recorded: str, placeholders: str | None = "WS, PORT"):
    return mod.invocation_alignment_check(
        _instance(recorded), to_text=_to_text(spec, placeholders), to_label="<fixture>")


# --------------------------------------------------------------------------- arms
def arm_divergences(mod) -> int:
    caught = 0
    for label, recorded in SEEDED:
        v, _f = _run(mod, SPEC_SMOKE, recorded)
        # The bar is not "it refused": it must refuse ONCE, name the criterion id, and print
        # BOTH strings -- a refusal a reader cannot act on is half a gate.
        ok = (len(v) == 1 and "F23-FIX1" in v[0]
              and SPEC_SMOKE in v[0] and recorded in v[0])
        check("divergence REFUSED, naming the id and both strings: " + label, ok,
              ("violations=%d" % len(v)) + ("" if not v else " | first=" + v[0][:160]))
        caught += bool(ok)
    print("DIVERGENCE CAUGHT: %d of %d" % (caught, len(SEEDED)))
    return caught


def arm_tolerated(mod) -> int:
    tolerated = 0
    for label, spec, recorded in TOLERATED:
        v, f = _run(mod, spec, recorded)
        ok = len(v) == 0 and any("1/1 comparable row(s) match" in x for x in f)
        check("placeholder expansion ACCEPTED: " + label, ok,
              ("violations=%d" % len(v)) + ("" if not v else " | " + v[0][:160]))
        tolerated += bool(ok)
    print("PLACEHOLDER EXPANSION TOLERATED: %d of %d" % (tolerated, len(TOLERATED)))
    return tolerated


def arm_anti_brick(mod) -> int:
    """The tolerance must come from the DECLARATION. Declare an empty placeholder set and the
    very same three pairs must all diverge -- otherwise arm_tolerated is green for the wrong
    reason and this battery is a brick."""
    diverged = 0
    for label, spec, recorded in TOLERATED:
        v, _f = _run(mod, spec, recorded, placeholders="NONE")
        ok = len(v) == 1
        check("anti-brick: with NO placeholder declared the same pair DIVERGES: " + label, ok,
              "violations=%d" % len(v))
        diverged += bool(ok)
    print("ANTI-BRICK (tolerance is the DECLARATION, not the limb): %d of %d" % (diverged, len(TOLERATED)))
    return diverged


def _round2_pairs() -> list[tuple[str, Path, Path, list[str]]]:
    """(cell, task order, instance, expected criterion ids) for the seven round-2 cells."""
    tos = {}
    for f in (PROJECT / "task-orders").glob("*.md"):
        m = re.search(r"<to_id>(.*?)</to_id>", f.read_text(encoding="utf-8", errors="replace"))
        if m:
            tos[m.group(1).strip()] = f
    out = []
    for cell in ROUND2_CELLS:
        to = tos.get("IRPT_FNTEND.TO-" + cell)
        insts = sorted(PROJECT.glob("deliverables/*/IRPT_FNTEND.TO-%s.*.proof_of_spec.json" % cell))
        if to is None or len(insts) != 1:
            out.append((cell, to, None, []))
            continue
        m = re.search(r"<expected_criteria>(.*?)</expected_criteria>",
                      to.read_text(encoding="utf-8", errors="replace"), re.S)
        ids = [c.strip() for c in m.group(1).split(",") if c.strip()] if m else []
        out.append((cell, to, insts[0], ids))
    return out


def arm_round2_corpus(mod) -> int:
    """REAL BYTES, through the checker's OWN CLI -- a DIFFERENT instrument from the function calls
    every other arm uses, so a fault in the wiring cannot pass here by agreeing with itself."""
    still_valid = 0
    pairs = _round2_pairs()
    for cell, to, inst, ids in pairs:
        if inst is None:
            check("round-2 corpus: %s resolves to exactly one committed instance" % cell, False,
                  "task order or instance not found")
            continue
        cmd = [sys.executable, str(CHECKER), str(inst)] + ([",".join(ids)] if ids else [])
        p = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8",
                           errors="replace", cwd=str(WORKSPACE), timeout=180)
        # rc AND the verdict word, together: this tool returns rc=0 on a READ-ERROR too, so rc
        # alone is not an oracle here and never keys an arm in this file.
        ok = p.returncode == 0 and re.search(r"\bVALID \(rc=0\)", p.stdout) is not None
        tail = [ln for ln in p.stdout.splitlines() if "VIOLATION:" in ln or "VALID" in ln]
        check("round-2 corpus STILL VALID under the limb: %s" % cell, ok,
              "rc=%d | %s" % (p.returncode, " || ".join(tail[:3])[:200]))
        still_valid += bool(ok)
    print("ROUND-2 CORPUS STILL VALID: %d of %d" % (still_valid, len(pairs)))
    return still_valid


def arm_round2_census(mod) -> None:
    """BLOCKED: THE DISCLOSURE BESIDE THE GREEN. "STILL VALID" is a statement about the VERDICT, not
    about alignment. This prints every round-2 row that DOES diverge under the strict rule, with
    both strings -- so the arm above cannot be quoted as "the corpus is aligned"."""
    rows = 0
    insts = 0
    print("ROUND-2 STRICT DIVERGENCE CENSUS (announce-only: no IRPT_FNTEND task order declares "
          "<placeholders>, so none of these refuses anything today)")
    for cell, to, inst, _ids in _round2_pairs():
        if inst is None:
            continue
        v, f = mod.invocation_alignment_check(
            json.loads(inst.read_text(encoding="utf-8")),
            to_text=to.read_text(encoding="utf-8", errors="replace"),
            to_label=str(to.relative_to(WORKSPACE)).replace("\\", "/"))
        hits = [x for x in f if x.startswith("invocation-announce")] + v
        if hits:
            insts += 1
            rows += len(hits)
            for h in hits:
                print("  %s: %s" % (cell, h))
    print("ROUND-2 STRICT DIVERGENCE CENSUS: %d row(s) across %d of %d instance(s)"
          % (rows, insts, len(ROUND2_CELLS)))


def main() -> int:
    mod = _load_checker()
    arm_divergences(mod)
    arm_tolerated(mod)
    arm_anti_brick(mod)
    arm_round2_corpus(mod)
    arm_round2_census(mod)

    width = max(len(n) for n, _, _ in results)
    print("")
    for name, verdict, detail in results:
        line = "  %-4s %s" % (verdict, name.ljust(width))
        if verdict == FAIL and detail:
            line += "   <- " + detail[:220]
        print(line)
    failed = [r for r in results if r[1] == FAIL]
    print("\ninvocation-limb battery: %d/%d arms as expected" % (len(results) - len(failed), len(results)))
    if failed:
        print("BATTERY FAILED -- the limb does not behave as specified.")
        return 1
    print("BATTERY PASS -- four seeded divergences refused with both strings, three substitutions "
          "tolerated, the tolerance shown to come from the declaration, and the seven committed "
          "round-2 instances still VALID on their real bytes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
