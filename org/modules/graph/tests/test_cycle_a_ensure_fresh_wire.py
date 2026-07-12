"""NFRA_LIVELEARN CYCLE A -- the consumption-driven ensure_fresh WIRE, exercised HERMETICALLY.

AC1/G1 is a WIRE property (CTO~D GO 2026-07-12, contract W1-W6): does comp-tool-health trigger
refresh-or-flag BEFORE reading the EFFECTIVE feed, on the correct (DEFAULT-feed) branch, with staleness
NEVER silent on any path, refresh-failure LOUD (never silent-fresh), and the sovereign LOAD-assert on the
refresh path? Provable with an injected fake probe/age -- NO live full-corpus estate probe during dev/test.

Hermetic, bd-safe: the fake `_ensure`/`_age` replace the live run; the sovereign guard is exercised as a
pure unit (assert_sovereign_safe on a seeded held target), never a real bd read.

# rail-checked: assurance oracle for the comp-tool-health CYCLE-A freshness wire under test (NFRA_LIVELEARN G1)
Author: 0.8.0_AE_CloudComp.
"""
from __future__ import annotations

import contextlib
import importlib.util
import io
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_WS = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(_HERE))))
_MODULE = os.path.join(_WS, "org", "modules", "graph", "comp_tool_health.py")
_spec = importlib.util.spec_from_file_location("comp_tool_health_cyclea", _MODULE)
th = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(th)


class _Spy:
    """A stand-in for tool_probe.ensure_fresh -- records kwargs, returns a canned result or raises."""
    def __init__(self, ret=None, raises=None):
        self.calls = []
        self.ret = ret if ret is not None else {"ran": True, "reason": "ran fresh (fake)"}
        self.raises = raises

    def __call__(self, **kw):
        self.calls.append(kw)
        if self.raises is not None:
            raise self.raises
        return self.ret


def _run(refresh, no_refresh, age, ensure):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rep = th._ensure_feed_fresh(refresh, no_refresh, _age=(lambda *a, **k: age), _ensure=ensure)
    return rep, buf.getvalue()


def test_V_fresh_within_ceiling_reuses_no_run():
    spy = _Spy()
    rep, _out = _run(False, False, 3.0, spy)          # 3d <= 7d ceiling
    assert rep["stale"] is False and rep["ran"] is False
    assert spy.calls == [], "W2: a fresh feed must NOT trigger a probe run"


def test_V_stale_auto_refresh_visible_banner_before_run():
    spy = _Spy(ret={"ran": True, "reason": "stale -- ran fresh"})
    rep, out = _run(False, False, 10.0, spy)          # 10d > 7d ceiling
    assert rep["stale"] is True and rep["ran"] is True and rep["refreshed"] is True
    assert len(spy.calls) == 1, "W3: stale default path runs exactly one refresh"
    assert "running fresh probe" in out.lower(), "W3: a VISIBLE pre-run banner is on stdout"
    assert spy.calls[0].get("corpus") is None, "W6: ensure called with corpus=None (sovereign LOAD-assert path)"
    assert spy.calls[0].get("force") is True, "an already-decided run forces the probe"


def test_V_stale_no_refresh_loud_banner_no_run():
    spy = _Spy()
    rep, out = _run(False, True, 10.0, spy)           # stale + --no-refresh
    assert rep["stale"] is True and rep["ran"] is False
    assert spy.calls == [], "--no-refresh must NOT run a probe"
    assert "stale" in out.lower() and "outdated" in out.lower(), \
        "W3: staleness is NEVER silent -- a LOUD banner on stdout even when not refreshing"


def test_V_fail_loud_serves_existing_no_crash():
    spy = _Spy(raises=RuntimeError("S3 timeout (simulated)"))
    rep, out = _run(False, False, 10.0, spy)          # stale -> tries to run -> raises
    assert rep["failed"] is True and rep["ran"] is False, "W5: never a silent-fresh on failure"
    assert "refresh failed" in out.lower() and "serving existing feed" in out.lower(), \
        "W5: refresh failure is LOUD + serves the existing feed"


def test_V_fresh_forced_by_refresh_flag_runs():
    # --refresh forces the run even within the ceiling (W3 --refresh), with an honest 'within ceiling' banner.
    spy = _Spy(ret={"ran": True, "reason": "forced"})
    rep, out = _run(True, False, 2.0, spy)            # 2d (fresh) but --refresh
    assert rep["stale"] is True and rep["ran"] is True, "--refresh forces the stale (run) path"
    assert len(spy.calls) == 1 and "within ceiling" in out.lower()


def test_V_sovereign_guard_voids_held_bd_target():
    # W6: the guard reachable from the wire (assert_sovereign_safe, called by tool_corpus.probes()) VOIDs a
    # held bd/schwab target -- so an auto-refresh can never silently read opal-data-bd.
    from org.modules.graph.compproof import tool_corpus as tc
    held = {"probe_id": "seed/held", "run": ["comp-x", "s3://opal-data-bd/49f-served-aua/x.json"]}
    raised = False
    try:
        tc.assert_sovereign_safe([held])
    except ValueError as e:
        raised = "SOVEREIGN" in str(e)
    assert raised, "the sovereign LOAD-assert MUST raise on a held bd target (never a silent bd read)"
    # non-vacuous negative control: an inf (in-scope) target does NOT raise
    tc.assert_sovereign_safe([{"probe_id": "seed/ok", "run": ["comp-x", "s3://opal-data-inf/x.json"]}])


def test_W1_refresh_only_on_default_feed_branch(monkeypatch):
    # W1: main() ensures freshness ONLY on the default-feed branch; an explicit --effective-feed is NEVER refreshed.
    calls = []
    monkeypatch.setattr(th, "_ensure_feed_fresh",
                        lambda refresh, no_refresh, **k: (calls.append((refresh, no_refresh)) or
                        {"age_days": 1.0, "stale": False, "ran": False, "refreshed": False,
                         "failed": False, "ceiling_days": 7.0}))
    monkeypatch.setattr(th, "load_effective_feed", lambda p: {})
    monkeypatch.setattr(th, "health", lambda **k: {"tools": [], "phase": "", "corpus_source": "",
                        "value_metric": "", "rail_enforcement": {"available": False}, "verdict_counts": {}})
    monkeypatch.setattr(th, "_render", lambda h, verdict_filter=None: "")
    monkeypatch.setattr(th.sys, "argv", ["comp-tool-health", "--effective-feed", "x.json"])
    th.main()
    assert calls == [], "W1: an explicit --effective-feed must NOT auto-refresh"
    monkeypatch.setattr(th.sys, "argv", ["comp-tool-health"])
    th.main()
    assert len(calls) == 1 and calls[0] == (False, False), \
        "W1: the DEFAULT-feed branch MUST ensure freshness before the read"


def test_F1_json_mode_stdout_stays_valid_json_banner_on_stderr(monkeypatch, capsys):
    # F1 REGRESSION (CTO~D gate, a0c995f4d break): on a STALE day, `comp-tool-health --json | jq` must
    # not break. The wire printed the W3 banner to STDOUT before json.dumps -> a raw line ahead of the
    # JSON. FIX: in --json mode banners route to STDERR; the same staleness facts live in
    # h["feed_freshness"] IN the JSON, so "staleness never silent" holds on BOTH channels. This test
    # would have caught F1 and prevents its return. (Hermetic: fake age+ensure, no live estate probe.)
    import json
    import org.modules.graph.compproof.tool_probe as tp
    monkeypatch.setattr(tp, "feed_age_days", lambda *a, **k: 10.0)                  # stale (> 7d)
    monkeypatch.setattr(tp, "ensure_fresh", lambda **k: {"ran": True, "reason": "stale -- ran (fake)"})
    monkeypatch.setattr(th, "load_effective_feed", lambda p: {})
    monkeypatch.setattr(th, "health", lambda **k: {"tools": [], "phase": "P", "corpus_source": "c",
                        "value_metric": "v", "rail_enforcement": {"available": False}, "verdict_counts": {}})
    monkeypatch.setattr(th.sys, "argv", ["comp-tool-health", "--json"])
    th.main()
    cap = capsys.readouterr()
    # THE regression: stdout must be pure, parseable JSON -- a raw banner line before it breaks json.loads/jq.
    assert cap.out.lstrip().startswith("{"), "stdout must start with JSON, no leading banner line"
    parsed = json.loads(cap.out)
    # staleness is NEVER silent on the machine channel -- it lives IN the JSON (feed_freshness)
    assert parsed["feed_freshness"]["stale"] is True and parsed["feed_freshness"]["refreshed"] is True
    # ...and the human banner is on STDERR, not polluting stdout
    assert "running fresh probe" in cap.err.lower(), "W3 banner routed to stderr in --json mode"
