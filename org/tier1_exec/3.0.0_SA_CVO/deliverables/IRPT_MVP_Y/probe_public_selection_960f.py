"""Fresh actual selection Entry projection checks for CTO013256."""
import copy
import json
import os
from pathlib import Path
import socket

import pytest

from probe_recipe_decimal import deny_network, load


def main():
    own = Path(__file__).resolve().parent
    root = own.parents[4]
    pin = os.environ.get('IRPT_SELECTION_BACKEND', '960f5f2a4501eff2670bcd0b5951926836093447')
    snap = root / '.runtime/codex-seats/3.0.0_SA_CVO~Y/outer-pair-backend' / pin
    socket.socket.connect = deny_network
    socket.socket.connect_ex = deny_network
    socket.create_connection = deny_network
    os.environ['IRPT_FIRM_REGISTRY'] = str(snap / 'data/firm_registry.json')
    base = snap / 'infra/aws/lambda/investor-reporting'
    subject = load('fresh_selection_fixture', base / 'directory/tests/test_selection_entry.py')
    contracts = load('selection_contract_validator', base / '_contracts/test_owned_outer_contracts.py')
    schema = contracts.validator(snap / 'docs/contracts/investor-reporting/v1/BoundaryRefusal.schema.json')
    controls = []
    with pytest.MonkeyPatch.context() as mp:
        boundary, rows, a, _b, _relation = subject.setup_entry(mp)
        success = boundary.handle(subject.request('ACCOUNT', [a]))
        assert success['data']['selected_account_ids'] == [a] and len(rows) == 1
        controls.append('actual_selection_success_exact_selected_set')
    with pytest.MonkeyPatch.context() as mp:
        boundary, rows, _a, _b, relation = subject.setup_entry(mp, permitted_both=False)
        refusal = boundary.handle(subject.request('RELATIONSHIP', [relation]))
        assert refusal['ok'] is False and not rows and 'data' not in refusal
        assert refusal['status']['public_reason_code'] == 'OBJECT_NOT_COVERED'
        assert 'internal_correlation_id' not in refusal['status']
        schema.validate(refusal)
        controls.append('actual_selection_partial_scope_refusal_public_schema_no_cid_no_write')
        private = copy.deepcopy(refusal)
        private['status']['internal_correlation_id'] = 'review-private-selection'
        assert list(schema.iter_errors(private))
        controls.append('selection_public_schema_rejects_reintroduced_cid')
    portal = root / '.runtime/codex-seats/3.0.0_SA_CVO~Y/outer-pair-portal' / os.environ.get(
        'IRPT_SELECTION_PORTAL', 'c09fea54e9f4613d44b874724e93b79c443f8cc8')
    supplied = json.loads((portal / 'src/pages/InvestorReporting/__tests__/mvp-selection/tests/producer-selection.json').read_text())
    assert supplied['refusal'] == refusal
    controls.append('fresh_selection_refusal_equals_repaired_portal_capture')
    doc = dict(pin=pin, success=success, refusal=refusal, controls=controls,
               limitation='Actual Entry with directory/ownership/persistence doubles; not deployed route or custody grade')
    output = own / os.environ.get('IRPT_SELECTION_DIRECTORY', 'OUTER_RETEST_960f') / 'SELECTION.json'
    assert output.resolve().is_relative_to(own.resolve())
    output.write_text(json.dumps(doc, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(dict(pin=pin, controls=controls), indent=2))


if __name__ == '__main__':
    main()
