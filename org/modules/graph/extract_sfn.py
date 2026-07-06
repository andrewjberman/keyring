"""
Pass 7: Step Functions INVOKE-edge bridge (NFRA_GRAPHUNI.SFNBRIDGE, 2026-07-06).

Projects SFN State Machine -> Lambda INVOKE edges into the trace graph so comp-blast/comp-iam surface a
Lambda's SFN-orchestrated dependents -- blast-radius COMPLETENESS. Before this pass, comp-blast on an
SFN-orchestrated Lambda missed its orchestrator entirely (trace_graph modelled no Step Functions), a
false-negative blast radius on a Rule-20 "what breaks if I change X" gate.

BOUNDED to invoke/dependency edges ONLY -- the deep SFN state model (branches, retries, choice logic)
stays in comp-aws, the SFN-authoritative tool (StepFunctions class F1=1.0, CVO-certified 2026-06-08).
trace_graph gets the invoke-edge PROJECTION, not a second SFN model.

REUSES the CERTIFIED comp_aws_cli._sfn_task_invokes walker -- NO re-implementation. comp_aws_cli imports
boto3 lazily (only inside _boto()), so importing it for that pure-Python walker adds no AWS dependency to
the graph build. Static: reads the ASL definition co-located with each aws_sfn_state_machine
(`definition = file("${path.module}/*.json")`), zero API calls -- same discipline as the other passes.

Dual-direction edges (mirrors trace_graph's CALLS/CALLED_BY convention so blast resolves from EITHER end):
  STATE_MACHINE -[SFN_INVOKES]->   LAMBDA          -- invocation direction; blast(SM) shows its Lambdas
  LAMBDA        -[SFN_INVOKED_BY]-> STATE_MACHINE   -- blast-radius direction; blast(Lambda) surfaces the SM
Deduped to UNIQUE (SM, Lambda) pairs: two Task states invoking one Lambda = ONE dependency edge, matching
the certified 26-invoke oracle (yang-generate-allocation-summary is invoked by 2 states = 1 edge; the ASL
has 27 Task-state invokes / 26 unique Lambda targets).
"""

from __future__ import annotations

import re
from pathlib import Path

from .trace_graph import Edge, Node, TraceGraph

# resource "aws_sfn_state_machine" "yang_pipeline" {
_SFN_RESOURCE = re.compile(r'resource\s+"aws_sfn_state_machine"\s+"(\w+)"\s*\{')
_SFN_NAME = re.compile(r'name\s*=\s*"([^"]+)"')
# definition = file("${path.module}/yang-pipeline-definition.json")
_DEF_FILE = re.compile(r'definition\s*=\s*file\(\s*"([^"]+)"\s*\)')
# definition = jsonencode({ ... })  -- inline form (best-effort; not present in the estate today)
_DEF_JSONENCODE = re.compile(r'definition\s*=\s*jsonencode\(')


def _extract_block(content: str, start: int) -> str:
    """Balanced {}-block starting at/after `start` (mirror of extract_eventbridge._extract_block)."""
    brace = content.find("{", start)
    if brace == -1:
        return ""
    depth, i = 1, brace + 1
    while i < len(content) and depth > 0:
        if content[i] == "{":
            depth += 1
        elif content[i] == "}":
            depth -= 1
        i += 1
    return content[brace:i]


def _lambda_name_from_arn(arn: str) -> str | None:
    """`arn:aws:lambda:...:function:NAME[:qualifier]` -> NAME. A non-Lambda target ARN -> None (bounded to
    Lambda invoke edges; a Task that invokes a non-Lambda service is out of this pass's scope)."""
    if ":function:" not in arn:
        return None
    name = arn.split(":function:", 1)[1]
    return name.split(":", 1)[0]  # drop any version/alias qualifier


def _resolve_definition(block: str, tf_dir: Path) -> str:
    """Resolve a state-machine `definition` to its ASL JSON string. Handles the estate's co-located
    `file("${path.module}/X.json")` form and an inline `jsonencode({...})` (best-effort: the {...} is
    handed to the certified walker, which json.loads-returns [] on a non-JSON HCL body -> graceful skip)."""
    fm = _DEF_FILE.search(block)
    if fm:
        rel = fm.group(1).replace("${path.module}/", "").replace("${path.module}", "").lstrip("/\\")
        p = tf_dir / rel
        if p.is_file():
            try:
                return p.read_text(encoding="utf-8", errors="replace")
            except OSError:
                return ""
        return ""
    jm = _DEF_JSONENCODE.search(block)
    if jm:
        return _extract_block(block, jm.start())
    return ""


def extract_sfn_invoke_edges(graph: TraceGraph, workspace_root: Path) -> None:
    """Bridge SFN->Lambda invoke edges into the trace graph, reusing the certified walker. Best-effort:
    any failure skips SFN edges rather than breaking the graph build (the other-pass convention)."""
    try:
        from . import comp_aws_cli  # boto3 is lazy inside _boto(); the walker is pure Python
    except Exception:  # noqa: BLE001 -- no walker available -> no SFN edges, never break the build
        return

    tf_base = workspace_root / "infra" / "aws" / "terraform"
    if not tf_base.exists():
        return

    for tf_file in sorted(tf_base.glob("*/*.tf")):
        try:
            content = tf_file.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        if "aws_sfn_state_machine" not in content:
            continue
        tf_dir = tf_file.parent
        rel_path = str(tf_file.relative_to(workspace_root)).replace("\\", "/")

        for m in _SFN_RESOURCE.finditer(content):
            block = _extract_block(content, m.start())
            nm = _SFN_NAME.search(block)
            sm_name = nm.group(1) if nm else m.group(1)
            defn = _resolve_definition(block, tf_dir)
            if not defn:
                continue
            try:
                invokes = comp_aws_cli._sfn_task_invokes(defn)
            except Exception:  # noqa: BLE001 -- a malformed definition skips, never crashes the build
                continue

            # dedup to UNIQUE (SM, Lambda): 2 Task states -> 1 dependency edge (the 26-invoke oracle grain)
            seen: set[str] = set()
            targets: list[tuple[str, str]] = []
            for state_name, arn in invokes:
                lname = _lambda_name_from_arn(arn)
                if not lname or lname in seen:
                    continue
                seen.add(lname)
                targets.append((state_name, lname))
            if not targets:
                continue

            sm_node_id = f"sfn:{sm_name}"
            graph.add_node(Node(
                id=sm_node_id,
                node_type="STATE_MACHINE",
                label=sm_name,
                file_path=rel_path,
                metadata={"invoke_count": len(targets), "source": "aws_sfn_state_machine"},
            ))
            for state_name, lname in targets:
                lambda_node_id = f"lambda:{lname}"
                if lambda_node_id not in graph.nodes:
                    graph.add_node(Node(
                        id=lambda_node_id,
                        node_type="LAMBDA",
                        label=lname,
                        metadata={"orchestrated_by_sfn": sm_name},
                    ))
                # invocation direction: blast(SM) -> its Lambdas; comp-iam sees the SM->Lambda invoke
                graph.add_edge(Edge(
                    source=sm_node_id,
                    target=lambda_node_id,
                    edge_type="SFN_INVOKES",
                    metadata={"state": state_name, "state_machine": sm_name},
                ))
                # blast-radius direction: blast(Lambda) surfaces the orchestrating SM (the SFNBRIDGE goal)
                graph.add_edge(Edge(
                    source=lambda_node_id,
                    target=sm_node_id,
                    edge_type="SFN_INVOKED_BY",
                    metadata={"state": state_name, "state_machine": sm_name},
                ))
