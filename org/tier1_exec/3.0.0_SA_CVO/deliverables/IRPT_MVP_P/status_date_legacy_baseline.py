"""Measure only the old closed status schema; not a verdict on the new extension."""
import copy
import hashlib
import json
from pathlib import Path
import subprocess

from jsonschema import Draft202012Validator

PIN = 'dea338a397fc71efc2cddee0d711e99effbefdfa'
SCHEMA = 'docs/contracts/investor-reporting/v1/StatusEnvelope.schema.json'
FIXTURE = 'infra/aws/lambda/investor-reporting/_contracts/fixtures/StatusEnvelope.valid.json'
HERE = Path(__file__).resolve()
ROOT = HERE.parents[5]


def blob(path):
    return subprocess.check_output(['git', 'show', PIN + ':' + path], cwd=ROOT)


schema_bytes = blob(SCHEMA)
schema = json.loads(schema_bytes)
validator = Draft202012Validator(schema)
fixture = json.loads(blob(FIXTURE))['instance']
results = []


def check(label, value, valid):
    errors = list(validator.iter_errors(value))
    assert (not errors) is valid, (label, [e.message for e in errors])
    results.append({'case': label, 'valid': not errors, 'expected_valid': valid,
                    'errors': [{'path': list(e.absolute_path), 'validator': e.validator} for e in errors]})


check('unchanged_recorded_positive', fixture, True)
for state in ('READY', 'PARTIAL', 'STALE', 'NEEDS_CORRECTION', 'UNCERTAIN'):
    value = copy.deepcopy(fixture)
    value['state'] = state
    value['source_dates'].pop('business_date', None)
    check(state + '_missing_business_date', value, False)
    value['source_dates']['business_date'] = None
    check(state + '_null_business_date', value, False)
    value['source_dates'].pop('business_date')
    value['source_dates']['date_basis'] = 'UNDATED_INPUT'
    check(state + '_new_basis_is_incompatible', value, False)
for state in ('QUEUED', 'RUNNING', 'UNAVAILABLE', 'FAILED'):
    value = copy.deepcopy(fixture)
    value['state'] = state
    value['source_dates'].pop('business_date', None)
    check(state + '_no_source_date_allowed', value, True)
    value['source_dates']['business_date'] = None
    check(state + '_null_business_date_rejected', value, False)
for basis in ('UNDATED_INPUT', 'PER_SECTION'):
    value = copy.deepcopy(fixture)
    value['source_dates']['date_basis'] = basis
    check(basis + '_unknown_even_with_existing_date', value, False)
value = copy.deepcopy(fixture)
value['unagreed_extension'] = True
check('closed_top_level_preserved', value, False)
value = copy.deepcopy(fixture)
value['state'] = 'READY'
value['source_dates'] = {'source_completion_date': '2026-09-22', 'as_of': '2026-09-22T23:59:00Z'}
check('completion_and_retrieval_do_not_satisfy_business_date', value, False)
evidence = {'pin': PIN, 'schema': SCHEMA, 'schema_sha256': hashlib.sha256(schema_bytes).hexdigest(),
            'cases': results, 'passed': len(results),
            'limits': 'Old JSON schema and existing fixture only. No new accepted prospect example, actual handler, browser parser/UI, export, frozen reopen, negotiation or paired compatibility proof.'}
HERE.with_suffix('.json').write_text(json.dumps(evidence, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'baseline_checks_passed': len(results), 'schema_sha256': evidence['schema_sha256']}))
