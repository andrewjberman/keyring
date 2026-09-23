"""Independent pinned actual Entry/event controls; offline storage and policy fixtures."""
import argparse
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
    parser.add_argument('--pin', default='8e8498c9c0')
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[5]
    pin = subprocess.check_output(['git', 'rev-parse', args.pin], cwd=root, text=True).strip()
    target = root / '.runtime/codex-seats/3.0.0_SA_CVO~Y/owned-entry-review' / pin
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
    subject = load('owned_entry_source_tests', source / 'ops/tests/test_owned_entry.py')
    results, responses = [], {}

    def world():
        w = subject.world.__wrapped__(subject.retention_world.__wrapped__())
        return subject.report_world.__wrapped__(w)

    def record(name, passed, **observed):
        results.append(dict(name=name, outcome='PASS' if passed else 'FAIL', **observed))

    for kind in subject.ROUTES:
        r = world()
        value = subject.call(r, kind)
        responses[kind] = value
        data = value.get('data')
        if kind == 'history':
            expected = {'items': [r.requests._public(r.record)], 'next_cursor': None}
        elif kind == 'read':
            expected = r.requests._public(r.record)
        elif kind == 'sections':
            expected = {key: r.report[key] for key in ('request_ref', 'sections', 'extraction_validation')}
        else:
            expected = data
        record('actual_event_' + kind + '_positive_projection', data is not None and data == expected
               and value['firm_id'].startswith('fir_'), response=value)

    # Resolve the exact data schema's local report pointers without remote fetching.
    schemas = target / 'docs/contracts/investor-reporting/v1'
    report_schema = json.loads((schemas / 'AnalysisReport.schema.json').read_text())
    sections_schema = json.loads((schemas / 'responses/analysis-report.response.schema.json').read_text())['properties']['data']
    for key, ref in sections_schema['properties'].items():
        assert ref == {'$ref': '../AnalysisReport.schema.json#/properties/' + key}
        sections_schema['properties'][key] = report_schema['properties'][key]
    errors = list(jsonschema.Draft202012Validator(sections_schema).iter_errors(responses['sections']['data']))
    record('actual_event_sections_closed_data_schema', not errors, errors=[e.message for e in errors])

    # Explicit expected phases, independent of the implementation's PHASES constant.
    phases = [('RECEIVED', 'QUEUED'), ('CLAIMED', 'RUNNING'), ('SUBMITTING', 'RUNNING'),
              ('SUBMITTED', 'RUNNING'), ('DOWNLOADING', 'RUNNING'), ('EXTRACTING', 'RUNNING'),
              ('CERTIFYING', 'RUNNING'), ('FAILED', 'FAILED'), ('UNCERTAIN', 'UNAVAILABLE'),
              ('ATTENTION', 'UNAVAILABLE'), ('READY', 'UNAVAILABLE')]
    for phase, public_state in phases:
        r = world()
        r.job['state']['S'] = phase
        reads = []
        original_read = r.reader.read
        def read(*args):
            reads.append(True)
            return original_read(*args)
        r.reader.read = read
        value = subject.call(r, 'status')
        data = value.get('data', {})
        expected_actions = ['WAIT'] if public_state in ('QUEUED', 'RUNNING') else []
        record('actual_status_phase_' + phase,
               data.get('state') == public_state and data.get('source_dates') == {}
               and [a['action'] for a in data.get('actions', [])] == expected_actions
               and all(a['safe'] is True for a in data.get('actions', []))
               and 'internal_correlation_id' not in data and len(reads) == int(phase == 'READY'),
               response=value, accepted_report_reads=len(reads), job_reads=len(r.calls))

    for bad in ('UNKNOWN', ''):
        r = world()
        r.job['state']['S'] = bad
        value = subject.call(r, 'status')
        record('invalid_phase_' + repr(bad), 'data' not in value, response=value)

    for kind in ('sections', 'status'):
        r = world()
        r.job['job_detail']['S'] = json.dumps(dict(r.detail, certification_sha256=int('1' * 64)))
        r.reader.reports.get = deny_network
        value = subject.call(r, kind)
        record(kind + '_malformed_READY_receipt_refuses_before_report_fetch', 'data' not in value, response=value)

        r = world()
        retained = r.w.stores.retention.require_live(r.w.case.principal, r.record['composition_ref']['retention_ref'])
        subject.support.after_report_blob(r, lambda: setattr(r.w.state, 'now', retained['expires_at']))
        value = subject.call(r, kind)
        record(kind + '_expiry_after_report_blob_refuses', 'data' not in value, response=value)

        r = world()
        subject.support.after_report_blob(r, lambda: setattr(r.requests, 'authorize_current', lambda *_: False))
        value = subject.call(r, kind)
        record(kind + '_authorization_loss_after_report_blob_refuses', 'data' not in value, response=value)

    # Record-authorizer fixture changes are distinct from Entry's copied request claims.
    # History has no single retained-record callback at Entry; its service owns per-item checks.
    boundary_observations = []
    for kind, obj_name, method in (('history', 'requests', 'history'), ('read', 'requests', 'read'),
                                  ('sections', 'reader', 'sections'), ('status', 'reader', 'read')):
        r = world()
        obj = getattr(r, obj_name)
        original = getattr(obj, method)
        def revoke(*args, **kwargs):
            result = original(*args, **kwargs)
            r.w.case.headers['x-user-email'] = 'revoked@example.invalid'
            return result
        setattr(obj, method, revoke)
        value = subject.call(r, kind)
        if kind == 'history':
            boundary_observations.append(dict(name='history_authorizer_fixture_changed_after_service_return',
                returned_data='data' in value, response=value,
                limit='No per-item authorization repeated by history Entry after service returns; '
                      'fixture mutation does not change Entry copied request claims.'))
        else:
            record(kind + '_record_authorizer_change_after_service_refuses', 'data' not in value, response=value)

    for kind in subject.ROUTES:
        r = world()
        boundary = subject.entry.build_owned_entry(requests=r.requests, reports=r.reader)
        route = subject.ROUTES[kind]
        operation = boundary.routes[route]
        original_compute = boundary.operations[operation]
        def change_actual_claims(request, scope, event, ctx):
            result = original_compute(request, scope, event, ctx)
            request.headers['x-user-email'] = 'changed-at-entry@example.invalid'
            return result
        boundary.operations[operation] = change_actual_claims
        event = {'routeKey': route, 'headers': dict(r.w.case.headers),
                 'pathParameters': {} if kind == 'history' else
                    {'requestId' if kind == 'read' else 'jobId': r.id}}
        value = subject.entry._entry.lambda_entry(boundary)(event)
        record(kind + '_actual_Entry_claim_change_after_compute_refuses', 'data' not in value, response=value)

    for kind, method in (('read', 'read'), ('sections', 'sections')):
        r = world()
        obj = r.requests if kind == 'read' else r.reader
        original = getattr(obj, method)
        def owner_change(*args, **kwargs):
            result = original(*args, **kwargs)
            key = next(iter(r.client.rows))
            row = json.loads(r.client.rows[key]['record']['S'])
            row['owner']['prospect_input_id'] = 'different-full-owner'
            r.client.rows[key]['record']['S'] = json.dumps(row)
            return result
        setattr(obj, method, owner_change)
        value = subject.call(r, kind)
        record(kind + '_full_owner_change_after_compute_refuses', 'data' not in value, response=value)

    for kind in ('read', 'sections', 'status'):
        r = world()
        r.w.case.s3.on_get = deny_network
        value = subject.call(r, kind, queryStringParameters={'account_ids': 'injected'})
        record(kind + '_unexpected_query_zero_job_and_blob', 'data' not in value and not r.calls, response=value)

    for kind in subject.ROUTES:
        r = world()
        r.w.case.s3.on_get = deny_network
        headers = dict(r.w.case.headers, **{'x-contract-version': 'v999'})
        value = subject.call(r, kind, headers=headers)
        record(kind + '_unsupported_contract_before_reads', 'data' not in value and not r.calls and not r.client.queries,
               response=value)

    r = world()
    headers = dict(r.w.case.headers, **{'x-user-email': 'other@example.invalid'})
    value = subject.call(r, 'history', headers=headers, queryStringParameters={'limit': '1'})
    record('history_other_principal_has_empty_page', value.get('data') == {'items': [], 'next_cursor': None}, response=value)

    r = world()
    boundary = subject.entry.build_owned_entry(requests=r.requests, reports=r.reader)
    record('summary_and_module_default_remain_unchanged',
           boundary.operations['status-summary'] is subject.entry.ENTRY.operations['status-summary']
           and 'status-summary' not in boundary.owner_read_modes
           and not subject.entry.ENTRY.owner_read_modes
           and subject.ROUTES['history'] not in subject.entry.ENTRY.routes)

    # Raw repository schemas include server-only fields; report observations separately,
    # not as a claim that this uninstalled factory has an agreed public wire contract.
    schema_observations = {}
    for kind, name in [('status', 'status-job'), ('sections', 'analysis-report')]:
        schema = json.loads((schemas / ('responses/' + name + '.response.schema.json')).read_text())
        data_schema = sections_schema if kind == 'sections' else json.loads((schemas / 'StatusEnvelope.schema.json').read_text())
        schema['properties']['data'] = data_schema
        schema['properties']['firm_id'] = {'type': 'string', 'pattern': '^fir_[a-f0-9]{24}$'}
        errors = list(jsonschema.Draft202012Validator(schema).iter_errors(responses[kind]))
        schema_observations[kind] = [dict(path=list(e.path), message=e.message) for e in errors]

    command = ('import socket,pytest; '
               'deny=lambda *a,**k: (_ for _ in ()).throw(AssertionError("NETWORK_FORBIDDEN")); '
               'socket.socket.connect=deny; socket.socket.connect_ex=deny; socket.create_connection=deny; '
               'raise SystemExit(pytest.main(' + repr(['-q', str(source / 'ops/tests/test_owned_entry.py')]) + '))')
    suite = subprocess.run([sys.executable, '-c', command], cwd=root, capture_output=True, text=True)
    args.output.write_text(json.dumps(dict(pin=pin, source_sha256=hashes, controls=results,
        raw_response_schema_observations=schema_observations, boundary_observations=boundary_observations,
        supplied=dict(returncode=suite.returncode, stdout=suite.stdout, stderr=suite.stderr),
        limitations=['Offline synthetic retained report/storage/clock/current ACTIVE policy fixtures',
                     'Factory explicitly uninstalled; no package, HTTP, browser, vendor, IAM or live proof',
                     'Raw source schemas are not an independently agreed public generated schema',
                     'No new date basis wire emitted or accepted; no integrated criterion grade']), indent=2) + '\n', encoding='utf-8')
    print(suite.stdout)
    print(json.dumps(dict(control_count=len(results),
        failures=[r for r in results if r['outcome'] != 'PASS'],
        raw_response_schema_observations=schema_observations,
        boundary_observations=boundary_observations), indent=2))
    return int(suite.returncode != 0 or any(row['outcome'] != 'PASS' for row in results))


if __name__ == '__main__':
    raise SystemExit(main())
