"""Land the two retained Holdings inputs in S3 (CTO R4 ruling, msg 100965): the 49F Tax SMA workbook projection and
the INF Eclipse membership map. Until now each existed only as a local file, so a scheduled host build could not
read it.

Every key is lib/opal_naming.address() output, under the owning firm's key prefix: `gateway` for the workbook read
through the opalgateway, `eclipse` for the Eclipse map. Each capture lands beside a manifest.json that carries its
source, its capture time (with the time's claim), sha256, bytes and rows. The capture files are copied byte for byte,
never re-serialised. Every put is IfNoneMatch='*', a new object only, and the script refuses rather than overwrite.

Usage (from the worktree root): python org/.../IRPT_MVP_M/land_retained_inputs.py --receipt <json>
"""
import argparse
import datetime as dt
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip())
sys.path.insert(0, str(ROOT))
WS = Path('C:/Users/AndrewBerman/Desktop/ajb_workspace')  # the captures live in the shared tree's .runtime (gitignored)
RULING = '1.0.0_SA_CTO msg 100965 (R4): land both retained inputs in S3; the build reads latest-at-or-before D'


def captures():
    tax = WS / '.runtime/cro-m-taxsma-20260923/taxsma_workbook_projected_snapshot.json'
    ecl = WS / '.runtime/codex-seats/4.0.0_SA_CRO/eclipse_membership/membership_map.json'
    tax_doc = json.loads(tax.read_bytes())
    ecl_mtime = dt.datetime.fromtimestamp(ecl.stat().st_mtime, dt.timezone.utc).replace(microsecond=0)
    return [
        {'name': 'IRPT_49F_TAX_MEMBERSHIP_SNAPSHOT', 'path': tax, 'object': 'taxsma_workbook_projected_snapshot.json',
         'address': ('gateway', '49financial', 'bronze', 'taxsma_workbook_projection',
                     'date=' + tax_doc['observed_at_utc'][:10]),
         'captured_at_utc': tax_doc['observed_at_utc'], 'captured_at_claim': 'measured (the capture\'s own observed_at_utc)',
         'source': tax_doc.get('source'), 'reader': tax_doc.get('reader'), 'contract': tax_doc.get('contract'),
         'rows': len(tax_doc.get('rows', []))},
        {'name': 'IRPT_INF_ECLIPSE_MEMBERSHIP_SNAPSHOT', 'path': ecl, 'object': 'membership_map.json',
         'address': ('eclipse', 'inflection', 'bronze', 'eclipse_membership_map', 'date=' + ecl_mtime.date().isoformat()),
         'captured_at_utc': ecl_mtime.isoformat().replace('+00:00', 'Z'),
         'captured_at_claim': 'inferred (the local file mtime; the capture carries no time of its own)',
         'source': 'Eclipse portfolio membership API, 9 batches (receipts.json beside the capture: 858 ids, all status 200)',
         'reader': '4.0.0_SA_CRO codex seat', 'contract': None, 'rows': len(json.loads(ecl.read_bytes()))},
    ]


def main():
    import boto3
    from lib.opal_naming import address
    ap = argparse.ArgumentParser()
    ap.add_argument('--receipt', required=True)
    args = ap.parse_args()
    s3 = boto3.client('s3', region_name='us-east-1')
    landed = []
    for c in captures():
        body = c['path'].read_bytes()
        sha = hashlib.sha256(body).hexdigest()
        uri = address(*c['address'], c['object'])
        bucket, key = uri[len('s3://'):].split('/', 1)
        manifest = {'input': c['name'], 'object': key, 'sha256': sha, 'bytes': len(body), 'rows': c['rows'],
                    'captured_at_utc': c['captured_at_utc'], 'captured_at_claim': c['captured_at_claim'],
                    'source': c['source'], 'reader': c['reader'], 'contract': c['contract'],
                    'origin_local_path': str(c['path']).replace('\\', '/'), 'landed_by': '2.0.0_SA_COO~M',
                    'landed_at_utc': dt.datetime.now(dt.timezone.utc).isoformat(), 'ruling': RULING}
        mkey = key.rsplit('/', 1)[0] + '/manifest.json'
        for k, b, ctype in ((key, body, 'application/json'),
                            (mkey, (json.dumps(manifest, indent=1) + '\n').encode('utf-8'), 'application/json')):
            try:
                s3.put_object(Bucket=bucket, Key=k, Body=b, ContentType=ctype, IfNoneMatch='*')
            except s3.exceptions.ClientError as exc:
                raise SystemExit('REFUSED: %s exists or cannot be written (%s) -- new objects only' % (k, exc))
        got = s3.get_object(Bucket=bucket, Key=key)
        back = got['Body'].read()
        landed.append({'input': c['name'], 'bucket': bucket, 'key': key, 'manifest_key': mkey,
                       'version_id': got.get('VersionId'), 'sha256': sha, 'read_back_equal': back == body,
                       'bytes': len(body), 'rows': c['rows'], 'captured_at_utc': c['captured_at_utc'],
                       'captured_at_claim': c['captured_at_claim']})
    Path(args.receipt).write_text(json.dumps({'ruling': RULING, 'landed': landed}, indent=1) + '\n', encoding='utf-8')
    for x in landed:
        print('OK: s3://%s/%s  %d bytes  read-back %s' % (x['bucket'], x['key'], x['bytes'], x['read_back_equal']))


if __name__ == '__main__':
    main()
