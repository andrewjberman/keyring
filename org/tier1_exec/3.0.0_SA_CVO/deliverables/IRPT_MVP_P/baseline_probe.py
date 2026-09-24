"""Offline CVO P boundary probe. Executes exact source functions, not a full API.

Only the downstream performance runner is replaced with an argument recorder.
No source imports, credentials, network, vendor calls, or implementation writes.
"""
import ast
import hashlib
import json
import pathlib
import subprocess
from datetime import datetime, timezone
from types import SimpleNamespace

ROOT = pathlib.Path(__file__).resolve().parents[5]
SOURCE = ROOT / "infra/aws/lambda/investor-reporting/performance/entry.py"


def main():
    raw = SOURCE.read_bytes()
    tree = ast.parse(raw.decode("utf-8-sig"))
    functions = [node for node in tree.body if isinstance(node, ast.FunctionDef)
                 and node.name in {"_requested_account_ids", "performance_report"}]
    assert len(functions) == 2
    namespace = {"_handler": SimpleNamespace(
        run=lambda scope, **kwargs: {"scope": scope, "arguments": kwargs})}
    exec(compile(ast.Module(body=functions, type_ignores=[]), str(SOURCE), "exec"), namespace)
    scope = {"permitted_account_set": ["A-1", "A-2"], "resolved_scope": {}}
    scenarios = {
        "browser_query_and_set_reference": {
            "pathParameters": {"accountSetId": "SET-EXAMPLE"},
            "queryStringParameters": {"start": "2026-01-01", "end": "2026-09-21"}},
        "missing_selection": {"queryStringParameters": {
            "start": "2026-01-01", "end": "2026-09-21"}},
        "internal_positive_control": {"account_ids": ["A-1"],
            "requested_start": "2026-01-01", "requested_end": "2026-09-21"},
    }
    observations = {name: namespace["performance_report"](None, scope, event, None)
                    for name, event in scenarios.items()}
    # These assertions verify the observed regression signatures, not product acceptance.
    browser = observations["browser_query_and_set_reference"]
    assert browser["arguments"]["requested_start"] is None
    assert browser["arguments"]["requested_end"] is None
    assert browser["scope"]["resolved_scope"]["scope_ids"] == ["SET-EXAMPLE"]
    assert observations["missing_selection"]["scope"]["resolved_scope"]["scope_ids"] == ["A-1", "A-2"]
    assert observations["internal_positive_control"]["arguments"]["requested_start"] == "2026-01-01"
    assert observations["internal_positive_control"]["scope"]["resolved_scope"]["scope_ids"] == ["A-1"]
    result = {
        "reviewer": "3.0.0_SA_CVO~P", "measured_at": datetime.now(timezone.utc).isoformat(),
        "workspace_head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        "portal_head": subprocess.check_output(["git", "-C", "portal", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        "source": str(SOURCE.relative_to(ROOT)), "source_sha256": hashlib.sha256(raw).hexdigest(),
        "boundary": "two exact AST-extracted functions; downstream runner replaced by argument recorder",
        "live_e2e": "NOT_EVALUATED", "observations": observations,
    }
    target = pathlib.Path(__file__).with_name("baseline_probe.json")
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
