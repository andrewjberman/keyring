"""
Pass 8: event-source + SNS -> Lambda INVOKE-edge bridge (NFRA_GRAPHUNI, 2026-07-06).

Companion to extract_sfn (Pass 7). Bridges the OTHER AWS Lambda-invoke mechanisms into trace_graph so
comp-blast/comp-iam surface a Lambda's non-code invokers -- blast-radius COMPLETENESS:
  - event-source-mappings : SQS / DynamoDB-stream / Kinesis -> Lambda
  - SNS subscriptions (protocol=lambda) : SNS topic -> Lambda
  - S3 bucket-notifications (LambdaFunctionConfigurations) : S3 bucket -> Lambda (ObjectCreated etc.)

LIVE-DERIVED (Andrew-direct 2026-07-06), NOT a static .tf parse. Rationale: deploys are TERRAFORM-ONLY,
so TF-declared front-runs live (declared >= deployed). A raw .tf parse therefore can carry a
DECLARED-not-APPLIED resource that invokes NOTHING live -> a PHANTOM blast edge (proven 2026-07-06: the
served-guard-49f ESM is in .tf but has NO live event-source-mapping; a static parse would have emitted a
false 49f edge). The blast radius must reflect what is ACTUALLY DEPLOYED, so this pass grounds on live via
read-only boto (list_event_source_mappings + list_subscriptions). Everything is wrapped: no boto / no creds
/ any AWS error -> the pass emits nothing (graceful, like the other passes), never breaking the build.
Trade-off vs the static passes: this pass makes the build depend on live AWS state (deliberate, per the
live-accuracy requirement); absent creds it degrades to no-edges rather than stale edges.

Dual-direction edges (mirror extract_sfn's SFN_INVOKES/SFN_INVOKED_BY + the estate's CALLS/CALLED_BY):
  {SQS_QUEUE|DYNAMODB_STREAM|KINESIS_STREAM} -[EVENT_INVOKES]-> LAMBDA ; LAMBDA -[EVENT_INVOKED_BY]-> src
  SNS_TOPIC                                  -[SNS_INVOKES]->   LAMBDA ; LAMBDA -[SNS_INVOKED_BY]->   topic
  S3_BUCKET                                  -[S3_INVOKES]->    LAMBDA ; LAMBDA -[S3_INVOKED_BY]->    bucket
so comp-blast(Lambda) surfaces its queue/stream/topic/bucket invoker AND comp-blast(source) shows its Lambdas.
"""

from __future__ import annotations

from pathlib import Path

from .trace_graph import Edge, Node, TraceGraph

# Deploys are region-scoped; the estate lives in us-east-1 (+ us-east-2 for a few resources). Iterate both
# so coverage is comprehensive (a Lambda invoked from either region appears).
_REGIONS = ("us-east-1", "us-east-2")


def _fn_name(arn_or_name: str | None) -> str | None:
    """A Lambda function ARN or bare name -> bare function name (drop any :version/:alias qualifier)."""
    if not arn_or_name:
        return None
    s = arn_or_name
    if ":function:" in s:
        s = s.split(":function:", 1)[1]
    return s.split(":", 1)[0]


def _source_node(arn: str) -> tuple[str, str, str]:
    """Classify an event_source_arn -> (node_id, node_type, label): SQS / DynamoDB-stream / Kinesis / other."""
    if ":sqs:" in arn:
        name = arn.rsplit(":", 1)[-1]
        return f"sqs:{name}", "SQS_QUEUE", name
    if ":dynamodb:" in arn and "/stream/" in arn:
        tbl = arn.split(":table/", 1)[1].split("/stream/", 1)[0]
        return f"ddbstream:{tbl}", "DYNAMODB_STREAM", f"{tbl} (stream)"
    if ":kinesis:" in arn:
        name = arn.rsplit(":", 1)[-1]
        return f"kinesis:{name}", "KINESIS_STREAM", name
    name = arn.rsplit(":", 1)[-1]
    return f"eventsource:{name}", "EVENT_SOURCE", name


def _warn_unverified(reason: str) -> None:
    """CTO note 2026-07-06: when the live calls can't run, a MISSING invoke edge this build is could-not-
    verify, NOT nonexistence. Emit a build-time signal so a creds-less rebuild is not misread as 'no such
    invoker' (mirrors emit_stale_warn / grain-sentinel; never blocks)."""
    import sys
    print("WARN (extract_event_invoke): live-derived invoke edges (event-source/SNS -> Lambda) NOT "
          "verified this build (%s) -- a MISSING SQS/stream/SNS invoke edge in comp-blast this build is "
          "COULD-NOT-VERIFY, not nonexistence." % reason, file=sys.stderr)


def _add_dual(graph: TraceGraph, source_id: str, source_type: str, source_label: str,
              lambda_name: str, fwd: str, rev: str, meta: dict) -> None:
    """Add the dual invoke edge (mirror extract_sfn): source -[fwd]-> lambda + lambda -[rev]-> source, so
    blast resolves from either end. Creates the source + lambda nodes if absent (never clobbers existing).
    Every edge/node carries provenance="live-derived" (CTO note): a consumer must be able to tell a
    live-derived edge (conditionally present -- absent on a creds-less build) from a verified-absent one."""
    edge_meta = {"provenance": "live-derived", **meta}
    if source_id not in graph.nodes:
        graph.add_node(Node(id=source_id, node_type=source_type, label=source_label,
                            metadata={"provenance": "live-derived"}))
    lambda_id = f"lambda:{lambda_name}"
    if lambda_id not in graph.nodes:
        graph.add_node(Node(id=lambda_id, node_type="LAMBDA", label=lambda_name,
                            metadata={"invoked_by": source_id, "provenance": "live-derived"}))
    graph.add_edge(Edge(source=source_id, target=lambda_id, edge_type=fwd, metadata=edge_meta))
    graph.add_edge(Edge(source=lambda_id, target=source_id, edge_type=rev, metadata=edge_meta))


def extract_event_invoke_edges(graph: TraceGraph, workspace_root: Path) -> None:
    """LIVE-derived bridge of event-source-mapping + SNS(protocol=lambda) -> Lambda invoke edges. Grounds on
    DEPLOYED state via read-only boto; graceful no-op if boto/creds/AWS unavailable (never breaks the build).
    Deduped by (source, lambda) per direction so a re-listing can't double an edge."""
    try:
        import boto3
    except Exception:  # noqa: BLE001 -- no boto -> no live edges, never break the build
        _warn_unverified("boto3 unavailable")
        return

    seen: set[tuple[str, str]] = set()
    reached_aws = False   # did ANY live list succeed? absent -> could-not-verify (not "no edges")

    for region in _REGIONS:
        # --- event-source-mappings (SQS / DynamoDB-stream / Kinesis -> Lambda) ---
        try:
            lam = boto3.client("lambda", region_name=region)
            for page in lam.get_paginator("list_event_source_mappings").paginate():
                reached_aws = True
                for esm in page.get("EventSourceMappings", []):
                    src_arn = esm.get("EventSourceArn") or ""
                    fn = _fn_name(esm.get("FunctionArn"))
                    if not src_arn or not fn:
                        continue
                    sid, stype, slabel = _source_node(src_arn)
                    if (sid, fn) in seen:
                        continue
                    seen.add((sid, fn))
                    _add_dual(graph, sid, stype, slabel, fn, "EVENT_INVOKES", "EVENT_INVOKED_BY",
                              {"mechanism": "event_source_mapping", "state": esm.get("State"),
                               "source_arn": src_arn, "region": region})
        except Exception:  # noqa: BLE001
            pass

        # --- SNS subscriptions with protocol=lambda (SNS topic -> Lambda) ---
        try:
            sns = boto3.client("sns", region_name=region)
            for page in sns.get_paginator("list_subscriptions").paginate():
                reached_aws = True
                for sub in page.get("Subscriptions", []):
                    if sub.get("Protocol") != "lambda":
                        continue
                    fn = _fn_name(sub.get("Endpoint"))
                    topic_arn = sub.get("TopicArn") or ""
                    if not fn or not topic_arn:
                        continue
                    topic = topic_arn.rsplit(":", 1)[-1]
                    sid = f"sns:{topic}"
                    if (sid, fn) in seen:
                        continue
                    seen.add((sid, fn))
                    _add_dual(graph, sid, "SNS_TOPIC", topic, fn, "SNS_INVOKES", "SNS_INVOKED_BY",
                              {"mechanism": "sns_subscription", "topic_arn": topic_arn, "region": region})
        except Exception:  # noqa: BLE001
            pass

    # --- S3 bucket-notification -> Lambda (ObjectCreated etc.). Buckets are GLOBAL -> scan once, not
    # per-region. Direct S3->Lambda only (an S3->EventBridge->Lambda write-trigger, e.g. served-guard, is
    # an EventBridge edge, not this; the module comment even says it does NOT touch the notification config). ---
    try:
        s3 = boto3.client("s3", region_name=_REGIONS[0])
        buckets = s3.list_buckets().get("Buckets", [])
        reached_aws = True
        for b in buckets:
            bucket = b.get("Name")
            if not bucket:
                continue
            try:
                cfg = s3.get_bucket_notification_configuration(Bucket=bucket)
            except Exception:  # noqa: BLE001 -- one inaccessible bucket must not abort the scan
                continue
            for lc in cfg.get("LambdaFunctionConfigurations", []):
                fn = _fn_name(lc.get("LambdaFunctionArn"))
                if not fn:
                    continue
                sid = f"s3bucket:{bucket}"
                if (sid, fn) in seen:
                    continue
                seen.add((sid, fn))
                _add_dual(graph, sid, "S3_BUCKET", bucket, fn, "S3_INVOKES", "S3_INVOKED_BY",
                          {"mechanism": "s3_bucket_notification", "events": lc.get("Events"), "bucket": bucket})
    except Exception:  # noqa: BLE001
        pass

    if not reached_aws:
        _warn_unverified("no creds / AWS unreachable")
