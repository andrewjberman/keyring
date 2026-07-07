"""
NFRA_COMPROUTE charter-2 -- INTENT-CONDITIONED affinity provider (the COMPLEARN-activation increment).

Extends the learned-affinity term from per-(cap,role) to per-(cap,role,INTENT-CLASS), keyed on the
route->run OUTCOME signal (comp_route_outcome: took-and-sufficed vs rejection-weighted), so the affinity
learns "has THIS role had good outcomes with THIS cap FOR THIS INTENT-CLASS" -- the intent-conditioning
CTO framed as charter-2's core (NOT w_h-sizing). Resolves the C1 finding that (cap,role)-only affinity
points at the role's FAVORITE tool, not the intent's correct tool.

CALIBRATION (folded, CTO-confirmed 20260707T110333Z -- MORE critical here, finer keys = thinner evidence):
  - MIN-N: a (cap,role,intent) with < N_MIN observations is SUPPRESSED (a 2-obs intent-affinity is noise).
  - SUPPRESS-EMPTY -> None: NEVER inject a value (esp. not a prior) from thin/absent evidence (the
    cold-start -9.1 double-count lesson) -- return None so the engine applies 0 contribution, not prior.
  NO backoff to the coarser (cap,role) grain: that would re-introduce the non-intent-conditioned
  role-favorite confound this increment exists to move past. Fire ONLY on real intent-specific evidence.

The re-gate (genuine held-out tail re-measure -> robust-positive) is the honest arbiter; this provider is
SHADOW until that cert + CTO's flip-gate.  Read-only, deterministic, ASCII.
Author: 0.8.0_AE_CloudComp~E (NFRA_COMPROUTE charter-2). 2026-07-07.
"""

from __future__ import annotations

import json
import os
from typing import Mapping, Optional

_HERE = os.path.dirname(os.path.abspath(__file__))
_WS = os.path.abspath(os.path.join(_HERE, "..", "..", ".."))
_SEP = "\t"
IC_CACHE_PATH = "org/mcp/comproute-affinity-ic-cache.json"
N_MIN = 5   # evidence threshold at the (cap,role,intent) grain (matches the (cap,role) calibration)


def emit_ic_cache(routes: list, runs: list, out_path: str = "", k: int = 5, w_rej: float = 3.0,
                  window_s: float = 300.0, classify=None) -> tuple:
    """Compute the intent-conditioned affinity cache from the route->run outcome capture."""
    from comp_route_outcome import capture_outcomes  # noqa: PLC0415
    cap = capture_outcomes(routes, runs, window_s=window_s, w_rej=w_rej, classify=classify)
    cache = {"k": k, "n_min": N_MIN, "grain": "per-(cap,role,intent_class)", "mode": "shadow",
             "signal": cap["signal"], "counts": cap["counts"], "entries": cap["entries"]}
    p = out_path or os.path.join(_WS, IC_CACHE_PATH)
    with open(p, "w", encoding="utf-8") as fh:
        json.dump(cache, fh, indent=2, sort_keys=True)
    return p, len(cache["entries"])


class IntentConditionedAffinityProvider:
    """AffinityProvider keyed on (cap_id, role, intent_class) with the min-N + suppress-empty calibration.
    affinity(cap_id, role, ctx, prior): ctx MUST carry 'intent_class'. Returns None (suppressed) when the
    (cap,role,intent) evidence is thin (< n_min) or absent -- never a prior (no cold-start double-count)."""

    def __init__(self, cache_path: str = "", k: Optional[int] = None, n_min: Optional[int] = None):
        self._c: dict = {}
        self._k = 5
        self._n_min = N_MIN if n_min is None else int(n_min)
        p = cache_path or os.path.join(_WS, IC_CACHE_PATH)
        try:
            with open(p, encoding="utf-8") as fh:
                d = json.load(fh)
            self._k = k if k is not None else int(d.get("k", 5))
            self._n_min = n_min if n_min is not None else int(d.get("n_min", N_MIN))
            self._c = d.get("entries", {})
        except Exception:  # noqa: BLE001 -- no cache -> every cap suppresses (safe cold-start)
            self._c = {}

    def affinity(self, cap_id: str, role: str, ctx: Mapping, prior: Optional[float] = None) -> Optional[float]:
        ic = str((ctx or {}).get("intent_class", "") or "")
        e = self._c.get(f"{cap_id}{_SEP}{role or ''}{_SEP}{ic}")
        n = float(e.get("n", 0)) if e else 0.0
        if n < self._n_min:
            return None                        # thin/absent intent-specific evidence -> SUPPRESS (never prior)
        p = prior if prior is not None else 0.5
        return (e["sum"] + self._k * p) / (n + self._k)


def _self_test() -> bool:
    ok = True

    def ck(name, cond):
        nonlocal ok
        print("  [%s] %s" % ("PASS" if cond else "FAIL", name))
        ok = ok and cond

    A = "0.8.0_AE_CloudComp~E"
    import tempfile

    def route(cap, t, ic):
        return {"ranked": [{"id": cap}], "role": "AE", "intent_class": ic, "serial": A, "ts_epoch": t, "kind": "decision"}

    def run(tool, t):
        return {"tool": tool, "ts_epoch": t, "serial": A}

    # Build a cache: comp-freshness took-and-sufficed 6x for intent_class 'read' (>= n_min).
    routes, runs = [], []
    for i in range(6):
        routes.append(route("comp-freshness", 100 + i * 1000, "read"))
        runs.append(run("comp-freshness", 130 + i * 1000))
    fd, tmp = tempfile.mkstemp(suffix=".json")
    os.close(fd)
    emit_ic_cache(routes, runs, out_path=tmp)
    prov = IntentConditionedAffinityProvider(cache_path=tmp)

    a_read = prov.affinity("comp-freshness", "AE", {"intent_class": "read"}, prior=0.5)
    ck("well-evidenced (cap,role,read) -> value applied (n>=n_min)", a_read is not None and a_read > 0.5)

    # DIFFERENT intent-class -> no evidence -> suppressed (the intent-conditioning: read-evidence != navigate).
    a_nav = prov.affinity("comp-freshness", "AE", {"intent_class": "navigate"}, prior=0.5)
    ck("same cap, DIFFERENT intent-class -> suppressed (None)", a_nav is None)

    # Thin evidence (< n_min) -> suppressed, never prior (the cold-start fix).
    thin = [route("comp-blast", 5, "read"), route("comp-blast", 2000, "read")]
    thinr = [run("comp-blast", 30), run("comp-blast", 2030)]
    fd2, tmp2 = tempfile.mkstemp(suffix=".json")
    os.close(fd2)
    emit_ic_cache(thin, thinr, out_path=tmp2)
    a_thin = IntentConditionedAffinityProvider(cache_path=tmp2).affinity("comp-blast", "AE", {"intent_class": "read"}, prior=0.7)
    ck("thin evidence (n<n_min) -> suppressed None, NOT prior", a_thin is None)

    # Missing cache -> safe suppress.
    safe = IntentConditionedAffinityProvider(cache_path=os.path.join(_WS, "nope.json"))
    ck("missing cache -> None (safe)", safe.affinity("x", "AE", {"intent_class": "read"}, prior=0.3) is None)

    for f in (tmp, tmp2):
        try:
            os.unlink(f)
        except OSError:
            pass
    print("OK: all checks pass" if ok else "FAIL")
    return ok


if __name__ == "__main__":
    import sys
    if "--self-test" in sys.argv:
        sys.exit(0 if _self_test() else 1)
    print("comp_route_affinity_ic: intent-conditioned affinity provider (charter-2). --self-test to verify.")
