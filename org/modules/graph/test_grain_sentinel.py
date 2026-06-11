"""Regression test for the AC-GRAIN grain sentinel (NFRA_GRAPHS D5)."""
from __future__ import annotations
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from grain_sentinel import run_grain_sentinel


def test_clean_s3_bucket_passes():
    nodes = [{"node_type": "S3_BUCKET", "node_id": "arn:aws:s3:::opal-data-bd"},
             {"node_type": "S3_BUCKET", "node_id": "opal-data-inf"},
             {"node_type": "LAMBDA", "node_id": "inf-accounts-v2-daily"}]
    assert run_grain_sentinel(nodes).passed


def test_object_key_as_bucket_fails():
    # the 23,664-phantom class: an S3 object ARN minted as a bucket
    nodes = [{"node_type": "S3_BUCKET",
              "node_id": "arn:aws:s3:::opal-data-inf/gold/artifacts/timeseries_chart.json"}]
    r = run_grain_sentinel(nodes)
    assert not r.passed
    assert any(v.bar == "AC-GRAIN.1" and v.node_type == "S3_BUCKET" for v in r.violations)


def test_magnitude_spike_fails():
    nodes = [{"node_type": "S3_BUCKET", "node_id": f"b{i}"} for i in range(100)]
    r = run_grain_sentinel(nodes, baseline={"S3_BUCKET": 34})
    assert not r.passed
    assert any(v.bar == "AC-GRAIN.2" for v in r.violations)


def test_legit_slash_classes_not_flagged():
    # IAM_POLICY / S3_DATA_KEY legitimately contain '/': must NOT be flagged
    nodes = [{"node_type": "IAM_POLICY", "node_id": "arn:aws:iam::123:policy/team/x"},
             {"node_type": "S3_DATA_KEY", "node_id": "opal-data-bd/gold/views/x.json"}]
    assert run_grain_sentinel(nodes).passed


if __name__ == "__main__":
    test_clean_s3_bucket_passes()
    test_object_key_as_bucket_fails()
    test_magnitude_spike_fails()
    test_legit_slash_classes_not_flagged()
    print("all 4 grain-sentinel tests PASS")
