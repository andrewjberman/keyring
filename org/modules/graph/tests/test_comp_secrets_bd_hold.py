"""comp-secrets `consumers` held-dir EXCLUDE MECHANISM oracle (post-lift form).

HISTORY: authored by 3.0.0_SA_CVO~B under NFRA_TOOLPASS while the 2026-07-09 hold was live;
the hold-era assertion (bd/schwab :(exclude) pathspecs present by default) went stale-red after
the retraction landed (SOVEREIGN_HELD_PATHS=() @7a07814b94 -- HELD_PATH_MARKERS aliases it, so
the exclude list is correctly EMPTY; dial F11, TO ADHOC.graph-tests-hygiene-f11-family).

TRUTH DETERMINATION (grounded at HEAD before this repair): LIFTED, mechanism retained --
.tools/comp-secrets:276-278 still derives `:(exclude)` pathspecs from HELD_PATH_MARKERS at call
time unless the include_held flag is set; the set is empty, so zero excludes emit. Repaired to
post-lift truth + INJECTED-mechanism cases (monkeypatch on the tool module's own binding).

Synthetic + monkeypatched as before -- NEVER actually git-greps anything.
# rail-checked: assurance oracle for comp-secrets (dial F11 repair)
Original author: 3.0.0_SA_CVO~B. F11 repair: 0.8.0_AE_CloudComp~D.
"""
from __future__ import annotations

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


# SYNTHETIC injection marker; must start with "data/" because the guard filters markers on that
# prefix (.tools/comp-secrets:278 `if m.startswith("data/")`).
_SYNTH_MARKER = "data/synthetic_held_zone_f11/"


def test_consumers_emits_no_excludes_post_lift():
    """POST-LIFT TRUTH: HELD_PATH_MARKERS is empty, so NO :(exclude) pathspecs emit -- the grep
    covers every tree, which is the correct lifted behavior."""
    calls = _run(include_held=False)
    assert calls, "cmd_consumers should invoke git grep"
    for argv in calls:
        excludes = [a for a in argv if str(a).startswith(":(exclude)")]
        assert excludes == [], (
            f"post-lift: zero excludes must emit (the governance set is empty): {excludes}"
        )


def test_injected_markers_emit_excludes_and_flag_drops_them(monkeypatch):
    """THE MECHANISM under injection: patch the tool module's own HELD_PATH_MARKERS binding
    (comp-secrets imported the name; :278 reads it from module globals at call time) -- the
    exclude derivation must emit the injected marker by default and DROP it under
    COMP_SECRETS_INCLUDE_HELD=1 (the non-vacuous pair)."""
    monkeypatch.setattr(cs, "HELD_PATH_MARKERS", (_SYNTH_MARKER,))
    default_calls = _run(include_held=False)
    assert default_calls, "cmd_consumers should invoke git grep"
    for argv in default_calls:
        assert ":(exclude)" + _SYNTH_MARKER in argv, (
            f"the INJECTED marker must emit as an exclude by default (mechanism): {argv}"
        )
    override_calls = _run(include_held=True)
    assert override_calls, "cmd_consumers should invoke git grep"
    for argv in override_calls:
        assert ":(exclude)" + _SYNTH_MARKER not in argv, (
            "COMP_SECRETS_INCLUDE_HELD=1 must DROP the injected exclude (non-vacuous)"
        )
