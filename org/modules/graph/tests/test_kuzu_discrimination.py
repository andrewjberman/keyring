"""NFRA_LIVELEARN CYCLE B tool-3 -- comp-kuzu QUERY-REACH discrimination probe (4-case runner).

CTO~D B2 + 4-case refinement (2026-07-12): score comp-kuzu's QUERY-REACH, SEPARATED from GLOBGRPH's
ingestion coverage. (1) edge confirmed-in-graph + targeted query FINDS it -> yes; (2) confirmed + MISSES
+ vintage current -> no (a REAL query-reach/dialect failure); (3) edge NOT ingested -> VOID (ingestion gap,
not the tool's fault); (4) BEHIND/UNKNOWN vintage + miss -> VOID. Plus the sovereign held-query guard +
isolation (the answer_term is NOT in the target query).

Hermetic: injected runner (fake stdout/stderr/rc); no live Kuzu DB, no AWS, no bd.

# rail-checked: assurance oracle for the comp-kuzu query-reach 4-case runner (NFRA_LIVELEARN CYCLE B tool-3)
Author: 0.8.0_AE_CloudComp.
"""
from __future__ import annotations

import importlib.util
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_WS = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(_HERE))))
_MODULE = os.path.join(_WS, "org", "modules", "graph", "compproof", "tool_probe.py")
_spec = importlib.util.spec_from_file_location("tool_probe_kuzu", _MODULE)
tp = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(tp)

_CONFIRM = ("MATCH (a:CloudNode)-[e:CloudEdge]->(b:CloudNode) WHERE a.name='inf-gold-layer-runner' "
            "AND b.name='opal-data-inf' AND e.edge_type='WRITES' RETURN b.name")
_TARGET = ("MATCH (a:CloudNode)-[e:CloudEdge]->(b:CloudNode) WHERE b.name='opal-data-inf' "
           "AND e.edge_type='WRITES' AND a.node_type='EC2_INSTANCE' RETURN a.name")


def _probe(confirm=_CONFIRM, target=_TARGET, term="inf-gold-layer-runner"):
    return {"probe_id": "comp-kuzu/cloud-estate-query-reach", "tool": "comp-kuzu",
            "tool_class": "cloud-estate-graph-query", "kind": "kuzu-discrimination",
            "fixture": {"confirm_query": confirm, "target_query": target,
                        "confirm_expect": "opal-data-inf", "answer_term": term},
            "usability_timeout_s": 150}


def _mk_runner(confirm_out, target_out, vintage="current", confirm_rc=0, target_rc=0):
    hdr = ("  Nessie HEAD: %s (pin == marker HEAD)\n" % vintage) if vintage in ("current", "behind") \
        else "  UNKNOWN VINTAGE -- freshness unverifiable\n"

    def run(q, to):
        if "a.name='inf-gold-layer-runner'" in q:      # the confirm query names the node
            return confirm_out, hdr, confirm_rc
        return target_out, hdr, target_rc              # the target query
    return run


def _run(runner):
    return tp._run_kuzu_discrimination_probe(_probe(), runner=runner)


def test_case1_confirmed_and_reached_YES():
    row = _run(_mk_runner("opal-data-inf\n(1 row)", "inf-gold-layer-runner\ninf-exporter\n(2 rows)", "current"))
    assert row["effective"] == "yes" and row["isolation_ok"] is True


def test_case2_confirmed_current_MISSED_no_real_query_reach_failure():
    # confirmed-in-graph BUT the targeted query lacks the term, vintage current -> a REAL comp-kuzu miss
    row = _run(_mk_runner("opal-data-inf\n(1 row)", "inf-exporter\n(1 row)", "current"))
    assert row["effective"] == "no"


def test_case3_NOT_ingested_VOIDs_ingestion_gap_not_a_miss():
    row = _run(_mk_runner("(0 rows)", "whatever", "current"))
    assert row["effective"] == "unknown" and "ingestion" in row["void_reason"].lower(), \
        "an un-ingested edge is a GLOBGRPH gap -> VOID, NEVER a comp-kuzu 'no'"


def test_case4_BEHIND_vintage_missed_VOIDs():
    row = _run(_mk_runner("opal-data-inf\n(1 row)", "inf-exporter\n(1 row)", "behind"))
    assert row["effective"] == "unknown" and "vintage" in row["void_reason"].lower()


def test_UNKNOWN_vintage_missed_VOIDs():
    row = _run(_mk_runner("opal-data-inf\n(1 row)", "inf-exporter\n(1 row)", "unknown"))
    assert row["effective"] == "unknown"


def test_confirm_query_rc_error_VOIDs():
    row = _run(_mk_runner("opal-data-inf", "x", "current", confirm_rc=1))
    assert row["effective"] == "unknown" and "unverifiable" in row["void_reason"].lower()


def test_sovereign_held_query_REFUSED():
    held = _probe(confirm="MATCH (a:CloudNode) WHERE a.name CONTAINS 'opal-data-bd' RETURN a.name")
    row = tp._run_kuzu_discrimination_probe(held, runner=_mk_runner("x", "y"))
    assert row["effective"] == "unknown" and "SOVEREIGN" in row["void_reason"], \
        "a query naming a held bd/schwab/49F target must be REFUSED (VOID), never run"


def test_isolation_answer_term_NOT_in_target_query():
    p = _probe()
    assert p["fixture"]["answer_term"] not in p["fixture"]["target_query"], \
        "isolation: the answer_term must NOT be in the target query (else the query leaks its own answer)"
