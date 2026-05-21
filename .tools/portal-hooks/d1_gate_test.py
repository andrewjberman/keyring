#!/usr/bin/env python3
"""VALGATE D-1 adapter-threading gate -- verification harness (ADHC_VALGATE.004 AC3).

Two layers:
  1. Verdict-logic unit tests -- _verdict_for_adapter / _adapter_spans / _overlaps
     against synthetic inputs. Fully deterministic, no S3, no portal fixture.
  2. End-to-end fixture tests -- a synthetic adapter with a deliberately
     un-threaded output path (an inverted `??` fallback chain -- the INFFIN-arc
     anchor pattern, 32df3b85 class) is BLOCKed; a correct adapter is not.
     The fixture .ts file is created in portal/src/api/endpoints/, exercised,
     and removed (try/finally) -- it is never committed.

Run:  python .tools/portal-hooks/d1_gate_test.py
Exit: 0 = all cases pass; 1 = a case failed.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

_THIS = Path(__file__).resolve()
sys.path.insert(0, str(_THIS.parent))
import d1_adapter_threading_gate as gate  # noqa: E402

_WORKSPACE = _THIS.parents[2]
_ENDPOINTS_DIR = _WORKSPACE / 'portal' / 'src' / 'api' / 'endpoints'
_GATE_PY = _THIS.parent / 'd1_adapter_threading_gate.py'
_AUDIT_MANIFEST_DIR = _WORKSPACE / 'org' / 'modules' / 'graph' / 'adapter-audit'

_results: list[tuple[bool, str]] = []


def _check(ok: bool, label: str) -> None:
    _results.append((ok, label))
    print(f'  {"PASS" if ok else "FAIL"}  {label}')


# --------------------------------------------------------------------------
# Layer 1 -- verdict-logic unit tests (synthetic, deterministic)
# --------------------------------------------------------------------------

def test_verdict_logic() -> None:
    print('\n[Layer 1] verdict-logic unit tests')

    # FALLBACK-ORDER on a partner-facing adapter -> BLOCK (the D-1 defect).
    v, _ = gate._verdict_for_adapter(['FALLBACK-ORDER'], partner_facing=True)
    _check(v == 'BLOCK', f'FALLBACK-ORDER + partner-facing -> BLOCK (got {v})')

    # Same finding, non-partner-facing -> WARN, never BLOCK.
    v, _ = gate._verdict_for_adapter(['FALLBACK-ORDER'], partner_facing=False)
    _check(v == 'WARN', f'FALLBACK-ORDER + non-partner-facing -> WARN (got {v})')

    # ~65 SCHEMA-DRIFT findings (the live-adapter baseline) -> WARN, not BLOCK.
    v, _ = gate._verdict_for_adapter(['SCHEMA-DRIFT'] * 65, partner_facing=True)
    _check(v == 'WARN', f'65x SCHEMA-DRIFT + partner-facing -> WARN (got {v})')

    # NOT-THREADED is the inverse direction (raw-unconsumed) -> WARN, not BLOCK.
    v, _ = gate._verdict_for_adapter(['NOT-THREADED'], partner_facing=True)
    _check(v == 'WARN', f'NOT-THREADED + partner-facing -> WARN not BLOCK (got {v})')

    # TYPE-ONLY (typed-but-absent, INFO-grade) -> WARN, not BLOCK.
    v, _ = gate._verdict_for_adapter(['TYPE-ONLY'], partner_facing=True)
    _check(v == 'WARN', f'TYPE-ONLY + partner-facing -> WARN (got {v})')

    # No findings -> PASS.
    v, _ = gate._verdict_for_adapter([], partner_facing=True)
    _check(v == 'PASS', f'no findings -> PASS (got {v})')

    # A FALLBACK-ORDER mixed into benign drift still BLOCKs (partner-facing).
    v, _ = gate._verdict_for_adapter(
        ['SCHEMA-DRIFT'] * 10 + ['FALLBACK-ORDER'], partner_facing=True)
    _check(v == 'BLOCK', f'SCHEMA-DRIFT + FALLBACK-ORDER + partner -> BLOCK (got {v})')

    # _adapter_spans finds a static partner adapter and its line span.
    sample = (
        'const x = 1;\n'
        'export async function getPlatinumThingStatic(id: string) {\n'
        '  const raw = await fetch(id);\n'
        '  return raw;\n'
        '}\n'
        'function helper() { return 2; }\n'
    )
    spans = gate._adapter_spans(sample)
    _check('getPlatinumThingStatic' in spans,
           f'_adapter_spans detects getPlatinumThingStatic (got {list(spans)})')
    _check('helper' not in spans,
           '_adapter_spans excludes a non-adapter helper function')
    if 'getPlatinumThingStatic' in spans:
        s, e = spans['getPlatinumThingStatic']
        _check(s == 2 and e == 5,
               f'_adapter_spans span is lines 2..5 (got {s}..{e})')

    # _overlaps -- a changed line inside the span is a hit; outside is not.
    _check(gate._overlaps((2, 5), [(3, 3)]) is True,
           '_overlaps: changed line 3 intersects span 2..5')
    _check(gate._overlaps((2, 5), [(9, 9)]) is False,
           '_overlaps: changed line 9 does not intersect span 2..5')


# --------------------------------------------------------------------------
# Layer 2 -- end-to-end fixture tests (synthetic adapter, real audit path)
# --------------------------------------------------------------------------

_FIXTURE_NAME = '__d1_gate_test_fixture.ts'

# An inverted `??` fallback chain: `.book` first masks fields only `.summary`
# carries -> the output silently drops them. This is the INFFIN #7 / 32df3b85
# defect pattern -- comp-adapter-audit flags it FALLBACK-ORDER.
# A second adapter spreads `summary` then `book` with no `??` -- no defect.
_FIXTURE_TS = '''// VALGATE D-1 gate test fixture -- created + removed by d1_gate_test.py.
// NEVER COMMITTED. If you see this file in git status, delete it.
import { apiRequest } from "../api-client";

interface D1TestRaw {
  book: Record<string, unknown>;
  summary: Record<string, unknown>;
}

// BLOCK case: inverted fallback chain drops summary-only fields from the output.
export async function getPlatinumD1TestBlockStatic(advisorId: string): Promise<unknown> {
  const raw = await apiRequest<D1TestRaw>(`/platinum/advisors/${advisorId}/book.json`);
  const merged = raw.book ?? raw.summary;
  return merged;
}

// PASS case: no fallback chain, spread-merge preserves all fields.
export async function getPlatinumD1TestPassStatic(advisorId: string): Promise<unknown> {
  const res = await fetch(`/platinum/advisors/${advisorId}/__d1_nonexist.json`);
  return res.json();
}
'''


def _run_gate(adapters: str) -> int:
    """Run the D-1 gate over an explicit adapter list; return its exit code."""
    r = subprocess.run(
        [sys.executable, str(_GATE_PY),
         '--local-sha', 'HEAD', '--remote-sha', 'HEAD',
         '--adapters', adapters],
        capture_output=True, text=True, timeout=180,
    )
    sys.stdout.write(r.stdout)
    if r.stderr.strip():
        sys.stdout.write(r.stderr)
    return r.returncode


def test_end_to_end() -> None:
    print('\n[Layer 2] end-to-end fixture tests (synthetic adapter)')
    fixture = _ENDPOINTS_DIR / _FIXTURE_NAME
    written = []
    try:
        fixture.write_text(_FIXTURE_TS, encoding='utf-8')

        # BLOCK case, partner-facing -> exit 1 (push refused).
        rc = _run_gate('getPlatinumD1TestBlockStatic:partner')
        _check(rc == 1,
               f'inverted-fallback adapter + partner-facing -> BLOCK exit 1 (got {rc})')

        # Same defect, non-partner-facing -> exit 0 (WARN, never BLOCK).
        rc = _run_gate('getPlatinumD1TestBlockStatic:nonpartner')
        _check(rc == 0,
               f'inverted-fallback adapter + non-partner-facing -> WARN exit 0 (got {rc})')

        # Correct adapter -> exit 0 (not blocked).
        rc = _run_gate('getPlatinumD1TestPassStatic:partner')
        _check(rc == 0,
               f'correct adapter (no inverted fallback) -> not blocked, exit 0 (got {rc})')
    finally:
        if fixture.exists():
            fixture.unlink()
        # Remove the audit manifests the test runs produced.
        for name in ('getPlatinumD1TestBlockStatic', 'getPlatinumD1TestPassStatic'):
            m = _AUDIT_MANIFEST_DIR / f'{name}.yaml'
            if m.exists():
                m.unlink()
                written.append(m.name)
        print(f'  cleanup: removed fixture + {len(written)} test manifest(s)')


def main() -> int:
    print('VALGATE D-1 adapter-threading gate -- verification harness')
    test_verdict_logic()
    test_end_to_end()
    passed = sum(1 for ok, _ in _results if ok)
    total = len(_results)
    print(f'\n{"PASS" if passed == total else "FAIL"}: {passed}/{total} cases passed')
    return 0 if passed == total else 1


if __name__ == '__main__':
    sys.exit(main())
