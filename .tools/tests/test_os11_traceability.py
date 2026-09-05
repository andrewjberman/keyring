#!/usr/bin/env python3
"""test_os11_traceability.py -- NFRA_OUTSET TO-OS-s-11 / criterion O11-AC1.

THE QUESTION: does every deterministic report line name the tool and vintage that produced it,
and does re-running that recipe REPRODUCE the row?

Run at both required grains:
  python .tools/tests/test_os11_traceability.py
  python -m pytest -q .tools/tests/test_os11_traceability.py

ARMS
  A  every deterministic stratum (A, B, C, D) carries a recipe with a tool, a NON-EMPTY concrete
     invocation, a vintage and a claim inside the declared domain -- on BOTH exits where a
     stratum has two (seam vs host, computed vs failed).
  B  RED MUTANT, the one the criterion names: the recipe dropped AT THE DEFINITION of _stratum,
     so every stratum emits an UNTRACEABLE row at once. Mutating at the definition rather than a
     use site is deliberate: a use-site mutant is only as wide as that site, and this worker
     already shipped one that left a second live carrier (NFRA_OUTSET-W2-S17).
  C  an ABSENT recipe renders LOUDLY -- 'NO RECIPE' and 'UNVERIFIABLE BY THE READER' -- because a
     row nobody can re-derive and a row with a recipe must never read the same. A second mutant
     makes the absent case render silently and must break the arm.
  D  the claim vocabulary is CLOSED: a value outside the declared domain is refused, not defaulted.
  E  THE REPRODUCTION, and it is the point of the whole cell: take stratum C's own printed recipe,
     run its two git commands here, re-derive the rows with an INDEPENDENT implementation of the
     documented fold, and compare to what the runner produced. Same rows or the arm fails.

NO AWS, NO NETWORK. Arm E runs `git` directly under a bound; nothing else leaves the process.
"""
from __future__ import annotations

import datetime as _dt
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUNNER = ROOT / "infra" / "aws" / "ec2" / "estate-report-runner" / "estate_report_runner.py"

RUNNER_ENV = {
    "ESTATE_REPORT_BUCKET": "os11-battery-not-a-real-bucket",
    "ESTATE_GITHUB_SECRET_ID": "x", "ESTATE_KIMI_SECRET_ID": "x",
    "ESTATE_KIMI_URL": "http://127.0.0.1:1", "ESTATE_KIMI_MODEL": "x",
    "ESTATE_REPO_URL": "http://127.0.0.1:1/x.git",
}

# RED MUTANT 1 -- the recipe dropped at the DEFINITION, so every stratum loses it at once.
TRACE_ANCHOR = '        "reproduce": reproduce,\n'
TRACE_MUTANT = '        "reproduce": None,   # RED MUTANT: every row becomes untraceable\n'

# RED MUTANT 2 -- an absent recipe renders as blank instead of loudly.
QUIET_ANCHOR = ('        return ("reproduce: *** NO RECIPE -- these rows name no tool and no '
                'invocation, so\\n"')
QUIET_MUTANT = '        return ""   # RED MUTANT: absence renders silently\n        _dead = ('

RESULTS: list[tuple[str, bool, str]] = []


def _record(name: str, ok: bool, detail) -> None:
    RESULTS.append((name, bool(ok), str(detail).replace("\n", " ")[:300]))


def _load(path, name, branch=None):
    keep = {}
    for k, v in RUNNER_ENV.items():
        keep[k] = os.environ.get(k)
        os.environ[k] = v
    keep["ESTATE_OUTSET_SEAM_PREFIX"] = os.environ.pop("ESTATE_OUTSET_SEAM_PREFIX", None)
    keep["ESTATE_REPO_BRANCH"] = os.environ.get("ESTATE_REPO_BRANCH")
    if branch:
        os.environ["ESTATE_REPO_BRANCH"] = branch
    try:
        spec = importlib.util.spec_from_file_location(name, str(path))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod
    finally:
        for k, v in keep.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v


NOW = _dt.datetime(2026, 9, 5, 12, 0, 0, tzinfo=_dt.timezone.utc)
EMPTY_MAPS = {"lambda_prefixes": [], "ec2_prefixes": [], "producer_paths": [], "prod_to_thread": {}}


def _branch() -> str:
    return subprocess.run(["git", "-C", str(ROOT), "rev-parse", "--abbrev-ref", "HEAD"],
                          capture_output=True, text=True, timeout=60).stdout.strip()


def _pin() -> str:
    return subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"],
                          capture_output=True, text=True, timeout=60).stdout.strip()


def _seam_artifact(tmp: Path, tool="comp-heat drift", argv=None):
    d = tmp / "seam"
    d.mkdir(parents=True, exist_ok=True)
    doc = {
        "schema_version": 1, "seam": "NFRA_OUTSET/OS-s-10", "tool": tool,
        "question": "q", "argv": argv if argv is not None else ["python", ".tools/comp-heat",
                                                               "drift", "--budget", "60", "--json"],
        "rc": 0, "answer_state": "OK", "answer_state_claim": "measured",
        "denominators": {"n": 1},
        "vintage": {"answer_produced_utc": (NOW - _dt.timedelta(hours=1)).strftime(
            "%Y-%m-%dT%H:%M:%SZ"), "tool_reported": "repo @cafe", "claim": "measured"},
        "rows": [{"x": 1}], "error": None, "payload_excerpt": None,
    }
    for key in ("comp_heat_drift.json", "comp_cochange.json"):
        (d / key).write_text(json.dumps(doc), encoding="utf-8")
    return str(d)


def _loader(source: str) -> str:
    with open(source, encoding="utf-8") as fh:
        return fh.read()


def _all_strata(mod, tmp, pin):
    """Every deterministic stratum, on every exit it has."""
    seam = _seam_artifact(tmp)
    return {
        "D_naming": mod._stratum_naming(
            {}, {"changed_paths_total": 0, "chain_resolved": 0, "resource_axis_total": 0,
                 "resource_axis_canon": 0, "resource_axis_fallback": 0, "records_axis_total": 0},
            pin),
        "C_lifecycle (computed)": mod._stratum_lifecycle(str(ROOT), NOW, pin),
        "C_lifecycle (git FAILED)": mod._stratum_lifecycle("/nonexistent-repo", NOW, pin),
        "B_cochange (host stand-in)": mod._stratum_cochange(str(ROOT), NOW, EMPTY_MAPS, pin,
                                                            prefix=None),
        "B_cochange (git FAILED)": mod._stratum_cochange("/nonexistent-repo", NOW, EMPTY_MAPS, pin,
                                                         prefix=None),
        "B_cochange (seam)": mod._stratum_cochange(str(ROOT), NOW, EMPTY_MAPS, pin, prefix=seam,
                                                   loader=_loader, now=NOW, max_age_hours=26.0),
        "A_propagation (unconfigured)": mod._stratum_propagation(pin, prefix=None),
        "A_propagation (seam)": mod._stratum_propagation(pin, prefix=seam, loader=_loader,
                                                         now=NOW, max_age_hours=26.0),
    }


# =============================================================================================
def arm_a_every_row_names_its_tool(mod, tmp, pin):
    strata = _all_strata(mod, tmp, pin)
    bad = []
    for label, s in strata.items():
        t = s.get("reproduce")
        if not isinstance(t, dict):
            bad.append("%s: NO RECIPE" % label)
            continue
        if not t.get("tool"):
            bad.append("%s: no tool" % label)
        if not t.get("invocation"):
            bad.append("%s: empty invocation" % label)
        if not t.get("vintage"):
            bad.append("%s: no vintage" % label)
        if t.get("claim") not in mod.REPRODUCIBILITY_CLAIMS:
            bad.append("%s: claim %r outside the declared domain" % (label, t.get("claim")))
    _record("A1 every deterministic stratum carries tool+invocation+vintage+claim", not bad,
            "%d of %d exits clean; problems=%s" % (len(strata) - len(bad), len(strata), bad))
    seam = strata["B_cochange (seam)"]["reproduce"]
    _record("A2 a SEAM-fed row names the PRODUCER's own tool and argv",
            seam["claim"] == "rail-reproducible" and "comp-heat" in seam["tool"]
            and any("comp-heat" in ln for ln in seam["invocation"]),
            "tool=%r argv=%r" % (seam["tool"], seam["invocation"]))
    host = strata["C_lifecycle (computed)"]["reproduce"]
    _record("A3 a HOST-computed row names concrete git argv at the pin",
            host["claim"] == "host-reproducible"
            and all(ln.startswith("git ") for ln in host["invocation"])
            and pin in host["note"],
            "invocation=%r" % (host["invocation"],))
    unc = strata["A_propagation (unconfigured)"]["reproduce"]
    _record("A4 a stratum with NOTHING to re-run says so, rather than inventing a command",
            unc["claim"] == "not-reproducible",
            "claim=%s tool=%r" % (unc["claim"], unc["tool"]))
    return strata


def arm_b_red_mutant_untraceable_row(tmp, pin):
    src = RUNNER.read_text(encoding="utf-8")
    assert src.count(TRACE_ANCHOR) == 1, "recipe anchor not unique at the definition"
    mpath = tmp / "runner_untraceable.py"
    mpath.write_text(src.replace(TRACE_ANCHOR, TRACE_MUTANT), encoding="utf-8")
    mod = _load(mpath, "os11_mutant_untraceable")
    strata = _all_strata(mod, tmp, pin)
    carried = [k for k, s in strata.items() if s.get("reproduce")]
    _record("B RED MUTANT (recipe dropped at the DEFINITION) makes EVERY row untraceable",
            not carried,
            "%d of %d exits still carry a recipe under the mutant: %s"
            % (len(carried), len(strata), carried))


def arm_c_absence_is_loud(mod, tmp):
    txt = mod.render_trace(None)
    loud = "NO RECIPE" in txt and "UNVERIFIABLE" in txt
    _record("C1 an ABSENT recipe renders LOUDLY", loud, txt.replace("\n", " ")[:150])
    src = RUNNER.read_text(encoding="utf-8")
    assert src.count(QUIET_ANCHOR) == 1, "quiet-render anchor not unique"
    mpath = tmp / "runner_quiet.py"
    mpath.write_text(src.replace(QUIET_ANCHOR, QUIET_MUTANT), encoding="utf-8")
    m2 = _load(mpath, "os11_mutant_quiet")
    _record("C2 RED MUTANT (absence renders silently) breaks C1",
            m2.render_trace(None) == "", "mutant rendered %r" % m2.render_trace(None)[:60])
    # And the recipe must reach the RENDERED stratum, not just the dict.
    s = mod._stratum_lifecycle(str(ROOT), NOW, "PINX")
    rendered = mod.render_stratum(s, max_rows=1)
    _record("C3 the recipe reaches the RENDERED stratum",
            "reproduce:" in rendered and "$ git " in rendered,
            [ln for ln in rendered.splitlines() if "reproduce" in ln or ln.strip().startswith("$")][:2])


def arm_d_claim_vocabulary_is_closed(mod):
    try:
        mod._trace("t", ["x"], "v", "definitely-not-a-declared-claim")
        ok, detail = False, "an undeclared claim was ACCEPTED"
    except ValueError as exc:
        ok, detail = True, str(exc)[:150]
    _record("D claim vocabulary is CLOSED (an undeclared value is refused, not defaulted)",
            ok, detail)


def arm_e_the_reproduction(mod, pin):
    """THE POINT OF THE CELL: run stratum C's own recipe and re-derive its rows independently."""
    branch = _branch()
    s = mod._stratum_lifecycle(str(ROOT), NOW, pin)
    if s["status"] != "OK":
        _record("E reproduction", False, "stratum C did not produce rows: %s" % s["status"])
        return
    recipe = s["reproduce"]
    # Re-run the recipe's OWN commands, substituting <repo> as the recipe's note instructs.
    env = dict(os.environ, TZ="UTC")
    outs = []
    for line in recipe["invocation"]:
        argv = line.replace("<repo>", str(ROOT)).split(" ")
        argv = [a for a in argv if a != ""]
        # `--pretty=format:` ends the line with an empty value; split() keeps it correctly.
        p = subprocess.run(argv, capture_output=True, text=True, timeout=100, env=env)
        if p.returncode != 0:
            _record("E reproduction", False,
                    "recipe command failed rc=%d: %s -- %s" % (p.returncode, line, p.stderr[:120]))
            return
        outs.append(p.stdout.splitlines())
    all_paths, touched_out = outs[0], outs[1]

    # An INDEPENDENT implementation of the documented fold -- deliberately not the runner's.
    def pre2(path):
        parts = path.split("/")
        return "/".join(parts[:2]) if len(parts) >= 3 else None

    universe = {pre2(x) for x in all_paths if pre2(x)}
    touched = {pre2(x.strip()) for x in touched_out if x.strip() and pre2(x.strip())}
    cold = sorted(universe - touched)
    mine = [{"subtree": c, "last_touch": ">= %dd ago (outside the scan window)"
             % mod.GROUP_C_TRAILING_DAYS} for c in cold][:30]

    same = mine == s["rows"]
    _record("E THE REPRODUCTION: the recipe re-derives the stratum's rows EXACTLY", same,
            "branch=%s pin=%s; runner rows=%d, independent re-derivation rows=%d, identical=%s%s"
            % (branch, pin[:10], len(s["rows"]), len(mine), same,
               "" if same else "; first divergence: %r vs %r"
               % (next((a for a, b in zip(mine, s["rows"]) if a != b), None),
                  next((b for a, b in zip(mine, s["rows"]) if a != b), None))))
    if same and s["rows"]:
        _record("E2 one named row, reproduced (the criterion's 'TAKE ONE')", True,
                "row %r re-derived from: %s" % (s["rows"][0], " && ".join(recipe["invocation"])))

    # E3 NEGATIVE CONTROL. Arm E is only worth something if it CAN fail. Corrupt the recipe --
    # move the --since window from 90 days to 2 -- and re-derive: far fewer subtrees have been
    # touched in 2 days, so the cold set must GROW and the rows must differ. Without this, "the
    # rows matched" would be a green arm that never demonstrated it could go red.
    wrong = [ln.replace("--since " + recipe["invocation"][1].split("--since ")[1].split(" ")[0],
                        "--since 2026-09-03T00:00:00+00:00")
             for ln in recipe["invocation"]]
    outs2 = []
    for line in wrong:
        argv = [a for a in line.replace("<repo>", str(ROOT)).split(" ") if a != ""]
        p2 = subprocess.run(argv, capture_output=True, text=True, timeout=100, env=env)
        outs2.append(p2.stdout.splitlines() if p2.returncode == 0 else [])
    touched2 = {pre2(x.strip()) for x in outs2[1] if x.strip() and pre2(x.strip())}
    cold2 = sorted(universe - touched2)
    mine2 = [{"subtree": c, "last_touch": ">= %dd ago (outside the scan window)"
              % mod.GROUP_C_TRAILING_DAYS} for c in cold2][:30]
    _record("E3 NEGATIVE CONTROL: a WRONG recipe does NOT reproduce the rows", mine2 != s["rows"],
            "corrupted --since (90d -> 2d): %d cold subtrees vs %d, rows differ=%s"
            % (len(cold2), len(cold), mine2 != s["rows"]))


def main() -> int:
    print("=== OS-s-11 O11-AC1: every deterministic row names its tool, vintage and recipe ===")
    pin = _pin()
    with tempfile.TemporaryDirectory(prefix="os11_") as td:
        tmp = Path(td)
        mod = _load(RUNNER, "os11_runner", branch=_branch())
        arm_a_every_row_names_its_tool(mod, tmp, pin)
        arm_b_red_mutant_untraceable_row(tmp, pin)
        arm_c_absence_is_loud(mod, tmp)
        arm_d_claim_vocabulary_is_closed(mod)
        arm_e_the_reproduction(mod, pin)
    for name, ok, detail in RESULTS:
        print("  %s  %s: %s" % ("PASS" if ok else "FAIL", name, detail))
    n_ok = sum(1 for _, ok, _ in RESULTS if ok)
    n = len(RESULTS)
    print("=== test_os11_traceability: %s (%d/%d) ===" %
          ("PASS" if n_ok == n else "FAIL", n_ok, n))
    return 0 if n_ok == n else 1


def test_os11_traceability():
    assert main() == 0


if __name__ == "__main__":
    sys.exit(main())
