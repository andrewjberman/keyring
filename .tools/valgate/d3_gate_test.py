#!/usr/bin/env python3
"""VALGATE D-3 multi-axis envelope gate -- verification harness (ADHC_VALGATE.005 AC3).

Three layers:
  1. Envelope-logic unit tests   -- axis_implausible against nonzero / range /
                                    non_null envelopes.
  2. Threshold-logic unit tests  -- evaluate_entity: >=2 bad axes WARN, a
                                    single off-axis PASS (threshold-2 holds).
  3. End-to-end + AC2            -- run the gate over synthetic platinum
                                    book.json artifacts with the SEED config;
                                    verify the seed preserves the shipped
                                    AdvisorBookView 6-axis coverage.

Run:  python .tools/valgate/d3_gate_test.py
Exit: 0 = all cases pass; 1 = a case failed.
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

_THIS = Path(__file__).resolve()
sys.path.insert(0, str(_THIS.parent))
import d3_multi_axis_envelope_gate as gate  # noqa: E402

_GATE_PY = _THIS.parent / 'd3_multi_axis_envelope_gate.py'
_SEED_CONFIG = _THIS.parent / 'd3-seed-config.json'

_results: list[tuple[bool, str]] = []


def _check(ok: bool, label: str) -> None:
    _results.append((ok, label))
    print(f'  {"PASS" if ok else "FAIL"}  {label}')


# --------------------------------------------------------------------------
# Layer 1 -- envelope-logic unit tests
# --------------------------------------------------------------------------

def test_envelope_logic() -> None:
    print('\n[Layer 1] envelope-logic unit tests')
    nz = {'nonzero': True}
    _check(gate.axis_implausible(0, nz)[0] is True, 'nonzero: 0 -> implausible')
    _check(gate.axis_implausible(None, nz)[0] is True, 'nonzero: null -> implausible')
    _check(gate.axis_implausible(301934.67, nz)[0] is False, 'nonzero: positive -> OK')
    _check(gate.axis_implausible(-5, nz)[0] is False, 'nonzero: negative -> OK (only 0/null fire)')

    rng = {'min': 0, 'max': 100}
    _check(gate.axis_implausible(50, rng)[0] is False, 'range[0,100]: 50 -> OK')
    _check(gate.axis_implausible(150, rng)[0] is True, 'range[0,100]: 150 -> implausible')
    _check(gate.axis_implausible(-1, rng)[0] is True, 'range[0,100]: -1 -> implausible')

    nn = {'non_null': True}
    _check(gate.axis_implausible(None, nn)[0] is True, 'non_null: null -> implausible')
    _check(gate.axis_implausible(0, nn)[0] is False, 'non_null: 0 -> OK (0 is not null)')

    _check(gate.axis_implausible(0, {})[0] is False, 'empty envelope: nothing fires')


# --------------------------------------------------------------------------
# Layer 2 -- threshold-logic unit tests
# --------------------------------------------------------------------------

def test_threshold_logic() -> None:
    print('\n[Layer 2] threshold-logic unit tests (joint >=N-axis fire rule)')
    axes = [
        {'key': 'a', 'envelope': {'nonzero': True}},
        {'key': 'b', 'envelope': {'nonzero': True}},
        {'key': 'c', 'envelope': {'nonzero': True}},
    ]
    # 0 bad axes -> PASS
    r = gate.evaluate_entity({'a': 1, 'b': 2, 'c': 3}, axes, threshold=2)
    _check(r['verdict'] == 'PASS', f'0 implausible axes -> PASS (got {r["verdict"]})')
    # 1 bad axis -> PASS (a single off-axis is legitimate sparse-emit)
    r = gate.evaluate_entity({'a': 0, 'b': 2, 'c': 3}, axes, threshold=2)
    _check(r['verdict'] == 'PASS',
           f'1 implausible axis + threshold 2 -> PASS (got {r["verdict"]})')
    # 2 bad axes -> WARN (jointly implausible)
    r = gate.evaluate_entity({'a': 0, 'b': None, 'c': 3}, axes, threshold=2)
    _check(r['verdict'] == 'WARN' and r['implausible_count'] == 2,
           f'2 implausible axes + threshold 2 -> WARN (got {r["verdict"]})')
    # 3 bad axes -> WARN
    r = gate.evaluate_entity({'a': 0, 'b': 0, 'c': 0}, axes, threshold=2)
    _check(r['verdict'] == 'WARN' and r['implausible_count'] == 3,
           f'3 implausible axes -> WARN (got {r["verdict"]})')
    # threshold is configurable -- threshold 1 fires on a single off-axis
    r = gate.evaluate_entity({'a': 0, 'b': 2, 'c': 3}, axes, threshold=1)
    _check(r['verdict'] == 'WARN',
           f'1 implausible axis + threshold 1 -> WARN (configurable) (got {r["verdict"]})')


# --------------------------------------------------------------------------
# Layer 3 -- end-to-end with the seed config + AC2 coverage check
# --------------------------------------------------------------------------

_HEALTHY = {'total_aua': 301934.67, 'fee_earning_aua': 250000.0, 'nna_ytd': 1200.0,
            'client_count': 7, 'account_count': 51, 'implied_annual_revenue': 3100.0}
_ONE_OFF = dict(_HEALTHY, nna_ytd=0)                       # 1 axis off -> PASS
_JOINTLY_BAD = dict(_HEALTHY, total_aua=0, fee_earning_aua=None, nna_ytd=0)  # 3 off -> WARN


def _write_advisor(root: Path, name: str, book: dict) -> None:
    d = root / name
    d.mkdir(parents=True, exist_ok=True)
    (d / 'book.json').write_text(
        json.dumps({'advisor_key': name, 'book': book}), encoding='utf-8')


def test_end_to_end() -> None:
    print('\n[Layer 3] end-to-end with the seed config')
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        _write_advisor(root, 'healthy_advisor', _HEALTHY)
        _write_advisor(root, 'one_off_advisor', _ONE_OFF)
        _write_advisor(root, 'jointly_bad_advisor', _JOINTLY_BAD)

        r = subprocess.run(
            [sys.executable, str(_GATE_PY),
             '--artifacts', str(root), '--config', str(_SEED_CONFIG)],
            capture_output=True, text=True, timeout=60)
        sys.stdout.write(r.stdout)
        out = r.stdout

        _check(r.returncode == 1,
               f'mixed artifacts (1 jointly-bad advisor) -> exit 1 / WARN (got {r.returncode})')
        _check('jointly_bad_advisor' in out,
               'jointly-bad advisor (>=2 implausible axes) is WARNed by name')
        _check('one_off_advisor' not in out,
               'one-off advisor (1 implausible axis) is NOT WARNed (threshold-2 holds)')
        _check('healthy_advisor' not in out,
               'healthy advisor is NOT WARNed')

        # all-healthy -> PASS / exit 0
        with tempfile.TemporaryDirectory() as tmp2:
            root2 = Path(tmp2)
            _write_advisor(root2, 'adv_a', _HEALTHY)
            _write_advisor(root2, 'adv_b', _HEALTHY)
            r2 = subprocess.run(
                [sys.executable, str(_GATE_PY),
                 '--artifacts', str(root2), '--config', str(_SEED_CONFIG)],
                capture_output=True, text=True, timeout=60)
            _check(r2.returncode == 0,
                   f'all-healthy artifacts -> exit 0 / PASS (got {r2.returncode})')


def test_ac2_coverage() -> None:
    print('\n[AC2] seed config preserves the shipped AdvisorBookView 6-axis coverage')
    config = json.loads(_SEED_CONFIG.read_text(encoding='utf-8'))
    surf = next((s for s in config['surfaces'] if s['name'] == 'advisor_book'), None)
    _check(surf is not None, 'seed config has the advisor_book surface')
    if not surf:
        return
    # The six axes of warnOnInflectionAdvisorDrift (AdvisorBookView.tsx:104-111).
    shipped_axes = {'total_aua', 'fee_earning_aua', 'nna_ytd',
                    'client_count', 'account_count', 'implied_annual_revenue'}
    seed_axes = {a['key'] for a in surf['axes']}
    _check(seed_axes == shipped_axes,
           f'seed axes match the shipped 6-axis set (got {sorted(seed_axes)})')
    _check(surf['threshold'] == 2, 'seed threshold is 2 (matches the shipped sentinel)')
    _check(all(a['envelope'] == {'nonzero': True} for a in surf['axes']),
           "every seed axis uses the 'nonzero' envelope (reproduces v==null||v===0)")


def main() -> int:
    print('VALGATE D-3 multi-axis envelope gate -- verification harness')
    test_envelope_logic()
    test_threshold_logic()
    test_end_to_end()
    test_ac2_coverage()
    passed = sum(1 for ok, _ in _results if ok)
    total = len(_results)
    print(f'\n{"PASS" if passed == total else "FAIL"}: {passed}/{total} cases passed')
    return 0 if passed == total else 1


if __name__ == '__main__':
    sys.exit(main())
