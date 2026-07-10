"""NFRA_TOOLPASS sovereign chokepoint (design-b, CTO ruling 20260710T221551Z): the trace-graph
INDEXER must MINT a node for a held-path file (bd/49F/schwab) but NEVER read its CONTENT
(no read_text / ast.parse / source_sha). This test is the PRE-COMMIT proof, run on a SYNTHETIC
FIXTURE (never a live bd read):

  - build the bd-reading extractors over a scratch repo containing held-path files + a non-held control
  - instrument the two content-read primitives (Path.read_text + trace_graph._compute_file_sha) to
    RECORD every held-path read
  - assert: held nodes EXIST (reachability preserved) with NO source_sha, and ZERO held-path reads
  - MUTATION arm: force the exclusion OFF -> held-path reads reappear (the test goes RED) -> non-vacuous

# rail-checked: assurance oracle for the trace-graph indexer under test (NFRA_TOOLPASS sec.6)

Author: 3.0.0_SA_CVO~B. Deterministic; touches only a tempdir; reads no real bd.
"""

import os
import shutil
import sys
import tempfile
from pathlib import Path

_HERE = os.path.dirname(os.path.abspath(__file__))
_WS = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(_HERE))))
for _p in (_WS, os.path.dirname(os.path.dirname(_HERE))):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import org.modules.graph.trace_graph as tg  # noqa: E402
from org.modules.graph import extract_s3, extract_pipeline  # noqa: E402


def _mk_fixture() -> Path:
    root = Path(tempfile.mkdtemp(prefix="bd_excl_"))

    def w(rel, content):
        p = root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")

    # HELD (bd) -- would be read for S3 keys / functions / sha if the chokepoint failed.
    w("data/black_diamond/scripts/gold/A_00.accounts_dimension.py",
      "import lib.s3_layout\nGOLD = 's3://opal-data-bd/gold/x.parquet'\ndef build_x():\n    return 1\n")
    w("data/black_diamond/scripts/gold/lib/s3_layout.py",
      "ACCOUNTS = 's3://opal-data-bd/gold/accounts.parquet'\n")
    w("data/black_diamond/scripts/gold/gold_dispatch.sh",
      'python3 "$SCRIPTS/A_00.accounts_dimension.py"\n')
    w("data/black_diamond/scripts/silver/build_silver.py",
      "Y = 's3://opal-data-bd/silver/y.parquet'\n")
    # NON-HELD control (inf) -- SHOULD be read (proves the gate discriminates, not blanket-skips).
    w("data/inf/scripts/gold/INF_00.control.py",
      "OUT = 's3://opal-data-inf/gold/z.parquet'\ndef main():\n    return 2\n")
    return root


def _run(exclusion_on: bool):
    """Run the bd-reading extractors over the fixture; return (graph, held_reads)."""
    root = _mk_fixture()
    held_reads = []

    orig_rt = Path.read_text
    orig_sha = tg._compute_file_sha
    orig_hit = tg._held_path_hit

    def _is_held(s):
        return any(m in s for m in tg._HELD_PATH_MARKERS)

    def rt(self, *a, **k):
        s = str(self).replace("\\", "/")
        if _is_held(s):
            held_reads.append(("read_text", s))
        return orig_rt(self, *a, **k)

    def sha(p):
        s = str(p).replace("\\", "/")
        if _is_held(s):
            held_reads.append(("sha", s))
        return orig_sha(p)

    Path.read_text = rt
    tg._compute_file_sha = sha
    if not exclusion_on:
        tg._held_path_hit = lambda _p: False   # MUTATION: disable the chokepoint

    try:
        g = tg.TraceGraph()
        extract_s3.extract_s3_edges(g, root)
        for dag_fn in (
            lambda: extract_pipeline.build_pipeline_dag(root),
            lambda: extract_pipeline.build_silver_dag(root, "bd-silver", "data/black_diamond/scripts/silver"),
            lambda: extract_pipeline.parse_gold_direct_invoke(root),
        ):
            try:
                dag_fn()
            except Exception:
                pass
    finally:
        Path.read_text = orig_rt
        tg._compute_file_sha = orig_sha
        tg._held_path_hit = orig_hit
        shutil.rmtree(root, ignore_errors=True)
    return g, held_reads


def test_indexer_never_reads_held_content():
    g, held_reads = _run(exclusion_on=True)
    # held node minted (reachability), but NO source_sha (content never read for a sha)
    bd_nodes = [n for n in g.nodes.values() if tg._held_path_hit(n.file_path)]
    assert bd_nodes, "expected the held bd node to be MINTED (metadata-only), not dropped"
    assert all(not n.source_sha for n in bd_nodes), \
        "a held node must carry NO source_sha (its content must never be read)"
    # THE proof: zero held-path content reads during the build
    assert held_reads == [], f"held-path CONTENT was read: {held_reads}"


def test_mutation_off_reintroduces_the_read():
    _g, held_reads = _run(exclusion_on=False)
    assert held_reads, "MUTATION (exclusion off) must reintroduce held-path reads -- else the test is vacuous"


def test_markers_match_canonical():
    from org.modules.graph.comp_constants_cli import SOVEREIGN_HELD_MARKERS
    assert set(tg._HELD_PATH_MARKERS) == set(SOVEREIGN_HELD_MARKERS), \
        "trace_graph._HELD_PATH_MARKERS drifted from comp_constants_cli.SOVEREIGN_HELD_MARKERS"


if __name__ == "__main__":
    test_markers_match_canonical()
    print("PASS: held markers match the canonical SOVEREIGN_HELD_MARKERS")
    g, reads = _run(exclusion_on=True)
    bd = [n for n in g.nodes.values() if tg._held_path_hit(n.file_path)]
    print(f"  held bd nodes minted: {len(bd)} | with a source_sha: {sum(1 for n in bd if n.source_sha)} (want 0)")
    print(f"  held-path CONTENT reads (exclusion ON): {len(reads)} (want 0)")
    test_indexer_never_reads_held_content()
    print("PASS: indexer minted held nodes metadata-only + read ZERO held content")
    _g, mreads = _run(exclusion_on=False)
    print(f"  held-path reads (exclusion OFF / mutation): {len(mreads)} (want > 0)")
    test_mutation_off_reintroduces_the_read()
    print("PASS: mutation (exclusion off) reintroduced the held read -- test is non-vacuous")
    print("=== INDEXER BD-CONTENT EXCLUSION: ALL PASS ===")
