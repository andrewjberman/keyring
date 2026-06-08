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
import glob
import re
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
            mode = r.get("mode")
            # managed = TF owns lifecycle; data = TF-aware reference (a resource
            # created out-of-band but referenced via a data block). CVO's state-
            # union counts BOTH as DECLARED (known to IaC) -- the tf_kind tag
            # preserves the managed-vs-referenced distinction (IAM 2-FN fix).
            if mode not in ("managed", "data"):
                continue
            for inst in r.get("instances", []):
                a = inst.get("attributes", {}) or {}
                resources.append({
                    "type": r["type"], "tf_name": r.get("name"), "module": module,
                    "tf_kind": mode,
                    "arn": a.get("arn"), "id": a.get("id"),
                    "name": a.get("name") or a.get("bucket") or a.get("function_name")
                            or a.get("alarm_name"),
                    "attrs": a,
                })
    _TFSTATE_CACHE["resources"] = resources
    _TFSTATE_CACHE["module_count"] = len({k.split("/")[0] for k in keys})
    return resources

def _hcl_declared(resource_types):
    """sec 1.4 point-3 SECONDARY check: HCL-aware (brace-balanced, NOT line-grep)
    scan of every *.tf for `resource "<type>" "<label>"` blocks, resolving the
    name literal. Catches config-declared resources whose root-module state is
    absent from the bucket (e.g. seeking-alpha) -> would otherwise false-shadow.
    Returns {resolved_name -> provenance}."""
    rts = set(resource_types)
    name_attrs = {"aws_iam_role": "name", "aws_s3_bucket": "bucket",
                  "aws_lambda_function": "function_name", "aws_dynamodb_table": "name",
                  "aws_sns_topic": "name", "aws_sqs_queue": "name",
                  "aws_cloudwatch_metric_alarm": "alarm_name", "aws_secretsmanager_secret": "name",
                  "aws_sfn_state_machine": "name", "aws_sfn_activity": "name"}
    out = {}
    for f in glob.glob(str(TF_ROOT / "**" / "*.tf"), recursive=True):
        try:
            txt = open(f, encoding="utf-8", errors="ignore").read()
        except OSError:
            continue
        module = Path(f).relative_to(TF_ROOT).parts[0]
        for rt in rts:
            for m in re.finditer(r'resource\s+"' + re.escape(rt) + r'"\s+"([^"]+)"\s*\{', txt):
                label = m.group(1)
                # brace-balance to read this block's name attr
                depth = 0
                j = m.end() - 1
                n = len(txt)
                while j < n:
                    if txt[j] == '{':
                        depth += 1
                    elif txt[j] == '}':
                        depth -= 1
                        if depth == 0:
                            break
                    j += 1
                body = txt[m.end():j]
                attr = name_attrs.get(rt, "name")
                nm = re.search(r'\b' + attr + r'\s*=\s*"([^"]+)"', body)
                resolved = nm.group(1) if nm else label
                out[resolved] = {"tf_module": module, "tf_resource": f"{rt}.{label}",
                                 "tf_type": rt, "tf_kind": "hcl-config"}
    return out

def dual_managed():
    """Resources whose ARN is 'managed' in >1 root-module state -- a DUAL-MANAGEMENT
    conflict (both modules' applies fight over the same resource; an attribute can
    ping-pong). The mirror of LIVE-no-DECLARED: not unmanaged, but OVER-managed. A
    structural config-integrity risk NFRA_COMPAWS surfaces (e.g. opal-users-v2 in
    portal-auth + shared-infra). Returns {arn: [modules]} for arns in >1 module."""
    from collections import defaultdict
    by_arn = defaultdict(set)
    for r in _load_all_tfstate():
        if r.get("tf_kind") == "managed" and r.get("arn"):
            by_arn[r["arn"]].add(r["module"])
    return {arn: sorted(m) for arn, m in by_arn.items() if len(m) > 1}

def tf_state_index(resource_types):
    """Build lookup indexes for the given TF resource type(s):
    by ARN, by id, by name. PRIMARY = terraform-state union (managed + data);
    SECONDARY = HCL config (sec 1.4 pt3) for state-missing modules.
    Returns (by_arn, by_id, by_name, declared_managed_list)."""
    if isinstance(resource_types, str):
        resource_types = [resource_types]
    rts = set(resource_types)
    by_arn, by_id, by_name = {}, {}, {}
    declared = []
    for r in _load_all_tfstate():
        if r["type"] not in rts:
            continue
        prov = {"tf_module": r["module"], "tf_resource": f'{r["type"]}.{r["tf_name"]}',
                "tf_type": r["type"], "tf_kind": r.get("tf_kind", "managed")}
        if prov["tf_kind"] == "managed":
            declared.append({"arn": r["arn"], "id": r["id"], "name": r["name"], "provenance": prov})
        if r["arn"]:
            by_arn[r["arn"]] = prov
        if r["id"]:
            by_id[str(r["id"])] = prov
        if r["name"]:
            by_name[r["name"]] = prov
    # SECONDARY: HCL config for resources whose state is absent (state-missing module)
    for nm, prov in _hcl_declared(rts).items():
        if nm not in by_name:
            by_name[nm] = prov
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

def _norm_statements(policy_doc):
    """Normalize a policy document to a comparable statement set (sec 1.5 full set --
    Sid/Effect/Principal/sorted-Action/sorted-Resource/Condition)."""
    stmts = policy_doc.get("Statement", [])
    if isinstance(stmts, dict):
        stmts = [stmts]
    out = []
    for s in stmts:
        def _l(x):
            return sorted(x) if isinstance(x, list) else ([x] if x is not None else [])
        out.append({
            "sid": s.get("Sid"), "effect": s.get("Effect"),
            "principal": s.get("Principal"),
            "action": _l(s.get("Action")), "resource": _l(s.get("Resource")),
            "condition": s.get("Condition"),
        })
    return out

def live_s3_policies():
    """S3_BUCKET_POLICY nodes (separate node per Q2; full normalized statement set
    per sec 1.5 so LIVE-no-DECLARED / removed-statement drift is expressible)."""
    import json as _j
    c = _boto("s3")
    nodes = []
    for b in c.list_buckets().get("Buckets", []):
        name = b["Name"]
        try:
            pol = c.get_bucket_policy(Bucket=name)["Policy"]
        except Exception:
            continue
        doc = _j.loads(pol)
        nodes.append({
            "id": name, "name": name, "type": "S3_BUCKET_POLICY",
            "bucket": name, "statements": _norm_statements(doc),
            "statement_count": len(_norm_statements(doc)),
        })
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
            env = (fn.get("Environment") or {}).get("Variables", {}) or {}
            nodes.append({"id": fn["FunctionName"], "type": "LAMBDA", "arn": fn.get("FunctionArn"),
                          "runtime": fn.get("Runtime"), "handler": fn.get("Handler"),
                          "role": (fn.get("Role") or "").split("/")[-1],
                          "code_sha": fn.get("CodeSha256"), "memory": fn.get("MemorySize"),
                          "timeout": fn.get("Timeout"),
                          "env_keys": sorted(env.keys()),   # KEYS only, never values
                          "layers": sorted((layer.get("Arn") or "").split(":layer:")[-1]
                                           for layer in fn.get("Layers", []))})
    return nodes

def live_eventbridge():
    import json as _j
    nodes = []
    c = _boto("events")
    pag = c.get_paginator("list_rules")
    for pg in pag.paginate():
        for r in pg["Rules"]:
            pat = r.get("EventPattern")
            nodes.append({"id": r["Name"], "type": "EVENT_RULE", "arn": r.get("Arn"),
                          "schedule": r.get("ScheduleExpression"),
                          "state": r.get("State"),
                          "event_pattern": _j.loads(pat) if pat else None,
                          "event_bus": r.get("EventBusName", "default")})
    return nodes

def classify_event_source(rule):
    """sec 3.3 determination: return (source_kind, service_or_api, detail_type, [pinned_resource_arns]).
    The pinned list is EMPTY for non-resource-bound origins (the rule gets an EVENT_SOURCE node);
    for a resource-bound pattern it holds ONE arn PER pinned resource-id (EV-EDGE-1: a pattern pinning
    N ids -> N EMITS_TO edges, the D4 fan-out on the source side). SCHEDULED if no pattern + a schedule."""
    pat = rule.get("event_pattern")
    if not pat:
        return ("SCHEDULED", rule.get("schedule") or "rate", None, [])
    srcs = pat.get("source") or []
    dts = pat.get("detail-type") or []
    detail = pat.get("detail") or {}
    detail_type = dts[0] if isinstance(dts, list) and dts else (dts if isinstance(dts, str) else None)
    # CloudTrail API events
    if any("CloudTrail" in str(d) for d in (dts if isinstance(dts, list) else [dts])):
        api = None
        if isinstance(detail, dict):
            ev = detail.get("eventName") or detail.get("eventSource")
            api = (ev[0] if isinstance(ev, list) else ev) if ev else None
        return ("CLOUDTRAIL_API", api or "api", detail_type, [])
    # resource-pinned (S3 bucket(s) / EC2 instance(s)) -- ALL pinned ids (EV-EDGE-1)
    if isinstance(detail, dict):
        bn = (((detail.get("bucket") or {}).get("name")) if isinstance(detail.get("bucket"), dict) else None)
        if bn:
            blist = bn if isinstance(bn, list) else [bn]
            return ("RESOURCE", "aws.s3", detail_type, [f"arn:aws:s3:::{b}" for b in blist])
        iid = detail.get("instance-id")
        if iid:
            ilist = iid if isinstance(iid, list) else [iid]
            return ("RESOURCE", "aws.ec2", detail_type,
                    [f"arn:aws:ec2:us-east-1:{ACCOUNT}:instance/{i}" for i in ilist])
    # AWS service-scoped (non-pinned) vs CUSTOM
    src = srcs[0] if isinstance(srcs, list) and srcs else (srcs if isinstance(srcs, str) else None)
    if src and str(src).startswith("aws."):
        return ("AWS_SERVICE", src, detail_type, [])
    return ("CUSTOM", src or "custom", detail_type, [])

def live_sns():
    nodes = []
    c = _boto("sns")
    for t in c.list_topics().get("Topics", []):
        arn = t["TopicArn"]
        name = arn.split(":")[-1]
        node = {"id": name, "type": "SNS_TOPIC", "arn": arn}
        try:
            attrs = c.get_topic_attributes(TopicArn=arn)["Attributes"]
            node["kms_encrypted"] = bool(attrs.get("KmsMasterKeyId"))
            node["kms_key_arn"] = attrs.get("KmsMasterKeyId")
            node["subscription_count"] = int(attrs.get("SubscriptionsConfirmed", 0))
        except Exception:
            node["kms_encrypted"] = None
        try:
            subs = c.list_subscriptions_by_topic(TopicArn=arn).get("Subscriptions", [])
            node["subscriptions"] = sorted(f'{s["Protocol"]}:{s["Endpoint"]}' for s in subs)
        except Exception:
            node["subscriptions"] = []
        nodes.append(node)
    return nodes

def live_sqs():
    nodes = []
    c = _boto("sqs")
    for url in c.list_queues().get("QueueUrls", []):
        name = url.split("/")[-1]
        node = {"id": name, "type": "SQS_QUEUE"}
        try:
            a = c.get_queue_attributes(QueueUrl=url, AttributeNames=["All"])["Attributes"]
            node["arn"] = a.get("QueueArn")
            node["encrypted"] = bool(a.get("KmsMasterKeyId")) or a.get("SqsManagedSseEnabled") == "true"
            node["kms_key_arn"] = a.get("KmsMasterKeyId")
            node["fifo"] = name.endswith(".fifo")
            node["visibility_timeout"] = a.get("VisibilityTimeout")
            import json as _j
            rd = a.get("RedrivePolicy")
            node["redrive_dlq_arn"] = (_j.loads(rd).get("deadLetterTargetArn") if rd else None)
        except Exception:
            node["encrypted"] = None
        nodes.append(node)
    return nodes

def live_dynamodb():
    nodes = []
    c = _boto("dynamodb")
    pag = c.get_paginator("list_tables")
    for pg in pag.paginate():
        for t in pg["TableNames"]:
            node = {"id": t, "type": "DYNAMODB_TABLE"}
            try:
                d = c.describe_table(TableName=t)["Table"]
                node["arn"] = d.get("TableArn")
                node["sse_type"] = d.get("SSEDescription", {}).get("SSEType")
                node["kms_key_arn"] = d.get("SSEDescription", {}).get("KMSMasterKeyArn")
                node["billing_mode"] = d.get("BillingModeSummary", {}).get("BillingMode")
                node["deletion_protection"] = d.get("DeletionProtectionEnabled")
                node["gsi"] = sorted(g["IndexName"] for g in d.get("GlobalSecondaryIndexes", []))
                node["stream_arn"] = d.get("LatestStreamArn")
            except Exception:
                pass
            try:
                node["pitr_enabled"] = c.describe_continuous_backups(TableName=t)[
                    "ContinuousBackupsDescription"]["PointInTimeRecoveryDescription"][
                    "PointInTimeRecoveryStatus"] == "ENABLED"
            except Exception:
                node["pitr_enabled"] = None
            nodes.append(node)
    return nodes

def live_cloudfront():
    nodes = []
    c = _boto("cloudfront")
    try:
        dl = c.list_distributions().get("DistributionList", {}).get("Items", [])
    except Exception:
        dl = []
    for d in dl:
        behaviors = []
        dcb = d.get("DefaultCacheBehavior") or {}
        if dcb:
            behaviors.append({"path": "default", "target_origin": dcb.get("TargetOriginId")})
        for cb in (d.get("CacheBehaviors", {}) or {}).get("Items", []):
            behaviors.append({"path": cb.get("PathPattern"), "target_origin": cb.get("TargetOriginId")})
        nodes.append({"id": d["Id"], "type": "CLOUDFRONT_DISTRIBUTION",
                      "arn": f"arn:aws:cloudfront::{ACCOUNT}:distribution/{d['Id']}",
                      "domain": d.get("DomainName"), "enabled": d.get("Enabled"),
                      "aliases": sorted(d.get("Aliases", {}).get("Items", [])),
                      "cache_behaviors": behaviors,
                      "origins": sorted(o.get("DomainName", "") for o in (d.get("Origins", {}) or {}).get("Items", []))})
    return nodes

def live_secrets():
    nodes = []
    c = _boto("secretsmanager")
    pag = c.get_paginator("list_secrets")
    for pg in pag.paginate():
        for s in pg["SecretList"]:
            nodes.append({"id": s["Name"], "name": s["Name"], "arn": s.get("ARN"),
                          "type": "SECRET", "kms": bool(s.get("KmsKeyId")),
                          "kms_key_arn": s.get("KmsKeyId"),
                          "rotation_enabled": s.get("RotationEnabled", False)})
    return nodes

def live_kms():
    nodes = []
    c = _boto("kms")
    pag = c.get_paginator("list_keys")
    for pg in pag.paginate():
        for k in pg["Keys"]:
            aws_managed = False
            try:
                meta = c.describe_key(KeyId=k["KeyId"])["KeyMetadata"]
                aws_managed = meta.get("KeyManager") == "AWS"
                aliases = sorted(a["AliasName"] for a in c.list_aliases(KeyId=k["KeyId"]).get("Aliases", []))
            except Exception:
                aliases = []
            node = {"id": k["KeyId"], "type": "KMS_KEY", "arn": k.get("KeyArn"), "aliases": aliases}
            if aws_managed:
                # AWS-service-owned key (alias/aws/*) -> AWS_MANAGED node (KMS-SCHEMA-1,
                # schema v0.3) so ENCRYPTS_WITH edges to it terminate cleanly. No policy/
                # rotation pull (not a customer resource); the _aws_managed flag overrides
                # the tf-join in derive_class -> provenance=AWS_MANAGED.
                node["_aws_managed"] = True
                nodes.append(node)
                continue
            try:
                node["rotation_enabled"] = c.get_key_rotation_status(KeyId=k["KeyId"]).get("KeyRotationEnabled")
            except Exception:
                node["rotation_enabled"] = None
            try:
                import json as _j
                pol = _j.loads(c.get_key_policy(KeyId=k["KeyId"], PolicyName="default")["Policy"])
                node["key_policy_statements"] = _norm_statements(pol)
            except Exception:
                node["key_policy_statements"] = None
            nodes.append(node)
    return nodes

def live_log_groups():
    nodes = []
    c = _boto("logs")
    pag = c.get_paginator("describe_log_groups")
    for pg in pag.paginate():
        for lg in pg.get("logGroups", []):
            nodes.append({"id": lg["logGroupName"], "name": lg["logGroupName"],
                          "arn": (lg.get("arn") or "").rstrip(":*"), "type": "LOG_GROUP",
                          "retention_days": lg.get("retentionInDays"),
                          "kms_key_arn": lg.get("kmsKeyId")})
    return nodes

def live_cloudwatch_alarms():
    nodes = []
    c = _boto("cloudwatch")
    pag = c.get_paginator("describe_alarms")
    for pg in pag.paginate():
        for a in pg.get("MetricAlarms", []):
            nodes.append({"id": a["AlarmName"], "type": "CW_ALARM", "arn": a.get("AlarmArn"),
                          "state": a.get("StateValue"),
                          "metric_namespace": a.get("Namespace"), "metric_name": a.get("MetricName"),
                          "threshold": a.get("Threshold"), "comparison": a.get("ComparisonOperator"),
                          "treat_missing_data": a.get("TreatMissingData"),
                          "alarm_actions": sorted(a.get("AlarmActions", [])),
                          "dimensions": {d["Name"]: d["Value"] for d in a.get("Dimensions", [])}})
    return nodes

def live_stepfunctions():
    import hashlib as _hl
    nodes = []
    c = _boto("stepfunctions")
    pag = c.get_paginator("list_state_machines")
    for pg in pag.paginate():
        for sm in pg.get("stateMachines", []):
            try:
                d = c.describe_state_machine(stateMachineArn=sm["stateMachineArn"])
                defn_raw = d.get("definition", "{}")
                defn_hash = _hl.sha256(
                    json.dumps(json.loads(defn_raw), sort_keys=True).encode()
                ).hexdigest()[:16]
                log_cfg = d.get("loggingConfiguration") or {}
                nodes.append({
                    "id": d["name"],
                    "name": d["name"],
                    "type": "STATE_MACHINE",
                    "arn": d["stateMachineArn"],
                    "machine_type": d.get("type", "STANDARD"),
                    "status": d.get("status", "ACTIVE"),
                    "definition_hash": defn_hash,
                    "role_arn": d.get("roleArn", ""),
                    "logging_level": log_cfg.get("level", "OFF"),
                    "tracing_enabled": bool(
                        (d.get("tracingConfiguration") or {}).get("enabled", False)
                    ),
                })
            except Exception:
                pass
    return nodes

def live_sfn_activities():
    nodes = []
    c = _boto("stepfunctions")
    pag = c.get_paginator("list_activities")
    for pg in pag.paginate():
        for a in pg.get("activities", []):
            nodes.append({
                "id": a["name"],
                "name": a["name"],
                "type": "ACTIVITY",
                "arn": a["activityArn"],
            })
    return nodes

def _walk_asl_states(states):
    """Recursively yield (state_name, state_dict) for all ASL states at any nesting depth."""
    for sname, state in states.items():
        yield sname, state
        for branch in state.get("Branches", []):         # Parallel
            yield from _walk_asl_states(branch.get("States", {}))
        ip = state.get("ItemProcessor") or {}             # Map (new-style)
        if ip.get("States"):
            yield from _walk_asl_states(ip["States"])
        it = state.get("Iterator") or {}                  # Map (legacy-style)
        if it.get("States"):
            yield from _walk_asl_states(it["States"])

def _sfn_task_invokes(definition_str):
    """Return list of (state_name, target_arn) for every Task state in an ASL JSON string.
    Handles direct arn:aws: Resource ARNs and arn:aws:states::: SDK integration patterns.
    Recurses into Parallel.Branches, Map.ItemProcessor, Map.Iterator at all depths."""
    try:
        defn = json.loads(definition_str)
    except Exception:
        return []
    result = []
    for sname, state in _walk_asl_states(defn.get("States", {})):
        if state.get("Type") != "Task":
            continue
        res = state.get("Resource", "")
        tgt_arn = None
        if res.startswith("arn:aws:states:::"):
            params = state.get("Parameters") or {}
            fn = params.get("FunctionName", "") or params.get("FunctionArn", "")
            if isinstance(fn, str) and fn.endswith(".$"):
                fn = ""  # runtime reference -- not statically resolvable
            if fn and fn.startswith("arn:aws:"):
                tgt_arn = fn
            elif fn:
                tgt_arn = f"arn:aws:lambda:us-east-1:{ACCOUNT}:function:{fn}"
        elif res.startswith("arn:aws:"):
            tgt_arn = res
        if tgt_arn:
            result.append((sname, tgt_arn))
    return result

# class -> (live_fn, [tf_resource_types that materialize this class's nodes])
CLASSES = {
    "s3":          (live_s3,                ["aws_s3_bucket"]),
    "s3_policy":   (live_s3_policies,       ["aws_s3_bucket_policy"]),
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
    "logs":        (live_log_groups,        ["aws_cloudwatch_log_group"]),
    "stepfunctions": (live_stepfunctions,   ["aws_sfn_state_machine"]),
    "sfn_activity":  (live_sfn_activities,  ["aws_sfn_activity"]),
}

def _node_arn(cls, node):
    """Canonical ARN for a live node (the sec 1 matching key). Prefer an API-given
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
        "stepfunctions": f"arn:aws:states:us-east-1:{ACCOUNT}:stateMachine:{i}",
        "sfn_activity":  f"arn:aws:states:us-east-1:{ACCOUNT}:activity:{i}",
    }.get(cls, i)

def derive_class(cls):
    live_fn, tf_types = CLASSES[cls]
    live = live_fn()
    by_arn, by_id, by_name, declared = tf_state_index(tf_types)
    matched_decl = set()
    _dm = dual_managed()   # sec1.3: ARNs managed in >1 root-module state
    for n in live:
        arn = _node_arn(cls, n)
        n["arn"] = arn
        if n.get("_aws_managed"):
            # AWS-service-owned (KMS-SCHEMA-1, schema v0.3): not a tf-join candidate
            n["drift_class"] = "AWS_MANAGED"
            n["provenance"] = {"tf_kind": "aws_managed"}
            n["tf_managed"] = False
            n["owner_pipeline"] = "aws"
        else:
            # ARN-canonical join, with id/name fallback (CVO sec 1 matching key).
            # name fallback uses (name or id) because some classes (IAM) set the
            # universal `name` prop only AFTER the join -- id IS the resolved name there.
            join_name = n.get("name") or n.get("id")
            prov = by_arn.get(arn) or by_id.get(str(n["id"])) or (by_name.get(join_name) if join_name else None)
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
            if arn in _dm:   # sec1.3 override: over-declared (>1 state) -> latent apply-conflict
                n["drift_class"] = "MULTI_STATE_MANAGED"
                n["multi_state_modules"] = _dm[arn]
        # sec 1.1 universal node properties
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
# EDGES -- typed relationships (PRD sec 3 / CVO schema). Derived from live AWS,
# discovery-based (no hardcoded edge lists). Each edge: (src_arn, dst_arn, type).
# ---------------------------------------------------------------------------
def _classify_principal(p):
    """sec3.2a: map a policy principal to a typed GRANTS target.
    Returns (target_id, node_type, sub_type, finding_class|None). Deterministic.
    our-account role/user -> existing IAM_ROLE / IAM_USER node (real arn);
    *.amazonaws.com + AWS pseudo-account (cloudfront OAI) -> SERVICE_PRINCIPAL (AWS_MANAGED);
    other-account -> EXTERNAL_PRINCIPAL{CROSS_ACCOUNT} (finding); SAML/OIDC/Cognito -> {FEDERATED};
    '*'/anonymous -> {PUBLIC} (finding). PUBLIC + CROSS_ACCOUNT surface, never wildcard-hidden."""
    if p in ("*", "arn:aws:iam::*:root"):
        return "external-principal::public", "EXTERNAL_PRINCIPAL", "PUBLIC", "PUBLIC_GRANT"
    if p.endswith(".amazonaws.com"):
        return f"service-principal::{p}", "SERVICE_PRINCIPAL", p.split(".")[0], None
    # AWS-service-owned pseudo-account identities (CloudFront OAI, etc.) -> SERVICE_PRINCIPAL,
    # NOT a cross-account finding (the OAI is the intended S3-origin lockdown).
    if p.startswith("arn:aws:iam::cloudfront:") or p.startswith("arn:aws:iam::cloudtrail:"):
        oid = p.split()[-1] if " " in p else p.split("/")[-1]
        return f"service-principal::oai::{oid}", "SERVICE_PRINCIPAL", "OAI", None
    if p.startswith(f"arn:aws:iam::{ACCOUNT}:role/"):
        return p, "IAM_ROLE", None, None          # our-account role -> existing node
    if p.startswith(f"arn:aws:iam::{ACCOUNT}:user/"):
        return p, "IAM_USER", None, None           # our-account user
    if p.startswith(f"arn:aws:iam::{ACCOUNT}:"):    # our-account root/other -> our principal
        return f"iam-user::{p.split(':')[-1]}", "IAM_USER", "ACCOUNT", None
    if ":saml-provider/" in p or ":oidc-provider/" in p or "cognito" in p.lower():
        return f"external-principal::federated::{p.split('/')[-1]}", "EXTERNAL_PRINCIPAL", "FEDERATED", None
    if p.startswith("arn:aws:iam::"):              # different real account -> cross-account finding
        acct = p.split(":")[4] if len(p.split(":")) > 4 else "unknown"
        return f"external-principal::cross-account::{acct}", "EXTERNAL_PRINCIPAL", "CROSS_ACCOUNT", "CROSS_ACCOUNT_GRANT"
    return f"external-principal::other::{p}", "EXTERNAL_PRINCIPAL", "OTHER", None

def derive_edges():
    edges = []
    def E(s, d, t, **extra):
        if s and d:
            edges.append({"source": s, "target": d, "edge_type": t, **extra})

    # KMS ref resolver: a kms_key_arn property may be a full ARN, a bare key-id (SNS
    # KmsMasterKeyId), or an alias -> resolve to the KMS_KEY node ARN so ENCRYPTS_WITH
    # terminates (0-dangling); unresolvable -> wildcard.
    _kn = live_kms()
    _kms_arns = {k["arn"] for k in _kn if k.get("arn")}
    _kms_by_id = {k["id"]: k["arn"] for k in _kn if k.get("arn")}
    _kms_by_alias = {al: k["arn"] for k in _kn for al in k.get("aliases", []) if k.get("arn")}

    def _enc(src, ref):
        if not (src and ref):
            return
        tgt = (ref if ref in _kms_arns else _kms_by_id.get(ref) or _kms_by_alias.get(ref))
        if tgt:
            E(src, tgt, "ENCRYPTS_WITH")
        else:
            E(src, ref, "ENCRYPTS_WITH", wildcard=True)

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
            dlq = (cfg.get("DeadLetterConfig") or {}).get("TargetArn")
            if dlq:  # lambda async DLQ (SQS or SNS) -- the producer->dlq linkage (SQS-EDGE-GAP)
                E(farn, dlq, "DEAD_LETTERS_TO")
        except Exception:
            pass
    # event-source-mapping OnFailure destinations -> DLQ
    try:
        for esm in lc.list_event_source_mappings().get("EventSourceMappings", []):
            onf = ((esm.get("DestinationConfig") or {}).get("OnFailure") or {}).get("Destination")
            if onf and esm.get("FunctionArn"):
                E(esm["FunctionArn"], onf, "DEAD_LETTERS_TO")
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
    # S3_BUCKET -[HAS_POLICY]-> S3_BUCKET_POLICY -[GRANTS]-> principal
    for p in live_s3_policies():
        barn = f"arn:aws:s3:::{p['bucket']}"
        parn = f"{barn}#policy"
        E(barn, parn, "HAS_POLICY")
        seen_pr = set()
        for st in p["statements"]:
            pr = st.get("principal")
            prkeys = []
            if isinstance(pr, dict):
                for v in pr.values():
                    prkeys += v if isinstance(v, list) else [v]
            elif isinstance(pr, str):
                prkeys = [pr]
            for pk in prkeys:
                if pk and pk not in seen_pr:
                    seen_pr.add(pk)
                    # sec3.2a: GRANTS terminates on a TYPED principal node (IAM_ROLE/USER |
                    # SERVICE_PRINCIPAL | EXTERNAL_PRINCIPAL). PUBLIC/CROSS_ACCOUNT surface as
                    # typed finding nodes -- NEVER wildcard-hidden (the grant IS the finding).
                    tgt, _pt, _sub, _find = _classify_principal(pk)
                    extra = {"effect": st.get("effect")}
                    if _find:
                        extra["finding_class"] = _find
                        extra["conditioned"] = bool(st.get("condition"))
                    E(parn, tgt, "GRANTS", **extra)
    # CLOUDFRONT -[ORIGIN]-> S3
    cf = _boto("cloudfront")
    try:
        for d in cf.list_distributions().get("DistributionList", {}).get("Items", []):
            darn = f"arn:aws:cloudfront::{ACCOUNT}:distribution/{d['Id']}"
            for o in d.get("Origins", {}).get("Items", []):
                dn = o.get("DomainName", "")
                if ".s3" in dn:
                    bucket = dn.split(".s3")[0]
                    barn = f"arn:aws:s3:::{bucket}"
                    E(darn, barn, "ORIGIN")
                    # origin-access lockdown (sec1.2: USES_OAC/USES_OAI -> the S3 origin bucket)
                    oac = o.get("OriginAccessControlId")
                    if oac:
                        E(darn, barn, "USES_OAC", oac_id=oac)
                    oai = (o.get("S3OriginConfig") or {}).get("OriginAccessIdentity")
                    if oai:
                        E(darn, barn, "USES_OAI", oai=oai.split("/")[-1])
    except Exception:
        pass
    # EVENT_RULE -[TRIGGERS]-> target  +  {resource|EVENT_SOURCE} -[EMITS_TO]-> EVENT_RULE (sec 3.3)
    ev = _boto("events")
    try:
        for r in live_eventbridge():
            rarn = r.get("arn")
            # EMITS_TO (origin)
            kind, svc, dt, pinned = classify_event_source(r)
            if pinned:  # one EMITS_TO per pinned resource-id (EV-EDGE-1 D4 source-side fan-out)
                for parn in pinned:
                    E(parn, rarn, "EMITS_TO")
            else:
                es_arn = f"event-source::{kind}::{svc}"
                E(es_arn, rarn, "EMITS_TO")
            # TRIGGERS (targets)
            try:
                for t in ev.list_targets_by_rule(Rule=r["id"]).get("Targets", []):
                    E(rarn, t["Arn"], "TRIGGERS")
                    dlq = (t.get("DeadLetterConfig") or {}).get("Arn")
                    if dlq:  # EventBridge target failure DLQ
                        E(rarn, dlq, "DEAD_LETTERS_TO")
            except Exception:
                pass
    except Exception:
        pass
    # Wave-2 edges derivable from enriched node properties (deterministic)
    # CW_ALARM -[NOTIFIES]-> SNS_TOPIC + -[MONITORS]-> metric-source resource (from Dimensions)
    _res_set = set()
    _res_set |= {f"arn:aws:lambda:us-east-1:{ACCOUNT}:function:{x['id']}" for x in live_lambda()}
    _res_set |= {x["arn"] for x in live_dynamodb() if x.get("arn")}
    _res_set |= {_node_arn("ec2", x) for x in live_ec2()}
    _res_set |= {x["arn"] for x in live_sqs() if x.get("arn")}
    _res_set |= {x["arn"] for x in live_sns() if x.get("arn")}
    _res_set |= {f"arn:aws:s3:::{x['id']}" for x in live_s3()}
    _res_set |= {x["arn"] for x in live_log_groups() if x.get("arn")}
    _res_set |= {x["arn"] for x in live_cloudfront() if x.get("arn")}

    def _dim_arn(name, val):
        return {
            "FunctionName": f"arn:aws:lambda:us-east-1:{ACCOUNT}:function:{val}",
            "TableName": f"arn:aws:dynamodb:us-east-1:{ACCOUNT}:table/{val}",
            "InstanceId": f"arn:aws:ec2:us-east-1:{ACCOUNT}:instance/{val}",
            "QueueName": f"arn:aws:sqs:us-east-1:{ACCOUNT}:{val}",
            "TopicName": f"arn:aws:sns:us-east-1:{ACCOUNT}:{val}",
            "BucketName": f"arn:aws:s3:::{val}",
            "LogGroupName": f"arn:aws:logs:us-east-1:{ACCOUNT}:log-group:{val}",
            "DistributionId": f"arn:aws:cloudfront::{ACCOUNT}:distribution/{val}",
        }.get(name)

    for n in live_cloudwatch_alarms():
        aarn = n.get("arn")
        for act in n.get("alarm_actions", []):
            if ":sns:" in act:
                E(aarn, act, "NOTIFIES")
        for dn, dv in (n.get("dimensions") or {}).items():
            ra = _dim_arn(dn, dv)
            if ra and ra in _res_set:  # resolve to a live resource node (custom-metric/deleted -> skip)
                E(aarn, ra, "MONITORS", dimension=dn)
    # SQS -[DEAD_LETTERS_TO]-> SQS ; {class} -[ENCRYPTS_WITH]-> KMS
    for n in live_sqs():
        if n.get("redrive_dlq_arn"):
            E(n.get("arn"), n["redrive_dlq_arn"], "DEAD_LETTERS_TO")
        if n.get("kms_key_arn"):
            _enc(n.get("arn"), n["kms_key_arn"])
    for n in live_sns():
        if n.get("kms_key_arn"):
            _enc(n.get("arn"), n["kms_key_arn"])
        for sub in n.get("subscriptions", []):
            proto, _, endpoint = sub.partition(":")
            if proto in ("lambda", "sqs") and endpoint.startswith("arn:"):
                # intra-account -> resolve to the actual lambda/sqs node (0-dangling)
                E(n.get("arn"), endpoint, "SUBSCRIBES", protocol=proto)
            else:
                # email/https/http/sms -> typed EXTERNAL_ENDPOINT{EMAIL|HTTPS|SMS} node (sec3.2a)
                E(n.get("arn"), f"external-endpoint::{proto}::{endpoint}", "SUBSCRIBES", protocol=proto)
    for n in live_dynamodb():
        if n.get("kms_key_arn"):
            _enc(n.get("arn"), n["kms_key_arn"])
    for n in live_secrets():
        if n.get("kms_key_arn"):
            _enc(n.get("arn"), n["kms_key_arn"])
    # STATE_MACHINE -[ASSUMES]-> IAM_ROLE ; -[INVOKES]-> targets ; -[LOGS_TO]-> LOG_GROUP
    # {LAMBDA} -[TRIGGERS]-> STATE_MACHINE (env var scan; EB TRIGGERS already derived above)
    try:
        sfnc = _boto("stepfunctions")
        _sfn_nodes = live_stepfunctions()
        _sm_arns = {sm["arn"] for sm in _sfn_nodes}
        for sm in _sfn_nodes:
            smarn = sm["arn"]
            if sm.get("role_arn"):
                E(smarn, sm["role_arn"], "ASSUMES")
            try:
                detail = sfnc.describe_state_machine(stateMachineArn=smarn)
                for sname, tgt_arn in _sfn_task_invokes(detail.get("definition", "{}")):
                    E(smarn, tgt_arn, "INVOKES", state_name=sname)
                log_cfg = detail.get("loggingConfiguration") or {}
                for dest in log_cfg.get("destinations", []):
                    lg_arn = (dest.get("cloudWatchLogsLogGroup") or {}).get("logGroupArn", "")
                    if lg_arn:
                        E(smarn, lg_arn.rstrip(":*"), "LOGS_TO")
            except Exception:
                pass
        if _sm_arns:
            for n in live_lambda():
                farn = _node_arn("lambda", n)
                try:
                    cfg = lc.get_function_configuration(FunctionName=n["id"])
                    env = (cfg.get("Environment") or {}).get("Variables", {}) or {}
                    for k, v in env.items():
                        if isinstance(v, str) and v in _sm_arns:
                            E(farn, v, "TRIGGERS", via=k)
                except Exception:
                    pass
    except Exception:
        pass
    return edges

# action-prefix -> (verb, target_node_kind) for the derived data-access edge layer
# (schema sec3.x: derived from role GRANTS; "intersect actual boto3 calls" is the
# over-perm refinement, captured as edge provenance, not a gate).
_ACTION_VERB = [
    ("s3:get", "READS", "s3"), ("s3:list", "READS", "s3"), ("s3:head", "READS", "s3"),
    ("s3:put", "WRITES", "s3"), ("s3:delete", "WRITES", "s3"), ("s3:*", "WRITES", "s3"),
    ("dynamodb:get", "READS", "dynamodb"), ("dynamodb:query", "READS", "dynamodb"),
    ("dynamodb:scan", "READS", "dynamodb"), ("dynamodb:batchget", "READS", "dynamodb"),
    ("dynamodb:put", "WRITES", "dynamodb"), ("dynamodb:update", "WRITES", "dynamodb"),
    ("dynamodb:delete", "WRITES", "dynamodb"), ("dynamodb:batchwrite", "WRITES", "dynamodb"),
    ("dynamodb:*", "WRITES", "dynamodb"),
    ("secretsmanager:getsecretvalue", "READS_SECRET", "secret"),
    ("sns:publish", "PUBLISHES_TO", "sns"),
    ("sqs:sendmessage", "SENDS_TO", "sqs"),
    ("kms:decrypt", "ENCRYPTS_WITH", "kms"), ("kms:encrypt", "ENCRYPTS_WITH", "kms"),
    ("kms:generatedatakey", "ENCRYPTS_WITH", "kms"), ("kms:creategrant", "ENCRYPTS_WITH", "kms"),
    ("logs:putlogevents", "LOGS_TO", "logs"), ("logs:createlogstream", "LOGS_TO", "logs"),
]

def _verbs_for_action(action):
    """Return ALL data-access (verb, kind) a single action grants. Service-wildcards
    (s3:*, dynamodb:*) + full admin (*) grant BOTH read+write capability -> emit both
    (the FullAccess/admin blast-radius is the high-value capability edge set)."""
    a = action.lower()
    out = []
    if a in ("*", "s3:*"):
        out += [("READS", "s3"), ("WRITES", "s3")]
    if a in ("*", "dynamodb:*"):
        out += [("READS", "dynamodb"), ("WRITES", "dynamodb")]
    if a == "*":
        out += [("READS_SECRET", "secret"), ("PUBLISHES_TO", "sns"),
                ("SENDS_TO", "sqs"), ("ENCRYPTS_WITH", "kms"), ("LOGS_TO", "logs")]
    if out:
        return out
    for pfx, verb, kind in _ACTION_VERB:
        if a.startswith(pfx):
            return [(verb, kind)]
    return []

def _res_kind(res):
    """The service-kind of a resource ARN (for the EDGE-CROSSWIRE-1 kind-gate)."""
    if res.startswith("arn:aws:s3:::"):
        return "s3"
    if ":dynamodb:" in res:
        return "dynamodb"
    if ":secretsmanager:" in res:
        return "secret"
    if ":sns:" in res:
        return "sns"
    if ":sqs:" in res:
        return "sqs"
    if ":kms:" in res:
        return "kms"
    if ":logs:" in res or ":log-group:" in res:
        return "logs"
    return None

def derive_data_access_edges():
    """sec3.x DERIVED edge layer (EDGE-GAP-DATA): project each IAM role's GRANTS
    (inline-policy statements) onto typed data-access edges, sourced from the
    role's compute CONSUMERS (Lambdas + EC2 that ASSUME it). Concrete-ARN targets
    only; Resource='*' grants are recorded as an edge property (wildcard=True) on a
    GRANTS-class edge rather than fan-out to every resource. Discovery-based."""
    iamc = _boto("iam")
    edges = []
    _mp_cache = {}  # managed-policy arn -> normalized statements (a policy attaches to many roles)

    def _managed_stmts(parn):
        if parn not in _mp_cache:
            try:
                ver = iamc.get_policy(PolicyArn=parn)["Policy"]["DefaultVersionId"]
                doc = iamc.get_policy_version(PolicyArn=parn, VersionId=ver)["PolicyVersion"]["Document"]
                _mp_cache[parn] = _norm_statements(doc if isinstance(doc, dict) else {})
            except Exception:
                _mp_cache[parn] = []
        return _mp_cache[parn]

    # role_arn -> [(verb, target_arn|None, wildcard, action)]
    grants = {}
    for n in live_iam_roles():
        rn = n["id"]
        rarn = n["arn"]
        stmts = []
        try:  # INLINE policy grants
            for pn in iamc.list_role_policies(RoleName=rn).get("PolicyNames", []):
                doc = iamc.get_role_policy(RoleName=rn, PolicyName=pn).get("PolicyDocument", {})
                stmts += _norm_statements(doc if isinstance(doc, dict) else {})
        except Exception:
            pass
        try:  # MANAGED policy grants (incl AWS-managed *FullAccess = service:* on * -> wildcard edges; DATA-EDGE-COVERAGE)
            for ap in iamc.list_attached_role_policies(RoleName=rn).get("AttachedPolicies", []):
                stmts += _managed_stmts(ap["PolicyArn"])
        except Exception:
            pass
        glist = []
        for s in stmts:
            if s.get("effect") != "Allow":
                continue
            for act in s.get("action", []):
                for verb, kind in _verbs_for_action(act):
                    for res in (s.get("resource") or []):
                        if res == "*" or res.strip() == "*":
                            glist.append((verb, None, True, act))
                        elif _res_kind(res) == kind:
                            # kind-gate (EDGE-CROSSWIRE-1): only pair a verb with a resource of
                            # its OWN service. A multi-service statement (e.g. s3:* +
                            # secretsmanager:GetSecretValue on [secret-arn, s3-arn]) otherwise
                            # cross-wires READS_SECRET->s3 / READS->secret. The mismatched
                            # (verb,res) belongs to the sibling action -> drop (not wildcard).
                            glist.append((verb, res, False, act))
        if glist:
            grants[rarn] = glist
    # consumers: compute nodes that ASSUME each role
    consumers = {}  # role_arn -> [compute_arn]
    for ln in live_lambda():
        if ln.get("role"):
            consumers.setdefault(f"arn:aws:iam::{ACCOUNT}:role/{ln['role']}", []).append(ln["arn"])
    prof_role = {}
    for e in live_ec2():
        prof = e.get("instance_profile")
        if not prof:
            continue
        if prof not in prof_role:
            try:
                r = iamc.get_instance_profile(InstanceProfileName=prof)
                prof_role[prof] = [x["Arn"] for x in r["InstanceProfile"]["Roles"]]
            except Exception:
                prof_role[prof] = []
        for rarn in prof_role[prof]:
            consumers.setdefault(rarn, []).append(_node_arn("ec2", e))
    # node-ARN sets for grant->node resolution (DATA-EDGE-DANGLING fix): a grant to a
    # sub-resource / object-path / name-pattern resolves to the PARENT node, or -- if no
    # concrete node matches -- becomes a wildcard=true edge. NEVER a concrete non-node ARN.
    sets = {
        "s3": {f"arn:aws:s3:::{n['id']}" for n in live_s3()},
        "dynamodb": {n["arn"] for n in live_dynamodb() if n.get("arn")},
        "secret": {n["arn"] for n in live_secrets() if n.get("arn")},
        "sns": {n["arn"] for n in live_sns() if n.get("arn")},
        "kms": {n["arn"] for n in live_kms() if n.get("arn")},
        "logs": {n["arn"] for n in live_log_groups() if n.get("arn")},
    }

    def _resolve(res):
        """grant resource-ARN -> (node_arn, is_wildcard). Parent-strip + prefix/pattern match."""
        if res.startswith("arn:aws:s3:::"):
            base = "arn:aws:s3:::" + res.split(":::", 1)[1].split("/")[0]
            return (base, False) if base in sets["s3"] else (None, True)
        if ":dynamodb:" in res and ":table/" in res:
            base = res.split("/index/")[0].split("/stream/")[0]
            return (base, False) if base in sets["dynamodb"] else (None, True)
        if ":secretsmanager:" in res:
            stem = res.rstrip("*").rstrip("-")
            for sarn in sets["secret"]:
                if sarn == res or sarn.startswith(stem):
                    return sarn, False
            return None, True
        if ":sns:" in res:
            return (res, False) if res in sets["sns"] else (None, True)
        if ":logs:" in res or ":log-group:" in res:
            base = res.rstrip(":*").rstrip("*")
            m = [lg for lg in sets["logs"] if lg.startswith(base) or base.startswith(lg)]
            return (m[0], False) if len(m) == 1 else (None, True)
        if ":kms:" in res:
            return (res, False) if res in sets["kms"] else (None, True)
        for s in sets.values():
            if res in s:
                return res, False
        return None, True

    # emit consumer -[verb]-> resolved-node (or wildcard) ; dedupe
    seen = set()
    for rarn, glist in grants.items():
        for carn in consumers.get(rarn, []):
            for verb, target, wild, act in glist:
                if wild:
                    tgt, is_wild = f"*:{verb.lower()}", True
                else:
                    node, w = _resolve(target)
                    tgt, is_wild = (f"*:{verb.lower()}", True) if w else (node, False)
                key = (carn, verb, tgt)
                if key in seen:
                    continue
                seen.add(key)
                e = {"source": carn, "target": tgt, "edge_type": verb,
                     "via_role": rarn.split("/")[-1], "semantic": "capability"}
                if is_wild:
                    e["wildcard"] = True
                edges.append(e)
    return edges

def derive_event_sources():
    """EVENT_SOURCE nodes (sec 3.3 EV-SCHEMA-GAP-1) -- one per distinct
    (source_kind, service_or_api) origin that is not a pinned resource."""
    seen = {}
    for r in live_eventbridge():
        kind, svc, dt, pinned = classify_event_source(r)
        if pinned:
            continue
        key = f"event-source::{kind}::{svc}"
        if key not in seen:
            seen[key] = {"id": key, "arn": key, "name": svc, "type": "EVENT_SOURCE",
                         "source_kind": kind, "service_or_api": svc, "detail_type": dt,
                         "drift_class": "LIVE-no-DECLARED", "tf_managed": False,
                         "owner_pipeline": None, "provenance": None}
    return list(seen.values())

def derive_aux_nodes(edges):
    """Emit the structural-edge TARGET node classes not enumerated by the per-class
    derive, so HAS_POLICY / HAS_PROFILE terminate (0-dangling, sec3.2 node classes):
      IAM_POLICY      -- HAS_POLICY targets (managed ARN | inline pseudo-id)
      INSTANCE_PROFILE-- HAS_PROFILE targets
    Provenance is edge-derived (approximate) here; refined at IAM full-edge cert."""
    nodes = []
    for parn in sorted({e["target"] for e in edges if e["edge_type"] == "HAS_POLICY"}):
        aws_mgd = parn.startswith("arn:aws:iam::aws:policy/")
        inline = "/inline/" in parn
        nodes.append({
            "id": parn, "arn": parn, "name": parn.split("/")[-1].split(":")[-1],
            "type": "IAM_POLICY",
            "policy_kind": "inline" if inline else ("managed-aws" if aws_mgd else "managed-customer"),
            "drift_class": "AWS_MANAGED" if aws_mgd else ("DECLARED" if inline else "LIVE-no-DECLARED"),
            "tf_managed": False, "owner_pipeline": None,
            "provenance": {"tf_kind": "aws_managed" if aws_mgd else "edge-derived"},
        })
    for parn in sorted({e["target"] for e in edges if e["edge_type"] == "HAS_PROFILE"}):
        nodes.append({
            "id": parn, "arn": parn, "name": parn.split("/")[-1], "type": "INSTANCE_PROFILE",
            "drift_class": "DECLARED", "tf_managed": True,
            "owner_pipeline": None, "provenance": {"tf_kind": "edge-derived"},
        })
    # sec3.2a typed principal/endpoint nodes (GRANTS/SUBSCRIBES targets) so those edges
    # terminate (0-dangling) + PUBLIC/CROSS_ACCOUNT grants SURFACE as held findings.
    find_of = {e["target"]: e.get("finding_class") for e in edges
               if e["edge_type"] == "GRANTS" and e.get("finding_class")}
    prin_targets = {e["target"] for e in edges if e["edge_type"] in ("GRANTS", "SUBSCRIBES")}
    for t in sorted(prin_targets):
        if t.startswith("service-principal::"):
            sub = "OAI" if "::oai::" in t else t.split("::")[-1].split(".")[0]
            nodes.append({"id": t, "arn": t, "name": t.split("::")[-1], "type": "SERVICE_PRINCIPAL",
                          "sub_type": sub, "drift_class": "AWS_MANAGED", "tf_managed": False,
                          "owner_pipeline": "aws", "provenance": {"tf_kind": "aws_managed"}})
        elif t.startswith("external-principal::"):
            sub = t.split("::")[1].replace("-", "_").upper()
            node = {"id": t, "arn": t, "name": t.split("::", 1)[1], "type": "EXTERNAL_PRINCIPAL",
                    "sub_type": sub, "drift_class": "LIVE-no-DECLARED", "tf_managed": False,
                    "owner_pipeline": None, "provenance": {"tf_kind": "external"}}
            if find_of.get(t):
                node["finding"] = {"class": find_of[t], "severity": "held", "surfaced": True}
            nodes.append(node)
        elif t.startswith("external-endpoint::"):
            nodes.append({"id": t, "arn": t, "name": t.split("::", 2)[-1], "type": "EXTERNAL_ENDPOINT",
                          "sub_type": t.split("::")[1].upper(), "drift_class": "LIVE-no-DECLARED",
                          "tf_managed": False, "owner_pipeline": None, "provenance": {"tf_kind": "external"}})
        elif t.startswith("iam-user::") or (t.startswith(f"arn:aws:iam::{ACCOUNT}:user/")):
            nodes.append({"id": t, "arn": t, "name": t.split("/")[-1].split("::")[-1], "type": "IAM_USER",
                          "drift_class": "LIVE-no-DECLARED", "tf_managed": False,
                          "owner_pipeline": None, "provenance": {"tf_kind": "edge-derived"}})
    return nodes

# ---------------------------------------------------------------------------
# ANALYTICS -- summary metrics + snapshot diff (NFRA_GLOBGRPH P1 analytics layer,
# in-process over the canonical graph JSON; the daily key-number-delta + audit
# change-log the versioned archive feeds. No Nessie/cluster needed for this layer.)
# ---------------------------------------------------------------------------
def compute_metrics(graph):
    """The 'key summary numbers' for a graph snapshot (the daily-delta + alarm surface)."""
    from collections import Counter
    cd = graph.get("classes_data", {})
    per_class, drift = {}, Counter()
    untyped = 0
    for cls, d in cd.items():
        ns = d.get("nodes", [])
        per_class[cls] = len(ns)
        for n in ns:
            drift[n.get("drift_class", "?")] += 1
            if not n.get("type"):
                untyped += 1
    edges = graph.get("edges", [])
    findings = {
        "overperm_roles": sum(1 for n in cd.get("iam", {}).get("nodes", []) if n.get("broad_managed")),
        "imdsv2_optional_ec2": sum(1 for n in cd.get("ec2", {}).get("nodes", []) if n.get("imdsv2_required") is False),
        "unencrypted_sns": sum(1 for n in cd.get("sns", {}).get("nodes", []) if n.get("kms_encrypted") is False),
        "unmanaged_secrets": sum(1 for n in cd.get("secrets", {}).get("nodes", []) if n.get("drift_class") == "LIVE-no-DECLARED"),
        "public_grants": sum(1 for n in cd.get("external_principal", {}).get("nodes", []) if (n.get("finding") or {}).get("class") == "PUBLIC_GRANT"),
        "cross_account_grants": sum(1 for n in cd.get("external_principal", {}).get("nodes", []) if (n.get("finding") or {}).get("class") == "CROSS_ACCOUNT_GRANT"),
        "live_no_declared_total": drift.get("LIVE-no-DECLARED", 0),
    }
    return {
        "node_total": sum(per_class.values()), "edge_total": len(edges), "untyped": untyped,
        "per_class": per_class, "drift_distribution": dict(drift),
        "edge_types": dict(Counter(e["edge_type"] for e in edges)),
        "security_findings": findings,
    }

def _node_keys(graph):
    return {n["arn"]: (cls, n) for cls, d in graph.get("classes_data", {}).items()
            for n in d.get("nodes", []) if n.get("arn")}

def _edge_keys(graph):
    return {(e["source"], e["target"], e["edge_type"]): e for e in graph.get("edges", [])}

def compute_diff(ga, gb):
    """ga (prior) -> gb (current): node/edge add/remove/modify + metric deltas (graph_changes)."""
    na, nb = _node_keys(ga), _node_keys(gb)
    ea, eb = _edge_keys(ga), _edge_keys(gb)
    nodes_added = sorted(set(nb) - set(na))
    nodes_removed = sorted(set(na) - set(nb))
    nodes_modified = sorted(k for k in (set(na) & set(nb))
                            if na[k][1].get("drift_class") != nb[k][1].get("drift_class"))
    ma, mb = compute_metrics(ga), compute_metrics(gb)
    deltas = {}
    for cls in set(ma["per_class"]) | set(mb["per_class"]):
        d = mb["per_class"].get(cls, 0) - ma["per_class"].get(cls, 0)
        if d:
            deltas[cls] = f"{ma['per_class'].get(cls,0)}->{mb['per_class'].get(cls,0)} ({d:+d})"
    fdeltas = {k: f"{ma['security_findings'].get(k,0)}->{v}"
               for k, v in mb["security_findings"].items() if v != ma["security_findings"].get(k, 0)}
    return {
        "nodes_added": nodes_added, "nodes_removed": nodes_removed, "nodes_modified": nodes_modified,
        "edges_added": len(set(eb) - set(ea)), "edges_removed": len(set(ea) - set(eb)),
        "class_count_deltas": deltas, "security_finding_deltas": fdeltas,
    }

def cmd_dual_managed(args):
    dm = dual_managed()
    print(f"DUAL-MANAGED resources (ARN managed in >1 root-module state): {len(dm)}")
    for arn, mods in sorted(dm.items()):
        print(f"  {arn:64} <- {mods}")

def cmd_metrics(args):
    graph = json.load(open(args.graph)) if args.graph else cmd_derive(argparse.Namespace(cls=None, out=None))
    print(json.dumps(compute_metrics(graph), indent=2, default=str))

def cmd_diff(args):
    ga = json.load(open(args.prior))
    gb = json.load(open(args.current))
    print(json.dumps(compute_diff(ga, gb), indent=2, default=str))

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

def score_stepfunctions():
    oracle = _load_yaml(SHAPES / "stepfunctions-hand-audit-fixture-v0.1.yaml")
    truth = {sm["name"]: sm for sm in oracle.get("state_machines", [])}
    derived = {n["id"]: n for n in derive_class("stepfunctions")["nodes"]}
    tp_nodes = set(truth) & set(derived)
    fp = len(set(derived) - set(truth))
    fn = len(set(truth) - set(derived))
    attr_total = attr_ok = 0
    for name in tp_nodes:
        t, d = truth[name], derived[name]
        for axis in ("machine_type", "definition_hash", "tf_managed"):
            if axis in t:
                attr_total += 1
                if str(d.get(axis, "")) == str(t[axis]):
                    attr_ok += 1
    pe, re_, fe = _f1(len(tp_nodes), fp, fn)
    act_truth_count = oracle.get("activity_count", 0)
    derived_acts = derive_class("sfn_activity")["nodes"]
    # INVOKES edge recall (the key graph metric for a state machine -- must pass >=0.95)
    truth_inv_arns = {
        e["target_arn"]
        for e in oracle.get("edges_certified", {}).get("invokes", [])
    }
    sfnc = _boto("stepfunctions")
    derived_inv_arns = set()
    for node in derived.values():
        try:
            detail = sfnc.describe_state_machine(stateMachineArn=node["arn"])
            for _, tgt in _sfn_task_invokes(detail.get("definition", "{}")):
                derived_inv_arns.add(tgt)
        except Exception:
            pass
    inv_tp = len(truth_inv_arns & derived_inv_arns)
    inv_fp = len(derived_inv_arns - truth_inv_arns)
    inv_fn = len(truth_inv_arns - derived_inv_arns)
    inv_pe, inv_re, inv_fe = _f1(inv_tp, inv_fp, inv_fn)
    return {
        "class": "stepfunctions",
        "node_tp": len(tp_nodes), "node_fp": fp, "node_fn": fn,
        "node_precision": round(pe, 4), "node_recall": round(re_, 4), "node_f1": round(fe, 4),
        "attr_accuracy": round(attr_ok / attr_total, 4) if attr_total else None,
        "attr_checked": attr_total,
        "activity_count_match": len(derived_acts) == act_truth_count,
        "activity_derived": len(derived_acts), "activity_truth": act_truth_count,
        "invokes_tp": inv_tp, "invokes_fp": inv_fp, "invokes_fn": inv_fn,
        "invokes_precision": round(inv_pe, 4), "invokes_recall": round(inv_re, 4),
        "invokes_f1": round(inv_fe, 4),
        "invokes_missed": sorted(truth_inv_arns - derived_inv_arns),
        "missed": sorted(set(truth) - set(derived)),
        "extra": sorted(set(derived) - set(truth)),
    }

SCORERS = {"s3": score_s3, "iam-ec2": score_iam_ec2, "stepfunctions": score_stepfunctions}

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
        es = derive_event_sources()
        graph["classes_data"]["event_source"] = {"class": "event_source", "nodes": es,
            "declared_no_live": [], "counts": {"live": len(es), "untyped": 0}}
        print(f"  event_source live={len(es):3} (typed EVENT_SOURCE origins, sec 3.3)")
        graph["edges"] = derive_edges() + derive_data_access_edges()
        aux = derive_aux_nodes(graph["edges"])
        # register every aux node TYPE as its own class so all edges terminate (0-dangling)
        _aux_types = {"IAM_POLICY": "iam_policy", "INSTANCE_PROFILE": "instance_profile",
                      "SERVICE_PRINCIPAL": "service_principal", "EXTERNAL_PRINCIPAL": "external_principal",
                      "EXTERNAL_ENDPOINT": "external_endpoint", "IAM_USER": "iam_user"}
        _aux_summary = []
        for _ntype, _cls in _aux_types.items():
            _ns = [n for n in aux if n["type"] == _ntype]
            graph["classes_data"][_cls] = {"class": _cls, "nodes": _ns, "declared_no_live": [],
                                           "counts": {"live": len(_ns), "untyped": 0}}
            if _ns:
                _aux_summary.append(f"{_ntype}={len(_ns)}")
        print("  aux nodes    " + " ".join(_aux_summary))
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

GLOBGRPH_BUCKET = "opal-313476888478-globgrph"   # ADHC_GLOBGRPH P1 snapshot/storage bucket

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
    print(f"snapshot -> {tgz} ({tgz.stat().st_size} bytes)")
    # P1: persist to the global-graph S3 archive (the time-travel black-box recorder).
    if not getattr(args, "no_s3", False):
        date = stamp[:8] if len(stamp) >= 8 and stamp[:8].isdigit() else "manual"
        key = f"snapshots/{date}/graph-{stamp}.tar.gz"
        try:
            s3 = _boto("s3")
            body = tgz.read_bytes()
            s3.put_object(Bucket=GLOBGRPH_BUCKET, Key=key, Body=body,
                          ContentType="application/gzip")
            s3.put_object(Bucket=GLOBGRPH_BUCKET, Key="snapshots/latest.txt",
                          Body=key.encode(), ContentType="text/plain")
            print(f"archived -> s3://{GLOBGRPH_BUCKET}/{key} (+ latest.txt pointer)")
        except Exception as e:
            print(f"WARN: S3 archive failed ({type(e).__name__}: {e}); local snapshot kept")

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
    sn.add_argument("--no-s3", action="store_true", dest="no_s3")
    sn.set_defaults(fn=cmd_snapshot)
    m = sub.add_parser("metrics")
    m.add_argument("--graph")
    m.set_defaults(fn=cmd_metrics)
    df = sub.add_parser("diff")
    df.add_argument("prior")
    df.add_argument("current")
    df.set_defaults(fn=cmd_diff)
    dm = sub.add_parser("dual-managed")
    dm.set_defaults(fn=cmd_dual_managed)
    c = sub.add_parser("classes")
    c.set_defaults(fn=cmd_classes)
    args = ap.parse_args()
    args.fn(args)

if __name__ == "__main__":
    main()
