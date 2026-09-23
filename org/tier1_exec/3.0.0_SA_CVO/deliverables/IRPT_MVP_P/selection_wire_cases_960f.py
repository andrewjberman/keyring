"""Independent actual selection refusal and retained diagnostic controls."""
import copy
import json
from pathlib import Path

import pytest
from jsonschema import ValidationError

import test_selection_contract as contract


def test_actual_selection_refusal_and_internal_diagnostic(monkeypatch):
    producer = contract.producer
    boundary, rows, a, b, relation = producer.setup_entry(monkeypatch, permitted_both=False)
    served = producer.entry._entry
    diagnostics = []
    correlation = 'corr-cvo-p-selection-internal'
    monkeypatch.setattr(served._errors, 'new_correlation_id', lambda: correlation)
    monkeypatch.setattr(served._errors, 'record_internal', lambda *args: diagnostics.append(args))
    answer = boundary.handle(producer.request('RELATIONSHIP', [relation]))
    assert answer['ok'] is False and not rows and 'data' not in answer
    assert answer['status']['public_reason_code'] == 'OBJECT_NOT_COVERED'
    assert diagnostics and diagnostics[-1][1:3] == (correlation, 'selection-create')
    assert correlation not in json.dumps(answer)
    assert 'internal_correlation_id' not in answer['status']
    contract.validator('BoundaryRefusal.schema.json').validate(answer)
    internal = served.status_envelope('selection-create', 'OBJECT_NOT_COVERED', correlation,
                                     business_date='2026-09-22')
    contract.validator('StatusEnvelope.schema.json').validate(internal)
    assert internal['internal_correlation_id'] == correlation
    assert answer['status'] == {key: value for key, value in internal.items()
                               if key != 'internal_correlation_id'}
    snapshot = Path.cwd()
    fixture = json.loads((snapshot / 'src/pages/InvestorReporting/__tests__/mvp-selection/tests/producer-selection.json').read_bytes())
    assert answer == fixture['refusal']
    (snapshot / 'actual-selection-refusal.json').write_text(json.dumps(answer, indent=2) + '\n', encoding='utf-8')


def test_selection_public_schema_rejects_injected_correlation(monkeypatch):
    producer = contract.producer
    boundary, rows, a, b, relation = producer.setup_entry(monkeypatch, permitted_both=False)
    answer = boundary.handle(producer.request('RELATIONSHIP', [relation]))
    contract.validator('BoundaryRefusal.schema.json').validate(answer)
    mutated = copy.deepcopy(answer)
    mutated['status']['internal_correlation_id'] = 'corr-must-remain-internal'
    with pytest.raises(ValidationError):
        contract.validator('BoundaryRefusal.schema.json').validate(mutated)


@pytest.mark.parametrize('kind', ['ACCOUNT', 'RELATIONSHIP'])
def test_actual_valid_selection_still_persists(monkeypatch, kind):
    producer = contract.producer
    boundary, rows, a, b, relation = producer.setup_entry(monkeypatch)
    answer = boundary.handle(producer.request(kind, [a] if kind == 'ACCOUNT' else [relation]))
    contract.validator('responses/selection-create.response.schema.json').validate(answer)
    selected = answer['data']
    assert rows[('49financial', selected['account_set_id'])]['account_ids'] == selected['selected_account_ids']
