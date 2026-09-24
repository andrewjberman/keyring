"""Pinned offline parser/local identity/upload/checkpoint/create-wire review."""
import argparse
import copy
from decimal import Decimal
import hashlib
import io
import json
from pathlib import Path
import socket
import subprocess
import sys
import zipfile

from probe_recipe_decimal import deny_network, load, multipart_parts, OfflineTransport, echo


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--pin', default='c2a01fb3f8')
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[5]
    pin = subprocess.check_output(['git', 'rev-parse', args.pin], cwd=root, text=True).strip()
    target = root / '.runtime/codex-seats/3.0.0_SA_CVO~Y/bridge-review' / pin
    target.mkdir(parents=True, exist_ok=True)
    prefix = 'infra/aws/lambda/investor-reporting'
    archive = subprocess.check_output(['git', 'archive', '--format=zip', pin,
                                      prefix + '/intake', prefix + '/ycharts/generate'], cwd=root)
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
    intake = target / prefix / 'intake'
    generate = target / prefix / 'ycharts/generate'
    sys.path[:0] = [str(intake), str(generate)]
    subject = load('bridge_source_tests', generate / 'tests/test_normalized_input.py')
    bridge, recipe = subject.bridge, subject.recipe
    settings = json.loads((intake / 'settings.json').read_text(encoding='utf-8'))
    results = []

    def record(name, passed, **observed):
        results.append(dict(name=name, outcome='PASS' if passed else 'FAIL', **observed))

    def bound(frozen, returned=None):
        prepared = bridge.prepare_normalized_upload(frozen)
        rows = returned if returned is not None else [
            (row['identifier'], row['quantity']['value']) for row in reversed(prepared['rows'])]
        transport = OfflineTransport(echo(rows))
        upload = recipe.step_upload(transport, prepared['rows'])
        checkpoint = json.loads(json.dumps(upload))
        return prepared, transport, checkpoint, bridge.bind_normalized_upload(frozen, checkpoint)

    def refused(name, frozen, upload=None):
        try:
            if upload is None:
                bridge.prepare_normalized_upload(frozen)
            else:
                bridge.bind_normalized_upload(frozen, upload)
            record(name, False, result='RETURNED')
        except (recipe.RecipeRefused, subject.portfolio.PortfolioRefused) as error:
            record(name, True, reason=str(error))

    frozen = subject.freeze('Ticker,Market Value,Currency\nAAPL,9007199254740993.01,USD\n'
                            'AAPL,0.10,USD\n$:CASH,1,USD\n')
    prepared, transport, checkpoint, binding = bound(frozen)
    recipe.step_create(transport, 'offline-review-owned', binding['upload_record_id'], binding['rows'], settings)
    parts = multipart_parts(transport.calls[1][2], transport.calls[1][3])
    items = json.loads(parts['items'], parse_float=Decimal)
    by_id = {row['security_id']: row['weighting'] for row in items}
    record('actual_upload_checkpoint_binding_create_wire_exact_dollars',
           by_id == {'AAPL': Decimal('9007199254740993.11'), '$:CASH': Decimal('1')}
           and binding['total_dollars'] == '9007199254740994.11'
           and b'local-AAPL' not in transport.calls[0][2]
           and b'9007199254740993.11' in parts['items'],
           total=binding['total_dollars'], items_payload=parts['items'].decode(),
           input_id=binding['input_id'], calls=[call[0] for call in transport.calls])

    original = copy.deepcopy(binding)
    checkpoint['rows'][0]['security_id'] = 'MUTATED'
    prepared['rows'][0]['quantity']['value'] = '1'
    record('bound_copy_isolated_from_checkpoint_and_prepared_mutation', binding == original)

    tampered = copy.deepcopy(frozen)
    tampered_row = next(row for row in tampered['document']['holdings']['rows']
                        if row['canonical_identifier'] == 'AAPL')
    assert tampered_row['dollars'] != '1', 'negative control must change a value'
    tampered_row['dollars'] = '1'
    refused('retained_document_change_rejected_without_rehash', tampered)
    tampered_id = copy.deepcopy(frozen)
    tampered_id['input_id'] = 'portfolio_' + '0' * 64
    refused('retained_input_id_change_rejected', tampered_id)

    equal = subject.freeze('Ticker,Market Value,Currency\nAAPL,1,USD\nMSFT,1,USD\n')
    other = subject.freeze('Ticker,Market Value,Currency\nGOOG,1,USD\nMETA,1,USD\n')
    _, _, foreign_checkpoint, _ = bound(other)
    refused('coherent_other_upload_same_amounts_refused', equal, foreign_checkpoint)

    _, _, changed_checkpoint, _ = bound(equal)
    changed_checkpoint['rows'][0]['security_id'] = 'S:' + changed_checkpoint['rows'][0]['security_id']
    refused('display_or_equal_amount_cannot_infer_prefixed_vendor_identity', equal, changed_checkpoint)

    _, _, changed_amount, _ = bound(frozen)
    next(row for row in changed_amount['rows'] if row['security_id'] == 'AAPL')['weighting'] = '9007199254740993.12'
    refused('checkpoint_cent_change_refused_despite_true_reconciled_flags', frozen, changed_amount)

    _, _, display_changed, _ = bound(equal)
    for row in display_changed['rows']:
        row['display_name'] = 'Unrelated label'
        row['display_security_id'] = 'Different display identifier'
    display_bound = bridge.bind_normalized_upload(equal, display_changed)
    record('display_labels_do_not_remap_exact_echo_identity',
           {row['vendor_security_id'] for row in display_bound['identity_bindings']} == {'AAPL', 'MSFT'},
           labels_are_passed_through_not_crosswalk=True)

    try:
        subject.freeze('Ticker,Market Value,Currency\nALIAS,0.000000000000000000000001,USD\n')
        record('upstream_out_of_range_tiny_value_refuses', False)
    except subject.portfolio.PortfolioRefused as error:
        record('upstream_out_of_range_tiny_value_refuses', True, reason=str(error))
    cusip = subject.freeze('Ticker,Market Value,Currency\nALIAS,0.01,USD\n',
        resolver=lambda identifier, namespace: {
            'security_key': 'local-cusip', 'canonical_identifier': '001234567',
            'canonical_identifier_namespace': 'CUSIP', 'resolution_revision': 'fixture-cusip-r1'})
    _, cusip_transport, _, cusip_bound = bound(cusip)
    recipe.step_create(cusip_transport, 'offline-cusip', cusip_bound['upload_record_id'], cusip_bound['rows'], settings)
    items_bytes = multipart_parts(cusip_transport.calls[1][2], cusip_transport.calls[1][3])['items']
    cusip_item = json.loads(items_bytes, parse_float=Decimal)[0]
    record('declared_cusip_leading_zeros_and_cent_survive_create',
           cusip_item['security_id'] == '001234567' and cusip_item['weighting'] == Decimal('0.01')
           and cusip_bound['identity_bindings'][0]['security_key'] == 'local-cusip',
           items_payload=items_bytes.decode())

    shares = subject.freeze('Ticker,Shares\nAAPL,2\n', price_date='2026-09-21', prices={
        'local-AAPL': {'security_key': 'local-AAPL', 'price': '12.35', 'currency': 'USD',
                       'as_of': '2026-09-21', 'source_revision': 'fixture-price-r1'}})
    _, _, _, shares_bound = bound(shares)
    record('frozen_share_price_result_bound_without_reresolution',
           shares_bound['total_dollars'] == '24.70'
           and shares_bound['content_sha256'] == shares['content_sha256'],
           dollars=shares_bound['total_dollars'])

    command = ('import socket,pytest; '
               'deny=lambda *a,**k: (_ for _ in ()).throw(AssertionError("NETWORK_FORBIDDEN")); '
               'socket.socket.connect=deny; socket.socket.connect_ex=deny; socket.create_connection=deny; '
               'raise SystemExit(pytest.main(' + repr(['-q', str(generate / 'tests/test_normalized_input.py'),
                   str(generate / 'tests/test_recipe_decimal.py'), str(intake / 'tests/test_portfolio.py')]) + '))')
    suite = subprocess.run([sys.executable, '-c', command], cwd=root, capture_output=True, text=True)
    output = dict(pin=pin, source_sha256=hashes, independent_controls=results,
                  supplied_tests=dict(returncode=suite.returncode, stdout=suite.stdout, stderr=suite.stderr),
                  limitations=['Local resolver fixtures, no actual M source or current-access ports',
                               'Pure bridge consumes caller-verified frozen data and checkpoint; no storage authorization proof',
                               'Actual recipe multipart captured by offline transport; no vendor calls',
                               'No fenced worker/runtime installation, mutation intent or process recovery proof'])
    args.output.write_text(json.dumps(output, indent=2) + '\n', encoding='utf-8')
    print(suite.stdout)
    print(json.dumps(dict(pin=pin, controls=results), indent=2))
    return int(suite.returncode != 0 or any(row['outcome'] != 'PASS' for row in results))


if __name__ == '__main__':
    raise SystemExit(main())
