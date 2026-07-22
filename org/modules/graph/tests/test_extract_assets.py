"""Tests for extract_assets -- bundle item 5 (comp-blast monolith silver NOT-FOUND).

The spec is the CLASS (name-grain silver artifact nodes, live-derived edges); the
S4-contract tables are TEST CASES of it (CTO 213649Z: "the six silver artifacts
become test cases rather than the spec").
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

WS = Path(__file__).resolve().parents[4]
if str(WS) not in sys.path:
    sys.path.insert(0, str(WS))

from org.modules.graph.trace_graph import TraceGraph  # noqa: E402
from org.modules.graph.extract_assets import (  # noqa: E402
    _NOT_TABLES,
    _SILVER_NODE_PREFIX,
    _fact_names_in_strings,
    inject_assets_silver_artifacts,
)


def _built_graph() -> TraceGraph:
    g = TraceGraph(built_at=time.time())
    added = inject_assets_silver_artifacts(g, WS)
    assert added > 0, "the pass added zero edges against the live workspace"
    return g


GRAPH = _built_graph()

# Every silver table DS's 3F-S4 contract (@4d58357d5) SS3 maps a gold consumer
# onto. These are CASES of the name-grain class, not an enumeration the code knows
# about. fact_rps (s1 positions) is deliberately NOT here: SS3 maps no gold read of
# it (the 49F AUA read is fact_rps_s2) -- it is asserted producer-side below.
S4_CONTRACT_TABLES = [
    "fact_rps_s2",
    "fact_assets",
    "fact_holdings",
    "fact_portfolios_full",
    "fact_model_aum_daily",
    "fact_model_allocation_roster",
    "fact_allocation_valuation",
    "fact_model_roster",
    "fact_model_blend",
    "fact_model_assignment",
]


def test_s4_contract_tables_all_minted():
    missing = [t for t in S4_CONTRACT_TABLES
               if _SILVER_NODE_PREFIX + t not in GRAPH.nodes]
    assert not missing, f"S4-contract tables absent from graph: {missing}"


def test_s4_contract_tables_all_have_a_consumer_edge():
    # DS SS3 maps a gold read for every one of these -- so every node must carry
    # at least one READS_S3 edge into a gold script.
    orphans = []
    for t in S4_CONTRACT_TABLES:
        nid = _SILVER_NODE_PREFIX + t
        has_read = any(e.source == nid and e.edge_type == "READS_S3"
                       for e in GRAPH.edges)
        if not has_read:
            orphans.append(t)
    assert not orphans, f"S4-mapped tables with zero consumer edges: {orphans}"


def test_fact_rps_minted_with_producer_edge_only():
    # Producer-side coverage: fact_rps exists in the coupling surface (the schwab
    # converter emits it) even though no MDPF gold consumer reads it (S4 SS3).
    nid = _SILVER_NODE_PREFIX + "fact_rps"
    assert nid in GRAPH.nodes, "fact_rps not minted from producer literals"
    assert any(e.target == nid and e.edge_type == "WRITES_S3"
               for e in GRAPH.edges), "fact_rps has no producer edge"


def test_producer_edge_blackdiamond_writes_model_roster():
    # rebalancer_conversion.py (vendored under opal-assets-silver-blackdiamond)
    # declares silver/fact_model_roster in its header.
    assert any(
        e.source == "lambda:opal-assets-silver-blackdiamond"
        and e.target == _SILVER_NODE_PREFIX + "fact_model_roster"
        and e.edge_type == "WRITES_S3"
        for e in GRAPH.edges
    ), "producer edge lambda:opal-assets-silver-blackdiamond -> fact_model_roster missing"


def test_consumer_edge_build_dim_model_portfolio_reads_assignment():
    # build_dim_model_portfolio.py:350 reads fact_model_assignment (S4 SS3 row).
    assert any(
        e.source == _SILVER_NODE_PREFIX + "fact_model_assignment"
        and e.target == "gold:build_dim_model_portfolio"
        and e.edge_type == "READS_S3"
        for e in GRAPH.edges
    ), "consumer edge fact_model_assignment -> build_dim_model_portfolio missing"


def test_negative_control_no_hallucinated_table():
    # A name no source file carries must NOT exist. If this fails, the extractor
    # is minting from something other than the estate's own literals.
    assert _SILVER_NODE_PREFIX + "fact_zzz_definitely_not_a_table" not in GRAPH.nodes


def test_denylist_fact_rows_is_not_a_table():
    # fact_rows is the conversion-manifest parity FIELD (conversion_manifest.py),
    # not a silver table. The denylist must hold or blast grows a phantom node
    # that every manifest-touching commit appears to hit.
    assert "fact_rows" in _NOT_TABLES
    assert _SILVER_NODE_PREFIX + "fact_rows" not in GRAPH.nodes


def test_extractor_positive_control(tmp_path):
    # The instrument itself, exercised in isolation: a string literal IS found; a
    # comment and a bare identifier are NOT. An extractor that cannot detect its
    # own condition is the instrument-that-cannot-fail class.
    probe = tmp_path / "probe.py"
    probe.write_text(
        '# comment mentions fact_comment_only\n'
        'fact_identifier_only = 1\n'
        'd = {"fact_dict_key_prose": None}\n'          # bare whole-string: REJECT
        'x = "docstring prose mentions fact_prose_only here"\n'
        'A = silver_table(s3, "fact_call_arg", d)\n'   # form B
        'PATH = "blackdiamond/cottonwood/silver/fact_path_literal/"\n'  # form A
        'F = f_prefix + "/fact_fstring_frag"\n'        # form A (leading slash)
        'DOC = "outputs -> fact_arrow_decl (same scope)"\n'             # form D
        'ENUM = "ruled names (fact_enum_a, fact_enum_b, fact_enum_c...)"\n'  # form C
        'PREFIX = "fact_concat_fragment_" + "suffix"\n',
        encoding="utf-8",
    )
    names = _fact_names_in_strings(probe)
    # Accepted: one per usage form. Rejected: prose mention, bare dict key,
    # comment, identifier, and the trailing-underscore concatenation fragment
    # (dropped WHOLE, not backtracked into a shorter phantom -- live instance:
    # "fact_model_"). Bare whole-string rejection is the FALSE-PRESENCE lock:
    # the first cut minted a node from a docstring that said a table was NEVER
    # DECLARED (etf_schemas.py:17).
    assert names == {"fact_call_arg", "fact_path_literal", "fact_fstring_frag",
                     "fact_arrow_decl", "fact_enum_a", "fact_enum_b",
                     "fact_enum_c"}, names


def test_downstream_fanin_emits_each_node_once():
    # Pre-existing walk defect surfaced by this pass (2026-07-22): a node reachable
    # via N same-frontier paths was emitted N times, so blast rendered duplicate
    # rows and "affects >= N" over-counted. Diamond graph: a->b->d, a->c->d.
    from org.modules.graph.trace_graph import Edge, Node

    g = TraceGraph(built_at=time.time())
    for nid in ("a", "b", "c", "d"):
        g.add_node(Node(id=nid, node_type="GOLD_SCRIPT", label=nid))
    for s, t in (("a", "b"), ("a", "c"), ("b", "d"), ("c", "d")):
        g.add_edge(Edge(source=s, target=t, edge_type="TRIGGERS"))
    down_ids = [n.id for n, _, _ in g.downstream("a")]
    assert sorted(down_ids) == ["b", "c", "d"], down_ids
    up_ids = [n.id for n, _, _ in g.upstream("d")]
    assert sorted(up_ids) == ["a", "b", "c"], up_ids


def test_extractor_unparseable_file_is_empty_not_fatal(tmp_path):
    broken = tmp_path / "broken.py"
    broken.write_text("def broken(:\n", encoding="utf-8")
    assert _fact_names_in_strings(broken) == set()
