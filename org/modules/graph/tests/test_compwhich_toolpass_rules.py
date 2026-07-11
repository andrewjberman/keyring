#!/usr/bin/env python3
"""comp-which NFRA_TOOLPASS curated-route additions (CVO 2026-07-10, CTO ruling 024149Z item-2+3).

The routing-quality scorecard found comp-which gave the canonical tool as rank-1 for only 4/12
catalog labels. This locks in the 5 fixes (cross-layer->comp-kuzu, MP/SEV1->comp-surface-check,
gold-run-done->comp-validate, bare-gold-script->comp-pipescript, grep/find-repo->comp-grep fallback)
+ the --json launcher passthrough, WITH bidirectional non-vacuity: the new routes fire AND the
guards do NOT over-fire (a benign benchmarks-FEED query stays comp-transform; a semantic search-phrased
rich route stays comp-xref/comp-blast/comp-symbols, NOT swept to grep).

Exercises the LIVE launcher (.tools/comp-which) via --json --route-only (side-effect-free: no shell-out
on the fallback). Read-only, bd-clean.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

_WS = Path(__file__).resolve().parents[4]
_CW = str(_WS / ".tools" / "comp-which")


def _route(q):
    out = subprocess.run([sys.executable, _CW, "--json", "--route-only", q],
                         capture_output=True, text=True, timeout=60).stdout
    o = json.loads(out)  # --json MUST always be valid JSON (CD1) -- a parse error fails the test
    tools = [r["tool"] for r in o.get("routed", [])]
    if o.get("kind") == "fallback" and o.get("fallback"):
        tools = [o["fallback"].split()[0]]
    return o.get("kind"), tools


# ---- the 5 FIXED routes (rank-1 == the canonical tool) ----

@pytest.mark.parametrize("q,canon", [
    ("cross-layer graph question", "comp-kuzu"),
    ("run a MATCH query across layers", "comp-kuzu"),
    ("Touching MP/benchmarks/ADVI backend", "comp-surface-check"),
    ("Gold run done, signaling AE", "comp-validate"),
    ("Editing a gold script", "comp-pipescript"),
    ("Running a gold script", "comp-pipescript"),
])
def test_fixed_routes_rank1(q, canon):
    kind, tools = _route(q)
    assert tools and tools[0] == canon, f"{q!r} -> {tools} (want {canon} rank-1)"


def test_grep_repo_honors_the_fallback():
    """The footer PROMISES comp-grep on no-fit; a literal grep/find-repo intent must honor it, not
    confidently mis-route to comp-trace."""
    kind, tools = _route("Need to grep/find the repo")
    assert kind == "fallback" and tools and tools[0] == "comp-grep", f"got kind={kind} tools={tools}"
    kind, tools = _route("grep the repo for FooBar")
    assert kind == "fallback" and tools == ["comp-grep"], f"got kind={kind} tools={tools}"


# ---- NON-VACUITY: the guards must NOT over-fire (the other direction) ----

def test_surface_check_pointer_does_NOT_over_fire():
    """A benchmarks-FEED question is comp-transform's job, NOT the SEV1 surface-check pointer -- the
    pointer only fires on a STRONG surface-check hit, not a casual 'benchmarks' mention."""
    kind, tools = _route("what feeds the benchmarks panel")
    assert tools and tools[0] == "comp-transform", f"pointer over-fired: {tools}"


@pytest.mark.parametrize("q,canon", [
    ("where is function build_dashboard defined", "comp-symbols"),  # search-phrased but a RICH route
    ("call sites of get_advisor", "comp-blast"),                    # 'sites' is not a grep-repo intent
    ("find duplicate resources in the estate", "comp-dups"),        # 'find' + rich curated -> NOT grep
])
def test_grep_guard_does_NOT_sweep_rich_search_routes(q, canon):
    kind, tools = _route(q)
    assert tools and tools[0] == canon, f"grep-guard wrongly swept {q!r} -> {tools} (want {canon})"


# ---- REGRESSION: previously-correct routes unchanged ----

@pytest.mark.parametrize("q,canon", [
    ("what breaks if I change build_dashboard", "comp-blast"),
    ("new boto3 call needs iam perms", "comp-iam"),
    ("4xx html response debugging", "comp-routes"),
    ("which tooltips still need migrating", "comp-tooltip"),
    ("cache key collisions", "comp-cache"),
    ("current state of the compiled system", "comp-system"),
])
def test_no_regression(q, canon):
    kind, tools = _route(q)
    assert any(t == canon for t in tools), f"REGRESSION: {q!r} -> {tools} (want {canon})"


# ---- --json contract (CD1) ----

def test_json_contract():
    out = subprocess.run([sys.executable, _CW, "--json", "--route-only", "cross-layer graph question"],
                         capture_output=True, text=True, timeout=60).stdout
    o = json.loads(out)
    assert set(("query", "kind", "routed")) <= set(o)
    assert o["routed"] and "tool" in o["routed"][0] and "call" in o["routed"][0]
    # fallback carries a fallback call string
    fb = subprocess.run([sys.executable, _CW, "--json", "--route-only", "grep the repo for X"],
                        capture_output=True, text=True, timeout=60).stdout
    ofb = json.loads(fb)
    assert ofb["kind"] == "fallback" and ofb.get("fallback", "").startswith("comp-grep")


if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-v"]))
