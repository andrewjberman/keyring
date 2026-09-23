# Opal / partner source review: dc51d8920d

Reviewer: `3.0.0_SA_CVO~M`. Authority: completion `CONTRACT.md`, CTO narrow reviewer resume `20260923T131715Z`, principal adjudication `20260923T132334Z`, and `LOCAL_LIVE_PARTNER_SCOPE_20260923.md` in `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/`. Exact COO P candidate handoff: `20260923T134227Z`.

## Verdict

**FAIL / M-OPAL-01 OPEN: request-local Opal eligibility is lost during actual holdings reauthorization.** The directory and selected-tenant controls tested below pass, but the accepted selection cannot continue through the actual downstream holdings Entry for non-admin Opal/Dev principals. This is a valid-flow failure; no unauthorized data disclosure was demonstrated.

Exact backend: `dc51d8920dd25d4c11bf48737cdca31ada3e8a63`, independently checked out in the clean private reviewer worktree. P's paired Portal pin and package handoff were pending at review start. CVO P owns schema/parser/browser work; this review does not duplicate it or supply a paired frontend verdict. Source review made no implementation edits, used no live API or cloud mutation, and resumed no unrelated held work.

## M-OPAL-01 reproduction and cause

1. Use the real directory Entry, real scope/guard/ID projection and real dependency loaders. Supply synthetic storage through `_loaders._get_json` only; the loader still reads its actual configured bucket map, directory pointer, ownership and content-derived entitlement revision. The principal qualifies either through verified `opal-capital` with role `user`, or a verified partner firm with `userType=Dev` and role `advisor`.
2. Create a real accepted selection for one account in the selected firm's directory but outside that principal's ordinary advisor ownership. This is allowed by the adjudicated Opal predicate and the candidate's actual request-local roster. The selection is saved under the selected registry tenant.
3. Send the same principal and retained reference through actual `holdings/entry.py::ENTRY.handle`, carrying the selected tenant in the query. The outer shared guard recognizes Opal eligibility, but the inner `_current_selection` reconstructs an Enforcer at line 48 with `ENTRY.opal_principal_ids`, the module's unchanged empty roster.
4. That inner resolver falls back to the ordinary advisor grant and refuses the selected member: public **OBJECT_NOT_COVERED**, no data, **zero snapshot reads**. Both eligible non-admin cases fail the required continuation assertion.

The paired positive controls use a partner advisor's owned member and an Opal admin's selected member. Both reach the exact snapshot loader with the selected tenant and exact single-account argument. The controlled snapshot loader deliberately raises SnapshotUnavailable, producing NOT_READY; this establishes authorization reachability only, not valid economic data or holdings acceptance. The admin path works because the lost internal designation still falls back to firm operations. The two non-admin cases expose the inconsistency without changing expected permissions.

Required repair: retain or re-derive the adjudicated request-local eligibility through each real downstream authorization check, including both pre-read and release-time checks. Do not mutate the module roster, remove reauthorization, or promote an advisor merely because a retained selection exists. Audit the selected downstream consumers for this same static-roster seam and identify their exact source/package dependencies. COO P is the temporary implementation owner.

## Checks and boundaries

| Independent run | Result |
|---|---|
| Supplied Opal context + previous bootstrap/browse/selection tests | 41 PASS in 0.98 seconds (13 new + 28 existing) |
| Unchanged M bootstrap suite from prior finding | 45 PASS in 1.36 seconds at the new exact pin |
| New independent directory / actual-loader controls | 66 PASS in initial run, 2.08 seconds |
| Final independent suite including seven actual holdings boundary cases | **71 PASS / 2 FAIL**, 2.89 seconds |

The final 73-case suite covers:

- Both exact internal predicate arms; explicit Global schema validation and per-firm opaque/registry identity; queries restricted to the configured tenant map and no union account grant.
- Partner admin, email-domain, tier and lowercase-Dev non-grants; missing subject/origin and renderer with/without delegate markers; foreign/Global refusals before storage.
- Same warm Entry and same subject switching from Opal to partner advisor/admin; no persistent roster mutation or Global inheritance. The actual directory Entry configures no shared payload cache (`shared_cache is None`), so claims concern fresh per-request processing, not a forced cache configuration absent from the candidate.
- Query/body/base64 selected-tenant carriers across all three firms; conflicting or opaque/unknown/null/empty intent; nested/encoded conflicting firm claims refused before reads.
- One/multiple missing, empty or wrong-firm directory outcomes retained visibly; PARTIAL/UNAVAILABLE not silently COMPLETE; removal from the configured tenant map prevents later querying of that tenant.
- Subject/tenant/query/limit/directory/ownership/internal-context cursor changes, complete bounded page walk, distinct principal-bound cursors, current advisor ownership rereads and partial/full revocation.
- Actual accepted selection under its own tenant, foreign/mixed/group/global negatives; actual holdings foreign-reference, stale-directory and revoked-account controls refuse before economic reads.

The final downstream cases create and consume the selection under the same principal. A preliminary downstream run used a shared eligible creator before varying the consuming principal and reproduced the same two failures; the final fixture removes that incidental variation without changing the failure assertion. Initial and final receipts are retained separately. The final complete driver below is the immutable repair-retest basis.

P attributes five existing shared-auth suite failures to baseline `69d50fbd64` (two legacy positive fixtures and three route-count assertions) in its candidate contract. This reviewer did not rerun that broad suite and does not independently certify that attribution; the explicit counts above are the tests run here. Prior evidence was rerun where cited, never inherited as current PASS.

## Evidence identity and execution

Driver: `.runtime/codex-seats/3.0.0_SA_CVO~M/test_opal_dc51_review.py`, SHA-256 `c782cfd9c4ddabb1fba407c400ce9166a7f7ba6568f44ad4be66dec83040d642`.
Final JUnit: sibling `opal_dc51_review_final.xml`, SHA-256 `b331662cf948716f21f042f7b246b68a68968e4c68766957a3763ddc1f4e3b1b`.
Metadata receipt: sibling `opal_dc51_metadata.json`. Network connections are explicitly forbidden by the independent fixture.

Git-byte source SHA-256 values:

| Source | SHA-256 |
|---|---|
| `_authz/served.py` | `75083247a6a06252780abb6ecca821532a08492c506406140f99f2c47db71987` |
| `directory/entry.py` | `82ada70c34d5351462241dcb1124d1c3442a06c5360246c6e7fe16c29f912781` |
| `holdings/entry.py` | `098e41bacc40f86f53f1b9e5cffb7f707c3fea4ca5cd5b47aeee73a81172c6d4` |
| `_authz/loaders.py` | `b84bb2918fc13be31358e81221e951ed4f4aa70da9dea2b7a8dbce93b1853da2` |
| `DirectoryContext.schema.json` | `8c76a0f0e028f1b1baf7224f633904e2c1b9aa2450b409c679be1bef4bea2404` |

Run from `C:/Users/AndrewBerman/Desktop/ajb_irpt_cvo_m_review` at the exact pin, with `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1` and `AWS_EC2_METADATA_DISABLED=true`:

```powershell
python -m pytest -q -p no:cacheprovider C:/Users/AndrewBerman/Desktop/ajb_workspace/.runtime/codex-seats/3.0.0_SA_CVO~M/test_opal_dc51_review.py --tb=short
```

Compiler routing was used before source inspection. `comp-read` identified the new request-local roster and Global callback; the narrow holdings name search found the actual Entry and its existing tests in a 17-file scope. Reading that actual downstream reauthorization exposed the incomplete propagation despite the passing directory battery. This finding was reproduced through the executable real Entry, not inferred from an outline.

## Remaining scope

The candidate trusts identity headers overwritten by the verified edge. These source tests inject synthetic verified-header shapes; they do not establish live JWT verification or the deployed edge version. Identity freshness remains the admitted token lifetime, with no new roster TTL or immediate mid-token revocation claim.

The retained reference is content-bound and non-bearer. Another principal with current authority may use it; lack of creator ownership is not the finding. What fails is an already eligible current principal losing that eligibility within the actual request.

Global browser presentation, strict consumer parser, signed-in request serialization and confirmation are CVO P's separate evidence. Flat package composition, runtime plans/apply, current live data and localhost-to-CloudFront smoke remain NOT_EVALUATED by this source review. No production promotion or cloud action is authorized or performed.

## Immutable independent assertions

```python
"""CVO M independent candidate controls: real Entry/loaders, synthetic storage only."""
import base64
import copy
import json
import importlib.util
from pathlib import Path
import socket
import sys

import pytest

ROOT = Path('C:/Users/AndrewBerman/Desktop/ajb_irpt_cvo_m_review')
PKG = ROOT / 'infra/aws/lambda/investor-reporting'
sys.path.insert(0, str(PKG / 'directory/tests'))
from test_bootstrap_browse import setup, validator
from test_selection_entry import entry

TENANTS = ['49financial', 'cottonwood', 'inflection']
RESOLVE = 'POST /api/scoped/investor-reporting/directory/resolve'
BROWSE = 'GET /api/scoped/investor-reporting/directory/browse'
SELECT = 'POST /api/scoped/investor-reporting/selections'


@pytest.fixture
def world(monkeypatch):
    template, _, _, _, _ = setup(monkeypatch)
    documents, ownership, accounts, records, calls = {}, {}, {}, {}, []
    bucket_map = {t: 'synthetic-' + t for t in TENANTS}
    for tenant in TENANTS:
        accounts[tenant] = [entry._ids.opaque_account(tenant, str(1000000000 + i)) for i in range(3)]
        doc = copy.deepcopy(template)
        doc['firm_id_opaque'] = entry._ids.opaque_firm(tenant)
        doc['entries'] = []
        for i, account in enumerate(accounts[tenant]):
            row = copy.deepcopy(template['entries'][0])
            row['display_name'] = 'Same name'
            row['masked_discriminator'] = '****' + str(i)
            row['ids'] = {'firm_id': doc['firm_id_opaque'], 'client_id': 'client-' + str(i),
                          'account_ids': [account]}
            row['permitted_scope'] = {'scope_kind': 'ACCOUNT', 'scope_ids': [account]}
            doc['entries'].append(row)
        documents[tenant] = doc
        ownership[tenant] = {'schema_version': 1, 'advisors': {
            'alice': {'accounts': accounts[tenant][:2], 'relationships': []},
            'bob': {'accounts': accounts[tenant][:2], 'relationships': []}}}

    def get_json(bucket, key, s3=None):
        tenant = next(t for t, b in bucket_map.items() if b == bucket)
        calls.append((tenant, key))
        if key.endswith('/latest.json'): return {'key': 'synthetic-directory.json'}
        if key == 'synthetic-directory.json': return copy.deepcopy(documents[tenant])
        if key == f'platinum/{tenant}/ownership_map.json': return copy.deepcopy(ownership[tenant])
        raise AssertionError('unexpected storage read')

    class Store:
        def save(self, firm, reference, record):
            records[(firm, reference)] = copy.deepcopy(record)
        def load(self, firm, reference):
            return copy.deepcopy(records.get((firm, reference)))

    def deny(*args, **kwargs): raise AssertionError('network forbidden')
    monkeypatch.setattr(socket.socket, 'connect', deny)
    monkeypatch.setattr(socket, 'create_connection', deny)
    monkeypatch.setenv('IRPT_DIRECTORY_BUCKET_MAP', json.dumps(bucket_map))
    monkeypatch.setattr(entry._loaders, '_get_json', get_json)
    monkeypatch.setattr(entry.ENTRY, 'deps', entry._loaders.deps)
    monkeypatch.setattr(entry.ENTRY, 'opaque_firm_for', entry._loaders.opaque_firm_for)
    monkeypatch.setattr(entry._selection_store, 'configured_store', Store)
    assert entry.ENTRY.shared_cache is None
    assert entry.ENTRY.opal_principal_ids == frozenset()
    return dict(docs=documents, owners=ownership, accounts=accounts, records=records,
                calls=calls, buckets=bucket_map)


def event(target='global', *, home='opal-capital', role='user', user_type=None,
          subject='same@example.invalid', route=RESOLVE):
    headers = {'x-contract-version': 'v1', 'x-origin-verify': 'cloudfront',
               'x-firm-id': home, 'x-user-role': role, 'x-user-email': subject,
               'x-advisor-id': 'alice'}
    if user_type is not None: headers['x-user-type'] = user_type
    answer = {'version': '2.0', 'routeKey': route, 'headers': headers}
    if route == RESOLVE: answer['body'] = json.dumps({'selected_tenant': target, 'account_ids': []})
    elif route == BROWSE: answer['queryStringParameters'] = {'selected_tenant': target, 'q': '', 'limit': '1'}
    return answer


def refuse(answer):
    assert answer.get('ok') is False and 'data' not in answer, answer


@pytest.mark.parametrize('home,user_type', [('opal-capital', None), ('49financial', 'Dev')])
def test_global_real_loader_scope_and_queries(world, home, user_type):
    response = entry.ENTRY.handle(event(home=home, user_type=user_type))
    validator('responses/resolve-scope.response.schema.json').validate(response)
    data = response['data']
    assert data['context_kind'] == 'GLOBAL' and data['completeness'] == 'COMPLETE'
    assert response['firm_id'] == 'global'
    assert set(t for t, _ in world['calls']) == set(TENANTS)
    assert 'permitted_account_set' not in data
    for outcome in data['firms']:
        tenant, scope = outcome['tenant'], outcome['scope']
        assert scope['registry_tenant'] == tenant
        assert scope['verified_request_firm_id'] == entry._ids.opaque_firm(tenant)
        assert scope['principal_class'] == 'OPAL_GLOBAL'
        assert scope['permitted_account_set'] == sorted(world['accounts'][tenant])
        assert not {'vendor_ids', '_census'} & scope.keys()
    assert entry.ENTRY.opal_principal_ids == frozenset()


@pytest.mark.parametrize('target', ['global', 'inflection'])
@pytest.mark.parametrize('identity', ['partner-admin', 'email-domain', 'internal-tier', 'lower-dev', 'missing-origin', 'missing-subject', 'renderer', 'renderer-marked'])
def test_nonqualifying_identity_cannot_cross_tenant(world, identity, target):
    ev = event(target, home='49financial', role='admin')
    if identity == 'email-domain': ev['headers']['x-user-email'] = 'someone@opalinvest.com'
    if identity == 'internal-tier': ev['headers']['x-user-tier'] = 'internal'
    if identity == 'lower-dev': ev['headers']['x-user-type'] = 'dev'
    if identity == 'missing-origin':
        ev['headers'].update({'x-firm-id': 'opal-capital', 'x-origin-verify': ''})
    if identity == 'missing-subject':
        ev['headers'].update({'x-firm-id': 'opal-capital', 'x-user-email': ''})
    if identity.startswith('renderer'):
        ev['headers'].update({'x-firm-id': 'opal-capital', 'x-user-role': 'renderer', 'x-user-type': 'Dev'})
        if identity == 'renderer-marked':
            ev['headers'].update({'x-render-delegator': 'someone', 'x-render-bundle': 'bundle', 'x-render-revision': 'r1'})
    refuse(entry.ENTRY.handle(ev))
    assert world['calls'] == []


@pytest.mark.parametrize('role', ['advisor', 'admin'])
def test_warm_opal_then_same_subject_partner_is_not_elevated(world, role):
    before = entry.ENTRY.opal_principal_ids
    assert entry.ENTRY.handle(event())['data']['completeness'] == 'COMPLETE'
    world['calls'].clear()
    refuse(entry.ENTRY.handle(event('inflection', home='49financial', role=role)))
    assert world['calls'] == []
    answer = entry.ENTRY.handle(event('49financial', home='49financial', role=role))['data']
    assert answer['principal_class'] == ('FIRM_ADVISOR' if role == 'advisor' else 'FIRM_OPERATIONS')
    expected = world['accounts']['49financial'][:2] if role == 'advisor' else world['accounts']['49financial']
    assert answer['permitted_account_set'] == sorted(expected)
    assert entry.ENTRY.opal_principal_ids is before
    assert entry.ENTRY.shared_cache is None


@pytest.mark.parametrize('carrier', ['query', 'body', 'encoded-body'])
@pytest.mark.parametrize('target', TENANTS)
def test_selected_registry_tenant_real_guard(world, carrier, target):
    ev = event(target)
    if carrier == 'query':
        ev['queryStringParameters'] = {'selected_tenant': target}
        ev['body'] = json.dumps({'account_ids': []})
    elif carrier == 'encoded-body':
        ev['body'] = base64.b64encode(ev['body'].encode()).decode()
        ev['isBase64Encoded'] = True
    result = entry.ENTRY.handle(ev)
    validator('responses/resolve-scope.response.schema.json').validate(result)
    assert result['data']['registry_tenant'] == target
    assert set(t for t, _ in world['calls']) == {target}


@pytest.mark.parametrize('change', ['query-vs-body', 'nested', 'claimed-body', 'claimed-query', 'encoded-claim', 'opaque', 'unknown', 'null', 'empty'])
def test_ambiguous_or_invalid_tenant_refused_before_reads(world, change):
    ev = event('inflection')
    body = json.loads(ev['body'])
    if change == 'query-vs-body': ev['queryStringParameters'] = {'selected_tenant': '49financial'}
    if change == 'nested': body['selection'] = {'selected_tenant': '49financial'}
    if change == 'claimed-body': body['firm_id'] = '49financial'
    if change == 'claimed-query': ev['queryStringParameters'] = {'firm_id': '49financial'}
    if change == 'encoded-claim': body['selection'] = {'firm_id': '49financial'}
    if change == 'opaque': body['selected_tenant'] = entry._ids.opaque_firm('inflection')
    if change == 'unknown': body['selected_tenant'] = 'not-registered'
    if change == 'null': body['selected_tenant'] = None
    if change == 'empty': body['selected_tenant'] = ''
    ev['body'] = json.dumps(body)
    if change == 'encoded-claim':
        ev['body'] = base64.b64encode(ev['body'].encode()).decode()
        ev['isBase64Encoded'] = True
    refuse(entry.ENTRY.handle(ev))
    assert world['calls'] == []


@pytest.mark.parametrize('failure', ['one-missing', 'all-missing', 'one-empty', 'foreign-artifact'])
def test_global_failed_firm_never_disappears(world, failure):
    if failure == 'one-missing': del world['docs']['inflection']
    if failure == 'all-missing': world['docs'].clear()
    if failure == 'one-empty': world['docs']['inflection']['entries'] = []
    if failure == 'foreign-artifact': world['docs']['inflection']['firm_id_opaque'] = entry._ids.opaque_firm('49financial')
    result = entry.ENTRY.handle(event())
    validator('responses/resolve-scope.response.schema.json').validate(result)
    data = result['data']
    assert set(x['tenant'] for x in data['firms']) == set(TENANTS)
    assert data['completeness'] == ('UNAVAILABLE' if failure == 'all-missing' else 'PARTIAL')
    failed = next(x for x in data['firms'] if x['tenant'] == 'inflection')
    assert failed['state'] == 'UNAVAILABLE' and failed['scope'] is None and failed['reason']


def test_registry_removal_prevents_subsequent_foreign_queries(world, monkeypatch):
    assert entry.ENTRY.handle(event())['data']['completeness'] == 'COMPLETE'
    reduced = {t: b for t, b in world['buckets'].items() if t != 'inflection'}
    monkeypatch.setenv('IRPT_DIRECTORY_BUCKET_MAP', json.dumps(reduced))
    world['calls'].clear()
    refuse(entry.ENTRY.handle(event('inflection')))
    assert world['calls'] == []
    answer = entry.ENTRY.handle(event())['data']
    assert set(x['tenant'] for x in answer['firms']) == set(reduced)
    assert set(t for t, _ in world['calls']) == set(reduced)


@pytest.mark.parametrize('change', ['subject', 'tenant', 'query', 'limit', 'directory', 'ownership', 'lost-internal'])
def test_cursor_context_change_refuses(world, change):
    ev = event('49financial', route=BROWSE)
    original = entry.ENTRY.handle(ev)['data']
    ev['queryStringParameters']['cursor'] = original['next_cursor']
    if change == 'subject': ev['headers']['x-user-email'] = 'new@example.invalid'
    if change == 'tenant': ev['queryStringParameters']['selected_tenant'] = 'inflection'
    if change == 'query': ev['queryStringParameters']['q'] = 'Same'
    if change == 'limit': ev['queryStringParameters']['limit'] = '2'
    if change == 'directory': world['docs']['49financial']['entries'][0]['display_name'] = 'Changed'
    if change == 'ownership': world['owners']['49financial']['advisors']['alice']['accounts'] = []
    if change == 'lost-internal': ev['headers'].update({'x-firm-id': '49financial', 'x-user-role': 'admin'})
    refuse(entry.ENTRY.handle(ev))


def test_same_warm_entry_pages_and_new_principal_have_fresh_bound_cursors(world):
    first = event('49financial', route=BROWSE)
    one = entry.ENTRY.handle(first)['data']
    cursor_one = one['next_cursor']
    second = copy.deepcopy(first)
    second['headers']['x-user-email'] = 'second@example.invalid'
    two = entry.ENTRY.handle(second)['data']
    assert two['entries'] == one['entries']
    assert two['next_cursor'] != cursor_one
    ids = one['entries'][0]['ids']['account_ids'][:]
    cursor = cursor_one
    while cursor is not None:
        first['queryStringParameters']['cursor'] = cursor
        data = entry.ENTRY.handle(first)['data']
        ids += data['entries'][0]['ids']['account_ids']
        cursor = data['next_cursor']
    assert len(ids) == len(set(ids)) == 3
    assert set(ids) == set(world['accounts']['49financial'])


@pytest.mark.parametrize('change', ['revoke-one', 'revoke-all', 'identity-change'])
def test_partner_requests_reread_current_authority(world, change):
    ev = event('49financial', home='49financial', role='advisor', route=BROWSE)
    ev['queryStringParameters']['limit'] = '100'
    assert len(entry.ENTRY.handle(ev)['data']['entries']) == 2
    if change == 'revoke-one': world['owners']['49financial']['advisors']['alice']['accounts'] = world['accounts']['49financial'][:1]
    elif change == 'revoke-all': world['owners']['49financial']['advisors']['alice']['accounts'] = []
    else: ev['headers']['x-advisor-id'] = 'unknown'
    answer = entry.ENTRY.handle(ev)
    if change == 'revoke-one':
        assert [r['ids']['account_ids'] for r in answer['data']['entries']] == [world['accounts']['49financial'][:1]]
    else: refuse(answer)


@pytest.mark.parametrize('kind', ['same', 'foreign-members', 'mixed-members', 'foreign-client', 'global'])
def test_accepted_selection_exact_tenant(world, kind):
    ev = event('inflection', route=SELECT)
    ev['queryStringParameters'] = {'selected_tenant': 'inflection'}
    members = world['accounts']['inflection'][:1]
    scope_kind = 'ACCOUNT'
    if kind == 'foreign-members': members = world['accounts']['49financial'][:1]
    if kind == 'mixed-members': members += world['accounts']['49financial'][:1]
    if kind == 'foreign-client': scope_kind, members = 'CLIENT', ['absent']
    if kind == 'global': ev['queryStringParameters']['selected_tenant'] = 'global'
    ev['body'] = json.dumps({'scope_kind': scope_kind, 'scope_ids': members})
    answer = entry.ENTRY.handle(ev)
    if kind == 'same':
        selected = answer['data']
        assert selected['firm_id'] == 'inflection'
        assert selected['selected_account_ids'] == members
        assert world['records'][('inflection', selected['account_set_id'])]['account_ids'] == members
    else:
        refuse(answer)
        assert world['records'] == {}


@pytest.mark.parametrize('carrier', ['query', 'body', 'encoded-body'])
def test_global_selector_supported_carriers(world, carrier):
    ev = event()
    if carrier == 'query':
        ev['queryStringParameters'] = {'selected_tenant': 'global'}
        ev['body'] = json.dumps({'account_ids': []})
    elif carrier == 'encoded-body':
        ev['body'] = base64.b64encode(ev['body'].encode()).decode()
        ev['isBase64Encoded'] = True
    assert entry.ENTRY.handle(ev)['data']['completeness'] == 'COMPLETE'


@pytest.mark.parametrize('field,value', [('account_ids',['foreign']), ('client_id','client-0'), ('relationship_id','relationship'), ('entitlement_revision','stale')])
def test_global_does_not_accept_single_firm_selection(world, field, value):
    ev = event()
    body = json.loads(ev['body'])
    body[field] = value
    ev['body'] = json.dumps(body)
    refuse(entry.ENTRY.handle(ev))
    assert world['calls'] == []


def holdings_module():
    sys.path.insert(0, str(PKG / 'holdings'))
    spec = importlib.util.spec_from_file_location('cvo_m_opal_holdings_entry', PKG / 'holdings/entry.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.mark.parametrize('principal', ['partner-advisor', 'opal-user', 'partner-dev', 'opal-admin'])
def test_accepted_selection_reaches_real_holdings_authorization(world, monkeypatch, principal):
    target = '49financial'
    member = world['accounts'][target][0 if principal == 'partner-advisor' else 2]
    create = event(target, route=SELECT)
    if principal == 'partner-advisor': create['headers'].update({'x-firm-id': target, 'x-user-role': 'advisor'})
    if principal == 'partner-dev': create['headers'].update({'x-firm-id': target, 'x-user-role': 'advisor', 'x-user-type': 'Dev'})
    if principal == 'opal-admin': create['headers']['x-user-role'] = 'admin'
    create['queryStringParameters'] = {'selected_tenant': target}
    create['body'] = json.dumps({'scope_kind': 'ACCOUNT', 'scope_ids': [member]})
    selected = entry.ENTRY.handle(create)['data']
    holdings = holdings_module()
    reads = []
    def unavailable_source(*args, **kwargs):
        reads.append((args, kwargs))
        raise holdings._snapshot.SnapshotUnavailable('synthetic economic source unavailable after authorization')
    monkeypatch.setattr(holdings._snapshot, 'load_snapshot', unavailable_source)
    ev = event(target)
    ev.pop('body')
    ev['routeKey'] = holdings.ROUTE_KEY
    ev['pathParameters'] = {'accountSetId': selected['account_set_id']}
    ev['queryStringParameters'] = {'selected_tenant': target}
    ev['headers'] = copy.deepcopy(create['headers'])
    answer = holdings.ENTRY.handle(ev)
    # Proves only the actual downstream authorization accepts the selection.
    # Economic bytes are deliberately unavailable, so this is not a holdings PASS.
    assert len(reads) == 1, answer.get('status', answer)
    assert reads[0][0][0] == target
    assert reads[0][1]['account_ids'] == [member]
    assert answer['status']['public_reason_code'] == 'NOT_READY'


@pytest.mark.parametrize('change', ['foreign-reference', 'directory-revision', 'revoked-account'])
def test_real_holdings_rejects_foreign_stale_or_revoked_reference(world, monkeypatch, change):
    target = '49financial'
    member = world['accounts'][target][0]
    create = event(target, route=SELECT)
    create['queryStringParameters'] = {'selected_tenant': target}
    create['body'] = json.dumps({'scope_kind': 'ACCOUNT', 'scope_ids': [member]})
    reference = entry.ENTRY.handle(create)['data']['account_set_id']
    holdings = holdings_module()
    reads = []
    def forbidden(*args, **kwargs):
        reads.append(True)
        raise AssertionError('unauthorized holdings read')
    monkeypatch.setattr(holdings._snapshot, 'load_snapshot', forbidden)
    ev = event(target, home=target, role='advisor')
    ev.pop('body')
    ev['routeKey'] = holdings.ROUTE_KEY
    ev['pathParameters'] = {'accountSetId': reference}
    ev['queryStringParameters'] = {'selected_tenant': target}
    if change == 'foreign-reference':
        ev['headers'].update({'x-firm-id': 'opal-capital', 'x-user-role': 'admin'})
        ev['queryStringParameters']['selected_tenant'] = 'inflection'
    if change == 'directory-revision': world['docs'][target]['entries'][0]['display_name'] = 'Changed'
    if change == 'revoked-account': world['owners'][target]['advisors']['alice']['accounts'] = world['accounts'][target][1:2]
    refuse(holdings.ENTRY.handle(ev))
    assert reads == []

```
