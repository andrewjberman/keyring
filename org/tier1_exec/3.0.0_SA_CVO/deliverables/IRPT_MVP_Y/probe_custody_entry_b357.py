"""Narrow resumed review: real Entry/guard, offline loaders/recording service."""
import base64
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
    pin = subprocess.check_output(['git', 'rev-parse', 'b357e0ba8f'], cwd=root, text=True).strip()
    target = root / '.runtime/codex-seats/3.0.0_SA_CVO~Y/custody-entry' / pin
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
    test_path = base / 'ycharts/generate/tests/test_custody_entry.py'
    command = ('import socket,pytest; '
        'deny=lambda *a,**k: (_ for _ in ()).throw(AssertionError("NETWORK_FORBIDDEN")); '
        'socket.socket.connect=deny; socket.socket.connect_ex=deny; socket.create_connection=deny; '
        'raise SystemExit(pytest.main(' + repr(['-q', str(test_path)]) + '))')
    suite = subprocess.run([sys.executable, '-c', command], cwd=root, capture_output=True,
                           text=True, encoding='utf-8', errors='replace')
    socket.socket.connect = deny_network
    socket.socket.connect_ex = deny_network
    socket.create_connection = deny_network
    fixture = load('custody_entry_review_fixture', test_path)
    entry, fx = fixture.entry, fixture.fx
    import pytest
    from prospect import resolve_prospect_owner
    results, observations = [], []

    def check(name, fn):
        try:
            results.append(dict(name=name, outcome='PASS', detail=fn()))
        except Exception as error:
            results.append(dict(name=name, outcome='FAIL', error=repr(error)))

    def installed(patch, *, service=True, prospect=False):
        recording = Mock()
        recording.submit.return_value = {'identity': {'request_id': 'recording-only'},
            'stage': 'RECEIVED', 'dispatch_pending': True}
        lookup = Mock(return_value=resolve_prospect_owner(fixture.event(opal=False)['headers'])) if prospect else None
        boundary = entry.build_entry(recording if service else None, lookup)
        boundary.deps = Mock(return_value=entry._loaders.fixture_deps(
            copy.deepcopy(fx.DIRECTORY), copy.deepcopy(fx.OWNERSHIP), (fx.POLICY, fx.ENTITLEMENT_REVISION)))
        boundary.opaque_firm_for = lambda _: fx.OPAQUE_FIRM
        patch.setenv('IRPT_DIRECTORY_BUCKET_MAP', json.dumps({'49financial': 'offline-bucket'}))
        return boundary, recording, lookup

    def actor(kind):
        with pytest.MonkeyPatch.context() as patch:
            boundary, service, _ = installed(patch)
            event = fixture.event(opal=kind == 'opal')
            if kind == 'dev':
                event['headers']['X-User-Type'] = 'Dev'
            original = copy.deepcopy(event)
            response = boundary.handle(event)
            assert 'data' in response, response
            payload, request, scope, received, ctx = service.submit.call_args.args
            assert payload == fixture.body() and received == original and event == original
            assert request.headers['X-Firm-Id'] == original['headers']['X-Firm-Id']
            assert request.headers['X-User-Email'] == original['headers']['X-User-Email']
            assert request.headers['X-Advisor-Id'] == original['headers']['X-Advisor-Id']
            assert ctx.tenant == '49financial' and scope['verified_request_firm_id'] == fx.OPAQUE_FIRM
            assert scope['principal_class'] == ('FIRM_ADVISOR' if kind == 'partner' else 'OPAL_GLOBAL')
            assert not boundary.opal_principal_ids and not boundary.prospect_modes and 'prospect_owner' not in scope
            assert boundary.deps.call_args.args == ('49financial',)
            return dict(home=request.headers['X-Firm-Id'], tenant=ctx.tenant,
                principal_class=scope['principal_class'], unchanged_account_ids=payload['account_ids'],
                unchanged_snapshot=payload['snapshot_id'], actor_email=request.headers['X-User-Email'])
    for kind in ('opal', 'dev', 'partner'):
        check('actual_entry_actor_tenant_' + kind, lambda kind=kind: actor(kind))

    def refused(change, *, prospect=False):
        with pytest.MonkeyPatch.context() as patch:
            boundary, service, _ = installed(patch, prospect=prospect)
            event = fixture.event()
            change(event)
            response = boundary.handle(event)
            assert response.get('ok') is False and 'data' not in response, response
            service.submit.assert_not_called()
            assert not boundary.opal_principal_ids
            return dict(reason=response.get('status', {}).get('reason_code'))

    def prospect_body(event):
        event['body'] = json.dumps(dict(fixture.body(), input_id='portfolio_' + 'a' * 64,
            client_id=None, account_ids=[], snapshot_id=None))

    def closed_body(key):
        return lambda ev: ev.update(body=json.dumps(dict(fixture.body(), **{key: 'forged'})))
    changes = {
        'global_generation': lambda ev: ev['queryStringParameters'].update(selected_tenant='global'),
        'unknown_tenant': lambda ev: ev['queryStringParameters'].update(selected_tenant='unregistered'),
        'conflicting_selectors': lambda ev: ev.update(pathParameters={'selected_tenant': 'inflection'}),
        'opaque_selector_not_slug': lambda ev: ev['queryStringParameters'].update(selected_tenant=fx.OPAQUE_FIRM),
        'missing_origin': lambda ev: ev['headers'].update({'X-Origin-Verify': ''}),
        'renderer': lambda ev: ev['headers'].update({'X-User-Role': 'renderer'}),
        'missing_subject': lambda ev: ev['headers'].update({'X-User-Email': ''}),
        'missing_contract': lambda ev: ev['headers'].pop('X-Contract-Version'),
        'server_owner_in_body': closed_body('owner'),
        'tenant_in_body': closed_body('selected_tenant'),
        'resolved_in_body': closed_body('resolved'),
        'identity_in_body': closed_body('identity'),
        'implicit_opal_prospect': prospect_body,
        'duplicate_body_key': lambda ev: ev.update(body=ev['body'][:-1] + ',"request_id":"second"}'),
        'malformed_base64': lambda ev: ev.update(body='@@@', isBase64Encoded=True),
    }
    for name, change in changes.items():
        check('refuse_' + name, lambda change=change: refused(change))

    def partner_prospect(event):
        event['headers']['X-Firm-Id'] = '49financial'
        prospect_body(event)
    check('refuse_implicit_partner_prospect', lambda: refused(partner_prospect))
    check('refuse_explicit_opal_prospect', lambda: refused(prospect_body, prospect=True))

    def warm():
        with pytest.MonkeyPatch.context() as patch:
            boundary, service, _ = installed(patch)
            assert 'data' in boundary.handle(fixture.event())
            assert not boundary.opal_principal_ids
            for tenant in ('global', 'inflection'):
                service.reset_mock()
                event = fixture.event(opal=False, tenant=tenant)
                event['headers']['X-User-Role'] = 'admin'
                event['headers']['X-User-Email'] = 'pretend@opal-capital.com'
                assert boundary.handle(event).get('ok') is False
                service.submit.assert_not_called()
            service.reset_mock()
            event = fixture.event(opal=False)
            assert 'data' in boundary.handle(event)
            assert service.submit.call_args.args[2]['principal_class'] == 'FIRM_ADVISOR'
            assert not boundary.opal_principal_ids
            return dict(warm_requests=4, no_roster_mutation=True)
    check('warm_opal_partner_admin_foreign_global_then_partner', warm)

    def explicit_prospect():
        with pytest.MonkeyPatch.context() as patch:
            boundary, service, lookup = installed(patch, prospect=True)
            event = fixture.event(opal=False)
            event.pop('queryStringParameters')
            prospect_body(event)
            assert 'data' in boundary.handle(event)
            scope = service.submit.call_args.args[2]
            assert scope['principal_class'] == 'FIRM_ADVISOR' and 'prospect_owner' in scope
            assert lookup.called
            boundary.deps.assert_not_called()
            return dict(explicit_prospect_mode=boundary.prospect_modes)
    check('explicit_partner_prospect_install_preserved', explicit_prospect)

    def absent_service():
        with pytest.MonkeyPatch.context() as patch:
            boundary, recording, _ = installed(patch, service=False)
            assert boundary.handle(fixture.event()).get('ok') is False
            recording.submit.assert_not_called()
        try:
            entry.build_entry(load_prospect_owner=Mock())
        except entry.RequestRefused as error:
            assert str(error) == 'SUBMISSION_AND_OWNER_LOOKUP_REQUIRED'
            return dict(reason=str(error))
        raise AssertionError('lookup without service accepted')
    check('missing_service_and_lookup_only_refused', absent_service)

    def encoded_positive():
        with pytest.MonkeyPatch.context() as patch:
            boundary, service, _ = installed(patch)
            event = fixture.event()
            event['body'] = base64.b64encode(event['body'].encode()).decode()
            event['isBase64Encoded'] = True
            assert 'data' in boundary.handle(event)
            assert service.submit.call_args.args[0] == fixture.body()
    check('base64_body_preserves_exact_custody_request', encoded_positive)

    # Evidence of the seam, not a PASS that these values are owned or accepted.
    with pytest.MonkeyPatch.context() as patch:
        boundary, service, _ = installed(patch)
        event = fixture.event(opal=False)
        unverified = dict(fixture.body(), account_ids=[fx.A5], snapshot_id='unaccepted-snapshot')
        event['body'] = json.dumps(unverified)
        response = boundary.handle(event)
        observations.append(dict(name='account_snapshot_validation_belongs_to_installed_service',
            reaches_recording_service=service.submit.called, response_has_data='data' in response,
            exact_unverified_payload=unverified,
            limitation='No durable service/accepted selection loaded; reaching mock does not authorize this basis'))

    report = dict(pin=pin, results=results, observations=observations, source_sha256=hashes,
        supplied=dict(exit_code=suite.returncode, stdout=suite.stdout, stderr=suite.stderr),
        limits=['Actual Y Entry/shared guard; offline directory/ownership/loaders and recording submission service',
                'No accepted selection/snapshot validation, custody owner/profile/admission/retained worker, live identity, package, vendor or runtime grade'])
    (own / 'CUSTODY_ENTRY_b357e0ba.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in report.items() if k != 'source_sha256'}, indent=2))
    return int(suite.returncode != 0 or any(row['outcome'] != 'PASS' for row in results))


if __name__ == '__main__':
    raise SystemExit(main())
