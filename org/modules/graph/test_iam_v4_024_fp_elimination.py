"""Regression fixture for ADHC_COMPIL_V4.024 — comp-iam gap-detector FP elimination.

Validates that the V4.024 changes:
  1. Class A: AWS-CLI patterns inside EC2-shipped triple-quoted strings
     (USER_DATA_SCRIPT, _CMD/_SCRIPT vars referenced in run_instances /
     send_command) are EXCLUDED from Lambda-role gap analysis.
  2. Class B: AWS-managed-policy attachments (aws_iam_role_policy_attachment
     with policy_arn = arn:aws:iam::aws:policy/...) contribute their actions
     to the role's grant set.
  3. Real gaps (Lambda calls action, role doesn't grant via inline OR managed)
     STILL SURFACE — FP elimination must not break real-gap detection.

Run: python org/modules/graph/test_iam_v4_024_fp_elimination.py
Exit 0 on all PASS, 1 on any FAIL.
"""
from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
_WORKSPACE = _THIS_DIR.parent.parent.parent
sys.path.insert(0, str(_WORKSPACE))

from org.modules.graph.extract_iam import (  # noqa: E402
    build_iam_report,
    _compute_ec2_shipped_line_ranges,
    _resolve_managed_policy_actions,
    IamRole,
    IamStatement,
)


def _write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def _make_fixture_workspace(root: Path) -> None:
    """Build a minimal fake workspace mirroring the real layout."""
    # Lambda 1: USER_DATA_SCRIPT — should be FP-suppressed (Class A)
    _write(root / "infra/aws/lambda/fixture-user-data-shipper/lambda_function.py", '''
import boto3

ec2 = boto3.client('ec2')

USER_DATA_SCRIPT = \'\'\'#!/bin/bash
aws s3 cp s3://bucket/file /tmp/x
aws s3 cp /tmp/result s3://bucket/result
\'\'\'

def lambda_handler(event, context):
    ec2.run_instances(ImageId='ami-x', UserData=USER_DATA_SCRIPT, MinCount=1, MaxCount=1)
''')

    # Lambda 2: SSM commands — should be FP-suppressed (Class A)
    _write(root / "infra/aws/lambda/fixture-ssm-shipper/lambda_function.py", '''
import boto3

ssm = boto3.client('ssm')

_CHAIN_CMD = """\\
aws s3 cp s3://bucket/script /tmp/script.sh
chmod +x /tmp/script.sh
/tmp/script.sh
"""

def lambda_handler(event, context):
    ssm.send_command(InstanceIds=['i-x'], DocumentName='AWS-RunShellScript',
                     Parameters={'commands': [_CHAIN_CMD]})
''')

    # Lambda 3: managed-policy coverage — should be FP-suppressed (Class B)
    _write(root / "infra/aws/lambda/fixture-managed-policy-covered/lambda_function.py", '''
import boto3
s3_client = boto3.client('s3')

def lambda_handler(event, context):
    s3_client.get_object(Bucket='b', Key='k')
''')

    # Lambda 4: REAL GAP — calls s3:DeleteObject, role does NOT grant
    _write(root / "infra/aws/lambda/fixture-real-gap/lambda_function.py", '''
import boto3
s3_client = boto3.client('s3')

def lambda_handler(event, context):
    s3_client.delete_object(Bucket='b', Key='k')
''')

    # the Lambda function map — wires Lambdas to roles
    _fmap_text = '''{
  "fixture-user-data-shipper": {
    "source": "infra/aws/lambda/fixture-user-data-shipper",
    "role": "fixture-user-data-shipper-role"
  },
  "fixture-ssm-shipper": {
    "source": "infra/aws/lambda/fixture-ssm-shipper",
    "role": "fixture-ssm-shipper-role"
  },
  "fixture-managed-policy-covered": {
    "source": "infra/aws/lambda/fixture-managed-policy-covered",
    "role": "fixture-managed-policy-covered-role"
  },
  "fixture-real-gap": {
    "source": "infra/aws/lambda/fixture-real-gap",
    "role": "fixture-real-gap-role"
  }
}'''
    # CT-ca-1: the Lambda function map is one <name>.json per function (the entry object alone)
    for _name, _entry in json.loads(_fmap_text).items():
        _write(root / "infra/aws/lambda/ci/function-map" / (_name + ".json"), json.dumps(_entry, indent=2))

    # Terraform iam.tf — defines roles + inline policies + managed attachment
    _write(root / "infra/aws/terraform/fixture/iam.tf", '''
resource "aws_iam_role" "user_data_shipper" {
  name = "fixture-user-data-shipper-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{ Effect = "Allow", Principal = { Service = "lambda.amazonaws.com" }, Action = "sts:AssumeRole" }]
  })
}

resource "aws_iam_role_policy" "user_data_shipper_inline" {
  name = "user-data-shipper-inline"
  role = aws_iam_role.user_data_shipper.name
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Action = ["ec2:RunInstances"]
      Resource = "*"
    }]
  })
}

resource "aws_iam_role" "ssm_shipper" {
  name = "fixture-ssm-shipper-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{ Effect = "Allow", Principal = { Service = "lambda.amazonaws.com" }, Action = "sts:AssumeRole" }]
  })
}

resource "aws_iam_role_policy" "ssm_shipper_inline" {
  name = "ssm-shipper-inline"
  role = aws_iam_role.ssm_shipper.name
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Action = ["ssm:SendCommand"]
      Resource = "*"
    }]
  })
}

resource "aws_iam_role" "managed_covered" {
  name = "fixture-managed-policy-covered-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{ Effect = "Allow", Principal = { Service = "lambda.amazonaws.com" }, Action = "sts:AssumeRole" }]
  })
}

resource "aws_iam_role_policy_attachment" "managed_covered_s3ro" {
  role       = aws_iam_role.managed_covered.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess"
}

resource "aws_iam_role" "real_gap" {
  name = "fixture-real-gap-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{ Effect = "Allow", Principal = { Service = "lambda.amazonaws.com" }, Action = "sts:AssumeRole" }]
  })
}

resource "aws_iam_role_policy" "real_gap_inline" {
  name = "real-gap-inline"
  role = aws_iam_role.real_gap.name
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Action = ["s3:GetObject"]
      Resource = "*"
    }]
  })
}
''')


def _run_test(name: str, fn) -> bool:
    try:
        fn()
        print(f"  PASS: {name}")
        return True
    except AssertionError as exc:
        print(f"  FAIL: {name} -- {exc}")
        return False
    except Exception as exc:
        print(f"  ERROR: {name} -- {type(exc).__name__}: {exc}")
        return False


def test_ec2_shipped_line_detection_user_data():
    code = '''
USER_DATA_SCRIPT = \'\'\'#!/bin/bash
aws s3 cp s3://x /tmp/x
\'\'\'

ec2.run_instances(UserData=USER_DATA_SCRIPT)
'''
    shipped = _compute_ec2_shipped_line_ranges(code)
    assert 4 in shipped, f"line 4 (aws s3 cp) should be shipped; got {sorted(shipped)}"


def test_ec2_shipped_line_detection_ssm():
    code = '''
_CHAIN_CMD = """\\
aws s3 cp s3://x /tmp/x
"""

ssm.send_command(Parameters={'commands': [_CHAIN_CMD]})
'''
    shipped = _compute_ec2_shipped_line_ranges(code)
    assert 4 in shipped, f"line 4 (aws s3 cp inside _CHAIN_CMD) should be shipped; got {sorted(shipped)}"


def test_unrelated_string_not_shipped():
    code = '''
RANDOM_DOC = """
some unrelated docstring that mentions aws s3 cp
"""

x = "hello"
'''
    shipped = _compute_ec2_shipped_line_ranges(code)
    assert 3 not in shipped, f"line 3 (unrelated string) should NOT be shipped; got {sorted(shipped)}"


def test_managed_policy_static_lookup():
    cache: dict[str, list[str]] = {}
    actions, source = _resolve_managed_policy_actions(
        'arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess', cache, Path("/tmp")
    )
    assert source == 'static', f"expected static lookup; got source={source}"
    assert 's3:Get*' in actions, f"AmazonS3ReadOnlyAccess should grant s3:Get*; got {actions}"


def test_grants_wildcard_get_star():
    role = IamRole(
        role_name='test',
        tf_resource='test',
        statements=[IamStatement(effect='Allow', actions=['s3:Get*'], resources=['*'], source_file='')]
    )
    assert role.grants('s3:GetObject'), "s3:Get* should match s3:GetObject"
    assert role.grants('s3:GetBucketLocation'), "s3:Get* should match s3:GetBucketLocation"
    assert not role.grants('s3:PutObject'), "s3:Get* should NOT match s3:PutObject"


def test_end_to_end_synthetic_workspace():
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        _make_fixture_workspace(root)
        profiles, roles, gaps = build_iam_report(root)

        gap_keys = {(g.service, g.iam_action) for g in gaps}

        # Class A FP suppressed: USER_DATA_SCRIPT
        assert ('fixture-user-data-shipper', 's3:GetObject') not in gap_keys, \
            f"Class A FP not suppressed (USER_DATA_SCRIPT s3:GetObject surfaced); gaps={gap_keys}"
        assert ('fixture-user-data-shipper', 's3:PutObject') not in gap_keys, \
            "Class A FP not suppressed (USER_DATA_SCRIPT s3:PutObject surfaced)"

        # Class A FP suppressed: SSM commands
        assert ('fixture-ssm-shipper', 's3:GetObject') not in gap_keys, \
            "Class A FP not suppressed (SSM _CHAIN_CMD s3:GetObject surfaced)"

        # Class B FP suppressed: AmazonS3ReadOnlyAccess attachment
        assert ('fixture-managed-policy-covered', 's3:GetObject') not in gap_keys, \
            "Class B FP not suppressed (managed-policy AmazonS3ReadOnlyAccess s3:GetObject surfaced)"

        # Real gap STILL surfaces: s3:DeleteObject not granted
        assert ('fixture-real-gap', 's3:DeleteObject') in gap_keys, \
            f"Real-gap detection broken (s3:DeleteObject for fixture-real-gap missing); gaps={gap_keys}"


def main() -> int:
    print("V4.024 FP-elimination regression fixture")
    print()

    tests = [
        ('ec2_shipped_line_detection_user_data', test_ec2_shipped_line_detection_user_data),
        ('ec2_shipped_line_detection_ssm', test_ec2_shipped_line_detection_ssm),
        ('unrelated_string_not_shipped', test_unrelated_string_not_shipped),
        ('managed_policy_static_lookup', test_managed_policy_static_lookup),
        ('grants_wildcard_get_star', test_grants_wildcard_get_star),
        ('end_to_end_synthetic_workspace', test_end_to_end_synthetic_workspace),
    ]
    passed = sum(1 for n, fn in tests if _run_test(n, fn))
    failed = len(tests) - passed
    print()
    print(f"Total: {passed}/{len(tests)} pass, {failed} fail")
    return 0 if failed == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
