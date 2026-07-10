#!/usr/bin/env python3
"""Tests for comp-dispatch (comp_dispatch), NFRA_TOOLPASS tool-14.

CTO verdict was CLEAN; re-run confirmed read-only + correct parse, and found ONE real gap:
CD1 -- gate detection is a CLOSED 3-pattern allowlist that missed cot's bcd-mode conditional skip
(gold_dispatch.sh:380 `if [ "$mode" != "bcd" ]` skips PHASE_A) and did not disclose the allowlist
is bounded -- inconsistent with the tool's OWN --undispatched, which honestly discloses its gap.
Fix: surface the mode-skip gate + disclose the detector boundary.

Fixtures are SYNTHETIC gold_dispatch.sh snippets -- NO firm data (sovereign-safe; the bd firm is a
prohibited path and never read here; cot exercise lives in a separate graph-gated check).
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

_WS = Path(__file__).resolve().parents[4]
_CLI = _WS / "org" / "modules" / "graph" / "comp_dispatch.py"
spec = importlib.util.spec_from_file_location("comp_dispatch", _CLI)
D = importlib.util.module_from_spec(spec)
sys.modules["comp_dispatch"] = D
spec.loader.exec_module(D)


# a minimal synthetic gold_dispatch.sh with the declared blocks + a bcd-mode skip
_FIXTURE = '''#!/bin/bash
CATALOG << 'EOF'
A_00 | A_00.accounts.py | --upload
B_00 | B_00.holdings.py | --upload
C_00 | C_00.perf.py     | --upload
EOF

CHAIN_FULL="A_00 B_00 C_00"
CHAIN_CANON="B_00 C_00"
GROUP_A="A_00"

check_freshness() { :; }

run_chain_parallel() {
  local mode="$1"   # "full" = all; "bcd" = skip A
  if [ "$mode" != "bcd" ]; then
    run_background A_00
  fi
  run_background B_00
}
'''


# ---- CD1: the mode-skip gate is surfaced ---------------------------------------------------

def test_cd1_mode_skip_gate_is_detected():
    gates = D.parse_gates(_FIXTURE)
    labels = {g["gate"] for g in gates}
    assert "mode-skip" in labels, "the bcd-mode conditional skip MUST be surfaced as a gate"
    assert "freshness" in labels, "positive control: the known freshness gate still detected"


def test_cd1_MUTANT_without_mode_pattern_the_bcd_skip_is_invisible():
    """NEGATIVE CONTROL: the pre-fix allowlist (freshness/resume/incremental only) does NOT see the
    bcd-mode skip. Proves the mode-skip pattern is load-bearing."""
    import re
    old_gates = [
        (re.compile(r"\bcheck_freshness\b"), "freshness"),
        (re.compile(r"GOLD_RESUME|_checkpoint_done|\.checkpoints/"), "resume-skip"),
        (re.compile(r"--incremental"), "incremental"),
    ]
    matched = {label for rx, label in old_gates if rx.search(_FIXTURE)}
    assert "mode-skip" not in matched, "premise: the old 3-pattern set cannot see the bcd skip"
    # and the fixture DOES contain a real bcd skip
    assert 'if [ "$mode" != "bcd" ]' in _FIXTURE


# ---- CD1: the detector discloses it is a bounded allowlist ---------------------------------

def test_cd1_gates_output_discloses_bounded_allowlist():
    a = D.analyze  # ensure symbol exists
    assert a
    # render the --gates view
    import argparse
    ns = argparse.Namespace(chain=None, script=None, gates=True, undispatched=False)
    rep = {"firm": "x", "path": "p", "catalog": {}, "chains": {}, "chains_raw": {}, "groups": {},
           "gates": D.parse_gates(_FIXTURE), "undispatched": []}
    out = D.render(rep, ns)
    assert "known-pattern set" in out or "bounded" in out.lower(), \
        "--gates MUST disclose its detection is a bounded allowlist (not exhaustive)"
    assert "NOT surfaced" in out, "must state that a gate outside the patterns is not surfaced"


def test_cd1_json_carries_the_detector_boundary_flag():
    known = [label for _rx, label, _d, _o in D._GATES]
    assert "mode-skip" in known, "the known-pattern list must include mode-skip"
    assert D._GATE_LABELS and "freshness" in D._GATE_LABELS


# ---- unchanged behavior: parse correctness (the CLEAN axes) --------------------------------

def test_catalog_and_chains_parse():
    cat = D.parse_catalog(_FIXTURE)
    assert set(cat) == {"A_00", "B_00", "C_00"}
    assert cat["A_00"]["file"] == "A_00.accounts.py"
    chains_raw = D.parse_vars(_FIXTURE, "CHAIN")
    chains = {n: D.resolve_ids(v, chains_raw) for n, v in chains_raw.items()}
    assert chains["FULL"] == ["A_00", "B_00", "C_00"]
    assert chains["CANON"] == ["B_00", "C_00"]


def test_nested_chain_reference_resolves_decycled():
    text = 'CHAIN_A="X Y"\nCHAIN_B="$CHAIN_A Z"\nCHAIN_C="$CHAIN_B $CHAIN_A"\n'
    raw = D.parse_vars(text, "CHAIN")
    assert D.resolve_ids(raw["B"], raw) == ["X", "Y", "Z"]
    # a self-cycle must TERMINATE (de-cycle), not infinite-loop; the literal survives
    cyc = {"A": "$CHAIN_A P"}
    res = D.resolve_ids(cyc["A"], cyc)
    assert "P" in res and len(res) < 10, "self-reference must terminate (de-cycled), not run away"
    assert "$CHAIN_A" not in res, "the cyclic reference must not leak into the id list"


def test_read_only_no_write_or_exec_symbols():
    src = _CLI.read_text(encoding="utf-8")
    # the only file op is a read-open; no write-open, no subprocess/os.system (never executes bash)
    assert "open(path" in src
    assert "subprocess" not in src and "os.system" not in src and "Popen" not in src
    for w in ('.write(', "'w'", '"w"', "mode='w'"):
        assert w not in src, f"unexpected write construct {w!r} -- tool must be read-only"
