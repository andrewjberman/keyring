"""Run captured old Positioning source with current inputs; intercept ALL S3 writes."""
import boto3
import gzip
import hashlib
import importlib.util
import json
import os
import sys
import zipfile
from pathlib import Path

from verify_published import diff, read_json

root = Path(sys.argv[1])
os.environ['AWS_LAMBDA_FUNCTION_NAME'] = 'yang-generate-positioning'
target = root / 'old_positioning_control'
target.mkdir(exist_ok=True)
with zipfile.ZipFile(root / 'yang-generate-positioning_before.zip') as archive:
    for name in ['lambda_function.py', 'etf_classifications_dynamodb.py']:
        (target / name).write_bytes(archive.read(name))
sys.path.insert(0, str(target))

after = read_json(root / 'after_opal_aggregate.json')
aum = after['weights_source']
real_client = boto3.client
real_s3 = real_client('s3', region_name='us-east-1')
reads = []
writes = {}


class S3ReadOnly:
    def get_object(self, **kwargs):
        if kwargs['Key'] == aum['key']:
            kwargs['VersionId'] = aum['version_id']
        response = real_s3.get_object(**kwargs)
        reads.append(dict(bucket=kwargs['Bucket'], key=kwargs['Key'], version=response.get('VersionId')))
        return response

    def put_object(self, **kwargs):
        key = kwargs['Key']
        assert key in ['json/positioning/positioning_data.json', 'json/positioning/opal_aggregate.json']
        writes[key] = kwargs['Body']
        (root / ('control_' + key.split('/')[-1])).write_bytes(kwargs['Body'])
        return {'ResponseMetadata': {'HTTPStatusCode': 200}}

    def __getattr__(self, name):
        assert name.startswith(('get_', 'head_', 'list_')), ('Refused S3 action', name)
        return getattr(real_s3, name)


def read_client(service, *args, **kwargs):
    return S3ReadOnly() if service == 's3' else real_client(service, *args, **kwargs)


boto3.client = read_client
spec = importlib.util.spec_from_file_location('old_positioning', target / 'lambda_function.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
event = json.loads((root / 'after.json').read_text())['event']
module.lambda_handler(event, None)
report = {'control': 'Pre-deploy source replay; S3 writes intercepted locally; AUM version pinned',
          'old_handler_sha256': hashlib.sha256((target / 'lambda_function.py').read_bytes()).hexdigest(),
          'reads': reads, 'surfaces': {}}
for key, body in writes.items():
    filename = key.split('/')[-1]
    control = json.loads(gzip.decompress(body))
    published = read_json(root / ('after_' + filename))
    changes = diff(control, published)
    unexpected = [r for r in changes if '/returns/' not in r['path'] and r['path'] != '/generated_at']
    report['surfaces'][filename] = {'differences': len(changes), 'non_return_mismatches': unexpected}
output = Path(sys.argv[2])
output.write_text(json.dumps(report, indent=2) + '\n', encoding='utf8')
print(json.dumps(report, indent=2))
assert len(writes) == 2
assert all(not r['non_return_mismatches'] for r in report['surfaces'].values())
