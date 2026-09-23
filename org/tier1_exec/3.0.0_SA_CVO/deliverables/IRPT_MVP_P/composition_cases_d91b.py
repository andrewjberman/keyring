"""Independent composition schema, exact binding and actual repository controls."""
import copy
import json

import pytest
from jsonschema import ValidationError

import test_request_composition as supplied

pytest_plugins = ['test_retained_uploads']


def checked(doc):
    supplied.validator().validate(doc)
    return supplied.validate_bindings(doc)


def recipient(doc, label):
    doc['browser']['prepared_for'] = label
    resolved = doc['resolved']
    resolved['profile']['prepared_for'] = label
    source = resolved['source_descriptors']['recipient']
    source['projection']['prepared_for'] = label
    source['projection_sha256'] = supplied.sha(source['projection'])


def store(world, doc, identity=None):
    data = checked(doc)
    ref = world.stores.artifacts.put(world.case.principal, doc['resolved']['owner'],
        'REQUEST_COMPOSITION', identity or doc['browser']['request_id'] + '-' + supplied.sha(doc),
        data, 'application/json', retention_dependencies=[
            doc['resolved']['input_ref']['artifact_ref']['retention_ref']])
    return data, ref


@pytest.mark.parametrize('label', ['A', 'é', 'e\u0301', '🌍' * 200, '  <>&" recipient  '])
def test_valid_exact_unicode_roundtrip(world, label):
    doc = supplied.example(world)
    recipient(doc, label)
    data, ref = store(world, doc)
    answer = world.stores.artifacts.get(world.case.principal, ref['artifact_id'])
    assert answer['data'] == data
    assert json.loads(data)['browser']['prepared_for'] == label


@pytest.mark.parametrize('label', [' ', '\t', 'x\u0000', 'x\u001f', 'x\u0080', '\udfff', '🌍' * 201])
def test_invalid_matching_recipient_refuses(world, label):
    doc = supplied.example(world)
    # Bind every location to the same invalid value, so equality cannot mask bad text.
    try:
        recipient(doc, label)
        with pytest.raises((ValidationError, supplied.CompositionRefused, UnicodeError)):
            checked(doc)
    except UnicodeError:
        assert any(0xD800 <= ord(c) <= 0xDFFF for c in label)


@pytest.mark.parametrize('path', [(), ('browser',), ('resolved',), ('resolved', 'owner'),
    ('resolved', 'profile'), ('resolved', 'profile_provenance', 'prepared_for'),
    ('resolved', 'source_descriptors', 'recipient'),
    ('resolved', 'source_descriptors', 'recipient', 'binding'),
    ('resolved', 'source_descriptors', 'recipient', 'source_scope'),
    ('resolved', 'source_descriptors', 'recipient', 'upstream_revision'),
    ('resolved', 'source_descriptors', 'recipient', 'source_dates')])
def test_closed_objects_refuse_unknown_members(world, path):
    doc = supplied.example(world)
    current = doc
    for key in path:
        current = current[key]
    current['unexpected_authority'] = True
    with pytest.raises(ValidationError):
        checked(doc)


@pytest.mark.parametrize('mutation', ['recipient_browser', 'recipient_resolved', 'recipient_projection',
    'source_firm', 'source_principal', 'numeric_digest', 'recipe', 'settings',
    'unknown_source', 'unknown_recipe', 'browser_preparer', 'revision_absence',
    'missing_label', 'comparison_extra', 'input_digest'])
def test_independent_binding_mutations_refuse(world, mutation):
    doc = supplied.example(world)
    r = doc['resolved']
    src = r['source_descriptors']['recipient']
    if mutation == 'recipient_browser':
        doc['browser']['prepared_for'] = 'different'
    elif mutation == 'recipient_resolved':
        r['profile']['prepared_for'] = 'different'
    elif mutation == 'recipient_projection':
        src['projection']['prepared_for'] = 'different'
        src['projection_sha256'] = supplied.sha(src['projection'])
    elif mutation == 'source_firm':
        src['binding'] = dict(src['binding'], firm_id='foreign')
    elif mutation == 'source_principal':
        src['binding'] = dict(src['binding'], principal_id='foreign')
    elif mutation == 'numeric_digest':
        src['projection_sha256'] = int('1' * 64)
    elif mutation == 'recipe':
        doc['recipe_version'] = 'replacement'
    elif mutation == 'settings':
        doc['settings']['management_fee'] = 5
    elif mutation == 'unknown_source':
        r['profile_provenance']['prepared_for']['source_id'] = 'missing'
    elif mutation == 'unknown_recipe':
        r['recipe_source_id'] = 'missing'
    elif mutation == 'browser_preparer':
        r['source_descriptors']['profile']['source_kind'] = 'BROWSER_REQUEST'
    elif mutation == 'revision_absence':
        src['upstream_revision']['absence_reason'] = None
    elif mutation == 'missing_label':
        del doc['browser']['prepared_for']
    elif mutation == 'comparison_extra':
        doc['browser']['comparison_keys'] = ['unresolved']
        doc['browser']['variant'] = 'comparison'
    elif mutation == 'input_digest':
        r['input_ref']['artifact_ref']['sha256'] = '0' * 64
    with pytest.raises((ValidationError, supplied.CompositionRefused)):
        checked(doc)


def test_new_revision_keeps_old_exact_bytes_and_deadline(world):
    doc = supplied.example(world)
    original, first = store(world, doc)
    deadline = world.stores.retention.require_live(world.case.principal, first['retention_ref'])['expires_at']
    world.state.now += 100
    recipient(doc, 'explicit changed recipient')
    doc['browser']['request_id'] = 'explicit-new-revision'
    changed, second = store(world, doc)
    assert first['artifact_id'] != second['artifact_id'] and original != changed
    assert world.stores.artifacts.get(world.case.principal, first['artifact_id'])['data'] == original
    assert world.stores.artifacts.get(world.case.principal, second['artifact_id'])['data'] == changed
    assert world.stores.retention.require_live(world.case.principal, second['retention_ref'])['expires_at'] == deadline


@pytest.mark.parametrize('mode', ['wrong_firm', 'wrong_principal', 'midread_revoke', 'expired', 'midread_expire'])
def test_actual_repository_rechecks_access_and_expiry(world, mode):
    doc = supplied.example(world)
    data, ref = store(world, doc)
    principal = copy.deepcopy(world.case.principal)
    deadline = world.stores.retention.require_live(principal, ref['retention_ref'])['expires_at']
    if mode == 'wrong_firm':
        principal['firm_id'] = 'foreign'
    elif mode == 'wrong_principal':
        principal['principal_id'] = 'foreign'
    elif mode == 'midread_revoke':
        world.case.s3.on_get = lambda: world.case.headers.update({'x-user-email': 'foreign@example.invalid'})
    elif mode == 'expired':
        world.state.now = deadline
    elif mode == 'midread_expire':
        world.case.s3.on_get = lambda: setattr(world.state, 'now', deadline)
    with pytest.raises((ValueError, PermissionError)):
        world.stores.artifacts.get(principal, ref['artifact_id'])


def test_changed_bytes_cannot_replace_existing_identity(world):
    doc = supplied.example(world)
    original, ref = store(world, doc, 'same-accepted-identity')
    recipient(doc, 'changed without new identity')
    with pytest.raises(ValueError, match='immutable artifact identity conflict'):
        store(world, doc, 'same-accepted-identity')
    assert world.stores.artifacts.get(world.case.principal, ref['artifact_id'])['data'] == original


@pytest.mark.parametrize('mode', ['blob_bytes', 'index_digest'])
def test_stored_byte_or_receipt_corruption_refuses(world, monkeypatch, mode):
    doc = supplied.example(world)
    data, ref = store(world, doc)
    if mode == 'blob_bytes':
        monkeypatch.setattr(world.stores.artifacts.blobs, 'get', lambda blob: data + b' ')
    else:
        row = world.table.rows[(doc['resolved']['owner']['firm_id'], 'ARTIFACT#' + ref['artifact_id'])]
        row['ref']['sha256'] = '0' * 64
    with pytest.raises(ValueError, match='artifact integrity failed'):
        world.stores.artifacts.get(world.case.principal, ref['artifact_id'])
