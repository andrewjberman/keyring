"""
NFRA_COMPROUTE Charter-1 -- POTION SemanticRelevanceProvider (the route() stage-2 relevance swap).

Feeds comp_route.route(relevance_provider=...) : replaces the LEXICAL query_match token-overlap relevance
(w_q term) with POTION semantic cosine + a lexical-exact-NAME secondary boost (CTO POTION design build-
shape). Structural gates (write_path/E1), surface_prior (w_s), affinity (w_h) + the extractors are ALL
UNCHANGED -- this swaps ONLY the relevance input, per design.

FAIL-SAFE (CTO gate #5): built from potion_embed.load_embedder() which returns None on any load failure;
build_provider() then returns None -> route() falls back to lexical (valid-if-weaker) + the alarm already
fired. The semantic path NEVER crashes the router.

SCALE: semantic cosine is mapped to [0,1] via max(0, cos) (a negative cosine = semantically opposite =
irrelevant -> 0), keeping the relevance in the same [0,1] band the lexical query_match produced so the
posterior weights (w_q) + relevance_floor stay comparable. name_boost is a small additive (default 0.15);
per CTO -- MEASURE it, do NOT over-tune to force top1 (that is the mini-Goodhart).

Author: 0.8.0_AE_CloudComp~E (NFRA_COMPROUTE Charter-1). 2026-07-07.
"""

from __future__ import annotations

import os
import sys
from typing import Optional

_HERE = os.path.dirname(os.path.abspath(__file__))
for _p in (_HERE, os.path.join(_HERE, "potion")):
    if _p not in sys.path:
        sys.path.insert(0, _p)


class SemanticRelevanceProvider:
    """relevance(intent, cap) -> (score_in_0_1, matched_terms), a drop-in for query_match in the posterior."""

    def __init__(self, embedder, cap_texts: dict, cap_keywords: dict, name_boost: float = 0.15,
                 blend: bool = False):
        from potion_embed import cosine  # noqa: PLC0415
        self._cos = cosine
        self._emb = embedder
        self._nb = float(name_boost)
        self._blend = bool(blend)
        self._kw = {k: set(str(x).lower() for x in (v or [])) for k, v in cap_keywords.items()}
        self._cap_vecs = {cid: embedder.embed(txt or cid) for cid, txt in cap_texts.items()}
        self._keywords_by_id = {k: list(v or []) for k, v in cap_keywords.items()}

    def relevance(self, intent: str, cap):
        cid = getattr(cap, "id", "")
        cv = self._cap_vecs.get(cid)
        if cv is None:
            return 0.0, ()
        iv = self._emb.embed(intent or "")
        sem = max(0.0, self._cos(iv, cv))        # [0,1] band (negative cosine -> irrelevant)
        # BLEND (CTO ruling: semantic-primary + STRONG-LEXICAL PRESERVE, NOT pure-semantic-replacement --
        # pure-semantic demoted comp-pii top-1, CVO~B c330fdebf). max(lexical, semantic): where lexical is
        # STRONG it self-preserves (keeps the lexical top-1); where lexical is ~0 (oblique) semantic drives
        # (keeps the 11->4 oblique lift). Satisfies BOTH per-case gates 1+2 by construction -- MEASURED.
        score = sem
        if self._blend:
            from comp_route import query_match  # noqa: PLC0415
            lex, _lm = query_match(intent or "", self._keywords_by_id.get(cid, []))
            score = max(sem, lex)
        itoks = set((intent or "").lower().split())
        names = self._kw.get(cid, set()) | {cid.replace("comp-", "")}
        matched = tuple(sorted(itoks & names))
        if matched:                              # lexical-exact-NAME secondary boost
            score = min(1.0, score + self._nb)
        return score, matched


def _cap_texts_and_keywords():
    """Per-cap description text (richest use_case/does) + keywords -- the same source the fixture ranks
    against (mirrors comp_route_shadow._gather_cases / potion_shadow_rank)."""
    import comp_route_shadow as _sh
    man = _sh._T._load_manifest()
    ti = man.get("tools_index", {})
    by_tool = {}
    for e in man.get("entries", []):
        by_tool.setdefault(str(e.get("tool", "")).split()[0], []).append(e)
    provider = _sh.capmap.get_provider()
    texts, kws = {}, {}
    for c in provider.capabilities():
        ucs = by_tool.get(c.id, [])
        texts[c.id] = (ucs[0]["use_case"] if ucs else ti.get(c.id, {}).get("does", "")) or c.id
        kws[c.id] = set(getattr(c, "keywords", []) or [])
    return texts, kws


def build_provider(name_boost: float = 0.15, model_dir: str = "",
                   blend: bool = False) -> Optional[SemanticRelevanceProvider]:
    """FAIL-SAFE factory: returns a SemanticRelevanceProvider, or None if the POTION embedder can't load
    (-> route() uses lexical + the alarm already fired). No crash. blend=True -> max(lexical,semantic)
    strong-lexical-preserve (CTO's ruled LIVE-flip shape)."""
    from potion_embed import load_embedder  # noqa: PLC0415
    emb = load_embedder(model_dir=model_dir)
    if emb is None:
        return None
    texts, kws = _cap_texts_and_keywords()
    return SemanticRelevanceProvider(emb, texts, kws, name_boost=name_boost, blend=blend)
