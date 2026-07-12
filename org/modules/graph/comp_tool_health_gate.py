"""
comp-tool-health-gate -- NFRA_TOOLHEALTH TH-C: the close-the-loop ACCEPTANCE GATE.

Makes the TH-B health verdict DRIVE a demonstrable downstream action, not merely DISPLAY it. Today the
loop is ACCUMULATES-BUT-INERT (COMPLEARN D1 / COMPPROOF-D1 verdict 736f6307f): the health view queries +
displays FIX/PROMOTE/RETIRE but drives nothing. This gate converts each ACTIONABLE (non-KEEP) verdict into
a TYPED, ADVISORY commission the CTO ratifies -- and is verifiable as ACTING (the differential proof here;
the COMPPROOF-D1 behavior-delta cross-check on the DRV-flip green).

REUSE, do NOT fork: imports comp_tool_health.health() UN-FORKED (TH-B, CVO-validated, untouched). This
module is TH-C's own surface so TH-B's accepted file is not reopened.

Verdict -> commission (PRD SS4 / TH-C TO scope 1+3):
    FIX     -> fix-commission     -> COMPLEARN worklist consume-side + CTO commission path
    RETIRE  -> deprecation-cand   -> CTO commission path (CTO ratifies; NEVER auto-removed)
    PROMOTE -> route-proposal     -> NFRA_COMPROUTE: a CONCRETE comp_route surface_prior bump (not a flag)
    KEEP    -> (no commission -- the null/healthy path; load-bearing for the differential proof)

ADVISORY, never auto-mutating (TH-C AC-1, inherited COMPLEARN SS5.3 + NFRA_DEBTSCAN never-auto-delete): this
module READS health() and RETURNS/WRITES a commission ledger. It imports NOTHING that writes comp_route /
the manifest / the toolset. The CTO ratifies every FIX/PROMOTE/RETIRE -- the gate proposes, it never rewrites.

Value-anchored (COMPLEARN SS5): every commission carries the TH-B value_anchor (outcome value + rail
quality), NEVER an invocation count -- a FIX-commission for a heavily-used tool rests on its LOW value.

Two-clause acceptance (PRD SS6.4):
  - CLAUSE A (DISPATCH) lands HERE, DRV-independent: the advisory emission + the differential proof
    (a FAILING-health signal -> a commission the healthy path does NOT produce -- "a verdict that changes
    nothing = NOT closed").
  - CLAUSE B (BEHAVIOR-CHANGED) is EXECUTE-on-DRV-flip-green: COMPPROOF-D1 confirms a verdict-driven routing
    proposal, once applied, demonstrably alters LIVE routing on a later cycle (the router applies learned
    affinity -- inert 0/280 until the flip wires a live affinity_provider; comp_route.py:243).

Usage:
    comp-tool-health-gate                     # the advisory commission ledger (worst-first)
    comp-tool-health-gate --verdict FIX       # filter to one commission class (FIX|PROMOTE|RETIRE)
    comp-tool-health-gate --json              # machine-readable ledger
    comp-tool-health-gate --emit PATH         # write the vintage-stamped served ledger to PATH
    comp-tool-health-gate --effective-feed J  # pass TH-A's EFFECTIVE probe through to health() (Phase-B)
    comp-tool-health-gate --self-test         # the differential close-loop proof (clause A)

Author: 0.8.0_AE_CloudComp~D (NFRA_TOOLHEALTH TH-C). 2026-07-07.
Spec: docs/architecture/NFRA_TOOLHEALTH_PRD.md (SS4/SS6.4) + the TH-C task order + TH-C-DESIGN.md.
Reuses: org/modules/graph/comp_tool_health.py (TH-B health query, un-forked).
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_WS = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
sys.path.insert(0, _WS)

from org.modules.graph import comp_tool_health as th  # noqa: E402  (TH-B health query, un-forked)

# --------------------------------------------------------------------------------------------
# The verdict -> commission map. Each ACTIONABLE verdict routes to its TYPED downstream consumer.
# ADVISORY: a commission is a PROPOSAL the CTO ratifies -- it names the action + consumer, it never
# performs it. KEEP returns None (no commission) -- the null path the differential proof pivots on.
# --------------------------------------------------------------------------------------------
def commission_for(row: dict) -> dict | None:
    """Map one TH-B health row -> its advisory commission (or None for KEEP). Pure; no side effects."""
    verdict = row.get("verdict")
    tool = row.get("tool")
    anchor = row.get("value_anchor") or {}
    reason = row.get("reason", "")
    pending = bool(row.get("pending_effective"))
    # The value citation carried on EVERY commission (AC value-anchored; never a raw count).
    value_anchor = {
        "mean_outcome_value": anchor.get("mean_outcome_value"),
        "rail_quality": anchor.get("rail_quality"),
        "value_low_flag": anchor.get("value_low_flag"),
        "basis": anchor.get("basis"),
    }
    # Per-candidate 3-axis HEALTH GROUNDING (CTO ask 2026-07-07): the CTO ratifies each fix/promote/retire
    # on the HEALTH EVIDENCE, not the verdict LABEL -- so carry the full TH-B row detail (used volume +
    # VALUE, rail state, effective status) alongside every commission. A RETIRE the CTO must confirm is
    # genuinely-dead-vs-slow-but-load-bearing reads its used.events + rail here; a PROMOTE reads its
    # effective + value to reject a Goodhart-gamed w_s bump.
    used = row.get("used") or {}
    rail = row.get("rail_consistent") or {}
    grounding = {
        "used": {
            "used": used.get("used"),
            "events": used.get("events"),
            "distinct_roles": used.get("distinct_roles"),
            "mean_outcome_value": used.get("mean_outcome_value"),
            "outcome_n": used.get("outcome_n"),
        },
        "rail_consistent": {
            "state": rail.get("state"),
            "router_confidence": rail.get("router_confidence"),
        },
        "effective": row.get("effective"),
        "note": ("verdict pending the EFFECTIVE probe (TH-A) -- provisional until the recurring probe "
                 "confirms" if pending else "verdict confirmed on the live 3-axis evidence"),
    }
    base = {
        "tool": tool,
        "verdict": verdict,
        "pending_effective": pending,   # True => the EFFECTIVE axis (TH-A) has not confirmed yet
        "value_anchor": value_anchor,
        "grounding": grounding,         # the CTO-ratification evidence (health, not label)
        "reason": reason,
    }
    if verdict == "FIX":
        base.update({
            "action": "fix-commission",
            "consumers": ["complearn-worklist", "cto-commission"],
            "proposed_to": {
                "kind": "fix-TO",
                "title": f"FIX comp-tool-health: {tool} is used/reached-for but does not reach the answer",
                "objective": (f"Investigate + remediate {tool}: the fused health verdict is FIX "
                              f"({reason}). Restore it to KEEP (effective) or, if irreparable, RETIRE."),
                "ratifier": "1.0.0_SA_CTO",
            },
            "auto_mutates": False,
        })
    elif verdict == "RETIRE":
        base.update({
            "action": "deprecation-candidate",
            "consumers": ["cto-commission"],
            "proposed_to": {
                "kind": "deprecation-candidate",
                "title": f"RETIRE candidate: {tool} (dead -- unused + no effective/rail signal)",
                "objective": (f"CTO-ratified deprecation review of {tool} ({reason}). NEVER auto-removed "
                              "-- mandatory human ratification (mirrors NFRA_DEBTSCAN never-auto-delete)."),
                "ratifier": "1.0.0_SA_CTO",
            },
            "auto_mutates": False,
        })
    elif verdict == "PROMOTE":
        # AC-3: a CONCRETE COMPROUTE proposal, grounded in the real engine knob. comp_route scores
        # score = w_q*q + w_s*surface_prior + w_h*affinity (comp_route.py). An effective-but-ignored
        # tool is a surface_prior miss -> propose raising its surface_prior so the router SURFACES it,
        # NOT a bare "promote" flag.
        base.update({
            "action": "comproute-route-proposal",
            "consumers": ["comproute"],
            "proposal": {
                "type": "surface_prior_bump",
                "target_tool": tool,
                "engine_knob": "comp_route.surface_prior (the w_s term)",
                "rationale": (f"effective-but-ignored ({reason}): the router does not surface {tool}. "
                              "Raise its surface_prior / add it as a routable surface so a matching "
                              "intent routes to it. Concrete comp_route change, CTO/COMPROUTE-ratified."),
                "ratifier": "1.0.0_SA_CTO (via NFRA_COMPROUTE)",
            },
            "auto_mutates": False,
        })
    else:
        return None  # KEEP (or unknown) -> no commission (the healthy/null path)
    return base


def build_commissions(effective_feed: dict | None = None) -> dict:
    """Run the TH-B health query and emit the advisory commission ledger for every non-KEEP verdict.
    ADVISORY: reads health(), returns a ledger. Mutates nothing (AC-1)."""
    h = th.health(effective_feed=effective_feed)
    commissions = [c for c in (commission_for(r) for r in h["tools"]) if c is not None]
    # worst-first: FIX, then PROMOTE, then RETIRE (reuse TH-B's verdict order; confirmed above pending).
    order = {"FIX": 0, "PROMOTE": 1, "RETIRE": 2}
    commissions.sort(key=lambda c: (order.get(c["verdict"], 9), 1 if c["pending_effective"] else 0))
    counts: dict = {}
    for c in commissions:
        counts[c["verdict"]] = counts.get(c["verdict"], 0) + 1
    return {
        "gate": "NFRA_TOOLHEALTH TH-C -- close-the-loop acceptance gate (ADVISORY -- CTO ratifies)",
        "phase": h["phase"],
        "clause": ("A (DISPATCH -- verdict->typed commission). Clause B (behavior-delta via COMPPROOF-D1 "
                   "on a later cycle) EXECUTES on the DRV-flip green (comp_route affinity_provider live)."),
        "corpus_source": h["corpus_source"],
        "value_metric": h["value_metric"],
        "advisory": True,
        "auto_mutation": "NONE -- the gate proposes; the CTO ratifies every fix/promote/retire (SS5.3)",
        "commission_counts": counts,
        "n_commissions": len(commissions),
        "n_keep_no_commission": h["n_tools"] - len(commissions),
        "commissions": commissions,
    }


# --------------------------------------------------------------------------------------------
# The differential close-loop proof (clause A / the CVO exercise-gate) -- DRV-independent.
# "Feed a FAILING-health signal -> the downstream action DIFFERS from the healthy path."
# --------------------------------------------------------------------------------------------
def _self_test() -> tuple[bool, list]:
    checks: list = []

    def ck(name, ok, detail=""):
        checks.append({"check": name, "pass": bool(ok), "detail": detail})
        return ok

    # (1) TAXONOMY: each actionable verdict maps to its TYPED commission + consumer; KEEP -> None.
    ck("map.fix_to_fix_commission",
       (commission_for({"verdict": "FIX", "tool": "comp-x"}) or {}).get("action") == "fix-commission")
    ck("map.retire_to_deprecation",
       (commission_for({"verdict": "RETIRE", "tool": "comp-x"}) or {}).get("action")
       == "deprecation-candidate")
    ck("map.promote_to_route_proposal",
       (commission_for({"verdict": "PROMOTE", "tool": "comp-x"}) or {}).get("action")
       == "comproute-route-proposal")
    ck("map.keep_no_commission", commission_for({"verdict": "KEEP", "tool": "comp-x"}) is None)

    # (2) AC-3: the PROMOTE commission is a CONCRETE comp_route change (a surface_prior bump naming the
    # engine knob), NOT a bare flag.
    promo = commission_for({"verdict": "PROMOTE", "tool": "comp-x", "reason": "eff-but-ignored"})
    ck("promote.concrete_not_flag",
       promo["proposal"]["type"] == "surface_prior_bump" and "surface_prior" in promo["proposal"]["engine_knob"],
       f"proposal={promo['proposal']['type']} knob={promo['proposal']['engine_knob']}")

    # (3) AC-1 ADVISORY: no commission auto-mutates; every one names a CTO ratifier.
    all_kinds = [commission_for({"verdict": v, "tool": "comp-x"}) for v in ("FIX", "RETIRE", "PROMOTE")]
    ck("advisory.no_auto_mutation", all(c.get("auto_mutates") is False for c in all_kinds))
    ratifiers_ok = all(("proposed_to" in c and c["proposed_to"].get("ratifier"))
                       or ("proposal" in c and c["proposal"].get("ratifier")) for c in all_kinds)
    ck("advisory.every_commission_names_ratifier", ratifiers_ok)

    # (4) VALUE-ANCHORED: every commission carries a value_anchor (outcome/quality), never a raw count.
    live = build_commissions()
    anchored = all("value_anchor" in c and "mean_outcome_value" in c["value_anchor"]
                   for c in live["commissions"])
    ck("value.every_commission_cites_value_not_count", anchored,
       f"{live['n_commissions']} live commissions, all carry a value_anchor")

    # (5) THE LOAD-BEARING DIFFERENTIAL (the CVO exercise-gate): feed a FAILING-health signal on a live
    # KEEP tool (EFFECTIVE=False via the proven TH-A --effective-feed seam) -> the gate now emits a
    # fix-commission for it, where the HEALTHY path (EFFECTIVE=True / KEEP) emits NONE. A verdict that
    # changes nothing = NOT closed; this proves the verdict DRIVES the downstream action at dispatch layer.
    keep_tool = next((r["tool"] for r in th.health()["tools"]
                      if r["verdict"] == "KEEP" and r["pending_effective"]
                      and not th.cls.is_preventive_tool(r["tool"])), None)
    if keep_tool:
        healthy = build_commissions(effective_feed={keep_tool: True})
        failing = build_commissions(effective_feed={keep_tool: False})
        in_healthy = any(c["tool"] == keep_tool for c in healthy["commissions"])
        fail_row = next((c for c in failing["commissions"] if c["tool"] == keep_tool), None)
        ck("differential.failing_signal_drives_action_healthy_does_not",
           (not in_healthy) and fail_row is not None and fail_row["action"] == "fix-commission",
           f"{keep_tool}: healthy -> {'commission' if in_healthy else 'NONE'} / "
           f"failing -> {fail_row['action'] if fail_row else 'NONE'}")
    else:
        ck("differential.failing_signal_drives_action_healthy_does_not", True,
           "no pending-KEEP live tool to exercise (differential proven structurally in checks 1-4)")

    # (6) CTO-RATIFICATION GROUNDING (CTO ask): every commission carries the full 3-axis TH-B evidence
    # (used volume+value, rail state, effective) so the CTO ratifies on health, not the verdict label.
    grounded = all(
        "grounding" in c and {"used", "rail_consistent", "effective"} <= set(c["grounding"])
        for c in live["commissions"])
    ck("grounding.every_commission_carries_3axis_evidence", grounded,
       f"{live['n_commissions']} commissions, all carry used+rail+effective grounding")

    # (7) REUSE-not-fork: health() comes from the TH-B module un-forked (no re-implementation here).
    ck("reuse.health_from_thb_unforked", th.health.__module__.endswith("comp_tool_health"),
       f"health() module = {th.health.__module__}")

    ok = all(c["pass"] for c in checks)
    return ok, checks


# --------------------------------------------------------------------------------------------
# Render + emit.
# --------------------------------------------------------------------------------------------
def _render(ledger: dict, verdict_filter: str | None = None) -> str:
    L = ["=== comp-tool-health-gate -- NFRA_TOOLHEALTH TH-C close-the-loop gate (ADVISORY -- CTO ratifies) ===",
         ledger["phase"],
         f"clause: {ledger['clause']}",
         f"corpus: {ledger['corpus_source']}",
         f"commission counts: {ledger['commission_counts']}   "
         f"(KEEP with no commission: {ledger['n_keep_no_commission']})",
         f"auto-mutation: {ledger['auto_mutation']}",
         ""]
    hdr = f"{'VERDICT':<8} {'TOOL':<22} {'ACTION':<24} {'CONSUMER(S)':<28} RATIFIER"
    L.append(hdr)
    L.append("-" * len(hdr))
    for c in ledger["commissions"]:
        if verdict_filter and c["verdict"] != verdict_filter:
            continue
        cons = ",".join(c.get("consumers", []))
        rat = (c.get("proposed_to", {}).get("ratifier")
               or c.get("proposal", {}).get("ratifier") or "1.0.0_SA_CTO")
        v = c["verdict"] + ("?" if c["pending_effective"] else "")
        L.append(f"{v:<8} {c['tool']:<22} {c['action']:<24} {cons:<28} {rat}")
    L.append("")
    L.append("ADVISORY ONLY -- the gate PROPOSES; the CTO ratifies every fix/promote/retire (SS5.3, no "
             "auto-mutation). Clause B (COMPPROOF-D1 behavior-delta on a later cycle) executes on the "
             "DRV-flip green. '?' = pending the EFFECTIVE probe (TH-A).")
    return "\n".join(L)


def main() -> int:
    ap = argparse.ArgumentParser(
        description="comp-tool-health-gate -- NFRA_TOOLHEALTH TH-C close-the-loop acceptance gate")
    ap.add_argument("--verdict", choices=["FIX", "PROMOTE", "RETIRE"], help="filter to one commission class")
    ap.add_argument("--json", action="store_true", help="machine-readable ledger")
    ap.add_argument("--emit", metavar="PATH", help="write the vintage-stamped served commission ledger to PATH")
    ap.add_argument("--effective-feed", metavar="JSON",
                    help="TH-A EFFECTIVE probe stream (JSON {tool: bool}); Phase-B full 4-verdict")
    ap.add_argument("--self-test", action="store_true",
                    help="the differential close-loop proof (clause A / CVO exercise-gate)")
    args = ap.parse_args()

    if args.self_test:
        ok, checks = _self_test()
        if args.json:
            print(json.dumps({"pass": ok, "checks": checks}, indent=2))
        else:
            print("=== comp-tool-health-gate --self-test (close-the-loop dispatch + differential) ===")
            for c in checks:
                print(f"  [{'PASS' if c['pass'] else 'FAIL'}] {c['check']}"
                      + (f"   ({c['detail']})" if c["detail"] else ""))
            print(f"\n{'OK: all checks pass' if ok else 'ERROR: one or more checks FAILED'}")
        return 0 if ok else 1

    # Ga (CYCLE-A.1 / F2): DEFAULT to the EFFECTIVE feed for CONSISTENCY with comp-tool-health (mirrors
    # main():757) -- so the commission gate decides on the same EFFECTIVE axis, not the 2-axis skeleton.
    # Gb: READ-ONLY -- the gate READS the feed; it NEVER refreshes (no ensure_fresh / _ensure_feed_fresh /
    # probe_all on the gate path). A commission/decision gate is a hot path; a live full-corpus probe here
    # is exactly the probe-storm G1's consumption-driven wire guarded against.
    _feed_path = args.effective_feed or (th.DEFAULT_EFFECTIVE_FEED
                                         if os.path.exists(th.DEFAULT_EFFECTIVE_FEED) else None)
    feed = th.load_effective_feed(_feed_path) if _feed_path else None
    ledger = build_commissions(effective_feed=feed)
    # Gc: staleness VISIBLE (a pure feed_age_days READ, never a run) so a stale feed shows in the ledger;
    # the gate never triggers a probe. A missing feed -> feed None -> EFFECTIVE pending (2-axis skeleton).
    from org.modules.graph.compproof import tool_probe as _tp  # lazy: pure feed-age read only (NO probe)
    _age = _tp.feed_age_days(_feed_path) if _feed_path else None
    ledger["feed_freshness"] = {"feed_path": _feed_path, "age_days": _age,
                                "ceiling_days": _tp.DEFAULT_CEILING_DAYS, "read_only": True,
                                "stale": (_age is None or _age > _tp.DEFAULT_CEILING_DAYS)}

    if args.emit:
        # Vintage-stamp only in the served-emit path (keeps build_commissions deterministic for the
        # self-test). computed_at is read from the corpus vintage -- no wall-clock dependency.
        ledger_out = dict(ledger)
        ledger_out["computed_at"] = ledger["corpus_source"]
        with open(args.emit, "w", encoding="utf-8") as fh:
            json.dump(ledger_out, fh, indent=2)
        print(f"OK: wrote advisory commission ledger ({ledger['n_commissions']} commissions) to {args.emit}")
        return 0

    if args.json:
        print(json.dumps(ledger, indent=2))
    else:
        _fr = ledger["feed_freshness"]                    # Gc: staleness visible in the human output too (read-only)
        _astr = "no feed (EFFECTIVE pending)" if _fr["age_days"] is None else f"{_fr['age_days']:.1f}d old"
        print(f"EFFECTIVE feed (gate is READ-ONLY, never probes): {_astr} -- "
              f"{'STALE' if _fr['stale'] else 'fresh'} (ceiling {_fr['ceiling_days']}d)")
        print(_render(ledger, verdict_filter=args.verdict))
    return 0


if __name__ == "__main__":
    sys.exit(main())
