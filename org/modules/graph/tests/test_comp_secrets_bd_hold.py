"""NFRA_TOOLPASS: comp-secrets `consumers` git-greps ["infra/","data/","org/",".tools/","docs/"]
for a secret name/arn -- `data/` includes data/black_diamond, so it READS bd SOURCE content (the
bd-reader class). FIX: git :(exclude) magic pathspec for the held dirs unless
COMP_SECRETS_INCLUDE_HELD=1, NAMED (loud-note), matching the comp-pipescript deployed pattern.

This test (synthetic, monkeypatched -- NEVER actually git-greps bd) captures the git-grep argv and
asserts the held :(exclude) pathspecs are present by default and dropped under the override.

# rail-checked: assurance oracle for comp-secrets under test (NFRA_TOOLPASS sec.6)
Author: 3.0.0_SA_CVO~B.
"""

import importlib.util
import io
import os
from contextlib import redirect_stdout
from importlib.machinery import SourceFileLoader
from types import SimpleNamespace

_HERE = os.path.dirname(os.path.abspath(__file__))
_WS = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(_HERE))))
_TOOL = os.path.join(_WS, ".tools", "comp-secrets")

# .tools/comp-secrets has no .py extension -> load it via an explicit SourceFileLoader.
_loader = SourceFileLoader("comp_secrets_tool", _TOOL)
_spec = importlib.util.spec_from_loader(_loader.name, _loader)
cs = importlib.util.module_from_spec(_spec)
_loader.exec_module(cs)


class _CP:
    stdout = ""
    stderr = ""
    returncode = 0


def _run(include_held: bool):
    captured: list = []
    orig_run, orig_client, orig_resolve = cs.subprocess.run, cs._client, cs._resolve

    def _fake_run(argv, **k):
        captured.append(list(argv))
        return _CP()

    cs.subprocess.run = _fake_run
    cs._client = lambda: object()
    cs._resolve = lambda client, ident: {
        "Name": "test/secret",
        "ARN": "arn:aws:secretsmanager:us-east-1:123456789012:secret:test-abc123",
    }
    if include_held:
        os.environ["COMP_SECRETS_INCLUDE_HELD"] = "1"
    else:
        os.environ.pop("COMP_SECRETS_INCLUDE_HELD", None)
    try:
        with redirect_stdout(io.StringIO()):
            cs.cmd_consumers(SimpleNamespace(ident="test/secret"))
    finally:
        cs.subprocess.run, cs._client, cs._resolve = orig_run, orig_client, orig_resolve
        os.environ.pop("COMP_SECRETS_INCLUDE_HELD", None)
    return [a for a in captured if a and a[0] == "git"]


def test_consumers_excludes_bd_and_schwab_by_default():
    calls = _run(include_held=False)
    assert calls, "cmd_consumers should invoke git grep"
    for argv in calls:
        assert ":(exclude)data/black_diamond/" in argv, f"bd source not excluded: {argv}"
        assert ":(exclude)data/canonical/schwab/silver/" in argv, f"schwab source not excluded: {argv}"


def test_include_held_override_drops_the_exclude_non_vacuous():
    calls = _run(include_held=True)
    assert calls, "cmd_consumers should invoke git grep"
    for argv in calls:
        assert ":(exclude)data/black_diamond/" not in argv, \
            "COMP_SECRETS_INCLUDE_HELD=1 must DROP the exclude (proves the guard gates -- non-vacuous)"


if __name__ == "__main__":
    d = _run(False)
    print(f"[default]  git calls={len(d)}  bd-excluded={all(':(exclude)data/black_diamond/' in a for a in d)}")
    test_consumers_excludes_bd_and_schwab_by_default()
    print("PASS: consumers excludes bd + schwab source by default (:(exclude) pathspec in every git-grep call)")
    o = _run(True)
    print(f"[override] git calls={len(o)}  bd-excluded={any(':(exclude)data/black_diamond/' in a for a in o)}")
    test_include_held_override_drops_the_exclude_non_vacuous()
    print("PASS: COMP_SECRETS_INCLUDE_HELD=1 drops the exclude (non-vacuous)")
    print("=== comp-secrets consumers bd-hold: ALL PASS ===")
