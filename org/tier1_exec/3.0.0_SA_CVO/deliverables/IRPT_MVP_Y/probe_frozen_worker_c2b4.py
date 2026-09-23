"""Independent read-only frozen worker review, with no network or vendor ports."""
import copy
import hashlib
import io
import json
import os
from pathlib import Path
import socket
import subprocess
import sys
from unittest.mock import Mock
import zipfile

from probe_recipe_decimal import deny_network, load


def main():
    own = Path(__file__).resolve().parent
    root = own.parents[4]
    pin = subprocess.check_output(['git', 'rev-parse', 'c2b467fa47'], cwd=root, text=True).strip()
    target = root / '.runtime/codex-seats/3.0.0_SA_CVO~Y/frozen-worker' / pin
    target.mkdir(parents=True, exist_ok=True)
    prefix = 'infra/aws/lambda/investor-reporting'
    raw = subprocess.check_output(['git', 'archive', '--format=zip', pin, prefix,
                                  'docs/contracts/investor-reporting', 'data/firm_registry.json'], cwd=root)
    hashes = {}
    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        for item in archive.infolist():
            path = (target / item.filename).resolve()
            if not path.is_relative_to(target.resolve()):
                raise ValueError('snapshot escape')
            if item.is_dir():
                path.mkdir(parents=True, exist_ok=True)
            else:
                data = archive.read(item)
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(data)
                hashes[item.filename] = hashlib.sha256(data).hexdigest()
    os.environ['IRPT_FIRM_REGISTRY'] = str(target / 'data/firm_registry.json')
    base = target / prefix
    tests = [base / 'ycharts/generate/tests' / name for name in
             ('test_frozen_worker.py', 'test_composition_admission.py', 'test_normalized_input.py')]
    command = ('import socket,pytest; '
        'deny=lambda *a,**k: (_ for _ in ()).throw(AssertionError("NETWORK_FORBIDDEN")); '
        'socket.socket.connect=deny; socket.socket.connect_ex=deny; socket.create_connection=deny; '
        'raise SystemExit(pytest.main(' + repr(['-q'] + [str(p) for p in tests]) + '))')
    suite = subprocess.run([sys.executable, '-c', command], cwd=root, capture_output=True,
                           text=True, encoding='utf-8', errors='replace')
    socket.socket.connect = deny_network
    socket.socket.connect_ex = deny_network
    socket.create_connection = deny_network
    fixture = load('frozen_worker_review_fixture', tests[0])
    module = sys.modules['frozen_worker']
    canonical = fixture.canonical_bytes
    results, observations = [], []

    def fresh():
        world = fixture.world.__wrapped__(fixture.retention_world.__wrapped__())
        result = fixture.assembled(world, source_refs=True)
        result.w = world
        return result

    def check(name, fn):
        try:
            results.append(dict(name=name, outcome='PASS', detail=fn()))
        except Exception as error:
            results.append(dict(name=name, outcome='FAIL', error=repr(error)))

    def refuse(r):
        count = r.w.case.s3.put_count
        try:
            r.prepare()
        except (ValueError, RuntimeError, PermissionError) as error:
            assert r.w.case.s3.put_count == count
            r.client.update_item.assert_not_called()
            return dict(exception=type(error).__name__, reason=str(error))
        raise AssertionError('invalid preparation returned worker inputs')

    def positive():
        r = fresh()
        before = (copy.deepcopy(r.client.rows), copy.deepcopy(r.w.table.rows), r.w.case.s3.put_count)
        first = r.prepare()
        original = canonical(first)
        assert first['profile']['prepared_for'] == r.body['prepared_for']
        assert first['cover']['prepared_for'] == r.body['prepared_for']
        assert first['profile']['contact_phone'] is None and first['cover']['contact_phone'] == ''
        assert first['profile_provenance']['contact_phone']['state'] == 'ABSENT'
        assert first['settings'] == r.service.settings
        assert first['upload']['total_dollars'] == '12.03'
        assert first['upload']['rows'] == [{'identifier': 'AAPL', 'quantity': {'units': 'USD', 'value': '12.03'}}]
        assert len(first['source_descriptors']) == 6 and first['comparisons'] == []
        # Poison the fresh-source paths and mutate every returned nested surface.
        r.service.resolve_inputs = Mock(side_effect=AssertionError('SOURCE_RERESOLUTION'))
        r.w.case.service.resolve_security = Mock(side_effect=AssertionError('SECURITY_RERESOLUTION'))
        r.service.settings.clear()
        r.loaded.clear()
        for field in ('identity', 'composition_ref', 'frozen_input', 'upload', 'profile', 'cover',
                      'profile_provenance', 'source_descriptors', 'settings'):
            first[field].clear()
        first['comparisons'].append({'forged': True})
        assert canonical(r.prepare()) == original
        assert before == (r.client.rows, r.w.table.rows, r.w.case.s3.put_count)
        r.client.update_item.assert_not_called()
        return dict(preparation_sha256=hashlib.sha256(original).hexdigest(),
                    source_count=6, exact_total='12.03', state=r.row['state']['S'], writes=0)
    check('frozen_detached_source_profile_cover_settings_upload_no_writes', positive)

    def early(change):
        r = fresh()
        change(r)
        r.w.case.s3.on_get = lambda: (_ for _ in ()).throw(AssertionError('BLOB_READ_BEFORE_REFUSAL'))
        return refuse(r)
    faults = {
        'principal': lambda r: r.w.case.principal.update(principal_id='foreign'),
        'tenant': lambda r: setattr(r.store, 'tenant', 'foreign'),
        'request': lambda r: setattr(r.store, 'request_id', 'REQ-' + '0' * 24),
        'composition': lambda r: setattr(r.store, 'composition_sha256', '0' * 64),
        'fence': lambda r: r.row.update(fence_token={'N': '2'}),
        'lease_owner': lambda r: r.row.update(lease_owner={'S': 'replacement'}),
        'lease_deadline': lambda r: setattr(r.w.state, 'now', r.w.state.now + 120),
        'missing_claim': lambda r: setattr(r.store, 'fence', None),
    }
    for name, change in faults.items():
        check('early_' + name, lambda change=change: early(change))

    def late(change):
        r = fresh()
        original = module.prepare_normalized_upload
        def prepare(value):
            result = original(value)
            change(r)
            return result
        module.prepare_normalized_upload = prepare
        try:
            return refuse(r)
        finally:
            module.prepare_normalized_upload = original
    late_faults = {
        'grant': lambda r: r.w.case.headers.update({'x-user-email': 'revoked@example.invalid'}),
        'fence': lambda r: r.row.update(fence_token={'N': '2'}),
        'lease_owner': lambda r: r.row.update(lease_owner={'S': 'replacement'}),
        'lease_deadline': lambda r: setattr(r.w.state, 'now', r.w.state.now + 120),
        'job_composition': lambda r: r.row.update(composition_sha256={'S': '0' * 64}),
        'accepted_record': lambda r: fixture.rewrite_record(r, lambda doc: doc.update(accepted_at=doc['accepted_at'] + 1)),
        'retention_policy': lambda r: r.w.registered.update(state='PENDING_ENFORCEMENT'),
        'retention_removed': lambda r: setattr(r.requests.artifacts, 'retention', None),
    }
    for name, change in late_faults.items():
        check('after_upload_preparation_' + name, lambda change=change: late(change))

    def artifact_fault(kind):
        r = fresh()
        actual_get = r.requests.artifacts.get
        def get(*args, **kwargs):
            result = actual_get(*args, **kwargs)
            if result['ref']['family'] == kind:
                result = copy.deepcopy(result)
                result['data'] += b' '
            return result
        r.requests.artifacts.get = get
        return refuse(r)
    for family in ('NORMALIZED_PORTFOLIO', 'REQUEST_COMPOSITION'):
        check('actual_read_bytes_changed_' + family, lambda family=family: artifact_fault(family))

    def rewritten(kind):
        r = fresh()
        artifacts, principal = r.w.stores.artifacts, r.w.case.principal
        doc = json.loads(artifacts.get(principal, r.record['composition_ref']['artifact_id'])['data'])
        refs = [doc['resolved']['input_ref']['artifact_ref']['retention_ref']]
        if kind != 'missing_source_dependencies':
            refs += [source['retention_ref'] for source in doc['resolved']['source_descriptors'].values()]
        if kind == 'missing_recipient':
            del doc['browser']['prepared_for']
        elif kind == 'recipient_binding':
            doc['resolved']['profile']['prepared_for'] = 'Changed'
        elif kind == 'browser_token':
            doc['browser']['request_id'] = 'other-request'
        elif kind == 'settings_binding':
            doc['settings']['management_fee'] = 999
        ref = artifacts.put(principal, r.record['owner'], 'REQUEST_COMPOSITION',
            'independent-' + kind, canonical(doc), 'application/json', retention_dependencies=refs)
        def change(record):
            record['composition_ref'] = ref
            if kind == 'browser_token':
                record['browser_sha256'] = fixture.digest(doc['browser'])
        fixture.rewrite_record(r, change)
        r.store.composition_sha256 = ref['sha256']
        r.row['composition_sha256'] = {'S': ref['sha256']}
        return refuse(r)
    for name in ('missing_source_dependencies', 'missing_recipient', 'recipient_binding', 'browser_token', 'settings_binding'):
        check('authentic_retained_rewrite_' + name, lambda name=name: rewritten(name))

    def source_revocation():
        r = fresh()
        source = r.loaded['source_descriptors']['maintained-user']['retention_ref']
        policy = r.requests.artifacts.retention
        actual = policy.require_live
        revoked = [False]
        def require(principal, ref, **kwargs):
            if revoked[0] and ref == source:
                raise PermissionError('INDEPENDENT_SOURCE_GRANT_REVOKED')
            return actual(principal, ref, **kwargs)
        policy.require_live = require
        original = module.prepare_normalized_upload
        def prepare(value):
            result = original(value)
            revoked[0] = True
            return result
        module.prepare_normalized_upload = prepare
        try:
            return refuse(r)
        finally:
            module.prepare_normalized_upload = original
    check('late_individual_source_grant_refused_by_recursive_final_retention', source_revocation)

    def cover():
        r = fresh()
        result = r.prepare()
        body = fixture.generation_body({'variant': 'OVERVIEW', 'template_id': 'synthetic',
            'comparison_securities': {'min': 0, 'max': 0}}, ['P:synthetic'], {},
            {**result['cover'], 'primary_name': 'Synthetic primary'})
        assert fixture.cover_fields_agree(body)[0] is True
        assert body['prepared_for'] == body['generationModalsState']['coverPageInfo']['preparedFor'] == r.body['prepared_for']
        return dict(exact_recipient=body['prepared_for'], synthetic_template=True)
    check('actual_generation_body_duplicate_cover_fields_agree', cover)

    report = dict(pin=pin, results=results, observations=observations, source_sha256=hashes,
        supplied=dict(exit_code=suite.returncode, stdout=suite.stdout, stderr=suite.stderr),
        limits=['Synthetic canonical readers, S3/Dynamo transaction effects and already-acquired lease row',
                'Actual acceptance/reader/admission/worker/recipe functions; no atomicity, lease race, transport, vendor, render, export or READY grade'])
    (own / 'FROZEN_WORKER_c2b467fa.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in report.items() if k != 'source_sha256'}, indent=2))
    return int(suite.returncode != 0 or any(row['outcome'] != 'PASS' for row in results))


if __name__ == '__main__':
    raise SystemExit(main())
