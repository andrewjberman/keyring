"""
Tests for comp-pipescript io gaps fixed in COMP_LEARNS.022.

Three gaps identified during gold chain DAG validation 2026-04-16:

  GAP 1 — FUNC-KEY write resolution:
    B_02 puts to canonical_lots_unrealized_key(date_str) / canonical_lots_realized_key(date_str).
    The put_object call spans multiple lines WITH args starting on the opening line
    (put_object(Bucket=..., Key=func(arg), ...)). Prior collapse heuristic required
    the opening paren to be the last char on the line; it missed this form.
    Result: B_02 WRITES was "(none detected)".

  GAP 2 — PREFIX-read vs FUNC-write cross-reference:
    A_03 writes positions_cube_key(date) → prefix gold/timeseries/positions_cube/.
    B_00 reads POSITIONS_CUBE_PREFIX = 'gold/timeseries/positions_cube/' (is_prefix=True).
    The tool saw both independently but did not emit the implicit dependency edge.
    Result: B_00 showed "(external/silver)" as the positions_cube provider.

  GAP 3 — Rolling-window prior-run read surfaced as circular dep:
    D_01 writes partner_analytics_key. Alias-collision `key = partner_analytics_key(gran)`
    → `key` matches unrelated get_object(Key=key) calls in other functions → tool
    classifies partner_analytics_key as BOTH read AND write for D_01. Surfaced as
    a bidirectional D_01 ↔ D_04 edge that looks like a circular dependency.
    Fix: emit ROLLING-WINDOW WARNING when a FUNC key appears in both reads and writes,
    without altering graph edges (D_04 stays as consumer in the writes section).

All tests below must:
  - FAIL against the pre-fix extract_pipeline.py (marked with # FAILS_BEFORE_FIX)
  - PASS against the post-fix extract_pipeline.py
"""

import sys
from pathlib import Path

import pytest

_WORKSPACE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(_WORKSPACE))

from org.modules.graph.extract_pipeline import build_pipeline_dag


@pytest.fixture(scope="module")
def dag():
    return build_pipeline_dag(_WORKSPACE)


# ---------------------------------------------------------------------------
# GAP 1: FUNC-KEY write detection (B_02)
# ---------------------------------------------------------------------------

class TestGap1FuncKeyWriteDetection:
    """B_02 put_object calls span multiple lines with args on the opening line.
    After the fix, canonical_lots_unrealized_key and canonical_lots_realized_key
    must appear in B_02's WRITES, not READS."""

    def test_b02_writes_canonical_lots_unrealized(self, dag):
        # FAILS_BEFORE_FIX: sio.writes was empty; keys defaulted to reads
        sio = dag.scripts.get('B_02')
        assert sio is not None, "B_02 not found in DAG"
        assert 'canonical_lots_unrealized_key' in sio.writes, (
            "canonical_lots_unrealized_key should be in B_02 WRITES "
            "(put_object(Bucket=S3_BUCKET, Key=canonical_lots_unrealized_key(date_str), ...) "
            "was not collapsed by the multiline heuristic)"
        )

    def test_b02_writes_canonical_lots_realized(self, dag):
        # FAILS_BEFORE_FIX: sio.writes was empty; keys defaulted to reads
        sio = dag.scripts.get('B_02')
        assert sio is not None, "B_02 not found in DAG"
        assert 'canonical_lots_realized_key' in sio.writes, (
            "canonical_lots_realized_key should be in B_02 WRITES"
        )

    def test_b02_does_not_read_canonical_lots_keys(self, dag):
        # FAILS_BEFORE_FIX: both keys were in reads (unknown → defaulted read)
        sio = dag.scripts.get('B_02')
        assert sio is not None
        assert 'canonical_lots_unrealized_key' not in sio.reads, (
            "canonical_lots_unrealized_key should not appear in B_02 READS"
        )
        assert 'canonical_lots_realized_key' not in sio.reads, (
            "canonical_lots_realized_key should not appear in B_02 READS"
        )

    def test_b02_write_keys_contain_canonical_lots_paths(self, dag):
        # FAILS_BEFORE_FIX: write_keys was empty
        sio = dag.scripts.get('B_02')
        assert sio is not None
        unrealized_path = 'gold/canonical/lots_unrealized/{*}.parquet'
        realized_path = 'gold/canonical/lots_realized/{*}.parquet'
        assert unrealized_path in sio.write_keys, (
            f"Expected {unrealized_path!r} in B_02 write_keys"
        )
        assert realized_path in sio.write_keys, (
            f"Expected {realized_path!r} in B_02 write_keys"
        )


# ---------------------------------------------------------------------------
# GAP 2: PREFIX-read vs FUNC-write cross-reference (B_00 + A_03, B_03 + B_02)
# ---------------------------------------------------------------------------

class TestGap2PrefixReadFuncWriteCrossRef:
    """After the fix, the DAG's _implicit_writers index must link:
      - A_03 (writes positions_cube_key → gold/timeseries/positions_cube/{*}) →
        B_00 (reads POSITIONS_CUBE_PREFIX → gold/timeseries/positions_cube/)
      - B_02 (writes canonical_lots_unrealized_key → gold/canonical/lots_unrealized/{*}) →
        B_03 (reads CANONICAL_LOTS_UNREALIZED_PREFIX → gold/canonical/lots_unrealized/)
    These edges are tagged as IMPLICIT (via FUNC-key) and do not appear in _writers."""

    def test_implicit_writers_index_built(self, dag):
        # FAILS_BEFORE_FIX: _implicit_writers did not exist
        assert hasattr(dag, '_implicit_writers'), (
            "PipelineDAG must have _implicit_writers index after build_index()"
        )
        assert isinstance(dag._implicit_writers, dict)

    def test_a03_is_implicit_writer_of_positions_cube_prefix(self, dag):
        # FAILS_BEFORE_FIX: _implicit_writers was empty / missing
        prefix = 'gold/timeseries/positions_cube/'
        implicit = dag._implicit_writers.get(prefix, [])
        assert 'A_03' in implicit, (
            f"A_03 should appear as implicit writer of prefix {prefix!r} "
            f"(A_03 writes positions_cube_key whose template starts with this prefix). "
            f"Got: {implicit}"
        )

    def test_b02_is_implicit_writer_of_canonical_lots_unrealized_prefix(self, dag):
        # FAILS_BEFORE_FIX: B_02 had no writes; _implicit_writers was empty
        prefix = 'gold/canonical/lots_unrealized/'
        implicit = dag._implicit_writers.get(prefix, [])
        assert 'B_02' in implicit, (
            f"B_02 should appear as implicit writer of prefix {prefix!r}. Got: {implicit}"
        )

    def test_b02_is_implicit_writer_of_canonical_lots_realized_prefix(self, dag):
        # FAILS_BEFORE_FIX: B_02 had no writes; _implicit_writers was empty
        prefix = 'gold/canonical/lots_realized/'
        implicit = dag._implicit_writers.get(prefix, [])
        assert 'B_02' in implicit, (
            f"B_02 should appear as implicit writer of prefix {prefix!r}. Got: {implicit}"
        )

    def test_b00_reads_positions_cube_prefix(self, dag):
        sio = dag.scripts.get('B_00')
        assert sio is not None
        assert 'POSITIONS_CUBE_PREFIX' in sio.reads, (
            "B_00 must import and read POSITIONS_CUBE_PREFIX from s3_layout"
        )

    def test_b03_reads_canonical_lots_unrealized_prefix(self, dag):
        sio = dag.scripts.get('B_03')
        assert sio is not None
        assert 'CANONICAL_LOTS_UNREALIZED_PREFIX' in sio.reads, (
            "B_03 must import and read CANONICAL_LOTS_UNREALIZED_PREFIX from s3_layout"
        )

    def test_implicit_writers_do_not_appear_in_direct_writers(self, dag):
        # Implicit edges must be kept separate from direct _writers to preserve
        # the semantic distinction between declared dependencies and inferred ones.
        prefix = 'gold/timeseries/positions_cube/'
        direct = dag._writers.get(prefix, [])
        assert 'A_03' not in direct, (
            "A_03 should only be in _implicit_writers for the prefix, not _writers. "
            "Direct _writers uses the FUNC template path, not the prefix."
        )


# ---------------------------------------------------------------------------
# GAP 3: Rolling-window warning (D_01 + partner_analytics_key)
# ---------------------------------------------------------------------------

class TestGap3RollingWindowDetection:
    """D_01 writes partner_analytics_key and, due to alias collision, the tool
    also classifies it as a read. After the fix, D_01.rolling_window_candidates
    must flag partner_analytics_key, and the WRITES consumer chain (-> D_04)
    must remain intact."""

    def test_d01_has_rolling_window_candidates(self, dag):
        # FAILS_BEFORE_FIX: rolling_window_candidates field did not exist
        sio = dag.scripts.get('D_01')
        assert sio is not None
        assert hasattr(sio, 'rolling_window_candidates'), (
            "ScriptIO must have rolling_window_candidates field"
        )
        assert len(sio.rolling_window_candidates) > 0, (
            "D_01 should have at least one rolling-window candidate "
            "(partner_analytics_key appears in both reads and writes due to alias collision)"
        )

    def test_d01_partner_analytics_key_is_rolling_window_candidate(self, dag):
        # FAILS_BEFORE_FIX: field did not exist / was empty
        sio = dag.scripts.get('D_01')
        assert sio is not None
        assert 'partner_analytics_key' in sio.rolling_window_candidates, (
            "partner_analytics_key must be flagged as rolling-window candidate for D_01. "
            "It appears in both reads (via alias collision) and writes (genuine write "
            "in write_s3 function). The tool should warn rather than silently surface "
            "a D_01 <-> D_04 bidirectional edge."
        )

    def test_d01_writes_partner_analytics_key(self, dag):
        sio = dag.scripts.get('D_01')
        assert sio is not None
        assert 'partner_analytics_key' in sio.writes, (
            "D_01 genuinely writes partner_analytics_key — this must remain in writes"
        )

    def test_d04_remains_consumer_of_d01_partner_analytics(self, dag):
        # The rolling-window warning must NOT break the consumer chain.
        # D_04 reads partner_analytics_key from D_01 — this is a real dependency.
        # FAILS_BEFORE_FIX (regression guard): if rolling-window detection removes
        # D_04 from _readers, D_01's write would show no consumers.
        partner_analytics_path = dag.s3_keys.get('partner_analytics_key')
        assert partner_analytics_path is not None
        key_path = partner_analytics_path.s3_path
        readers = dag._readers.get(key_path, [])
        assert 'D_04' in readers, (
            f"D_04 must remain in _readers[{key_path!r}] after the rolling-window fix. "
            "The fix must be display-only — do not remove genuine readers from the index."
        )

    def test_sciptio_rolling_window_candidates_field_exists_on_all_scripts(self, dag):
        for sid, sio in dag.scripts.items():
            assert hasattr(sio, 'rolling_window_candidates'), (
                f"ScriptIO for {sid} is missing rolling_window_candidates field"
            )
            assert isinstance(sio.rolling_window_candidates, list)
