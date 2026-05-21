#!/usr/bin/env python3
"""VALGATE D-2 visual-rendering-baseline gate -- verdict-layer verification (AC3).

Tests the D-2 verdict layer (d2_visual_baseline_gate.evaluate_results) against
synthetic runner-results JSONs -- the three AC3 cases:
  - a deliberately-emptied panel  -> WARN
  - a wrong-scope panel           -> WARN
  - a correct render              -> PASS
plus the per-observed-value classification.

The verdict layer is the deterministic, browser-independent half of D-2 and is
fully covered here. The render half (d2_runner.mjs) is exercised against a
served portal in the AC3 live runner-session (see VALGATE_D2.md).

Run:  python .tools/valgate/d2_gate_test.py
Exit: 0 = all cases pass; 1 = a case failed.
"""
from __future__ import annotations

import sys
from pathlib import Path

_THIS = Path(__file__).resolve()
sys.path.insert(0, str(_THIS.parent))
import d2_visual_baseline_gate as gate  # noqa: E402

_results: list[tuple[bool, str]] = []


def _check(ok: bool, label: str) -> None:
    _results.append((ok, label))
    print(f'  {"PASS" if ok else "FAIL"}  {label}')


def _data(name, observed):
    return {'type': 'data_bearing', 'name': name, 'observed': observed}


def _scope(name, observed):
    return {'type': 'scope', 'name': name, 'observed': observed}


def main() -> int:
    print('VALGATE D-2 visual-rendering-baseline gate -- verdict-layer verification')

    # AC3 case 1 -- a correct render: every node non-empty, scope OK -> PASS.
    correct = {'panel': 'advisor-book-headline', 'baseline': 'seed', 'checks': [
        _data('total-aua-hero', 'non_empty'),
        _data('client-bell-curve', 'non_empty'),
        _scope('advisor-scoped', 'scope_ok'),
    ]}
    s = gate.evaluate_results(correct)
    _check(s['verdict'] == 'PASS', f'correct render -> PASS (got {s["verdict"]})')

    # AC3 case 2 -- a deliberately-emptied panel: a data-bearing node empty -> WARN.
    emptied = {'panel': 'advisor-book-headline', 'baseline': 'seed', 'checks': [
        _data('total-aua-hero', 'empty'),          # "--" hero card
        _data('client-bell-curve', 'non_empty'),
        _scope('advisor-scoped', 'scope_ok'),
    ]}
    s = gate.evaluate_results(emptied)
    _check(s['verdict'] == 'WARN' and len(s['breaches']) == 1,
           f'deliberately-emptied panel -> WARN (got {s["verdict"]})')
    _check(s['breaches'][0]['name'] == 'total-aua-hero',
           'the emptied node is named in the breach list')

    # an empty CHART (empty bell-curve -- the INFFIN anchor) -> WARN.
    empty_chart = {'panel': 'p', 'baseline': 'seed', 'checks': [
        _data('client-bell-curve', 'empty'),
    ]}
    _check(gate.evaluate_results(empty_chart)['verdict'] == 'WARN',
           'empty bell-curve chart -> WARN')

    # a missing node (selector matched nothing) -> WARN.
    missing = {'panel': 'p', 'baseline': 'seed', 'checks': [_data('hero', 'missing')]}
    _check(gate.evaluate_results(missing)['verdict'] == 'WARN',
           'missing data-bearing node -> WARN')

    # AC3 case 3 -- a wrong-scope panel: firm-aggregate where advisor expected.
    wrong_scope = {'panel': 'advisor-book-headline', 'baseline': 'seed', 'checks': [
        _data('total-aua-hero', 'non_empty'),
        _data('client-bell-curve', 'non_empty'),
        _scope('advisor-scoped', 'scope_drift'),   # firm-aggregate leaked in
    ]}
    s = gate.evaluate_results(wrong_scope)
    _check(s['verdict'] == 'WARN', f'wrong-scope panel -> WARN (got {s["verdict"]})')
    _check(s['breaches'][0]['type'] == 'scope',
           'the scope-drift breach is classified type=scope')

    # a runner error on a check -> WARN (fail-loud).
    errored = {'panel': 'p', 'baseline': 'seed', 'checks': [_data('hero', 'error')]}
    _check(gate.evaluate_results(errored)['verdict'] == 'WARN',
           'a runner error on a check -> WARN (fail-loud)')

    # an unrecognized observed value -> WARN (fail-loud).
    weird = {'panel': 'p', 'baseline': 'seed', 'checks': [_data('hero', 'banana')]}
    _check(gate.evaluate_results(weird)['verdict'] == 'WARN',
           'unrecognized observed value -> WARN (fail-loud)')

    # no checks at all -> PASS (vacuous -- nothing to assert).
    _check(gate.evaluate_results({'panel': 'p', 'checks': []})['verdict'] == 'PASS',
           'empty checks list -> PASS (vacuous)')

    # mixed -- counts are correct.
    mixed = {'panel': 'p', 'baseline': 'seed', 'checks': [
        _data('a', 'non_empty'), _data('b', 'empty'),
        _scope('c', 'scope_ok'), _scope('d', 'scope_drift'),
    ]}
    s = gate.evaluate_results(mixed)
    _check(s['verdict'] == 'WARN' and s['checks_ok'] == 2 and len(s['breaches']) == 2,
           f'mixed checks -> WARN, 2 ok / 2 breach (got ok={s["checks_ok"]})')

    passed = sum(1 for ok, _ in _results if ok)
    total = len(_results)
    print(f'\n{"PASS" if passed == total else "FAIL"}: {passed}/{total} cases passed')
    return 0 if passed == total else 1


if __name__ == '__main__':
    sys.exit(main())
