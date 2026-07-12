"""NFRA_LIVELEARN CYCLE B tool-4 -- comp-blast IMPACT-REACH discrimination probe.

CTO~D B2 (2026-07-12): score comp-blast's IMPACT-REACH -- does the blast radius of a node REACH a KNOWN
downstream dependent (grounded from SOURCE)? comp-blast is graph-backed, so the runner SEPARATES reach
from graph coverage: in-graph + dependent reached -> yes; in-graph + a known dependent MISSED -> no (a real
impact-traversal miss); NOT-FOUND (node absent / SHA-drifted out) -> VOID (graph-coverage/staleness, NOT a
reach miss). Plus the sovereign held-query guard + isolation (the dependent term is NOT in the query).

Hermetic: injected runner (fake stdout/rc); no ~34s trace-graph build, no AWS, no bd.

# rail-checked: assurance oracle for the comp-blast impact-reach runner (NFRA_LIVELEARN CYCLE B tool-4)
Author: 0.8.0_AE_CloudComp.
"""
from __future__ import annotations

import importlib.util
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_WS = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(_HERE))))
_MODULE = os.path.join(_WS, "org", "modules", "graph", "compproof", "tool_probe.py")
_spec = importlib.util.spec_from_file_location("tool_probe_blast", _MODULE)
tp = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(tp)


def _probe(query="gold:INF_A_00.accounts_dimension", term="INF_C_00.canonical_performance"):
    return {"probe_id": "comp-blast/impact-reach-discrimination", "tool": "comp-blast",
            "tool_class": "impact-blast-radius", "kind": "blast-discrimination",
            "fixture": {"query": query, "answer_term": term}, "usability_timeout_s": 150}


def _run(out, rc=0, query="gold:INF_A_00.accounts_dimension"):
    return tp._run_blast_discrimination_probe(_probe(query=query), runner=lambda q, to: (out, rc))


def test_in_graph_and_dependent_REACHED_yes():
    out = ("BLAST RADIUS: gold:INF_A_00.accounts_dimension\n  GOLD_SCRIPT (28):\n"
           "    - INF_A_04.client_dimension\n    - INF_C_00.canonical_performance\n")
    assert _run(out)["effective"] == "yes"


def test_in_graph_but_known_dependent_MISSED_no():
    # node found (a real blast radius) BUT the known dependent is absent -> a real impact-traversal miss
    out = "BLAST RADIUS: gold:INF_A_00.accounts_dimension\n  GOLD_SCRIPT (1):\n    - INF_A_04.client_dimension\n"
    assert _run(out)["effective"] == "no"


def test_NOT_FOUND_VOIDs_graph_coverage_not_a_reach_miss():
    out = ("NOT-FOUND: no graph node matches 'gold:INF_A_00.accounts_dimension' -- check the name or run "
           "comp-build. This is a NOT-FOUND, not a 'nothing breaks' clear.")
    row = _run(out)
    assert row["effective"] == "unknown" and "NOT-FOUND" in row["void_reason"], \
        "a NOT-FOUND node is a graph-coverage/staleness issue -> VOID, NEVER a comp-blast reach 'no'"


def test_run_failure_VOIDs_never_silent_no():
    def boom(q, to):
        raise RuntimeError("subprocess died")
    row = tp._run_blast_discrimination_probe(_probe(), runner=boom)
    assert row["effective"] == "unknown" and "run failed" in row["void_reason"]


def test_sovereign_held_query_REFUSED():
    row = tp._run_blast_discrimination_probe(_probe(query="gold:bd-49f-etf-ownership"), runner=lambda q, to: ("x", 0))
    assert row["effective"] == "unknown" and "SOVEREIGN" in row["void_reason"], \
        "a query targeting a held bd/49F node must be REFUSED (VOID), never run"


def test_isolation_answer_term_NOT_in_query():
    p = _probe()
    assert p["fixture"]["answer_term"] not in p["fixture"]["query"], \
        "isolation: the dependent term must NOT be in the query (else the query leaks its own answer)"
