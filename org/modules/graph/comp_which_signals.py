"""
NFRA_COMPROUTE DR2 -- the SignalExtractors + the 2-tier intent classifier (~C's surface side).

The vetted curated / surface-first / fuzzy layers of comp-which become SignalExtractors feeding DR1's
3-stage route() as PRIORS, instead of pre-router return-gates. Each extractor REUSES comp-which's
existing signal functions (imported live, not duplicated) and maps them to the locked interface
(~E DR1): `ex(intent, ctx_d) -> iterable[{cap_id, confidence, vetted}]`.

BANDED SCORING (CTO ruling 2026-07-01, structural not tuned): route() scores a VETTED signal at
1.0 + confidence (dominant band [1.0, 2.0)); a SOFT (fuzzy) signal adds into the base band [0, 1).
So a vetted match ALWAYS outranks non-vetted -> the vetted hot path (34/34 self + 20 paraphrase + 3
audit) is preserved by CONSTRUCTION; no-regression is a theorem, not a calibration. Within the vetted
band, curated (confidence 1.0 -> 2.0) outranks surface-first (confidence < 1.0 -> [1.0, 2.0)) -- so the
existing "surface-first never steals a vetted curated route" invariant falls out of confidence-ordering.

SEV1 SAFETY: this module does NOT touch the live comp-which. The DR2 shadow harness runs route()+these
extractors in PARALLEL with today's cascade to prove ZERO regression BEFORE the flip (which is
hard-gated on CVO~B's DRV cert). Author: 0.8.0_AE_CloudComp~C (NFRA_COMPROUTE.DR2). 2026-07-01.
"""

from __future__ import annotations

import importlib.util
import os
import re

_HERE = os.path.dirname(os.path.abspath(__file__))
_WS = os.path.abspath(os.path.join(_HERE, "..", "..", ".."))
_COMP_WHICH = os.path.join(_WS, ".tools", "comp-which")


def _load_comp_which():
    """Import the live comp-which (a python3 script, no .py ext) for its signal functions/regexes/RULES.
    Module-level is side-effect-free (functions defined, main() guarded), so this only loads the logic.
    A no-extension file needs an explicit SourceFileLoader (spec_from_file_location can't infer one)."""
    from importlib.machinery import SourceFileLoader
    loader = SourceFileLoader("comp_which_live", _COMP_WHICH)
    spec = importlib.util.spec_from_loader("comp_which_live", loader)
    mod = importlib.util.module_from_spec(spec)
    loader.exec_module(mod)
    return mod


_CW = _load_comp_which()


def _cap_from_call(call: str) -> str:
    """The cap_id (tool name) from a comp-which call string: 'comp-pipescript io <script>' -> 'comp-pipescript'.
    cap_id must equal a provider Capability.id (the .tools/comp-* tool name)."""
    tok = (call or "").strip().split()
    return tok[0] if tok else ""


def _curated_hits(intent: str):
    """Reproduce comp-which's curated hit computation (GOLD_ID / CALLSITE / HEAT / RULES) -- the SAME
    signal comp-which's cascade uses -> [(score, label, calls, why)], sorted strongest-first."""
    q = (intent or "").strip()
    qtok = _CW._tokens(q)
    hits = []
    gid = _CW.GOLD_ID.search(q)
    if gid:
        hits.append((6, "gold-id", ["comp-pipescript io %s" % gid.group(0)], ""))
    if _CW.CALLSITE_RX.search(q):
        hits.append((6, "callsites", ["comp-blast"], ""))
    if _CW.HEAT_RX.search(q):
        hits.append((6, "heat", ["comp-heat freshness"], ""))
    for keywords, label, calls, why in _CW.RULES:
        s = _CW._score_rule(q, qtok, keywords)
        if s > 0:
            hits.append((s, label, calls, why))
    hits.sort(key=lambda x: -x[0])
    return hits


# mirrors comp-which main()'s STRONG (`best_score >= STRONG` => route curated). A curated hit is the
# VETTED hot path ONLY at/above STRONG; a WEAK hit (< STRONG) is NOT routed by comp-which (it falls to
# surface-first/fuzzy) -- so it must NOT dominate here, or route() would steal a fuzzy/surface route.
_STRONG = 4


def curated_extractor(intent, ctx_d):
    """VETTED. comp-which's curated rules -> the routed tool(s). comp-which routes a hit by _route_print-ing
    ALL its `calls` (a rule can name MULTIPLE tools, e.g. portal/route -> comp-transform|comp-routes|pipescript)
    and shows the top hits together -- the fixture asserts the expected tool is AMONG them. So emit EVERY
    cap_id from a routed hit's calls (co-equal within the hit -> route() surfaces them, matching the list).
    STRONG hits (>= STRONG) are the vetted hot path; if there is NO strong hit, comp-which still routes the
    TOP weak hit (cascade step 6 `if hits: _route_print`) -- reproduce that at a lower (below-fuzzy) confidence."""
    hits = _curated_hits(intent)
    if not hits:
        return []
    is_strong = hits[0][0] >= _STRONG
    out = []
    seen = set()
    for rank, (score, _label, calls, _why) in enumerate(hits[:3]):
        if is_strong:
            if score < _STRONG:
                continue
            conf = max(0.15, min(1.0, score / 6.0) - 0.12 * rank)   # rank-decayed vetted hot path
        else:
            if rank != 0:                                          # only the TOP weak hit routes (step 6)
                continue
            conf = 0.4                                             # weak-curated: below curated-strong/surface-first
        for call in (calls or []):
            cid = _cap_from_call(call)
            if cid and cid not in seen:
                seen.add(cid)
                out.append({"cap_id": cid, "confidence": conf, "vetted": True})
    return out


def surface_first_extractor(intent, ctx_d):
    """VETTED (the CI-guarded coverage-map). comp-which's surface-first ledger drill -> the surface's
    tool(s). Confidence in [0, 1) (below curated's 1.0), rank-decayed within the surface toolkit."""
    q = (intent or "").strip()
    qtok = _CW._tokens(q)
    sf = _CW._surface_first(q, qtok)
    if not sf:
        return []
    _sid, _high, drilled, _gap = sf
    out = []
    seen = set()
    for rank, item in enumerate((drilled or [])[:4]):
        tool = item[0] if isinstance(item, (list, tuple)) else str(item)
        cid = _cap_from_call(tool)
        if not cid or cid in seen:
            continue
        seen.add(cid)
        out.append({"cap_id": cid, "confidence": max(0.05, 0.85 - 0.15 * rank), "vetted": True})
    return out


_MF_STRONG = 3   # mirrors comp-which main()'s MF_STRONG: a manifest-backstop overlap that EARNS a route.


def fuzzy_extractor(intent, ctx_d):
    """comp-which's manifest-fuzzy backstop -> tool(s). comp-which ROUTES a CONFIDENT fuzzy match
    (mf[0] overlap >= MF_STRONG) -- but ONLY when the query is NOT a search-verb query (a search verb
    greps FIRST, cascade step 3, before fuzzy step 4). So reproduce: the confident-fuzzy TOP is a VETTED
    signal (dominant, but BELOW curated/surface-first in the vetted band -> matches comp-which's cascade
    order strong-curated > surface-first > fuzzy); the rest / a weak fuzzy stay SOFT (base band). A
    search-verb query emits NO vetted fuzzy -> route() floors to the grep/glob fallback, as comp-which greps."""
    q = (intent or "").strip()
    qtok = _CW._tokens(q)
    mf = _CW._manifest_matches(q, qtok)
    if not mf:
        return []
    search_intent = bool(_CW.SEARCHVERB_RX.search(q))
    # comp-which routes a CONFIDENT fuzzy (mf[0] overlap >= MF_STRONG, non-search-verb) by showing the
    # TOP-N closest tools TOGETHER (the fixture asserts the expected tool is among them). Emit the top-N
    # co-equal VETTED (below surface-first/curated) -> route() DISAMBIGUATES them -> the expected surfaces.
    confident = (float(mf[0][0]) >= _MF_STRONG and not search_intent)
    out = []
    seen = set()
    for rank, row in enumerate(mf[:4]):
        overlap, tool, call = row[0], row[1], (row[2] if len(row) > 2 else "")
        cid = _cap_from_call(tool or call)
        if not cid or cid in seen:
            continue
        seen.add(cid)
        if confident and rank < 3:
            out.append({"cap_id": cid, "confidence": 0.5, "vetted": True})     # co-equal top-N -> disambiguation
        else:
            out.append({"cap_id": cid, "confidence": min(0.999, float(overlap) / 5.0), "vetted": False})
    return out


EXTRACTORS = [curated_extractor, surface_first_extractor, fuzzy_extractor]


# ============================================================================================
# 2-TIER INTENT RAIL (COMPRAIL rescope) -- Tier-1 cheap SYNTACTIC classification at the hook.
# navigation/read on an Opal property -> route; shell/active-computation -> FREE. Tier-2 (ambiguous)
# defers to the router. The rail-log measures classification accuracy for outcome-anchored tuning.
# ============================================================================================
# COMPUTE (active computation -> FREE): interpreters/build/deploy/vcs/test/container runners.
_COMPUTE_RX = re.compile(
    r"^\s*(python3?|pip3?|npm|npx|node|bun|deno|terraform|tofu|git|pytest|make|docker|"
    r"bash|sh|zsh|cargo|go|mvn|gradle|ruby|perl|java|dotnet|\./|\.tools/|safe-|comp-to)\b", re.I)
# NAVIGATE/READ (repo/estate navigation + inspection -> ROUTE to a read surface):
_NAVIGATE_RX = re.compile(
    r"^\s*(grep|egrep|fgrep|rg|ack|find|fd|ls|tree|glob|"
    r"aws\s+\S+\s+(describe|list|get|ls|lookup|scan|query|head))\b", re.I)


def classify_command(command: str) -> str:
    """Tier-1 syntactic intent class for a shell command. Returns 'compute' (FREE) / 'navigate' (ROUTE)
    / '' (ambiguous -> Tier-2 router). COMPUTE wins over NAVIGATE (a `python x.py` that greps is compute)."""
    c = (command or "").strip()
    if not c:
        return ""
    if _COMPUTE_RX.search(c):
        return "compute"
    if _NAVIGATE_RX.search(c):
        return "navigate"
    return ""


# A comp-which QUESTION describing a genuine WRITE/mutate ACTION (rebuild/re-derive/refresh-cache) is a
# COMPUTE intent -- the agent wants to DO the write, so it's FREE (not read-routed) and DR1's E1 mode
# pre-filter is skipped (a write-path tool like comp-build MAY surface). Everything else is a knowledge
# READ (the router's default). Kept TIGHT to the genuine write-path verbs so it never mis-flags a read
# ("will this pass its checks before I push" stays read -- it's a validation question, not a write).
_WRITE_ACTION_RX = re.compile(
    r"\b(re-?build|re-?generate|re-?derive|derive (the|a|my|cloud|graph)|refresh (the )?(cache|graph|derive)|"
    r"materialize|re-?materialize|persist (the )?(graph|cache)|write (the )?(source[- ]?map|cache))\b", re.I)


def classify_query_intent(query: str) -> str:
    """NL intent class for a comp-which question (the router surface): 'compute' for a genuine write/mutate
    action (E1 mode-filter skipped, free), else 'read' (the default -- routed, E1 excludes write-path tools)."""
    return "compute" if _WRITE_ACTION_RX.search(query or "") else "read"


if __name__ == "__main__":
    import json
    import sys
    # quick extractor smoke on the CLI arg intent
    intent = " ".join(sys.argv[1:]) or "what produces canonical_prices.parquet"
    ctx = {"role": "", "intent_class": "read"}
    print("intent: %s" % intent)
    for name, ex in (("curated", curated_extractor), ("surface_first", surface_first_extractor),
                     ("fuzzy", fuzzy_extractor)):
        print("  %-14s -> %s" % (name, json.dumps(ex(intent, ctx))))
