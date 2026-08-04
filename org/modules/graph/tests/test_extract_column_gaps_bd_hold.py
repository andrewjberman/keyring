"""extract_pipeline._extract_column_gaps -- held-path GUARD MECHANISM oracle (post-lift form).

HISTORY: authored by 3.0.0_SA_CVO~B under NFRA_TOOLPASS C0, when the 2026-07-09 sovereign hold
was live -- the original three tests asserted bd/schwab paths were SKIPPED, which was true under
the governance values then loaded. The hold was RETRACTED 2026-07-14 (SOVEREIGN_HELD_PATHS=()
is the CORRECT engine state per Andrew's verbatim + the CTO 07-22 predicate split), and the
assertions went stale-red for ~3 weeks unobserved -- the file predates the F9 gate's watch globs
(dial F10 @37bf63f4a: the F9 rot class survives wherever the glob cannot see).

REPAIRED to post-lift truth 2026-08-04 (TO ADHOC.graph-tests-hygiene-f10, 0.8.0_AE_CloudComp~D):
  - POST-LIFT TRUTH: a bd path is READ now, same as inf -- asserting the read happens.
  - MECHANISM VIA INJECTION: the guard chain (_extract_column_gaps -> trace_graph._held_path_hit
    -> sovereign_held.is_held_path, which resolves SOVEREIGN_HELD_PATHS at CALL time) is tested
    against an INJECTED SYNTHETIC marker (monkeypatch on sovereign_held), never the governance
    set -- the mechanism stays testable while correctly holding nothing. _path_matches is a
    substring check (sovereign_held.py:80), so the synthetic marker matches by construction.
  - The include_held_override io-threading contract is exercised UNDER the injected hold.

Hermetic + bd-SAFE as before: synthetic tmp files only; the real trees are never touched.
This file is enrolled in the F9 pipescript-suite gate watch globs (single derivation point in
.tools/git-hooks/pipescript-suite-check.sh) in the same landing.

# rail-checked: assurance oracle for extract_pipeline._extract_column_gaps (dial F10 repair)
Original author: 3.0.0_SA_CVO~B. F10 repair: 0.8.0_AE_CloudComp~D.
"""
from __future__ import annotations

import os
import sys
import tempfile
from pathlib import Path

_HERE = os.path.dirname(os.path.abspath(__file__))
_WS = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(_HERE))))
if _WS not in sys.path:
    sys.path.insert(0, _WS)

from org.modules.graph import extract_pipeline as ep  # noqa: E402
from org.modules.graph import sovereign_held as sh  # noqa: E402

# A gold-script with a real column gap: loads columns ['a','b'] but accesses 'missing_col'.
_SCRIPT = (
    "KEY = 's3://x/y.parquet'\n"
    "df = _load_parquet(KEY, columns=['a', 'b'])\n"
    "x = df['missing_col']\n"
)

# SYNTHETIC injection marker -- matches nothing real; _path_matches is substring, so any tmp
# path containing this segment is "held" while the injection is active.
_SYNTH_ZONE = "synthetic_held_zone_f10"


def _write(dirpath: Path) -> Path:
    dirpath.mkdir(parents=True, exist_ok=True)
    f = dirpath / "fake_gold.py"
    f.write_text(_SCRIPT, encoding="utf-8")
    return f


def test_bd_and_inf_paths_are_both_read_post_lift():
    """POST-LIFT TRUTH: the 07-14 retraction emptied the governance set, so a bd gold path is
    READ and analyzed exactly like an inf path -- the read HAPPENS now (this inverts the
    hold-era assertion, deliberately)."""
    with tempfile.TemporaryDirectory() as d:
        inf_file = _write(Path(d) / "data" / "inf" / "scripts" / "gold")
        bd_file = _write(Path(d) / "data" / "black_diamond" / "scripts" / "gold")
        inf_gaps = ep._extract_column_gaps(inf_file)
        bd_gaps = ep._extract_column_gaps(bd_file)
    assert inf_gaps, f"an inf gold path must be READ + analyzed (column-gap finding expected): {inf_gaps}"
    assert bd_gaps, (
        "POST-LIFT: a bd gold path must be READ like any other -- SOVEREIGN_HELD_PATHS=() is the "
        f"correct state and nothing is held; got: {bd_gaps}"
    )


def test_guard_mechanism_catches_injected_held_values(monkeypatch):
    """THE MECHANISM, tested without governance: inject a synthetic held marker into
    sovereign_held.SOVEREIGN_HELD_PATHS (resolved at call time by is_held_path) and prove the
    guard skips a matching path BEFORE the read, while an identical file outside the injected
    zone still reads -- the non-vacuous pair."""
    monkeypatch.setattr(sh, "SOVEREIGN_HELD_PATHS", (_SYNTH_ZONE + "/",))
    with tempfile.TemporaryDirectory() as d:
        held_file = _write(Path(d) / _SYNTH_ZONE / "scripts" / "gold")
        free_file = _write(Path(d) / "data" / "inf" / "scripts" / "gold")
        held_gaps = ep._extract_column_gaps(held_file)
        free_gaps = ep._extract_column_gaps(free_file)
    assert held_gaps == [], (
        f"a path under the INJECTED held marker must be SKIPPED by the guard -> []: {held_gaps}"
    )
    assert free_gaps, (
        f"the same content OUTSIDE the injected zone must still read (proves the skip is the "
        f"guard, not a broken analyzer): {free_gaps}"
    )


def test_include_held_override_reads_under_injected_hold(monkeypatch):
    """io-threading contract (comp-pipescript io passes include_held_override): UNDER an injected
    hold, default skips and override=True reads -- the DS deploy/verify lift path stays exercised
    even though the live governance set is empty."""
    monkeypatch.setattr(sh, "SOVEREIGN_HELD_PATHS", (_SYNTH_ZONE + "/",))
    with tempfile.TemporaryDirectory() as d:
        held_file = _write(Path(d) / _SYNTH_ZONE / "scripts" / "gold")
        skipped = ep._extract_column_gaps(held_file)
        read = ep._extract_column_gaps(held_file, include_held_override=True)
    assert skipped == [], f"default under injected hold must skip: {skipped}"
    assert read, f"include_held_override=True must READ despite the injected hold (non-vacuous): {read}"
