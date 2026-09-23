"""Offline probe for extracted source /var/task and dependencies /opt/python.

Run in a digest-pinned AWS Lambda Python 3.12 container with network disabled.
No production snapshot, storage, credentials or deployment is used.
"""
import importlib
import importlib.metadata
import json
from pathlib import Path
import sys

def main():
    sys.path[:0] = ['/var/task', '/opt/python']
    assert sys.version_info[:2] == (3, 12)
    expected = {
        'jsonschema': ('jsonschema', '4.26.0'),
        'attrs': ('attrs', '26.1.0'),
        'jsonschema-specifications': ('jsonschema_specifications', '2025.9.1'),
        'referencing': ('referencing', '0.37.0'),
        'rpds-py': ('rpds', '2026.6.3'),
        'typing_extensions': ('typing_extensions', '4.16.0'),
    }
    dependency_rows = []
    for distribution, (module_name, version) in expected.items():
        module = importlib.import_module(module_name)
        origin = Path(module.__file__).resolve()
        assert origin.is_relative_to(Path('/opt/python')), (module_name, str(origin))
        actual = importlib.metadata.version(distribution)
        assert actual == version, (distribution, actual, version)
        dependency_rows.append(dict(distribution=distribution, version=actual, origin=str(origin)))

    from jsonschema import Draft202012Validator, ValidationError
    from rpds import HashTrieMap
    assert HashTrieMap({'native': 'linux'})['native'] == 'linux'
    validator = Draft202012Validator({'type': 'integer'})
    validator.validate(1)
    try:
        validator.validate('not-an-integer')
    except ValidationError:
        pass
    else:
        raise AssertionError('schema negative control accepted')

    import boto3
    from botocore.stub import Stubber
    import entry
    import custody_submission
    from recipe_snapshot import capture_configuration
    assert Path(custody_submission.__file__).resolve().parent == Path('/var/task')
    sdk = boto3.client('dynamodb', region_name='us-east-1',
                       aws_access_key_id='offline', aws_secret_access_key='offline')
    with Stubber(sdk):
        boundary = custody_submission.build_custody_entry(
            dynamodb=sdk, table=object(), s3=object(), schema_directory='/var/task/contracts',
            reporting_policy=lambda *args: None,
            reporting_destination=lambda *args, **kwargs: None,
            authorize_snapshot=lambda *args: False, load_normalized=lambda *args: None,
            send=lambda *args: None, queue_url='offline-no-send', clock=lambda: 0,
            ingestion_revision='offline-construction', destination_revision='offline-construction',
            configuration=lambda owner, browser: capture_configuration(owner, browser,
                templates_path='/var/task/templates.json', settings_path='/var/task/settings.json'))
        assert boundary is not entry.ENTRY

        from accepted_custody import AcceptedCustodyReader
        from custody_binding import CustodyBindingStore
        reader = AcceptedCustodyReader(CustodyBindingStore(sdk, 'offline-requests'),
            current_selection=lambda *args: None, publication_for=lambda *args: None)
        accepted_boundary = custody_submission.build_accepted_custody_entry(
            reader, dynamodb=sdk, table=object(), s3=object(), schema_directory='/var/task/contracts',
            reporting_policy=lambda *args: None,
            reporting_destination=lambda *args, **kwargs: None,
            send=lambda *args: None, queue_url='offline-no-send', clock=lambda: 0,
            ingestion_revision='offline-construction', destination_revision='offline-construction',
            configuration=lambda owner, browser: capture_configuration(owner, browser,
                templates_path='/var/task/templates.json', settings_path='/var/task/settings.json'))
        assert accepted_boundary is not entry.ENTRY
        assert reader.interpret_source is None and reader.validate_evidence is None
        assert reader.authorize_snapshot({}, {}) is False
        for name in ('accepted_custody', 'custody_binding', 'custody_portfolio', 'parse'):
            assert Path(importlib.import_module(name).__file__).resolve().parent == Path('/var/task')

    print(json.dumps(dict(result='PASS', python=sys.version, dependencies=dependency_rows,
        native_rpds='PASS', schema_positive_and_negative='PASS', flat_factory_construction='PASS',
        accepted_factory_construction='PASS', absent_source_refusal='PASS',
        limits='Synthetic refusing producer ports; no request, storage, queue, vendor or live acceptance.'), indent=2))


if __name__ == '__main__':
    main()
