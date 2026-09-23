"""Independent offline controls for exact retained publisher 6c3bfae3e6."""
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
    pin = subprocess.check_output(['git', 'rev-parse', '6c3bfae3e6'], cwd=root, text=True).strip()
    target = root / '.runtime/codex-seats/3.0.0_SA_CVO~Y/retained-publisher' / pin
    target.mkdir(parents=True, exist_ok=True)
    prefix = 'infra/aws/lambda/investor-reporting'
    raw = subprocess.check_output(['git', 'archive', '--format=zip', pin, prefix,
                                   'docs/contracts/investor-reporting', 'data/firm_registry.json',
                                   'docs/briefs/sources/YCHARTS_COMPARISON_REPORT_FIELD_SCRAPE_20260909.json'], cwd=root)
    hashes = {}
    with zipfile.ZipFile(io.BytesIO(raw)) as bundle:
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
    base = target / prefix
    tests = [base / x for x in ('ycharts/generate/tests/test_publisher.py',
        'ycharts/extract/tests/test_publication.py', 'ycharts/generate/tests/test_retained_report_index.py')]
    command = ('import socket,pytest; '
        'deny=lambda *a,**k: (_ for _ in ()).throw(AssertionError("NETWORK_FORBIDDEN")); '
        'socket.socket.connect=deny; socket.socket.connect_ex=deny; socket.create_connection=deny; '
        'raise SystemExit(pytest.main(' + repr(['-q'] + [str(p) for p in tests]) + '))')
    suite = subprocess.run([sys.executable, '-c', command], cwd=root, capture_output=True, text=True)
    if suite.returncode:
        print(suite.stdout, suite.stderr)
        return suite.returncode
    subject = load('publisher_review_fixture', tests[0])
    publisher_module = sys.modules['publisher']
    results, observations = [], []

    def fresh(refresh=False):
        return subject.assemble(subject.world.__wrapped__(subject.retention_world.__wrapped__()), refresh=refresh)

    def check(name, fn):
        try:
            detail = fn()
            results.append(dict(name=name, outcome='PASS', detail=detail))
        except Exception as exc:
            results.append(dict(name=name, outcome='FAIL', error=repr(exc)))

    def refuse(r, invoke=None, *, no_transaction=True):
        try:
            (invoke or r.publish)()
        except (ValueError, RuntimeError, PermissionError) as exc:
            if no_transaction:
                assert not r.transactions, 'report transaction occurred'
            return dict(exception=type(exc).__name__, reason=str(exc), transactions=len(r.transactions))
        raise AssertionError('invalid publication returned a receipt')

    def positive(refresh):
        r = fresh(refresh)
        order = []
        retention = r.w.stores.retention
        promote = retention.promote
        def traced(principal, ref):
            row = retention.require_live(principal, ref)
            for dep in row['dependencies']:
                retention.require_live(principal, dep, accepted=True)
            order.append(copy.deepcopy(row['owner']))
            return promote(principal, ref)
        retention.promote = traced
        result = r.publish()
        ev = r.w.stores.artifacts.get(r.w.case.principal, result['extraction_evidence_ref']['artifact_id'])
        wrapper = json.loads(ev['data'])
        assert hashlib.sha256(ev['data']).hexdigest() == result['certification_sha256']
        assert wrapper['verification']['source_sha256'] == hashlib.sha256(r.data).hexdigest()
        assert wrapper['pdf_ref'] == r.pdf_ref
        assert wrapper['request_identity'] == r.record['identity']
        assert wrapper['verification_sha256'] == hashlib.sha256(subject._bytes(wrapper['verification'])).hexdigest()
        ref = result['report_ref']
        stored = r.w.stores.reports.get(r.w.case.principal, ref['report_id'], ref['revision'])
        assert stored['provenance']['extraction_evidence_ref'] == result['extraction_evidence_ref']
        assert stored['provenance']['pdf_ref'] == r.pdf_ref
        assert r.publish() == result and len(r.transactions) == 1
        assert r.row['state'] == {'S': 'CERTIFYING'}
        if refresh:
            assert len({owner['prospect_input_id'] for owner in order}) > 1
        return dict(transaction_count=len(r.transactions), promotion_calls=len(order),
                    distinct_input_ids=sorted({owner['prospect_input_id'] for owner in order}),
                    retained_wrapper_sha256=result['certification_sha256'], state='CERTIFYING')

    check('actual_pdf_evidence_report_and_idempotent_replay', lambda: positive(False))
    check('refresh_ancestor_ids_and_dependency_first_promotion', lambda: positive(True))

    def job_fault(field, value):
        r = fresh()
        r.row[field] = value
        return refuse(r)
    check('stale_composition_hash', lambda: job_fault('composition_sha256', {'S': '0' * 64}))
    check('stale_worker_owner', lambda: job_fault('lease_owner', {'S': 'other-worker'}))
    check('lease_expired', lambda: job_fault('lease_expires_at', {'N': '0'}))
    check('already_ready', lambda: job_fault('state', {'S': 'READY'}))

    def metadata_fault(kind):
        r = fresh()
        if kind == 'length':
            r.metadata['vendor_artifact']['byte_length'] += 1
        elif kind == 'revision_bool':
            r.metadata['request_ref']['request_revision'] = True
        elif kind == 'report_identity':
            r.w.stores.reports.index.report_id = 'RPT-' + '0' * 32
        return refuse(r)
    for kind in ('length', 'revision_bool', 'report_identity'):
        check('metadata_binding_' + kind, lambda kind=kind: metadata_fault(kind))

    def during_extraction(kind):
        r = fresh()
        original = publisher_module.build_publication
        def intercepted(*args, **kwargs):
            built = original(*args, **kwargs)
            if kind == 'principal':
                r.w.case.headers['x-user-email'] = 'revoked@example.invalid'
            elif kind == 'pending_policy':
                r.w.registered['state'] = 'PENDING_ENFORCEMENT'
            elif kind == 'pdf_row':
                key = (r.record['owner']['firm_id'], 'ARTIFACT#' + r.pdf_ref['artifact_id'])
                r.w.table.rows[key]['ref']['sha256'] = '0' * 64
            elif kind == 'accepted_record':
                client = r.requests.acceptance.client
                key = next(iter(client.rows))
                doc = json.loads(client.rows[key]['record']['S'])
                doc['accepted_at'] += 1
                client.rows[key]['record']['S'] = json.dumps(doc)
            return built
        publisher_module.build_publication = intercepted
        before = r.w.case.s3.put_count
        try:
            result = refuse(r)
            assert r.w.case.s3.put_count == before, 'evidence written after extraction-time invalidation'
            return result
        finally:
            publisher_module.build_publication = original
    for kind in ('principal', 'pending_policy', 'pdf_row', 'accepted_record'):
        check('post_extraction_' + kind, lambda kind=kind: during_extraction(kind))

    def changed_evidence():
        r = fresh()
        artifacts = r.w.stores.artifacts
        original = artifacts.get
        def get(*args, **kwargs):
            result = original(*args, **kwargs)
            if result['ref']['family'] == 'EXTRACTION_EVIDENCE':
                result = dict(result, data=result['data'] + b' ')
            return result
        artifacts.get = get
        return refuse(r)
    check('evidence_readback_bytes_mismatch', changed_evidence)

    def lease_after_evidence():
        r = fresh()
        artifacts = r.w.stores.artifacts
        original = artifacts.put
        def put(*args, **kwargs):
            result = original(*args, **kwargs)
            if result['family'] == 'EXTRACTION_EVIDENCE':
                r.row['fence_token'] = {'N': '2'}
            return result
        artifacts.put = put
        return refuse(r)
    check('lease_lost_after_evidence_write_no_report_transaction', lease_after_evidence)

    def after_transaction():
        r = fresh()
        client = r.store.client
        original = client.transact_write_items
        def transact(**kwargs):
            original(**kwargs)
            r.row['fence_token'] = {'N': '2'}
        client.transact_write_items = transact
        result = refuse(r, no_transaction=False)
        assert len(r.transactions) == 1
        rows = [v for (t, k), v in r.w.table.rows.items() if k.startswith('REPORT#')]
        assert len(rows) == 1
        result['persisted_report_after_refusal'] = True
        return result
    check('post_transaction_loss_refuses_but_does_not_undo_write', after_transaction)

    for field, value in (('holdings_fingerprint', '0' * 64), ('settings', {'unverified': True})):
        r = fresh()
        r.metadata['effective_inputs'][field] = value
        result = r.publish()
        ref = result['report_ref']
        accepted = r.w.stores.reports.get(r.w.case.principal, ref['report_id'], ref['revision'])
        observations.append(dict(name='worker_supplied_' + field, accepted=accepted['report']['effective_inputs'][field],
                                 note='Metadata trust observation; not a vendor read-back or accepted-composition grade.'))
    evidence = dict(pin=pin, source_sha256=hashes, supplied=dict(exit_code=suite.returncode,
        stdout=suite.stdout, stderr=suite.stderr), results=results, observations=observations,
        scope='Offline actual PDF/extractor/certifier/repositories; AWS transaction effects doubled; no READY/runtime/vendor.')
    (own / 'RETAINED_PUBLISHER_6c3bfae3.json').write_text(json.dumps(evidence, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(dict(pin=pin, supplied=suite.stdout, results=results, observations=observations), indent=2))
    return int(any(x['outcome'] == 'FAIL' for x in results))


if __name__ == '__main__':
    raise SystemExit(main())
