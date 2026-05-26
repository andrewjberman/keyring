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
# AWS-managed-policy action lookup (V4.024 FP Class B)
# ---------------------------------------------------------------------------
# Static table of common AWS-managed policies and the IAM action wildcards they
# grant. When a Lambda role has `aws_iam_role_policy_attachment` referencing one
# of these ARNs, comp-iam treats those wildcards as Allow statements during
# gap-compare — eliminating false positives where coverage came from a managed
# policy rather than an inline statement.
#
# Coverage scope: minimum-required per ADHC_COMPIL_V4.024 AC3 + ARNs observed in
# the workspace (news-pipeline, others). Unknown ARNs fall through to the cache
# + API resolver below.
_AWS_MANAGED_POLICY_ACTIONS: dict[str, list[str]] = {
    'AmazonS3ReadOnlyAccess': ['s3:Get*', 's3:List*', 's3:Describe*'],
    'AmazonS3FullAccess': ['s3:*'],
    'AmazonS3ObjectLambdaExecutionRolePolicy': ['s3-object-lambda:WriteGetObjectResponse', 'logs:CreateLogGroup', 'logs:CreateLogStream', 'logs:PutLogEvents'],
    'AWSLambdaBasicExecutionRole': ['logs:CreateLogGroup', 'logs:CreateLogStream', 'logs:PutLogEvents'],
    'service-role/AWSLambdaBasicExecutionRole': ['logs:CreateLogGroup', 'logs:CreateLogStream', 'logs:PutLogEvents'],
    'AWSLambdaVPCAccessExecutionRole': ['ec2:CreateNetworkInterface', 'ec2:DescribeNetworkInterfaces', 'ec2:DeleteNetworkInterface', 'ec2:AssignPrivateIpAddresses', 'ec2:UnassignPrivateIpAddresses', 'logs:CreateLogGroup', 'logs:CreateLogStream', 'logs:PutLogEvents'],
    'service-role/AWSLambdaVPCAccessExecutionRole': ['ec2:CreateNetworkInterface', 'ec2:DescribeNetworkInterfaces', 'ec2:DeleteNetworkInterface', 'logs:*'],
    'AmazonSSMReadOnlyAccess': ['ssm:Describe*', 'ssm:Get*', 'ssm:List*'],
    'AmazonSSMFullAccess': ['ssm:*'],
    'AmazonSSMManagedInstanceCore': ['ssm:UpdateInstanceInformation', 'ssm:ListAssociations', 'ssm:ListInstanceAssociations', 'ssm:DescribeAssociation', 'ssm:GetDocument', 'ssm:GetManifest', 'ssm:GetParameters', 'ssm:DescribeDocument', 'ssm:ListCommandInvocations', 'ssm:GetCommandInvocation', 'ssmmessages:*', 'ec2messages:*'],
    'AmazonDynamoDBFullAccess': ['dynamodb:*', 'dax:*'],
    'AmazonDynamoDBReadOnlyAccess': ['dynamodb:Get*', 'dynamodb:Query', 'dynamodb:Scan', 'dynamodb:BatchGet*', 'dynamodb:Describe*', 'dynamodb:List*'],
    'SecretsManagerReadWrite': ['secretsmanager:*', 'kms:DescribeKey', 'kms:ListAliases', 'kms:ListKeys'],
    'CloudWatchFullAccess': ['cloudwatch:*', 'logs:*', 'sns:*'],
    'CloudWatchReadOnlyAccess': ['cloudwatch:Describe*', 'cloudwatch:Get*', 'cloudwatch:List*', 'logs:Describe*', 'logs:Get*'],
    'CloudWatchLogsFullAccess': ['logs:*'],
    'CloudWatchLogsReadOnlyAccess': ['logs:Describe*', 'logs:Get*', 'logs:List*', 'logs:StartQuery', 'logs:StopQuery', 'logs:TestMetricFilter', 'logs:FilterLogEvents'],
    'AWSLambda_FullAccess': ['lambda:*', 'cloudwatch:*', 'iam:ListRoles', 'logs:*'],
    'AWSLambda_ReadOnlyAccess': ['lambda:Get*', 'lambda:List*', 'logs:Describe*', 'logs:Get*'],
    'AmazonEC2ReadOnlyAccess': ['ec2:Describe*', 'ec2:Get*', 'ec2:List*'],
    'AmazonEC2FullAccess': ['ec2:*', 'elasticloadbalancing:*', 'cloudwatch:*', 'autoscaling:*'],
}


def _managed_policy_cache_path(workspace_root: Path) -> Path:
    return workspace_root / ".comp-graph" / "managed_policy_actions_cache.json"


def _load_managed_policy_cache(workspace_root: Path) -> dict[str, list[str]]:
    p = _managed_policy_cache_path(workspace_root)
    if not p.exists():
        return {}
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _save_managed_policy_cache(workspace_root: Path, cache: dict[str, list[str]]) -> None:
    p = _managed_policy_cache_path(workspace_root)
    try:
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(cache, indent=2, sort_keys=True), encoding="utf-8")
    except Exception:
        pass


def _resolve_managed_policy_actions(
    policy_arn: str,
    cache: dict[str, list[str]],
    workspace_root: Path,
) -> tuple[list[str], str]:
    """Resolve the list of IAM actions covered by an AWS-managed policy ARN.

    Returns (actions, source) where source is 'static' | 'cache' | 'api' | 'unknown'.
    Unknown returns []; caller should emit a MANAGED_POLICY_UNKNOWN advisory and
    NOT claim coverage (per V4.024 AC4 — prefer surfacing potential FP over
    silent miss).
    """
    if not policy_arn.startswith("arn:aws:iam::aws:policy/"):
        return [], 'unknown'

    suffix = policy_arn.split("arn:aws:iam::aws:policy/", 1)[1]

    if suffix in _AWS_MANAGED_POLICY_ACTIONS:
        return list(_AWS_MANAGED_POLICY_ACTIONS[suffix]), 'static'

    if policy_arn in cache:
        return list(cache[policy_arn]), 'cache'

    try:
        import boto3  # type: ignore[import-not-found]
        iam = boto3.client('iam')
        policy = iam.get_policy(PolicyArn=policy_arn)
        version_id = policy['Policy']['DefaultVersionId']
        version = iam.get_policy_version(PolicyArn=policy_arn, VersionId=version_id)
        doc = version['PolicyVersion']['Document']
        if isinstance(doc, str):
            doc = json.loads(doc)
        actions: list[str] = []
        statements = doc.get('Statement', [])
        if not isinstance(statements, list):
            statements = [statements]
        for stmt in statements:
            if stmt.get('Effect', 'Allow') != 'Allow':
                continue
            stmt_actions = stmt.get('Action', [])
            if isinstance(stmt_actions, str):
                stmt_actions = [stmt_actions]
            actions.extend(stmt_actions)
        if actions:
            cache[policy_arn] = actions
            _save_managed_policy_cache(workspace_root, cache)
            return actions, 'api'
    except Exception:
        pass

    return [], 'unknown'


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
        """Check if this role grants the given IAM action.

        Supports `*` (any), exact match, prefix wildcard `s3:*`, and partial
        wildcards `s3:Get*` / `s3:*Object`. AWS-managed policies expanded via
        _AWS_MANAGED_POLICY_ACTIONS (V4.024) commonly use `s3:Get*` form.
        """
        action_lower = action.lower()
        for stmt in self.statements:
            if stmt.effect.lower() != 'allow':
                continue
            for a in stmt.actions:
                a_lower = a.lower()
                if a == '*' or a_lower == action_lower:
                    return True
                if '*' in a_lower:
                    pattern = re.escape(a_lower).replace(r'\*', '.*')
                    if re.fullmatch(pattern, action_lower):
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

# Variable-name pattern for triple-quoted strings shipped to EC2 — used as
# fallback when the variable isn't directly referenced in run_instances /
# send_command (e.g., variable interpolated into a larger formatted string).
_EC2_SHIP_VAR_NAMES = re.compile(
    r'^(USER_DATA(_SCRIPT)?|user_data|.*_CMD|.*_SCRIPT|.*_COMMANDS?|.*_CHAIN_CMD)$'
)


def _compute_ec2_shipped_line_ranges(content: str) -> set[int]:
    """Return line numbers (1-indexed) inside triple-quoted string assignments
    that are shipped to EC2 via ec2.run_instances UserData= or ssm.send_command
    commands=[] / Parameters={'commands': [...]}.

    AWS-CLI patterns inside such strings run on the destination EC2's instance
    profile, NOT on the Lambda's role — flagging them against the Lambda role
    is a false positive. V4.024 FP Class A elimination.

    Detection strategy: collect (var_name, line-range) for every triple-quoted
    assignment, then mark lines as shipped if (a) the var is referenced by an
    EC2-ship function arg, or (b) the var name matches a recognized ship-context
    convention (USER_DATA*, *_CMD, *_SCRIPT, *_COMMANDS).
    """
    shipped_lines: set[int] = set()

    # Step 1: find triple-quoted multi-line string assignments (var = '''...''' / """...""")
    string_ranges: dict[str, list[tuple[int, int]]] = {}
    pos = 0
    while pos < len(content):
        m = re.search(r'(\w+)\s*=\s*("""|\'\'\')', content[pos:])
        if not m:
            break
        var_name = m.group(1)
        delim = m.group(2)
        open_pos = pos + m.end()
        close_pos = content.find(delim, open_pos)
        if close_pos == -1:
            break
        start_line = content[:pos + m.start()].count('\n') + 1
        end_line = content[:close_pos].count('\n') + 1
        string_ranges.setdefault(var_name, []).append((start_line, end_line))
        pos = close_pos + len(delim)

    # Step 1b (ADHC_COMPIL_V5 post-TO-VAL refinement, 2026-05-26): also catch
    # the `"\n".join([...])` multi-line string-builder pattern, which composes a
    # shell script line-by-line for SSM-ship. Empirical anchor: mdpf-daily-
    # trigger Lambda surfaced as comp-iam-gap byproduct in COMPIL_V5.001 AC4
    # cross-product detection (bootstrap = "\n".join([..., f"aws s3 cp ...", ...])
    # → ssm.send_command(Parameters={"commands": [bootstrap]})). The aws-cli line
    # runs on EC2 under mdpf-daily-runner-ec2-role (which DOES grant s3:Get/Put),
    # not on the Lambda role — the Lambda-role IAM gap was a false positive.
    # Detection: find `var = "..."` joiner across a multi-line `.join([...])`
    # argument; capture lines between the `[` and its matching `]`.
    pos = 0
    while pos < len(content):
        m = re.search(
            r'(\w+)\s*=\s*["\'][^"\']*["\']\.join\s*\(\s*\[',
            content[pos:],
        )
        if not m:
            break
        var_name = m.group(1)
        open_bracket_pos = pos + m.end() - 1  # position of '['
        # Walk forward to matching ']' tracking bracket nesting
        depth = 1
        scan = open_bracket_pos + 1
        n = len(content)
        while scan < n and depth > 0:
            ch = content[scan]
            if ch == '[':
                depth += 1
            elif ch == ']':
                depth -= 1
            scan += 1
        if depth != 0:
            break  # unbalanced; skip
        close_bracket_pos = scan - 1
        start_line = content[:pos + m.start()].count('\n') + 1
        end_line = content[:close_bracket_pos].count('\n') + 1
        string_ranges.setdefault(var_name, []).append((start_line, end_line))
        pos = close_bracket_pos + 1

    if not string_ranges:
        return shipped_lines

    # Step 2: which of these vars are referenced as EC2-ship args?
    shipped_vars: set[str] = set()

    for m in re.finditer(r'(?:UserData|user_data)\s*=\s*(\w+)\b', content):
        shipped_vars.add(m.group(1))

    for m in re.finditer(r"['\"]commands['\"]\s*:\s*\[\s*(\w+)\s*\]", content):
        shipped_vars.add(m.group(1))
    for m in re.finditer(r"\bcommands\s*=\s*\[\s*(\w+)\s*\]", content):
        shipped_vars.add(m.group(1))

    # Step 3: name-convention fallback — variables matching ship-context naming
    # are shipped even if direct-reference detection misses them (e.g., variable
    # interpolated into a larger formatted string passed to send_command).
    for var_name in string_ranges:
        if _EC2_SHIP_VAR_NAMES.match(var_name):
            shipped_vars.add(var_name)

    # Step 4: collect line ranges for all shipped vars
    for var_name in shipped_vars:
        for (start, end) in string_ranges.get(var_name, []):
            shipped_lines.update(range(start, end + 1))

    return shipped_lines


def _scan_python_for_operations(content: str, file_path: str) -> list[Operation]:
    """Scan a Python file for boto3 client method calls and AWS CLI subprocess invocations."""
    ops = []
    lines = content.splitlines()
    ec2_shipped_lines = _compute_ec2_shipped_line_ranges(content)

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
        # Skip when the line is inside an EC2-shipped triple-quoted string (V4.024 FP Class A) —
        # the call runs on the destination EC2's instance profile, not the Lambda role.
        if lineno in ec2_shipped_lines:
            continue
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


_TF_MANAGED_POLICY_ARN = re.compile(
    r'policy_arn\s*=\s*["\'](arn:aws:iam::aws:policy/[^"\']+)["\']'
)


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

    # Third pass: parse aws_iam_role_policy_attachment with AWS-managed-policy
    # ARNs (V4.024 FP Class B) — synthesize Allow statements from static lookup
    # or cache+API fallback so gap-compare credits the role with managed coverage.
    managed_cache = _load_managed_policy_cache(workspace_root)
    for tf_file in all_tf_files:
        try:
            content = tf_file.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        rel = str(tf_file.relative_to(workspace_root)).replace("\\", "/")

        for m in _TF_POLICY_ATTACHMENT.finditer(content):
            block = _extract_tf_block(content, m.start())
            arn_m = _TF_MANAGED_POLICY_ARN.search(block)
            if not arn_m:
                continue
            policy_arn = arn_m.group(1)

            role_ref = _TF_ROLE_REF.search(block)
            if not role_ref:
                continue
            tf_role = role_ref.group(1)
            role_name = role_tf_to_name.get(tf_role)
            if not role_name or role_name not in roles:
                continue

            actions, source = _resolve_managed_policy_actions(
                policy_arn, managed_cache, workspace_root
            )
            if actions:
                roles[role_name].statements.append(IamStatement(
                    effect='Allow',
                    actions=actions,
                    resources=['*'],
                    source_file=f"{rel} (managed-policy: {policy_arn} via {source})",
                ))
            else:
                # Unknown managed policy — record advisory statement with empty
                # actions so future reporting can surface it without claiming
                # coverage.
                roles[role_name].statements.append(IamStatement(
                    effect='Allow',
                    actions=[],
                    resources=[],
                    source_file=f"{rel} (MANAGED_POLICY_UNKNOWN: {policy_arn})",
                ))

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
    """Load EC2 service scripts from EC2_MANIFEST.json and gold scripts directory.

    ADHC_COMPIL_V5.001 (2026-05-26): extended to consume the full EC2_MANIFEST.json
    catalog. Previously hardcoded ONLY bd-gold-runner (gold scripts under
    data/black_diamond/scripts/gold/[A-D]_*.py with role bd-exporter-ec2-role).
    Now iterates every manifest service with an iam_role + source_path and creates
    one ServiceProfile per service, scanning its source dir/file for boto3 ops.
    Multi-service-per-role (e.g. bd-allocations / bd-transactions / bd-fees /
    bd-assets / bd-price-runner all on bd-exporter-ec2-role) all surface in
    `comp-iam services` output and contribute to cross-product gap detection
    (AC4). Gold-script-dir hardcode preserved as bd-gold-runner profile to keep
    historical baseline + cover scripts not in manifest source_path.
    """
    profiles = []

    # Gold scripts (run on EC2 bd-gold-layer-runner) -- preserved hardcoded entry
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

    # ADHC_COMPIL_V5.001: EC2_MANIFEST.json full catalog
    manifest_file = workspace_root / "infra" / "aws" / "ec2" / "EC2_MANIFEST.json"
    if not manifest_file.exists():
        return profiles
    try:
        manifest = json.loads(manifest_file.read_text(encoding="utf-8"))
    except Exception:
        return profiles

    for svc_name, cfg in manifest.get("services", {}).items():
        if not isinstance(cfg, dict):
            continue
        iam_role = cfg.get("iam_role")
        if not iam_role:
            continue
        source_path = cfg.get("source_path") or cfg.get("source_dir")
        if not source_path:
            continue

        abs_path = workspace_root / source_path
        ops: list = []
        files_scanned: list[str] = []

        if abs_path.is_dir():
            for py_file in sorted(abs_path.rglob("*.py")):
                try:
                    content = py_file.read_text(encoding="utf-8", errors="replace")
                except Exception:
                    continue
                rel = str(py_file.relative_to(workspace_root)).replace("\\", "/")
                ops.extend(_scan_python_for_operations(content, rel))
                files_scanned.append(rel)
        elif abs_path.is_file() and abs_path.suffix == ".py":
            try:
                content = abs_path.read_text(encoding="utf-8", errors="replace")
            except Exception:
                continue
            rel = str(abs_path.relative_to(workspace_root)).replace("\\", "/")
            ops = _scan_python_for_operations(content, rel)
            files_scanned = [rel]
        else:
            # Path doesn't exist or non-Python file; still register profile
            # so service-name lookup works (role-side actions still visible).
            files_scanned = [source_path]

        profiles.append(ServiceProfile(
            name=svc_name,
            service_type="ec2",
            iam_role=iam_role,
            source_files=files_scanned or [source_path],
            operations=ops,
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
