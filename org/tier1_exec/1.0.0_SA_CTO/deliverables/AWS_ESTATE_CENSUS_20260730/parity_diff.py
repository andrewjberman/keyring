"""ARN-grain parity diff: LIVE AWS census vs globgrph CloudNode (aws layer).

Instruments (all files in this dir, produced 2026-07-30 by 1.0.0_SA_CTO):
  LIVE side : re_us-east-1.json + re_us-east-2.json (Resource Explorer list-resources),
              s3_buckets.json, iam_roles.json, iam_users.json, iam_policies_local.json,
              cloudfront.json (direct global enumerations)
  GRAPH side: kuzu_aws_nodes_raw.txt (comp-kuzu dump of layer='aws' nodes)

Output: parity_report.json + stdout summary.
Denominators printed for every verdict; no silent caps.
"""
from __future__ import annotations

import json
import re
from collections import defaultdict

ACCT = "313476888478"


def norm(arn: str) -> str:
    a = arn.strip()
    if a.endswith(":*"):
        a = a[:-2]
    return a


# ---- GRAPH side ----------------------------------------------------------
graph = defaultdict(set)          # node_type -> set of normalized arns
graph_noarn = defaultdict(int)    # node_type -> count with no arn
rows = 0
with open("kuzu_aws_nodes_raw.txt", encoding="utf-8", errors="replace") as f:
    started = False
    for line in f:
        if line.startswith("----"):
            started = True
            continue
        if not started:
            continue
        parts = line.split()
        if len(parts) < 2 or parts[0] in ("(", ""):
            continue
        ntype = parts[0]
        if not re.match(r"^[A-Z0-9_]+$", ntype):
            continue
        rows += 1
        arn_tok = next((p for p in parts[1:] if p.startswith("arn:aws")), None)
        if arn_tok:
            graph[ntype].add(norm(arn_tok))
        else:
            graph_noarn[ntype] += 1

# ---- LIVE side -----------------------------------------------------------
live = defaultdict(set)           # RE ResourceType -> arns
for fn in ("re_us-east-1.json", "re_us-east-2.json"):
    d = json.load(open(fn))
    for r in d.get("Resources", []):
        live[r["ResourceType"]].add(norm(r["Arn"]))

s3_live = {f"arn:aws:s3:::{b}" for b in json.load(open("s3_buckets.json"))}
iam_roles_live = {norm(r["a"]) for r in json.load(open("iam_roles.json"))}
iam_users_live = {norm(u["a"]) for u in json.load(open("iam_users.json"))}
iam_pol_local = {norm(p["a"]) for p in json.load(open("iam_policies_local.json"))}
cf_live = {f"arn:aws:cloudfront::{ACCT}:distribution/{d['id']}"
           for d in (json.load(open("cloudfront.json")) or [])}

# ---- type mapping: graph node_type -> live arn set -----------------------
MAP = {
    "LAMBDA":               live["lambda:function"],
    "LOG_GROUP":            live["logs:log-group"],
    "EVENT_RULE":           live["events:rule"],
    "SECRET":               live["secretsmanager:secret"],
    "CW_ALARM":             live["cloudwatch:alarm"],
    "DYNAMODB_TABLE":       live["dynamodb:table"],
    "S3_BUCKET":            s3_live,
    "IAM_ROLE":             iam_roles_live,
    "IAM_USER":             iam_users_live,
    "EC2_INSTANCE":         live["ec2:instance"],
    "SECURITY_GROUP":       live["ec2:security-group"],
    "SNS_TOPIC":            live["sns:topic"],
    "SQS_QUEUE":            live["sqs:queue"],
    "KMS_KEY":              live["kms:key"],
    "SSM_DOCUMENT":         live["ssm:document"],
    "INSTANCE_PROFILE":     live["iam:instance-profile"],
    "ECS_TASK_DEFINITION":  live["ecs:task-definition"],
    "ECS_CLUSTER":          live["ecs:cluster"],
    "CLOUDFRONT_DISTRIBUTION": cf_live,
    "STATE_MACHINE":        live["states:stateMachine"],
    "CODEBUILD_PROJECT":    live["codebuild:project"],
    "VPC_ENDPOINT":         live["ec2:vpc-endpoint"],
    "LOAD_BALANCER":        live["elasticloadbalancing:loadbalancer"]
                            | live["elasticloadbalancing:loadbalancer/app"]
                            | live["elasticloadbalancing:loadbalancer/net"],
    "SCHEDULE":             live["scheduler:schedule"],
    "API_GW":               live["apigateway:apis"] | live["apigateway:restapis"],
}

report = {}
print(f"GRAPH rows parsed: {rows} (aws layer)")
print(f"{'node_type':26s} {'graph':>5s} {'live':>5s} {'match':>5s} {'g-only':>6s} {'l-only':>6s}")
for ntype in sorted(MAP, key=lambda t: -len(graph.get(t, set()))):
    g = graph.get(ntype, set())
    lv = MAP[ntype]
    inter = g & lv
    report[ntype] = {
        "graph": len(g), "live": len(lv), "matched": len(inter),
        "graph_only": sorted(g - lv), "live_only": sorted(lv - g),
    }
    print(f"{ntype:26s} {len(g):5d} {len(lv):5d} {len(inter):5d} "
          f"{len(g - lv):6d} {len(lv - g):6d}")

# graph types with no live mapping (abstractions / sub-resources / config nodes)
all_gtypes = set(graph) | set(graph_noarn)
unmapped_graph = {t: len(graph.get(t, set())) + graph_noarn.get(t, 0)
                  for t in all_gtypes if t not in MAP}
# live types with no graph mapping (the blindness surface)
mapped_live_arns = set()
for s in MAP.values():
    mapped_live_arns |= s
unmapped_live = {t: len(v) for t, v in live.items()
                 if not (v & mapped_live_arns) and len(v) > 0}

print("\nGRAPH-ONLY node types (abstraction/sub-resource/config -- no 1:1 live type):")
for t, c in sorted(unmapped_graph.items(), key=lambda x: -x[1]):
    print(f"  {t}: {c}")
print("\nLIVE-ONLY resource types (graph models NOTHING here -- the blindness surface):")
for t, c in sorted(unmapped_live.items(), key=lambda x: -x[1]):
    print(f"  {t}: {c}")

print("\n--- live-only detail (every non-zero delta, full list) ---")
for ntype, r in report.items():
    if r["live_only"]:
        print(f"  {ntype} ({len(r['live_only'])}):")
        for a in r["live_only"]:
            print(f"    {a}")
    if r["graph_only"]:
        print(f"  {ntype} GRAPH-ONLY ({len(r['graph_only'])}):")
        for a in r["graph_only"]:
            print(f"    {a}")

with open("parity_report.json", "w") as f:
    json.dump({"per_type": report,
               "graph_unmapped_types": unmapped_graph,
               "live_unmapped_types": unmapped_live}, f, indent=1)
print("\nwrote parity_report.json")
