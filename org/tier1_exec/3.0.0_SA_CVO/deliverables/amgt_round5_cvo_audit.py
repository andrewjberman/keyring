"""Read-only round-5 census and proof validation; writes only its own evidence file."""
import datetime
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[4]
PROJECT = ROOT / 'org/missions/D5/AMGT/AMGT_RESAPP'
OUTPUT = Path(__file__).with_name('AMGT_RESAPP_ROUND5_CVO_EVIDENCE_20260911_Z.json')


def run(argv):
    p = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True,
                       encoding='utf-8', errors='replace', timeout=110)
    return {'argv': argv, 'rc': p.returncode, 'stdout': p.stdout, 'stderr': p.stderr}


def rows(path):
    result = []
    for block in re.findall(r'```json\s*(.*?)```', path.read_text(encoding='utf-8'), re.S):
        value = json.loads(block)
        result.extend(value if isinstance(value, list) else [value])
    return result


def fingerprint(path):
    return {'path': path.relative_to(ROOT).as_posix(),
            'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}


def expected_ids(order_text):
    match = re.search(r'^\s*<proof_of_spec>\s*$\n(.*?)^\s*</proof_of_spec>\s*$',
                      order_text, re.S | re.M)
    return re.findall(r'<criterion\s+id="([^"]+)"', match.group(1)) if match else []


def main():
    if '--repair-expectations' in sys.argv:
        out = json.loads(OUTPUT.read_text(encoding='utf-8'))
        out['instrument_correction'] = 'Initial expected-ID lookup used spec_ref.doc, which names the PRD rather than the governing TO in four historical instances. This produced an erroneous empty expected set. An attempted regex-only repair still refused; inspecting both references identified the cause. Corrected to decomp_ref.to_ref, with standalone XML tags; only those four checks rerun. Initial results retained.'
        for item in out['proofs']:
            if item['expected_ids']:
                continue
            path = ROOT / item['path']
            doc = json.loads(path.read_text(encoding='utf-8'))
            ids = expected_ids((ROOT / doc['decomp_ref']['to_ref']).read_text(encoding='utf-8'))
            if not ids:
                raise ValueError('No criterion IDs recovered: ' + str(path))
            item['initial_instrument_error'] = item['check']
            item['expected_ids'] = ids
            item['check'] = run([sys.executable, '.tools/proof-of-spec-check.py', str(path), ','.join(ids)])
        OUTPUT.write_text(json.dumps(out, indent=2, ensure_ascii=True) + '\n', encoding='utf-8')
        print(json.dumps({'proofs': len(out['proofs']), 'invalid': [p['path'] for p in out['proofs'] if p['check']['rc']]}))
        return
    out = {'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
           'serial': '3.0.0_SA_CVO~Z', 'head_start': run(['git', 'rev-parse', 'HEAD']),
           'scope': 'Repository evidence; no AWS write, vendor call, deploy or portal mutation.'}
    channel = PROJECT / 'surprise-channel'
    investigations = rows(channel / 'investigations/INVESTIGATION_v1.md')
    latest = {}
    for path in sorted((channel / 'adjudications').glob('*.md')):
        for row in rows(path):
            for target in row.get('adjudicates', []):
                latest[target] = {'row': row['id'], 'disposition': row['disposition'],
                                  'file': path.relative_to(ROOT).as_posix()}
    out['intake'] = {'investigation_count': len(investigations),
                     'latest': {r['id']: latest.get(r['id']) for r in investigations},
                     'new_ids': [r['id'] for r in investigations if r['id'] not in latest]}
    out['orders'] = []
    for path in sorted((PROJECT / 'task-orders').glob('*.md')):
        text = path.read_text(encoding='utf-8')
        out['orders'].append({**fingerprint(path),
                              'status': re.findall(r'<status>(.*?)</status>', text),
                              'round': re.findall(r'<round>(.*?)</round>', text)})
    out['proofs'] = []
    for path in sorted((PROJECT / 'deliverables').glob('*/*.proof_of_spec.json')):
        doc = json.loads(path.read_text(encoding='utf-8'))
        order = ROOT / doc['decomp_ref']['to_ref']
        order_text = order.read_text(encoding='utf-8')
        expected = expected_ids(order_text)
        result = run([sys.executable, '.tools/proof-of-spec-check.py', str(path), ','.join(expected)])
        out['proofs'].append({**fingerprint(path), 'to_id': doc['to_id'],
                              'last_commit': run(['git', 'log', '-1', '--format=%H', '--', str(path)]),
                              'expected_ids': expected, 'check': result})
    out['portal_pin'] = run(['git', '-C', 'portal', 'rev-parse', 'e6057f26^{commit}'])
    out['portal_branch'] = run(['git', '-C', 'portal', 'rev-parse', 'wk-amgt_resapp-5-8-portal'])
    out['recorded_gitlink'] = run(['git', 'ls-tree', 'HEAD', 'portal'])
    out['portal_negative_control'] = run(['git', '-C', 'portal', 'cat-file', '-t', '0000000000000000000000000000000000000001'])
    out['head_end'] = run(['git', 'rev-parse', 'HEAD'])
    OUTPUT.write_text(json.dumps(out, indent=2, ensure_ascii=True) + '\n', encoding='utf-8')
    print(json.dumps({'evidence': str(OUTPUT), 'investigations': len(investigations),
                      'new': len(out['intake']['new_ids']), 'proofs': len(out['proofs']),
                      'invalid': [{'path': p['path'], 'output': p['check']} for p in out['proofs'] if p['check']['rc']],
                      'orders': len(out['orders'])}, ensure_ascii=True))


if __name__ == '__main__':
    main()
