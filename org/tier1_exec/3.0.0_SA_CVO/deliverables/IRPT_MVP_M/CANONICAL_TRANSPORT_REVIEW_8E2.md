# Canonical profile transport and retained prospect input: independent review

Reviewer: `3.0.0_SA_CVO~M`, 2026-09-23 UTC.
Authority: completion CONTRACT reviewer mandate, maintained-source rulings 01/02.
Trigger: exact COO~M notification `20260923T030243Z`.

## Verdict and boundary

**BOUNDED SOURCE PASS** for
`8e2ba7830352b2a34c97ec96984d043654cab340`, parent
`55a65d3bdb52c66b106ccfc5c50e8e745356fb6b`.
No adapter defect was reproduced in this source/SDK/retained-input scope.
This does not establish an installed factory, IAM, live canonical reads,
production retention activation, custody authorization, vendor/render, deployed
runtime, acceptance-to-worker execution or full M/E2E.

The clean detached reviewer checkout is
`C:/Users/AndrewBerman/Desktop/ajb_irpt_cvo_m_review`. The five candidate files
are the two new `_scope/canonical_profile_reads.py` and
`_scope/retained_input_authorizer.py` modules, their supplied SDK tests and
retained probe, and M CANONICAL_PROFILE_RUNTIME.md. Read all five completely.
Also read Y's complete owner contract at `9db2deb4ac` and the relevant actual
UploadService/P retention functions at exact paired pin
`ef9e8f51c4fe81b60c89f7a1a3a6ec575e3cc182`, canonical TS partner table-name
contract, and checked-in users table/index definition.

## Measured result

| Execution at exact M candidate | Result |
| --- | --- |
| `python -m pytest infra/aws/lambda/investor-reporting/_scope/tests -q` | 123 passed, 57 subtests passed, 2.11s |
| `python infra/aws/lambda/investor-reporting/_scope/tests/probe_retained_input_authorizer.py` | 19 controls pass, exact Y/P pin above, synthetic ACTIVE policy/offline storage |
| `python -m pytest <independent driver below> -q` | 42 passed, 4.96s |

The independent driver constructs its own botocore Stubber expectations and
adversarial cases, uses actual M source, and extracts actual Y/P intake/reports
code and schemas from the exact paired Git pin into a temporary directory. It
reuses only Y/P test infrastructure to construct uploads and offline retained
storage/policy. Network connections are blocked; credentials are dummy values.
No AWS read/write or vendor request occurred. Source checks of the other two
firms' table addressing do not constitute real three-firm retained input proof;
the composed retained fixtures use synthetic 49financial uploads.

An initial independent run reported 34 pass/8 fail because the reviewer expected
PermissionError alone for retention failures. All eight actually refused with
the real P RetentionRefused/ReportDenied (including RetentionExpired) hierarchy.
Only the test's accepted refusal classes were corrected after inspecting that
hierarchy. Candidate and peer implementation stayed unchanged. The final run
above is the corrected 42-test denominator; no refusal was changed into success.

Independent driver SHA256:
`edcaac32085a6d21119406e3a9c4b31134fb712f4c0a174f74a89a77e0447fb4`.
Runtime path:
`C:/Users/AndrewBerman/Desktop/ajb_workspace/.runtime/codex-seats/3.0.0_SA_CVO~M/test_runtime_8e2_review.py`.
Complete driver is embedded below.

## Source and protocol findings

The adapter queries `opal-users-v2`/`email-index`, limit two, rejects duplicate or
incomplete results, and uses the returned actual PK with SK PROFILE. It does not
reconstruct a PK from email. Index and PROFILE readback must match the subject and
key. Missing profiles return unavailable without fallback; SDK errors propagate.
Strongly consistent GetItem requests project only approved profile/report fields.
Independent checks cover wrong DynamoDB-typed identities, missing readback
identity, two distinct PKs with one subject, an empty truncated page, and SDK
failure after a successful index query.

The Query itself has no ProjectionExpression; the checked-in Terraform
`infra/aws/terraform/shared-infra/dynamo.tf` defines that GSI as KEYS_ONLY. This is
a checked-in source-contract observation, not a measured deployed index setting.
Unexpected additional returned fields are not projected into report values.
The GSI remains eventually consistent: these checks do not prove transactional
uniqueness or eliminate stale-index races. The actual source resolver's repeated
profile/current-owner checks are not a transaction either.

Partner calls use exactly `opal-partner-{verified firm}` and email key, strong
consistency and the approved projection. The stricter IRPT firm enumeration and
lowercase ASCII checks precede SDK use. Synthetic SDK requests cover 49financial,
cottonwood and inflection without alternate table, scan or write. The retained
composition controls cover advisor and operations; operations use actual user
name and perform no partner lookup. No credentials or MFA contact data enter
the returned profile projections.

The retained authorizer preserves the existing lane distinction: document owner
is the complete base prospect-owner-v1, while repository owner additionally has
account_ids=[] and the exact UP- upload identity. The constructor requires that
exact extended owner and content-addressed normalized reference, copies selected
bindings, and refuses custody or invented account scope. Calls re-resolve current
trusted headers, require exact selected input, run real UploadService.read_input,
compare returned owner/ref/source lane/upload, check the actual P retention
owner/family/logical ID, then recheck current identity. Recipient display and
client-provided fingerprints are not substituted for server assembly.

The actual Y/P chain checks normalized bytes/ref/digest, original CSV source and
retained dependencies. Independent controls remove, expire or change owners,
families and logical IDs on both original and normalized retention rows; all
refuse. Current grant revocation, changed headers during blob read, changed
returned owner/receipt/source, retention removal after reading, and invalid
constructor bindings refuse. The supplied unchanged probe separately exercises
refresh lineage and corruption, same-principal wrong-input selection, pending
policy, receipt drift, expiry during read and final profile-capture revocation.

Both M adapters compose successfully with actual Y/P reader/repository/retention
logic for synthetic advisor and operations input. Repeated authorization performs
no artifact writes; later revocation refuses. This measures the exercised source
composition, not installed protected HTTP entry, accepted stored composition,
queue worker or cover behavior.

## Integration obligations and unchanged holds

Y must supply the actual verified factory/client, current authorization and
retention policy, server-selected owner/reference and final acceptance assembly.
The caller must preserve error refusal at its public boundary. The authorizer
intentionally depends on actual UploadService/ArtifactRepository current-access
semantics; it does not independently mint grants, authenticate headers or activate
retention. Synthetic ACTIVE configuration is not the real X10
PENDING_ENFORCEMENT state. No live IAM or deployed source/index projection was
measured here.

Custody remains unavailable pending its real selected producer, normalized input,
retained owner and current account-authorization implementation. Recipe/title,
all selected comparisons, actual vendor limits and rendering, accepted-byte
storage/replay and independent P/Y integrated reviews remain separate. No
transactional cross-store uniqueness/freshness claim follows. Existing economic,
publication, runtime, live and full-product holds are unchanged. Prior source
verdicts `e64d917252` and `5da821b8a4` remain separately bounded; no grade is
inherited or expanded by this candidate.

## Reproducible independent driver

Restore this UTF-8 script and run it at the exact M candidate. ROOT may be updated
only to the clean review checkout location. The Y/P pin remains explicit.

```python
"""Independent M SDK/retained-input review. Synthetic I/O, actual pinned Y/P."""
import copy
import importlib
import socket
import subprocess
import sys
from pathlib import Path
from types import SimpleNamespace

import boto3
from boto3.dynamodb.types import TypeSerializer
from botocore.exceptions import ClientError
from botocore.stub import Stubber
import pytest

ROOT = Path('C:/Users/AndrewBerman/Desktop/ajb_irpt_cvo_m_review')
BASE = 'infra/aws/lambda/investor-reporting/'
PIN = 'ef9e8f51c4fe81b60c89f7a1a3a6ec575e3cc182'
sys.path[:0] = [str(ROOT / BASE / d) for d in ('_scope', '_authz')]
from canonical_profile_reads import CanonicalProfileReaders
from retained_input_authorizer import RetainedProspectInputAuthorizer
from maintained_sources import MaintainedSourceRefused, snapshot_profile_sources
from prospect import resolve_prospect_owner


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def refuse(*a, **kw): raise AssertionError('network prohibited')
    monkeypatch.setattr(socket, 'create_connection', refuse)
    monkeypatch.setattr(socket.socket, 'connect', refuse)


@pytest.fixture(scope='session')
def peers(tmp_path_factory):
    root = tmp_path_factory.mktemp('pinned_y_p_8e2')
    prefixes = [BASE + 'intake', BASE + 'reports', 'docs/contracts/investor-reporting/v1/']
    paths = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', PIN, '--', *prefixes], cwd=ROOT, text=True).splitlines()
    for path in paths:
        if path.endswith(('.py', '.json')):
            target = root / path; target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(subprocess.check_output(['git', 'show', PIN + ':' + path], cwd=ROOT))
    sys.path[:0] = [str(root / BASE / d) for d in ('intake', 'intake/tests', 'reports', 'reports/tests')]
    return SimpleNamespace(uploads=importlib.import_module('test_uploads'),
        tests=importlib.import_module('test_retention'), repo=importlib.import_module('repository'),
        retention=importlib.import_module('retention'))


def setup(peers, operations=False):
    c = peers.uploads.UploadIntegrationTests(methodName='runTest'); c.setUp()
    if operations:
        c.headers.update({'x-user-role': 'admin', 'x-advisor-id': ''})
        c.owner = resolve_prospect_owner(c.headers)
        c.principal = {key: c.owner[key] for key in ('firm_id', 'principal_id')}
    w = peers.tests.world.__wrapped__()
    w.registered['families']['NORMALIZED_PORTFOLIO'] = {'unreferenced_days': 30, 'accepted_ceiling_days': 2555}
    def allow(principal, owner): return w.state.access and c.authorize(principal, owner)
    policy = peers.retention.RetentionPolicy(peers.retention.DynamoRetentionIndex(w.table),
        w.policy.reporting_policy, allow, clock=lambda: w.state.now)
    c.service.index = peers.repo.DynamoReportIndex(w.table)
    c.service.authorize_current = allow
    c.service.artifacts = peers.repo.ArtifactRepository(c.service.index,
        peers.repo.S3ReportBlobs(c.s3, lambda firm, family, identity, sha:
            ('synthetic-private', '/'.join((firm, family, identity, sha)))),
        allow, {'ORIGINAL_CSV', 'NORMALIZED_PORTFOLIO'}, retention=policy)
    created = c.create(); assert created['state'] == 'NORMALIZED'
    loaded = c.service.read_input(c.principal, c.owner, created['input_id'])
    adapter = RetainedProspectInputAuthorizer(headers=c.headers, uploads=c.service,
        expected_owner=loaded['owner'], expected_input_ref=loaded['input_ref'])
    return c, w, created, loaded, adapter


def invoke(e):
    c, _, _, loaded, adapter = e
    return adapter(c.owner, loaded['input_ref'])


EMAIL = 'advisor@example.invalid'
def typed(row): return {key: TypeSerializer().serialize(value) for key, value in row.items()}
def query():
    return {'TableName': 'opal-users-v2', 'IndexName': 'email-index',
            'KeyConditionExpression': 'email = :email',
            'ExpressionAttributeValues': {':email': {'S': EMAIL}}, 'Limit': 2}
def projected(table, key, fields):
    names = {'#f' + str(i): field for i, field in enumerate(fields)}
    return {'TableName': table, 'Key': typed(key), 'ConsistentRead': True,
            'ProjectionExpression': ', '.join(names), 'ExpressionAttributeNames': names}
KEY = {'PK': 'usr_actual_opaque_pk', 'SK': 'PROFILE', 'email': EMAIL}
USER_GET = projected('opal-users-v2', {'PK': KEY['PK'], 'SK': 'PROFILE'},
                     ('PK', 'SK', 'email', 'firmId', 'status', 'name', 'updatedAt'))


@pytest.fixture
def sdk():
    client = boto3.client('dynamodb', region_name='us-east-1',
                          aws_access_key_id='offline', aws_secret_access_key='offline')
    with Stubber(client) as stub:
        yield CanonicalProfileReaders(client), stub
        stub.assert_no_pending_responses()


@pytest.mark.parametrize('firm', ['49financial', 'cottonwood', 'inflection'])
def test_sdk_canonical_tables_keys_projection_and_detached_output(sdk, firm):
    reader, stub = sdk
    row = {**KEY, 'firmId': firm, 'status': 'active', 'name': 'Actual User',
           'passwordHash': 'NEVER-RETURN', 'phoneNumber': 'MFA-ONLY'}
    stub.add_response('query', {'Items': [typed(KEY)]}, query())
    stub.add_response('get_item', {'Item': typed(row)}, USER_GET)
    result = reader.get_user(EMAIL)
    assert result == {'email': EMAIL, 'firmId': firm, 'status': 'active', 'name': 'Actual User'}
    partner = {'email': EMAIL, 'firmId': firm, 'advisorKey': 'actual-advisor',
               'advisorName': 'Actual Advisor', 'firmRole': None, 'credentials': 'NEVER-RETURN'}
    expect = projected('opal-partner-' + firm, {'email': EMAIL},
                        ('email', 'firmId', 'advisorKey', 'advisorName', 'firmRole', 'updatedAt'))
    stub.add_response('get_item', {'Item': typed(partner)}, expect)
    answer = reader.get_partner_profile(EMAIL, firm)
    assert answer['firmRole'] == 'user' and answer['advisorKey'] == 'actual-advisor'
    assert set(answer['raw']) == {'email', 'firmId', 'advisorKey', 'advisorName', 'firmRole'}
    assert 'NEVER-RETURN' not in repr(answer)


@pytest.mark.parametrize('change', [{'PK': None}, {'PK': 12}, {'SK': None},
    {'email': None}, {'email': 'ADVISOR@example.invalid'}])
def test_index_wrong_typed_identity_refuses_before_profile_get(sdk, change):
    reader, stub = sdk
    stub.add_response('query', {'Items': [typed(KEY | change)]}, query())
    with pytest.raises(MaintainedSourceRefused): reader.get_user(EMAIL)


def test_duplicate_distinct_primary_keys_and_empty_truncated_page_refuse(sdk):
    reader, stub = sdk
    for response in [{'Items': [typed(KEY), typed(KEY | {'PK': 'other_actual_pk'})]},
                     {'Items': [], 'LastEvaluatedKey': typed(KEY)}]:
        stub.add_response('query', response, query())
        with pytest.raises(MaintainedSourceRefused): reader.get_user(EMAIL)


@pytest.mark.parametrize('key', ['PK', 'SK', 'email'])
def test_profile_disappearing_readback_identity_refuses(sdk, key):
    reader, stub = sdk
    row = dict(KEY); del row[key]
    stub.add_response('query', {'Items': [typed(KEY)]}, query())
    stub.add_response('get_item', {'Item': typed(row)}, USER_GET)
    with pytest.raises(MaintainedSourceRefused): reader.get_user(EMAIL)


def test_profile_sdk_error_is_propagated(sdk):
    reader, stub = sdk
    stub.add_response('query', {'Items': [typed(KEY)]}, query())
    stub.add_client_error('get_item', 'ProvisionedThroughputExceededException', expected_params=USER_GET)
    with pytest.raises(ClientError): reader.get_user(EMAIL)


@pytest.mark.parametrize('operations', [False, True])
def test_actual_retained_authorizer_composes_sdk_reads_without_writes(peers, sdk, operations):
    e = setup(peers, operations); c, w, _, loaded, adapter = e
    reader, stub = sdk; count = c.s3.put_count
    for _ in range(2):
        stub.add_response('query', {'Items': [typed(KEY)]}, query())
        stub.add_response('get_item', {'Item': typed(KEY | {'firmId': '49financial',
            'status': 'active', 'name': 'Actual User'})}, USER_GET)
        if not operations:
            expect = projected('opal-partner-49financial', {'email': EMAIL},
                ('email', 'firmId', 'advisorKey', 'advisorName', 'firmRole', 'updatedAt'))
            stub.add_response('get_item', {'Item': typed({'email': EMAIL,
                'advisorKey': c.owner['advisor_id'], 'advisorName': 'Actual Advisor'})}, expect)
    snap = snapshot_profile_sources(c.headers, loaded['input_ref'], get_user=reader.get_user,
        get_partner_profile=reader.get_partner_profile, authorize_input=adapter)
    assert snap.prepared_by == ('Actual User' if operations else 'Actual Advisor')
    assert snap.input_ref == loaded['input_ref'] and c.s3.put_count == count
    assert invoke(e) is True
    w.state.access = False
    with pytest.raises(PermissionError): invoke(e)


@pytest.mark.parametrize('which', ['original', 'normalized'])
@pytest.mark.parametrize('change', ['missing', 'expiry', 'owner', 'family', 'logical_id'])
def test_actual_retained_dependency_drift_refuses(peers, which, change):
    e = setup(peers); c, w, first, loaded, _ = e
    if which == 'normalized': ref = loaded['input_ref']['artifact_ref']['retention_ref']
    else:
        ref = w.table.rows[(c.owner['firm_id'], 'UPLOAD#' + first['upload_id'])]['artifact_ref']['retention_ref']
    key = (c.owner['firm_id'], 'RETENTION#' + ref['retention_id'])
    row = w.table.rows[key]
    if change == 'missing': del w.table.rows[key]
    elif change == 'expiry': w.state.now = row['expires_at']
    elif change == 'owner': row['owner']['principal_id'] = 'other@example.invalid'
    elif change == 'family': row['family'] = 'OTHER'
    else: row['logical_id'] = 'other-input'
    with pytest.raises((PermissionError, peers.retention.RetentionRefused, peers.repo.ReportDenied)): invoke(e)


@pytest.mark.parametrize('change', ['firm', 'email', 'advisor', 'role', 'origin'])
def test_owner_changes_during_actual_blob_read_refuse(peers, change):
    e = setup(peers); c = e[0]
    key, value = {'firm': ('x-firm-id','cottonwood'), 'email': ('x-user-email','other@example.invalid'),
        'advisor': ('x-advisor-id','other'), 'role': ('x-user-role','admin'), 'origin': ('x-origin-verify','')}[change]
    c.s3.on_get = lambda: c.headers.update({key: value})
    with pytest.raises(PermissionError): invoke(e)


@pytest.mark.parametrize('change', ['retention_removed', 'returned_owner', 'returned_ref', 'lane', 'upload_id'])
def test_post_reader_exact_binding_refuses(peers, change):
    e = setup(peers); c = e[0]; original = c.service.read_input
    def read(*args):
        result = original(*args)
        if change == 'retention_removed': c.service.artifacts.retention = None
        elif change == 'returned_owner': result['owner']['account_ids'] = ['not-a-grant']
        elif change == 'returned_ref': result['input_ref']['artifact_ref']['version_id'] = 'changed'
        elif change == 'lane': result['document']['source']['lane'] = 'CUSTODY'
        else: result['document']['source']['upload_id'] = 'UP-' + '0' * 64
        return result
    c.service.read_input = read
    with pytest.raises(MaintainedSourceRefused): invoke(e)


@pytest.mark.parametrize('change', ['upload_format', 'custody', 'extra_owner', 'numeric_digest', 'family', 'digest', 'extra_ref'])
def test_constructor_rejects_noncanonical_server_binding(peers, change):
    e = setup(peers); c, _, _, loaded, _ = e
    owner = copy.deepcopy(loaded['owner']); ref = copy.deepcopy(loaded['input_ref'])
    if change == 'upload_format': owner['prospect_input_id'] = 'UP-' + 'G' * 64
    elif change == 'custody': owner['account_ids'] = ['not-a-grant']
    elif change == 'extra_owner': owner['extra'] = True
    elif change == 'numeric_digest': ref['content_sha256'] = int('1' * 64)
    elif change == 'family': ref['artifact_ref']['family'] = 'ORIGINAL_CSV'
    elif change == 'digest': ref['artifact_ref']['sha256'] = '0' * 64
    else: ref['extra'] = True
    with pytest.raises(MaintainedSourceRefused):
        RetainedProspectInputAuthorizer(headers=c.headers, uploads=c.service,
            expected_owner=owner, expected_input_ref=ref)

```
