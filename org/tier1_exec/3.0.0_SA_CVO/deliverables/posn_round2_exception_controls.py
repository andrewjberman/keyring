"""Exercise the authorized exception and refusal boundaries without changing git or orders."""
import copy
import importlib.util
import json
from pathlib import Path
import re
import subprocess
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[4]


def main():
    spec = importlib.util.spec_from_file_location('rowgate', ROOT / '.tools/surprise-row-gate.py')
    gate = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(gate)
    record = json.loads((ROOT / gate.POSN_R2_EXCEPTION_PATH).read_text(encoding='utf-8'))
    opened = gate._open_tos_for_project(str(ROOT), 'POSN_ASTTAX')
    results = []
    for item in record['rows']:
        text = (ROOT / item['path']).read_text(encoding='utf-8')
        rows = json.loads(re.search(r'```json\s*(.*?)```', text, re.S).group(1))
        row = next(r for r in rows if r['id'] == item['id'])
        violations = gate._route_precondition_violations(
            str(ROOT), item['path'], row, 'POSN_ASTTAX', open_tos=opened)
        assert not violations, violations
        results.append({'case': 'authorized ' + item['path'] + '#' + row['id'], 'passed': True})
    rel = item['path']

    def refused(label, candidate=None, path=rel, code='POSN_ASTTAX', orders=opened):
        violations = gate._route_precondition_violations(
            str(ROOT), path, candidate or row, code, open_tos=orders)
        assert violations, label
        results.append({'case': label, 'passed': True, 'refusal': violations})

    changed = copy.deepcopy(row)
    changed['remedy'] += ' UNAUTHORIZED WIDENING'
    refused('changed row content', changed)
    changed = copy.deepcopy(row)
    changed['id'] = 'POSN_ASTTAX-Z-C-S999'
    refused('unlisted row id', changed)
    refused('another round file', path=rel.replace('REMEDIATION_v2', 'REMEDIATION_v3'))
    refused('another project', code='AMGT_RESAPP')
    refused('extra open order', orders=(opened[0] + ['EXTRA [staged]'], 9, ''))
    refused('one named order changed status', orders=(opened[0][:1], 8, ''))
    refused('census failed', orders=(None, 0, 'injected unreadable census'))
    real_blob = gate._blob

    def missing_authority(root, pin, path):
        if path == gate.POSN_R2_EXCEPTION_PATH:
            return 'ABSENT', None
        return real_blob(root, pin, path)

    with patch.object(gate, '_blob', side_effect=missing_authority):
        refused('authorization pin unavailable')

    def changed_order(root, pin, path):
        state, text = real_blob(root, pin, path)
        if pin == 'HEAD' and path == record['orders'][0]['path']:
            return state, text + '\nUNREVIEWED ORDER CHANGE\n'
        return state, text

    with patch.object(gate, '_blob', side_effect=changed_order):
        refused('named order content changed')
    ordinary = gate._route_precondition_violations(
        str(ROOT), rel, row, 'OTHER_PROJECT', open_tos=([], 1, ''))
    assert not ordinary
    results.append({'case': 'ordinary terminal-only case still passes', 'passed': True})
    unresolved = ({'POSN_ASTTAX-Z-W8-S2': 'UNDER_INVESTIGATION'}, [], 1, '')
    twin = gate._investigations_precondition_violations(rel, row, 'POSN_ASTTAX', 'slug', unresolved)
    assert twin and 'NOT dispositioned' in twin[0]
    results.append({'case': 'independent investigation-completion gate still refuses', 'passed': True, 'refusal': twin})
    output = {'authority_pin': gate.POSN_R2_EXCEPTION_PIN,
              'head': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
              'controls': results, 'count': len(results),
              'scope': 'Read-only production predicate calls. Mutated inputs are in memory; no index, task order, gate environment or service was changed.'}
    Path(__file__).with_name('POSN_ROUND2_EXCEPTION_CONTROLS_20260911_Z.json').write_text(
        json.dumps(output, indent=2) + '\n', encoding='utf-8')
    print('PASS:', len(results), 'controls; 19 authorized row cases plus 11 boundary/control cases')


if __name__ == '__main__':
    main()
