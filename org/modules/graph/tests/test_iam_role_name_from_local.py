"""
Regression: comp-iam was BLIND to any role whose `name` is built from a ${local.X}.

Root cause (0.8.0_AE_CloudComp 2026-07-13): `_parse_terraform_iam` resolved ${var.X} in a role's
`name` but NOT ${local.X} -- an ASYMMETRY, because policy RESOURCE ARNs already resolved locals
(`_resolve_tf_locals` in the statement pass). So a role declared

    locals { emitter_name = "opal-assets-daily-emitter" }
    resource "aws_iam_role" "emitter" { name = "${local.emitter_name}-role" }

keyed under the LITERAL string "${local.emitter_name}-role". That key never matched the concrete
name the service side reports, so the role linked ZERO statements and EVERY operation on that
Lambda degraded to [UNKNOWN] / "role not mapped".

This is the TWIN of the label-collision bug next door (test_iam_role_label_collision.py): both end
in a role credited 0 statements in a Rule-20/22a deploy-gate tool.

IMPORTANT -- WHAT THIS WAS AND WAS NOT: it was NOT a false-GREEN. comp-iam said UNKNOWN, never
GRANTED, so Rule 22a was never undermined -- silence is not a pass. It was a COVERAGE hole: the
tool went silent on a whole module, and a brand-new pipeline is exactly when the graph is least
useful and most needed. Live: opal-assets-daily-emitter, found while the mandated comp-iam check
could not answer the one question Rule 20 asks of it, and the whole verification had to fall back
to live simulate-principal-policy.

These tests FAIL against the pre-fix parser (locals unresolved in role names) and PASS post-fix.
"""

import sys
from pathlib import Path

import pytest

_WORKSPACE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(_WORKSPACE))

from org.modules.graph.extract_iam import _parse_terraform_iam  # noqa: E402


def _write_module(tf_base: Path, module: str, name_expr: str, extra_head: str = ""):
    """Write infra/aws/terraform/<module>/main.tf whose role `name` is `name_expr` verbatim."""
    mod_dir = tf_base / module
    mod_dir.mkdir(parents=True, exist_ok=True)
    (mod_dir / "main.tf").write_text(
        f'''
{extra_head}

resource "aws_iam_role" "emitter" {{
  name = {name_expr}
  assume_role_policy = jsonencode({{
    Version   = "2012-10-17"
    Statement = [{{ Effect = "Allow", Principal = {{ Service = "lambda.amazonaws.com" }}, Action = "sts:AssumeRole" }}]
  }})
}}

resource "aws_iam_role_policy" "emitter" {{
  name = "emitter-scoped"
  role = aws_iam_role.emitter.id
  policy = jsonencode({{
    Version = "2012-10-17"
    Statement = [{{ Effect = "Allow", Action = ["s3:GetObject", "dynamodb:PutItem"], Resource = ["*"] }}]
  }})
}}
''',
        encoding="utf-8",
    )


@pytest.fixture
def local_named_workspace(tmp_path):
    """The live shape: role name from a plain-string local (opal-assets/emitter.tf)."""
    tf_base = tmp_path / "infra" / "aws" / "terraform"
    _write_module(
        tf_base, "opal-assets", '"${local.emitter_name}-role"',
        extra_head='locals {\n  emitter_name    = "opal-assets-daily-emitter"\n  platinum_bucket = "opal-data-portal-v2"\n}',
    )
    return tmp_path


def test_role_named_from_a_local_resolves_to_its_concrete_name(local_named_workspace):
    """THE REGRESSION. The role must key under its CONCRETE name, not the literal interpolation."""
    roles = _parse_terraform_iam(local_named_workspace)
    assert "opal-assets-daily-emitter-role" in roles, (
        "role keyed under the literal '${local.emitter_name}-role' -- it will never match the "
        "concrete name the service side reports, and every operation reads UNKNOWN")
    assert "${local.emitter_name}-role" not in roles, "the unresolved literal must not be a key"


def test_the_role_actually_carries_its_statements(local_named_workspace):
    """Keying correctly is worthless if the grants do not link. THIS is what UNKNOWN was about:
    the role existed and carried ZERO statements."""
    roles = _parse_terraform_iam(local_named_workspace)
    role = roles["opal-assets-daily-emitter-role"]
    assert len(role.statements) > 0, "role linked ZERO statements -- the exact 'role not mapped' failure"
    actions = {a for st in role.statements for a in st.actions}
    assert "s3:GetObject" in actions
    assert "dynamodb:PutItem" in actions
    assert role.grants("s3:GetObject") is True


def test_a_var_named_role_still_resolves(tmp_path):
    """NO-REGRESSION: the pre-existing ${var.X} path must keep working. The fix adds locals; it
    must not trade one resolution for the other."""
    tf_base = tmp_path / "infra" / "aws" / "terraform"
    _write_module(
        tf_base, "var-module", '"${var.name}-role"',
        extra_head='variable "name" {\n  default = "m365-mcp-gateway"\n}',
    )
    roles = _parse_terraform_iam(tmp_path)
    assert "m365-mcp-gateway-role" in roles
    assert len(roles["m365-mcp-gateway-role"].statements) > 0


def test_a_plain_literal_role_still_resolves(tmp_path):
    """NO-REGRESSION: the overwhelmingly common case -- a literal name -- is untouched."""
    tf_base = tmp_path / "infra" / "aws" / "terraform"
    _write_module(tf_base, "literal-module", '"plain-literal-role"')
    roles = _parse_terraform_iam(tmp_path)
    assert "plain-literal-role" in roles
    assert len(roles["plain-literal-role"].statements) > 0


def test_an_INTERPOLATED_local_is_not_half_guessed(tmp_path):
    """HONESTY: `_collect_module_locals` deliberately collects plain STRING locals only. A local
    that is itself an interpolation (local.x = "${var.env}-emitter") must NOT be half-guessed into
    a wrong concrete name -- a confidently-wrong role key is worse than an unresolved one, because
    it would silently attribute grants to a role that does not exist.

    The role stays unresolved (and the parser says so on stderr rather than keying it silently).
    """
    tf_base = tmp_path / "infra" / "aws" / "terraform"
    _write_module(
        tf_base, "interp-module", '"${local.emitter_name}-role"',
        extra_head='variable "env" {\n  default = "prod"\n}\nlocals {\n  emitter_name = "${var.env}-emitter"\n}',
    )
    roles = _parse_terraform_iam(tmp_path)
    # It must NOT invent a concrete name...
    assert "prod-emitter-role" not in roles, "half-guessed an interpolated local into a concrete key"
    # ...and it must NOT silently attribute the grants to some other role either.
    for name, role in roles.items():
        assert "${" in name or not role.statements or "emitter" not in name, (
            "an unresolvable role must not silently acquire grants under a wrong key")
