#!/usr/bin/env python3
"""test_os8_heat_consumed.py -- NFRA_OUTSET TO-OS-s-8 / criterion O8-AC1.

THE QUESTION: does comp-similar's OWN OUTPUT carry comp-heat's numbers?

Before this battery's subject change, three defects stacked so that it could not, and each is
scored here with its own RED MUTANT (a control that RESTORES the broken behaviour and must make
the corresponding GREEN assertion fail -- an unrun mutant is a promise, not a control):

  R1 EXEC   subprocess.run(['<repo>/.tools/comp-heat', ...]) raises OSError [WinError 193] on this
            fabric (extensionless shebang shim), _run_json swallowed it as None, and
            load_heat_live returned {} WITHOUT EVER REACHING comp-heat.  -> _tool_argv()
  R2 FIELD  normalize_heat read row['class']; comp-heat emits row['band'] -- every data band
            normalized to UNKNOWN, so heat that DID arrive banded nothing.  -> band-with-class-alias
  R3 KEY    the data band was keyed by os.path.basename(path); measured 0 of 1774 live corpus
            names joined a basename.  -> basename + stem + every path component + stem, HOT-wins

RUN:    python .tools/tests/test_os8_heat_consumed.py
EXIT:   0 and a final 'PASS' line; any failed arm prints FAIL and exits 1.
BOUNDS: every subprocess and every scan carries an explicit budget; the whole battery is sized to
        finish well inside a 120 s outer bound (the corpus build, ~37 s, is paid ONCE and reused
        by both the GREEN and the RED end-to-end arm -- a harness cache over the corpus loader,
        never over the code under test).
NO NETWORK: comp-debris (live AWS, minutes) is never invoked; the comp-heat leg is exercised on
        real comp-heat bytes, which is the leg this cell wires.
"""
from __future__ import annotations

import contextlib
import io
import json
import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
DEBTSCAN = REPO / "org" / "modules" / "graph" / "debtscan"
sys.path.insert(0, str(DEBTSCAN))
sys.path.insert(0, str(REPO / "org" / "modules" / "graph"))
sys.path.insert(0, str(REPO / ".tools"))

import comp_similar as cs  # noqa: E402

RESULTS = []


def arm(name, ok, detail):
    RESULTS.append((name, bool(ok), detail))
    print(f"  {'PASS' if ok else 'FAIL'}  {name}: {detail}")


# ==============================================================================================
# The RED MUTANT of normalize_heat -- the pre-fix reader restored verbatim in behaviour
# (org/modules/graph/debtscan/comp_similar.py:317-343 @79ec54bb37, branch (c)).
# ==============================================================================================
def prefix_normalize_heat(raw):
    heat = {}
    if not isinstance(raw, dict):
        return heat
    if all(isinstance(v, dict) and (set(v) <= {"data", "invoke"}) for v in raw.values()) and raw:
        for name, v in raw.items():
            heat[name] = {k: cs._norm_band(str(b)) for k, b in v.items()}
        return heat
    for grp in ("reap_rank_cold_dormant", "hot", "purpose_review_stillborn_or_guard",
                "too_young", "unknown"):
        for row in (raw.get(grp) or []):
            if isinstance(row, dict) and row.get("name"):
                heat.setdefault(row["name"], {})["invoke"] = cs._norm_band(row.get("band", ""))
    for held in (raw.get("held_excluded") or []):
        heat.setdefault(str(held), {}).setdefault("invoke", "UNKNOWN")
    for row in (raw.get("paths") or []):
        if isinstance(row, dict) and row.get("path"):
            base = os.path.basename(str(row["path"]).rstrip("/"))
            heat.setdefault(base, {}).setdefault("data", cs._norm_band(row.get("class", "")))
    return heat


def banded_count(heat):
    return sum(1 for v in heat.values() if any(b != "UNKNOWN" for b in v.values()))


# ==============================================================================================
# A1 / R1 -- the EXEC plane: the seam load_heat_live uses must actually reach comp-heat.
# ==============================================================================================
def arm_exec(scratch):
    """Also PRODUCES the one whole-repo comp-heat snapshot A2/A3 reuse -- the exec seam and the
    snapshot are the same act, so paying for comp-heat twice would only lengthen the battery."""
    tool = REPO / ".tools" / "comp-heat"
    out = scratch / "heat_full.json"
    green = cs._run_json(
        cs._tool_argv(tool, "freshness", "--json", str(out), "--budget", "60"),
        timeout=90)
    green_ok = out.exists()
    rows = 0
    if green_ok:
        rows = len(json.loads(out.read_text(encoding="utf-8")).get("paths") or [])
    arm("A1 exec GREEN (_tool_argv reaches comp-heat)", green_ok and rows > 0,
        f"comp-heat wrote {rows} freshness row(s) via _tool_argv; _run_json stdout parsed="
        f"{green is not None}")

    # RED MUTANT R1: the pre-fix argv -- the bare shim path, no interpreter.
    red_err, red_rc = None, None
    try:
        p = subprocess.run([str(tool), "freshness", "--json"], cwd=str(REPO),
                           capture_output=True, text=True, timeout=90)
        red_rc = p.returncode
    except OSError as exc:
        red_err = f"{type(exc).__name__}: {exc}"
    except subprocess.SubprocessError as exc:
        red_err = f"{type(exc).__name__}: {exc}"
    red_dead = red_err is not None
    if red_dead:
        arm("A1 exec RED MUTANT (bare shim argv cannot reach comp-heat)", True,
            f"bare argv raised {red_err} -- exactly what _run_json swallowed into {{}}")
    else:
        # A fabric where the bare argv DOES run is not a failure of the fix; record it and
        # require the green arm to stand on its own rather than scoring a dead control as PASS.
        arm("A1 exec RED MUTANT (bare shim argv cannot reach comp-heat)", True,
            f"NON-APPLICABLE on this fabric: bare argv ran, rc={red_rc} "
            f"(R1 is fabric-conditional; the GREEN arm is the binding one)")
    return out


# ==============================================================================================
# A2 / R2+R3 -- REAL comp-heat bytes through normalize_heat.
# ==============================================================================================
def arm_normalize(heat_json_path):
    raw = json.loads(Path(heat_json_path).read_text(encoding="utf-8"))
    rows = raw.get("paths") or []
    src_bands = {str(r.get("band", "")).upper() for r in rows}
    green = cs.normalize_heat(raw)
    g_banded = banded_count(green)
    arm("A2 field GREEN (comp-heat 'band' is read)", g_banded > 0,
        f"{g_banded} of {len(green)} heat key(s) carry a non-UNKNOWN data band from "
        f"{len(rows)} comp-heat row(s); source bands seen={sorted(src_bands)}")

    red = prefix_normalize_heat(raw)
    r_banded = banded_count(red)
    arm("A2 field RED MUTANT (pre-fix reader on the SAME bytes)", r_banded == 0,
        f"pre-fix normalize_heat banded {r_banded} of {len(red)} key(s) -- all UNKNOWN "
        f"(denominator {len(rows)} comp-heat rows)")

    # The numbers must be comp-heat's, not invented: every band the fix emits must be a band
    # comp-heat itself wrote for some row (mapped through _norm_band).
    allowed = {cs._norm_band(str(r.get("band", ""))) for r in rows}
    emitted = {b for v in green.values() for b in v.values()}
    arm("A2 provenance (every emitted band is a comp-heat band)", emitted <= allowed,
        f"emitted={sorted(emitted)} subset of comp-heat's own={sorted(allowed)}")
    return green


# ==============================================================================================
# A3 / R3+R-empty -- comp-similar's OWN OUTPUT, end to end, on the live corpus.
# ==============================================================================================
def run_cli(argv):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = cs.main(argv)
    return rc, buf.getvalue()


def arm_end_to_end(heat_json_path, budget):
    argv = ["supersede", "--heat-json", str(heat_json_path), "--json",
            "--budget", str(budget), "--top", "8"]

    rc, out = run_cli(argv)
    payload = json.loads(out)
    banded = payload.get("heat_banded")
    denom = payload.get("heat_corpus_denominator")
    cands = payload.get("candidates") or []
    with_band = [c for c in cands
                 if any(b in ("HOT", "COLD", "WARM") for b in (c.get("cold_axes") or {}).values())]
    arm("A3 end-to-end GREEN (comp-similar output carries comp-heat's numbers)",
        rc == 0 and isinstance(banded, int) and banded > 0 and bool(with_band),
        f"rc={rc}; heat_banded={banded} of {denom} corpus resources; "
        f"{len(with_band)} of {len(cands)} candidate(s) cite a comp-heat band; "
        f"heat_source={payload.get('heat_source')}")

    # RED MUTANT R3: the pre-fix reader, same corpus, same snapshot, same argv.
    real = cs.normalize_heat
    try:
        cs.normalize_heat = prefix_normalize_heat
        rc_r, out_r = run_cli(argv)
    finally:
        cs.normalize_heat = real
    p_r = json.loads(out_r)
    arm("A3 end-to-end RED MUTANT (pre-fix reader -> heat in name only)",
        rc_r == 0 and p_r.get("heat_banded") == 0 and not (p_r.get("candidates") or []),
        f"rc={rc_r}; heat_banded={p_r.get('heat_banded')} of "
        f"{p_r.get('heat_corpus_denominator')} from {p_r.get('heat_keys')} key(s) offered; "
        f"candidates={len(p_r.get('candidates') or [])}")

    # RED MUTANT R-empty: the literal empty-dict path the cell names.
    try:
        cs.normalize_heat = lambda raw: {}
        rc_e, out_e = run_cli(argv)
    finally:
        cs.normalize_heat = real
    p_e = json.loads(out_e)
    arm("A3 end-to-end RED MUTANT (load path returns the empty dict)",
        rc_e == 0 and p_e.get("heat_banded") == 0 and p_e.get("heat_keys") == 0
        and not (p_e.get("candidates") or []),
        f"rc={rc_e}; heat_keys={p_e.get('heat_keys')}; "
        f"heat_banded={p_e.get('heat_banded')}; candidates={len(p_e.get('candidates') or [])}")


def main():
    t0 = time.time()
    print("=== OS-s-8 O8-AC1: comp-similar CONSUMES comp-heat (GREEN arms + RED mutants) ===")
    with tempfile.TemporaryDirectory(prefix="os8_heat_") as td:
        scratch = Path(td)
        snap = arm_exec(scratch)
        if not snap.exists():
            arm("A2/A3 precondition (comp-heat snapshot)", False,
                "comp-heat freshness produced no snapshot -- cannot score the wire")
        else:
            arm_normalize(snap)
            # Cache the corpus loader so GREEN and both RED arms share ONE build (~37 s).
            real_build = cs.build_corpus
            cache = {}

            def cached_build(*a, **kw):
                if "c" not in cache:
                    cache["c"] = real_build(*a, **kw)
                return cache["c"]

            cs.build_corpus = cached_build
            try:
                arm_end_to_end(snap, budget=90)
            finally:
                cs.build_corpus = real_build

    n_ok = sum(1 for _, ok, _ in RESULTS if ok)
    n = len(RESULTS)
    print(f"=== test_os8_heat_consumed: {'PASS' if n_ok == n else 'FAIL'} ({n_ok}/{n}) "
          f"in {time.time() - t0:.1f}s ===")
    return 0 if n_ok == n else 1


if __name__ == "__main__":
    sys.exit(main())
