"""Conformance suite for the PROD-TARGET WRITE SAFETY leaf (prod_write_guard.py).

Carries forward, unchanged in substance, the invariants that guarded these symbols while they lived
in sovereign_held.py -- extracted by NFRA_TOOLUNIFY.GOVRIP step 1 (2026-07-25) so that deleting the
retracted GOVERNANCE module cannot take this live control with it.

  - the module's own invariant: it imports STDLIB ONLY (ast check over its import nodes) -- a
    load-bearing security leaf must never fail to import or move under a dependency change.
  - the predicates are PURE STRING checks -- they never open a file.
  - THE GUARD IS ARMED: the tuples are POPULATED and carry their exact values.

WHY THE ARMED-NESS TEST EXISTS, and it is the sharp one:
    The retracted `RETRACTED_20260709_*` tuples were BYTE-IDENTICAL to the live tuples here. So a
    sweep keyed on the PATH LITERALS rather than the SYMBOL NAME cannot tell the dead set from the
    live one -- it empties both, AND IT LOOKS LIKE IT WORKED. Emptying the tuples does not raise:
    `_path_matches` returns False on falsy `markers`, so `is_prod_write_forbidden` degrades to
    "nothing is ever forbidden" while the symbol, its signature and every name-keyed check survive
    intact. **A disarmed guard and an armed one are indistinguishable from the outside unless
    something asserts the VALUES.** That is what test_the_guard_is_ARMED does.

Pure-function + ast; hermetic + bd-safe (no file/AWS reads).
"""

from __future__ import annotations

import ast
import importlib.util
import os
from pathlib import Path

_MODULE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "prod_write_guard.py")
_spec = importlib.util.spec_from_file_location("prod_write_guard_undertest", _MODULE)
pg = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(pg)


def test_the_guard_is_ARMED():
    """The values ARE the control. An empty tuple silently disarms it and raises nothing."""
    assert pg.PROD_WRITE_FORBIDDEN_PATHS, "DISARMED: forbidden PATHS is empty -- nothing is guarded"
    assert pg.PROD_WRITE_FORBIDDEN_BUCKETS, "DISARMED: forbidden BUCKETS is empty -- nothing is guarded"
    assert pg.PROD_WRITE_FORBIDDEN_PATHS == (
        "data/black_diamond/",
        "data/canonical/schwab/silver/",
        "schwab/silver/",
    ), "the live prod-write PATH set changed -- these literals are load-bearing, not leftovers"
    assert pg.PROD_WRITE_FORBIDDEN_BUCKETS == (
        "opal-data-bd",
        "opal-data-schwab",
    ), "the live prod-write BUCKET set changed -- these literals are load-bearing, not leftovers"


def test_MUTANT_emptying_the_tuples_disarms_without_raising():
    """Proves the failure mode the armed-ness test exists to catch is SILENT, not loud.

    If this ever starts raising instead of returning False, the disarm becomes self-announcing and
    test_the_guard_is_ARMED could be relaxed. Until then it is the only detector.
    """
    assert pg._path_matches("data/black_diamond/x", ()) is False
    assert pg._bucket_matches("opal-data-bd", ()) is False


def test_prod_write_forbidden_path_forms():
    assert pg.is_prod_write_forbidden("data/black_diamond/x.parquet") is True
    assert pg.is_prod_write_forbidden("data/canonical/schwab/silver/a") is True
    assert pg.is_prod_write_forbidden("schwab/silver/a") is True
    assert pg.is_prod_write_forbidden("data\\black_diamond\\win.parquet") is True  # backslash normalized
    # POSITIVE CONTROL -- the predicate must be able to say NO, or it is not a predicate
    assert pg.is_prod_write_forbidden("data/inflection/ok.csv") is False
    assert pg.is_prod_write_forbidden("") is False
    assert pg.is_prod_write_forbidden(None) is False


def test_prod_write_forbidden_bucket_family_boundary():
    """Family match, and the boundary that matters: a DISTINCT bucket must not be captured."""
    assert pg.is_prod_write_forbidden("opal-data-bd") is True
    assert pg.is_prod_write_forbidden("opal-data-bd-raw") is True
    assert pg.is_prod_write_forbidden("opal-data-bd/key") is True
    assert pg.is_prod_write_forbidden("opal-data-schwab") is True
    # opal-data-bdx is a DIFFERENT bucket -- capturing it would be a false positive
    assert pg.is_prod_write_forbidden("opal-data-bdx") is False


def test_prod_write_forbidden_uri_and_arn_forms():
    """The ARN form is REQUIRED: comp-iam passes an S3 ARN, and without the strip a bd ARN read as
    not-matching -- a safety hole (CTO 2026-07-12)."""
    assert pg.is_prod_write_forbidden("s3://opal-data-bd/key") is True
    assert pg.is_prod_write_forbidden("arn:aws:s3:::opal-data-schwab/k") is True
    assert pg.is_prod_write_forbidden("arn:aws:s3:::opal-data-bd") is True
    assert pg.is_prod_write_forbidden("OPAL-DATA-BD") is True  # lowercasing only ADDS matches


def test_module_imports_are_stdlib_only():
    """The load-bearing invariant, carried verbatim from test_sovereign_held.py."""
    tree = ast.parse(Path(_MODULE).read_text(encoding="utf-8"))
    mods = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for n in node.names:
                mods.add(n.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                mods.add(node.module.split(".")[0])
    allowed = {"os", "__future__"}
    assert mods <= allowed, f"prod_write_guard must import STDLIB ONLY; found non-allowed: {mods - allowed}"


if __name__ == "__main__":
    test_the_guard_is_ARMED()
    test_MUTANT_emptying_the_tuples_disarms_without_raising()
    test_prod_write_forbidden_path_forms()
    test_prod_write_forbidden_bucket_family_boundary()
    test_prod_write_forbidden_uri_and_arn_forms()
    test_module_imports_are_stdlib_only()
    print("=== prod_write_guard: armed + predicates + stdlib-only invariant: ALL PASS ===")
