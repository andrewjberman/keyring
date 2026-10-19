"""Read-only before-images for the authorized News Scanner repair."""
import hashlib
import json
from pathlib import Path
from urllib.request import urlopen

import boto3

ROOT = Path('.runtime/news-sentiment-fix-20261019/backup')
FUNCTIONS = ['finbert-batch-processor', 'news-trending-analysis',
             'opal-news-layer3-curation', 'opal-trending-topics-portal-publisher']


def main():
    ROOT.mkdir(parents=True, exist_ok=True)
    client = boto3.client('lambda', region_name='us-east-1')
    manifest = {}
    for name in FUNCTIONS:
        path = ROOT / (name + '.zip')
        if path.exists():
            raise RuntimeError('Refusing to overwrite baseline: ' + str(path))
        result = client.get_function(FunctionName=name)
        with urlopen(result['Code']['Location'], timeout=120) as response:
            data = response.read()
        path.write_bytes(data)
        config = result['Configuration']
        (ROOT / (name + '.config.json')).write_text(json.dumps(config, default=str, indent=2))
        manifest[name] = {'sha256': hashlib.sha256(data).hexdigest(),
                          'code_sha256': config['CodeSha256'], 'revision': config['RevisionId'],
                          'last_modified': config['LastModified'], 'bytes': len(data)}
    s3 = boto3.client('s3', region_name='us-east-1')
    for bucket, key, filename in [
        ('opal-data-portal-v2', 'json/trending/latest.json', 'portal-before.json'),
        ('opal-data-news-v2', 'trending_reports/latest.json', 'layer2-before.json'),
    ]:
        response = s3.get_object(Bucket=bucket, Key=key)
        data = response['Body'].read()
        (ROOT / filename).write_bytes(data)
        manifest[filename] = {'bucket': bucket, 'key': key, 'version': response.get('VersionId'),
                              'sha256': hashlib.sha256(data).hexdigest()}
    (ROOT / 'manifest.json').write_text(json.dumps(manifest, indent=2))
    print(json.dumps(manifest, indent=2))


if __name__ == '__main__':
    main()
