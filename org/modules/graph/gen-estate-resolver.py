#!/usr/bin/env python3
"""Generate estate-coverage-resolver.json (the pipescript CLI read-source) by joining
CVO's AUTHORITATIVE routing (estate-coverage-manifest, owning_tool per CTO's ratified
medallion-only boundary) with the census per-thread detail (producers/served/frontend).

owning_tool/status/named_thread come from CVO (the census + tool-boundary authority) -
NOT a heuristic. An earlier heuristic over-assigned comp-pipescript (79 vs correct 13);
CVO caught it (seed-of-record 61e91d334). This regenerates the resolver from CVO's rows."""
from __future__ import annotations
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
CENSUS = os.path.join(ROOT, "org", "tier1_exec", "3.0.0_SA_CVO", "logs", "2026-06-15", "estate_census")
ROUTING = os.path.join(ROOT, ".runtmp", "manifest_rows.json")   # CVO authoritative routing rows
RESOLVER = os.path.join(ROOT, "org", "modules", "graph", "estate-coverage-resolver.json")


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
    rows = json.load(open(ROUTING, encoding="utf-8"))   # CVO authoritative
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
    CATALOG_ORDER = ["advi", "model-portfolios", "news", "market", "pm-optimizer", "partners",
                     "trade-submission", "graph-platform", "causality", "ops-internal", "mdpf",
                     "fred-macro", "security-scanner", "insurance", "portal-infra"]
    named_order = [n for n in CATALOG_ORDER if n in seen] + sorted(n for n in seen if n not in CATALOG_ORDER)
    resolver = {"schema_version": 1,
                "generated_from": "CVO census 2d9a0a2a1 + authoritative manifest 61e91d334 (owning_tool per CTO ratified medallion-only boundary)",
                "last_review": "2026-06-15", "named_threads": named_order, "threads": threads}
    json.dump(resolver, open(RESOLVER, "w", encoding="utf-8"), indent=1)

    from collections import Counter
    print(f"rows (CVO authoritative): {len(rows)} | resolver threads: {len(threads)} | named: {len(named_order)}")
    print("owning_tool:", dict(Counter(t["owning_tool"] for t in threads)))
    print("status:", dict(Counter(t["status"] for t in threads)))
    print(f"threads w/o census detail (routing-only): {len(no_detail)} {no_detail if no_detail else ''}")
    print(f"WROTE {RESOLVER}")


if __name__ == "__main__":
    main()
