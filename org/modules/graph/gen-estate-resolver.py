#!/usr/bin/env python3
"""Generate estate-coverage-resolver.json (the pipescript CLI read-source) by joining
CVO's AUTHORITATIVE routing (estate-coverage-manifest, owning_tool per CTO's ratified
medallion-only boundary) with the census per-thread detail (producers/served/frontend).

owning_tool/status/named_thread come from CVO (the census + tool-boundary authority) -
NOT a heuristic. An earlier heuristic over-assigned comp-pipescript (79 vs correct 13);
CVO caught it (seed-of-record 61e91d334). This regenerates the resolver from CVO's rows."""
from __future__ import annotations
import json, os, yaml

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
CENSUS = os.path.join(ROOT, "org", "tier1_exec", "3.0.0_SA_CVO", "logs", "2026-06-15", "estate_census")
# Routing source = the COMMITTED canonical manifest (CVO-authoritative, reproducible from a
# fresh checkout). Each manifest entry: {family(=thread_id), named_thread, owning_tool, status,
# tool_pointer, reason?, last_reviewed, debtscan_flags}.
MANIFEST = os.path.join(ROOT, "org", "modules", "graph", "estate-coverage-manifest.yaml")
RESOLVER = os.path.join(ROOT, "org", "modules", "graph", "estate-coverage-resolver.json")


def load_routing():
    m = yaml.safe_load(open(MANIFEST, encoding="utf-8"))
    out = []
    for e in m.get("threads", []):
        out.append({"family": e.get("family"), "named_thread": e.get("named_thread"),
                    "owning_tool": e.get("owning_tool"), "status": e.get("status"),
                    "reason": e.get("reason")})
    return out


def load_census_detail():
    detail = {}
    p1 = json.load(open(os.path.join(CENSUS, "pass1_inventory.json"), encoding="utf-8"))
    for t in p1["allThreads"]:
        detail[t["thread_id"]] = t
    for fam in json.load(open(os.path.join(CENSUS, "pass2_gapfamilies.json"), encoding="utf-8")):
        for t in fam.get("threads", []):
            t = dict(t); t.setdefault("family", fam.get("family"))
            detail[t["thread_id"]] = t
    return detail


def main():
    rows = load_routing()   # CVO authoritative, from the committed manifest
    detail = load_census_detail()
    seen, threads, no_detail = set(), [], []
    for r in rows:
        tid = r["family"]            # CVO's 'family' key == thread_id
        d = detail.get(tid, {})
        if not d:
            no_detail.append(tid)
        flags = []
        if r["status"] == "unreviewed":
            flags.append("needs-consumer-trace")
        rsn = (d.get("classification_reason") or "").lower()
        if "orphan" in rsn or "superseded" in rsn or "not invoked" in rsn or "no event source" in rsn:
            flags.append("orphan-candidate")
        seen.add(r["named_thread"])
        threads.append({
            "thread_id": tid, "named_thread": r["named_thread"],
            "family": d.get("family"), "owning_tool": r["owning_tool"], "status": r["status"],
            "reason": r.get("reason"), "debtscan_flags": flags,
            "description": d.get("description", ""),
            "producers": d.get("producers", []),
            "served_artifacts": d.get("served_artifacts", []),
            "frontend_resolution": d.get("frontend_resolution", ""),
        })
    # AUTHORITATIVE resource-level taxonomy (CVO 26b32687a): lambda -> named_thread, single source
    # the fixtures are also derived from. This is the resource enumeration `pipescript <name>` surfaces
    # (Andrew's "every resource in that thread") + what gate-b reproduces resource-exact.
    from collections import Counter, defaultdict
    taxo = json.load(open(os.path.join(CENSUS, "AUTHORITATIVE_lambda_taxonomy.json"), encoding="utf-8"))
    l2nt = taxo["lambda_to_named_thread"]
    resources_by_named_thread = defaultdict(list)
    for lam, nt in l2nt.items():
        resources_by_named_thread[nt].append(lam)
    for nt in resources_by_named_thread:
        resources_by_named_thread[nt] = sorted(resources_by_named_thread[nt])

    all_names = set(seen) | set(resources_by_named_thread)
    CATALOG_ORDER = ["advi-bd", "advi-inf", "advi-cot", "model-portfolios", "news", "market-overview",
                     "macroeconomics", "factor-tilts", "valuation", "correlation", "positioning", "cma",
                     "attribution", "portfolio-management", "trade-submission", "causality",
                     "security-scanner", "smartx", "mdpf", "partners", "graph-platform", "insurance",
                     "portal-infra", "ops-internal", "data-refresh"]
    named_order = [n for n in CATALOG_ORDER if n in all_names] + sorted(n for n in all_names if n not in CATALOG_ORDER)
    resolver = {"schema_version": 1,
                "generated_from": "CVO census 2d9a0a2a1 + manifest (named_thread) + AUTHORITATIVE_lambda_taxonomy 26b32687a (resource-level, single source w/ fixtures)",
                "last_review": "2026-06-15", "named_threads": named_order,
                "resources_by_named_thread": dict(resources_by_named_thread), "threads": threads}
    json.dump(resolver, open(RESOLVER, "w", encoding="utf-8"), indent=1)
    print("resource-level named threads:", len(resources_by_named_thread), "| total lambdas mapped:", len(l2nt))

    from collections import Counter
    print(f"rows (CVO authoritative): {len(rows)} | resolver threads: {len(threads)} | named: {len(named_order)}")
    print("owning_tool:", dict(Counter(t["owning_tool"] for t in threads)))
    print("status:", dict(Counter(t["status"] for t in threads)))
    print(f"threads w/o census detail (routing-only): {len(no_detail)} {no_detail if no_detail else ''}")
    print(f"WROTE {RESOLVER}")


if __name__ == "__main__":
    main()
