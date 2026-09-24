"""Unchanged candidate assertions for real guarded resolve/bootstrap contract."""
import copy
import json
from pathlib import Path

import pytest

import test_selection_contract as contract


@pytest.fixture(scope='module')
def captures():
    producer = contract.producer
    entry = producer.entry
    request = json.loads((Path.cwd() / 'bootstrap-request.json').read_bytes())
    mp = pytest.MonkeyPatch()
    seed, rows, a, b, relation = producer.setup_entry(mp)
    # Only external dependencies change. ENTRY, resolve, handler, guard and envelope stay real.
    mp.setattr(entry.ENTRY, 'deps', seed.deps)
    mp.setattr(entry.ENTRY, 'opaque_firm_for', seed.opaque_firm_for)
    headers = producer.request('ACCOUNT', [a])['headers']
    headers.update(request.get('headers', {}))
    event = {'version': '2.0', 'routeKey': request['method'] + ' ' + request['url'],
             'headers': headers, 'body': request['body']}
    cases = {}
    for role in ('advisor', 'operations'):
        ev = copy.deepcopy(event)
        if role == 'operations':
            ev['headers']['x-user-role'] = 'admin'
        cases[role] = entry.ENTRY.handle(ev)
    flat = copy.deepcopy(event)
    flat['body'] = json.dumps(dict(json.loads(event['body']), account_ids=[a]))
    nested = copy.deepcopy(event)
    nested['body'] = json.dumps({'selection': {'account_ids': [a]}})
    cases['flat_account'] = entry.ENTRY.handle(flat)
    cases['nested_diagnostic'] = entry.ENTRY.handle(nested)
    negatives = {}
    for name in ('unverified_origin', 'missing_firm', 'foreign_firm', 'unknown_advisor', 'wrong_version'):
        ev = copy.deepcopy(event)
        if name == 'unverified_origin':
            ev['headers']['x-origin-verify'] = ''
        elif name == 'missing_firm':
            ev['headers'].pop('x-firm-id')
        elif name == 'foreign_firm':
            ev['body'] = json.dumps(dict(json.loads(event['body']), firm_id='foreign-firm'))
        elif name == 'unknown_advisor':
            ev['headers']['x-advisor-id'] = 'foreign-advisor'
        else:
            ev['headers']['x-contract-version'] = 'unsupported'
        negatives[name] = entry.ENTRY.handle(ev)
    selection = seed.handle(producer.request('ACCOUNT', [a]))
    output = {'request': request, 'cases': cases, 'negatives': negatives,
              'selection_positive': selection, 'expected_accounts': [a, b]}
    (Path.cwd() / 'bootstrap-actual.json').write_text(json.dumps(output, indent=2) + '\n', encoding='utf-8')
    mp.undo()
    return output


@pytest.mark.parametrize('role', ['advisor', 'operations'])
def test_real_bootstrap_matches_published_response(captures, role):
    answer = captures['cases'][role]
    assert 'data' in answer, answer
    contract.validator('responses/resolve-scope.response.schema.json').validate(answer)


@pytest.mark.parametrize('role', ['advisor', 'operations'])
def test_real_bootstrap_preserves_verified_permitted_accounts(captures, role):
    data = captures['cases'][role]['data']
    assert data.get('permitted_account_set') == captures['expected_accounts'], data
    assert data['viewer_policy']['policy_id']
    assert data['principal_class'] == ('FIRM_ADVISOR' if role == 'advisor' else 'FIRM_OPERATIONS')


def test_flat_requested_accounts_are_recorded(captures):
    data = captures['cases']['flat_account']['data']
    assert data.get('requested_scope') == {
        'scope_kind': 'ACCOUNT', 'scope_ids': captures['expected_accounts'][:1]}, data


@pytest.mark.parametrize('name', ['unverified_origin', 'missing_firm', 'foreign_firm', 'unknown_advisor', 'wrong_version'])
def test_auth_negative_remains_public_refusal(captures, name):
    answer = captures['negatives'][name]
    assert answer['ok'] is False and 'data' not in answer
    contract.validator('BoundaryRefusal.schema.json').validate(answer)
    assert 'internal_correlation_id' not in answer['status']


def test_existing_real_selected_set_positive(captures):
    answer = captures['selection_positive']
    contract.validator('responses/selection-create.response.schema.json').validate(answer)
    assert answer['data']['selected_account_ids'] == captures['expected_accounts'][:1]
