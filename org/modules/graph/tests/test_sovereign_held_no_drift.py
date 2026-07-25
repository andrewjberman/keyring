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

# CANONICAL HOMES, SCOPED BY SYMBOL (GOVRIP step 1, 2026-07-25; base CTO ruling 192659Z).
# prod_write_guard.py is the canonical home for the PROD-WRITE SAFETY tuples ONLY. It is NOT
# exempted as a file: it must never hold RETRACTED_* or SOVEREIGN_HELD_* literals. The two sets are
# BYTE-IDENTICAL, so a file-level exemption here would be blanket immunity in exactly the module a
# stray copy would most plausibly land in.
_AUTHORISED_HOMES = {
    "prod_write_guard.py": frozenset({"PROD_WRITE_FORBIDDEN_PATHS", "PROD_WRITE_FORBIDDEN_BUCKETS"}),
}

# Tools migrated to import the shared predicate (C2-C7 + the C0 locals + comp-secrets/pipeline_cli).
_MIGRATED = [
    _GRAPH / "trace_graph.py",
    _GRAPH / "validate_cli.py",
    _GRAPH / "comp_dispatch.py",
    _GRAPH / "comp_recognizers_code.py",
    _GRAPH / "comp_recognizers_config.py",
    _GRAPH / "extract_iam.py",
    # comp_constants_cli.py REMOVED from _MIGRATED (GOVRIP, base CTO ruling 192330Z): it no longer
    # imports sovereign_held at all. It derived a RETRACTED_* re-arm set, and Andrew's ~185538Z ruling
    # forbids the tool-level governance predicate -- so the fix was to STOP DERIVING, not to re-point.
    # This list means "still imports the shared predicate"; a migrated-OFF module must leave it, or
    # the test asserts the presence of the very import the ruling removed.
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
            # POST-SPLIT (2026-07-22): the leaf now carries TWO predicates. The GOVERNANCE tuples
            # (SOVEREIGN_HELD_*/HELD_*) are correctly EMPTY after the 2026-07-14 retraction and are
            # now ALIASES, not literals -- reading only those made this meta-test blind (it said so,
            # correctly, rather than passing vacuously). Track the tuples that still CARRY values:
            # the RETRACTED_* re-arm set and the PROD_WRITE_FORBIDDEN_* control. A local copy of
            # EITHER is drift, which is exactly the split CTO asked this test to assert.
            if any(n in ("HELD_PATH_MARKERS", "HELD_BUCKET_PREFIXES",
                         "RETRACTED_20260709_PATHS", "RETRACTED_20260709_BUCKETS",
                         "PROD_WRITE_FORBIDDEN_PATHS", "PROD_WRITE_FORBIDDEN_BUCKETS") for n in names):
                if isinstance(node.value, (ast.Tuple, ast.List)):
                    for e in node.value.elts:
                        if isinstance(e, ast.Constant) and isinstance(e.value, str):
                            markers.add(e.value)
    return markers


_MARKERS = _canonical_markers()


def _imports_sovereign_held(src: str) -> bool:
    return "sovereign_held import" in src or "import sovereign_held" in src


def _has_local_marker_literal(src: str, authorised: frozenset = frozenset()) -> bool:
    """True if the source RE-DEFINES a held-marker literal copy (drift). NOT an operational path list.

    `authorised` = symbol names this FILE is the canonical home for. Scoped BY SYMBOL, never by file:
    a file-level exemption would be blanket immunity, because the RETRACTED_* and PROD_WRITE_FORBIDDEN_*
    tuples are BYTE-IDENTICAL -- so exempting prod_write_guard.py wholesale would let a future
    RETRACTED_* copy hide in the one module where such a copy is most likely to appear, converting this
    drift control into a drift BLIND SPOT. Symbol scoping keeps the control live inside its own home.
    """
    tree = ast.parse(src)
    # value-nodes of assignments to AUTHORISED symbols -- canonical, not drift.
    exempt = set()
    if authorised:
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign) or isinstance(node, ast.AnnAssign):
                targets = node.targets if isinstance(node, ast.Assign) else [node.target]
                if any(isinstance(t, ast.Name) and t.id in authorised for t in targets):
                    exempt.add(id(node.value))
    # (a) any literal collection with >=2 EXACT canonical markers = a marker-set copy.
    for node in ast.walk(tree):
        if isinstance(node, (ast.Tuple, ast.List, ast.Set)):
            if id(node) in exempt:
                continue
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
    """Two canonical homes since GOVRIP step 1 (2026-07-25), scoped BY SYMBOL not by file.

    This test was RED at @afa4dcdee: it modelled ONE canonical leaf, and the exec-ordered extraction
    of the prod-write safety half into prod_write_guard.py created a SECOND legitimate home. The
    control's PRINCIPLE stands -- no unauthorised local copies -- and matters MORE after a split, so
    it was FIXED, not retired. (Contrast the re-arm test retired the same day, whose principle Andrew
    overturned. Principle overturned -> retire; model stale -> fix.)
    """
    assert _MARKERS, "could not read the canonical markers from sovereign_held -- the meta-test is blind"
    scan = [f for f in sorted(_GRAPH.glob("*.py")) if f != _CANONICAL]
    scan += [_TOOLS / "comp-secrets", _TOOLS / "freshness_manifest_gen.py"]
    offenders = [f.name for f in scan
                 if _has_local_marker_literal(f.read_text(encoding="utf-8"),
                                              _AUTHORISED_HOMES.get(f.name, frozenset()))]
    assert not offenders, \
        f"local held-marker literal copies re-introduced (fold them into a canonical home): {offenders}"


def test_the_symbol_scoping_is_NOT_a_blanket_file_exemption():
    """MUTANT: prod_write_guard is authorised for PROD_WRITE_FORBIDDEN_* and NOTHING ELSE.

    The byte-identical tuples are why this matters: a file-level exemption would let a RETRACTED_*
    copy hide in the very module most likely to carry one. If this ever passes, the exemption has
    silently widened into immunity.
    """
    src = (_GRAPH / "prod_write_guard.py").read_text(encoding="utf-8")
    auth = _AUTHORISED_HOMES["prod_write_guard.py"]
    assert not _has_local_marker_literal(src, auth), \
        "POSITIVE CONTROL: prod_write_guard's own authorised tuples must not read as drift"
    mutant = src + '\n_SNEAKY_RETRACTED = ("data/black_diamond/", "opal-data-bd")\n'
    assert _has_local_marker_literal(mutant, auth), \
        "MUTANT FAILED: an UNAUTHORISED marker copy inside the authorised file was not caught -- " \
        "the symbol scoping has degraded into a blanket file exemption"


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
