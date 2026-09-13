"""Validate the new adjudication against the repository schema and full item census."""
import importlib.util
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[4]
HOME = Path(__file__).parent
NEW = 'org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/adjudications/ADJUDICATION_v4.md'
spec = importlib.util.spec_from_file_location('gate', ROOT / '.tools/surprise-row-gate.py')
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)


def read_rows(path):
    records, malformed = gate._rows((ROOT / path).read_text(encoding='utf-8'), path.endswith('.json'))
    assert not malformed, (path, malformed)
    return records


def main():
    rows = read_rows(NEW)
    issues = [v for r in rows for v in gate._check_row(r, 'INVESTIGATION', gate._schema(str(ROOT), 'INVESTIGATION'))]
    assert len(rows) == 29 and not issues, issues
    paths = {NEW}
    for pattern in gate.INVESTIGATION_PATTERNS + gate.ADJUDICATION_PATTERNS + gate.REMEDIATION_PATTERNS:
        found, error = gate._index_paths(str(ROOT), [pattern % 'POSN_ASTTAX'])
        assert found is not None, error
        paths.update(found)
    files, rem_ids = [], []
    ids = []
    for path in sorted(paths):
        records = read_rows(path)
        if gate._kind(path) == 'REMEDIATION':
            rem_ids.extend(r['id'] for r in records)
        else:
            files.append((path, records))
            ids.extend(r['id'] for r in records)
    duplicates = sorted({rid for rid in ids if ids.count(rid) > 1})
    latest, unknown = gate._resolve_latest(files, rem_ids)
    pending = sorted(k for k,v in latest.items() if v == 'UNDER_INVESTIGATION')
    orders = gate._open_tos_for_project(str(ROOT), 'POSN_ASTTAX')
    assert len(latest) == 49 and pending == ['POSN_ASTTAX-Z-W14-S1'], (len(latest), pending)
    assert not unknown and not duplicates, (unknown, duplicates)
    assert latest['POSN_ASTTAX-Z-W4-S2'] == 'GRADUATED'
    assert len(orders[0]) == 4 and orders[1] == 15, orders
    evidence = json.loads((HOME / 'POSN_ASTTAX_ROUND3_CVO_EVIDENCE_20260912_Z.json').read_text())
    assert evidence['summary'] == {'candidate_source_after_carried':11, 'candidate_downloaded_after_raises':11, 'candidate_denominator':11}
    for arm in evidence['generator_arms']:
        if arm['arm'] == 'pinned_source':
            assert abs(arm['readings']['after']['lg'] - arm['input_weight']) < 1e-9
        else:
            assert 'KeyError' in arm['readings']['after']['RAISED']
    controls = {x['scenario']:x for x in evidence['reseed_controls']}
    assert controls['conflict']['rc'] == 3 and controls['conflict']['writes'] == 0
    assert controls['scan_denied']['rc'] == 2 and controls['scan_denied']['writes'] == 0
    assert controls['concurrent_curation']['ACSG_after']['curator_note'] == 'A'
    assert controls['normal']['ACSG_after']['curator_note'] == 'A'
    assert evidence['second_writer']['securities'] == 57 and len(evidence['second_writer']['intersection']) == 4
    # Measure the pending DI refusal using the canonical helper, without staging or minting DI.
    proposed = dict(next(r for r in rows if r.get('adjudicates') == ['POSN_ASTTAX-Z-W14-S1']))
    proposed['disposition'] = 'DECOMP_INVALIDATING'
    refusal = gate._route_precondition_violations(str(ROOT), NEW, proposed, 'POSN_ASTTAX', route_word='disposition=DECOMP_INVALIDATING (CVO read-only proposed-disposition check)')
    assert refusal, 'Expected terminality refusal is missing; reassess before publishing a hold'
    result = {'head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
              'rows':len(rows),'issues':issues,'originals':len(latest),'pending_originals':pending,
              'unknown_targets':unknown,'duplicate_ids':duplicates,'orders':orders,
              'proposed_di_refusal':refusal,'offline_control_assertions':'PASS',
              'limits':'Prospective working-file census; safe-commit enforces the actual index. No L10 carrier and no override.'}
    (HOME / 'POSN_ASTTAX_ROUND3_CVO_VALIDATION_20260912_Z.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
