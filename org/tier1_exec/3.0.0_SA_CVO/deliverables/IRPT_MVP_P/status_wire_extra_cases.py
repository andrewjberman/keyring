"""Additional repaired public projection/internal diagnostic controls."""
import pytest
from jsonschema import ValidationError

import test_owned_outer_contracts as outer


@pytest.mark.parametrize('kind', ['history', 'read', 'sections', 'status'])
def test_retained_internal_diagnostic_and_equal_public_projection(report_world, kind):
    served = outer.producer.entry._entry
    operation = outer.producer.call(report_world, kind)['operation']
    correlation = 'corr-reviewer-internal-' + kind
    internal = served.status_envelope(operation, 'CONTRACT_VERSION', correlation)
    public = served.refuse(operation, None, 'CONTRACT_VERSION', correlation)
    outer.validator(outer.BASE / 'StatusEnvelope.schema.json').validate(internal)
    outer.validator(outer.BASE / 'BoundaryRefusal.schema.json').validate(public)
    assert internal['internal_correlation_id'] == correlation
    assert public['status'] == {key: value for key, value in internal.items() if key != 'internal_correlation_id'}
    assert internal['internal_correlation_id'] == correlation
    assert public['status']['public_reason_code'] == 'CONTRACT_VERSION'


@pytest.mark.parametrize('kind', ['history', 'read', 'sections', 'status'])
def test_public_schema_rejects_reintroduced_server_only_correlation(report_world, kind):
    response = outer.producer.call(report_world, kind,
        headers={**report_world.w.case.headers, 'x-contract-version': 'unsupported'})
    outer.validator(outer.BASE / 'BoundaryRefusal.schema.json').validate(response)
    response['status']['internal_correlation_id'] = 'corr-must-stay-internal'
    with pytest.raises(ValidationError):
        outer.validator(outer.BASE / 'BoundaryRefusal.schema.json').validate(response)
