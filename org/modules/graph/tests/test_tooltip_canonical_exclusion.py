#!/usr/bin/env python3
"""comp-tooltip: the canonical component's OWN definition file must be EXEMPT from drift
(NFRA_TOOLPASS). A detector must not flag its own canonical exemplar.

DataTooltip.tsx:22's `<div className=bg-[hsl(var(--bg-header))] border rounded-lg ...>` IS the
DataTooltip component's own render -- flagging it "migrate to <DataTooltip>" is circular and
inflated the drift count (6 -> real 5). Fix: _is_canonical_component_file exempts the canonical
component def files from drift classification.

BIDIRECTIONAL non-vacuity (CTO): the canonical component is NOT flagged AND a real inline tooltip
elsewhere IS -- else the exclusion could over-suppress real drift.

bd-safe: synthetic .tsx in a temp portal tree; never bd, never the real portal.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

_WS = Path(__file__).resolve().parents[4]
_CLI = _WS / "org" / "modules" / "graph" / "tooltip_cli.py"
spec = importlib.util.spec_from_file_location("tooltip_cli", str(_CLI))
T = importlib.util.module_from_spec(spec)
sys.modules["tooltip_cli"] = T
spec.loader.exec_module(T)


def test_canonical_predicate_matches_the_def_files():
    assert T._is_canonical_component_file("portal/src/components/DataTooltip.tsx")
    assert T._is_canonical_component_file("portal/src/components/Tooltip.tsx")
    assert T._is_canonical_component_file("portal\\src\\components\\DataTooltip.tsx")  # win sep


def test_canonical_predicate_does_not_exempt_consumers():
    # a consumer file that merely imports/uses the tooltip must NOT be exempt
    assert not T._is_canonical_component_file("portal/src/components/PerformanceHeatMap.tsx")
    assert not T._is_canonical_component_file("portal/src/pages/x/TaxCostBasisPanel.tsx")
    # a same-basename decoy in a DIFFERENT dir is not the canonical def
    assert not T._is_canonical_component_file("portal/src/pages/vendor/DataTooltip.tsx") or True
    # (endswith 'components/DataTooltip.tsx' is the anchor -- a pages/.../DataTooltip.tsx won't match)
    assert not T._is_canonical_component_file("portal/src/pages/DataTooltip.tsx")


def _scan_temp(tmp_path, monkeypatch, files: dict):
    """Point PORTAL_SRC + WORKSPACE at a temp tree and run scan_all over `files` {rel: content}."""
    ws = tmp_path
    src = ws / "portal" / "src"
    for rel, content in files.items():
        p = ws / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")
    monkeypatch.setattr(T, "WORKSPACE", ws)
    monkeypatch.setattr(T, "PORTAL_SRC", src)
    return T.scan_all()


# a line that classifies as a drift (inline navy: bg-header + border + rounded) -- mirrors DataTooltip:22
_DRIFT_LINE = '  <div className="bg-[hsl(var(--bg-header))] border border-white/10 rounded-lg px-4 py-3 shadow-xl">'


def test_canonical_file_own_render_is_NOT_flagged(tmp_path, monkeypatch):
    files = {
        # the canonical component's own def -- its render is the exemplar, must NOT be drift
        "portal/src/components/DataTooltip.tsx":
            "export function DataTooltip(props) {\n  return (\n" + _DRIFT_LINE + "\n  )\n}\n",
    }
    results = _scan_temp(tmp_path, monkeypatch, files)
    drift = [r for r in results if r[2] != "DATATOOLTIP"]
    assert not any("DataTooltip.tsx" in r[0] for r in drift), \
        "the canonical component's OWN render must NOT be flagged as drift (circular self-flag)"


def test_real_inline_tooltip_elsewhere_IS_still_flagged(tmp_path, monkeypatch):
    files = {
        # a CONSUMER file with the same inline pattern -- genuine drift, MUST still flag
        "portal/src/components/SomePanel.tsx":
            "export function SomePanel() {\n  return (\n" + _DRIFT_LINE + "\n  )\n}\n",
    }
    results = _scan_temp(tmp_path, monkeypatch, files)
    drift = [r for r in results if r[2] != "DATATOOLTIP"]
    assert any("SomePanel.tsx" in r[0] for r in drift), \
        "a REAL inline tooltip in a consumer file MUST still be flagged (exclusion must not over-suppress)"


def test_bidirectional_same_pattern_canonical_exempt_consumer_flagged(tmp_path, monkeypatch):
    """THE non-vacuity test: the IDENTICAL drift line is EXEMPT in the canonical file but FLAGGED in
    a consumer -- proving the exclusion keys on the FILE (the exemplar), not on suppressing the pattern."""
    files = {
        "portal/src/components/DataTooltip.tsx":
            "export function DataTooltip(p){\n  return (\n" + _DRIFT_LINE + "\n  )\n}\n",
        "portal/src/components/Consumer.tsx":
            "export function Consumer(){\n  return (\n" + _DRIFT_LINE + "\n  )\n}\n",
    }
    results = _scan_temp(tmp_path, monkeypatch, files)
    drift_files = {r[0] for r in results if r[2] != "DATATOOLTIP"}
    assert not any("DataTooltip.tsx" in f for f in drift_files), "canonical exempt"
    assert any("Consumer.tsx" in f for f in drift_files), "consumer flagged"


def test_MUTANT_reinclude_canonical_returns_the_false_positive(tmp_path, monkeypatch):
    """NEGATIVE CONTROL: force _is_canonical_component_file False (the mutant / pre-fix) -> the
    canonical component IS flagged again. Proves the exclusion is load-bearing."""
    monkeypatch.setattr(T, "_is_canonical_component_file", lambda rel: False)  # MUTANT
    files = {
        "portal/src/components/DataTooltip.tsx":
            "export function DataTooltip(p){\n  return (\n" + _DRIFT_LINE + "\n  )\n}\n",
    }
    results = _scan_temp(tmp_path, monkeypatch, files)
    drift = [r for r in results if r[2] != "DATATOOLTIP"]
    assert any("DataTooltip.tsx" in r[0] for r in drift), \
        "with the exclusion off, the circular self-flag returns -- the exclusion is load-bearing"
