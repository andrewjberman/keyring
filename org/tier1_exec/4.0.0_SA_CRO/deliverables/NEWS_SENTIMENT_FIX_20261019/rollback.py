"""Scoped rollback preparation. Verify by default; mutations require --execute.

Lambda code is restored through versioned artifact uploads followed by safe-apply,
never direct update-function-code. Data journals contain DynamoDB wire values.
"""
import argparse
import base64
import hashlib
import json
from pathlib import Path

import boto3

ROOT = Path(__file__).resolve().parents[5]
SCRATCH = ROOT / '.runtime/news-sentiment-fix-20261019'
FUNCTIONS = {
    'finbert-batch-processor': 'news-pipeline',
    'news-trending-analysis': 'news-pipeline',
    'opal-news-layer3-curation': 'news-pipeline',
    'opal-trending-topics-portal-publisher': 'market-overview',
}


def restore_attribute(client, entry, execute=False):
    current = client.get_item(TableName=entry['table'], Key=entry['key'], ConsistentRead=True).get('Item', {})
    attribute = entry['attribute']
    if current.get(attribute) == entry.get('before'):
        return 'already_restored'
    if current.get(attribute) != entry['after']:
        raise ValueError('concurrent_writer: refusing to overwrite ' + attribute)
    if execute:
        values = {':after': entry['after']}
        expression = 'REMOVE #field'
        if entry.get('before') is not None:
            values[':before'] = entry['before']
            expression = 'SET #field = :before'
        client.update_item(TableName=entry['table'], Key=entry['key'], UpdateExpression=expression,
                           ConditionExpression='#field = :after', ExpressionAttributeNames={'#field': attribute},
                           ExpressionAttributeValues=values)
    return 'restored' if execute else 'verified'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=['verify', 'stage-code', 'data'])
    parser.add_argument('--execute', action='store_true')
    args = parser.parse_args()
    manifest = json.loads((SCRATCH / 'backup/manifest.json').read_text())
    for name in FUNCTIONS:
        package = (SCRATCH / 'backup' / (name + '.zip')).read_bytes()
        if hashlib.sha256(package).hexdigest() != manifest[name]['sha256']:
            raise ValueError('backup_hash_mismatch: ' + name)
        print('BACKUP VERIFIED', name)
    if args.mode == 'verify':
        return
    if args.mode == 'data':
        client = boto3.client('dynamodb', region_name='us-east-1')
        for path in sorted((SCRATCH / 'journals').glob('*.json')):
            for entry in json.loads(path.read_text()):
                print(path.name, entry['attribute'], restore_attribute(client, entry, args.execute))
        return
    # release.json is written only after deployment readback, with exact deployed code hashes.
    release = json.loads((SCRATCH / 'release.json').read_text())
    lam = boto3.client('lambda', region_name='us-east-1')
    s3 = boto3.client('s3', region_name='us-east-1')
    bucket = 'opal-313476888478-lambda-artifacts'
    for name, pipeline in FUNCTIONS.items():
        live = lam.get_function_configuration(FunctionName=name)
        expected = release[name]['code_sha256']
        if live['CodeSha256'] != expected:
            raise ValueError('concurrent_code_writer: ' + name)
        key = pipeline + '/' + name + '.zip'
        current = s3.head_object(Bucket=bucket, Key=key)
        if current.get('Metadata', {}).get('content-sha256') != expected:
            raise ValueError('concurrent_artifact_writer: ' + name)
        if args.execute:
            package = (SCRATCH / 'backup' / (name + '.zip')).read_bytes()
            sha = base64.b64encode(hashlib.sha256(package).digest()).decode()
            s3.put_object(Bucket=bucket, Key=key, Body=package, ContentType='application/zip',
                          Metadata={'content-sha256': sha}, IfMatch=current['ETag'])
        print('RESTORE ARTIFACT' if args.execute else 'VERIFIED ARTIFACT', name)
    print('Next: targeted Terraform plan; inspect code-only changes; safe-apply saved plan; verify baseline CodeSha256.')


if __name__ == '__main__':
    main()
