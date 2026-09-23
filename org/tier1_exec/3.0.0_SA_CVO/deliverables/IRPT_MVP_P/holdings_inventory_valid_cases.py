"""Valid digest types remain accepted without fetching unselected bytes."""
import copy
import json

import entry

baseline, s3, event, accounts, unselected_number, unselected_keys, pin_inventory = (
    globals()[name] for name in ('baseline', 's3', 'event', 'accounts', 'unselected_number',
                                 'unselected_keys', 'pin_inventory'))
valid_results = []
for target in ('unselected_part', 'gold'):
    for digest_value in ('1' * 64, 'abcdef01' * 8):
        candidate = copy.deepcopy(baseline)
        reference = (candidate['partitions'][unselected_number]['object']
                     if target == 'unselected_part' else candidate['gold'])
        reference['sha256'] = digest_value
        pin_inventory(candidate)
        s3.calls.clear()
        response = entry.lambda_handler(event)
        assert response['data']['scope']['account_ids'] == [accounts[0]]
        assert len(s3.calls) == 4
        assert all(call['VersionId'] == 'version-1' for call in s3.calls[1:])
        assert not any(call['Key'] in unselected_keys or call['Key'].endswith('.parquet')
                       for call in s3.calls)
        valid_results.append({'target': target, 'digest': digest_value, 'pass': True})
pin_inventory(baseline)
print(json.dumps({'independent_valid_digest_controls': valid_results, 'network': False}))
