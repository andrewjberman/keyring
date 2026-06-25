#!/usr/bin/env python3
"""
S0 -- the shared heat_map analytic primitive (NFRA_HEATMAP macro).

ONE write-activity/freshness analytic, applied to TWO domains (NFRA_HEATMAP_SCOPING.md):
  - OBJECT substrate  -- repo/estate files; "heat" = per-path WRITE recency (git/mtime). -> O1-O4
  - PROCESS substrate -- OPLMCP UoW traffic; "heat" = invocation recency + frequency.    -> P0-P4
Both reduce to the same core: write/activity recency + decay -> hot/warm/cold, + locality
clustering ("a cold SUBTREE is a stronger signal than scattered cold items").

This module is a PURE library (no I/O, no git, no S3) -- the domain engines (O1 object-freshness,
the P-legs) gather the substrate's activity timestamps and call in here. Domain behaviour is
PARAMETERIZED via HeatParams (half-life, band thresholds, frequency weight), never branched.

ADVISORY boundary: this layer only SCORES + CLUSTERS. It NEVER recommends or deletes -- the
archive/delete RECOMMENDATION (O3) is a separate, guardrailed layer (ADVISORY-ONLY, never
auto-delete, blast-radius verify-before-recommend). Inheriting NFRA_DEBTSCAN doctrine.

Author: 0.4.0_DS_ClientPlatform (NFRA_EXPAND Strand-C, leg S0). 2026-06-25.
"""

from __future__ import annotations

import math
from collections import defaultdict
from dataclasses import dataclass
from typing import Callable, Iterable, Sequence

LN2 = math.log(2.0)


@dataclass(frozen=True)
class HeatParams:
    """Domain-parameterized scoring knobs. Defaults tuned for OBJECT (repo-file) hygiene;
    the PROCESS legs pass their own (e.g. shorter half-life, frequency-weighted)."""
    half_life_days: float = 30.0   # recency_score halves every this-many days of inactivity
    hot_days: float = 7.0          # age <= hot_days  -> band "hot"
    warm_days: float = 30.0        # age <= warm_days -> band "warm"; older -> "cold"
    freq_weight: float = 0.0       # 0 = recency-only (object default); >0 blends activity FREQUENCY

    def __post_init__(self) -> None:
        if self.half_life_days <= 0:
            raise ValueError("half_life_days must be > 0")
        if not (self.hot_days <= self.warm_days):
            raise ValueError("require hot_days <= warm_days")


@dataclass(frozen=True)
class HeatScore:
    item_id: str
    age_days: float          # days since last activity (>= 0)
    recency_score: float     # exp-decayed recency in (0, 1]
    frequency: int           # activity count over the window (1 if not tracked)
    score: float             # combined heat (recency, optionally frequency-blended)
    band: str                # "hot" | "warm" | "cold"


def recency_score(age_days: float, half_life_days: float) -> float:
    """Exponential decay: 1.0 at age 0, 0.5 at one half-life, ->0 as age grows."""
    age = max(0.0, age_days)
    return math.exp(-LN2 * age / half_life_days)


def classify_band(age_days: float, p: HeatParams) -> str:
    if age_days <= p.hot_days:
        return "hot"
    if age_days <= p.warm_days:
        return "warm"
    return "cold"


def score_item(item_id: str, age_days: float, frequency: int = 1,
               p: HeatParams | None = None) -> HeatScore:
    """Score a single item from its activity AGE (days since last write/invocation)."""
    p = p or HeatParams()
    rs = recency_score(age_days, p.half_life_days)
    if p.freq_weight:
        # log-damped frequency boost (a file written 100x isn't 100x hotter than 10x)
        combined = rs + p.freq_weight * math.log1p(max(0, frequency))
    else:
        combined = rs
    return HeatScore(item_id=item_id, age_days=max(0.0, age_days), recency_score=rs,
                     frequency=max(1, frequency), score=combined,
                     band=classify_band(age_days, p))


def score_items(items: Iterable[Sequence], now_ts: float,
                p: HeatParams | None = None) -> list[HeatScore]:
    """Score many items. Each item = (item_id, last_activity_ts_epoch[, frequency]).
    now_ts is passed in (caller-provided clock) so scoring is deterministic + testable."""
    p = p or HeatParams()
    out: list[HeatScore] = []
    for it in items:
        item_id = it[0]
        last_ts = float(it[1])
        freq = int(it[2]) if len(it) > 2 else 1
        age_days = max(0.0, (now_ts - last_ts) / 86400.0)
        out.append(score_item(item_id, age_days, freq, p))
    return out


def cluster_by_locality(scores: Sequence[HeatScore],
                        locality_fn: Callable[[str], str]) -> dict:
    """Group scored items by a domain LOCALITY key (objects: directory prefix; process:
    workflow/UoW). A cluster that is mostly COLD is a far stronger archive signal than
    scattered cold items -- O2 consumes cold_frac to detect dead subtrees. Returns
    {locality_key: {n, n_cold, cold_frac, mean_score, oldest_age_days, items[]}}."""
    groups: dict[str, list[HeatScore]] = defaultdict(list)
    for s in scores:
        groups[locality_fn(s.item_id)].append(s)
    out: dict[str, dict] = {}
    for key, g in groups.items():
        n = len(g)
        n_cold = sum(1 for s in g if s.band == "cold")
        out[key] = {
            "n": n,
            "n_cold": n_cold,
            "cold_frac": (n_cold / n) if n else 0.0,
            "mean_score": (sum(s.score for s in g) / n) if n else 0.0,
            "oldest_age_days": max((s.age_days for s in g), default=0.0),
            "items": [s.item_id for s in g],
        }
    return out


def summarize(scores: Sequence[HeatScore]) -> dict:
    """Band counts + score stats over a scored set (for O4 reporting / quick diagnostics)."""
    n = len(scores)
    bands = {"hot": 0, "warm": 0, "cold": 0}
    for s in scores:
        bands[s.band] += 1
    return {"n": n, "bands": bands,
            "cold_frac": (bands["cold"] / n) if n else 0.0,
            "mean_score": (sum(s.score for s in scores) / n) if n else 0.0}


if __name__ == "__main__":
    # self-test: deterministic clock; verify decay, banding, clustering.
    now = 1_000_000_000.0
    day = 86400.0
    sample = [
        ("a/fresh.py", now - 1 * day),       # hot
        ("a/recent.py", now - 20 * day),     # warm
        ("a/stale.py", now - 90 * day),      # cold
        ("b/dead1.py", now - 200 * day),     # cold
        ("b/dead2.py", now - 365 * day),     # cold
    ]
    scores = score_items(sample, now)
    for s in scores:
        print(f"  {s.item_id:16s} age={s.age_days:6.1f}d score={s.score:.4f} band={s.band}")
    assert scores[0].band == "hot" and scores[1].band == "warm" and scores[2].band == "cold"
    assert scores[0].score > scores[1].score > scores[2].score  # monotone decay
    assert abs(recency_score(30.0, 30.0) - 0.5) < 1e-9          # half-life check
    clusters = cluster_by_locality(scores, lambda p: p.split("/")[0])
    assert clusters["b"]["cold_frac"] == 1.0 and clusters["a"]["n"] == 3
    print("OK: heat_map S0 self-test passed; b/ is a fully-cold cluster (cold_frac=1.0).")
