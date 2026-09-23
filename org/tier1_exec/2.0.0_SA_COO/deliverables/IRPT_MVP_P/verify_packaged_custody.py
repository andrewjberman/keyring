"""PARKED UNEXECUTED DRAFT under CTO5edf991c06; no evidence claim.

Intended offline extracted M/P/Y replay; synthetic stored bytes/economic authority.

Only /var/task runtime modules are imported. Fixture storage is populated with
versioned synthetic accepted JSON, not produced upstream economic evidence.
"""
import copy
import hashlib
import io
from pathlib import Path


class Storage:
    def __init__(self):
        self.versions, self.latest, self.reads = {}, {}, []

    def seed(self, location, body):
        version = str(len(self.versions) + 1)
        self.versions[(*location, version)] = body
        self.latest[location] = version
        return dict(bucket=location[0], key=location[1], version_id=version,
                    sha256=hashlib.sha256(body).hexdigest(), byte_length=len(body))

    def get_object(self, *, Bucket, Key, VersionId=None):
        self.reads.append((Bucket, Key, VersionId))
        version = VersionId or self.latest[(Bucket, Key)]
        body = self.versions[(Bucket, Key, version)]
        return dict(VersionId=version, ETag='"' + hashlib.sha256(body).hexdigest() + '"', Body=io.BytesIO(body))


class Dynamo:
    def __init__(self):
        self.items = {}

    @staticmethod
    def key(item):
        return item['tenant']['S'], item['request_revision']['S']

    def put_item(self, *, TableName, Item, ConditionExpression):
        assert TableName == 'offline-requests'
        assert ConditionExpression == 'attribute_not_exists(tenant) AND attribute_not_exists(request_revision)'
        key = self.key(Item)
        assert key not in self.items
        self.items[key] = copy.deepcopy(Item)

    def get_item(self, *, TableName, Key, ConsistentRead):
        assert TableName == 'offline-requests' and ConsistentRead is True
        item = self.items.get(self.key(Key))
        return {'Item': copy.deepcopy(item)} if item else {}


def run():
    import publication
    import snapshot
    import accepted_custody
    import custody_binding
    import custody_portfolio
    import portfolio
    import opal_naming
    from custody import CustodyOwnershipRefused

    for module in (publication, snapshot, accepted_custody, custody_binding,
                   custody_portfolio, portfolio, opal_naming):
        assert Path(module.__file__).resolve().parent == Path('/var/task')
    storage = Storage()
    # Uses the packaged canonical address builder and its actual registry files.
    service = publication.HoldingsPublication(storage, '49financial')
    date, account = '2026-09-21', 'account-0'
    dumps, digest = publication.canonical_bytes, custody_binding.digest

    def seed_publication(amount):
        document = {'scope': {'firm_id': '49financial', 'account_ids': [account]},
                    'nodes': [{'node_id': account, 'node_kind': 'ACCOUNT', 'parent_node_id': None,
                               'amount': {'value': amount}}], 'source_set_revision': [], 'clocks': {}}
        raw = dumps(document)
        revision = publication.digest(raw)
        partition = 'date=' + date
        platinum = storage.seed(service.location('platinum', partition, revision + '.json'), raw)
        # Reader validates Gold reference metadata; it does not read/decode Gold.
        # These explicit fixture bytes are not claimed to be a Parquet producer.
        gold = storage.seed(service.location('gold', partition, revision + '.parquet'), b'synthetic-reference-only')
        manifest = {'schema_version': 'irpt-holdings-manifest-v1', 'firm_id': '49financial',
                    'business_date': date, 'revision': revision, 'source_set_revision': [], 'clocks': {},
                    'gold': gold, 'platinum': platinum}
        ref = storage.seed(service.location('platinum', partition, revision + '.manifest.json'), dumps(manifest))
        index = {'schema_version': 'irpt-holdings-index-v1', 'firm_id': '49financial',
                 'latest_date': date, 'dates': {date: {'revision': revision, 'manifest': ref}}}
        storage.seed(service.location('platinum', 'current', 'manifest.json'), dumps(index))
        return revision

    first = seed_publication(100)
    principal = dict(firm_id='49financial', principal_id='offline-person', home_firm_id='opal-capital',
                     principal_class='OPAL_GLOBAL', advisor_id=None)
    principal['ownership_fingerprint'] = digest(principal)
    owner = {k: v for k, v in principal.items() if k != 'ownership_fingerprint'}
    owner.update(schema_version='custody-owner-v1', account_ids=[account], account_set_id='sel_' + 'a'*64,
                 snapshot_id='cst_'+'b'*64, directory_revision='d1', entitlement_revision='e1')
    owner['ownership_fingerprint'] = digest(owner)
    state = {'permitted': True, 'current_calls': 0, 'interpreted': 0}

    def current(p, o):
        state['current_calls'] += 1
        assert p == principal and o['account_ids'] == [account]
        return 'f'*64 if state['permitted'] else None

    def interpret(document, manifest, **kwargs):
        state['interpreted'] += 1
        assert document['nodes'][0]['amount']['value'] == 100
        ref = [{'source_receipt_id': 'fixture-positions', 'row_index': 0}]
        facts = {
            'cash': {'source_field': 'Cash', 'source_value': False, 'classification': 'NON_CASH', 'evidence': ref},
            'side': {'source_field': 'Side', 'source_value': 'L', 'position_side': 'LONG', 'sign_rule_revision': 'fixture', 'evidence': ref},
            'security': {'resolution_revision': 'fixture', 'resolved_identifier': {'namespace': 'TICKER', 'value': 'SPY'},
                         'evidence': ref, 'security_key': 'fixture-SPY', 'resolution_source_receipt_id': 'fixture-positions'},
            'source_quantity': {'value': '2', 'source_field': 'Units', 'source_units': 'shares', 'unit_rule_revision': 'fixture', 'evidence': ref},
            'accrual': {'treatment': 'INCLUDED_IN_MARKET_VALUE', 'value': '0', 'unaccrued_market_value': '100', 'rule_revision': 'fixture', 'evidence': ref}}
        originals = [{'account_id': account, 'position_id': 'fixture-position',
                      'source_security_id': {'namespace': 'FIXTURE', 'value': 'instrument'},
                      'market_value': {'value': '100', 'currency': 'USD'}, 'quantity': {'value': '2', 'units': 'SHARES'},
                      'economic_facts': copy.deepcopy(facts), 'source_row': {'source_receipt_id': 'fixture-positions',
                          'row_index': i, 'relationship_id': 'fixture-relation-' + str(i)}} for i in range(2)]
        position = {k: copy.deepcopy(v) for k, v in originals[0].items() if k != 'source_row'}
        position['source_rows'] = [copy.deepcopy(r['source_row']) for r in originals]
        actual = {'schema_version': 'synthetic-actual-v1', 'firm_id': '49financial', 'custody_as_of': date,
                  'valuation_as_of': date, 'account_ids': [account], 'positions': [position],
                  'census': [{'account_id': account, 'raw_row_count': 2, 'unique_position_count': 1,
                    'duplicate_relationship_row_count': 1, 'unsupported_original_row_count': 0,
                    'conflict_original_row_count': 0, 'completeness': 'COMPLETE', 'empty_account_evidence': None}],
                  'reconciliation': [{'account_id': account, 'position_value': '100', 'independent_value': '100',
                    'absolute_difference': '0', 'tolerance_usd': '0.01', 'currency': 'USD',
                    'custody_as_of': date, 'valuation_as_of': date, 'independent_source_rows': ref}]}
        return {'actual_custody': actual, 'original_rows': originals,
                'source_receipts': [{'source_receipt_id': 'fixture-positions', 'role': 'synthetic-economic-interpretation',
                    'account_ids': [account], 'object': manifest['platinum'], 'row_count': 2}],
                'revision_refs': {name: {'revision': 'fixture', 'source_receipt_id': 'fixture-positions'}
                                  for name in custody_binding.REVISION_FIELDS}}

    db = Dynamo()
    reader = accepted_custody.AcceptedCustodyReader(custody_binding.CustodyBindingStore(db, 'offline-requests'),
        current_selection=current, publication_for=lambda firm: service,
        interpret_source=interpret, validate_evidence=lambda *args, **kwargs: True)
    accepted = reader.create(principal, owner, as_of=date)
    stored = reader.store.load('49financial', accepted['snapshot_id'])
    receipt = stored['publication_receipt']
    assert seed_publication(999) != first
    storage.reads.clear()
    browser = dict(snapshot_id=accepted['snapshot_id'], account_ids=[account])
    normalizer = custody_portfolio.AcceptedCustodyNormalizer(reader)
    frozen = normalizer.load_normalized(browser, principal, accepted['owner'])
    retained = portfolio.verify_frozen_portfolio(frozen)
    assert retained['source']['accepted_custody'] == accepted
    assert retained['source']['source_revision'] == first
    assert len(retained['rows']) == 1 and len(accepted['original_rows']) == 2
    assert all(version is not None for _, _, version in storage.reads)
    decorated = snapshot.load_pinned_snapshot('49financial', receipt, s3_client=storage, account_ids=[account])
    assert decorated['nodes'][0]['amount']['value'] == 100
    # A valid owner/current selection and successful exact M load reach _interpret.
    before = state['interpreted']
    storage.reads.clear()
    reader.validate_evidence = None
    assert reader.authorize_snapshot(principal, accepted['owner']) is False
    assert state['interpreted'] == before and storage.reads
    reader.validate_evidence = lambda *args, **kwargs: True
    state['permitted'] = False
    storage.reads.clear()
    try:
        normalizer.load_normalized(browser, principal, accepted['owner'])
    except CustodyOwnershipRefused:
        pass
    else:
        raise AssertionError('revoked owner accepted')
    assert not storage.reads
    return {'packaged_m_p_y_replay': 'PASS', 'packaged_snapshot_wrapper': 'PASS',
            'missing_economic_validator_after_pinned_read': 'PASS', 'revocation_before_storage': 'PASS',
            'limits': 'Synthetic versioned accepted JSON, storage, economics and authority. Gold metadata only; no source producer or real economics proof.'}
