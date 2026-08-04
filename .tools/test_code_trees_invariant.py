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
# FROZEN FIXTURE -- hand-written literals, never computed from the code under
# test. RE-FROZEN 2026-08-04: the mdpf rows below changed from the original
# 92e41ad1b3 transcription on ANDREW-DIRECT authority (0.2.0_DS terminal
# ~18:4xZ, "If you are editing these scripts you need to be able to deploy
# them"; CTO shape-approval 185213Z) -- the exact live-behavior change the old
# fixture existed to refuse is now the AUTHORIZED contract. bd/inf/cot rows are
# byte-identical to the original fixture; a divergence there is still the
# firm-separation defect class this file guards.
# ---------------------------------------------------------------------------
FROZEN_PIPELINE_MAP = {
    "black_diamond": ("opal-data-bd", "bd"),
    "inf": ("opal-data-inf", "inf"),
    "cot": ("opal-data-cot", "cot"),
    "mdpf": ("opal-data-mdpf", "mdpf"),
}
FROZEN_VALID_LAYERS = {"gold", "silver", "bronze", "backfill", "feeders", "assets_gold"}

# file_to_s3_target semantics: bd/inf/cot unchanged; mdpf resolves per its
# declared non-standard layout (code/scripts/<layer>/, assets_* fed from
# data/assets/). Shared-home membership (S3-key-existence) is enforced at
# DEPLOY time in main(), not here -- resolution is deliberately lexical.
FROZEN_TARGETS = [
    ("data/black_diamond/scripts/gold/x.py", ("opal-data-bd", "code/gold/x.py", "bd")),
    ("data/black_diamond/scripts/gold/lib/y.py", ("opal-data-bd", "code/gold/lib/y.py", "bd")),
    ("data/black_diamond/scripts/silver/s.py", ("opal-data-bd", "code/silver/s.py", "bd")),
    ("data/inf/scripts/gold/g.py", ("opal-data-inf", "code/gold/g.py", "inf")),
    ("data/inf/scripts/bronze/b.py", ("opal-data-inf", "code/bronze/b.py", "inf")),
    ("data/cot/scripts/silver/c.py", ("opal-data-cot", "code/silver/c.py", "cot")),
    ("data/mdpf/scripts/gold/m.py", ("opal-data-mdpf", "code/scripts/gold/m.py", "mdpf")),
    ("data/mdpf/scripts/backfill/build_aggregate_aua_timeseries.py",
     ("opal-data-mdpf", "code/scripts/backfill/build_aggregate_aua_timeseries.py", "mdpf")),
    ("data/assets/scripts/gold/build_dim_model_portfolio.py",
     ("opal-data-mdpf", "code/scripts/assets_gold/build_dim_model_portfolio.py", "mdpf")),
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


def test_artifacts_are_modelled_and_unresolved_ones_surface(results: list) -> None:
    """Non-script artifacts must be EXPRESSIBLE, and an unresolved target must SURFACE.

    Raised by AE-base 210149Z: the dispatch syncs code/scripts/ with --delete, so a
    config file with no declared home is silently reverted on the next run. A model
    that only knows .py files excludes the class entirely.
    """
    workspace = _TOOLS.parent
    arts = _core.CODE_TREES["mdpf"].get("artifacts")
    _check(
        results,
        "mdpf declares a non-script artifact class",
        bool(arts),
        "artifacts key absent -- the config-artifact class has nowhere to live",
    )
    if not arts:
        return
    # A declared artifact's repo_path must exist -- same fail-loudly rule as layers.
    missing = [
        f"{n} -> {a['repo_path']}"
        for n, a in arts.items()
        if not (workspace / a["repo_path"]).is_file()
    ]
    _check(
        results,
        "every declared artifact repo_path exists on disk",
        not missing,
        "MISSING: " + "; ".join(missing),
    )
    # UNRESOLVED targets must be VISIBLE, never silently treated as done.
    unresolved = sorted(n for n, a in arts.items() if a.get("s3_key") is None)
    _check(
        results,
        f"unresolved artifact targets surface by name ({len(unresolved)} open)",
        all(arts[n].get("owner") and arts[n].get("why") for n in unresolved),
        "an unresolved artifact must carry owner + why, else it is an absence "
        "wearing a declaration's costume",
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


def _load_pipeline_cli():
    return importlib.machinery.SourceFileLoader(
        "pipeline_cli", str(_TOOLS.parent / "org" / "modules" / "graph" / "pipeline_cli.py")
    ).load_module()  # noqa: FWD001


# Routing contract. Case 3 RE-FROZEN 2026-08-04: the bare-id -> bd-gold fallback
# this fixture previously PRESERVED was SUPERSEDED by the Andrew-direct stub
# ruling 2026-07-30 (@64a17a77b9, extending @10d1bb29e3: a bare id returns None
# and the caller REFUSES loud -- the silent bd default was the wrong-tree class
# on the deploy verifier itself). This fixture went STALE for 5 days (frozen
# 07-28, superseded 07-30, failing since) -- found + re-frozen during the
# 2026-08-04 mdpf-flip landing; the finding is the fixture's staleness, not the
# router.
FROZEN_ROUTING = [
    ("data/black_diamond/scripts/gold/x.py", "bd-gold", "case1 data-dir path"),
    ("data/inf/scripts/silver/s.py", "inf-gold", "case1 data-dir path"),
    ("data/cot/scripts/bronze/b.py", "cot-gold", "case1 data-dir path"),
    ("data/mdpf/scripts/gold/m.py", "mdpf", "case1 data-dir path"),
    ("data/assets/scripts/gold/build_cottonwood_mdpf_pair.py", "mdpf", "case2 cross-tree repo home"),
    ("data/assets/scripts/silver/rebalancer_schemas.py", "mdpf", "case2 cross-tree repo home"),
    ("D_00", None, "case3 SUPERSEDED 07-30: bare id refuses (None), no bd default"),
    ("dim_mdpf_aggregate_aua_timeseries.py", None, "case3 SUPERSEDED bare id"),
    ("", None, "case3 SUPERSEDED empty"),
]


def test_routing_contract(results: list) -> None:
    pcli = _load_pipeline_cli()
    bad = [
        f"{arg or '(empty)'}: got={pcli.resolve_pipeline_from_arg(arg)!r} want={exp!r} [{note}]"
        for arg, exp, note in FROZEN_ROUTING
        if pcli.resolve_pipeline_from_arg(arg) != exp
    ]
    _check(
        results,
        f"routing contract holds ({len(FROZEN_ROUTING)} cases: identity + new + PRESERVED)",
        not bad,
        "; ".join(bad),
    )
    # The superseded case, called out on its own so the refusal cannot silently
    # regress back to a bd default (the 07-30 stub ruling's whole point).
    _check(
        results,
        "SUPERSEDED: a bare id returns None (caller refuses; no silent bd-gold default)",
        pcli.resolve_pipeline_from_arg("D_00") is None,
        "a non-None bare-id resolution reintroduces the wrong-tree silent default",
    )


def test_routing_mutant(results: list) -> None:
    """Perturb the derived mapping; the routing contract must FAIL, then restore."""
    pcli = _load_pipeline_cli()
    tree = pcli._CODE_TREES["mdpf"]
    original = dict(tree["layers"])
    try:
        broken = dict(original)
        broken["assets_gold"] = ("data/nowhere/scripts/gold", "code/scripts/assets_gold/")
        tree["layers"] = broken
        _check(
            results,
            "MUTANT: breaking assets_gold's repo_home BREAKS routing (detected)",
            pcli.resolve_pipeline_from_arg(
                "data/assets/scripts/gold/build_cottonwood_mdpf_pair.py"
            ) != "mdpf",
            "mutation not detected -- the routing test is inert",
        )
    finally:
        tree["layers"] = original
    _check(
        results,
        "routing restored after mutation",
        pcli.resolve_pipeline_from_arg(
            "data/assets/scripts/gold/build_cottonwood_mdpf_pair.py"
        ) == "mdpf",
        "restore failed -- shared state left corrupted",
    )


def main_test() -> int:
    results: list = []
    test_pipeline_map_identical(results)
    test_file_to_s3_target_unchanged(results)
    test_declared_repo_homes_exist(results)
    test_uncovered_direction(results)
    test_artifacts_are_modelled_and_unresolved_ones_surface(results)
    test_routing_contract(results)
    test_routing_mutant(results)
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
