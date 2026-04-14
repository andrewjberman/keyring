"""
Pass 4: EventBridge Trigger Mapper -- extract TRIGGERS edges.

Scans infra/aws/terraform/*/eventbridge.tf for:
  - aws_cloudwatch_event_rule resources (schedule rules)
  - aws_cloudwatch_event_target resources (rule -> Lambda mapping)

Resolves Lambda target ARNs/names to match existing LAMBDA nodes in the graph.
Handles both direct function references and module output references.

Also scans lambdas.tf in each pipeline to resolve module names to function names
(e.g., module.gold_trigger.function_arn -> bd-gold-trigger).

Zero API calls. Pure regex/HCL extraction.
"""

from __future__ import annotations

import re
from pathlib import Path

from .trace_graph import TraceGraph, Node, Edge

# ---------------------------------------------------------------------------
# Terraform HCL patterns
# ---------------------------------------------------------------------------

# resource "aws_cloudwatch_event_rule" "bd_allocation_pipeline" {
_EVENT_RULE = re.compile(
    r'resource\s+"aws_cloudwatch_event_rule"\s+"(\w+)"\s*\{',
)

# name = "bd-allocation-pipeline-trigger"
_RULE_NAME = re.compile(r'name\s*=\s*"([^"]+)"')

# schedule_expression = "cron(...)" or "rate(...)"
_SCHEDULE = re.compile(r'schedule_expression\s*=\s*"([^"]+)"')

# state = "ENABLED" or "DISABLED"
_STATE = re.compile(r'state\s*=\s*"(ENABLED|DISABLED)"')

# description = "..."
_DESCRIPTION = re.compile(r'description\s*=\s*"([^"]*)"')

# resource "aws_cloudwatch_event_target" "bd_allocation_pipeline_target" {
_EVENT_TARGET = re.compile(
    r'resource\s+"aws_cloudwatch_event_target"\s+"(\w+)"\s*\{',
)

# rule = aws_cloudwatch_event_rule.bd_allocation_pipeline.name
_TARGET_RULE_REF = re.compile(
    r'rule\s*=\s*aws_cloudwatch_event_rule\.(\w+)\.name'
)

# arn = module.gold_trigger.function_arn
_TARGET_ARN_MODULE = re.compile(
    r'arn\s*=\s*module\.(\w+)\.function_arn'
)

# arn = aws_lambda_function.ingestion_scheduler.arn
_TARGET_ARN_RESOURCE = re.compile(
    r'arn\s*=\s*aws_lambda_function\.(\w+)\.arn'
)

# arn = "arn:aws:lambda:...:function:opal-portal-fear-greed-fetcher"
_TARGET_ARN_LITERAL = re.compile(
    r'arn\s*=\s*"[^"]*:function:([^"]+)"'
)

# arn with interpolation: "arn:aws:lambda:${local.region}:${local.account_id}:function:name"
_TARGET_ARN_INTERPOLATED = re.compile(
    r'arn\s*=\s*"arn:aws:lambda:\$\{[^}]+\}:\$\{[^}]+\}:function:([^"]+)"'
)

# module "gold_trigger" { ... function_name = "bd-gold-trigger" ... }
_MODULE_BLOCK = re.compile(
    r'module\s+"(\w+)"\s*\{',
)

_FUNCTION_NAME = re.compile(
    r'function_name\s*=\s*"([^"]+)"'
)

# aws_lambda_function "ingestion_scheduler" { ... function_name = "news-ingestion-scheduler" }
_LAMBDA_RESOURCE = re.compile(
    r'resource\s+"aws_lambda_function"\s+"(\w+)"\s*\{',
)


def _extract_block(content: str, start: int) -> str:
    """Extract the {} block starting at position start (after the opening {)."""
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


def _build_module_map(tf_dir: Path) -> dict[str, str]:
    """Build map: module_name -> function_name from lambdas.tf files."""
    module_map = {}
    for tf_file in tf_dir.glob("*.tf"):
        try:
            content = tf_file.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue

        for m in _MODULE_BLOCK.finditer(content):
            module_name = m.group(1)
            block = _extract_block(content, m.start())
            fn_match = _FUNCTION_NAME.search(block)
            if fn_match:
                module_map[module_name] = fn_match.group(1)

    return module_map


def _build_resource_map(tf_dir: Path) -> dict[str, str]:
    """Build map: resource_name -> function_name from aws_lambda_function resources."""
    resource_map = {}
    for tf_file in tf_dir.glob("*.tf"):
        try:
            content = tf_file.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue

        for m in _LAMBDA_RESOURCE.finditer(content):
            resource_name = m.group(1)
            block = _extract_block(content, m.start())
            fn_match = _FUNCTION_NAME.search(block)
            if fn_match:
                fn_name = fn_match.group(1)
                # Skip self-references like function_name = module.xxx.function_name
                if not fn_name.startswith("module."):
                    resource_map[resource_name] = fn_name

    return resource_map


def extract_eventbridge_edges(graph: TraceGraph, workspace_root: Path):
    """Extract EventBridge rule -> Lambda trigger edges from Terraform files."""

    tf_base = workspace_root / "infra" / "aws" / "terraform"
    if not tf_base.exists():
        return

    for pipeline_dir in sorted(tf_base.iterdir()):
        if not pipeline_dir.is_dir():
            continue

        eb_file = pipeline_dir / "eventbridge.tf"
        if not eb_file.exists():
            continue

        try:
            content = eb_file.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue

        rel_path = str(eb_file.relative_to(workspace_root)).replace("\\", "/")
        pipeline_name = pipeline_dir.name

        # Build resolution maps for this pipeline
        module_map = _build_module_map(pipeline_dir)
        resource_map = _build_resource_map(pipeline_dir)

        # --- Extract rules ---
        rules: dict[str, dict] = {}  # tf_resource_name -> {name, schedule, state, ...}

        for m in _EVENT_RULE.finditer(content):
            tf_name = m.group(1)
            block = _extract_block(content, m.start())

            rule_name_match = _RULE_NAME.search(block)
            schedule_match = _SCHEDULE.search(block)
            state_match = _STATE.search(block)
            desc_match = _DESCRIPTION.search(block)

            rule_name = rule_name_match.group(1) if rule_name_match else tf_name
            schedule = schedule_match.group(1) if schedule_match else ""
            state = state_match.group(1) if state_match else "ENABLED"
            description = desc_match.group(1) if desc_match else ""

            rules[tf_name] = {
                "name": rule_name,
                "schedule": schedule,
                "state": state,
                "description": description,
            }

            # Create EVENTBRIDGE node
            node_id = f"eventbridge:{rule_name}"
            graph.add_node(Node(
                id=node_id,
                node_type="EVENTBRIDGE",
                label=rule_name,
                file_path=rel_path,
                metadata={
                    "schedule": schedule,
                    "state": state,
                    "pipeline": pipeline_name,
                    "description": description,
                },
            ))

        # --- Extract targets and link to rules ---
        for m in _EVENT_TARGET.finditer(content):
            block = _extract_block(content, m.start())

            # Which rule does this target belong to?
            rule_ref_match = _TARGET_RULE_REF.search(block)
            if not rule_ref_match:
                continue

            rule_tf_name = rule_ref_match.group(1)
            if rule_tf_name not in rules:
                continue

            rule_info = rules[rule_tf_name]
            rule_node_id = f"eventbridge:{rule_info['name']}"

            # Resolve target Lambda name
            lambda_name = None

            # Try module reference: module.gold_trigger.function_arn
            mod_match = _TARGET_ARN_MODULE.search(block)
            if mod_match:
                mod_name = mod_match.group(1)
                lambda_name = module_map.get(mod_name)

            # Try resource reference: aws_lambda_function.ingestion_scheduler.arn
            if not lambda_name:
                res_match = _TARGET_ARN_RESOURCE.search(block)
                if res_match:
                    res_name = res_match.group(1)
                    lambda_name = resource_map.get(res_name)

            # Try interpolated ARN literal
            if not lambda_name:
                interp_match = _TARGET_ARN_INTERPOLATED.search(block)
                if interp_match:
                    lambda_name = interp_match.group(1)

            # Try plain ARN literal
            if not lambda_name:
                lit_match = _TARGET_ARN_LITERAL.search(block)
                if lit_match:
                    lambda_name = lit_match.group(1)

            if not lambda_name:
                continue

            # Create or reference LAMBDA node
            lambda_node_id = f"lambda:{lambda_name}"
            if lambda_node_id not in graph.nodes:
                graph.add_node(Node(
                    id=lambda_node_id,
                    node_type="LAMBDA",
                    label=lambda_name,
                    metadata={"pipeline": pipeline_name},
                ))

            # Create TRIGGERS edge
            graph.add_edge(Edge(
                source=rule_node_id,
                target=lambda_node_id,
                edge_type="TRIGGERS",
                metadata={
                    "schedule": rule_info["schedule"],
                    "state": rule_info["state"],
                },
            ))


# ---------------------------------------------------------------------------
# Lambda -> EC2 SSM invocation edges
# ---------------------------------------------------------------------------

# SSM send_command patterns in Lambda source
_SSM_SEND_CMD = re.compile(
    r'send_command\s*\(',
    re.IGNORECASE,
)

# InstanceIds: ['i-...'] or os.environ.get('INSTANCE_ID')
_INSTANCE_IDS_LITERAL = re.compile(
    r'InstanceIds\s*=\s*\[\s*[\'"]([^\'"]+)[\'"]\s*\]'
)

_INSTANCE_IDS_ENVVAR = re.compile(
    r'InstanceIds\s*=\s*\[?\s*(?:os\.environ(?:\.get)?\s*\(\s*[\'"](\w+)[\'"]|'
    r'environ\.get\s*\(\s*[\'"](\w+)[\'"])',
    re.IGNORECASE,
)

# Target EC2 instance tag filter: Targets=[{'Key': 'tag:Name', 'Values': ['bd-gold-runner']}]
_SSM_TARGET_TAG = re.compile(
    r"Targets\s*=\s*\[.*?'Values'\s*:\s*\[\s*['\"]([^'\"]+)['\"]",
    re.DOTALL,
)


def extract_lambda_ec2_edges(graph: TraceGraph, workspace_root: Path):
    """Detect Lambda -> EC2 edges via SSM send_command calls in Lambda source.

    Scans each Lambda source file (via lambda-source-map.json) for
    ssm.send_command / ssm_client.send_command calls. Creates INVOKES_EC2
    edges in the graph: lambda:{name} -> ec2:{instance_id_or_name}.
    """
    source_map_file = (
        workspace_root / "infra" / "aws" / "lambda" / "ci" / "lambda-source-map.json"
    )
    if not source_map_file.exists():
        return

    try:
        import json as _json
        source_map = _json.loads(source_map_file.read_text(encoding="utf-8"))
    except Exception:
        return

    for fn_name, entry in source_map.items():
        # Source map entries can be dicts with 'source' key or plain strings
        if isinstance(entry, dict):
            source_path = entry.get("source") or entry.get("path") or ""
        else:
            source_path = str(entry)

        if not source_path:
            continue

        abs_path = workspace_root / source_path
        # Accept both directory (look for lambda_function.py) and direct file path
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

        if not _SSM_SEND_CMD.search(content):
            continue

        # Found SSM send_command -- extract instance targets
        lambda_node_id = f"lambda:{fn_name}"
        if lambda_node_id not in graph.nodes:
            graph.add_node(Node(
                id=lambda_node_id,
                node_type="LAMBDA",
                label=fn_name,
                metadata={"source": str(abs_path.relative_to(workspace_root))},
            ))

        targets: list[str] = []

        # Literal instance ID
        for m in _INSTANCE_IDS_LITERAL.finditer(content):
            targets.append(f"i-{m.group(1)}" if not m.group(1).startswith('i-') else m.group(1))

        # Env var reference
        for m in _INSTANCE_IDS_ENVVAR.finditer(content):
            env_var = m.group(1) or m.group(2) or ""
            if env_var:
                targets.append(f"${{{env_var}}}")

        # SSM tag target
        for m in _SSM_TARGET_TAG.finditer(content):
            targets.append(f"tag:{m.group(1)}")

        # If we found send_command but no target patterns, add a generic edge
        if not targets:
            targets.append("ec2-runner (target via SSM)")

        for target in targets:
            ec2_node_id = f"ec2:{target}"
            if ec2_node_id not in graph.nodes:
                graph.add_node(Node(
                    id=ec2_node_id,
                    node_type="EC2_SERVICE",
                    label=target,
                    metadata={"detection": "ssm_send_command"},
                ))

            edge_exists = any(
                e.source == lambda_node_id and e.target == ec2_node_id
                and e.edge_type == "INVOKES_EC2"
                for e in graph.edges
            )
            if not edge_exists:
                graph.add_edge(Edge(
                    source=lambda_node_id,
                    target=ec2_node_id,
                    edge_type="INVOKES_EC2",
                    metadata={
                        "mechanism": "SSM send_command",
                        "source_file": str(abs_path.relative_to(workspace_root)),
                    },
                ))
