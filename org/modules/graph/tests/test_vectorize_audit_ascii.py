"""NFRA_TOOLPASS CP1: comp-perf vectorize-audit HARD-CRASHED with UnicodeEncodeError on a cp1252
console because a refactor_sketch template carried U+2192 (->). ROOT = de-unicode the templates;
BELT = harden stdout. This test asserts ASCII output / no crash (RED before, GREEN after).

# rail-checked: assurance oracle for comp-perf under test (NFRA_TOOLPASS sec.6)
Author: 3.0.0_SA_CVO~B. Deterministic; synthetic fixture; bd-safe (no data/inf or data/bd read).
"""

import io
import os
import sys
from pathlib import Path

_HERE = os.path.dirname(os.path.abspath(__file__))
_WS = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(_HERE))))
for _p in (_WS, os.path.dirname(os.path.dirname(_HERE))):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import org.modules.graph.vectorize_audit_cli as va  # noqa: E402

_MODULE = os.path.join(os.path.dirname(_HERE), "vectorize_audit_cli.py")


def test_module_source_is_pure_ascii():
    """ROOT: the production source must carry NO non-ASCII (CLAUDE.md rule). RED before (4), GREEN after."""
    src = open(_MODULE, encoding="utf-8").read()
    bad = [(i, hex(ord(c))) for i, c in enumerate(src) if ord(c) > 127]
    assert not bad, f"non-ASCII in vectorize_audit_cli.py production source: {bad[:8]}"


def test_threadpool_finding_sketch_is_ascii():
    """ROOT: the THREADPOOL-PER-PARTITION finding's refactor_sketch (which HAD the -> arrows) is now ASCII."""
    src = (
        "from concurrent.futures import ThreadPoolExecutor\n"
        "def run(pool, parts):\n"
        "    for p in parts:\n"
        "        pool.submit(load_partition, p)\n"
    )
    findings = va._audit_script(Path("fixture_threadpool.py"), source=src)
    tp = [f for f in findings if f["rule"] == "THREADPOOL-PER-PARTITION"]
    assert tp, "fixture should trigger THREADPOOL-PER-PARTITION (pool.submit in a loop)"
    for f in findings:
        for field in ("refactor_sketch", "detail", "snippet"):
            s = f.get(field, "")
            assert all(ord(c) < 128 for c in s), f"non-ASCII in finding {field}: {s!r}"


def test_belt_hardens_stdout_against_cp1252_crash():
    """BELT: errors='replace' makes a cp1252 stream survive a stray non-ASCII, where a plain one crashes."""
    # Control: a plain cp1252 stream MUST crash on U+2192 (else the belt test is vacuous).
    plain = io.TextIOWrapper(io.BytesIO(), encoding="cp1252")
    crashed = False
    try:
        plain.write("sketch: list comp → pd.concat")
        plain.flush()
    except UnicodeEncodeError:
        crashed = True
    assert crashed, "control: a plain cp1252 stream must raise on U+2192 (test would be vacuous otherwise)"
    # Belt: the harden pattern the tool applies (errors='replace') does NOT raise.
    hardened = io.TextIOWrapper(io.BytesIO(), encoding="cp1252", errors="replace")
    hardened.write("sketch: list comp → pd.concat")   # must not raise
    hardened.flush()


if __name__ == "__main__":
    test_module_source_is_pure_ascii()
    print("PASS: production source is pure ASCII (0 non-ASCII)")
    test_threadpool_finding_sketch_is_ascii()
    print("PASS: THREADPOOL finding sketch (+ all findings) are ASCII")
    test_belt_hardens_stdout_against_cp1252_crash()
    print("PASS: belt (errors='replace') survives U+2192 where a plain cp1252 stream crashes")
    print("=== comp-perf CP1 (vectorize-audit ASCII): ALL PASS ===")
