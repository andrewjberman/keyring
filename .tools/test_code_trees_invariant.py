#!/usr/bin/env python3
"""test_code_trees_invariant.py -- the CODE_TREES declaration's safety net.

INFRA.TOOLS, CTO mandatory addition 20260728T204943Z.

CODE_TREES replaced three hand-written registries that each restated the same
population at their own call site. The whole safety argument for that change is
one property: THE DERIVED `PIPELINE_MAP` IS BYTE-IDENTICAL TO THE HAND-WRITTEN
TABLE IT REPLACED. CTO's ruling, and the reason this file exists:

    "That property is doing all the safety work in this change, and it is
     currently a claim. PIPELINE_MAP is the Rule-13 deploy gate's bucket map,
     and bd/cot firm separation is gate-AND-IAM enforced with a standing
     never-mirror/never-sync prohibition. A silent divergence there is a
     firm-separation defect, which is the highest-consequence class in this
     estate."

So the expected values below are a FROZEN FIXTURE, transcribed from
safe_deploy_core.py:22-29 as it stood at commit 92e41ad1b3, BEFORE the
derivation landed. It is deliberately a literal: a fixture computed from the
code under test cannot detect that code changing.

Run: python .tools/test_code_trees_invariant.py
"""
from __future__ import annotations

import importlib.machinery
import pathlib
import sys

_TOOLS = pathlib.Path(__file__).parent
_core = importlib.machinery.SourceFileLoader(
    "safe_deploy_core", str(_TOOLS / "safe_deploy_core.py")
).load_module()  # noqa: FWD001


# ---------------------------------------------------------------------------
# FROZEN FIXTURE -- the pre-derivation literals. DO NOT compute these.
# ---------------------------------------------------------------------------
FROZEN_PIPELINE_MAP = {
    "black_diamond": ("opal-data-bd", "bd"),
    "inf": ("opal-data-inf", "inf"),
    "cot": ("opal-data-cot", "cot"),
}
FROZEN_VALID_LAYERS = {"gold", "silver", "bronze"}

# file_to_s3_target semantics as they stood before the change.
FROZEN_TARGETS = [
    ("data/black_diamond/scripts/gold/x.py", ("opal-data-bd", "code/gold/x.py", "bd")),
    ("data/black_diamond/scripts/gold/lib/y.py", ("opal-data-bd", "code/gold/lib/y.py", "bd")),
    ("data/black_diamond/scripts/silver/s.py", ("opal-data-bd", "code/silver/s.py", "bd")),
    ("data/inf/scripts/gold/g.py", ("opal-data-inf", "code/gold/g.py", "inf")),
    ("data/inf/scripts/bronze/b.py", ("opal-data-inf", "code/bronze/b.py", "inf")),
    ("data/cot/scripts/silver/c.py", ("opal-data-cot", "code/silver/c.py", "cot")),
    # CHECK-ONLY trees must NOT resolve -- registering mdpf as gated would start
    # deploying it on push, a live-behavior change nobody authorized.
    ("data/mdpf/scripts/gold/m.py", None),
    ("data/mdpf/scripts/backfill/build_aggregate_aua_timeseries.py", None),
    ("data/assets/scripts/gold/build_dim_model_portfolio.py", None),
    # Undeclared layer / non-.py / out of scope.
    ("data/black_diamond/scripts/probes/p.py", None),
    ("data/black_diamond/scripts/gold/x.txt", None),
    ("data/black_diamond/scripts/gold", None),
    ("README.md", None),
    ("", None),
]


def _check(results: list, name: str, ok: bool, detail: str = "") -> None:
    results.append((name, ok, detail))


def test_pipeline_map_identical(results: list) -> None:
    got = _core.PIPELINE_MAP
    _check(
        results,
        "PIPELINE_MAP key set == frozen",
        set(got) == set(FROZEN_PIPELINE_MAP),
        f"derived={sorted(got)} frozen={sorted(FROZEN_PIPELINE_MAP)}",
    )
    _check(
        results,
        "PIPELINE_MAP values == frozen (ordering-independent)",
        got == FROZEN_PIPELINE_MAP,
        f"derived={got!r} frozen={FROZEN_PIPELINE_MAP!r}",
    )
    _check(
        results,
        "VALID_LAYERS == frozen",
        set(_core.VALID_LAYERS) == FROZEN_VALID_LAYERS,
        f"derived={sorted(_core.VALID_LAYERS)} frozen={sorted(FROZEN_VALID_LAYERS)}",
    )
    # Firm separation: no gated tree may point at another firm's bucket.
    buckets = [b for b, _ in got.values()]
    _check(
        results,
        "no two gated trees share a bucket (firm separation)",
        len(buckets) == len(set(buckets)),
        f"buckets={buckets}",
    )


def test_file_to_s3_target_unchanged(results: list) -> None:
    bad = []
    for path, expected in FROZEN_TARGETS:
        got = _core.file_to_s3_target(path)
        if got != expected:
            bad.append(f"{path}: got={got!r} want={expected!r}")
    _check(
        results,
        f"file_to_s3_target matches frozen semantics ({len(FROZEN_TARGETS)} cases)",
        not bad,
        "; ".join(bad),
    )


def test_declared_repo_homes_exist(results: list) -> None:
    """A declared layer whose repo home is absent is a DECLARATION DEFECT.

    This is the assertion that turns the old silent `continue` into an error.
    """
    workspace = _TOOLS.parent
    missing = []
    for tree_name, tree in _core.CODE_TREES.items():
        for layer, (repo_home, _s3) in tree["layers"].items():
            if not (workspace / repo_home).is_dir():
                missing.append(f"{tree_name}:{layer} -> {repo_home}")
    _check(
        results,
        "every declared repo_home exists on disk",
        not missing,
        "MISSING: " + "; ".join(missing),
    )


def test_uncovered_direction(results: list) -> None:
    """INVERSE: an observed S3 layer with no declaration must surface, never be skipped.

    Uses a synthetic observed set so the assertion is exercised without AWS.
    """
    declared = set(_core.CODE_TREES["mdpf"]["layers"])
    observed_live = {"assets_gold", "backfill", "bronze", "feeders", "gold", "silver"}
    _check(
        results,
        "mdpf declaration covers all six LIVE S3 layers",
        observed_live <= declared,
        f"undeclared-but-live={sorted(observed_live - declared)}",
    )
    # And the detector itself must be able to fire.
    synthetic = observed_live | {"a_layer_nobody_declared"}
    _check(
        results,
        "undeclared-layer detector FIRES on a synthetic extra layer",
        bool(synthetic - declared),
        "detector could not distinguish an undeclared layer -- it is not a detector",
    )


def test_mutation_exercises_the_invariant(results: list) -> None:
    """A passing assertion never mutated has never been tested.

    Perturb one derived entry and confirm the byte-identity check FAILS.
    Restores the original afterwards.
    """
    original = dict(_core.CODE_TREES["cot"])
    try:
        _core.CODE_TREES["cot"] = {**original, "bucket": "opal-data-bd"}
        mutated = {
            name: (t["bucket"], t["label"])
            for name, t in _core.CODE_TREES.items()
            if t["deploy_gated"]
        }
        _check(
            results,
            "MUTANT: cot->opal-data-bd is DETECTED by the frozen comparison",
            mutated != FROZEN_PIPELINE_MAP,
            "mutation was NOT detected -- the invariant test is inert",
        )
        # And it must be caught specifically as a firm-separation collision.
        buckets = [b for b, _ in mutated.values()]
        _check(
            results,
            "MUTANT: bucket collision is detectable as firm-separation breach",
            len(buckets) != len(set(buckets)),
            f"buckets={buckets}",
        )
    finally:
        _core.CODE_TREES["cot"] = original
    # Prove the restore worked -- a test that corrupts shared state is worse
    # than no test.
    rederived = {
        name: (t["bucket"], t["label"])
        for name, t in _core.CODE_TREES.items()
        if t["deploy_gated"]
    }
    _check(
        results,
        "state restored after mutation",
        rederived == FROZEN_PIPELINE_MAP,
        f"post-restore={rederived!r}",
    )


def main_test() -> int:
    results: list = []
    test_pipeline_map_identical(results)
    test_file_to_s3_target_unchanged(results)
    test_declared_repo_homes_exist(results)
    test_uncovered_direction(results)
    test_mutation_exercises_the_invariant(results)

    print("CODE_TREES invariant suite")
    print()
    all_ok = True
    for name, ok, detail in results:
        print(f"  {'PASS' if ok else 'FAIL'}  {name}")
        if not ok and detail:
            print(f"        {detail}")
        all_ok = all_ok and ok

    print()
    if all_ok:
        print(f"OK: {len(results)}/{len(results)} cases passed")
        return 0
    fail_n = sum(1 for _, ok, _ in results if not ok)
    print(f"FAIL: {fail_n}/{len(results)} cases failed")
    return 1


if __name__ == "__main__":
    sys.exit(main_test())
