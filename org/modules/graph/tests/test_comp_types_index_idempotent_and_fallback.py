"""NFRA_TOOLPASS: comp-types `index` -- TWO defects found by exercise + fixed (CVO confirm pass).

(1) NON-IDEMPOTENT manifest. cmd_index wrote `elapsed_seconds: {elapsed:.2f}` -- a PER-RUN DURATION --
    into the committed cache org/modules/graph/types-index/<Type>.yaml, so `index` produced a DIFFERENT
    manifest sha on every run even when the type was unchanged (observed: run1=595f7cd1 run2=7eac0844).
    Fix: drop elapsed_seconds from the manifest (it stays in the stdout PASS line). The manifest is now
    fully deterministic (sorted consumers + stable counts) -> re-run == no diff.

(2) default-fallback SELF-CONTRADICTION. `_classify_line` files `... || DEFAULT_LAYOUT` as
    category='default-fallback' (its substring clause), but the separate `is_default_fallback` FLAG only
    matched `??`-style coalescing, so a row the table LABELED default-fallback was reported by the summary
    + manifest as "none detected / default_fallback_sites: 0" -- a self-contradiction that UNDER-COUNTED
    firm-fallback sites. Fix: the flag is now (cat == 'default-fallback') OR the ??-regex, so it can never
    disagree with the category, and ||-style fallbacks are counted.

Hermetic + bd-SAFE: mocks _grep_portal + _find_type_definition (NEVER greps the real portal tree, never
touches data/black_diamond) and redirects _TYPES_INDEX_DIR to a tmp dir. Both assertions FAIL against the
pre-fix code (non-vacuous): the elapsed line would be present + churn run-to-run; the ||-DEFAULT_LAYOUT
row would carry default_fallback: false and default_fallback_sites: 0.

# rail-checked: assurance oracle for comp-types under test (NFRA_TOOLPASS sec.6)
Author: 3.0.0_SA_CVO~B.
"""

import importlib.util
import io
import os
import tempfile
from contextlib import redirect_stdout
from pathlib import Path
from types import SimpleNamespace

_HERE = os.path.dirname(os.path.abspath(__file__))
_WS = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(_HERE))))
_MODULE = os.path.join(_WS, "org", "modules", "graph", "types_cli.py")

_spec = importlib.util.spec_from_file_location("types_cli_undertest", _MODULE)
tc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(tc)

# Canned grep hits keyed by the search pattern cmd_index passes. Only the type-name pattern returns
# rows; the hook / DEFAULT_LAYOUT / layout.* patterns return [] so nothing real is scanned.
#   row 1: `... || DEFAULT_LAYOUT` -> _classify_line files it 'default-fallback' via the substring clause
#          (||-style, NOT ??-style) -> the exact site the old flag missed.
#   row 2: an import line -> category 'import', a genuine non-fallback consumer.
_CANNED = {
    "TenantLayoutConfig": [
        "portal/src/foo.tsx:10:const layoutFirm = LAYOUTS[firmId] || DEFAULT_LAYOUT",
        "portal/src/bar.tsx:20:import { TenantLayoutConfig } from '../types'",
    ],
}


def _run_index(tmp_dir, type_name="TenantLayoutConfig"):
    saved = (tc._grep_portal, tc._find_type_definition, tc._TYPES_INDEX_DIR)
    tc._grep_portal = lambda pattern, extra=None: list(_CANNED.get(pattern, []))
    tc._find_type_definition = lambda name: None
    tc._TYPES_INDEX_DIR = Path(tmp_dir)
    args = SimpleNamespace(type_name=type_name, firm_conditional_sites=False, severity=None)
    try:
        with redirect_stdout(io.StringIO()):
            rc = tc.cmd_index(args)
    finally:
        (tc._grep_portal, tc._find_type_definition, tc._TYPES_INDEX_DIR) = saved
    manifest = (Path(tmp_dir) / f"{type_name}.yaml").read_text(encoding="utf-8")
    return rc, manifest


def test_index_manifest_is_idempotent_and_carries_no_run_duration():
    with tempfile.TemporaryDirectory() as d:
        rc1, m1 = _run_index(d)
        rc2, m2 = _run_index(d)
    assert rc1 == 0 and rc2 == 0, f"index should succeed; got rc1={rc1} rc2={rc2}"
    # non-vacuous: the pre-fix manifest carried `elapsed_seconds: X.YZ` and two runs differed on it.
    assert "elapsed_seconds" not in m1, f"a per-run DURATION must not be in the committed cache:\n{m1}"
    assert m1 == m2, f"index manifest must be idempotent (re-run == no diff); it churned:\n---1---\n{m1}\n---2---\n{m2}"


def test_default_fallback_flag_agrees_with_category_and_counts_or_style():
    with tempfile.TemporaryDirectory() as d:
        rc, m = _run_index(d)
    assert rc == 0, f"index should succeed; got rc={rc}"
    # the ||-DEFAULT_LAYOUT row: category default-fallback AND flag true (they can no longer disagree).
    assert "category: default-fallback" in m, f"the ||-DEFAULT_LAYOUT site should categorize default-fallback:\n{m}"
    assert "default_fallback: true" in m, \
        f"pre-fix BUG: a row LABELED default-fallback carried default_fallback: false (flag != category):\n{m}"
    # the summary count must include the ||-style site (was 0 pre-fix -> the "none detected" contradiction).
    assert "default_fallback_sites: 1" in m, f"the ||-style fallback must be COUNTED (was 0 pre-fix):\n{m}"


if __name__ == "__main__":
    test_index_manifest_is_idempotent_and_carries_no_run_duration()
    print("PASS: index manifest is idempotent + carries no run-duration (elapsed removed)")
    test_default_fallback_flag_agrees_with_category_and_counts_or_style()
    print("PASS: default-fallback flag agrees with category + counts ||-style sites")
    print("=== comp-types index idempotency + fallback-consistency: ALL PASS ===")
