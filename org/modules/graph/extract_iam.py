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
import os
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

# SOVEREIGN sec.8 HOLD (CLAUDE.md / memory: 49F/bd/Schwab standing hold). IAM1 (CTO 20260710T222627Z):
# extract_iam.py read_text()s data/black_diamond gold + manifest-driven bd source on EVERY comp-iam
# command (build_iam_report -> _build). That FALSIFIED sec.8's "comp-iam runs freely" clearance (a tool
# that reads bd CONTENT, not just TF metadata). This is the 6th content-reader guard.
#   - COMP_IAM_INCLUDE_HELD=1 SET -> bd gold/service SOURCE scanned (pipeline / explicit opt-in).
#   - UNSET (default agent) -> a held-path SOURCE read is SKIPPED (returns None), loud-noted ONCE.
# comp-iam KEEPS its bd ROLE / TF-IAM-policy analysis -- that is genuine sec.8-safe METADATA (the TF
# policy documents), NOT the gold/service .py source. The decision is a pure str.startswith on the
# relative path -- it NEVER opens a held file to decide (the load-bearing property of every prior guard).
_HELD_SOURCE_PREFIXES = (
    "data/black_diamond/",
    "data/canonical/schwab/silver/",
)
_HELD_NOTE_EMITTED = {"done": False}


def _rel_is_held(rel: str) -> bool:
    return rel.replace("\\", "/").startswith(_HELD_SOURCE_PREFIXES)


def _include_held() -> bool:
    return os.environ.get("COMP_IAM_INCLUDE_HELD") == "1"


def _read_source_if_allowed(abs_path: Path, workspace_root: Path) -> Optional[str]:
    """read_text(abs_path) UNLESS it is a sec.8-held source path and the hold is in effect.
    Returns the file text, or None when the read is refused (held + no opt-in) or on any OS error.
    A held refusal is decided by the RELATIVE PATH string -- the held file is never opened to decide."""
    try:
        rel = str(abs_path.relative_to(workspace_root)).replace("\\", "/")
    except ValueError:
        rel = str(abs_path).replace("\\", "/")
    if _rel_is_held(rel) and not _include_held():
        if not _HELD_NOTE_EMITTED["done"]:
            print("NOTE: held gold/service SOURCE NOT scanned: sovereign hold (agent context) -- "
                  "comp-iam bd role/IAM-policy analysis is from TF metadata only. "
                  "Set COMP_IAM_INCLUDE_HELD=1 for the full scan (pipeline/opt-in).", file=sys.stderr)
            _HELD_NOTE_EMITTED["done"] = True
        return None
    try:
        return abs_path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return None


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

# boto3 secretsmanager method -> IAM action(s)
_BOTO3_SECRETSMANAGER = {
    'get_secret_value': ['secretsmanager:GetSecretValue'],
    'list_secrets':     ['secretsmanager:ListSecrets'],
    'describe_secret':  ['secretsmanager:DescribeSecret'],
    'put_secret_value': ['secretsmanager:PutSecretValue'],
    'create_secret':    ['secretsmanager:CreateSecret'],
}

# boto3 ec2 method -> IAM action(s). get_waiter polls describe_* (separately detected).
_BOTO3_EC2 = {
    'describe_instances':       ['ec2:DescribeInstances'],
    'start_instances':          ['ec2:StartInstances'],
    'stop_instances':           ['ec2:StopInstances'],
    'run_instances':            ['ec2:RunInstances'],
    'terminate_instances':      ['ec2:TerminateInstances'],
    'describe_volumes':         ['ec2:DescribeVolumes'],
    'describe_security_groups': ['ec2:DescribeSecurityGroups'],
    'describe_addresses':       ['ec2:DescribeAddresses'],
    'get_waiter':               [],
}

# boto3 lambda method -> IAM action(s)
_BOTO3_LAMBDA = {
    'invoke':         ['lambda:InvokeFunction'],
    'invoke_async':   ['lambda:InvokeFunction'],
    'list_functions': ['lambda:ListFunctions'],
    'get_function':   ['lambda:GetFunction'],
    'get_paginator':  [],
}

# boto3 sns method -> IAM action(s)
_BOTO3_SNS = {
    'publish': ['sns:Publish'],
}

# boto3 stepfunctions method -> IAM action(s). NOTE: client('stepfunctions') but
# the IAM action prefix is 'states:'.
_BOTO3_STEPFUNCTIONS = {
    'start_execution':        ['states:StartExecution'],
    'stop_execution':         ['states:StopExecution'],
    'describe_execution':     ['states:DescribeExecution'],
    'list_state_machines':    ['states:ListStateMachines'],
    'describe_state_machine': ['states:DescribeStateMachine'],
}

# boto3 cloudfront method -> IAM action(s)
_BOTO3_CLOUDFRONT = {
    'create_invalidation': ['cloudfront:CreateInvalidation'],
    'list_distributions':  ['cloudfront:ListDistributions'],
    'get_invalidation':    ['cloudfront:GetInvalidation'],
}

# boto3 cloudwatch method -> IAM action(s)
_BOTO3_CLOUDWATCH = {
    'put_metric_data':       ['cloudwatch:PutMetricData'],
    'get_metric_statistics': ['cloudwatch:GetMetricStatistics'],
    'put_metric_alarm':      ['cloudwatch:PutMetricAlarm'],
}

# Unified service -> method-map registry. A boto3 client of any service NOT in
# this registry produces an UNMODELED sentinel (coverage-unknown, surfaced LOUD)
# rather than a silent zero-ops "no gap". Modeling a new service = add its map
# here. The 7 services below were added after comp-iam's UNMODELED sweep surfaced
# 50 coverage-unknowns (secretsmanager secret-reads, ec2 start/stop, lambda
# invoke, sns, stepfunctions, cloudfront, cloudwatch) -- now VERIFIED, not just
# flagged. Method maps grounded in the actual calls in infra/aws/lambda.
_BOTO3_BY_SERVICE: dict[str, dict] = {
    's3': _BOTO3_S3, 's3_client': _BOTO3_S3,
    'ssm': _BOTO3_SSM,
    'dynamodb': _BOTO3_DYNAMODB, 'DynamoDB': _BOTO3_DYNAMODB,
    'secretsmanager': _BOTO3_SECRETSMANAGER,
    'ec2': _BOTO3_EC2,
    'lambda': _BOTO3_LAMBDA,
    'sns': _BOTO3_SNS,
    'stepfunctions': _BOTO3_STEPFUNCTIONS, 'sfn': _BOTO3_STEPFUNCTIONS,
    'cloudfront': _BOTO3_CLOUDFRONT,
    'cloudwatch': _BOTO3_CLOUDWATCH,
}
_MODELED_BOTO3_SERVICES = set(_BOTO3_BY_SERVICE)

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
    # --- NFRA_COMPIAM_RESOURCE (0.8.0, 2026-07-10) -------------------------
    # The RESOURCE the call actually touches. Before this, `Operation` had no
    # resource field at all: comp-iam matched the ACTION NAME and never knew
    # what the call addressed, so `s3:GetObject` on a bucket the role does not
    # hold printed [GRANTED]. The verdict was invariant to the truth -- GRANTED
    # when simulate-principal-policy said implicitDeny, and GRANTED after the
    # grant landed (mdpf-daily-trigger / opal-data-portal-v2, ed415e268).
    #
    # resource_arn may contain '*' where a segment could not be statically
    # resolved (a runtime variable). `resource_exact` records whether ANY '*'
    # was introduced by resolution -- it governs whether a "no statement
    # matched" result is DEFINITIVE (exact) or merely UNRESOLVABLE (inexact).
    # Never fold an unresolvable resource into GRANTED.
    resource_arn: Optional[str] = None   # e.g. 'arn:aws:s3:::opal-data-inf/gold/x.json'
    resource_exact: bool = False         # True iff no '*' was introduced by us
    resource_expr: str = ""              # raw source expr, e.g. 'Bucket=PLATINUM_BUCKET, Key=f"{P}/{as_of}.json"'


# ---------------------------------------------------------------------------
# NFRA_COMPIAM_RESOURCE -- resolving WHAT a call touches
# ---------------------------------------------------------------------------
# S3 splits its ARN space: object actions address `arn:aws:s3:::bucket/key`,
# bucket actions address `arn:aws:s3:::bucket` (NO trailing slash). A policy
# granting `bucket/*` does NOT grant s3:ListBucket, and vice versa. Modeling
# them as one space is the same action-for-resource defect one level down.
_S3_BUCKET_LEVEL_ACTIONS = {
    's3:listbucket', 's3:listbucketversions', 's3:getbucketlocation',
    's3:getbucketpolicy', 's3:listbucketmultipartuploads',
}

# `NAME = os.environ.get("X", "default")` / `os.getenv("X", "default")`
_PY_ENV_CONST = re.compile(
    r'^\s*([A-Za-z_][A-Za-z0-9_]*)\s*=\s*os\.(?:environ\.get|getenv)\s*\(\s*'
    r'["\'][^"\']*["\']\s*,\s*["\']([^"\']*)["\']\s*\)', re.M)
# `NAME = "literal"` (no interpolation, no f-string)
_PY_LIT_CONST = re.compile(
    r'^\s*([A-Za-z_][A-Za-z0-9_]*)\s*=\s*["\']([^"\'{}]*)["\']\s*(?:#.*)?$', re.M)
# `{expr}` inside an f-string
_FSTRING_FIELD = re.compile(r'\{([^{}!:]+)(?:![rsa])?(?::[^{}]*)?\}')
# any residual Terraform interpolation, e.g. ${local.x}, ${aws_instance.y.id}
_TF_ANY_INTERP = re.compile(r'\$\{[^}]*\}')
_TF_LOCAL_INTERP = re.compile(r'\$\{local\.([A-Za-z_][A-Za-z0-9_]*)\}')
# `name = "literal"` inside a `locals { }` block (string literals only)
_TF_LOCAL_ASSIGN = re.compile(
    r'^\s*([A-Za-z_][A-Za-z0-9_]*)\s*=\s*"([^"$]*)"\s*(?:#.*)?$', re.M)
_TF_LOCALS_BLOCK = re.compile(r'^\s*locals\s*\{', re.M)


def _build_py_const_map(content: str) -> dict[str, str]:
    """Module-level string constants a call site can reference by name.

    Deliberately narrow: env-with-literal-default and bare string literals. An
    `os.environ["X"]` (no default) is NOT resolvable and must stay unresolved --
    guessing it would manufacture a confident wrong ARN.
    """
    consts: dict[str, str] = {}
    for m in _PY_LIT_CONST.finditer(content):
        consts[m.group(1)] = m.group(2)
    # env-with-default wins over a bare literal of the same name (later binding)
    for m in _PY_ENV_CONST.finditer(content):
        consts[m.group(1)] = m.group(2)
    return consts


def _balanced_call_args(text: str, open_paren: int, max_chars: int = 2000) -> str:
    """Return the argument text between `open_paren` and its matching ')'.

    Calls routinely span lines (`s3.get_object(Bucket=B, Key=k,\\n  Range=...)`),
    so a line-local regex sees `Bucket=B, Key=k,` and silently loses nothing --
    but a call whose Bucket sits on line 2 would be missed entirely. Walk the
    real parens. Quote-aware so a ')' inside a string never closes the call.
    """
    depth = 0
    i = open_paren
    end = min(len(text), open_paren + max_chars)
    quote = ''
    while i < end:
        c = text[i]
        if quote:
            if c == '\\':
                i += 2
                continue
            if c == quote:
                quote = ''
        elif c in '"\'':
            quote = c
        elif c == '(':
            depth += 1
        elif c == ')':
            depth -= 1
            if depth == 0:
                return text[open_paren + 1:i]
        i += 1
    return ''


def _kwarg_expr(argtext: str, name: str) -> Optional[str]:
    """Extract the raw expression bound to keyword `name` at paren/bracket depth 0."""
    m = re.search(rf'\b{re.escape(name)}\s*=', argtext)
    if not m:
        return None
    i = m.end()
    depth = 0
    quote = ''
    out = []
    while i < len(argtext):
        c = argtext[i]
        if quote:
            out.append(c)
            if c == '\\' and i + 1 < len(argtext):
                out.append(argtext[i + 1])
                i += 2
                continue
            if c == quote:
                quote = ''
        elif c in '"\'':
            quote = c
            out.append(c)
        elif c in '([{':
            depth += 1
            out.append(c)
        elif c in ')]}':
            if depth == 0:
                break
            depth -= 1
            out.append(c)
        elif c == ',' and depth == 0:
            break
        else:
            out.append(c)
        i += 1
    return ''.join(out).strip() or None


def _resolve_py_expr(expr: Optional[str], consts: dict[str, str]) -> tuple[Optional[str], bool]:
    """Resolve a call-site expression to a literal string.

    Returns (value, exact). `exact=False` means we substituted '*' for at least
    one segment we could not resolve -- the value is a PATTERN, not a key, and a
    caller must not treat a failed match against it as definitive.
    Returns (None, False) when nothing at all could be resolved.
    """
    if not expr:
        return (None, False)
    e = expr.strip()

    # plain string literal
    m = re.fullmatch(r'["\']([^"\']*)["\']', e)
    if m:
        return (m.group(1), True)

    # bare NAME
    if re.fullmatch(r'[A-Za-z_][A-Za-z0-9_]*', e):
        if e in consts:
            return (consts[e], True)
        return (None, False)

    # f-string: resolve {NAME} fields we know, '*' the rest
    fm = re.fullmatch(r'f["\'](.*)["\']', e, re.S)
    if fm:
        body = fm.group(1)
        exact = True

        def _sub(mm):
            nonlocal exact
            field = mm.group(1).strip()
            if field in consts:
                return consts[field]
            exact = False
            return '*'

        val = _FSTRING_FIELD.sub(_sub, body)
        val = re.sub(r'\*{2,}', '*', val)
        return (val, exact)

    # os.environ.get("X", "lit") inline at the call site
    em = re.fullmatch(r'os\.(?:environ\.get|getenv)\s*\(\s*["\'][^"\']*["\']\s*,\s*["\']([^"\']*)["\']\s*\)', e)
    if em:
        return (em.group(1), True)

    return (None, False)


def _s3_arn(bucket: Optional[str], key: Optional[str], key_exact: bool,
            bucket_level: bool) -> tuple[Optional[str], bool]:
    """Build an S3 ARN. No bucket -> nothing checkable."""
    if not bucket:
        return (None, False)
    if bucket_level:
        return (f'arn:aws:s3:::{bucket}', True)
    if key is None:
        return (f'arn:aws:s3:::{bucket}/*', False)
    return (f'arn:aws:s3:::{bucket}/{key}', key_exact)


def _arn_bucket(arn: str) -> Optional[str]:
    """'arn:aws:s3:::b/k' -> 'b'."""
    if not arn.startswith('arn:aws:s3:::'):
        return None
    return arn[len('arn:aws:s3:::'):].split('/', 1)[0] or None


def _iam_resource_matches(policy_res: str, arn: str) -> Optional[bool]:
    """Does a policy Resource pattern cover `arn`?

    THREE states, and the third is the whole point:
      True  -- covered.
      False -- definitively not covered.
      None  -- INDETERMINATE: the policy string still holds an unresolved
               Terraform interpolation (`${aws_instance.x.id}`), so we cannot
               say. Treating None as True is exactly the defect this fixes,
               one level down.
    """
    if policy_res == '*':
        return True
    if _TF_ANY_INTERP.search(policy_res):
        return None
    pat = re.escape(policy_res).replace(r'\*', '.*').replace(r'\?', '.')
    # CASE-SENSITIVE. (CVO P0, 2026-07-10.) This line carried `re.IGNORECASE`, and
    # S3 OBJECT KEYS ARE CASE-SENSITIVE -- IAM matches the resource-id verbatim.
    # EXERCISED on the live plane against lambda-execution-role, whose grant is
    # `arn:aws:s3:::opal-data-pm/*/processed/*`:
    #     .../PFDE/processed/x.json  -> allowed
    #     .../PFDE/PROCESSED/x.json  -> implicitDeny
    #     .../PFDE/Processed/x.json  -> implicitDeny
    # With IGNORECASE, a policy on `Public/*` matched a call to `public/secret.json`.
    # DIRECTION OF HARM: a false GRANT *suppresses* UNGRANTED-RESOURCE -- the very
    # verdict this tool exists to emit. The original defect (output independent of the
    # resource) survived in this same expression as output independent of its CASE.
    # Bucket names are lowercase by AWS constraint, so dropping IGNORECASE wholesale
    # is conservative and loses nothing.
    return re.fullmatch(pat, arn) is not None


# `copy_object(Bucket=dst, Key=k, CopySource=src)` emits BOTH s3:CopyObject and
# s3:GetObject -- but GetObject addresses the SOURCE, not `Bucket=`. Modeling it
# from the kwargs would produce a confident WRONG ARN. Refuse to guess.
_S3_AMBIGUOUS_METHODS = {'copy_object'}

# Methods whose bucket/key arrive POSITIONALLY: name -> (bucket_idx, key_idx)
_S3_POSITIONAL = {
    'upload_file': (1, 2),      # upload_file(Filename, Bucket, Key)
    'download_file': (0, 1),    # download_file(Bucket, Key, Filename)
}


def _split_top_level_args(argtext: str) -> list[str]:
    """Split a call's argument text on top-level commas (quote/bracket aware)."""
    out, buf, depth, quote = [], [], 0, ''
    i = 0
    while i < len(argtext):
        c = argtext[i]
        if quote:
            buf.append(c)
            if c == '\\' and i + 1 < len(argtext):
                buf.append(argtext[i + 1])
                i += 2
                continue
            if c == quote:
                quote = ''
        elif c in '"\'':
            quote = c
            buf.append(c)
        elif c in '([{':
            depth += 1
            buf.append(c)
        elif c in ')]}':
            depth -= 1
            buf.append(c)
        elif c == ',' and depth == 0:
            out.append(''.join(buf).strip())
            buf = []
        else:
            buf.append(c)
        i += 1
    if buf:
        out.append(''.join(buf).strip())
    return [a for a in out if a]


def _op_resource(service: str, method: str, actions: list[str], argtext: str,
                 consts: dict[str, str]) -> tuple[Optional[str], bool, str]:
    """Resolve the ARN a single boto3 call addresses. (arn, exact, raw_expr).

    (None, False, expr) means UNRESOLVABLE -- which the verdict layer prints
    rather than folding into GRANTED. Only S3 is modeled here; every other
    service degrades to UNRESOLVABLE by design, and says so.
    """
    if not argtext:
        return (None, False, '')
    if service in ('s3', 's3_client'):
        if method in _S3_AMBIGUOUS_METHODS:
            return (None, False, f'{method}(...) -- source/dest ambiguous, not modeled')
        b_expr = _kwarg_expr(argtext, 'Bucket')
        k_expr = _kwarg_expr(argtext, 'Key')
        if b_expr is None and method in _S3_POSITIONAL:
            pos = _split_top_level_args(argtext)
            bi, ki = _S3_POSITIONAL[method]
            b_expr = pos[bi] if len(pos) > bi else None
            k_expr = pos[ki] if len(pos) > ki else None
        bucket, _bx = _resolve_py_expr(b_expr, consts)
        key, key_exact = _resolve_py_expr(k_expr, consts)
        bucket_level = bool(actions) and all(
            a.lower() in _S3_BUCKET_LEVEL_ACTIONS for a in actions)
        arn, exact = _s3_arn(bucket, key, key_exact, bucket_level)
        parts = []
        if b_expr:
            parts.append(f'Bucket={b_expr}')
        if k_expr and not bucket_level:
            parts.append(f'Key={k_expr}')
        return (arn, exact, ', '.join(parts))
    return (None, False, f'resource not modeled for boto3 service {service!r}')


V_GRANTED = 'GRANTED'
V_GRANTED_BROAD = 'GRANTED-BROAD'
V_UNGRANTED_RESOURCE = 'GRANTED-ACTION / UNGRANTED-RESOURCE'
V_UNGRANTED = 'UNGRANTED'
V_UNRESOLVABLE = 'UNRESOLVABLE-RESOURCE'

# Verdicts that must never be read as "cleared".
V_NOT_CLEARED = (V_GRANTED_BROAD, V_UNGRANTED_RESOURCE, V_UNGRANTED, V_UNRESOLVABLE)


def _action_pattern_matches(pattern: str, action: str) -> bool:
    """IAM action glob: '*', exact, 's3:*', 's3:Get*', 's3:*Object'."""
    p, a = pattern.lower(), action.lower()
    if pattern == '*' or p == a:
        return True
    if '*' in p:
        return re.fullmatch(re.escape(p).replace(r'\*', '.*'), a) is not None
    return False


def _stmt_action_matches(stmt: "IamStatement", action: str) -> bool:
    return any(_action_pattern_matches(a, action) for a in stmt.actions)


@dataclass
class IamStatement:
    """A single Allow/Deny statement in an IAM policy."""
    effect: str                    # Allow or Deny
    actions: list[str]             # e.g., ['s3:GetObject', 's3:PutObject']
    resources: list[str]           # e.g., ['arn:aws:s3:::opal-data-bd/*']
    source_file: str
    condition: str = ""            # raw Condition block text ("" if none)

    def scoping_condition(self) -> Optional[str]:
        """If this statement's Condition narrows WHICH resources the action can
        act on (TBAC tag / account / org / ARN scoping), return a short summary
        of that scoping; else None.

        This is the NFRA_COMPAWS.IAM-CONDITIONS fix: comp-iam used to surface
        Action + Resource but DROP the Condition, so a tag-scoped (TBAC)
        Resource:"*" grant false-read as broad/unscoped. Anchor FP =
        bd-exporter-ec2-role ec2:TerminateInstances Resource:"*" WITH
        Condition StringEquals{ec2:ResourceTag/ManagedBy=lambda-scheduler}
        (bd-pipeline/iam.tf) -- it can only terminate lambda-scheduler-tagged
        runners, NOT account-wide, so it is NOT broad. Sibling to the existing
        Deny-is-condition-scoped handling in deny_matches()."""
        if not self.condition:
            return None
        # Resource-scoping keys: tag-based (TBAC), account, org boundary.
        m = re.search(
            r'["\']?((?:aws|[a-z0-9]+):(?:ResourceTag/[^"\'\s=:]+|ResourceAccount'
            r'|ResourceOrgID|ResourceOrgPaths))["\']?\s*[=:]\s*["\']([^"\']+)["\']',
            self.condition, re.IGNORECASE)
        if m:
            return f"{m.group(1)}={m.group(2)}"
        # ARN-scoping operators (ArnLike/ArnEquals pinning a resource ARN).
        if re.search(r'\bArn(?:Like|Equals)\b', self.condition, re.IGNORECASE):
            am = re.search(r'["\'](arn:aws:[^"\']+)["\']', self.condition)
            return f"ArnLike {am.group(1)}" if am else "ArnLike (resource-scoped)"
        return None

    def is_resource_scoped_by_condition(self) -> bool:
        """True iff Resource is wildcard ('*') BUT a Condition narrows the
        resources -> the grant is tag/ARN/account-scoped, NOT broad. A genuinely
        broad grant (Resource:'*', no scoping Condition) returns False."""
        if not any(r == '*' for r in self.resources):
            return False
        return self.scoping_condition() is not None


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

    def resource_verdict(self, action: str, arn: Optional[str],
                         exact: bool = True) -> tuple[str, Optional["IamStatement"], str]:
        """Does this role grant `action` ON `arn`? Returns (verdict, stmt, note).

        `grants()` above answers only "is the ACTION held anywhere," which is why
        `s3:GetObject` against a bucket the role has never heard of printed
        [GRANTED]. This answers the question the caller actually asked.

        Verdicts:
          GRANTED                            action AND resource match.
          GRANTED-BROAD                      action matches a Resource:'*' statement.
                                             NOT CLEARED -- no resource check can
                                             falsify a wildcard role. Surfaced, never
                                             silently folded into GRANTED.
          GRANTED-ACTION / UNGRANTED-RESOURCE  the action is held on OTHER resources.
                                             The defect this tool exists to catch.
          UNGRANTED                          no matching action at all.
          UNRESOLVABLE-RESOURCE              could not statically determine coverage.
                                             A tool that cannot state what it could
                                             not check has not checked.

        SOUNDNESS: when `exact` is False the ARN is a PATTERN (a runtime key we
        replaced with '*'). A failed match is then NOT evidence of absence -- the
        real key may land inside a granted prefix. Only BUCKET-LEVEL absence is a
        sound definitive claim there. Getting this backwards would trade the false
        negative for a false positive.
        """
        allows = [s for s in self.statements
                  if s.effect.lower() == 'allow' and _stmt_action_matches(s, action)]
        if not allows:
            return (V_UNGRANTED, None, '')

        for s in allows:
            if any(r == '*' for r in s.resources) and not s.is_resource_scoped_by_condition():
                return (V_GRANTED_BROAD, s,
                        "Resource:'*' -- no resource check can falsify this role")

        if arn is None:
            return (V_UNRESOLVABLE, None, 'call resource not statically resolvable')

        # CVO P1a (2026-07-10). `exact` was a CALLER-SUPPLIED FLAG and the invariant
        # "a '*' in the ARN implies exact is False" was assumed, never asserted. A
        # literal `Key="prefix/*"` resolves exact=True with a '*' in the ARN, and the
        # exact branch below would emit a confident UNGRANTED-RESOURCE against a
        # pattern -- a false accusation that reads as "you are missing a permission,"
        # and someone grants a permission that was never needed. My own defect,
        # inverted into over-permission.
        # DERIVE the property from the evidence; never trust the flag over the string.
        exact = exact and '*' not in arn

        indeterminate = ''
        for s in allows:
            if not s.resources:
                # Parser could not see a Resource (e.g. an unquoted TF reference).
                # Absence of evidence is not evidence of absence.
                indeterminate = indeterminate or 'an Allow statement has no parseable Resource'
                continue
            for r in s.resources:
                hit = _iam_resource_matches(r, arn)
                if hit is True:
                    return (V_GRANTED, s, '')
                if hit is None:
                    indeterminate = indeterminate or \
                        'policy Resource holds an unresolved ${...} interpolation'
        if indeterminate:
            return (V_UNRESOLVABLE, None, indeterminate)

        if exact:
            return (V_UNGRANTED_RESOURCE, None,
                    f'action held on other resources, not on {arn}')

        # Inexact ARN: only bucket-level absence is sound.
        bucket = _arn_bucket(arn)
        if not bucket:
            return (V_UNRESOLVABLE, None, 'non-S3 ARN with unresolved segments')
        # CVO P1 (2026-07-10): the tri-state was applied to the POLICY's uncertainty
        # and not to MY OWN. If the BUCKET segment holds a '*', it is there because
        # THIS parser could not resolve it (`Bucket=f"{env}-data"`), not because the
        # call addresses many buckets. The real bucket may well be one the role holds,
        # so bucket-level absence proves nothing. Returning UNGRANTED-RESOURCE here
        # would read as "you are missing a permission" and someone would add a grant
        # that was never needed -- my own defect class, inverted into over-permission.
        if '*' in bucket:
            return (V_UNRESOLVABLE, None,
                    f'bucket segment {bucket!r} was not statically resolvable -- '
                    f'cannot claim absence')
        held: set[str] = set()
        for s in allows:
            for r in s.resources:
                b = _arn_bucket(r)
                if not b:
                    continue
                if '*' in b:
                    # a wildcard BUCKET segment could cover ours; cannot be definitive
                    return (V_UNRESOLVABLE, None,
                            f'policy bucket pattern {b!r} may cover {bucket!r}')
                held.add(b.lower())
        if bucket.lower() not in held:
            return (V_UNGRANTED_RESOURCE, None,
                    f'bucket {bucket!r} appears in NO Allow statement for {action} '
                    f'(held: {sorted(held) or "none"})')
        return (V_UNRESOLVABLE, None,
                f'bucket {bucket!r} IS held; key not statically resolvable -- cannot confirm')

    def deny_matches(self, action: str) -> list["IamStatement"]:
        """Return Deny statements whose action pattern matches `action`.

        grants() above considers ONLY Allow -- it silently ignored Deny, so an
        explicit Deny (which overrides Allow in AWS eval) read as GRANTED (a
        false-safe; e.g. opal-data-schwab's TLS/SSE Deny bucket-policies). This
        SURFACES matching Deny statements so a false-GRANTED becomes a visible
        'granted-but-Deny-present, verify' rather than a silent pass. We do NOT
        hard-flip to denied here: a Deny is usually resource- and/or
        condition-scoped (e.g. Deny s3:* unless SecureTransport), so treating any
        action-match as an unconditional block would OVER-deny (false gaps). The
        resource/condition-precise effective-allow-after-deny resolution is the
        census-backed reconcile tier (0.7.0 comp-aws live statements w/ resources
        + conditions); here we make the Deny visible, not assumed-either-way."""
        action_lower = action.lower()
        matched: list[IamStatement] = []
        for stmt in self.statements:
            if stmt.effect.lower() != 'deny':
                continue
            for a in stmt.actions:
                a_lower = a.lower()
                if a == '*' or a_lower == action_lower or (
                    '*' in a_lower and re.fullmatch(re.escape(a_lower).replace(r'\*', '.*'), action_lower)
                ):
                    matched.append(stmt)
                    break
        return matched


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

    # Module-level string constants, for resolving `Bucket=PLATINUM_BUCKET`.
    consts = _build_py_const_map(content)

    def _args_at(lineno: int, paren_idx: int) -> str:
        """Argument text of a call whose '(' is at `paren_idx` of line `lineno` (1-based).

        A window of following lines, NOT an absolute offset: `splitlines()` has
        already eaten \\r\\n, so byte offsets into `content` would drift one per
        line on CRLF files and silently mis-slice every multi-line call.
        """
        window = '\n'.join(lines[lineno - 1: lineno - 1 + 12])
        return _balanced_call_args(window, paren_idx)

    # Track (file, service) pairs already flagged UNMODELED so we emit ONE
    # coverage sentinel per unmodeled service per file, not one per call.
    unmodeled_emitted: set = set()

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
                if service not in _MODELED_BOTO3_SERVICES:
                    if (file_path, service) not in unmodeled_emitted:
                        unmodeled_emitted.add((file_path, service))
                        ops.append(Operation(
                            iam_actions=[f'{service}:UNMODELED'],
                            source_pattern=f'{client_var}.{method} (boto3 service {service!r} not modeled by comp-iam)',
                            file_path=file_path,
                            line_number=lineno,
                        ))
                    continue
                action_map = _BOTO3_BY_SERVICE.get(service, {})

                if method in action_map:
                    actions = action_map[method]
                    if actions:
                        _arn, _exact, _expr = _op_resource(
                            service, method, actions, _args_at(lineno, m.end() - 1), consts)
                        ops.append(Operation(
                            iam_actions=actions,
                            source_pattern=f'{client_var}.{method}',
                            file_path=file_path,
                            line_number=lineno,
                            resource_arn=_arn,
                            resource_exact=_exact,
                            resource_expr=_expr,
                        ))

        # Generic boto3 method calls even without tracked client var
        # e.g.: boto3.client('s3').delete_object(...)
        for m in re.finditer(r"boto3\.client\s*\(\s*['\"](\w+)['\"]\s*\)\.(\w+)\s*\(", line):
            service = m.group(1)
            method = m.group(2)
            if service not in _MODELED_BOTO3_SERVICES:
                if (file_path, service) not in unmodeled_emitted:
                    unmodeled_emitted.add((file_path, service))
                    ops.append(Operation(
                        iam_actions=[f'{service}:UNMODELED'],
                        source_pattern=f"boto3.client('{service}').{method} (service not modeled by comp-iam)",
                        file_path=file_path,
                        line_number=lineno,
                    ))
                continue
            action_map = _BOTO3_BY_SERVICE.get(service, {})
            if method in action_map and action_map[method]:
                _arn, _exact, _expr = _op_resource(
                    service, method, action_map[method], _args_at(lineno, m.end() - 1), consts)
                ops.append(Operation(
                    iam_actions=action_map[method],
                    source_pattern=f"boto3.client('{service}').{method}",
                    file_path=file_path,
                    line_number=lineno,
                    resource_arn=_arn,
                    resource_exact=_exact,
                    resource_expr=_expr,
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
# NFRA_COMPIAM_ROLEREF (0.8.0, 2026-07-10): an `aws_iam_role_policy` may attach to a
# role by LITERAL NAME rather than by TF reference -- the cross-module attachment
# pattern (`role = "lambda-execution-role"` in portfolio-management/, where the role
# resource lives in shared-infra/). `_TF_ROLE_REF` matches only the reference form, so
# the caller hit a bare `continue` and DROPPED the whole policy block, silently: no
# counter, no stderr, no verdict. 21 of 330 blocks estate-wide, across 4 roles.
#
# That is what actually produced comp-iam's `GRANTED-ACTION / UNGRANTED-RESOURCE` on
# opal-pm-optimization-loader's s3:DeleteObject: `OpalDataPMCacheBustAccess`
# (portfolio-management/main.tf:323, Sid PMProcessedCacheDelete,
# arn:aws:s3:::opal-data-pm/*/processed/*) IS Terraform-declared and IS inside the
# scanned tree. The file was read. The statement was discarded.
#
# It is NOT a DESIRED-vs-APPLIED plane limitation. Attributing it to one would have
# taught every reader to dismiss this class as a console-drift artifact. (CTO,
# 2026-07-10: "a true explanation, applied to a symptom it did not produce.")
# Role names are globally unique in AWS, so the literal form resolves GLOBALLY by
# name; the reference form stays module-local (the collision guard depends on it).
_TF_ROLE_LITERAL = re.compile(r'role\s*=\s*"([^"$]+)"')
_TF_POLICY_NAME = re.compile(r'name\s*=\s*"([^"]+)"')

# `_TF_POLICY_RESOURCE` matches BOTH `aws_iam_role_policy` (inline, carries `role =`)
# and `aws_iam_policy` (standalone, attached later via aws_iam_role_policy_attachment
# and therefore carrying NO `role =` by design). Counting a standalone policy as
# "NOT ATTACHED -- unresolvable role ref" lumps two different worlds into one number
# and prints a reason that is FALSE for it. 5 of 330 estate-wide. Same class as
# ROLL_SOURCE_ABSENT vs ROLL_SOURCE_UNREADABLE: a bare count collapsing worlds.
_TF_STANDALONE_POLICY = re.compile(r'resource\s+"aws_iam_policy"\s+"(\w+)"\s*\{')

_HCL_LINE_COMMENT = re.compile(r'^(\s*)(#|//).*$', re.M)


def _mask_hcl_comments(content: str) -> str:
    """Blank out whole-line HCL comments, PRESERVING LENGTH so offsets stay valid.

    `_TF_POLICY_RESOURCE` happily matches a commented-out
    `# resource "aws_iam_role_policy" "ghost" {`, which would inflate the block
    census with a policy that does not exist. Latent estate-wide today (0 hits), and
    invisible because the census re-derives its total with the SAME regex -- a test
    inherits every blindness of the instrument it imports (CVO, 2026-07-10).
    Offsets are preserved so `_extract_tf_block(content, m.start())` still reads the
    ORIGINAL text.
    """
    return _HCL_LINE_COMMENT.sub(lambda m: m.group(1) + ' ' * (len(m.group(0)) - len(m.group(1))),
                                 content)

# Attachment census. comp-iam must be able to STATE what it read and what it could
# not attach -- the same rule it now enforces on resources. Populated by
# _parse_terraform_iam(); read by the CLI banner.
_ATTACH_STATS: dict = {
    'attached': 0, 'dropped': 0, 'dropped_detail': [], 'tf_files': 0,
    # standalone aws_iam_policy blocks: no `role =` by design, attached via
    # aws_iam_role_policy_attachment. NOT a drop; a different world.
    'standalone': 0,
    # Deny statements inside blocks we could not attach. CTO arch-gate 2026-07-10:
    # printed on EVERY invocation until zero.
    'deny_unparsed': 0, 'deny_reasons': set(), 'deny_detail': [],
}


def _drop_reason(block: str, role_name: Optional[str], roles: dict) -> str:
    """Why a policy block could not be attached. Named, never lumped together."""
    m = re.search(r'role\s*=\s*(.+)', block)
    expr = (m.group(1).strip() if m else '').split('\n')[0]
    if 'each.value' in expr or 'each.key' in expr:
        return 'for_each -- `role = each.value` not resolved'
    if '${' in expr:
        return 'role name is an unresolved interpolation'
    if role_name and role_name not in roles:
        return f'literal role {role_name!r} has no aws_iam_role resource in the scanned trees'
    if expr.startswith('aws_iam_role.'):
        return 'TF reference does not resolve within its own module'
    if 'var.' in expr or 'module.' in expr or 'local.' in expr:
        return 'role name comes from a var/module/local'
    return 'role reference form not recognised'

# The Terraform trees comp-iam reads. Anything outside them is INVISIBLE to every
# comp-iam verdict. Printed on every sweep so "it did not read your tree" is never
# mistaken for "your role does not hold it".
TF_SCAN_ROOTS = [
    "infra/aws/terraform",
    "infra/aws/multi-account/terraform",
    "infra/aws/ec2",
]
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


# ${var.X} resolution for resource names (e.g. name = "${var.name}-role"). TF variables are
# module-scoped, so resolution is same-module-dir ONLY -- a generic var name like "name" can be
# defined differently in two modules, so resolving cross-module would mis-key roles.
_TF_VARIABLE = re.compile(r'variable\s+"(\w+)"\s*\{')
_TF_VAR_DEFAULT = re.compile(r'default\s*=\s*"([^"]*)"')
_TF_VAR_INTERP = re.compile(r'\$\{var\.(\w+)\}')


def _collect_module_var_defaults(module_dir: Path) -> dict[str, str]:
    """Collect `variable "X" { default = "Y" }` string-defaults from every .tf in ONE module
    directory, for resolving ${var.X} in resource names. Same-module scope only."""
    out: dict[str, str] = {}
    try:
        tf_files = sorted(module_dir.glob("*.tf"))
    except Exception:
        return out
    for f in tf_files:
        try:
            content = f.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        for m in _TF_VARIABLE.finditer(content):
            block = _extract_tf_block(content, m.start())
            dm = _TF_VAR_DEFAULT.search(block)
            if dm:
                out[m.group(1)] = dm.group(1)
    return out


def _resolve_tf_vars(value: str, var_defaults: dict[str, str]) -> str:
    """Substitute ${var.X} with its module default; leave any unresolved ref literal."""
    return _TF_VAR_INTERP.sub(lambda m: var_defaults.get(m.group(1), m.group(0)), value)


def _collect_module_locals(module_dir: Path) -> dict[str, str]:
    """Collect `locals { name = "literal" }` string values from every .tf in ONE module dir.

    Policy Resources are written as `arn:aws:s3:::${local.inf_bucket}/gold/...`.
    Without resolving locals, EVERY S3 resource ARN is an unresolved interpolation
    and every resource verdict correctly-but-uselessly degrades to
    UNRESOLVABLE-RESOURCE. Same-module scope only (TF locals are module-local).
    Plain string literals only -- an interpolated local (`"${var.env}-bucket"`)
    stays unresolved on purpose rather than being half-guessed.
    """
    out: dict[str, str] = {}
    try:
        tf_files = sorted(module_dir.glob("*.tf"))
    except Exception:
        return out
    for f in tf_files:
        try:
            content = f.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        for bm in _TF_LOCALS_BLOCK.finditer(content):
            block = _extract_tf_block(content, bm.start())
            for m in _TF_LOCAL_ASSIGN.finditer(block):
                out.setdefault(m.group(1), m.group(2))
    return out


def _resolve_tf_locals(value: str, locals_map: dict[str, str]) -> str:
    """Substitute ${local.X}; leave any unresolved ref literal (so it reads as indeterminate)."""
    return _TF_LOCAL_INTERP.sub(lambda m: locals_map.get(m.group(1), m.group(0)), value)


def _resolve_stmt_resources(stmts: list["IamStatement"], module_dir: Path,
                            locals_cache: dict, var_cache: dict) -> list["IamStatement"]:
    """Resolve ${local.X} / ${var.X} inside every statement's Resource list, in place."""
    if module_dir not in locals_cache:
        locals_cache[module_dir] = _collect_module_locals(module_dir)
    if module_dir not in var_cache:
        var_cache[module_dir] = _collect_module_var_defaults(module_dir)
    lm, vm = locals_cache[module_dir], var_cache[module_dir]
    for s in stmts:
        s.resources = [_resolve_tf_vars(_resolve_tf_locals(r, lm), vm) for r in s.resources]
    return stmts


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

    def _field_object(name: str, text: str) -> str:
        """Extract the brace-balanced { ... } block for object field `name`
        (e.g. Condition) from HCL or JSON. Returns '' if absent. Used to carry
        the IAM Condition through so a tag-scoped Resource:* is not false-read
        as broad (NFRA_COMPAWS.IAM-CONDITIONS)."""
        m = re.search(rf'["\']?{name}["\']?\s*[=:]\s*\{{', text, re.IGNORECASE)
        if not m:
            return ""
        start = m.end() - 1  # position of the opening {
        depth = 0
        for i in range(start, len(text)):
            ch = text[i]
            if ch == '{':
                depth += 1
            elif ch == '}':
                depth -= 1
                if depth == 0:
                    return ' '.join(text[start:i + 1].split())
        return ""

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
                    condition = _field_object('Condition', single_stmt)

                    if actions:
                        statements.append(IamStatement(
                            effect=effect,
                            actions=actions,
                            resources=resources,
                            source_file=source_file,
                            condition=condition,
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

    # Scan ALL terraform roots, not just infra/aws/terraform. multi-account/terraform and the
    # per-service ec2/*/terraform roots declare real IAM roles too; globbing only the primary
    # root left them with NO gap-check at all -- a silent coverage hole on this Rule-20 deploy
    # gate (0.5.0_AE surfaced it during the collision fix; CTO routed it to the comp-tools
    # campaign 2026-06-26). The module-keyed role_tf_to_name + loud collision guard (below)
    # make multi-root scanning safe -- a bare label reused across roots no longer mis-links.
    _ATTACH_STATS.update({'attached': 0, 'dropped': 0, 'dropped_detail': [], 'tf_files': 0,
                          'standalone': 0,
                          'deny_unparsed': 0, 'deny_reasons': set(), 'deny_detail': []})
    tf_roots = [workspace_root / p for p in TF_SCAN_ROOTS]
    all_tf_files: list[Path] = []
    seen_tf: set[Path] = set()
    for root in tf_roots:
        if not root.exists():
            continue
        for f in root.rglob("*.tf"):
            # skip .terraform/ vendored module + provider caches (would double-count copies)
            if ".terraform" in f.parts:
                continue
            rf = f.resolve()
            if rf not in seen_tf:
                seen_tf.add(rf)
                all_tf_files.append(f)
    _ATTACH_STATS['tf_files'] = len(all_tf_files)
    if not all_tf_files:
        return roles
    all_tf_files.sort()

    # First pass: collect all role definitions
    # NAMESPACED by module dir: a Terraform resource label (`aws_iam_role "orchestrator"`) is
    # module-LOCAL, so the same bare label reused across two roots is two DIFFERENT roles. Keying
    # this map by the bare label (pre-2026-06-26) collided them last-writer-wins, so the loser
    # role's inline policy linked to the winner -> the loser was credited 0 statements -> every
    # action FALSE-MISSING in this Rule-20 deploy-gate tool (incident: astn-wsjft-orchestrator-role
    # vs etfs-reports-orchestrator-role, both `aws_iam_role "orchestrator"`; root-caused 0.5.0_AE
    # 2026-06-26, brief docs/briefs/comp-iam-false-missing-tf-resource-collision-20260626.md).
    role_tf_to_name: dict[tuple[str, str], str] = {}  # (module_dir, tf_resource) -> role_name
    _label_to_roles: dict[str, set[str]] = {}  # bare tf_resource label -> {role_names} (collision detector)
    module_var_cache: dict[Path, dict[str, str]] = {}  # module dir -> {var: default} (lazy)
    module_locals_cache: dict[Path, dict[str, str]] = {}  # module dir -> {local: literal} (lazy)
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
                # Resolve ${var.X} against the module's variable defaults so e.g.
                # name = "${var.name}-role" keys as "m365-mcp-gateway-role" (and links to its
                # inline policies + the EC2_MANIFEST service iam_role), not the literal string.
                if "${var." in role_name:
                    mod_dir = tf_file.parent
                    if mod_dir not in module_var_cache:
                        module_var_cache[mod_dir] = _collect_module_var_defaults(mod_dir)
                    role_name = _resolve_tf_vars(role_name, module_var_cache[mod_dir])
                # A still-unresolved ${var.X} = a REUSABLE module template (e.g.
                # multi-account/terraform/modules/lambda) with no concrete default -- it is
                # instantiated elsewhere under a concrete name (which we DO scan). Listing the
                # templated pseudo-name is unqueryable noise; skip it, but LOUDLY (no silent drop).
                if "${var." in role_name:
                    print(f"comp-iam: NOTE -- skipping reusable module-template role "
                          f"'{role_name}' in {rel} (unresolved var; instantiated concretely "
                          f"elsewhere).", file=sys.stderr)
                    continue
                role_tf_to_name[(str(tf_file.parent), tf_res)] = role_name
                _label_to_roles.setdefault(tf_res, set()).add(role_name)
                if role_name not in roles:
                    roles[role_name] = IamRole(
                        role_name=role_name,
                        tf_resource=tf_res,
                        source_file=rel,
                    )

    # Collision guard (LOUD): a bare TF role label reused across modules used to silently
    # mis-link policies (see the namespacing note above). With module-keyed role_tf_to_name the
    # link is now correct, but surface the reuse to stderr so a future collision is never silent.
    for _label, _rnames in sorted(_label_to_roles.items()):
        if len(_rnames) > 1:
            print(f"comp-iam: NOTE -- TF role label '{_label}' is reused across modules by "
                  f"{sorted(_rnames)}; now module-namespaced (pre-fix this silently mis-linked "
                  f"their inline policies -> FALSE-MISSING).", file=sys.stderr)

    # Second pass: parse inline policies and attach to roles
    for tf_file in all_tf_files:
        try:
            content = tf_file.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        rel = str(tf_file.relative_to(workspace_root)).replace("\\", "/")

        # aws_iam_role_policy (inline policy on a role).
        # Scan the COMMENT-MASKED text so a commented-out block is never counted;
        # extract from the ORIGINAL (mask preserves offsets).
        scan = _mask_hcl_comments(content)
        for m in _TF_POLICY_RESOURCE.finditer(scan):
            block = _extract_tf_block(content, m.start())
            role_ref = _TF_ROLE_REF.search(block)
            if role_ref:
                tf_role = role_ref.group(1)
                # Resolve the role ref WITHIN the same module (TF refs are module-local).
                role_name = role_tf_to_name.get((str(tf_file.parent), tf_role))
            else:
                # NFRA_COMPIAM_ROLEREF: `role = "literal-name"` -- the cross-module
                # attachment. Role names are globally unique in AWS, so resolve by name.
                lit = _TF_ROLE_LITERAL.search(block)
                role_name = lit.group(1) if lit else None
            if not role_name or role_name not in roles:
                # A STANDALONE aws_iam_policy has no `role =` BY DESIGN -- it is
                # attached below via aws_iam_role_policy_attachment. Calling it an
                # unattachable role-policy is a false reason on a real count.
                if _TF_STANDALONE_POLICY.match(content[m.start():m.end() + 1]) or \
                        _TF_STANDALONE_POLICY.search(block[:120]):
                    _ATTACH_STATS['standalone'] += 1
                    continue
                # NEVER a silent drop. A tool that cannot state what it failed to
                # attach cannot be trusted to have attached yours.
                _ATTACH_STATS['dropped'] += 1
                pol = _TF_POLICY_NAME.search(block)
                why = _drop_reason(block, role_name, roles)
                _ATTACH_STATS['dropped_detail'].append(
                    f"{pol.group(1) if pol else '(unnamed)'} -> "
                    f"{role_name or '(unresolvable role ref)'} [{rel}]  ({why})")
                # CTO arch-gate 2026-07-10: a tool that cannot see a Deny must SAY SO.
                # We could not ATTACH this block, but we can still PARSE it and learn
                # whether it carried a Deny. NEVER#1's cross-firm belts are Deny
                # statements attached via `role = each.value`; comp-iam's Deny overlay
                # exists so an explicit Deny never reads as GRANTED, and it cannot warn
                # on a Deny it never parsed. Silence reads as allowed.
                for _s in _parse_iam_statements(block, rel):
                    if _s.effect.lower() == 'deny':
                        _ATTACH_STATS['deny_unparsed'] += 1
                        _ATTACH_STATS['deny_reasons'].add(why)
                        _ATTACH_STATS['deny_detail'].append(
                            f"{pol.group(1) if pol else '(unnamed)'} "
                            f"[{rel}] ({why})")
                continue

            # Parse the policy JSON (embedded in jsonencode or heredoc)
            stmts = _parse_iam_statements(block, rel)
            _resolve_stmt_resources(stmts, tf_file.parent, module_locals_cache, module_var_cache)
            roles[role_name].statements.extend(stmts)
            _ATTACH_STATS['attached'] += 1

        # aws_iam_policy (standalone policy document)
        for m in re.finditer(r'resource\s+"aws_iam_policy"\s+"(\w+)"\s*\{', content):
            block = _extract_tf_block(content, m.start())
            stmts = _parse_iam_statements(block, rel)
            _resolve_stmt_resources(stmts, tf_file.parent, module_locals_cache, module_var_cache)
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
                    role_name = role_tf_to_name.get((str(tf_file.parent), tf_role))
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
            role_name = role_tf_to_name.get((str(tf_file.parent), tf_role))
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

        content = _read_source_if_allowed(abs_path, workspace_root)  # sec.8 chokepoint (defense-in-depth)
        if content is None:
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
            content = _read_source_if_allowed(py_file, workspace_root)  # sec.8 chokepoint
            if content is None:
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
                content = _read_source_if_allowed(py_file, workspace_root)  # sec.8 chokepoint
                if content is None:
                    continue
                rel = str(py_file.relative_to(workspace_root)).replace("\\", "/")
                ops.extend(_scan_python_for_operations(content, rel))
                files_scanned.append(rel)
        elif abs_path.is_file() and abs_path.suffix == ".py":
            content = _read_source_if_allowed(abs_path, workspace_root)  # sec.8 chokepoint
            if content is None:
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
                # UNMODELED sentinel: the source uses a boto3 service comp-iam
                # doesn't model -> coverage-unknown, NOT a real perm gap and NOT
                # clean. Surface distinctly so "no gaps" isn't falsely confident.
                if action.endswith(':UNMODELED'):
                    gaps.append(PermissionGap(
                        service=profile.name, iam_role=profile.iam_role,
                        iam_action=action, source_pattern=op.source_pattern,
                        file_path=op.file_path, line_number=op.line_number,
                        severity="UNMODELED",
                    ))
                    continue
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
                else:
                    # Granted via Allow -- but does a Deny also match? grants()
                    # used to ignore Deny entirely (false-safe). Surface it.
                    denies = role.deny_matches(action)
                    if denies:
                        deny_res = sorted({r for s in denies for r in (s.resources or ['*'])})
                        gaps.append(PermissionGap(
                            service=profile.name, iam_role=profile.iam_role,
                            iam_action=action,
                            source_pattern=f"{op.source_pattern} -- ALLOW granted BUT Deny present on {deny_res}",
                            file_path=op.file_path, line_number=op.line_number,
                            severity="DENY-PRESENT",
                        ))

    return all_profiles, roles, gaps
