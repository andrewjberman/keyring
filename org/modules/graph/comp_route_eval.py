"""
NFRA_COMPPROOF C1 -- COMPROUTE efficacy eval (precision@1 / recall), Goodhart-gated, dual-arm.

Answers the Andrew-facing C1 question: does the DEFAULT ROUTER (comp_route.route + ~C's
SignalExtractors -- the live comp-which default since the DR2 flip 94b64a5af) route an agent's
REAL question to the CORRECT comp-tool? And does turning the LEARNED AFFINITY on (the DRV-flip
= affinity-on-2nd-flip) IMPROVE that without regressing the E1 structural safety gate?

ALIGNED-BY-CONSTRUCTION with the DRV shadow: reuses comp_route_shadow's fixture gather + the exact
router path (same route() + extractors + intent classifier). This eval ADDS the scoring layer the
shadow lacks -- precision@1 vs recall, a Goodhart tier-split, and the affinity OFF/ON A/B -- so ONE
affinity-on pass feeds BOTH the DRV-flip cert AND C1 (COO TO 20260707T054922Z).

METRICS (computed per TIER, per ARM):
  precision@1  = fraction of cases whose TOP-1 routed cap is a correct cap (strict).
  recall@surf  = fraction whose correct cap is SURFACED (top-1 OR within-margin disambiguation) -- a
                 defensible-but-not-top-1 route still earns recall credit.
  struct_gate  = read/navigate-intent-NEVER-surfaces-a-write_path-cap compliance (E1). NON-NEGOTIABLE:
                 must be 1.0 in EVERY arm; ONE leak blocks the flip regardless of precision (POTION
                 3-criterion gate #2).
  fallback_rate= fraction routed to comp-grep/glob (the on-rails never-dead-end). Context, not pass/fail.

CORPUS TIERS (the Goodhart honesty split -- WHY the headline is held-out, not canonical):
  CANON     -- self-route: each tool queried by its OWN richest use_case sentence. NEAR-TAUTOLOGICAL
               (the fixture the router is developed against; the routing-test docstring says so). A
               ceiling. Reported, NEVER the headline.
  DIVERSE   -- paraphrase + the 3 audit cases: real-agent phrasings worded UNLIKE the manifest. The
               floor the router is actually held to today.
  HELD-OUT  -- novel intents the router was NOT tuned against (this file, ~E-authored) + the E1 bucket
               phrasings. THE HONEST HEADLINE. You cannot call a router "precise" off the tier it was
               fit to. CAVEAT: held-out labels are author-provided; the CVO honesty-gate should bless
               or re-label a held-out set for the official cert (invited, not assumed).

ARMS:
  OFF -- affinity_provider=None                         (today's LIVE comp-which config)
  ON  -- CachedAffinityProvider(live emitted cache)     (the DRV-flip target config)
  The affinity term is per-(cap_id, ROLE); the ON arm is evaluated at --role (default AE) so it can
  actually fire (role="" cold-starts). Live comp-which passes the caller's real role.

EXERCISE-GATE (CVO): actually invokes route() on every corpus query and scores real output; writes a
report. Not "the eval code exists" -- the router evaluates + routes on real queries.

Run from workspace root:
  python org/modules/graph/comp_route_eval.py [--arm off|on|both] [--role AE] [--json] [--verbose]
  python org/modules/graph/comp_route_eval.py --self-test
Read-only, deterministic, ASCII-only.
Author: 0.8.0_AE_CloudComp~E (NFRA_COMPPROOF C1). 2026-07-07.
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_WS = os.path.abspath(os.path.join(_HERE, "..", "..", ".."))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import comp_route_shadow as _sh                     # noqa: E402  (fixture + router path substrate)
from comp_route_affinity import CachedAffinityProvider  # noqa: E402

_REPORT = os.path.join(_HERE, "compproof", "comproute_c1_report.json")

# ---------------------------------------------------------------------------------------------------
# HELD-OUT corpus (~E-authored; the router was NOT developed against these). Labels are SETS -- any
# member is a correct top-1 (avoids false-misses on genuinely near-equivalent tools, e.g. graph reads).
# tier "heldout" cases are precision+recall+struct scored; "heldout-e1" cases are STRUCT-ONLY (the
# "which read tool is correct" is intentionally not asserted -- only that a READ never surfaces a
# write_path/rebuild cap, the E1 safety invariant, holds for the bucket phrasings).
# ---------------------------------------------------------------------------------------------------
_HELDOUT = [
    ("did last night's gold job actually publish new numbers or is it stale", {"comp-freshness"}),
    ("if I rename this gold helper function what portal pages break", {"comp-blast"}),
    ("does the inflection lambda even have permission to write its output bucket", {"comp-iam"}),
    ("could this new holdings column expose a client social security number on the site", {"comp-pii"}),
    ("the endpoint hands back an html error page instead of the json I expected", {"comp-routes"}),
    ("which cached queries go stale when a client's holdings change", {"comp-cache"}),
    ("what fields does the positions gold script write and which dashboards read them",
     {"comp-pipescript"}),
    ("this portal card renders undefined, is a field missing from the transform", {"comp-transform"}),
    ("before I tell AE the run is good, check the served artifact invariants", {"comp-validate"}),
    ("trace how this ticker symbol connects across the whole estate graph", {"comp-kuzu", "comp-blast"}),
]
_HELDOUT_E1 = [
    "what lambdas read from the opal-data-bd bucket",
    "what reads from the opal-data-bd bucket",
    "which functions consume the cot silver tables",
]


def _route_arm(intent, provider, affinity_provider, role):
    """The router path, identical to comp_route_shadow._primary EXCEPT the affinity arm + role vary.
    A clean A/B: same extractors, same intent classifier, same route() engine."""
    ic = _sh.sig.classify_query_intent(intent)
    ctx = {"role": role, "working_set": [], "trajectory": [], "intent_class": ic}
    r = _sh.comp_route.route(intent, ctx, provider, affinity_provider=affinity_provider,
                             extractors=_sh.sig.EXTRACTORS)
    return r, ic


def _surfaced(r):
    within = [s.cap.id for s in r.within_margin]
    top = r.ranked[0].cap.id if r.ranked else None
    return top, (set(within) | ({top} if top else set()))


def _labeled_cases():
    """Assemble (query, accept_set|None, tier) across all tiers.
    CANON=self, DIVERSE=paraphrase+audit (from the shared shadow fixture), HELD-OUT=this file."""
    cases = []
    for q, expect, kind in _sh._gather_cases():
        tier = "canon" if kind == "self" else "diverse"
        cases.append((q, {expect} if expect else None, tier, kind))
    for q, accept in _HELDOUT:
        cases.append((q, accept, "heldout", "heldout"))
    for q in _HELDOUT_E1:
        cases.append((q, None, "heldout", "heldout-e1"))
    return cases


def _blank_tier():
    return {"n": 0, "p1_hits": 0, "recall_hits": 0, "fallbacks": 0,
            "read_cases": 0, "struct_leaks": 0, "scored": 0}


def run_arm(arm, role, verbose=False):
    """Run ONE arm ('off'|'on') over the full corpus; return per-tier aggregates + per-case rows."""
    provider = _sh.capmap.get_provider()
    cap_write = {c.id: bool(getattr(c, "write_path", False)) for c in provider.capabilities()}
    affinity_provider = CachedAffinityProvider() if arm == "on" else None
    tiers = {t: _blank_tier() for t in ("canon", "diverse", "heldout")}
    rows = []
    for q, accept, tier, kind in _labeled_cases():
        r, ic = _route_arm(q, provider, affinity_provider, role)
        top, surf = _surfaced(r)
        agg = tiers[tier]
        agg["n"] += 1
        is_fallback = (r.kind == "fallback")
        if is_fallback:
            agg["fallbacks"] += 1
        # STRUCTURAL gate (read/navigate intent must surface no write_path cap).
        leaked = False
        if ic in ("read", "navigate"):
            agg["read_cases"] += 1
            for cid in surf:
                if cap_write.get(cid, False):
                    agg["struct_leaks"] += 1
                    leaked = True
                    break
        # PRECISION / RECALL only for cases with an asserted label (skip struct-only e1 cases).
        p1 = rc = None
        if accept is not None:
            agg["scored"] += 1
            p1 = (top in accept) and not is_fallback
            rc = bool(surf & accept) and not is_fallback
            if p1:
                agg["p1_hits"] += 1
            if rc:
                agg["recall_hits"] += 1
        rows.append({"q": q[:70], "tier": tier, "kind": kind, "ic": ic, "route_kind": r.kind,
                     "top": top, "accept": sorted(accept) if accept else None,
                     "p1": p1, "recall": rc, "struct_leak": leaked})
        if verbose:
            tag = "P1" if p1 else ("RC" if rc else ("--" if accept else "st"))
            leak = " LEAK!" if leaked else ""
            print("  [%s] %-8s ic=%-8s top=%-16s exp=%-24s%s"
                  % (tag, tier, ic, top, (sorted(accept) if accept else "(struct-only)"), leak))
    return tiers, rows


def _pct(n, d):
    return round(100.0 * n / d, 1) if d else None


def _summarize(tiers):
    out = {}
    for t, a in tiers.items():
        out[t] = {
            "n": a["n"],
            "scored": a["scored"],
            "precision_at_1_pct": _pct(a["p1_hits"], a["scored"]),
            "recall_at_surf_pct": _pct(a["recall_hits"], a["scored"]),
            "fallback_rate_pct": _pct(a["fallbacks"], a["n"]),
            "read_cases": a["read_cases"],
            "struct_gate_leaks": a["struct_leaks"],
            "struct_gate_pass": (a["struct_leaks"] == 0),
        }
    return out


def evaluate(role="AE", arms=("off", "on"), verbose=False):
    result = {"role": role, "arms": {}}
    for arm in arms:
        if verbose:
            print("=== ARM: affinity-%s (role=%s) ===" % (arm.upper(), role))
        tiers, rows = run_arm(arm, role, verbose=verbose)
        result["arms"][arm] = {"tiers": _summarize(tiers), "rows": rows}
    # DRV-flip inputs: the held-out delta + the E1 structural invariant across arms.
    if "off" in result["arms"] and "on" in result["arms"]:
        off_h = result["arms"]["off"]["tiers"]["heldout"]
        on_h = result["arms"]["on"]["tiers"]["heldout"]
        p_off, p_on = off_h["precision_at_1_pct"], on_h["precision_at_1_pct"]
        struct_ok_all = all(result["arms"][a]["tiers"][t]["struct_gate_pass"]
                            for a in ("off", "on") for t in ("canon", "diverse", "heldout"))
        result["drv_flip_inputs"] = {
            "heldout_precision_at_1_off_pct": p_off,
            "heldout_precision_at_1_on_pct": p_on,
            "heldout_precision_delta_pts": (round(p_on - p_off, 1)
                                            if (p_off is not None and p_on is not None) else None),
            "affinity_on_net_gain": (p_on is not None and p_off is not None and p_on > p_off),
            "structural_gate_zero_regression": struct_ok_all,
            "note": ("DRV-flip criteria (POTION-mirror): net gain on held-out precision@1 AND zero "
                     "structural-gate leak in EITHER arm. Headline = held-out, not canon (Goodhart)."),
        }
    return result


def evaluate_roles(roles=("AE", "DS", "CTO", ""), verbose=False):
    """Role-sensitivity sweep (CTO ruling #2): the affinity term is per-(cap,ROLE), so report the
    OFF-vs-ON held-out delta at each of several representative roles + role="" (the cold-start floor).
    A role where affinity-on misroutes (or moves at all) is a finding."""
    sweep = {}
    for role in roles:
        res = evaluate(role=role or "", arms=("off", "on"), verbose=verbose)
        d = res.get("drv_flip_inputs", {})
        sweep[role or "(cold-start)"] = {
            "heldout_p1_off_pct": d.get("heldout_precision_at_1_off_pct"),
            "heldout_p1_on_pct": d.get("heldout_precision_at_1_on_pct"),
            "delta_pts": d.get("heldout_precision_delta_pts"),
            "structural_gate_zero_regression": d.get("structural_gate_zero_regression"),
        }
    return sweep


def _print_report(res):
    print("\n=== NFRA_COMPPROOF C1 -- COMPROUTE efficacy eval  (role=%s) ===" % res["role"])
    hdr = "  %-9s | %-6s | %-11s | %-11s | %-9s | %s"
    print(hdr % ("TIER", "scored", "precision@1", "recall@surf", "fallback", "struct-gate"))
    for arm in ("off", "on"):
        if arm not in res["arms"]:
            continue
        print("  -- affinity-%s --" % arm.upper())
        for t in ("canon", "diverse", "heldout"):
            s = res["arms"][arm]["tiers"][t]
            print(hdr % (t, s["scored"],
                         ("%s%%" % s["precision_at_1_pct"]) if s["precision_at_1_pct"] is not None else "n/a",
                         ("%s%%" % s["recall_at_surf_pct"]) if s["recall_at_surf_pct"] is not None else "n/a",
                         ("%s%%" % s["fallback_rate_pct"]) if s["fallback_rate_pct"] is not None else "n/a",
                         "PASS" if s["struct_gate_pass"] else ("LEAK x%d" % s["struct_gate_leaks"])))
    d = res.get("drv_flip_inputs")
    if d:
        print("\n  DRV-FLIP INPUTS (held-out tier, the honest headline):")
        print("    precision@1  off=%s%%  on=%s%%  delta=%s pts"
              % (d["heldout_precision_at_1_off_pct"], d["heldout_precision_at_1_on_pct"],
                 d["heldout_precision_delta_pts"]))
        print("    affinity-on net gain:            %s" % d["affinity_on_net_gain"])
        print("    structural-gate zero-regression: %s" % d["structural_gate_zero_regression"])


def _self_test():
    """Cheap sanity: the corpus assembles, both arms run, struct gate computes, report shape holds."""
    res = evaluate(role="AE", arms=("off",), verbose=False)
    assert "canon" in res["arms"]["off"]["tiers"], "tiers missing"
    assert res["arms"]["off"]["tiers"]["heldout"]["n"] >= len(_HELDOUT), "heldout not assembled"
    assert res["arms"]["off"]["tiers"]["canon"]["scored"] > 0, "canon not scored"
    print("OK: self-test passed (corpus assembles, arm runs, tiers score, struct gate computes)")


def main():
    ap = argparse.ArgumentParser(description="NFRA_COMPPROOF C1 -- COMPROUTE efficacy eval")
    ap.add_argument("--arm", choices=["off", "on", "both"], default="both")
    ap.add_argument("--role", default="AE", help="role for the affinity-on arm (default AE)")
    ap.add_argument("--json", action="store_true", help="emit report.json + print JSON")
    ap.add_argument("--roles", default="", help="comma-list -> role-sensitivity sweep (e.g. AE,DS,CTO,)")
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        _self_test()
        return
    if args.roles:
        roles = tuple(r.strip() for r in args.roles.split(","))
        sweep = evaluate_roles(roles=roles, verbose=False)
        print("=== C1 role-sensitivity sweep (held-out tier: OFF vs ON precision@1) ===")
        for role, s in sweep.items():
            print("  role=%-12s off=%-6s on=%-6s delta=%-6s struct-zero-reg=%s"
                  % (role, s["heldout_p1_off_pct"], s["heldout_p1_on_pct"],
                     s["delta_pts"], s["structural_gate_zero_regression"]))
        return
    arms = ("off", "on") if args.arm == "both" else (args.arm,)
    res = evaluate(role=args.role, arms=arms, verbose=args.verbose)
    _print_report(res)
    if args.json:
        # drop the heavy per-case rows from the persisted headline report (keep aggregates + drv inputs).
        slim = {"role": res["role"],
                "arms": {a: {"tiers": res["arms"][a]["tiers"]} for a in res["arms"]},
                "drv_flip_inputs": res.get("drv_flip_inputs"),
                "generated_by": "comp_route_eval.py (NFRA_COMPPROOF C1)"}
        os.makedirs(os.path.dirname(_REPORT), exist_ok=True)
        with open(_REPORT, "w", encoding="utf-8") as fh:
            json.dump(slim, fh, indent=1)
        print("\nOK: wrote %s" % _REPORT)
        print(json.dumps(slim["drv_flip_inputs"], indent=1))


if __name__ == "__main__":
    main()
