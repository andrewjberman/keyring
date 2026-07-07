"""
NFRA_COMPROUTE charter-2 -- route->run OUTCOME CAPTURE (the intent-conditioning SIGNAL).

The live flywheel captured route DECISIONS but outcome=None (749/749) -- no route-RESOLUTION signal. This
module derives one by JOINING each route (comp-which surfaced cap X for agent A at ts T, now stamped with
serial+ts_epoch, charter-2 step-1) to A's subsequent comp-tool RUNS (the rolling corpus, keyed
serial+tool+ts_epoch+result) within a task window.

THE SIGNAL (CTO GO 20260707T110333Z -- anti-compliance-confound): bare "took the suggestion" is COMPLIANCE,
and the router CAUSED the route -> training on bare-took is a self-reinforcing Goodhart loop. So:
  POSITIVE = TOOK-AND-SUFFICED : agent ran the routed cap X in the window AND did NOT fall back after
             (no comp-grep/comp-glob, no re-route, no different-comp-tool override). A correctness proxy.
  NEGATIVE = REJECTED : routed-to-X but the agent ran a FALLBACK (grep/glob) or a DIFFERENT comp-tool
             INSTEAD, or took-X-THEN-fell-back. An active OVERRIDE is GENUINE (unconfounded) -> the
             strong signal. WEIGHTED (w_rej) so the unconfounded rejection dominates the confounded took.
  NOT COUNTED : no comp-tool activity in the window (agent didn't act -> no signal; NOT a negative).
The re-gate (genuine held-out tail re-measure) is the honest arbiter -- a compliance-artifact affinity
would FAIL to improve real routing. This module only makes the training signal LESS confounded.

Output = per-(cap, role, intent_class) weighted sufficient stats {sum, n}, the charter-2 intent-conditioned
affinity input (folds the min-N + suppress-empty calibration downstream).
Read-only, deterministic, ASCII.  Author: 0.8.0_AE_CloudComp~E. 2026-07-07.
"""

from __future__ import annotations

import os
import sys
from collections import defaultdict
from typing import Optional

_HERE = os.path.dirname(os.path.abspath(__file__))
_WS = os.path.abspath(os.path.join(_HERE, "..", "..", ".."))

_FALLBACK_TOOLS = ("comp-grep", "comp-glob")   # the on-rails never-dead-end -> a fallback = the route was rejected
_SEP = "\t"


def _routed_cap(route: dict) -> str:
    """The cap comp-which SURFACED as the decision top-1 (what the agent was routed to)."""
    ranked = route.get("ranked") or []
    if ranked and isinstance(ranked[0], dict):
        return str(ranked[0].get("id", ""))
    return ""


def _role_of(route: dict) -> str:
    return str(route.get("role", "") or "")


def _intent_class_of(route: dict, classify=None) -> str:
    ic = route.get("intent_class")
    if ic:
        return str(ic)
    if classify is not None:                       # derive from the raw intent for pre-intent_class rows
        try:
            return str(classify(route.get("intent", "")) or "")
        except Exception:  # noqa: BLE001
            return ""
    return ""


def classify_route_outcome(route: dict, runs: list, window_s: float = 300.0) -> Optional[str]:
    """Join ONE route to the agent's subsequent comp-tool runs -> 'sufficed' | 'rejected' | None.
    runs: the SAME serial's comp-tool run rows [{tool, ts_epoch, ...}], any order. Window [T, T+window_s]."""
    cap = _routed_cap(route)
    t = route.get("ts_epoch")
    serial = route.get("serial", "")
    if not cap or t is None or not serial or route.get("kind") == "fallback":
        return None                                # unroutable/keyless/router-already-fell-back -> no signal
    win = sorted(
        ((float(r.get("ts_epoch", 0) or 0), str(r.get("tool", "") or "").split()[0])
         for r in runs
         if str(r.get("serial", "")) == serial and t < float(r.get("ts_epoch", 0) or 0) <= t + window_s),
        key=lambda x: x[0])
    if not win:
        return None                                # no comp-tool activity after the route -> no signal
    tools_after = [tool for _ts, tool in win]
    took_at = next((i for i, tool in enumerate(tools_after) if tool == cap), None)
    if took_at is None:
        # never ran the routed cap; ran SOMETHING else -> an override/fallback = rejection
        return "rejected"
    after_took = tools_after[took_at + 1:]
    # took X, then fell back to grep/glob or overrode to a different comp-tool -> rejected; else sufficed
    if any(tool in _FALLBACK_TOOLS or (tool.startswith("comp-") and tool != cap) for tool in after_took):
        return "rejected"
    return "sufficed"


def capture_outcomes(routes: list, runs: list, window_s: float = 300.0, w_rej: float = 3.0,
                     classify=None) -> dict:
    """Aggregate per-(cap, role, intent_class) WEIGHTED sufficient stats from the route->run join.
    sufficed -> (value 1.0, weight 1.0); rejected -> (value 0.0, weight w_rej) so the unconfounded
    rejection dominates the confounded compliance. Returns {'cap\trole\tintent_class': {sum, n}}."""
    stats: dict = defaultdict(lambda: {"sum": 0.0, "n": 0.0})
    counts = {"sufficed": 0, "rejected": 0, "no_signal": 0}
    for route in routes:
        oc = classify_route_outcome(route, runs, window_s=window_s)
        if oc is None:
            counts["no_signal"] += 1
            continue
        counts[oc] += 1
        cap, role, ic = _routed_cap(route), _role_of(route), _intent_class_of(route, classify)
        key = f"{cap}{_SEP}{role}{_SEP}{ic}"
        val, wt = (1.0, 1.0) if oc == "sufficed" else (0.0, float(w_rej))
        stats[key]["sum"] += val * wt
        stats[key]["n"] += wt
    return {"entries": {k: {"sum": round(v["sum"], 4), "n": round(v["n"], 4)} for k, v in stats.items()},
            "grain": "per-(cap,role,intent_class)", "signal": "took-and-sufficed(+1) vs rejected(0, w=%s)" % w_rej,
            "window_s": window_s, "counts": counts}


def _self_test() -> bool:
    """Constructed routes+runs proving the took-and-sufficed / rejection / no-signal logic (pre-accrual)."""
    ok = True

    def ck(name, cond):
        nonlocal ok
        print("  [%s] %s" % ("PASS" if cond else "FAIL", name))
        ok = ok and cond

    A = "0.8.0_AE_CloudComp~E"
    def route(cap, t, ic="read"):
        return {"ranked": [{"id": cap}], "role": "AE", "intent_class": ic, "serial": A, "ts_epoch": t, "kind": "decision"}
    def run(tool, t, serial=A):
        return {"tool": tool, "ts_epoch": t, "serial": serial}

    # 1. took-and-sufficed: routed comp-freshness, ran it, no fallback after.
    r = capture_outcomes([route("comp-freshness", 100)], [run("comp-freshness", 130)])
    ck("took-and-sufficed -> 1 sufficed", r["counts"]["sufficed"] == 1 and r["counts"]["rejected"] == 0)

    # 2. rejected (override): routed comp-freshness, ran a DIFFERENT comp-tool instead.
    r = capture_outcomes([route("comp-freshness", 100)], [run("comp-blast", 130)])
    ck("override-to-different-tool -> 1 rejected", r["counts"]["rejected"] == 1 and r["counts"]["sufficed"] == 0)

    # 3. rejected (fallback): routed comp-freshness, ran comp-grep (fell back).
    r = capture_outcomes([route("comp-freshness", 100)], [run("comp-grep", 130)])
    ck("fallback-to-grep -> 1 rejected", r["counts"]["rejected"] == 1)

    # 4. took-then-fell-back -> rejected.
    r = capture_outcomes([route("comp-freshness", 100)], [run("comp-freshness", 120), run("comp-grep", 140)])
    ck("took-then-fellback -> 1 rejected", r["counts"]["rejected"] == 1 and r["counts"]["sufficed"] == 0)

    # 5. no comp-tool activity in window -> NOT counted.
    r = capture_outcomes([route("comp-freshness", 100)], [run("comp-freshness", 9999)])
    ck("no-activity-in-window -> no_signal", r["counts"]["no_signal"] == 1)

    # 6. rejection weighting: 1 sufficed + 1 rejected on the same key -> mean < 0.5 (rejection dominates).
    r = capture_outcomes([route("comp-freshness", 100), route("comp-freshness", 500)],
                         [run("comp-freshness", 130), run("comp-grep", 530)], w_rej=3.0)
    e = list(r["entries"].values())[0]
    mean = e["sum"] / e["n"]
    ck("rejection-weighted: 1suff+1rej -> mean=%.3f < 0.5" % mean, mean < 0.5)

    # 7. cross-serial isolation: a run by a DIFFERENT agent does not count.
    r = capture_outcomes([route("comp-freshness", 100)], [run("comp-freshness", 130, serial="9.9.9_XX")])
    ck("cross-serial run ignored -> no_signal", r["counts"]["no_signal"] == 1)

    print("OK: all checks pass" if ok else "FAIL: some checks failed")
    return ok


def accrual_check(routes: list, runs: list, k_ready: int = 20, n_min: int = 5,
                  classify=None) -> dict:
    """Charter-2 re-measure TRIGGER (COO 20260707T111717Z: err toward MORE evidence -- a thin corpus ->
    noisy tail-measure -> wrong flip). READY when the accrued route->run corpus has >= k_ready evidenced
    (cap,role,intent) triples (n >= n_min) -- AND, the sharper criterion, enough that INTERSECT the tail
    corpus's (cap,intent-class) targets (else the affinity has nothing to tie-break ON the tail, so the
    sign can't move regardless of raw count). NOT a manual poll: run this from a periodic sweep (COO
    /drive); on READY -> emit the IC cache + re-run --tail/--rank -> RAVC CVO the re-gate."""
    cap = capture_outcomes(routes, runs, classify=classify)
    evidenced = [key for key, v in cap["entries"].items() if v.get("n", 0) >= n_min]
    tail_targets = set()
    try:                                             # tail (cap,intent-class) targets, best-effort
        sys.path.insert(0, _HERE)
        import comp_route_eval as _ev
        _cls = classify
        for q, accept in getattr(_ev, "_TAIL", []):
            ic = _cls(q) if _cls else ""
            for c in accept:
                tail_targets.add(f"{c}{_SEP}{ic}")
    except Exception:  # noqa: BLE001
        pass
    tail_hits = sum(1 for key in evidenced
                    if _SEP.join([key.split(_SEP)[0], key.split(_SEP)[2]]) in tail_targets) if tail_targets else None
    ready = len(evidenced) >= k_ready and (tail_hits is None or tail_hits >= max(3, k_ready // 4))
    return {
        "joined_outcomes": cap["counts"], "evidenced_triples_n_ge_%d" % n_min: len(evidenced),
        "k_ready": k_ready, "tail_relevant_evidenced": tail_hits,
        "READY": ready,
        "verdict": ("READY -> emit IC cache + re-run --tail/--rank -> RAVC CVO the re-gate" if ready else
                    "NOT-READY -> keep accruing (%d/%d evidenced triples%s); re-check from the periodic sweep"
                    % (len(evidenced), k_ready,
                       "" if tail_hits is None else ", %s tail-relevant" % tail_hits)),
    }


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        sys.exit(0 if _self_test() else 1)
    # live: join the recent routes (post charter-2 step-1 emission fix) to the rolling run corpus.
    sys.path.insert(0, _HERE)
    sys.path.insert(0, os.path.join(_WS, "infra", "aws", "globgrph"))
    import json
    routes = []
    rp = os.path.join(_WS, "org", "mcp", "comproute-routing.jsonl")
    if os.path.exists(rp):
        for line in open(rp, encoding="utf-8"):
            line = line.strip()
            if not line:
                continue
            try:
                routes.append(json.loads(line))
            except Exception:  # noqa: BLE001
                pass
    runs = []
    try:
        from comp_learns_score import load_corpus
        runs = list(load_corpus().get("rolling", []))
    except Exception:  # noqa: BLE001
        pass
    classify = None
    try:
        import comp_which_signals as _sig
        classify = _sig.classify_query_intent
    except Exception:  # noqa: BLE001
        pass
    joinable = [r for r in routes if r.get("ts_epoch") and r.get("serial")]
    if "--accrual-check" in sys.argv:
        res = accrual_check(joinable, runs, classify=classify)
        res["routes_joinable_post_fix"] = len(joinable)
        print(json.dumps(res, indent=1))
        sys.exit(0 if res["READY"] else 2)   # exit 2 = NOT-READY (a periodic sweep can branch on it)
    out = capture_outcomes(joinable, runs, classify=classify)
    out["routes_total"] = len(routes)
    out["routes_joinable_post_fix"] = len(joinable)
    print(json.dumps({k: v for k, v in out.items() if k != "entries"}, indent=1))
    print("entries:", len(out["entries"]))
