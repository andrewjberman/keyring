"""comp_coverage_view.py -- the tools_index GENERATED VIEW projector (NFRA_COMPUNIFY S1, CTO ruling #1).

comp-coverage-map.yaml is the SOURCE OF TRUTH for the comp-tool inventory + each tool's
(surface|seam) x granularity x concern home. graph-call-manifest.yaml's flat tools_index is a
REGENERATED PROJECTION of it -- ONE catalog, never a second hand-maintained one.

This module:
  - emit()    -- project the ledger into the tool-inventory view (tool -> home/concern, or role).
  - verify()  -- the NON-BREAKING guard: every tool in the manifest tools_index MUST exist in the
                 ledger union(tools, meta_tools); a manifest tool absent from the ledger is drift.

Read-only. No mutation of the manifest (the operational fields -- does/subcommands/entries/routing/
examples -- stay there; only the INVENTORY is a ledger projection). Run `--verify` in CI / at S2
gate time to keep the two in lockstep.

Usage:
  comp_coverage_view.py            # print the projection (YAML) to stdout
  comp_coverage_view.py --verify   # exit 0 if manifest tools_index subset-of ledger; 2 on drift
"""

from __future__ import annotations

import os
import sys

import yaml

_HERE = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(_HERE, "comp-coverage-map.yaml")
MANIFEST = os.path.join(_HERE, "graph-call-manifest.yaml")


def _load(path: str) -> dict:
    with open(path, encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


def project(ledger: dict) -> dict:
    """Project the ledger into the tool-inventory view the manifest tools_index regenerates from."""
    view: dict = {}
    for t in ledger.get("tools", []):
        home = t.get("surface") or t.get("seam")
        view[t["tool"]] = {
            "home": home,
            "granularity": t.get("granularity"),
            "concern": t.get("concern"),
        }
    for m in ledger.get("meta_tools", []):
        view[m["tool"]] = {"home": "meta", "role": m.get("role")}
    return view


def emit() -> int:
    view = project(_load(LEDGER))
    sys.stdout.write(yaml.safe_dump({"tools_index_view": view}, sort_keys=True, width=120))
    return 0


def verify() -> int:
    ledger = _load(LEDGER)
    union = {t["tool"] for t in ledger.get("tools", [])} | {
        m["tool"] for m in ledger.get("meta_tools", [])
    }
    manifest = _load(MANIFEST)
    inventory = set(manifest.get("tools_index", {}).keys())
    lost = sorted(inventory - union)
    if lost:
        sys.stderr.write(
            "DRIFT: manifest tools_index carries tool(s) absent from the ledger "
            "(would be LOST in regeneration): " + ", ".join(lost) + "\n"
        )
        return 2
    sys.stdout.write(
        "OK: all %d manifest tools_index entries present in the ledger union (%d tools); "
        "regeneration is non-breaking.\n" % (len(inventory), len(union))
    )
    return 0


def main(argv: list[str]) -> int:
    if "--verify" in argv:
        return verify()
    return emit()


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
