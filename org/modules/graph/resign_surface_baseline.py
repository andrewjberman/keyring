#!/usr/bin/env python3
"""DEPRECATED -- DO NOT USE for the surface-scan baseline (NFRA_GRAPHS.D8-FP, CTO 204916Z).

This DEV-BOX signer reads a comp-kuzu/snapshot INDIRECTION whose keys can DIVERGE from the live
derive's scan cn -- the dump-vs-derive divergence behind the 3 D8 key-space mismatches. The baseline
is now signed BY CONSTRUCTION by `derive_runner.py --sign-baseline` (same _graph_to_scan_nodes on the
same in-VPC graph the scan diffs) -> baseline-keys == scan-cn-keys is the same code on the same data,
impossible to diverge. Re-running THIS tool re-opens that divergence class = a footgun. Kept as the
historical record + membership-parse reference only; never (re)sign the critical-surface baseline with
it. (Hard-gated below: needs ALLOW_DEPRECATED_RESIGN=1 to run at all.)

--- original (superseded) ---
Re-sign the critical-surface scan baseline as PER-SURFACE AWS-BACKEND MEMBERSHIP
(NFRA_GRAPHS.D8-FP, Option A).

The in-derive surface scan (derive_runner.run_critical_surface_scan) diffs the AWS-only
derive graph against this baseline. The OLD baseline was a portal-inclusive comp-graph node
set -> domain mismatch -> the 06-17 SEV1/SEV2 false-positive. This tool builds the baseline
from each surface's aws_backend block (critical-surfaces.yaml): producers / serving-Lambdas /
served-buckets, by NAME, resolved to node_id + drift_class against the LIVE canonical graph
(comp-kuzu, ARN-keyed -- the same derive output the scan diffs). A removed/changed member then
fires that surface x firm. Producer-identity anchored (NOT bucket-writers).

Baseline schema written:
  { "schema": "d8fp-aws-backend-membership-v1", "built_at": <ts>, "f6_marker": {...},
    "surfaces": { "<surface_id>__<firm>": { "severity": "SEV1|SEV2",
                  "members": { "<node_id>": {"node_type":..,"name":..,"source_sha":<drift_class>} } } },
    "unresolved": { "<surface_id>__<firm>": [<name>, ...] } }   # recorded coverage caveats

Usage (run from the workspace root):
  python org/modules/graph/resign_surface_baseline.py --dry-run   # build + print, NO upload
  python org/modules/graph/resign_surface_baseline.py             # build + upload to S3 (backs up old)

NB: cot ADVI is a DOCUMENTED no-op (aws_backend.per_firm.cot.status == 'no-op', CTO C3) -- skipped,
not armed. getAUMMetrics is a PORTAL endpoint (CTO C2) -- a dev-box B5 concern, not an AWS-scan node.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time

import boto3
import yaml

SURFACES_YAML = "org/modules/graph/critical-surfaces.yaml"
SNAPSHOT_BUCKET = "opal-313476888478-globgrph"
BASELINE_KEY = "critical-surface-baseline.json"
F6_MARKER_KEY = "warehouse/_branch_head.main.json"
REGION = "us-east-1"


def _load_node_map(nodes_json: str) -> dict:
    """Read a comp-kuzu --json dump of CloudNodes -> {name: {node_id, node_type, source_sha}}.
    Produce that dump (run from the workspace root, where comp-kuzu is on PATH) with:
      comp-kuzu --json "MATCH (n:CloudNode) RETURN n.name AS name, n.node_id AS node_id,
                        n.node_type AS node_type, n.drift_class AS drift_class" 2>/dev/null > <file>
    Prefer the concrete arn: resource node (not the *_POLICY shadow / non-arn dup) per name.
    source_sha = drift_class (matches derive_runner._graph_to_scan_nodes)."""
    with open(nodes_json, encoding="utf-8") as f:
        rows = json.load(f)
    by_name: dict = {}
    for r in rows:
        nm = r.get("name")
        nid = str(r.get("node_id", ""))
        ntype = str(r.get("node_type", ""))
        if not nm or not nid:
            continue
        good = nid.startswith("arn:") and not ntype.endswith("_POLICY")
        cur = by_name.get(nm)
        if cur is None or (good and not cur["good"]):
            by_name[nm] = {"node_id": nid, "node_type": ntype,
                           "source_sha": str(r.get("drift_class", "")), "good": good}
    return {k: {"node_id": v["node_id"], "node_type": v["node_type"],
                "source_sha": v["source_sha"]} for k, v in by_name.items()}


def _members_for(block: dict) -> list:
    """Flatten a producers/served_buckets/serving_lambdas block -> list of names."""
    out = []
    for key in ("producers", "served_buckets", "serving_lambdas"):
        out.extend(block.get(key, []) or [])
    return out


def build_baseline(nodes_json: str) -> dict:
    with open(SURFACES_YAML, encoding="utf-8") as f:
        doc = yaml.safe_load(f)

    # collect all member names across all surfaces x firms, then resolve once
    surface_members: dict = {}   # sf_key -> (severity, [names])
    all_names: set = set()
    for s in doc.get("surfaces", []):
        sid, sev = s["id"], s.get("severity", "SEV2")
        ab = s.get("aws_backend", {}) or {}
        if ab.get("firm_scope") == "per_firm":
            for firm, fb in (ab.get("per_firm", {}) or {}).items():
                if (fb or {}).get("status") == "no-op":
                    print(f"INFO: {sid}__{firm} = documented no-op (skipped, not armed)")
                    continue
                names = _members_for(fb or {})
                surface_members[f"{sid}__{firm}"] = (sev, names)
                all_names.update(names)
        else:
            names = _members_for(ab)
            surface_members[f"{sid}__all"] = (sev, names)
            all_names.update(names)

    resolved = _load_node_map(nodes_json)
    n_hit = sum(1 for nm in all_names if nm in resolved)
    print(f"INFO: resolved {n_hit}/{len(all_names)} member names from {nodes_json} "
          f"({len(resolved)} graph nodes loaded)")

    surfaces_out: dict = {}
    unresolved: dict = {}
    for sf_key, (sev, names) in surface_members.items():
        members = {}
        miss = []
        for nm in names:
            r = resolved.get(nm)
            if r:
                members[r["node_id"]] = {"node_type": r["node_type"], "name": nm,
                                         "source_sha": r["source_sha"]}
            else:
                miss.append(nm)
        surfaces_out[sf_key] = {"severity": sev, "members": members}
        if miss:
            unresolved[sf_key] = miss
            print(f"CAVEAT: {sf_key} unresolved members (recorded, not silent): {miss}")

    f6 = {}
    try:
        s3 = boto3.client("s3", region_name=REGION)
        f6 = json.loads(s3.get_object(Bucket=SNAPSHOT_BUCKET, Key=F6_MARKER_KEY)["Body"].read())
    except Exception as e:
        print(f"WARN: could not read F6 marker for vintage anchor: {e}")

    return {"schema": "d8fp-aws-backend-membership-v1", "built_at": time.time(),
            "f6_marker": f6, "surfaces": surfaces_out, "unresolved": unresolved}


def main() -> int:
    if os.environ.get("ALLOW_DEPRECATED_RESIGN") != "1":
        print("ERROR: resign_surface_baseline.py is DEPRECATED (NFRA_GRAPHS.D8-FP, CTO 204916Z) -- it\n"
              "       signs from a dump/snapshot INDIRECTION that can DIVERGE from the live scan cn (the\n"
              "       3-mismatch class). Sign BY CONSTRUCTION instead: derive_runner.py --sign-baseline.\n"
              "       (forensic override only: ALLOW_DEPRECATED_RESIGN=1)", file=sys.stderr)
        return 2
    ap = argparse.ArgumentParser(description="Re-sign critical-surface baseline (D8-FP membership)")
    ap.add_argument("--dry-run", action="store_true", help="build + print, do NOT upload")
    ap.add_argument("--nodes-json", default=".runtmp/d8fp_allnodes.json",
                    help="comp-kuzu --json CloudNode dump (name/node_id/node_type/drift_class)")
    args = ap.parse_args()

    baseline = build_baseline(args.nodes_json)
    n_surf = len(baseline["surfaces"])
    n_mem = sum(len(s["members"]) for s in baseline["surfaces"].values())
    print(f"INFO: built baseline -- {n_surf} surface x firm, {n_mem} members, "
          f"{len(baseline['unresolved'])} surface(s) with unresolved caveats")
    for k, v in sorted(baseline["surfaces"].items()):
        print(f"  {k} [{v['severity']}]: {len(v['members'])} members")

    if args.dry_run:
        print("DRY-RUN: not uploaded. Re-run without --dry-run to publish.")
        return 0

    s3 = boto3.client("s3", region_name=REGION)
    # back up the existing baseline before overwrite
    try:
        old = s3.get_object(Bucket=SNAPSHOT_BUCKET, Key=BASELINE_KEY)["Body"].read()
        s3.put_object(Bucket=SNAPSHOT_BUCKET, Key=BASELINE_KEY + ".legacy-pre-d8fp",
                      Body=old, ContentType="application/json")
        print(f"OK: backed up old baseline -> {BASELINE_KEY}.legacy-pre-d8fp")
    except Exception as e:
        print(f"WARN: no old baseline to back up (or read failed): {e}")
    s3.put_object(Bucket=SNAPSHOT_BUCKET, Key=BASELINE_KEY,
                  Body=json.dumps(baseline, indent=2).encode(), ContentType="application/json")
    print(f"OK: RE-SIGNED baseline -> s3://{SNAPSHOT_BUCKET}/{BASELINE_KEY} "
          f"({n_surf} surface x firm, {n_mem} members)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
