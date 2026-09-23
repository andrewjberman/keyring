"""C1 exact-byte preflight/upload verification. Never rebuilds or updates Lambda."""
import argparse
import base64
import datetime
import hashlib
import json
from pathlib import Path

import boto3

BUCKET = 'opal-313476888478-lambda-artifacts'
KEY = 'research/opal-amgt-scoped-api.zip'
FUNCTION = 'opal-amgt-scoped-api'
EXPECTED = '0c44108821fe52850c77b119490039453b082c3639fae6dbf58de054b1397a55'
BASELINE = 'r93CxQqrk8k8h2Q8KO4Iicn3pk8kyF4SFo47a9Cca5w='
REVISION = 'd906e911-aed5-4e21-afcd-0b9a6dcdbdc7'
HOME = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['preflight', 'upload', 'verify-deployed'])
    args = parser.parse_args()
    raw = Path('C:/tmp/amgt-r-no-span-package-20260923/candidate.zip').read_bytes()
    digest = hashlib.sha256(raw).digest()
    encoded = base64.b64encode(digest).decode()
    assert digest.hex() == EXPECTED and len(raw) == 807904
    assert hashlib.md5(raw).hexdigest() == 'cb90ed8636c79c9dbc29120923349bc5'
    account = boto3.client('sts', region_name='us-east-1').get_caller_identity()['Account']
    assert account == '313476888478'
    client = boto3.client('lambda', region_name='us-east-1')
    config = client.get_function_configuration(FunctionName=FUNCTION)
    report = {'observed_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'mode': args.mode, 'account': account, 'function': FUNCTION,
              'live_code_sha256': config['CodeSha256'], 'live_revision_id': config['RevisionId'],
              'candidate_sha256': EXPECTED, 'candidate_code_sha256': encoded,
              'candidate_size': len(raw), 'candidate_md5': hashlib.md5(raw).hexdigest(),
              'bucket': BUCKET, 'key': KEY, 'upload_performed': False}
    if args.mode != 'verify-deployed':
        assert config['CodeSha256'] == BASELINE, 'STOP: live code baseline changed'
        assert config['RevisionId'] == REVISION, 'STOP: live RevisionId changed'
        overrides = [key for key in config.get('Environment', {}).get('Variables', {})
                     if key in ['AMGT_DRAFTING_ROOT', 'AMGT_DRAFTING_BUCKET', 'AMGT_DRAFTING_PREFIX']]
        assert not overrides, 'STOP: drafting override requires re-review'
    else:
        assert config['CodeSha256'] == encoded, 'STOP: deployed code does not match candidate'
        assert config['LastUpdateStatus'] == 'Successful'
        assert config['State'] == 'Active'
    s3 = boto3.client('s3', region_name='us-east-1')
    before = s3.get_object(Bucket=BUCKET, Key=KEY)
    prior = before['Body'].read()
    report['s3_before'] = {'sha256': hashlib.sha256(prior).hexdigest(),
                           'size': len(prior), 'version_id': before.get('VersionId'),
                           'metadata_code_sha256': before.get('Metadata', {}).get('content-sha256')}
    expected_object = encoded if args.mode == 'verify-deployed' else BASELINE
    assert base64.b64encode(hashlib.sha256(prior).digest()).decode() == expected_object, 'STOP: S3 object baseline changed'
    assert before.get('Metadata', {}).get('content-sha256') == expected_object, 'STOP: S3 metadata drift'
    if args.mode == 'upload':
        ledger = next(p for p in HOME.parents if (p / '.git').exists()) / 'org/critical_paths/change_management/20260923T215256Z_amgt_exact_nospan_C1_cutover.md'
        assert 'Status: OPEN' in ledger.read_text(encoding='utf-8'), 'STOP: act ledger is not open'
        receipt = s3.put_object(Bucket=BUCKET, Key=KEY, Body=raw,
                                ContentMD5=base64.b64encode(hashlib.md5(raw).digest()).decode(),
                                Metadata={'content-sha256': encoded})
        report['upload_performed'] = True
        report['uploaded_version_id'] = receipt.get('VersionId')
        # Preserve the receipt before any verification can fail.
        (HOME / 'C1_UPLOAD_RECEIPT.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
        head = s3.head_object(Bucket=BUCKET, Key=KEY)
        assert head['ContentLength'] == len(raw)
        assert head['Metadata']['content-sha256'] == encoded
        assert head['ETag'].strip('"') == hashlib.md5(raw).hexdigest()
        stored = s3.get_object(Bucket=BUCKET, Key=KEY)
        assert stored['Body'].read() == raw, 'STOP: stored bytes do not equal candidate'
        assert stored.get('VersionId') == receipt.get('VersionId')
        report['s3_verified'] = {'size': head['ContentLength'], 'etag': head['ETag'],
                                 'content_sha256': head['Metadata']['content-sha256'],
                                 'version_id': head.get('VersionId'), 'exact_bytes_equal': True}
    (HOME / ('C1_' + args.mode.upper().replace('-', '_') + '.json')).write_text(
        json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
