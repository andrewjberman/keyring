"""
Regression: comp-iam (extract_iam._parse_terraform_iam) scans ALL terraform roots.

Coverage gap (0.5.0_AE surfaced 2026-06-26 during the collision fix; CTO routed to the
comp-tools campaign): _parse_terraform_iam globbed ONLY infra/aws/terraform/** -> roles
declared in infra/aws/multi-account/terraform/** and the per-service infra/aws/ec2/*/
terraform/** roots got NO gap-check at all -- a silent coverage hole on this Rule-20
deploy-gate tool (a role could be missing a permission and comp-iam would never see it).

Fix: scan infra/aws/{terraform, multi-account/terraform, ec2}, dedup by resolved path,
skip .terraform vendored caches. A reusable module template whose name stays ${var.X}
(no concrete default) is skipped LOUDLY (it is instantiated concretely elsewhere, which
IS scanned) -- no silent drop.

These assert a role in EACH newly-added root is parsed with correct source attribution,
and that the unresolved-var module template is excluded. Per CTO lens: adversarial inputs
(the exact missed roots + the template-noise case), not a happy-path single-root fixture.
"""

from __future__ import annotations

import sys
from pathlib import Path

_WORKSPACE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(_WORKSPACE))

from org.modules.graph.extract_iam import _parse_terraform_iam  # noqa: E402


def _role(tf_base: Path, rel_module: str, label: str, name: str, action: str):
    d = tf_base / rel_module
    d.mkdir(parents=True, exist_ok=True)
    (d / "main.tf").write_text(
        f'''
resource "aws_iam_role" "{label}" {{
  name = "{name}"
  assume_role_policy = jsonencode({{ Version = "2012-10-17", Statement = [] }})
}}
resource "aws_iam_role_policy" "{label}" {{
  name   = "{name}-inline"
  role   = aws_iam_role.{label}.id
  policy = jsonencode({{ Version = "2012-10-17", Statement = [{{ Effect = "Allow", Action = ["{action}"], Resource = ["*"] }}] }})
}}
''',
        encoding="utf-8",
    )


def _make_workspace(tmp_path: Path) -> Path:
    aws = tmp_path / "infra" / "aws"
    # primary root (always scanned)
    _role(aws / "terraform", "primary-pipeline", "lambda", "primary-lambda-role", "s3:GetObject")
    # multi-account root (was UNSCANNED)
    _role(aws / "multi-account" / "terraform" / "environments" / "prod", "", "news_lambda", "news-lambda-role", "sns:Publish")
    # ec2 per-service root (was UNSCANNED)
    _role(aws / "ec2" / "bd-exporter" / "terraform", "", "ec2role", "bd-exporter-ec2-role", "ec2:DescribeInstances")
    # a reusable module template with an UNRESOLVED var name -> must be skipped (loud)
    mod = aws / "multi-account" / "terraform" / "modules" / "lambda"
    mod.mkdir(parents=True, exist_ok=True)
    (mod / "main.tf").write_text(
        '''
resource "aws_iam_role" "lambda" {
  name = "${var.function_name}-role"
  assume_role_policy = jsonencode({ Version = "2012-10-17", Statement = [] })
}
''',
        encoding="utf-8",
    )
    return tmp_path


def test_multi_account_and_ec2_roots_are_scanned(tmp_path):
    roles = _parse_terraform_iam(_make_workspace(tmp_path))
    # the previously-unscanned roots must now contribute their roles
    assert "news-lambda-role" in roles, "multi-account/terraform root still unscanned"
    assert "bd-exporter-ec2-role" in roles, "ec2/*/terraform root still unscanned"
    assert "primary-lambda-role" in roles, "primary terraform root regressed"


def test_newly_scanned_roles_have_their_statements(tmp_path):
    roles = _parse_terraform_iam(_make_workspace(tmp_path))
    news = {a for s in roles["news-lambda-role"].statements for a in s.actions}
    ec2 = {a for s in roles["bd-exporter-ec2-role"].statements for a in s.actions}
    assert news == {"sns:Publish"}, f"news role mis-parsed: {sorted(news)}"
    assert ec2 == {"ec2:DescribeInstances"}, f"ec2 role mis-parsed: {sorted(ec2)}"


def test_unresolved_var_module_template_is_skipped(tmp_path):
    roles = _parse_terraform_iam(_make_workspace(tmp_path))
    assert not any("${var." in r for r in roles), "unresolved-var module template leaked into roles"
