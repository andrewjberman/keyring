"""NFRA_LIVELEARN CYCLE-A.1 (F2) -- the commission GATE defaults to the EFFECTIVE feed, READ-ONLY.

CTO~D gate contract (2026-07-12): comp_tool_health_gate must default to DEFAULT_EFFECTIVE_FEED (Ga, so
the commission gate decides on the same EFFECTIVE axis as comp-tool-health, not the 2-axis skeleton) BUT
never refresh on the gate path (Gb -- a decision gate is a hot path; a live full-corpus probe there is the
probe-storm G1 guarded against). Staleness is VISIBLE via a pure feed_age_days READ (Gc), never a run.

Hermetic: build_commissions/health stubbed; tool_probe.ensure_fresh + probe_all SPIED to prove 0 calls.

# rail-checked: assurance oracle for the comp-tool-health-gate read-only feed wire under test (NFRA_LIVELEARN CYCLE-A.1)
Author: 0.8.0_AE_CloudComp.
"""
from __future__ import annotations

import importlib.util
import json
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_WS = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(_HERE))))
_GATE = os.path.join(_WS, "org", "modules", "graph", "comp_tool_health_gate.py")
_spec = importlib.util.spec_from_file_location("comp_tool_health_gate_a1", _GATE)
gate = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(gate)


class _Spy:
    def __init__(self, ret=None):
        self.calls = []
        self.ret = ret

    def __call__(self, *a, **k):
        self.calls.append((a, k))
        return self.ret


def _minimal_ledger(effective_feed=None):
    return {"n_commissions": 0, "commissions": [], "corpus_source": "c"}


def test_Gd_i_stale_default_feed_read_but_NO_probe(monkeypatch, capsys):
    # Ga: default to the EFFECTIVE feed. Gc: staleness visible. Gb: the gate NEVER refreshes.
    import org.modules.graph.compproof.tool_probe as tp
    ef, pa = _Spy(), _Spy()
    monkeypatch.setattr(tp, "ensure_fresh", ef)
    monkeypatch.setattr(tp, "probe_all", pa)
    monkeypatch.setattr(tp, "feed_age_days", lambda *a, **k: 10.0)      # stale (> 7d)
    monkeypatch.setattr(gate.th, "load_effective_feed", lambda p: {})
    monkeypatch.setattr(gate, "build_commissions", _minimal_ledger)
    monkeypatch.setattr(gate.sys, "argv", ["comp-tool-health-gate", "--json"])
    rc = gate.main()
    led = json.loads(capsys.readouterr().out)
    assert rc == 0
    assert led["feed_freshness"]["feed_path"] == gate.th.DEFAULT_EFFECTIVE_FEED, \
        "Ga: absent --effective-feed defaults to the EFFECTIVE feed (same axis as comp-tool-health)"
    assert led["feed_freshness"]["stale"] is True and led["feed_freshness"]["read_only"] is True, \
        "Gc: staleness visible in the ledger; read-only"
    assert ef.calls == [] and pa.calls == [], \
        "Gb: the gate NEVER refreshes -- 0 ensure_fresh / probe_all calls on the gate path"


def test_Gd_ii_explicit_effective_feed_honored(monkeypatch, capsys):
    import org.modules.graph.compproof.tool_probe as tp
    monkeypatch.setattr(tp, "feed_age_days", lambda *a, **k: 1.0)
    monkeypatch.setattr(gate.th, "load_effective_feed", lambda p: {})
    monkeypatch.setattr(gate, "build_commissions", _minimal_ledger)
    monkeypatch.setattr(gate.sys, "argv",
                        ["comp-tool-health-gate", "--json", "--effective-feed", "/tmp/x.json"])
    gate.main()
    led = json.loads(capsys.readouterr().out)
    assert led["feed_freshness"]["feed_path"] == "/tmp/x.json", \
        "an explicit --effective-feed is honored, never overridden by the default"


def test_Gd_iii_absent_feed_pending_no_crash(monkeypatch, capsys):
    import org.modules.graph.compproof.tool_probe as tp  # noqa: F401 (imported for symmetry / patch scope)
    monkeypatch.setattr(gate.th, "load_effective_feed", lambda p: {})
    monkeypatch.setattr(gate.th, "DEFAULT_EFFECTIVE_FEED", "/no/such/effective_feed.json")  # absent
    monkeypatch.setattr(gate, "build_commissions", _minimal_ledger)
    monkeypatch.setattr(gate.sys, "argv", ["comp-tool-health-gate", "--json"])
    rc = gate.main()
    led = json.loads(capsys.readouterr().out)
    assert rc == 0, "absent feed -> no crash"
    assert led["feed_freshness"]["feed_path"] is None and led["feed_freshness"]["age_days"] is None, \
        "absent feed -> None path/age (EFFECTIVE pending, 2-axis skeleton -- never a silent False)"
    assert led["feed_freshness"]["stale"] is True, "no feed = infinitely stale (still no probe)"
