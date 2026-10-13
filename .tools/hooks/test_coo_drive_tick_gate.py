"""coo-drive-tick-gate.py: the empty-tick rule, read from the turn (Andrew-direct 2026-10-13 ~21:1xZ)."""
import importlib.util
import json
import pathlib

HOOK = pathlib.Path(__file__).resolve().parent / "coo-drive-tick-gate.py"
_spec = importlib.util.spec_from_file_location("gate", HOOK)
gate = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(gate)


def _tool(name, **inp):
    return {"type": "assistant", "message": {"content": [{"type": "tool_use", "name": name, "input": inp}]}}


def _run(tmp_path, serial, prompt, tools, active=False, switch=True):
    lines = [_tool("mcp__opal-agent-comms__register_agent", agent_serial=serial),
             {"type": "user", "message": {"content": prompt}}] + tools
    t = tmp_path / "t.jsonl"
    t.write_text("\n".join(json.dumps(x) for x in lines), encoding="utf-8")
    return gate.verdict({"transcript_path": str(t), "stop_hook_active": active}, str(tmp_path), switch=lambda _r: switch)


def test_case_study_empty_tick_labelled_drive_forward_blocks(tmp_path):
    tools = [_tool("Skill", skill="canonical-drive"), _tool("Bash", command="python .tools/drive-mode.py read NFRA_CTLPLN"),
             _tool("mcp__opal-agent-comms__heartbeat", agent_serial="2.0.0_SA_COO~C")]
    r = _run(tmp_path, "2.0.0_SA_COO~C", "/canonical-drive", tools)
    assert r and "/next-calls" in r and "unblock.py tick" in r


def test_log_only_commit_is_not_an_act(tmp_path):
    tools = [_tool("Bash", command="bash .tools/safe-commit.sh --author x -F m.txt -- org/tier1_exec/2.0.0_SA_COO~C/drive_log_20261013T21Z_laptop.md")]
    assert _run(tmp_path, "2.0.0_SA_COO~C", "/canonical-drive", tools)


def test_fired_acts_pass(tmp_path):
    for t in (_tool("Agent", prompt="cell"), _tool("mcp__opal-agent-comms__send_message", body="nudge"),
              _tool("Bash", command="bash .tools/safe-commit.sh -F m -- org/missions/D0/X/task-orders/A.md"),
              _tool("Bash", command="bash .tools/safe-merge.sh wk-x")):
        assert _run(tmp_path, "2.0.0_SA_COO~C", "/canonical-drive", [t]) is None


def test_empty_tick_with_rule_run_passes(tmp_path):
    tools = [_tool("Skill", skill="next-calls", args="NFRA_CTLPLN --drive"),
             _tool("Bash", command="python .tools/unblock.py tick --serial 2.0.0_SA_COO~C --project NFRA_CTLPLN --result nothing")]
    assert _run(tmp_path, "2.0.0_SA_COO~C", "/canonical-drive", tools) is None


def test_non_application(tmp_path):
    assert _run(tmp_path, "1.0.0_SA_CTO", "/canonical-drive", []) is None          # not a COO
    assert _run(tmp_path, "2.0.0_SA_COO~C", "what is the status?", []) is None    # no drive this turn
    assert _run(tmp_path, "2.0.0_SA_COO~C", "/canonical-drive", [], switch=False) is None  # switch OFF
    assert _run(tmp_path, "2.0.0_SA_COO~C", "/canonical-drive", [], active=True) is None   # blocks once per turn
