#!/usr/bin/env python3
"""comp-which routing regression guard (LD-0208 fix (D), CTO / NFRA_COMPRAIL TO-6).

The standing "every comp-tool is reachable via the mandated router" oracle Andrew
asked for (2026-06-22, brief comp-which-routing-audit §4.4). Two assertions:

  TEST 1 (end-to-end self-routing -- the strong oracle, adapted from MSTR's coverage
    probe 2026-06-25): feed EACH tools_index tool its OWN richest use_case sentence as
    the question and assert comp-which SURFACES that tool's name end-to-end (not merely
    that the backstop *could* surface it). This catches keyword-collision misroutes
    (comp-platinum vs the portal rule) and search-verb hijacks (comp-xref's "find every
    ..." hitting the grep primitive) that a backstop-only check passes blind. Excludes
    the RUN-primitives + the router itself ({comp-grep, comp-glob, comp-which}).

  TEST 2 (audit reproduction): the three queries the 2026-06-22 audit caught misrouting
    ("is upstream data fresh" / "artifact invariants before upload" / "component expose
    PII") route to comp-freshness / comp-validate / comp-pii -- a rich ROUTE, not a grep.

Read-only, deterministic, ASCII-only. Run from workspace root:
  python .tools/comp-which-routing-test.py [--verbose]
Exit 0 = all pass; exit 1 = a regression (a tool went unreachable or an audit case
misrouted). Wire into the comp-tool test sweep; re-run after any comp-which/manifest edit.
"""
from __future__ import annotations

import os
import subprocess
import sys

WS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COMP_WHICH = os.path.join(WS, ".tools", "comp-which")
MANIFEST = os.path.join(WS, "org", "modules", "graph", "graph-call-manifest.yaml")

# RUN-primitives (comp-which routes TO rich tools, not these) + the router itself.
EXCLUDE = {"comp-grep", "comp-glob", "comp-which"}


def _load_manifest():
    import yaml
    with open(MANIFEST, encoding="utf-8") as f:
        return yaml.safe_load(f)


def _run_comp_which(q: str) -> str:
    r = subprocess.run([sys.executable, COMP_WHICH, q],
                       cwd=WS, capture_output=True, text=True, timeout=60)
    return (r.stdout or "") + (r.stderr or "")


def test_self_routing(manifest, verbose=False):
    """Every routable tools_index tool must surface itself end-to-end when queried by its
    own richest use_case sentence (MSTR coverage-probe semantics)."""
    ti = manifest.get("tools_index", {})
    entries = manifest.get("entries", [])
    by_tool = {}
    for e in entries:
        by_tool.setdefault(str(e.get("tool", "")).split()[0], []).append(e)
    tools = [t for t in sorted(ti.keys()) if t not in EXCLUDE]
    fails = []
    for t in tools:
        ucs = by_tool.get(t, [])
        q = (ucs[0]["use_case"] if ucs else ti[t].get("does", "")).strip().rstrip("?.")
        out = _run_comp_which(q)
        routed = t in out
        if verbose:
            print("  [%s] %-22s q='%s'" % ("OK " if routed else "MISS", t, q[:58]))
        if not routed:
            fails.append("%s: comp-which did not surface it for q='%s'" % (t, q[:70]))
    return tools, fails


def test_audit_reproduction(verbose=False):
    """The three audit-caught misroutes now route to the right rich tool (not a grep)."""
    cases = [
        ("is upstream data fresh", "comp-freshness"),
        ("artifact invariants before upload", "comp-validate"),
        ("component expose PII", "comp-pii"),
    ]
    fails = []
    for q, want in cases:
        try:
            out = _run_comp_which(q)
        except Exception as exc:  # noqa: BLE001
            fails.append('"%s" -> ERROR running comp-which: %s' % (q, exc))
            continue
        ran_primitive = "running the ON-RAILS primitive" in out
        routed_right = want in out
        if verbose:
            print("  [%s] '%s' -> %s" % ("OK " if (routed_right and not ran_primitive) else "MISS", q, want))
        if ran_primitive or not routed_right:
            how = "ran grep primitive" if ran_primitive else "did not name %s" % want
            fails.append('"%s" -> expected route to %s, but %s' % (q, want, how))
    return cases, fails


def main() -> int:
    verbose = "--verbose" in sys.argv
    manifest = _load_manifest()

    tools, f1 = test_self_routing(manifest, verbose)
    cases, f2 = test_audit_reproduction(verbose)

    print("\ncomp-which routing regression guard (LD-0208)")
    print("  TEST 1 end-to-end self-routing: %d/%d routable tools surface themselves"
          % (len(tools) - len(f1), len(tools)))
    for line in f1:
        print("    FAIL: %s" % line)
    print("  TEST 2 audit reproduction:      %d/%d audit cases route correctly"
          % (len(cases) - len(f2), len(cases)))
    for line in f2:
        print("    FAIL: %s" % line)

    if f1 or f2:
        print("\nRESULT: FAIL (%d unreachable + %d audit regressions)" % (len(f1), len(f2)))
        return 1
    print("\nRESULT: PASS -- all %d routable tools self-route; all %d audit cases route correctly"
          % (len(tools), len(cases)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
