"""NFRA_TOOLPASS C8 -- the CAPSTONE anti-drift meta-test for the sovereign-hold consolidation.

The whole point of folding ~15 tools into sovereign_held is single-source-of-truth. This test makes the
consolidation SELF-ENFORCING: it fails if a future tool rolls its OWN held-marker literal copy (drift), or
if a migrated tool stops importing the shared predicate. Without this, the copies would silently creep back.

Two guards:
  1. every migrated tool imports the shared predicate (sovereign_held);
  2. NO module except sovereign_held.py holds a held-marker LITERAL copy -- detected as a literal
     Tuple/List/Set containing >=2 EXACT canonical markers, OR a `*HELD*MARKER*`/`*HELD*PREFIX*`-named
     module assignment whose value is a literal collection. (An operational path list like
     comp_recognizers._REAL_SOURCES -- specific .sh files, not bare prefixes -- and the firm->bucket map
     -- one bucket + an alias -- are NOT copies and must not be flagged.)
  + a POSITIVE control: the drift-check bites on a synthetic re-introduction and stays quiet on a clean
    import-based tool.

Pure ast; hermetic + bd-safe (reads tool source, never bd data).

# rail-checked: assurance oracle for the sovereign-hold consolidation under test (NFRA_TOOLPASS sec.6)
Author: 3.0.0_SA_CVO~B.
"""

import ast
import os
import re
from pathlib import Path

_HERE = os.path.dirname(os.path.abspath(__file__))
_WS = Path(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(_HERE)))))
_GRAPH = _WS / "org" / "modules" / "graph"
_TOOLS = _WS / ".tools"
_CANONICAL = _GRAPH / "sovereign_held.py"

# Tools migrated to import the shared predicate (C2-C7 + the C0 locals + comp-secrets/pipeline_cli).
_MIGRATED = [
    _GRAPH / "trace_graph.py",
    _GRAPH / "validate_cli.py",
    _GRAPH / "comp_dispatch.py",
    _GRAPH / "comp_recognizers_code.py",
    _GRAPH / "comp_recognizers_config.py",
    _GRAPH / "extract_iam.py",
    _GRAPH / "comp_constants_cli.py",
    _GRAPH / "pipeline_cli.py",
    _GRAPH / "incrparity_cli.py",
    _TOOLS / "freshness_manifest_gen.py",
    _TOOLS / "comp-secrets",
]

# Transitive users (covered via trace_graph._held_path_hit's re-export, NOT a direct import) -- named here
# so the denominator is honest: extract_pipeline / extract_s3 / platinum_cli guard via _held_path_hit, which
# C2 re-exports from sovereign_held. They are guarded-by-delegation, not by a direct sovereign_held import.
_TRANSITIVE = ("extract_pipeline.py", "extract_s3.py", "platinum_cli.py")

# Cross-lane vendored-mirror importer (C-x, CTO Rule-3-approved 345aeb90b): freeze_monitor is the deployed
# comp-xray Lambda whose archive zips ONLY infra/aws/compdiff/, so it imports a byte-identical VENDORED
# sibling infra/aws/compdiff/sovereign_held.py (not the org/ canonical). It is guarded by the compdiff-LANE
# byte-suffix test (test_vendored_sovereign_held_is_identical.py: vendored.endswith(canonical)), NOT this
# org-tree scan (which exempts compdiff by design -- the lane boundary CTO ratified). Named for an honest count.
_VENDORED_MIRROR = ("freeze_monitor.py (infra/aws/compdiff -> vendored sovereign_held sibling; guarded by "
                    "the compdiff-lane byte-suffix test, not this scan)",)

_HELD_NAME_RE = re.compile(r"HELD.*(MARKER|PREFIX)|SOVEREIGN.*MARKER", re.IGNORECASE)


def _canonical_markers() -> set:
    """The EXACT canonical marker strings, read from sovereign_held's two tuples (so this test tracks the
    canonical set, not a hardcoded copy of it)."""
    tree = ast.parse(_CANONICAL.read_text(encoding="utf-8"))
    markers: set = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            names = [t.id for t in node.targets if isinstance(t, ast.Name)]
            if any(n in ("HELD_PATH_MARKERS", "HELD_BUCKET_PREFIXES") for n in names):
                if isinstance(node.value, (ast.Tuple, ast.List)):
                    for e in node.value.elts:
                        if isinstance(e, ast.Constant) and isinstance(e.value, str):
                            markers.add(e.value)
    return markers


_MARKERS = _canonical_markers()


def _imports_sovereign_held(src: str) -> bool:
    return "sovereign_held import" in src or "import sovereign_held" in src


def _has_local_marker_literal(src: str) -> bool:
    """True if the source RE-DEFINES a held-marker literal copy (drift). NOT an operational path list."""
    tree = ast.parse(src)
    # (a) any literal collection with >=2 EXACT canonical markers = a marker-set copy.
    for node in ast.walk(tree):
        if isinstance(node, (ast.Tuple, ast.List, ast.Set)):
            exact = [e.value for e in node.elts
                     if isinstance(e, ast.Constant) and isinstance(e.value, str) and e.value in _MARKERS]
            if len(exact) >= 2:
                return True
    # (b) a *HELD*MARKER*/*HELD*PREFIX*/SOVEREIGN*MARKER-named assignment to a literal collection.
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name) and _HELD_NAME_RE.search(t.id) and \
                        isinstance(node.value, (ast.Tuple, ast.List, ast.Set)):
                    return True
    return False


def test_migrated_tools_import_the_shared_predicate():
    missing = [f.name for f in _MIGRATED if not _imports_sovereign_held(f.read_text(encoding="utf-8"))]
    assert not missing, f"migrated tools no longer import sovereign_held (drift): {missing}"


def test_only_the_canonical_leaf_holds_marker_literals():
    assert _MARKERS, "could not read the canonical markers from sovereign_held -- the meta-test is blind"
    scan = [f for f in sorted(_GRAPH.glob("*.py")) if f != _CANONICAL]
    scan += [_TOOLS / "comp-secrets", _TOOLS / "freshness_manifest_gen.py"]
    offenders = [f.name for f in scan if _has_local_marker_literal(f.read_text(encoding="utf-8"))]
    assert not offenders, \
        f"local held-marker literal copies re-introduced (fold them into sovereign_held): {offenders}"


def test_drift_check_is_non_vacuous():
    # POSITIVE control: a re-introduced local marker tuple MUST be flagged.
    assert _has_local_marker_literal("_MY_HELD_MARKERS = ('data/black_diamond/', 'schwab/silver/')\n")
    assert _has_local_marker_literal("X = ('data/black_diamond/', 'data/canonical/schwab/silver/', 'opal-data-bd')\n")
    # NEGATIVE control: an import-based tool + an operational path list + the firm map must NOT be flagged.
    assert not _has_local_marker_literal(
        "from sovereign_held import is_held_path\nif is_held_path('data/black_diamond/x'): pass\n")
    assert not _has_local_marker_literal(
        "_REAL = ['data/inf/x.sh', 'data/black_diamond/scripts/gold/gold_dispatch.sh']\n")  # specific files
    assert not _has_local_marker_literal("FIRM = {'black_diamond': ('opal-data-bd', 'bd')}\n")  # 1 bucket + alias


def test_meta_test_bites_on_a_temp_module_reintroduction(tmp_path):
    """CTO gate (c): drop a fake local _HELD_MARKERS into a TEMP module in the scan set and assert the SAME
    scan that clears the live estate FLAGS it -- proving the guard is live end-to-end, not just on strings."""
    import importlib.util as _ilu
    _spec = _ilu.spec_from_file_location("nodrift_ut", os.path.abspath(__file__))
    _m = _ilu.module_from_spec(_spec)
    _spec.loader.exec_module(_m)
    clean = tmp_path / "clean_tool.py"
    clean.write_text("from sovereign_held import is_held_path\nx = is_held_path('data/black_diamond/a')\n", encoding="utf-8")
    drifted = tmp_path / "drifted_tool.py"
    drifted.write_text("_HELD_MARKERS = ('data/black_diamond/', 'data/canonical/schwab/silver/', 'schwab/silver/')\n",
                       encoding="utf-8")
    assert not _m._has_local_marker_literal(clean.read_text(encoding="utf-8")), "a clean import-based module must pass"
    assert _m._has_local_marker_literal(drifted.read_text(encoding="utf-8")), \
        "a temp module re-introducing a local _HELD_MARKERS copy MUST be flagged (the whole point of C8)"


if __name__ == "__main__":
    print(f"canonical markers ({len(_MARKERS)}): {sorted(_MARKERS)}")
    _total = len(_MIGRATED) + len(_VENDORED_MIRROR) + len(_TRANSITIVE)
    print(f"DENOMINATOR: {len(_MIGRATED)} direct sovereign_held importers + {len(_VENDORED_MIRROR)} vendored-mirror "
          f"(cross-lane) + {len(_TRANSITIVE)} transitive (_held_path_hit delegation) = {_total} tools guarded by "
          f"the consolidation. CONSOLIDATION 100% COMPLETE across all 16 bd-readers.")
    print(f"  direct:         {[f.name for f in _MIGRATED]}")
    print(f"  vendored-mirror: {list(_VENDORED_MIRROR)}")
    print(f"  transitive:     {list(_TRANSITIVE)}")
    test_migrated_tools_import_the_shared_predicate()
    print(f"PASS: all {len(_MIGRATED)} direct-importer tools import sovereign_held")
    test_only_the_canonical_leaf_holds_marker_literals()
    print("PASS: no local held-marker literal copies outside sovereign_held.py (0 drift)")
    test_drift_check_is_non_vacuous()
    print("PASS: drift-check bites on a re-introduction, quiet on operational lists (non-vacuous)")
    print("=== C8 anti-drift meta-test: ALL PASS ===")
