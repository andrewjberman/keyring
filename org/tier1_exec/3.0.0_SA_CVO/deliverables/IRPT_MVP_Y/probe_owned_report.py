"""Pinned owned report reader and READY receipt validation; offline only."""
import argparse
import copy
import hashlib
import io
import json
import os
from pathlib import Path
import socket
import subprocess
import sys
import zipfile

from probe_recipe_decimal import deny_network, load


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--pin', default='9ac485733e')
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[5]
    pin = subprocess.check_output(['git', 'rev-parse', args.pin], cwd=root, text=True).strip()
    target = root / '.runtime/codex-seats/3.0.0_SA_CVO~Y/owned-report-review' / pin
    target.mkdir(parents=True, exist_ok=True)
    prefix = 'infra/aws/lambda/investor-reporting'
    archive = subprocess.check_output(['git', 'archive', '--format=zip', pin, prefix,
        'docs/contracts/investor-reporting', 'data/firm_registry.json'], cwd=root)
    hashes = {}
    with zipfile.ZipFile(io.BytesIO(archive)) as bundle:
        for member in bundle.infolist():
            path = (target / member.filename).resolve()
            if not path.is_relative_to(target.resolve()):
                raise ValueError('snapshot escape')
            if member.is_dir():
                path.mkdir(parents=True, exist_ok=True)
            else:
                data = bundle.read(member)
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(data)
                hashes[member.filename] = hashlib.sha256(data).hexdigest()
    socket.socket.connect = deny_network
    socket.socket.connect_ex = deny_network
    socket.create_connection = deny_network
    os.environ['IRPT_FIRM_REGISTRY'] = str(target / 'data/firm_registry.json')
    source = target / prefix
    sys.path.insert(0, str(source / 'ops/tests'))
    subject = load('owned_report_source_tests', source / 'ops/tests/test_owned_report.py')
    durable = sys.modules['durable_job']
    results = []

    def world():
        w = subject.world.__wrapped__(subject.retention_world.__wrapped__())
        return subject.report_world.__wrapped__(w)

    def record(name, passed, **observed):
        results.append(dict(name=name, outcome='PASS' if passed else 'FAIL', **observed))

    def refuses(name, r, expected=subject.owned_report.RequestReadRefused):
        try:
            value = r.reader.read(r.w.case.principal, r.id)
            record(name, False, returned_complete_report=value == r.report)
        except expected as error:
            record(name, True, exception=type(error).__name__, reason=str(error))

    r = world()
    value = r.reader.read(r.w.case.principal, r.id)
    original = copy.deepcopy(value)
    value['request_ref']['request_revision'] = 99
    record('full_schema_report_and_returned_copy_isolation',
           original == r.report and r.reader.read(r.w.case.principal, r.id) == original,
           job_reads=len(r.calls), request_ref=original['request_ref'])

    # Same hexadecimal characters: accepted digest string versus noncompliant JSON number.
    r = world()
    detail = dict(r.detail, certification_sha256='1' * 64)
    r.job['job_detail']['S'] = json.dumps(detail)
    record('string_certification_digest_positive_control',
           r.reader.read(r.w.case.principal, r.id) == r.report)
    detail['certification_sha256'] = int('1' * 64)
    r.job['job_detail']['S'] = json.dumps(detail)
    refuses('numeric_certification_digest_must_refuse', r)
    store = durable.DynamoGenerationStore(r.client, tenant=r.w.case.principal['firm_id'],
        request_id=r.id, composition_sha256=r.record['composition_ref']['sha256'])
    try:
        store.put_state(r.id, 'READY', detail)
        record('canonical_READY_writer_rejects_same_numeric_digest', False)
    except durable.LeaseRefused as error:
        record('canonical_READY_writer_rejects_same_numeric_digest',
               str(error) == 'CERTIFIED_REPORT_RECEIPT_REQUIRED', reason=str(error))

    r = world()
    detail = dict(r.detail)
    detail.pop('certification_sha256')
    r.job['job_detail']['S'] = json.dumps(detail)
    r.reader.reports.get = deny_network
    refuses('missing_certification_digest_refuses_before_report_fetch', r)

    r = world()
    subject.after_report_blob(r, lambda: r.job.update(job_detail={'S': json.dumps(
        dict(r.detail, certification_sha256='d' * 64))}))
    refuses('READY_receipt_change_after_blob_refuses_even_same_report', r)

    r = world()
    first_key = next(iter(r.client.rows))

    def change_accepted():
        value = json.loads(r.client.rows[first_key]['record']['S'])
        value['accepted_at'] += 1
        r.client.rows[first_key]['record']['S'] = json.dumps(value)

    subject.after_report_blob(r, change_accepted)
    refuses('accepted_record_change_after_report_blob_refuses', r)

    r = world()
    key = (r.w.case.principal['firm_id'], 'REPORT#' + r.ref['report_id'] + '#' + r.ref['revision'])
    subject.after_report_blob(r, lambda: r.w.table.rows[key].update(retention_ref=r.source['retention_ref']))
    refuses('report_retention_reference_substitution_after_blob_refuses', r)

    r = world()
    key = (r.w.case.principal['firm_id'], 'RETENTION#' + r.source['retention_ref']['retention_id'])
    subject.after_report_blob(r, lambda: r.w.table.rows.pop(key))
    refuses('report_source_retention_loss_after_blob_refuses', r, subject.support.support.RetentionExpired)

    r = world()
    subject.after_report_blob(r, lambda: setattr(r.requests.artifacts, 'retention', None))
    refuses('composition_retention_service_loss_after_report_blob_refuses', r)

    r = world()
    subject.after_report_blob(r, lambda: setattr(r.requests, 'authorize_current', lambda *_: False))
    refuses('accepted_owner_current_authorization_loss_after_report_blob_refuses', r)

    r = world()
    r.w.case.s3.on_get = deny_network
    try:
        r.reader.read(dict(r.w.case.principal, principal_id='other'), r.id)
        record('wrong_owner_zero_blob_and_job_reads', False)
    except subject.support.reader_module.RequestReadDenied as error:
        record('wrong_owner_zero_blob_and_job_reads', not r.calls, job_reads=len(r.calls), reason=str(error))

    paths = [str(source / 'ops/tests/test_owned_report.py'), str(source / 'ops/tests/test_owned_requests.py'),
             str(source / 'intake/tests/test_retained_uploads.py')]
    command = ('import socket,pytest; '
               'deny=lambda *a,**k: (_ for _ in ()).throw(AssertionError("NETWORK_FORBIDDEN")); '
               'socket.socket.connect=deny; socket.socket.connect_ex=deny; socket.create_connection=deny; '
               'raise SystemExit(pytest.main(' + repr(['-q'] + paths) + '))')
    suite = subprocess.run([sys.executable, '-c', command], cwd=root, capture_output=True, text=True)
    args.output.write_text(json.dumps(dict(pin=pin, source_sha256=hashes, controls=results,
        supplied=dict(returncode=suite.returncode, stdout=suite.stdout, stderr=suite.stderr),
        limitations=['Synthetic schema-valid report and offline storage/clock/ACTIVE policy doubles',
                     'Malformed numeric digest is injected into persisted job detail; normal writer rejects it',
                     'No actual certifier/publication provenance, HTTP, vendor, IAM or runtime proof']), indent=2) + '\n', encoding='utf-8')
    print(suite.stdout)
    print(json.dumps(results, indent=2))
    return int(suite.returncode != 0 or any(row['outcome'] != 'PASS' for row in results))


if __name__ == '__main__':
    raise SystemExit(main())
