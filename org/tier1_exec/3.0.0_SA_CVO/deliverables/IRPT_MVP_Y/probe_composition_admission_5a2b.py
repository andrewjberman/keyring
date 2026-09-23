"""Independent acceptance/replay controls on exact pinned offline composition."""
import copy
import hashlib
import io
import json
import os
from pathlib import Path
import socket
import subprocess
import sys
from types import SimpleNamespace
from unittest.mock import Mock
import zipfile

from probe_recipe_decimal import deny_network, load


def main():
    own = Path(__file__).resolve().parent
    root = own.parents[4]
    pin = subprocess.check_output(['git', 'rev-parse', '5a2b531645'], cwd=root, text=True).strip()
    target = root / '.runtime/codex-seats/3.0.0_SA_CVO~Y/composition-admission' / pin
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
    tests = [base / name for name in (
        'ycharts/generate/tests/test_composition_admission.py',
        'ycharts/generate/tests/test_submission.py',
        'intake/tests/test_retained_uploads.py', 'intake/tests/test_uploads.py')]
    command = ('import socket,pytest; '
        'deny=lambda *a,**k: (_ for _ in ()).throw(AssertionError("NETWORK_FORBIDDEN")); '
        'socket.socket.connect=deny; socket.socket.connect_ex=deny; socket.create_connection=deny; '
        'raise SystemExit(pytest.main(' + repr(['-q'] + [str(p) for p in tests]) + '))')
    suite = subprocess.run([sys.executable, '-c', command], cwd=root, capture_output=True,
                           text=True, encoding='utf-8', errors='replace')
    socket.socket.connect = deny_network
    socket.socket.connect_ex = deny_network
    socket.create_connection = deny_network
    sys.path.insert(0, str(base / 'intake/tests'))
    fixture = load('admission_review_fixture', base / 'intake/tests/test_retained_uploads.py')
    canonical = sys.modules['submission'].canonical_bytes
    results, observations = [], []

    def fresh():
        world = fixture.world.__wrapped__(fixture.retention_world.__wrapped__())
        first = world.case.create()
        service, accepted, body, loaded = fixture.submission(world, first)
        return SimpleNamespace(w=world, first=first, s=service, a=accepted, body=body, loaded=loaded)

    def submit(r):
        return r.s.submit(r.body, None, {}, {}, None)

    def accept(r):
        result = submit(r)
        owner, _, ref = r.a.accept.call_args.args
        r.record = copy.deepcopy(dict(owner=owner, composition_ref=ref, identity=result['identity']))
        r.a.lookup.return_value = r.record
        r.a.dispatch.reset_mock()
        r.ref = ref
        r.data = r.w.stores.artifacts.get(r.w.case.principal, ref['artifact_id'])['data']
        return result

    def check(name, fn):
        try:
            results.append(dict(name=name, outcome='PASS', detail=fn()))
        except Exception as error:
            results.append(dict(name=name, outcome='FAIL', error=repr(error)))

    def refuse(r, *, initial=False, no_write=True):
        count = r.w.case.s3.put_count
        try:
            submit(r)
        except (ValueError, RuntimeError, PermissionError) as error:
            r.a.dispatch.assert_not_called()
            if initial:
                r.a.accept.assert_not_called()
            if no_write:
                assert r.w.case.s3.put_count == count
            return dict(exception=type(error).__name__, reason=str(error))
        raise AssertionError('invalid composition dispatched or returned success')

    def add_source_refs(r):
        refs = []
        for index, source in enumerate(r.loaded['source_descriptors'].values()):
            ref = r.w.stores.artifacts.put(r.w.case.principal, r.loaded['owner'],
                'ORIGINAL_CSV', 'review-source-' + str(index),
                ('source-' + str(index)).encode(), 'text/csv')
            source['retention_ref'] = ref['retention_ref']
            refs.append(ref['retention_ref'])
        return refs

    def positive():
        r = fresh()
        refs = add_source_refs(r)
        initial = accept(r)
        row = r.w.stores.retention.require_live(r.w.case.principal, r.ref['retention_ref'])
        expected = [r.first['input_ref']['artifact_ref']['retention_ref']] + refs
        assert {canonical(x) for x in row['dependencies']} == {canonical(x) for x in expected}
        frozen = json.loads(r.data)
        assert frozen['browser'] == r.body
        assert frozen['resolved']['profile']['prepared_for'] == r.body['prepared_for']
        assert frozen['resolved']['profile']['organization'] == '49 Financial'
        assert frozen['resolved']['profile']['contact_phone'] is None
        r.loaded['profile']['prepared_by'] = 'Changed upstream'
        r.loaded['document']['holdings']['total_dollars'] = '999'
        r.loaded['source_descriptors'].clear()
        r.s.settings['management_fee'] = 123
        r.s.recipe_version = 'future-recipe'
        r.s.resolve_inputs = Mock(side_effect=AssertionError('REPLAY_RESOLVED_LIVE_SOURCE'))
        before = r.w.case.s3.put_count
        assert submit(r) == initial
        assert r.w.stores.artifacts.get(r.w.case.principal, r.ref['artifact_id'])['data'] == r.data
        assert r.w.case.s3.put_count == before
        assert r.a.accept.call_count == 1
        r.s.resolve_inputs.assert_not_called()
        return dict(dependency_count=len(expected), exact_composition_sha256=hashlib.sha256(r.data).hexdigest(),
                    unchanged_expiry=row['expires_at'], acceptance_count=1)

    check('all_source_dependencies_and_frozen_exact_replay', positive)

    def initial_fault(change):
        r = fresh()
        change(r)
        return refuse(r, initial=True)

    changes = {
        'extra_resolved_key': lambda r: r.loaded.update(extra='forged'),
        'extra_browser_key': lambda r: r.body.update(principal_id='forged'),
        'recipient_mismatch': lambda r: r.loaded['profile'].update(prepared_for='Other'),
        'normalized_document_changed': lambda r: r.loaded['document']['holdings'].update(total_dollars='999'),
        'source_projection_changed': lambda r: r.loaded['source_descriptors']['maintained-user']['projection'].update(name='Changed'),
        'source_owner_changed': lambda r: r.loaded['source_descriptors']['maintained-user']['binding'].update(principal_id='foreign'),
        'unrequested_comparison': lambda r: r.loaded['comparison_catalog'].update(foreign={'vendor_id': 'P:1'}),
        'recipe_changed_without_source': lambda r: setattr(r.s, 'recipe_version', 'other'),
        'settings_changed_without_source': lambda r: r.s.settings.update(management_fee=999),
        'missing_admission': lambda r: setattr(r.s, 'admission', None),
        'missing_retention_service': lambda r: setattr(r.s.artifacts, 'retention', None),
        'current_access_revoked': lambda r: setattr(r.s, 'authorize_current', lambda *a: False),
        'old_browser_missing_label': lambda r: r.body.pop('prepared_for'),
    }
    for name, change in changes.items():
        check('pre_accept_' + name, lambda change=change: initial_fault(change))

    def replay_fault(change):
        r = fresh()
        accept(r)
        change(r)
        return refuse(r)

    replays = {
        'recipient_changed': lambda r: r.body.update(prepared_for='Other'),
        'title_changed': lambda r: r.body.update(report_title='Other'),
        'current_access_revoked': lambda r: setattr(r.s, 'authorize_current', lambda *a: False),
        'principal_header_changed': lambda r: r.w.case.headers.update({'x-user-email': 'foreign@example.invalid'}),
        'owner_changed': lambda r: r.record['owner'].update(prospect_input_id='foreign'),
        'receipt_hash_changed': lambda r: r.record['composition_ref'].update(sha256='0' * 64),
        'missing_admission': lambda r: setattr(r.s, 'admission', None),
        'pending_policy': lambda r: r.w.registered.update(state='PENDING_ENFORCEMENT'),
        'input_expired': lambda r: setattr(r.w.state, 'now',
            r.w.stores.retention.require_live(r.w.case.principal, r.ref['retention_ref'])['expires_at']),
    }
    for name, change in replays.items():
        check('replay_' + name, lambda change=change: replay_fault(change))

    def stored_legacy():
        r = fresh()
        accept(r)
        doc = json.loads(r.data)
        del doc['browser']['prepared_for']
        r.record['composition_ref'] = r.w.stores.artifacts.put(r.w.case.principal,
            r.loaded['owner'], 'REQUEST_COMPOSITION', 'review-legacy', canonical(doc),
            'application/json', retention_dependencies=[r.ref['retention_ref']])
        return refuse(r)
    check('replay_legacy_stored_label_missing', stored_legacy)

    def missing_dependency():
        r = fresh()
        refs = add_source_refs(r)
        accept(r)
        # Authentic schema-valid bytes, but a newly forged artifact receipt omits
        # declared source dependencies. Real repository writes; no head stub.
        r.record['composition_ref'] = r.w.stores.artifacts.put(r.w.case.principal,
            r.loaded['owner'], 'REQUEST_COMPOSITION', 'review-missing-dependencies', r.data,
            'application/json', retention_dependencies=[r.first['input_ref']['artifact_ref']['retention_ref']])
        detail = refuse(r)
        detail['omitted_dependencies'] = len(refs)
        return detail
    check('replay_authentic_bytes_omitted_source_dependencies', missing_dependency)

    def expired_source():
        r = fresh()
        refs = add_source_refs(r)
        # Current source is expired before first request-composition write.
        expiry = r.w.stores.retention.require_live(r.w.case.principal, refs[0])['expires_at']
        r.w.state.now = expiry
        return refuse(r, initial=True)
    check('pre_accept_expired_source_or_input', expired_source)

    def revoke_during_read():
        r = fresh()
        accept(r)
        r.w.case.s3.on_get = lambda: r.w.case.headers.update({'x-user-email': 'foreign@example.invalid'})
        return refuse(r)
    check('replay_access_changes_during_blob_read', revoke_during_read)

    def final_authorization():
        r = fresh()
        accept(r)
        calls = []
        def authorized(*args):
            calls.append(True)
            return len(calls) < 3
        r.s.authorize_current = authorized
        detail = refuse(r)
        assert len(calls) == 3
        return detail
    check('replay_access_changes_after_composition_verification', final_authorization)

    report = dict(pin=pin, supplied=dict(exit_code=suite.returncode, stdout=suite.stdout, stderr=suite.stderr),
        results=results, observations=observations, source_sha256=hashes,
        limits=['Actual M/P/Y functions with synthetic canonical readers, clock, S3 and Dynamo effects',
                'Acceptance and dispatch ports mocked; no atomic acceptance, queue, worker, browser, vendor or runtime grade'])
    (own / 'COMPOSITION_ADMISSION_5a2b.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in report.items() if k != 'source_sha256'}, indent=2))
    return int(suite.returncode != 0 or any(row['outcome'] != 'PASS' for row in results))


if __name__ == '__main__':
    raise SystemExit(main())
