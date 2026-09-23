"""Actual Entry outer fixtures, exact closed-schema negatives and public-field conflict."""
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

from probe_recipe_decimal import deny_network, load


def main():
    root = Path(__file__).resolve().parents[5]
    own = Path(__file__).resolve().parent
    repo = Path('C:/Users/AndrewBerman/Desktop/irpt-mvp-p-20260922')
    pin = subprocess.check_output(['git', 'rev-parse', '7915bc9b2c'], cwd=repo, text=True).strip()
    target = root / '.runtime/codex-seats/3.0.0_SA_CVO~Y/outer-pair-backend' / pin
    target.mkdir(parents=True, exist_ok=True)
    prefix = 'infra/aws/lambda/investor-reporting'
    raw = subprocess.check_output(['git', 'archive', '--format=zip', pin, prefix,
        'docs/contracts/investor-reporting', 'data/firm_registry.json'], cwd=repo)
    hashes = {}
    with zipfile.ZipFile(io.BytesIO(raw)) as bundle:
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
    source_test = target / prefix / '_contracts/test_owned_outer_contracts.py'
    outer = own / 'OUTER_PAIR_7915_OUTER.json'
    dates = own / 'OUTER_PAIR_7915_DATES.json'
    environment = dict(os.environ, IRPT_WRITE_OWNED_OUTER_FIXTURE=str(outer),
                       IRPT_WRITE_OWNED_DATE_OUTER_FIXTURE=str(dates))
    command = ('import socket,pytest; '
        'deny=lambda *a,**k: (_ for _ in ()).throw(AssertionError("NETWORK_FORBIDDEN")); '
        'socket.socket.connect=deny; socket.socket.connect_ex=deny; socket.create_connection=deny; '
        'raise SystemExit(pytest.main(' + repr(['-q', str(source_test)]) + '))')
    suite = subprocess.run([sys.executable, '-c', command], cwd=root, env=environment, capture_output=True, text=True)
    if suite.returncode:
        print(suite.stdout, suite.stderr)
        return suite.returncode
    subject = load('outer_contract_source_tests', source_test)
    base = target / 'docs/contracts/investor-reporting/v1'
    public = subject.validator(base / 'PublicStatusEnvelope.schema.json')
    internal_doc = json.loads((base / 'StatusEnvelope.schema.json').read_text())
    server_only = {key for key, value in internal_doc['properties'].items() if value.get('x-server-only')}
    controls, conflicts, negatives = [], [], []
    outer_cases = json.loads(outer.read_text())['cases']
    date_cases = json.loads(dates.read_text())['cases']
    for kind, pair in outer_cases.items():
        for family, wire in pair.items():
            schema = subject.validator(base / ('BoundaryRefusal.schema.json' if family == 'refusal' else
                'responses/' + wire['operation'] + '.response.schema.json'))
            controls.append(dict(name=kind + '_' + family + '_declared_schema', passed=not list(schema.iter_errors(wire))))
        raw_status = pair['refusal']['status']
        projected = {k: v for k, v in raw_status.items() if k not in server_only}
        conflicts.append(dict(kind=kind, exposed_server_only_fields=sorted(server_only & raw_status.keys()),
            raw_refusal_status_public_schema_errors=[e.message for e in public.iter_errors(raw_status)],
            projected_refusal_status_valid=not list(public.iter_errors(projected))))
    for name, wire in date_cases.items():
        schema = subject.validator(base / 'responses/status-job.response.schema.json')
        controls.append(dict(name=name + '_full_outer_schema', passed=not list(schema.iter_errors(wire))))
    mutations = {
        'outer_unknown': lambda w: w.update(unagreed='x'),
        'missing_grant': lambda w: w.pop('unprojected_grant'),
        'data_unknown': lambda w: w['data'].update(unagreed='x'),
        'operation_unknown_field': lambda w: w['data']['operation'].update(unagreed='x'),
        'null_business_date': lambda w: w['data']['source_dates'].update(business_date=None),
        'invalid_calendar': lambda w: w['data']['source_dates'].update(business_date='2026-02-30'),
        'source_unknown_field': lambda w: w['data']['source_dates'].update(unagreed='x'),
        'unsafe_action': lambda w: w['data'].update(actions=[dict(action='RETRY', safe=False, description='unsafe')]),
        'grant_unknown': lambda w: w['unprojected_grant'].update(unagreed='x'),
    }
    schema = subject.validator(base / 'responses/status-job.response.schema.json')
    for name, mutate in mutations.items():
        wire = copy.deepcopy(date_cases['single_date'])
        mutate(wire)
        errors = [e.message for e in schema.iter_errors(wire)]
        negatives.append(dict(name=name, wire=wire, schema_rejects=bool(errors), errors=errors))
        controls.append(dict(name=name + '_closed_schema_rejects', passed=bool(errors)))
    for name, mutate in {
        'wrong_lane': lambda w: w['data']['operation'].update(operation_kind='performance_report'),
        'null_extension_date': lambda w: w['data']['source_dates'].update(business_date=None),
    }.items():
        wire = copy.deepcopy(date_cases['per_section'])
        mutate(wire)
        errors = [e.message for e in schema.iter_errors(wire)]
        negatives.append(dict(name=name, wire=wire, schema_rejects=bool(errors), errors=errors))
        controls.append(dict(name=name + '_closed_schema_rejects', passed=bool(errors)))
    result = dict(pin=pin, source_sha256=hashes, controls=controls,
        public_refusal_contract_conflicts=conflicts, negatives=negatives,
        supplied=dict(returncode=suite.returncode, stdout=suite.stdout, stderr=suite.stderr),
        limitations=['Actual Entry fixture generator with offline retained storage and synthetic reports',
                     'BoundaryRefusal schema validation does not resolve its server-only public-field conflict',
                     'No live route/package/browser/vendor/deploy or integrated acceptance'])
    (own / 'OUTER_PAIR_7915_REVIEW.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(suite.stdout)
    print(json.dumps(dict(controls=len(controls), failed=[r for r in controls if not r['passed']], conflicts=conflicts), indent=2))
    return int(any(not r['passed'] for r in controls))


if __name__ == '__main__':
    raise SystemExit(main())
