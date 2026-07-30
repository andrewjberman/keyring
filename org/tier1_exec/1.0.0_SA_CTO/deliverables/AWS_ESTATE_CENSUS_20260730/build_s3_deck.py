"""Assemble the S3 bucket review deck: one card per bucket, instrument verdicts
pre-computed, RULING line blank for Andrew's keep/kill session.

Inputs (this dir): s3_buckets_dated.json, bucket_metrics.tsv, s3_configs_from_dr.json,
kuzu_bucket_edges_raw.txt, kuzu_bucket_drift_raw.txt. Output: S3_BUCKET_DECK.md.
"""
from __future__ import annotations

import json
import re
from collections import defaultdict

buckets = json.load(open("s3_buckets_dated.json"))
metrics = {}
for line in open("bucket_metrics.tsv"):
    parts = line.rstrip("\n").split("\t")
    if len(parts) == 3:
        n, sz, no = parts
        bad = ("None", "null", "")
        metrics[n] = (
            float(sz) if sz not in bad else None,
            float(no) if no not in bad else None,
        )
dr = {b["name"]: b for b in json.load(open("s3_configs_from_dr.json"))["buckets"]}

drift = {}
for line in open("kuzu_bucket_drift_raw.txt", encoding="utf-8", errors="replace"):
    m = re.match(r"^(\S+)\s{2,}(\S+)\s{2,}(\S+)\s*$", line)
    if m and m.group(1) != "n.name" and not m.group(1).startswith("-"):
        drift[m.group(1)] = m.group(2)

edges = defaultdict(lambda: defaultdict(list))   # bucket -> edge_type -> [other]
started = False
for line in open("kuzu_bucket_edges_raw.txt", encoding="utf-8", errors="replace"):
    if line.startswith("----"):
        started = True
        continue
    if not started or line.startswith("("):
        continue
    parts = re.split(r"\s{2,}", line.rstrip())
    if len(parts) >= 4:
        b, etype, otype, oname = parts[0], parts[1], parts[2], parts[3]
        edges[b][etype].append(f"{oname} ({otype})")

GROUPS = [
    ("A. PIPELINE DATA (bronze/silver/gold estates)", lambda n: n.startswith("opal-data-")),
    ("B. PLATFORM / DEPLOY INFRA", lambda n: n in (
        "opal-313476888478-lambda-artifacts", "opal-313476888478-lambda-layers",
        "opal-313476888478-terraform-state", "opal-313476888478-globgrph",
        "opal-runner-shared", "opal-ci-staging", "opal-infrastructure-snapshots")),
    ("C. LOGS / AUDIT / BILLING", lambda n: n in (
        "opal-cloudtrail-logs-313476888478", "opal-cloudfront-logs-313476888478",
        "opal-schwab-d4-access-logs-313476888478", "opal-served-key-write-trail-logs",
        "opal-mcp-audit", "opal-cur-313476888478", "opal-mcp-athena-results")),
    ("D. PORTAL / WEBSITE / SERVING", lambda n: n in (
        "opalinvest-portal", "opal-website-backups", "opal-analytics-dashboard",
        "opal-market-data-v2", "opal-market-update")),
    ("E. RESEARCH / OTHER", lambda n: True),
]

def fmt_size(sz):
    if sz is None:
        return "no CW datapoint (empty or brand-new)"
    if sz > 1 << 30:
        return f"{sz / (1 << 30):.1f} GB"
    if sz > 1 << 20:
        return f"{sz / (1 << 20):.1f} MB"
    return f"{sz / 1024:.0f} KB"

out = ["# S3 Bucket Review Deck -- 39 cards (2026-07-30)", ""]
out.append("Per-card instrument verdicts pre-computed: size/objects = CloudWatch "
           "(1-2d lag); versioning/encryption = the estate's own DR snapshot "
           "(2026-07-30); TF = graph drift_class (DECLARED = in Terraform, "
           "LIVE-no-DECLARED = NOT in Terraform); edges = kuzu (non-S3Key). "
           "RULING left blank for the session.")
out.append("")

placed = set()
for gtitle, pred in GROUPS:
    grp = [b for b in buckets if b["name"] not in placed and pred(b["name"])]
    for b in grp:
        placed.add(b["name"])
    grp.sort(key=lambda b: -(metrics.get(b["name"], (0, 0))[0] or 0))
    out.append(f"\n## {gtitle}  ({len(grp)} buckets)\n")
    for b in grp:
        n = b["name"]
        sz, no = metrics.get(n, (None, None))
        cfg = dr.get(n, {})
        e = edges.get(n, {})
        out.append(f"### {n}")
        out.append(f"- created {b['created'][:10]} | {fmt_size(sz)} | "
                   f"{int(no) if no else 0:,} objects | "
                   f"versioning={cfg.get('versioning', '?')} | "
                   f"encrypted={cfg.get('encryption', '?')} | "
                   f"TF={drift.get(n, '?')}")
        if e:
            for etype in sorted(e, key=lambda t: -len(e[t])):
                peers = e[etype]
                shown = ", ".join(peers[:6]) + (f" +{len(peers) - 6} more" if len(peers) > 6 else "")
                out.append(f"- {etype} ({len(peers)}): {shown}")
        else:
            out.append("- NO GRAPH EDGES (no modeled producer/consumer/policy -- "
                       "either inert or invisible to the derive)")
        out.append("- **RULING:** ____________  **business_function:** ____________")
        out.append("")

open("S3_BUCKET_DECK.md", "w", encoding="utf-8").write("\n".join(out))
print(f"deck written: {len(placed)} cards")
no_edge = [n for n in placed if not edges.get(n)]
print(f"buckets with ZERO graph edges: {len(no_edge)}: {sorted(no_edge)}")
untf = [n for n, d in drift.items() if d == "LIVE-no-DECLARED"]
print(f"NOT in Terraform: {len(untf)}: {sorted(untf)}")
