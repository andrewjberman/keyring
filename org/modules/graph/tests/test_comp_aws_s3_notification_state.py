#!/usr/bin/env python3
"""Regression arms for honest S3 notification reads and declared trigger edges."""
from __future__ import annotations

import importlib.util
from pathlib import Path


_HERE = Path(__file__).resolve().parent
_MOD = _HERE.parent / "comp_aws_cli.py"


def _load():
    spec = importlib.util.spec_from_file_location("comp_aws_s3_notification_under_test", _MOD)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


caw = _load()


class FakeS3:
    def __init__(self, configurations=None, denied=None):
        self.configurations = configurations or {}
        self.denied = set(denied or [])
        self.notification_calls = []

    def list_buckets(self):
        names = sorted(set(self.configurations) | self.denied)
        return {"Buckets": [{"Name": name} for name in names]}

    def get_bucket_notification_configuration(self, Bucket):
        self.notification_calls.append(Bucket)
        if Bucket in self.denied:
            raise PermissionError("planted AccessDenied")
        return self.configurations.get(Bucket, {})

    def get_bucket_location(self, Bucket):
        return {"LocationConstraint": None}

    def get_bucket_versioning(self, Bucket):
        return {}

    def get_public_access_block(self, Bucket):
        raise LookupError("not configured")

    def get_bucket_policy(self, Bucket):
        raise LookupError("not configured")

    def get_bucket_lifecycle_configuration(self, Bucket):
        raise LookupError("not configured")

    def get_bucket_cors(self, Bucket):
        raise LookupError("not configured")

    def get_bucket_website(self, Bucket):
        raise LookupError("not configured")


def _lambda(arn):
    return {"LambdaFunctionArn": arn, "Events": ["s3:ObjectCreated:*"]}


def test_denied_node_read_is_unreadable_not_zero_and_moves_denominator(monkeypatch):
    client = FakeS3(configurations={"readable": {}}, denied={"denied"})
    monkeypatch.setattr(caw, "_boto", lambda service, region="us-east-1": client)
    caw._S3_NOTIFICATION_CACHE.clear()
    caw._S3_SUBCFG_CACHE.clear()

    nodes = {node["id"]: node for node in caw.live_s3()}

    assert nodes["readable"]["notification_read_state"] == "READ"
    assert nodes["readable"]["event_notifications"] == 0
    assert nodes["denied"]["notification_read_state"] == "UNREADABLE"
    assert nodes["denied"]["event_notifications"] is None
    assert nodes["denied"]["notify_sns"] is None
    assert nodes["denied"]["notify_sqs"] is None
    assert "PermissionError" in nodes["denied"]["notification_read_error"]
    assert caw._s3_notification_read_summary() == {
        "buckets_read": 1,
        "buckets_unreadable": 1,
        "unreadable_buckets": ["denied"],
    }

    # live_s3 and edge derivation share one result; the read is not repeated or
    # allowed to change meaning between the node and edge twins.
    caw._read_s3_notification_configuration(client, "denied")
    assert client.notification_calls.count("denied") == 1


def test_planted_denial_kills_the_legacy_zero_mutant():
    client = FakeS3(denied={"denied"})

    def legacy_count():
        try:
            result = client.get_bucket_notification_configuration(Bucket="denied")
            return len(result.get("LambdaFunctionConfigurations", []))
        except Exception:
            return 0

    assert legacy_count() == 0, "the pre-fix branch manufactures a genuine-zero value"
    caw._S3_NOTIFICATION_CACHE.clear()
    honest = caw._read_s3_notification_configuration(client, "denied")
    assert honest["state"] == "UNREADABLE"
    assert honest["configuration"] is None


def test_trigger_edges_merge_live_declared_and_unreadable_provenance():
    both = "arn:aws:lambda:us-east-1:313476888478:function:both"
    live_only = "arn:aws:lambda:us-east-1:313476888478:function:live-only"
    declared_only = "arn:aws:lambda:us-east-1:313476888478:function:declared-only"
    client = FakeS3(
        configurations={"readable": {"LambdaFunctionConfigurations": [_lambda(both), _lambda(live_only)]}},
        denied={"denied"},
    )
    declared = [
        {"bucket": "readable", "target": both, "configuration_id": "both-id",
         "provenance": {"tf_module": "m1", "tf_resource": "aws_s3_bucket_notification.r1", "tf_kind": "managed"}},
        {"bucket": "denied", "target": declared_only, "configuration_id": "denied-id",
         "provenance": {"tf_module": "m2", "tf_resource": "aws_s3_bucket_notification.r2", "tf_kind": "managed"}},
    ]
    caw._S3_NOTIFICATION_CACHE.clear()

    edges = caw._derive_s3_lambda_trigger_edges(
        client, [{"id": "readable"}, {"id": "denied"}], declared=declared)
    by_target = {edge["target"]: edge for edge in edges}

    assert by_target[both]["provenance"] == "both"
    assert by_target[both]["source_disagreement"] == "NONE"
    assert by_target[live_only]["provenance"] == "live"
    assert by_target[live_only]["source_disagreement"] == "LIVE_ONLY"
    assert by_target[declared_only]["provenance"] == "declared"
    assert by_target[declared_only]["live_read_state"] == "UNREADABLE"
    assert by_target[declared_only]["source_disagreement"] == "UNKNOWN_LIVE_UNREADABLE"
    assert by_target[declared_only]["declared_configuration_count"] == 1


def test_declared_targets_keep_resolved_terraform_provenance(monkeypatch):
    monkeypatch.setattr(caw, "_load_all_tfstate", lambda: [{
        "type": "aws_s3_bucket_notification",
        "module": "bd-pipeline",
        "tf_name": "bd_data_bucket",
        "tf_kind": "managed",
        "id": "opal-data-bd",
        "name": "opal-data-bd",
        "attrs": {
            "bucket": "opal-data-bd",
            "lambda_function": [{
                "id": "ProcessAllocationFiles",
                "lambda_function_arn": "arn:aws:lambda:us-east-1:313476888478:function:bd-allocation-processor",
                "events": ["s3:ObjectCreated:*"],
                "filter_prefix": "forwardfill_v2/allocations/",
                "filter_suffix": ".xlsx",
            }],
        },
    }])

    rows = caw._declared_s3_lambda_notifications()
    assert rows == [{
        "bucket": "opal-data-bd",
        "target": "arn:aws:lambda:us-east-1:313476888478:function:bd-allocation-processor",
        "configuration_id": "ProcessAllocationFiles",
        "events": ["s3:ObjectCreated:*"],
        "filter_prefix": "forwardfill_v2/allocations/",
        "filter_suffix": ".xlsx",
        "provenance": {
            "tf_module": "bd-pipeline",
            "tf_resource": "aws_s3_bucket_notification.bd_data_bucket",
            "tf_kind": "managed",
        },
    }]
