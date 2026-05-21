#!/usr/bin/env python3
"""VALGATE D-3 -- multi-axis envelope-validation sentinel gate (ADHC_VALGATE.005).

Generalizes the shipped INFFIN.006 AdvisorBookView 6-axis threshold-2 sentinel
(portal/src/pages/AdvisorIntelligence/_shared/AdvisorBookView.tsx,
`warnOnInflectionAdvisorDrift`) into a reusable, configuration-driven gate.

The shipped instance hardcodes one entity (an advisor's `book`), six axes, and
a trivial "null-or-zero" envelope, fires a `console.warn` when >= 2 axes are
jointly implausible, and lives inline in one React component. D-3 lifts that
core -- the per-axis envelope check + the joint >=N-axis fire rule -- into a
gate driven by an (entity type, metric vector, per-axis envelopes, threshold)
config that applies to any entity-metric surface in a platinum artifact, post
chain-emit.

Section-3.2 gate anatomy
------------------------
  Trigger     post chain-emit -- run against the freshly-emitted platinum
              artifacts (PRD section 3.3). Standalone + config-driven; it does
              not modify the gold chain.
  Input       each entity's metric vector in a platinum artifact, per the
              surfaces declared in the config.
  Reference   a per-axis plausibility envelope (declared in the config) --
              `nonzero`, `non_null`, and/or `min`/`max` bounds.
  Comparison  count the axes whose value falls outside its envelope; the
              entity fires when count >= the surface's threshold (default 2 --
              a single off-axis is often legitimate sparse-emit; two jointly
              is a signal).
  Verdict     PASS  no entity hit its threshold.
              WARN  >= 1 entity hit its threshold.
              (D-3 ships WARN-not-BLOCK in v1 -- PRD section 7 Q1.)
  Action      WARN -> surface (printed report + a written report file for a
              session log / post-chain step). D-3 never BLOCKs.

Exit codes
----------
  0  PASS  -- every entity within envelope on < threshold axes.
  1  WARN  -- >= 1 entity jointly implausible on >= threshold axes.
  3  gate internal error (bad config, no artifacts, etc.).
A post-chain caller treats exit 1 as WARN -- log it, do NOT fail the chain.

Usage
-----
  d3_multi_axis_envelope_gate.py --artifacts <file-or-dir> [--config <json>]
                                 [--surface <name>] [--report <path>]
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

_THIS = Path(__file__).resolve()
_DEFAULT_CONFIG = _THIS.parent / 'd3-seed-config.json'


# -------------------------------------------------------------------------
# Envelope evaluation -- the reusable core lifted from the INFFIN.006 sentinel
# -------------------------------------------------------------------------

def axis_implausible(value: object, envelope: dict) -> tuple[bool, str]:
    """Is `value` outside its plausibility `envelope`?

    Returns (implausible, reason). An empty envelope never fires. Supported
    envelope constraints (any combination -- implausible if ANY is violated):
      nonzero       true -> value must be present and != 0
      non_null      true -> value must be present (not None)
      min / max               inclusive bounds
      min_exclusive / max_exclusive   exclusive bounds
    """
    if not envelope:
        return False, ''

    is_num = isinstance(value, (int, float)) and not isinstance(value, bool)

    if envelope.get('non_null') and value is None:
        return True, 'null'
    if envelope.get('nonzero'):
        if value is None:
            return True, 'null'
        if is_num and value == 0:
            return True, 'zero'
        if not is_num:
            return True, 'non-numeric'

    for key, op in (('min', '<'), ('min_exclusive', '<='),
                    ('max', '>'), ('max_exclusive', '>=')):
        if key not in envelope:
            continue
        bound = envelope[key]
        if value is None:
            return True, f'null (expected {key}={bound})'
        if not is_num:
            return True, f'non-numeric (expected {key}={bound})'
        if op == '<' and value < bound:
            return True, f'{value} < min {bound}'
        if op == '<=' and value <= bound:
            return True, f'{value} <= min_exclusive {bound}'
        if op == '>' and value > bound:
            return True, f'{value} > max {bound}'
        if op == '>=' and value >= bound:
            return True, f'{value} >= max_exclusive {bound}'

    return False, ''


def evaluate_entity(metric_obj: dict, axes: list[dict], threshold: int) -> dict:
    """Evaluate one entity's metric vector. Returns a result dict."""
    implausible: list[dict] = []
    for axis in axes:
        key = axis['key']
        envelope = axis.get('envelope', {})
        value = metric_obj.get(key) if isinstance(metric_obj, dict) else None
        bad, reason = axis_implausible(value, envelope)
        if bad:
            implausible.append({'axis': key, 'value': value, 'reason': reason})
    n = len(implausible)
    verdict = 'WARN' if n >= threshold else 'PASS'
    return {
        'verdict': verdict,
        'implausible_count': n,
        'axis_count': len(axes),
        'threshold': threshold,
        'implausible_axes': implausible,
    }


# -------------------------------------------------------------------------
# Artifact loading + path walking
# -------------------------------------------------------------------------

def get_path(obj: object, dotted: str) -> object:
    """Walk a dotted path into a nested dict. Missing -> None."""
    cur = obj
    for part in dotted.split('.'):
        if isinstance(cur, dict) and part in cur:
            cur = cur[part]
        else:
            return None
    return cur


def load_artifacts(artifacts: Path, artifact_filename: str) -> list[tuple[str, dict]]:
    """Load platinum JSON artifacts.

    `artifacts` may be a single JSON file or a directory. For a directory, all
    files named `artifact_filename` anywhere beneath it are loaded (the
    platinum layout is .../advisors/<name>/<artifact_filename>).
    """
    out: list[tuple[str, dict]] = []
    if artifacts.is_file():
        files = [artifacts]
    elif artifacts.is_dir():
        files = sorted(artifacts.rglob(artifact_filename)) if artifact_filename \
            else sorted(artifacts.rglob('*.json'))
    else:
        return out
    for f in files:
        try:
            data = json.loads(f.read_text(encoding='utf-8', errors='ignore'))
            if isinstance(data, dict):
                out.append((str(f), data))
        except Exception as exc:  # noqa: BLE001
            print(f'  WARN: could not parse {f}: {exc}')
    return out


# -------------------------------------------------------------------------
# Surface evaluation
# -------------------------------------------------------------------------

def evaluate_surface(surface: dict, artifacts: Path) -> dict:
    """Evaluate one config surface against its artifacts."""
    name = surface['name']
    threshold = int(surface.get('threshold', 2))
    axes = surface['axes']
    metric_path = surface.get('metric_path', '')
    entity_id_path = surface.get('entity_id_path', '')
    artifact_filename = surface.get('artifact_filename', '')

    loaded = load_artifacts(artifacts, artifact_filename)
    entities: list[dict] = []
    for src, data in loaded:
        metric_obj = get_path(data, metric_path) if metric_path else data
        entity_id = get_path(data, entity_id_path) if entity_id_path else None
        if entity_id is None:
            entity_id = src
        if not isinstance(metric_obj, dict):
            entities.append({
                'entity_id': entity_id, 'source': src,
                'result': {'verdict': 'PASS', 'implausible_count': 0,
                           'axis_count': len(axes), 'threshold': threshold,
                           'implausible_axes': [],
                           'note': f'metric_path {metric_path!r} not an object'},
            })
            continue
        result = evaluate_entity(metric_obj, axes, threshold)
        entities.append({'entity_id': entity_id, 'source': src, 'result': result})

    warned = [e for e in entities if e['result']['verdict'] == 'WARN']
    return {
        'surface': name,
        'entity_type': surface.get('entity_type', ''),
        'threshold': threshold,
        'entities_evaluated': len(entities),
        'entities_warned': len(warned),
        'verdict': 'WARN' if warned else 'PASS',
        'entities': entities,
    }


def run(config: dict, artifacts: Path, only_surface: str | None) -> tuple[int, list[dict]]:
    """Run every (or one) surface. Returns (exit_code, surface_results)."""
    surfaces = config.get('surfaces', [])
    if only_surface:
        surfaces = [s for s in surfaces if s['name'] == only_surface]
        if not surfaces:
            print(f'  ERROR: surface {only_surface!r} not in config')
            return 3, []
    results = [evaluate_surface(s, artifacts) for s in surfaces]
    any_warn = any(r['verdict'] == 'WARN' for r in results)
    return (1 if any_warn else 0), results


def _print_report(results: list[dict]) -> None:
    for r in results:
        print(f"\n  Surface: {r['surface']} ({r['entity_type']}) "
              f"-- threshold {r['threshold']}, "
              f"{r['entities_evaluated']} entit(ies), {r['verdict']}")
        for e in r['entities']:
            res = e['result']
            if res['verdict'] != 'WARN':
                continue
            axes_str = ', '.join(
                f"{a['axis']}={a['value']}({a['reason']})"
                for a in res['implausible_axes'])
            print(f"    WARN  {e['entity_id']} -- "
                  f"{res['implausible_count']}/{res['axis_count']} axes "
                  f"jointly implausible: {axes_str}")


def main() -> int:
    ap = argparse.ArgumentParser(prog='d3-multi-axis-envelope-gate')
    ap.add_argument('--artifacts', required=True,
                    help='a platinum JSON artifact file, or a directory of them')
    ap.add_argument('--config', default=str(_DEFAULT_CONFIG))
    ap.add_argument('--surface', default=None, help='run only this surface')
    ap.add_argument('--report', default=None, help='write a JSON report here')
    args = ap.parse_args()

    print('VALGATE D-3 -- multi-axis envelope-validation sentinel gate '
          '(ADHC_VALGATE.005)')

    try:
        config = json.loads(Path(args.config).read_text(encoding='utf-8'))
    except Exception as exc:  # noqa: BLE001
        print(f'  ERROR: could not load config {args.config}: {exc}')
        return 3

    artifacts = Path(args.artifacts)
    if not artifacts.exists():
        print(f'  ERROR: --artifacts path not found: {artifacts}')
        return 3

    try:
        code, results = run(config, artifacts, args.surface)
    except Exception as exc:  # noqa: BLE001
        print(f'  ERROR: gate internal error: {exc}')
        return 3

    if not results:
        print('  ERROR: no surfaces evaluated')
        return 3

    _print_report(results)

    total_warned = sum(r['entities_warned'] for r in results)
    if code == 1:
        print(f'\n  D-3 VERDICT: WARN -- {total_warned} entit(ies) jointly '
              f'implausible on >= threshold axes. (WARN-class -- surface in a '
              f'session log; does not block.)')
    else:
        print('\n  D-3 VERDICT: PASS -- no entity jointly implausible.')

    if args.report:
        try:
            Path(args.report).write_text(
                json.dumps({'exit_code': code, 'surfaces': results}, indent=2),
                encoding='utf-8')
            print(f'  Report: {args.report}')
        except Exception as exc:  # noqa: BLE001
            print(f'  WARN: could not write report: {exc}')

    return code


if __name__ == '__main__':
    sys.exit(main())
