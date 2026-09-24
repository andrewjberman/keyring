"""Independent actual SDK reader -> retained acceptance -> frozen worker review."""
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
    pin = subprocess.check_output(['git', 'rev-parse', 'cdbd4de74d'], cwd=root, text=True).strip()
    target = root / '.runtime/codex-seats/3.0.0_SA_CVO~Y/canonical-consumer' / pin
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
        'ycharts/generate/tests/test_canonical_profile_consumption.py',
        'ycharts/generate/tests/test_frozen_worker.py',
        'ycharts/generate/tests/test_recipe_snapshot.py',
        'ycharts/generate/tests/test_composition_admission.py',
        '_scope/tests/test_canonical_profile_reads.py', '_scope/tests/test_maintained_sources.py')]
    command = ('import socket,pytest; '
        'deny=lambda *a,**k: (_ for _ in ()).throw(AssertionError("NETWORK_FORBIDDEN")); '
        'socket.socket.connect=deny; socket.socket.connect_ex=deny; socket.create_connection=deny; '
        'raise SystemExit(pytest.main(' + repr(['-q'] + [str(p) for p in tests]) + '))')
    suite = subprocess.run([sys.executable, '-c', command], cwd=root, capture_output=True,
                           text=True, encoding='utf-8', errors='replace')
    socket.socket.connect = deny_network
    socket.socket.connect_ex = deny_network
    socket.create_connection = deny_network
    sys.path.insert(0, str(base / 'ycharts/generate/tests'))
    fixture = load('canonical_consumer_review_fixture', tests[0])
    support = fixture.support
    import pytest
    from botocore.exceptions import ClientError
    results = []

    def check(name, fn):
        try:
            results.append(dict(name=name, outcome='PASS', detail=fn()))
        except Exception as error:
            results.append(dict(name=name, outcome='FAIL', error=repr(error)))

    def responses(stub, owner, fault=None):
        email, firm = owner['principal_id'], owner['firm_id']
        key = {'PK': {'S': 'offline-actual-user-key'}, 'SK': {'S': 'PROFILE'}, 'email': {'S': email}}
        query = dict(TableName='opal-users-v2', IndexName='email-index',
            KeyConditionExpression='email = :email', ExpressionAttributeValues={':email': {'S': email}}, Limit=2)
        user = {**key, **{k: {'S': v} for k, v in {
            'firmId': firm, 'status': 'active', 'name': 'Independent SDK User',
            'phone': 'PRIVATE-MFA-NOT-REPORT', 'passwordHash': 'PRIVATE-HASH-NOT-REPORT'}.items()}}
        partner = {k: {'S': v} for k, v in {'email': email, 'firmId': firm,
            'advisorKey': owner['advisor_id'], 'advisorName': 'Independent SDK Advisor',
            'phone': 'PRIVATE-PARTNER-NOT-REPORT'}.items()}
        if fault == 'sdk_denied':
            stub.add_client_error('query', service_error_code='AccessDeniedException', expected_params=query)
            return
        if fault in ('ambiguous', 'incomplete', 'missing_user'):
            response = {'Items': [key, key] if fault == 'ambiguous' else [] if fault == 'missing_user' else [key]}
            if fault == 'incomplete':
                response['LastEvaluatedKey'] = {k: key[k] for k in ('PK', 'SK')}
            stub.add_response('query', response, query)
            return
        if fault == 'profile_pk':
            user['PK'] = {'S': 'different-key'}
        elif fault == 'user_firm':
            user['firmId'] = {'S': 'cottonwood'}
        elif fault == 'disabled_user':
            user['status'] = {'S': 'disabled'}
        elif fault == 'partner_owner':
            partner['advisorKey'] = {'S': 'different-advisor'}
        elif fault == 'partner_firm':
            partner['firmId'] = {'S': 'cottonwood'}
        for sequence in range(2):
            current_partner = copy.deepcopy(partner)
            if fault == 'midread_name' and sequence == 1:
                current_partner['advisorName'] = {'S': 'Changed between reads'}
            stub.add_response('query', {'Items': [key]}, query)
            stub.add_response('get_item', {'Item': user}, fixture.projected('opal-users-v2',
                {k: key[k] for k in ('PK', 'SK')}, ('PK', 'SK', 'email', 'firmId', 'status', 'name', 'updatedAt')))
            stub.add_response('get_item', {'Item': current_partner}, fixture.projected('opal-partner-' + firm,
                {'email': {'S': email}}, ('email', 'firmId', 'advisorKey', 'advisorName', 'firmRole', 'updatedAt')))

    def run(fault=None, midread=None, after=None):
        w = fixture.world.__wrapped__(fixture.retention_world.__wrapped__())
        client = fixture.boto3.client('dynamodb', region_name='us-east-1',
            aws_access_key_id='offline', aws_secret_access_key='offline')
        with fixture.Stubber(client) as stub, pytest.MonkeyPatch.context() as patch:
            readers = fixture.CanonicalProfileReaders(client)
            responses(stub, w.case.owner, fault)
            if midread:
                original = readers.get_user
                triggered = []
                def read(email):
                    value = original(email)
                    if not triggered:
                        triggered.append(True)
                        if midread == 'principal':
                            w.case.headers['x-user-email'] = 'revoked@example.invalid'
                        elif midread == 'retention_service':
                            w.case.service.artifacts.retention = None
                        elif midread == 'policy':
                            w.registered['state'] = 'PENDING_ENFORCEMENT'
                        elif midread == 'expiry':
                            w.state.now += 31 * 86400
                        else:
                            key = next(key for key, row in w.table.rows.items() if row.get('family') == 'ORIGINAL_CSV')
                            del w.table.rows[key]
                    return value
                readers.get_user = read
            fixture.install_consumer(patch, w, readers)
            try:
                r = support.assembled(w, configuration=lambda body, principal, owner:
                    fixture.capture_configuration(owner, body))
            except (ValueError, RuntimeError, PermissionError, ClientError) as error:
                if not fault and not midread:
                    raise
                assert w.case.s3.put_count == 2, 'composition persisted after source refusal'
                return dict(exception=type(error).__name__, reason=str(error), artifact_writes=2)
            if fault or midread:
                raise AssertionError('invalid source accepted into composition')
            stub.assert_no_pending_responses()
            first = r.worker.recipe_inputs(w.case.principal, r.store.request_id)
            assert first['cover']['prepared_by'] == 'Independent SDK Advisor'
            assert first['cover']['prepared_for'] == r.body['prepared_for']
            assert first['profile']['contact_email'] is None and first['profile']['contact_phone'] is None
            assert 'PRIVATE-' not in repr(first) and 'Synthetic Maintained Advisor' not in repr(first)
            assert first['profile_provenance']['prepared_by']['source_id'] == 'maintained-partner'
            assert first['source_descriptors']['maintained-user']['projection']['name'] == 'Independent SDK User'
            assert len(first['recipe']['settings']['settings']) == 7
            assert first['upload']['rows'][0]['quantity']['value'] == '12.03'
            before = (copy.deepcopy(r.client.rows), copy.deepcopy(w.table.rows), w.case.s3.put_count)
            if after:
                if after == 'grant':
                    w.case.headers['x-user-email'] = 'revoked@example.invalid'
                elif after == 'fence':
                    r.row['fence_token'] = {'N': '2'}
                else:
                    w.registered['state'] = 'PENDING_ENFORCEMENT'
                try:
                    r.worker.recipe_inputs(w.case.principal, r.store.request_id)
                except (ValueError, RuntimeError, PermissionError) as error:
                    r.client.update_item.assert_not_called()
                    return dict(exception=type(error).__name__, reason=str(error))
                raise AssertionError('revoked accepted consumer returned inputs')
            r.accepted.lookup.return_value = copy.deepcopy(r.record)
            r.service.resolve_inputs = Mock(side_effect=AssertionError('LIVE_PROFILE_RECAPTURE'))
            r.service.resolve_configuration = Mock(side_effect=AssertionError('LIVE_CONFIG_RECAPTURE'))
            client.query = Mock(side_effect=AssertionError('NEW_SDK_QUERY'))
            client.get_item = Mock(side_effect=AssertionError('NEW_SDK_READ'))
            r.service.submit(r.body, None, {}, {}, None)
            assert r.worker.recipe_inputs(w.case.principal, r.store.request_id) == first
            retained = support.canonical_bytes(first)
            first['profile']['prepared_by'] = 'Caller changed'
            first['source_descriptors'].clear()
            assert support.canonical_bytes(r.worker.recipe_inputs(w.case.principal, r.store.request_id)) == retained
            assert before == (r.client.rows, w.table.rows, w.case.s3.put_count)
            r.client.update_item.assert_not_called()
            return dict(prepared_sha256=hashlib.sha256(retained).hexdigest(), source='Independent SDK Advisor',
                        exact_total='12.03', secret_fields_absent=True, replay_writes=0)

    check('actual_sdk_source_to_acceptance_recipe_worker_and_frozen_retry', run)
    for fault in ('sdk_denied', 'ambiguous', 'incomplete', 'missing_user', 'profile_pk', 'user_firm',
                  'disabled_user', 'partner_owner', 'partner_firm', 'midread_name'):
        check('source_' + fault, lambda fault=fault: run(fault=fault))
    for fault in ('principal', 'retention_service', 'policy', 'expiry', 'original_dependency_removed'):
        check('during_sdk_' + fault, lambda fault=fault: run(midread=fault))
    for fault in ('grant', 'fence', 'policy'):
        check('accepted_worker_' + fault, lambda fault=fault: run(after=fault))
    report = dict(pin=pin, results=results, source_sha256=hashes,
        supplied=dict(exit_code=suite.returncode, stdout=suite.stdout, stderr=suite.stderr),
        limits=['Actual M SDK/read authorizer and Y/P consumer code; synthetic botocore/source/storage/ACTIVE policy/held lease',
                'Prospect Overview advisor fixture; no operations/three-firm/custody/installed factory/IAM/live policy/race/vendor/render/READY grade'])
    (own / 'CANONICAL_CONSUMER_cdbd4de7.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in report.items() if k != 'source_sha256'}, indent=2))
    return int(suite.returncode != 0 or any(row['outcome'] != 'PASS' for row in results))


if __name__ == '__main__':
    raise SystemExit(main())
