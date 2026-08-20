#!/usr/bin/env python3
"""Generate estate-coverage-resolver.json (the pipescript CLI read-source) by joining
CVO's AUTHORITATIVE routing (estate-coverage-manifest, owning_tool per CTO's ratified
medallion-only boundary) with the census per-thread detail (producers/served/frontend).

owning_tool/status/named_thread come from CVO (the census + tool-boundary authority) -
NOT a heuristic. An earlier heuristic over-assigned comp-pipescript (79 vs correct 13);
CVO caught it (seed-of-record 61e91d334). This regenerates the resolver from CVO's rows."""
from __future__ import annotations

import datetime
import json
import os

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
CENSUS = os.path.join(ROOT, "org", "modules", "graph", "estate_census")  # RE-POINTED 2026-08-20: the census-regen landing (CVO-named successor home, adjudication @d7a660b69c);
# the 06-15 originals remain at org/tier1_exec/3.0.0_SA_CVO/logs/2026-06-15/estate_census/ as the dated record -- nothing reads them.
# Routing source = the COMMITTED canonical manifest (CVO-authoritative, reproducible from a
# fresh checkout). Each manifest entry: {family(=thread_id), named_thread, owning_tool, status,
# tool_pointer, reason?, last_reviewed, debtscan_flags}.
MANIFEST = os.path.join(ROOT, "org", "modules", "graph", "estate-coverage-manifest.yaml")
# OPAL_RESOLVER_OUT lets the last_review-preservation behaviour be EXERCISED without
# regenerating the live substrate -- that regen is deliberately parked (CTO 2026-08-14),
# and a fix whose only test is "run it in production" is not tested, it is deployed.
RESOLVER = os.environ.get("OPAL_RESOLVER_OUT") or os.path.join(
    ROOT, "org", "modules", "graph", "estate-coverage-resolver.json")


def load_routing():
    m = yaml.safe_load(open(MANIFEST, encoding="utf-8"))
    out = []
    for e in m.get("threads", []):
        out.append({"family": e.get("family"), "named_thread": e.get("named_thread"),
                    "owning_tool": e.get("owning_tool"), "status": e.get("status"),
                    "reachability_status": e.get("reachability_status"),  # P3.2 CVO ground-truth
                    "reason": e.get("reason"),
                    # Optional self-contained detail for estate threads NOT in the lambda census
                    # (e.g. an EC2/ALB service like m365-mcp-gateway). Falls back to census when absent.
                    "description": e.get("description"), "producers": e.get("producers"),
                    "served_artifacts": e.get("served_artifacts"),
                    "frontend_resolution": e.get("frontend_resolution"),
                    # PROSE_FIELD homes (OPAL_KIMIPIPELINE.FIELDHOME F1, CTO 63386): an ADJUDICATED
                    # classification/classification_reason/enrichment placed on the manifest row
                    # WINS over the frozen 2026-06-15 census, exactly as `description` already does
                    # (main():81). The manifest is committed + reproducible; the census is a dated
                    # bootstrap default no adjudication may edit. This makes an adjudicated text
                    # survive regen BY CONSTRUCTION rather than by re-landing discipline.
                    "classification": e.get("classification"),
                    "classification_reason": e.get("classification_reason"),
                    "enrichment": e.get("enrichment")})
    return out


def load_census_detail():
    detail = {}
    p1 = json.load(open(os.path.join(CENSUS, "pass1_inventory.json"), encoding="utf-8"))
    for t in p1["allThreads"]:
        detail[t["thread_id"]] = t
    for fam in json.load(open(os.path.join(CENSUS, "pass2_gapfamilies.json"), encoding="utf-8")):
        for t in fam.get("threads", []):
            t = dict(t)
            t.setdefault("family", fam.get("family"))
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
        # PROSE_FIELD homes (FIELDHOME F1): resolve each with manifest-wins-over-census, the :81
        # `description` pattern applied to all four prose fields. An adjudicated manifest value
        # wins; else the frozen census bootstrap. The orphan-candidate flag reads the RESOLVED
        # classification_reason (not the raw census one) so an adjudicated reason correctly
        # governs the flag -- the sovereign-plane value is authoritative for the derived signal too.
        classification = r.get("classification") or d.get("classification", "")
        classification_reason = r.get("classification_reason") or d.get("classification_reason", "")
        enrichment = r.get("enrichment") or d.get("enrichment", "")
        rsn = (classification_reason or "").lower()
        if "orphan" in rsn or "superseded" in rsn or "not invoked" in rsn or "no event source" in rsn:
            flags.append("orphan-candidate")
        seen.add(r["named_thread"])
        threads.append({
            "thread_id": tid, "named_thread": r["named_thread"],
            "family": d.get("family"), "owning_tool": r["owning_tool"], "status": r["status"],
            "reachability_status": r.get("reachability_status"),  # P3.2 CVO ground-truth FE-reachability
            "reason": r.get("reason"), "debtscan_flags": flags,
            # manifest-provided detail wins (self-contained non-census threads); else census.
            "description": r.get("description") or d.get("description", ""),
            "producers": r.get("producers") or d.get("producers", []),
            "served_artifacts": r.get("served_artifacts") or d.get("served_artifacts", []),
            "frontend_resolution": r.get("frontend_resolution") or d.get("frontend_resolution", ""),
            # FIELDHOME F1: the three prose fields now carried in the resolver output with
            # manifest-wins precedence, so an adjudicated text is served AND survives regen.
            "classification": classification,
            "classification_reason": classification_reason,
            "enrichment": enrichment,
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
    # `attribution` REMOVED 2026-08-20 (W-15 grain-3 landing, CRO word (c)): registry-retired at v1.4
    # (content lives under positioning); a retired name in an ordering roster is inert-but-misleading
    # drift. Rendering-safe by the construction below (absent from all_names renders nothing).
    # `canonical-schwab` + `observability` ADDED same landing (the TO's optional act, taken): both are
    # populated verticals post-landing; a populated vertical absent from the deliberate order falls to
    # the sorted tail, which reads as an afterthought rather than a placement.
    CATALOG_ORDER = ["advi-bd", "advi-inf", "advi-cot", "model-portfolios", "news", "market-overview",
                     "macroeconomics", "factor-tilts", "valuation", "correlation", "positioning", "cma",
                     "portfolio-management", "trade-submission", "causality",
                     "security-scanner", "smartx", "canonical-schwab", "mdpf", "partners",
                     "graph-platform", "insurance", "portal-infra", "observability", "ops-internal",
                     "data-refresh"]
    named_order = [n for n in CATALOG_ORDER if n in all_names] + sorted(n for n in all_names if n not in CATALOG_ORDER)
    # A REGEN IS NOT A REVIEW. `last_review` answers "when did a human/CVO last REVIEW this
    # substrate", and it drives the staleness age in comp-estate's provenance header
    # (opal_estate_infrastructure.py:138-144). It was a FROZEN LITERAL here, so every regen
    # OVERWROTE the real review date with a hardcoded one -- and by 2026-08-20 the literal had
    # fallen BEHIND the live artifact, so a refresh would have moved the review vintage BACKWARDS
    # six weeks (live 2026-07-30 -> written 2026-06-15) and asserted a review nobody performed.
    # That is why CTO's 2026-08-14 substrate-fuse decision PARKED the regen: honest staleness beats
    # a false freshness stamp. Preserving the prior value fixes the direction AND the lie -- a
    # regen now leaves the review clock exactly where the last real review left it.
    # `generated_at` carries the fact the literal was pretending to carry, separately, so the two
    # questions ("when reviewed" / "when regenerated") stop sharing one field.
    _prior_review = "2026-06-15"          # floor: only used when no prior artifact exists
    try:
        with open(RESOLVER, encoding="utf-8") as _f:
            _prior_review = json.load(_f).get("last_review") or _prior_review
    except (OSError, ValueError):
        pass                              # first mint: the floor stands, and it is honest

    resolver = {"schema_version": 1,
                "generated_from": "CVO census 2d9a0a2a1 + manifest (named_thread) + AUTHORITATIVE_lambda_taxonomy 26b32687a (resource-level, single source w/ fixtures)",
                "last_review": _prior_review,
                "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                "named_threads": named_order,
                "resources_by_named_thread": dict(resources_by_named_thread), "threads": threads}
    json.dump(resolver, open(RESOLVER, "w", encoding="utf-8"), indent=1)
    print("resource-level named threads:", len(resources_by_named_thread), "| total lambdas mapped:", len(l2nt))

    print(f"rows (CVO authoritative): {len(rows)} | resolver threads: {len(threads)} | named: {len(named_order)}")
    print("owning_tool:", dict(Counter(t["owning_tool"] for t in threads)))
    print("status:", dict(Counter(t["status"] for t in threads)))
    print(f"threads w/o census detail (routing-only): {len(no_detail)} {no_detail if no_detail else ''}")
    print(f"WROTE {RESOLVER}")


if __name__ == "__main__":
    main()
