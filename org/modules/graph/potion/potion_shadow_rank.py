"""
NFRA_COMPROUTE Charter-1 -- POTION shadow residual-rank measurement (the CTO-required deliverable).

Measures the POST-FIX RESIDUAL RANK of the correct cap on the C1 non-vetted tail corpus under SEMANTIC
relevance (POTION cosine + lexical-exact-NAME boost), vs the LEXICAL baseline (query_match, which buries
the correct cap at ~rank-11 -- the C1-measured disease). The residual is what SIZES Charter-2 (CVO~B):
a small residual -> intent-conditioned affinity has standalone value on a near-top cap; a large residual
-> base still buries it. SHADOW-ONLY: measures, does NOT touch live comp-which.

Also does CTO refinement #3: SHADOW-TEST 2M vs 8M -> report the residual for BOTH so the SMALLEST model
that achieves the drop is picked (don't default to richer -- earn it).

Run:  python org/modules/graph/potion/potion_shadow_rank.py --model-dir <2M_dir> [--label 2M] [--verbose]
      (point --model-dir at the vendored model, or a local snapshot for the pre-vendor shadow-test)
Read-only, deterministic, ASCII.  Author: 0.8.0_AE_CloudComp~E. 2026-07-07.
"""

from __future__ import annotations

import argparse
import json
import os
import statistics as st
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_GRAPH = os.path.dirname(_HERE)
for _p in (_HERE, _GRAPH):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import comp_route_shadow as _sh        # noqa: E402  cap provider + fixture
import comp_route_eval as _ev          # noqa: E402  the _TAIL corpus + _route_arm
from potion_embed import PotionEmbedder, cosine  # noqa: E402


def _cap_texts():
    """Per-cap description text to embed (the same richest use_case/does the fixture ranks against)."""
    man = _sh._T._load_manifest()
    ti = man.get("tools_index", {})
    by_tool = {}
    for e in man.get("entries", []):
        by_tool.setdefault(str(e.get("tool", "")).split()[0], []).append(e)
    texts, kws = {}, {}
    provider = _sh.capmap.get_provider()
    routable = {c.id for c in provider.capabilities() if getattr(c, "routable", True)}
    for c in provider.capabilities():
        t = c.id
        ucs = by_tool.get(t, [])
        desc = (ucs[0]["use_case"] if ucs else ti.get(t, {}).get("does", "")) or t
        texts[t] = desc.strip()
        kws[t] = set(str(k).lower() for k in getattr(c, "keywords", []) or [])
    return texts, kws, routable


def semantic_rank(emb: PotionEmbedder, intent, cap_vecs, cap_ids, kws, accept, name_boost=0.15):
    """Rank caps by SEMANTIC cosine + a lexical-exact-NAME secondary boost (CTO build-shape). Return the
    best-ranked correct cap's 1-based rank (or None)."""
    iv = emb.embed(intent)
    itoks = set(intent.lower().split())
    scored = []
    for cid, cv in zip(cap_ids, cap_vecs):
        s = cosine(iv, cv)
        # lexical-exact-NAME secondary boost: the intent literally names the tool / a keyword.
        if cid.replace("comp-", "") in itoks or (kws.get(cid, set()) & itoks):
            s += name_boost
        scored.append((s, cid))
    scored.sort(key=lambda x: (-x[0], x[1]))
    order = [cid for _, cid in scored]
    pos = [i for i, cid in enumerate(order) if cid in accept]
    return (pos[0] + 1) if pos else None


def measure(model_dir, label, verbose=False):
    emb = PotionEmbedder(model_dir)   # pre-vendor shadow: no manifest hash-gate (measuring, not serving)
    texts, kws, routable = _cap_texts()
    cap_ids = [c for c in texts if c in routable]
    cap_vecs = [emb.embed(texts[c]) for c in cap_ids]
    sem_ranks, lex_ranks = [], []
    provider = _sh.capmap.get_provider()
    for q, accept in _ev._TAIL:
        # LEXICAL baseline rank (affinity-actable tail only, same filter as --rank)
        r, _ic = _ev._route_arm(q, provider, None, "AE")
        if not r.ranked or (r.ranked[0].vetted and r.kind != "fallback"):
            continue
        ids = [s.cap.id for s in r.ranked]
        lpos = [i for i, cid in enumerate(ids) if cid in accept]
        if not lpos:
            continue
        lex_rank = lpos[0] + 1
        sem_rank = semantic_rank(emb, q, cap_vecs, cap_ids, kws, accept)
        lex_ranks.append(lex_rank)
        sem_ranks.append(sem_rank)
        if verbose:
            print("  lexical=%2d  semantic=%2s | %s" % (lex_rank, sem_rank, q[:40]))
    n = len(lex_ranks)
    def med(xs):
        xs = [x for x in xs if x is not None]
        return st.median(xs) if xs else None
    def top1(xs):
        return sum(1 for x in xs if x == 1)
    return {
        "model": label, "dim": emb.dim, "tail_n": n,
        "lexical_rank_median": med(lex_ranks), "lexical_rank_mean": round(st.mean(lex_ranks), 1) if n else None,
        "lexical_top1": top1(lex_ranks),
        "semantic_rank_median": med(sem_ranks),
        "semantic_rank_mean": round(st.mean([x for x in sem_ranks if x is not None]), 1) if any(sem_ranks) else None,
        "semantic_top1": top1(sem_ranks),
        "residual_rank_reduction_median": (med(lex_ranks) - med(sem_ranks))
            if (med(lex_ranks) is not None and med(sem_ranks) is not None) else None,
    }


def main():
    ap = argparse.ArgumentParser(description="POTION shadow residual-rank (2M vs 8M)")
    ap.add_argument("--model-dir", required=True)
    ap.add_argument("--label", default="model")
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()
    res = measure(args.model_dir, args.label, verbose=args.verbose)
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
