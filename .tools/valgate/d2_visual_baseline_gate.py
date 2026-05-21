#!/usr/bin/env python3
"""VALGATE D-2 -- visual-rendering-vs-baseline gate, verdict layer (ADHC_VALGATE.006).

D-2 is the visual-rendering-fidelity gate: did the right data reach the SCREEN?
Two halves, mirroring D-1 (a diagnostic produces observations; the gate renders
the verdict):

  d2_runner.mjs              the RENDER half -- drives a partner-facing panel in
                             a real browser (puppeteer-core + CDP Chrome), per a
                             structural baseline, and emits a raw results JSON.
  d2_visual_baseline_gate.py the VERDICT half (this file) -- reads the runner's
                             results JSON and renders the D-2 gate verdict.

Phase-0 mechanism (PRD section 7 Q4) -- CONFIRMED structural-assertion variant:
assert a panel's data-bearing nodes are non-empty and correctly scoped, against
a stored structural baseline. NOT pixel-diffing (brittle, CI-expensive). The
runner reuses the /frontend-dev constitution vocabulary but executes via a
standalone puppeteer-core runner -- not the plugin's subagents -- which also
avoids the documented Bun+Playwright CDP-WS hang on Windows.

Section-3.2 gate anatomy
------------------------
  Trigger     post chain-emit, against a served portal -- run on-demand /
              post-deploy (D-2 needs a rendered portal; it does not run inside
              the gold chain -- TO `<cross_domain_coordination>`).
  Input       a rendered partner-facing panel's data-bearing DOM nodes.
  Reference   a stored structural baseline per panel (the data-bearing-node
              set + the expected-scope assertions).
  Comparison  structural emptiness (an empty histogram, a "--" hero card) and
              scope drift (firm-aggregate where advisor-scoped is expected).
  Verdict     PASS  every data-bearing node non-empty + every scope assertion OK.
              WARN  >= 1 structural-emptiness or scope-drift breach.
              (D-2 ships WARN-not-BLOCK in v1 -- PRD section 7 Q1.)
  Action      WARN -> printed report + JSON report for a session log. Never BLOCKs.

Exit codes: 0 PASS, 1 WARN, 3 gate internal error (no results / bad results).

Usage:  d2_visual_baseline_gate.py --results <d2-runner-results.json> [--report <path>]
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# A check's `observed` value and whether it is a breach.
_BREACH_OBSERVED = {'empty', 'missing', 'scope_drift', 'error'}
_OK_OBSERVED = {'non_empty', 'scope_ok'}


def evaluate_results(results: dict) -> dict:
    """Render the D-2 verdict from a runner results JSON.

    `results` shape:
      {"panel": str, "baseline": str, "checks": [
          {"type": "data_bearing"|"scope", "name": str,
           "observed": "non_empty"|"empty"|"missing"|"scope_ok"|"scope_drift"|"error",
           "detail": str (optional)}, ...]}
    """
    checks = results.get('checks', [])
    breaches: list[dict] = []
    ok = 0
    for c in checks:
        observed = c.get('observed', 'error')
        if observed in _BREACH_OBSERVED:
            breaches.append(c)
        elif observed in _OK_OBSERVED:
            ok += 1
        else:
            # unknown observed value -- treat as a breach (fail-loud)
            breaches.append(dict(c, observed=f'{observed} (unrecognized)'))
    verdict = 'WARN' if breaches else 'PASS'
    return {
        'panel': results.get('panel', '<unknown>'),
        'baseline': results.get('baseline', ''),
        'checks_total': len(checks),
        'checks_ok': ok,
        'breaches': breaches,
        'verdict': verdict,
    }


def _print_report(summary: dict) -> None:
    print(f"\n  Panel: {summary['panel']}  (baseline: {summary['baseline']})")
    print(f"  Checks: {summary['checks_ok']}/{summary['checks_total']} OK, "
          f"{len(summary['breaches'])} breach(es) -- {summary['verdict']}")
    for b in summary['breaches']:
        kind = 'structural-emptiness' if b.get('type') == 'data_bearing' \
            else 'scope-drift' if b.get('type') == 'scope' else b.get('type', '?')
        detail = f" -- {b['detail']}" if b.get('detail') else ''
        print(f"    WARN  [{kind}] {b.get('name', '?')} "
              f"observed={b.get('observed')}{detail}")


def main() -> int:
    ap = argparse.ArgumentParser(prog='d2-visual-baseline-gate')
    ap.add_argument('--results', required=True,
                    help='the d2_runner.mjs results JSON')
    ap.add_argument('--report', default=None, help='write the verdict JSON here')
    args = ap.parse_args()

    print('VALGATE D-2 -- visual-rendering-vs-baseline gate (ADHC_VALGATE.006)')

    rp = Path(args.results)
    if not rp.exists():
        print(f'  ERROR: results file not found: {rp}')
        return 3
    try:
        results = json.loads(rp.read_text(encoding='utf-8'))
    except Exception as exc:  # noqa: BLE001
        print(f'  ERROR: could not parse results JSON: {exc}')
        return 3
    if not isinstance(results, dict) or 'checks' not in results:
        print('  ERROR: results JSON missing the "checks" array')
        return 3

    summary = evaluate_results(results)
    _print_report(summary)

    if summary['verdict'] == 'WARN':
        print(f"\n  D-2 VERDICT: WARN -- {len(summary['breaches'])} render-fidelity "
              f"breach(es). (WARN-class -- surface in a session log; does not block.)")
        code = 1
    else:
        print('\n  D-2 VERDICT: PASS -- panel renders all data-bearing nodes, scope OK.')
        code = 0

    if args.report:
        try:
            Path(args.report).write_text(json.dumps(summary, indent=2),
                                         encoding='utf-8')
            print(f'  Report: {args.report}')
        except Exception as exc:  # noqa: BLE001
            print(f'  WARN: could not write report: {exc}')

    return code


if __name__ == '__main__':
    sys.exit(main())
