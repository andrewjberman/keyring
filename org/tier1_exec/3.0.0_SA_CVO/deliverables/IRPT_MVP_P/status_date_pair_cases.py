"""Independent actual Entry and closed-schema controls at the paired backend pin."""
import copy
import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator, FormatChecker, ValidationError

import test_owned_outer_contracts as outer

world = outer.world
retention_world = outer.retention_world
report_world = outer.report_world


def actual(r, dated=(), undated=(), header=True):
    outer.date_producer.publish(r, dated, undated)
    headers = dict(r.w.case.headers)
    if header:
        headers['x-irpt-status-dates'] = 'prospect-v1'
    return outer.producer.call(r, 'status', headers=headers)


@pytest.mark.parametrize('dated,undated', [([], ['one']),
    ([('d1', '2026-08-31'), ('d2', '2026-09-01')], ['u1']),
    ([('one', '2026-09-01'), ('two', '2026-09-01')], [])])
def test_actual_dates_preserve_census_and_legacy_shape(report_world, dated, undated):
    response = actual(report_world, dated, undated)
    outer.validator(outer.BASE / 'responses/status-job.response.schema.json').validate(response)
    data = response['data']
    assert data['state'] == 'READY' and 'internal_correlation_id' not in data
    legacy = Draft202012Validator(json.loads(Path('old-public-status.json').read_text()), format_checker=FormatChecker())
    if not undated and len({day for _, day in dated}) == 1:
        assert data['source_dates'] == {'business_date': dated[0][1]}
        legacy.validate(data)
    else:
        assert data['source_dates']['section_dates'] == (
            [{'section_id': key, 'as_of_date': day} for key, day in dated]
            + [{'section_id': key, 'as_of_date': None} for key in undated])
        assert 'business_date' not in data['source_dates']
        with pytest.raises(ValidationError):
            legacy.validate(data)


@pytest.mark.parametrize('mutation', ['outer_unknown', 'grant_missing', 'grant_negative',
    'public_correlation', 'null_business', 'invalid_section_date', 'missing_section_identity'])
def test_new_closed_schema_refuses_bad_actual_wire(report_world, mutation):
    response = actual(report_world, [('d1', '2026-09-01')], ['u1'])
    if mutation == 'outer_unknown':
        response['unknown'] = True
    elif mutation == 'grant_missing':
        response.pop('unprojected_grant')
    elif mutation == 'grant_negative':
        response['unprojected_grant']['count'] = -1
    elif mutation == 'public_correlation':
        response['data']['internal_correlation_id'] = 'server-only'
    elif mutation == 'null_business':
        response['data']['source_dates']['business_date'] = None
    elif mutation == 'invalid_section_date':
        response['data']['source_dates']['section_dates'][0]['as_of_date'] = '2026-02-30'
    elif mutation == 'missing_section_identity':
        response['data']['source_dates']['section_dates'][0].pop('section_id')
    with pytest.raises(ValidationError):
        outer.validator(outer.BASE / 'responses/status-job.response.schema.json').validate(response)


def test_legacy_negotiation_and_process_timestamp_replay(report_world):
    r = report_world
    original = actual(r, [], ['undated'])
    before = copy.deepcopy(original['data']['source_dates'])
    r.record['accepted_at'] += 12345
    replay = outer.producer.call(r, 'status', headers={**r.w.case.headers, 'x-irpt-status-dates': 'prospect-v1'})
    assert replay['data']['source_dates'] == before
    legacy = outer.producer.call(r, 'status')
    assert legacy['data']['state'] == 'UNAVAILABLE' and legacy['data']['source_dates'] == {}
    Draft202012Validator(json.loads(Path('old-public-status.json').read_text())).validate(legacy['data'])


@pytest.mark.parametrize('kind', ['history', 'read', 'sections', 'status'])
def test_actual_refusals_remain_payload_free_and_schema_valid(report_world, kind):
    response = outer.producer.call(report_world, kind, headers={**report_world.w.case.headers, 'x-origin-verify': ''})
    assert response['ok'] is False and 'data' not in response and 'unprojected_grant' not in response
    outer.validator(outer.BASE / 'BoundaryRefusal.schema.json').validate(response)
    response['data'] = {'unexpected': 'payload'}
    with pytest.raises(ValidationError):
        outer.validator(outer.BASE / 'BoundaryRefusal.schema.json').validate(response)


@pytest.mark.parametrize('kind', ['history', 'read', 'sections', 'status'])
def test_raw_refusal_respects_schema_marked_server_only_boundary(report_world, kind):
    response = outer.producer.call(report_world, kind,
        headers={**report_world.w.case.headers, 'x-contract-version': 'unsupported'})
    internal_schema = json.loads((outer.BASE / 'StatusEnvelope.schema.json').read_text())
    marked = {key for key, spec in internal_schema['properties'].items() if spec.get('x-server-only')}
    assert marked == {'internal_correlation_id'}
    assert response['ok'] is False and 'data' not in response
    assert not marked.intersection(response['status']), 'Server-only member in actual caller response'
