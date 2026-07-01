#!/usr/bin/env python3
"""comp-which routing regression guard (LD-0208 fix (D), CTO / NFRA_COMPRAIL TO-6).

The standing "every comp-tool is reachable via the mandated router" oracle Andrew
asked for (2026-06-22, brief comp-which-routing-audit section 4.4). Two assertions:

  TEST 1 (end-to-end self-routing -- the strong oracle, adapted from MSTR's coverage
    probe 2026-06-25): feed EACH tools_index tool its OWN richest use_case sentence as
    the question and assert comp-which SURFACES that tool's name end-to-end (not merely
    that the backstop *could* surface it). This catches keyword-collision misroutes
    (comp-platinum vs the portal rule) and search-verb hijacks (comp-xref's "find every
    ..." hitting the grep primitive) that a backstop-only check passes blind. Excludes
    the RUN-primitives + the router itself ({comp-grep, comp-glob, comp-which}).

  TEST 2 (audit reproduction): the three queries the 2026-06-22 audit caught misrouting
    ("is upstream data fresh" / "artifact invariants before upload" / "component expose
    PII") route to comp-freshness / comp-validate / comp-pii -- a rich ROUTE, not a grep.

  TEST 3 (DIVERSE-PARAPHRASE -- the anti-false-green guard, CVO 2026-06-26): real-agent
    phrasings DELIBERATELY worded UNLIKE the manifest use_case sentences (the source TEST 1
    scores against). TEST 1 is near-tautological -- it feeds each tool the very text the
    backstop matches, so a green TEST 1 says nothing about how an AGENT actually phrases a
    question. This set caught a real 15/20 -> the curated rules were keyword-thin on real NL
    (leak/ssn -> pii, "hands data to <panel>" -> transform, "change to X affect" -> blast,
    "symbol across the graph" -> xref, "is X current" -> freshness all mis-grabbed to the
    backstop/grep). Applies CTO's standing lens: "a test that exercises only canonical inputs
    is a false-green." Expand this set over time; it is the routing floor, not the ceiling.

Read-only, deterministic, ASCII-only. Run from workspace root:
  python .tools/comp-which-routing-test.py [--verbose]
Exit 0 = all pass; exit 1 = a regression (a tool went unreachable or an audit case
misrouted). Wire into the comp-tool test sweep; re-run after any comp-which/manifest edit.
"""
from __future__ import annotations

import os
import subprocess
import sys

WS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COMP_WHICH = os.path.join(WS, ".tools", "comp-which")
MANIFEST = os.path.join(WS, "org", "modules", "graph", "graph-call-manifest.yaml")

# RUN-primitives (comp-which routes TO rich tools, not these) + the router itself.
EXCLUDE = {"comp-grep", "comp-glob", "comp-which"}


def _load_manifest():
    import yaml
    with open(MANIFEST, encoding="utf-8") as f:
        return yaml.safe_load(f)


def _run_comp_which(q: str) -> str:
    r = subprocess.run([sys.executable, COMP_WHICH, q],
                       cwd=WS, capture_output=True, text=True, timeout=60)
    return (r.stdout or "") + (r.stderr or "")


def test_self_routing(manifest, verbose=False):
    """Every routable tools_index tool must surface itself end-to-end when queried by its
    own richest use_case sentence (MSTR coverage-probe semantics)."""
    ti = manifest.get("tools_index", {})
    entries = manifest.get("entries", [])
    by_tool = {}
    for e in entries:
        by_tool.setdefault(str(e.get("tool", "")).split()[0], []).append(e)
    tools = [t for t in sorted(ti.keys()) if t not in EXCLUDE]
    fails = []
    for t in tools:
        ucs = by_tool.get(t, [])
        q = (ucs[0]["use_case"] if ucs else ti[t].get("does", "")).strip().rstrip("?.")
        out = _run_comp_which(q)
        routed = t in out
        if verbose:
            print("  [%s] %-22s q='%s'" % ("OK " if routed else "MISS", t, q[:58]))
        if not routed:
            fails.append("%s: comp-which did not surface it for q='%s'" % (t, q[:70]))
    return tools, fails


def test_audit_reproduction(verbose=False):
    """The three audit-caught misroutes now route to the right rich tool (not a grep)."""
    cases = [
        ("is upstream data fresh", "comp-freshness"),
        ("artifact invariants before upload", "comp-validate"),
        ("component expose PII", "comp-pii"),
    ]
    fails = []
    for q, want in cases:
        try:
            out = _run_comp_which(q)
        except Exception as exc:  # noqa: BLE001
            fails.append('"%s" -> ERROR running comp-which: %s' % (q, exc))
            continue
        ran_primitive = "running the ON-RAILS primitive" in out
        routed_right = want in out
        if verbose:
            print("  [%s] '%s' -> %s" % ("OK " if (routed_right and not ran_primitive) else "MISS", q, want))
        if ran_primitive or not routed_right:
            how = "ran grep primitive" if ran_primitive else "did not name %s" % want
            fails.append('"%s" -> expected route to %s, but %s' % (q, want, how))
    return cases, fails


# TEST 3 corpus: real-agent paraphrases worded UNLIKE the manifest use_case text.
# (paraphrase, expected rich-tool substring). A correct case ROUTES to the tool and does
# NOT fall through to the grep primitive. This is the diverse-input floor -- ADD to it.
_PARAPHRASES = [
    ("can I change the column output of D_04 without breaking the dashboard?", "comp-pipescript io"),
    ("if I rename build_dashboard what else falls over?", "comp-blast"),
    ("does the etl-runner have the newest code or is it behind?", "comp-pipescript deployed"),
    ("is the bd silver data recent enough for me to kick off the gold chain?", "comp-freshness"),
    ("will this artifact pass its checks before I push it to s3?", "comp-validate"),
    ("could the AdvisorsTab leak a client SSN to the browser?", "comp-pii"),
    ("what hands data to the AdvisorScorecard panel?", "comp-transform"),
    ("which lambda is behind /api/scoped/advisor-intelligence?", "comp-routes"),
    ("my endpoint returns html instead of json, why?", "comp-routes"),
    ("does the scraper role actually have ec2 stop permission?", "comp-iam"),
    ("show me everything in the news pipeline", "pipescript"),
    ("are two react-query hooks fighting over the same key?", "comp-cache"),
    ("what writes canonical_prices.parquet?", "comp-pipescript io"),
    ("which directories are dead and safe to delete?", "comp-heat"),
    ("have I got uncommitted work lying around?", "comp-heat"),
    ("trace the full path from the Holdings component back to its gold script", "comp-platinum"),
    ("where does the symbol compute_nav show up across the graph?", "comp-xref"),
    ("who calls the function load_positions?", "comp-blast"),
    ("what would a change to lambda inf-incremental-updater affect?", "comp-blast"),
    ("is the served cot artifact actually current?", "comp-freshness"),
]


def test_diverse_paraphrase(verbose=False):
    """Real-agent paraphrases (worded unlike the use_case text) must ROUTE to the right rich
    tool, not fall through to the grep primitive. The anti-false-green guard."""
    fails = []
    for q, want in _PARAPHRASES:
        try:
            out = _run_comp_which(q)
        except Exception as exc:  # noqa: BLE001
            fails.append('"%s" -> ERROR: %s' % (q[:50], exc))
            continue
        ran_primitive = "running the ON-RAILS primitive" in out
        routed_right = (want in out) and not ran_primitive
        if verbose:
            print("  [%s] '%s' -> %s" % ("OK " if routed_right else "MISS", q[:52], want))
        if not routed_right:
            how = "fell through to grep" if ran_primitive else "did not name %s" % want
            fails.append('"%s" -> expected %s, but %s' % (q[:50], want, how))
    return _PARAPHRASES, fails


def test_comproute_posterior_live(verbose=False):
    """NFRA_COMPROUTE L4 -- the surface-aware posterior resolves the grounded failure modes LIVE against
    the REAL 49-cap COMPUNIFY provider (not a fixture). Asserts (A) never-silent-argmax -- a genuine
    near-tie surfaces BOTH candidates each carrying a concern; and PRIOR-not-FILTER -- a strong
    query_match is NEVER excluded by surface; and graceful cold-start (empty role still routes)."""
    checks, fails = [], []
    try:
        _gm = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                           "org", "modules", "graph")
        if _gm not in sys.path:
            sys.path.insert(0, _gm)
        import comp_route
        import comp_capability_provider as _capmap
        prov = _capmap.get_provider()
    except Exception as e:  # a broken engine/provider IS a real L4 regression
        return checks, ["COMPROUTE engine/provider unavailable: %s" % e]

    # (A) within-margin cross-tool on the LIVE map -> disambiguation, BOTH surfaced, each with a concern
    checks.append("A.disambiguation-live")
    rA = comp_route.route("audit portal component fields for schema issues",
                          {"role": "DE", "working_set": [], "trajectory": []}, prov)
    idsA = [s.cap.id for s in rA.within_margin]
    if rA.kind != "disambiguation" or len(idsA) < 2:
        fails.append('A: expected a near-tie disambiguation, got %s %s' % (rA.kind, idsA))
    elif not {"comp-transform", "comp-adapter-audit"} & set(idsA):
        fails.append('A: expected the portal-component near-tie, got %s' % idsA)
    elif any(not getattr(s.cap, "concern", "") for s in rA.within_margin):
        fails.append('A: a within-margin candidate lacks a concern (cannot disambiguate)')

    # (PRIOR-not-FILTER) a strong query_match on a NON-ctx surface still ranks (prior is additive, not a filter)
    checks.append("PRIOR-not-FILTER-live")
    rP = comp_route.route("iam permission grant gaps before deploy",
                          {"role": "DE", "working_set": [], "trajectory": []}, prov)  # DE ctx, AWS/iam query
    if "comp-iam" not in [s.cap.id for s in rP.ranked[:3]]:
        fails.append('PRIOR-not-FILTER: comp-iam must still rank for an iam query under a DE ctx, got %s'
                     % [s.cap.id for s in rP.ranked[:3]])

    # (cold-start) empty role still routes (degrades to query+prior+margin -- the PRD promise)
    checks.append("cold-start-live")
    rC = comp_route.route("iam permission grant gaps before deploy",
                          {"role": "", "working_set": [], "trajectory": []}, prov)
    if not rC.ranked:
        fails.append('cold-start: empty-role query returned no ranking')
    return checks, fails


def main() -> int:
    verbose = "--verbose" in sys.argv
    manifest = _load_manifest()

    tools, f1 = test_self_routing(manifest, verbose)
    cases, f2 = test_audit_reproduction(verbose)
    paras, f3 = test_diverse_paraphrase(verbose)
    pchecks, f4 = test_comproute_posterior_live(verbose)

    print("\ncomp-which routing regression guard (LD-0208)")
    print("  TEST 1 end-to-end self-routing: %d/%d routable tools surface themselves"
          % (len(tools) - len(f1), len(tools)))
    for line in f1:
        print("    FAIL: %s" % line)
    print("  TEST 2 audit reproduction:      %d/%d audit cases route correctly"
          % (len(cases) - len(f2), len(cases)))
    for line in f2:
        print("    FAIL: %s" % line)
    print("  TEST 3 diverse-paraphrase:      %d/%d real-NL paraphrases route to the right tool"
          % (len(paras) - len(f3), len(paras)))
    for line in f3:
        print("    FAIL: %s" % line)
    print("  TEST 4 COMPROUTE posterior LIVE: %d/%d grounded cases resolve (never-silent-argmax + PRIOR-not-FILTER + cold-start)"
          % (len(pchecks) - len(f4), len(pchecks)))
    for line in f4:
        print("    FAIL: %s" % line)

    if f1 or f2 or f3 or f4:
        print("\nRESULT: FAIL (%d unreachable + %d audit regressions + %d paraphrase misroutes + %d posterior)"
              % (len(f1), len(f2), len(f3), len(f4)))
        return 1
    print("\nRESULT: PASS -- %d tools self-route; %d audit + %d paraphrases route; %d COMPROUTE-posterior grounded cases resolve live"
          % (len(tools), len(cases), len(paras), len(pchecks)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
