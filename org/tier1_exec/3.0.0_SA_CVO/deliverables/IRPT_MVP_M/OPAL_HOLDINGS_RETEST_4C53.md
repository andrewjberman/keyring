# M-OPAL-01: bounded independent source closure

Reviewer: `3.0.0_SA_CVO~M`, 2026-09-23. Authority: completion `CONTRACT.md`, narrow live-scope reviewer resume, CTO exact `140536Z` unchanged-retest instruction and COO P exact `141013Z` committed replacement handoff.

**M-OPAL-01 CLOSED at source, bounded to request-local eligibility continuity through the actual holdings pre/post rechecks.** Independently tested exact backend `4c53e0ebcf4d224fc68fe04a2766fe04ae9d685b` in the clean detached reviewer worktree `C:/Users/AndrewBerman/Desktop/ajb_irpt_cvo_m_review`. No producer files were edited. This is not integrated release, package, live data, economic reconciliation of production bytes or custody owner/profile acceptance.

## Original failure and unchanged replay

Original independent evidence `f6dd91f5d7`, [OPAL_SCOPE_REVIEW_DC51.md](OPAL_SCOPE_REVIEW_DC51.md), records 71 PASS / 2 FAIL at `dc51d8920dd25d4c11bf48737cdca31ada3e8a63`. Non-admin home-Opal and partner Dev principals created an accepted selection but holdings reconstructed its inner enforcer with the empty module roster, refusing before the economic loader. Partner advisor and Opal admin controls reached it.

The original 366-line driver remained byte-identical, including ROOT, with SHA256 `c782cfd9c4ddabb1fba407c400ce9166a7f7ba6568f44ad4be66dec83040d642`. Independent replay at the correction: **73 PASS in 1.49 seconds**. No assertion or expected outcome changed. Original failing receipts remain preserved.

```powershell
$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD='1'
$env:PYTHONDONTWRITEBYTECODE='1'
python -m pytest -q -p no:cacheprovider '.runtime/codex-seats/3.0.0_SA_CVO~M/test_opal_dc51_review.py' --junitxml='.runtime/codex-seats/3.0.0_SA_CVO~M/opal_4c53_review.xml'
```

Receipt SHA256: `e81bfce7b8b662c3615fce19baf538e81e2e0e69d4bc96bd21495a72832f06b9`.

The unchanged downstream positive controls deliberately raise `SnapshotUnavailable` in the loader and expect `NOT_READY`. They establish exact tenant/account reachability after actual authorization, not successful economic reads or the post-read recheck. Foreign-reference, stale-directory and revoked-account controls remain refusal before any snapshot read. Global, identity, selector, cursor and same-warm-process directory controls all remain passing.

## Actual source correction and supplemental post-read controls

Across the candidate application/contract trees, the baseline-to-correction diff changes only `infra/aws/lambda/investor-reporting/holdings/entry.py`: `_current_selection` receives an explicit eligible-subject roster and both callers pass `ctx.opal_principal_ids`. Fresh directory/ownership/policy loads, selection validation and before/after equality checks remain intact; no module roster mutation was introduced. The commit also updates the producer handoff document.

Corrected holdings Entry committed-byte SHA256: `ddd1b72ac9ea9f630fc1147a2b418c50204f2058c3f91d672310593d62cb0fc2`.

An additional independent driver (embedded below) exercises actual Entry, selection, loaders, enforcer, projection, reconciliation and clock checks. Only external storage/selection persistence and snapshot loading use controlled synthetic data; network is denied by the reused original fixture. The wrapper around `_current_selection` records calls and invokes the real function without replacing its result.

**13 PASS in 0.43 seconds**:

- Four identity positives: non-admin home-Opal, partner Dev, partner advisor and Opal admin. Each reaches both real authorization checks and returns the exact selected single-account synthetic projection. Both calls receive the expected request-local roster; the module rosters stay empty.
- Eight post-read negatives: the four identities crossed with directory revision change and retained selection membership tampering during snapshot loading. Each reaches the post-read recheck and refuses `OBJECT_NOT_COVERED`, with no protected response data.
- One partner-advisor grant revocation during snapshot loading refuses at the post-read boundary.
- Within the two non-admin internal positives, reuse the same warm holdings Entry and same subject after removing internal claims. The formerly permitted extra account refuses before another snapshot read.

```powershell
$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD='1'
$env:PYTHONDONTWRITEBYTECODE='1'
python -m pytest -q -p no:cacheprovider '.runtime/codex-seats/3.0.0_SA_CVO~M/test_opal_4c53_postread.py' --junitxml='.runtime/codex-seats/3.0.0_SA_CVO~M/opal_4c53_postread.xml'
```

Supplemental driver SHA256: `f15268e84399bbeaea9e4b67564d7acd56d2e054ba3f663375406e807505c07c`.
Supplemental receipt SHA256: `61d8c2be8b616eb798e0e803f5b9875c8fecc50ecd27dd949cac34bed063be66`.

Synthetic snapshot nodes are deliberately minimal serving-boundary fixtures, not a production publication or schema-certified economic dataset. No canonical publication fetch, live S3 proof, package import, Lambda-role read, vendor execution or authenticated browser trace is claimed. Current JWT lifetime still bounds identity freshness; a changed verified request is not proof of immediate revocation inside that lifetime.

## Remaining boundaries

The custody owner/profile extension is explicitly excluded from P's correction handoff and remains NOT EVALUATED. Its actor/home/maintained-organization and source-provenance controls stay pending at [OPAL_PARTNER_SCOPE_REVIEW_PLAN_20260923.md](OPAL_PARTNER_SCOPE_REVIEW_PLAN_20260923.md), evidence `55d7c7724c`. This finding's closure supplies no fabricated Opal organization, advisor identity or prospect privilege.

COO M's data audit `9cc02ebff7` remains attributed evidence: dated directories, absent Inflection ownership, empty Cottonwood ownership and failing 49F projection calls are not repaired by this roster continuity change. Browser, paired schema, generation, retained consumers, package/deployment and live acceptance keep their separate gates. No cloud mutation, producer invocation, IAM change, vendor call or deployment occurred in this review.

## Supplemental driver

```python
"""Independent supplemental actual holdings pre/post controls; no economic proof."""
import copy
import json
import pytest
from test_opal_dc51_review import world, event, entry, holdings_module, SELECT, refuse


@pytest.mark.parametrize('principal', ['opal-user', 'partner-dev', 'partner-advisor', 'opal-admin'])
@pytest.mark.parametrize('change', ['none', 'directory-change', 'selection-change'])
def test_actual_projection_then_fresh_postcheck(world, monkeypatch, principal, change):
    target = '49financial'
    member = world['accounts'][target][0 if principal == 'partner-advisor' else 2]
    create = event(target, route=SELECT)
    if principal == 'partner-dev':
        create['headers'].update({'x-firm-id': target, 'x-user-role': 'advisor', 'x-user-type': 'Dev'})
    if principal == 'partner-advisor':
        create['headers'].update({'x-firm-id': target, 'x-user-role': 'advisor'})
    if principal == 'opal-admin':
        create['headers']['x-user-role'] = 'admin'
    create['queryStringParameters'] = {'selected_tenant': target}
    create['body'] = json.dumps({'scope_kind': 'ACCOUNT', 'scope_ids': [member]})
    selected = entry.ENTRY.handle(create)['data']
    reference = selected['account_set_id']
    holdings = holdings_module()
    checks, reads = [], []
    original = holdings._current_selection

    def checked(request, tenant, selection_id, opal_principal_ids=frozenset()):
        checks.append((tenant, selection_id, opal_principal_ids))
        return original(request, tenant, selection_id, opal_principal_ids)

    def snapshot(tenant, prefix, as_of, *, account_ids):
        reads.append((tenant, account_ids))
        clocks = {'custody_as_of': '2026-09-17', 'overlay_as_of': '2026-09-16'}
        doc = {
            'scope': {'firm_id': target}, 'clocks': clocks,
            'nodes': [{'node_id': member, 'node_kind': 'ACCOUNT', 'parent_node_id': None,
                       'amount': {'value': 100.0, 'currency': 'USD'}, 'clocks': clocks}],
            'attribution_holdouts': {'reconcile': {'reconciled': True}},
        }
        if change == 'directory-change':
            world['docs'][target]['entries'][0]['display_name'] = 'Changed during read'
        elif change == 'selection-change':
            world['records'][(target, reference)]['account_ids'] = world['accounts'][target][:2]
        return doc

    monkeypatch.setattr(holdings, '_current_selection', checked)
    monkeypatch.setattr(holdings._snapshot, 'load_snapshot', snapshot)
    ev = event(target)
    ev.pop('body')
    ev.update(routeKey=holdings.ROUTE_KEY, pathParameters={'accountSetId': reference},
              queryStringParameters={'selected_tenant': target}, headers=copy.deepcopy(create['headers']))
    answer = holdings.ENTRY.handle(ev)
    assert reads == [(target, [member])]
    expected_roster = frozenset() if principal == 'partner-advisor' else frozenset([create['headers']['x-user-email']])
    assert checks == [(target, reference, expected_roster)] * 2
    assert holdings.ENTRY.opal_principal_ids == frozenset()
    assert entry.ENTRY.opal_principal_ids == frozenset()
    if change == 'none':
        assert answer.get('ok') is not False, answer
        assert answer['data']['scope']['account_ids'] == [member]
        assert answer['data']['custody_totals']['total_market_value']['value'] == 100.0
        # Reuse the same warm Entry as the same subject after loss of internal claims.
        if principal in ('opal-user', 'partner-dev'):
            ev['headers'].update({'x-firm-id': target, 'x-user-role': 'advisor'})
            ev['headers'].pop('x-user-type', None)
            reads.clear()
            refuse(holdings.ENTRY.handle(ev))
            assert reads == []
    else:
        refuse(answer)
        assert answer['status']['public_reason_code'] == 'OBJECT_NOT_COVERED'


def test_partner_revocation_during_snapshot_read(world, monkeypatch):
    # Same actual operation/projection with the grant revoked during the storage read.
    target = '49financial'
    member = world['accounts'][target][0]
    create = event(target, home=target, role='advisor', route=SELECT)
    create['queryStringParameters'] = {'selected_tenant': target}
    create['body'] = json.dumps({'scope_kind': 'ACCOUNT', 'scope_ids': [member]})
    reference = entry.ENTRY.handle(create)['data']['account_set_id']
    holdings = holdings_module()
    reads = []
    def snapshot(tenant, prefix, as_of, *, account_ids):
        reads.append((tenant, account_ids))
        world['owners'][target]['advisors']['alice']['accounts'] = []
        clocks = {'custody_as_of': '2026-09-17', 'overlay_as_of': '2026-09-16'}
        return {'scope': {'firm_id': target}, 'clocks': clocks,
                'nodes': [{'node_id': member, 'node_kind': 'ACCOUNT', 'parent_node_id': None,
                           'amount': {'value': 100.0}, 'clocks': clocks}],
                'attribution_holdouts': {'reconcile': {'reconciled': True}}}
    monkeypatch.setattr(holdings._snapshot, 'load_snapshot', snapshot)
    ev = event(target, home=target, role='advisor')
    ev.pop('body')
    ev.update(routeKey=holdings.ROUTE_KEY, pathParameters={'accountSetId': reference},
              queryStringParameters={'selected_tenant': target})
    answer = holdings.ENTRY.handle(ev)
    assert reads == [(target, [member])]
    refuse(answer)
    assert answer['status']['public_reason_code'] == 'OBJECT_NOT_COVERED'

```
