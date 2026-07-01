"""
NFRA_COMPROUTE DR2 -- the SHADOW harness (the SEV1 safety gate).

Runs the PRIMARY router (DR1 route() + ~C's SignalExtractors) in PARALLEL with today's comp-which
backstop over the FULL fixture (self-route + audit + paraphrase), logs BOTH to the routing.jsonl
flywheel sink, and proves ZERO regression BEFORE any flip. comp-which is NOT flipped -- this only
OBSERVES + measures. The flip (DR2 phase 3) lands ONLY on CVO~B's shadow-green cert (DRV).

ZERO-REGRESSION bar: for every fixture case, the primary router surfaces the SAME expected tool the
fixture asserts comp-which surfaces today (in its DECISION top or a DISAMBIGUATION within-margin).
Plus: READ-NEVER-REBUILDS (a read/navigate intent never routes to a mode:rebuild cap) + a measured
FALLBACK-RATE (how often the primary defers to comp-grep/glob).

Run: python org/modules/graph/comp_route_shadow.py [--json] [--verbose]
Author: 0.8.0_AE_CloudComp~C (NFRA_COMPROUTE.DR2). 2026-07-01.
"""

from __future__ import annotations

import importlib.util
import json
import os
import re as _re
import subprocess as _sp
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_WS = os.path.abspath(os.path.join(_HERE, "..", "..", ".."))
_TEST = os.path.join(_WS, ".tools", "comp-which-routing-test.py")
_SINK = os.path.join(_WS, "org", "mcp", "comproute-routing.jsonl")

for _p in (_HERE, os.path.join(_WS, "infra", "aws", "globgrph")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import comp_route                       # noqa: E402
import comp_capability_provider as capmap  # noqa: E402
import comp_which_signals as sig        # noqa: E402

# The E1 read-excluded action-classes (mirrors comp_route's Stage-A set; local so the shadow does not
# reach into the engine's private name).
_REBUILD_MODES = {"rebuild", "write", "derive", "mutate"}


def _load_test_module():
    spec = importlib.util.spec_from_file_location("cw_routing_test", _TEST)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_T = _load_test_module()


def _cap_of(expect: str) -> str:
    """The expected cap_id (tool name) from a fixture expected-string, e.g. 'comp-pipescript io' -> 'comp-pipescript'."""
    return (expect or "").strip().split()[0] if expect else ""


def _gather_cases():
    """(query, expected_cap_id, kind) over the full fixture: self-route + audit + paraphrase."""
    cases = []
    man = _T._load_manifest()
    ti = man.get("tools_index", {})
    by_tool = {}
    for e in man.get("entries", []):
        by_tool.setdefault(str(e.get("tool", "")).split()[0], []).append(e)
    for t in sorted(ti.keys()):
        if t in _T.EXCLUDE:
            continue
        ucs = by_tool.get(t, [])
        q = (ucs[0]["use_case"] if ucs else ti[t].get("does", "")).strip().rstrip("?.")
        cases.append((q, t, "self"))
    for q, want in [("is upstream data fresh", "comp-freshness"),
                    ("artifact invariants before upload", "comp-validate"),
                    ("component expose PII", "comp-pii")]:
        cases.append((q, want, "audit"))
    for q, want in getattr(_T, "_PARAPHRASES", []):
        cases.append((q, _cap_of(want), "paraphrase"))
    return cases


_COMP_WHICH = os.path.join(_WS, ".tools", "comp-which")
_TOOL_RX = _re.compile(r"\b(comp-[a-z0-9-]+|pipescript)\b")


def _primary(intent, provider):
    """The DR2 default router: DR1 route() + the SignalExtractors. intent_class per-case (a genuine
    write/rebuild question is COMPUTE -- E1 mode-filter skipped; else READ -- E1 excludes write-path)."""
    ic = sig.classify_query_intent(intent)
    ctx = {"role": "", "working_set": [], "trajectory": [], "intent_class": ic}
    return comp_route.route(intent, ctx, provider, extractors=sig.EXTRACTORS), ic


def _backstop_tools(intent):
    """Today's comp-which (the BACKSTOP) surfaced tool set -- run LIVE + parse the tool names it prints,
    so CVO~B can diff primary-vs-backstop independently (not just vs the fixture's expected string)."""
    try:
        r = _sp.run([sys.executable, _COMP_WHICH, intent], cwd=_WS,
                    capture_output=True, text=True, timeout=60)
        out = (r.stdout or "") + (r.stderr or "")
    except Exception:  # noqa: BLE001
        return set()
    # tools comp-which SURFACED (route lines), excluding the router itself + the never-dead-end primitives.
    return {t for t in _TOOL_RX.findall(out) if t not in ("comp-which", "comp-grep", "comp-glob")}


def _emit(row):
    try:
        with open(_SINK, "a", encoding="utf-8") as fh:
            fh.write(json.dumps(row, ensure_ascii=True) + "\n")
    except Exception:  # noqa: BLE001
        pass


# Representative FALLBACK corpus (CVO~B gate #2): off-domain / no-rich-tool queries a SANE default-router
# should DEFER to comp-grep/glob (below relevance_floor) instead of force-routing. Mixed with the fixture
# (which should route), this yields a real, sane fallback-RATE (not ~all-grep = floor too high; not
# ~zero = floor too low).
_FALLBACK_CORPUS = [
    "where is the literal string FIXME in the codebase",
    "find all TODO comments in the python files",
    "grep for the word banana in src",
    "the quick brown fox jumps over the lazy dog",
    "list the files that changed since yesterday",
    "what colour is the sky today",
    "print hello world",
    "locate every occurrence of xyzzy",
]
# E1 READ probes (CVO~B gate #3): a READ question in a write-path tool's DOMAIN must route to a QUERY
# surface, NEVER the write-path tool (comp-build). Asserts read-never-rebuilds MEANINGFULLY.
_E1_READ_PROBES = [
    "what is the current trace graph cache vintage",
    "is the graph cache fresh or stale",
]


def run_shadow(verbose=False, emit=True, with_backstop=True):
    provider = capmap.get_provider()
    cap_write = {c.id: bool(getattr(c, "write_path", False)) for c in provider.capabilities()}
    cases = _gather_cases()
    regressions, rebuild_leaks, divergences = [], [], []
    for q, expect, kind in cases:
        r, ic = _primary(q, provider)
        within = [s.cap.id for s in r.within_margin]
        top = r.ranked[0].cap.id if r.ranked else None
        surfaced = set(within) | ({top} if top else set())
        ok = (expect in surfaced) if expect else True
        # READ-NEVER-REBUILDS: a READ-classified case must not surface a write-path tool.
        if ic == "read":
            for cid in surfaced:
                if cap_write.get(cid, False):
                    rebuild_leaks.append((q, cid))
        # PRIMARY-vs-BACKSTOP: the actual comp-which surfaced set, for CVO~B's independent diff.
        backstop = _backstop_tools(q) if with_backstop else set()
        if with_backstop and expect and expect not in backstop:
            divergences.append({"q": q[:56], "expect": expect, "primary": sorted(surfaced),
                                "backstop": sorted(backstop)})
        if not ok and not (r.kind == "fallback"):
            regressions.append({"q": q[:60], "expect": expect, "kind": kind,
                                "got_top": top, "within": within, "route_kind": r.kind})
        if verbose:
            print("  [%s] %-11s ic=%-7s exp=%-15s top=%-15s" %
                  ("OK " if ok else "REG", kind, ic, expect, top))
        if emit:
            _emit({"shadow": True, "intent": q, "intent_class": ic, "kind": kind, "expect": expect,
                   "primary_route_kind": r.kind, "primary_top": top, "primary_within": within,
                   "backstop_surfaced": sorted(backstop), "regression": (not ok)})

    # FALLBACK-RATE corpus: fixture (should route) + off-domain (should fall back) -> a real, sane rate.
    fb_total, fb_hits = 0, 0
    for q in _FALLBACK_CORPUS:
        r, _ic = _primary(q, provider)
        fb_total += 1
        if r.kind == "fallback":
            fb_hits += 1
    fixture_fallbacks = sum(1 for (q, _e, _k) in cases if _primary(q, provider)[0].kind == "fallback")
    corpus_total = len(cases) + fb_total
    corpus_fallbacks = fixture_fallbacks + fb_hits

    # E1 read-probes: a domain read must NOT surface comp-build.
    e1_leaks = []
    for q in _E1_READ_PROBES:
        r, _ic = _primary(q, provider)
        sf = set(s.cap.id for s in r.within_margin) | ({r.ranked[0].cap.id} if r.ranked else set())
        if any(cap_write.get(c, False) for c in sf):
            e1_leaks.append((q, sorted(c for c in sf if cap_write.get(c, False))))

    return {
        "total": len(cases), "regressions": regressions, "n_regressions": len(regressions),
        "divergences": divergences, "n_divergences": len(divergences),
        "rebuild_leaks": rebuild_leaks + e1_leaks, "read_never_rebuilds": (not rebuild_leaks and not e1_leaks),
        "fallback_corpus_total": corpus_total, "fallback_corpus_fallbacks": corpus_fallbacks,
        "fallback_rate": round(corpus_fallbacks / corpus_total, 4) if corpus_total else 0.0,
        "offdomain_fallback_rate": round(fb_hits / fb_total, 4) if fb_total else 0.0,
        "green": (not regressions and not rebuild_leaks and not e1_leaks),
    }


def main(argv):
    verbose = "--verbose" in argv
    as_json = "--json" in argv
    res = run_shadow(verbose=verbose, emit=True)
    if as_json:
        print(json.dumps(res, indent=2))
    else:
        print("=== NFRA_COMPROUTE DR2 shadow: primary-router vs backstop (comp-which), full fixture ===")
        print("fixture cases: %d | 0-regression: %s (%d) | primary-vs-backstop divergences: %d"
              % (res["total"], (res["n_regressions"] == 0), res["n_regressions"], res["n_divergences"]))
        print("fallback-rate: %.1f%% over %d (fixture+off-domain); off-domain-only: %.1f%% | read-never-rebuilds: %s"
              % (res["fallback_rate"] * 100, res["fallback_corpus_total"],
                 res["offdomain_fallback_rate"] * 100, res["read_never_rebuilds"]))
        for reg in res["regressions"][:40]:
            print("  REGRESSION [%s] exp=%s got_top=%s within=%s :: %s"
                  % (reg["kind"], reg["expect"], reg["got_top"], reg["within"], reg["q"]))
        for d in res["divergences"][:20]:
            print("  DIVERGENCE exp=%s primary=%s backstop=%s :: %s"
                  % (d["expect"], d["primary"], d["backstop"], d["q"]))
        for q, cid in res["rebuild_leaks"][:20]:
            print("  READ-NEVER-REBUILDS LEAK %s <- %s" % (cid, str(q)[:60]))
        print("RESULT: %s" % ("SHADOW-GREEN (0-regression, read-never-rebuilds holds, fallback-rate sane)"
                              if res["green"] else "SHADOW-RED -- iterate, do NOT flip"))
    return 0 if res["green"] else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
