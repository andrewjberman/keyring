"""NFRA_LIVELEARN CYCLE B batch -- the generic graph-reach discrimination runner (comp-trace / comp-xref).

CTO~D batch (2026-07-12): reach-based probes over the cli.py graph subcommands. Does a traversal REACH a
KNOWN dependent grounded from SOURCE? Graph-backed -> NOT-FOUND / ambiguity (void_markers) -> VOID (graph
coverage/staleness, NOT a reach miss); in-graph + reached -> yes / missed -> no. + sovereign held-guard +
isolation (the answer_term is NOT in cli_args).

Hermetic: injected runner (fake stdout/rc); no ~34s trace-graph build, no AWS, no bd.

# rail-checked: assurance oracle for the generic graph-reach runner (NFRA_LIVELEARN CYCLE B comp-trace/comp-xref)
Author: 0.8.0_AE_CloudComp.
"""
from __future__ import annotations

import importlib.util
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_WS = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(_HERE))))
_MODULE = os.path.join(_WS, "org", "modules", "graph", "compproof", "tool_probe.py")
_spec = importlib.util.spec_from_file_location("tool_probe_graphreach", _MODULE)
tp = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(tp)


def _probe(cli_args, term, void_markers=()):
    return {"probe_id": "comp-trace/upstream-reach-discrimination", "tool": "comp-trace",
            "tool_class": "dependency-path-trace", "kind": "graphreach-discrimination",
            "fixture": {"cli_args": cli_args, "answer_term": term, "void_markers": list(void_markers)},
            "usability_timeout_s": 150}


def _run(out, rc=0, cli_args=None, term="INF_A_00.accounts_dimension", void_markers=("Multiple matches for",)):
    p = _probe(cli_args or ["trace", "gold:INF_A_04.client_dimension", "--direction", "up", "--all"], term, void_markers)
    return tp._run_graphreach_discrimination_probe(p, runner=lambda a, to: (out, rc))


def test_reached_yes():
    out = "UPSTREAM trace from: gold:INF_A_04.client_dimension\n  <- [WRITES_S3] INF_A_00.accounts_dimension (GOLD_SCRIPT)\n"
    assert _run(out)["effective"] == "yes"


def test_in_graph_but_missed_no():
    out = "UPSTREAM trace from: gold:INF_A_04.client_dimension\n  <- [READS_S3] some/other/thing (S3_ARTIFACT)\n"  # lacks the producer
    assert _run(out)["effective"] == "no"


def test_NOT_FOUND_VOIDs():
    out = "NOT-FOUND: no graph node matches 'gold:INF_A_04.client_dimension'. This is a NOT-FOUND, not a 'nothing breaks' clear."
    row = _run(out)
    assert row["effective"] == "unknown" and "NOT-FOUND" in row["void_reason"]


def test_ambiguity_void_marker_VOIDs():
    out = "Multiple matches for 'gold:INF_A_04.client_dimension':\n  ... use --all"
    row = _run(out)
    assert row["effective"] == "unknown" and "Multiple matches" in row["void_reason"], \
        "an ambiguous match is a graph/naming issue -> VOID, not a reach 'no'"


def test_run_failure_VOIDs():
    def boom(a, to):
        raise RuntimeError("subprocess died")
    row = tp._run_graphreach_discrimination_probe(_probe(["trace", "x"], "INF_A_00.accounts_dimension"), runner=boom)
    assert row["effective"] == "unknown" and "run failed" in row["void_reason"]


def test_sovereign_held_query_REFUSED():
    row = _run("x", cli_args=["trace", "gold:bd-49f-etf"], term="INF_A_00.accounts_dimension")
    assert row["effective"] == "unknown" and "SOVEREIGN" in row["void_reason"]


def test_isolation_both_corpus_probes_term_not_in_cli_args():
    import importlib.util as _il
    tc_path = os.path.join(_WS, "org", "modules", "graph", "compproof", "tool_corpus.py")
    _s = _il.spec_from_file_location("tool_corpus_gr", tc_path)
    tc = _il.module_from_spec(_s)
    _s.loader.exec_module(tc)
    for pid in ("comp-trace/upstream-reach-discrimination", "comp-xref/symbol-reference-reach-discrimination"):
        p = next(pp for pp in tc.TOOL_PROBES if pp["probe_id"] == pid)
        argstr = " ".join(str(a) for a in p["fixture"]["cli_args"])
        assert p["fixture"]["answer_term"] not in argstr, \
            "isolation: %s answer_term must NOT be in cli_args (result-only)" % pid
