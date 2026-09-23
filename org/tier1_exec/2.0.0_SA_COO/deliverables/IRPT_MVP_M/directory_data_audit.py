"""Read-only, aggregate-only directory/ownership evidence; never invokes producers.

Uses exact committed canonical helpers, not a parallel identity implementation.
S3 payloads remain in memory. Only sanitized counts and object receipts are saved.
"""
from __future__ import annotations

import argparse
from collections import Counter
import datetime as dt
import hashlib
import importlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

import boto3
from botocore.exceptions import ClientError
from jsonschema import Draft202012Validator


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-pin', required=True)
    parser.add_argument('--out', required=True)
    args = parser.parse_args()
    root = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip())
    pin = subprocess.check_output(['git', 'rev-parse', args.source_pin], text=True).strip()
    now = dt.datetime.now(dt.timezone.utc)
    report = {'measured_at_utc': now.isoformat(), 'source_pin': pin,
              'mode': 'READ_ONLY_AGGREGATE_DATA_AUDIT_NOT_AUTHORIZATION_OR_E2E',
              'source_files': {}, 'firms': {}}
    sources = {
        'ids.py': 'infra/aws/lambda/investor-reporting/_ids/ids.py',
        'raw_keys.json': 'infra/aws/lambda/investor-reporting/_ids/raw_keys.json',
        'data/custodian_key_seam.json': 'infra/aws/lambda/investor-reporting/_ids/data/custodian_key_seam.json',
        'resolve.py': 'infra/aws/lambda/investor-reporting/_scope/resolve.py',
        'selection.py': 'infra/aws/lambda/investor-reporting/_scope/selection.py',
        'firm_registry.json': 'data/firm_registry.json',
        'DirectoryEntry.schema.json': 'docs/contracts/investor-reporting/v1/DirectoryEntry.schema.json',
        'trading_calendar.py': 'lib/trading_calendar.py',
    }
    s3 = boto3.client('s3', region_name='us-east-1')
    config = boto3.client('lambda', region_name='us-east-1').get_function_configuration(
        FunctionName='irpt-directory-search')
    env = config.get('Environment', {}).get('Variables', {})
    mapping = json.loads(env['IRPT_DIRECTORY_BUCKET_MAP'])
    prefix = env.get('IRPT_DIRECTORY_PREFIX', 'investor-reporting/directory')
    own_template = env.get('IRPT_OWNERSHIP_KEY', 'platinum/{firm}/ownership_map.json')
    report['runtime_configuration'] = {
        'function': config['FunctionName'], 'code_sha256_base64': config['CodeSha256'],
        'last_modified': config['LastModified'], 'directory_bucket_map': mapping,
        'directory_prefix': prefix, 'ownership_key_template': own_template,
        'id_namespace': env.get('IRPT_DIRECTORY_ID_NAMESPACE', 'IRPT_DIRECTORY_ID_NS_V1'),
        'access_limit': 'Operator S3 reads; no Lambda execution-role simulation or HTTP invocation.',
    }

    def read(bucket, key, version=None):
        request = {'Bucket': bucket, 'Key': key}
        if version:
            request['VersionId'] = version
        response = s3.get_object(**request)
        with response['Body'] as stream:
            raw = stream.read(16 * 1024 * 1024 + 1)
        if len(raw) > 16 * 1024 * 1024:
            raise ValueError('audit input bound exceeded')
        receipt = {'bucket': bucket, 'key': key, 'version_id': response.get('VersionId'),
                   'sha256': sha(raw), 'bytes': len(raw),
                   'last_modified_utc': response['LastModified'].isoformat()}
        return json.loads(raw), receipt

    def capture(bucket, key):
        doc, receipt = read(bucket, key)
        version = receipt['version_id']
        receipt['exact_version_verified'] = False
        if version and version != 'null':
            _, again = read(bucket, key, version)
            receipt['exact_version_verified'] = all(
                receipt[k] == again[k] for k in again)
        return doc, receipt

    def failure(exc):
        if isinstance(exc, ClientError):
            code = exc.response.get('Error', {}).get('Code', 'UNKNOWN')
            status = exc.response.get('ResponseMetadata', {}).get('HTTPStatusCode')
            return {'state': 'ABSENT' if code in ('NoSuchKey', '404') else 'UNREADABLE',
                    'error_code': code, 'http_status': status}
        return {'state': 'INVALID_OR_INCOMPATIBLE', 'error_class': type(exc).__name__}

    def projection_reason(exc):
        # Match fixed canonical messages, never retain their instance text.
        message = str(exc)
        for marker, reason in (
            ('raw key that is a display name', 'NAME_SHAPED_RAW_KEY'),
            ('raw key that is an e-mail address', 'EMAIL_SHAPED_RAW_KEY'),
            ('raw key must not be None', 'NULL_RAW_KEY'),
            ('raw key must be a non-empty value', 'EMPTY_RAW_KEY'),
        ):
            if marker in message:
                return reason
        return type(exc).__name__

    with tempfile.TemporaryDirectory(prefix='irpt-m-data-audit-') as directory:
        temp = Path(directory)
        for name, path in sources.items():
            raw = subprocess.check_output(['git', 'show', f'{pin}:{path}'], cwd=root)
            target = temp / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(raw)
            report['source_files'][path] = {'sha256': sha(raw)}
        os.environ['IRPT_FIRM_REGISTRY'] = str(temp / 'firm_registry.json')
        os.environ['IRPT_DIRECTORY_ID_NAMESPACE'] = report['runtime_configuration']['id_namespace']
        sys.path.insert(0, str(temp))
        ids = importlib.import_module('ids')
        scope = importlib.import_module('resolve')
        selection = importlib.import_module('selection')
        calendar = importlib.import_module('trading_calendar')
        schema = json.loads((temp / 'DirectoryEntry.schema.json').read_text())
        validator = Draft202012Validator(schema)
        registry = json.loads((temp / 'firm_registry.json').read_text())
        registry_rows = registry['firms']
        prior = calendar.prev_trading_day(now.date())
        report['calendar'] = {'source': calendar.calendar_source(),
                              'prior_completed_trading_day': prior.isoformat(),
                              'basis': 'Conservative prior trading day; not an assumed producer SLA.'}
        for firm in ('49financial', 'inflection', 'cottonwood'):
            row = report['firms'][firm] = {}
            registry_row = next(r for r in registry_rows if r['firm_id'] == firm)
            row['registry'] = {k: registry_row.get(k) for k in ('firm_id', 'enabled', 'kind', 'bucket')}
            bucket = mapping[firm]
            pointer_key = prefix + '/latest.json'
            directory_doc = None
            try:
                pointer, pointer_receipt = capture(bucket, pointer_key)
                row['pointer'] = pointer_receipt
                key = pointer['key']
                if not isinstance(key, str) or not key.startswith(prefix + '/') or '..' in key:
                    raise ValueError('pointer target outside directory prefix')
                directory_doc, receipt = capture(bucket, key)
                row['directory_object'] = receipt
                entries = directory_doc['entries']
                if not isinstance(entries, list):
                    raise ValueError('entries not list')
                opaque = directory_doc.get('firm_id_opaque')
                expected = ids.opaque('firm', firm, firm)
                population, census = scope.firm_population(directory_doc, opaque)
                schema_errors = Counter()
                invalid_entries = 0
                for entry in entries:
                    errors = list(validator.iter_errors(entry))
                    invalid_entries += bool(errors)
                    for error in errors:
                        # Schema location only. No raw instance value or error message.
                        schema_errors['/'.join(str(x) for x in error.absolute_schema_path)] += 1
                dates = Counter(e.get('revision', {}).get('as_of_business_date') for e in entries)
                completion_dates = Counter(e.get('revision', {}).get('source_completion_date') for e in entries)
                business_date = dt.date.fromisoformat(directory_doc['as_of_business_date'])
                age = calendar.trading_days_behind(business_date, prior)
                entry_firms = Counter(e.get('ids', {}).get('firm_id') for e in entries)
                revision = directory_doc.get('directory_revision')
                entry_revision_mismatch = sum(e.get('revision', {}).get('directory_revision') != revision for e in entries)
                row['directory'] = {
                    'state': 'READABLE_EMPTY' if not entries else 'READABLE_NONEMPTY',
                    'schema': directory_doc.get('schema'), 'schema_version': directory_doc.get('schema_version'),
                    'declared_registry_tenant': directory_doc.get('firm_id'),
                    'opaque_firm_id': opaque, 'canonical_opaque_firm_matches': opaque == expected,
                    'entry_firm_mismatch_count': sum(n for value, n in entry_firms.items() if value != opaque),
                    'declared_entry_count': directory_doc.get('entry_count'), 'actual_entry_count': len(entries),
                    'schema_valid_entries': len(entries) - invalid_entries,
                    'schema_invalid_entries': invalid_entries, 'schema_error_counts': dict(schema_errors),
                    'declared_revision': revision, 'content_revision_sha256': selection.directory_revision(directory_doc),
                    'entry_revision_mismatch_count': entry_revision_mismatch,
                    'source_revision': directory_doc.get('source_revision'),
                    'business_date': business_date.isoformat(),
                    'source_completion_date': directory_doc.get('source_completion_date'),
                    'entry_business_date_counts': dict(dates), 'entry_source_completion_date_counts': dict(completion_dates),
                    'trading_days_behind_prior_completed_day': age,
                    'freshness': 'DATED_BEHIND_PRIOR_TRADING_DAY' if age else 'AT_OR_AFTER_PRIOR_TRADING_DAY',
                    'population': census,
                    'nonissued_unique_account_count': sum(not ids.is_issued('account', a) for a in population),
                    'pointer_metadata_matches': {k: pointer.get(k) == directory_doc.get(k) for k in
                        ('directory_revision', 'entry_count', 'as_of_business_date', 'source_completion_date', 'generated_at')},
                }
                row['pointer']['still_current_after_target_read'] = s3.head_object(
                    Bucket=bucket, Key=pointer_key).get('VersionId') == pointer_receipt['version_id']
            except Exception as exc:
                row['directory_failure'] = failure(exc)

            ownership_key = own_template.format(firm=firm)
            try:
                ownership, receipt = capture(bucket, ownership_key)
                row['ownership_object'] = receipt
                advisors = ownership.get('advisors')
                if ownership.get('schema_version') != 1 or not isinstance(advisors, dict):
                    raise ValueError('ownership schema incompatible')
                own = row['ownership'] = {
                    'state': 'PRESENT_EMPTY' if not advisors else 'PRESENT_NONEMPTY',
                    'schema_version': ownership['schema_version'], 'advisor_count': len(advisors),
                    'top_level_fields': sorted(ownership),
                    'declared_firm_matches_if_present': ownership.get('firm_id', firm) == firm,
                    'generated_at': ownership.get('generated_at'),
                }
                account_values, relation_values = set(), set()
                projected_accounts, projected_relations = set(), set()
                projection_failures = Counter()
                account_rows = relationship_rows = nonempty_advisors = 0
                projection = ids.projection_for_firm(firm)
                seam_name = ids.raw_key_for(firm, 'account').get('projection_seam')
                seam_index = ids.load_seam_index(seam_name).get('index', {}) if seam_name else {}
                for advisor, grant in advisors.items():
                    if not isinstance(grant, dict) or any(not isinstance(grant.get(k, []), list) for k in ('accounts', 'relationships')):
                        projection_failures['INVALID_GRANT_SHAPE'] += 1
                        continue
                    accounts, relationships = grant.get('accounts', []), grant.get('relationships', [])
                    account_rows += len(accounts)
                    relationship_rows += len(relationships)
                    nonempty_advisors += bool(accounts or relationships)
                    account_values.update(accounts)
                    relation_values.update(relationships)
                    try:
                        pa, pr, _ = scope.advisor_grant(ownership, advisor, projection)
                        projected_accounts.update(pa)
                        projected_relations.update(pr)
                    except Exception as exc:
                        projection_failures[projection_reason(exc)] += 1
                own.update({'advisor_nonempty_count': nonempty_advisors,
                            'account_grant_rows': account_rows, 'relationship_grant_rows': relationship_rows,
                            'unique_raw_accounts': len(account_values), 'unique_raw_relationships': len(relation_values),
                            'unique_projected_accounts': len(projected_accounts),
                            'unique_projected_relationships': len(projected_relations),
                            'projection_error_advisor_counts': dict(projection_failures)})
                if directory_doc is not None:
                    opaque = directory_doc.get('firm_id_opaque')
                    population = set(scope.firm_population(directory_doc, opaque)[0])
                    relationships = scope._relationship_index(directory_doc, opaque)
                    reasons = scope.unmatched_reasons(projected_accounts, directory_doc, opaque)
                    relation_matched = projected_relations.intersection(relationships)
                    expanded = {a for r in relation_matched for a in relationships[r]}
                    own['successful_advisor_helper_compatibility'] = {
                        'advisor_denominator': len(advisors) - sum(projection_failures.values()),
                        'unprojected_direct_account_matches': len(account_values.intersection(population)),
                        'projected_account_matches': len(projected_accounts.intersection(population)),
                        'unmatched_account_reason_counts': dict(Counter(r['reason'].split(':', 1)[0] for r in reasons)),
                        'projected_relationship_matches': len(relation_matched),
                        'unmatched_projected_relationships': len(projected_relations - set(relationships)),
                        'union_accounts_reachable_by_any_advisor': len((projected_accounts | expanded).intersection(population)),
                        'directory_accounts_without_any_projected_advisor_grant': len(population - projected_accounts - expanded),
                        'note': 'Only advisors whose entire canonical advisor_grant call returned. Any rejected account or relationship makes that whole call fail. Not a principal authorization or complete raw-account overlap census.',
                    }
                    own['individual_key_diagnostic'] = {}
                    for kind, raw_values, target_values in (
                        ('account', account_values, population),
                        ('relationship', relation_values, set(relationships)),
                    ):
                        values, errors, stages = set(), Counter(), Counter()
                        for value in raw_values:
                            try:
                                values.add(projection(kind, value))
                            except Exception as exc:
                                errors[projection_reason(exc)] += 1
                                mapped = seam_index.get(str(value).strip()) if kind == 'account' else None
                                stage = 'BUNDLED_SEAM_TARGET' if mapped is not None else 'DIRECT_RAW_KEY'
                                stages[stage] += 1
                        diagnostic = {
                            'unique_raw_values': len(raw_values), 'unique_projected_values': len(values),
                            'key_projection_error_counts': dict(errors),
                            'key_projection_error_stage_counts': dict(stages),
                            'directory_matches': len(values.intersection(target_values)),
                            'not_in_directory': len(values - target_values),
                            'note': 'Independent per-key diagnostic only; never a fallback grant or relaxation of advisor_grant.',
                        }
                        if kind == 'account':
                            diagnostic['unmatched_reason_counts'] = dict(Counter(
                                r['reason'].split(':', 1)[0] for r in
                                scope.unmatched_reasons(values, directory_doc, opaque)))
                        own['individual_key_diagnostic'][kind] = diagnostic
                own['projection_seam'] = seam_name
                if seam_name:
                    seam = ids.load_seam_index(seam_name)
                    own['seam_index_count'] = len(seam.get('index', {}))
                own['still_current_after_projection'] = s3.head_object(
                    Bucket=bucket, Key=ownership_key).get('VersionId') == receipt['version_id']
            except Exception as exc:
                row['ownership_failure'] = {'bucket': bucket, 'key': ownership_key, **failure(exc)}
            print(json.dumps({'firm': firm, 'directory': row.get('directory', {}).get('state'),
                              'ownership': row.get('ownership', {}).get('state'),
                              'failure_fields': [k for k in row if k.endswith('_failure')]}))
    report['completed_at_utc'] = dt.datetime.now(dt.timezone.utc).isoformat()
    Path(args.out).write_text(json.dumps(report, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print('Sanitized evidence written: ' + args.out)


if __name__ == '__main__':
    main()
