# Bootstrap scope and browse review: 69144433df

Reviewer: `3.0.0_SA_CVO~M`. Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`, live directive `90eac8c562`, temporary P implementer transfer `09b9573688` / `6551b8be25`, and CTO exact source handoff `20260923T060637Z`.

## Verdict

**FAIL: M-BOOT-01 remains open.** Malformed selector values and non-object JSON bodies are silently interpreted as valid full-permitted-scope bootstrap requests. This is a request validation / exact scope intent defect; the reproduction does not show access outside the verified principal's permission set.

Backend independently checked out at `69144433df8c4938cf95cb81e46ac04ae72cc61e`, clean before and after review. Committed `directory/entry.py` SHA-256 `41256ae9edb0ca362151fb5ce5113f05b570bc270bd9ee52e43c11faf1591539`, matching the handoff. The candidate changes only that entry and `directory/tests/test_bootstrap_browse.py` relative to its parent. Review made no producer changes.

The paired Portal pin is `cdc60da247597940b278dd43779b3953565093b7`. Per CTO allocation, CVO P owns the unchanged R-P12 client/Entry/parser replay; this reviewer did not duplicate it. CVO P's exact `061016Z` notice reports independent closure at `71e114f69a`, `IRPT_MVP_P/BOOTSTRAP_RETEST_6914.md`: 11 backend PASS, 10 frontend PASS / 20 assertions, all five original authorization-negative families preserved, original assertion bytes unchanged. That attributed closure is limited to the original offline contract mismatch and does not close M-BOOT-01.

## M-BOOT-01: malformed input becomes full scope

At candidate `directory/entry.py:195`, `accounts = selection.get("account_ids") or []` runs before type validation. Each of these bodies produces a served ResolvedScope with the fixture's two permitted accounts and requested/resolved FIRM scope:

```json
{"account_ids": false}
{"account_ids": 0}
{"account_ids": ""}
{"account_ids": {}}
```

At `_event_params` lines 132-135, a successfully parsed JSON body is merged only if it is a dictionary; any other JSON type is ignored. Bodies `[]`, `false`, `"not-an-object"`, and `5` therefore also reach the default full-scope bootstrap. In contrast, a nonempty account string or `[null]` is refused. This truthiness-dependent validation is inconsistent with the explicit string-array check and cannot distinguish a legitimate empty selection from a malformed request.

Required repair: validate present selector types before defaulting; reject a supplied non-object JSON request with public INVALID_INPUT and no data. Preserve the agreed empty-array bootstrap and optional selector semantics, strict partial selection, existing authorization controls, and the original R-P12 assertion bytes. COO P is the temporary sole implementer. Retest the eight failing cases unchanged at the new exact pin; do not reinterpret them as valid FIRM requests.

## Independent evidence

Actual `ENTRY.handle` executes the candidate's guard, scope resolver, ID projection, pure projection, browse/resolve operation and response envelope. Existing test setup provides controlled directory/ownership/policy dependencies; independent tests add synthetic contexts and adversarial requests. Network connects are forbidden by the reviewer fixture. No credentials or client records are used.

| Check | Result |
|---|---|
| Candidate supplied `test_bootstrap_browse.py` plus existing `test_selection_entry.py` | 19 PASS, 0.79 seconds |
| Independent suite, final run | 37 PASS / 8 FAIL, 1.21 seconds |
| Advisor and operations bootstrap plus browse for each of 49financial, cottonwood and inflection | 6 PASS; actual resolver and published response schema |
| Exact account/client/relationship requests, duplicate account canonicalization, strict mixed/foreign refusal, ambiguous selector and stale entitlement refusal | 7 PASS |
| Malformed selector types and non-object bodies | 8 FAIL above; nonempty-string / null-member array negative controls PASS |
| Cursor role, advisor, verified/claimed firm, policy, directory date and full revocation changes; untrusted header cannot alter authorization | 8 PASS |
| Cursor binding, zero/negative/bool/fraction/outside offset, extra member and non-object cursor | 8 PASS |
| Complete page walk | 237 unique synthetic entries in 10 bounded pages; no omission/duplicate, deterministic name/discriminator ordering, final null cursor |
| Unknown advisor, missing verified origin, forged client scope, foreign row and partial group | 5 PASS; no permission expansion or partial-document leakage |

The three-firm fixture deliberately supplies already-issued account IDs, keeping this scope review separate from the existing 49F custody crosswalk. Initial development run was 36 PASS / 9 FAIL: one additional failure was a reviewer fixture using unjoined raw 49F custody IDs. The real guard correctly refused that fixture. Correcting only the synthetic ownership fixture to already-issued IDs produced the final 37 PASS / 8 FAIL; candidate source and the eight failing assertions were unchanged. This is not new custody crosswalk evidence.

The selected supplied files collect 19 tests; P's message claimed an additional 21-test suite. This report cites only the 19 independently run here, without claiming those commands reproduce P's unspecified additional count.

Driver: `.runtime/codex-seats/3.0.0_SA_CVO~M/test_bootstrap_691_review.py`, SHA-256 `945787544ffad0e88ad72b6c7d38cc80d77445e569c36d3631888dba7cc17adb`. JUnit receipt: sibling `bootstrap_691_review.xml`, SHA-256 `4485ede665a0d7e8d956a9b629b4694b842b998cf694fbe804ea919ec5d1bcef`. Complete driver is preserved below for unchanged repair retest.

Run from reviewer checkout at the exact pin with `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1` and `AWS_EC2_METADATA_DISABLED=true`:

```powershell
python -m pytest -q -p no:cacheprovider C:/Users/AndrewBerman/Desktop/ajb_workspace/.runtime/codex-seats/3.0.0_SA_CVO~M/test_bootstrap_691_review.py --tb=no
```

## Scope and remaining acceptance

The cursor is a context-bound continuation marker, not a signed credential: every request is guarded and pages are built only from whole permitted documents. Arbitrary offset changes within the same authorized projection are not evidence of an access bypass. The tests cover context changes between requests, not atomic revocation at every instruction during a request.

Header/UI visibility, multiple-firm catalogue, asynchronous stale-response reset, real HTTP, deployed package/configuration, CloudFront-served DEV and Andrew visual smoke remain **NOT_EVALUATED / open**. No runtime apply, deployment, provider call or localhost UI bypass was performed. Runtime `30069a5254` package and fresh exact-artifact plan gates remain unchanged. Source tests cannot close the live incident.

Compiler observations: `comp-read` routed and outlined the actual entry, scope, guard, ID and projection modules. `comp-find --name` in the 42-file contract scope found only response/schema files for scope/browse, not the initially guessed request-schema paths. A broad `comp-which` fallback for a mixed search question timed out at 90 seconds; it supplied no absence evidence. The handler outline's reported signature contradictions concerned docstring shorthand, not a demonstrated runtime defect.

## Immutable independent assertions

```python
"""Independent CVO M actual Entry scope and continuation controls; offline."""
import base64
import copy
import json
import os
from pathlib import Path
import socket
import sys

import pytest

ROOT = Path('C:/Users/AndrewBerman/Desktop/ajb_irpt_cvo_m_review')
PKG = ROOT / 'infra/aws/lambda/investor-reporting'
sys.path.insert(0, str(PKG / 'directory/tests'))
from test_bootstrap_browse import setup, browse, entry, request, validator


@pytest.fixture(autouse=True)
def offline(monkeypatch):
    def deny(*args, **kwargs):
        raise AssertionError('network forbidden in independent source review')
    monkeypatch.setattr(socket, 'create_connection', deny)
    monkeypatch.setattr(socket.socket, 'connect', deny)


def resolve_event(body):
    event = request('ACCOUNT', [])
    event['routeKey'] = 'POST /api/scoped/investor-reporting/directory/resolve'
    event['body'] = json.dumps(body)
    return event


def refused(answer):
    assert answer.get('ok') is False and 'data' not in answer, answer


@pytest.mark.parametrize('firm', ['49financial', 'cottonwood', 'inflection'])
@pytest.mark.parametrize('role', ['advisor', 'admin'])
def test_real_scope_three_firms_and_lanes(monkeypatch, firm, role):
    directory, owner, revision, _, _ = setup(monkeypatch)
    opaque = entry._ids.opaque_firm(firm)
    raw_accounts = ['1000000001', '1000000002']
    accounts = [entry._ids.opaque_account(firm, a) for a in raw_accounts]
    directory['firm_id_opaque'] = opaque
    for row, account in zip(directory['entries'], accounts):
        row['ids']['firm_id'] = opaque
        row['ids']['account_ids'] = [account]
        row['permitted_scope'] = {'scope_kind': 'ACCOUNT', 'scope_ids': [account]}
    # Already-issued IDs isolate scope semantics from the existing 49F custody seam.
    owner['advisors']['advisor']['accounts'] = accounts
    monkeypatch.setattr(entry.ENTRY, 'opaque_firm_for', entry._ids.opaque_firm)
    for operation in ['resolve', 'browse']:
        event = resolve_event({'account_ids': []}) if operation == 'resolve' else browse(limit='100')
        event['headers']['x-firm-id'] = firm
        event['headers']['x-user-role'] = role
        answer = entry.ENTRY.handle(event)
        assert 'data' in answer, answer
        if operation == 'resolve':
            data = answer['data']
            assert data['verified_request_firm_id'] == opaque
            assert data['permitted_account_set'] == sorted(accounts)
            assert data['principal_class'] == ('FIRM_OPERATIONS' if role == 'admin' else 'FIRM_ADVISOR')
            assert data['requested_scope'] == {'scope_kind': 'FIRM', 'scope_ids': [opaque]}
            assert not {'vendor_ids', '_census', 'permitted_firm_catalogue'} & data.keys()
            validator('responses/resolve-scope.response.schema.json').validate(answer)
        else:
            assert sorted(a for row in answer['data']['entries'] for a in row['ids']['account_ids']) == sorted(accounts)


@pytest.mark.parametrize('selector', ['client', 'relationship', 'account', 'foreign-account', 'mixed-account', 'ambiguous', 'stale-entitlement'])
def test_exact_selector_semantics(monkeypatch, selector):
    directory, owner, revision, a, b = setup(monkeypatch)
    relation = entry._ids.opaque_relationship('49financial', 'shared')
    for row in directory['entries']:
        row['ids']['relationship_id'] = relation
    body = {'client_id': 'client-0'}
    expected = [a]
    if selector == 'relationship':
        body, expected = {'relationship_id': relation}, sorted([a, b])
    elif selector == 'account':
        body = {'account_ids': [a, a]}
    elif selector == 'foreign-account':
        body, expected = {'account_ids': ['foreign']}, []
    elif selector == 'mixed-account':
        body, expected = {'account_ids': [a, 'foreign']}, []
    elif selector == 'ambiguous':
        body = {'client_id': 'client-0', 'account_ids': [a]}
    elif selector == 'stale-entitlement':
        body = {'account_ids': [a], 'entitlement_revision': 'stale'}
    answer = entry.ENTRY.handle(resolve_event(body))
    if selector in ['ambiguous', 'stale-entitlement']:
        refused(answer)
    else:
        assert answer['data']['permitted_account_set'] == expected
        if not expected:
            assert answer['data']['resolved_scope']['scope_kind'] == 'UNSUPPORTED'


@pytest.mark.parametrize('value', [False, 0, '', {}, 'account-not-array', [None]])
def test_malformed_account_selector_never_becomes_full_scope(monkeypatch, value):
    setup(monkeypatch)
    refused(entry.ENTRY.handle(resolve_event({'account_ids': value})))


@pytest.mark.parametrize('body', [[], False, 'not-an-object', 5])
def test_nonobject_request_never_becomes_bootstrap(monkeypatch, body):
    setup(monkeypatch)
    refused(entry.ENTRY.handle(resolve_event(body)))


@pytest.mark.parametrize('change', ['role', 'advisor', 'firm-header', 'firm-query', 'policy', 'directory-date', 'revoke-all', 'untrusted-header'])
def test_cursor_context_independently(monkeypatch, change):
    directory, owner, revision, a, b = setup(monkeypatch)
    cursor = entry.ENTRY.handle(browse())['data']['next_cursor']
    event = browse(cursor)
    if change == 'role': event['headers']['x-user-role'] = 'admin'
    if change == 'advisor':
        owner['advisors']['other'] = copy.deepcopy(owner['advisors']['advisor'])
        event['headers']['x-advisor-id'] = 'other'
    if change == 'firm-header': event['headers']['x-firm-id'] = 'cottonwood'
    if change == 'firm-query': event['queryStringParameters']['firm_id'] = 'cottonwood'
    if change == 'directory-date': directory['as_of_business_date'] = '2026-09-21'
    if change == 'revoke-all': owner['advisors']['advisor']['accounts'] = []
    if change == 'untrusted-header': event['headers']['x-browser-admin'] = 'true'
    if change == 'policy':
        load, owned, policy = entry.ENTRY.deps('49financial')
        old, ent = policy('49financial')
        updated = {**old, 'policy_revision': 'changed'}
        monkeypatch.setattr(entry.ENTRY, 'deps', lambda tenant: (load, owned, lambda _: (updated, ent)))
    answer = entry.ENTRY.handle(event)
    if change == 'untrusted-header':
        assert answer['data']['entries'][0]['ids']['account_ids'] == [b]
    else:
        refused(answer)


@pytest.mark.parametrize('mutation', ['binding', 'zero', 'negative', 'bool', 'fraction', 'outside', 'extra', 'not-object'])
def test_cursor_validation(monkeypatch, mutation):
    setup(monkeypatch)
    cursor = entry.ENTRY.handle(browse())['data']['next_cursor']
    decoded = json.loads(base64.urlsafe_b64decode(cursor))
    if mutation == 'binding': decoded['binding'] = '0' * 64
    if mutation == 'zero': decoded['offset'] = 0
    if mutation == 'negative': decoded['offset'] = -1
    if mutation == 'bool': decoded['offset'] = True
    if mutation == 'fraction': decoded['offset'] = 1.5
    if mutation == 'outside': decoded['offset'] = 10000
    if mutation == 'extra': decoded['principal'] = 'other'
    if mutation == 'not-object': decoded = []
    forged = base64.urlsafe_b64encode(json.dumps(decoded).encode()).decode()
    refused(entry.ENTRY.handle(browse(forged)))


def test_full_page_walk_no_omissions_or_duplicates(monkeypatch):
    directory, owner, revision, a, b = setup(monkeypatch)
    template = directory['entries'][0]
    rows = []
    accounts = []
    for i in range(237):
        row = copy.deepcopy(template)
        account = entry._ids.opaque_account('49financial', str(1000000000 + i))
        accounts.append(account)
        row['ids'].update(client_id=f'client-{i:03}', account_ids=[account])
        row['permitted_scope']['scope_ids'] = [account]
        row['display_name'] = f'Investor {i % 17:02}'
        row['masked_discriminator'] = f'****{i:04}'
        rows.append(row)
    directory['entries'] = list(reversed(rows))
    owner['advisors']['advisor']['accounts'] = accounts
    seen, cursor, pages = [], None, 0
    while True:
        answer = entry.ENTRY.handle(browse(cursor, limit='25'))
        validator('responses/directory-browse.response.schema.json').validate(answer)
        batch = answer['data']['entries']
        assert 0 < len(batch) <= 25
        seen.extend(a for row in batch for a in row['ids']['account_ids'])
        cursor = answer['data']['next_cursor']
        pages += 1
        if cursor is None: break
        assert pages < 12
    assert pages == 10 and len(seen) == len(set(seen)) == 237
    assert set(seen) == set(accounts)
    expected = [row['ids']['account_ids'][0] for row in sorted(rows, key=lambda r: (r['display_name'].lower(), r['masked_discriminator']))]
    assert seen == expected


@pytest.mark.parametrize('kind', ['unknown-advisor', 'missing-origin', 'client-forged-scope', 'foreign-row', 'partial-group'])
def test_no_request_or_partial_row_expands_access(monkeypatch, kind):
    directory, owner, revision, a, b = setup(monkeypatch)
    event = browse(limit='100')
    owner['advisors']['advisor']['accounts'] = [a]
    if kind == 'unknown-advisor': event['headers']['x-advisor-id'] = 'unknown'
    if kind == 'missing-origin': event['headers'].pop('x-origin-verify')
    if kind == 'client-forged-scope':
        event['resolved_scope'] = {'principal_class': 'OPAL_GLOBAL', 'permitted_account_set': [a, b]}
        event['queryStringParameters']['account_ids'] = json.dumps([a, b])
    if kind == 'foreign-row': directory['entries'][0]['ids']['firm_id'] = 'foreign'
    if kind == 'partial-group': directory['entries'][0]['ids']['account_ids'] = [a, b]
    answer = entry.ENTRY.handle(event)
    if kind in ['unknown-advisor', 'missing-origin']:
        refused(answer)
    elif kind == 'client-forged-scope':
        assert [r['ids']['account_ids'] for r in answer['data']['entries']] == [[a]]
    elif 'data' in answer:
        assert answer['data']['entries'] == []
    else:
        refused(answer)

```
