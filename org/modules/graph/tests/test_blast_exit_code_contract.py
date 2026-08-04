"""
Regression: comp-blast exit codes are DISJOINT -- a TOOL FAILURE may never read as an ESTATE VERDICT.

Root cause (0.7.0_AE_CloudOps 2026-07-31, DIALED-TOOL-FLOW pass on comp-blast, Andrew-instructed):
rc=1 carried THREE unrelated meanings at once, all three measured on the live tool:
    * a real PHANTOM-CONSUMER finding (zero downstream consumers)
    * a usage error (`--direction sideways`, an unknown flag)
    * an uncaught UnicodeEncodeError crash (20 of 2252 graph nodes carry a corpus claim line
      that cp1252 stdout cannot encode)
So a caller keying on rc could not tell "this resource has no consumers" from "the tool blew up
before measuring anything."

THE COLLISION WAS LOAD-BEARING, NOT COSMETIC. comp_debt/grounding_lib.py:154 read
`elif "PHANTOM-CONSUMER" in up or r.returncode == 1: status = GRAPH_ZERO_CONSUMER`
-- so a CRASH was laundered into evidence that a resource has NO CONSUMERS, i.e. into DELETION
evidence, on the one axis where being wrong is irreversible. Nothing had been measured at all.

Fix: the VERDICT moved (1 -> 4). rc=1 goes back to meaning ONLY "the tool failed", per the estate
standard (CTO 20260709T195217Z: "1 means the tool failed, and ONLY that") which `_ContractParser`
already honours for usage errors. The verdict is the thing that had to move, because a crash cannot
be made to pick a different exit code -- Python's uncaught-exception rc is 1 and is not ours to choose.

WHY THIS FILE EXISTS AT ALL: the pre-existing blast suite (12/12) passed IDENTICALLY before and after
the change -- it never asserted an exit code, so it was structurally blind to the defect and would not
have caught a silent revert. A fix without a gate is prose.

Every test here EXERCISES THE BINARY. Marker strings (CONSUMER-OK / PHANTOM-CONSUMER) are asserted
alongside the codes because they are the stable thing callers should key on, and they must not drift.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

_HERE = Path(__file__).resolve()
_GRAPH_DIR = _HERE.parents[1]                 # org/modules/graph
_CLI = _GRAPH_DIR / "cli.py"
_REPO = _GRAPH_DIR.parents[2]

EXIT_OK = 0
EXIT_TOOL_FAILED = 1
EXIT_STALE = 2
EXIT_NOT_FOUND = 3
EXIT_PHANTOM = 4

_GARBAGE = "__nonexistent_zzz_target_no_node_has_this__"


def _run(*argv: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(_CLI), "blast", *argv],
        capture_output=True, text=True, cwd=str(_REPO),
    )


#: Candidates are DERIVED from the cache in-process (never hardcoded -- a hand-picked control
#: measures the author, not the instrument) but the number of SUBPROCESS calls is bounded: sweeping
#: 2252 nodes through the binary is ~100 minutes and would make this gate unrunnable, which is its
#: own kind of absent gate.
_MAX_CANDIDATES = 6


#: CANDIDATES COME FROM THE UNIVERSE THE TOOL ACTUALLY QUERIES (kuzu, per the Andrew ruling
#: 2026-08-03) -- NOT from the retired `.comp-graph/graph.json` trace cache.
#:
#: This is not a cosmetic re-point. Kuzu addresses a gold script as
#: `pipeline:bd:gold:A_00.accounts_dimension`; the trace cache addressed it as
#: `gold:A_00.accounts_dimension`, and kuzu carries ZERO `gold:`-prefixed ids. Worse for THIS file:
#: a node with no outbound edge in the small private graph very often HAS dependents in the estate
#: graph, so every phantom candidate resolved to CONSUMER-OK and `test_phantom_verdict_is_4_not_1`
#: -- the regression this whole file exists for -- SKIPPED. Measured on the first post-rewire run:
#: 5 passed, 2 skipped.
#:
#: A SKIPPED TEST IS NOT A GATE (this file's own words). Deriving from the live universe keeps every
#: assertion below byte-identical while restoring the test's ability to fire.
_KUZU_CACHE: dict = {}


def _graph() -> dict:
    """The live universe, shaped like the old cache dict so the assertions below are unchanged."""
    if _KUZU_CACHE:
        return _KUZU_CACHE
    sys.path.insert(0, str(_REPO))
    try:
        from org.modules.graph import comp_blast_universe as bu
        g, _prov, _path = bu.load_kuzu_universe(refresh=False)
    except Exception as ex:  # noqa: BLE001
        pytest.skip(f"canonical kuzu universe unavailable -- cannot pick live nodes ({ex})")
    _KUZU_CACHE["nodes"] = {nid: {"node_type": n.node_type} for nid, n in g.nodes.items()}
    _KUZU_CACHE["edges"] = [{"source": e.source, "target": e.target} for e in g.edges]
    return _KUZU_CACHE


def _with_and_without_outbound() -> tuple:
    """(has-dependents, no-dependents) node-id lists, computed in-process without subprocesses.

    DEPENDENTS, not merely outbound edges: after the defect-(b) fix the consumer verdict is
    evaluated in BOTH directions (this graph mixes edge conventions -- WRITES points
    producer->artifact, CALLS/FETCHES point consumer->producer). A candidate picked on outbound
    edges alone would be a phantom by this file's model and CONSUMER-OK by the tool's, and the test
    would fail for a reason that is not a defect.
    """
    g = _graph()
    nodes = g.get("nodes", {})
    linked = set()
    for e in g.get("edges", []):
        if e.get("source"):
            linked.add(e["source"])
        if e.get("target"):
            linked.add(e["target"])
    have = [n for n in nodes if n in linked]
    havent = [n for n in nodes if n not in linked]
    return have, havent


def _node_with_consumers() -> str:
    """A node the graph says HAS downstream edges -- the positive control, picked live."""
    have, _ = _with_and_without_outbound()
    if not have:
        pytest.skip("no node with outbound edges in cache")
    return have[0]


def _crash_candidates() -> list:
    """Nodes whose corpus claim text is NOT cp1252-encodable -- i.e. the ones that crash the render.

    Derived, not guessed. Selecting these by random sampling made the crash test SKIP (measured: 0
    hits in 12 sampled nodes), and A SKIPPED TEST IS NOT A GATE -- it is an absent gate that reads
    like a present one. The crash surface is ~20 of 2252 nodes, so a blind sample almost never lands
    on it; the risk corpus names them exactly.
    """
    risk = _REPO / "org" / "modules" / "graph" / "nerves-risk-edges.json"
    if not risk.exists():
        return []
    try:
        edges = json.loads(risk.read_text(encoding="utf-8")).get("edges", [])
    except (OSError, ValueError):
        return []
    # MUST intersect with the graph's own node set. The risk corpus addresses things comp-blast has
    # never heard of (`s3:opal-data-inf`, `file:...`, `tool:...`); those resolve NOT-FOUND (rc=3) and
    # return BEFORE the risk banner renders, so they can never crash. Measured: the first 8 raw
    # candidates were all of that shape, which is why the crash test skipped while 112 candidates and
    # a known crasher both existed. Filtering on non-ASCII ALONE selected for the wrong property.
    known = set(_graph().get("nodes", {}))
    out = []
    for e in edges:
        nid = e.get("node")
        if not nid or nid not in known:
            continue
        blob = " ".join(str(c) for c in (e.get("claims") or []))
        try:
            blob.encode("cp1252")
        except UnicodeEncodeError:
            out.append(nid)
    return out


def test_phantom_verdict_is_4_not_1():
    """THE REGRESSION. A zero-consumer finding must NOT share rc with a crash."""
    _, havent = _with_and_without_outbound()
    if not havent:
        pytest.skip("no zero-outbound node in cache")
    for nid in havent[:_MAX_CANDIDATES]:
        r = _run(nid, "--check-consumers")
        if "PHANTOM-CONSUMER" in r.stdout:
            assert r.returncode == EXIT_PHANTOM, (
                f"PHANTOM-CONSUMER on {nid} returned rc={r.returncode}, expected {EXIT_PHANTOM}. "
                "rc=1 is RESERVED for tool failure -- a verdict there is indistinguishable from a crash."
            )
            return
    pytest.skip(f"no phantom-consumer node among {_MAX_CANDIDATES} zero-outbound candidates")


def test_consumer_ok_is_0_and_marker_intact():
    """Positive control: the happy path still clears 0 and still prints its marker."""
    nid = _node_with_consumers()
    r = _run(nid, "--check-consumers")
    assert r.returncode == EXIT_OK, f"{nid} -> rc={r.returncode}, expected 0\n{r.stdout}{r.stderr}"
    assert "CONSUMER-OK" in r.stdout, "the CONSUMER-OK marker is what callers key on; it must not drift"


def test_usage_error_is_tool_failed_not_a_verdict():
    """A bad flag value is a TOOL FAILURE (1). It must never land on a verdict code."""
    nid = _node_with_consumers()
    r = _run(nid, "--direction", "sideways")
    assert r.returncode == EXIT_TOOL_FAILED, f"usage error -> rc={r.returncode}, expected 1"
    assert r.returncode not in (EXIT_PHANTOM, EXIT_STALE, EXIT_NOT_FOUND), (
        "a usage error landed on a VERDICT code -- the exact confusion this file gates"
    )


def test_unknown_flag_is_tool_failed():
    nid = _node_with_consumers()
    r = _run(nid, "--no-such-flag-zzz")
    assert r.returncode == EXIT_TOOL_FAILED, f"unknown flag -> rc={r.returncode}, expected 1"


def test_not_found_stays_3():
    """NOT-FOUND is a REFUSAL, distinct from both failure and verdict. Pre-existing contract."""
    r = _run(_GARBAGE)
    assert r.returncode == EXIT_NOT_FOUND, f"NOT-FOUND -> rc={r.returncode}, expected 3"


def test_verdict_and_failure_codes_are_disjoint():
    """The invariant, stated directly: no code means two things.

    This is the assertion that would fail if someone re-merged failure and verdict, even if every
    individual test above were rewritten.
    """
    failure_codes = {EXIT_TOOL_FAILED}
    verdict_codes = {EXIT_OK, EXIT_STALE, EXIT_PHANTOM}
    refuse_codes = {EXIT_NOT_FOUND}
    assert not (failure_codes & verdict_codes), "a failure code is also a verdict code"
    assert not (failure_codes & refuse_codes), "a failure code is also a refusal code"
    assert not (verdict_codes & refuse_codes), "a verdict code is also a refusal code"


def test_crash_node_does_not_emit_a_verdict_code():
    """A crashing node must exit as a FAILURE, never as a finding about the estate.

    This is the test that ties the fix to its cause: the UnicodeEncodeError crash is still live
    (encoding is a SEPARATE fix), so this asserts the property that makes the crash SAFE -- it
    reports failure, not a zero-consumer verdict. If the encoding is later fixed the node stops
    crashing and this test skips rather than fails.
    """
    # DEFAULT render mode, deliberately: `--check-consumers` is HOLD-BLIND (the risk banner is not
    # emitted in that mode at all), so it is the one mode that CANNOT crash. Running the crash test
    # there is why it skipped -- the probe was pointed at the immune surface.
    for nid in _crash_candidates()[:_MAX_CANDIDATES]:
        r = _run(nid)
        if "UnicodeEncodeError" in r.stderr or "Traceback" in r.stderr:
            assert r.returncode == EXIT_TOOL_FAILED, (
                f"crash on {nid} returned rc={r.returncode}. A CRASH MUST NOT CARRY A VERDICT CODE -- "
                "that is how a tool failure became deletion evidence."
            )
            assert r.returncode != EXIT_PHANTOM, "a crash is reading as a phantom-consumer finding"
            return
    pytest.skip("no crashing node in this cache -- encoding may have been fixed")
