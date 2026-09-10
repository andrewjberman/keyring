#!/usr/bin/env python3
"""comp-aws -- comprehensive AWS cloud compiler (ADHC_CMPAWS).

Derives a typed, certified graph of the AWS cloud by reconciling THREE truths:
  1. IaC  (Terraform parse, HCL-aware -- NOT text-grep; see IE-GAP-3 finding 2026-06-08)
  2. LIVE (boto3 describe/list, read-only, in-process -- NOT shell+CLI; see CRLF finding)
  3. source/provenance (commit/sha where derivable)

Emits typed nodes + edges + drift classes (DECLARED / LIVE-no-DECLARED /
DECLARED-no-LIVE / NO-PROVENANCE) per resource class, and SCORES the derivation
against the CVO-certified hand-audit oracles (org/modules/graph/aws-shapes/*.yaml).

Subcommands:
  derive [--class C] [--out FILE]   live+TF derive -> canonical typed graph JSON
  score  [--class C]                RECALL / ATTR / UNRECONCILED vs certified oracle
  snapshot                          archive the canonical graph (PRD AC7)
  classes                           list supported resource classes

SCORE SEMANTICS (CTO arch ruling 20260710T152154Z -- read this before "fixing" score):
  `score` is OFFLINE-ADJUDICATING. It derives (which necessarily calls AWS -- the derive
  IS its input) and then compares that derive to the fixture with NO further AWS call.
  It NEVER asks AWS to adjudicate a disagreement.

  PRECISION IS NOT COMPUTABLE OFFLINE and is therefore NOT PRINTED. An entry the derive
  emitted that the fixture does not list is either a compiler phantom or a fixture gap,
  and only a human (via --reconcile-fixture) may say which. Reporting it as a false
  positive slanders the compiler; excusing it slanders the fixture.

  Hence the THIRD STATE: UNRECONCILED = |derived - fixture|. Not a pass. Not a compiler
  error. "The derive and the fixture disagree and no human has looked."

  DO NOT "improve" this by auto-excusing extras that exist in AWS. If every extant extra
  is excused, precision can fall only on a phantom -- and the AC-GRAIN sentinel already
  refuses to emit those -- so precision becomes structurally 1.0 and the cert can never
  fail. Guarded by tests/test_comp_aws_cert_mutants.py::test_fixture_gap_is_not_absorbed.

  UNSCORED != PASS != INVALID. All three are distinguishable in token AND exit code.

Goal: deterministic cloud navigation. (The former ">=95% aggregate F1" goal is RETIRED:
it averaged 5 heterogeneous metrics from 3 of 30 classes into one estate-level number,
one leg of which -- ec2 declared_f1 -- was structurally pinned to 1.0.)

Author: 0.7.0_AE_CloudOps. Pattern: extends comp-iam / comp-lambdamap (PRD AC6).
Cert layer rebuilt 2026-07-10 by 3.0.0_SA_CVO~A (NFRA_TOOLPASS tool-2 pass; CTO-gated).
"""
from __future__ import annotations
import argparse
import sys
import json
import tarfile
import io
import glob
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

WS = Path(__file__).resolve().parents[3]   # ajb_workspace root (org/modules/graph/<file>)
TF_ROOT = WS / "infra" / "aws" / "terraform"
SHAPES = WS / "org" / "modules" / "graph" / "aws-shapes"
ACCOUNT = "313476888478"
REGIONS = ["us-east-1", "us-east-2"]

# --- exit codes -------------------------------------------------------------
# A1: main() previously discarded every handler's return, so comp-aws could only exit
# nonzero on an uncaught exception. `score --class zzqq-nope` exited 0 and was recorded
# as PASS in org/compiler-tools-log.md (the launcher logs $?). The success token was
# bound to the wrong step.
RC_OK           = 0
RC_FAIL         = 1   # a real negative verdict (unreconciled / recall miss)
RC_INVALID      = 2   # caller error: class does not exist  (argparse also uses 2)
RC_DERIVE_ERROR = 3   # derive could not run (e.g. unmappable ARN)
RC_UNSCORED     = 4   # valid class, NO oracle -> UNMEASURED, never recorded as success

# A6/A2: a fixture is a hand-audit frozen at a vintage. Past this age the estate has
# almost certainly moved. STALE is an ADVISORY WARN and NEVER by itself an rc -- making
# age fail the cert would rebuild the aging clock this fix exists to remove. The failing
# condition is UNRECONCILED (a real disagreement), not the calendar.
FIXTURE_STALE_DAYS = 14

# A2: printed wherever a number cannot be computed honestly. A number you cannot compute
# honestly is not improved by computing it dishonestly.
UNAVAILABLE = "UNAVAILABLE (requires reconciliation)"

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
_S3_SUBCFG_CACHE = {}   # WAVE-4: per-bucket lifecycle/cors/website cache (live_s3 called repeatedly)
_S3_NOTIFICATION_CACHE = {}  # per-build READ / UNREADABLE notification result; never collapse failure to zero

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
                _arn = a.get("arn")
                # WAVE-4: synthesize an arn for declared types the provider leaves arn-less
                # (apigatewayv2_route) so the live-node arn join lands (else false 0-match drift).
                if not _arn and r["type"] == "aws_apigatewayv2_route" and a.get("api_id") and a.get("id"):
                    _arn = f"arn:aws:apigateway:us-east-1::/apis/{a['api_id']}/routes/{a['id']}"
                resources.append({
                    "type": r["type"], "tf_name": r.get("name"), "module": module,
                    "tf_kind": mode,
                    "arn": _arn, "id": a.get("id"),
                    # WAVE-4: + layer_name (aws_lambda_layer_version has no `name`/`arn`-without-version)
                    "name": a.get("name") or a.get("bucket") or a.get("function_name")
                            or a.get("alarm_name") or a.get("layer_name"),
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


def _read_s3_notification_configuration(client, bucket):
    """Read one bucket notification configuration with an explicit two-state result.

    A missing configuration is a successful READ whose three configuration arrays are
    empty.  An exception is UNREADABLE and carries no configuration object at all.  The
    distinction is cached because live_s3() and derive_edges() share this read during a
    full build.
    """
    if bucket in _S3_NOTIFICATION_CACHE:
        return _S3_NOTIFICATION_CACHE[bucket]
    try:
        configuration = client.get_bucket_notification_configuration(Bucket=bucket)
        result = {"state": "READ", "configuration": configuration, "error": None}
    except Exception as exc:  # the error is data; never turn it into an empty configuration
        result = {
            "state": "UNREADABLE",
            "configuration": None,
            "error": f"{type(exc).__name__}: {exc}",
        }
    _S3_NOTIFICATION_CACHE[bucket] = result
    return result


def _s3_notification_read_summary():
    read = sorted(k for k, v in _S3_NOTIFICATION_CACHE.items() if v["state"] == "READ")
    unreadable = sorted(k for k, v in _S3_NOTIFICATION_CACHE.items() if v["state"] == "UNREADABLE")
    return {
        "buckets_read": len(read),
        "buckets_unreadable": len(unreadable),
        "unreadable_buckets": unreadable,
    }


def _print_s3_notification_read_summary():
    summary = _s3_notification_read_summary()
    names = ",".join(summary["unreadable_buckets"]) or "none"
    print("  s3 notifications buckets read=%d / buckets unreadable=%d; unreadable=%s" % (
        summary["buckets_read"], summary["buckets_unreadable"], names))


def _declared_s3_lambda_notifications():
    """Resolved Lambda targets from Terraform's declared-side state union.

    _load_all_tfstate() is this compiler's canonical terraform-show-equivalent plane:
    it retains the source module/resource while providing resolved bucket names and
    Lambda ARNs that raw HCL expressions cannot supply reliably.
    """
    rows = []
    for resource in _load_all_tfstate():
        if resource.get("type") != "aws_s3_bucket_notification":
            continue
        attrs = resource.get("attrs") or {}
        bucket = attrs.get("bucket") or resource.get("id") or resource.get("name")
        if not bucket:
            continue
        provenance = {
            "tf_module": resource.get("module"),
            "tf_resource": "aws_s3_bucket_notification.%s" % resource.get("tf_name"),
            "tf_kind": resource.get("tf_kind", "managed"),
        }
        for configuration in attrs.get("lambda_function") or []:
            target = configuration.get("lambda_function_arn")
            if not target:
                continue
            rows.append({
                "bucket": bucket,
                "target": target,
                "configuration_id": configuration.get("id"),
                "events": configuration.get("events") or [],
                "filter_prefix": configuration.get("filter_prefix"),
                "filter_suffix": configuration.get("filter_suffix"),
                "provenance": provenance,
            })
    return rows


def _derive_s3_lambda_trigger_edges(client, s3_nodes, declared=None):
    """Merge live and Terraform-declared S3->Lambda trigger observations.

    Provenance is exactly live / declared / both.  A successful live read can
    disagree with Terraform; an UNREADABLE live read stays unknown and leaves the
    declared edge standing instead of manufacturing a zero.
    """
    observations = {}
    live_states = {}

    def observation(bucket, target):
        return observations.setdefault((bucket, target), {
            "live": [], "declared": [], "declared_provenance": [],
        })

    for node in s3_nodes:
        bucket = node["id"]
        result = _read_s3_notification_configuration(client, bucket)
        live_states[bucket] = result["state"]
        if result["state"] != "READ":
            continue
        for configuration in (result["configuration"] or {}).get("LambdaFunctionConfigurations", []):
            target = configuration.get("LambdaFunctionArn")
            if target:
                observation(bucket, target)["live"].append(configuration)

    declared_rows = _declared_s3_lambda_notifications() if declared is None else declared
    for row in declared_rows:
        bucket, target = row.get("bucket"), row.get("target")
        if not (bucket and target):
            continue
        item = observation(bucket, target)
        item["declared"].append({
            "configuration_id": row.get("configuration_id"),
            "events": row.get("events") or [],
            "filter_prefix": row.get("filter_prefix"),
            "filter_suffix": row.get("filter_suffix"),
        })
        if row.get("provenance") and row["provenance"] not in item["declared_provenance"]:
            item["declared_provenance"].append(row["provenance"])

    edges = []
    for (bucket, target), item in sorted(observations.items()):
        live_present, declared_present = bool(item["live"]), bool(item["declared"])
        provenance = "both" if live_present and declared_present else ("live" if live_present else "declared")
        read_state = live_states.get(bucket, "NOT_LISTED")
        if live_present and declared_present:
            disagreement = "NONE"
        elif live_present:
            disagreement = "LIVE_ONLY"
        elif read_state == "UNREADABLE":
            disagreement = "UNKNOWN_LIVE_UNREADABLE"
        else:
            disagreement = "DECLARED_ONLY"
        edges.append({
            "source": f"arn:aws:s3:::{bucket}",
            "target": target,
            "edge_type": "TRIGGERS",
            "provenance": provenance,
            "live_read_state": read_state,
            "source_disagreement": disagreement,
            "live_configuration_count": len(item["live"]),
            "declared_configuration_count": len(item["declared"]),
            "declared_provenance": item["declared_provenance"],
        })
    return edges

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
        notification = _read_s3_notification_configuration(c, name)
        node["notification_read_state"] = notification["state"]
        node["notification_read_error"] = notification["error"]
        if notification["state"] == "READ":
            nc = notification["configuration"]
            node["event_notifications"] = len(nc.get("LambdaFunctionConfigurations", []))
            # WAVE-4 node-typing depth: full notification target census (not just Lambda)
            node["notify_sns"] = len(nc.get("TopicConfigurations", []))
            node["notify_sqs"] = len(nc.get("QueueConfigurations", []))
        else:
            node["event_notifications"] = None
            node["notify_sns"] = None
            node["notify_sqs"] = None
        # WAVE-4 node-typing depth: lifecycle / CORS / website sub-configs (S3 typing gap),
        # cached per bucket -- live_s3 is called several times per derive; bound to once/bucket.
        sub = _S3_SUBCFG_CACHE.get(name)
        if sub is None:
            sub = {}
            try:
                sub["lifecycle_rules"] = len(c.get_bucket_lifecycle_configuration(Bucket=name).get("Rules", []))
            except Exception:
                sub["lifecycle_rules"] = 0
            try:
                c.get_bucket_cors(Bucket=name)
                sub["cors_enabled"] = True
            except Exception:
                sub["cors_enabled"] = False
            try:
                c.get_bucket_website(Bucket=name)
                sub["website_enabled"] = True
            except Exception:
                sub["website_enabled"] = False
            _S3_SUBCFG_CACHE[name] = sub
        node.update(sub)
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

def _paged(client, op, result_key, frame=None, **kw):
    """FULL token walk via the service paginator -- the TRUNCLASS FIX12 F5 pattern (census
    @e141eb5f30 Tier-2: a single-page list_* makes resource #101+ read as NONEXISTENT to every
    graph consumer -- the deletion-warrant shape, an absent edge in the estate graph). ONE
    pattern for all eight fixed sites; result_key may be a tuple for nested shapes (CloudFront's
    DistributionList.Items). `frame` prints the denominator beside the count (stderr, one line
    per walk) so the retrieval carries its own frame (F6). Ops without a paginator fall back to
    one direct call -- none of the eight fixed sites hits that branch."""
    def _pluck(page):
        d = page
        for k in (result_key if isinstance(result_key, tuple) else (result_key,)):
            d = (d or {}).get(k)
        return d or []
    items, pages = [], 0
    try:
        for page in client.get_paginator(op).paginate(**kw):
            pages += 1
            items.extend(_pluck(page))
    except Exception:  # noqa: BLE001  -- OperationNotPageableError etc.: one honest direct call
        items, pages = list(_pluck(getattr(client, op)(**kw))), 1
    if frame:
        print("[frame] %s: %d item(s) over %d page(s), full walk" % (frame, len(items), pages),
              file=sys.stderr)
    return items


def live_sns():
    nodes = []
    c = _boto("sns")
    for t in _paged(c, "list_topics", "Topics", frame="sns.list_topics"):
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
            subs = _paged(c, "list_subscriptions_by_topic", "Subscriptions", TopicArn=arn)
            node["subscriptions"] = sorted(f'{s["Protocol"]}:{s["Endpoint"]}' for s in subs)
        except Exception:
            node["subscriptions"] = []
        nodes.append(node)
    return nodes

def live_sqs():
    nodes = []
    c = _boto("sqs")
    for url in _paged(c, "list_queues", "QueueUrls", frame="sqs.list_queues"):
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
        dl = _paged(c, "list_distributions", ("DistributionList", "Items"),
                    frame="cloudfront.list_distributions")
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
# ---------------------------------------------------------------------------
# COVERAGE EXPANSION (NFRA_COMPAWS WAVE-4, 2026-06-11, Andrew /goal): new AWS
# resource classes closing the adversarial-audit gaps (API Gateway, ECS/Fargate,
# VPC SG/endpoint, SSM document, EventBridge Scheduler, Lambda layer). ADDITIVE
# ONLY -- the certified-13 derive paths are untouched. Each live_* returns typed
# nodes carrying an `arn` (so _node_arn returns it verbatim) for reconciliation.
# ---------------------------------------------------------------------------
def _apigw_paged(c, method, **kwargs):
    """Drain an apigatewayv2 paged call (NextToken protocol). These endpoints default
    to MaxResults=25 and SILENTLY truncate -- the unpaginated form cost 38/63 routes on
    opal-portal-data-proxy-api (CVO WAVE-4 cert finding, 2026-06-11)."""
    items = []
    resp = getattr(c, method)(**kwargs)
    items += resp.get("Items", [])
    while resp.get("NextToken"):
        resp = getattr(c, method)(NextToken=resp["NextToken"], **kwargs)
        items += resp.get("Items", [])
    return items

def live_apigw():
    """API_GW nodes (aws_apigatewayv2_api). The HTTP/WebSocket serving layer between
    CloudFront/clients and Lambda that the certified graph dead-ended at."""
    c = _boto("apigatewayv2")
    nodes = []
    try:
        items = _apigw_paged(c, "get_apis")
    except Exception:
        return nodes
    for a in items:
        aid = a["ApiId"]
        nodes.append({
            "id": aid, "type": "API_GW",
            "arn": f"arn:aws:apigateway:us-east-1::/apis/{aid}",
            "name": a.get("Name"), "protocol": a.get("ProtocolType"),
            "endpoint": a.get("ApiEndpoint"),
            "execute_api_disabled": bool(a.get("DisableExecuteApiEndpoint", False)),
        })
    return nodes

def live_api_routes():
    """API_ROUTE nodes (aws_apigatewayv2_route) -- one per route, carrying the resolved
    integration target (Lambda arn for AWS_PROXY) for the ROUTES_TO edge."""
    c = _boto("apigatewayv2")
    nodes = []
    try:
        apis = _apigw_paged(c, "get_apis")
    except Exception:
        return nodes
    for a in apis:
        aid = a["ApiId"]
        integ = {}
        try:
            for it in _apigw_paged(c, "get_integrations", ApiId=aid):
                integ[it["IntegrationId"]] = {"type": it.get("IntegrationType"),
                                              "uri": it.get("IntegrationUri")}
        except Exception:
            pass
        try:
            routes = _apigw_paged(c, "get_routes", ApiId=aid)
        except Exception:
            routes = []
        for r in routes:
            rid = r["RouteId"]
            tgt = r.get("Target", "") or ""
            it = integ.get(tgt.split("/")[-1], {}) if tgt else {}
            nodes.append({
                "id": f"{aid}/{rid}", "type": "API_ROUTE",
                "arn": f"arn:aws:apigateway:us-east-1::/apis/{aid}/routes/{rid}",
                "name": r.get("RouteKey"), "api_id": aid, "route_key": r.get("RouteKey"),
                "authorization": r.get("AuthorizationType"),
                "authorizer_id": r.get("AuthorizerId"),
                "integration_type": it.get("type"),
                "integration_uri": it.get("uri"),   # Lambda arn -> ROUTES_TO edge target
            })
    return nodes

def live_ecs_tasks():
    """ECS_TASK_DEFINITION nodes (aws_ecs_task_definition) -- the Fargate/ECS compute
    surface (incl the GLOBGRPH Nessie task) the certified graph could not see. Indexes
    the ACTIVE revision per family; carries task/execution role arns for ASSUMES."""
    c = _boto("ecs")
    nodes = []
    try:
        arns = []
        tok = None
        while True:
            kw = {"status": "ACTIVE", "sort": "DESC"}
            if tok:
                kw["nextToken"] = tok
            resp = c.list_task_definitions(**kw)
            arns += resp.get("taskDefinitionArns", [])
            tok = resp.get("nextToken")
            if not tok:
                break
    except Exception:
        return nodes
    seen_family = set()
    for tdarn in arns:
        try:
            td = c.describe_task_definition(taskDefinition=tdarn)["taskDefinition"]
        except Exception:
            continue
        fam = td.get("family")
        if fam in seen_family:   # keep only the latest active revision per family
            continue
        seen_family.add(fam)
        nodes.append({
            "id": fam, "type": "ECS_TASK_DEFINITION",
            "arn": td.get("taskDefinitionArn"), "name": fam,
            "launch_type": (td.get("requiresCompatibilities") or ["EC2"])[0],
            "is_fargate": "FARGATE" in (td.get("requiresCompatibilities") or []),
            "network_mode": td.get("networkMode"),
            "task_role": (td.get("taskRoleArn") or "").split("/")[-1] or None,
            "execution_role": (td.get("executionRoleArn") or "").split("/")[-1] or None,
            "task_role_arn": td.get("taskRoleArn"),
            "execution_role_arn": td.get("executionRoleArn"),
            "container_count": len(td.get("containerDefinitions") or []),
            "cpu": td.get("cpu"), "memory": td.get("memory"),
        })
    return nodes

def live_ecs_clusters():
    """ECS_CLUSTER nodes (aws_ecs_cluster) -- the Fargate cluster that EventBridge rules /
    Scheduler target via RunTask; modeled so rule->cluster TRIGGERS terminates (0-dangling)."""
    c = _boto("ecs")
    nodes = []
    try:
        arns = _paged(c, "list_clusters", "clusterArns", frame="ecs.list_clusters")
        for i in range(0, len(arns), 100):
            for cl in c.describe_clusters(clusters=arns[i:i + 100]).get("clusters", []):
                nodes.append({
                    "id": cl["clusterName"], "type": "ECS_CLUSTER",
                    "arn": cl["clusterArn"], "name": cl["clusterName"],
                    "status": cl.get("status"),
                    "running_tasks": cl.get("runningTasksCount"),
                    "active_services": cl.get("activeServicesCount"),
                })
    except Exception:
        return nodes
    return nodes

def live_security_groups():
    """SECURITY_GROUP nodes (aws_security_group) -- the network-boundary surface. ARN is
    given by the API (SecurityGroupArn). Carries vpc_id + ingress/egress rule counts."""
    nodes = []
    for region in REGIONS:
        c = _boto("ec2", region)
        try:
            tok = None
            while True:
                kw = {}
                if tok:
                    kw["NextToken"] = tok
                resp = c.describe_security_groups(**kw)
                for sg in resp.get("SecurityGroups", []):
                    nodes.append({
                        "id": sg["GroupId"], "type": "SECURITY_GROUP",
                        "arn": sg.get("SecurityGroupArn")
                               or f"arn:aws:ec2:{region}:{ACCOUNT}:security-group/{sg['GroupId']}",
                        "name": sg.get("GroupName"), "region": region,
                        "vpc_id": sg.get("VpcId"),
                        "ingress_rules": len(sg.get("IpPermissions") or []),
                        "egress_rules": len(sg.get("IpPermissionsEgress") or []),
                        "open_ingress": any(
                            any(r.get("CidrIp") == "0.0.0.0/0" for r in p.get("IpRanges", []))
                            for p in sg.get("IpPermissions") or []),
                    })
                tok = resp.get("NextToken")
                if not tok:
                    break
        except Exception:
            continue
    return nodes

def live_vpc_endpoints():
    """VPC_ENDPOINT nodes (aws_vpc_endpoint) -- PrivateLink/gateway endpoints; carries the
    service name + attached SG ids (for USES_SG) so the private-network path is visible."""
    nodes = []
    for region in REGIONS:
        c = _boto("ec2", region)
        try:
            tok = None
            while True:
                kw = {}
                if tok:
                    kw["NextToken"] = tok
                resp = c.describe_vpc_endpoints(**kw)
                for ve in resp.get("VpcEndpoints", []):
                    nodes.append({
                        "id": ve["VpcEndpointId"], "type": "VPC_ENDPOINT",
                        "arn": f"arn:aws:ec2:{region}:{ACCOUNT}:vpc-endpoint/{ve['VpcEndpointId']}",
                        "name": ve.get("ServiceName"), "region": region,
                        "service_name": ve.get("ServiceName"),
                        "endpoint_type": ve.get("VpcEndpointType"),
                        "vpc_id": ve.get("VpcId"), "state": ve.get("State"),
                        "sg_ids": sorted(g.get("GroupId") for g in ve.get("Groups", []) if g.get("GroupId")),
                        "private_dns": bool(ve.get("PrivateDnsEnabled")),
                    })
                tok = resp.get("NextToken")
                if not tok:
                    break
        except Exception:
            continue
    return nodes

def live_ssm_documents():
    """SSM_DOCUMENT nodes (aws_ssm_document) -- the EC2 code-deploy mechanism (CLAUDE.md
    Rule 12); Self-owned only (exclude AWS-public docs). The deploy path the graph missed."""
    c = _boto("ssm")
    nodes = []
    try:
        tok = None
        while True:
            kw = {"Filters": [{"Key": "Owner", "Values": ["Self"]}]}
            if tok:
                kw["NextToken"] = tok
            resp = c.list_documents(**kw)
            for d in resp.get("DocumentIdentifiers", []):
                nm = d["Name"]
                nodes.append({
                    "id": nm, "type": "SSM_DOCUMENT",
                    "arn": f"arn:aws:ssm:us-east-1:{ACCOUNT}:document/{nm}",
                    "name": nm, "doc_type": d.get("DocumentType"),
                    "doc_format": d.get("DocumentFormat"),
                    "target_type": d.get("TargetType"),
                    "platforms": d.get("PlatformTypes") or [],
                })
            tok = resp.get("NextToken")
            if not tok:
                break
    except Exception:
        return nodes
    return nodes

def live_codebuild_projects():
    """CODEBUILD_PROJECT nodes (aws_codebuild_project) -- the CI/build-runner surface the graph
    never scanned. Fills the opal-drift-producer NODEGAP finding (2026-07-08, design doc
    org/tier2_senior/0.7.0_AE_CloudOps/deliverables/NFRA_GLOBGRPH.NODEGAP.codebuild-recognizer-design.md).
    CTO arch-gate GO 20260708T202059Z + CVO count re-sign b9a04eb8f (NODE_TYPE_LAYER 'aws')."""
    c = _boto("codebuild")
    nodes = []
    try:
        names = []
        tok = None
        while True:
            kw = {"nextToken": tok} if tok else {}
            resp = c.list_projects(**kw)
            names += resp.get("projects", [])
            tok = resp.get("nextToken")
            if not tok:
                break
        # batch_get_projects caps at 100 names/call; chunk defensively so this doesn't silently
        # truncate if the estate's CodeBuild footprint grows past today's single project.
        for i in range(0, len(names), 100):
            resp = c.batch_get_projects(names=names[i:i + 100])
            for p in resp.get("projects", []):
                nm = p["name"]
                src = p.get("source", {}) or {}
                nodes.append({
                    "id": nm, "type": "CODEBUILD_PROJECT",
                    "arn": p.get("arn"), "name": nm,
                    "service_role": p.get("serviceRole"),
                    "source_type": src.get("type"),
                    "timeout_minutes": p.get("timeoutInMinutes"),
                })
    except Exception:
        return nodes
    return nodes

def live_schedules():
    """SCHEDULE nodes (aws_scheduler_schedule) -- EventBridge Scheduler, a DISTINCT service
    from classic Events rules (live_eventbridge); carries the target arn for TRIGGERS."""
    c = _boto("scheduler")
    nodes = []
    try:
        tok = None
        schedules = []
        while True:
            kw = {}
            if tok:
                kw["NextToken"] = tok
            resp = c.list_schedules(**kw)
            schedules += resp.get("Schedules", [])
            tok = resp.get("NextToken")
            if not tok:
                break
    except Exception:
        return nodes
    for s in schedules:
        nm, grp = s["Name"], s.get("GroupName", "default")
        node = {"id": nm, "type": "SCHEDULE", "arn": s.get("Arn"), "name": nm,
                "group": grp, "state": s.get("State")}
        try:
            d = c.get_schedule(Name=nm, GroupName=grp)
            node["schedule_expression"] = d.get("ScheduleExpression")
            tgt = d.get("Target") or {}
            node["target_arn"] = tgt.get("Arn")            # -> TRIGGERS edge
            node["target_role_arn"] = tgt.get("RoleArn")
        except Exception:
            pass
        nodes.append(node)
    return nodes

def live_lambda_layers():
    """LAMBDA_LAYER nodes (aws_lambda_layer_version) -- a dependency surface the certified
    graph collected as a Lambda property but never typed. The pyiceberg-nessie-deps /
    Iceberg dependency enters here (the Nessie blind spot). Keyed on the layer (latest ver)."""
    c = _boto("lambda")
    nodes = []
    try:
        layers = []
        marker = None
        while True:
            kw = {}
            if marker:
                kw["Marker"] = marker
            resp = c.list_layers(**kw)
            layers += resp.get("Layers", [])
            marker = resp.get("NextMarker")
            if not marker:
                break
    except Exception:
        return nodes
    for la in layers:
        lv = la.get("LatestMatchingVersion") or {}
        nodes.append({
            "id": la["LayerName"], "type": "LAMBDA_LAYER",
            "arn": la.get("LayerArn"), "name": la.get("LayerName"),
            "latest_version": lv.get("Version"),
            "latest_version_arn": lv.get("LayerVersionArn"),
            "runtimes": lv.get("CompatibleRuntimes") or [],
        })
    return nodes

# ---------------------------------------------------------------------------
# OPLMCP.07 AC2 -- ALB-stack derive-classes (aws_lb / aws_lb_listener /
# aws_lb_target_group / aws_route53_record). Additive (outside the certified-13
# + WAVE-4 score baseline; no per-class scorer -- the aws-shapes oracle is CVO's
# independent-cert follow-on, per NFRA_COMPAWS_SCHEMA + PRD Addendum A). Edges in
# derive_edges() resolve the blast-radius chain Route53->ALB->listener->TG->EC2.
# ---------------------------------------------------------------------------
def live_lb():
    """LOAD_BALANCER nodes (aws_lb) -- ALB/NLB. ARN given by the API (LoadBalancerArn).
    Carries SGs + subnets + dns_name/zone_id (for USES_SG / IN_SUBNET / Route53 ALIAS_TO)."""
    nodes = []
    for region in REGIONS:
        c = _boto("elbv2", region)
        try:
            for page in c.get_paginator("describe_load_balancers").paginate():
                for lb in page.get("LoadBalancers", []):
                    nodes.append({
                        "id": lb["LoadBalancerName"], "type": "LOAD_BALANCER",
                        "arn": lb["LoadBalancerArn"], "name": lb["LoadBalancerName"],
                        "region": region,
                        "lb_type": lb.get("Type"), "scheme": lb.get("Scheme"),
                        "vpc_id": lb.get("VpcId"),
                        "dns_name": lb.get("DNSName"),
                        "canonical_zone_id": lb.get("CanonicalHostedZoneId"),
                        "security_groups": lb.get("SecurityGroups") or [],
                        "subnets": [az.get("SubnetId") for az in lb.get("AvailabilityZones") or [] if az.get("SubnetId")],
                    })
        except Exception:
            continue
    return nodes


def live_lb_target_groups():
    """TARGET_GROUP nodes (aws_lb_target_group). ARN given (TargetGroupArn). Carries the
    parent LB arns (ON_LB) + the registered instance target ids (TARGETS -> EC2) + health path."""
    nodes = []
    for region in REGIONS:
        c = _boto("elbv2", region)
        try:
            for page in c.get_paginator("describe_target_groups").paginate():
                for tg in page.get("TargetGroups", []):
                    targets = []
                    try:
                        th = c.describe_target_health(TargetGroupArn=tg["TargetGroupArn"])
                        for d in th.get("TargetHealthDescriptions", []):
                            tid = (d.get("Target") or {}).get("Id")
                            if tid:
                                targets.append(tid)
                    except Exception:
                        pass
                    nodes.append({
                        "id": tg["TargetGroupName"], "type": "TARGET_GROUP",
                        "arn": tg["TargetGroupArn"], "name": tg["TargetGroupName"],
                        "region": region,
                        "port": tg.get("Port"), "protocol": tg.get("Protocol"),
                        "vpc_id": tg.get("VpcId"), "target_type": tg.get("TargetType"),
                        "health_check_path": tg.get("HealthCheckPath"),
                        "load_balancer_arns": tg.get("LoadBalancerArns") or [],
                        "targets": targets,
                    })
        except Exception:
            continue
    return nodes


def live_lb_listeners():
    """LB_LISTENER nodes (aws_lb_listener). ARN given (ListenerArn). Carries the parent LB
    (ON_LB), the forward TG arns (FORWARDS_TO), the cert arns (USES_CERT), + an authenticate_oidc
    flag so the OPLMCP.02 OIDC default-action surfaces as a graph property."""
    nodes = []
    for region in REGIONS:
        c = _boto("elbv2", region)
        try:
            lb_arns = []
            for page in c.get_paginator("describe_load_balancers").paginate():
                lb_arns += [lb["LoadBalancerArn"] for lb in page.get("LoadBalancers", [])]
            for lb_arn in lb_arns:
                for page in c.get_paginator("describe_listeners").paginate(LoadBalancerArn=lb_arn):
                    for ls in page.get("Listeners", []):
                        fwd, has_oidc = [], False
                        for act in ls.get("DefaultActions", []):
                            if act.get("Type") == "authenticate-oidc":
                                has_oidc = True
                            if act.get("Type") == "forward":
                                if act.get("TargetGroupArn"):
                                    fwd.append(act["TargetGroupArn"])
                                for t in ((act.get("ForwardConfig") or {}).get("TargetGroups") or []):
                                    if t.get("TargetGroupArn"):
                                        fwd.append(t["TargetGroupArn"])
                        nodes.append({
                            "id": ls["ListenerArn"].rsplit("/", 1)[-1], "type": "LB_LISTENER",
                            "arn": ls["ListenerArn"],
                            "name": f"{lb_arn.rsplit('/', 1)[-1]}:{ls.get('Port')}",
                            "region": region,
                            "load_balancer_arn": lb_arn,
                            "port": ls.get("Port"), "protocol": ls.get("Protocol"),
                            "certificate_arns": [x.get("CertificateArn") for x in ls.get("Certificates") or [] if x.get("CertificateArn")],
                            # AWS returns a single-TG forward action's target both as TargetGroupArn
                            # (legacy shorthand) AND in ForwardConfig.TargetGroups -> dedup so the
                            # FORWARDS_TO edge fires once per (listener, TG), not twice.
                            "forward_target_group_arns": list(dict.fromkeys(fwd)),
                            "authenticate_oidc": has_oidc,
                        })
        except Exception:
            continue
    return nodes


def live_route53_records():
    """ROUTE53_RECORD nodes (aws_route53_record) -- A/AAAA ALIAS records (the DNS entry to the
    ALB). Route53 is GLOBAL (no region). The provider leaves these arn-less -> synthesize a
    deterministic arn (mirror the apigatewayv2_route precedent); the TF-state join lands by_name
    (the record name, e.g. mcp.opalinvest.dev). Carries the alias target dns (ALIAS_TO -> LB)."""
    nodes = []
    try:
        c = _boto("route53")
        for zpage in c.get_paginator("list_hosted_zones").paginate():
            for z in zpage.get("HostedZones", []):
                zid = z["Id"].rsplit("/", 1)[-1]
                for rpage in c.get_paginator("list_resource_record_sets").paginate(HostedZoneId=z["Id"]):
                    for rs in rpage.get("ResourceRecordSets", []):
                        if rs.get("Type") not in ("A", "AAAA"):
                            continue
                        alias = rs.get("AliasTarget") or {}
                        if not alias.get("DNSName"):
                            continue
                        name = rs["Name"].rstrip(".")
                        rtype = rs["Type"]
                        nodes.append({
                            "id": f"{zid}_{name}_{rtype}", "type": "ROUTE53_RECORD",
                            "arn": f"arn:aws:route53:::hostedzone/{zid}/record/{name}/{rtype}",
                            "name": name, "region": "global",
                            "record_type": rtype, "zone_id": zid,
                            "alias_target_dns": (alias.get("DNSName") or "").rstrip("."),
                            "alias_target_zone": alias.get("HostedZoneId"),
                        })
    except Exception:
        pass
    return nodes

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
    # WAVE-4 coverage expansion (Andrew /goal 2026-06-11) -- additive classes
    "apigw":         (live_apigw,           ["aws_apigatewayv2_api"]),
    "api_route":     (live_api_routes,      ["aws_apigatewayv2_route"]),
    "ecs_task":      (live_ecs_tasks,       ["aws_ecs_task_definition"]),
    "ecs_cluster":   (live_ecs_clusters,    ["aws_ecs_cluster"]),
    "security_group":(live_security_groups, ["aws_security_group"]),
    "vpc_endpoint":  (live_vpc_endpoints,   ["aws_vpc_endpoint"]),
    "ssm_document":  (live_ssm_documents,   ["aws_ssm_document"]),
    "codebuild_project": (live_codebuild_projects, ["aws_codebuild_project"]),
    "scheduler":     (live_schedules,       ["aws_scheduler_schedule"]),
    "lambda_layer":  (live_lambda_layers,   ["aws_lambda_layer_version"]),
    # OPLMCP.07 AC2 -- ALB-stack (additive; outside the certified-13 + WAVE-4 score baseline)
    "lb":             (live_lb,               ["aws_lb"]),
    "lb_target_group":(live_lb_target_groups, ["aws_lb_target_group"]),
    "lb_listener":    (live_lb_listeners,     ["aws_lb_listener"]),
    "route53_record": (live_route53_records,  ["aws_route53_record"]),
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
        for esm in _paged(lc, "list_event_source_mappings", "EventSourceMappings",
                          frame="lambda.list_event_source_mappings(dlq)"):
            onf = ((esm.get("DestinationConfig") or {}).get("OnFailure") or {}).get("Destination")
            if onf and esm.get("FunctionArn"):
                E(esm["FunctionArn"], onf, "DEAD_LETTERS_TO")
    except Exception:
        pass
    # S3_BUCKET -[TRIGGERS]-> LAMBDA, merged from live reads and Terraform declarations.
    # A failed live read remains UNREADABLE; declared edges survive with that state visible.
    s3c = _boto("s3")
    _s3_nodes = live_s3()
    edges.extend(_derive_s3_lambda_trigger_edges(s3c, _s3_nodes))
    # S3_BUCKET -[HAS_POLICY]-> S3_BUCKET_POLICY -[GRANTS]-> principal
    for p in live_s3_policies():
        barn = f"arn:aws:s3:::{p['bucket']}"
        parn = f"{barn}#policy"
        E(barn, parn, "HAS_POLICY")
        seen_pr = set()
        for st in p["statements"]:
            # GRANTS = Allow only (IAM-PUBLIC-DENY-FP): a Deny statement is a guardrail, NOT a
            # grant. Deny+Principal:* (e.g. DenyInsecureTransport) must NOT emit a public-principal
            # node/finding -- that's the opposite of public exposure.
            if st.get("effect") != "Allow":
                continue
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
        for d in _paged(cf, "list_distributions", ("DistributionList", "Items"),
                        frame="cloudfront.list_distributions(origins)"):
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

    # ===================================================================
    # WAVE-4 COVERAGE-EXPANSION EDGES (Andrew /goal 2026-06-11). Additive;
    # every edge is guarded to terminate on a typed class node (0-dangling).
    # ===================================================================
    _exp_lam = live_lambda()
    _lambda_arns = {f"arn:aws:lambda:us-east-1:{ACCOUNT}:function:{x['id']}" for x in _exp_lam}
    _sqs_arns    = {x["arn"] for x in live_sqs() if x.get("arn")}
    _sns_arns    = {x["arn"] for x in live_sns() if x.get("arn")}
    _dynamo_arns = {x["arn"] for x in live_dynamodb() if x.get("arn")}
    _role_arns   = {n["arn"] for n in live_iam_roles()}
    _sg_by_id    = {x["id"]: x["arn"] for x in live_security_groups()}
    _layer_arns  = {x["arn"] for x in live_lambda_layers() if x.get("arn")}
    _sfn_arns    = {x["arn"] for x in live_stepfunctions()}

    # API_GW -[HAS_ROUTE]-> API_ROUTE ; API_ROUTE -[ROUTES_TO]-> LAMBDA
    # (the #1 audit gap: the HTTP-API serving layer the certified graph dead-ended at)
    for r in live_api_routes():
        rarn = r["arn"]
        E(f"arn:aws:apigateway:us-east-1::/apis/{r['api_id']}", rarn, "HAS_ROUTE")
        uri = r.get("integration_uri") or ""
        m = re.search(r"(arn:aws:lambda:[a-z0-9-]+:\d+:function:[A-Za-z0-9_-]+)", uri)
        if m and m.group(1) in _lambda_arns:
            E(rarn, m.group(1), "ROUTES_TO", integration=r.get("integration_type"))

    # LAMBDA -[USES_LAYER]-> LAMBDA_LAYER (types the dependency the cert kept as a property;
    # the pyiceberg-nessie-deps / Iceberg layer becomes a first-class visible node)
    for n in _exp_lam:
        farn = f"arn:aws:lambda:us-east-1:{ACCOUNT}:function:{n['id']}"
        for lyr in n.get("layers", []):     # "name:version" tails (live_lambda strips :layer:)
            base = lyr.rsplit(":", 1)[0] if ":" in lyr else lyr
            larn = f"arn:aws:lambda:us-east-1:{ACCOUNT}:layer:{base}"
            if larn in _layer_arns:
                E(farn, larn, "USES_LAYER",
                  version=(lyr.rsplit(":", 1)[-1] if ":" in lyr else None))

    # SCHEDULE -[TRIGGERS]-> target (EventBridge Scheduler -- distinct service from Events rules)
    _sched_targets = _lambda_arns | _sqs_arns | _sns_arns | _sfn_arns | _dynamo_arns
    for s in live_schedules():
        ta = s.get("target_arn")
        tb = re.sub(r"(:function:[^:]+):.*$", r"\1", ta) if ta else None  # strip lambda alias/ver
        if tb and tb in _sched_targets:
            E(s["arn"], tb, "TRIGGERS", via="scheduler")

    # event-source-mapping SOURCE -[TRIGGERS]-> LAMBDA (SQS / DynamoDB-stream -- the cert
    # modeled only the ESM DLQ/OnFailure side; this adds the actual trigger source)
    try:
        for esm in _paged(lc, "list_event_source_mappings", "EventSourceMappings",
                          frame="lambda.list_event_source_mappings(triggers)"):
            src, fn = esm.get("EventSourceArn"), esm.get("FunctionArn")
            if not (src and fn):
                continue
            fnb = re.sub(r"(:function:[^:]+):.*$", r"\1", fn)
            if fnb not in _lambda_arns:
                continue
            if ":sqs:" in src and src in _sqs_arns:
                E(src, fnb, "TRIGGERS", src_kind="sqs")
            elif "/stream/" in src and ":dynamodb:" in src:
                tbl = src.split("/stream/")[0]
                if tbl in _dynamo_arns:
                    E(tbl, fnb, "TRIGGERS", src_kind="dynamodb-stream")
    except Exception:
        pass

    # S3_BUCKET -[NOTIFIES]-> SNS_TOPIC | SQS_QUEUE (cert modeled only S3->Lambda NOTIFIES)
    for n in _s3_nodes:
        notification = _read_s3_notification_configuration(s3c, n["id"])
        if notification["state"] != "READ":
            continue
        nc = notification["configuration"]
        barn = f"arn:aws:s3:::{n['id']}"
        for tc in nc.get("TopicConfigurations", []):
            if tc.get("TopicArn") in _sns_arns:
                E(barn, tc["TopicArn"], "NOTIFIES", msg_target="sns")
        for qc in nc.get("QueueConfigurations", []):
            if qc.get("QueueArn") in _sqs_arns:
                E(barn, qc["QueueArn"], "NOTIFIES", msg_target="sqs")

    # LAMBDA -[IN_VPC]-> SECURITY_GROUP + LAMBDA -[INVOKES]-> LAMBDA. VpcConfig AND env
    # Variables both ship in the list_functions response -> ONE paginated call, no per-fn describe.
    _lam_name_arn = {x["id"]: f"arn:aws:lambda:us-east-1:{ACCOUNT}:function:{x['id']}" for x in _exp_lam}
    try:
        for _pg in lc.get_paginator("list_functions").paginate():
            for _fn in _pg["Functions"]:
                farn = re.sub(r"(:function:[^:]+):.*$", r"\1", _fn.get("FunctionArn") or "")
                for sg in (_fn.get("VpcConfig") or {}).get("SecurityGroupIds", []):
                    if sg in _sg_by_id:
                        E(farn, _sg_by_id[sg], "IN_VPC", via="security_group")
                # LAMBDA -[INVOKES]-> LAMBDA: an env value naming another live function = a
                # configured invoke target (same signal-class as the existing SM-arn->TRIGGERS scan)
                for _k, _v in ((_fn.get("Environment") or {}).get("Variables", {}) or {}).items():
                    if not isinstance(_v, str):
                        continue
                    tgt = None
                    if _v in _lambda_arns:
                        tgt = re.sub(r"(:function:[^:]+):.*$", r"\1", _v)
                    elif _v in _lam_name_arn:
                        tgt = _lam_name_arn[_v]
                    if tgt and tgt != farn:
                        E(farn, tgt, "INVOKES", via_env=_k)
    except Exception:
        pass

    # ECS_TASK_DEFINITION -[ASSUMES]-> IAM_ROLE (Fargate task + execution identity)
    for t in live_ecs_tasks():
        for rk in ("task_role_arn", "execution_role_arn"):
            ra = t.get(rk)
            if ra and ra in _role_arns:
                E(t["arn"], ra, "ASSUMES", role_kind=rk.replace("_arn", ""))

    # VPC_ENDPOINT -[USES_SG]-> SECURITY_GROUP
    for ve in live_vpc_endpoints():
        for sg in ve.get("sg_ids", []):
            if sg in _sg_by_id:
                E(ve["arn"], _sg_by_id[sg], "USES_SG")

    # OPLMCP.07 AC2 -- ALB-STACK edges (closes the blast-radius chain
    # Route53 -> LB -> listener -> TG -> EC2; EC2 already -> profile -> role above).
    # ROUTE53 -[ALIAS_TO]-> LB ; LISTENER -[ON_LB]-> LB + -[FORWARDS_TO]-> TG + -[USES_CERT]-> ACM(wild) ;
    # TG -[ON_LB]-> LB + -[TARGETS]-> EC2 ; LB -[USES_SG]-> SG + -[IN_SUBNET]-> subnet(wild).
    _lbs = live_lb()
    _lb_arns = {x["arn"] for x in _lbs if x.get("arn")}
    _lb_by_dns = {x["dns_name"].rstrip(".").lower(): x["arn"]
                  for x in _lbs if x.get("dns_name") and x.get("arn")}
    _tg_arns = {x["arn"] for x in live_lb_target_groups() if x.get("arn")}
    _ec2_by_id = {x["id"]: _node_arn("ec2", x) for x in live_ec2()}
    for lb in _lbs:
        for sg in lb.get("security_groups", []):
            if sg in _sg_by_id:
                E(lb["arn"], _sg_by_id[sg], "USES_SG")
        for sn in lb.get("subnets", []):
            E(lb["arn"], f"arn:aws:ec2:{lb.get('region', 'us-east-1')}:{ACCOUNT}:subnet/{sn}",
              "IN_SUBNET", wildcard=True)
    for ls in live_lb_listeners():
        if ls.get("load_balancer_arn") in _lb_arns:
            E(ls["arn"], ls["load_balancer_arn"], "ON_LB")
        for _tg in ls.get("forward_target_group_arns", []):
            if _tg in _tg_arns:
                E(ls["arn"], _tg, "FORWARDS_TO")
        for _cert in ls.get("certificate_arns", []):
            E(ls["arn"], _cert, "USES_CERT", wildcard=True)
    for tg in live_lb_target_groups():
        for lbarn in tg.get("load_balancer_arns", []):
            if lbarn in _lb_arns:
                E(tg["arn"], lbarn, "ON_LB")
        for tid in tg.get("targets", []):
            if tid in _ec2_by_id:
                E(tg["arn"], _ec2_by_id[tid], "TARGETS")
    for rr in live_route53_records():
        # EXACT alias-target dns match only: an alias target IS an exact dns-name, so a
        # fuzzy endswith is a latent mis-alias FP (CTO arch-gate hardening). Normalize the
        # one AWS-injected prefix -- an IPv6/dualstack alias target to an ALB carries a
        # leading "dualstack." -- so the resolver stays EXACT/deterministic (never fuzzy)
        # and doesn't false-NEGATIVE-miss a dualstack alias edge (CTO-endorsed robustness).
        _dns = rr.get("alias_target_dns", "").lower()
        if _dns.startswith("dualstack."):
            _dns = _dns[len("dualstack."):]
        _tgt = _lb_by_dns.get(_dns)
        if _tgt:
            E(rr["arn"], _tgt, "ALIAS_TO")

    # {SERVICE_PRINCIPAL|EXTERNAL_PRINCIPAL|IAM_*} -[CAN_ASSUME]-> IAM_ROLE
    # (the trust-policy / assume-role graph -- the IAM typing gap: who-can-assume-what,
    # surfacing OIDC/SAML federation + cross-account trust as typed principal nodes/findings)
    try:
        for _pg in iamc.get_paginator("list_roles").paginate():
            for _r in _pg["Roles"]:
                if _r.get("Path", "/").startswith("/aws-service-role/"):
                    continue
                _rarn = _r["Arn"]
                _doc = _r.get("AssumeRolePolicyDocument") or {}
                _stmts = _doc.get("Statement", [])
                if isinstance(_stmts, dict):
                    _stmts = [_stmts]
                for _st in _stmts:
                    if _st.get("Effect") != "Allow":
                        continue
                    _pr = _st.get("Principal", {})
                    _vals = []
                    if isinstance(_pr, dict):
                        for _v in _pr.values():
                            _vals += _v if isinstance(_v, list) else [_v]
                    elif isinstance(_pr, str):
                        _vals = [_pr]
                    for _pk in _vals:
                        if not _pk:
                            continue
                        _tgt, _pt, _sub, _find = _classify_principal(_pk)
                        _ex = {"via": "trust-policy"}
                        if _find:
                            _ex["finding_class"] = _find
                        if _sub:
                            _ex["principal_sub"] = _sub
                        E(_tgt, _rarn, "CAN_ASSUME", **_ex)
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
            except Exception as _e:
                # LOUD, not silent (NFRA_GCONTR EC2-WRITES root-cause 2026-06-16):
                # a perm gap here (e.g. iam:GetInstanceProfile denied on the Fargate
                # derive role) silently yields 0 roles -> 0 EC2 consumers -> 0
                # EC2-WRITES edges ESTATE-WIDE with NO error -- the exact silent-
                # failure class that hid the EC2-producer blind spot for months. Log
                # which profile + the error so a future derive perm-gap is VISIBLE,
                # never a silent graph-completeness hole.
                print(f"WARN: EC2_WRITES_PROFILE_RESOLVE_FAIL profile={prof} "
                      f"err={type(_e).__name__}: {_e} -- EC2 consumers of this profile's "
                      f"role(s) get 0 WRITES edges (check iam:GetInstanceProfile on the derive role)",
                      file=sys.stderr)
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
    # WAVE-4: CAN_ASSUME principals appear on the SOURCE side (trust-policy graph) -- type
    # them too so the edge's principal end is a typed node (0-dangling) + findings surface.
    find_of.update({e["source"]: e.get("finding_class") for e in edges
                    if e["edge_type"] == "CAN_ASSUME" and e.get("finding_class")})
    prin_targets = {e["target"] for e in edges if e["edge_type"] in ("GRANTS", "SUBSCRIBES")}
    prin_targets |= {e["source"] for e in edges if e["edge_type"] == "CAN_ASSUME"}
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
    flat_nodes = []  # for the grain sentinel (NFRA_GRAPHS D5 / AC-GRAIN)
    for cls, d in cd.items():
        ns = d.get("nodes", [])
        per_class[cls] = len(ns)
        for n in ns:
            drift[n.get("drift_class", "?")] += 1
            if not n.get("type"):
                untyped += 1
            flat_nodes.append(n)
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
    # AC-GRAIN sentinel (NFRA_GRAPHS D5): structural wrong-grain catch (e.g. an
    # S3 object-key minted as an S3_BUCKET). Additive metric; cmd_metrics hard-fails on it.
    grain = {"passed": True, "violations": []}
    try:
        from grain_sentinel import run_grain_sentinel, IDENTITY_FORMAT_INVARIANTS  # noqa: F401
        _gr = run_grain_sentinel(flat_nodes)  # AC-GRAIN.1 always; AC-GRAIN.2 when a baseline is supplied
        grain = {"passed": _gr.passed,
                 "violations": [{"bar": v.bar, "node_type": v.node_type,
                                 "detail": v.detail, "samples": v.samples}
                                for v in _gr.violations]}
    except Exception as _e:  # sentinel import/runtime issue must not break metrics
        grain = {"passed": None, "error": str(_e)}
    return {
        "node_total": sum(per_class.values()), "edge_total": len(edges), "untyped": untyped,
        "per_class": per_class, "drift_distribution": dict(drift),
        "edge_types": dict(Counter(e["edge_type"] for e in edges)),
        "security_findings": findings,
        "grain": grain,
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
    m = compute_metrics(graph)
    print(json.dumps(m, indent=2, default=str))
    # AC-GRAIN hard-fail (NFRA_GRAPHS D5): a wrong-grain class fails the run.
    g = m.get("grain", {})
    if g.get("passed") is False:
        print("\nGRAIN-SENTINEL: FAIL — wrong-grain class detected (AC-GRAIN). See grain.violations.",
              file=sys.stderr)
        sys.exit(3)

def cmd_diff(args):
    ga = json.load(open(args.prior))
    gb = json.load(open(args.current))
    print(json.dumps(compute_diff(ga, gb), indent=2, default=str))


def cmd_contract_diff(args):
    """NFRA_GCONTR Q1+Q2: the value-layer never-widen diff. Q1 snapshot-diffs the
    WRITES edges into each contracted artifact's bucket(s); Q2 JOINs the delta +
    observed-at-HEAD writers against globgrph.graph_contracts and classifies
    CLEAN / WATCH / SANCTIONED / UNSANCTIONED. ADVISORY (exit 0) by default --
    the comp-surface-check commit-time gate is the warn surface; the hard-block
    ramp-flip is a later one-line CTO call. Engine: contract_engine.py."""
    import datetime as _dt
    try:
        import contract_engine as ce
    except Exception as e:  # pragma: no cover
        print(f"ADVISORY: contract_engine unavailable ({type(e).__name__}: {e}) -- skipping.")
        return 0

    contracts, cstatus = ce.load_contracts()
    if cstatus == "absent":
        print("comp-aws contract-diff: globgrph.graph_contracts NOT created yet "
              "(NFRA_GCONTR TO-2 table stand-up pending / in-VPC create). Nothing to diff. "
              "(advisory, exit 0)")
        return 0
    if cstatus.startswith("unavailable"):
        print(f"ADVISORY: graph_contracts unreachable ({cstatus}) -- skipping (never block).")
        return 0
    if not contracts:
        print("comp-aws contract-diff: graph_contracts table EXISTS but holds 0 active rows "
              "(CVO TO-3 authoring pending). No contracted surfaces to evaluate. (advisory)")
        return 0

    base_ref = getattr(args, "since", None)
    cur_ref = getattr(args, "current_ref", None) or "latest"
    try:
        cur = ce.load_graph_snapshot(cur_ref)
        base = ce.load_graph_snapshot(base_ref) if base_ref else None
    except Exception as e:
        print(f"ADVISORY: could not load graph snapshot(s) ({type(e).__name__}: {e}) -- skipping.")
        return 0

    # window: [baseline date .. today] when --since given, else today only.
    today = _dt.date.today()
    if base_ref and len(str(base_ref)) >= 8 and str(base_ref)[:8].isdigit():
        try:
            start = _dt.date(int(base_ref[:4]), int(base_ref[4:6]), int(base_ref[6:8]))
        except Exception:
            start = today
    else:
        start = today
    window = (start, today)

    q1 = ce.q1_writes_diff(base, cur, contracts)
    q2 = ce.q2_join(contracts, q1, window=window)

    if getattr(args, "json", False):
        merged = {cid: {**q1.get(cid, {}), **q2.get(cid, {})} for cid in q1}
        print(json.dumps({"window": [str(window[0]), str(window[1])],
                          "baseline": base_ref or None, "current": cur_ref,
                          "contracts": merged}, indent=2, default=str))
        return 0

    print(f"comp-aws contract-diff  (window {window[0]}..{window[1]}; "
          f"baseline={base_ref or '(none -- observed-at-HEAD only)'}; current={cur_ref})\n")
    order = {"UNSANCTIONED": 0, "SANCTIONED": 1, "WATCH": 2, "CLEAN": 3}
    for cid in sorted(q2, key=lambda k: (order.get(q2[k]["status"], 9), k)):
        v = q2[cid]
        d = q1.get(cid, {})
        tag = {"UNSANCTIONED": "UNSANCTIONED", "SANCTIONED": "SANCTIONED",
               "WATCH": "WATCH", "CLEAN": "OK"}[v["status"]]
        print(f"{tag}: {cid}  [canonical_writer={v['canonical_writer']}]")
        print(f"    buckets: {', '.join(d.get('buckets', []))}")
        if d.get("added"):
            print(f"    +added writers: {[r for r, _ in d['added']]}")
        if d.get("removed"):
            print(f"    -removed writers: {[r for r, _ in d['removed']]}")
        if v["forbidden_hits"] or v["added_forbidden"]:
            print(f"    FORBIDDEN present: observed={v['forbidden_hits']} added={v['added_forbidden']}")
        if v["status"] == "WATCH":
            print(f"    non-canonical (advisory): {len(v['intruders'])} role(s) hold s3:put "
                  f"(shared-bucket noise)")
        print(f"    -> {v['reason']}")
        print()

    uns = [cid for cid in q2 if q2[cid]["status"] == "UNSANCTIONED"]
    print(f"summary: {len(uns)} UNSANCTIONED, "
          f"{sum(1 for c in q2 if q2[c]['status']=='SANCTIONED')} SANCTIONED, "
          f"{sum(1 for c in q2 if q2[c]['status']=='WATCH')} WATCH, "
          f"{sum(1 for c in q2 if q2[c]['status']=='CLEAN')} CLEAN  "
          f"(ADVISORY -- exit 0; hard-block flip deferred to CTO ramp)")
    return 0

# ---------------------------------------------------------------------------
# SCORE -- P/R/F1 vs certified oracle.  Oracle = ground truth.
# ---------------------------------------------------------------------------
def _load_yaml(p):
    import yaml
    return yaml.safe_load(open(p, encoding="utf-8"))


def _recall(tp: int, fn: int) -> float:
    """Recall is the ONLY set-metric computable offline.

    (`_f1(tp, fp, fn)` is deliberately gone. Offline, `fp` is not a false positive --
    it is an UNRECONCILED disagreement -- so precision and F1 have no honest value.
    The ec2 leg used to launder this as `_f1(tp, 0, fn)`, hardcoding fp=0 and pinning
    declared_f1 to a permanent 1.0000. A control that has only ever printed one value
    is not a control.)
    """
    return tp / (tp + fn) if (tp + fn) else 0.0


def _git_iso(rev_or_path, is_path: bool = False) -> str | None:
    """Committer-date of a rev, or of a path's last commit. Local git, no network."""
    args = (["git", "log", "-1", "--format=%cI", "--", str(rev_or_path)] if is_path
            else ["git", "show", "-s", "--format=%cI", str(rev_or_path)])
    try:
        r = subprocess.run(args, cwd=str(WS), capture_output=True, text=True, timeout=20)
        return r.stdout.strip() if r.returncode == 0 and r.stdout.strip() else None
    except Exception:
        return None


def _fixture_vintage(path: Path, meta: dict) -> dict:
    """Resolve a fixture's as_of. NEVER from mtime.

    A6/U3. U3 RESOLVED 2026-07-10: NO fixture carries an `as_of` field (0 of 6 yaml).
    All three scored fixtures DO carry `meta.tf_commit_at_audit` -- a commit-ish, which
    per CLAUDE.md Rule 22 is a STRONGER vintage than a bare date.

    mtime is a fact about the filesystem, not about the audit: `git checkout`, a copy, or
    a `touch` rewrites it without a human re-auditing anything. Precedence:
      1. meta.as_of                      (honored if a human ever adds it)
      2. git last-commit date OF THE FIXTURE FILE   (when its assertions last changed)
      3. UNKNOWN -> FAIL CLOSED (treated as stale)
    `meta.tf_commit_at_audit` is always reported: it names WHICH terraform tree the hand
    audit was taken against, which mtime and file-date both fail to record.
    """
    as_of, src = None, None
    if meta.get("as_of"):
        as_of, src = str(meta["as_of"]), "meta.as_of"
    else:
        g = _git_iso(path, is_path=True)
        if g:
            as_of, src = g, "git:last-commit-of-fixture"

    age_days = None
    if as_of:
        try:
            dt = datetime.fromisoformat(as_of.replace("Z", "+00:00"))
            age_days = (datetime.now(timezone.utc) - dt).days
        except Exception:
            as_of, src = None, None

    fver = str(meta.get("fixture_version", "UNKNOWN"))
    # DECLARATIVE DRIFT (found 2026-07-10): the scorer loads fixtures by HARDCODED
    # FILENAME, and in all 3 the filename version disagrees with meta.fixture_version
    # (s3 file v1.1 / meta 1.5; iam-ec2 file v0.1 / meta 0.2; sfn file v0.1 / meta 0.2).
    # The name is a lie about the content. Print the content's version, flag the skew.
    name_skew = fver not in path.name

    try:
        rel = str(path.relative_to(WS)).replace("\\", "/")
    except ValueError:
        rel = path.name   # fixture outside the workspace tree (e.g. a test tmp path)
    return {
        "path": rel,
        "fixture_version": fver,
        "filename_version_skew": name_skew,
        "tf_commit_at_audit": str(meta.get("tf_commit_at_audit", "UNKNOWN")),
        "as_of": as_of or "UNKNOWN",
        "as_of_source": src or "UNRESOLVED",
        "age_days": age_days,
        "stale": (age_days is None) or (age_days > FIXTURE_STALE_DAYS),
    }


def _load_fixture(filename: str) -> tuple[dict, dict]:
    p = SHAPES / filename
    doc = _load_yaml(p)
    return doc, _fixture_vintage(p, doc.get("meta", {}) or {})

def score_s3():
    """Node-enumeration + key-attr agreement vs the s3 oracle. OFFLINE adjudication."""
    oracle, vintage = _load_fixture("s3-hand-audit-fixture-v1.1.yaml")
    truth = {b["bucket_name"]: b for b in oracle["s3_buckets"]}
    derived = {n["id"]: n for n in derive_class("s3")["nodes"]}
    tset, dset = set(truth), set(derived)
    tp_nodes = tset & dset
    missed = sorted(tset - dset)        # oracle bucket the compiler MISSED -> real recall miss
    unreconciled = sorted(dset - tset)  # derived, not in fixture -> NOBODY HAS LOOKED
    # attribute correctness within matched nodes (versioning + PAB = the certified axes)
    attr_total = attr_ok = 0
    for b in tp_nodes:
        for axis, dkey in [("versioning_enabled", "versioning_enabled"), ("public_access_block", "public_access_block")]:
            if axis in truth[b]:
                attr_total += 1
                if derived[b].get(dkey) == truth[b][axis]:
                    attr_ok += 1
    return {
        "class": "s3", "_fixture": vintage,
        "node_tp": len(tp_nodes), "node_fn": len(missed),
        "node_recall": round(_recall(len(tp_nodes), len(missed)), 4),
        "node_precision": UNAVAILABLE, "node_f1": UNAVAILABLE,
        "attr_accuracy": round(attr_ok / attr_total, 4) if attr_total else None,
        "attr_checked": attr_total,
        "missed": missed,
        "unreconciled": unreconciled, "unreconciled_count": len(unreconciled),
    }

def score_iam_ec2():
    oracle, vintage = _load_fixture("iam-ec2-hand-audit-fixture-v0.1.yaml")
    res = {"_fixture": vintage}
    # --- IAM role enumeration ---
    iam_truth_count = oracle["iam_roles"]["customer_role_count"]
    derived_iam = derive_class("iam")["nodes"]
    di = len(derived_iam)
    truth_overperm = {o["role"] for o in oracle["iam_cataloged_findings_HELD"]["overperm_roles"]}
    derived_overperm = {n["id"] for n in derived_iam if n.get("broad_managed")}
    tp = len(truth_overperm & derived_overperm)
    overperm_missed = sorted(truth_overperm - derived_overperm)
    overperm_unrec = sorted(derived_overperm - truth_overperm)
    res["iam"] = {
        "truth_role_count": iam_truth_count, "derived_role_count": di,
        # A4: `count_match` was computed, printed, and never entered any verdict -- a
        # 57-role discrepancy (111 truth vs 168 derived) had ZERO effect. It now BITES:
        # cmd_score treats a nonzero delta as an unreconciled condition.
        "count_match": di == iam_truth_count,
        "role_count_delta": di - iam_truth_count,
        "overperm_recall": round(_recall(tp, len(overperm_missed)), 4),
        "overperm_precision": UNAVAILABLE, "overperm_f1": UNAVAILABLE,
        "overperm_truth": sorted(truth_overperm), "overperm_derived": sorted(derived_overperm),
        "overperm_missed": overperm_missed,
        "unreconciled": overperm_unrec, "unreconciled_count": len(overperm_unrec),
        # PREDICATE MISMATCH, recorded on the face of the output (CVO 2026-07-10, live-verified).
        # The fixture's overperm_roles asserts EFFECTIVE PERMISSION ("wildcard-action",
        # "account-wide S3+Dynamo read/write/DELETE"). `broad_managed` (live_iam_roles:315)
        # tests whether an ATTACHED-MANAGED POLICY NAME contains "FullAccess"/"Administrator".
        # Those are different predicates. It is blind to all 376 inline policies in the
        # account and to the CONTENT of every customer-managed policy. A recall miss here
        # may mean the compiler is blind OR the fixture is stale, and this metric CANNOT
        # tell you which. Verified 2026-07-10: market-update-lambda-role's recall miss is
        # a genuine REMEDIATION (simulate-principal-policy -> implicitDeny on every
        # permission the fixture claims), not a compiler defect. Census that day: 0 roles
        # grant Action:*|svc:* on Resource:* via customer-managed or inline policy, so the
        # blindness is REAL BUT LATENT -- harm not demonstrated.
        "predicate_note": ("broad_managed tests POLICY NAME on attached-managed policies; the "
                           "fixture asserts EFFECTIVE PERMISSION. Different predicates. Blind to "
                           "inline policies and to customer-managed policy content."),
    }
    # --- EC2 enumeration ---
    decl_truth = {e["name"] for e in oracle["ec2_declared"]}
    derived_ec2 = derive_class("ec2")
    derived_declared = {n["name"] for n in derived_ec2["nodes"] if n.get("drift_class") == "DECLARED"}
    expected_no_live = {e["name"] for e in oracle["ec2_declared"] if "REMOVED" in (e.get("note") or "")}
    tp = len(decl_truth & (derived_declared | expected_no_live))
    ec2_missed = sorted(decl_truth - (derived_declared | expected_no_live))
    # A3: `_f1(tp, 0, fn)` hardcoded fp=0 -> declared_f1 was structurally 1.0000 and could
    # not detect a phantom EC2 instance. The set it ignored is exactly this one:
    ec2_unrec = sorted(derived_declared - decl_truth - expected_no_live)
    res["ec2"] = {
        "truth_declared": len(decl_truth), "derived_live": derived_ec2["counts"]["live"],
        "derived_declared": sorted(derived_declared),
        "declared_recall": round(_recall(tp, len(ec2_missed)), 4),
        "declared_precision": UNAVAILABLE, "declared_f1": UNAVAILABLE,
        "missed": ec2_missed,
        "unreconciled": ec2_unrec, "unreconciled_count": len(ec2_unrec),
        "live_no_declared": derived_ec2["counts"]["live_no_declared"],
    }
    return res

def score_stepfunctions():
    oracle, vintage = _load_fixture("stepfunctions-hand-audit-fixture-v0.1.yaml")
    truth = {sm["name"]: sm for sm in oracle.get("state_machines", [])}
    derived = {n["id"]: n for n in derive_class("stepfunctions")["nodes"]}
    tp_nodes = set(truth) & set(derived)
    node_missed = sorted(set(truth) - set(derived))
    node_unrec = sorted(set(derived) - set(truth))
    attr_total = attr_ok = 0
    for name in tp_nodes:
        t, d = truth[name], derived[name]
        for axis in ("machine_type", "definition_hash", "tf_managed"):
            if axis in t:
                attr_total += 1
                if str(d.get(axis, "")) == str(t[axis]):
                    attr_ok += 1
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
    inv_missed = sorted(truth_inv_arns - derived_inv_arns)
    inv_unrec = sorted(derived_inv_arns - truth_inv_arns)
    return {
        "class": "stepfunctions", "_fixture": vintage,
        "node_tp": len(tp_nodes), "node_fn": len(node_missed),
        "node_recall": round(_recall(len(tp_nodes), len(node_missed)), 4),
        "node_precision": UNAVAILABLE, "node_f1": UNAVAILABLE,
        "attr_accuracy": round(attr_ok / attr_total, 4) if attr_total else None,
        "attr_checked": attr_total,
        "activity_count_match": len(derived_acts) == act_truth_count,
        "activity_derived": len(derived_acts), "activity_truth": act_truth_count,
        "invokes_tp": inv_tp, "invokes_fn": len(inv_missed),
        "invokes_recall": round(_recall(inv_tp, len(inv_missed)), 4),
        "invokes_precision": UNAVAILABLE, "invokes_f1": UNAVAILABLE,
        "invokes_missed": inv_missed,
        "missed": node_missed,
        "unreconciled": sorted(set(node_unrec) | set(inv_unrec)),
        "unreconciled_count": len(node_unrec) + len(inv_unrec),
    }

SCORERS = {"s3": score_s3, "iam-ec2": score_iam_ec2, "stepfunctions": score_stepfunctions}
# `iam` and `ec2` are real CLASSES covered by the composite `iam-ec2` scorer. Without this
# they would report UNSCORED, which would be false.
SCORER_ALIASES = {"iam": "iam-ec2", "ec2": "iam-ec2"}

# ---------------------------------------------------------------------------
def cmd_classes(args):
    print("Supported resource classes:")
    for c in CLASSES:
        print(f"  {c:12} -> {CLASSES[c][1]}")
    print("\nCertified oracle scorers:", ", ".join(SCORERS))

# A7: the ARN->class map, hoisted to a module constant so arn_unreachable_classes()
# can COMPUTE the unreachable set rather than restate it. A hardcoded "8 classes have no
# ARN route" comment silently rots the moment someone adds a class.
_ARN_SERVICE_MAP = {
    "s3": "s3", "iam": "iam", "ec2": "ec2", "lambda": "lambda",
    "events": "eventbridge", "sns": "sns", "sqs": "sqs",
    "dynamodb": "dynamodb", "cloudfront": "cloudfront",
    "secretsmanager": "secrets", "kms": "kms",
    "logs": "logs", "cloudwatch": "cloudwatch", "states": "stepfunctions",
    # WAVE-4 expansion classes
    "apigateway": "apigw", "ecs": "ecs_task", "ssm": "ssm_document",
    "scheduler": "scheduler",
    # OPLMCP.07 AC2 -- ALB-stack
    "route53": "route53_record",
}
# the 3 ELB classes share one service token and are disambiguated by resource-path
_ELB_PREFIX_MAP = {
    "targetgroup/": "lb_target_group",
    "listener/": "lb_listener",
    "loadbalancer/": "lb",
}


def arn_unreachable_classes() -> list[str]:
    """CLASSES with no ARN route -> `derive --resource` can never reach them.

    COMPUTED from the maps above, so it cannot drift from CLASSES.
    """
    reachable = set(_ARN_SERVICE_MAP.values()) | set(_ELB_PREFIX_MAP.values())
    return sorted(set(CLASSES) - reachable)


def _arn_to_cls(arn: str) -> str | None:
    """Map an ARN to a CLASSES key for bounded derive. Returns None if unknown."""
    service = arn.split(":")[2] if arn.count(":") >= 2 else ""
    # OPLMCP.07 AC2: the 3 ELB classes share the 'elasticloadbalancing' service ->
    # distinguish by the resource-path so --resource on a TG/listener arn is exact.
    if service == "elasticloadbalancing":
        res = arn.split(":")[5] if arn.count(":") >= 5 else ""
        for prefix, cls in _ELB_PREFIX_MAP.items():
            if res.startswith(prefix):
                return cls
        # listener-rule/ (e.g. the .06 OIDC-bypass rules) + any future ELBv2 sub-type
        # are UNMODELED -> return None, NEVER phantom-classify as lb under a catch-all.
        return None
    return _ARN_SERVICE_MAP.get(service)


def cmd_derive(args):
    """Derive the graph. RETURN CONTRACT IS LOAD-BEARING -- do not change it.

    derive_runner.py:100 calls this IN-PROCESS and its return value IS the nightly's
    graph (-> commit_to_iceberg -> Nessie -> comp-kuzu's canonical surface). It returns
    a graph dict on success and {} on failure; main() must NEVER consume that as an exit
    code (see cmd_derive_cli). Nothing user-facing about persistence belongs in here --
    the nightly DOES persist, and a "NOT PERSISTED" banner printed here would write a
    falsehood into the nightly's log.
    """
    # One invocation is one read denominator. Repeated live_s3()/derive_edges() calls
    # share this cache, but a later in-process build must measure the world again.
    _S3_NOTIFICATION_CACHE.clear()

    # Bounded derive: --resource <arn> restricts to just that class (NFRA_GLOBGRPH Item-2b)
    resource_arn = getattr(args, "resource", None)
    if resource_arn:
        resource_cls = _arn_to_cls(resource_arn)
        if not resource_cls:
            # A7: was print + return {} -> main() discarded it -> rc 0. An unroutable ARN
            # exited SUCCESS. Name the unreachable classes: --resource is bounded OUTPUT,
            # not bounded WORK, and 8 of 30 classes have no ARN route at all.
            unreachable = arn_unreachable_classes()
            print(f"ERROR: cannot infer class from ARN: {resource_arn}", file=sys.stderr)
            print(f"  {len(unreachable)} of {len(CLASSES)} classes have NO ARN route and can never be "
                  f"reached via --resource:", file=sys.stderr)
            print(f"    {', '.join(unreachable)}", file=sys.stderr)
            print("  (an ELB listener-rule/ ARN is also unmodeled by design -- never "
                  "catch-all classified as 'lb')", file=sys.stderr)
            return {}
        # Run the single class derive; the full graph context is unavailable in bounded mode
        try:
            cd = derive_class(resource_cls)
            # Filter nodes to only the specific ARN
            nodes = [n for n in cd.get("nodes", []) if n.get("arn") == resource_arn or n.get("id") == resource_arn.split(":")[-1]]
            cd["nodes"] = nodes
            cd["counts"]["live"] = len(nodes)
        except Exception as e:
            print(f"ERROR: bounded derive failed: {e}", file=sys.stderr)
            return {}
        graph = {"meta": {"account": ACCOUNT, "classes": [resource_cls], "bounded_resource": resource_arn,
                          "edges_computed": False},
                 "classes_data": {resource_cls: cd}, "edges": []}
        if args.out:
            Path(args.out).write_text(json.dumps(graph, indent=2, default=str), encoding="utf-8")
            print(f"wrote {args.out}")
        print(f"  {resource_cls:12} bounded_derive arn={resource_arn} nodes={len(nodes)}")
        # A8/R5: a bounded derive computes NO relationships. Say so.
        print("  NOTE: bounded derive -- 0 edges computed (relationships require a full derive).")
        return graph

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
    graph["meta"]["edges_computed"] = bool(not args.cls and not getattr(args, "no_edges", False))
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
    else:
        # A8/R5 (exercised 2026-07-10: `derive --class lambda` returned a graph with NO
        # 'edges' key at all -- consumers doing .get("edges", []) read 0 relationships as
        # "this class has none"). Emit the key AND disclose that it was never computed.
        graph["edges"] = []
        why = "--class given" if args.cls else "--no-edges given"
        print(f"  edges        NOT COMPUTED ({why}) -- this graph carries 0 relationships.")
        print("               Edge derivation is a whole-account pass; run a full derive for edges.")
    graph["meta"]["s3_notification_reads"] = _s3_notification_read_summary()
    _print_s3_notification_read_summary()
    # AC-GRAIN refuse-to-emit (NFRA_GRAPHS D5): a full derive must not emit a
    # wrong-grain graph (e.g. an S3 object-key minted as an S3_BUCKET). Identity-
    # format bar only (no baseline here -> no magnitude false-fire); structurally
    # safe (an S3 bucket name cannot contain '/'). Mirrors derive_stitch's producer guard.
    try:
        from grain_sentinel import run_grain_sentinel
        _flat = [n for d in graph.get("classes_data", {}).values() for n in d.get("nodes", [])]
        _gr = run_grain_sentinel(_flat)
        if not _gr.passed:
            print("\n" + _gr.render(), file=sys.stderr)
            print("comp-aws derive: REFUSING to emit a wrong-grain graph (AC-GRAIN).", file=sys.stderr)
            sys.exit(2)
    except SystemExit:
        raise
    except Exception:
        pass  # sentinel import/runtime issue must not break a clean derive
    if args.out:
        Path(args.out).write_text(json.dumps(graph, indent=2, default=str), encoding="utf-8")
        print(f"\nwrote {args.out}")
    return graph


def cmd_derive_cli(args):
    """CLI seam over cmd_derive: carries the EXIT CODE and the persistence disclosure.

    Why a seam instead of changing cmd_derive: derive_runner.py:100 imports this module
    and calls cmd_derive() IN-PROCESS, consuming its RETURN VALUE as the nightly's graph.
    Making cmd_derive return an int would break the nightly; making main() exit on its
    dict is worse -- EXERCISED 2026-07-10:

        sys.exit(cmd_derive(args) or 0)
          success -> returns graph dict  -> rc 1  + whole graph dumped to stderr
          failure -> returns {}          -> rc 0
        i.e. EXACTLY INVERTED.

    So: cmd_derive keeps its contract; this wrapper owns the rc.
    """
    graph = cmd_derive(args)
    if not graph or not graph.get("meta"):
        return RC_DERIVE_ERROR

    # A9: `derive` PERSISTS NOTHING (exercised 2026-07-10: latest.txt ETag, snapshots/
    # object count, and the canonical DB mtime all unchanged across a derive). 89 of 188
    # parsed comp-aws invocations were `derive`; 5 were `snapshot`. An operator who
    # believes derive refreshed the projection is holding a stale graph and a fresh belief.
    #
    # U4 RESOLVED (source-confirmed) -- and it is why this wording is not "use snapshot":
    #   comp-kuzu reads the SERVED projection and nothing else (it is a thin client with no
    #   database path, NFRA_CLDGRPH round 5). Bare `snapshot` writes a tarball +
    #   snapshots/latest.txt -- artifacts the served projection is not built from, so telling
    #   an operator to "run snapshot to publish" would send them to a verb that does not move
    #   the surface they query. The surface moves when the served projection's pointer moves.
    if not args.out:
        print("\nNOT PERSISTED -- this derive was not published, and nothing downstream saw it.")
    else:
        print(f"\nNOT PUBLISHED -- {args.out} is a local file; no shared surface changed.")
    print("  comp-kuzu reads the SERVED projection, which still serves its previous vintage --")
    print("  the vintage its own VINTAGE line will state on your next read. To move THAT surface:")
    print("      comp-aws snapshot --commit-to-nessie   |   comp-aws iceberg-commit")
    print("      (or wait for the nightly derive_runner)")
    print("  NOTE: bare `comp-aws snapshot` does NOT move it -- it writes the tarball +")
    print("  snapshots/latest.txt, which the served projection is not built from.")
    return RC_OK


def _walk_metrics(d):
    """Yield (key, value) over a scorer result, skipping the _fixture provenance block."""
    for k, v in d.items():
        if k == "_fixture":
            continue
        if isinstance(v, dict):
            yield from _walk_metrics(v)
        else:
            yield k, v


def _print_fixture_banner(v: dict) -> None:
    """A6: the single fact required to interpret the output. Never omitted."""
    print(f"  FIXTURE  {v['path']}")
    print(f"           fixture_version={v['fixture_version']}  tf_commit_at_audit={v['tf_commit_at_audit']}")
    age = "unknown" if v["age_days"] is None else f"{v['age_days']}d"
    print(f"           as_of={v['as_of']}  (source: {v['as_of_source']})  age={age}")
    if v["filename_version_skew"]:
        print(f"           WARN: filename does not carry content version {v['fixture_version']} "
              f"-- the scorer loads this fixture by HARDCODED FILENAME.")
    if v["stale"]:
        reason = ("as_of UNRESOLVED -- failing closed" if v["age_days"] is None
                  else f"older than {FIXTURE_STALE_DAYS}d")
        print(f"           FIXTURE STALE ({reason}) -- ADVISORY. Staleness alone never fails the cert;")
        print("           UNRECONCILED does. Run `comp-aws score --reconcile-fixture` to produce a gap report.")


def _class_verdict(result: dict) -> tuple[list[str], int, list[str]]:
    """Return (tokens, unreconciled_total, recall_miss_labels)."""
    unrec, recall_misses, count_delta = 0, [], 0
    for k, v in _walk_metrics(result):
        if k == "unreconciled_count" and isinstance(v, int):
            unrec += v
        elif k == "role_count_delta" and isinstance(v, int):
            count_delta = v
        elif k.endswith("_recall") and isinstance(v, (int, float)) and v < 1.0:
            recall_misses.append(f"{k}={v:.4f}")
    tokens = []
    if unrec > 0:
        tokens.append("UNRECONCILED")
    if count_delta != 0:
        tokens.append("ROLE-COUNT-DELTA")
    if recall_misses:
        tokens.append("RECALL-MISS")
    if not tokens:
        tokens.append("PASS")
    return tokens, unrec, recall_misses


def cmd_score(args):
    """OFFLINE-ADJUDICATING cert. See module docstring before changing anything here.

    A5/A1: UNSCORED, INVALID, and PASS are distinguishable in BOTH token and exit code.
    They used to be rc=0 with a near-identical one-liner, so `score --class zzqq-nope`
    was recorded as PASS in org/compiler-tools-log.md.
    """
    if getattr(args, "reconcile_fixture", False):
        return cmd_reconcile_fixture(args)

    if args.cls:
        cls = SCORER_ALIASES.get(args.cls, args.cls)
        if cls in SCORERS:
            targets = [cls]
        elif args.cls in CLASSES:
            # A5: a REAL class with NO oracle. Not a pass. Not an error. UNMEASURED.
            print(f"UNSCORED: '{args.cls}' is a real resource class with NO certified oracle.")
            print("  Its derive correctness is UNMEASURED -- not verified, not clean.")
            print(f"  CERT COVERAGE: {len(SCORERS)} of {len(CLASSES)} classes have an oracle "
                  f"({', '.join(sorted(SCORERS))}).")
            return RC_UNSCORED
        else:
            print(f"INVALID CLASS: '{args.cls}' is not a resource class.", file=sys.stderr)
            print(f"  {len(CLASSES)} known classes: {', '.join(sorted(CLASSES))}", file=sys.stderr)
            return RC_INVALID
    else:
        targets = list(SCORERS)

    failed = False
    for t in targets:
        print(f"\n=== SCORE: {t} ===")
        r = SCORERS[t]()
        if r.get("_fixture"):
            _print_fixture_banner(r["_fixture"])
        print(json.dumps(r, indent=2, default=str))

        tokens, unrec, recall_misses = _class_verdict(r)
        print(f"\n  VERDICT [{t}]: {' + '.join(tokens)}")
        if unrec:
            print(f"    UNRECONCILED = {unrec}. The derive and the fixture disagree and NO HUMAN HAS")
            print("    LOOKED. This is neither a compiler false positive nor a fixture gap until")
            print("    someone says which. PRECISION is not computable offline and is not printed.")
        if recall_misses:
            print(f"    RECALL MISS: {', '.join(recall_misses)} -- the derive did not find something")
            print("    the fixture asserts. This IS well-defined offline.")
        if "PASS" not in tokens:
            failed = True

    # A5: the denominator, on the face of every run.
    print("\n=== CERT COVERAGE ===")
    pct = 100.0 * len(SCORERS) / len(CLASSES)
    print(f"  {len(SCORERS)} of {len(CLASSES)} resource classes have a certified oracle ({pct:.1f}%).")
    print(f"  {len(CLASSES) - len(SCORERS)} classes are UNMEASURED. UNMEASURED IS NOT CLEAN.")
    # A3/A5: no aggregate. It averaged heterogeneous metrics across 3 of 30 classes, was
    # pushed DOWN by legitimate estate growth and propped UP by a leg pinned to 1.0.
    print("  No AGGREGATE is emitted (a number whose denominator is invisible).")
    return RC_FAIL if failed else RC_OK


# ---------------------------------------------------------------------------
# RECONCILE -- the SEPARATE, EXPLICIT, NETWORKED pass. Writes a gap report for a human.
# ---------------------------------------------------------------------------
def _exists_s3(name: str) -> bool | None:
    try:
        _boto("s3").head_bucket(Bucket=name)
        return True
    except Exception as e:
        return False if "404" in str(e) or "Not Found" in str(e) else None


def _exists_ec2(name: str) -> bool | None:
    try:
        r = _boto("ec2").describe_instances(Filters=[{"Name": "tag:Name", "Values": [name]}])
        return bool([i for res in r["Reservations"] for i in res["Instances"]])
    except Exception:
        return None


def _exists_iam_role(name: str) -> bool | None:
    try:
        _boto("iam").get_role(RoleName=name)
        return True
    except Exception as e:
        return False if "NoSuchEntity" in str(e) else None


_EXISTS = {"s3": _exists_s3, "ec2": _exists_ec2, "iam": _exists_iam_role}


def cmd_reconcile_fixture(args):
    """Classify each UNRECONCILED entry as EXISTS (fixture gap) or ABSENT (compiler phantom).

    THIS TOOL NEVER AMENDS A FIXTURE. The fixture's authority comes from a hand having
    made it; a hand-audit a tool can rewrite is the derive's opinion with a yaml
    extension. We write a report; a human merges it.

    Note the epistemics: `head_bucket` and the derive both ask AWS. They are NOT
    independent for the failure mode "AWS is right and the derive is right." They DO
    discriminate the realistic phantom (a mangled name / an object key minted as a
    bucket -> 404). Never let this classification touch a precision number.
    """
    targets = [SCORER_ALIASES.get(args.cls, args.cls)] if args.cls else list(SCORERS)
    report = {"generated_by": "comp-aws score --reconcile-fixture", "classes": {}}
    phantoms = 0

    for t in targets:
        if t not in SCORERS:
            continue
        r = SCORERS[t]()
        legs = {k: v for k, v in r.items() if isinstance(v, dict) and k != "_fixture"} or {t: r}
        report["classes"][t] = {"fixture": r.get("_fixture"), "entries": []}
        for leg_name, leg in legs.items():
            probe = _EXISTS.get(leg_name if leg_name in _EXISTS else t)
            for entry in leg.get("unreconciled", []) or []:
                if probe is None:
                    verdict = "UNKNOWN (no existence probe for this class)"
                else:
                    ex = probe(entry)
                    verdict = ("EXISTS -> FIXTURE GAP" if ex is True else
                               "ABSENT -> COMPILER PHANTOM" if ex is False else
                               "UNKNOWN (probe inconclusive)")
                if verdict.startswith("ABSENT"):
                    phantoms += 1
                report["classes"][t]["entries"].append(
                    {"leg": leg_name, "entry": entry, "verdict": verdict})
                print(f"  [{t}/{leg_name}] {entry}: {verdict}")

    out = Path(args.report_out) if getattr(args, "report_out", None) else \
        SHAPES / "reconcile-gap-report.json"
    out.write_text(json.dumps(report, indent=2, default=str), encoding="utf-8")
    print(f"\nGAP REPORT -> {out}")
    print("  A HUMAN merges this into the fixture. This command did NOT amend it.")
    if phantoms:
        print(f"  {phantoms} COMPILER PHANTOM(S) -- the derive emitted something that does not exist.")
        return RC_FAIL
    return RC_OK

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

    # TO-F3 (NFRA_GLOBGRPH ruling F3): opt-in --commit-to-nessie so an ad-hoc
    # derive lands as a Nessie commit BY CONSTRUCTION instead of only the tarball
    # side-channel (CVO verdict be17d49eb leg-3: ad-hoc derives never reached
    # Nessie). Default (flag absent) is unchanged. Reuses the importable
    # derive_runner.commit_to_iceberg (the canonical 8-field-schema + retry/backoff
    # writer the nightly + the Lambda agree on -- NOT the stale 7-field
    # cmd_iceberg_commit). F5 doctrine: a re-derive is graph maintenance, not
    # verification; read-your-own-writes stays on served-artifact / live AWS.
    if getattr(args, "commit_to_nessie", False):
        import time as _time
        gg = Path(__file__).resolve().parents[3] / "infra" / "aws" / "globgrph"
        sys.path.insert(0, str(gg))
        import derive_runner  # noqa: E402  (path inserted above; comp_aws_cli already loaded -> no circular re-exec)
        batch_ts = int(_time.time() * 1000)
        print(f"INFO: --commit-to-nessie: committing ad-hoc derive to Nessie ({derive_runner.NESSIE_URI})")
        _cat = derive_runner.commit_to_iceberg(graph, batch_ts)
        # TO-F6: stamp the branch-head marker so the canonical reader sees this commit.
        try:
            derive_runner.stamp_branch_head_marker(_cat, "comp_aws_snapshot")
        except Exception as _e:
            print(f"WARN: MARKER_STAMP_FAIL err={_e}")
        print("OK: ad-hoc derive committed to Nessie -- re-derive is now a Nessie "
              "version (the canonical surface serves it on next rebuild), not just "
              "the tarball side-channel.")

def cmd_iceberg_commit(args):
    """
    Write a graph JSON to Iceberg tables via pyiceberg + Nessie catalog.
    NFRA_GLOBGRPH P1: populates graph_nodes / graph_edges for AC2 (atomic versioning).
    Usage: comp-aws iceberg-commit [--graph FILE] [--nessie-uri URI] [--warehouse URI]
    If --graph is omitted, derives fresh (full derive then commit).
    """
    try:
        from pyiceberg.catalog.rest import RestCatalog  # type: ignore
        import pyarrow as pa                             # type: ignore
    except ImportError as e:
        # A1: this printed ERROR and returned None -> rc 0. A commit that never happened
        # exited SUCCESS.
        print(f"ERROR: pyiceberg not installed: {e}", file=sys.stderr)
        print("  Install: pip install 'pyiceberg[pyarrow]' pyarrow", file=sys.stderr)
        return RC_DERIVE_ERROR

    import time
    nessie_uri    = args.nessie_uri or "http://nessie.opal-globgrph.local:19120/api/v2"
    warehouse_uri = args.warehouse  or "s3://opal-313476888478-globgrph/warehouse"  # noqa: F841  reference-only (catalog uses warehouse name "default"; see comment below)
    branch        = args.branch     or "main"
    batch_ts      = int(time.time() * 1000)

    # Load or derive graph
    if args.graph:
        graph = json.loads(Path(args.graph).read_text(encoding="utf-8"))
    else:
        print("No --graph provided; running full derive...")
        graph = cmd_derive(argparse.Namespace(cls=None, out=None, resource=None))

    # Flatten all nodes
    all_nodes: list[dict] = []
    for cls_data in graph.get("classes_data", {}).values():
        for node in cls_data.get("nodes", []):
            all_nodes.append(node)

    all_edges: list[dict] = graph.get("edges", [])

    print(f"  iceberg-commit: {len(all_nodes)} nodes, {len(all_edges)} edges -> Nessie {nessie_uri}")

    # Nessie 0.96.x: Iceberg REST endpoint at /iceberg/{branch}; NessieCatalog removed in pyiceberg 0.7+
    # warehouse="default" matches NESSIE_CATALOG_DEFAULT_WAREHOUSE in ECS task def.
    # warehouse_uri (S3 URI) is for reference only; catalog lookup uses the name.
    base = nessie_uri.replace("/api/v2", "")
    catalog = RestCatalog(name="nessie", **{
        "uri": f"{base}/iceberg/{branch}", "warehouse": "default"
    })

    ns = "globgrph"
    try:
        catalog.create_namespace(ns)
    except Exception:
        pass

    # Ensure / load graph_nodes table
    from pyiceberg.schema import Schema
    from pyiceberg.types import NestedField, StringType, LongType
    nodes_schema = Schema(
        NestedField(1, "node_id",     StringType(), required=True),
        NestedField(2, "arn",         StringType(), required=False),
        NestedField(3, "node_type",   StringType(), required=True),
        NestedField(4, "name",        StringType(), required=False),
        NestedField(5, "layer",       StringType(), required=False),
        NestedField(6, "drift_class", StringType(), required=False),
        NestedField(7, "snapshot_ts", LongType(),   required=False),
    )
    nodes_id = (ns, "graph_nodes")
    try:
        nodes_table = catalog.load_table(nodes_id)
    except Exception:
        nodes_table = catalog.create_table(nodes_id, schema=nodes_schema)

    edges_schema = Schema(
        NestedField(1, "src_id",      StringType(), required=True),
        NestedField(2, "dst_id",      StringType(), required=True),
        NestedField(3, "edge_type",   StringType(), required=True),
        NestedField(4, "layer",       StringType(), required=False),
        NestedField(5, "snapshot_ts", LongType(),   required=False),
    )
    edges_id = (ns, "graph_edges")
    try:
        edges_table = catalog.load_table(edges_id)
    except Exception:
        edges_table = catalog.create_table(edges_id, schema=edges_schema)

    # Write nodes
    if all_nodes:
        nodes_table.overwrite(pa.table({
            "node_id":     [n.get("id", "")       for n in all_nodes],
            "arn":         [n.get("arn", "")       for n in all_nodes],
            "node_type":   [n.get("type", "")      for n in all_nodes],
            "name":        [n.get("name", "")      for n in all_nodes],
            "layer":       [n.get("layer", "aws")  for n in all_nodes],
            "drift_class": [n.get("drift_class","") for n in all_nodes],
            "snapshot_ts": [batch_ts               for _ in all_nodes],
        }))
        print(f"  WRITE OK: {len(all_nodes)} nodes -> graph_nodes")

    # Write edges
    if all_edges:
        # A11 (CVO 2026-07-10, exercised): this read e["src"]/e["dst"], but BOTH
        # edges.append sites in this file emit {"source", "target"} (:1290, :1936) --
        # derive_runner.py:357-358 documents exactly that remap. So _nid returned "" for
        # every edge and graph_edges was overwritten with EMPTY src_id/dst_id on all rows.
        # Silent: the schema's required=True is satisfied by "" (non-null).
        # This verb is the stale duplicate of derive_runner.commit_to_iceberg (see the
        # comment at cmd_snapshot); 2 invocations ever. FIX + FAIL CLOSED, and it is
        # recommended for deprecation rather than maintenance.
        def _nid(e, *keys):
            for k in keys:
                n = e.get(k)
                if isinstance(n, dict) and n.get("id"):
                    return n["id"]
                if isinstance(n, str) and n:
                    return n
            return ""
        src_ids = [_nid(e, "source", "src") for e in all_edges]
        dst_ids = [_nid(e, "target", "dst") for e in all_edges]
        bad = [i for i, (s, d) in enumerate(zip(src_ids, dst_ids)) if not s or not d]
        if bad:
            # NEVER overwrite a canonical table with dangling endpoints.
            print(f"ERROR: {len(bad)} of {len(all_edges)} edges have an empty endpoint after key "
                  f"resolution (tried 'source'/'src', 'target'/'dst').", file=sys.stderr)
            print(f"  first offender: {all_edges[bad[0]]!r}", file=sys.stderr)
            print("  REFUSING to overwrite globgrph.graph_edges. Fix the edge shape first.",
                  file=sys.stderr)
            return RC_FAIL
        edges_table.overwrite(pa.table({
            "src_id":      src_ids,
            "dst_id":      dst_ids,
            "edge_type":   [e.get("edge_type", "")  for e in all_edges],
            "layer":       ["aws"                    for _ in all_edges],
            "snapshot_ts": [batch_ts                 for _ in all_edges],
        }))
        print(f"  WRITE OK: {len(all_edges)} edges -> graph_edges")

    print(f"  Nessie commit on branch={branch} at ts={batch_ts} -- DONE")
    return RC_OK


DEPRECATION_PREAMBLE = (
    "comp-aws: DEPRECATED FOR AGENT USE since 2026-09-09 (Andrew-direct; recorded in "
    "org/tier1_exec/1.0.0_SA_CTO/deliverables/"
    "ANDREW_DIRECT_20260909_191xZ_NO_LAPTOP_GRAPH_REFRESH_COMP_AWS_WRITE_PATHS_RETIRED.md).\n"
    "  The cloud graph is SERVED: read it with `comp-kuzu \"<Cypher>\"` -- manifest entry "
    "cloud.read.served_vintage, which states how old its answer is on every call.\n"
    "  It is REFRESHED estate-side by the nightly Fargate derive-runner (full reconcile) and by "
    "the incremental updater. There is no refresh for you to run and no question is ever the "
    "cause of a rebuild.\n"
    "  This CLI is NO LONGER ROUTED BY comp-which. It is NOT gated: nothing here refuses, and "
    "every subcommand's exit code is unchanged.\n"
)

_PREAMBLE_ENV = "COMP_AWS_PREAMBLE_PRINTED"


def print_deprecation_preamble(cmd=None):
    """Print the deprecation notice ONCE per invocation, on STDERR, BEFORE the subcommand runs.

    STDERR AND NOT STDOUT, DELIBERATELY: stdout is the subcommands' DATA channel (`metrics` and
    `contract-diff --json` emit JSON that consumers parse). A stderr preamble changes no stdout
    byte, which is exactly how "then behaves exactly as before" is measured -- byte-identical
    stdout and an equal rc against a pre-change baseline.

    ONE PRINT PER INVOCATION: the wrapper .tools/comp-aws prints first and exports
    COMP_AWS_PREAMBLE_PRINTED=1 before exec'ing this module, which this function honours. A direct
    `python comp_aws_cli.py ...` (no wrapper) has the variable unset and prints here instead. So a
    caller of EITHER entry sees it exactly once.

    NOT A GATE. It returns; it never refuses, never exits, never changes rc (Andrew: "We do not
    need to gate it, merely need to pull it out of comp-which selection, that will be enough").
    """
    import os   # LOCAL on purpose: this module has no module-level `import os` (it imports argparse,
    #             sys, json, tarfile, io, glob, re, subprocess, datetime, pathlib). Adding one would
    #             be an edit OUTSIDE main() + this function, and the engine stays untouched.
    if os.environ.get(_PREAMBLE_ENV) == "1":
        return False
    sys.stderr.write(DEPRECATION_PREAMBLE)
    if cmd:
        sys.stderr.write("  -- running %s as before.\n" % cmd)
    else:
        sys.stderr.write("  -- running as before.\n")
    try:
        sys.stderr.flush()
    except Exception:
        pass
    os.environ[_PREAMBLE_ENV] = "1"
    return True


def main():
    # BEFORE parse_args(), so `--help` and a usage error (argparse exits inside parse_args) both
    # carry the notice too. sys.argv[1:] is read only to NAME the subcommand in the last line --
    # argparse still owns all parsing, and this call cannot change what argparse decides.
    _cmd = next((a for a in sys.argv[1:] if not a.startswith("-")), None)
    print_deprecation_preamble(_cmd)
    ap = argparse.ArgumentParser(prog="comp-aws")
    sub = ap.add_subparsers(dest="cmd", required=True)
    d = sub.add_parser("derive")
    d.add_argument("--class", dest="cls")
    d.add_argument("--out")
    d.add_argument("--resource", dest="resource", help="ARN for bounded single-resource derive (NFRA_GLOBGRPH Item-2b)")
    d.set_defaults(fn=cmd_derive_cli)   # A1: the CLI seam owns the rc; cmd_derive keeps its return contract
    s = sub.add_parser("score")
    s.add_argument("--class", dest="cls")
    s.add_argument("--reconcile-fixture", action="store_true", dest="reconcile_fixture",
                   help="SEPARATE NETWORKED PASS: classify each UNRECONCILED entry as EXISTS "
                        "(fixture gap) or ABSENT (compiler phantom) and write a gap report. "
                        "Never amends the fixture -- a human merges it.")
    s.add_argument("--report-out", dest="report_out",
                   help="where --reconcile-fixture writes its gap report "
                        "(default: org/modules/graph/aws-shapes/reconcile-gap-report.json)")
    s.set_defaults(fn=cmd_score)
    sn = sub.add_parser("snapshot")
    sn.add_argument("--stamp")
    sn.add_argument("--no-s3", action="store_true", dest="no_s3")
    sn.add_argument("--commit-to-nessie", action="store_true", dest="commit_to_nessie",
                    help="TO-F3: also commit this ad-hoc derive to Nessie (opt-in; "
                         "default = tarball side-channel only)")
    sn.set_defaults(fn=cmd_snapshot)
    m = sub.add_parser("metrics")
    m.add_argument("--graph")
    m.set_defaults(fn=cmd_metrics)
    df = sub.add_parser("diff")
    df.add_argument("prior")
    df.add_argument("current")
    df.set_defaults(fn=cmd_diff)
    cd = sub.add_parser("contract-diff",
                        help="NFRA_GCONTR Q1+Q2: value-layer never-widen diff vs graph_contracts (ADVISORY)")
    cd.add_argument("--since", dest="since", default=None,
                    help="baseline snapshot ref for the Q1 delta (YYYYMMDD / local path / s3 key); "
                         "omit = observed-at-HEAD only")
    cd.add_argument("--current", dest="current_ref", default="latest",
                    help="current snapshot ref (default: latest)")
    cd.add_argument("--json", action="store_true")
    cd.set_defaults(fn=cmd_contract_diff)
    dm = sub.add_parser("dual-managed")
    dm.set_defaults(fn=cmd_dual_managed)
    c = sub.add_parser("classes")
    c.set_defaults(fn=cmd_classes)
    ic = sub.add_parser("iceberg-commit")
    ic.add_argument("--graph",      dest="graph",      help="Path to derived graph JSON (default: run full derive)")
    ic.add_argument("--nessie-uri", dest="nessie_uri", help="Nessie API URI (default: http://nessie.opal-globgrph.local:19120/api/v2)")
    ic.add_argument("--warehouse",  dest="warehouse",  help="Iceberg warehouse S3 URI")
    ic.add_argument("--branch",     dest="branch",     default="main")
    ic.set_defaults(fn=cmd_iceberg_commit)
    args = ap.parse_args()

    # A1: PROPAGATE the handler's exit code. Previously `args.fn(args)` -- the return was
    # discarded, so comp-aws could exit nonzero ONLY on an uncaught exception or the
    # AC-GRAIN sys.exit(2). `score` printing "BELOW 0.95" exited 0. `score --class
    # zzqq-nope` exited 0 and .tools/comp-aws logged it as PASS (the launcher passes $? to
    # comp_log_auto.py). The success token was bound to the wrong step, and it poisoned
    # org/compiler-tools-log.md.
    #
    # NOT `sys.exit(args.fn(args) or 0)`: cmd_derive returns the graph DICT, so that form
    # exits 1 on success (dumping the graph to stderr) and 0 on failure. Handlers that can
    # fail return an int; informational handlers return None -> RC_OK. An uncaught
    # exception still exits 1 via the interpreter.
    rv = args.fn(args)
    if isinstance(rv, bool) or not isinstance(rv, int):
        rv = RC_OK
    sys.exit(rv)

if __name__ == "__main__":
    main()
