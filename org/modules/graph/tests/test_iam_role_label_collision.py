"""
Regression: comp-iam cross-module TF role-label COLLISION (false-MISSING / mis-attribution).

Root cause (0.5.0_AE 2026-06-26, brief docs/briefs/comp-iam-false-missing-tf-resource-collision-20260626.md):
extract_iam._parse_terraform_iam keyed `role_tf_to_name` by the BARE terraform resource label
(e.g. `aws_iam_role "orchestrator"`), not namespaced by module. A label is module-LOCAL in
Terraform, so the same generic label reused across two roots (orchestrator/scheduler/lambda_role/
sfn_role/...) collided last-writer-wins: the loser role's inline policy linked to the WINNER, so the
loser was credited 0 statements -> every action FALSE-MISSING in this Rule-20 deploy-gate tool, AND
the loser's statements were MIS-ATTRIBUTED onto the winner (false-GREEN risk).

Live incident: astn-wsjft-orchestrator-role vs etfs-reports-orchestrator-role (both
`aws_iam_role "orchestrator"`) -> astn role parsed 0 statements -> drove a confusing all-MISSING
signal during a CEO-brief outage diagnosis.

Fix: key role_tf_to_name by (module_dir, tf_resource) + resolve the policy's role ref within the
same module + a loud collision guard.

These tests FAIL against the pre-fix parser (bare-label key) and PASS post-fix.
"""

import sys
from pathlib import Path

import pytest

_WORKSPACE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(_WORKSPACE))

from org.modules.graph.extract_iam import _parse_terraform_iam  # noqa: E402


def _write_module(tf_base: Path, module: str, role_label: str, role_name: str, actions: list[str]):
    """Write infra/aws/terraform/<module>/main.tf declaring aws_iam_role <role_label> (name=role_name)
    with an inline aws_iam_role_policy granting `actions`."""
    mod_dir = tf_base / module
    mod_dir.mkdir(parents=True, exist_ok=True)
    acts = ", ".join(f'"{a}"' for a in actions)
    (mod_dir / "main.tf").write_text(
        f'''
resource "aws_iam_role" "{role_label}" {{
  name = "{role_name}"
  assume_role_policy = jsonencode({{
    Version   = "2012-10-17"
    Statement = [{{ Effect = "Allow", Principal = {{ Service = "lambda.amazonaws.com" }}, Action = "sts:AssumeRole" }}]
  }})
}}

resource "aws_iam_role_policy" "{role_label}" {{
  name = "{role_name}-inline"
  role = aws_iam_role.{role_label}.id
  policy = jsonencode({{
    Version = "2012-10-17"
    Statement = [{{ Effect = "Allow", Action = [{acts}], Resource = ["*"] }}]
  }})
}}
''',
        encoding="utf-8",
    )


@pytest.fixture
def collided_workspace(tmp_path):
    """Two DIFFERENT modules, each declaring the same generic label `lambda_role` with DIVERGENT
    policies -- the exact cross-module collision class (generalized beyond orchestrator/scheduler)."""
    tf_base = tmp_path / "infra" / "aws" / "terraform"
    _write_module(tf_base, "alpha-pipeline", "lambda_role", "alpha-lambda-role", ["s3:GetObject", "s3:PutObject"])
    _write_module(tf_base, "beta-pipeline", "lambda_role", "beta-lambda-role", ["dynamodb:GetItem", "sns:Publish"])
    return tmp_path


def test_no_role_loses_its_statements_to_a_label_collision(collided_workspace):
    roles = _parse_terraform_iam(collided_workspace)
    assert "alpha-lambda-role" in roles
    assert "beta-lambda-role" in roles
    # Neither role may be left at 0 statements (the FALSE-MISSING symptom).
    assert len(roles["alpha-lambda-role"].statements) > 0, "alpha-lambda-role lost its policy to the collision"
    assert len(roles["beta-lambda-role"].statements) > 0, "beta-lambda-role lost its policy to the collision"


def test_each_role_gets_ONLY_its_own_statements_no_cross_attribution(collided_workspace):
    roles = _parse_terraform_iam(collided_workspace)
    alpha = {a for s in roles["alpha-lambda-role"].statements for a in s.actions}
    beta = {a for s in roles["beta-lambda-role"].statements for a in s.actions}
    # alpha has ONLY its own grants; beta's must NOT bleed in (the MIS-ATTRIBUTION / false-GREEN harm).
    assert alpha == {"s3:GetObject", "s3:PutObject"}, f"alpha mis-attributed: {sorted(alpha)}"
    assert beta == {"dynamodb:GetItem", "sns:Publish"}, f"beta mis-attributed: {sorted(beta)}"
    # And the winner must NOT be credited with the loser's actions.
    assert "dynamodb:GetItem" not in alpha and "sns:Publish" not in alpha
    assert "s3:GetObject" not in beta and "s3:PutObject" not in beta


def test_grants_resolves_correctly_post_fix(collided_workspace):
    """The action-level verdict comp-iam emits (role.grants(action)) is correct for BOTH roles."""
    roles = _parse_terraform_iam(collided_workspace)
    assert roles["alpha-lambda-role"].grants("s3:GetObject") is True
    assert roles["alpha-lambda-role"].grants("dynamodb:GetItem") is False   # NOT beta's grant
    assert roles["beta-lambda-role"].grants("dynamodb:GetItem") is True
    assert roles["beta-lambda-role"].grants("s3:GetObject") is False        # NOT alpha's grant
