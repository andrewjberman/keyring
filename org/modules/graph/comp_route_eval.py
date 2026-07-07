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
_TAIL_REPORT = os.path.join(_HERE, "compproof", "comproute_c1_tail_report.json")

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

# ---------------------------------------------------------------------------------------------------
# NON-VETTED TAIL corpus (NFRA_COMPPROOF C1 basis-b, CTO MEASURE-FIRST ruling 20260707T062419Z; CVO~B
# cert-design 20260707T062743Z). The ambiguous/vague intents where NO extractor vets -> route falls to
# the base posterior -> affinity ACTS. This is the ONLY tier where affinity-on can change a decision, so
# it is where affinity's tail-efficacy SIGN is measured (moved != improved). Labels are accept-SETS,
# ~E-authored, CVO~B-honesty-gated. Deliberately oblique/keyword-avoiding phrasings (a strong tool
# keyword makes the extractor vet -> affinity-immune -> not tail). run_tail_eval AUTO-FILTERS to the
# affinity-actable (base-band OR fallback in the OFF arm) subset -- a case that vets is reported excluded,
# NOT scored (vetted == affinity cannot touch it). NOTE (honest caveat): the labelable-non-vetted band is
# INTRINSICALLY NARROW -- clear-labelable intents tend to carry a tool keyword and thus vet; truly vague
# intents lack a clean label. So N is small and labels are softer than the fixture BY THE NATURE OF THE
# TAIL; the change-DIRECTION (toward/away/neutral) is reported alongside precision as the label-robust signal.
# ---------------------------------------------------------------------------------------------------
_TAIL = [
    ("should I trust yesterday's numbers or did they not update", {"comp-freshness"}),
    ("who depends on the thing this job spits out", {"comp-pipescript"}),
    ("are we keeping the real values or the masked ones", {"comp-pii"}),
    ("is my output going to be accepted downstream", {"comp-validate"}),
    ("did the overnight thing actually do its job", {"comp-freshness"}),
    ("what feeds this and what eats what it produces", {"comp-pipescript"}),
    ("could a client end up seeing a raw identifier", {"comp-pii"}),
    ("is the snapshot I am staring at from today", {"comp-freshness"}),
    ("before I hand this off is it going to pass their checks", {"comp-validate"}),
    ("what else leans on this output of mine", {"comp-pipescript"}),
    ("are the private bits actually hidden or still in the clear", {"comp-pii"}),
    ("will they accept what I am about to give them", {"comp-validate"}),
    ("has the source moved on since I last looked", {"comp-freshness"}),
    ("who else is downstream of what this produces", {"comp-pipescript"}),
    ("is there a raw value sitting where it should be scrubbed", {"comp-pii"}),
    ("help me understand the dependencies here", {"comp-blast", "comp-trace"}),   # CVO~B example probe
    ("trace the thing through the system", {"comp-trace"}),                        # CVO~B example probe
]


def _route_arm(intent, provider, affinity_provider, role, relevance_provider=None):
    """The router path, identical to comp_route_shadow._primary EXCEPT the affinity arm + role +
    relevance signal vary. A clean A/B: same extractors, same intent classifier, same route() engine.
    relevance_provider (POTION Charter-1) swaps the stage-2 lexical relevance for semantic when passed."""
    ic = _sh.sig.classify_query_intent(intent)
    ctx = {"role": role, "working_set": [], "trajectory": [], "intent_class": ic}
    r = _sh.comp_route.route(intent, ctx, provider, affinity_provider=affinity_provider,
                             extractors=_sh.sig.EXTRACTORS, relevance_provider=relevance_provider)
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


def run_arm(arm, role, verbose=False, relevance_provider=None):
    """Run ONE arm ('off'|'on') over the full corpus; return per-tier aggregates + per-case rows.
    relevance_provider (POTION Charter-1) swaps the stage-2 relevance lexical->semantic when passed."""
    provider = _sh.capmap.get_provider()
    cap_write = {c.id: bool(getattr(c, "write_path", False)) for c in provider.capabilities()}
    affinity_provider = CachedAffinityProvider() if arm == "on" else None
    tiers = {t: _blank_tier() for t in ("canon", "diverse", "heldout")}
    rows = []
    for q, accept, tier, kind in _labeled_cases():
        r, ic = _route_arm(q, provider, affinity_provider, role, relevance_provider=relevance_provider)
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


def run_tail_eval(role="AE", verbose=False):
    """NFRA_COMPPROOF C1 basis-b: measure affinity's tail-efficacy SIGN on the NON-VETTED tail.
    AUTO-FILTERS _TAIL to the affinity-actable subset (base-band OR fallback in the OFF arm; a vetted
    case is affinity-immune -> excluded). On that subset: precision@1 OFF vs ON + the label-robust
    change-DIRECTION decomposition (toward-label / away-label / neutral wrong->wrong). The SIGN:
      positive delta (toward>away)  -> affinity IMPROVES the tail -> flip-authorization evidence.
      zero/negative                 -> affinity moves-but-does-not-improve -> HOLD flip; w_h/affinity
                                       calibration is a SEPARATE pre-flip gate (CTO ruling)."""
    provider = _sh.capmap.get_provider()
    ap = CachedAffinityProvider()
    excluded_vetted = 0
    scored = 0
    p1_off = p1_on = 0
    toward = away = neutral = 0
    rows = []
    for q, accept in _TAIL:
        r_off, ic = _route_arm(q, provider, None, role)
        r_on, _ = _route_arm(q, provider, ap, role)
        toff = r_off.ranked[0] if r_off.ranked else None
        # affinity-immune (vetted, non-fallback) -> not tail; exclude.
        if toff is not None and toff.vetted and r_off.kind != "fallback":
            excluded_vetted += 1
            continue
        scored += 1
        off_id = "FALLBACK" if r_off.kind == "fallback" else (toff.cap.id if toff else None)
        ton = r_on.ranked[0] if r_on.ranked else None
        on_id = "FALLBACK" if r_on.kind == "fallback" else (ton.cap.id if ton else None)
        off_hit = off_id in accept
        on_hit = on_id in accept
        p1_off += int(off_hit)
        p1_on += int(on_hit)
        direction = None
        if off_id != on_id:
            if on_hit and not off_hit:
                toward += 1
                direction = "toward"
            elif off_hit and not on_hit:
                away += 1
                direction = "away"
            else:
                neutral += 1
                direction = "neutral(wrong->wrong)"
        rows.append({"q": q[:60], "accept": sorted(accept), "off": off_id, "on": on_id,
                     "off_hit": off_hit, "on_hit": on_hit, "direction": direction})
        if verbose:
            print("  off=%-14s on=%-14s exp=%-22s %s"
                  % (off_id, on_id, sorted(accept), direction or ("=hit" if off_hit else "=miss")))
    delta = (_pct(p1_on, scored) or 0) - (_pct(p1_off, scored) or 0) if scored else None
    sign = ("positive" if (toward > away) else ("negative" if (away > toward) else "zero"))
    return {
        "role": role, "tail_authored": len(_TAIL), "excluded_vetted_affinity_immune": excluded_vetted,
        "tail_scored_affinity_actable": scored,
        "precision_at_1_off_pct": _pct(p1_off, scored), "precision_at_1_on_pct": _pct(p1_on, scored),
        "precision_delta_pts": (round(delta, 1) if delta is not None else None),
        "changes_toward_label": toward, "changes_away_label": away,
        "changes_neutral_wrong_to_wrong": neutral,
        "tail_efficacy_sign": sign,
        "verdict": ("POSITIVE tail-efficacy -> affinity IMPROVES the ambiguous tail -> flip-authorization evidence"
                    if sign == "positive" else
                    ("NEGATIVE tail-efficacy -> affinity DEGRADES the tail -> HOLD flip (calibration gate)"
                     if sign == "negative" else
                     "ZERO tail-efficacy -> affinity MOVES but does NOT improve the tail (moved != improved) "
                     "-> HOLD the value-flip; w_h/affinity calibration is a SEPARATE pre-flip gate")),
        "rows": rows,
    }


def rank_diagnostic(role="AE", relevance_provider=None):
    """CHARTER-1 sizing instrument (CVO~B verdict 39462886a): the correct-cap BASE RANK + score-gap-to-top
    + within-affinity-swing reachability on the affinity-actable tail. This is the number that scopes the
    two COMPROUTE charters and, run AGAIN after the base oblique-precision fix (Charter-1), gives the
    POST-FIX RESIDUAL RANK -- Charter-2's real target (CVO~B: 'measure the residual before charter-2 is
    sized; it may be much smaller than rank-11'). Baseline now: median rank ~11 of ~57, 10/11 within w_h.
    Affinity (bounded by w_h) can only tie-break a cap already close in SCORE, so a small residual gap ->
    intent-conditioned affinity has standalone value; a large residual -> base must surface it first."""
    provider = _sh.capmap.get_provider()
    w = _sh.comp_route.Weights()
    ranks, gaps = [], []
    within_swing = 0
    rows = []
    for q, accept in _TAIL:
        r, _ic = _route_arm(q, provider, None, role, relevance_provider=relevance_provider)
        if not r.ranked or (r.ranked[0].vetted and r.kind != "fallback"):
            continue
        ids = [s.cap.id for s in r.ranked]
        scores = [s.score for s in r.ranked]
        pos = [i for i, cid in enumerate(ids) if cid in accept]
        if not pos:
            continue
        i0 = pos[0]
        rank = i0 + 1
        gap = round(scores[0] - scores[i0], 3)
        reachable = gap <= w.w_h
        ranks.append(rank)
        gaps.append(gap)
        within_swing += int(reachable)
        rows.append({"q": q[:50], "correct_cap": ids[i0], "base_rank": rank,
                     "gap_to_top": gap, "reachable_within_w_h": reachable})
    n = len(ranks)
    med = sorted(ranks)[n // 2] if n else None
    mean = round(sum(ranks) / n, 1) if n else None
    return {
        "role": role, "w_h": w.w_h, "tail_scored": n,
        "correct_cap_base_rank_median": med, "correct_cap_base_rank_mean": mean,
        "within_affinity_swing_gap_le_w_h": ("%d/%d" % (within_swing, n)) if n else None,
        "reading": ("correct tool is rank-buried (~%s of ~57) but SCORE-reachable (%d/%d within w_h=%.2f) "
                    "-> base-precision is the primary lever; affinity's block is signal-DIRECTION not "
                    "surfacing. Re-run post-Charter-1 for the residual rank = Charter-2's real target."
                    % (med, within_swing, n, w.w_h)) if n else "no scored tail cases",
        "rows": rows,
    }


def per_case_table(role="AE", relevance_provider=None, arm_label="arm"):
    """CVO~B per-case BLEND re-cert table (c330fdebf / pre-spec 073552Z): for EACH tail case, LEXICAL
    (rank, top1-correct) vs the ARM (rank, top1-correct), flagging any lexical-top-1 DEMOTION (gate #1)
    and confirming the oblique LIFT is preserved (gate #2). Per-case, NOT median/mean (CTO banned
    aggregate for this gate)."""
    provider = _sh.capmap.get_provider()
    rows = []
    demotions = lifts_kept = 0
    for q, accept in _TAIL:
        rl, _ = _route_arm(q, provider, None, role, relevance_provider=None)
        ra, _ = _route_arm(q, provider, None, role, relevance_provider=relevance_provider)
        if not rl.ranked or (rl.ranked[0].vetted and rl.kind != "fallback"):
            continue

        def rank_of(r):
            ids = [s.cap.id for s in r.ranked]
            pos = [i for i, cid in enumerate(ids) if cid in accept]
            return (pos[0] + 1) if pos else None
        lr, ar = rank_of(rl), rank_of(ra)
        lt1, at1 = (lr == 1), (ar == 1)
        demoted = bool(lt1 and not at1)                       # gate #1: lexical top-1 lost
        lifted = bool(lr is not None and ar is not None and lr > 3 and ar <= 4)  # gate #2: oblique lift
        if demoted:
            demotions += 1
        if lifted:
            lifts_kept += 1
        rows.append({"q": q[:46], "lex_rank": lr, "lex_top1": lt1,
                     "%s_rank" % arm_label: ar, "%s_top1" % arm_label: at1,
                     "DEMOTED": demoted, "lifted": lifted})
    return {"role": role, "arm": arm_label, "tail_n": len(rows),
            "lexical_top1_demotions": demotions,     # MUST be 0 for the blend to pass gate #1
            "oblique_lifts_kept": lifts_kept,
            "gate1_no_lexical_top1_demoted": (demotions == 0),
            "rows": rows}


def flip_gate(role="AE", name_boost=0.15):
    """The 3-criterion SEMANTIC-RELEVANCE flip-gate (POTION design sec-4; CTO order: run AFTER CVO~B's
    residual cert). Compares LEXICAL vs SEMANTIC relevance (both affinity-off) over the full corpus:
      (1) net precision@1 GAIN (semantic vs lexical) -- charter-1 alone may NOT meet this (correct cap
          near-top but not top-1 -> precision unchanged; that is HONEST, top-1 is charter-2's job).
      (2) ZERO structural-gate regression -- read-intent never surfaces a write_path cap under semantic.
      (3) E1 bucket phrasings -- the heldout-e1 read probes still surface 0 write_path under semantic.
    Reports HONESTLY: reachability-improving + E1-fixed + zero-regression is a SAFE base improvement even
    if precision@1 awaits charter-2 -- do NOT spin near-top as top-1 (CTO)."""
    from comp_potion_relevance import build_provider
    rp = build_provider(name_boost=name_boost)
    if rp is None:
        return {"error": "semantic provider unavailable (fail-safe) -- cannot run flip-gate"}
    lex = _summarize(run_arm("off", role, relevance_provider=None)[0])
    sem = _summarize(run_arm("off", role, relevance_provider=rp)[0])
    def p1(s, t):
        return s[t]["precision_at_1_pct"]
    net_gain = {t: (None if (p1(sem, t) is None or p1(lex, t) is None)
                    else round(p1(sem, t) - p1(lex, t), 1)) for t in ("canon", "diverse", "heldout")}
    struct_ok = all(sem[t]["struct_gate_pass"] for t in ("canon", "diverse", "heldout"))
    any_gain = any((g or 0) > 0 for g in net_gain.values())
    any_regress = any((g or 0) < 0 for g in net_gain.values())
    # PER-CASE regression scan (CVO~B c330fdebf: the tier-aggregate MASKS a top-1 swap -- semantic can
    # demote a genuine lexical top-1 (comp-pii 1->3) while gaining another, netting unchanged. A no-
    # regression gate MUST be per-case, not median/mean). Scan the union of the labeled corpus + the tail
    # (where semantic actually moves a non-vetted top-1); report EACH lexical-right->semantic-wrong loss.
    provider = _sh.capmap.get_provider()
    seen, per_case_reg, per_case_gain = set(), [], []
    corpus = [(q, acc) for q, acc, _t, _k in _labeled_cases() if acc] + list(_TAIL)
    for q, accept in corpus:
        if q in seen:
            continue
        seen.add(q)
        rl, _ = _route_arm(q, provider, None, role, relevance_provider=None)
        rs, _ = _route_arm(q, provider, None, role, relevance_provider=rp)
        lt = rl.ranked[0].cap.id if (rl.ranked and rl.kind != "fallback") else None
        stop = rs.ranked[0].cap.id if (rs.ranked and rs.kind != "fallback") else None
        lex_hit, sem_hit = (lt in accept), (stop in accept)
        if lex_hit and not sem_hit:
            per_case_reg.append({"q": q[:48], "lexical_top": lt, "semantic_top": stop, "correct": sorted(accept)})
        elif sem_hit and not lex_hit:
            per_case_gain.append({"q": q[:48], "semantic_top": stop, "correct": sorted(accept)})
    return {
        "role": role, "name_boost": name_boost,
        "precision_at_1_lexical": {t: p1(lex, t) for t in ("canon", "diverse", "heldout")},
        "precision_at_1_semantic": {t: p1(sem, t) for t in ("canon", "diverse", "heldout")},
        "net_precision_gain_pts": net_gain,
        "criterion_1_net_precision_gain": ("gain" if any_gain and not any_regress else
                                           ("regression" if any_regress else "neutral")),
        "criterion_2_zero_structural_regression": struct_ok,
        "criterion_3_e1_struct_holds_semantic": struct_ok,   # e1 cases are read-intent struct-only
        "per_case_top1_regressions": per_case_reg,   # PER-CASE no-regression gate (CVO~B): the honest signal
        "per_case_top1_gains": per_case_gain,
        "per_case_verdict": ("%d top-1 REGRESSION(s) + %d gain(s) -- the tier-aggregate masks these; a "
                             "PER-CASE no-regression gate is REQUIRED for the live flip (CVO~B)"
                             % (len(per_case_reg), len(per_case_gain))),
        "honest_verdict": (
            "REGRESSION -> do NOT flip" if any_regress else
            ("net precision GAIN + zero-regression + E1-holds -> flip-favorable" if any_gain and struct_ok else
             "SAFE + reachability-improving but precision@1 UNCHANGED (top-1 pending charter-2); "
             "E1-holds + zero-regression -> a base-safe reachability improvement, NOT a top-1 delivery "
             "(CTO judges the flip on this honest state)")),
    }


def affinity_reach_diagnostic(role="AE"):
    """THE load-bearing C1 finding, made reproducible: quantify WHERE affinity can act. A top routed
    in the VETTED band [1.0,2.0) is affinity-IMMUNE (the band structurally pre-empts the base posterior
    where affinity lives, comp_route.py:310); only a BASE-band top is affinity-sensitive. Reports, over
    the full corpus: #vetted tops / #base-band tops / #tops that CHANGE off->on. A 0/0-changed result
    means affinity-on is a no-op on this corpus BY CONSTRUCTION (not a wiring bug) -- its efficacy lives
    only on the non-vetted tail. Re-runnable by CVO~B independently (exercise-gate)."""
    provider = _sh.capmap.get_provider()
    ap = CachedAffinityProvider()
    vetted_top = base_top = fallback = changed = 0
    changed_examples = []
    for q, _accept, _tier, _kind in _labeled_cases():
        r_off, _ = _route_arm(q, provider, None, role)
        r_on, _ = _route_arm(q, provider, ap, role)
        if not r_off.ranked:
            continue
        toff = r_off.ranked[0]
        ton = r_on.ranked[0] if r_on.ranked else None
        if r_off.kind == "fallback":
            fallback += 1
        elif toff.vetted:
            vetted_top += 1
        else:
            base_top += 1
        if ton is not None and toff.cap.id != ton.cap.id and r_off.kind != "fallback":
            changed += 1
            changed_examples.append((q[:44], toff.cap.id, ton.cap.id))
    return {"role": role, "n": len(_labeled_cases()), "vetted_tops_affinity_immune": vetted_top,
            "base_band_tops_affinity_sensitive": base_top, "fallbacks": fallback,
            "tops_changed_off_to_on": changed, "changed_examples": changed_examples,
            "verdict": ("affinity-on is a NO-OP on this corpus (all tops vetted -> affinity pre-empted "
                        "by the vetted band; efficacy confined to the non-vetted tail)"
                        if changed == 0 else
                        "affinity-on MOVES %d top(s) on this corpus (base-band cases exist)" % changed)}


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
    ap.add_argument("--diagnostic", action="store_true",
                    help="reproduce the affinity-reach finding (vetted vs base-band tops; off->on changes)")
    ap.add_argument("--tail", action="store_true",
                    help="basis-b: measure affinity's tail-efficacy SIGN on the non-vetted tail corpus")
    ap.add_argument("--rank", action="store_true",
                    help="charter-1 sizing: correct-cap base rank + within-w_h reachability on the tail "
                         "(re-run post-base-fix for the residual = charter-2's target)")
    ap.add_argument("--semantic", action="store_true",
                    help="POTION Charter-1: use the semantic relevance provider (full-posterior) for --rank")
    ap.add_argument("--flip-gate", action="store_true",
                    help="POTION 3-criterion flip-gate: lexical vs semantic precision + struct-regression (run AFTER CVO residual cert)")
    ap.add_argument("--blend", action="store_true",
                    help="use the BLEND relevance (max(lexical,semantic)+name-boost, CTO's ruled flip shape)")
    ap.add_argument("--per-case", action="store_true",
                    help="CVO~B per-case table: lexical vs arm rank/top1 per tail case (demotion gate)")
    ap.add_argument("--name-boost", type=float, default=0.15,
                    help="lexical-exact-NAME secondary boost for the semantic arm (default 0.15)")
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        _self_test()
        return
    if args.diagnostic:
        print(json.dumps(affinity_reach_diagnostic(role=args.role), indent=1))
        return
    if args.flip_gate:
        print(json.dumps(flip_gate(role=args.role, name_boost=args.name_boost), indent=1))
        return
    if args.per_case:
        from comp_potion_relevance import build_provider
        rp = build_provider(name_boost=args.name_boost, blend=args.blend)
        label = "blend" if args.blend else "semantic"
        if rp is None:
            print("ALARM: semantic provider unavailable (fail-safe)")
            return
        res = per_case_table(role=args.role, relevance_provider=rp, arm_label=label)
        print(json.dumps({k: v for k, v in res.items() if k != "rows"}, indent=1))
        print("  %-46s | lex_rk lex_t1 | %s_rk %s_t1 | flag" % ("intent", label, label))
        for r in res["rows"]:
            flag = "DEMOTED!" if r["DEMOTED"] else ("lift" if r["lifted"] else "")
            print("  %-46s |   %-4s %-5s |  %-4s %-5s | %s"
                  % (r["q"], r["lex_rank"], r["lex_top1"], r["%s_rank" % label],
                     r["%s_top1" % label], flag))
        return
    if args.rank:
        rp = None
        if args.semantic:
            from comp_potion_relevance import build_provider
            rp = build_provider(name_boost=args.name_boost)
            if rp is None:
                print("ALARM: semantic provider unavailable -> measuring LEXICAL (fail-safe)")
        res = rank_diagnostic(role=args.role, relevance_provider=rp)
        res["relevance"] = "semantic(POTION)" if rp is not None else "lexical"
        print(json.dumps({k: v for k, v in res.items() if k != "rows"}, indent=1))
        if args.verbose:
            for r in res["rows"]:
                print("  rank=%2d gap=%.3f reachable=%s  %-16s | %s"
                      % (r["base_rank"], r["gap_to_top"], r["reachable_within_w_h"],
                         r["correct_cap"], r["q"]))
        return
    if args.tail:
        # ALWAYS a role SWEEP -- the tail-efficacy sign is role-dependent (affinity is per-role), so a
        # single-role headline would misrepresent. AE/DS/CTO + cold-start floor.
        roles = tuple(r.strip() for r in args.roles.split(",")) if args.roles else ("AE", "DS", "CTO", "")
        per_role = {}
        for r in roles:
            res = run_tail_eval(role=r, verbose=args.verbose)
            per_role[r or "(cold-start)"] = {k: v for k, v in res.items() if k != "rows"}
        signs = [v["tail_efficacy_sign"] for v in per_role.values()]
        overall = ("robust-positive" if all(s == "positive" for s in signs) else
                   ("mixed-role-dependent" if "positive" in signs else
                    ("negative" if "negative" in signs else "zero")))
        sweep = {
            "corpus": "non-vetted tail (NFRA_COMPPROOF C1 basis-b)",
            "per_role": per_role,
            "overall_sign": overall,
            "flip_recommendation": (
                "ROLE-DEPENDENT / not-robust: tail-efficacy is positive only at some roles and the "
                "positive is small-N + composition-fragile -> do NOT authorize the value-flip on this "
                "alone; route to w_h/affinity calibration (CTO's separate pre-flip gate) + CVO~B "
                "honesty-gate on the labels + the high-affinity-tool concentration"
                if overall == "mixed-role-dependent" else
                ("HOLD value-flip: zero tail-efficacy (affinity moves but does not improve) -> "
                 "w_h/affinity calibration is the separate pre-flip gate" if overall == "zero" else
                 ("HOLD: negative tail-efficacy" if overall == "negative" else
                  "flip-authorization evidence: robust positive across roles"))),
            "honesty_caveats": [
                "labelable non-vetted band is intrinsically narrow (N per role ~11); labels softer than fixture BY NATURE OF THE TAIL",
                "any positive concentrates on a few toward-changes; leave-one-out fragile -> CVO~B honesty-gate",
                "base tail precision is very low regardless of arm -> the router itself is weak on oblique phrasings (separate router-quality finding, independent of affinity)",
            ],
        }
        if args.json:
            os.makedirs(os.path.dirname(_TAIL_REPORT), exist_ok=True)
            with open(_TAIL_REPORT, "w", encoding="utf-8") as fh:
                json.dump(sweep, fh, indent=1)
            print("OK: wrote %s" % _TAIL_REPORT)
        print(json.dumps(sweep, indent=1))
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
