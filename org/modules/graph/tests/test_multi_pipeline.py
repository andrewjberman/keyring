"""
Tests for ADHC_COMPIL.001 — multi-pipeline indexing extension.

Five gaps that existed before this extension:

  TEST 1 — INF gold script io + READS/WRITES:
    build_inf_gold_dag didn't exist. comp-pipescript io against any INF gold script
    (e.g. D_04.client_portal_summary.py) returned nothing.

  TEST 2 — BD silver script io:
    build_silver_dag didn't exist. BD silver scripts had no io manifest.

  TEST 3 — INF silver script io:
    build_silver_dag didn't exist. INF silver scripts had no io manifest.

  TEST 4 — Cross-pipeline reader index:
    build_multi_pipeline_dag didn't exist. INF gold consumers of silver artifacts
    could not be enumerated in a unified cross-pipeline context.

  TEST 5 — Pipeline labeling:
    ScriptIO had no `pipeline` field. BD gold output was unlabeled; cross-pipeline
    blast analysis required manual pipeline identification.

All tests below must:
  - FAIL against the pre-extension extract_pipeline.py (marked # FAILS_BEFORE_FIX)
  - PASS against the post-extension extract_pipeline.py
"""

import sys
from pathlib import Path

import pytest

_WORKSPACE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(_WORKSPACE))

# FAILS_BEFORE_FIX: these three names didn't exist before ADHC_COMPIL.001
from org.modules.graph.extract_pipeline import (  # noqa: E402
    build_pipeline_dag,
    build_inf_gold_dag,
    build_silver_dag,
    build_multi_pipeline_dag,
    _parse_orion_dispatch,
)


@pytest.fixture(scope="module")
def bd_gold_dag():
    return build_pipeline_dag(_WORKSPACE)


@pytest.fixture(scope="module")
def inf_gold_dag():
    return build_inf_gold_dag(_WORKSPACE)


@pytest.fixture(scope="module")
def bd_silver_dag():
    return build_silver_dag(_WORKSPACE, "bd-silver", "data/black_diamond/scripts/silver")


@pytest.fixture(scope="module")
def inf_silver_dag():
    return build_silver_dag(_WORKSPACE, "inf-silver", "data/inf/scripts/silver")


@pytest.fixture(scope="module")
def multi_dag():
    return build_multi_pipeline_dag(_WORKSPACE)


# ---------------------------------------------------------------------------
# TEST 1: INF gold script io + READS/WRITES (D_04)
# ---------------------------------------------------------------------------

class TestInfGoldScriptIO:
    """D_04.client_portal_summary.py must be indexed by build_inf_gold_dag with
    correct pipeline label, reads (gold/ + silver/ precursors), and writes
    (platinum/firm/ portal artifacts)."""

    def test_d04_present_in_inf_gold_dag(self, inf_gold_dag):
        # FAILS_BEFORE_FIX: build_inf_gold_dag raised ImportError
        assert 'INF_D_04' in inf_gold_dag.scripts, (
            "INF_D_04 not indexed in INF gold DAG. "
            "Expected INF_D_04.client_portal_summary.py to be discovered from orion-gold-dispatch.sh catalog "
            "(the catalog id is INF_D_04 -- the whole inf chain is INF_-prefixed; bd's is bare D_04)."
        )

    def test_d04_pipeline_label(self, inf_gold_dag):
        # FAILS_BEFORE_FIX: build_inf_gold_dag raised ImportError
        sio = inf_gold_dag.scripts['INF_D_04']
        assert sio.pipeline == 'inf-gold', (
            f"D_04 pipeline label should be 'inf-gold', got '{sio.pipeline}'"
        )

    def test_d04_reads_firm_mix_views(self, inf_gold_dag):
        # FAILS_BEFORE_FIX: build_inf_gold_dag raised ImportError
        sio = inf_gold_dag.scripts['INF_D_04']
        assert 'gold/artifacts/firm_mix_views.json' in sio.read_keys, (
            "D_04 should READ gold/artifacts/firm_mix_views.json "
            "(FIRM_MIX_VIEWS_KEY used in s3.get_object(Key=FIRM_MIX_VIEWS_KEY))."
        )

    def test_d04_reads_silver_accounts_dim(self, inf_gold_dag):
        # FAILS_BEFORE_FIX: build_inf_gold_dag raised ImportError
        sio = inf_gold_dag.scripts['INF_D_04']
        assert 'silver/accounts_dim/latest.parquet' in sio.read_keys, (
            "D_04 should READ silver/accounts_dim/latest.parquet "
            "(SILVER_ACCOUNTS_DIM used in _read_s3_parquet(SILVER_ACCOUNTS_DIM))."
        )

    def test_d04_writes_platinum_timeseries(self, inf_gold_dag):
        # FAILS_BEFORE_FIX: build_inf_gold_dag raised ImportError
        sio = inf_gold_dag.scripts['INF_D_04']
        assert 'platinum/firm/timeseries_overview.json' in sio.write_keys, (
            "D_04 should WRITE platinum/firm/timeseries_overview.json "
            "(_write_json_s3(overview, 'platinum/firm/timeseries_overview.json'))."
        )

    def test_d04_writes_gold_artifacts_header_metrics(self, inf_gold_dag):
        # FAILS_BEFORE_FIX: build_inf_gold_dag raised ImportError
        sio = inf_gold_dag.scripts['INF_D_04']
        assert 'gold/artifacts/summary/header_metrics.json' in sio.write_keys, (
            "D_04 should WRITE gold/artifacts/summary/header_metrics.json "
            "(_write_json_s3(header, GOLD_ARTIFACTS_HEADER_METRICS_KEY))."
        )


# ---------------------------------------------------------------------------
# TEST 2: BD silver script io (convert_assets_to_silver)
# ---------------------------------------------------------------------------

class TestBdSilverScriptIO:
    """convert_assets_to_silver.py must be indexed by build_silver_dag as [bd-silver]
    and its compacted parquet write must be detected."""

    def test_convert_assets_present(self, bd_silver_dag):
        # FAILS_BEFORE_FIX: build_silver_dag raised ImportError
        assert 'convert_assets_to_silver' in bd_silver_dag.scripts, (
            "convert_assets_to_silver not found in bd-silver DAG."
        )

    def test_pipeline_label_bd_silver(self, bd_silver_dag):
        # FAILS_BEFORE_FIX: build_silver_dag raised ImportError
        sio = bd_silver_dag.scripts['convert_assets_to_silver']
        assert sio.pipeline == 'bd-silver', (
            f"Expected 'bd-silver', got '{sio.pipeline}'"
        )

    def test_writes_compacted_parquet(self, bd_silver_dag):
        # FAILS_BEFORE_FIX: build_silver_dag raised ImportError
        sio = bd_silver_dag.scripts['convert_assets_to_silver']
        assert 'silver/bd_assets.parquet' in sio.write_keys, (
            "convert_assets_to_silver should WRITE silver/bd_assets.parquet "
            "(COMPACTED_KEY used in s3.put_object(Key=COMPACTED_KEY, ...))."
        )


# ---------------------------------------------------------------------------
# TEST 3: INF silver script io (convert_orion_to_silver)
# ---------------------------------------------------------------------------

class TestInfSilverScriptIO:
    """convert_orion_to_silver.py must be indexed by build_silver_dag as [inf-silver]
    with watermark read and gap_manifest write detected."""

    def test_convert_orion_present(self, inf_silver_dag):
        # FAILS_BEFORE_FIX: build_silver_dag raised ImportError
        assert 'convert_orion_to_silver' in inf_silver_dag.scripts, (
            "convert_orion_to_silver not found in inf-silver DAG."
        )

    def test_pipeline_label_inf_silver(self, inf_silver_dag):
        # FAILS_BEFORE_FIX: build_silver_dag raised ImportError
        sio = inf_silver_dag.scripts['convert_orion_to_silver']
        assert sio.pipeline == 'inf-silver', (
            f"Expected 'inf-silver', got '{sio.pipeline}'"
        )

    def test_reads_watermark(self, inf_silver_dag):
        # FAILS_BEFORE_FIX: build_silver_dag raised ImportError
        sio = inf_silver_dag.scripts['convert_orion_to_silver']
        assert 'silver/meta/trn_watermark.json' in sio.read_keys, (
            "convert_orion_to_silver should READ silver/meta/trn_watermark.json "
            "(_s3.get_object(Key=WATERMARK_KEY) at _read_watermark())."
        )

    def test_writes_gap_manifest(self, inf_silver_dag):
        # FAILS_BEFORE_FIX: build_silver_dag raised ImportError
        sio = inf_silver_dag.scripts['convert_orion_to_silver']
        assert 'silver/meta/gap_manifest.json' in sio.write_keys, (
            "convert_orion_to_silver should WRITE silver/meta/gap_manifest.json "
            "(_s3.put_object(Key=SILVER_META_KEY, ...) in write_gap_manifest())."
        )


# ---------------------------------------------------------------------------
# TEST 4: Cross-pipeline reader index
# ---------------------------------------------------------------------------

class TestCrossPipelineEdge:
    """The multi-pipeline DAG must unify all pipeline namespaces so that a gold
    consumer's silver read is visible in the cross-pipeline _readers index.
    This tests the foundation required for nested-key reverse lookup (ADHC_COMPIL.005)."""

    def test_inf_gold_d04_in_multi_dag(self, multi_dag):
        # FAILS_BEFORE_FIX: build_multi_pipeline_dag raised ImportError
        assert 'inf-gold:INF_D_04' in multi_dag.scripts, (
            "'inf-gold:INF_D_04' missing from multi-pipeline DAG. "
            "INF gold scripts must be namespaced as inf-gold:<script_id>."
        )

    def test_inf_silver_in_multi_dag(self, multi_dag):
        # FAILS_BEFORE_FIX: build_multi_pipeline_dag raised ImportError
        assert 'inf-silver:convert_orion_to_silver' in multi_dag.scripts, (
            "'inf-silver:convert_orion_to_silver' missing from multi-pipeline DAG."
        )

    def test_silver_accounts_dim_has_inf_gold_consumer(self, multi_dag):
        # FAILS_BEFORE_FIX: build_multi_pipeline_dag raised ImportError
        # D_04 reads silver/accounts_dim/latest.parquet from the silver layer.
        # The multi-pipeline _readers index must contain 'inf-gold:INF_D_04' for this key,
        # establishing the cross-layer (silver -> gold) consumer relationship.
        readers = multi_dag._readers.get('silver/accounts_dim/latest.parquet', [])
        assert 'inf-gold:INF_D_04' in readers, (
            "The multi-pipeline _readers index should contain 'inf-gold:INF_D_04' for "
            "'silver/accounts_dim/latest.parquet'. D_04 reads SILVER_ACCOUNTS_DIM via "
            "_read_s3_parquet(SILVER_ACCOUNTS_DIM). "
            f"Actual readers: {readers}"
        )

    def test_multi_dag_has_scripts_from_all_four_pipelines(self, multi_dag):
        # FAILS_BEFORE_FIX: build_multi_pipeline_dag raised ImportError
        present_pipelines = {sio.pipeline for sio in multi_dag.scripts.values()}
        for expected in ('bd-gold', 'inf-gold', 'bd-silver', 'inf-silver'):
            assert expected in present_pipelines, (
                f"Pipeline '{expected}' has no scripts in the multi-pipeline DAG."
            )


# ---------------------------------------------------------------------------
# TEST 5: Pipeline labeling correctness
# ---------------------------------------------------------------------------

class TestPipelineLabeling:
    """Every script must carry an explicit pipeline label so that cross-pipeline
    blast analysis can identify impact boundaries."""

    def test_bd_gold_script_carries_bd_gold_label(self, bd_gold_dag):
        # FAILS_BEFORE_FIX: ScriptIO had no `pipeline` field (AttributeError)
        sio = bd_gold_dag.scripts.get('D_04')
        assert sio is not None, "D_04 not found in BD gold DAG"
        assert sio.pipeline == 'bd-gold', (
            f"BD gold D_04 should have pipeline='bd-gold', got '{sio.pipeline}'. "
            "Pipeline label is required for cross-pipeline blast analysis."
        )

    def test_all_bd_gold_scripts_have_bd_gold_label(self, bd_gold_dag):
        # FAILS_BEFORE_FIX: ScriptIO had no `pipeline` field (AttributeError)
        unlabeled = [
            sid for sid, sio in bd_gold_dag.scripts.items()
            if sio.pipeline != 'bd-gold'
        ]
        assert not unlabeled, (
            f"These BD gold scripts have wrong pipeline label: {unlabeled}"
        )

    def test_namespaced_ids_in_multi_dag(self, multi_dag):
        # FAILS_BEFORE_FIX: build_multi_pipeline_dag raised ImportError
        assert 'bd-gold:D_04' in multi_dag.scripts, (
            "BD gold D_04 should appear as 'bd-gold:D_04' in multi-pipeline DAG"
        )
        assert 'inf-gold:INF_D_04' in multi_dag.scripts, (
            "INF gold client_portal_summary should appear as 'inf-gold:INF_D_04' in multi-pipeline DAG. "
            "BD's catalog id is bare D_04, INF's is INF_D_04 (the inf chain is INF_-prefixed); the "
            "pipeline namespace (bd-gold:/inf-gold:) prevents collisions for any genuinely-shared id."
        )
        assert 'bd-silver:convert_assets_to_silver' in multi_dag.scripts, (
            "BD silver script should appear as 'bd-silver:convert_assets_to_silver'"
        )


# ---------------------------------------------------------------------------
# TEST 6: ORPHAN-SHADOW SENTINEL (build_inf_gold_dag normalization hardening)
# ---------------------------------------------------------------------------

def _inf_gold_orphan_shadows():
    """Return the inf gold tree's orphan-shadow set: on-disk *.py files that are
    NOT in the dispatch catalog but whose INF_-prefixed twin IS cataloged.

    SAFETY (carry these, they are real constraints):
      * PATH-ANCHORED to data/inf/scripts/gold ONLY. The bare names (A_*/B_*/C_*/
        D_00c/D_02/...) are LIVE CANONICAL producers in the bd + cot gold trees --
        a cross-tree bare-name glob would falsely flag (and risk deleting) live
        bd/cot scripts. We compare each tree against ITS OWN dispatch catalog.
      * DISPATCH-PINNED, not glob-discovered. A file is a shadow only when its
        INF_<name> twin is an authoritative catalog entry (provably the live
        producer). Files with no cataloged twin (I_D00*/valgate_*/run_c_chain +
        INF_run_c_chain -- both non-cataloged runner helpers) are NOT flagged;
        they need their own investigation, not auto-deletion.

    The orphan-shadow set is dead code left by the inf gold tree's bd-style fork
    (bare names) -> INF_-prefixed re-creation (the live chain). D_04 was the first
    one surfaced (the 9-RED); the sentinel guards the whole class going forward.
    """
    import glob
    import os
    gold_dir = _WORKSPACE / "data" / "inf" / "scripts" / "gold"
    _, _, catalog = _parse_orion_dispatch(gold_dir)
    catfiles = set(catalog.values())  # live cataloged filenames (INF_-prefixed)
    disk = {os.path.basename(p) for p in glob.glob(str(gold_dir / "*.py"))}
    return sorted(f for f in disk if f not in catfiles and ("INF_" + f) in catfiles)


class TestInfGoldOrphanShadowSentinel:
    """No bare-named gold .py may shadow a cataloged INF_-prefixed producer.

    Structural guard for the build_inf_gold_dag normalization: had it existed, it
    would have caught all 24 orphan-shadows at once instead of one (D_04) via a
    failing io test. Born green only after the inf bare-shadow set is removed."""

    def test_no_orphan_shadows_in_inf_gold(self):
        shadows = _inf_gold_orphan_shadows()
        assert not shadows, (
            f"{len(shadows)} orphan-shadow gold script(s) in data/inf/scripts/gold/ "
            f"shadow a cataloged INF_ producer (dead code from the bd-style fork -> "
            f"INF_-prefix re-creation). Remove the data/inf copies ONLY (bare names are "
            f"live in bd/cot): {shadows}"
        )
