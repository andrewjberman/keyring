"""Additional multipart controls following the unchanged seven package controls."""
import json

import enforce
import entry
import selection

accounts, s3, manifest, event, firm, headers, directory, ownership = (
    globals()[name] for name in ('accounts', 's3', 'manifest', 'event', 'firm', 'headers', 'directory', 'ownership'))
rows = globals()['rows']
parts = manifest['partitions']
missing = [p['object'] for p in parts if accounts[0] not in p['account_ids']]
assert missing
removed = {(ref['bucket'], ref['key']): s3.rows.pop((ref['bucket'], ref['key'])) for ref in missing}
try:
    s3.calls.clear()
    answer = entry.lambda_handler(event)
    assert answer['data']['scope']['account_ids'] == [accounts[0]]
    assert not {key for _, key in removed}.intersection(call['Key'] for call in s3.calls)
finally:
    s3.rows.update(removed)

guard, context = entry.ENTRY.enforcer_for(firm)
scope, refusal = guard.resolve_now(enforce.Request(headers, 'holdings_snapshot'))
assert refusal is None
selected = selection.create_selection(scope, directory, accounts,
    directory_revision=selection.directory_revision(directory),
    save_selection=lambda tenant, ref, record: rows.update({(tenant, ref): record}))
whole_event = {**event, 'pathParameters': {'accountSetId': selected['account_set_id']}}
s3.calls.clear()
answer = entry.lambda_handler(whole_event)
assert set(answer['data']['scope']['account_ids']) == set(accounts)
needed = [part for part in parts if set(accounts).intersection(part['account_ids'])]
assert len(needed) > 1
assert len(s3.calls) == 3 + len(needed)
assert {part['object']['key'] for part in needed} <= {call['Key'] for call in s3.calls}
assert all(call['VersionId'] == 'version-1' for call in s3.calls[1:])

last = needed[-1]['object']
location = (last['bucket'], last['key'])
saved = s3.rows[location]
try:
    s3.rows[location] = saved + b'corrupted-selected-part'
    s3.calls.clear()
    answer = entry.lambda_handler(whole_event)
    assert answer.get('ok') is False and 'data' not in answer
    assert needed[0]['object']['key'] in [call['Key'] for call in s3.calls]
finally:
    s3.rows[location] = saved
print(json.dumps({'multipart_checks': ['missing_unselected_blob_not_read',
    'complete_selected_parts_versioned_exact_read_count', 'later_selected_corruption_no_partial_release'],
    'selected_parts': len(needed), 'network': False}))
