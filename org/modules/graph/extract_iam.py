"""
IAM permission cross-reference tool.

Scans Lambda source files and gold EC2 scripts for AWS operations,
then cross-references against Terraform IAM policy documents.
Flags cases where a script calls an operation the role may not permit.

Authoritative sources:
  1. infra/aws/lambda/ci/lambda-source-map.json  -- Lambda function -> source path
  2. infra/aws/terraform/*/iam.tf               -- IAM role policies
  3. Lambda source .py files                    -- boto3 client calls
  4. data/black_diamond/scripts/gold/*.py        -- gold scripts on EC2 (boto3 + aws CLI)
  5. infra/aws/ec2/EC2_MANIFEST.json             -- EC2 service -> IAM role mapping
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


# ---------------------------------------------------------------------------
# Operation maps: source-code pattern -> IAM action
# ---------------------------------------------------------------------------

# boto3 s3 client method -> IAM action(s)
_BOTO3_S3 = {
    'get_object':       ['s3:GetObject'],
    'put_object':       ['s3:PutObject'],
    'delete_object':    ['s3:DeleteObject'],
    'delete_objects':   ['s3:DeleteObject'],
    'list_objects':     ['s3:ListBucket'],
    'list_objects_v2':  ['s3:ListBucket'],
    'copy_object':      ['s3:CopyObject', 's3:GetObject'],
    'head_object':      ['s3:GetObject'],
    'upload_file':      ['s3:PutObject'],
    'upload_fileobj':   ['s3:PutObject'],
    'download_file':    ['s3:GetObject'],
    'download_fileobj': ['s3:GetObject'],
    'get_paginator':    [],  # ListBucket-like, but depends on paginator used
}

# boto3 ssm client method -> IAM action(s)
_BOTO3_SSM = {
    'send_command':             ['ssm:SendCommand'],
    'get_command_invocation':   ['ssm:GetCommandInvocation'],
    'put_parameter':            ['ssm:PutParameter'],
    'get_parameter':            ['ssm:GetParameter'],
    'get_parameters':           ['ssm:GetParameters'],
    'describe_instance_information': ['ssm:DescribeInstanceInformation'],
}

# boto3 dynamodb/resource method -> IAM action(s)
_BOTO3_DYNAMODB = {
    'put_item':     ['dynamodb:PutItem'],
    'get_item':     ['dynamodb:GetItem'],
    'update_item':  ['dynamodb:UpdateItem'],
    'delete_item':  ['dynamodb:DeleteItem'],
    'query':        ['dynamodb:Query'],
    'scan':         ['dynamodb:Scan'],
    'batch_write_item': ['dynamodb:BatchWriteItem'],
    'batch_get_item':   ['dynamodb:BatchGetItem'],
}

# AWS CLI patterns in shell/Python subprocess -> IAM action(s)
_AWS_CLI_S3 = [
    (re.compile(r'aws\s+s3\s+rm\b'),         ['s3:DeleteObject']),
    (re.compile(r'aws\s+s3\s+cp\b'),          ['s3:GetObject', 's3:PutObject']),
    (re.compile(r'aws\s+s3\s+sync\b'),         ['s3:GetObject', 's3:PutObject', 's3:ListBucket']),
    (re.compile(r'aws\s+s3\s+ls\b'),           ['s3:ListBucket']),
    (re.compile(r'aws\s+s3\s+mv\b'),           ['s3:GetObject', 's3:PutObject', 's3:DeleteObject']),
    (re.compile(r'aws\s+s3api\s+delete-object\b'), ['s3:DeleteObject']),
    (re.compile(r'aws\s+s3api\s+put-object\b'),    ['s3:PutObject']),
    (re.compile(r'aws\s+s3api\s+get-object\b'),    ['s3:GetObject']),
    (re.compile(r'aws\s+ssm\s+send-command\b'),    ['ssm:SendCommand']),
    (re.compile(r'aws\s+ssm\s+get-parameter\b'),   ['ssm:GetParameter']),
    (re.compile(r'aws\s+lambda\s+invoke\b'),        ['lambda:InvokeFunction']),
]


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

@dataclass
class Operation:
    """An AWS operation detected in source code."""
    iam_actions: list[str]         # e.g., ['s3:DeleteObject']
    source_pattern: str            # e.g., 's3.delete_object'
    file_path: str
    line_number: int


@dataclass
class IamStatement:
    """A single Allow/Deny statement in an IAM policy."""
    effect: str                    # Allow or Deny
    actions: list[str]             # e.g., ['s3:GetObject', 's3:PutObject']
    resources: list[str]           # e.g., ['arn:aws:s3:::opal-data-bd/*']
    source_file: str


@dataclass
class IamRole:
    """An IAM role with its attached policies."""
    role_name: str                 # e.g., bd-exporter-ec2-role
    tf_resource: str               # terraform resource name
    statements: list[IamStatement] = field(default_factory=list)
    source_file: str = ""

    def grants(self, action: str) -> bool:
        """Check if this role grants the given IAM action."""
        action_lower = action.lower()
        for stmt in self.statements:
            if stmt.effect.lower() != 'allow':
                continue
            for a in stmt.actions:
                if a == '*' or a.lower() == action_lower:
                    return True
                # Wildcard: s3:* matches s3:DeleteObject
                if a.endswith(':*') and action_lower.startswith(a[:-1].lower()):
                    return True
        return False


@dataclass
class ServiceProfile:
    """A Lambda function or EC2 service with its IAM role and detected operations."""
    name: str                      # e.g., bd-gold-trigger
    service_type: str              # lambda or ec2
    iam_role: Optional[str]        # role name
    source_files: list[str] = field(default_factory=list)
    operations: list[Operation] = field(default_factory=list)


@dataclass
class PermissionGap:
    """A detected permission gap: service calls an action its role doesn't grant."""
    service: str
    iam_role: str
    iam_action: str
    source_pattern: str
    file_path: str
    line_number: int
    severity: str = "ERROR"        # ERROR if blocking, WARN if non-critical


# ---------------------------------------------------------------------------
# Step 1: Extract operations from Python source
# ---------------------------------------------------------------------------

def _scan_python_for_operations(content: str, file_path: str) -> list[Operation]:
    """Scan a Python file for boto3 client method calls and AWS CLI subprocess invocations."""
    ops = []
    lines = content.splitlines()

    # Map client variable names to service: s3_client = boto3.client('s3') -> {'s3_client': 's3'}
    client_map: dict[str, str] = {}
    for m in re.finditer(
        r'(\w+)\s*=\s*(?:boto3\.client|boto3\.resource|self\.\w+\.client)\s*\(\s*[\'"](\w+)[\'"]',
        content
    ):
        client_map[m.group(1)] = m.group(2)

    # Also: self.s3 = boto3.client('s3') inside __init__
    for m in re.finditer(
        r'self\.(\w+)\s*=\s*boto3\.client\s*\(\s*[\'"](\w+)[\'"]',
        content
    ):
        client_map[f'self.{m.group(1)}'] = m.group(2)
        client_map[m.group(1)] = m.group(2)  # also plain name

    # Scan line by line for method calls on known clients
    for lineno, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith('#'):
            continue

        # boto3 method calls: client_var.method_name(
        for client_var, service in client_map.items():
            if client_var not in line:
                continue
            # Match: client_var.method_name(
            for m in re.finditer(
                rf'\b{re.escape(client_var)}\.(\w+)\s*\(',
                line
            ):
                method = m.group(1)
                action_map = {}
                if service in ('s3', 's3_client'):
                    action_map = _BOTO3_S3
                elif service == 'ssm':
                    action_map = _BOTO3_SSM
                elif service in ('dynamodb', 'DynamoDB'):
                    action_map = _BOTO3_DYNAMODB

                if method in action_map:
                    actions = action_map[method]
                    if actions:
                        ops.append(Operation(
                            iam_actions=actions,
                            source_pattern=f'{client_var}.{method}',
                            file_path=file_path,
                            line_number=lineno,
                        ))

        # Generic boto3 method calls even without tracked client var
        # e.g.: boto3.client('s3').delete_object(...)
        for m in re.finditer(r"boto3\.client\s*\(\s*['\"](\w+)['\"]\s*\)\.(\w+)\s*\(", line):
            service = m.group(1)
            method = m.group(2)
            action_map = {}
            if service == 's3':
                action_map = _BOTO3_S3
            elif service == 'ssm':
                action_map = _BOTO3_SSM
            elif service == 'dynamodb':
                action_map = _BOTO3_DYNAMODB
            if method in action_map and action_map[method]:
                ops.append(Operation(
                    iam_actions=action_map[method],
                    source_pattern=f"boto3.client('{service}').{method}",
                    file_path=file_path,
                    line_number=lineno,
                ))

        # AWS CLI via subprocess: subprocess.run(['aws', 's3', 'rm', ...]) or os.system('aws s3 rm ...')
        for pat, actions in _AWS_CLI_S3:
            if pat.search(line):
                ops.append(Operation(
                    iam_actions=actions,
                    source_pattern=pat.pattern.replace(r'\b', '').replace(r'\s+', ' '),
                    file_path=file_path,
                    line_number=lineno,
                ))
                break  # one match per line is enough

    return ops


# ---------------------------------------------------------------------------
# Step 2: Parse Terraform IAM policies
# ---------------------------------------------------------------------------

_TF_ROLE_RESOURCE = re.compile(
    r'resource\s+"aws_iam_role"\s+"(\w+)"\s*\{'
)
_TF_ROLE_NAME = re.compile(r'name\s*=\s*"([^"]+)"')

_TF_POLICY_RESOURCE = re.compile(
    r'resource\s+"aws_iam_(?:role_)?policy"\s+"(\w+)"\s*\{'
)
_TF_POLICY_ATTACHMENT = re.compile(
    r'resource\s+"aws_iam_role_policy_attachment"\s+"(\w+)"\s*\{'
)
_TF_ROLE_REF = re.compile(r'role\s*=\s*aws_iam_role\.(\w+)\.(?:name|id)')
_TF_JSONENCODE_EFFECT = re.compile(r'["\']effect["\']\s*:\s*["\'](Allow|Deny)["\']', re.IGNORECASE)
_TF_JSONENCODE_ACTIONS = re.compile(
    r'["\']actions?["\']\s*:\s*\[([^\]]+)\]', re.IGNORECASE | re.DOTALL
)
_TF_JSONENCODE_ACTION_SINGLE = re.compile(
    r'["\']actions?["\']\s*:\s*["\']([^"\']+)["\']', re.IGNORECASE
)


def _extract_tf_block(content: str, start: int) -> str:
    """Extract the {} block starting at or after position start."""
    brace_pos = content.find('{', start)
    if brace_pos == -1:
        return ""
    depth = 1
    i = brace_pos + 1
    while i < len(content) and depth > 0:
        if content[i] == '{':
            depth += 1
        elif content[i] == '}':
            depth -= 1
        i += 1
    return content[brace_pos:i]


def _parse_iam_statements(policy_text: str, source_file: str) -> list[IamStatement]:
    """Parse IAM statements from a jsonencode() block.

    Handles both HCL style (Terraform jsonencode):
        Statement = [{ Effect = "Allow" Action = ["s3:GetObject"] }]
    and JSON style:
        "Statement": [{ "Effect": "Allow", "Action": ["s3:GetObject"] }]
    """
    statements = []

    # Find Statement = [...] or "Statement": [...] arrays using depth-balanced
    # bracket matching. Regex alone fails because Terraform nests Action = [...]
    # and Resource = [...] arrays inside each Statement — non-greedy .+? matches
    # the inner ] first, and a lookahead for } fails on HCL's jsonencode ")"
    # closing char.
    anchor_re = re.compile(
        r'(?:["\']Statement["\']\s*:|Statement\s*=)\s*\[',
        re.IGNORECASE,
    )

    def _find_statement_arrays(text: str) -> list[str]:
        results = []
        for am in anchor_re.finditer(text):
            array_start = am.end() - 1  # position of opening [
            depth = 1
            i = array_start + 1
            while i < len(text) and depth > 0:
                ch = text[i]
                if ch == '[':
                    depth += 1
                elif ch == ']':
                    depth -= 1
                i += 1
            if depth == 0:
                results.append(text[array_start + 1:i - 1])
        return results

    # Shim the old stmt_re interface so the rest of the function works unchanged
    class _Match:
        def __init__(self, content): self._content = content
        def group(self, n): return self._content

    stmt_re = type('_StmtRE', (), {
        'finditer': lambda self, text: (_Match(c) for c in _find_statement_arrays(text))
    })()

    # Unified field patterns — match either HCL (Key = "val") or JSON ("Key": "val")
    def _field_value(name: str, text: str) -> str | None:
        """Extract a single string value for field `name` from HCL or JSON."""
        m = re.search(
            rf'(?:["\']?{name}["\']?\s*[=:]\s*)["\']([^"\']+)["\']',
            text, re.IGNORECASE
        )
        return m.group(1) if m else None

    def _field_array(name: str, text: str) -> list[str]:
        """Extract string array values for field `name` from HCL or JSON."""
        m = re.search(
            rf'(?:["\']?{name}["\']?\s*[=:]\s*)\[([^\]]+)\]',
            text, re.DOTALL | re.IGNORECASE
        )
        if m:
            # Extract only quoted strings (skip TF references like aws_instance.foo.arn)
            return re.findall(r'["\']([^"\']+)["\']', m.group(1))
        # Fallback: single unquoted or quoted value
        single = _field_value(name, text)
        return [single] if single else []

    for sm in stmt_re.finditer(policy_text):
        stmt_block = sm.group(1)

        # Walk the array content, extracting each { ... } statement block
        depth = 0
        start = -1
        for i, c in enumerate(stmt_block):
            if c == '{':
                if depth == 0:
                    start = i
                depth += 1
            elif c == '}':
                depth -= 1
                if depth == 0 and start >= 0:
                    single_stmt = stmt_block[start:i+1]

                    effect = _field_value('Effect', single_stmt) or 'Allow'
                    actions = _field_array('Action', single_stmt)
                    resources = _field_array('Resource', single_stmt)

                    if actions:
                        statements.append(IamStatement(
                            effect=effect,
                            actions=actions,
                            resources=resources,
                            source_file=source_file,
                        ))
                    start = -1

    return statements


def _parse_terraform_iam(workspace_root: Path) -> dict[str, IamRole]:
    """Parse all IAM roles and their policies from Terraform files.
    Returns dict: role_name -> IamRole."""
    roles: dict[str, IamRole] = {}

    tf_base = workspace_root / "infra" / "aws" / "terraform"
    if not tf_base.exists():
        return roles

    all_tf_files = list(tf_base.rglob("*.tf"))

    # First pass: collect all role definitions
    role_tf_to_name: dict[str, str] = {}  # tf_resource_name -> role_name
    for tf_file in all_tf_files:
        try:
            content = tf_file.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        rel = str(tf_file.relative_to(workspace_root)).replace("\\", "/")

        for m in _TF_ROLE_RESOURCE.finditer(content):
            tf_res = m.group(1)
            block = _extract_tf_block(content, m.start())
            name_m = _TF_ROLE_NAME.search(block)
            if name_m:
                role_name = name_m.group(1)
                role_tf_to_name[tf_res] = role_name
                if role_name not in roles:
                    roles[role_name] = IamRole(
                        role_name=role_name,
                        tf_resource=tf_res,
                        source_file=rel,
                    )

    # Second pass: parse inline policies and attach to roles
    for tf_file in all_tf_files:
        try:
            content = tf_file.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        rel = str(tf_file.relative_to(workspace_root)).replace("\\", "/")

        # aws_iam_role_policy (inline policy on a role)
        for m in _TF_POLICY_RESOURCE.finditer(content):
            block = _extract_tf_block(content, m.start())
            role_ref = _TF_ROLE_REF.search(block)
            if not role_ref:
                continue
            tf_role = role_ref.group(1)
            role_name = role_tf_to_name.get(tf_role)
            if not role_name or role_name not in roles:
                continue

            # Parse the policy JSON (embedded in jsonencode or heredoc)
            stmts = _parse_iam_statements(block, rel)
            roles[role_name].statements.extend(stmts)

        # aws_iam_policy (standalone policy document)
        for m in re.finditer(r'resource\s+"aws_iam_policy"\s+"(\w+)"\s*\{', content):
            block = _extract_tf_block(content, m.start())
            stmts = _parse_iam_statements(block, rel)
            if not stmts:
                continue

            # Try to find which role this policy is attached to
            # Look for aws_iam_role_policy_attachment referencing this policy
            policy_tf_name = m.group(1)
            attachment_re = re.compile(
                rf'policy_arn\s*=\s*aws_iam_policy\.{re.escape(policy_tf_name)}\.arn'
            )
            for attach_m in re.finditer(r'resource\s+"aws_iam_role_policy_attachment"\s+"\w+"\s*\{', content):
                attach_block = _extract_tf_block(content, attach_m.start())
                if not attachment_re.search(attach_block):
                    continue
                role_ref = _TF_ROLE_REF.search(attach_block)
                if role_ref:
                    tf_role = role_ref.group(1)
                    role_name = role_tf_to_name.get(tf_role)
                    if role_name and role_name in roles:
                        roles[role_name].statements.extend(stmts)

    return roles


# ---------------------------------------------------------------------------
# Step 3: Load service profiles (Lambda + EC2)
# ---------------------------------------------------------------------------

def _load_lambda_profiles(workspace_root: Path, roles: dict[str, IamRole]) -> list[ServiceProfile]:
    """Load Lambda functions from lambda-source-map.json and scan their source."""
    source_map_file = workspace_root / "infra" / "aws" / "lambda" / "ci" / "lambda-source-map.json"
    if not source_map_file.exists():
        return []

    try:
        source_map = json.loads(source_map_file.read_text(encoding="utf-8"))
    except Exception:
        return []

    # Support nested structure: merge 'functions' sub-dict into top-level iteration
    if isinstance(source_map.get("functions"), dict):
        merged = dict(source_map["functions"])
        for k, v in source_map.items():
            if k != "functions" and isinstance(v, dict):
                merged[k] = v
        source_map = merged

    profiles = []
    for fn_name, entry in source_map.items():
        if isinstance(entry, dict):
            source_path = entry.get("source") or entry.get("path") or entry.get("source_dir") or ""
            iam_role = entry.get("role") or entry.get("iam_role") or ""
        else:
            source_path = str(entry)
            iam_role = ""

        if not source_path:
            continue

        abs_path = workspace_root / source_path
        if abs_path.is_dir():
            candidates = list(abs_path.glob("lambda_function.py")) + list(abs_path.glob("index.py"))
            if not candidates:
                continue
            abs_path = candidates[0]

        if not abs_path.exists():
            continue

        try:
            content = abs_path.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue

        rel = str(abs_path.relative_to(workspace_root)).replace("\\", "/")
        ops = _scan_python_for_operations(content, rel)

        profile = ServiceProfile(
            name=fn_name,
            service_type="lambda",
            iam_role=iam_role or None,
            source_files=[rel],
            operations=ops,
        )
        profiles.append(profile)

    return profiles


def _load_ec2_profiles(workspace_root: Path) -> list[ServiceProfile]:
    """Load EC2 service scripts from EC2_MANIFEST.json and gold scripts directory."""
    profiles = []

    # Gold scripts (run on EC2 bd-gold-layer-runner)
    gold_dir = workspace_root / "data" / "black_diamond" / "scripts" / "gold"
    if gold_dir.exists():
        gold_ops = []
        for py_file in sorted(gold_dir.glob("[A-D]_*.py")):
            try:
                content = py_file.read_text(encoding="utf-8", errors="replace")
            except Exception:
                continue
            rel = str(py_file.relative_to(workspace_root)).replace("\\", "/")
            ops = _scan_python_for_operations(content, rel)
            gold_ops.extend(ops)

        if gold_ops:
            profiles.append(ServiceProfile(
                name="bd-gold-runner (EC2)",
                service_type="ec2",
                iam_role="bd-exporter-ec2-role",  # known from EC2_MANIFEST
                source_files=["data/black_diamond/scripts/gold/*.py"],
                operations=gold_ops,
            ))

    return profiles


# ---------------------------------------------------------------------------
# Main: build full IAM gap report
# ---------------------------------------------------------------------------

def build_iam_report(workspace_root: Path) -> tuple[list[ServiceProfile], dict[str, IamRole], list[PermissionGap]]:
    """Build the full IAM cross-reference report.
    Returns (profiles, roles, gaps)."""
    roles = _parse_terraform_iam(workspace_root)
    lambda_profiles = _load_lambda_profiles(workspace_root, roles)
    ec2_profiles = _load_ec2_profiles(workspace_root)
    all_profiles = lambda_profiles + ec2_profiles

    gaps = []
    for profile in all_profiles:
        if not profile.iam_role:
            continue
        role = roles.get(profile.iam_role)
        if not role:
            continue  # role not found in Terraform -- may be managed policy

        for op in profile.operations:
            for action in op.iam_actions:
                if not role.grants(action):
                    gaps.append(PermissionGap(
                        service=profile.name,
                        iam_role=profile.iam_role,
                        iam_action=action,
                        source_pattern=op.source_pattern,
                        file_path=op.file_path,
                        line_number=op.line_number,
                        severity="ERROR",
                    ))

    return all_profiles, roles, gaps
