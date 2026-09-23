"""Exact recipient validator and historical catalogue data review, no live calls."""
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
    pin = subprocess.check_output(['git', 'rev-parse', '70eabdcf3b'], cwd=root, text=True).strip()
    catalogue_pin = subprocess.check_output(['git', 'rev-parse', '9daa67433e'], cwd=root, text=True).strip()
    target = root / '.runtime/codex-seats/3.0.0_SA_CVO~Y/recipient-boundary' / pin
    target.mkdir(parents=True, exist_ok=True)
    prefix = 'infra/aws/lambda/investor-reporting'
    raw = subprocess.check_output(['git', 'archive', '--format=zip', pin, prefix,
                                   'docs/contracts/investor-reporting', 'data/firm_registry.json'], cwd=root)
    hashes = {}
    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        for member in archive.infolist():
            path = (target / member.filename).resolve()
            if not path.is_relative_to(target.resolve()):
                raise ValueError('snapshot escape')
            if member.is_dir():
                path.mkdir(parents=True, exist_ok=True)
            else:
                data = archive.read(member)
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(data)
                hashes[member.filename] = hashlib.sha256(data).hexdigest()
    socket.socket.connect = deny_network
    socket.socket.connect_ex = deny_network
    socket.create_connection = deny_network
    os.environ['IRPT_FIRM_REGISTRY'] = str(target / 'data/firm_registry.json')
    test = target / prefix / 'ycharts/generate/tests/test_submission.py'
    command = ('import socket,pytest; '
        'deny=lambda *a,**k: (_ for _ in ()).throw(AssertionError("NETWORK_FORBIDDEN")); '
        'socket.socket.connect=deny; socket.socket.connect_ex=deny; socket.create_connection=deny; '
        'raise SystemExit(pytest.main(' + repr(['-q', str(test)]) + '))')
    suite = subprocess.run([sys.executable, '-c', command], cwd=root, capture_output=True, text=True)
    if suite.returncode:
        print(suite.stdout, suite.stderr)
        return suite.returncode
    subject = load('recipient_review_fixture', test)
    validation = sys.modules['submission']
    results = []

    def check(name, fn):
        try:
            results.append(dict(name=name, outcome='PASS', detail=fn()))
        except Exception as exc:
            results.append(dict(name=name, outcome='FAIL', error=repr(exc)))

    def body(lane):
        value = subject.browser()
        if lane == 'prospect':
            value.update(input_id='UP-example', client_id=None, account_ids=[], snapshot_id=None)
        return value

    def rejects(value):
        try:
            validation.validate_public_request(value)
        except validation.SubmissionRefused as exc:
            return exc.code
        raise AssertionError('invalid recipient accepted')

    for lane in ('custody', 'prospect'):
        def positives(lane=lane):
            labels = ['  Exact Recipient  ', '\U0001f600' * 200, 'e\u0301', '<script>"& recipient']
            for label in labels:
                value = body(lane)
                value['prepared_for'] = label
                accepted = validation.validate_public_request(value)
                assert accepted == value
                assert {k: v for k, v in accepted.items() if k != 'prepared_for'} == {
                    k: v for k, v in body(lane).items() if k != 'prepared_for'}
                value['prepared_for'] = 'mutated'
                value['comparison_keys'].append('not_accepted')
                assert accepted['prepared_for'] == label and accepted['comparison_keys'] == []
            return dict(positive_values=len(labels), exact_text=True, title_scope_unchanged=True)
        check(lane + '_exact_text_and_no_alias_or_scope_change', positives)

        def missing_invalid(lane=lane):
            value = body(lane)
            del value['prepared_for']
            assert rejects(value) == 'MISSING_REQUEST_FIELD'
            bad = [None, True, 12, [], {}, '', ' \u2003\u00a0 ', 'x' * 201, '\U0001f600' * 201]
            for label in bad:
                assert rejects(dict(body(lane), prepared_for=label)) == 'PREPARED_FOR'
            return dict(missing=1, invalid_values=len(bad))
        check(lane + '_missing_blank_type_and_length_refused', missing_invalid)

        def prohibited(lane=lane):
            points = list(range(32)) + list(range(127, 160)) + list(range(0xD800, 0xE000))
            for point in points:
                assert rejects(dict(body(lane), prepared_for='Recipient' + chr(point))) == 'PREPARED_FOR'
            return dict(C0_C1_and_DEL=65, surrogate_codepoints=2048)
        check(lane + '_all_control_and_surrogate_codepoints_refused', prohibited)

        def forged_owner(lane=lane):
            for field in ('owner', 'principal_id', 'firm_id', 'resolved', 'prepared_for_provenance'):
                value = dict(body(lane), **{field: 'forged'})
                assert rejects(value) == 'UNKNOWN_OR_SERVER_OWNED_FIELD'
            return dict(server_field_attempts=5)
        check(lane + '_label_cannot_add_server_owned_keys', forged_owner)

    def before_resolver():
        callbacks = {key: Mock(side_effect=AssertionError('invalid body reached ' + key))
                     for key in ('resolve_owner', 'authorize_current', 'resolve_inputs', 'send')}
        service = subject.SubmissionService(acceptance=Mock(), artifacts=Mock(),
            settings={'version': 1}, recipe_version='review', ingestion_revision='v1',
            destination_revision='v1', queue_url='offline', **callbacks)
        value = dict(body('custody'), prepared_for='')
        try:
            service.submit(value, None, {}, {}, None)
        except validation.SubmissionRefused as exc:
            assert exc.code == 'PREPARED_FOR'
        else:
            raise AssertionError('invalid submission accepted')
        assert all(not callback.called for callback in callbacks.values())
        return 'invalid recipient refused before resolver, authorization or send callbacks'
    check('service_refuses_invalid_recipient_before_resolution', before_resolver)

    def local_freeze():
        value = body('custody')
        resolved = dict(owner=copy.deepcopy(subject.OWNER), input_ref=dict(input_id='UP-review', content_sha256='a' * 64),
                        client=dict(client_id=value['client_id'], account_ids=list(value['account_ids'])),
                        holdings=dict(snapshot_id=value['snapshot_id']))
        first = validation.compose_frozen_request(value, resolved, recipe_version='review', settings={'v': 1})
        value['prepared_for'] = 'Changed explicit recipient'
        second = validation.compose_frozen_request(value, resolved, recipe_version='review', settings={'v': 1})
        assert first['content_sha256'] != second['content_sha256']
        assert first['document']['browser']['prepared_for'] == subject.browser()['prepared_for']
        assert first['document']['resolved'] == second['document']['resolved']
        assert first['document']['browser']['report_title'] == second['document']['browser']['report_title']
        return 'local composition hashes differ; persistence/worker canonical integration not graded'
    check('local_hash_changes_without_rewriting_prior_composition', local_freeze)

    cat_path = prefix + '/ycharts/generate/templates.json'
    cat_bytes = subprocess.check_output(['git', 'show', catalogue_pin + ':' + cat_path], cwd=root)
    previous_bytes = subprocess.check_output(['git', 'cat-file', 'blob', 'ed18c59c86ef89b33eb4759f0d2a939b964e5ac8'], cwd=root)
    catalogue = json.loads(cat_bytes)['comparison_catalog']
    historical = {r['key']: r for r in json.loads(previous_bytes)['comparison_catalog']['entries']}
    for row in catalogue['entries']:
        def inspect(row=row):
            old = historical[row['key']]
            for key in ('security_id', 'security_type', 'label', 'live_proven'):
                assert row[key] == old[key]
            candidate = row['candidate']
            assert candidate['namespace'] == 'YCHARTS'
            assert candidate['vendor_id'] == row['security_id']
            assert candidate['name'] == row['label']
            assert candidate['identity_status'] == candidate['entitlement_status'] == 'UNVERIFIED'
            assert candidate['permitted_firm_ids'] == candidate['permitted_principal_classes'] == []
            assert candidate['verification_ref'] is None
            assert 'ed18c59c86ef89b33eb4759f0d2a939b964e5ac8' in candidate['mapping_evidence']
            return dict(key=row['key'], historical_id=row['security_id'], current_authorization='NONE_DECLARED')
        check('historical_unverified_candidate_' + row['key'], inspect)
    assert len(catalogue['entries']) == 4
    assert catalogue['admission'] == 'UNVERIFIED_CURRENT_IDENTITY_AND_ENTITLEMENT'
    doc = dict(recipient_pin=pin, catalogue_pin=catalogue_pin, source_sha256=hashes,
        catalogue_sha256=hashlib.sha256(cat_bytes).hexdigest(), historical_blob='ed18c59c86ef89b33eb4759f0d2a939b964e5ac8',
        supplied=dict(exit_code=suite.returncode, stdout=suite.stdout, stderr=suite.stderr), results=results,
        limitations=['Application validator and static candidate data only',
                     '200 codepoint application cap is not independent proof of vendor/render text limits',
                     'Hostile text is preserved as data; render escaping not executed',
                     'No canonical composition persistence, resolver admission, worker, cover, UI or live entitlement grade'])
    (own / 'RECIPIENT_CATALOGUE_70ea_9daa.json').write_text(json.dumps(doc, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(dict(recipient_pin=pin, catalogue_pin=catalogue_pin, supplied=suite.stdout, results=results), indent=2))
    return int(any(r['outcome'] == 'FAIL' for r in results))


if __name__ == '__main__':
    raise SystemExit(main())
