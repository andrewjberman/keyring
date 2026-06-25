#!/usr/bin/env python3
"""comp-which routing regression guard (LD-0208 fix (D), CTO / NFRA_COMPRAIL TO-6).

The standing "every comp-tool is reachable via the mandated router" oracle Andrew
asked for (2026-06-22). Two assertions:

  TEST 1 (defect-A regression): for EVERY tool in the manifest tools_index, querying
    its own entry use_case through comp-which's manifest backstop (_manifest_matches)
    surfaces that tool. This is the direct guard for the bug where _manifest_matches
    read the wrong key (`use_cases` instead of `entries`) and matched NOTHING, leaving
    ~28 long-tail tools unreachable.

  TEST 2 (audit reproduction): the three queries the 2026-06-22 audit caught misrouting
    ("is upstream data fresh" / "artifact invariants before upload" / "component expose
    PII") now route to comp-freshness / comp-validate / comp-pii respectively -- a rich
    ROUTE, not a raw grep-the-term dead-end.

Read-only, deterministic, ASCII-only. Run: python .tools/comp-which-routing-test.py
Exit 0 = all pass; exit 1 = a regression (a tool went unreachable or an audit case
misrouted). Wire into the comp-tool test sweep; re-run after any comp-which edit.
"""
from __future__ import annotations

import importlib.util
import os
import subprocess
import sys

WS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COMP_WHICH = os.path.join(WS, ".tools", "comp-which")
MANIFEST = os.path.join(WS, "org", "modules", "graph", "graph-call-manifest.yaml")


def _load_comp_which():
    # comp-which has no .py suffix, so importlib can't infer a loader -- pass one explicitly.
    from importlib.machinery import SourceFileLoader
    loader = SourceFileLoader("comp_which", COMP_WHICH)
    spec = importlib.util.spec_from_loader("comp_which", loader)
    mod = importlib.util.module_from_spec(spec)
    loader.exec_module(mod)
    return mod


def _load_manifest():
    import yaml
    with open(MANIFEST, encoding="utf-8") as f:
        return yaml.safe_load(f)


def test_backstop_reachability(mod, manifest):
    """Every tools_index tool must be surfaced by the backstop when queried by its own
    entry use_case. Guards the dead-key defect directly."""
    fails = []
    tools = sorted(manifest.get("tools_index", {}).keys())
    entries = manifest.get("entries", [])
    by_tool = {}
    for e in entries:
        by_tool.setdefault(e.get("tool"), []).append(e)
    for tool in tools:
        ents = by_tool.get(tool, [])
        if not ents:
            fails.append("%s: no manifest entry carries this tool (catalog gap)" % tool)
            continue
        reachable = False
        for e in ents:
            uc = e.get("use_case", "")
            if not uc:
                continue
            matches = mod._manifest_matches(uc, mod._tokens(uc), top=5)
            if any(m[1] == tool for m in matches):
                reachable = True
                break
        if not reachable:
            fails.append("%s: backstop did not surface it for any of its own use_case strings" % tool)
    return tools, fails


def test_audit_reproduction():
    """The three audit-caught misroutes now route to the right rich tool (not a grep)."""
    cases = [
        ("is upstream data fresh", "comp-freshness"),
        ("artifact invariants before upload", "comp-validate"),
        ("component expose PII", "comp-pii"),
    ]
    fails = []
    for q, want in cases:
        try:
            out = subprocess.run(
                [sys.executable, COMP_WHICH, q],
                cwd=WS, capture_output=True, text=True, timeout=30,
            ).stdout
        except Exception as exc:  # noqa: BLE001
            fails.append('"%s" -> ERROR running comp-which: %s' % (q, exc))
            continue
        ran_primitive = "running the ON-RAILS primitive" in out
        routed_right = want in out
        if ran_primitive or not routed_right:
            how = "ran grep primitive" if ran_primitive else "did not name %s" % want
            fails.append('"%s" -> expected route to %s, but %s' % (q, want, how))
    return cases, fails


def main() -> int:
    mod = _load_comp_which()
    manifest = _load_manifest()

    tools, f1 = test_backstop_reachability(mod, manifest)
    cases, f2 = test_audit_reproduction()

    print("comp-which routing regression guard (LD-0208)")
    print("  TEST 1 backstop reachability: %d/%d tools_index tools reachable via backstop"
          % (len(tools) - len(f1), len(tools)))
    for line in f1:
        print("    FAIL: %s" % line)
    print("  TEST 2 audit reproduction:   %d/%d audit cases route correctly"
          % (len(cases) - len(f2), len(cases)))
    for line in f2:
        print("    FAIL: %s" % line)

    if f1 or f2:
        print("\nRESULT: FAIL (%d reachability + %d audit regressions)" % (len(f1), len(f2)))
        return 1
    print("\nRESULT: PASS -- all %d tools reachable; all %d audit cases route correctly"
          % (len(tools), len(cases)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
