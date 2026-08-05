"""WS-1 (NFRA_SCRIPTGEN): the roster -> predicate move, and the HONEST refusal that replaces a
false instruction.

WHY THIS FILE EXISTS. Two defects were live before it:

  1. `_discover_script_trees` / `_resolve_tree_from_path` were DEAD CODE -- defined, never called.
     The roster->predicate move looked landed and was not. A test that calls them is the only thing
     that keeps them wired.
  2. For a real tree with no curated DAG (`data/assets`, 77 files), the five non-`io` subcommands
     refused with *"--pipeline/-p is now REQUIRED ... re-run with the one you mean"* -- and
     `--pipeline` HAS NO VALID VALUE for `assets`. **The tool demanded a flag that cannot be
     supplied and reported it as user error.** An instruction the caller cannot follow is worse than
     a refusal: it sends them hunting a spelling that does not exist.

The behavioral tests below assert on the DISTINCTION between those two refusals, because that
distinction is the whole feature. Asserting only "rc==2" would pass against the defect.

Named `test_pipescript_*` deliberately: the suite gate's WATCH_GLOBS carries `test_pipescript_*.py`,
so this battery is covered by construction rather than by a later allowlist edit that nobody makes.
"""
from __future__ import annotations

import importlib.util
import os
import subprocess
import sys

import pytest

_HERE = os.path.dirname(os.path.abspath(__file__))
_GRAPH = os.path.dirname(_HERE)
# org/modules/graph -> org/modules -> org -> <workspace root>. THREE levels; an off-by-one here
# resolved to .../org and made three tests SKIP silently (a skip reads like a pass in the summary).
_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(_GRAPH)))
_spec = importlib.util.spec_from_file_location("pipeline_cli", os.path.join(_GRAPH, "pipeline_cli.py"))
pcli = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(pcli)

CLI = os.path.join(_GRAPH, "pipeline_cli.py")


def _run(*argv):
    p = subprocess.run([sys.executable, CLI, *argv], capture_output=True, text=True, cwd=_ROOT)
    return p.returncode, (p.stdout or "") + (p.stderr or "")


def _one(tree, layer="gold"):
    d = os.path.join(_ROOT, "data", tree, "scripts", layer)
    if not os.path.isdir(d):
        return None
    for f in sorted(os.listdir(d)):
        if f.endswith(".py") and not f.startswith("__"):
            return f"data/{tree}/scripts/{layer}/{f}"
    return None


# ------------------------------------------------------------------ the predicate itself

def test_predicate_is_wired_not_dead():
    """Both functions were swept in as dead code once. This is the wire-check."""
    assert callable(pcli._discover_script_trees)
    assert callable(pcli._resolve_tree_from_path)


def test_predicate_sees_more_trees_than_the_roster():
    """The point of WS-1. If these ever converge, the predicate has silently become a roster."""
    trees = pcli._discover_script_trees()
    assert len(trees) > len(pcli._DATADIR_TO_PIPELINE)
    for t in pcli._DATADIR_TO_PIPELINE:          # roster must be a SUBSET, never divergent
        if t in trees or t == "mdpf":
            continue
        pytest.fail(f"roster tree {t!r} not discoverable by the predicate")


def test_predicate_is_derived_from_disk_not_a_literal():
    """Every discovered tree must actually exist with a scripts/ dir -- i.e. it was READ, not typed."""
    for tree, layers in pcli._discover_script_trees().items():
        assert os.path.isdir(os.path.join(_ROOT, "data", tree, "scripts")), tree
        assert layers, f"{tree} reported with no layers"


def test_resolve_marks_roster_membership_correctly():
    bd = pcli._resolve_tree_from_path("data/black_diamond/scripts/gold/A_00.x.py")
    assert bd is not None and bd[0] == "black_diamond" and bd[1] == "gold"
    assert bd[2] is True, "bd is a curated/roster tree"
    az = pcli._resolve_tree_from_path("data/assets/scripts/gold/whatever.py")
    if az is not None:                            # assets exists in this repo; guard for portability
        assert az[0] == "assets" and az[2] is False, "assets has no curated DAG"


def test_resolve_returns_None_for_a_bare_id():
    """A bare id has nothing to resolve FROM -- it must stay a genuine refusal (07-30 ruling)."""
    assert pcli._resolve_tree_from_path("A_00") is None
    assert pcli._resolve_tree_from_path("") is None
    assert pcli._resolve_tree_from_path(None) is None


def test_resolve_rejects_a_non_scripts_path():
    assert pcli._resolve_tree_from_path("data/black_diamond/notscripts/gold/x.py") is None


# ------------------------------------------------------------------ the refusals, behaviorally

def test_bare_id_still_refuses_with_the_flag_instruction():
    """The 07-30 no-silent-default ruling must still bind. This is the guard against 'fixing' the
    refusal by relaxing it."""
    rc, out = _run("feeds", "A_00")
    assert rc == 2
    assert "REQUIRED" in out


def test_uncurated_tree_does_NOT_tell_you_to_pass_an_impossible_flag():
    """THE LOAD-BEARING TEST. Before WS-1 completion this said '--pipeline is REQUIRED' for a tree
    with no possible --pipeline value. Asserting rc==2 alone would PASS against that defect, so the
    assertion is on WHICH refusal is given."""
    target = _one("assets")
    if target is None:
        pytest.skip("data/assets not present in this checkout")
    rc, out = _run("feeds", target)
    assert rc == 2
    assert "NO CURATED GRAPH" in out
    assert "assets" in out
    assert "NOT a missing flag" in out
    # and it must point at something that actually works
    assert "comp-pipescript io" in out


def test_roster_tree_path_still_resolves_without_a_flag():
    """WS-1's positive case, and the regression guard for the incident where a dead `if False:`
    made this refuse for five of six subcommands."""
    target = _one("black_diamond")
    if target is None:
        pytest.skip("data/black_diamond not present")
    for cmd in ("io", "feeds", "consumers"):
        rc, out = _run(cmd, target)
        assert rc == 0, f"{cmd} regressed: rc={rc}\n{out[:400]}"


def test_io_names_the_real_tree_not_a_placeholder():
    """An out-of-graph answer must say WHICH tree it resolved; '<no curated tree>' is the tool
    saying it gave up, which a reader cannot act on."""
    target = _one("assets")
    if target is None:
        pytest.skip("data/assets not present in this checkout")
    rc, out = _run("io", target)
    assert rc == 0
    assert "assets" in out
    assert "<no curated tree>" not in out
