"""Bounded actual owned reader/acceptance/retained repository adversarial review."""
import argparse
import base64
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
    parser.add_argument('--pin', default='e93300e34b')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[5]
    pin = subprocess.check_output(['git', 'rev-parse', args.pin], cwd=root, text=True).strip()
    target = root / '.runtime/codex-seats/3.0.0_SA_CVO~Y/owned-request-review' / pin
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
    subject = load('owned_request_source_tests', source / 'ops/tests/test_owned_requests.py')
    results = []

    def world(tokens=('control-one', 'control-two', 'control-three')):
        value = subject.world.__wrapped__(subject.retention_world.__wrapped__())
        reader, records, client = subject.setup(value, tokens)
        return value, reader, records, client

    def record(name, passed, **observed):
        results.append(dict(name=name, outcome='PASS' if passed else 'FAIL', **observed))

    def mutate(client, key, update):
        value = json.loads(client.rows[key]['record']['S'])
        update(value)
        client.rows[key]['record']['S'] = json.dumps(value)

    def refuses(name, action, expected):
        try:
            result = action()
            record(name, False, returned=result)
        except expected as error:
            record(name, True, exception=type(error).__name__, reason=str(error))

    w, reader, records, client = world()
    page = reader.history(w.case.principal, limit=3)
    record('full_bounded_page_matches_individual_reads_and_projects_only_public_identity',
           len(page['items']) == 3 and page['next_cursor'] is None and len(client.queries) == 1
           and all(item == reader.read(w.case.principal, item['identity']['request_id']) for item in page['items'])
           and all(set(item) == {'identity', 'accepted_at'} for item in page['items']),
           page=page, query=client.queries[0])

    w, reader, records, client = world()
    heads = []
    original_head = reader.artifacts.head

    def count_head(*args):
        heads.append(args)
        return original_head(*args)

    reader.artifacts.head = count_head
    refuses('wrong_owner_refuses_before_artifact_port',
            lambda: reader.read(dict(w.case.principal, principal_id='other'), records[0]['identity']['request_id']),
            subject.reader_module.RequestReadDenied)
    record('wrong_owner_zero_artifact_calls', not heads, count=len(heads))

    w, reader, records, client = world()
    first_key = sorted(client.rows)[0]
    request_id = first_key[1].split('#')[1]
    mutate(client, first_key, lambda r: r['identity'].update(tenant_firm_id='foreign'))
    reader.artifacts.head = deny_network  # Any artifact call is a failed pre-I/O refusal.
    refuses('accepted_tenant_mismatch_refuses_before_artifact',
            lambda: reader.read(w.case.principal, request_id), subject.reader_module.RequestReadRefused)

    w, reader, records, client = world()
    first_key = sorted(client.rows)[0]
    mutate(client, first_key, lambda r: r['owner'].update(principal_id='other'))
    first = reader.history(w.case.principal, limit=1)
    decoded = json.loads(base64.urlsafe_b64decode(first['next_cursor']))
    decoded['key'] = sorted(client.rows)[1][1]  # An attacker can seek, but cannot grant access.
    seek = base64.urlsafe_b64encode(json.dumps(decoded).encode()).decode()
    last = reader.history(w.case.principal, limit=1, cursor=seek)
    record('foreign_empty_page_continues_and_forged_own_seek_does_not_grant_foreign_access',
           first['items'] == [] and bool(first['next_cursor']) and len(last['items']) == 1
           and len(client.queries) == 2 and last['next_cursor'] is None,
           empty_page=first, forged_seek_result=last)
    before = len(client.queries)
    refuses('cursor_replay_under_other_owner_refuses_before_query',
            lambda: reader.history(dict(w.case.principal, principal_id='other'), cursor=first['next_cursor']),
            subject.reader_module.RequestReadRefused)
    record('foreign_cursor_zero_additional_queries', len(client.queries) == before)

    w, reader, records, client = world()
    original_head = reader.artifacts.head
    first_key = sorted(client.rows)[0]
    visits = []

    def change_first_after_last_blob(*args):
        result = original_head(*args)
        visits.append(args)
        if len(visits) == 3:
            mutate(client, first_key, lambda r: r.update(accepted_at=r['accepted_at'] + 1))
        return result

    reader.artifacts.head = change_first_after_last_blob
    refuses('first_record_changed_during_last_blob_refuses_whole_page',
            lambda: reader.history(w.case.principal, limit=3), subject.reader_module.RequestReadRefused)
    record('record_change_schedule_reached_last_blob', len(visits) == 3, artifact_reads=len(visits))

    w, reader, records, client = world()
    expiry = w.stores.retention.require_live(w.case.principal,
        records[0]['composition_ref']['retention_ref'])['expires_at']
    original_head = reader.artifacts.head
    visits = []

    def expire_after_last_blob(*args):
        result = original_head(*args)
        visits.append(args)
        if len(visits) == 3:
            w.state.now = expiry
        return result

    reader.artifacts.head = expire_after_last_blob
    refuses('exact_expiry_after_last_blob_refuses_whole_page',
            lambda: reader.history(w.case.principal, limit=3), subject.support.RetentionExpired)
    record('expiry_schedule_reached_last_blob', len(visits) == 3, artifact_reads=len(visits))

    w, reader, records, client = world()
    original_head = reader.artifacts.head
    visits = []

    def remove_service_after_last_blob(*args):
        result = original_head(*args)
        visits.append(args)
        if len(visits) == 3:
            reader.artifacts.retention = None
        return result

    reader.artifacts.head = remove_service_after_last_blob
    refuses('retention_service_loss_after_last_blob_refuses',
            lambda: reader.history(w.case.principal, limit=3), subject.reader_module.RequestReadRefused)
    record('service_loss_schedule_reached_last_blob', len(visits) == 3, artifact_reads=len(visits))

    w, reader, records, client = world()
    first_key = sorted(client.rows)[0]
    mutate(client, first_key, lambda r: r.update(composition_ref={}))
    reader.artifacts.head = deny_network
    refuses('owned_missing_composition_ref_refuses_before_artifact',
            lambda: reader.history(w.case.principal, limit=3), subject.reader_module.RequestReadRefused)

    w, reader, records, client = world()
    original_query = client.query

    def too_many(**kwargs):
        result = original_query(**kwargs)
        result['Items'].append(copy.deepcopy(result['Items'][0]))
        return result

    client.query = too_many
    reader.artifacts.head = deny_network
    refuses('oversized_backend_page_refuses_before_artifact',
            lambda: reader.history(w.case.principal, limit=1), subject.reader_module.RequestReadRefused)

    w, reader, records, client = world()
    original_query = client.query

    def foreign_last_key(**kwargs):
        result = original_query(**kwargs)
        result['LastEvaluatedKey']['tenant'] = {'S': 'other'}
        return result

    client.query = foreign_last_key
    refuses('foreign_last_evaluated_key_refuses_page_release',
            lambda: reader.history(w.case.principal, limit=1), subject.reader_module.RequestReadRefused)

    test_paths = [str(source / 'ops/tests/test_owned_requests.py'),
                  str(source / 'intake/tests/test_retained_uploads.py')]
    command = ('import socket,pytest; '
               'deny=lambda *a,**k: (_ for _ in ()).throw(AssertionError("NETWORK_FORBIDDEN")); '
               'socket.socket.connect=deny; socket.socket.connect_ex=deny; socket.create_connection=deny; '
               'raise SystemExit(pytest.main(' + repr(['-q'] + test_paths) + '))')
    suite = subprocess.run([sys.executable, '-c', command], cwd=root, capture_output=True, text=True)
    args.output.write_text(json.dumps(dict(pin=pin, source_sha256=hashes, controls=results,
        supplied=dict(returncode=suite.returncode, stdout=suite.stdout, stderr=suite.stderr),
        limitations=['Actual reader/acceptance/P repositories with offline storage, clock and ACTIVE policy doubles',
                     'Sequential metadata finalization is not an atomic page snapshot',
                     'No real Dynamo expressions, IAM, HTTP, worker or report route proof']), indent=2) + '\n', encoding='utf-8')
    print(suite.stdout)
    print(json.dumps(results, indent=2))
    return int(suite.returncode != 0 or any(row['outcome'] != 'PASS' for row in results))


if __name__ == '__main__':
    raise SystemExit(main())
