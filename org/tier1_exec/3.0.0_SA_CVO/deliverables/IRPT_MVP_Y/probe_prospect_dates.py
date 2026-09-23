"""Pinned retained-source to Entry date wires; offline only, no vendor certification."""
import argparse
import copy
import hashlib
import io
import json
import os
from pathlib import Path
import socket
import subprocess
import sys
import zipfile

import jsonschema
from probe_recipe_decimal import deny_network, load


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--pin', default='f4f16b283f')
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[5]
    pin = subprocess.check_output(['git', 'rev-parse', args.pin], cwd=root, text=True).strip()
    target = root / '.runtime/codex-seats/3.0.0_SA_CVO~Y/prospect-date-review' / pin
    target.mkdir(parents=True, exist_ok=True)
    prefix = 'infra/aws/lambda/investor-reporting'
    archive = subprocess.check_output(['git', 'archive', '--format=zip', pin, prefix,
        'docs/contracts/investor-reporting', 'data/firm_registry.json'], cwd=root)
    hashes = {}
    with zipfile.ZipFile(io.BytesIO(archive)) as bundle:
        for member in bundle.infolist():
            path = (target / member.filename).resolve()
            if not path.is_relative_to(target.resolve()):
                raise ValueError('snapshot escape')
            if member.is_dir():
                path.mkdir(parents=True, exist_ok=True)
            else:
                data = bundle.read(member)
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(data)
                hashes[member.filename] = hashlib.sha256(data).hexdigest()
    socket.socket.connect = deny_network
    socket.socket.connect_ex = deny_network
    socket.create_connection = deny_network
    os.environ['IRPT_FIRM_REGISTRY'] = str(target / 'data/firm_registry.json')
    source = target / prefix
    sys.path.insert(0, str(source / 'ops/tests'))
    subject = load('prospect_date_source_tests', source / 'ops/tests/test_prospect_dates.py')
    results, wires, bad_wires = [], {}, {}
    validator = jsonschema.Draft202012Validator(subject.PUBLIC, format_checker=jsonschema.FormatChecker())

    def world(csv=None):
        w = subject.world.__wrapped__(subject.retention_world.__wrapped__())
        if csv is not None:
            original = w.case.create
            w.case.create = lambda: original(subject.support.support.support.upload_tests.payload(csv))
        return subject.report_world.__wrapped__(w)

    def record(name, passed, **detail):
        results.append(dict(name=name, outcome='PASS' if passed else 'FAIL', **detail))

    def call(r, extra=None):
        return subject.boundary.call(r, 'status', headers={**r.w.case.headers,
            **({'x-irpt-status-dates': 'prospect-v1'} if extra is None else extra)})

    cases = [('undated', [], ['undated-one', 'undated-two'], 'UNDATED_INPUT'),
             ('empty', [], [], 'UNDATED_INPUT'),
             ('per_section', [('one', '2024-02-29'), ('two', '2026-09-02')], [], 'PER_SECTION'),
             ('mixed', [('one', '2026-09-01')], ['undated-one'], 'PER_SECTION'),
             ('single_date', [('one', '2026-09-01'), ('two', '2026-09-01')], [], None)]
    for name, dated, undated, basis in cases:
        r = world()
        subject.publish(r, dated, undated)
        value = call(r)
        wires[name] = value
        data = value.get('data', {})
        expected = ([{'section_id': key, 'as_of_date': day} for key, day in dated]
                    + [{'section_id': key, 'as_of_date': None} for key in undated])
        sd = data.get('source_dates', {})
        errors = [e.message for e in validator.iter_errors(data)]
        bound = sd.get('prospect_analysis', {})
        record(name + '_actual_Entry_public_schema_and_exact_dates', not errors and data.get('state') == 'READY'
               and (sd == {'business_date': '2026-09-01'} if basis is None else
                    sd.get('date_basis') == basis and sd.get('section_dates') == expected
                    and 'business_date' not in sd and bound.get('request_id') == r.id
                    and bound.get('report_revision') == r.detail['revision']
                    and bound.get('report_id') == r.detail['report_id']
                    and bound.get('input_id') == 'portfolio_' + bound.get('content_sha256', '')),
               schema_errors=errors)
        before = copy.deepcopy(data)
        r.w.state.now += 100
        value2 = call(r)['data']
        record(name + '_reconstructed_reader_advanced_clock_same_source_facts', value2 == before)

    for name, header in [('old_consumer', {}), ('unknown_capability', {'x-irpt-status-dates': 'prospect-v2'}),
                         ('duplicate_capability', {'x-irpt-status-dates': 'prospect-v1', 'X-IRPT-Status-Dates': 'prospect-v1'}),
                         ('comma_capability', {'x-irpt-status-dates': 'prospect-v1,prospect-v1'})]:
        r = world()
        value = call(r, header)
        wires[name] = value
        record(name + '_no_extension', value.get('data', {}).get('state') == 'UNAVAILABLE'
               and value['data']['source_dates'] == {} and not list(validator.iter_errors(value['data'])))

    for name, csv in [('date_column', 'Ticker,Market Value,Currency,Date\nAAPL,12.03,USD,2026-09-01\n'),
                      ('notes', 'Ticker,Market Value,Currency,Notes\nAAPL,12.03,USD,Date unknown\n'),
                      ('preamble', 'As of 2026-09-01\nTicker,Market Value,Currency\nAAPL,12.03,USD\n')]:
        r = world(csv)
        value = call(r)
        wires[name] = value
        record(name + '_unknown_source_stays_unavailable', value.get('data', {}).get('state') == 'UNAVAILABLE'
               and value['data']['source_dates'] == {})

    for name, mutate in [('missing_original_index', lambda row: None),
                         ('original_source_hash', lambda row: dict(row, content_sha256='0' * 64)),
                         ('original_owner', lambda row: dict(row, owner=dict(row['owner'], principal_id='other')))]:
        r = world()
        previous = r.requests.artifacts.index.get
        def get(tenant, key):
            value = previous(tenant, key)
            return mutate(value) if key.startswith('UPLOAD#') else value
        r.requests.artifacts.index.get = get
        value = call(r)
        record(name + '_refuses_not_undated', 'data' not in value, response=value)

    for name in ('expiry', 'access', 'original_index', 'job_receipt'):
        r = world()
        retained = r.w.stores.retention.require_live(r.w.case.principal, r.record['composition_ref']['retention_ref'])
        original = r.reader.read
        def after_report(*args):
            result = original(*args)
            if name == 'expiry':
                r.w.state.now = retained['expires_at']
            elif name == 'access':
                r.requests.authorize_current = lambda *_: False
            elif name == 'original_index':
                for (_, key), row in r.w.table.rows.items():
                    if key.startswith('UPLOAD#'):
                        row['content_sha256'] = '0' * 64
            else:
                r.job['job_detail']['S'] = json.dumps(dict(r.detail, certification_sha256='e' * 64))
            return result
        r.reader.read = after_report
        value = call(r)
        record(name + '_after_all_source_and_report_bytes_refuses', 'data' not in value, response=value)

    for name, dated, undated in [('duplicate', [('same', '2026-09-01')], ['same']),
                                ('invalid_date', [('bad', '2026-02-29')], []),
                                ('too_many', [], ['s' + str(n) for n in range(1001)])]:
        r = world()
        subject.publish(r, dated, undated)
        value = call(r)
        record(name + '_section_census_refuses', 'data' not in value, response=value)

    r = world()
    subject.publish(r, [], ['s' + str(n) for n in range(1000)])
    value = call(r)
    record('exact_1000_section_boundary_retained', len(value.get('data', {}).get('source_dates', {}).get('section_dates', [])) == 1000)

    for phase in ('RECEIVED', 'CERTIFYING', 'FAILED', 'UNCERTAIN'):
        r = world()
        r.job['state']['S'] = phase
        r.reader.read = deny_network
        value = call(r)
        wires['phase_' + phase] = value
        record(phase + '_opt_in_never_overrides_phase_or_reads_report', value.get('data', {}).get('state') != 'READY'
               and value['data']['source_dates'] == {})

    r = world()
    r.job['job_detail']['S'] = json.dumps(dict(r.detail, certification_sha256=int('1' * 64)))
    r.reader.reports.get = deny_network
    value = call(r)
    record('malformed_READY_report_receipt_cannot_release_dates', 'data' not in value, response=value)

    # Same regenerated data crosses both the runtime validator and paired browser parser.
    changes = {
        'wrong_operation': lambda v: v['operation'].update(operation_kind='holdings_snapshot'),
        'wrong_request': lambda v: v['operation'].update(operation_id='REQ-' + 'f' * 24),
        'wrong_input': lambda v: v['source_dates']['prospect_analysis'].update(input_id='portfolio_' + 'f' * 64),
        'mutable': lambda v: v['source_dates']['prospect_analysis'].update(immutable=False),
        'unknown_basis': lambda v: v['source_dates'].update(date_basis='UNKNOWN'),
        'null_business_date': lambda v: v['source_dates'].update(business_date=None),
        'duplicate_sections': lambda v: v['source_dates']['section_dates'].append(copy.deepcopy(v['source_dates']['section_dates'][0])),
        'bad_calendar': lambda v: v['source_dates']['section_dates'][0].update(as_of_date='2026-02-30'),
        'unknown_source_field': lambda v: v['source_dates'].update(today='2026-09-22'),
        'missing_binding': lambda v: v['source_dates'].pop('prospect_analysis'),
    }
    for name, change in changes.items():
        value = copy.deepcopy(wires['mixed']['data'])
        change(value)
        bad_wires[name] = value
        internal = dict(value, internal_correlation_id='offline-review')
        record(name + '_runtime_wire_binding_refuses', bool(subject.status.validate_envelope(internal)),
               schema_rejects=bool(list(validator.iter_errors(value))))

    fixture = source / 'ops/tests/fixtures/prospect_status_dates.json'
    fixture_before = fixture.read_bytes()
    paths = ['test_prospect_dates.py', 'test_owned_entry.py', 'test_owned_report.py']
    command = ('import socket,pytest; '
        'deny=lambda *a,**k: (_ for _ in ()).throw(AssertionError("NETWORK_FORBIDDEN")); '
        'socket.socket.connect=deny; socket.socket.connect_ex=deny; socket.create_connection=deny; '
        'raise SystemExit(pytest.main(' + repr(['-q'] + [str(source / 'ops/tests' / p) for p in paths]) + '))')
    environment = dict(os.environ, IRPT_REGENERATE_DATE_WIRES='1')
    suite = subprocess.run([sys.executable, '-c', command], cwd=root, env=environment, capture_output=True, text=True)
    record('supplied_actual_Entry_fixture_regenerates_exact_bytes', fixture.read_bytes() == fixture_before)
    evidence = dict(pin=pin, source_sha256=hashes, controls=results, wires=wires, malformed_wires=bad_wires,
        supplied=dict(returncode=suite.returncode, stdout=suite.stdout, stderr=suite.stderr),
        limitations=['Synthetic reports, offline retained storage/current policy/clock',
                     'No vendor certification, runtime package, real browser, deployment or integrated criterion grade'])
    args.output.write_text(json.dumps(evidence, indent=2) + '\n', encoding='utf-8')
    print(suite.stdout)
    print(json.dumps(dict(count=len(results), failures=[r for r in results if r['outcome'] != 'PASS']), indent=2))
    return int(suite.returncode != 0 or any(r['outcome'] != 'PASS' for r in results))


if __name__ == '__main__':
    raise SystemExit(main())
