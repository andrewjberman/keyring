#!/usr/bin/env python3
"""Generate the complete estate-coverage-manifest from the CVO census + named-thread catalog.
COO-driven (Andrew /goal NFRA_PIPESCRIPT). CVO verifies the determinations."""
from __future__ import annotations
import json, re, sys

BASE = "org/tier1_exec/3.0.0_SA_CVO/logs/2026-06-15/estate_census"
CATALOG = f"{BASE}/NAMED_THREAD_CATALOG.md"
PASS1 = f"{BASE}/pass1_inventory.json"
PASS2 = f"{BASE}/pass2_gapfamilies.json"

# --- 1. parse the catalog for named_thread -> [thread_id] + per-thread status ---
named_of = {}        # thread_id -> named_thread
status_of_cat = {}   # thread_id -> STATUS (from catalog bullet)
named_order = []     # ordered list of named threads
cur = None
for line in open(CATALOG, encoding="utf-8"):
    m = re.match(r"^## pipescript\s+(\S+)", line)
    if m:
        cur = m.group(1)
        if cur not in named_order:
            named_order.append(cur)
        continue
    b = re.match(r"^-\s+\*\*([^*]+)\*\*\s+\[([A-Z_]+)\]", line)
    if b and cur:
        tid = b.group(1).strip()
        named_of[tid] = cur
        status_of_cat[tid] = b.group(2)

# --- 2. load census detail (pass1 allThreads + pass2 gapfamilies) ---
p1 = json.load(open(PASS1, encoding="utf-8"))
detail = {}
for t in p1["allThreads"]:
    detail[t["thread_id"]] = t
p2 = json.load(open(PASS2, encoding="utf-8"))
for fam in p2:
    famname = fam.get("family")
    for t in fam.get("threads", []):
        t = dict(t)
        t.setdefault("family", famname)
        detail[t["thread_id"]] = t

# --- 3. owning_tool heuristic from current_coverage + classification ---
def owning_tool(t):
    cov = (t.get("current_coverage") or "").lower()
    cls = (t.get("classification") or "").upper()
    desc = (t.get("description") or "").lower()
    fe = (t.get("frontend_resolution") or "").lower()
    blob = cov + " " + desc
    if "comp-pipescript" in cov or "medallion" in cov:
        return "comp-pipescript"
    if "stitch" in cov or "cross-layer" in cov:
        return "stitch"
    if ("portal" in cov or "frontend" in cov or "consumer" in cov) and "none" not in fe[:6]:
        return "portal-consumer-tools"
    if "globgrph" in cov or "comp-kuzu" in cov or "aws-resource" in blob or "lambda" in blob or "ec2" in blob or "stepfn" in blob or "step function" in blob:
        return "globgrph"
    if cls == "EXPLICITLY_OUT":
        return "none"
    return "globgrph"  # default: it's deployed AWS infra

STATUS_MAP = {"IN_SCOPE": "in-scope", "EXPLICITLY_OUT": "explicit-out", "UNREVIEWED": "unreviewed"}

# CTO's hand-authored special notes (carry into the matching generated entry)
SPECIAL = {
    "find-dualbiz": {"owning_tool": "none", "reason": "local-runnable medallion (.runtmp), analyst CSV to Andrew, no S3/Lambda gold-deploy, no portal/pipeline consumer. The gold/ path is the LOCAL medallion convention, not an S3 served-gold deploy."},
}

threads_out = []
seen = set()
for tid, named in named_of.items():
    t = detail.get(tid)
    if not t:
        # in catalog but not census detail -> minimal entry, flag for trace
        threads_out.append({"thread_id": tid, "named_thread": named, "family": None,
                            "owning_tool": "globgrph", "status": STATUS_MAP.get(status_of_cat.get(tid, ""), "unreviewed"),
                            "debtscan_flags": ["needs-detail-trace"]})
        seen.add(tid); continue
    cls = t.get("classification", "")
    ot = owning_tool(t)
    entry = {
        "thread_id": tid,
        "named_thread": named,
        "family": t.get("family"),
        "owning_tool": ot,
        "status": STATUS_MAP.get(cls, "unreviewed"),
        "debtscan_flags": [],
    }
    # debt flags from classification_reason / coverage
    reason = (t.get("classification_reason") or "").lower()
    if "orphan" in reason or "superseded" in reason or "not invoked" in reason or "no event source" in reason:
        entry["debtscan_flags"].append("orphan-candidate")
    if entry["status"] == "unreviewed":
        entry["debtscan_flags"].append("needs-consumer-trace")
    sp = SPECIAL.get(tid)
    if sp:
        entry.update({k: v for k, v in sp.items()})
    threads_out.append(entry)
    seen.add(tid)

# census threads not in any named thread (catalog gap) -> flag
orphan_from_catalog = [tid for tid in detail if tid not in seen]

# --- 4. reconciliation report ---
print(f"named threads ({len(named_order)}): {named_order}")
print(f"manifest entries: {len(threads_out)}")
print(f"census detail threads: {len(detail)} | catalog-mapped: {len(named_of)}")
print(f"census threads NOT in catalog (would be silently-missing): {len(orphan_from_catalog)}")
if orphan_from_catalog:
    print("  ->", orphan_from_catalog[:40])
from collections import Counter
print("by named_thread:", dict(Counter(e["named_thread"] for e in threads_out)))
print("by owning_tool:", dict(Counter(e["owning_tool"] for e in threads_out)))
print("by status:", dict(Counter(e["status"] for e in threads_out)))

# --- 5. emit YAML (preserve CTO header) ---
import io
HEADER = open("org/modules/graph/estate-coverage-manifest.yaml", encoding="utf-8").read().split("\nthreads:")[0]
out = io.StringIO()
out.write(HEADER)
out.write("\n\n# ---- FULL POPULATION (COO-generated from CVO census 2d9a0a2a1 + NAMED_THREAD_CATALOG d33fe4aab; CVO verifies determinations) ----\n")
out.write("threads:\n")
for e in sorted(threads_out, key=lambda x: (x["named_thread"], x["thread_id"])):
    out.write(f"  - thread_id: {e['thread_id']}\n")
    out.write(f"    named_thread: {e['named_thread']}\n")
    out.write(f"    family: {e['family']!r}\n" if e['family'] else "    family: null\n")
    out.write(f"    owning_tool: {e['owning_tool']}\n")
    out.write(f"    status: {e['status']}\n")
    if e.get("reason"):
        out.write(f"    reason: {json.dumps(e['reason'])}\n")
    out.write(f"    debtscan_flags: [{', '.join(e['debtscan_flags'])}]\n")
open("org/modules/graph/estate-coverage-manifest.yaml", "w", encoding="utf-8").write(out.getvalue())
print("\nWROTE org/modules/graph/estate-coverage-manifest.yaml")

# --- 6. emit the machine-read resolver JSON (full detail merged; the pipescript CLI reads THIS) ---
resolver = {"schema_version": 1, "generated_from": "CVO census 2d9a0a2a1 + NAMED_THREAD_CATALOG d33fe4aab",
            "last_review": "2026-06-15", "named_threads": named_order, "threads": []}
for e in sorted(threads_out, key=lambda x: (x["named_thread"], x["thread_id"])):
    t = detail.get(e["thread_id"], {})
    resolver["threads"].append({
        "thread_id": e["thread_id"], "named_thread": e["named_thread"], "family": e["family"],
        "owning_tool": e["owning_tool"], "status": e["status"], "debtscan_flags": e["debtscan_flags"],
        "description": t.get("description", ""),
        "producers": t.get("producers", []),
        "served_artifacts": t.get("served_artifacts", []),
        "frontend_resolution": t.get("frontend_resolution", ""),
    })
json.dump(resolver, open("org/modules/graph/estate-coverage-resolver.json", "w", encoding="utf-8"), indent=1)
print("WROTE org/modules/graph/estate-coverage-resolver.json (CLI read-source)")
