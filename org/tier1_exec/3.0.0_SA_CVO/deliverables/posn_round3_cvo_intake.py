"""Read the drained POSN round-3 artifacts without changing orders or the retained scratch tree."""
import datetime
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[4]
HOME = Path(__file__).parent
PROJECT = 'org/missions/D4/POSN/POSN_ASTTAX'


def run(args):
    p = subprocess.run(args, cwd=ROOT, capture_output=True, text=True, encoding='utf-8', errors='replace')
    return {'rc': p.returncode, 'stdout': p.stdout, 'stderr': p.stderr}


def main():
    spec = importlib.util.spec_from_file_location('gate', ROOT / '.tools/surprise-row-gate.py')
    gate = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(gate)
    latest, unknown, count, note = gate._latest_dispositions(str(ROOT), 'POSN_ASTTAX')
    paths, err = gate._index_paths(str(ROOT), [p % 'POSN_ASTTAX' for p in gate.INVESTIGATION_PATTERNS])
    assert paths is not None, err
    originals = []
    for path in paths:
        records, bad = gate._rows((ROOT / path).read_text(encoding='utf-8'), path.endswith('.json'))
        assert not bad
        originals.extend({'path': path, 'row': r} for r in records)
    evidence = {'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'head': run(['git', 'rev-parse', 'HEAD']),
                'orders': gate._open_tos_for_project(str(ROOT), 'POSN_ASTTAX'),
                'latest_dispositions': latest, 'unknown': unknown, 'documents_read': count, 'census_note': note,
                'new_originals': [r for r in originals if latest[r['row']['id']] == 'UNDER_INVESTIGATION'], 'proofs': []}
    tracked = run(['git', 'ls-files', PROJECT + '/deliverables/*/*.proof_of_spec.json'])['stdout'].splitlines()
    for path in tracked:
        data = json.loads((ROOT / path).read_text(encoding='utf-8'))
        if '.TO-T' not in data.get('to_id', ''):
            continue
        to_path = PROJECT + '/task-orders/' + Path(path).name.replace('.proof_of_spec.json', '.md')
        expected_ids = re.findall(r'<criterion\s+id="([^"]+)"', (ROOT / to_path).read_text(encoding='utf-8'))
        assert expected_ids, to_path
        expected = ','.join(expected_ids)
        evidence['proofs'].append({'path': path, 'proof': data, 'commit': run(['git', 'log', '-1', '--format=%H', '--', path]),
           'to_path': to_path, 'expected_from_issued_to': expected_ids,
           'structure': run([sys.executable, '.tools/proof-of-spec-check.py', path, expected])})
    evidence['instrument_correction'] = 'Initial CVO intake used id instead of criterion_id and stopped before checking any proof. Final expected IDs are read independently from each issued TO, not mirrored from its proof.'
    out = HOME / 'POSN_ASTTAX_ROUND3_CVO_INTAKE_20260912_Z.json'
    out.write_text(json.dumps(evidence, indent=2, ensure_ascii=True) + '\n', encoding='utf-8')
    print(json.dumps({'originals': len(latest), 'new': [x['row']['id'] for x in evidence['new_originals']],
      'orders': evidence['orders'], 'proofs': [{'path': p['path'], 'keys': list(p['proof']['acceptance'][0]), 'check_rc': p['structure']['rc']} for p in evidence['proofs']]}))


if __name__ == '__main__':
    main()
