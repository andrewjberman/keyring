"""NFRA_COMPAWS.PHASE-0 G2 -- cut-1 edge-census ORACLE generator (CVO-ruled 191744Z).

INDEPENDENT live hand-audit of the IAM/security-adjacent edge classes, enumerated
from raw boto3 -- DELIBERATELY independent of comp_aws_cli.derive_edges so the
PASS-2 cert (derive-emitted edges diff-to-0 vs this oracle) is NOT circular. This
is the ground-truth the derive must match; if the derive misses an edge this finds,
that's a derive FINDING (routed to CVO), not a silent fold.

Cut-1 classes (CVO ruling 3):
  1. compute -> IAM_ROLE   (ASSUMES): EC2(via instance-profile) / Lambda / SFN / ECS-task-def
  2. compute -> SECURITY_GROUP (IN_SG): EC2 / VPC-Lambda  (+ the SG node census --
     makes the "0 world-open non-web SG" assertion certifiable, CVO hand-audit G2)
  3. role -> S3_BUCKET (GRANTS, one-sided) -- increment-2 (the policy-parse; effperm
     intersection is increment-(b) per CVO ruling 2). NOT in this cut.

Emits a YAML census (source/target/edge_class per edge) -> aws-shapes/g2-edge-census-cut1.yaml.
Run: python g2_edge_oracle.py  (us-east-1; read-only). Author: 0.7.0_AE_CloudOps~B.
"""
from __future__ import annotations

import boto3

REGION = "us-east-1"
ACCOUNT = "313476888478"


def _paginate(client, op, key, **kw):
    items = []
    paginator = client.get_paginator(op)
    for page in paginator.paginate(**kw):
        items.extend(page.get(key, []))
    return items


def assumes_edges():
    """compute -> IAM_ROLE (ASSUMES), every compute identity from live."""
    edges = []
    lam = boto3.client("lambda", region_name=REGION)
    ec2 = boto3.client("ec2", region_name=REGION)
    iam = boto3.client("iam", region_name=REGION)
    sfn = boto3.client("stepfunctions", region_name=REGION)
    ecs = boto3.client("ecs", region_name=REGION)

    lambdas = _paginate(lam, "list_functions", "Functions")
    for fn in lambdas:
        edges.append({"source": f"LAMBDA:{fn['FunctionName']}", "target": fn["Role"],
                      "edge_class": "ASSUMES", "via": "lambda.Role"})
    # EC2 -> instance-profile -> role
    prof_role = {ip["Arn"]: [r["Arn"] for r in ip.get("Roles", [])]
                 for ip in _paginate(iam, "list_instance_profiles", "InstanceProfiles")}
    res = _paginate(ec2, "describe_instances", "Reservations",
                    Filters=[{"Name": "instance-state-name", "Values": ["running", "stopped"]}])
    for r in res:
        for inst in r["Instances"]:
            ip = (inst.get("IamInstanceProfile") or {}).get("Arn")
            for rarn in prof_role.get(ip, []) if ip else []:
                edges.append({"source": f"EC2:{inst['InstanceId']}", "target": rarn,
                              "edge_class": "ASSUMES", "via": f"instance-profile {ip.split('/')[-1]}"})
    # State machines -> role
    for sm in _paginate(sfn, "list_state_machines", "stateMachines"):
        d = sfn.describe_state_machine(stateMachineArn=sm["stateMachineArn"])
        edges.append({"source": f"STATE_MACHINE:{sm['name']}", "target": d["roleArn"],
                      "edge_class": "ASSUMES", "via": "stepfunctions.roleArn"})
    # ECS task definitions -> task + execution role (ACTIVE)
    for arn in _paginate(ecs, "list_task_definitions", "taskDefinitionArns", status="ACTIVE"):
        td = ecs.describe_task_definition(taskDefinition=arn)["taskDefinition"]
        fam = f"ECS_TASK_DEF:{td['family']}:{td['revision']}"
        for key in ("taskRoleArn", "executionRoleArn"):
            if td.get(key):
                edges.append({"source": fam, "target": td[key], "edge_class": "ASSUMES",
                              "via": f"ecs.{key}"})
    return edges


def sg_edges_and_nodes():
    """compute -> SECURITY_GROUP (IN_SG) + the SG node census (world-open flagged)."""
    ec2 = boto3.client("ec2", region_name=REGION)
    lam = boto3.client("lambda", region_name=REGION)
    edges = []
    res = _paginate(ec2, "describe_instances", "Reservations",
                    Filters=[{"Name": "instance-state-name", "Values": ["running", "stopped"]}])
    for r in res:
        for inst in r["Instances"]:
            for sg in inst.get("SecurityGroups", []):
                edges.append({"source": f"EC2:{inst['InstanceId']}", "target": f"SG:{sg['GroupId']}",
                              "edge_class": "IN_SG", "via": "ec2.SecurityGroups"})
    for fn in _paginate(lam, "list_functions", "Functions"):
        for sgid in (fn.get("VpcConfig") or {}).get("SecurityGroupIds", []) or []:
            edges.append({"source": f"LAMBDA:{fn['FunctionName']}", "target": f"SG:{sgid}",
                          "edge_class": "IN_SG", "via": "lambda.VpcConfig"})
    nodes = []
    for sg in _paginate(ec2, "describe_security_groups", "SecurityGroups"):
        world_open = []
        for p in sg.get("IpPermissions", []):
            if any(rg.get("CidrIp") == "0.0.0.0/0" for rg in p.get("IpRanges", [])):
                lo, hi = p.get("FromPort"), p.get("ToPort")
                world_open.append(f"{lo}-{hi}" if lo != hi else str(lo))
        nodes.append({"id": f"SG:{sg['GroupId']}", "name": sg.get("GroupName", ""),
                      "world_open_ingress_ports": world_open})
    return edges, nodes


def render(assumes, sg_edges, sg_nodes):
    world_open = [n for n in sg_nodes if n["world_open_ingress_ports"]]
    lines = ["# NFRA_COMPAWS G2 cut-1 edge-census ORACLE (independent live hand-audit, raw boto3).",
             "# Diff TARGET for hand-audit PASS-2: derive-emitted edges must == this set, 0-diff.",
             "# Generated by g2_edge_oracle.py. role->bucket GRANTS = increment-2 (not in this cut).",
             f"counts: {{assumes: {len(assumes)}, in_sg: {len(sg_edges)}, "
             f"sg_nodes: {len(sg_nodes)}, world_open_sg: {len(world_open)}}}",
             "assumes_edges:"]
    for e in sorted(assumes, key=lambda x: (x["source"], x["target"])):
        lines.append(f'  - {{source: "{e["source"]}", target: "{e["target"]}", via: "{e["via"]}"}}')
    lines.append("in_sg_edges:")
    for e in sorted(sg_edges, key=lambda x: (x["source"], x["target"])):
        lines.append(f'  - {{source: "{e["source"]}", target: "{e["target"]}"}}')
    lines.append("sg_nodes:")
    for n in sorted(sg_nodes, key=lambda x: x["id"]):
        wp = ",".join(n["world_open_ingress_ports"]) or "none"
        lines.append(f'  - {{id: "{n["id"]}", name: "{n["name"]}", world_open_ingress: "{wp}"}}')
    return "\n".join(lines)


def main():
    assumes = assumes_edges()
    sg_edges, sg_nodes = sg_edges_and_nodes()
    print(render(assumes, sg_edges, sg_nodes))


if __name__ == "__main__":
    main()
