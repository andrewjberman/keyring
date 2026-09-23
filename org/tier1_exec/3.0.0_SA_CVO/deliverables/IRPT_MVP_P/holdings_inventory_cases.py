"""Independently repin complete-inventory metadata through the packaged Entry."""
import copy
import json

import entry
import publication

accounts, s3, manifest, event, store, date, revision = (
    globals()[name] for name in ('accounts', 's3', 'manifest', 'event', 'store', 'date', 'revision'))
baseline = copy.deepcopy(manifest)
unselected_number = next(i for i, part in enumerate(baseline['partitions'])
                         if accounts[0] not in part['account_ids'])
unselected_keys = {part['object']['key'] for part in baseline['partitions']
                   if accounts[0] not in part['account_ids']}


def pin_inventory(candidate):
    location = store.location('platinum', 'date=' + date, revision + '.manifest.json')
    manifest_reference = s3.add(location, publication.canonical_bytes(candidate))
    index = {'schema_version': 'irpt-holdings-index-v1', 'firm_id': store.firm,
             'latest_date': date, 'dates': {date: {'revision': revision, 'manifest': manifest_reference}}}
    s3.add(store.location('platinum', 'current', 'manifest.json'), publication.canonical_bytes(index))


results = []
for target in ('unselected_part', 'gold'):
    mutations = [('missing_reference', None, None), ('null_reference', None, None),
                 ('foreign_bucket', 'bucket', 'other-tenant'), ('foreign_key', 'key', 'wrong'),
                 ('null_version', 'version_id', None), ('literal_null_version', 'version_id', 'null'),
                 ('numeric_digest', 'sha256', int('1' * 64)), ('short_digest', 'sha256', 'abc'),
                 ('boolean_length', 'byte_length', True), ('string_length', 'byte_length', '1'),
                 ('zero_length', 'byte_length', 0)]
    for label, field, value in mutations:
        candidate = copy.deepcopy(baseline)
        container = candidate['partitions'][unselected_number] if target == 'unselected_part' else candidate
        key = 'object' if target == 'unselected_part' else 'gold'
        if label == 'missing_reference':
            container.pop(key)
        elif label == 'null_reference':
            container[key] = None
        else:
            container[key][field] = value
        pin_inventory(candidate)
        s3.calls.clear()
        response = entry.lambda_handler(event)
        private_reads = [call['Key'] for call in s3.calls
                         if call['Key'] in unselected_keys or call['Key'].endswith('.parquet')]
        refused = response.get('ok') is False and 'data' not in response
        results.append({'case': target + '_' + label, 'pass': refused and not private_reads,
                        'whole_response_refused': refused, 'unselected_or_gold_reads': private_reads,
                        'read_count': len(s3.calls), 'response_ok': response.get('ok'),
                        'data_released': 'data' in response})
pin_inventory(baseline)
s3.calls.clear()
valid = entry.lambda_handler(event)
assert valid['data']['scope']['account_ids'] == [accounts[0]]
print(json.dumps({'independent_inventory_cases': results, 'valid_restored_control': True,
                  'all_mutations_manifest_and_index_repinned': True, 'network': False}))
assert all(row['pass'] for row in results), [row['case'] for row in results if not row['pass']]
