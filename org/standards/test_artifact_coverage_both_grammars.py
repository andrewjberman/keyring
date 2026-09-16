"""Acceptance battery: proof-of-spec-check artifact-coverage tests COVERAGE, not NAMING.

COO's acceptance note, honoured literally: exercise BOTH id grammars, because a one-sided test
would let a fix that simply DISABLES the rule look correct. So this battery asserts in four
directions, and two of them must still FAIL:

  A  DS-grammar instance that passes today            -> MUST STILL PASS   (no regression)
  B  WP1-N-grammar instance that fails today          -> MUST FLIP to pass (the force-class fix)
  C  genuinely uncovered artifact                     -> MUST STILL FAIL   (rule not disabled)
  D  artifact "covered" only by an incidental mention
     of its stem inside an UNRELATED exclusion        -> MUST NOW FAIL     (the silent false pass)
  E  artifact_covered_by naming a REAL row            -> MUST PASS
  F  artifact_covered_by naming a row that is absent  -> MUST FAIL

D is the one this seat found on its OWN accepted deliverable: TO-1's broker.py passed because an
exclusion about the site-Z fabric leg contains the word "broker". A false FAIL is loud and gets
argued with; a false PASS is believed.

BROUGHT CURRENT 2026-09-14 (IRPT_FNTEND FE-s-44, 1.0.0_SA_CTO RULING AB, row W4-S15 / C-S90):
  * The instances are written INSIDE the tree whose checker grades them (under <tree>/.scratch/).
    Since 709b9556a3 the checker refuses an instance outside its own tree with
    artifact-resolution/CHECKER-SCOPE before any artifact row is read (proof-of-spec-check.py
    :322-342). That limb is right. This battery used to write to the OS temp dir, so from
    2026-09-10 every arm was refused by it: A, B and E read red, and C, D and F read green only
    because the blanket refusal also carried a coverage line.
  * A control passes only when EVERY violation the checker prints is its NAMED one: the uncovered
    artifact for C and D, the dangling citation for F. The header's violation count must also equal
    the number of named lines. A refusal for any other reason no longer counts as the control
    firing. Each control prints the violation line it matched.
  * The fixture's artifact row pins a REAL commit that carries the path, so the resolution limb
    resolves it rather than announcing it UNRESOLVED-HERE. The fixture's field set and vocabulary
    are checked against a real committed instance read as a committed blob (RULING AC). The
    fixture deliberately omits decomp_ref, and its to_id resolves no governing order. So every
    order-bound limb only ANNOUNCES, and the arms isolate the instance-intrinsic rules.
  * THE MUTANT, run every time: a scratch copy of the checker with its artifact-coverage loop
    disabled (<tree>/.scratch/, removed afterwards) must turn C, D and F red while A, B and E stay
    green. Otherwise the battery cannot fail on the case it exists for.

Usage: python org/standards/test_artifact_coverage_both_grammars.py
  (a SCRIPT: it exits at the end with rc 0 only when every line below holds; pytest collects zero)
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

WS = Path(subprocess.run(["git", "rev-parse", "--show-toplevel"],
                         cwd=str(Path(__file__).resolve().parent),
                         capture_output=True, text=True).stdout.strip())
CHECKER = WS / ".tools" / "proof-of-spec-check.py"
SCRATCH = WS / ".scratch"
RESULTS: list[tuple[str, str, str]] = []
RUN_TIMEOUT_S = 300

ART = "data/mdpf/scripts/gold/dim_mdpf_aum_metrics.py"

# The real committed instance the fixture's SHAPE is compared with, read as a committed blob. It is a
# BUILD-GENERAL / FABRIC / OTHER instance whose artifact rows include a data/*/scripts/gold script pinned
# to a real commit, with command-method PASS rows carrying `expect`.
REAL_PIN = "b9a3fcc335"
REAL_PATH = ("org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/"
             "IRPT_BCKEND.TO-IB-rt-7.the-holdings-handler-and-the-attribution-holdouts.proof_of_spec.json")

# The one line the mutant replaces: the per-artifact loop of the coverage rule in conditional_checks.
MUTATION_SITE = ('    for a in inst.get("artifacts_produced", []):\n'
                 '        # SCOPE IS BACKEND-DS-ID-GRAMMAR-SPECIFIC BY DESIGN')
MUTATION = ('    for a in []:  # MUTANT (test_artifact_coverage_both_grammars): coverage rule disabled\n'
            '        # SCOPE IS BACKEND-DS-ID-GRAMMAR-SPECIFIC BY DESIGN')

NAMED_UNCOVERED = f"artifact-coverage: '{ART}' has NO acceptance row referencing it"
NAMED_DANGLING = (f"artifact-coverage: '{ART}' artifact_covered_by names criterion id(s) ['WP9-9'] "
                  f"that do not exist in this instance")


def git(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=str(WS), capture_output=True, timeout=120)


def rec(tid, ok, detail):
    RESULTS.append((tid, "PASS" if ok else "FAIL", detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {tid}: {detail}")


def art_pin() -> str:
    """The commit that last touched ART, and it must carry ART. A real pin, never a made-up hash."""
    pin = git("log", "-1", "--format=%H", "--", ART).stdout.decode().strip()
    if not pin or git("cat-file", "-e", f"{pin}:{ART}").returncode != 0:
        print(f"ERROR: no commit in this tree carries {ART} -- the fixture has no real pin; cannot run (rc=2)")
        sys.exit(2)
    return pin


PIN = art_pin()


def base(criterion_ids, artifacts, exclusions=None, rows_extra=None):
    return {
        "schema_version": "1.0", "to_id": "FIXTURE.T", "phase": "BUILD-GENERAL", "firm": "FABRIC",
        "assignee": "0.8.0_AE_CloudComp",
        "spec_ref": {"doc": "docs/architecture/D0_INFRA_TIGHTENING_PRD.md", "group": "OTHER",
                     "vintage_commit": "4bf291b26c"},
        "session_log": "org/x/log.md",
        "artifacts_produced": artifacts,
        "acceptance": [
            {"criterion_id": c,
             "criterion_verbatim": "a criterion long enough to satisfy minLength",
             "method": "command",
             "invocation": (rows_extra or {}).get(c, "python -c 'pass'"),
             "expect": "OK: exercised",
             "output_evidence": "OK: exercised", "denominator": "1 of 1", "status": "PASS"}
            for c in criterion_ids],
        "controls": {
            "mutant": {"description": "a mutant description long enough", "expected": "x",
                       "observed": "y", "status": "FIRED-AS-EXPECTED"},
            "determinism": {"method": "two runs compared", "observed": "same", "status": "STABLE"}},
        "declared_exclusions": exclusions or [],
        "surprises": [],
        "compiler_tools": [{"tool": "t", "invocation": "i", "result": "r"}],
    }


def art(**extra):
    row = {"path_or_key": ART, "kind": "script", "commit_or_etag": PIN[:10],
           "deployed_state": "COMMITTED-NOT-DEPLOY-SCOPE", "deploy_evidence": "n/a"}
    row.update(extra)
    return row


# (id, wants, instance, named violation for a control, what the arm asserts)
ARMS = [
    ("A-DS-GRAMMAR-STILL-PASSES", "pass",
     base(["MDPF-A-AUMMETRICS-01"], [art()]), None,
     "DS-grammar id carrying the artifact stem (must be 0; no regression)"),
    ("B-WP1-GRAMMAR-FLIPS", "pass",
     base(["WP1-1"], [art()], rows_extra={"WP1-1": f"python {ART} --dry-run"}), None,
     "WP1-N id whose row INVOKES the artifact (must be 0; the force-class fix)"),
    ("C-UNCOVERED-STILL-FAILS", "fail",
     base(["WP1-1"], [art()]), NAMED_UNCOVERED,
     "artifact referenced NOWHERE (must FAIL on the coverage rule; proves the rule was not disabled)"),
    ("D-INCIDENTAL-EXCLUSION-NOW-FAILS", "fail",
     base(["WP1-1"], [art()], exclusions=[{"item": "the site-Z leg",
                                           "reason": "unreachable; note dim_mdpf_aum_metrics is unrelated here"}]),
     NAMED_UNCOVERED,
     "stem appears ONLY incidentally in an unrelated exclusion's REASON (must FAIL on the coverage rule)"),
    ("E-EXPLICIT-FIELD-PASSES", "pass",
     base(["WP1-1"], [art(artifact_covered_by=["WP1-1"])]), None,
     "artifact_covered_by naming a real row (must be 0)"),
    ("F-DANGLING-CITATION-FAILS", "fail",
     base(["WP1-1"], [art(artifact_covered_by=["WP9-9"])]), NAMED_DANGLING,
     "artifact_covered_by citing a NONEXISTENT row (must FAIL on the dangling citation)"),
]


def run(inst, checker: Path) -> tuple[int, str]:
    """Write the instance INSIDE the tree the checker grades, and run the checker on it."""
    SCRATCH.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(dir=str(SCRATCH), prefix="aco_inst_") as td:
        f = Path(td) / "i.json"
        f.write_text(json.dumps(inst, indent=1), encoding="utf-8")
        try:
            p = subprocess.run([sys.executable, str(checker), str(f)], cwd=str(WS), capture_output=True,
                               text=True, encoding="utf-8", errors="replace", timeout=RUN_TIMEOUT_S)
        except subprocess.TimeoutExpired:
            return 124, f"TIMEOUT after {RUN_TIMEOUT_S} s"
        return p.returncode, (p.stdout or "") + (p.stderr or "")


def violations(out: str) -> list[str]:
    return [ln.strip()[len("VIOLATION:"):].strip() for ln in out.splitlines()
            if ln.strip().startswith("VIOLATION:")]


def header_count(out: str) -> int | None:
    m = re.search(r"\| violations=(\d+)", out)
    return int(m.group(1)) if m else None


def judge(wants: str, named: str | None, rc: int, out: str) -> tuple[bool, str, list[str]]:
    """PASS arm: rc 0 and no violation at all. CONTROL arm: rc 1, and EVERY violation is the named one."""
    v = violations(out)
    hc = header_count(out)
    if wants == "pass":
        ok = rc == 0 and not v and hc == 0
        return ok, f"rc={rc}, violations={hc} (want rc=0, 0)", v
    named_lines = [x for x in v if x.startswith(named)]
    foreign = [x for x in v if not x.startswith(named)]
    ok = rc == 1 and bool(named_lines) and not foreign and hc == len(named_lines)
    return ok, (f"rc={rc}, violations={hc}: {len(named_lines)} named, {len(foreign)} other "
                f"(want rc=1, every violation the named one)"), v


def run_all(checker: Path) -> list[tuple[int, str]]:
    with ThreadPoolExecutor(max_workers=len(ARMS)) as pool:
        futs = [pool.submit(run, inst, checker) for _, _, inst, _, _ in ARMS]
        return [f.result() for f in futs]


def shape_check() -> tuple[bool, list[str]]:
    """The fixture carries no field and no vocabulary value that the real committed instance lacks."""
    b = git("show", f"{REAL_PIN}:{REAL_PATH}")
    if b.returncode != 0:
        return False, [f"FIXTURE SHAPE: the comparison instance does not resolve at {REAL_PIN} -- cannot compare"]
    real = json.loads(b.stdout.decode("utf-8", "replace"))
    fx = [inst for _, _, inst, _, _ in ARMS]
    real_arts = [a for a in real.get("artifacts_produced", []) if isinstance(a, dict)]
    real_rows = [r for r in real.get("acceptance", []) if isinstance(r, dict)]
    rk_top, rk_art = set(real), set().union(*(set(a) for a in real_arts))
    rk_row = set().union(*(set(r) for r in real_rows))
    fk_top = set().union(*(set(i) for i in fx))
    fk_art = set().union(*(set(a) for i in fx for a in i["artifacts_produced"]))
    fk_row = set().union(*(set(r) for i in fx for r in i["acceptance"]))
    vocab = {
        "phase": ({i["phase"] for i in fx}, {real.get("phase")}),
        "firm": ({i["firm"] for i in fx}, {real.get("firm")}),
        "spec_ref.group": ({i["spec_ref"]["group"] for i in fx}, {real.get("spec_ref", {}).get("group")}),
        "artifact kind": ({a["kind"] for i in fx for a in i["artifacts_produced"]}, {a.get("kind") for a in real_arts}),
        "deployed_state": ({a["deployed_state"] for i in fx for a in i["artifacts_produced"]},
                           {a.get("deployed_state") for a in real_arts}),
        "acceptance method": ({r["method"] for i in fx for r in i["acceptance"]}, {r.get("method") for r in real_rows}),
        "acceptance status": ({r["status"] for i in fx for r in i["acceptance"]}, {r.get("status") for r in real_rows}),
    }
    miss_top, miss_art, miss_row = fk_top - rk_top, fk_art - rk_art, fk_row - rk_row
    vocab_ok = [k for k, (f, r) in vocab.items() if f <= r]
    real_gold = [a for a in real_arts if a.get("kind") == "script"
                 and str(a.get("path_or_key", "")).startswith("data/") and "/scripts/gold/" in str(a.get("path_or_key"))]
    pin_ok = git("cat-file", "-e", f"{PIN}:{ART}").returncode == 0
    ok = not miss_top and not miss_art and not miss_row and len(vocab_ok) == len(vocab) and bool(real_gold) and pin_ok
    lines = [
        f"FIXTURE SHAPE vs {REAL_PATH} @{REAL_PIN} (committed blob):",
        f"  top-level keys: {len(fk_top - miss_top)} of {len(fk_top)} fixture keys carried by the real instance "
        f"(real carries {len(rk_top)}; not carried by the fixture: {sorted(rk_top - fk_top)} -- the fixture's to_id "
        f"resolves no governing order, deliberately){'; MISSING ' + str(sorted(miss_top)) if miss_top else ''}",
        f"  artifact-row keys: {len(fk_art - miss_art)} of {len(fk_art)} carried by the real rows"
        f"{'; MISSING ' + str(sorted(miss_art)) if miss_art else ''}",
        f"  acceptance-row keys: {len(fk_row - miss_row)} of {len(fk_row)} carried by the real rows"
        f"{'; MISSING ' + str(sorted(miss_row)) if miss_row else ''}",
        f"  vocabulary: {len(vocab_ok)} of {len(vocab)} fields carry only values the real instance carries "
        f"({', '.join(k + '=' + '/'.join(sorted(vocab[k][0])) for k in vocab)})",
        f"  the real instance's own data/*/scripts/gold script rows: {len(real_gold)} "
        f"({', '.join(str(a.get('path_or_key')) + ' @' + str(a.get('commit_or_etag')) for a in real_gold)})",
        f"  fixture pin: {PIN[:10]} carries {ART} (git cat-file -e): {'yes' if pin_ok else 'NO'}",
    ]
    return ok, lines


def build_mutant() -> tuple[Path | None, int]:
    """A copy of the checker being graded, with the coverage loop disabled. It lives ONE level under the tree
    (the checker derives its tree as its own parent.parent), so it grades the same tree."""
    src = CHECKER.read_bytes().decode("utf-8").replace("\r\n", "\n")
    n = src.count(MUTATION_SITE)
    if n != 1:
        return None, n
    SCRATCH.mkdir(exist_ok=True)
    fd, name = tempfile.mkstemp(dir=str(SCRATCH), prefix="aco_mutant_", suffix=".py")
    with os.fdopen(fd, "wb") as fh:
        fh.write(src.replace(MUTATION_SITE, MUTATION).encode("utf-8"))
    return Path(name), n


# ---------------------------------------------------------------------------------------------------------
head_blob = git("show", "HEAD:.tools/proof-of-spec-check.py").stdout.replace(b"\r\n", b"\n")
live_blob = CHECKER.read_bytes().replace(b"\r\n", b"\n")
print(f"checker under test: {CHECKER} (bytes equal HEAD's blob, EOL-normalised: "
      f"{'yes' if head_blob == live_blob else 'NO -- a working-tree change is being graded'})")
print(f"instances written under: {SCRATCH} (inside the tree the checker grades)")
print(f"fixture artifact: {ART} @ {PIN[:10]}")
print()

shape_ok, shape_lines = shape_check()
for ln in shape_lines:
    print(ln)
print(f"FIXTURE SHAPED LIKE A REAL COMMITTED INSTANCE: {'yes' if shape_ok else 'no'}")
print()

outs = run_all(CHECKER)
controls_named = 0
for (tid, wants, _inst, named, what), (rc, out) in zip(ARMS, outs):
    ok, detail, v = judge(wants, named, rc, out)
    rec(tid, ok, f"{what} -> {detail}")
    if wants == "fail":
        for x in v:
            tag = "named" if x.startswith(named) else "OTHER"
            print(f"      violation ({tag}): {x[:170]}")
        if ok:
            controls_named += 1
    elif v:
        for x in v:
            print(f"      violation: {x[:170]}")
    if "CHECKER-SCOPE" in out:
        print("      NOTE: CHECKER-SCOPE refused this instance -- it was written outside the checker's tree")
n = sum(1 for _, v, _ in RESULTS if v == "PASS")
n_controls = sum(1 for a in ARMS if a[1] == "fail")
print()
print(f"CONTROLS FAIL FOR THEIR NAMED VIOLATION: {controls_named} of {n_controls} "
      f"(C and D: the uncovered artifact; F: the dangling citation; any other violation disqualifies)")
print()

# --- THE MUTANT: the coverage rule disabled in a scratch copy must turn the controls red. ---
mutant, sites = build_mutant()
caught = False
if mutant is None:
    print(f"MUTANT: the mutation site occurs {sites} time(s) in the checker, not exactly once -- no mutant built")
else:
    try:
        m_outs = run_all(mutant)
        red_controls = green_positives = 0
        for (tid, wants, _inst, named, _what), (rc, out) in zip(ARMS, m_outs):
            ok, detail, _v = judge(wants, named, rc, out)
            print(f"  mutant  {tid}: {'still passes' if ok else 'goes RED'} ({detail})")
            if wants == "fail" and not ok:
                red_controls += 1
            if wants == "pass" and ok:
                green_positives += 1
        n_pos = len(ARMS) - n_controls
        caught = red_controls == n_controls and green_positives == n_pos
        print(f"  mutant: {red_controls} of {n_controls} controls go red; {green_positives} of {n_pos} positive "
              f"arms stay green (so the red is the disabled rule's, not a broken copy)")
    finally:
        mutant.unlink(missing_ok=True)
    print(f"  mutant copy {mutant.name} removed: {'yes' if not mutant.exists() else 'NO'}")
print(f"WITH THE COVERAGE RULE DISABLED IN A SCRATCH COPY, THE CONTROLS CATCH IT: {'yes' if caught else 'no'}")

print()
print("=" * 80)
print(f"ARTIFACT-COVERAGE BATTERY: {n}/{len(RESULTS)} PASS (denominator {len(RESULTS)})")
print("  C, D and F are the anti-disable controls -- they must FAIL the checker, on their named violation, to PASS here.")
print("=" * 80)
sys.exit(0 if (n == len(RESULTS) and controls_named == n_controls and caught and shape_ok) else 1)
