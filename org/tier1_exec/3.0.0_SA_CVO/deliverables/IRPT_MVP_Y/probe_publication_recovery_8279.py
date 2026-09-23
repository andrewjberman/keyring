"""Independent post-download recovery controls; offline effects, no READY claim."""
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
    own = Path(__file__).resolve().parent
    root = own.parents[4]
    pin = subprocess.check_output(['git', 'rev-parse', '82792f4864'], cwd=root, text=True).strip()
    target = root / '.runtime/codex-seats/3.0.0_SA_CVO~Y/publication-recovery' / pin
    target.mkdir(parents=True, exist_ok=True)
    prefix = 'infra/aws/lambda/investor-reporting'
    raw = subprocess.check_output(['git', 'archive', '--format=zip', pin, prefix,
                                   'docs/contracts/investor-reporting', 'data/firm_registry.json'], cwd=root)
    hashes = {}
    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        for member in archive.infolist():
            path = (target / member.filename).resolve()
            if not path.is_relative_to(target.resolve()):
                raise ValueError('snapshot escape')
            if member.is_dir():
                path.mkdir(parents=True, exist_ok=True)
            else:
                data = archive.read(member)
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(data)
                hashes[member.filename] = hashlib.sha256(data).hexdigest()
    socket.socket.connect = deny_network
    socket.socket.connect_ex = deny_network
    socket.create_connection = deny_network
    os.environ['IRPT_FIRM_REGISTRY'] = str(target / 'data/firm_registry.json')
    base = target / prefix / 'ycharts/generate'
    sys.path.insert(0, str(base / 'tests'))
    tests = [str(base / 'tests' / name) for name in ('test_publisher.py', 'test_durable_job.py', 'test_publication_worker.py')]
    command = ('import socket,pytest; '
        'deny=lambda *a,**k: (_ for _ in ()).throw(AssertionError("NETWORK_FORBIDDEN")); '
        'socket.socket.connect=deny; socket.socket.connect_ex=deny; socket.create_connection=deny; '
        'raise SystemExit(pytest.main(' + repr(['-q'] + tests) + '))')
    suite = subprocess.run([sys.executable, '-c', command], cwd=root, capture_output=True, text=True)
    if suite.returncode:
        print(suite.stdout, suite.stderr)
        return suite.returncode
    subject = load('recovery_review_fixture', base / 'tests/test_publication_worker.py')
    results = []

    def fresh():
        return subject.prepared(subject.world.__wrapped__(subject.retention_world.__wrapped__()))

    def check(name, fn):
        try:
            results.append(dict(name=name, outcome='PASS', detail=fn()))
        except Exception as exc:
            results.append(dict(name=name, outcome='FAIL', error=repr(exc)))

    def refused(fn, r, *, transactions=0):
        try:
            fn()
        except (ValueError, RuntimeError, PermissionError) as exc:
            assert len(r.transactions) == transactions
            assert r.row['state'] != {'S': 'READY'}
            return dict(exception=type(exc).__name__, reason=str(exc), report_transactions=len(r.transactions))
        raise AssertionError('receipt returned unexpectedly')

    class Death(BaseException):
        pass

    def recovery(stage):
        r = fresh()
        frozen = subject.checkpoint(r)
        original_pdf_checkpoint = copy.deepcopy(r.row['checkpoint_pdf'])
        if stage == 'report':
            original = r.publisher.publish
            def publish(*args, **kwargs):
                original(*args, **kwargs)
                raise Death()
            r.publisher.publish = publish
            try:
                r.worker.finish(r.principal, r.id)
            except Death:
                pass
            else:
                raise AssertionError('cut point not reached')
            r.publisher.publish = original
        elif stage == 'receipt':
            original = r.store.client.update_item
            def update(**kwargs):
                result = original(**kwargs)
                if kwargs.get('ExpressionAttributeNames', {}).get('#checkpoint') == 'checkpoint_publication':
                    raise Death()
                return result
            r.store.client.update_item = update
            try:
                r.worker.finish(r.principal, r.id)
            except Death:
                pass
            else:
                raise AssertionError('cut point not reached')
            r.store.client.update_item = original
        old_store = r.store
        subject.restart(r)
        r.row['lease_owner'] = {'S': 'independent-replacement'}
        r.store.worker_id = 'independent-replacement'
        before = len(r.transactions)
        refused(lambda: old_store.get_checkpoint(r.id, 'pdf'), r, transactions=before)
        # Caller-owned mutable objects are now wrong. Recovery must use checkpoint bytes.
        r.metadata['effective_inputs']['settings']['after_checkpoint'] = 'must not enter accepted report'
        r.census['sections'][0]['title'] = 'changed after checkpoint'
        receipt = r.worker.finish(r.principal, r.id)
        again = r.worker.finish(r.principal, r.id)
        assert receipt == again and len(r.transactions) == 1
        assert r.row['checkpoint_pdf'] == original_pdf_checkpoint
        assert json.loads(r.row['checkpoint_pdf']['S']) == frozen
        persisted = r.w.stores.reports.get(r.principal, receipt['report_id'], receipt['revision'])
        assert persisted['report']['effective_inputs'] == frozen['metadata']['effective_inputs']
        evidence_ref = persisted['provenance']['extraction_evidence_ref']
        evidence = r.w.stores.artifacts.get(r.principal, evidence_ref['artifact_id'])
        assert hashlib.sha256(evidence['data']).hexdigest() == receipt['certification_sha256']
        assert json.loads(evidence['data'])['census'] == frozen['census']
        assert r.row['state'] == {'S': 'CERTIFYING'}
        assert not any(u['ExpressionAttributeValues'].get(':state') == {'S': 'READY'} for u in r.updates)
        assert not any(key.startswith('intent_') for key in r.row)
        return dict(cut=stage, report_transactions=1, same_replay_receipt=True, state='CERTIFYING',
                    original_checkpoint_unchanged=True, old_lease_refused=True)
    for stage in ('pdf', 'report', 'receipt'):
        check('replacement_worker_after_' + stage, lambda stage=stage: recovery(stage))

    def changed_checkpoint(field):
        r = fresh()
        subject.checkpoint(r)
        original = copy.deepcopy(r.row['checkpoint_pdf'])
        if field == 'metadata':
            r.metadata['effective_inputs']['settings']['changed'] = True
        else:
            r.census['sections'][0]['title'] = 'different'
        result = refused(lambda: subject.checkpoint(r), r)
        assert r.row['checkpoint_pdf'] == original
        return result
    for field in ('metadata', 'census'):
        check('immutable_checkpoint_' + field, lambda field=field: changed_checkpoint(field))

    def after_checkpoint(kind):
        r = fresh()
        subject.checkpoint(r)
        if kind == 'revoked':
            r.w.case.headers['x-user-email'] = 'revoked@example.invalid'
        elif kind == 'pending_policy':
            r.w.registered['state'] = 'PENDING_ENFORCEMENT'
        elif kind == 'lease_expired':
            r.row['lease_expires_at'] = {'N': '0'}
        elif kind == 'failed_phase':
            r.row['state'] = {'S': 'FAILED'}
        return refused(lambda: r.worker.finish(r.principal, r.id), r)
    for kind in ('revoked', 'pending_policy', 'lease_expired', 'failed_phase'):
        check('checkpoint_does_not_override_' + kind, lambda kind=kind: after_checkpoint(kind))

    def publication_tamper():
        r = fresh()
        subject.checkpoint(r)
        r.worker.finish(r.principal, r.id)
        doc = json.loads(r.row['checkpoint_publication']['S'])
        doc['certification_sha256'] = '0' * 64
        r.row['checkpoint_publication'] = {'S': json.dumps(doc)}
        subject.restart(r)
        return refused(lambda: r.worker.finish(r.principal, r.id), r, transactions=1)
    check('publication_receipt_not_a_trusted_shortcut', publication_tamper)

    def lease_after_report():
        r = fresh()
        subject.checkpoint(r)
        original = r.publisher.publish
        def publish(*args, **kwargs):
            value = original(*args, **kwargs)
            r.row['fence_token'] = {'N': '2'}
            return value
        r.publisher.publish = publish
        outcome = refused(lambda: r.worker.finish(r.principal, r.id), r, transactions=1)
        assert 'checkpoint_publication' not in r.row
        assert r.row['state'] == {'S': 'CERTIFYING'}
        return outcome
    check('post_report_lease_loss_no_receipt_checkpoint_no_ready', lease_after_report)

    def large_checkpoint():
        r = fresh()
        r.metadata['effective_inputs']['settings']['large'] = 'x' * (33 * 1024)
        outcome = refused(lambda: subject.checkpoint(r), r)
        assert 'checkpoint_pdf' not in r.row and not r.updates
        return outcome
    check('oversized_checkpoint_refused_before_update', large_checkpoint)
    doc = dict(pin=pin, source_sha256=hashes, supplied=dict(exit_code=suite.returncode,
        stdout=suite.stdout, stderr=suite.stderr), results=results,
        limitations=['Offline modeled update/transaction effects, synthetic PDF and exception cut points',
                     'Replacement lease assumed acquired; no process kill, server race or queue/session transport',
                     'Effective-input readback trust unchanged; no READY, runtime, vendor or integrated acceptance'])
    (own / 'PUBLICATION_RECOVERY_82792f48.json').write_text(json.dumps(doc, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(dict(pin=pin, supplied=suite.stdout, results=results), indent=2))
    return int(any(r['outcome'] == 'FAIL' for r in results))


if __name__ == '__main__':
    raise SystemExit(main())
