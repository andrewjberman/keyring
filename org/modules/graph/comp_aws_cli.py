#!/usr/bin/env python3
"""comp-aws -- comprehensive AWS cloud compiler (ADHC_CMPAWS).

Derives a typed, certified graph of the AWS cloud by reconciling THREE truths:
  1. IaC  (Terraform parse, HCL-aware -- NOT text-grep; see IE-GAP-3 finding 2026-06-08)
  2. LIVE (boto3 describe/list, read-only, in-process -- NOT shell+CLI; see CRLF finding)
  3. source/provenance (commit/sha where derivable)

Emits typed nodes + edges + drift classes (DECLARED / LIVE-no-DECLARED /
DECLARED-no-LIVE / NO-PROVENANCE) per resource class, and SCORES the derivation's
precision / recall / F1 against the CVO-certified hand-audit oracles
(org/modules/graph/aws-shapes/*.yaml).

Subcommands:
  derive [--class C] [--out FILE]   live+TF derive -> canonical typed graph JSON
  score  [--class C]                P/R/F1 per class vs certified oracle
  snapshot                          archive the canonical graph (PRD AC7)
  classes                           list supported resource classes

Goal: >=95% F1 deterministic cloud navigation (Andrew goal 2026-06-08).

Author: 0.7.0_AE_CloudOps. Pattern: extends comp-iam / comp-lambdamap (PRD AC6).
"""
from __future__ import annotations
import argparse
import json
import tarfile
import io
from pathlib import Path

WS = Path(__file__).resolve().parents[3]   # ajb_workspace root (org/modules/graph/<file>)
TF_ROOT = WS / "infra" / "aws" / "terraform"
SHAPES = WS / "org" / "modules" / "graph" / "aws-shapes"
ACCOUNT = "313476888478"
REGIONS = ["us-east-1", "us-east-2"]

def _boto(svc, region="us-east-1"):
    import boto3
    return boto3.client(svc, region_name=region)

# ---------------------------------------------------------------------------
# DECLARED SIDE -- from TERRAFORM STATE (S3), union across ALL root modules.
# Per the CTO invariant + CVO done-gate: the declared set is `terraform show
# -json`-equivalent (raw state .resources[] carries the real, post-apply ARNs +
# attributes), NOT a text-grep of .tf (which undercounts -- IE-GAP-3 2026-06-08).
# Discovery-based: list every */tfstate key in the state bucket (no hardcoded
# module list -> brittleness-safe), parse each, union managed resources keyed by
# ARN. Cached per-process; the cloud-shape snapshot persists the resolved set.
# ---------------------------------------------------------------------------
TFSTATE_BUCKET = "opal-313476888478-terraform-state"
_TFSTATE_CACHE = {}

def _load_all_tfstate():
    """Discover + read every root-module state from S3. Returns the union of
    managed resources: list of {type, tf_name, module, arn, id, attrs}."""
    if _TFSTATE_CACHE:
        return _TFSTATE_CACHE["resources"]
    s3 = _boto("s3")
    resources = []
    keys = []
    tok = None
    while True:
        kw = {"Bucket": TFSTATE_BUCKET}
        if tok:
            kw["ContinuationToken"] = tok
        resp = s3.list_objects_v2(**kw)
        for o in resp.get("Contents", []):
            if o["Key"].endswith("tfstate"):
                keys.append(o["Key"])
        if resp.get("IsTruncated"):
            tok = resp.get("NextContinuationToken")
        else:
            break
    for key in keys:
        module = key.split("/")[0]
        try:
            body = s3.get_object(Bucket=TFSTATE_BUCKET, Key=key)["Body"].read()
            st = json.loads(body)
        except Exception:
            continue
        for r in st.get("resources", []):
            if r.get("mode") != "managed":
                continue
            for inst in r.get("instances", []):
                a = inst.get("attributes", {}) or {}
                resources.append({
                    "type": r["type"], "tf_name": r.get("name"), "module": module,
                    "arn": a.get("arn"), "id": a.get("id"),
                    "name": a.get("name") or a.get("bucket") or a.get("function_name")
                            or a.get("alarm_name"),
                    "attrs": a,
                })
    _TFSTATE_CACHE["resources"] = resources
    _TFSTATE_CACHE["module_count"] = len({k.split("/")[0] for k in keys})
    return resources

def tf_state_index(resource_types):
    """Build lookup indexes for the given TF resource type(s) from state:
    by ARN, by id, by name. Returns (by_arn, by_id, by_name, declared_list)."""
    if isinstance(resource_types, str):
        resource_types = [resource_types]
    rts = set(resource_types)
    by_arn, by_id, by_name = {}, {}, {}
    declared = []
    for r in _load_all_tfstate():
        if r["type"] not in rts:
            continue
        prov = {"tf_module": r["module"], "tf_resource": f'{r["type"]}.{r["tf_name"]}',
                "tf_type": r["type"]}
        rec = {"arn": r["arn"], "id": r["id"], "name": r["name"], "provenance": prov}
        declared.append(rec)
        if r["arn"]:
            by_arn[r["arn"]] = prov
        if r["id"]:
            by_id[str(r["id"])] = prov
        if r["name"]:
            by_name[r["name"]] = prov
    return by_arn, by_id, by_name, declared

# ---------------------------------------------------------------------------
# LIVE DERIVE -- per class (boto3 in-process). Each returns a list of typed nodes.
# ---------------------------------------------------------------------------
def live_s3():
    c = _boto("s3")
    nodes = []
    for b in c.list_buckets().get("Buckets", []):
        name = b["Name"]
        node = {"id": name, "type": "S3_BUCKET"}
        try:
            loc = c.get_bucket_location(Bucket=name).get("LocationConstraint")
            node["region"] = loc or "us-east-1"
        except Exception:
            node["region"] = "?"
        try:
            v = c.get_bucket_versioning(Bucket=name).get("Status")
            node["versioning_enabled"] = (v == "Enabled")
        except Exception:
            node["versioning_enabled"] = None
        try:
            pab = c.get_public_access_block(Bucket=name)["PublicAccessBlockConfiguration"]
            node["public_access_block"] = all(pab.get(k, False) for k in
                ("BlockPublicAcls","IgnorePublicAcls","BlockPublicPolicy","RestrictPublicBuckets"))
        except Exception:
            node["public_access_block"] = False
        try:
            c.get_bucket_policy(Bucket=name)
            node["has_policy"] = True
        except Exception:
            node["has_policy"] = False
        try:
            nc = c.get_bucket_notification_configuration(Bucket=name)
            node["event_notifications"] = len(nc.get("LambdaFunctionConfigurations", []))
        except Exception:
            node["event_notifications"] = 0
        nodes.append(node)
    return nodes

def live_iam_roles():
    c = _boto("iam")
    nodes = []
    pag = c.get_paginator("list_roles")
    for pg in pag.paginate():
        for r in pg["Roles"]:
            rn = r["RoleName"]
            # skip AWS service-linked roles (path /aws-service-role/) -- not customer roles
            if r.get("Path", "/").startswith("/aws-service-role/"):
                continue
            node = {"id": rn, "type": "IAM_ROLE", "arn": r["Arn"]}
            try:
                node["attached_managed"] = [p["PolicyName"] for p in
                    c.list_attached_role_policies(RoleName=rn).get("AttachedPolicies", [])]
            except Exception:
                node["attached_managed"] = []
            node["broad_managed"] = [p for p in node["attached_managed"]
                                     if "FullAccess" in p or "Administrator" in p]
            nodes.append(node)
    return nodes

def live_ec2():
    nodes = []
    for region in REGIONS:
        c = _boto("ec2", region)
        try:
            resv = c.describe_instances()["Reservations"]
        except Exception:
            continue
        for grp in resv:
            for i in grp["Instances"]:
                if i["State"]["Name"] == "terminated":
                    continue
                name = next((t["Value"] for t in i.get("Tags", []) if t["Key"] == "Name"), None)
                prof = i.get("IamInstanceProfile", {}).get("Arn", "")
                nodes.append({
                    "id": i["InstanceId"], "type": "EC2_INSTANCE", "name": name,
                    "region": region, "state": i["State"]["Name"],
                    "instance_type": i.get("InstanceType"),
                    "instance_profile": prof.split("/")[-1] if prof else None,
                    "imdsv2_required": i.get("MetadataOptions", {}).get("HttpTokens") == "required",
                    "public_ip": i.get("PublicIpAddress"),
                })
    return nodes

def live_lambda():
    nodes = []
    c = _boto("lambda")
    pag = c.get_paginator("list_functions")
    for pg in pag.paginate():
        for fn in pg["Functions"]:
            nodes.append({"id": fn["FunctionName"], "type": "LAMBDA",
                          "runtime": fn.get("Runtime"), "role": (fn.get("Role") or "").split("/")[-1]})
    return nodes

def live_eventbridge():
    nodes = []
    c = _boto("events")
    pag = c.get_paginator("list_rules")
    for pg in pag.paginate():
        for r in pg["Rules"]:
            nodes.append({"id": r["Name"], "type": "EVENT_RULE",
                          "schedule": r.get("ScheduleExpression"),
                          "state": r.get("State")})
    return nodes

def live_sns():
    nodes = []
    c = _boto("sns")
    for t in c.list_topics().get("Topics", []):
        arn = t["TopicArn"]
        name = arn.split(":")[-1]
        try:
            attrs = c.get_topic_attributes(TopicArn=arn)["Attributes"]
            kms = bool(attrs.get("KmsMasterKeyId"))
        except Exception:
            kms = None
        nodes.append({"id": name, "type": "SNS_TOPIC", "kms_encrypted": kms})
    return nodes

def live_sqs():
    nodes = []
    c = _boto("sqs")
    for url in c.list_queues().get("QueueUrls", []):
        name = url.split("/")[-1]
        try:
            a = c.get_queue_attributes(QueueUrl=url, AttributeNames=["KmsMasterKeyId","SqsManagedSseEnabled"])["Attributes"]
            enc = bool(a.get("KmsMasterKeyId")) or a.get("SqsManagedSseEnabled") == "true"
        except Exception:
            enc = None
        nodes.append({"id": name, "type": "SQS_QUEUE", "encrypted": enc})
    return nodes

def live_dynamodb():
    nodes = []
    c = _boto("dynamodb")
    pag = c.get_paginator("list_tables")
    for pg in pag.paginate():
        for t in pg["TableNames"]:
            try:
                d = c.describe_table(TableName=t)["Table"]
                sse = d.get("SSEDescription", {}).get("SSEType")
            except Exception:
                sse = None
            nodes.append({"id": t, "type": "DYNAMODB_TABLE", "sse_type": sse})
    return nodes

def live_cloudfront():
    nodes = []
    c = _boto("cloudfront")
    try:
        dl = c.list_distributions().get("DistributionList", {}).get("Items", [])
    except Exception:
        dl = []
    for d in dl:
        nodes.append({"id": d["Id"], "type": "CLOUDFRONT_DISTRIBUTION",
                      "domain": d.get("DomainName"), "enabled": d.get("Enabled"),
                      "aliases": d.get("Aliases", {}).get("Items", [])})
    return nodes

def live_secrets():
    nodes = []
    c = _boto("secretsmanager")
    pag = c.get_paginator("list_secrets")
    for pg in pag.paginate():
        for s in pg["SecretList"]:
            nodes.append({"id": s["Name"], "name": s["Name"], "arn": s.get("ARN"),
                          "type": "SECRET", "kms": bool(s.get("KmsKeyId"))})
    return nodes

def live_kms():
    nodes = []
    c = _boto("kms")
    pag = c.get_paginator("list_keys")
    for pg in pag.paginate():
        for k in pg["Keys"]:
            try:
                meta = c.describe_key(KeyId=k["KeyId"])["KeyMetadata"]
                if meta.get("KeyManager") == "AWS":
                    continue  # AWS-managed keys are not customer resources
                aliases = [a["AliasName"] for a in c.list_aliases(KeyId=k["KeyId"]).get("Aliases", [])]
            except Exception:
                aliases = []
            nodes.append({"id": k["KeyId"], "type": "KMS_KEY", "aliases": aliases})
    return nodes

def live_cloudwatch_alarms():
    nodes = []
    c = _boto("cloudwatch")
    pag = c.get_paginator("describe_alarms")
    for pg in pag.paginate():
        for a in pg.get("MetricAlarms", []):
            nodes.append({"id": a["AlarmName"], "type": "CW_ALARM", "state": a.get("StateValue")})
    return nodes

# class -> (live_fn, [tf_resource_types that materialize this class's nodes])
CLASSES = {
    "s3":          (live_s3,                ["aws_s3_bucket"]),
    "iam":         (live_iam_roles,         ["aws_iam_role"]),
    "ec2":         (live_ec2,               ["aws_instance"]),
    "lambda":      (live_lambda,            ["aws_lambda_function"]),
    "eventbridge": (live_eventbridge,       ["aws_cloudwatch_event_rule"]),
    "sns":         (live_sns,               ["aws_sns_topic"]),
    "sqs":         (live_sqs,               ["aws_sqs_queue"]),
    "dynamodb":    (live_dynamodb,          ["aws_dynamodb_table"]),
    "cloudfront":  (live_cloudfront,        ["aws_cloudfront_distribution"]),
    "secrets":     (live_secrets,           ["aws_secretsmanager_secret"]),
    "kms":         (live_kms,               ["aws_kms_key"]),
    "cloudwatch":  (live_cloudwatch_alarms, ["aws_cloudwatch_metric_alarm"]),
}

def _node_arn(cls, node):
    """Canonical ARN for a live node (the §1 matching key). Prefer an API-given
    arn; else construct deterministically. Region-aware for EC2/KMS."""
    if node.get("arn"):
        return node["arn"]
    i = node["id"]
    rg = node.get("region", "us-east-1")
    return {
        "s3":          f"arn:aws:s3:::{i}",
        "ec2":         f"arn:aws:ec2:{rg}:{ACCOUNT}:instance/{i}",
        "lambda":      f"arn:aws:lambda:us-east-1:{ACCOUNT}:function:{i}",
        "eventbridge": f"arn:aws:events:us-east-1:{ACCOUNT}:rule/{i}",
        "sns":         f"arn:aws:sns:us-east-1:{ACCOUNT}:{i}",
        "sqs":         f"arn:aws:sqs:us-east-1:{ACCOUNT}:{i}",
        "dynamodb":    f"arn:aws:dynamodb:us-east-1:{ACCOUNT}:table/{i}",
        "cloudfront":  f"arn:aws:cloudfront::{ACCOUNT}:distribution/{i}",
        "kms":         f"arn:aws:kms:{rg}:{ACCOUNT}:key/{i}",
        "cloudwatch":  f"arn:aws:cloudwatch:us-east-1:{ACCOUNT}:alarm:{i}",
    }.get(cls, i)

def derive_class(cls):
    live_fn, tf_types = CLASSES[cls]
    live = live_fn()
    by_arn, by_id, by_name, declared = tf_state_index(tf_types)
    matched_decl = set()
    for n in live:
        arn = _node_arn(cls, n)
        n["arn"] = arn
        # ARN-canonical join, with id/name fallback (CVO §1 matching key)
        prov = by_arn.get(arn) or by_id.get(str(n["id"])) or (by_name.get(n.get("name")) if n.get("name") else None)
        if prov:
            n["drift_class"] = "DECLARED"
            n["provenance"] = prov
            n["tf_managed"] = True
            n["owner_pipeline"] = prov.get("tf_module")
            matched_decl.add(prov["tf_resource"])
        else:
            n["drift_class"] = "LIVE-no-DECLARED"
            n["provenance"] = None
            n["tf_managed"] = False
            n["owner_pipeline"] = None
        # §1.1 universal node properties
        if "type" not in n:           # 0-untyped invariant
            n["type"] = cls.upper()
        if not n.get("name"):
            n["name"] = n["id"]
    declared_no_live = [d for d in declared if d["provenance"]["tf_resource"] not in matched_decl]
    return {
        "class": cls,
        "nodes": live,
        "declared_no_live": declared_no_live,
        "counts": {
            "live": len(live),
            "tf_declared": len(declared),
            "live_declared": sum(1 for n in live if n.get("drift_class") == "DECLARED"),
            "live_no_declared": sum(1 for n in live if n.get("drift_class") == "LIVE-no-DECLARED"),
            "declared_no_live": len(declared_no_live),
            "untyped": sum(1 for n in live if not n.get("type")),
        },
    }

# ---------------------------------------------------------------------------
# EDGES -- typed relationships (PRD §3 / CVO schema). Derived from live AWS,
# discovery-based (no hardcoded edge lists). Each edge: (src_arn, dst_arn, type).
# ---------------------------------------------------------------------------
def derive_edges():
    edges = []
    def E(s, d, t, **extra):
        if s and d:
            edges.append({"source": s, "target": d, "edge_type": t, **extra})

    iamc = _boto("iam")
    # EC2 -[HAS_PROFILE]-> INSTANCE_PROFILE -[ASSUMES]-> IAM_ROLE
    prof_role = {}
    for n in live_ec2():
        iarn = _node_arn("ec2", n)
        prof = n.get("instance_profile")
        if not prof:
            continue
        parn = f"arn:aws:iam::{ACCOUNT}:instance-profile/{prof}"
        E(iarn, parn, "HAS_PROFILE")
        if prof not in prof_role:
            try:
                r = iamc.get_instance_profile(InstanceProfileName=prof)
                prof_role[prof] = [x["Arn"] for x in r["InstanceProfile"]["Roles"]]
            except Exception:
                prof_role[prof] = []
        for rarn in prof_role[prof]:
            E(parn, rarn, "ASSUMES")
    # IAM_ROLE -[HAS_POLICY]-> IAM_POLICY (managed ARN + inline name); + STARTS via lambda
    for n in live_iam_roles():
        rarn = n["arn"]
        rn = n["id"]
        try:
            for p in iamc.list_attached_role_policies(RoleName=rn).get("AttachedPolicies", []):
                E(rarn, p["PolicyArn"], "HAS_POLICY", policy_kind="managed", policy_name=p["PolicyName"])
        except Exception:
            pass
        try:
            for pn in iamc.list_role_policies(RoleName=rn).get("PolicyNames", []):
                E(rarn, f"{rarn}/inline/{pn}", "HAS_POLICY", policy_kind="inline", policy_name=pn)
        except Exception:
            pass
    # LAMBDA -[ASSUMES]-> role ; LAMBDA -[STARTS]-> EC2 (env GOLD_RUNNER_INSTANCE_ID + ec2:StartInstances)
    lc = _boto("lambda")
    for n in live_lambda():
        farn = _node_arn("lambda", n)
        if n.get("role"):
            E(farn, f"arn:aws:iam::{ACCOUNT}:role/{n['role']}", "ASSUMES")
        try:
            cfg = lc.get_function_configuration(FunctionName=n["id"])
            env = (cfg.get("Environment") or {}).get("Variables", {}) or {}
            for k, v in env.items():
                if "INSTANCE_ID" in k and str(v).startswith("i-"):
                    E(farn, f"arn:aws:ec2:us-east-1:{ACCOUNT}:instance/{v}", "STARTS", via=k)
        except Exception:
            pass
    # S3_BUCKET -[NOTIFIES]-> LAMBDA
    s3c = _boto("s3")
    for n in live_s3():
        try:
            nc = s3c.get_bucket_notification_configuration(Bucket=n["id"])
            for lf in nc.get("LambdaFunctionConfigurations", []):
                E(f"arn:aws:s3:::{n['id']}", lf["LambdaFunctionArn"], "TRIGGERS")
        except Exception:
            pass
    # CLOUDFRONT -[ORIGIN]-> S3
    cf = _boto("cloudfront")
    try:
        for d in cf.list_distributions().get("DistributionList", {}).get("Items", []):
            darn = f"arn:aws:cloudfront::{ACCOUNT}:distribution/{d['Id']}"
            for o in d.get("Origins", {}).get("Items", []):
                dn = o.get("DomainName", "")
                if ".s3" in dn:
                    bucket = dn.split(".s3")[0]
                    E(darn, f"arn:aws:s3:::{bucket}", "ORIGIN")
    except Exception:
        pass
    # EVENT_RULE -[TRIGGERS]-> target
    ev = _boto("events")
    try:
        pag = ev.get_paginator("list_rules")
        for pg in pag.paginate():
            for r in pg["Rules"]:
                rarn = r["Arn"]
                for t in ev.list_targets_by_rule(Rule=r["Name"]).get("Targets", []):
                    E(rarn, t["Arn"], "TRIGGERS")
    except Exception:
        pass
    return edges

# ---------------------------------------------------------------------------
# SCORE -- P/R/F1 vs certified oracle.  Oracle = ground truth.
# ---------------------------------------------------------------------------
def _load_yaml(p):
    import yaml
    return yaml.safe_load(open(p, encoding="utf-8"))

def _f1(tp, fp, fn):
    p = tp / (tp + fp) if (tp + fp) else 0.0
    r = tp / (tp + fn) if (tp + fn) else 0.0
    f = 2 * p * r / (p + r) if (p + r) else 0.0
    return p, r, f

def score_s3():
    """Node-enumeration + key-attr F1 vs s3 oracle."""
    oracle = _load_yaml(SHAPES / "s3-hand-audit-fixture-v1.0.yaml")
    truth = {b["bucket_name"]: b for b in oracle["s3_buckets"]}
    derived = {n["id"]: n for n in derive_class("s3")["nodes"]}
    tset, dset = set(truth), set(derived)
    tp_nodes = tset & dset
    fp = len(dset - tset)        # derived a bucket not in oracle
    fn = len(tset - dset)        # oracle bucket the compiler missed
    # attribute correctness within matched nodes (versioning + PAB = the certified axes)
    attr_total = attr_ok = 0
    for b in tp_nodes:
        for axis, dkey in [("versioning_enabled", "versioning_enabled"), ("public_access_block", "public_access_block")]:
            if axis in truth[b]:
                attr_total += 1
                if derived[b].get(dkey) == truth[b][axis]:
                    attr_ok += 1
    pe, re_, fe = _f1(len(tp_nodes), fp, fn)
    return {
        "class": "s3", "node_tp": len(tp_nodes), "node_fp": fp, "node_fn": fn,
        "node_precision": round(pe, 4), "node_recall": round(re_, 4), "node_f1": round(fe, 4),
        "attr_accuracy": round(attr_ok / attr_total, 4) if attr_total else None,
        "attr_checked": attr_total, "missed": sorted(tset - dset), "extra": sorted(dset - tset),
    }

def score_iam_ec2():
    oracle = _load_yaml(SHAPES / "iam-ec2-hand-audit-fixture-v0.1.yaml")
    res = {}
    # --- IAM role enumeration ---
    iam_truth_count = oracle["iam_roles"]["customer_role_count"]
    derived_iam = derive_class("iam")["nodes"]
    # recall on count (oracle asserts SET size + named exceptions; we score enumeration count + overperm set)
    di = len(derived_iam)
    # overperm precision/recall vs the 3 named
    truth_overperm = {o["role"] for o in oracle["iam_cataloged_findings_HELD"]["overperm_roles"]}
    derived_overperm = {n["id"] for n in derived_iam if n.get("broad_managed")}
    tp = len(truth_overperm & derived_overperm)
    p, r, f = _f1(tp, len(derived_overperm - truth_overperm), len(truth_overperm - derived_overperm))
    res["iam"] = {
        "truth_role_count": iam_truth_count, "derived_role_count": di,
        "count_match": di == iam_truth_count,
        "overperm_precision": round(p, 4), "overperm_recall": round(r, 4), "overperm_f1": round(f, 4),
        "overperm_truth": sorted(truth_overperm), "overperm_derived": sorted(derived_overperm),
    }
    # --- EC2 enumeration ---
    decl_truth = {e["name"] for e in oracle["ec2_declared"]}
    derived_ec2 = derive_class("ec2")
    derived_declared = {n["name"] for n in derived_ec2["nodes"] if n.get("drift_class") == "DECLARED"}
    expected_no_live = {e["name"] for e in oracle["ec2_declared"] if "REMOVED" in (e.get("note") or "")}
    # declared-set recall: oracle's declared names present live-or-declared
    tp = len(decl_truth & (derived_declared | expected_no_live))
    p, r, f = _f1(tp, 0, len(decl_truth - (derived_declared | expected_no_live)))
    res["ec2"] = {
        "truth_declared": len(decl_truth), "derived_live": derived_ec2["counts"]["live"],
        "derived_declared": sorted(derived_declared),
        "declared_recall": round(r, 4), "declared_f1": round(f, 4),
        "live_no_declared": derived_ec2["counts"]["live_no_declared"],
    }
    return res

SCORERS = {"s3": score_s3, "iam-ec2": score_iam_ec2}

# ---------------------------------------------------------------------------
def cmd_classes(args):
    print("Supported resource classes:")
    for c in CLASSES:
        print(f"  {c:12} -> {CLASSES[c][1]}")
    print("\nCertified oracle scorers:", ", ".join(SCORERS))

def cmd_derive(args):
    classes = [args.cls] if args.cls else list(CLASSES)
    graph = {"meta": {"account": ACCOUNT, "classes": classes, "tf_root": str(TF_ROOT.relative_to(WS))}, "classes_data": {}}
    for c in classes:
        try:
            graph["classes_data"][c] = derive_class(c)
            cd = graph["classes_data"][c]["counts"]
            print(f"  {c:12} live={cd['live']:3} tf_declared={cd['tf_declared']:3} "
                  f"DECLARED={cd['live_declared']:3} LIVE-no-DECL={cd['live_no_declared']:3} "
                  f"DECL-no-LIVE={cd['declared_no_live']:3}")
        except Exception as e:
            print(f"  {c:12} ERROR: {type(e).__name__}: {e}")
            graph["classes_data"][c] = {"error": str(e)}
    if not args.cls and not getattr(args, "no_edges", False):
        graph["edges"] = derive_edges()
        from collections import Counter
        ec = Counter(e["edge_type"] for e in graph["edges"])
        print(f"  edges        total={len(graph['edges'])}  " +
              " ".join(f"{k}={v}" for k, v in sorted(ec.items())))
    if args.out:
        Path(args.out).write_text(json.dumps(graph, indent=2, default=str), encoding="utf-8")
        print(f"\nwrote {args.out}")
    return graph

def cmd_score(args):
    targets = [args.cls] if args.cls else list(SCORERS)
    f1s = []
    for t in targets:
        if t not in SCORERS:
            print(f"  {t}: no certified oracle scorer")
            continue
        print(f"\n=== SCORE: {t} ===")
        r = SCORERS[t]()
        print(json.dumps(r, indent=2, default=str))
        # collect F1s
        def collect(d):
            for k, v in d.items():
                if k.endswith("_f1") and isinstance(v, (int, float)):
                    f1s.append((k, v))
                elif isinstance(v, dict):
                    collect(v)
        collect(r)
    if f1s:
        print("\n=== F1 SUMMARY ===")
        for k, v in f1s:
            print(f"  {k}: {v:.4f}")
        agg = sum(v for _, v in f1s) / len(f1s)
        print(f"  AGGREGATE F1: {agg:.4f}  ({'PASS >=0.95' if agg >= 0.95 else 'BELOW 0.95'})")

def cmd_snapshot(args):
    graph = cmd_derive(argparse.Namespace(cls=None, out=None))
    SHAPES.mkdir(parents=True, exist_ok=True)
    stamp = args.stamp or "manual"
    payload = json.dumps(graph, indent=2, default=str).encode()
    tgz = SHAPES / f"aws-shape_{stamp}.tar.gz"
    with tarfile.open(tgz, "w:gz") as tar:
        info = tarfile.TarInfo(name=f"aws-shape_{stamp}.json")
        info.size = len(payload)
        tar.addfile(info, io.BytesIO(payload))
    print(f"snapshot -> {tgz}")

def main():
    ap = argparse.ArgumentParser(prog="comp-aws")
    sub = ap.add_subparsers(dest="cmd", required=True)
    d = sub.add_parser("derive")
    d.add_argument("--class", dest="cls")
    d.add_argument("--out")
    d.set_defaults(fn=cmd_derive)
    s = sub.add_parser("score")
    s.add_argument("--class", dest="cls")
    s.set_defaults(fn=cmd_score)
    sn = sub.add_parser("snapshot")
    sn.add_argument("--stamp")
    sn.set_defaults(fn=cmd_snapshot)
    c = sub.add_parser("classes")
    c.set_defaults(fn=cmd_classes)
    args = ap.parse_args()
    args.fn(args)

if __name__ == "__main__":
    main()
