"""
comp-route-affinity -- the CachedAffinityProvider + affinity-cache emitter (NFRA_COMPROUTE learned term).

The bridge from the COMPLEARN signal (tool_activity outcomes) to the COMPROUTE engine's LEARNED term
(w_h). Per the CTO grain ruling (2026-07-01): the learned affinity is PER-CAP-ID with an m-estimate
whose prior is the cap's surface_prior (passed by the engine at route-time). This module:
  - computes per-(cap_id, role) outcome SUFFICIENT STATISTICS {sum_v, n} from tool_activity into a
    small JSON cache, and
  - serves them as a fast O(1) AffinityProvider the engine consumes (no per-call corpus load -- comp-which
    is the hottest path).

SHADOW MODE (CTO seq step 3): the affinity is COMPUTED + logged, NOT weighting the live comp-which
decision. comp-which keeps affinity_provider=None until real routing-OUTCOME telemetry (with validated
inference-attribution quality) justifies activation (step 4 -- bring CTO the justification first). A
learned term off a weakly-attributed proxy is still a proxy; SHADOW guards it (calibrate-on-real-telemetry).

ONE SIGNAL, TWO CONSUMERS: reuses comp_route.outcome_value verbatim (the same outcome-weighting the P2
scorer + the L3 engine use). Read-only, deterministic, lane-portable, ASCII.

Usage:
    comp-route-affinity emit [--out PATH]     # (re)compute the cache from the live tool_activity corpus
    comp-route-affinity show [--cache PATH]   # summarize the cache (top per-cap affinities)
    comp-route-affinity shadow "<intent>" [--role R] [--surface-affinity k:v,...]  # what w_h WOULD add (shadow)
    comp-route-affinity --self-test

Author: 0.8.0_AE_CloudComp~E (NFRA_COMPROUTE learned-term bridge). 2026-07-01.
Spec: docs/architecture/NFRA_COMPROUTE_PRD.md section 2 + the CTO grain ruling (per-cap-id, m-estimate prior=surface).
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from collections import defaultdict
from typing import Mapping, Optional

_WS = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
sys.path.insert(0, _WS)
from org.modules.graph.comp_route import outcome_value  # noqa: E402 -- one signal, two consumers

CACHE_PATH = "org/mcp/comproute-affinity-cache.json"
_SEP = "\t"   # cap_id<TAB>role key (JSON-safe, unambiguous vs comp-tool names)


# ============================================================================================
# Cache computation -- per-(cap_id, role) outcome sufficient statistics.
# ============================================================================================
def _is_real_cap(tool: str, valid_caps: Optional[set]) -> bool:
    """A cache entry must be a REAL capability id. Prefer the provider's cap-id set; else a sanity
    filter (the rolling-log `tool` column can carry non-tool summary text like '(session summary)')."""
    if not tool:
        return False
    if valid_caps:
        return tool in valid_caps
    return "(" not in tool and " " not in tool and len(tool) <= 40


def build_affinity_stats(rows: list, valid_caps: Optional[set] = None) -> dict:
    """Aggregate per-(cap_id, role) outcome sufficient stats {sum_v, n} from tool_activity rows.
    cap_id == the row's `tool` (filtered to REAL caps); the outcome value is the SHARED
    comp_route.outcome_value (result-class + gap bonus, never count). SHADOW source = tool-run outcomes
    (rolling-log) until routing-OUTCOME capture lands (the real per-route resolution signal)."""
    stats: dict = defaultdict(lambda: {"sum": 0.0, "n": 0})
    for r in rows:
        tool = r.get("tool")
        if not _is_real_cap(tool, valid_caps):
            continue
        s = stats[(tool, r.get("role") or "")]
        s["sum"] += outcome_value(r)
        s["n"] += 1
    return stats


def emit_affinity_cache(rows: list, out_path: str = "", k: int = 5,
                        valid_caps: Optional[set] = None) -> tuple[str, int]:
    """Compute + write the per-cap-id affinity cache (sufficient stats). Returns (path, n_entries)."""
    stats = build_affinity_stats(rows, valid_caps=valid_caps)
    cache = {
        "k": k, "grain": "per-cap-id", "mode": "shadow",
        "note": "SHADOW -- computed, NOT weighting the live comp-which decision until real "
                "routing-outcome telemetry justifies activation (CTO seq step 4). Source = tool-run "
                "outcomes (proxy) until routing-outcome capture lands.",
        "entries": {f"{cap}{_SEP}{role}": {"sum": round(v["sum"], 4), "n": v["n"]}
                    for (cap, role), v in stats.items()},
    }
    p = out_path or os.path.join(_WS, CACHE_PATH)
    with open(p, "w", encoding="utf-8") as fh:
        json.dump(cache, fh, indent=2, sort_keys=True)
    return p, len(cache["entries"])


# ============================================================================================
# The AffinityProvider -- fast O(1), applies the m-estimate with the runtime surface-prior.
# ============================================================================================
class CachedAffinityProvider:
    """AffinityProvider off the pre-computed cache (fast O(1); no per-call corpus load). Implements the
    NFRA_COMPROUTE AffinityProvider protocol: affinity(cap_id, role, ctx, prior). Applies the m-estimate
    (sum + k*prior)/(n + k) with the RUNTIME prior (the cap's surface_prior the engine passes), so a hot
    cap converges to its per-cap outcome mean and a cold cap backs off to the surface-grain prior. Absent
    cap -> prior (the (c) hybrid, subsumed). Load failure -> empty cache -> every cap backs off (safe)."""

    def __init__(self, cache_path: str = "", k: Optional[int] = None):
        self._c: dict = {}
        self._k = 5
        p = cache_path or os.path.join(_WS, CACHE_PATH)
        try:
            with open(p, encoding="utf-8") as fh:
                d = json.load(fh)
            self._k = k if k is not None else int(d.get("k", 5))
            self._c = d.get("entries", {})
        except Exception:  # noqa: BLE001 -- no cache => every cap backs off to prior (safe cold-start)
            self._c = {}

    def affinity(self, cap_id: str, role: str, ctx: Mapping, prior: Optional[float] = None) -> Optional[float]:
        e = self._c.get(f"{cap_id}{_SEP}{role or ''}") or self._c.get(f"{cap_id}{_SEP}")
        if not e or not e.get("n"):
            return prior   # cold cap -> surface-grain backoff (None if the engine passed none)
        p = prior if prior is not None else 0.5
        return (e["sum"] + self._k * p) / (e["n"] + self._k)


# ============================================================================================
# Live-corpus emit (reuses the COMPLEARN corpus loader -- rolling + routing rows).
# ============================================================================================
def _live_rows() -> list:
    """tool_activity rows from the live corpus (rolling-log outcomes now; routing-outcomes once
    capture lands). Best-effort: [] if the loader is unavailable."""
    try:
        from org.modules.graph.comp_learns_score import load_corpus
        c = load_corpus()
        return list(c.get("rolling", [])) + list(c.get("routing", []))
    except Exception:  # noqa: BLE001
        return []


# ============================================================================================
# Self-test
# ============================================================================================
def _self_test() -> tuple[bool, list]:
    checks = []

    def ck(name, ok, detail=""):
        checks.append({"check": name, "pass": bool(ok), "detail": detail})
        return ok

    # A hot cap converges toward its per-cap outcome mean; a low-outcome cap scores lower -- outcome,
    # not count (the shared outcome_value).
    rows = ([{"tool": "comp-good", "role": "AE", "result": "PASS"}] * 10
            + [{"tool": "comp-bad", "role": "AE", "result": "FAIL"}] * 10)
    import tempfile
    fd, tmp = tempfile.mkstemp(suffix=".json")
    os.close(fd)
    emit_affinity_cache(rows, out_path=tmp, k=5)
    prov = CachedAffinityProvider(cache_path=tmp)
    a_good = prov.affinity("comp-good", "AE", {}, prior=0.5)
    a_bad = prov.affinity("comp-bad", "AE", {}, prior=0.5)
    ck("hot_cap_reflects_outcome_not_count", a_good > 0.8 and a_bad < 0.2 and a_good > a_bad,
       f"good={a_good:.3f} bad={a_bad:.3f}")

    # A cold cap (absent) backs off to the passed surface-prior (the (c) hybrid).
    a_cold = prov.affinity("comp-never-seen", "AE", {}, prior=0.7)
    ck("cold_cap_backs_off_to_prior", a_cold == 0.7, f"cold={a_cold}")

    # Usage does NOT rescue a LOW-outcome cap (m-estimate mean, not sum): 100 FAILs -> ~0, not up. (More
    # data on a HIGH-outcome cap correctly CONVERGES toward its true mean -- that's confidence, not
    # inflation; the anti-Goodhart invariant is that OUTCOME, not count, sets the direction.)
    spam = [{"tool": "comp-spam", "role": "AE", "result": "FAIL"}] * 100
    fd2, tmp2 = tempfile.mkstemp(suffix=".json")
    os.close(fd2)
    emit_affinity_cache(spam, out_path=tmp2, k=5)
    a_spam = CachedAffinityProvider(cache_path=tmp2).affinity("comp-spam", "AE", {}, prior=0.5)
    ck("usage_does_not_rescue_low_outcome", a_spam < 0.1,
       f"100 FAILs -> {a_spam:.3f} (count does not inflate a low-outcome cap)")

    # Missing cache -> safe: every cap backs off to prior (no crash).
    safe = CachedAffinityProvider(cache_path=os.path.join(_WS, "does-not-exist.json"))
    ck("missing_cache_is_safe", safe.affinity("x", "AE", {}, prior=0.3) == 0.3, "")

    for t in (tmp, tmp2):
        try:
            os.remove(t)
        except OSError:
            pass
    ok = all(c["pass"] for c in checks)
    return ok, checks


def main() -> int:
    ap = argparse.ArgumentParser(description="comp-route-affinity -- CachedAffinityProvider + cache emitter (SHADOW)")
    sub = ap.add_subparsers(dest="cmd")
    pe = sub.add_parser("emit", help="(re)compute the cache from the live tool_activity corpus")
    pe.add_argument("--out", default="")
    ps = sub.add_parser("show", help="summarize the cache")
    ps.add_argument("--cache", default="")
    psh = sub.add_parser("shadow", help="what w_h WOULD add for an intent (shadow -- not live)")
    psh.add_argument("intent")
    psh.add_argument("--role", default="")
    psh.add_argument("--surface-affinity", default="")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if args.self_test:
        ok, checks = _self_test()
        if args.json:
            print(json.dumps({"pass": ok, "checks": checks}, indent=2))
        else:
            print("=== comp-route-affinity --self-test ===")
            for c in checks:
                print(f"  [{'PASS' if c['pass'] else 'FAIL'}] {c['check']}" + (f"   ({c['detail']})" if c["detail"] else ""))
            print(f"\n{'OK: all checks pass' if ok else 'ERROR: one or more checks FAILED'}")
        return 0 if ok else 1

    if args.cmd == "emit":
        rows = _live_rows()
        valid = None
        try:
            from org.modules.graph.comp_capability_provider import get_provider
            valid = {getattr(c, "id", None) for c in get_provider().capabilities()}
            valid.discard(None)
        except Exception:  # noqa: BLE001 -- no provider => the sanity filter fallback applies
            valid = None
        p, n = emit_affinity_cache(rows, out_path=args.out, valid_caps=valid)
        print(json.dumps({"cache": p, "entries": n, "source_rows": len(rows), "mode": "shadow"}, indent=2)
              if args.json else f"OK: wrote affinity cache -> {p} ({n} per-cap-id entries from {len(rows)} rows). "
              f"SHADOW -- not weighting the live comp-which decision (CTO seq step 3).")
        return 0

    if args.cmd == "show":
        p = args.cache or os.path.join(_WS, CACHE_PATH)
        try:
            with open(p, encoding="utf-8") as fh:
                d = json.load(fh)
        except Exception as e:  # noqa: BLE001
            print(f"comp-route-affinity: cannot read cache {p} ({e})")
            return 1
        ents = d.get("entries", {})
        prov = CachedAffinityProvider(cache_path=p)
        ranked = sorted(ents.items(), key=lambda kv: -(kv[1]["sum"] / kv[1]["n"] if kv[1]["n"] else 0))
        print(f"=== affinity cache: {p}  ({len(ents)} entries, k={d.get('k')}, mode={d.get('mode')}) ===")
        for key, v in ranked[:25]:
            cap, _, role = key.partition(_SEP)
            mean = v["sum"] / v["n"] if v["n"] else 0.0
            print(f"  {cap:24s} role={role or '-':6s} n={v['n']:4d} mean_outcome={mean:.3f} "
                  f"(m-est@prior0.5={prov.affinity(cap, role, {}, prior=0.5):.3f})")
        return 0

    if args.cmd == "shadow":
        # SHADOW: route WITH the cached affinity vs WITHOUT, print the w_h delta -- calibration only.
        from org.modules.graph.comp_route import RouteContext, route
        try:
            from org.modules.graph.comp_capability_provider import get_provider
            provider = get_provider()
        except Exception as e:  # noqa: BLE001
            print(f"comp-route-affinity shadow: need ~C's provider ({e})")
            return 1
        sa = {}
        for pair in args.surface_affinity.split(","):
            if ":" in pair:
                s, _, val = pair.partition(":")
                try:
                    sa[s.strip()] = float(val)
                except ValueError:
                    pass
        # provider.surface_prior reads its own role_surface_affinity; sa is only a CLI hint if needed.
        ctx = RouteContext(role=args.role)
        cold = route(args.intent, ctx, provider)
        warm = route(args.intent, ctx, provider, affinity_provider=CachedAffinityProvider())
        print(f'=== SHADOW route: "{args.intent}" (role={args.role}) -- affinity NOT live, calibration only ===')
        print(f"  cold (live behavior): {cold.kind} -> "
              + (cold.decision.cap.id if cold.decision else ",".join(s.cap.id for s in cold.within_margin)))
        print(f"  warm (w/ shadow w_h): {warm.kind} -> "
              + (warm.decision.cap.id if warm.decision else ",".join(s.cap.id for s in warm.within_margin)))
        if cold.kind != warm.kind or [s.cap.id for s in cold.within_margin] != [s.cap.id for s in warm.within_margin]:
            print("  -> the learned term WOULD change this route (a calibration data point for step-4 activation)")
        return 0

    ap.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
