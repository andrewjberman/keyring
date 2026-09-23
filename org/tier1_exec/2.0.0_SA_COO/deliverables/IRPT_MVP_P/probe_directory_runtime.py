"""Run only inside matching Lambda image, network disabled, no cloud credentials."""
import hashlib
import importlib
import importlib.metadata
import json
import os
from pathlib import Path
import shutil
import sys

assert sys.version_info[:2] == (3, 12)
sys.path.insert(0, '/var/task')
manifest = json.loads(Path('/proof/manifest.json').read_text())
for item in manifest['members']:
    assert hashlib.sha256((Path('/var/task') / item['member']).read_bytes()).hexdigest() == item['sha256']
os.environ['IRPT_CONTRACTS_DIR'] = '/var/task/contracts'
os.environ['IRPT_FIRM_REGISTRY'] = '/var/task/firm_registry.json'
os.environ['AWS_EC2_METADATA_DISABLED'] = 'true'
entry = importlib.import_module('entry')
owner_reads = importlib.import_module('owner_reads')
custody = importlib.import_module('custody')
assert Path(entry.__file__).resolve() == Path('/var/task/entry.py')
assert Path(owner_reads.__file__).resolve() == Path('/var/task/owner_reads.py')
assert Path(custody.__file__).resolve() == Path('/var/task/custody.py')
cold = entry.lambda_handler({'headers': {}}, None)
cold_body = json.loads(cold['body'])
assert cold_body['ok'] is False and 'data' not in cold_body
print('COLD_HANDLER_PASS: actual entry.lambda_handler, no test dependencies or mocks loaded')
print('RUNTIME_DEPENDENCIES', json.dumps({n: importlib.metadata.version(n) for n in ['boto3', 'botocore']}))

# Runtime ZIP remains untouched. Original pinned tests are placed at their
# expected repository-relative locations, with ONLY entry.py a symlink to the
# extracted runtime. Assertions/fixtures are byte-identical to their Git blobs.
layout = Path('/tmp/directory-test-repo')
shutil.copytree('/proof/test-inputs', layout)
for item in manifest['test_inputs']:
    assert hashlib.sha256((layout / item['path']).read_bytes()).hexdigest() == item['sha256']
directory = layout / 'infra/aws/lambda/investor-reporting/directory'
(directory / 'entry.py').symlink_to('/var/task/entry.py')
sys.path.insert(0, '/proof/test-deps')
sys.path.insert(0, str(directory / 'tests'))
pytest = importlib.import_module('pytest')
rc = pytest.main(['-q', '-p', 'no:cacheprovider', str(directory / 'tests')])
assert rc == 0, rc
cases = importlib.import_module('test_opal_context')
assert Path(cases.entry.__file__).resolve() == Path('/var/task/entry.py')
with pytest.MonkeyPatch.context() as patch:
    cases.arrange(patch)
    result = cases.entry.lambda_handler(cases.opal(), None)
    body = json.loads(result['body'])
    assert body['data']['context_kind'] == 'GLOBAL'
    assert body['data']['completeness'] == 'COMPLETE'
    Path('/tmp/directory-global-wire.json').write_text(json.dumps(body))
print('PAIRED_HANDLER_PASS: actual packaged lambda_handler with synthetic external data ports')
for name in ['entry', 'served', 'loaders', 'resolve', 'enforce', 'owner_reads', 'custody', 'selection', 'selection_store']:
    module = importlib.import_module(name)
    assert Path(module.__file__).resolve().parent == Path('/var/task'), (name, module.__file__)
print('PACKAGE_ORIGINS_PASS: runtime modules all resolve inside /var/task')
print('TEST_DEPENDENCIES', json.dumps({n: importlib.metadata.version(n) for n in
      ['pytest', 'jsonschema', 'referencing', 'rpds-py', 'attrs', 'jsonschema-specifications', 'pluggy', 'iniconfig', 'packaging', 'typing-extensions']}))
