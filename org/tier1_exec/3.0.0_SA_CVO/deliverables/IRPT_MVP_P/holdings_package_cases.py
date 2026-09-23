"""Additional controls executed inside the exact flat package after supplied setup."""
import fnmatch
import io
import json
import os
import sys

import entry
import loaders
import publication
import selection_store

# The runner appends these cases to the pinned producer's setup in one namespace.
ownership, accounts, s3, doc, event, selected, firm, flat = (
    globals()[name] for name in ('ownership', 'accounts', 's3', 'doc', 'event', 'selected', 'firm', 'flat'))

ownership['advisors']['advisor']['accounts'] = list(accounts)
s3.revoke = False
checks = []
for field, value in [('snapshot_fixture', doc), ('resolved_scope', {}), ('object_id', 'foreign')]:
    s3.calls.clear()
    refused = entry.lambda_handler({**event, field: value})
    assert refused.get('ok') is False and 'data' not in refused
    assert not s3.calls
    checks.append('injected_' + field + '_zero_product_reads')
s3.calls.clear()
refused = entry.lambda_handler({**event, 'pathParameters': {'accountSetId': 'sel_' + '0' * 64}})
assert refused.get('ok') is False and 'data' not in refused and not s3.calls
checks.append('missing_selection_zero_product_reads')

class DynamoSpy:
    def __init__(self):
        self.calls = []

    def get_item(self, **kwargs):
        self.calls.append(kwargs)
        return {'Item': {'selection_record': {'S': json.dumps({'accepted': True})}}}

dyn = DynamoSpy()
assert selection_store.SelectionStore(dyn, 'pinned-requests').load(firm, selected['account_set_id']) == {'accepted': True}
assert dyn.calls == [{'TableName': 'pinned-requests', 'ConsistentRead': True, 'Key': {
    'tenant': {'S': firm}, 'request_revision': {'S': 'SELECTION#' + selected['account_set_id']}}}]
checks.append('actual_selection_store_tenant_consistent_getitem')

class ScopeSpy:
    def __init__(self, expected_bucket):
        self.expected_bucket = expected_bucket
        self.calls = []

    def get_object(self, **kwargs):
        assert kwargs['Bucket'] == self.expected_bucket
        assert set(kwargs) == {'Bucket', 'Key'}
        self.calls.append(kwargs)
        result = {'key': 'investor-reporting/directory/revision.json'} if kwargs['Key'].endswith('/latest.json') else {}
        return {'Body': io.BytesIO(json.dumps(result).encode())}

identity = json.loads((flat / 'firm_registry.json').read_text())['firms']
identity = [row for row in identity if row['kind'] == 'client' and row['enabled']]
os.environ['IRPT_DIRECTORY_BUCKET_MAP'] = json.dumps({row['firm_id']: row['bucket'] for row in identity})
scope_calls = {}
for row in identity:
    spy = ScopeSpy(row['bucket'])
    loaders.load_directory(row['firm_id'], s3=spy)
    loaders.load_ownership(row['firm_id'], s3=spy)
    expected = ['investor-reporting/directory/latest.json', 'investor-reporting/directory/revision.json',
                'platinum/' + row['firm_id'] + '/ownership_map.json']
    assert [call['Key'] for call in spy.calls] == expected
    scope_calls[row['firm_id']] = spy.calls
checks.append('actual_scope_loader_calls_all_enabled_identity_firms')

registry_rows = json.loads((flat / 'infra/logic/registry/scopes.json').read_text())['scopes']
registry_rows = [row for row in registry_rows if row['class'] == 'FIRM'
                 and row.get('tenant', {}).get('kind') == 'client' and row.get('tenant', {}).get('enabled')]
assert {row['long'] for row in registry_rows} == {'49financial', 'cottonwood', 'inflection'}
product_locations = {}
for row in registry_rows:
    owner = publication.HoldingsPublication(s3, row['long'])
    current = owner.location('platinum', 'current', 'manifest.json')
    version = owner.location('platinum', 'date=2026-09-22', 'a' * 64 + '.manifest.json')
    assert current == (row['bucket'], 'irpt/' + row['long'] + '/platinum/holdings/current/manifest.json')
    pattern = 'irpt/' + row['long'] + '/platinum/holdings/date=*/*'
    assert version[0] == row['bucket'] and fnmatch.fnmatchcase(version[1], pattern)
    for disallowed in [current[1], version[1].replace('/platinum/', '/gold/'),
                       version[1].replace('/holdings/', '/holdings_qa/')]:
        assert not fnmatch.fnmatchcase(disallowed, pattern)
    product_locations[row['long']] = {'current': current, 'version': version, 'version_key_pattern': pattern}
checks.append('canonical_product_locations_and_negative_resource_patterns')
assert 'pyarrow' not in sys.modules
print(json.dumps({'additional_checks': checks, 'scope_calls': scope_calls,
                  'product_locations': product_locations, 'network': False}))
